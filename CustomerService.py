# ur/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
import Conexao
import Customer

class CustomerService:
    def __init__(self, Host, usuario, senha, database):
        self.__bd = Conexao.BD(Host,usuario,senha)
        self.__cursor = self.__bd.getCursor()
        self.__cursor.execute("use {0}".format(database))
    def salvar(self, id, cpf_cnpj, nome, status, valor):
        sql = """insert into tb_customer_account values({0},'{1}','{2}',{3},{4});""".format(id,cpf_cnpj,nome,status,valor)
        try:
            self.__cursor.execute(sql)
            self.__bd.commit()
            print("Inserção bem sucedida")
        except:
            self.__bd.close()
            print("Inserção mal sucedida")

    def selecao(self):
        sql = """select * from tb_customer_account where vl_total > 560 and id_customer between 1500 and 2700 order by vl_total desc;"""
        customers = []

        self.__cursor.execute(sql)
        results = self.__cursor.fetchall()
        for row in results:
            id = row[0]
            cpf_cnpj = row[1]
            nome = row[2]
            status = row[3]
            valor = row[4]
            customers.append(Customer.Customer(id, cpf_cnpj, nome, status, valor))

        return customers

    def encerra(self):
        self.__bd.close()
