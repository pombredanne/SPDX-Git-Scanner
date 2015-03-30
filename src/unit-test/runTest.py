import unittest
import Config_test
import GitSPDX_test



suite = unittest.TestSuite([Config_test.ConfigTestSuite().suite()])

unittest.TextTestRunner().run(suite)