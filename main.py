import sqlite3


class ProjetoBD:
    def __init__(self,arquivo):
        self.connect = sqlite3.connect(arquivo)
        self.cursor = self.connect.cursor()

    def inserirPaginaDeCadastro(self,usuario,email,senha):
        consulta = 'INSERT OR IGNORE INTO pagina_de_cadastro (usuario,email,senha) VALUES (?,?,?)'
        self.cursor.execute(consulta,(usuario,email,senha))
        self.connect.commit()

    def inserirPaginaDeLogin(self,usuario,senha):
        consulta = 'INSERT OR IGNORE INTO pagina_de_login (usuario,senha) VALUES (?,?)'
        self.cursor.execute(consulta,(usuario,senha))
        self.connect.commit()

    def editarPaginaDeLogin(self, usuario,senha,id):
        consulta = 'UPDATE OR IGNORE pagina_de_login SET usuario=?, senha=?, WHERE id=?'
        self.cursor.execute(consulta,(usuario,senha,id))
        self.connect.commit()

    def excluirPaginaDeUsuario(self,id):
        consulta = 'DELETE FROM pagina_de_login WHERE id=?'
        self.cursor.execute(consulta,(id,))
        self.connect.commit()

    def excluirPaginaDeCadastro(self,id):
        consulta = 'DELETE FROM pagina_de_cadastro WHERE id=?'
        self.cursor.execute(consulta,(id,))
        self.connect.commit()

    def listarPaginaDeCadastro(self):
        self.cursor.execute('SELECT * FROM pagina_de_cadastro')

        for linha in self.cursor.fetchall():
            print(linha)

    def listarPaginaDeLogin(self):
        self.cursor.execute('SELECT * FROM pagina_de_login')
        
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.connect.close()


if __name__ == "__main__":
    projeto = ProjetoBD("banco.sqlite")
    projeto.inserirPaginaDeCadastro("Marcos",'marcos@gmail.com',"1345356")
    projeto.listarPaginaDeCadastro()
