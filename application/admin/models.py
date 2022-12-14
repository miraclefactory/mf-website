# ///////////////////////////////////////////////////////////////////////////
# @file: admin/models.py
# @time: 2022/12/01
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.co
# @organisation: Miracle Factory
# @url: https://miraclefactory.co
# ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////
# module import
from application import app, db
# ///////////////////////////////////////////////////////////////////////////


class admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)            # admin_id
    name = db.Column(db.String(60), nullable=False)         # admin_name
    email = db.Column(db.String(60), nullable=False)        # admin_email
    password = db.Column(db.String(60), nullable=False)     # admin_password

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
