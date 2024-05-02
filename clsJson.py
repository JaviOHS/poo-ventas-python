import json
import os
from utilities import gotoxy, borrarPantalla
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from company import Company

path, _ = os.path.split(os.path.abspath(__file__))

from customer import RegularClient, VipClient
class JsonFile:
  def __init__(self, filename):
    self.filename = filename

  def save(self, data):
    with open(self.filename, 'w') as file:
      json.dump(data, file) # dump:graba datos a un archivo json
      
  def read(self):
    try:
      with open(self.filename,'r') as file:
        data = json.load(file)# load:carga datos desde un archivo json
    except FileNotFoundError:
      data = []
    return data
     
  def find(self,atributo,buscado):
    try:
      with open(self.filename,'r') as file:
        datas = json.load(file)
        data = [item for item in datas if item[atributo] == buscado ]
    except FileNotFoundError:
      data = []
    return data
    
  def replace(self, filename, updated_invoices):
    with open(filename, 'r') as file:
      invoices = json.load(file)
    for i, invoice in enumerate(invoices):
      if invoice['factura'] == updated_invoices[0]['factura']:
        invoices[i] = updated_invoices[0]
        break
    with open(filename, 'w') as file:
      json.dump(invoices, file)

  def delete(self, key, value):
    with open(self.filename, 'r') as file:
      data = json.load(file)
    for i, item in enumerate(data):
      if item.get(key) == value:
        del data[i] 
    with open(self.filename, 'w') as file:
      json.dump(data, file, indent=4)

  # def update_invoice(self, invoice):
  #   try:
  #     invoice['subtotal'] = sum(item['precio'] * item['cantidad'] for item in invoice['detalle'])
  #     invoice['descuento'] = invoice['subtotal'] * 0.1 
  #     invoice['iva'] = round(invoice['subtotal'] * 0.12, 2) 
  #     invoice['total'] = round(invoice['subtotal'] - invoice['descuento'] + invoice['iva'], 2)
  #   except Exception as e:
  #     print('ERROR', e)


  def update_invoice(self, invoice):
    try:
      subtotal = 0
      discount = 0
      iva = 0
      for item in invoice['detalle']:
        subtotal += item['precio'] * item['cantidad']
      client_type = invoice['cliente']
      json_file_clients = JsonFile(path + '/archivos/clients.json')
      clients_data = json_file_clients.read()
      for client in clients_data:
        if client['nombre'] == client_type:
          if client['tipo'] == 'VIP':
            vip_client = VipClient(dni=client['dni'])
            discount = vip_client.discount
            break
          else:
            regular_client = RegularClient(dni=client['dni'])
            discount = regular_client.discount
            break
      discount_amount = subtotal * discount
      iva = round(subtotal * 0.12, 2)
      total = round(subtotal - discount_amount + iva, 2)
      invoice['subtotal'] = subtotal
      invoice['descuento'] = discount_amount
      invoice['iva'] = iva
      invoice['total'] = total
    except Exception as e:
        print('ERROR', e)


 
  def delete_all(self):
    with open(self.filename, 'r') as file:
      invoices = json.load(file)
    invoices_to_keep = [invoice for invoice in invoices if invoice['factura'] == 0]
    with open(self.filename, 'w') as file:
      json.dump(invoices_to_keep, file)

  def delete_all_products(self):
    with open(self.filename, 'r') as file:
      products = json.load(file)
    products_to_keep = [product for product in products if product['id'] == 0]
    with open(self.filename, 'w') as file:
      json.dump(products_to_keep, file)


  def print_all_invoices(self, invoices):
    gotoxy(6,5);print(f"{yellow_color}- Facturas cargados con éxito: {len(invoices):<10} ✅ Presione ENTER para continuar. ​🗿 ​")
    gotoxy(5,7);print(red_color + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" * 4 + reset_color)
    gotoxy(10,9);print(Company.get_business_name())
    gotoxy(5,11);print(red_color + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" * 4 + reset_color)
    current_line = 12  
    for invoice_data in invoices:
      current_line += 1 
      line_div_2 = green_color + "--------------------" * 4 + reset_color
      gotoxy(5, current_line);print(f"{purple_color}Número de Factura: {blue_color}{invoice_data['factura']:<10}{purple_color}Fecha: {blue_color}{invoice_data['Fecha']:<20}{purple_color}Cliente: {blue_color}{invoice_data['cliente']}")
      current_line += 1
      gotoxy(5, current_line);print(f"{purple_color}Subtotal: {yellow_color}{invoice_data['subtotal']:<19}{purple_color}Descuento: {yellow_color}{invoice_data['descuento']:<16}{purple_color}IVA: {yellow_color}{invoice_data['iva']:<10}{purple_color}")
      current_line += 1
      gotoxy(5, current_line);print(line_div_2)
      current_line += 1
      gotoxy(15, current_line);print(f"{purple_color}{'Productos':<15} {'Precio':<10} {'Cantidad':<10}")
      current_line += 1
      for detail in invoice_data['detalle']:
          gotoxy(15, current_line);print(blue_color + f"{detail['producto']:<15} {detail['precio']:<10} {detail['cantidad']:<10}")
          current_line += 1
      gotoxy(5,current_line);print(line_div_2)
      current_line += 1
      gotoxy(15, current_line);print(f"{purple_color}{'Total: ':<38}{red_color}{invoice_data['total']}")
      current_line += 2
      gotoxy(5,current_line);print(green_color + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" * 4 + reset_color)
      current_line += 2
    gotoxy(90,5);input()
  borrarPantalla()


  def print_all_products(self, *args, **kwargs):
    products_data = args[0] 
    gotoxy(6,5);print(f"{yellow_color}- Productos cargados con éxito: {len(products_data):<10} ✅ Presione ENTER para continuar. ​🗿 ​")
    gotoxy(15,7);print(red_color + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" * 4 + reset_color)
    gotoxy(20,9);print(Company.get_business_name())
    gotoxy(15,11);print(red_color + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" * 4 + reset_color)
    current_line = 12 
    for product in products_data:
        current_line += 1
        gotoxy(25, current_line);print(f"{purple_color}ID: {blue_color}{product['id']:<15}{purple_color}Producto: {blue_color}{product['descripcion']:<20}")
        current_line += 1
        gotoxy(25, current_line);print(f"{purple_color}Precio: {yellow_color}{product['precio']:<11}{purple_color}Stock: {yellow_color}{product['stock']:<20}")
        current_line += 1
        gotoxy(15, current_line);print(cyan_color + "--------------------" * 4 + reset_color)
        current_line += 1
    gotoxy(90,5)
    input()
  borrarPantalla()

  def print_all_clients(self, clients):
    gotoxy(6,5);print(f"{yellow_color}- Clientes cargados con éxito: {len(clients):<10} ✅ Presione ENTER para continuar. ​🗿 ​")
    gotoxy(8,7);print(red_color + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" * 4 + reset_color)
    gotoxy(16,9);print(Company.get_business_name())
    gotoxy(8,11);print(red_color + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" * 4 + reset_color)
    current_line = 12 
    for client in clients:
      current_line += 1 
      gotoxy(10, current_line);print(f"{purple_color}DNI: {blue_color}{client['dni']:<25}{purple_color}Nombres: {blue_color}{client['nombre']} {client['apellido']:<20}")
      current_line += 1
      gotoxy(10, current_line);print(f"{purple_color}Valor: {yellow_color}{client['valor']:<23}{purple_color}Tipo: {yellow_color}{client['tipo']:<20}")
      current_line += 1
      gotoxy(8, current_line);print(yellow_color + "--------------------" * 4 + reset_color)
      current_line += 1
    gotoxy(90,5);input()
  borrarPantalla()
    