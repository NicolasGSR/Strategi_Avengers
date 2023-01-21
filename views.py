"""Rotas"""

from flask import render_template, request, redirect
from main import app, db
from classes import Hero, Selecao, Vingadores, Equipe
from config import marvel

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/heroes')
def heroes():
    characters = marvel.characters
    all_characters = characters.all()["data"]["results"]
    heroes = []
    for char in all_characters:
        heroi = Hero(char["thumbnail"]["path"] + "." + char["thumbnail"]["extension"], char["name"], char["description"])
        heroes.append(heroi)
    return render_template('heroes.html', heroes = heroes)

@app.route('/search', methods = ['POST',])
def search():
    search = request.form['search']
    if search == "":
        return redirect('/heroes')
    else:
        characters = marvel.characters
        all_characters = characters.all(nameStartsWith=search)["data"]["results"]
        heroes = []
        for char in all_characters:
            heroi = Hero(char["thumbnail"]["path"] + "." + char["thumbnail"]["extension"], char["name"], char["description"])
            heroes.append(heroi)
    return render_template('heroes.html', heroes = heroes)

@app.route('/select')
def select():
    lista = Selecao.query.order_by(Selecao.id)
    return render_template('select.html', heroes = lista)

@app.route('/selecting', methods = ['POST',])
def selecting():
    picture = request.form['picture']
    name = request.form['name']
    description = request.form['description']

    new_selecao = Selecao(picture = picture, name = name, description = description)

    db.session.add(new_selecao)
    db.session.commit()
    return redirect('/select')

@app.route('/teams')
def teams():
    lista = Vingadores.query.order_by(Vingadores.id)
    return render_template('teams.html', avengers = lista)

@app.route('/teams2')
def teams2():
    lista = Equipe.query.order_by(Equipe.id)
    return render_template('teams2.html', equipe = lista)

@app.route('/delete/<int:id>')
def delete(id):
    Selecao.query.filter_by(id = id).delete()
    db.session.commit()

    return redirect('/select')

@app.route('/avengers/<int:id>')
def avengers(id):
    avenger = Selecao.query.filter_by(id = id).first()
    picture = avenger.picture
    name = avenger.name
    description = avenger.description

    new_avenger = Vingadores(picture = picture, name = name, description = description)

    db.session.add(new_avenger)
    db.session.commit()

    return redirect('/teams')

@app.route('/equipe/<int:id>')
def equipe(id):
    member = Selecao.query.filter_by(id = id).first()
    picture = member.picture
    name = member.name
    description = member.description

    new_member = Equipe(picture = picture, name = name, description = description)

    db.session.add(new_member)
    db.session.commit()

    return redirect('/teams2')

@app.route('/delete2/<int:id>')
def delete2(id):
    Vingadores.query.filter_by(id = id).delete()
    db.session.commit()

    return redirect('/teams')

@app.route('/delete3/<int:id>')
def delete3(id):
    Equipe.query.filter_by(id = id).delete()
    db.session.commit()

    return redirect('/teams2')

@app.route('/transferir/<int:id>')
def transferir(id):
    member = Vingadores.query.filter_by(id = id).first()
    picture = member.picture
    name = member.name
    description = member.description

    new_member = Equipe(picture = picture, name = name, description = description)

    db.session.add(new_member)
    db.session.commit()

    Vingadores.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/teams')

@app.route('/transferir2/<int:id>')
def transferir2(id):
    member = Equipe.query.filter_by(id = id).first()
    picture = member.picture
    name = member.name
    description = member.description

    new_member = Vingadores(picture = picture, name = name, description = description)

    db.session.add(new_member)
    db.session.commit()

    Equipe.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/teams2')