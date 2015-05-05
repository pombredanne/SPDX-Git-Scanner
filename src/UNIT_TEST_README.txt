===============================================================
Setup:

There is no setup in order to test the config parsing.  However, testing GitSPDX requires some config file changes.  The first config file is the config file in the src/ directory.  Change the branch to a Github branch, your user to your Github username, and the password to your Github password.  Change the DoSOCS and database settings if neccessary.  LEAVE AUTOCOMMIT AS TRUE,and PRINTTYPE AS JSON

For the next config file, unit-test/testconfig.txt, you must change the branch to include the path to SPDX-Git-Scanner.  Any database and DoSOCS settings must also be changed here.  LEAVE AUTOCOMMIT AS FALSE, and PRINTTYPE AS JSON.

TmpDir must not be changed for the first one.
You may change Verbose if you want to.

After the configuration has been set, simply run 'runUnitTest.py' while in the \src directory.