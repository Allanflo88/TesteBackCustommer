# ur/bin/python3
# -*- coding: utf-8 -*-

import CustomerService
import Customer


#Host = raw_input("Host: ")
#usuario = raw_input("User: ")
#senha = raw_input("Password: ")
#database = raw_input("Database: ")
#service = CustomerService.CustomerService(Host,usuario, senha, database)

service = CustomerService.CustomerService("localhost","root", "Andreia16", "Testes")
customers = []

x = input("Digite o total de clientes a serem cadastrados: ")

for i in range(x):
    status = 2
    id = input("ID: ")
    registro = raw_input("CPF ou CNPJ: ")
    nome = raw_input("Nome: ")
    valor = input("Valor total: ")
    while(status != 0 and status != 1):
        status = input("Digite 1 para ativo ou 0 para não ativo: ")
    service.salvar(id,registro,nome,status,valor)

customers = service.selecao()
service.encerra()

for i in range(len(customers)):
    print("ID: " + str(customers[i].getId()))
    print("CPF_CNPJ: " + str(customers[i].getCpf_cnpj()))
    print("Nome: " + str(customers[i].getNome()))
    print("Status: " + str(customers[i].getStatus()))
    print("Valor: " + str(customers[i].getValor()))
    print("\n")
