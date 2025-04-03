print('=-'*15)
print(' SISTEMA DE SUSTENTABILIDADE')
print('=-'*15)

rodar_novamente = True

while rodar_novamente:    
    while True: #TESTE DE VALIDAÇÃO DA DATA
        try:
            print('Escreva uma data seguindo o modelo (dia/mês/ano)\n ex: (20/11/2025)')
            data_str = input('Qual é a data: ')
            dia, mes, ano = data_str.split("/")
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
        except ValueError:
            print('\033[91mA data precisa ser numérica\033[0m')
        else:
            if ano < -45: #anos antes de -45 não são válidos
                print('\033[91mData inválida\033[0m')
                print('O ano é anterior a -45 e deve ser considerado inválido')
            elif  ano == 0: #ano zero não existiu
                print('\033[91mData inválida\033[0m')
                print('O ano zero não existiu')
            elif mes > 12 or mes < 1:
                print('\033[91mData inválida\033[0m')
                print('Os meses do ano vão de 1 a 12')
            elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
                print('\033[91mData inválida\033[0m') #meses com mais de 31 dias são inválidos
            elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30: 
                print('\033[91mData inválida\033[0m') #meses 4,6,9,11 com mais de 30 dias são inválidos
            elif mes == 2 and dia > 29: #fevereiro com mais de 29 dias é inválido
                print('\033[91mData inválida\033[0m')
            elif mes == 2 and dia == 29 and (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)):
                print('\033[91mData inválida\033[0m') #nos anos b
            elif dia < 1 or mes < 1: #os dias e os meses precisam ser maiores que 1
                print('\033[91mData inválida\033[0m')
            elif (ano == 1582) and (mes == 10) and dia >= 5 and dia <= 14: #dias inválidos devido à reforma do calendário
                print('\033[91mData inválida\033[0m')
                print('*Esse dia faz parte da reforma do calendário e não existiu.')
            else:
                print('\033[92mData válida\033[0m')
                break
    #SEGUNDA PERGUNTA (SOBRE CONSUMO DE ÁGUA)
    while True:
        try:
            consumo_de_agua = float(input('Quantos litros de água você consumiu hoje? (Aprox. em litros): '))
        except ValueError:
            print('\033[91mO valor precisa ser numérico\033[0m')
        else:
            break
    #TERCEIRA PERGUNTA (SOBRE KWH DE ENERGIA)
    while True:
        try:
            kWh = float(input('Quantos kWh de energia elétrica você consumiu hoje?: '))
        except ValueError:
            print('\033[91mO valor precisa ser numérico\033[0m')
        else:
            break
    #QUARTA PERGUNTA (SOBRE QUANTIDADE DE KG DE RESÍDUOS NÃO RECICLÁVEIS)
    while True:
        try:
            kg_de_residuos = float(input('Quantos kg de resíduos não recicláveis você gerou hoje?: '))
        except ValueError:
            print('\033[91mO valor precisa ser numérico\033[0m')
        else:
            break
    #QUINTA PERGUNTA (SOBRE PORCENTAGEM DE RESÍDUOS RECICLADOS NO TOTAL)
    while True:
        try:
            porcentagem_de_residuos_reciclaveis = int(input('Qual a porcentagem de resíduos reciclados no total (em %)?: '))
        except ValueError:
            print('\033[91mO valor precisa ser numérico\033[0m')
        else:
            break
    #SEXTA PERGUNTA (SOBRE O MEIO DE TRASPORTE ULTILIZADO)
    while True:
        try:
            meio_de_trasporte = int(input('Qual o meio de transporte você usou hoje?: \n'
        '[1] Transporte público (ônibus, metrô, trem)\n'
        '[2] Bicicleta\n'
        '[3] Caminhada\n'
        '[4] Carro (combustível fósseis)\n'
        '[5] Carro elétrico\n'
        '[6] Carona compartilhada\n'
        'Resp: '))
        except ValueError:
            print('\033[91mO valor precisa ser numérico\033[0m')
        else:
            if meio_de_trasporte < 1 or meio_de_trasporte > 6:
                print('\033[91mA opção escolhida deve estar no intervalo de 1 a 6\033[0m')
            else:
                break
    #FEEDBACK DAS PERGUNTAS
    print('=-'*14)
    print('  FEEDBACK DAS PERGUNTAS')
    print('=-'*14)
    #RESULTADO DO CONSUMO DE ÁGUA
    if consumo_de_agua < 150:
        print('Consumo de água: \033[92mAlta sustentabilidade.\033[0m')
    elif consumo_de_agua >= 150 and consumo_de_agua <= 200:
        print('Consumo de água: \033[93mModerada sustentabilidade.\033[0m')
    elif consumo_de_agua > 200:
        print('Consumo de água: \033[91mBaixa sustentabilidade.\033[0m')
    #RESULTADO DO CONSUMO DE ENERGIA ELÉTRICA
    if kWh < 5:
        print('Consumo de energia: \033[92mAlta sustentabilidade.\033[0m')
    elif kWh >= 5 and kWh <= 10:
        print('Consumo de energia: \033[93mModerada sustentabilidade.\033[0m')
    elif kWh > 10:
        print('Consumo de energia: \033[91mBaixa sustentabilidade.\033[0m')
    #RESULTADO PORCENTAGEM DA GERAÇÃO DE RESÍDUOS NÃO RECICLÁVEIS
    if porcentagem_de_residuos_reciclaveis > 50:
        print('Geração de Resíduos Não Recicláveis: \033[92mAlta sustentabilidade.\033[0m')
    elif porcentagem_de_residuos_reciclaveis >= 20 and porcentagem_de_residuos_reciclaveis <= 50:
        print('Geração de Resíduos Não Recicláveis: \033[93mModerada sustentabilidade.\033[0m')
    elif porcentagem_de_residuos_reciclaveis < 20:
        print('Geração de Resíduos Não Recicláveis: \033[91mBaixa sustentabilidade.\033[0m')
    #RESULTADO DO TIPO DE TRASPORTE ULTILIZADO
    if meio_de_trasporte == 2 or meio_de_trasporte == 3 or meio_de_trasporte == 5:
        print('Uso de transporte: \033[92mAlta sustentabilidade.\033[0m')
    elif meio_de_trasporte == 6 or meio_de_trasporte == 1:
        print('Uso de trasporte: \033[93mModerada sustantabilidade.\033[0m')
    elif meio_de_trasporte == 4:
        print('Uso de transporte: \033[91mBaixa sustentabilidade.\033[0m')
    while True:
        continuar = input('Você gostaria de rodar novamente? (SIM ou NAO): ').strip().upper()
        if continuar not in ['SIM', 'NAO']:
            print("Digite novamente: SIM ou NAO")
        elif continuar == 'NAO':
            print("Encerrando o programa.")           
            rodar_novamente = False     
            break                
        else:
            print("Reiniciando...")
            # Aqui você pode colocar um `break` ou reiniciar o programa dependendo da lógica desejada
            break