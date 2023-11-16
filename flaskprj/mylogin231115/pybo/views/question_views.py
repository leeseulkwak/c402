from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User, Question

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
   return render_template('question/question_list.html')

@bp.route('/detail/')
def _detail():
    
    return render_template('question/question_detail.html')
