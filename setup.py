# ///////////////////////////////////////////////////////////////////////////
# @file: setup.py
# @time: 2022/07/15
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.ai
# @organisation: Miracle Factory
# @url: https://miraclefactory.ai
# ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////
# library import
from setuptools import setup
# ///////////////////////////////////////////////////////////////////////////


requirements = ['flask', 
                'flask-sqlalchemy', 
                'flask-mail', 
                'python-decouple', 
                'itsdangerous', 
                'flask-dance',
                'flask-migrate',
                'flask-sijax',
                'flask-wtf',
                'wtforms',
                'gunicorn',
                'werkzeug',
                'jinja2',
                'sqlalchemy',]

setup(
    name='application',
    packages=['application'],
    include_package_data=True,
    install_requires=requirements,
)
