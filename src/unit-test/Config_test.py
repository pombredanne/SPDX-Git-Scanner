import unittest
import sys
sys.path.append("../")
from Config import Config

class ConfigTestSuite(unittest.TestSuite):
#	class CfgMthdParseTestSuite(unittest.TestSuite):

#	class CfgMthdParseFileTestSuite(unittest.TestSuite):

#	class CfgMthdHasParmTestSuite(unittest.TestSuite):

#	class CfgMthdGetTestSuite(unittest.TestSuite):

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

#	class CfgMthdGetAsBoolTestSuite(unittest.TestSuite):

#	class CfgMthdSetTestSuite(unittest.TestSuite):

#	class CfgMthdPrintConfigTestSuite(unittest.TestSuite):
	def suite(self):
		return unittest.TestSuite([self.CfgMthdGetAsNumTestSuite().suite()])