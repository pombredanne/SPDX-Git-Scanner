import DoSPDX

argHash = { 'scanOption': 'fa', 
            'packagePath': '/home/zach/Downloads/fossology-spdx-master.zip',
            'scan': True,
            'documentComment': 'fs'}

DoSPDX.dospdx(argHash)
