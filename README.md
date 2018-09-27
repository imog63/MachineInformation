:: Copyright (c) 2018 Software AG, Darmstadt, Germany and/or its licensors
::
:: SPDX-License-Identifier: Apache-2.0
::
:: Licensed under the Apache License, Version 2.0 (the "License");
:: you may not use this file except in compliance with the License.
:: You may obtain a copy of the License at
::
::    http://www.apache.org/licenses/LICENSE-2.0
::
:: Unless required by applicable law or agreed to in writing, software
:: distributed under the License is distributed on an "AS IS" BASIS,
:: WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
:: See the License for the specific language governing permissions and
:: limitations under the License.


"# MachineInformation" 

******************************************************************************************************
***************************** RUNNING THE PLUGIN FROM APAMA DESIGNER *********************************
******************************************************************************************************

A work-in-progress Apama Designer project using a Python Plugin to expose a class including psutil. This version was initially developed and tested on MS Windows, it should however also work on Linux but has not been tested on Linux.

The purpose of the plugin is to give EPL scripts a simple way to access information about the hardware on which the correlator is running.

To use it, install SAG Apama. Run an Apama command prompt and navigate to \Apama\third_party\python and execute the following command:

python -m pip install -U psutil

Create a project in the Apama Designer, and working from the steps described in 
https://iwiki.eur.ad.sag/display/~IAMO/Developing+Python+Plug-ins+in+Apama+Designer 
install PyDev (or other editor) and add PythonPlugins\System.py, monitors\pythonRun.mon, and config\CorrelatorConfig.yaml from this repository to the Designer project.

Running the project in Designer should call each method on the Python class in turn and log the returned values.


******************************************************************************************************
****************** RUNNING THE PLUGIN FROM THE COMMAND LINE ON WINDOWS OR ON LINUX *******************
******************************************************************************************************
As an alternative to using Apama Designer you can run the plug-in from the command-line on Windows or Linux. Below are the step-by-step instructions for running the plugin from the command line.


****** SETTING UP THE APAMA ENVIRONMENT IN A COMMAND LINE CONSOLE.

 	On Windows, run a command prompt and navigate to SoftwareAG\Apama\bin then run apama_env.bat.
 	On Linux, run a command prompt and nagivate to SoftwareAG/Apama/bin then source apama_env.

In both cases the folder softwareAG is the location where you have installed your softwareAG product and the file apama_env will set up the Apama environment.


****** CREATING DIRECTORIES AND INSTALLING PLUGIN FILES.

Create the following folders in the $APAMA_WORK (%APAMA_WORK%) directory.
 	$APAMA_WORK\lib (Windows) or %APAMA_WORK%/lib (Linux).
 	$APAMA_WORK\eventdefinitions (Windows) or %APAMA_WORK%/eventdefinitons (Linux).
 	Copy the plugin file System.py to the directory $APAMA_WORK\lib (Windows) or %APAMA_WORK%/lib (Linux).
 	Copy the plugin file PythonRun.mon to the directory $APAMA_WORK\eventdefinitions (Windows) or %APAMA_WORK%/eventdefinitions (Linux).


*******	CREATING THE DOCUMENTATION FOR THE PLUGIN.

In %APAMA_WORK% ($APAMA_WORK), run the following command 	
	
	java -jar %APAMA_HOME%\lib\ap-generate-apamadoc.jar doc eventdefinitions 	(On Windows)
	java -jar $APAMA_HOME/lib/ap-generate-apamadoc.jar doc eventdefinitions		(On Linux)

Note that the jar file is in a subfolder of APAMA_HOME, but the documentation is created in a new doc subfolder of APAMA_WORK.


****** UPDATING THE PYTHON PACKAGES
Update your Apama python packages to include the package psutil. To do this type the following command in your command prompt.
	
	$APAMA_HOME\third_party\python -m pip install -U psutil			(On Windows)
	%APAMA_HOME%/third_party/python -m pip install -U psutil			(On Linux)
	
	
****** UPDATE THE PLUGIN CONFIGURATION FILE "CorrelatorConfig.yaml".	
To update "CorrelatorConfig.yaml", replace the existing configuration with the following text.

eplPlugins:
  pythonSystem:
    pythonFile: ${APAMA_WORK}/lib/System.py
    class: systemPlugin

	
****** RUNNING THE CORRELATOR WITH THE PLUG-IN.
Run the correlator with the --config option to load the configurations file. Make sure to specific the path to
the plug-in configuration file. It should look something like this.

	correlator --config pathToConfigFile\CorrelatorConfig.yaml	(Windows)
	correlator --config pathToConfigFile/CorrelatorConfig.yaml	(Linux)
	
	
In a separate command prompt run apama_env.bat as described above. In the same prompt, use the engine_inject command to inject the pythonRun.mon file in to the correlator. It should look something like this.

	engine_inject pathToPythonRun\pythonRun.mon				(Windows)
	engine_inject pathToPythonRun/pythonRun.mon				(Linux)

	
*************************************************************************************************************
******************* USING PYSYS TO TEST THE PLUG-IN *********************************************************
*************************************************************************************************************
To run the pysys test that comes with the plug-in, change to the directory that contains the python test,
this will be,

	$APAMA_WORK\MachineInformation-master\tests\testplugin		(On Windows)
	%APAMA_WORK%/MachineInformation-master/tests/testplugin		(On Linux)
	
Then run pysys by typing,

	pysys run
	
 
	
