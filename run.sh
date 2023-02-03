# ///////////////////////////////////////////////////////////////////////////
# @file: run.sh
# @time: 2022/07/15
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.co
# @organisation: Miracle Factory
# @url: https://miraclefactory.co
# ///////////////////////////////////////////////////////////////////////////

export FLASK_APP=application
flask run --host=0.0.0.0 --port=9000 --no-debugger
