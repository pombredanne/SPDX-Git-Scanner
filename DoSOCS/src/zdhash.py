class ZDHash:
    """ Dictionary wrapper to allow default key values.
    Must extend ZDHash in order to use.

    param: zdict - partial Dictionary
    """
    def __init__(self, zdict):
        self.createDict()
        for key in zdict.keys():
            self.dict[key] = zdict[key]
    def createDict(self):
        self.dict = {}
