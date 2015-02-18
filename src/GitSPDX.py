import sys
import Config
import os
import shutil
import time
import re

# Git API imports
import git.cmd
import git.remote
import git
from git.exc import GitCommandError

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

def DBG( line ):
    DoPrint( "*** DBG: " + line, True )
    
def Main( config = fileConfig ):

    config.PrintConfig()

    bVerbose                = config.GetAsBool("Verbose")
    vBranch                 = config.Get("Branch")
    vTmpDir                 = config.Get("TmpDir")
    vSPDXFileName_Relative  = config.Get("SPDXOutput")
    vSPDXFileName_Absolute  = os.path.join( vTmpDir, vSPDXFileName_Relative )
    vCommitComment          = config.Get("CommitComment")
    vUser                   = config.Get("User")
    vPassword               = config.Get("Password")

    vCurrentOp              = ""

    try:
        
        # Set up temporary directory
        vCurrentOp = "Deleting old temporary directory if present"
        DoPrint( vCurrentOp, bVerbose )
        DelDir( vTmpDir )
        
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

        # Write SPDX Header
        bSPDXExisted    = os.path.isfile( vSPDXFileName_Absolute )
        vSPDXFile       = open( vSPDXFileName_Absolute, 'w' )
        vSPDXFile.write( "Hi, I'm the header, generated on %s\n" % time.ctime() )

        vCurrentOp      = "Processing files"
        DoPrint( vCurrentOp, bVerbose )
        for vFile in vFileList:
            vSPDXFile.write( vFile + "\n" )
            # if not dosocs.iscached( vFile ):
            #    Give to dosocs
            # read from dosocs DB
            # write SPDX info

        # Write SPDX tail
        vSPDXFile.write( "And I'm the tail\n" )
        vSPDXFile.close()
        
        # Push SPDX to repository
        vCurrentOp      = "Adding SPDX file to local branch"
        DoPrint( vCurrentOp, bVerbose )
        vGitNtfc.add( vSPDXFileName_Relative )

        vCurrentOp      = "Committing SPDX changes"
        DoPrint( vCurrentOp, bVerbose )
        vGitNtfc.commit( message=time.strftime( vCommitComment ) )

        vRepo = git.Repo( vTmpDir )
        vAuthString = ""
        if vUser:
            vAuthString = vUser + "@"
            if vPassword:
                vAuthString = vPassword + vAuthString
        
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
        
        # Delete local directory
        DelDir( vTmpDir )
    except GitCommandError as exc:
        print( '*'*30 )
        print( 'Error during "%s". Here\'s what was given to stderr:' % vCurrentOp )
        print( exc.stderr.decode('ascii') )
        print( '*'*30 )

if __name__ == '__main__':
    args = sys.argv[1:]
    argc = len(args)

    commandLineConfig = fileConfig
    commandLineConfig.Parse( args )
    Main( commandLineConfig )
