import os, pyinputplus as pyip

# ask user to input the absolute path to the directory
print('Please input the path to the directory that you would like to clean: ')
toCleanDir = pyip.inputFilepath()

# go through the directory
for folderName, subfolders, fileNames in os.walk(toCleanDir):
    for file_name in fileNames:
        fileName = os.path.join(folderName, fileName) # create a fileName based on current folder and its name
        if os.path.getsize(fileName) > 100000:
            print(fileName, os.path.getsize(fileName))