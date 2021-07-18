from application import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(100))
    founders = db.Column(db.String(100))

# class Games(db.Model):
#     gid = db.Column(db.Integer, primary_key=True)
#     game_name = db.Column(db.String(30), nullable=False)
#     release_date = db.Column(db.DateTime, nullable =False)
#     genre = db.Column(db.String(30))
#     company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)