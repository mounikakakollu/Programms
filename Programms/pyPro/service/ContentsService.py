from dao import ContentsDao

def createContents(contentsJson):
    contents = ContentsDao.createContents(contentsJson)
    return contents

def getContents():
    contents = ContentsDao.getContents()
    print(contents)
    return contents
