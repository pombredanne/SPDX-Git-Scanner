#!/usr/bin/python
import DoSPDX
from dospdx_arghash import DospdxArgHash
#argHash = { 'scanOption': 'fa', 
#            'packagePath': '/home/zach/Downloads/fossology-spdx-master.zip',
#            'scan': True,
#            'documentComment': 'fs'}

#DoSPDX.dospdx(argHash)

good_test_dict = {'packagePath': '/'}
bad_test_dict = {'dosga': 'sdgs'}

DospdxArgHash(good_test_dict)
DospdxArgHash(bad_test_dict)

test_arg1 = {'packagePath': '/media/sf_vbox/nu-master.zip'}
DoSPDX.dospdx(test_arg1)
