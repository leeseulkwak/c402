from flask import Blueprint, render_template

bp=Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')


#화면 코딩
# @bp.route('/question')
# def question(): # 질문 목록 객체
#     # question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('question/question_list.html', question_list=question_list)