import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import youtube_dl
import datetime
import requests
from PIL import Image, ImageFont, ImageDraw
import io
import os
import shutil

Bot: Bot = commands.Bot(command_prefix='!')
Bot.remove_command('help')


# Запуск бота
@Bot.event
async def on_ready():
    print("Bot is online")


# Стандартные команда - ответ
@Bot.command(aliases=['Ситх'])
async def Mantra(ctx):
    await ctx.send(':rage:')
    await ctx.send('https://i.pinimg.com/236x/20/38/45/20384517934c35b2af7aad45f08f50ce.jpg')


@Bot.command(aliases=['Джедай'])
async def jedi(ctx):
    await ctx.send('😇')
    await ctx.send('https://pm1.narvii.com/7191/ed27c60e167a6c25a3ed6bfb2e618f241db6522cr1-734-1024v2_hq.jpg')


@Bot.command(aliases=['Серый'])
async def grey(ctx):
    await ctx.send('😐')
    await ctx.send('https://i05.fotocdn.net/s116/05db59ec2cc5e88c/public_pin_l/2632228145.jpg')


# Clear Message
@Bot.command(aliases=['Удали'])
# @commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    await ctx.send(f'66 {author.mention}')


# Kick
@Bot.command(aliases=['Кикни'])
# @commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    await ctx.send(f'Кикнут {member.mention}')


# Ban
@Bot.command(aliases=['Забань'])
# @commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    emb = discord.Embed(title='Ban', description='Вы попали под приказ 66', colour=discord.Color.red())
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    emb.set_author(name=member.name, icon_url=member.avatar_url)
    emb.add_field(name='Ban user', value='Baned user : {}'.format(member.mention))
    await ctx.send(embed=emb)
    await ctx.send(f'ban user {member.mention}')


# Unban
@Bot.command(aliases=['Разбань'])
# @commands.has_permissions(administrator=True)
async def unban(ctx):
    banned_users = await ctx.guild.bans()
    for ban.entry in banned_users:
        user = ban.entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned user {user.mention}')
        return


# Help
@Bot.command(aliases=['Хэлп'])
async def Help(ctx):
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(title='Навигация по командам')
    emb.add_field(name='{}clear'.format('!'), value='Очистка чата')
    emb.add_field(name='{}kick'.format('!'), value='Кикнуть участника')
    emb.add_field(name='{}ban'.format('!'), value='Заблокировать участника')
    emb.add_field(name='{}unban'.format('!'), value='Разблокировать участника')
    emb.add_field(name='{}time'.format('!'), value='Узнать время по МСК')
    emb.add_field(name='{}user_card'.format('!'), value='Посмотреть карточку пользователя')
    emb.add_field(name='{}send_message'.format('/'), value='Отправить сообщение себе в лс')
    emb.add_field(name='{}join'.format('!'), value='Присоединить бота к голосовому чату')
    emb.add_field(name='{}leave'.format('!'), value='Отключение бота от голосового чата')
    emb.add_field(name='{}mute'.format('!'), value='Не даёт пользователю отправлять сообщения в чат')
    emb.add_field(name='{}play'.format('!'), value='Воспроизвести Музыку')
    emb.add_field(name='{}pause'.format('!'), value='Поставить музыку на паузу')
    emb.add_field(name='{}resume'.format('!'), value='Снова проигрывать музыку')
    emb.add_field(name='{}stop'.format('!'), value='Остановить проигрывание музыки')
    emb.add_field(name='{}Mantra'.format('!'), value='Кодекс Ситхов')
    emb.add_field(name='{}jedi'.format('!'), value='Кодекс джедаев')
    emb.add_field(name='{}grey'.format('!'), value='Кодекс Серых джедаев')
    emb.add_field(name='{}queue'.format('!'), value='Добавить музыку в очередь')
    emb.add_field(name='{}msg_to_friend'.format('!'), value='Отправить другу в лс сообщение')
    await ctx.send(embed=emb)


# Красивый вывод времени
@Bot.command(aliases=['Время'])
async def time(ctx):
    emb = discord.Embed(title='Time', colour=discord.Color.green(), url='https://www.timeserver.ru/cities/ru/nizhni-novgorod')
    emb.set_author(name=Bot.user.name, icon_url=Bot.user.avatar_url)
    emb.set_footer(text='Спасибо за использование WopBot!')
    emb.set_thumbnail(url='https://sun9-70.userapi.com/c855528/v855528246/225547/b5UED0PE60I.jpg')

    now_time = datetime.datetime.now()
    emb.add_field(name='time', value='time : {}'.format(now_time))
    await ctx.send(embed=emb)


