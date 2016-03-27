from app import db


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