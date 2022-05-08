from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment,Pitch, User,Upvote,Downvote
from .. import db