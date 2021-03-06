# Fundamental project for QA

## Objective 
### Overall objective with this project is the following:

> To create a CRUD application with utilisation of supporting tools.
> Methodologies and technologies that encapsulate all core modules.
> Covered during training.

### Specific Requirements
* Application must have CRUD functionality.
* Apllication mustbe created in Python.
* Fully designed test suites for the application.
* A functioning front-end website and integrated API's, using Flask.
* Code fully integrated into a Version Control System.

## Initial Ideas

* Recipes to ingredients - Simple and effective but want to do something a bit different.
* Car makes to models - Will be interesting but might get dull.
* Game studioes to games - A lot of information and constant updating.
* Chocolate company to chocolate - Simple but relatively dull.

From my initial ideas I would want to go for the game studios and there games.

## Proposal

I have decided to create a site where the users are able to see the video games from certain Video Game Design studio's.

Create - Profiles of games and Video Game Studio's:
* Title
* Description
* Founders

Read
* Video Game Studio's
* Video Games

Update
* New games come out
* New Studio's are created

Delete:
* Delete a game or a Video Game Studio

## Planning
 
### Risk Assessment:  
#### Initial risk assessment 
Everything we had learned up to that poin.
![Risk Assessment](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/initial_risk.jpg)
12/July/2021

My full risk assessment is printed below which goes into detail the low and high risks of this project
This risk assessment has been updated constantly throughout the timeline of the project.

![Risk Assessment](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/risk_assessment_2.jpg)
19/July/2021

### User Story:

![User Story](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/User_Stories.jpg)
12/July/2021

### Kanban Board:

![Kanban Board](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/kanban_requirements.jpg)
12/July/2021

#### Tools:
* Jira

### Entity Relationship Diagram

#### One to Many:
![One to Many](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/ERD.jpg)
12/July/2021

#### Tools:
* LucidChart


### Pipeline for CI
![Pipline](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/pipeline_design.jpg)
12/July/2021

#### Tools:
* LucidChart

### Model:

    class Company:
        id = Column
        name = Column
        description = Column
        founders = Column
        games = relationship('Games', backref='games') 

    class Games:
        id = Column, primary_key=True
        name = Column
        genre = Column
        company_id = Column, db.ForeignKey('company.id')

This was the model for the database and the one to many relationship.

#### Tools:
* MySQL
* Python3
* .db

### Application:

#### Create:
    @app.route('/create')
        form = CompanyFrom()
            new_company = (
                name=form.name.data, 
                description = form.description.data, 
                founders = form.founders.data
            )
            db.session.commit()

            return redirect('home')
        else:
            return ('create.html')

    @app.route('/create_game')
        form = GamesForm()
            new_game = (
                name=form.name.data, 
                genre = form.genre.data, 
                company_id = form.company.data
            )
            db.session.commit()

            return 'home')
        else:
            companies = all
            return 'create_game.html'

#### Update:
    @app.route('/update/<int:id>')
        form = CompanyFrom()
            companies name = form.name.data
            companies description = form.description.data  
            companies founders = form.founders.data
            db.session.commit()

            return 'home'
        else:
            return 'update.html'

    @app.route('/update_game/<int:id>')
        form = GamesForm()

            games name = form.name.data
            games genre = form.genre.data  
            games company = form.company.data
            db.session.commit()

            return 'home'
        else:
            return 'create_game.html'
#### Read:
    @app.route('/')
    def home():
        companies = Company.query.all()
        games = Games.query.all()
        return render_template('home.html', companies = companies, games=games)
#### Delete:
    @app.route('/delete/<int:id>')
    def delete(id):
        companies = Company.query.get(id)
        db.session.delete(companies)
        db.session.commit()

        return 'home'

    @app.route('/delete_game/<int:id>')
    def delete_game(id):
        games = Games.query.get(id)
        db.session.delete(games)
        db.session.commit()

        return 'home'


Below are screenshots from the front end of the application. Very little designing was implemented but the functionlity all works well.

#### Home Page:

![Home Page](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/home%20page.jpg)

The Home page was a simple table with the companies information above and the games below. You are able to update which will take you back to form page or delete the entrey completely.

#### Company From:
![Company](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/company%20form.jpg)

This will add a new company or update one using forms.

#### Game From:
![Game](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/game%20form.jpg)

This will add a new game or update one using forms.

#### Tools:
* python3
* pip3
* Flask
* Jinja
* SQLAlchemy
* flask_wtf
* pymysql

