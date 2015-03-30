import unittest
import sys
sys.path.append("../")
from Config import Config

class ConfigTestSuite(unittest.TestSuite):
	class CfgMthdParseTestSuite(unittest.TestSuite):
		def suite(self):
			pass

	class CfgMthdParseFileTestSuite(unittest.TestSuite):
		def suite(self):
			pass

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

	class CfgMthdGetTestSuite(unittest.TestSuite):
		def suite(self):
			pass

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
		# Not to be added
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
	class CfgMthdSetTestSuite(unittest.TestSuite):
		def suite(self):
			pass

	class CfgMthdPrintConfigTestSuite(unittest.TestSuite):
		def suite(self):
			pass
			
	def suite(self):
		return unittest.TestSuite([self.CfgMthdGetAsNumTestSuite().suite(),
		                           self.CfgMthdGetAsBoolTestSuite().suite(),
		                           self.CfgMthdHasParmTestSuite().suite()])