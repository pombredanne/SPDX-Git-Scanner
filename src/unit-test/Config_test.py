import unittest

class ConfigTestSuite(unitTest.TestSuite):
#	class CfgMthdParseTestSuite(unittest.TestSuite):

#	class CfgMthdParseFileTestSuite(unittest.TestSuite):

#	class CfgMthdHasParmTestSuite(unittest.TestSuite):

#	class CfgMthdGetTestSuite(unittest.TestSuite):

	class CfgMthdGetAsNumTestSuite(unittest.TestSuite):
		# Not to be added
		class SprMthdGetAsNumWithBadValRaisesExceptionTestCase(unittest.TestCase):
			badVal = None
			def __init__(self):

		class MthdGetAsNumWithStrValRaisesExceptionTestCase(SprMthdGetAsNumWithBadValRaisesExceptionTestCase):
			def setUp():
			def runTest():

		class MthdGetAsNumWithNoneValRaisesExceptionTestCase(SprMthdGetAsNumWithBadValRaisesExceptionTestCase):
			def __init__(self):
				

		class MthdGetAsNumWithDecimalValReturnsFloatTestCase(unittest.TestCase):

		class MthdGetAsNumWithIntegerValReturnsIntegerTestCase(unittest.TestCase):
#	class CfgMthdGetAsBoolTestSuite(unittest.TestSuite):

#	class CfgMthdSetTestSuite(unittest.TestSuite):

#	class CfgMthdPrintConfigTestSuite(unittest.TestSuite):