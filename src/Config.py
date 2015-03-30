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

import os

class Config:
    def __init__( self ):
        self._params = {}
        self._dosocs_params = {}

        self.Set( 'TmpDir'                  , os.path.join('.','TMP')           )
        self.Set( 'TmpZip'                  , 'SPDXPackagedFiles.zip'           )
        self.Set( 'Verbose'                 , True                              )
        self.Set( 'SPDXOutputBase'          , 'SPDXFile'                        )
        self.Set( 'CommitComment'           , 'SPDX Generation %Y%m%d%H%M%S'    )
        self.Set( 'User'                    , None                              )
        self.Set( 'Password'                , None                              )
        self.Set( 'PrintType'               , 'JSON'                            )
        self.Set( 'Branch'                  , None                              )
        self.Set( 'DoSOCS.database_user'    , None                              )
        self.Set( 'DoSOCS.database_pass'    , None                              )
        self.Set( 'DoSOCS.database_host'    , None                              )
        self.Set( 'DoSOCS.database_port'    , None                              )
        self.Set( 'DoSOCS.database_name'    , None                              )

    def Parse( self, paramList ):
        for param in paramList:
            if not '=' in param:
                name, value = param,""
            else:
                name, value = param.split('=',1)
            self.Set( name, value )

    def ParseFile( self, fileName ):
        try:
            file = open( fileName, 'r' )
            lines = file.readlines()
            file.close()

            vParseLines = []
            for line in lines:
                if not line.strip().startswith('//'):
                    vParseLines.append( line )

            self.Parse( vParseLines )
        except:
            pass

    def HasParm( self, param ):
        return self.Get( param ) != None

    def Get( self, param ):
        param = param.lower()
        if param in self._params.keys():
            return self._params[ param ]
        return None

    def GetDoSOCSParms( self ):
        return self._dosocs_params

    def GetAsNum( self, param ):
        value = self.Get(param)
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except:
            raise Exception( "Expected value to be a number, but there was an error converting it: [" + value + "]" )

    def GetAsBool( self, param ):
        value = self.Get(param)
        return value != None and value.lower() == 'true'

    def SetDoSOCS( self, param, value ):
        if not len(param):
            return
        self._dosocs_params[param] = value
        
    def Set( self, param, value ):
        
        param = param.strip()
        if not len(param):
            return

        if value == None:
            value = ''
        elif not type(value) == str:
            value = repr(value)
        value = value.strip()

        l_param = param.lower()
        if l_param.startswith("dosocs."):
            self.SetDoSOCS( param[7:], value )
            return
        param = l_param

        self._params[ param ] = value

    def PrintConfig( self ):
        longest = 0
        for key in self._params.keys():
            if len(key) > longest:
                longest = len(key)
        for key in self._dosocs_params.keys():
            if len(key) > longest:
                longest = len(key)
        fmt = "%-" + repr(longest) + "s = %s"
        for key in self._params.keys():
            print( fmt % (key, self._params[key]) )
        for key in self._dosocs_params.keys():
            print( fmt % (key, self._dosocs_params[key]) )

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

if __name__ == '__main__':
    __TestConfig()
