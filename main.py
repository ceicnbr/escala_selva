#escala de selva
import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password='',
    database='escala_sv',
)
cursor= conexao.cursor()
comando = 'INSERT INTO soldados (nome_soldado, nm_soldado) VALUE ("adiel", "297")'
cursor.execute(comando)
conexao.commit()









cursor.close()
conexao.close()