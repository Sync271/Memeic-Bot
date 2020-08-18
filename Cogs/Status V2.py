import discord
from itertools import cycle
import random
from discord.ext import commands, tasks


class Status(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.change_status.start()

    def cog_unload(self):
        self.change_status.cancel()

    @tasks.loop(seconds=120)
    async def change_status(self):
        fs = ['Sweat (A La La La La Long)','Witch Doctor - Cartoons','Wannabe - Spice Girls','Dragostea Din Tei - O-Zone','Boom, Boom, Boom, Boom!! - Vengaboys','Barbie Girl - Aqua','Friday - Rebecca Black',"U Can't Touch This - MC Hammer",'Mambo No. 5 (A Little Bit Of...) - Lou Bega','Call Me Maybe - Carly Ras Jepsen',"Stayin' Alive - Bee Gees",'Gonna Make You Sweat (Everybody Dance Now) - C & C Music Factory',' Like to Move It - Real 2 Real','Y.M.C.A - Village People','Tunak Tunak Tun - Daler Mehndi','Lemon Tree - Fools Garden','Macarena - Los Del Rio','Gangnam Style - PSY','Funky Town - Lipps Inc.','#SELFIE - The Chainsmokers','Lollipop - Mika','The Lazy Song - Bruno Mars','Hot N Cold - Katy Perry (and the Chipettes version’s even better)','Dub-I-Dub - Me & My','Girls Just Wanna Have Fun - Cyndi Lauper','We No Speak Americano - Yolanda Be Cool, DCup','Livin’ La Vida Loca - Ricky Martin','Dancing Lasha Tumbai - VERKA SERDUCHKA','My First Kiss - 3oh3! feat. Ke$ha','We Will Rock You - Queen','Uptown Funk - Mark Ronson & Bruno Mars','Summer Nights - Olivia Newton-John, John Travolta (soundtrack from Grease)','Rude - MAGIC!','We Like To Party! - Vengaboys','Beat It - Michael Jackson','Sexy And I Know It - LMFAO','Waka Waka - Shakira','Pump It - The Black Eyed Peas','Hooked on a Feeling - Blue Swede','Grace Kelly - Mika','Don’t Stop Me Now - Queen','Money Money Money - Abba','Beauty School Drop Out - Frankie Avalon (soundtrack from Grease)','Ice Ice Baby - Vanilla Ice','You Can’t Roller Skate In A Buffalo Herd - Roger Miller','YOLO - The Lonely Island, Adam Levine, Kendrick Lamar','Axel F - Crazy Frog']
        #await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'~help - {random.choice(fs)}'))
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='~help'))


    @change_status.before_loop
    async def before_change_status(self):
        print('Bot Ready!')
        await self.client.wait_until_ready()

def setup(client):
    client.add_cog(Status(client))
