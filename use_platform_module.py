
import platform

system_name:str = platform.system()
print(f"System Name: {system_name}")

version:str = platform.version()
print(f"System Version: {version}")

python_version:str = platform.python_version()
print(f"Python Version: {python_version}")

uname:str = platform.uname()
print(f"Uname Interface: {uname}")

machine:str = platform.machine()
print(f"Machine Type: {machine}")

processor:str = platform.processor()
print(f"Processor Type: {processor}")

import sys
from locale import getdefaultlocale, getencoding, getlocale

print({
    'System Python Version': sys.version,
    "System Platform": sys.platform,
    "System Executable (Python)": sys.executable,
    
    "getdefaultencoding": sys.getdefaultencoding(),
    "Locale Settings (Language)": getdefaultlocale(),
    "Encoding Type": sys.getdefaultencoding(),
    "File System Encoding": sys.getfilesystemencoding(),
    "Locale Settings (Recommended)": getlocale(),
    "Encoding Type (Recommended)": getencoding()
})

object_str = 'Hello world!'
print(f"Object Size: {sys.getsizeof(object_str)} bytes")

arguments:list[str] = sys.argv
print(f"Command Line Arguments: {arguments}")
