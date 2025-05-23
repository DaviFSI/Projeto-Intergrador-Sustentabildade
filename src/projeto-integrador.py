import sys
import os
import re

#Adiciona a pasta "banco" ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banco')))

from conexao import conexao, cursor

def inserir_Valores(nome,consumo_de_agua,kWh , kg_de_residuos, porcentagem_de_residuos_reciclaveis, meio_de_trasporte,data_str):
    sql = """
            insert into dados_consumo(nome,consumo_de_agua,kwh,kg_de_residuos,porcentagem_de_residuos_reciclaveis,meio_de_trasporte,dt_digitada,dt_insercao)
            VALUES (%s,%s, %s, %s, %s, %s, %s,NOW())
            """
    valores = (nome,consumo_de_agua,kWh , kg_de_residuos, porcentagem_de_residuos_reciclaveis, meio_de_trasporte,data_str)
    cursor.execute(sql, valores)
    conexao.commit()
def pegar_valores(nome):
        sql = """select * from dados_consumo where nome=%s ORDER BY dt_insercao desc """
        valores=(nome,)
        cursor.execute(sql,valores)    
        resultados = cursor.fetchall()
       
    
        return  resultados

def atualizar_valores(consumo_de_agua,kWh, kg_de_residuos, porcentagem_de_residuos_reciclaveis, meio_de_trasporte,data_str,idd):
    sql = """UPDATE  dados_consumo 
                SET consumo_de_agua =%s,
                kwh=%s,
                kg_de_residuos=%s,
                porcentagem_de_residuos_reciclaveis=%s,
                meio_de_trasporte=%s,
                dt_digitada=%s
                    where id=%s """
    valores = (consumo_de_agua,kWh,kg_de_residuos,porcentagem_de_residuos_reciclaveis,meio_de_trasporte,data_str,idd)
    cursor.execute(sql, valores)
    conexao.commit()
def deletar_valores(id):
    sql = """DELETE FROM dados_consumo WHERE id=%s"""
    valores = (id,)
    cursor.execute(sql, valores)
    conexao.commit()

def validar_nome(nome):
    padrao = r"^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*$"
    return re.fullmatch(padrao, nome) is not None
      

print('=-'*15)
print(' SISTEMA DE SUSTENTABILIDADE')
print('=-'*15)


