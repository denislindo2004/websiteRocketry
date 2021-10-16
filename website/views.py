from flask import Blueprint, render_template, request, jsonify
from flask.helpers import flash
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views =  Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return  render_template('home.html', user=current_user)

@views.route('/about')
def about():
    return  render_template('about.html', user=current_user)

@views.route('/escola', methods=['GET', 'POST'])
@login_required
def escola():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.', category='success')

    return  render_template('escola.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note =  Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('escola/pesquisa_bootstrap')
def pesquisa_bootstrap():
    return render_template('pesquisa_bootstrap.html', user=current_user)
