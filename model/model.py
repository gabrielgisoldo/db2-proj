# -*- coding: utf-8 -*-
from model.db.db import DB
from datetime import datetime
from bson.objectid import ObjectId
import base64 as b64


class Model(object):
    """docstring for Model."""

    def __init__(self):
        """."""
        self.banco = DB()

    def inserir_paciente(self, cpf, nome):
        """."""
        t = {'cpf': cpf, 'nome': nome, 'data_criacao': datetime.now()}
        id_pac = self.banco.get_db_pac().insert_one(t).inserted_id
        return id_pac

    def inserir_img_paciente(self, id_paciente, nome_imagem, imagem):
        """."""
        if not nome_imagem or not imagem:
            return None
        id_paciente = ObjectId(id_paciente)
        t = {'id_paciente': id_paciente,
             'nome_imagem': nome_imagem, 'binario': imagem.read()}
        id_img = self.banco.get_db_img().insert_one(t).inserted_id
        return id_img

    def buscar_pacientes(self):
        """."""
        return self.banco.get_db_pac().find()

    def buscar_paciente(self, id_pac):
        """."""
        id_pac = ObjectId(id_pac)
        r = self.banco.get_db_pac().find_one({'_id': id_pac})
        img = self.banco.get_db_img().find({'id_paciente': id_pac})
        r['imagens'] = [i for i in img]
        for item in r['imagens']:
            item['b64'] = b64.b64encode(item['binario']).decode()
        return r
