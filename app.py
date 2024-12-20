from flask import Flask, render_template, request, redirect
from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os

app = Flask(__name__, template_folder ="siteciencia/templates", static_folder = "siteciencia/static")

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "cd.sqlite")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(200), nullable=False)
  date_created = db.Column(db.DateTime, default=dt.now())
  def __repr__(self):
    return  f"Task: #{self.id}, description: {self.description}"

class Frase(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  frase = db.Column(db.String(500), nullable=False)
  autor = db.Column(db.String(50), default='Anônimo')
  def __repr__(self):
    return  f"Frase: #{self.id}, autor: {self.autor}, frase: {self.frase}"

  
@app.route("/")
def index():
  return render_template("index.html")


@app.route("/analise")
def analise():
  return render_template("analise.html")


@app.route('/estatistica') 
def estatistica(): 
  return render_template('estatistica.html') 


@app.route('/programacao') 
def programacao(): 
  return render_template('programacao.html')


@app.route('/tarefas') 
def tarefas(): 
  return render_template('tarefas.html')


@app.route('/frases') 
def frases(): 
  return render_template('frases.html')


@app.route("/galeria")
def galeria():
  numeros = random.sample(range(1, 61), 30)
  lista_imagens = [f"{num}.jpg" for num in numeros]
  return render_template("galeria.html", imagens=lista_imagens)


# novas rotas

@app.errorhandler(404)
def not_found(error):
  return render_template("404.html")


if __name__ == "__main__":
  app.run(debug=True, port=5001)
