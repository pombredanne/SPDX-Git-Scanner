###############################################################################
# Copyright 2015 Jacob Vosik, Dan Patten, Zach Meyer
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# SPDXLicenseID: Apache-2.0

import os

class Config:
    def __init__( self ):
        self._params = {}
        self._dosocs_params = {}

        # Default values for variables
        self.Set( 'TmpDir'                  , os.path.join('.','TMP')           )
        self.Set( 'TmpZip'                  , 'SPDXPackagedFiles.zip'           )
        self.Set( 'Verbose'                 , True                              )
        self.Set( 'SPDXOutputBase'          , 'SPDXFile'                        )
        self.Set( 'CommitComment'           , 'SPDX Generation %Y%m%d%H%M%S'    )
        self.Set( 'AutoCommit'              , True                              )
        self.Set( 'User'                    , None                              )
        self.Set( 'Password'                , None                              )
        self.Set( 'PrintType'               , 'JSON'                            )
        self.Set( 'Branch'                  , None                              )
        self.Set( 'DoSOCS.database_user'    , None                              )
        self.Set( 'DoSOCS.database_pass'    , None                              )
        self.Set( 'DoSOCS.database_host'    , None                              )
        self.Set( 'DoSOCS.database_port'    , None                              )
        self.Set( 'DoSOCS.database_name'    , None                              )

    # Processes a list of params and sets the value in the config
    def Parse( self, paramList ):
        for param in paramList:
            
            # If '=' isn't in the param, it is a basic flag. Nothing currently uses this, but the support is here
            if not '=' in param:
                name, value = param,""              # Just add the name with no value
            else:
                name, value = param.split('=',1)    #  Split on the first '='
            self.Set( name, value )

    # Parses an entire file for parameters
    def ParseFile( self, fileName ):
        try:
            file = open( fileName, 'r' )
            lines = file.readlines()
            file.close()

            # Check all the lines. We'll only process lines that aren't comment-lines
            vParseLines = []
            for line in lines:
                if not line.strip().startswith('//'):
                    vParseLines.append( line )

            self.Parse( vParseLines )
        except:
            raise Exception( "File " + fileName + " does not exist\n" )

    # Basic check for the existence of a param
    def HasParm( self, param ):
        return self.Get( param ) != None

    # Gets the value of a parameter. If it doesn't exist, returns None
    def Get( self, param ):
        param = param.lower()
        if param in self._params.keys():
            return self._params[ param ]
        return None

    # Gets parameters that are specifically meant to pass into DoSOCS' config
    def GetDoSOCSParms( self ):
        return self._dosocs_params

    # Gets a parameter as a number if possible, otherwise throw an exception
    def GetAsNum( self, param ):
        value = self.Get(param)
        try:
            if '.' in value:            # If it has a period, assume it's a decimal
                return float(value)
            else:                       # Otherwise, assume it's an integer (or long)
                return int(value) 
        except:
            raise Exception( "Expected value to be a number, but there was an error converting it: [" + value + "]" )

    # Gets a parameter as a bool (true if parameter is case-insensitive "true", false otherwise)
    def GetAsBool( self, param ):
        value = self.Get(param)
        return value != None and value.lower() == 'true'

    # Sets a DoSOCS parameter. The names here ARE case sensitive, since that's what DoSOCS requires
    def SetDoSOCS( self, param, value ):
        if not len(param):
            return
        self._dosocs_params[param] = value
        
    # Sets any parameter. If it's determined to be a DoSOCS parameter, call out to the correct method
    def Set( self, param, value ):
        
        # Get rid of beginning/ending spaces
        param = param.strip()
        
        # If it's empty, we don't want to set anything
        if not len(param):
            return

        # Swap 'None' to be an empty string (only happens with default parameters)
        if value == None:
            value = ''
        # For non-strings, convert it to string
        elif not type(value) == str:
            value = repr(value)
        
        # Get rid of beginning/ending spaces
        value = value.strip()

        # Check if this is a DoSOCS parameter
        l_param = param.lower()
        if l_param.startswith("dosocs."):
            self.SetDoSOCS( param[7:], value ) # If it is, drop the 'dosocs.' call out to the right function
            return                             #  and we're done
        
        # Use the lower-case name so our dictionary is case-insensitive
        param = l_param

        # Add the value to the dictionary
        self._params[ param ] = value

    # Print the entire config. Also returns it as a string for testing purposes.
    def PrintConfig( self ):
        longest = 0
        asString = ""
        for key in self._params.keys():
            if len(key) > longest:
                longest = len(key)
        for key in self._dosocs_params.keys():
            if len(key) > longest:
                longest = len(key)
        fmt = "%-" + repr(longest) + "s = %s"
        for key in self._params.keys():
            cur = fmt % (key, self._params[key])
            asString +=  cur + "\n"
            print( cur )
        for key in self._dosocs_params.keys():
            cur = fmt % (key, self._dosocs_params[key])
            asString +=  cur + "\n"
            print( cur )
        return asString

# Tests some of the configuration functions
def __TestConfig():
    c = Config()
    firstList = """
    Hello=blah
    NoVal=
    BAD_LINE
    one=1
    two = 2
    =
    flag
    """.split("\n")

    secondList = """
    Hello=World
    """.split("\n")

    c.Parse( firstList )
    c.PrintConfig()
    c.Parse( secondList )
    c.PrintConfig()

    c.Set( 'two', 2.0 )
    print( c.Get( 'two' ) )

    print( c.GetAsNum('onE') )
    try:
        c.GetAsNum('Hello')
    except Exception as e:
        print( e )

# If the config is run as the main script, run the test
if __name__ == '__main__':
    __TestConfig()
