from fastapi import FastAPI, Depends, Body, UploadFile, File, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import*
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
import time
from PIL import Image
import os
import json



from search_algo import search_algoritm
import all_functions 

	


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Person_model(BaseModel):
	login: str
	password: str

class Post_result(BaseModel):
	login: str
	cur_score: int

class Search_Users_Model(BaseModel):
	login_chunk: str

class Message_Data(BaseModel):
	message: str
	time: str
	date: str
		

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def send_data(db: Session = Depends(get_db)):

	return FileResponse('Templates/index.html')

@app.get('/css')
def send_data(db: Session = Depends(get_db)):

	return FileResponse('Templates/style.css')

@app.get('/javascript')
def send_data(db: Session = Depends(get_db)):

	return FileResponse('Templates/prototypes.js')


@app.post('/registration')
def registration(data: Person_model,  db: Session = Depends(get_db)):
	
	user = db.query(User).filter(User.login == data.login).first()

	if user == None:
		new_user = User(login = data.login, password = data.password, victories = 0, defeats = 0, online = 1)

		db.add(new_user)
		db.commit()
		status_code = 200
	else:
		status_code = 404

	return JSONResponse(status_code=status_code, content={'message': 'Уже зарегистрирован'})


@app.post('/authorization')
def authorization(data: Person_model,  db: Session = Depends(get_db)):
	
	# Логины всегда уникальны, эта проверка происходит при регистрации
	user = db.query(User).filter(User.login == data.login).first()
	# print(user.login, user.password)
	if user == None:
		status_code = 300 # Допустим такой, просто придумал для различия
		msg = 1
	elif user.password == data.password:
		status_code = 200
		msg = 2
	else:
		status_code = 404
		msg = 3

	return JSONResponse(status_code=status_code, content={'msg': msg})



@app.post('/search_users')
def search_users(data: Search_Users_Model,  db: Session = Depends(get_db)):
	
	# Логины всегда уникальны, эта проверка происходит при регистрации
	users = db.query(User).all()

	# Вызов функции из search_algo.py
	output_logins = search_algoritm(users, data.login_chunk)

	return JSONResponse(status_code=200, content={'users_logins': output_logins})


# Обработка отпрвление своей аватарки
# Фото уже отправляется квадратным и большого размера (дальше делается уменьшенная копия)
@app.post('/post_photo')
def search_users(file: UploadFile = File(...), request: Request = '2', db: Session = Depends(get_db)):

	response = all_functions.post_photo(file, request, db)
	return JSONResponse(content = response)
		


@app.post('/check_user')
def check_user_avatar(data: Request = '2', db: Session = Depends(get_db)):

	response = all_functions.check_user_avatar(data, db)
	return JSONResponse(content = response)


@app.post('/post_message')
def post_message(data: Message_Data, request: Request = '2', db: Session = Depends(get_db)):

	response = all_functions.post_message(request, data, db)
	return JSONResponse(content = response)


@app.get('/get_last_messages')
def get_last_messages(request: Request = '2', db: Session = Depends(get_db)):
	
	response = all_functions.get_last_messages(request, db)
	return JSONResponse(content = response)



@app.get('/get_chat_list')
def get_chat_list(request: Request = '2', db: Session = Depends(get_db)):

	response =  all_functions.get_all_chats_of_user(request, db)
	return JSONResponse(content = response)



@app.get('/get_chats')
def get_chat_list(request: Request = '2', db: Session = Depends(get_db)):

	response =  all_functions.get_chats(request, db)

	# response = директория файла
	return FileResponse(response)



@app.get('/get_some')
def shit():
	return 'Ignat'


















@app.get('/get_photo')
def search_users(request: Request = '2', db: Session = Depends(get_db)):
	login = request.headers.get('login')

	user = db.query(User).filter(User.login == login).first()
	dir_arr =  os.listdir("Avatars")

	if user != None:
		if f'avatar_{user.id}.png' in dir_arr:

			# Нельзя отправлять ничего кроме файла!
			return FileResponse(f"Avatars/avatar_{user.id}.png")




@app.get('/get_chat_excisting')
def search_users(request: Request = '2', db: Session = Depends(get_db)):
	login_1 = request.headers.get('login_1')
	login_2 = request.headers.get('login_2')

	chat = db.query(Chats).filter(or_(and_(Chats.login_1 == login_2, Chats.login_2 == login_1),and_(Chats.login_1 == login_1, Chats.login_2 == login_2))).first()

	if chat != None:
		return JSONResponse(content = {'result': 'Yes'})

	return JSONResponse(content = {'result': 'No'})



	


	


	
	

		

	


