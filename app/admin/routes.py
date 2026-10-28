from flask import Blueprint

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/panel")
def panel():
    return "Bienvenido al panel de administracion"