
import _defines as File

class Inventory():

    def __init__(self, player):

        if File.FileExist(player.directory):

            self.slot = player.getInventory()

        else: print("[ERR.151] Can't Find File! : _classes.py, 12")


class Player():

    def __init__(self, userid:int | str, userName:str = None):

        self.directory = f"data/user/{userid}.json"

        if File.FileExist(self.directory):
            
            self.data = File.ReadFile(self.directory)

        else:

            File.createFile(self.directory)

            File.setValue(self.directory, "login", True) # 로그인 여부
            File.setValue(self.directory, "username", userName) # 유저 이름
            File.setValue(self.directory, "level", 0) # 레벨
            File.setValue(self.directory, "exp", 0) # 경험치
            File.setValue(self.directory, "needexp", 100) # 최대경험치
            File.setValue(self.directory, "usingHunt", None) # 사냥중인 사냥터
            File.setValue(self.directory, "usingweapon", None) # 장착중인 무기
            File.setValue(self.directory, "inventory", []) # 가방

    def getInventory(self) -> Inventory:

        return Inventory(self)

    def create(userid:int | str, userName:str = None):

        directory = f"data/user/{userid}.json"

        File.createFile(directory)
            
        File.setValue(directory, "login", True) # 로그인 여부
        File.setValue(directory, "username", userName) # 유저 이름
        File.setValue(directory, "level", 0) # 레벨
        File.setValue(directory, "exp", 0) # 경험치
        File.setValue(directory, "needexp", 100) # 최대경험치
        File.setValue(directory, "usingHunt", None) # 사냥중인 사냥터
        File.setValue(directory, "usingweapon", None) # 장착중인 무기
        File.setValue(directory, "inventory", []) # 가방

        return Player(userid=userid, userName=userName)
