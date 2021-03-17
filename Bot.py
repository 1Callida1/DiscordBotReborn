import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
from gtts import gTTS
import os
import threading
from threading import Thread
import random
import time
import googletrans
from googletrans import Translator
import subprocess
import asyncio
from enum import Enum
from vk_audio import audio
import vk_api
import urllib.request
from pydub import AudioSegment
import operator
import traceback

disconnect_quiz = False
autor_Check = False
name_check = False
check_quiz = False
quiz_members = []
preroll = False
songs = []
quiz_started = False
list_question = []
quiz_channel = ''
quiz_ch = []

client = commands.Bot(command_prefix = 'r!')
TOKEN = 'NzA3MzE1MTEwOTgwNjE2MjIy.XrHBaQ.eXUQDaN6QVSEkVCv0W-TlryC_Tw'
serverid = 689361874365841411
rainbowrolename = "🌈Rainbow"
delay = 1
nicks = ['lida', 'l ida', 'l i da', 'l i d a', 'l i da', 'l ida', 'lida', '#lida#', '##ida#', '###da#', '####a#', '######', '####a#', '###da#', '##ida#', '#lida#']
Token = 'NzkxNTY0NTY2NjEzOTgzMjUy.X-Q_8w.pkHgMeLMD3wPGJud6GiiNjRw5kk'

client = commands.Bot(command_prefix = 'y!')

class question:
    def __init__(self, file, autor, name):
        self.file = file
        self.autor = autor
        self.name = name
    
class member_quiz:
    def __init__(self, id, score):
        self.id = id
        self.score = score


def clear(x):
    incorrect_text = [' (zaycev.net)', ' Album Version', ' UK Extended Mix',' Avicii Instrumental Radio Edit', ' Radio Edit', ' K-Mix', ' x', ' Original Motion Picture Soundtrack', ' live', ' Album Version (Edited)', '&#39;', '-', ' Reprise']
    incorrect_words = ['(', ')', '[', ']']
    if(x.startswith('й') or x.startswith('ц') or x.startswith('у') or x.startswith('к') or x.startswith('е') or x.startswith('н') or x.startswith('г') or x.startswith('ш') or x.startswith('щ') or x.startswith('з') or x.startswith('х') or x.startswith('ъ') or x.startswith('ф') or x.startswith('ы') or x.startswith('в') or x.startswith('а') or x.startswith('п') or x.startswith('р') or x.startswith('о') or x.startswith('л') or x.startswith('д') or x.startswith('ж') or x.startswith('э') or x.startswith('ё') or x.startswith('я') or x.startswith('ч') or x.startswith('с') or x.startswith('м') or x.startswith('и') or x.startswith('т') or x.startswith('ь') or x.startswith('б') or x.startswith('ю') or x.startswith('Й') or x.startswith('Ц') or x.startswith('У') or x.startswith('К') or x.startswith('Е') or x.startswith('Н') or x.startswith('Г') or x.startswith('Ш') or x.startswith('Щ') or x.startswith('З') or x.startswith('Х') or x.startswith('Ъ') or x.startswith('Ф') or x.startswith('Ы') or x.startswith('В') or x.startswith('А') or x.startswith('П') or x.startswith('Р') or x.startswith('О') or x.startswith('Л') or x.startswith('Д') or x.startswith('Ж') or x.startswith('Э') or x.startswith('Ё') or x.startswith('Я') or x.startswith('Ч') or x.startswith('С') or x.startswith('М') or x.startswith('И') or x.startswith('Т') or x.startswith('Ь') or x.startswith('Б') or x.startswith('Ю')):
        pass
    else:
        mapping = str.maketrans("арохкусмивАРОХКУСМИВ", "apoxkycmnbAPOXKYCMNB")
        x = x.translate(mapping)        
    for i in range(len(incorrect_text)):
        x = x.replace('КАР-МЭН', 'кар мэн')
        x = x.replace(incorrect_text[i], "")
        x = x.replace("ё", "е")
        x = x.replace("Ё", "е")
        x = x.replace("é", "е")
    for i in range(len(incorrect_words)):
        if(incorrect_words[i] in x):
            if(incorrect_words[len(incorrect_words)-1] in x or incorrect_words[i+1] in x): 
                s = list(x)
                index_min = x.index(incorrect_words[i])
                if(i == len(incorrect_words)-1):
                    index_max = x.index(incorrect_words[len(incorrect_words)-1])
                else:
                    index_max = x.index(incorrect_words[i+1])
                j = 0
                while index_min <= index_max:
                    del s[index_min]
                    j=j+1
                    if(index_min == index_max-j+1):
                        break
                x = "".join(s)
                if('  ' in x):
                    x = x.replace('  ', ' ')
    return x


