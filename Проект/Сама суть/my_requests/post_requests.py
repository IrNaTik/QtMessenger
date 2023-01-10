import aiohttp
import asyncio
import requests



# Подбор логинов по введенному кусочку
async def make_request_of_searching(login_chunk):
        async with aiohttp.ClientSession() as session:
                try:
                        async with session.post('http://127.0.0.1:8000/search_users', json = {'login_chunk': login_chunk}) as resp:
                                response = await resp.json()
                                
                                return response['users_logins']
                except:

                        return False


# Отправление аватарки
async def make_request_photo(file, login):
        file = {'file': open('Images/my_avatar.png', 'rb')}
        headers = {'login': login}
                        
        try:
                resp = requests.post(url='http://127.0.0.1:8000/post_photo', files = file, headers = headers)
        except:
                print('Bad')


async def check_user(login):
        async with aiohttp.ClientSession() as session:
                try:
                        headers = {'login': login}
                        async with session.post('http://127.0.0.1:8000/check_user', headers = headers) as resp:
                                response = await resp.json(content_type=None)
                                
                                return response['condition']
                except:

                        return False


async def post_message(login_sender, login_getter, message, time_now, date):
        async with aiohttp.ClientSession() as session:
                try:
                        headers = {'login_sender': login_sender, 
                                   'login_getter': login_getter}

                        data = {'message': message,
                                'time': time_now,
                                'date': date}

                        async with session.post('http://127.0.0.1:8000/post_message',  json = data, headers = headers) as resp:
                                response = await resp.json(content_type=None)
                                
                                return response['condition']
                except:

                        return False
         