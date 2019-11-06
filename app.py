# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, url_for, redirect
import os
from controller.controller import Controller

app = Flask(__name__)
controller = Controller()


@app.errorhandler(404)
def not_found(error):
    """Pagina not found."""
    return jsonify('Not Found.')


@app.route('/', methods=["GET"])
def index_html(erro=""):
    """Pagina principal da aplicacao."""
    pacientes = controller.buscar_pacientes()
    return render_template('index.html', pacientes=pacientes)


@app.route('/adicionar_paciente', methods=["GET"])
def adicionar_paciente():
    """."""
    return render_template('add_pac.html')


@app.route('/gravar_paciente', methods=["POST"])
def gravar_paciente():
    """."""
    controller.gravar_pac()
    return redirect(url_for('index_html'))


@app.route('/ver_paciente/<id_paciente>', methods=["GET"])
def ver_paciente(id_paciente):
    """."""
    paciente = controller.buscar_paciente(id_paciente)
    return render_template('paciente.html', paciente=paciente)


@app.route('/add_img_paciente', methods=["POST"])
def add_img_paciente():
    """."""
    r = controller.inserir_img()
    return redirect(r)


port = int(os.environ.get('PORT', "5000"))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, use_reloader=True)
