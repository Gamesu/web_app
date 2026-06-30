import os
from flask import Blueprint, render_template, request
from app.database import get_db

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/contacto", methods=["GET"])
def contacto():
    nombre = request.args.get("nombre", "")
    mensaje = request.args.get("mensaje", "")
    ip = request.remote_addr

    conn = get_db()
    conn.execute(f"INSERT INTO mensajes (nombre, mensaje, ip) VALUES ('{nombre}', '{mensaje}', '{ip}')")
    conn.commit()
    conn.close()

    return render_template(
        "index.html",
        nombre=nombre,
        mensaje=mensaje,
        request_ip=ip,
        script_path=os.path.abspath(__file__),
        enviado=True
    )

@main.route("/admin/mensajes")
def listar_mensajes():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM mensajes")
    mensajes = cursor.fetchall()
    conn.close()
    return render_template("mensajes.html", mensajes=mensajes)
