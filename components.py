from utilities import borrarPantalla, gotoxy
import time
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from datetime import datetime
from clsJson import JsonFile
import os
import math
path, _ = os.path.split(os.path.abspath(__file__))

class Menu:
  def __init__(self,titulo="",opciones=[],col=6,fil=1):
    self.titulo=titulo
    self.opciones=opciones
    self.col=col
    self.fil=fil
      
  def menu(self):
    gotoxy(self.col,self.fil);print(self.titulo)
    self.col-=5

    for opcion in self.opciones:
      self.fil +=1 
      gotoxy(self.col,self.fil);print(opcion)
    gotoxy(self.col+5,self.fil+2)
    opc = input(f"{cyan_color}- Ingrese una opcion {red_color}[1 ... {len(self.opciones)}]: ") 
    return opc   

class Valida:
  def solo_numeros(self,mensaje, mensajeError,col,fil):
    while True:
      gotoxy(col, fil)
      valor = input(mensaje)
      try:
        valor = int(valor)
        if valor > 0:
          break
        else:
          gotoxy(col, fil);print(mensajeError);time.sleep(2)
          gotoxy(col, fil);print(' '*len(mensajeError))
          continue
      except:
        gotoxy(col, fil);print(mensajeError);time.sleep(2)
        gotoxy(col, fil);print(' '*len(mensajeError))
        continue
    return valor 

  def solo_letras(self,mensaje, mensajeError, col, fil): 
    while True:
      gotoxy(col, fil)
      valor = str(input(mensaje))
      try: 
        if valor.isalpha():
          break
        else:
          gotoxy(col, fil);print(mensajeError);time.sleep(2)
          gotoxy(col, fil);print(' '*len(mensajeError))
          continue
      except:
        gotoxy(col, fil);print(mensajeError);time.sleep(2)
        gotoxy(col, fil);print(' '*len(mensajeError))
    return valor

  def solo_decimales(self,mensaje,mensajeError, col, fil):
    while True:
      gotoxy(col, fil)
      valor = str(input(mensaje))
      try:
        valor = float(valor)
        if valor > float(0):
          break
        else:
          gotoxy(col, fil);print(mensajeError);time.sleep(2)
          gotoxy(col, fil);print(' '*len(mensajeError))
          continue
      except:
        gotoxy(col, fil);print(mensajeError);time.sleep(2)
        gotoxy(col, fil);print(' '*len(mensajeError))
        continue
    return valor
  
  def solo_fecha(self, mensaje, mensajeError, col, fil):
    while True:
      gotoxy(col, fil)
      valor = input(mensaje)
      try:
        if len(valor) == 10 and valor[4] == valor[7] == '-' and valor[:4].isdigit() and valor[5:7].isdigit() and valor[8:].isdigit():
          datetime.strptime(valor, '%Y-%m-%d')
          break
        else:
          gotoxy(col, fil);print(mensajeError);time.sleep(2)
          gotoxy(col, fil);print(' '*len(mensajeError))
          continue
      except:
        gotoxy(col, fil);print(mensajeError);time.sleep(2)
        gotoxy(col, fil);print(' '*len(mensajeError))
        continue
    return valor
  
  def validar_dni_sistema(self, mensaje, col, fil):
    mensajeErrorDNIExistente = f"{red_color}El DNI ya existe en el sistema. Intentelo de nuevo. 😡"
    mensajeErrorFormato = f"{red_color}El formato del DNI es inválido. Intentelo de nuevo. 😕"
    while True:
      gotoxy(col, fil);dni = input(mensaje)

      if self.es_cedula_valida(dni, col, fil):
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni", dni)
        if not client:
            return dni
        else:
            gotoxy(col, fil);print(mensajeErrorDNIExistente);time.sleep(2)
            gotoxy(col, fil);print(' ' * len(mensajeErrorDNIExistente))
      else:
          gotoxy(col, fil)
          print(mensajeErrorFormato)
          time.sleep(2)
          gotoxy(col, fil)
          print(' ' * len(mensajeErrorFormato))

  def es_cedula_valida(self, cedula, col, fil):
    try: 
      if len(cedula) != 10:
        pass
      else:
        multiplicador = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        ced_array = list(map(lambda k: int(k), list(cedula)))[0:9]  # Corrección aquí
        ultimo_digito = int(cedula[9])
        resultado = []
        arr = map(lambda x, j: (x, j), ced_array, multiplicador)
        for (i, j) in arr:
          if i * j < 10:
            resultado.append(i * j)
          else:
            resultado.append((i * j)-9)
        if ultimo_digito == int(math.ceil(float(sum(resultado)) / 10) * 10) - sum(resultado):
          return True
        else:
          return False
    except:
      pass
  