from flask import render_template, redirect, url_for, flash, g
from flask.ext.login import login_required, current_user

from app import db
from . import cast
from .forms import PickForm, CastForm
from ..models import User, Cast, Pick

from datetime import datetime

@cast.before_request
def before_request():
	g.next_cast = Cast.query.order_by(Cast.cast_number.desc()).first()

@cast.route('/')
def index():
	return render_template('cast/index.html', cast=g.next_cast)

@cast.route('/pick', methods=['GET', 'POST'])
@login_required
def pick():
	form = PickForm()
	if form.validate_on_submit():
		pick = Pick()

		form.to_model(pick)
		pick.cast = g.next_cast
		pick.author = current_user
		pick.date_added = datetime.utcnow()

		db.session.add(pick)
		db.session.commit()

		flash('Pick added successfully!')
		return redirect(url_for('cast.index'))

	return render_template('cast/pick.html', form=form)

@cast.route('/create', methods=['GET', 'POST'])
@login_required
def create_cast():
	form = CastForm()
	form.host.choices = [ (user.id, user.username) for user in User.query.all()]
	form.cast_number.data =   g.next_cast.cast_number + 1  if g.next_cast else 1

	if form.validate_on_submit():
		cast = Cast()
		form.to_model(cast)

		host = User.query.get(form.host.data)
		cast.host = host

		db.session.add(cast)
		db.session.commit()

		flash('Cast added.')
		return redirect(url_for('cast.index'))


	return render_template('cast/create.html', form=form)