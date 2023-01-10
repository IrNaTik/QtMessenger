
def main_idea(password):
	hash_password = [0]*len(password)

	for i in range(len(password)):
		num = str(bin(ord(password[i])))[2:]
		hash_password[len(password) - i - 1] = num
	return ''.join(hash_password)


