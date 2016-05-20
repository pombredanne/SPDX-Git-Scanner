# SPDX-Git-Scanner
The SPDX-Git-Scanner is aimed at processing branches from Git into SPDX documents. The utility will retrieve, scan, and return a single SPDX document back into the branch. Scanning is completed through the [doSOCS](https://github.com/socs-dev-env/DoSOCS) module and files are cached in a MySQL database through [SOCsDatabase](https://github.com/socs-dev-env/SOCSDatabase).

#Prerequisites
* Python 2.7+
* MySQL
* Python-MySQLDB
* FOSSology
* PHP
* Git
* Python-Git

#Installation
1. Download and run install.sh
2. Configure Git config in SPDX-Git-Scanner/src/config.txt

#Usage
[Usage information for running SPDX Git Scanner](https://github.com/SPDX-Git/SPDX-Git-Scanner/wiki/Running-GitSPDX)

#License
Source Code: Apache 2.0

Documentation: Creative Commons 4.0 - Attribution-ShareAlike 4.0 International.

#Copyright
Copyright © 2015 Daniel Patten, Zachary Meyer, and Jacob Vosik

#Code Contributions
All contributions to SPDX-Git-Scanner will be subject to review by the owner(s) of the repo before being merged
