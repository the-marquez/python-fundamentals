
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))

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
