from flask_admin import Admin
from flask_admin.theme import Bootstrap4Theme
from flask_admin.contrib.sqla import ModelView
from models.user import User, db


def admin_setup(app):
    admin = Admin(app, name="Admin", theme=Bootstrap4Theme(swatch="cosmo"))

    class AdminUser(ModelView):
        can_create = False
        can_delete = True
        can_edit = True

    admin.add_view(AdminUser(User, db.session))

