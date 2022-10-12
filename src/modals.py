
import os, sys

from _classes import *
sys.path.insert(1, os.path.abspath(''))

# ========================================================

import discord
import _defines as File
import random
from datetime import datetime

def log(msg):

    now = datetime.now()

    print(now.strftime(('[ %Y-%m-%d %H:%M:%S ]')) + msg)
    with open("data/log/log.txt", mode="a+", encoding="UTF-8") as f:
        f.write(now.strftime(('[ %Y-%m-%d %H:%M:%S ]')) + msg + "\n")

# ========================================================

class CreateUser(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        global secretcode
        secretcode = str(random.randint(100000, 999999))

        self.add_item(discord.ui.InputText(label="닉네임"))
        self.add_item(discord.ui.InputText(label="보안 코드 [ " + secretcode + " ]"))

    async def callback(self, interaction: discord.Interaction):

        self.isHuman = secretcode == self.children[1].value

        name = self.children[0].value
        end = False

        if self.isHuman:

            nicknameBanList = [
                " ",
                ":",
                ";",
                "'",
                '"',
                "/",
                "\\",
                ",",
                ".",
                "!",
                "@",
                "#",
                "$",
                "%",
                "^",
                "&",
                "*",
                "(",
                ")",
                "-",
                "+",
                "=",
                "|",
                "<",
                ">",
                "?"
            ]

            if not end and len(name) < 2 : embed = discord.Embed(title=":x: 닉네임이 너무 짧아요!\n", description="닉네임은 **2글자에서 16글자 사이**예요.\n", colour=discord.Colour.red()); end=True
            if not end and len(name) > 16 : embed = discord.Embed(title=":x: 닉네임이 너무 길어요!\n", description="닉네임은 **2글자에서 16글자 사이**예요.\n", colour=discord.Colour.red()); end=True
            
            for str in nicknameBanList:

                if not end and name.find(str) != -1: embed = discord.Embed(title=":x: 닉네임에는 **알파벳, 숫자, 한글, 밑줄 만 사용 가능**해요.\n", colour=discord.Colour.red()); end=True; break      

            name = name.replace("_", "\_")

            log(f"[COMMAND:user_create] : {interaction.user.name}'s new User Data :")
            log(f"\tNICKNAME : {name}")
            log(f"\tisHUMAN ? {self.isHuman}")

            userid = interaction.user.id

            if not end:
                Player.create(userid, name)
                embed = discord.Embed(title = f"환영합니다,  {name}님!\n", description="계정이 성공적으로 생성되었습니다.\n", color = 0x48BF91); end=True

        elif not end:

            embed = discord.Embed(title = ":x: 보안 코드가 틀렸습니다.\n", colour = discord.Colour.red()); end=True
            
        embed.add_field(name = "문제가 있나요?", value="[저희 디스코드 서버로 오세요!](https://discord.com/invite/H9N78BKyAT)\n")
        embed.set_footer(text = "\nⓒ 모든 저작권은 웰로 스튜디오에 있습니다.")

        await interaction.response.send_message(embeds=[embed])