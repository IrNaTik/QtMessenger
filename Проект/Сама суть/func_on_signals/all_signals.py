from PyQt5 import QtCore, QtGui, QtWidgets
import asyncio
from PIL import Image
import io
import os

from datetime import datetime 




from my_requests import post_requests, get_requests
from work_with_photo import cropping, photo_reduction_to_small
def search_users(self):
        login_chunk = self.lineEdit.text()

        # 17 это максимальная длина логина 
        if login_chunk != '' and len(login_chunk) < 17:

                # Очистка
                self.user_search_list_to_back()

                # Получение списка логинов после запроса
                result = asyncio.run(post_requests.make_request_of_searching(login_chunk)) 
                
                
                # Оформление и вывод этого списка
                if result != False:
                        self.show_list(result)
                else:
                        self.show_list(['интернет -'])
        elif login_chunk == '':
                self.list_to_back()
                
        
def post_avatar(self):
        
        response = QtWidgets.QFileDialog.getOpenFileNames(self.centralwidget, 'Open file', '/', 'Image files (*.jpg *.png)')
        cropping(response[0][0])

        with open('Images/my_avatar.png', 'rb') as file:
                files = {'file': file}

                # Пока так, типо для тестов
                login = self.lineEdit.text()
                
                
                response = asyncio.run(post_requests.make_request_photo(files, login)) 
                

def get_avatar(self):

        login = self.lineEdit.text()
        response = asyncio.run(post_requests.check_user(login)) 

        self.textBrowser_2.setText(response)
        if response == 'good':
                data = asyncio.run(get_requests.get_avatar_by_login(login)) 
                

                if data == False:
                        print('Ошибка в get_avatar')
                else:
                        


                        image = Image.open(io.BytesIO(data))
                        image.save(f'Images/avatar_{login}.png', quality=100)
                        photo_reduction_to_small(f'Images/avatar_{login}.png', login)

                        self.label_5.setPixmap(QtGui.QPixmap(f'Images/avatar_small_{login}.png'))


# i - это индекс кнопки в массиве по которой нажали 
def show_chat_with_person(self, i, my_login):

        # Очищаем чат
        clearning_of_chat(self.users_messages_to_delete)
        self.users_messages_to_delete = []     

        login = self.user_search_list[i].text()

        response = asyncio.run(post_requests.check_user(login)) 
        print(response)
        if response == 'no_avatar':
                self.label_5.setPixmap(QtGui.QPixmap("Images/no_avatar.png"))
                self.label_6.setText(login)
        elif response == 'good':
                data = asyncio.run(get_requests.get_avatar_by_login(login)) 
                

                if data == False:
                        print('Ошибка в show_chat_with_person')
                else:
                        

                        image = Image.open(io.BytesIO(data))
                        image.save(f'Images/avatar_{login}.png', quality=100)
                        photo_reduction_to_small(f'Images/avatar_{login}.png', login)

                        self.label_5.setPixmap(QtGui.QPixmap(f'Images/avatar_small_{login}.png'))
                        self.label_6.setText(login)

        print('Has changed')
        self.pushButton_4.setGeometry(QtCore.QRect(880, 730, 93, 51))
        self.frame_5.setGeometry(QtCore.QRect(440, 0, 521, 80))
        self.textMessage.setGeometry(QtCore.QRect(420, 730, 451, 51))
        self.scrollArea_3.setGeometry(QtCore.QRect(380, 130, 651, 591))

        print(self.frame_5.geometry())
        # self.scrollArea_3.setGeometry(QtCore.QRect(380, 130, 271, 311))

        response = asyncio.run(get_requests.check_chat_existing(login, my_login)) 

        if response == 'Yes':
                # Здесь подразумевается, что их чат существует

                dir_arr = os.listdir(f'Chats_{my_login}')
                if f'chat_{my_login}_{login}.txt' in dir_arr:
                        direct = f'Chats_{my_login}/chat_{my_login}_{login}.txt'
                else:
                        direct = f'Chats_{my_login}/chat_{login}_{my_login}.txt'

                with open(direct, 'r') as file:
                        for line in file.readlines():

                                # В сообщении не должно быть ;
                                line = line.strip()
                                line = line.split(';') 
                                message = line[0]
                                print(message)

                               

                                if my_login == line[-1]:
                                        print('getter')
                                        condition = "getter"
                                else:
                                        print('sender')
                                        condition = 'sender'

                                show_message(self, message, condition)

                                self.verticalLayout_4.addWidget(self.label)
        elif response == 'No':

                # Создать пустую переписку(просто вывести, как в тг делается)
                # Суть в том, что через этот запрос мы создаём текстовый файл на сервере с перепиской этих двух пользователей

                # a+ то, что нам нужно
                pass



