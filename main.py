import sqlite3


class ProjetoBD:
    def __init__(self,arquivo):
        self.connect = sqlite3.connect(arquivo)
        self.cursor = self.connect.cursor()
    # Função de inserção de código sql na base de dados
    def inserirPaginaDeCadastro(self,usuario,email,senha):
        consulta = 'INSERT OR IGNORE INTO pagina_de_cadastro (usuario,email,senha) VALUES (?,?,?)'
        self.cursor.execute(consulta,(usuario,email,senha))
        self.connect.commit()

    def inserirPaginaDeLogin(self,usuario,senha):
        consulta = 'INSERT OR IGNORE INTO pagina_de_login (usuario,senha) VALUES (?,?)'
        self.cursor.execute(consulta,(usuario,senha))
        self.connect.commit()
        # Função de edição de código sql na base de dados
    def editarPaginaDeLogin(self, usuario,senha,id):
        consulta = 'UPDATE OR IGNORE pagina_de_login SET usuario=?, senha=?, WHERE id=?'
        self.cursor.execute(consulta,(usuario,senha,id))
        self.connect.commit()
        # Função de exclusão de código sql na base de dados
    def excluirPaginaDeUsuario(self,id):
        consulta = 'DELETE FROM pagina_de_login WHERE id=?'
        self.cursor.execute(consulta,(id,))
        self.connect.commit()

    def excluirPaginaDeCadastro(self,id):
        consulta = 'DELETE FROM pagina_de_cadastro WHERE id=?'
        self.cursor.execute(consulta,(id,))
        self.connect.commit()
        # Função de listagem do código sql na base de dados
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
    #Instanciando Banco de dados
    projeto = ProjetoBD("banco.sqlite")
    #Inserindo dados na tabela de cadastro 
    projeto.inserirPaginaDeCadastro("Marcos",'marcos@gmail.com',"1345356")
    projeto.inserirPaginaDeCadastro("José",'josehenrique@gmail.com',"jose34563")
    projeto.inserirPaginaDeCadastro("Marcia",'marciacristina77@gmail.com',"soumarcia87532")
    projeto.inserirPaginaDeCadastro("Cristina Araujo",'araujocris@gmail.com',"crisujo857326")
    projeto.inserirPaginaDeCadastro("Flavio",'flavindopneu@gmail.com',"pneukkk")
    projeto.inserirPaginaDeCadastro("Kaun Nogueira",'kaunogueira@yahoo.com',"cristianomelhordomundo")

    #Inserindo dados na tabela de cadastro
    projeto.inserirPaginaDeLogin("Guilherme Barcelos","minecraft777squirtt")
    projeto.inserirPaginaDeLogin("Felipe Azevedo","73492Fe")
    projeto.inserirPaginaDeLogin("Vladimir Putin","Ukraniakkk")
    projeto.inserirPaginaDeLogin("Cabo Daciolo","gloriadeus")

    #Editando dados da tabela
    projeto.editarPaginaDeLogin("Guilherme Barcelos","gui1346345",1)
    projeto.editarPaginaDeLogin("Valerio Putin","uk123528",6)

    #Deletando dados da Tabela
    projeto.excluirPaginaDeCadastro(8)
    projeto.excluirPaginaDeUsuario(2)

    #Listando tabela
    projeto.listarPaginaDeCadastro()

    #Fechando a configuração de tabelas
    projeto.fechar()
