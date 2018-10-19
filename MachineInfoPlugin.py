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

import os
import psutil
import time

from apama.eplplugin import EPLAction, EPLPluginBase

class systemPlugin(EPLPluginBase):
    start=0
    def __init__(self,init):
        super(systemPlugin,self).__init__(init)
        self.getLogger().info("Python systemPlugin initialised with config: %s" % self.getConfig())
        systemPlugin.start=time.time()
    @EPLAction("action< > returns float")
    def bytesperMB(self):
        #1024*1024=1048576
        return 1048576.0
    @EPLAction("action< > returns integer")
    def get_start_time(self):
        self.getLogger().info("Executing get_start_time")
        return systemPlugin.start    
    @EPLAction("action<float>")
    def pause(self, seconds):
        self.getLogger().info("Executing pause")
        time.sleep(seconds)
        return    
    @EPLAction("action< > returns integer")
    def cpu_count(self):
        self.getLogger().info("Executing cpu_count")
        retval=os.cpu_count()        
        return retval 
    @EPLAction("action< > returns float")
    def disk_total_mb(self):
        self.getLogger().info("Executing disk_total_mb")
        #  ??? WHICH DISK(S) ???
        retval=psutil.disk_usage('/').total / self.bytesperMB()
        return retval
    @EPLAction("action< > returns float")  
    def disk_available_mb(self):
        self.getLogger().info("Executing disk_available_mb")
        #  ??? WHICH DISK(S) ???
        retval=psutil.disk_usage('/').free / self.bytesperMB()        
        return retval 
    @EPLAction("action< > returns float")
    def physical_memory_total_mb(self):
        self.getLogger().info("Executing physical_memory_total_mb")
        #  Virtual memory retrieves physical memory
        retval=psutil.virtual_memory().total / self.bytesperMB()         
        return retval 
    @EPLAction("action< > returns float")
    def physical_memory_available_mb(self):
        self.getLogger().info("Executing physical_memory_available_mb")
        #  Virtual memory retrieves physical memory
        retval=psutil.virtual_memory().available / self.bytesperMB()           
        return retval  
    @EPLAction("action< > returns float")
    def virtual_memory_total_mb(self):
        self.getLogger().info("Executing virtual_memory_total_mb")
        #  Swap memory returns virtual memory
        retval=psutil.swap_memory().total / self.bytesperMB()       
        return retval 
    @EPLAction("action< > returns float")
    def virtual_memory_available_mb(self):
        self.getLogger().info("Executing virtual_memory_available_mb")
        #  Swap memory returns virtual memory
        retval=psutil.swap_memory().free / self.bytesperMB()           
        return retval  
    @EPLAction("action<integer> returns float")
    def load_average(self, period_seconds):
        self.getLogger().info("Executing load_average")
        try:
            retval = psutil.cpu_percent(period_seconds)                                           
        except Exception as err:
            self.getLogger().warn("getloadavg failed")
            self.getLogger().info(err)
            retval = 0
        return retval   
    @EPLAction("action< > returns integer")
    def system_clock_time(self):
        self.getLogger().info("Executing disk_total_mb")
        retval=time.time()  
        return retval  
    @EPLAction("action< > returns integer")
    def uptime(self):
        self.getLogger().info("Executing uptime")
        retval=time.time() - systemPlugin.start    
        return retval  
