
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))

print(f"Process ID: {os.getpid()}")

print({ 'current_path': current_path })

# Environment Variables
path_value = os.getenv('Path') # Windows: Path; Linux: PATH;
# print({ 'path_value': path_value })

java_home = os.getenv('JAVA_HOME_II')

if java_home is None:
    print('JAVA_HOME_II is not configured!')
else:
    print({ 'java_home': java_home })
    print(f'Java installation directory: {java_home}')
    
nvm_home = os.getenv('NVM_HOME')
if nvm_home is None:
    print('NVM_HOME is not configured!')
else:
    print({ 'nvm_home': nvm_home })
    print(f'NVM installation directory: {nvm_home}')

print(f"Contents of {current_path}:")

content_dir:list[str] = os.listdir(current_path)

for index, item in enumerate(content_dir):
    print(f"{index}: {item}")
