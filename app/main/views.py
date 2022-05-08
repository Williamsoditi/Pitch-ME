from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment,Pitch, User,Upvote,Downvote
from .. import db
from .forms import CommentForm,PitchForm,UpdateProfile


#Application views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch - M'
    pitches = Pitch.query.all()
    users = User.query.all()
    pickuplines = Pitch.query.filter_by(category = 'Pick-up Lines').all()
    sales = Pitch.query.filter_by(category = 'Sales').all()
    innovation = Pitch.query.filter_by(category = 'Innovation').all()
    humanity = Pitch.query.filter_by(category = 'Humanity').all()
    music = Pitch.query.filter_by(category = 'Music').all()
    religion = Pitch.query.filter_by(category = 'Religion').all()

    return render_template('index.html',title = title,pitches = pitches,pickuplines=pickuplines,sales=sales,innovation=innovation,humanity=humanity,music=music,religion=religion,users=users)

