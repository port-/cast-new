from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Length, EqualTo
from datetime import datetime

class PickForm(Form):
	artist = StringField('Artist', validators=[Required()])
	album = StringField('Album', validators=[Required()])
	song = StringField('Song', validators=[Required()])
	description = TextAreaField('Description')
	submit = SubmitField('Pick!')

	def from_model(self, pick):
		self.artist.data = pick.artist
		self.album.data = pick.album
		self.song.data = pick.song
		self.description.data = pick.description

	def to_model(self, pick):
		pick.artist = self.artist.data
		pick.album = self.album.data
		pick.song = self.song.data
		pick.description = self.description.data

class CastForm(Form):
	cast_number = StringField('Cast Number', validators=[Required()])
	time = StringField('Time', validators=[Required()])
	date = StringField('Date', validators=[Required()])
	host = SelectField('Host', coerce=int, validators=[Required()])
	description = TextAreaField('Description')
	picture_url = StringField('Picture URL (optional)')
	submit = SubmitField('Create cast')

	def from_model(self, cast):
		self.cast_number.data = cast.cast_number.data
		self.time.data = cast.time
		self.date.data = cast.date
		self.description.data = cast.description
		self.picture_url.data = cast.picture_url

	def to_model(self, cast):
		cast.cast_number = self.cast_number.data
		cast.time = self.time.data
		cast.date = self.date.data
		cast.description = self.description.data
		cast.picture_url = self.picture_url.data