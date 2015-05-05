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
from Config import Config

class ConfigTestSuite(unittest.TestSuite):
###############################################################################
# Not Started. Will not be started.
###############################################################################
    class CfgMthdParseTestSuite(unittest.TestSuite):
        def suite(self):
            pass
###############################################################################
# Unfinished. Will not be finished.
###############################################################################
    class CfgMthdParseFileTestSuite(unittest.TestSuite):
        class MthdParseFileNoFileExistsRaisesExceptionTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                with self.assertRaises(Exception):
                    c.ParseFile("I_DO_NOT_EXIST_HAHAHA.txt")

        def suite(self):
            cases = self.__class__()
            cases.addTest(cases.MthdParseFileNoFileExistsRaisesExceptionTestCase())
            return cases
###############################################################################
# Finished
###############################################################################
    class CfgMthdHasParmTestSuite(unittest.TestSuite):
        class MthdHasParmWithSomethingReturnsTrueTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                c.Set("Value", "X")
                self.assertTrue(c.HasParm("Value"))

        class MthdHasParmWithNothingReturnsFalseTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                self.assertFalse(c.HasParm("NoExist"))

        def suite(self):
            cases = self.__class__()
            cases.addTest(cases.MthdHasParmWithSomethingReturnsTrueTestCase())
            cases.addTest(cases.MthdHasParmWithSomethingReturnsTrueTestCase())
            return cases
###############################################################################
# Finished
###############################################################################
    class CfgMthdGetTestSuite(unittest.TestSuite):
        class MthdGetReturnsValIfExistsTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                c.Set("Value", "roflcopter")
                self.assertEqual(c.Get("Value"), "roflcopter")
        class MthdGetReturnsNoneIfNotExistsTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                self.assertEqual(c.Get("NotExistsss"), None)
        class MthdGetReturnsValRegardlessOfCaseTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                c.Set("RaNDom", "trollol")
                self.assertEqual(c.Get("RANDOM"), "trollol")
        def suite(self):
            cases = self.__class__()
            cases.addTest(cases.MthdGetReturnsValIfExistsTestCase())
            cases.addTest(cases.MthdGetReturnsNoneIfNotExistsTestCase())
            cases.addTest(cases.MthdGetReturnsValRegardlessOfCaseTestCase())
            return cases
###############################################################################
# Finished
###############################################################################
    class CfgMthdGetAsNumTestSuite(unittest.TestSuite):
        class MthdGetAsNumWithDecimalValReturnsFloatTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                c.Set("Value", 1.0002)
                self.assertEqual(c.GetAsNum("Value"), 1.0002)

        class MthdGetAsNumWithIntegerValReturnsIntegerTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                c.Set("Value", 33)
                self.assertEqual(c.GetAsNum("Value"), 33)

        class SprMthdGetAsNumWithBadValRaisesExceptionTestCase(unittest.TestCase):
            badVal = None
            def setUp(self, bv):
                badVal = bv
            def runTest(self):
                c = Config()
                c.Set("Value", self.badVal)
                with self.assertRaises(Exception):
                    c.GetAsNum("Value")
                
        class MthdGetAsNumWithStrValRaisesExceptionTestCase(SprMthdGetAsNumWithBadValRaisesExceptionTestCase):
            def setUp(self):
                super(self.__class__, self).setUp("Print")

        class MthdGetAsNumWithNoneValRaisesExceptionTestCase(SprMthdGetAsNumWithBadValRaisesExceptionTestCase):
            def setUp(self):
                super(self.__class__, self).setUp(None)
                
        def suite(self):
            cases = self.__class__()
            cases.addTest(cases.MthdGetAsNumWithStrValRaisesExceptionTestCase())
            cases.addTest(cases.MthdGetAsNumWithNoneValRaisesExceptionTestCase())
            cases.addTest(cases.MthdGetAsNumWithDecimalValReturnsFloatTestCase())
            cases.addTest(cases.MthdGetAsNumWithIntegerValReturnsIntegerTestCase())
            return cases
###############################################################################
# Finished
###############################################################################
    class CfgMthdGetAsBoolTestSuite(unittest.TestSuite):
        class MthdGetAsBoolWithTrueReturnsTrueBoolean(unittest.TestCase):
            def runTest(self):
                c = Config()
                c.Set("Boolean1", "True")
                c.Set("Boolean2", "true")
                c.Set("Boolean3", 'TRUE')
                c.Set("Boolean4", "TrUe")

                truth = (c.GetAsBool("Boolean1") and
                         c.GetAsBool("Boolean2") and
                         c.GetAsBool("Boolean3") and
                         c.GetAsBool("Boolean4"))

                self.assertTrue(truth)
        class MthdGetAsBoolWithOtherReturnsFalseBoolean(unittest.TestCase):
            def runTest(self):
                c = Config()
                c.Set("Boolean", "False")
                self.assertFalse(c.GetAsBool("Boolean"))

        def suite(self):
            cases = self.__class__()
            cases.addTest(cases.MthdGetAsBoolWithTrueReturnsTrueBoolean())
            cases.addTest(cases.MthdGetAsBoolWithOtherReturnsFalseBoolean())
            return cases
###############################################################################
# Finished??? I don't know
###############################################################################
    class CfgMthdSetTestSuite(unittest.TestSuite):
        class MthdSetWithNoneGivesNullQuotesTestCase(unittest.TestCase):
            def runTest(self):
                c = Config()
                c.Set("Nil", None)
                self.assertEqual(c.Get("Nil"), '')

        def suite(self):
            cases = self.__class__()
            cases.addTest(cases.MthdSetWithNoneGivesNullQuotesTestCase())
            return cases
            
###############################################################################
# Not Started. Will not be started.
###############################################################################
    class CfgMthdPrintConfigTestSuite(unittest.TestSuite):
        def suite(self):
            pass
###############################################################################
# Suite setup
###############################################################################
    def suite(self):
        return unittest.TestSuite([self.CfgMthdGetAsNumTestSuite().suite(),
                                   self.CfgMthdGetAsBoolTestSuite().suite(),
                                   self.CfgMthdHasParmTestSuite().suite(),
                                   self.CfgMthdParseFileTestSuite().suite(),
                                   self.CfgMthdGetTestSuite().suite(),
                                   self.CfgMthdSetTestSuite().suite()])