# Get Current working directory
import os
import shutil

print(os.getcwd())

# change directory
# os.chdir('C:\\Python33')
print(os.getcwd())

# List directory - This method takes in a path and returns a list of subdirectories and files in that path.
print(os.listdir())  # ['pyFileManagement.py', '__init__.py']

# Making a new directory
os.mkdir('test')
print(os.listdir())  # ['pyFileManagement.py', 'test', '__init__.py']

# Removing a directory
os.remove('test')
print(os.listdir())

# renaming a directory or file
os.mkdir('test')
os.rename('test', 'new test')
print(os.listdir())
os.remove('test')

# delete the empty directory "mydir"
os.rmdir("test")

# delete "test" directory and all of its contents
shutil.rmtree("test")
