import os
import shutil
import sys

try:
    apama_work = os.environ['APAMA_WORK']
    apama_home = os.environ['APAMA_HOME']
except KeyError:
    print("APAMA_WORK has not been set, please ensure you are running inside an Apama Command shell")
    sys.exit(1)

lib_dir=os.path.join(apama_work, 'lib')
os.makedirs(lib_dir, exist_ok=True)

shutil.copy('MachineInfoPlugin.py', os.path.join(lib_dir, 'MachineInfoPlugin.py'))
print("Installed to %s"%apama_work)

