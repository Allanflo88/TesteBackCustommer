# ur/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb

class BD:
    def __init__(self, Host, usuario, senha):
        self.__con = MySQLdb.connect(host=Host,user=usuario,passwd=senha)
        self.__cursor = self.__con.cursor()

    def getCursor(self):
        return self.__cursor

    def close(self):
        self.__con.close()

    def commit(self):
        return self.__con.commit()
