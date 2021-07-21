# Fundamental project for QA

Mark Scheme:
Software Design
- Modeling (done)
- README (done)
Programming/Software Development
- Code (done)
- Tests 
- Tools and Workflows
Testing
- Designs test cases and scripts 
- Analyses
Systems Integration and Build
- Build server
- Tests Scripts 
- Risks (done)

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
My risk assessment is printed below which goes into detail the low and high risks of this project
This risk assessment has been updated constantly throughout the timeline of the project.

![Risk Assessment](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/risk_assessment_2.jpg)

### User Story:

![User Story](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/User_Stories.jpg)

### Entity Relationship Diagram

#### One to Many:
![First Attempt](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/ERD.jpg)


### Pipeline for CI
![Pipline](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/pipeline_design.jpg)

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

This was the model for the database and the relationship.

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

### Testing:
Using unit testing as for this project there was no need for selenium as the appication isnt advanved enough.
#### Unit Testing:
Here's a link to [Unit Tests][https://github.com/PranayWara/fundemental_project/blob/feature/tests/test_unit.py]

When designing the tests I wanted to test each aspect of the build. All the CRUD functionality which passed and gave me a coverage of 82%.

#### Report:
#### Analyses:

### CI Server:

### Future Plans:
![ERD Future](https://raw.githubusercontent.com/PranayWara/fundemental_project/main/Images/ERD_2.jpg)






