# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 19:51:26 2021

@author: AlexAbajo
"""

from datetime import*
      

def VerificarFecha(digito):
    #Uso de Try/Except para detectar fechas invalidas.
    try:
        fecha=input("Ingrese la fecha la cual desea consultar(aaaa-mm-dd):")
        datetime.strptime(fecha, '%Y-%m-%d')
    except ValueError:
        print("Ingreso una fecha invalida, por favor vuelva a intentar.")
        return "No"
    
    #convertir substrings a enteros para usar en metodo date
    #weekday nos regresa un entero en funcion del dia de la semana que se envia como parametro.
    
    separados=fecha.split("-")
    
    year = int(separados[0])
    mes = int(separados[1])
    dia = int(separados[2])
    fechaFormato=date(year, mes, dia)
    numDia=fechaFormato.weekday()
    if (numDia==0):#Lunes
        if(digito==1 or digito==2):
            return "No"
        else:
            return "Si"
    elif (numDia==1):#Martes
        if(digito==3 or digito==4):
            return "No"
        else:
            return "Si"
    elif (numDia==2):#Miercoles
        if(digito==5 or digito==6):
            return "No"
        else:
            return "Si"
    elif (numDia==3):#Jueves
        if(digito==7 or digito==8):
            return "No"
        else:
            return "Si"
    elif (numDia==4):#Viernes
        if(digito==9 or digito==0):
            return "No"
        else:
            return "Si"
    else:#Fin de Semana
        return "Si"

def PicoPlaca(placa, hora):
    
    #Declaracion rangos de horas.
    horaLimInf1=datetime.strptime("07:00:00", "%X").time()
    horaLimSup1=datetime.strptime("09:30:00", "%X").time()
    horaLimInf2=datetime.strptime("16:00:00", "%X").time()
    horaLimSup2=datetime.strptime("19:30:00", "%X").time()
    horaConsulta=time.fromisoformat(hora)
    #Conseguir el ultimo digito de la placa
    digito=int(placa[-1])
    
    
    if(VerificarFecha(digito)=="No"):
        if ((horaLimInf1<=horaConsulta and horaConsulta<=horaLimSup1) or (horaLimInf2<=horaConsulta and horaConsulta<=horaLimSup2)):
            print("Lo sentimos, usted no puede circular bajo los parametros señalados.")
        else:
            print("Usted puede circular bajo los parametros señalados.")
    else:
        print("Usted puede circular bajo los parametros señalados.")
    
    
placa=input("Ingrese la placa a revisar (Ej: 9023 ):")
#fecha=input("Ingrese la fecha la cual desea consultar(dd/mm/aaaa):")
hora=input("Ingrese la hora la cual desea consultar(Ej: 19:30 ):")

hora=hora+":00"

PicoPlaca(placa, hora)