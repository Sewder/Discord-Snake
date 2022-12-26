import discord
import responses
import gameobjects

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
        else:
            await message.channel.send("Boyle bir islemim yoktur lutfen !help yaziniz")
    except Exception as e:
        print(e)
async def send_images(message,user_message):
    try:
        
        response =responses.file(user_message.lower())
        if response:
            await message.channel.send(file=discord.File(response))
        else:
            await message.channel.send("Dosya yok")
    except Exception as e:
        print(e)



def run_discord_bot():
    TOKEN = 'MTA1MjIxMTM3MDIwNjE3NTMwMg.G4u8rY.RCGRAGN7giE8HEzEjLLCLA9Ar4zv1gjZ-XcaFQ'  
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        splitted_message= user_message.split()
        if splitted_message[0].lower()=="image":
            user_message= splitted_message[1]
            await send_images(message,user_message)
                
        elif splitted_message[0].lower()=='!play':
            snake= gameobjects.Snake()
            
            wrong_direction=False
            def check(m):
                return m.author == message.author and m.channel == message.channel
            while True:
                snake.draw_snake()
                snake.apple.draw_apple()
                await message.channel.send(snake.map.draw_map())
                embed = discord.Embed(color=discord.Color.red())
                embed.title = f"🐍 Nereye gideceksin? 🎮 Skorun: 🍎{snake.apple.print_score()} 🎮"
                if wrong_direction:
                    await message.channel.send('😎😎😎sadece w a s d argümanlrini alir😎😎😎')
                    await message.channel.send(embed=embed)
                    move = await client.wait_for('message', check=check)
                    wrong_direction=False
                else:
                    await message.channel.send(embed=embed)
                    move = await client.wait_for('message', check=check)
                if move.content == 'q':
                    break
                if not move.content in ['w','a','s','d'] :
                    wrong_direction = True
                    continue
                result = snake.move(move.content)
                if not result:
                    if snake.deadly_eaten:
                        embed_deadly= discord.Embed(color=discord.Color.dark_blue())
                        embed_deadly.title= "**SADECE ELMALARI YE**"
                        await message.channel.send(embed=embed_deadly)
                    embed_game_over=discord.Embed(color=discord.Color.dark_orange())
                    embed_game_over.title= f'**Skorunuz:** {snake.apple.print_score()} \n*Devam etmek istiyor musunuz? Eğer istiyorsanız `r` yazın*'
                    await message.channel.send(embed=embed_game_over)
                    d = await client.wait_for('message', check=check)
                    if d.content == 'r':
                        snake = gameobjects.Snake()
                    else:
                        await message.channel.send('🎉🎉🎉🎉Tesekkürler🎉🎉🎉🎉')
                        break
                    
                   
        if splitted_message[0]=='message':
            try:
                user_message=splitted_message[1]
                if user_message[0] == '?':
                    user_message = user_message[1:]
                    await send_message(message, user_message, is_private=True)
                else:
                    await send_message(message, user_message, is_private=False)

            except:
                await message.channel.send(" Lütfen messagein yanina komutu girin")
                
            

    client.run(TOKEN)