from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from flask import url_for
import os
from application import app, db
from application.models import Company

class TestBase(TestCase):
    def create_app(self):
        
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY=str(os.urandom(16)),
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()

        db.session.add(Company(name = 'Run Unit Test', description = 'Test', founders = 'PRANAY'))
        db.session.add(Company(name = 'Valve', description = 'Big Company', founders = 'Gabe'))

        db.session.commit()

    def tearDown (self):
        db.drop_all()  


class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        assert '1 | Run Unit Test | Test | PRANAY'  in response.data.decode()
        assert '2 | Valve | Big Company | Gabe'  in response.data.decode()

class TestCreate(TestBase):
    def test_create(self):
        response = self.client.post(
            url_for('add'),
            data = {'name': 'Test1', 'description':'Test2', 'founders':'Test3'},
            follow_redirects = True
        )

        assert response.current_url == url_for('home')

        raise AssertionError(response.data)