from Class_Agenda import * 

class Menu:
    def __init__(self):
        agenda_julia = Agenda()
        
        while True:
            entrada = input('Informe a opção desejada:' 
                            '\n1 - Novo contato' 
                            '\n2 - Listar contatos'
                            '\n3 - Alterar contato'
                            '\n0 - Sair\n')
            
            if entrada == '1':
                agenda_julia.salvar_contatos()
            elif entrada == '2':
                agenda_julia.mostrar_contatos()
            elif entrada == '3':
                agenda_julia.mudar_telefone()
            elif entrada == '0':
                break
            else:
                print('Opção inválida!')