def rgb_gen_v2(num):
    for r in range(17):
        if(num[0] == 255):
            for g in range(17):
                if(num[1] == 255):
                    for b in range(17):
                        if(num[2] == 255):
                            num = [15, 0, 0]
                            return num
                        else:
                            num[2]=num[2]+15
                            return num
                else:
                    num[1]=num[1]+15
                    return num
        else:
            num[0]=num[0]+15
            return num
 

@client.event
async def on_ready():
    print('[log] Бот запущен')
    client.loop.create_task(rainbowrole(rainbowrolename))

@client.command(pass_context = True)
async def server(ctx):
    all = []
    for guild in client.guilds:
        all.append(guild.id)
    print(all)

@client.command(pass_context = True)
async def rainbowrole(role):
    rgb = [0, 0, 0]
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not client.is_closed():
                try:
                    rgb_gen_v2(rgb)
                    print(rgb, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
                    if(rgb[2] == 255):
                        rgb = [0, 0, 0]
                    await role.edit(color=discord.Colour.from_rgb(rgb[0],rgb[1],rgb[2]))
                except Exception:
                    print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

@client.command(pass_context = True)
async def nick_chang(ctx):
    while not client.is_closed():
        for i in range(len(nicks)):
            await ctx.author.edit(nick= nicks[i])
            await asyncio.sleep(delay)
    

def next_track():
    global disconnect_quiz
    global check_quiz
    global autor_Check
    global name_check
    global quiz_members
    global quiz_ch
    autor_Check = False
    name_check = False

    try:
        voice.stop()
        global list_question
        os.remove("qustions/{}-{}.mp3".format(clear(list_question[0].autor), clear(list_question[0].name)))
        del list_question[0]
        time.sleep(1.5)
        voice.play(discord.FFmpegPCMAudio(list_question[0].file), after = check_queue)
    except Exception:
        if(len(list_question) == 0):
            print('[log] игра оконченна')
            check_quiz = False
            disconnect_quiz = True

def check_queue(x):
    global disconnect_quiz
    global check_quiz
    global list_question
    global autor_Check
    global name_check
    global quiz_members
    global quiz_ch
    autor_Check = False
    name_check = False
    
    try:
        if(voice.is_playing() == False and len(list_question) > 0):
            if(str(x) != 'abc'):
                os.remove("qustions/{}-{}.mp3".format(clear(list_question[0].autor), clear(list_question[0].name)))
                del list_question[0]
                time.sleep(1.5)
        voice.play(discord.FFmpegPCMAudio(list_question[0].file), after = check_queue)
    except Exception:
        if(len(list_question) == 0):
            print('[log] игра оконченна')
            check_quiz = False
            disconnect_quiz = True
            
async def dis():
    try:
        global quiz_ch
        global voice
        global check_quiz
        global quiz_members
        if(voice.is_connected() == True and voice.is_playing() == False):
            embed1=discord.Embed(title="Результаты музыкальньного поединка",  description="Поздравляем победителей!!!", color=0x33c14b)
            embed1.set_author(name="YoboBobo")
            quiz_members.sort(key=operator.attrgetter('score'))
            quiz_members.reverse()
            await voice.disconnect()
            for i in range(len(quiz_members)):
                member_quiz = discord.utils.find(lambda r: r.id == quiz_members[i].id, quiz_ch.guild.members)
                embed1.add_field(name=f"{member_quiz.nick}", value=f"{quiz_members[i].score}", inline=False)
                #await quiz_ch.send(f'{member_quiz.mention} - {quiz_members[i].score}')
            await quiz_ch.send(embed=embed1)
    except Exception as e:
        tb = traceback.format_exc()
        await quiz_ch.send(f'{e}')
        await quiz_ch.send(f'{tb}')

@client.command(pass_context = True)
async def create_teams(ctx):
    red_team = discord.Embed(
    title = 'Красная команда',
    colour = discord.Colour.from_rgb(255,0,0)
    )
    red_team.set_author(name = 'Распределение по командам')
    blue_team = discord.Embed(
        title = 'Синяя команда',
        colour = discord.Colour.from_rgb(0,0,255)
        )
    blue_team.set_author(name = 'Распределение по командам')

    all = []
    rTeam =[]
    bTeam = []
    print('[log]ищу людей')
    for member in ctx.guild.members:
        if(member.voice != None):
            all.append(member.id)

    for i in range(len(all)):
        x = random.choice(all)
        all.remove(x)
        if x not in rTeam and len(rTeam) <= len(all):
            rTeam.append(x)
        else:
            bTeam.append(x)
                
    print(f'До изменения{all}\n')
    random.shuffle(all)
    print(all)
    print(f'Красная команда: {rTeam}')
    print(f'Синяя команда: {bTeam}')

    try:
        channel = discord.utils.get(ctx.guild.channels, name='rTeam')
        await channel.clone(name='temp')
    except AttributeError:
        for channel in ctx.guild.channels:
            if(str(channel.type) == 'voice'):
                ch = discord.utils.get(ctx.guild.channels, name=channel.name)
                await ch.clone(name='rTeam')
                await ch.clone(name='bTeam')
                break
    else:
        print('[log]каналы уже созданы')
        channel = discord.utils.get(ctx.guild.channels, name='temp')
        await channel.delete(reason='None')

    for i in range(len(rTeam)):
        channel = discord.utils.get(ctx.guild.channels, name='rTeam')
        member = discord.utils.find(lambda r: r.id == rTeam[i], ctx.guild.members)
        await member.move_to(channel)
        await ctx.channel.send(f'{member.mention}', embed = red_team)
    for i in range(len(bTeam)):
        channel = discord.utils.get(ctx.guild.channels, name='bTeam')
        member = discord.utils.find(lambda r: r.id == bTeam[i], ctx.guild.members)
        await member.move_to(channel)
        await ctx.channel.send(f'{member.mention}', embed = blue_team) 

@client.command(pass_context = True)
async def die(ctx):   
    await ctx.channel.send(file=discord.File('my_file.gif'))
    global voice
    channel_voice = ctx.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel_voice)
    else:
        voice = await channel_voice.connect()
        voice.play(discord.FFmpegPCMAudio('song.mp3'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.7
    time.sleep(20)
    await ctx.delete()
    await voice.disconnect()

@client.command(pass_context = True)
async def alarm(ctx, member: discord.Member):      
    try:
        if(member.voice.self_mute == True):
            default_channel = member.voice.channel
            if(member.voice != None): 
                try:
                    channel = discord.utils.get(ctx.guild.channels, name='Alarm1')
                    await channel.clone(name='temp')
                except AttributeError:
                    await ctx.guild.create_voice_channel('Alarm1')
                    await ctx.guild.create_voice_channel('Alarm2')
                    print('[log]каналы уже созданы')
            else:
                channel = discord.utils.get(ctx.guild.channels, name='temp')
                await channel.delete(reason='None')
            while member.voice.self_mute:
                channel = discord.utils.get(ctx.guild.channels, name='Alarm1')
                await member.move_to(channel)
                await asyncio.sleep(0.5)
                channel = discord.utils.get(ctx.guild.channels, name='Alarm2')
                await member.move_to(channel)
                await asyncio.sleep(0.5)
            if(member.voice.self_mute != True):
                await member.move_to(default_channel)
                await ctx.channel.send(f'{member.mention} Доброе утро!')
                await asyncio.sleep(3)
                channel = discord.utils.get(ctx.guild.channels, name='Alarm1')
                await channel.delete(reason='None')
                channel = discord.utils.get(ctx.guild.channels, name='Alarm2')
                await channel.delete(reason='None') 
            else:
                await ctx.channel.send(f'У {member.mention} подключен голос')
    except Exception as e:
        tb = traceback.format_exc()
        await ctx.channel.send(f'{e}')
        await ctx.channel.send(f'{tb}')
        try:
            print('User не подключен')
            channel = discord.utils.get(ctx.guild.channels, name='Alarm1')
            await channel.delete(reason='None')
            channel = discord.utils.get(ctx.guild.channels, name='Alarm2')
            await channel.delete(reason='None')
        except Exception as e:
            tb = traceback.format_exc()
            await ctx.channel.send(f'{e}')
            await ctx.channel.send(f'{tb}')
            print('каналы не созданны')

@client.command(pass_context = True)
async def move(ctx):
    members = await ctx.guild.fetch_members(limit=None).flatten()
    for Member in members:
        if(Member.voice != None): 
            await Member.move_to(ctx.author.voice.channel)

@client.command(pass_context = True)
async def fr(ctx, message):
    global voice
    ch = message
    ch = ch.replace("r!fr ", "")
    translator = Translator()
    result = translator.translate(text = ch, dest='fr')
    song_def = os.path.isfile('songs/def_text.mp3')
    song_there = os.path.isfile('songs/fr_text.mp3')

    try:
        if song_there:
            os.remove('songs/fr_text.mp3')
            os.remove('songs/def_text.mp3')
    except PermissionError:
        print('[log] Не удалось удалить файл')
            
    tts_def = gTTS(text=ch, lang='ru')
    tts_def.save('songs/def_text.mp3')
    tts = gTTS(text=str(result.text), lang='fr')
    tts.save('songs/fr_text.mp3')

    channel_voice = ctx.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel_voice)
    else:
        if voice and voice.is_connected():
            print('[log] voice connected')
        else:
            try:
                voice = await channel_voice.connect()
            except discord.ClientException as e:
                print(e)
            else:
                voice.play(discord.FFmpegPCMAudio('songs/def_text.mp3'), after = lambda e: voice.play(discord.FFmpegPCMAudio('songs/fr_text.mp3'), after = lambda e: voice.play(discord.FFmpegPCMAudio('songs/fr_song.mp3'))))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.7
                        
                await voice.disconnect()
    
async def check_queue(x):
    global disconnect_quiz
    global check_quiz
    global list_question
    global autor_Check
    global name_check
    global quiz_members
    global quiz_ch
    autor_Check = False
    name_check = False
    
    try:
        while(voice.is_playing()):
            await asyncio.sleep(0.5)
        if(voice.is_playing() == False and len(list_question) > 0):
            if(str(x) != 'abc'):
                loop = ass.get_event_loop()
                embed=discord.Embed(title="Название трека:", description=f"{list_question[0].autor}-{list_question[0].name}", color=0x100ce9)
                embed.set_author(name="YoboBobo")
                embed.set_thumbnail(url="https://cs6.pikabu.ru/post_img/big/2014/06/26/7/1403778383_1086897993.jpg")
                await quiz_ch.send(embed=embed)
                await loop.run_in_executor(None, lambda e: os.remove("qustions/{}-{}.mp3".format(clear(list_question[0].autor), clear(list_question[0].name))), None)
                del list_question[0]
                await asyncio.sleep(1.5)
        print(f"{list_question[0].autor} {list_question[0].name}")
        voice.play(discord.FFmpegPCMAudio(list_question[0].file))
        while(voice.is_playing()):
            await asyncio.sleep(0.5)
        await check_queue('a')
    except Exception:
        if(len(list_question) == 0):
            print('[log] игра оконченна')
            check_quiz = False
            disconnect_quiz = True
            try:
                if(voice.is_connected() == True and voice.is_playing() == False):
                    embed1=discord.Embed(title="Результаты музыкальньного поединка",  description="Поздравляем участников", color=0x33c14b)
                    embed1.set_author(name="YoboBobo")
                    embed1.set_thumbnail(url="https://avatars.mds.yandex.net/get-pdb/1689173/ea82b6e5-6276-473f-b381-90d30c66f23b/s1200?webp=false")
                    quiz_members.sort(key=operator.attrgetter('score'))
                    quiz_members.reverse()
                    await voice.disconnect()
                    for i in range(len(quiz_members)):
                        member_quiz = discord.utils.find(lambda r: r.id == quiz_members[i].id, quiz_ch.guild.members)
                        embed1.add_field(name=f"{member_quiz.nick}", value=f"{quiz_members[i].score}", inline=False)
                await quiz_ch.send(embed=embed1)
            except Exception as e:
                tb = traceback.format_exc()
                await quiz_ch.send(f'{e}')
                await quiz_ch.send(f'{tb}')

@client.event
async def on_message(message):
    try:
        global disconnect_quiz
        global check_quiz
        global list_question
        global quiz_channel
        global voice
        global quiz_started
        global quiz_members
        global autor_Check
        global name_check
        global quiz_ch
        global delite_start
        
        if(message.author.bot):
            return


        if(disconnect_quiz == True):
            disconnect_quiz = False
            list_question.clear()
            quiz_members.clear()
            quiz_started = False

        elif(message.content == 'r!quiz'):
            await message.channel.send('Музыкальный поединок начинается')

            login = '79994461067'  
            password = 'Slololoshka123'

            quiz_ch = message.channel
            channel_voice = message.author.voice.channel
            voice = get(client.voice_clients, guild = message.guild)
            
            if(not quiz_started):
                quiz_started = True
                vk_session = vk_api.VkApi(login=login, password=password)
                vk_session.auth()
                audio_obj = audio(vk_session)
                print('[log] загрзука начата')
                x = []
                a = 0
                map_audio_object = audio_obj.get(need_list=True)
                while len(x) < 3:
                    b = random.randint(0, len(map_audio_object))
                    c = random.randint(0, len(map_audio_object))
                    if(b > c):
                        p = random.randint(c, b)
                        o = random.randint(c, b)
                        if(p > o):
                            a = random.randint(o, p)
                        else:
                            a = random.randint(p, o)
                    else:
                        p = random.randint(b, c)
                        o = random.randint(b, c)
                        if(p > o):
                            a = random.randint(o, p)
                        else:
                            a = random.randint(p, o)
                    if(a not in x):
                        x.append(a)
                        list_question.append(question("qustions/{}-{}.mp3".format(clear(map_audio_object[a].title), clear(map_audio_object[a].artist)), clear(map_audio_object[a].title), clear(map_audio_object[a].artist)))
                        urllib.request.urlretrieve(map_audio_object[a].url, "qustions/{}-{}.mp3".format(clear(map_audio_object[a].title), clear(map_audio_object[a].artist)))
                        sound = AudioSegment.from_mp3("qustions/{}-{}.mp3".format(clear(map_audio_object[a].title), clear(map_audio_object[a].artist)))
                        startpoint = random.randint(10000, len(sound) - 50000)
                        sound[startpoint: startpoint + 30000].export("qustions/{}-{}.mp3".format(clear(map_audio_object[a].title), clear(map_audio_object[a].artist)))
                print('[log] загрузка закончена')
                
                quiz_channel = str(message.channel)
                if voice and voice.is_connected():
                    await voice.move_to(channel_voice)
                else:
                    voice = await channel_voice.connect()
                check_quiz = True
                await message.channel.send('Поехали!')
                voice.play(discord.FFmpegPCMAudio('songs/start_quiz.mp3'), after = lambda e: check_queue('abc'))
            else:
                await message.channel.send('Поединок уже начался')
    


        #quiz
        elif(check_quiz == True):
            if(quiz_channel == str(message.channel)):
                if(message.content.lower() == 'r!quiz'):
                    return
                if('-' in message.content.lower()):
                    a = list(message.content.lower().split('-'))
                    if(a[0].lower() == list_question[0].autor.lower() and a[1].lower() == list_question[0].name.lower() and autor_Check == False and name_check == False):
                        await message.add_reaction('✅')
                        print('1')
                        name_check = True
                        autor_Check = True
                        if(len(quiz_members) == 0):
                            quiz_members.append(member_quiz(message.author.id, 2))   
                            await message.channel.send(f'{message.author.mention} Правильно +2 очка')
                        else:
                            count = 0
                            for i in range(len(quiz_members)):
                                if(not (message.author.id == quiz_members[i].id)):
                                    count += 1
                                else:
                                    quiz_members[i].score += 2  
                                    await message.channel.send(f'{message.author.mention} Правильно +2 очка')
                                    break
                            if(count == len(quiz_members)):
                                quiz_members.append(member_quiz(message.author.id, 2))   
                                await message.channel.send(f'{message.author.mention} Правильно +2 очка')
                        await next_track()
                    elif(a[0].lower() == list_question[0].autor.lower() and a[1].lower() == list_question[0].name.lower() and autor_Check == True and name_check == False):
                        await message.add_reaction('✅')
                        print('2')
                        name_check = True
                        autor_Check = True
                        if(len(quiz_members) == 0):
                            quiz_members.append(member_quiz(message.author.id, 1))   
                            await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                        else:
                            count = 0
                            for i in range(len(quiz_members)):
                                if(not (message.author.id == quiz_members[i].id)):
                                    count += 1
                                else:
                                    quiz_members[i].score += 1  
                                    await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                                    break
                            if(count == len(quiz_members)):
                                quiz_members.append(member_quiz(message.author.id, 1))   
                                await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                        await next_track()
                    elif(a[0].lower() == list_question[0].autor.lower() and a[1].lower() == list_question[0].name.lower() and autor_Check == False and name_check == True):
                        await message.add_reaction('✅')
                        print('3')
                        name_check = True
                        autor_Check = True
                        if(len(quiz_members) == 0):
                            quiz_members.append(member_quiz(message.author.id, 1))   
                            await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                        else:
                            count = 0
                            for i in range(len(quiz_members)):
                                if(not (message.author.id == quiz_members[i].id)):
                                    count += 1
                                else:
                                    quiz_members[i].score += 1  
                                    await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                                    break
                            if(count == len(quiz_members)):
                                quiz_members.append(member_quiz(message.author.id, 1))   
                                await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                        await next_track()
                    else:
                        await message.add_reaction('❌')
                elif((message.content.lower() == list_question[0].autor.lower() and autor_Check == False) or (len(message.content) > 7 and message.content.lower() in list_question[0].autor.lower() and autor_Check == False)):
                        await message.add_reaction('✅')
                        print('4')
                        autor_Check = True
                        if(name_check == True):
                            await next_track()
                        if(len(quiz_members) == 0):
                            quiz_members.append(member_quiz(message.author.id, 1))   
                            await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                        else:
                            count = 0
                            for i in range(len(quiz_members)):
                                if(not (message.author.id == quiz_members[i].id)):
                                    count += 1
                                else: 
                                    quiz_members[i].score += 1  
                                    await message.channel.send(f'{message.author.mention} Правильно +1 очко') 
                                    break
                            if(count == len(quiz_members)):
                                quiz_members.append(member_quiz(message.author.id, 1))   
                                await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                elif((message.content.lower() == list_question[0].name.lower() and name_check == False) or (len(message.content) > 7 and message.content.lower() in list_question[0].name.lower() and name_check == False)):
                        await message.add_reaction('✅')
                        print('5')
                        name_check = True
                        if(autor_Check == True):
                            await next_track()
                        if(len(quiz_members) == 0):
                            quiz_members.append(member_quiz(message.author.id, 1))   
                            await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                        else:
                            count = 0
                            for i in range(len(quiz_members)):
                                if(not (message.author.id == quiz_members[i].id)):
                                    count += 1
                                else:
                                    quiz_members[i].score += 1  
                                    await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                                    break
                            if(count == len(quiz_members)):
                                quiz_members.append(member_quiz(message.author.id, 1))   
                                await message.channel.send(f'{message.author.mention} Правильно +1 очко')
                else:
                    await message.add_reaction('❌')
    except Exception as e:
        tb = traceback.format_exc()
        await message.channel.send(f'{e}')
        await message.channel.send(f'{tb}')
    await client.process_commands(message)

client.run(Token)

