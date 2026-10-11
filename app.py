import os
from flask import Flask
from flask_login import LoginManager
from models import db, Student


def create_app():
    app = Flask(__name__)

    # ── Configuration ──────────────────────────────────────────────────────────
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-prod')
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'sqlite:///' + os.path.join(basedir, 'instance', 'career_portal.db')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Make sure the instance folder exists
    os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)

    # ── Extensions ─────────────────────────────────────────────────────────────
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'warning'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Student.query.get(int(user_id))

    # ── Blueprints ──────────────────────────────────────────────────────────────
    from routes.auth        import auth_bp
    from routes.dashboard   import dashboard_bp
    from routes.careers     import careers_bp
    from routes.internships import internships_bp
    from routes.profile     import profile_bp
    from routes.main        import main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp,        url_prefix='/auth')
    app.register_blueprint(dashboard_bp,   url_prefix='/dashboard')
    app.register_blueprint(careers_bp,     url_prefix='/careers')
    app.register_blueprint(internships_bp, url_prefix='/internships')
    app.register_blueprint(profile_bp,     url_prefix='/profile')

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
