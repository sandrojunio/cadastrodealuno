import sqlite3
from ConexaoBanco import Conexao

class home_db:

    def selectAluno(self):

        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:    
            #Consultar todo o banco
            sql = "SELECT * FROM Aluno ORDER BY nomeAluno ASC"
            resultado = cursor.execute(sql).fetchall()

            cursor.execute(sql)
            conexao.close()

            return resultado
        except:
            return "Ops! Ocorreu um erro na consulta dos regitros!"