import sqlite3

connection = sqlite3.connect('data.db')
c = connection.cursor()

#SQL

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados (id integer, numero integer, nome text, chapa text, votou integer, votos integer)')


create_table()

def dataentry():
    c.execute("INSERT INTO dados VALUES(1,0212, 'ALESSON ALVES DA SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(2,0239, 'ALEX EMANUEL BARBOSA DE SOUZA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(3,0093, 'ALEXANDRE HENRIQUE SILVA DO NASCIMENTO', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(4,0042, 'ANDERSON RAFAEL AMERICO DO NASCIMENTO', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(5,0255, 'ARTHUR HENRIQUE MENDES DOS SANTOS', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(5,0018, 'BRENO FERNANDES SILVA DO NASCIMENTO', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(7,0069, 'CHRISTIAN OLIVEIRA DO RAMO', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(8,0352, 'DIOGO DO NASCIMENTO GOMES', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(9,0115, 'ELISAMA SABRINA DOS SANTOS', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(10,0166, 'ERICK PEREIRA DE ARAúJO ALVES DOS SANTOS', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(11,0140, 'GABRIEL LIMA GONçALVES DA SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(12,0190, 'GASTON ALEXANDRE GOUVEIA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(13,0077, 'GUSTAVO OLAVO NUNES', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(14,0107, 'GUSTAVO RODRIGO GOUVEIA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(15,0263, 'HENRIQUE BENJAMIM DE BRITO ROCHA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(16,0271, 'IGOR CANTALICE MENDES', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(17,0344, 'ÍTALO HENRIQUE DE LIMA SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(18,0417, 'JEFFERSON MARCELO DA PAIXãO SANTOS', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(19,0310, 'JORGE LUIS BENEDITO DE LEMOS', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(20,0131, 'JOSE MARIANO BARBOSA JUNIOR', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(21,0409, 'KEIZA ANALIZI DA SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(22,0050, 'MARIA CECILIA DOS SANTOS SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(23,0204, 'MARIA ROSA GOMES MORAIS', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(24,0360, 'MATHEUS SILVA BEZERRA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(25,0220, 'MIKE RODRIGUES DA SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(26,0085, 'OSNALDO MORAES SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(27,0247, 'PABLO VINICIUS JOSE DA SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(28,0026, 'PAULO HENRIQUE ALVES XIMENES', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(29,0280, 'PEDRO ALVES DAMAZIO JUNIOR', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(30,0395, 'PEDRO PAULO DE OLIVEIRA MOURA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(31,0034, 'RAYLSON CASSIANO ALVES DA SILVA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(32,0182, 'REYVSON LUCAS LEONIDAS DE ALBUQUERQUE', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(33,0158, 'RODRIGO LOPES DE SOUZA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(34,0301, 'ROMARIO ARAUJO CARLOS', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(35,0387, 'RUBENS RATES DE ALBUQUERQUE', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(36,0336, 'SELTON HENRIQUE DE SOUZA CAMARA', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(37,0328, 'VALéRIA BARBOSA DE ARAUJO', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(38,0379, 'VINICIUS AUGUSTO ANDRADE ALBUQUERQUE', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(39,0123, 'WILLIAM TELES DE ANDRADE JUNIOR', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(40,0298, 'WLADSON VASCONCELOS DOS SANTOS', 'ADS/2019.2', 0, 0)")
    c.execute("INSERT INTO dados VALUES(99,11111, 'BRANCO', '#', 1, 0)")
    c.execute("INSERT INTO dados VALUES(99,22222, 'NULO', '#', 1, 0)")
    connection.commit()

dataentry()
   
