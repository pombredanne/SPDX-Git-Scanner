import zdhash

class DospdxArgHash(zdhash.ZDHash):
    def createDict(self):
        self.dict = {'documentComment': "",
                     'packagePath': None,
                     'creator': "",
		             'creatorComment': "",
		             'licenseListVersion': "",
		             'packageVersion': "",
                     'packageSupplier': "",
                     'packageOriginator': "",
                     'packageDownloadLocation': "",
                     'packageHomePage': "",
                     'packageSourceInfo': "",
                     'packageLicenseComments': "",
                     'packageDescription': "",
                     'scanOption': "",
                     'output': "",
                     'scan': False,
                     'spdxDocId': None}
