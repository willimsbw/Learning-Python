import os
import string

def removeNumerical(filePath):
    """
    Given a file path, removes numerical character: "1234567890" from the name of
    every file in that path.

    filePath: string. The path to the directory with the files you want to rename.
    """
    #get files names from folder
    fileList = os.listdir(filePath)
    print("Original file names:")
    print(fileList)
    #for each file
    for fileName in fileList:
        #will delete  any numerical characters when used in str.translate()
        transTable = str.maketrans("1234567890", "          ", "1234567890")
        #new name is the file name with any numerical characters deleted
        newName = fileName.translate(transTable)
        os.rename(fileName, newName)

    print("renamed files:")
    print(fileList)

removeNumerical(r"c:/version-control/Learning-Python/prank/prank-photos")
