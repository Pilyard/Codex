import discord, json, requests

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('#meme'):
            await message.channel.send(get_meme())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('293821fv18v78192v21uv8219mvc219s129s129fn2917f8917v8912vu2189v12uv89') #Token ID randomly just to git push on github.
