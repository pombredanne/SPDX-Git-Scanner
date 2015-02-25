#!/usr/bin/python

#Attempt to print SPDX doc #1 from database
import DoSPDX
from dospdx_arghash import DospdxArgHash
argHash = { 'scan': False,
            'output': 'TAG',
            'spdxDocId': '1'}

DoSPDX.dospdx(argHash)