import discord
from discord import app_commands 
import random
import datetime

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f'{self.user}이 시작되었습니다')  #  봇이 시작하였을때 터미널에 뜨는 말
        game = discord.Game('민섭 E 야 이라고 부르세요!')          # ~~ 하는중
        await self.change_presence(status=discord.Status.online, activity=game)

client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name = '민섭아', description='여기 있다') 
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"민섭 E 이 여기 있습니다!", ephemeral = True) 

@tree.command(name = '바보니', description='아니 나 바보라고') 
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"아...니요? 전 바보 아니예요.", ephemeral = True) 

@tree.command(name = '게임', description='게임 해줘요!') 
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"전 게임를 못합니다...", ephemeral = True) 

@tree.command(name = '봇여기로초대함', description='민섭 E이 알려줘요!') 
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"봇은 9월12일날에 생성 되어고 들어온날짜은 11월 16일입니다.", ephemeral = True) 

@tree.command(name = '다른거은', description='안돼') 
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"안됨니다", ephemeral = True) 

@tree.command(name = '주사위', description='랜덤 뽑아요!') 
async def slash(interaction: discord.Interaction):
    ran = random.randint(0,5)       # 봇 랜덤 변수 갯수   0,3 = 0,1,2,3  /  0,5 = 0,1,2,3,4,5
    if ran == 0:        # 랜덤 변수 0
        d = "1"           # 랜덤 변수 0 의 내용
    if ran == 1:        # 랜덤 변수 1
        d = "2"           # 랜덤 변수 1 의 내용
    if ran == 2:        # 랜덤 변수 2
        d = "3"           # 랜덤 변수 2 의 내용
    if ran == 3:        # 랜덤 변수 3
        d = "4"           # 랜덤 변수 3 의 내용
    if ran == 4:        # 랜덤 변수 3
        d = "5"           # 랜덤 변수 3 의 내용
    if ran == 5:        # 랜덤 변수 3
        d = "6"           # 랜덤 변수 3 의 내용
    await interaction.response.send_message(d)

@tree.command(name = '도옴말', description='도옴말 알려줘요!') 
async def slash(interaction: discord.Interaction):
    embed = discord.Embed(title="도옴말", color=0x4000FF) #큰 제목과 작은 제목을 보여준다
    embed.add_field(name="민섭아", value="기본말 입니다.", inline=False)
    embed.add_field(name="주사위", value="랜덤으로 뽑습니다.", inline=False)
    embed.add_field(name="다른거은?", value="안돼안돼", inline=False)
    embed.add_field(name="봇여기로초대함?", value="알려 줘요!", inline=False)
    embed.add_field(name="게임", value="게임 할 수 없다", inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(name = '테스트', description='테스트') 
async def slash(interaction: discord.Interaction):
    embed = discord.Embed(title="안녕하세요", color=0xFFE400)
    embed.add_field(name="asd", value="asd", inline=False)
    await interaction.response.send_message(embed=embed)

client.run('MTAxODc2MjYzMjMxMzk3NDc5NA.G4D6bD.sXYionxoTmVp_K8T-fquNnxyjemlsoibH1Woxc')