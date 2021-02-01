from main import db

class User(db.Model):
 __tablename__= 'userregister'
 id=db.Column(db.Integer, primary_key=True)
 firstname=db.Column(db.String(20), unique=False, nullable=False)
 lastname = db.Column(db.String(20), unique=False, nullable=False)
 dateofbirth = db.Column(db.Integer, unique=False, nullable=True)
 residentialaddress = db.Column(db.String(50), unique=True, nullable=False)
 nationality = db.Column(db.String(20), unique=False, nullable=False)
 nationalidentitynumber = db.Column(db.Integer, unique=False, nullable=False)
 # represent the object when it is queried for

 def __repr__(self):
 return '<Register {}>'.format(self.id)