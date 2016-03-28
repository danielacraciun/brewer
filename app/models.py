from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.Integer(), nullable=False)
    sign_up_date = db.Column(db.Date())

    def __init__(self, user_id, name, email, password, date):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.sign_up_date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Tea(db.Model):
    __tablename__ = 'teas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=True)
    quantity = db.Column(db.Integer(), nullable=True)
    price = db.Column(db.Integer(), nullable=True)

    def __init__(self, tea_id, name, tea_type, qty, price):
        self.id = tea_id
        self.name = name
        self.type = tea_type
        self.quantity = qty
        self.price = price

    def __repr__(self):
        return '<id {}>'.format(self.id)
