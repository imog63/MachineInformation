# Apama MachineInformation Plugin

A work-in-progress Apama Python Plugin to expose system information.

The purpose of the plugin is to give EPL scripts a simple way to access information about the hardware on which the correlator is running.

## Building the plugin

To build the plugin, first ensure you have sourced the `apama_env` script in your current shell. This script can be found inside the `bin` directory of your Apama installation.

Next, satisfy the dependency requirements. This is most easily achieved by running the below command:

	On Unix:
	python3 -m pip install -r requirements.txt --target $APAMA_HOME/third_party/python/lib/python3.6/site-packages

	On Windows:
	python3 -m pip install -r requirements.txt --target %APAMA_HOME%\third_party\python\lib\python3.6\site-packages

Finally, run the setup.py script to install the plug-in.

## Running the tests

To run the tests, first ensure you have sourced the `apama_env` script in your current shell. This script can be found inside the `bin` directory of your Apama installation. Next, navigate to the `tests` directory and execute the following command:

	pysys run