@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(configure.config['channel'])
    role = discord.utils.get(member.guild.roles, id=YOUR ID)
    await member.add_roles(role)
    await channel.send(embed=discord.Embed(description=f'Пользователь {member.name}, прийсоединился к нам!, color=0x0c0c0c'))


# Голос
@Bot.command(aliases=['вступи'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот присоединился к каналу: {channel}')


# Выход из голоса
@Bot.command(aliases=['покинь'])
async def leave(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        print('Бот покинул голосовой чат!')


# Карточка пользователя
@Bot.command(aliases=['карточка'])
# @commands.has_permissions(administrator=True)
async def user_card(ctx):
    img = Image.new('RGB',  (400, 200), "#232529")
    url = str(ctx.author.avatar_url)[:-10]
    response = requests.get(url, stream=True)
    response = Image.open(io.BytesIO(response.content))
    response = response.convert('RGB')
    response = response.resize((100, 100), Image.ANTIALIAS)

    img.paste(response, (15, 15, 115, 115))
    idraw = ImageDraw.Draw(img)
    wop = ctx.author.name
    tag = ctx.author.discriminator
    headline = ImageFont.truetype('arial.ttf', size=20)
    undertext = ImageFont.truetype('arial.ttf', size=12)

    idraw.text((145, 15), f'{wop}#{tag}', font=headline)
    idraw.text((145, 50), f'ID: {ctx.author.id}', font=undertext)
    img.save('user_card.png')

    await ctx.send(file=discord.File(fp='user_card.png'))


# Отправка сообщения в лс
@Bot.command(aliases=['лс'])
# @commands.has_permissions(administrator=True)
async def send_message(ctx):
    await ctx.author.send('Execute order 66!')
    await ctx.author.send('https://www.youtube.com/watch?v=P0AjA51Q38M')


# Отправка сообщения другу в лс
@Bot.command(aliases=['друг'])
async def mgs_to_friend(ctx, member: discord.Member):
    await member.send(f'{member.name}, Исполнить приказ 66!! {ctx.author.name}')


# mute
@Bot.command(aliases=['мут'])
# @commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, id=YOUR ID2)
    await member.add_roles(mute_role)
    await ctx.send(f'У {member.mention}, ограничение переписки за нарушение правил чата!')


# Проигрывание музыки
@Bot.command(aliases=['сыграй'])
# @commands.has_permissions(administrator=True)
async def play(ctx, url: str):
    def check_queue():
        global Queue_infile
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("Больше нет песен в очереди")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue" + "\\" + first_file))
            if length != 0:
                print("Музыка готова, сыграю в следующей очереди")
                print(f"Музыка еще в очереди: {still_q}")
                global song_there
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("mp.3")
                global file
                shutil.move(song_path, main_location)
                for file in os.lostdir("./"):
                    if file.endswith('mp.3'):
                        os.rename(file, "song.mp3")

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return
        else:
            queues.clear()
            print("Больше нет музыки в очереди")
    global voice
    global name
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Удаление старого музыкального файла")
    except PermissionError:
        print("Пробую удалять музыкальный файл, но она играет")
        await ctx.send("Ошибка: Музыка играет!")
        return

    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Удаляю старую очередь")
            shutil.rmtree(Queue_folder)
    except:
        print("Нет очереди")
    await ctx.send("Получение чего-либо готового")

    voice = get(Bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Загрузка музыки\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Переименовываю файл: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Играет: {nname}")
    print("playing\n")


# Пауза
@Bot.command(aliases=['Останови'])
async def pause(ctx):
    global voice
    voice = get(Bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        print("Музыка на паузе")
        voice.pause()
        await ctx.send("Пауза")
    else:
        print("Музыка не играет чтобы поставить на паузу")
        await ctx.send("Не поставить на паузу")


# Продолжать играть
@Bot.command(aliases=['продолжай'])
async def resume(ctx):
    global voice
    voice = get(Bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_paused():
        print("Продолжаю играть музыку")
        voice.resume()
        await ctx.send("Продолжаю")
    else:
        print("Музыка уже играла")
        await ctx.send("Уже играла")


# Стоп
@Bot.command(aliases=['Стоп'])
async def stop(ctx):
    global voice
    voice = get(Bot.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_playing():
        print("Музыка остановлена")
        voice.stop()
        await ctx.send("Остановка")
    else:
        print("Музыка уже была остановлена или была на паузе")
        await ctx.send("Уже была остановлена")


queues = {}


# Система очереди
@Bot.command(aliases=['q'])
async def queue(ctx, url: str):
    global Queue_infile
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"song .format{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': queue_path + '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Загрузка музыки \n")
        ydl.download([url])
    await ctx.send("Добавляю музыку в очередь")
    print("Музыка добавлена в очередь")

Bot.run('YOUR TOKEN HERE')