def clearning_of_chat(objects):
        for obj in objects:
                obj.deleteLater()



# i - это индекс кнопки в массиве по которой нажали 
def show_chat_with_user(self, key, my_login):

        # Очищаем чат
        clearning_of_chat(self.users_messages_to_delete)
        self.users_messages_to_delete = []      

        login = key.text()

        response = asyncio.run(post_requests.check_user(login)) 
        print(response)
        if response == 'no_avatar':
                self.label_5.setPixmap(QtGui.QPixmap("Images/no_avatar.png"))
                self.label_6.setText(login)
        elif response == 'good':
                data = asyncio.run(get_requests.get_avatar_by_login(login)) 
                

                if data == False:
                        print('Ошибка в show_chat_with_person')
                else:
                        

                        image = Image.open(io.BytesIO(data))
                        image.save(f'Images/avatar_{login}.png', quality=100)
                        photo_reduction_to_small(f'Images/avatar_{login}.png', login)

                        self.label_5.setPixmap(QtGui.QPixmap(f'Images/avatar_small_{login}.png'))
                        self.label_6.setText(login)

        print('Has changed')
        self.pushButton_4.setGeometry(QtCore.QRect(880, 730, 93, 51))
        self.frame_5.setGeometry(QtCore.QRect(440, 0, 521, 80))
        self.textMessage.setGeometry(QtCore.QRect(420, 730, 451, 51))
        self.scrollArea_3.setGeometry(QtCore.QRect(380, 130, 651, 591))

        print(self.frame_5.geometry())
        # self.scrollArea_3.setGeometry(QtCore.QRect(380, 130, 271, 311))

        response = asyncio.run(get_requests.check_chat_existing(login, my_login)) 

        print(response)
        if response == 'Yes':
                # Здесь подразумевается, что их чат существует

                dir_arr = os.listdir(f'Chats_{my_login}')
                if f'chat_{my_login}_{login}.txt' in dir_arr:
                        direct = f'Chats_{my_login}/chat_{my_login}_{login}.txt'
                else:
                        direct = f'Chats_{my_login}/chat_{login}_{my_login}.txt'

                with open(direct, 'r') as file:
                        for line in file.readlines():

                                # В сообщении не должно быть ;
                                line = line.strip()
                                line = line.split(';') 
                                message = line[0]
                                print(message)

                               

                                if my_login == line[-1]:
                                        print('getter')
                                        condition = "getter"
                                else:
                                        print('sender')
                                        condition = 'sender'

                                show_message(self, message, condition)

                                self.verticalLayout_4.addWidget(self.label)

                                
                        


                # отрпавление запроса на получение всех файлов
                # хз, стоит ли это прописывать, нужно продумать обновление чатов
                # причём это должно происходить динмически
        elif response == 'No':

                # Создать пустую переписку(просто вывести, как в тг делается)
                # Суть в том, что через этот запрос мы создаём текстовый файл на сервере с перепиской этих двух пользователей

                # a+ то, что нам нужно
                pass                


