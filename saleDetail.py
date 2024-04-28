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
