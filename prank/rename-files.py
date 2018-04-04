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
    #save original current working directory (cwd) then change cwd to filePath
    originalDir = os.getcwd()
    os.chdir(filePath)
    #for each file
    for fileName in fileList:
        #will delete  any numerical characters when used in str.translate()
        transTable = str.maketrans("1234567890", "          ", "1234567890")
        #new name is the file name with any numerical characters deleted
        newName = fileName.translate(transTable)
        print("renaming " + fileName + " to " + newName)
        os.rename(fileName, newName)

    print("The files have had numbers removed from their names. Check '" + filePath + "' to see for yourself")
    #put the current working directory back to where we found it
    os.chdir(originalDir)

removeNumerical(r"c:/version-control/Learning-Python/prank/prank-photos")
