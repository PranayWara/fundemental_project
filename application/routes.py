from re import A
from application.models import Company, Games
from . import app, db
from flask import Flask, render_template, request, redirect, url_for
from application.models import Company, Games
from .forms import CompanyFrom, GamesForm

@app.route('/')
def home():
    companies = Company.query.all()
    games = Games.query.all()
    return render_template('home.html', companies = companies, games=games)

@app.route('/create', methods = ['GET', 'POST'])
def add():
    error = ''
    
    form = CompanyFrom()

    if request.method == 'POST':

        new_company = (Company(name=form.name.data, description = form.description.data, founders = form.founders.data))
        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('create.html', form=form)

@app.route('/create_game', methods = ['GET', 'POST'])
def create_game():
    form = GamesForm()

    if request.method == 'POST':

        new_game = (Games(name=form.name.data, genre = form.genre.data, company_id = form.company.data))
        db.session.add(new_game)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        companies = Company.query.all()

        form.company.choices = [(company.id, company.name) for company in companies]
        return render_template('create_game.html', form=form)

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    form = CompanyFrom()
    companies = Company.query.get(id)

    if request.method == 'POST':

        companies.name = form.name.data
        companies.description = form.description.data  
        companies.founders = form.founders.data
        db.session.add(companies)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('update.html', form=form)


@app.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    companies = Company.query.get(id)
    db.session.delete(companies)
    db.session.commit()

    return redirect(url_for('home'))


