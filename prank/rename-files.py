import os
import string

def renameFiles():
    #get files names from folder
    fileList = os.listdir(r"c:/version-control/Learning-Python/prank/prank-photos")
    print(fileList)
    #for each file
    for fileName in fileList:
        #will delete  any numerical characters when used in str.translate()
        transTable = str.maketrans("1234567890", "          ", "1234567890")
        #new name is the file name with any numerical characters deleted
        newName = fileName.translate(transTable)
        os.rename(fileName, newName)

    print("renamed:")
    print(fileList)

renameFiles()
