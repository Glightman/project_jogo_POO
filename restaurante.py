from relogio import Relogio
relogio = Relogio()


def cardapio(self):
    bife = 0
    frango = 0
    suco = 0
    agua = 0

    while True:
        opcao = int(input(''' SEJA BEM VINDO!!
        EM NOSSO CARDAPIO TEMOS AS SEGUINTES OPÇÕES:
        [ 1 ] PF BIFE COM BATATA FRITA....... R$ 18,00
        [ 2 ] PF FRANGO A PASSARINHO......... R$ 15,00
        [ 3 ] SUCO DE LARANJA  500ML......... R$  8,00
        [ 4 ] ÁGUA MINERAL S/ GAS  510ML......R$  4,00
        [ 0 ] CONFIRMAR PEDIDO
        FAÇA SEU PEDIDO
        '''))
        soma = (bife * 18.0) + ( frango * 15.0) + (suco * 8.0) + (agua * 4.0)
        if opcao == 1 :
            bife += 1
        elif opcao == 2 :
            frango += 1
        elif opcao == 3:
            suco += 1
        elif opcao == 4:
            agua += 1
        elif opcao == 0:
            print(f'''POR FAVOR CONFIRME O PEDIDO:
            [{bife} ] PF BIFE COM BATATA FRITA
            [ {frango} ] PF FRANGO A PASSARINHO
            [ {suco} ] SUCO DE LARANJA  500ML
            [ {agua} ] ÁGUA  500ML     

            ''')
            per = ('''VOCÊ CONFIRMA O PEDIDO?
            [ 1 ] SIM
            [ 0 ] NÃO
            ''')
            if per == 1:
                print(f'''SEU PEDIDO SERÁ PREPARADO, 
                APÓS A CONFIRMAÇÃO DE PAGAMENTO
                O VALOR TOTAL É DE R$ {soma:.2f}''').replace('.',',')
                if self.dinheiro() < soma:
                    print('VOCÊ NÃO POSSUI DINHEIRO SUFICIENTE')
        else:
            print('NÚMERO INVÁLIDO. TENTE NOVAMENTE')
            





            

    
            