from re import A
from application.models import Company
from . import app, db
from flask import Flask, render_template, request, redirect, url_for
from application.models import Company
from .forms import CompanyFrom

@app.route('/')
def home():
    companies = Company.query.all()
    return render_template('home.html', companies = companies)

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


