#!/usr/bin/python
###############################################################################
# Copyright 2015 Jacob Vosik, Dan Patten, Zach Meyer
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# SPDXLicenseID: Apache-2.0


import unittest
import sys
sys.path.append("../")
import GitSPDX
import Config
import os

import git.cmd
import git.remote
import git
from git.exc import GitCommandError

class GitSPDXTestSuite(unittest.TestSuite):
###############################################################################
# Not Started. Test not to be done. 
###############################################################################
    class GitMthdDelDirTestSuite(unittest.TestSuite):
        def suite(self):
            pass
    class GitMthdMakeDirTreeTestSuite(unittest.TestSuite):
        def suite(self):
            pass
    class GitMthdDoPrintTestSuite(unittest.TestSuite):
        def suite(self):
            pass

###############################################################################
# Assumptions:
# - You configure everything correctly
# - This shall test the SPDX file has been pushed.
###############################################################################
    class GitSPDXPushIsSuccessfulTestCase(unittest.TestCase):
        def runTest(self):
            # Again, we are assuming the user has configured his or her git
            # branch, and so on.
            fileConfig = Config.Config()
            fileConfig.ParseFile( 'config.txt' )

            os.system("cd ..")
            GitSPDX.Main(fileConfig)


            branch = fileConfig.Get("Branch")

            os.system("cd unit-test")
           # GitSPDXDelDir("TMP")
            os.makedirs("TMP")
            gitd = git.cmd.Git("TMP")
            gitd.init()
            gitd.pull(branch)
            self.assertTrue(os.path.isfile("TMP/SPDXFile.json"))

        def tearDown(self):
            GitSPDX.DelDir("TMP")

###############################################################################
# Suite setup
###############################################################################
    def suite(self):
        #return unittest.TestSuite([self.GitMthdDelDirTestSuite.suite(),
        #                           self.GitMthdMakeDirTreeTestSuite.suite(),
        #                           self.GitMthdDoPrintTestSsuite.suite()])

        cases = self.__class__()
        cases.addTest(cases.GitSPDXPushIsSuccessfulTestCase())
        return cases