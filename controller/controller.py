# -*- coding: utf-8 -*-
from model.model import Model
from flask import request


class Controller(object):
    """docstring for Controller"""

    def __init__(self):
        """."""
        self.model = Model()

    def buscar_pacientes(self):
        """."""
        return self.model.buscar_pacientes()

    def gravar_pac(self):
        """."""
        nome = request.form.get('nome_paciente')
        cpf = request.form.get('cpf')
        imagens = request.files.getlist('imagens')

        id_pac = self.model.inserir_paciente(cpf, nome)

        for item in imagens:
            self.model.inserir_img_paciente(
                id_paciente=id_pac, nome_imagem=item.filename, imagem=item)

    def buscar_paciente(self, id_paciente):
        """."""
        return self.model.buscar_paciente(id_paciente)
