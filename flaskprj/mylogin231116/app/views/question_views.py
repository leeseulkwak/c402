from flask import Blueprint, render_template
from app.models import Question

bp =Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def list():
    question_list=Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')#값1을 받아서 
# 요청받은 변수를 매개변수에 전달!!!
def detail(question_id):#값1을 넣어 주기
    question=Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)