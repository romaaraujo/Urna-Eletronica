#--------------------------------------------------#
from PyQt5 import QtWidgets, uic,  QtCore, QtGui
import sys, time
#--------------------------------------------------#
#
#               URNA ELETRÔNICA
#        PROJETO: INTRODUÇÃO À PROGRAMAÇÃO
#        ALUNOS: ROMÁRIO ARAÚJO E ALESSON ALVES
#
#--------------------------------------------------#
#                   QtDesigner Interface
janela = QtWidgets.QApplication([])
interface = uic.loadUi("urn4.ui")
login = uic.loadUi("login-interface.ui")
fim1 = uic.loadUi("fim.ui")
# VARIAVEIS #
valores = [99, 99, 99, 99]
branqueando = [99]
valido = [99]
numeroeleitor = [99]
numerovotado = [99]

#                       SQLITE
import sqlite3
connection = sqlite3.connect('data.db')
c = connection.cursor()
sql = 'SELECT * FROM dados WHERE numero = ?' #P/ VOTAR E LOGAR
sqle = 'UPDATE dados SET votou = 1 WHERE numero = (?)' #P/ BUSCAR SETAR QUE VOTOU
sqlb = 'UPDATE dados SET votos = (?) WHERE numero = (?)' #P/ ADICIONAR VOTO AO CANDIDATO

# FUNÇÃO PARA SELECIONAR O CANDIDATO NA URNA #
def lercandidato(wordUsed):
    for row in c.execute(sql, (wordUsed,)):
        interface.label_11.setText(row[2])
        interface.label_11.show()
        interface.label_12.show()
        interface.label_13.setText(row[3])
        interface.label_13.show()    
        interface.label_10.show()
        interface.label_11.show() #(NOME CANDIDATO)
        interface.label_13.show() #(NOME CHAPA)
        interface.label_9.show() #Número
        interface.label_10.show() #Nome
        interface.label_12.show() #Chapa
        print("SISTEMA: USUÁRIO SELECIONOU O CANDIDATO ", row[2], "DA CHAPA", row[3])
        numerovotado[0] = row[1]
        break
    else:
            print('SISTEMA: USUÁRIO SELECIONOU VOTO NULO')
            interface.label_16.show() #VotoNulo
            interface.label_17.show() #VotoErrado
            valido[0] = 11
            numerovotado[0] = 22222

# FUNÇÃO DA TECLA CONFIRMA #
def CONFIRMA():
    def del_and_update():
        c.execute('SELECT * FROM dados')
        data = c.fetchall()
        [print(row) for row in data]
    if(branqueando[0] == 11):
        c.execute(sqle, (numeroeleitor[0],))
        print('**{} VOTOU EM BRANCO'.format(interface.label_18.text()))
        CONFIRMAB()
    elif(valido[0] == 99 and valores[3] != 99):
        c.execute(sqle, (numeroeleitor[0],))
        print('**{} VOTOU EM {} DA CHAPA {}'.format(interface.label_18.text(), interface.label_11.text(), interface.label_13.text()))
        CONFIRMAB()
    elif(valido[0] == 11 and valores[3] != 99):
        c.execute(sqle, (numeroeleitor[0],))
        print('**{} VOTOU NULO'.format(interface.label_18.text()))
        CONFIRMAB()
        
# BRAÇO DA FUNÇÃO CONFIRMA
def CONFIRMAB():
    for row in c.execute(sql, (numerovotado[0],)):
        quantosvotostem = row[5] + 1
    c.execute(sqlb, (quantosvotostem,numerovotado[0],))
    c.execute(sqle, (numeroeleitor[0],))
    connection.commit()
    c.execute('SELECT * FROM dados')
    data = c.fetchall()
    [print(row) for row in data]
    start()
    
# FUNÇÃO DA TECLA BRANCO #
def BRANCO():
    if(valores[0] == 99 and valores[1] == 99 and valores[2] == 99 and valores[3] == 99 and branqueando[0] == 99):
        print("SISTEMA: USUÁRIO PRESSIONOU O BOTÃO BRANCO")
        interface.label_3.show() #Voto Branco
        interface.label_15.show() #Acabamento xd
        interface.label_14.show() #Info Rodapé
        interface.label_5.hide() #1NUMERALPAINEL
        interface.label_6.hide() #2NUMERALPAINEL
        interface.label_7.hide() #3NUMERALPAINEL
        interface.label_8.hide() #4NUMERALPAINEL
        branqueando[0] = 11
        numerovotado[0] = 11111
        interface.label_4.show() #Seu voto para

# FUNÇÃO PROGRESSBAR #
def start():
    fim1.show()
    fim1.label.show()
    fim1.progressBar.show()
    fim1.progressBar.setValue(100)
    interface.hide()

# PARA VOTAR NOVAMENTE #
def reset2():
    reset()
    fim1.hide()
    login.show()

