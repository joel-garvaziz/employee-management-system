from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from models.employee import Employee
from sqlalchemy import func

from flask_bcrypt import Bcrypt

from models.user import db
from models.user import User

auth_bp = Blueprint(
    "auth",
    __name__
)

bcrypt = Bcrypt()


@auth_bp.route("/")
def home():
    return render_template("login.html")


@auth_bp.route("/register")
def register_page():
    return render_template("register.html")


@auth_bp.route("/register", methods=["POST"])
def register():

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return redirect("/")


@auth_bp.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(
        email=email
    ).first()

    if user and bcrypt.check_password_hash(
        user.password,
        password
    ):

        session["user_id"] = user.id
        session["username"] = user.username
        session["role"] = user.role

        return redirect("/dashboard")

    return "Invalid Credentials"


@auth_bp.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/")

    total_employees = Employee.query.count()

    total_departments = (
        db.session.query(
            func.count(
                func.distinct(Employee.department)
            )
        ).scalar()
    )

    total_users = User.query.count()

    return render_template(
        "dashboard.html",
        username=session["username"],
        role=session["role"],
        total_employees=total_employees,
        total_departments=total_departments,
        total_users=total_users
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/")