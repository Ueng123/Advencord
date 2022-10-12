
# ========================================================

import discord
from datetime import datetime

def log(msg):

    now = datetime.now()

    print(now.strftime(('[ %Y-%m-%d %H:%M:%S ]')) + msg)
    with open("data/log/log.txt", mode="a+", encoding="UTF-8") as f:
        f.write(now.strftime(('[ %Y-%m-%d %H:%M:%S ]')) + msg + "\n")

import modals as Modal
import asyncio
import _defines as File

bot = discord.Bot() # Bot 인스턴트

# 48BF91 : Ocean green | discord.Colour.red : Red;

# ========================================================

data:dict = File.ReadFile('src/config.json')

@bot.event
async def on_ready():

    print("\n"*10)
    print("="*20)
    print("\n")
    print("\n")
    print(f"{data['project']} Project : [ v. {data['version']} ]")
    print(f"    {data['description']}")
    print("\n")
    print(f"Made by. {data['author']}")
    print("\n")
    print("\n")
    print("="*20)
    print("\n"*10)

user = bot.create_group("계정", "유저 관련 명령어들입니다.")

@user.command(name="생성", description="당신의 모험이 시작됩니다.")
async def user_create(ctx:discord.ApplicationContext):

    log(f"[COMMAND:user_create] : {ctx.author.name} has tried create user;")

    if not File.FileExist(f"data/user/{ctx.author.id}.json"):

        createModal = Modal.CreateUser(title="계정 생성")

        await ctx.send_modal(createModal)

    else:

        embed = discord.Embed(title = ":x: 이미 계정이 존재합니다.", colour = discord.Colour.red())
        embed.add_field(name = "문제가 있나요?", value="[저희 디스코드 서버로 오세요!](https://discord.com/invite/H9N78BKyAT)", inline=False)
        embed.add_field(name = "계정을 새로 만들려면?", value="</탈퇴:123123> 후 다시 시도해주세요!")
        embed.set_footer(text = "모든 저작권은 Wello Studio에 있습니다.")

        await ctx.respond(embed=embed)

#user.command(name="탈퇴", description="당신의 모험을 끝냅니다.")

    
@bot.command(name="사냥",description="사냥터로 이동해 사냥합니다.")
async def goHunt(ctx):

    pass

    # 사냥터 고르기

    

    # 값 받아서 사냥 돌려주기 : (Player).data["Hunting"]에 저장


#@bot.command(name="던전")
#@bot.command(name="보스")

daily = bot.create_group("일일", "자정 12시에 초기화 됩니다.")
#@daily.command(name="보상")
#@daily.command(name="퀘스트")

weekly = bot.create_group("주간", "초기화 7일 후 자정 12시에 초기화 됩니다.")
#@weekly.command(name="퀘스트")

#@bot.user_command(name="프로필 조회")

# ========================================================

bot.run(data['token'])