rodar_novamente_programa = True
while rodar_novamente_programa:           
    menu = True  
    while menu:
        rodar_novamente_resgistrar = True
        nome =''
        try:
            menuresp = int(input('Selecione a opção que deseja: \n'
            '[1] Registrar Dados\n'
            '[2] Consultar Dados\n'
            '[3] Deletar Dados\n'
            '[4] Atualizar Dados\n'
            '[5] Encerrar o Programa\n'
            'Resp: '))
        except ValueError:
                print('\033[91mO valor precisa ser numérico\033[0m')
        else:
            if menuresp < 1 or menuresp > 5:
                    print('\033[91mA opção escolhida deve estar no intervalo de 1 a 5\033[0m')
            else:
                if menuresp == 1:
                    while rodar_novamente_resgistrar :
                        data_while = True
                        agua = True
                        kWH_while =True
                        kg_residuos = True
                        residuos_reciclaveis= True
                        transporte= True
                        novamente= True
                        user_while= True
                        while user_while :
                            try: 
                                nome = input('Digite seu nome (Lembre-se dele para consultar dados)')
                            except ValueError:
                                print('\033[91mO valor precisa ser numérico\033[0m')  
                            else: 
                                if validar_nome(nome):
                                    print("Nome válido!")
                                    user_while= False
                                else:
                                    print("Nome inválido.")          
                        while data_while : #TESTE DE VALIDAÇÃO DA DATA
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
                                    data_while = False
                        #SEGUNDA PERGUNTA (SOBRE CONSUMO DE ÁGUA)
                        while agua:
                            try:
                                consumo_de_agua = float(input('Quantos litros de água você consumiu hoje? (Aprox. em litros): ').replace(',', '.'))
                            except ValueError:
                                print('\033[91mO valor precisa ser numérico\033[0m')
                            else:
                                if consumo_de_agua < 0:
                                    print('\033[91mO valor deve ser positivo\033[0m')
                                else:
                                    agua = False
                        #TERCEIRA PERGUNTA (SOBRE KWH DE ENERGIA)
                        while kWH_while :
                            try:
                                kWh = float(input('Quantos kWh de energia elétrica você consumiu hoje?: ').replace(',', '.'))
                            except ValueError:
                                print('\033[91mO valor precisa ser numérico\033[0m')
                            else:
                                if kWh < 0:
                                    print('\033[91mO valor deve ser positivo\033[0m')
                                else:
                                    kWH_while= False
                        #QUARTA PERGUNTA (SOBRE QUANTIDADE DE KG DE RESÍDUOS NÃO RECICLÁVEIS)
                        while kg_residuos:
                            try:
                                kg_de_residuos = float(input('Quantos kg de resíduos não recicláveis você gerou hoje?: ').replace(',', '.'))
                            except ValueError:
                                print('\033[91mO valor precisa ser numérico\033[0m')
                            else:
                                if kg_de_residuos < 0:
                                    print('\033[91mO valor deve ser positivo\033[0m')
                                else:
                                    kg_residuos = False
                        #QUINTA PERGUNTA (SOBRE PORCENTAGEM DE RESÍDUOS RECICLADOS NO TOTAL)
                        while residuos_reciclaveis:
                            try:
                                porcentagem_de_residuos_reciclaveis = int(input('Qual a porcentagem de resíduos reciclados no total (em %)?: '))
                            except ValueError:
                                print('\033[91mO valor precisa ser numérico\033[0m')
                            else:
                                if porcentagem_de_residuos_reciclaveis < 0:
                                    print('\033[91mO valor deve ser positivo\033[0m')
                                else:
                                    residuos_reciclaveis= False
                        #SEXTA PERGUNTA (SOBRE O MEIO DE TRASPORTE ULTILIZADO)
                        while transporte:
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
                                    inserir_Valores(nome,consumo_de_agua,kWh , kg_de_residuos, porcentagem_de_residuos_reciclaveis, meio_de_trasporte,data_str)    
                                    print('ok')
                                    transporte =False                                    
                        filtro_denovo = True
                        while filtro_denovo:
                            continuar_registrar = input('Você gostaria de Registrar Novamente? (SIM ou NAO): ').strip().upper()
                            if continuar_registrar not in ['SIM', 'NAO']:
                                    print("Digite novamente: SIM ou NAO")
                            elif continuar_registrar == 'NAO':                       
                                rodar_novamente_resgistrar = False
                                filtro_denovo =False
                            else:
                                filtro_denovo =False
                         
                                                
                                                           
                elif menuresp == 2 :                          
                    #FEEDBACK DAS PERGUNTAS
                    print('=-'*14)
                    print('  FEEDBACK DAS PERGUNTAS')
                    print('=-'*14)
                    #RESULTADO DO CONSUMO DE ÁGUA
                    consulta_reg=True
                    while consulta_reg:
                        try:
                            nome = input('Digite o nome que deseja procurar : ')
                        except ValueError:
                            print('\033[91mO valor precisa ser texto\033[0m')
                        else:
                            valores = pegar_valores(nome)
                            if valores ==[]:
                                print('\033[91mO Esse nome não existe\033[0m')
                            else:
                                registro_while=True
                                while registro_while:
                                    for i in range(len(valores)):
                                        print('['+str(valores[i]['id'])+']-'+str(valores[i]['dt_insercao']))
                                    try:
                                            opcao = int(input("Selecione o ID que você quer CONSULTAR: "))
                                    except ValueError:
                                         print('\033[91mO valor precisa ser numérico\033[0m')
                                    else:
                                       for i in range(len(valores)):
                                            if valores[i]['id']== opcao:                                           
                                                
                                                consumo_de_agua = valores[i]['consumo_de_agua']
                                                kWh = valores[i]['kwh']
                                                porcentagem_de_residuos_reciclaveis= valores[i]['porcentagem_de_residuos_reciclaveis']
                                                meio_de_trasporte =  valores[i]['meio_de_trasporte']
                                                
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
                                                    print('valor valido')
                                                registro_while= False    
                        filtro_denovo = True
                        while filtro_denovo:
                            continuar_registrar = input('Você gostaria de CONSULTAR de novo (SIM ou NAO): ').strip().upper()
                            if continuar_registrar not in ['SIM', 'NAO']:
                                    print("Digite novamente: SIM ou NAO")
                            elif continuar_registrar == 'NAO':                                                     
                                filtro_denovo= False
                                consulta_reg =False
                            else:
                                filtro_denovo= False
                elif menuresp == 3:
                    consulta_reg=True
                    while consulta_reg:
                        try:
                            nome = input('Digite o nome que deseja procurar : ')
                        except ValueError:
                            print('\033[91mO valor precisa ser texto\033[0m')
                        else:
                            valores = pegar_valores(nome)
                            if valores ==[]:
                                print('\033[91mO Esse nome não existe\033[0m')
                            else:
                                registro_while=True
                                while registro_while:
                                    for i in range(len(valores)):
                                        print('['+str(valores[i]['id'])+']-'+str(valores[i]['dt_insercao']))
                                    try:
                                            opcao = int(input("Selecione o ID que você quer DELETAR: "))
                                    except ValueError:
                                         print('\033[91mO valor precisa ser numérico\033[0m')
                                    else:
                                       for i in range(len(valores)):
                                            if valores[i]['id']== opcao:
                                                deletar_valores(opcao)
                                                registro_while = False
                        filtro_denovo = True
                        while filtro_denovo:
                            continuar_registrar = input('Você gostaria de DELETAR outros dados (SIM ou NAO): ').strip().upper()
                            if continuar_registrar not in ['SIM', 'NAO']:
                                    print("Digite novamente: SIM ou NAO")
                            elif continuar_registrar == 'NAO':                                                     
                                filtro_denovo= False
                                consulta_reg =False
                            else:
                                filtro_denovo= False                
                                                
                elif menuresp == 4:
                    consulta_reg=True
                    while consulta_reg:
                        try:
                            nome = input('Digite o nome que deseja procurar : ')
                        except ValueError:
                            print('\033[91mO valor precisa ser texto\033[0m')
                        else:
                            valores = pegar_valores(nome)
                            if valores ==[]:
                                print('\033[91mO Esse nome não existe\033[0m')
                            else:
                                registro_while=True
                                while registro_while:
                                    for i in range(len(valores)):
                                        print('['+str(valores[i]['id'])+']-'+str(valores[i]['dt_insercao']))
                                    try:
                                            opcao = int(input("Selecione o ID que você quer ATUALIZAR: "))
                                    except ValueError:
                                         print('\033[91mO valor precisa ser numérico\033[0m')
                                    else:
                                       for i in range(len(valores)):
                                            if valores[i]['id']== opcao:
                                                idd= valores[i]['id']
                                                data_while = True
                                                agua = True
                                                kWH_while =True
                                                kg_residuos = True
                                                residuos_reciclaveis= True
                                                transporte= True
                                                novamente= True
                                                user_while= True
                                                while data_while : #TESTE DE VALIDAÇÃO DA DATA
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
                                                            data_while = False
                                                        #SEGUNDA PERGUNTA (SOBRE CONSUMO DE ÁGUA)
                                                        while agua:
                                                            try:
                                                                consumo_de_agua = float(input('Quantos litros de água você consumiu hoje? (Aprox. em litros): ').replace(',', '.'))
                                                            except ValueError:
                                                                print('\033[91mO valor precisa ser numérico\033[0m')
                                                            else:
                                                                if consumo_de_agua < 0:
                                                                    print('\033[91mO valor deve ser positivo\033[0m')
                                                                else:
                                                                    agua = False
                                                        #TERCEIRA PERGUNTA (SOBRE KWH DE ENERGIA)
                                                        while kWH_while :
                                                            try:
                                                                kWh = float(input('Quantos kWh de energia elétrica você consumiu hoje?: ').replace(',', '.'))
                                                            except ValueError:
                                                                print('\033[91mO valor precisa ser numérico\033[0m')
                                                            else:
                                                                if kWh < 0:
                                                                    print('\033[91mO valor deve ser positivo\033[0m')
                                                                else:
                                                                    kWH_while= False
                                                        #QUARTA PERGUNTA (SOBRE QUANTIDADE DE KG DE RESÍDUOS NÃO RECICLÁVEIS)
                                                        while kg_residuos:
                                                            try:
                                                                kg_de_residuos = float(input('Quantos kg de resíduos não recicláveis você gerou hoje?: ').replace(',', '.'))
                                                            except ValueError:
                                                                print('\033[91mO valor precisa ser numérico\033[0m')
                                                            else:
                                                                if kg_de_residuos < 0:
                                                                    print('\033[91mO valor deve ser positivo\033[0m')
                                                                else:
                                                                    kg_residuos = False
                                                        #QUINTA PERGUNTA (SOBRE PORCENTAGEM DE RESÍDUOS RECICLADOS NO TOTAL)
                                                        while residuos_reciclaveis:
                                                            try:
                                                                porcentagem_de_residuos_reciclaveis = int(input('Qual a porcentagem de resíduos reciclados no total (em %)?: '))
                                                            except ValueError:
                                                                print('\033[91mO valor precisa ser numérico\033[0m')
                                                            else:
                                                                if porcentagem_de_residuos_reciclaveis < 0:
                                                                    print('\033[91mO valor deve ser positivo\033[0m')
                                                                else:
                                                                    residuos_reciclaveis= False
                                                        #SEXTA PERGUNTA (SOBRE O MEIO DE TRASPORTE ULTILIZADO)
                                                        while transporte:
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
                                                                    atualizar_valores(consumo_de_agua,kWh, kg_de_residuos, porcentagem_de_residuos_reciclaveis, meio_de_trasporte,data_str,idd)
                                                                    transporte =False                                     
                                              

                elif menuresp == 5:
                    menu= False
                    rodar_novamente_programa= False
                    
                    


                                  


    # while novamente :
    #     continuar = input('Você gostaria de rodar novamente? (SIM ou NAO): ').strip().upper()
    #     if continuar not in ['SIM', 'NAO']:
    #         print("Digite novamente: SIM ou NAO")
    #     elif continuar == 'NAO':
    #         print("Encerrando o programa.")           
    #         novamente =False
    #         rodar_novamente_programa = False                                 
    #     else:
    #         print("Reiniciando...")
    #         # Aqui você pode colocar um `break` ou reiniciar o programa dependendo da lógica desejada
    #         novamente =False
           