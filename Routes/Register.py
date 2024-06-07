from flask import Blueprint, jsonify, request
from Controllers.RegisterController import RegisterController

cont = RegisterController()

register = Blueprint('register',__name__)

@register.route("/register", methods = ['POST'])
def create_register():
    data = request.get_json()
    return jsonify(cont.create(data))