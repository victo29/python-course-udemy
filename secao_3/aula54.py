lista_de_compras = []

while True:
    opcao = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar:' ).upper()
    if opcao == 'I':
        item_inserido  = input("Digite o item: ")
        if len(item_inserido) > 1:
            lista_de_compras.append(item_inserido)
    elif opcao == 'A':
        if len(lista_de_compras )> 0:
            indice_do_item = input('Digite o índice do item a ser excluido: ')
            try:
                indice_do_item = int(indice_do_item)
                lista_de_compras.pop(indice_do_item)
                print('Item apagado com sucesso!')
            except ValueError:
                print('O valor digitado não é um número!')
            except IndexError:
                print('O indice inserido não está presente na lista!')
        else: 
            print('lista vazia!')
    elif opcao == 'L':
        if len(lista_de_compras) > 0:
            for indice, item in enumerate(lista_de_compras):
                print(indice,'-',item)
        else:
            print('lista vazia!')
    else:
        print('Nenhuma das opções foi selecionada!')
            