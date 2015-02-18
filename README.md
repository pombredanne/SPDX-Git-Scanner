# SPDX-Git-Scanner
The SPDX-Git-Scanner is aimed at processing branches from Git into SPDX documents. The utility will retrieve, scan, and return a single SPDX document back into the branch. Scanning is completed through the doSOCS module and files are cached in a MySQL databsae.

#Prerequisites
* Python 2.7
* MySQL
* Python-MySQLDB
* FOSSology
* PHP
* Git
* Python-Git

#Installation
1. Download SPDX-Git-Scanner master and unzip
2. Install any required prerequisites
3. Run ./install.sh
4. Configure Git config in /src/config.txt
5. Configure doSOCS config in /doSOCS/src/settings.py

#Usage
TODO

#License
Source Code: Apache 2.0

Documentation: Creative Commons 4.0

#Copyright
Copyright © 2015 Daniel Patten, Zachary Meyer, and Jacob Vosik

#Code Contributions
All contributions to SPDX-Git-Scanner will be subject to review by the owner(s) of the repo before being merged
