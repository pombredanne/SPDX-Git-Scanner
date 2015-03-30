import sys
import os
if os.name == "nt":
	sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\unit-test")
else:
	sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/unit-test")	

import runTest

# Runs unit tests...