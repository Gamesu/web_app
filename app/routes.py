import os
from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/contacto", methods=["GET"])
def contacto():
    nombre = request.args.get("nombre", "")
    mensaje = request.args.get("mensaje", "")
    return render_template(
        "index.html",
        nombre=nombre,
        mensaje=mensaje,
        request_ip=request.remote_addr,
        script_path=os.path.abspath(__file__)
    )