def show_message(self, message, condition):
        
               
        self.label = QtWidgets.QLabel()
        # self.label.setGeometry(0, 0, 100, 60)



        if  condition == 'getter':
                color = "rgb(80, 80, 122)"
                margin = "0px"
        elif condition == 'sender':
                color = "rgb(189, 210, 255)"
                margin = "100px"
       
        self.label.setStyleSheet(f"background-color: {color};\n"
                                 f"margin-left: {margin};\n"
                                 "font-size: 20px;\n"
                                 "padding-left: 10px;\n"
                                 "padding-top: 10px;\n"
                                 "padding-bottom: 10px;\n"
                                 "border-radius: 10px;")
        self.label.setText(message)
        self.label.setObjectName("label")
        self.label.setWordWrap(True)


        self.users_messages_to_delete.append(self.label)

        y = self.frame_6.geometry().y()
        self.frame_6.move(0, y - 50)

        self.scrollArea_3.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

        self.verticalLayout_4.addWidget(self.label)


def send_message(self, my_login):
        # В первую очередь отображаем у себя в аккаунте и в файлах переписок у себя локально на компе( чтобы потом перслать)
        # В случае обрыва интернета

        # Берём из шапки
        login = self.label_6.text()

        message =  self.textMessage.toPlainText()



        condition = 'sender'
        show_message(self, message, condition)


        

        now = datetime.now() 
        current_time = now.strftime("%H:%M")  
        # date_today = datetime.date.today()
        # year = date_today.year
        # month = date_today.month
        # day = date_today.day

        dir_arr = os.listdir(f'Chats_{my_login}')

        line = ';'.join([message, f'24, 12, 2022', current_time , my_login, login,])

        direct = f'Chats_{my_login}/chat_{login}_{my_login}.txt'
        if f'chat_{my_login}_{login}.txt' in dir_arr:
                direct = f'Chats_{my_login}/chat_{my_login}_{login}.txt'

        with open(direct, 'a+') as file:
                file.write(line + '\n')
        
       
        # login - sender, my_login - getter
        response = asyncio.run(post_requests.post_message(my_login, login, message, current_time, f'24, 12, 2022')) 

        print(response, 'сообщение отправлено')


def message_typing(self):
        text = self.textMessage.toPlainText()

        print(self.textMessage.textCursor().position())


# my_login = login_getter
def make_last_messages_request(self, my_login):
        response = asyncio.run(get_requests.get_last_messages(my_login)) 
        
        for sender in response.keys():

                dir_arr = os.listdir(f'Chats_{my_login}')

                direct = f'Chats_{my_login}/chat_{sender}_{my_login}.txt'
                if f'chat_{my_login}_{sender}.txt' in dir_arr:
                        direct = f'Chats_{my_login}/chat_{my_login}_{sender}.txt'

                with open(direct, 'a+') as file:
                        for line in response[sender]:
                                print(line)
                                file.write(line + '\n')

                                line = line.strip()
                                line = line.split(';')

                                if line[-1] == my_login:
                                        condition = 'getter'
                                else:
                                        condition = 'sender'
                                
                                show_message(self, line[0], condition)


def get_users_of_chats(self, my_login):
        response = asyncio.run(get_requests.get_users_of_chats(my_login)) 

        return response


def get_user_chats(self, my_login, users):

        dir_arr = os.listdir()
        print(dir_arr, 'fdsfdsfdsfdsfsdfdsfdsdfsdfdsfdsf')
        if f'Chats_{my_login}' not in dir_arr:
                print('gooooood')
                os.mkdir(f'Chats_{my_login}')

        dir_arr = os.listdir(f'Chats_{my_login}')
        for user in users:
                response = asyncio.run(get_requests.get_user_chats(my_login, user)) 
                print(type(response))


                # У пользователя на компе будет папка со всеми чатами всех юзеров этого компьютера
                # При чём на первом месте в назавнии всегда будет владелец аккаунта
                # А уже в самих файлах на последнем месте getter, на предпоследнем sender



                if f'chat_{my_login}_{user}.txt' in dir_arr:
                        with open(f'Chats_{my_login}/chat_{my_login}_{user}.txt', 'wb+') as file:
                                file.write(response)

                else:
                        with open(f'Chats_{my_login}/chat_{user}_{my_login}.txt', 'wb+') as file:
                                file.write(response)


        return 'Good'
       



        
                        