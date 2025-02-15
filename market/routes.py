from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegistrationForm
from market import db


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a new user instance
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=form.password1.data,
        )

        # Add the user to the session and commit the changes to the database
        db.session.add(user_to_create)
        db.session.commit()

        # Redirect to the market page after successful registration
        return redirect(url_for("market_page"))

    if form.errors != {}:  # If there are errors from the validations
        for field, err_msgs in form.errors.items():  # Loop through form errors
            for err_msg in err_msgs:  # Each field might have multiple errors
                flash(err_msg, category="danger")

    return render_template("register.html", form=form)
