"""Script para criação do banco de dados necessario para testes no localhost
DEPRECIADO, APP CONECTADO A UM DB HOSTEADO NO RENDER
"""

#import mysql.connector
#from mysql.connector import errorcode

#print("Conectando...")
#try:
#      conn = mysql.connector.connect(
#            host='192.168.0.85',
#            user='nicolassreis',
#            password='senhauser'
#      )
#except mysql.connector.Error as err:
#      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#            print('Existe algo errado no nome de usuário ou senha')
#      else:
#            print(err)

#cursor = conn.cursor()

#cursor.execute("DROP DATABASE IF EXISTS `marvel_db`;")

#cursor.execute("CREATE DATABASE `marvel_db`;")

#cursor.execute("USE `marvel_db`;")

#TABLES = {}
#TABLES['Selecao'] = ('''
#      CREATE TABLE `selecao` (
#      `id` int(11) NOT NULL AUTO_INCREMENT,
#      `picture` varchar(400),
#     `name` varchar(50) NOT NULL,
#      `description` varchar(500),
#      PRIMARY KEY (`id`)
#      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

#TABLES['Vingadores'] = ('''
#      CREATE TABLE `vingadores` (
#      `id` int(11) NOT NULL AUTO_INCREMENT,
#      `picture` varchar(400),
#      `name` varchar(50) NOT NULL,
#      `description` varchar(500),
#      PRIMARY KEY (`id`)
#      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

#TABLES['Equipe'] = ('''
#      CREATE TABLE `equipe` (
#      `id` int(11) NOT NULL AUTO_INCREMENT,
#      `picture` varchar(400),
#      `name` varchar(50) NOT NULL,
#      `description` varchar(500),
#      PRIMARY KEY (`id`)
#      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

#for tabela_nome in TABLES:
#      tabela_sql = TABLES[tabela_nome]
#      try:
#            print('Criando tabela {}:'.format(tabela_nome), end=' ')
#            cursor.execute(tabela_sql)
#      except mysql.connector.Error as err:
#            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                  print('Já existe')
#            else:
#                  print(err.msg)
#      else:
#            print('OK')

#conn.commit()

#cursor.close()
#conn.close()