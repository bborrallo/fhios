'''
Created on 9 dic 2021

@author: Borja Borrallo
'''
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#################################
#    Ejercicio 1
#################################
baraja = ('AP','2P','3P','JD','QT','KC')    # Se representan algunos valores de la baraja. En este caso se muestran en una tupla donde el primer caracter es el valor de la carta (A= AS, 2,3,4...,J,Q,K)
                                            # y el segundo caracter es el palo de la baraja (P = Picas, D = Diamantes, T = Treboles, C = Corazones)

#################################
#    Ejercicio 2
#################################
def checkPoker(mano):                       # Se pasa una mano en forma de tupla con 5 cartas
    poker='poker'                           # Se definen variables para retornar los mensajes de poker o no poker
    no_poker='No existe poker'
    
    for j in range(2):                      # Se evaluan las 2 primeras cartas con el resto (solo son necesarias estas 2 cartas para saber si existe poker o no)
        contador = 0                        # Se usa una variable contador para saber si existe poker
        carta=mano[j][0]                    # Se escoge la carta a evaluar
        for i in range(j,5):                # Se comprueba si esta carta es igual al resto de cartas
            if carta==mano[i][0]:           # En caso de ser igual, se suma 1 a contador
                contador +=1
        if contador==4:                     # Tras recorrer todas las cartas, se comprueba si hay 4 iguales para conocer si hay poker
            return poker
    return no_poker                         # Si tras evaluar las 2 primeras cartas, no ha habido poker, entonces no puede existir poker


#################################
#    Ejercicio 3
#################################
def diaSiguienteA(dia, mes, ano):
    bisiesto = False

    if ano % 4 == 0:                        # Se comprueba si es un año bisiesto
        if ano % 100 == 0:
            if ano % 400 == 0:
                bisiesto = True
        else:
            bisiesto = True

    if mes in (1, 3, 5, 7, 8, 10, 12):      # Segun el mes, se adjudican los días de ese mes (28/29, 30, 31)
        dias_mes = 31
    elif mes == 2:
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30

    if dia < dias_mes:                      # Se comprueba que el día proporcionado no supere el máximo de días del mes
        dia += 1
    else:                                   # En caso contrario se añade 1 mes o 1 mes + 1 año
        dia = 1
        if mes == 12:
            mes = 1
            ano += 1
        else:
            mes += 1
    
    return (dia, mes, ano)
    
#################################
#    Ejercicio 4
#################################       
def diaSiguienteB(dia, mes, ano):           # Misma explicacion que el ejercicio anterior con la salvedad de seleccionar el mes
    bisiesto = False
    meses = ('Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic')   # En una tupla se ponen todos los meses del año en formato string
    mes = meses.index(mes)+1                                                            # Se selecciona el nº del mes
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                bisiesto = True
        else:
            bisiesto = True

    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes == 2:
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30

    if dia < dias_mes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            ano += 1
        else:
            mes += 1
    
    return (dia, meses[mes-1], ano)

#################################
#    Ejercicio 5
#################################        
def textCorreos(texto, sizeMax):
    texto = texto.strip()                                   # Elimina los espacios iniciales y finales
    if texto[len(texto)-1] == '.':                          # Apartado b
        texto = texto[:len(texto)-1]+' STOPSTOP'            # Se sustituye punto final si lo hubiera por STOPSTOP o se añade si no lo hubiera
    else:
        texto = texto + ' STOPSTOP'
    texto = texto.replace('.',' STOP')
    
    frase = texto.split(' ')                                # Apartado a
    for i in range(len(frase)):                             # Se separan las palabras de la frase por espacios y se añaden a una lista
        if(frase[i]!= 'STOP' and frase[i] != 'STOPSTOP'):   # Se evita que se realice el proceso para las palabras clave STOP / STOPSTOP
            if len(frase[i])>sizeMax:                       # Si la palabra tiene un tamaño mayor que el indicado se aplica el remplazamientp
                frase[i] = frase[i][:sizeMax] + '@'         # Se sustituyen los caracteres, a partir del tamaño maximo, por @
    texto = ' '.join(frase)                                 # Se unen las palabras de la lista para formar una frase de nuevo
    return texto

