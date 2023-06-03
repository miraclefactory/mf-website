# ///////////////////////////////////////////////////////////////////////////
# @file: run.sh
# @time: 2022/07/15
# @author: Yuelin Xin
# @email: yuelinxin@miraclefactory.ai
# @organisation: Miracle Factory
# @url: https://miraclefactory.ai
# ///////////////////////////////////////////////////////////////////////////

export FLASK_APP=application
flask run --host=0.0.0.0 --port=9000 --debugger --reload
