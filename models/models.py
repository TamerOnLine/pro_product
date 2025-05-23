
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))  
    specs = db.Column(db.Text)         
    product_code = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Product {self.name}>'
