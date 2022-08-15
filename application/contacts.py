# ///////////////////////////////////////////////////////////////////////////
# @file: contacts.py
# @time: 2022/07/15
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.co
# @organisation: Miracle Factory
# @url: https://miraclefactory.co
# ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////
# module import
from application import app, db
# ///////////////////////////////////////////////////////////////////////////


class contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)            # user_id
    name = db.Column(db.String(60), nullable=False)         # user_name
    email = db.Column(db.String(60), nullable=False)        # user_email
    type = db.Column(db.String(10), nullable=False)         # user_type: join / contact
    message = db.Column(db.String(1000), nullable=False)    # user_message
    activated = db.Column(db.Boolean, default=False)        # user_activated: True / False

    def __init__(self, name, email, type, message, activated=False):
        self.name = name
        self.email = email
        self.type = type
        self.message = message
        self.activated = activated

    # asynchronous add contact
    def add_contact(self):
        with app.app_context():
            db.session.add(self)
            db.session.commit()

    # asynchronous activate contact
    def activate_contact(self):
        with app.app_context():
            self.activated = True
            db.session.commit()

    # asynchronous delete contact
    def delete_contact(self):
        with app.app_context():
            db.session.delete(self)
            db.session.commit()
