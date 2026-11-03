from flask import Blueprint, render_template

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/form_clients')
def form_clients():
    return render_template('clients/form_clients.html')

@clients_bp.route('/list_clients')
def list_clients():
    return render_template('/clients/list_clients.html')
