from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class AlertForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    description = TextAreaField("Description")
    severity = SelectField(
        "Severity",
        choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")],
        validators=[DataRequired()],
    )
    user_id = SelectField("User", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Create Alert")


class HouseholdForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    address = StringField("Address", validators=[Length(max=200)])
    user_id = SelectField("User", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Create Household")


class KitForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    description = TextAreaField("Description")
    household_id = SelectField("Household", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Create Kit")


class CommunityForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    description = TextAreaField("Description")
    submit = SubmitField("Create Community")
