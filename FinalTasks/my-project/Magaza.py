#Bir mağaza düşünün.Bu mağaza fərqli kategoriyalarda məhsul satışı ilə məşquldur.
#Məhsulların (ad,qiymət,miqdar,kategoriya,əlavə informasiya) məlumatlarının idarə olunması üçün 
#lazım olan database strukturunu qurun.(dbdesigner.com saytından istifadə edə bilərsiniz strukturu qurmaq üçün).
# Nəticəni şəkil olaraq reponuza yerləşdirib linkini qeyd edin
from enum import unique
from pickle import FALSE
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/alchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=FALSE
db = SQLAlchemy(app)

# CREATE TABLE some_table (
#     id INTEGER NOT NULL,
#     data INTEGER NOT NULL ON CONFLICT FAIL,
#     PRIMARY KEY (id)
# )
class User(db.model):
   id =db.Column(db.integer , primary_key=True)
   ad =db.Column(db.string(80) ,unique=True )
   qiymet=db.Column