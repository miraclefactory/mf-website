# ///////////////////////////////////////////////////////////////////////////
# @file: user/models.py
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


# define a many-to-many relationship between users and projects
users_projects = db.Table('users_projects',
                          db.Column('user_id', db.Integer, db.ForeignKey('joins.id')),
                          db.Column('project_id', db.Integer, db.ForeignKey('projects.id')))

# define a many-to-many relationship between users and teams
users_teams = db.Table('users_teams', 
                       db.Column('user_id', db.Integer, db.ForeignKey('joins.id')), 
                       db.Column('team_id', db.Integer, db.ForeignKey('teams.id')))


class joins(db.Model):
    id = db.Column(db.Integer, primary_key=True)                # user_id
    name = db.Column(db.String(60), nullable=False)             # user_name
    email = db.Column(db.String(60), nullable=False)            # user_email
    type = db.Column(db.String(10), nullable=False)             # user_type: join / contact
    password = db.Column(db.String(60), nullable=False)         # user_password
    activated = db.Column(db.Boolean, default=False)            # user_activated: True / False
    is_admin = db.Column(db.Boolean, default=False)             # user_is_admin: True / False
    email_feed = db.Column(db.Boolean, default=False)           # user_email_feed: True / False
    public_member = db.Column(db.Boolean, default=False)        # user_public_member: True / False
    active_contributor = db.Column(db.Boolean, default=False)   # user_active_contributor: True / False
    code_reviewer = db.Column(db.Boolean, default=False)        # user_code_reviewer: True / False
    avatar = db.Column(db.String(60),                           # user_avatar
                       default='../../static/images/default-avatar.png')
    projects = db.relationship('projects', secondary=users_projects, 
                                         backref='members')
    teams = db.relationship('teams', secondary=users_teams, 
                                      backref='members')

    def __init__(self, 
                 name, 
                 email, 
                 type, 
                 password, 
                 activated=False,
                 is_admin=False,
                 email_feed=False,
                 public_member=False,
                 active_contributor=False,
                 code_reviewer=False,
                 avatar='../../static/images/caltech.jpg'):
        self.name = name
        self.email = email
        self.type = type
        self.password = password
        self.activated = activated
        self.is_admin = is_admin
        self.email_feed = email_feed
        self.public_member = public_member
        self.active_contributor = active_contributor
        self.code_reviewer = code_reviewer
        self.avatar = avatar

    # asynchronous add user
    def add_user(self):
        with app.app_context():
            db.session.add(self)
            db.session.commit()

    # asynchronous activate user
    def activate_user(self):
        with app.app_context():
            self.activated = True
            db.session.commit()

    # asynchronous delete user
    def delete_user(self):
        with app.app_context():
            db.session.delete(self)
            db.session.commit()
    
    # asynchronous update user profile
    def update_user_profile(self, name, email, password, avatar):
        with app.app_context():
            self.name = name
            self.email = email
            self.password = password
            self.avatar = avatar
            db.session.commit()
    
    # asynchronous update user settings
    def update_user_settings(self, email_feed, public_member, active_contributor, code_reviewer):
        with app.app_context():
            self.email_feed = email_feed
            self.public_member = public_member
            self.active_contributor = active_contributor
            self.code_reviewer = code_reviewer
            db.session.commit()
    
    # asynchronous update user projects
    def update_user_projects(self, projects):
        with app.app_context():
            self.projects.append(projects)
            db.session.add(self)
            db.session.commit()
    
    # asynchronous update user teams
    def update_user_teams(self, teams):
        with app.app_context():
            self.teams.append(teams)
            db.session.add(self)
            db.session.commit()
        

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
    def add_user(self):
        with app.app_context():
            db.session.add(self)
            db.session.commit()

    # asynchronous activate contact
    def activate_user(self):
        with app.app_context():
            self.activated = True
            db.session.commit()

    # asynchronous delete contact
    def delete_user(self):
        with app.app_context():
            db.session.delete(self)
            db.session.commit()


class projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)                # project_id
    name = db.Column(db.String(60), nullable=False)             # project_name
    description = db.Column(db.String(1000), nullable=False)    # project_description
    url = db.Column(db.String(1000), nullable=False)            # project_url
    owner = db.Column(db.Integer, nullable=False)               # project_owner: user_id

    def __init__(self, name, description, url, owner):
        self.name = name
        self.description = description
        self.url = url
        self.owner = owner

    # asynchronous add project
    def add_project(self):
        with app.app_context():
            db.session.add(self)
            db.session.commit()

    # asynchronous delete project
    def delete_project(self):
        with app.app_context():
            db.session.delete(self)
            db.session.commit()
    
    # asynchronous update project
    def update_project(self, name, description, url, owner):
        with app.app_context():
            self.name = name
            self.description = description
            self.url = url
            self.owner = owner
            db.session.commit()
    
    # # asynchronous update project members
    # def update_project_members(self, members):
    #     with app.app_context():
    #         self.members = members
    #         db.session.commit()


class teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)                # team_id
    name = db.Column(db.String(60), nullable=False)             # team_name
    description = db.Column(db.String(1000), nullable=False)    # team_description
    owner = db.Column(db.Integer, nullable=False)               # team_owner: user_id

    def __init__(self, name, description, owner):
        self.name = name
        self.description = description
        self.owner = owner

    # asynchronous add team
    def add_team(self):
        with app.app_context():
            db.session.add(self)
            db.session.commit()

    # asynchronous delete team
    def delete_team(self):
        with app.app_context():
            db.session.delete(self)
            db.session.commit()
    
    # asynchronous update team settings
    def update_team(self, name, description, owner):
        with app.app_context():
            self.name = name
            self.description = description
            self.owner = owner
            db.session.commit()
    
    # # asynchronous update team members
    # def update_team_members(self, members):
    #     with app.app_context():
    #         self.members = members
    #         db.session.commit()
