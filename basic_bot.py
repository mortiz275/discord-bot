import discord
import random
import os
from emoji import UNICODE_EMOJI

# COPY THIS FOR EVERY LINE
#if message.content.lower().strip().startswith("$Lux")

client= discord.Client()
lolList= ["Time to grind League of Legends","Do not play League of Legends"]
TAKASHI_LIST = ["-_-",":"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    global cj_toggle
    cj_toggle = True

@client.event
async def on_message(message):
    global cj_toggle
    
    if message.author == client.user:
        return

    if message.content.lower().strip().startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.lower().strip().startswith('$lol'):
        await message.channel.send(random.choice(lolList))
            
    if message.content.lower().strip().startswith("$lons"):
        await message.channel.send("Lons ~~Bad~~ Good :)")

    if message.content.lower().strip().startswith("$lonsgood"):
        await message.channel.send("Lons good???? https://streamable.com/tcq8xb")

    if message.content.lower().strip().startswith("$jakob"):
        await message.channel.send("I just love lux so much shes such a silly little champion from her laugh to her emotes everything about her is just so sparkly (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ) Her quotes are also just so kawaii ~ cute o3o my favorite by far is The superior tactic is to never give up because its true!!!! u should never give up! (づ｡◕‿‿◕｡)づ Not to mention her skins are so (~˘▾˘)~ cutee to look at they're so bright and shinyy!!!! just like her personality haha (｡◕‿‿◕｡)")

    if message.content.lower().strip().startswith("$cj"):
        await message.channel.send("Hi I’m CJ and I will use analytical data to prove why yuumi does 4 more damage using my build")

    if message.content.lower().strip().startswith("$dexter"):
        await message.channel.send("https://imgur.com/xTHVRRo")

    if message.content.lower().strip().startswith("$andrew"):
        await message.channel.send("Andrew be like: i WaNt CUuM iN mY AsSSsSssSSs")

    if message.content.lower().strip().startswith("$kinomoto"):
        await message.channel.send("Kinomoto uses the art of Ninjutsu and stealth to out-maneuver his enemies.")
            
    if message.content.lower().strip().startswith("$summer"):
        await message.channel.send("Click this: https://www.wattpad.com/925104640-a-cold-summer-night-bakugou-x-deku-lemon-a-cold")
        
    if message.content.lower().strip().startswith("$love"):
        await message.channel.send("I love you Onii-chan!~ uwu")
        
    if message.content.lower().strip().startswith("$kippy"):
        await message.channel.send("Fricking furry peddle file")
        
    if message.content.lower().strip().startswith("$lux"):
        await message.channel.send("For you, Jacob <3 * kiss *: http://luxandria.detergentisthe.best/")

    if message.content.lower().strip().startswith("$steak"):
        await message.channel.send("Its what's for dinner")
        
    if message.content.lower().strip().startswith("$debug2"):
        await message.channel.send(str(any(i in message.content for i in UNICODE_EMOJI)))
    elif message.content.lower().strip().startswith("$debug"):
        await message.channel.send('`'+message.content+'`')
        print(message.content)
    
        
    if message.content.lower().strip().startswith("$cjtoggle") and (message.author.id == 456352346880999424 or message.author.id == 248273753782353928):
        cj_toggle = not(cj_toggle)
        await message.channel.send("CJ toggle is now: "+str(cj_toggle))
    
    if 'despacito' in message.content:
        await message.add_reaction('<:GRIEF:714226306996371476>')
        await message.add_reaction('<:sadyeehaw:728823509492695113>')
        await message.channel.send("This is so sad... Rythm play Despacito <:sadyeehaw:728823509492695113>")
        
    if (message.author.id == 468230976317685795) and (any(i in message.content for i in UNICODE_EMOJI) or any(i in message.content for i in TAKASHI_LIST)):
        await message.delete()
        await message.channel.send("Shut up takashi kimono :clown:")
        
    if(message.author.id==352623344660643841) and (message.content= "horny"):
        await message.delete()
        await message.channel.send("No horny in general")

    if len(message.content)>=200 and cj_toggle:
        await message.channel.send("CJ Moment")

    if 'Takashi Kinomoto' in message.content:
        await message.channel.send("Coming soon...")

    if message.content.lower().strip().startswith("$music"):
        await message.channel.send("Mauricio's Playlist: https://www.youtube.com/playlist?list=PLiM1Bzslu7LmLOjd3ZhXSNno1pNJW2kW4")

    if message.content.lower().strip().startswith("$kimono"):
        await message.channel.send("https://cdn.discordapp.com/attachments/608503491782246423/765716688402120735/takashi_kimono.png")
        


client.run(os.environ.get('BOT_TOKEN'))
