@client.command(pass_context = True)
async def l(message):
    if(message.content == 'r!l'):
        await message.channel.send('Музыкальный поединок начинается')

        global list_question
        login = '79994461067'  
        password = 'Slololoshka123'  

        global quiz_channel
        global voice
        channel_voice = message.author.voice.channel
        voice = get(client.voice_clients, guild = message.guild)
        global quiz_started
        if(not quiz_started):
            vk_session = vk_api.VkApi(login=login, password=password)
            vk_session.auth()
            audio_obj = audio(vk_session)
            print('[log] загрзука начата')
            x = []
            map_audio_object = audio_obj.get(need_list=True)
            while len(x) < 6:
                a = random.randint(0, len(map_audio_object))
                if(a not in x):
                    x.append(a)
                    list_question.append(question("qustions/{}-{}.mp3".format(map_audio_object[a].title, map_audio_object[a].artist), map_audio_object[a].title, map_audio_object[a].artist))
                    urllib.request.urlretrieve(map_audio_object[a].url, "qustions/{}-{}.mp3".format(map_audio_object[a].title, map_audio_object[a].artist))
                    sound = AudioSegment.from_mp3("qustions/{}-{}.mp3".format(map_audio_object[a].title, map_audio_object[a].artist))
                    startpoint = random.randint(10000, len(sound) - 50000)
                    sound[startpoint: startpoint + 30000].export("qustions/{}-{}.mp3".format(map_audio_object[a].title, map_audio_object[a].artist))
            print('[log] загрузка закончена')
            quiz_started = True
            quiz_channel = str(message.channel)
            if voice and voice.is_connected():
                await voice.move_to(channel_voice)
            else:
                voice = await channel_voice.connect()
            voice.play(discord.FFmpegPCMAudio('songs/start_quiz.mp3'), after = lambda e: check_queue('abc'))
        else:
            await message.channel.send('Поединок уже начался')

d
