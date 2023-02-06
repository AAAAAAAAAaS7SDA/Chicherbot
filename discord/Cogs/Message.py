import discord, time, urllib, bs4
from discord.ext import commands
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def soup(self, url):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        soup = bs4.BeautifulSoup(html, "html.parser")
        return soup
    
    @commands.command(aliases=['현재핑알려줘'])
    async def ping(self, ctx):
        pings = round(self.bot.latency*1000)
        if pings < 100:
            pinglevel = '🔵 매우좋음'
        elif pings < 300: 
            pinglevel = '🟢 좋음'
        elif pings < 400: 
            pinglevel = '🟡 보통'
        elif pings < 6000: 
            pinglevel = '🔴 나쁨'
        else: 
            pinglevel = '⚪ 매우나쁨'
        embed = discord.Embed(title='ping', description=f'{pings} ms\n{pinglevel}')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['메세지지워줘'])
    async def clean(self, ctx, *args):
        try:
            i = (ctx.message.author.guild_permissions.administrator)
            if i is True:
                await ctx.channel.purge(limit=int(1))
                await ctx.channel.purge(limit=int(args))
                embed = discord.Embed(title="메시지 삭제 알림", description=f"최근 디스코드 채팅 {args}개가\n관리자 {ctx.message.author}님의 요청으로 인해 정상 삭제 조치 되었습니다", color=0x00FFFF)
                load = await ctx.send(embed=embed)
                time.sleep(5)
                await load.delete()
            if i is False:
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{ctx.message.author.mention}, 당신은 명령어를 사용할 수 있는 권한이 없습니다")
        except:
            await ctx.channel.purge(limit=int(1))
            load = await ctx.send("> :x: - 관리자 권한, 메시지 삭제 권한 부여 및 숫자를 적어주세요!")
            await load.delete()
        
    @commands.command()
    async def 카트유저(self, ctx):
        try:
            if len(ctx.message.content.split(" ")) == 1: await ctx.send("> :x: - 검색할 카트 유저 적어주세요!")
            learn = ctx.message.content.split(" ")
            location = learn[1]
            url = f"https://bazzi.gg/rider/{urllib.parse.quote(location)}"
            soup = self.soup(url)
            userimg = soup.find('img', {'class':'rider-form__character__image'})['src']
            imm =  soup.find('div', {'class':'level-item has-text-centered pt-2 pb-2'})
            imh = imm.next_sibling.next_sibling
            rankan = imh.find('p', {'class':'subtitle has-text-weight-bold'}).get_text()
            imh2 = imh.next_sibling.next_sibling
            _BIG_PLAY = imh2.find('p', {'class':'subtitle has-text-weight-bold'}).get_text()
            imh3 = imh2.next_sibling.next_sibling
            kart = imh3.find('p', {'class':'subtitle has-text-weight-bold'}).get_text()
            winningrate = soup.find('p', attrs={'class':'subtitle mb-2 has-text-weight-bold'}).get_text()
            winner = soup.find('span', attrs={'class':'recent-matches-summary__win'}).get_text()
            loseing = soup.find('span', attrs={'class':'recent-matches-summary__lose'}).get_text()
            embed = discord.Embed(title="카트 유저검색", description=f"{location}님의 라이더 정보", color=0x00FFFF)
            embed.add_field(name="bazzi.gg에서 검색", value=url, inline=False)
            embed.add_field(name="종합 승률", value=f'{winningrate}{str(winner)}승 {str(loseing)}패', inline=True)
            embed.add_field(name="평균 순위", value=rankan, inline=True)
            embed.add_field(name="가장 많이 플레이한 트랙", value=_BIG_PLAY, inline=True)
            embed.add_field(name="가장 많이 사용한 카트바디", value=kart, inline=True)
            embed.set_footer(text='Made in ! Chives F541(준서)#5090.', icon_url='https://cdn.discordapp.com/avatars/726048454245351534/752a3e938bb363d2472b9ec56bf9cb23.png?size=128')
            embed.set_image(url=userimg)
            await ctx.send(embed=embed)
        except AttributeError: await ctx.send("> :x: - 올바르지 않는 카트 유저입니다. 다시 확인 해 주세요.")
        except UnicodeEncodeError: await ctx.send("> :x: - 올바르지 않는 카트 유저입니다. 다시 확인 해 주세요.")

def setup(bot):
    bot.add_cog(Message(bot))