# FUNÇÃO IMPRIMA #
def IMPRIMA():
    imprima = open("RESULTADOS.txt","w")
    c.execute('SELECT * FROM dados WHERE id = 99')
    imprima.write("*************************************************\r")
    imprima.write("\n         RESULTADOS - URNA ELETRÔNICA\r")
    imprima.write("\n*************************************************\r")
    imprima.write("\n ")    
    imprima.write("\n ")
    c.execute('SELECT sum(votos) from dados')
    data = c.fetchall()
    imprima.write("\nTOTAL DE VOTOS: {}\r".format(data[0]))
    c.execute('SELECT * FROM dados WHERE id = 99')
    data = c.fetchall()
    imprima.write(" \n")
    for row in data:
        imprima.write("\n{} | VOTOS: {}\r".format( row[2], row[5]))
    c.execute('SELECT * FROM dados WHERE numero NOT IN (11111,22222) ORDER BY votos DESC LIMIT 5')
    data = c.fetchall()
    counter = 0
    imprima.write(" \n")
    for row in data:
        counter += 1
        imprima.write("\n{}º - CANDIDATO: {} | VOTOS: {}\r".format(counter, row[2], row[5]))
    imprima.close()
    
# FUNÇÃO PARA RESETAR URNA #
def reset():
    interface.label_11.hide() #(NOME CANDIDATO)
    interface.label_13.hide() #(NOME CHAPA)
    interface.label_14.hide() #Info Rodapé
    interface.label_9.hide() #Número
    interface.label_10.hide() #Nome
    interface.label_12.hide() #Chapa
    interface.label_3.hide() #Voto Branco
    interface.label_15.hide()       #Acabamento xd
    interface.label_5.setText(' ') #1NUMERALPAINEL
    interface.label_6.setText(' ') #2NUMERALPAINEL
    interface.label_7.setText(' ') #3NUMERALPAINEL
    interface.label_8.setText(' ') #4NUMERALPAINEL
    interface.label_5.show() #1NUMERALPAINEL
    interface.label_6.show() #2NUMERALPAINEL
    interface.label_7.show() #3NUMERALPAINEL
    interface.label_8.show() #4NUMERALPAINEL
    interface.label_4.hide() #Seu voto para
    fim1.label.hide() #fim
    valores[0] = 99
    valores[1] = 99
    valores[2] = 99
    valores[3] = 99
    branqueando[0] = 99
    valido[0] = 99
    numeroeleitor[0] = 99
    numerovotado[0] = 99
    interface.label_17.hide()    
    interface.label_16.hide()
    login.setFixedSize(573, 172);
    interface.setFixedSize(932, 495);
    fim1.setFixedSize(932, 495);
    
# FUNÇÃO DA TECLA CORRIGE #
def CORRIGE():
    if(valores[0] != 99 or branqueando[0] == 11):
        print("SISTEMA: USUÁRIO PRESSIONOU O BOTÃO CORRIGE")
        reset()

# ADICIONA O NÚMERO AO PAINEL #
def ADDNUMERO(a):
    if(branqueando[0] == 99 and valores[3] == 99):
        print("SISTEMA: USUÁRIO PRESSIONOU O BOTÃO ", a)
        if(valores[0] == 99):
            valores[0] = a
            interface.label_5.setText('{}'.format(valores[0]))
        elif(valores[1] == 99):
            valores[1] = a
            interface.label_6.setText('{}'.format(valores[1]))
        elif(valores[2] == 99):
            valores[2] = a
            interface.label_7.setText('{}'.format(valores[2]))
        elif(valores[3] == 99):
            valores[3] = a 
            interface.label_8.setText('{}'.format(valores[3]))                  
            interface.label_4.show() #Seu voto para
            interface.label_15.show()       #Acabamento xd
            interface.label_14.show() #Info Rodapé
            interface.label_9.show()
            lercandidato('{}{}{}{}'.format(valores[0],valores[1],valores[2],valores[3]))

#SISTEMA DE LOGIN
def logando(n):
    for row in c.execute(sql, (n,)):
        if(row[4] == 0):
            print("SISTEMA: USUÁRIO", row[2], "ENTROU NO PAINEL DE VOTAÇÃO")
            interface.show()
            interface.label_18.setText("ELEITOR: {}".format(row[2]))
            login.hide()
            numeroeleitor[0] = n
            break
        else:
            print("SISTEMA: USUÁRIO", row[2], "JÁ VOTOU E NÃO TEM ACESSO À URNA ELETRÔNICA")
            break
    else:
        print("SISTEMA: USUÁRIO DIGITOU UMA MATRÍCULA ERRADA")
           
# FUNÇÕES PyQt5 AO CLICAR NOS BOTÕES #  
interface.pushButton_4.clicked.connect(lambda:ADDNUMERO(1))
interface.pushButton_2.clicked.connect(lambda: ADDNUMERO(2))
interface.pushButton_3.clicked.connect(lambda: ADDNUMERO(3))
interface.pushButton_5.clicked.connect(lambda: ADDNUMERO(4))
interface.pushButton_6.clicked.connect(lambda: ADDNUMERO(5))
interface.pushButton_7.clicked.connect(lambda: ADDNUMERO(6))
interface.pushButton_8.clicked.connect(lambda: ADDNUMERO(7))
interface.pushButton_10.clicked.connect(lambda: ADDNUMERO(8))
interface.pushButton_9.clicked.connect(lambda: ADDNUMERO(9))
interface.pushButton_11.clicked.connect(lambda: ADDNUMERO(0))
interface.pushButton_13.clicked.connect(CORRIGE)
interface.pushButton_12.clicked.connect(BRANCO)
interface.pushButton_14.clicked.connect(CONFIRMA)
fim1.pushButton.clicked.connect(reset2)
fim1.pushButton_2.clicked.connect(IMPRIMA)
login.pushButton.clicked.connect(lambda:logando(login.lineEdit.text()))

# INICIALIZADOR DO PROGRAMA #
reset()
login.show()
sys.exit(janela.exec_())
