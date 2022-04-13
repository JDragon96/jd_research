import os
import sys

def getFileNameFromPath(path: str):
    return os.path.basename(path)

def getFileExtFromPath(path: str):
    return os.path.splitext(path)[1]

def getFileDirFromPath(path: str):
    return os.path.dirname(path)

def getSplitFromPath(path: str):
    return os.path.split(path)

def getOnlyFileName(path: str):
    fName = getFileNameFromPath(path)
    return os.path.splitext(fName)[0]

if __name__=="__main__":
    print(getFileNameFromPath("C:Users\ADMIN\Desktop\git_project\my_repo\jd_pyqt_research\README.md"))
    print(getFileExtFromPath("C:Users\ADMIN\Desktop\git_project\my_repo\jd_pyqt_research\README.md"))
    print(getFileDirFromPath("C:Users\ADMIN\Desktop\git_project\my_repo\jd_pyqt_research\README.md"))
    print(getOnlyFileName("C:Users\ADMIN\Desktop\git_project\my_repo\jd_pyqt_research\README.md"))