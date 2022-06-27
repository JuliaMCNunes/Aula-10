from Class_Contato import *

class Agenda:
    def __init__(self):
        self.lista_contatos = []
        
    
    def salvar_contatos(self):
        entrada_cod = input('Informe o código: ')
        entrada_nome = input('Informe o nome: ')
        entrada_telefone = input('Informe o telefone: ')
        self.lista_contatos.append(Contato(entrada_cod, entrada_nome, entrada_telefone))
        print('Contato salvo com sucesso!')
        
    def mostrar_contatos(self):
        for i in range(len(self.lista_contatos)):
            print('Código:', self.lista_contatos[i].cod, ' Nome:', self.lista_contatos[i].nome, ' Telefone:', self.lista_contatos[i].telefone)

    def mudar_telefone(self):
        cont = 0
        contato = input('Informe o nome da pessoa: ')
        for i in range(len(self.lista_contatos)):
            if self.lista_contatos[i].nome == contato:
                novo_telefone = input('Informe o novo telefone: ')
                self.lista_contatos[i].telefone = novo_telefone
            else:
                cont += 1
                if cont == len(self.lista_contatos):
                    print('Contato inexistente!')
            