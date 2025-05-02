from flask import Blueprint, render_template, request, redirect, url_for
from models.models import Product, db

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main_routes.route('/admin')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@main_routes.route('/admin/add', methods=['GET', 'POST'])
def admin_add_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            price=float(request.form['price']),
            description=request.form.get('description'),
            image=request.form.get('image'),
            specs=request.form.get('specs')
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('main.admin_dashboard'))
    
    return render_template('admin/add_product.html')


@main_routes.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)
