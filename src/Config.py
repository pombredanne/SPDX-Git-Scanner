import os

class Config:
    def __init__( self ):
        self._params = {}

        self.Set( 'TmpDir'                  , os.path.join('.','TMP')           )
        self.Set( 'TmpZip'                  , 'SPDXPackagedFiles.zip'           )
        self.Set( 'Verbose'                 , True                              )
        self.Set( 'SPDXOutput'              , 'SPDXFile.txt'                    )
        self.Set( 'CommitComment'           , 'SPDX Generation %Y%m%d%H%M%S'    )
        self.Set( 'User'                    , None                              )
        self.Set( 'Password'                , None                              )
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
        prefix = "dosocs."
        params = {}
        for param in self._params.keys():
            if param.startswith( prefix ):
                ds_param = param.replace(prefix,'',1)
                params[ ds_param ] = self._params[ param ]
        return params
                

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
        
    def Set( self, param, value ):
        param = param.strip().lower()

        if not len(param):
            return

        if value == None:
            value = ''
        elif not type(value) == str:
            value = repr(value)
            
        value = value.strip()
        self._params[ param ] = value

    def PrintConfig( self ):
        longest = 0
        for key in self._params.keys():
            if len(key) > longest:
                longest = len(key)
        fmt = "%-" + repr(longest) + "s = %s"
        for key in self._params.keys():
            print( fmt % (key, self._params[key]) )

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
