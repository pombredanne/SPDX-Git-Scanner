class ZDHash:
    """ Dictionary wrapper to allow default key values.
    Must extend ZDHash in order to use.

    param: zdict - partial Dictionary
    """
    def __init__(self, zdict):
        self.createDict()
        for key in zdict.keys():
            if key not in self.dict.keys():
            	print "WARNING: " + key + " is not in the list.  Check your spelling"
            
            self.dict[key] = zdict[key]  
    def createDict(self):
        self.dict = {}
