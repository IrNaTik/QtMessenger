import os


# while True:
dir_arr =  os.listdir("Chats")
last_messages = {}

for direct in dir_arr:
	with open(f'Chats/{direct}', 'r') as f:
		for line in f:
			pass

		last_messages[direct] = line



while True:
	dir_arr =  os.listdir("Chats")

	for direct in dir_arr:


		with open(f'Chats/{direct}', 'r') as f:
			for line in f:
				pass

			if direct not in last_messages.keys():
				last_messages[direct] = line
				line_2 = line.strip()
				line_2 = line_2.split(';')

				direct_2 = f'Chats_changes/chat_{line_2[-2]}_{line_2[-1]}.txt'
				with open(direct_2, 'a+') as f:
					f.write(line)
			else:

				if line != last_messages[direct]:

					# Регистрация изменений
					# В первую очередь через файлы
					line_2 = line.strip()
					line_2 = line_2.split(';')
					direct_2 = f'Chats_changes/chat_{line_2[-2]}_{line_2[-1]}.txt'
					with open(direct_2, 'a+') as f:
						f.write(line)

					last_messages[direct] = line






