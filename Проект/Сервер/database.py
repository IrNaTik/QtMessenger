from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  Column, Integer, String
 

 
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app_2.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
 
 
Base = declarative_base()
class User(Base):
    __tablename__ = "Users"
 
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
    victories = Column(Integer)
    defeats = Column(Integer)

    # online - 1, offline - 0
    online = Column(Integer) 

class Chats(Base):
    __tablename__ = "Chats"
 
    id = Column(Integer, primary_key=True, index=True)
    login_1 = Column(String)
    login_2 = Column(String)


# class Top_Players(Base):
#     __tablename__ = "Top_Players"
 
#     id = Column(Integer, primary_key=True, index=True)
#     login = Column(String)
#     victories = Column(Integer)

# class Wait_For_Player(Base):
#     __tablename__ = "Wait_For_Player"
 
#     id = Column(Integer, primary_key=True, index=True)
#     login = Column(String)

# class In_Game(Base):
#     __tablename__ = "In_Game"
 
#     id = Column(Integer, primary_key=True, index=True)
#     login_1 = Column(String)
#     login_2 = Column(String)
#     score_now_1 = Column(Integer)
#     score_now_2 = Column(Integer)
#     all_score_1 = Column(Integer)
#     all_score_2 = Column(Integer)
    
    

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base.metadata.create_all(bind = engine)



# SessionLocal = sessionmaker(autoflush=False, bind=engine)
# db = SessionLocal()

# ignat = Person(name = "Ignat", age = 17)
# andrew = Person(name = "Andrew", age = 18)

# # Только один объект
# db.add(ignat)

# # Получает список
# db.add_all((ignat, andrew))
# db.commit()