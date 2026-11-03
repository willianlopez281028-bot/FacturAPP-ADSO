"""Rutas HTTP para la administración de usuarios de demostración."""
from flask import Blueprint, abort, current_app, flash, redirect, render_template, request, url_for

from src.services.users.user_service import UserService, UserValidationError, ALLOWED_ROLES

users_bp = Blueprint("users", __name__, url_prefix="/users")


def _service():
    return UserService(current_app.extensions["user_repository"])


@users_bp.get("/")
def list_users():
    search = request.args.get("q", "")
    users = _service().list_users(search)
    return render_template("users/index.html", users=users, search=search, active_page="users")


@users_bp.route("/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        confirmation = request.form.get("password_confirmation", "")
        role = request.form.get("role", "")
        if password != confirmation:
            flash("Las contraseñas no coinciden.", "danger")
        else:
            try:
                _service().create_user(username, password, role)
                flash("Usuario creado correctamente.", "success")
                return redirect(url_for("users.list_users"))
            except UserValidationError as error:
                flash(str(error), "danger")
        return render_template("users/form.html", user=None, roles=ALLOWED_ROLES,
                               form_data=request.form, active_page="users")
    return render_template("users/form.html", user=None, roles=ALLOWED_ROLES,
                           form_data={}, active_page="users")


@users_bp.route("/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    service = _service()
    user = service.get_user(user_id)
    if not user:
        abort(404)
    if request.method == "POST":
        try:
            service.update_user(
                user_id,
                request.form.get("username", ""),
                request.form.get("role", ""),
                request.form.get("is_active") == "1",
            )
            flash("Usuario actualizado correctamente.", "success")
            return redirect(url_for("users.list_users"))
        except UserValidationError as error:
            flash(str(error), "danger")
            user.username = request.form.get("username", user.username)
            user.role = request.form.get("role", user.role)
            user.is_active = request.form.get("is_active") == "1"
    return render_template("users/form.html", user=user, roles=ALLOWED_ROLES,
                           form_data={}, active_page="users")


@users_bp.post("/<int:user_id>/password")
def reset_password(user_id):
    password = request.form.get("password", "")
    confirmation = request.form.get("password_confirmation", "")
    if password != confirmation:
        flash("Las contraseñas no coinciden.", "danger")
    else:
        try:
            _service().change_password(user_id, password)
            flash("Contraseña actualizada correctamente.", "success")
        except UserValidationError as error:
            flash(str(error), "danger")
    return redirect(url_for("users.edit_user", user_id=user_id))
