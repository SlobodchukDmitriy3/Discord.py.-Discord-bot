import discord
class MyClient(discord.Client):
    async def Klubnika(self):
        print('Logged on as {0}!'.format(self.user))
        async def Calc(self,message):
            print('Message from {0.autor: {0.content}'.format(message))
client = MyClient()
client.run('Here is the TOKEN')
