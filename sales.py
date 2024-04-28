from calculos import Icalculo
from datetime import date
import os
from clsJson import JsonFile
from company import Company
from utilities import gotoxy
reset_color = "\033[0m"
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
blue_color = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"
path, _ = os.path.split(os.path.abspath(__file__))


class SaleDetail:
  _line=0
  def __init__(self,product,quantity):
    SaleDetail._line += 1
    self.__id = SaleDetail._line
    self.product = product
    self.preci = product.preci
    self.quantity = quantity
  
  @property
  def id(self):
    return self.__id
  
  def __repr__(self):
    return f'{self.id} {self.product.descrip} {self.preci} {self.quantity}'  
        
class Sale(Icalculo):
  next=0
  FACTOR_IVA=0.12
  def __init__(self,client):
    Sale.next += 1
    self.__invoice = Sale.next
    self.date = date.today()
    self.client = client
    self.subtotal = 0
    self.percentage_discount = client.discount 
    self.discount = 0
    self.iva = 0 
    self.total = 0
    self.sale_detail = []
  
  @property
  def invoice(self):
    return self.__invoice
  
  def __repr__(self):
    return f'Factura# {self.invoice} {self.date} {self.client.fullName()} {self.total}'  
  
  def cal_iva(self,iva=0.12,valor=0):
    return round(valor*iva,2)
  
  def cal_discount(self,valor=0,discount=0):
    return valor*discount
  
  def add_detail(self,prod,qty):
    detail = SaleDetail(prod,qty)
    self.subtotal += round(detail.preci*detail.quantity,2)
    self.discount = self.cal_discount(self.subtotal,self.percentage_discount)     
    self.iva = self.cal_iva(Sale.FACTOR_IVA,self.subtotal-self.discount)
    self.total = round(self.subtotal+self.iva-self.discount,2)
    self.sale_detail.append(detail) 
    new_invoice_data = self.getJson()
    json_file = JsonFile(path + '/archivos/invoices.json')  # Reemplaza 'ruta/a/tu/archivo/invoices.json' con la ruta real de tu archivo
    json_file.update_invoice(new_invoice_data)
    
  def getJson(self):
    # Método especial para representar la clase venta como diccionario
    invoice= {"factura":self.invoice,"Fecha":self.date.strftime("%Y-%m-%d")
,"cliente":self.client.fullName(),"subtotal":self.subtotal,"descuento": self.discount,"iva": self.iva,"total": self.total,"detalle":[]}
    for det in self.sale_detail:
      invoice["detalle"].append(
          {"producto":det.product.descrip,
          "precio": det.preci,
          "cantidad": det.quantity}
      )  
    return invoice
  