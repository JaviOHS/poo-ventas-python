
class Client:
  def __init__(self, first_name="Consumidor", last_name="Final", dni="9999999999", client_type = "regular"):
    self.first_name = first_name
    self.last_name = last_name
    self.__dni = dni
    self.client_type = client_type
                  
  @property
  def dni(self):
    return self.__dni
  
  @dni.setter
  def dni(self, value):
    if len(value) in (10, 13):
      self.__dni = value
    else:
      self.__dni ="9999999999"

  def __str__(self):
    return f'Cliente: {self.first_name} {self.last_name}'  
  
  def fullName(self):
    return self.first_name + ' ' + self.last_name
  
  def return_dni(self):
    return self.__dni
  
class RegularClient(Client):
  def __init__(self, first_name="Cliente", last_name="Final", dni="9999999999", card=False):
    super().__init__(first_name, last_name, dni) 
    self.__discount = 0.10 if card else 0
            
  @property
  def discount(self):
    return self.__discount
        
  def __str__(self):
    return f'Client:{self.first_name} {self.last_name} Descuento:{self.discount}'
    
  def show(self):
    print(f'Cliente Minorista: DNI:{self.dni} Nombre:{self.first_name} {self.last_name} Descuento:{self.discount*100}%')

  def getJson(self):
    return {"dni":self.dni,"nombre":self.first_name,"apellido":self.last_name,"valor": self.discount}

class VipClient(Client):
  def __init__(self, first_name="Consumidor", last_name="Final", dni="9999999999", card=False):
    super().__init__(first_name, last_name, dni)
    self.__limit = 10000
    self.__discount = 0.10 if card else 0

  @property
  def discount(self):
    return self.__discount
  
  @property
  def limit(self):
    return self.__limit
  
  @limit.setter
  def limit(self, value):
    self.__limit = 10000 if (value < 10000 or value > 20000) else value 

  def __str__(self):
    return f'Cliente:{self.first_name} {self.last_name} Cupo: {self.limit}'
          
  def show(self):
    print(f'Cliente Vip: DNI:{self.dni} Nombre: {self.first_name} {self.last_name} Cupo: {self.limit}')     
      
  def getJson(self):
    # Método para imprimir los detalles del cliente VIP en la consola
    return {"dni":self.dni,"nombre":self.first_name,"apellido":self.last_name,"valor": self.limit}

if __name__ == '__main__':  
  regular_cli1 = RegularClient() # instancia la clase RegularClient en el objeto regular_cli1 y ejecuta el constructor
  regular_cli2 = RegularClient("Daniel", "Vera", "0914122419", card=True)
  vip_cli1 = VipClient("Erick", "Vera", "0914122412")
  vip_cli2 = VipClient("Yadira", "Bohorquez", "0914122411")
  vip_cli2.limit = 15000
  datos=(2,4,6,8)
  for dat in datos: print(dat*2)
  clients = (regular_cli1, regular_cli2, vip_cli1, vip_cli2)
  for cli in clients: print(cli.getJson())