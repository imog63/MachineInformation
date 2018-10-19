# Copyright (c) 2018 Software AG, Darmstadt, Germany and/or its licensors
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pysys.constants import *
from apama.basetest import ApamaBaseTest
from apama.correlator import CorrelatorHelper
import re
import os

class PySysTest(ApamaBaseTest):
	def execute(self):
		correlator = CorrelatorHelper(self, name='testcorrelator')
		correlator.start(logfile='testcorrelator.log', config=os.path.join(self.input, 'CorrelatorConfig.yaml'))
		correlator.injectEPL(filenames=['test.mon'])
		correlator.flush() 					
		
	def validate(self):
		exprList = []
		exprList.append("Loaded monitor RunPythonPlugin")	
		exprList.append("cpu count is") 
		exprList.append("start time is") 
		exprList.append("disk total is") 
		exprList.append("disk available is") 
		exprList.append("physical memory total is") 
		exprList.append("physical memory available is")
		exprList.append("virtual memory total is") 
		exprList.append("virtual memory available is")
		exprList.append("load average is")
		exprList.append("the time is")
		exprList.append("uptime is")				
		exprList.append("All Done.")
		self.assertOrderedGrep('testcorrelator.log',exprList=exprList)
		self.assertGrep('testcorrelator.log', expr=' (ERROR|FATAL) ', contains=False)		
		
	
			
	
