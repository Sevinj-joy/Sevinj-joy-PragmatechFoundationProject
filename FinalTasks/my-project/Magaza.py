#Bir mağaza düşünün.Bu mağaza fərqli kategoriyalarda məhsul satışı ilə məşquldur.
#Məhsulların (ad,qiymət,miqdar,kategoriya,əlavə informasiya) məlumatlarının idarə olunması üçün 
#lazım olan database strukturunu qurun.(dbdesigner.com saytından istifadə edə bilərsiniz strukturu qurmaq üçün).
# Nəticəni şəkil olaraq reponuza yerləşdirib linkini qeyd edin
from enum import unique
from pickle import FALSE
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=FALSE
db = SQLAlchemy(app)

# CREATE TABLE some_table (
#     id INTEGER NOT NULL,
#     data INTEGER NOT NULL ON CONFLICT FAIL,
#     PRIMARY KEY (id)
# )
class User(db.Model):
   id =db.Column(db.Integer , primary_key=True)
   ad =db.Column(db.String(80) ,unique=True )
   qiymet=db.Column(db.Integer, nullable=True)
   miqdar =db.Column(db.String(80), nullable= True)
   kateqoriya=db.Column(db.String(80), nullable= True)
   elave_informasiya=db.Column(db.String(250), nullable= True)

