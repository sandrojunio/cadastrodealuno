import sqlite3
from ConexaoBanco import Conexao

class Cadastro_Assunto:

    def insert(self, nomeAssunto):
        
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            #SQL para inserir os dados no banco de dados.
            sql = 'INSERT INTO Assunto (nomeAssunto) VALUES (?)'

            cursor.execute(sql, [nomeAssunto])
        
            conexao.commit()
            cursor.close()
            conexao.close()

            return "Cadastrado com sucesso!"
        except:
            return "Erro ao inserir aluno!"