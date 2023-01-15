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

# for fileName in os.listdir(depDir):
#     mo = extPattern.search(fileName) # mo will be None if fileName ends with different extension
#     if mo == None:
#         continue
#     else:
#         absDepDir = os.path.abspath(depDir) # get the absolute paths to depature and destination directories
#         absDesDir = os.path.abspath(desDir)
#         fileName = os.path.join(absDepDir, fileName) # create an absolute path to the file wich will be copied

#         shutil.copy(fileName, absDesDir) # copy this file

for folderName, subfolders, fileNames in os.walk(depDir):
    for fileName in fileNames:
        fileName = os.path.join(folderName, fileName)
        mo = extPattern.search(fileName)
        if mo == None:
            continue
        else:
            shutil.copy(fileName, desDir)