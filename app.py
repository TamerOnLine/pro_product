import os
from flask import Flask
from models.models import db
from routes import main_routes

def create_app():
    app = Flask(__name__)

    # تحديد المسار الكامل لقاعدة البيانات داخل مجلد instance
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'instance', 'products.db')

    # تأكد من وجود مجلد instance
    os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(main_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8030)
