import sys
import Config
import os
import shutil
import time
import re
import zipfile

# Git API imports
import git.cmd
import git.remote
import git
from git.exc import GitCommandError

# DoSOCS import
import DoSPDX

fileConfig = Config.Config()
fileConfig.ParseFile( 'config.txt' )

def DelDir( s ):
    if os.path.isdir( s ):
        if not os.name == 'nt': # Not a windows pc
            shutil.rmtree( s )
        else:
            os.system( 'rmdir /S /Q "' + s  + '"' ) # Windows has permission problems doing it the normal way

def MakeDirTree( s ):
    dirTree = s
    if os.path.sep in dirTree:
        dirTree = dirTree[ : dirTree.rfind( os.path.sep ) ]
    os.makedirs( dirTree )

def DoPrint( line, bVerbose ):
    if bVerbose:
        print( line )
    
def Main( config = fileConfig ):

    config.PrintConfig()

    bVerbose                = config.GetAsBool("Verbose")
    vBranch                 = config.Get("Branch")
    vTmpDir                 = config.Get("TmpDir")
    vTmpZip_Relative        = config.Get("TmpZip")
    vTmpZip_Absolute        = os.path.join( vTmpDir, vTmpZip_Relative )
    vSPDXFileName_Relative  = config.Get("SPDXOutput")
    vSPDXFileName_Absolute  = os.path.join( vTmpDir, vSPDXFileName_Relative )
    vCommitComment          = config.Get("CommitComment")
    vUser                   = config.Get("User")
    vPassword               = config.Get("Password")

    vCurrentOp              = ""

    vDoSOCSSettingsPath     = os.path.join(".")
    vDoSOCSSettingsFile     = os.path.join(vDoSOCSSettingsPath,"settings.py")
    vDoSOCSSettingsFile_TMP = os.path.join(vDoSOCSSettingsPath,"_settings.py")

    vDoSOCSParms            = config.GetDoSOCSParms()

    bMovedSettingsFile      = False

    try:

        # Add the desired parameters to the DoSOCS settings file
        vCurrentOp      = "Backing up DoSOCS settings file"
        DoPrint( vCurrentOp, bVerbose )
        if os.path.isfile( vDoSOCSSettingsFile_TMP ):
            os.remove( vDoSOCSSettingsFile_TMP )
        shutil.copyfile( vDoSOCSSettingsFile, vDoSOCSSettingsFile_TMP )
        bMovedSettingsFile = True

        vCurrentOp      = "Adding parameters to DoSOCS settings file"
        DoPrint( vCurrentOp, bVerbose )
        file = open( vDoSOCSSettingsFile, 'a' )
        for parm in vDoSOCSParms.keys():
            file.write( "\n%s = '%s'" % (parm,vDoSOCSParms[parm]) )
        file.close()

        # Set up temporary directory
        vCurrentOp = "Deleting old temporary directory if present"
        DoPrint( vCurrentOp, bVerbose )
        DelDir( vTmpDir )
        
        # Sleep to make sure the directory is fully deleted before writing it
        time.sleep(1)
        
        vCurrentOp      = "Making temporary directory"
        DoPrint( vCurrentOp, bVerbose )
        MakeDirTree( vSPDXFileName_Absolute )
        
        # Connect to Git
        vCurrentOp      = "Connecting to Git"
        DoPrint( vCurrentOp, bVerbose )
        vGitNtfc        = git.cmd.Git( vTmpDir )

        # Initiate a temporary repository
        vCurrentOp      = "Initiating temporary Git branch"
        DoPrint( vCurrentOp, bVerbose )
        vGitNtfc.init()

        # Pull the files down
        vCurrentOp      = "Pulling Git branch located at " + vBranch
        DoPrint( vCurrentOp, bVerbose )
        vGitNtfc.pull( vBranch )

        # Get all the file names
        vCurrentOp      = "Retrieving list of files from Git branch"
        DoPrint( vCurrentOp, bVerbose )
        vFileList       = vGitNtfc.ls_files().split("\n")

        # Create zip file
        vCurrentOp      = "Creating package file"
        DoPrint( vCurrentOp, bVerbose )
        vZipFile        = zipfile.ZipFile( vTmpZip_Absolute , 'w' )

        # Add files to package
        vCurrentOp      = "Processing files"
        DoPrint( vCurrentOp, bVerbose )
        if vSPDXFileName_Relative in vFileList: # Don't process the SPDX file
            vFileList.remove( vSPDXFileName_Relative )
        for vFile in vFileList:
            vZipFile.write( os.path.join( vTmpDir, vFile ), vFile )

        # Write SPDX tail
        vZipFile.close()

        vCurrentOp	= "Calling DoSPDX"
        DoPrint( vCurrentOp, bVerbose )
        DoSPDX.main([ '-p', vTmpZip_Absolute
                    , '--print', 'JSON'
                    , '--scan'
                    , '--scanOption', 'Fossology'
                    ]) 

        # Remove the zip file
        vCurrentOp      = "Removing package file"
        DoPrint( vCurrentOp, bVerbose )
        os.remove( vTmpZip_Absolute )
        
        # Push SPDX to repository
        vCurrentOp      = "Adding SPDX file to local branch"
        DoPrint( vCurrentOp, bVerbose )
        vGitNtfc.add( vSPDXFileName_Relative )

        vRepo = git.Repo( vTmpDir )
        if vRepo.is_dirty():
            vCurrentOp      = "Committing SPDX changes"
            DoPrint( vCurrentOp, bVerbose )
            vGitNtfc.commit( message=time.strftime( vCommitComment ) )
        
            vAuthString = ""
            if vUser:
                vAuthString = "@"
                if vPassword:
                    vAuthString = ':' + vPassword + vAuthString
                vAuthString = vUser + vAuthString
            
            vPushTarg   = vBranch
            vCxnInfo    = re.findall( r"^(https?://)?(.*)", vPushTarg )
            if vCxnInfo:
                vProtocol, vURL = vCxnInfo[0]
                vPushTarg = vProtocol + vAuthString + vURL

            vCurrentOp      = "Connecting to remote repository"
            DoPrint( vCurrentOp, bVerbose )
            vRemote = git.remote.Remote( vRepo, vPushTarg )

            vCurrentOp      = "Pushing SPDX file to remote repository"
            DoPrint( vCurrentOp, bVerbose )
            vRemote.push()
        else:
            DoPrint( "SPDX Document is already up to date", bVerbose )
        
        # Delete local directory
        vCurrentOp          = "Deleting temporary directory"
        DoPrint( vCurrentOp, bVerbose )
        DelDir( vTmpDir )

    except GitCommandError as exc:
        print( '*'*30 )
        print( 'Error during "%s". Here\'s what was given to stderr:' % vCurrentOp )
        print( exc.stderr.decode('ascii') )
        print( '*'*30 )
    except Exception as exc:
        print( '*'*30 )
        print( 'Error during "%s". Here\'s the exception that was raised:' % vCurrentOp )
        raise exc
    finally:
        # Restore the DoSOCS settings file
        if bMovedSettingsFile:
            try:
                vCurrentOp      = "Replacing original DoSOCS settings file"
                DoPrint( vCurrentOp, bVerbose )
                #shutil.copyfile( vDoSOCSSettingsFile_TMP, vDoSOCSSettingsFile )
            except:
                pass

if __name__ == '__main__':
    args = sys.argv[1:]
    argc = len(args)

    commandLineConfig = fileConfig
    commandLineConfig.Parse( args )
    Main( commandLineConfig )
