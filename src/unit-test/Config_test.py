import unittest

class ConfigTestSuite(unittest.TestSuite):
#	class CfgMthdParseTestSuite(unittest.TestSuite):

#	class CfgMthdParseFileTestSuite(unittest.TestSuite):

#	class CfgMthdHasParmTestSuite(unittest.TestSuite):

#	class CfgMthdGetTestSuite(unittest.TestSuite):

	class CfgMthdGetAsNumTestSuite(unittest.TestSuite):
		# Not to be added
		class SprMthdGetAsNumWithBadValRaisesExceptionTestCase(unittest.TestCase):
			badVal = None
			def setUp(self, bv):
				badVal = bv
				print "Set up Super"
			def runTest(self):
				print "Run Super"
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

			return cases

#		class MthdGetAsNumWithDecimalValReturnsFloatTestCase(unittest.TestCase):

#		class MthdGetAsNumWithIntegerValReturnsIntegerTestCase(unittest.TestCase):
#	class CfgMthdGetAsBoolTestSuite(unittest.TestSuite):

#	class CfgMthdSetTestSuite(unittest.TestSuite):

#	class CfgMthdPrintConfigTestSuite(unittest.TestSuite):
	def suite(self):
		return unittest.TestSuite([self.CfgMthdGetAsNumTestSuite().suite()])