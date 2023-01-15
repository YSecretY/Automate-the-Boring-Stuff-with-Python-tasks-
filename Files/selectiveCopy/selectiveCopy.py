import os, shutil, pyinputplus as pyip, re

# ask user to input the absolute path to the depature folder
print('Please input the depature path to the files: ')
depDir = pyip.inputFilepath()

# ask user to input the files extensions name
print('Please input the files extensions name: ')
ext = pyip.inputFilepath()

# ask user to input the absolute path to the destination folder
print('Please input the destination path: ')
desDir = pyip.inputFilepath()

# create regularly expression that will find all the files with such extension
extPattern = re.compile(f'{ext}$')

for folderName, subfolders, fileNames in os.walk(depDir):
    for fileName in fileNames:
        fileName = os.path.join(folderName, fileName) # create a fileName for current file in current directory (there can be subdirs)
        mo = extPattern.search(fileName) # mo will be None if file has a different extension
        if mo == None:
            continue
        else:
            shutil.copy(fileName, desDir)