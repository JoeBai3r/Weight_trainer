from main import db

class Body(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    benchMax = db.Column(db.Integer)
    squatMax = db.Column(db.Integer)
    deadliftMax = db.Column(db.Integer)

    def __repr__(self):
        return f"Body('{self.age}', '{self.benchMax}')"

class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    benchMax = db.Column(db.Integer)
    squatMax = db.Column(db.Integer)
    deadliftMax = db.Column(db.Integer)

    def __repr__(self):
        return f"Power('{self.age}', '{self.benchMax}')"