#################################
#    Ejercicio 6
#################################  
def concatenarLista(lista1,lista2):
    lista1+=lista2
    return lista1

def concatenarTupla(tupla1,tupla2):
    tupla1+=tupla2
    return tupla1

def concatenarDiccionario(dic1, dic2):
    dic1.update(dic2)
    return dic1
    
#################################
#    Ejercicio 7
#################################  

def automationTest():
    driver = webdriver.Chrome()
    numMain = 0
    numServ = 0
    numClientes = 0
    numEquipo = 0
    numContacto = 0
    numUnete = 0
    
    try:
        driver.get('https://www.fhios.es/')
        numMain = len(driver.find_elements_by_xpath("//*[contains(text(), 'fhios')]"))
        print(numMain)
    
    except:
        print("Text was not found")
        
    try:    
        driver.implicitly_wait(10)
        
        driver.find_element_by_xpath('//a[@href="https://www.fhios.es/servicios/"]').click()   
        numServ = len(driver.find_elements_by_xpath("//*[contains(text(), 'fhios')]"))
        print(numServ)
    except:
        print("Text was not found")
        
    try:        
        driver.implicitly_wait(10)
        
        driver.find_element_by_xpath('//a[@href="https://www.fhios.es/clientes/"]').click()
        numClientes = len(driver.find_elements_by_xpath("//*[contains(text(), 'fhios')]"))
        print(numClientes)
    except:
        print("Text was not found")
        
    try:        
        driver.implicitly_wait(10)
        
        driver.find_element_by_xpath('//a[@href="https://www.fhios.es/equipo/"]').click()
        numEquipo = len(driver.find_elements_by_xpath("//*[contains(text(), 'fhios')]"))
        print(numEquipo)
    except:
        print("Text was not found")
        
    try:    
        driver.implicitly_wait(10)
        
        driver.find_element_by_xpath('//a[@href="https://www.fhios.es/contactanos/"]').click()
        numContacto = len(driver.find_elements_by_xpath("//*[contains(text(), 'fhios')]"))
        print(numContacto)
    except:
        print("Text was not found")
        
    try:    
        driver.implicitly_wait(10)
        
        driver.find_element_by_xpath('//a[@href="https://www.fhios.es/unete/"]').click()
        numUnete = len(driver.find_elements_by_xpath("//*[contains(text(), 'fhios')]"))
        print(numUnete)
        
    except:
        print("Text was not found")
    
    total = numMain + numServ + numClientes + numEquipo + numContacto + numUnete
    print("En total, fhio aparece "+str(total)+" veces.")
    
#################################
#    MAIN
#################################  
if __name__ == '__main__':
    # En todos los ejemplos se proporciona directamente los datos a evaluar cuando se llama a la funcion, por tanto no se tendran en cuenta los casos
    # de introduccion incorrecta de datos por parte del usuario
    mano1 = ('5C','4P','5D','5P','5T')
    print(checkPoker(mano1))
    # A modo de ejemplo, se pide que se introduzca por teclado día, mes y año a evaluar
    print("A continuación introduzca la fecha que se quiere evaluar:")
    dia = input('Día: ')
    mes = input('Mes: ')
    ano = input('Año: ')
    print(diaSiguienteA(int(dia), int(mes), int(ano)))
    print(diaSiguienteA(28, 2, 1908))
    print(diaSiguienteB(31, 'Dic', 2021))
    print(diaSiguienteB(28, 'Oct', 1908))
    print(textCorreos(" Llego por la mañana alrededor del mediodía, esperame para cenar ",5))
    print(textCorreos(" Llego mañana. Voy a almorzar ",5))
    print(concatenarLista([1,2,3,4], [1,2,3,4]))
    print(concatenarTupla((1,2,3,4), (1,2,3,4)))
    print(concatenarDiccionario( {1: "a" , 2: "b" , 3: "c"},  {4: "q" , 5: "w" , 6: "e"}))
    
    automationTest()