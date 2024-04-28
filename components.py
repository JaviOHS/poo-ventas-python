from utilities import borrarPantalla, gotoxy
import time
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from datetime import datetime

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

  def solo_letras(self,mensaje,mensajeError, col, fil): 
    while True:
      valor = str(input(mensaje))
      if valor.isalpha():
        break
      else:
        gotoxy(col, fil);print(mensajeError);time.sleep(2)
        gotoxy(col, fil);print(' '*len(mensajeError))
        continue
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
      
  def cedula(self, mensaje, col, fil):
    mensajeError = f"{red_color}- El DNI debe tener al menos 10 dígitos. 🙂               {reset_color}"
    while True:
      gotoxy(col, fil)
      valor = str(input(mensaje))
      try:
        if len(valor) >= 10:
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
  
if __name__ == '__main__':
  # instanciar el menu
  opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
  menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
  # llamada al menu
  opcion_elegida = menu.menu()
  print("Opción escogida:", opcion_elegida)
  valida = Valida()
  if(opciones_menu==1):
    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)
  
  numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
  print("Número validado:", numero_validado)
  
  letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
  print("Letra validada:", letra_validada)
  
  decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
  print("Decimal validado:", decimal_validado)