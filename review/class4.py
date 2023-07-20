import csv

class Item:
    
    pay_rate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity: int):
        
        assert price >= 0, "The price must be greater or equal to zero"
        assert quantity >= 0, "The quantity must be greater or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls, path: str):
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item( name = item.get('name'), price = float(item.get('price')), quantity = int(item.get('quantity')))

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"

#Inheritance: criamos agora uma classe filha da classe item
#A classe compartilha os atributos básicos da classe mãe mas pode ter suas próprias especificidades

class Phone(Item):
    
    all = []

    def __init__(self, name: str, price: float, quantity: int, broken_phones: int):
        
        #Chamar o pai da classe phone (classe item) usando o super, assim aprofeitamos as propriedades do init da classe mãe

        super().__init__(name, price, quantity)

        assert broken_phones >= 0, "The quantity of broken phones must be greater or equal to zero"
        self.broken_phones = broken_phones

    #Fazendo nossa representação de instancia da classe filha phone
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.broken_phones})"

phone1 = Phone('Iphone12', 3000, 20, 10)
phone2 = Phone('Iphone13', 4000, 30, 10)

Item.instantiate_from_csv('itens.csv')

#Perceba que a função funciona perfeitamente
print(phone1.calculate_total_price())

print(Item.all)
