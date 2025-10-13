from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional


class JoinCommunityForm(FlaskForm):
    community_id = SelectField("Community", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Join Community")


class ProfileForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[Optional(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[Optional(), EqualTo("password")]
    )
    submit = SubmitField("Update Profile")
