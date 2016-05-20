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
import Config_test
import GitSPDX_test



suite = unittest.TestSuite([Config_test.ConfigTestSuite().suite(),
                            GitSPDX_test.GitSPDXTestSuite().suite()])

unittest.TextTestRunner().run(suite)