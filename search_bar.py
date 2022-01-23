from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SeachBar(FlaskForm):
    search_bar = StringField('Destination Eg: restaurant, bar, hiking',
                           validators=[DataRequired(), Length(min=2, max=15, message='Invalid response')])
    zip_bar = StringField('Search by Zip-Code',
                             validators=[DataRequired(), Length(min=5, max=5, message='Invalid zip code')])
    search_button = SubmitField('Search')
class inputBox(FlaskForm):
    search_bar = StringField('Search by Zip-Code',
                           validators=[DataRequired(), Length(min=5, max=5, message='Invalid zip code')])
    search_button = SubmitField('Search')