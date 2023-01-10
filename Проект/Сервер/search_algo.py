
# Нахождение логинов, которые начинаются на chunk
def find_sutes(chunk, login):
		if len(chunk) > len(login):
			return 0
		g = 0
		if login.lower().startswith(chunk.lower()):
			g = 1

		return g


# arr_siblings отвечает именно за индексы наиболее подходящих user
def simple_sort(arr):
	arr_sibling = list(range(len(arr)))
	for i in range(len(arr)-1): # До предпоследнего включительно
		min_id = i
		for g in range(i+1, len(arr)): # До последнего включительно
			if arr[g] < arr[min_id]:
				min_id = g
		arr[i], arr[min_id] = arr[min_id], arr[i]
		arr_sibling[i], arr_sibling[min_id] = arr_sibling[min_id], arr_sibling[i]

	if len(arr) < 10:
		g = 0
	else:
		g = len(arr) - 10

	while (g <= len(arr) - 1) and (arr[g] == 0):
		g += 1

	print(arr)
	# Топ 10
	return arr_sibling[g:][::-1]


def search_algoritm(users, login_chunk):
		if len(users) < 10:
			most_sute_id = list(range(len(users)))
		else:
			most_sute_id = list(range(10))


		sute_lets_num = [find_sutes(login_chunk, user.login) for user in users] 
		

		# Для улучшения скорости (просто нам нужно найти 10 лучших)
		# Если длина будет меньше 1000, то всё в любом случае быстро, а вообще лучше подумать как улучшить
		most_sute_id = simple_sort(sute_lets_num)

		output_users = [users[i] for i in most_sute_id]
		output_logins = [user.login for user in output_users]

		return output_logins