"""Nome: Strategi Avengers
Descrição: Webapp para a seleção da empresa Strategi Consultoria.
Um webapp que disponibiliza uma lista de herois através da MarvelAPI, e permite a seleção desses 
herois e divisão dos mesmo em equipes.
"""

from flask import Flask #Importando flask
from flask_sqlalchemy import SQLAlchemy #Importando SQLAlchemy

app = Flask(__name__) #Instanciando a aplicação


app.config.from_pyfile('config.py') #Definindo as configurações necessarias

db = SQLAlchemy(app) #Conectando ao banco de dados

from views import * #Importando todas as rotas

if __name__ == '__main__':
    app.run(debug=True)