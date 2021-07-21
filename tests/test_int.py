from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
import os
from application import app, db



class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY=str(os.urandom(16)),
            TESTING = True,
            DEBUG=True,
            LIVESERVER_PORT=self.TEST_PORT,
            )
        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() 

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown (self):
        db.drop_all()  

        self.driver.quit()


    def test_server(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        assert response.code == 200

class TestCreate(TestBase):
    def test_create(self):
        #navigate to create company page
        self.driver.find_element_by_xpath('/html/body/a[1]').click()
        #fill in form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Create company name working')
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('Create company description working')
        self.driver.find_element_by_xpath('//*[@id="founders"]').send_keys('Create company founders working')
        #submit form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        #navigate to create game page
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        #fill in form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Create game name working')
        self.driver.find_element_by_xpath('//*[@id="genre"]').send_keys('Create game genre working')
        #submit form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        #check
        elements = self.driver.find_element_by_xpath('/html/body/div')
        assert 'Create company name working' in elements.text
        assert 'Create game name working' in elements.text
    
class TestUpdate(TestBase):
    def test_update(self):
        #navigate to create company page
        self.driver.find_element_by_xpath('/html/body/a[1]').click()
        #fill in form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Create company name working')
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('Create company description working')
        self.driver.find_element_by_xpath('//*[@id="founders"]').send_keys('Create company founders working')
        #submit form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        #navigate to create game page
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        #fill in form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Create game name working')
        self.driver.find_element_by_xpath('//*[@id="genre"]').send_keys('Create game genre working')
        #submit form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        #navigate to update company page
        self.driver.find_element_by_xpath( '/html/body/div/a[1]' ).click()
        #fill in form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('update company name')
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys(' update description ')
        self.driver.find_element_by_xpath('//*[@id="founders"]').send_keys('update founder')
        #submit form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        #navigate to update game page
        self.driver.find_element_by_xpath('/html/body/div/a[3]').click()
        #fill in form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Update Game name')
        self.driver.find_element_by_xpath('//*[@id="genre"]').send_keys('update genre')
        #submit form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        #check
        elements = self.driver.find_element_by_xpath('/html/body/div')
        assert 'Create company name working' not in elements.text
        assert 'Create game name working' not in elements.text

        assert 'update company name' in elements.text
        assert 'Update Game name' in elements.text
    
class TestDelete(TestBase):
    def test_delete(self):
        #navigate to create company page
        self.driver.find_element_by_xpath('/html/body/a[1]').click()
        #fill in form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Create company name working')
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('Create company description working')
        self.driver.find_element_by_xpath('//*[@id="founders"]').send_keys('Create company founders working')
        #submit form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        #navigate to create game page
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        #fill in form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Create game name working')
        self.driver.find_element_by_xpath('//*[@id="genre"]').send_keys('Create game genre working')
        #submit form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        #delete game
        self.driver.find_element_by_xpath('/html/body/div/a[4]').click()
        #delete company
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()

        #check
        elements = self.driver.find_element_by_xpath('/html/body/div')
        assert 'Create company name working' not in elements.text
        assert 'Create game name working' not in elements.text