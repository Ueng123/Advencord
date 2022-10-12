
import json
import os

def FileExist(filename:str) -> bool:
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            result = json.loads(f.read())
    except:
        return False

    else:
        return True
        
def ReadFile(filedir:str) -> dict:
    filename = filedir
    print("Checking "+filename)
    result = []

    folder = "/".join(filename.split("/")[:-1])
    createFolder(directory=folder)

    try:
        open(filename, 'a+').close()
    except:pass

    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            result = json.loads(f.read())
    except:
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write("{}")
            
    return result

def getValue(filedir:str, param:str | int):
    filename = filedir
    file:dict = ReadFile(filename)
    print(param)
    if type(file) == list:
        file = {}
    try:
       file[param]
    except:
        print("error: can't get Value ", param, "in", filename)
        return False

    else:
        return file[param]

def setValue(filedir: str, param: str, value: any) -> None:
    filename = filedir
    """

    :rtype: object
    """
    file: dict = ReadFile(filename)
    print(type(file))
    if type(file) == list:
        file = {}
    try:
        file[param] = value
    except:
        print("error: can't set Value ", param, "in", filename, "to", value)

    newfile = json.dumps(file, indent=4)
 
    with open(filename, 'w+', encoding='UTF-8') as f:
        f.write(newfile)


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError: 
        pass

def createFile(directory):

    folder = "/".join(directory.split("/")[:-1])
    createFolder(directory=folder)

    try:
        f = open(directory, 'r', encoding='UTF-8')
    except:
        with open(directory, 'w', encoding='UTF-8') as f:
            f.write("{}")
    finally:
        f.close()
