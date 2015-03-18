import unittest

class ConfigTestSuite(unitTest.TestSuite):
	class CfgMthdParseTestSuite(unittest.TestSuite):
	class CfgMthdParseFileTestSuite(unittest.TestSuite):
	class CfgMthdHasParmTestSuite(unittest.TestSuite):
	class CfgMthdGetTestSuite(unittest.TestSuite):
	class CfgMthdGetAsNumTestSuite(unittest.TestSuite):
		class MthdGetAsNumWithStringValRaisesExceptionTestCase(unittest.TestCase):
		class MthdGetAsNumWithDecimalValReturnsFloatTestCase(unittest.TestCase):
		class MthdGetAsNumWithIntegerValReturnsIntegerTestCase(unittest.TestCase):
	class CfgMthdGetAsBoolTestSuite(unittest.TestSuite):
	class CfgMthdSetTestSuite(unittest.TestSuite):
	class CfgMthdPrintConfigTestSuite(unittest.TestSuite):