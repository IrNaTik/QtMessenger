import os
from database import*
from sqlalchemy import and_, or_

def post_photo(file, request, db):

	login = request.headers.get('login')

	with open('avatar.png','wb+') as f:
		f.write(file.file.read())

	
	# file хранит и автарку и логин
	user = db.query(User).filter(User.login == login).first()
	dir_arr =  os.listdir("Avatars")

	

	if f'avatar_{user.id}.png' in dir_arr:
		os.remove(f"Avatars/avatar_{user.id}.png")
		
	print(type(file.file))
	im = Image.open(file.file)
	if im.mode in ("RGBA", "P"): 
		im = im.convert("RGB")
	im.save(f"Avatars/avatar_{user.id}.png", quality=100) 
	
	return {'message': 'Good'}



def check_user_avatar(data, db):

	users = db.query(User).all()
	users_logins = [user.login for user in users]
	user_login = data.headers.get('login')

	if user_login not in users_logins:
		return {'condition': 'no_user'}
	else:
		dir_arr =  os.listdir("Avatars")

		user = db.query(User).filter(User.login == user_login).first()
		if f'avatar_{user.id}.png' not in dir_arr:
			return {'condition': 'no_avatar'}
		else:
			return {'condition': 'good'}



def post_message(request, data, db):
	login_sender = request.headers.get('login_sender')
	login_getter = request.headers.get('login_getter')

	# Чтобы не было проблем с хранением
	message = data.message.replace('\n', ' ')
	
	time = data.time
	date = data.date

	chat = db.query(Chats).filter(or_(and_(Chats.login_1 == login_sender, Chats.login_2 == login_getter),
									  and_(Chats.login_1 == login_getter, Chats.login_2 == login_sender))).first()

	if chat == None:
		new_chat = Chats(login_1 = login_sender, login_2 = login_getter)
		db.add(new_chat)
		db.commit()

	dir_arr =  os.listdir("Chats")
	direct = ''
	if f'chat_{login_sender}_{login_getter}.txt' in dir_arr:
		print(1)
		direct = f'Chats/chat_{login_sender}_{login_getter}.txt'
	elif f'chat_{login_getter}_{login_sender}.txt' in dir_arr:
		print(2)
		direct = f'Chats/chat_{login_getter}_{login_sender}.txt'
	else:
		print(3)
		direct = f'Chats/chat_{login_sender}_{login_getter}.txt'


	with open(direct, 'a+') as file:
		line = f'{message};{date};{time};{login_sender};{login_getter}'
		file.write(line + '\n')

	return {'condition': 'good'}



def get_last_messages(request, db):
	login_getter = request.headers.get('login_getter')

	new_messages = {}

	dir_arr =  os.listdir("Chats_changes")
	for direct in dir_arr:
		print(direct[:-4], login_getter)
		if direct[:-4].endswith(login_getter):

			# Чтение файла
			with open(f'Chats_changes/{direct}', 'r') as file:
				user_messages = []
				for line in file.readlines():
					line = line.strip().split(';')

					# Стоит ли заканчивать если это не так?
					print(line[-1], login_getter)
					if line[-1] == login_getter:
						user_messages.append(';'.join(line))


			# Очистка
			with open(f'Chats_changes/{direct}', 'w') as file:
				pass

			a = direct.index(login_getter)
			if a == 0:

				left_b = len('chat_') + len(login_getter) + 1
				right_b = len(direct) - len('.txt') + 1

				login_sender = direct[left_b : right_b]
			else:

				left_b = len('chat_')
				right_b = len(direct) - len('.txt') - len(login_getter) - 1

				login_sender = direct[left_b : right_b]


			if user_messages != []:
				new_messages[login_sender] = user_messages
				print(login_sender, user_messages)

	return new_messages



def get_all_chats_of_user(request, db):

	login = request.headers.get('login')

	chats = db.query(Chats).filter(Chats.login_1 == login).all()
	users_1 = [chat.login_2 for chat in chats]

	chats = db.query(Chats).filter(Chats.login_2 == login).all()
	users_2 = [chat.login_1 for chat in chats]

	users = users_1 + users_2

	return {'users': users}



def get_chats(request, db):

	login_1 = request.headers.get('login_1')
	login_2 = request.headers.get('login_2')

	dir_arr =  os.listdir("Chats")
	print(f'chat_{login_1}_{login_2}.txt' in dir_arr, f'chat_{login_2}_{login_1}.txt' in dir_arr)
	if f'chat_{login_1}_{login_2}.txt' in dir_arr:
		direct = f'chat_{login_1}_{login_2}.txt'
	elif f'chat_{login_2}_{login_1}.txt' in dir_arr:
		direct = f'chat_{login_2}_{login_1}.txt'
	else:
		print('Error')
		return 'Error'

	return 'Chats/' + direct




