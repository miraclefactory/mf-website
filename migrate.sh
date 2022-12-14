# ///////////////////////////////////////////////////////////////////////////
# @file: migrate.sh
# @time: 2022/12/14
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.co
# @organisation: Miracle Factory
# @url: https://miraclefactory.co
# ///////////////////////////////////////////////////////////////////////////


export FLASK_APP=application
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
