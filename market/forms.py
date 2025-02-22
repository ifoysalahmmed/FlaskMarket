from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from market.models import User


class RegistrationForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                "Username already exists! Please try a different username"
            )

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data
        ).first()
        if email_address:
            raise ValidationError("Email already exists! Please try a different email")

    # Username field with length constraints and required validation
    username = StringField(
        label="Username:",
        validators=[
            DataRequired(),
            Length(min=2, max=30),
        ],
    )

    # Email field with required validation and proper email format check
    email_address = StringField(
        label="Email:",
        validators=[
            DataRequired(),
            Email(),
            Length(max=50),
        ],
    )

    # Password field with minimum length and required validation
    password1 = PasswordField(
        label="Password:",
        validators=[
            DataRequired(),
            Length(min=6, max=60),
        ],
    )

    # Confirm password field with match validation
    password2 = PasswordField(
        label="Confirm Password:",
        validators=[
            DataRequired(),
            EqualTo("password1"),
        ],
    )

    # Submit button
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    # Username field with required validation
    username = StringField(
        label="Username:",
        validators=[DataRequired()],
    )

    # Password field with required validation
    password = PasswordField(
        label="Password:",
        validators=[DataRequired()],
    )

    # Submit button
    submit = SubmitField(label="Sign In")


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item")


class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item")
