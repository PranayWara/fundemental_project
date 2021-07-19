from application import app, db
from application.models import Company, Games
from flask import Flask, render_template


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
