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
            DataRequired(message="Username is required."),
            Length(
                min=2, max=30, message="Username must be between 2 and 30 characters."
            ),
        ],
    )

    # Email field with required validation and proper email format check
    email_address = StringField(
        label="Email:",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Invalid email address."),
            Length(max=50, message="Email must be less than 50 characters."),
        ],
    )

    # Password field with minimum length and required validation
    password1 = PasswordField(
        label="Password:",
        validators=[
            DataRequired(message="Password is required."),
            Length(
                min=6, max=60, message="Password must be between 6 and 60 characters."
            ),
        ],
    )

    # Confirm password field with match validation
    password2 = PasswordField(
        label="Confirm Password:",
        validators=[
            DataRequired(message="Please confirm your password."),
            EqualTo("password1", message="Passwords must match."),
        ],
    )

    # Submit button
    submit = SubmitField(label="Create Account")
