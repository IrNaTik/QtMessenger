from PIL import Image
import sys
import os

from constants import AVATAR_SIZE_BIG, AVATAR_SIZE_SMALL


def photo_reduction(img):
	img = img.resize(AVATAR_SIZE_BIG, Image.ANTIALIAS)

	return img



		

def cropping(file_path):
	img = Image.open(file_path).convert('RGB')
	width, height = img.size

	# Мы обрезаем в квадрат
	if width > height:
		buf = int((width - height) / 2)
		new_img = img.crop((buf, 0, width - buf, height))
	elif height > width:
		buf = int((height - width) / 2)
		new_img = img.crop((0, buf, width, height - buf))
	else:
		new_img = img


	dir_arr =  os.listdir("Images")

	# В Images хранятся аватарки всех юзеров, которым писал сообщения
	# my_avatar.png это автар юзера
	if 'my_avatar.png' in dir_arr:
		os.remove("Images/my_avatar.png")

	new_img = photo_reduction(new_img)

	new_img.save('Images/my_avatar.png', quality=100) 


def photo_reduction_to_small(file_path, login):
	img = Image.open(file_path).convert('RGB')
	img = img.resize(AVATAR_SIZE_SMALL, Image.ANTIALIAS)
	img.save(f'Images/avatar_small_{login}.png', quality=100) 
	


	







