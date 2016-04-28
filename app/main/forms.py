from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length


class LoginForm(Form):
    username = StringField('Username', validators=[Required(), Length(1, 16)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


#tag submission form class
# for Brightcove:
#    no tag > 128 characters
#    A video can have no more than a total of 1200 tags
#    Only the first 100 tags are cached and will be the only ones that are available via type ahead
#rules:
#    multiple words separated by a space (converted to %20 as per RFC 1738) will be considered as one tag. 
#    words or phrases separated by commas are treated as distinct tags



class TagSearchForm(Form):
    tag = StringField('Search CMS for metatag:', )
    submit = SubmitField('Submit')


