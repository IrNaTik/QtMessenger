import aiohttp
import asyncio

from PIL import Image


async def get_avatar_by_login(login):
	async with aiohttp.ClientSession() as session:
		try:
			headers = {'login': login}
			async with session.get('http://127.0.0.1:8000/get_photo', headers = headers) as resp:
				

				
				reader = resp.content
				
				
				# объект класса StreamReader(он слишком большой и память не успевает выделится)
				# поэтому читаем по кускам
				empty_bytes = b''
				result = empty_bytes

				while True:
				    chunk = await reader.read(8)

				    if chunk == empty_bytes:
				        return result

				    result += chunk

		except:

			return False


async def check_chat_existing(login_1, login_2):
	async with aiohttp.ClientSession() as session:
		try:
			headers = {'login_1': login_1, 'login_2': login_2}
			async with session.get('http://127.0.0.1:8000/get_chat_excisting', headers = headers) as resp:
				

				result = await resp.json()
				
				return result['result']
				

		except:

			return False


# login_getter будет логином юзера, который сейчас в мессенджере
async def get_last_messages(login_getter):
	async with aiohttp.ClientSession() as session:
		try:
			headers = {'login_getter': login_getter}
			async with session.get('http://127.0.0.1:8000/get_last_messages', headers = headers) as resp:
				

				result = await resp.json()

				if result != {}:
					print(result)
				return result
				

		except:

			return False


async def get_users_of_chats(my_login):
	async with aiohttp.ClientSession() as session:
		try:
			headers = {'login': my_login}
			async with session.get('http://127.0.0.1:8000/get_chat_list', headers = headers) as resp:
				

				result = await resp.json()
				
				return result['users']
				

		except:

			return False



async def get_user_chats(my_login, user):
	async with aiohttp.ClientSession() as session:
		try:
			headers = {'login_1': my_login, 'login_2': user}
			async with session.get('http://127.0.0.1:8000/get_chats', headers = headers) as resp:
				
				reader = resp.content
			
				empty_bytes = b''
				result = empty_bytes

				while True:
				    chunk = await reader.read(8)

				    if chunk == empty_bytes:
				        return result

				    result += chunk
				

		except:

			return False