### Issues:
![Issues](https://github.com/PranayWara/fundemental_project/blob/main/Images/Issues.jpg)
 
 #### Not being able to display the games table on my homepage:

 The biggest issues I had when i came to this project is the fact that i wasnt able to display the games under the companies. Originally on my home.html page I had:

    {% if company.games %}
    {{ company.games.name }}
    <br>
    {% endif %}

This wouldn't displace any games under the company. However if was to do 

    {{ company.games }}   

the output would be

    <Games1>

This showed that the relationship between the two tables was working so it had to be with the home page coding itself.

After many hours I was able to find the right line to debugg the code and display the games:

    {% for game in games %}
    {% if company.id == game.company_id %}
    {{ game.name }}
    <a href = "{{url_for ('update_game', id=game.id)  }}">'>Update</a> 
    <a href = "{{url_for ('delete_game', id=game.id)  }}">'>Delete</a>
    <br>
    {% endif %}
    {% endfor %}

Also meant I could implament the CRUD funtionality to the second table as well.

 #### Test Coverage being too small:

 When i first wrote my test, the coverage was 73%, meaning i needed to rewrite some of my tests.

 The main area where I was failing was viewing of the information on the homepage, with the below test I was able to increase the coverage:

    class TestView(TestBase):
        def test_home(self):
            response = self.client.get(url_for('home'))  
            self.assert200(response)

        def test_create(self):
            response = self.client.get(url_for('add'))  
            self.assert200(response)
        
        def test_update(self):
            response = self.client.get(url_for('update', id=1))  
            self.assert200(response)

However my tests still needed to cover the second table. By looking at the table itself instead of the output I was able to complete this but not cover all of the routes for example redirecting the user back to the homepage.

    self.assert200(response)
    assert Games.query.filter_by(name='Test1').first() != None

The coverage is now at an acceptable 82%.

 #### Not being able to delete or update games:

 This was closely linked to the first problem, as the solutuion to the first was the same to this. Being able to finally call the information from the second tabel to the homepage meant calling it to update and delete was just simply copying the same code used in table 1 and changing the input to call for the second table.

### Testing:
Using both Unit Testing and Integration Testing I was able to test the CRUD functionality of both of the tables and have a relatively high coverage.
#### Unit Testing:
Here's a link to [Unit Tests][https://github.com/PranayWara/fundemental_project/blob/feature/tests/test_unit.py]

When designing the tests I wanted to test each aspect of the build. All the CRUD functionality which passed and gave me a coverage of 82%.

#### Integration Testing:
Here's a link to [Integration Tests][https://github.com/PranayWara/fundemental_project/blob/feature/tests/test_int.py]

Using integration testing I can test for redirects and the entire applicaiton is working using steps. 

#### Report:
![Coverage Report](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/coverage.jpg)
#### Analyses:
With an overall coverage of 82% the tests seemed to go relatively well. The CRUD functionality for the Company table all passed the tests with 100% coverage. However where I lose coverage in unit test when the CRUD functionality for the second table, Games. The Create and read where fine but the Update and Delete was loosing me a lot of coverage. I would see which lines where failing by using the:
    python3 -m pytest --cov=application --cov-report term-missing

![Coverage Report Missing Terms](https://github.com/PranayWara/fundemental_project/blob/main/Images/coverage_missing_term.jpg)

42-45 = Sending the user back to the main home page after creating. This can be solved by using headless testing, Selenium.

66-79 = Even though my tests checks for updating the game. It doesnt check for updating the home page or sending the user back to the home page.

91-95 = Deleting a game could not be tested and would need, selenium to test it.

#### Tools:
* python3
* pytest
* pytest-cov

### CI Server:
Using Jenkins I was able to test my application which has been directly pushed to my github repository. This was done by creating a new VM and installing jenkins and giving it the ability to sudo install. By opening port 8080 I could use to write the following script:

    #!/bin/bash

    sudo apt-get install python3 -y
    sudo apt-get install python3-pip -y
    sudo apt-get install python3-venv -y
    sudo apt install chromium-browser -y
    sudo apt install wget unzip -y
    version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version | grep -oP 'Chromium \K\d+'))
    wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
    sudo unzip chromedriver_linux64.zip -d /usr/bin
    rm chromedriver_linux64.zip

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirments.txt

    python3 -m pytest --cov=application --cov-report xml --junitxml junit.xml

Having linked the repository to jenkins using a webhook. Everytime I pushed something it would run the script.
This would go into my github repository clone it. Then install the relevant requirements and then run the unit tests.

![Jenkins Test](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/coverage_jenkins.jpg)

Using the plugin JUnit and Cobertura I was able to create a detailed report on the tests.
#### JUnit:
Showed the individual tests and if they passed or not.
##### Cobertura:
Gave me the coverage breakdown and the trend of the application.

![Cobertura Test](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/cobertura.jpg)

#### Tools:
* Jenkins

### End of Project:

![End of Project Kanban Board](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/end%20of%20project%20kanban.jpg)

All tasks where completed for the project.


### Future Plans:
My next stage would be to have a log in feature so users are able to favorite their favorite Company. This will all them to quickly see if there is any new games released.

Video Studio Companies has also collaborated on games so having a many-to-many relationship will also the next step. The diagram below is a start to this plan:
![ERD Future](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/ERD_2.jpg)

### Author
Pranay Wara





