import requests

url = "https://api.telegram.org/bot<831584493:AAGk8-v3jAD6ihqa7Rb3JiONwR_EWj0_PdA>/"
def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()
def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
        sleep(1)       
if __name__ == '__main__':  
    main()
def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()
greet_bot = BotHandler(token)  
greetings ='G-day'
now = datetime.datetime.now()
def main():  
    new_offset = None
    today = now.day
    hour = now.hour
    while True:
        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good morning, {}'.format(last_chat_name))
            today += 1
        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'G-day, {}'.format(last_chat_name))
            today += 1
        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good evening, {}'.format(last_chat_name))
            today += 1
        new_offset = last_update_id + 1
if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()