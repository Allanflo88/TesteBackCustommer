# ur/bin/python3
# -*- coding: utf-8 -*-

class Customer:
    def __init__(self, id, cpf_cnpj, nome, status, valor):
        self.__id = id
        self.__cpf_cnpj = cpf_cnpj
        self.__nome = nome
        self.__status = status
        self.__valor = valor

    def getId(self):
        return self.__id

    def getCpf_cnpj(self):
        return self.__cpf_cnpj

    def getNome(self):
        return self.__nome

    def getStatus(self):
        return self.__status

    def getValor(self):
        return self.__valor
