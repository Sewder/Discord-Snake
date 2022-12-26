import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"
    if p_message == 'ali':
        print('veli')
def file(message) -> str:
    images=['images\\Ankara.jpg', 'images\\PEPEGA.jpg', 'images\\videoyun.jpg']
    lower_images=['ankara', 'pepega', 'videoyun']
    if message in lower_images:
        return images[lower_images.index(message)]
    
    