import discord, random, urllib, bs4
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
    
    @commands.command()
    async def 주사위(ctx):
        randnum = random.randint(1, 6)  # 1이상 6이하 랜덤 숫자를 뽑음
        await ctx.send(f'주사위 결과는 {randnum} 입니다.')

    @commands.command()
    async def 광산(ctx):
        minerals = ['다이아몬드', '루비', '에메랄드', '자수정', '철', '석탄']
        weights = [1, 3, 6, 15, 25, 50]
        results = random.choices(minerals, weights=weights, k=5)  # 광물 5개를 가중치에 따라 뽑음
        await ctx.send(', '.join(results) + ' 광물들을 획득하였습니다.')

    @commands.command()
    async def 가위바위보(ctx, user: str):  # user:str로 !game 다음에 나오는 메시지를 받아줌
        rps_table = ['가위', '바위', '보']
        bot = random.choice(rps_table)
        result = rps_table.index(user) - rps_table.index(bot)  # 인덱스 비교로 결과 결정
        if result == 0:
            await ctx.send(f'{user} vs {bot}  비겼습니다.')
        elif result == 1 or result == -2:
            await ctx.send(f'{user} vs {bot}  유저가 이겼습니다.')
        else:
            await ctx.send(f'{user} vs {bot}  봇이 이겼습니다.')
    
    @commands.command()
    async def 검색(ctx,search=None):
        if search==None:
            searchem = discord.Embed(title='그래서 뭘 검색 하라고요? `?!검색 (원하는 컨탠츠)`',description='띄어쓰기 하면 한 문장만 검색 되요!',color=0xFF0F13)
            return await ctx.send(embed = searchem)
        embed = discord.Embed(title='**검색 결과**')
        embed.add_field(name='네이버', value=f'[바로가기](https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={search})')
        embed.add_field(name='유튜브',value=f'[바로가기](https://m.youtube.com/results?sp=mAEA&search_query={search})')
        embed.add_field(name='구글',value=f'[바로가기](https://www.google.com/search?q={search})')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Message(bot))