from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from models.user import User
from sqlalchemy import func

from models.user import db
from models.employee import Employee

employee_bp = Blueprint(
    "employee",
    __name__
)
@employee_bp.route("/dashboard")
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
        total_employees=total_employees,
        total_departments=total_departments,
        total_users=total_users
    )

# Step 4 - Employee List Route
@employee_bp.route("/employees")
def employees():

    if "user_id" not in session:
        return redirect("/")
    if session.get("role") != "admin":
        return "Access Denied"

    employee_list = Employee.query.all()

    return render_template(
        "employees.html",
        employees=employee_list
    )

# Step 5 - Add Employee Page
@employee_bp.route("/employee/add")
def add_employee_page():

    if "user_id" not in session:
        return redirect("/")

    if session.get("role") != "admin":
        return "Access Denied"

    return render_template(
        "add_employee.html"
    )


# Step 5 - Save Employee
@employee_bp.route(
    "/employee/add",
    methods=["POST"]
)
def add_employee():

    employee = Employee(
        name=request.form["name"],
        department=request.form["department"],
        salary=request.form["salary"]
    )

    db.session.add(employee)
    db.session.commit()

    return redirect("/employees")
@employee_bp.route("/employee/edit/<int:id>")
def edit_employee_page(id):

    if "user_id" not in session:
        return redirect("/")

    if session.get("role") != "admin":
        return "Access Denied"

    employee = Employee.query.get_or_404(id)

    return render_template(
        "edit_employee.html",
        employee=employee
    )


@employee_bp.route(
    "/employee/edit/<int:id>",
    methods=["POST"]
)
def edit_employee(id):

    employee = Employee.query.get_or_404(id)

    if session.get("role") != "admin":
     return "Access Denied"
    employee.name = request.form["name"]
    employee.department = request.form["department"]
    employee.salary = request.form["salary"]

    db.session.commit()

    return redirect("/employees")
@employee_bp.route("/employee/delete/<int:id>")
def delete_employee(id):

    if "user_id" not in session:
        return redirect("/")
    
    if session.get("role") != "admin":
        return "Access Denied"

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)

    db.session.commit()

    return redirect("/employees")