import csv

class Item:
    
    pay_rate = 0.8

    #Fazendo uma lista com todas as instâncias
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
    
    #Usando class method (métodos que são aplicados na classe e não nas instancias)
    #Para fazer isso o @classmethod deve ser adicionado antes do método

    #Faremos uma função para adicionar instancias a partir de um csv
    @classmethod
    def instantiate_from_csv(cls, path: str):
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item( name = item.get('name'), price = float(item.get('price')), quantity = int(item.get('quantity')))

    #Outro caso é a static method que diferente dos outros métodos não recebe a instância nem a classe como parâmetro
    #Pode ser chamado no nivel da classe ou da instancia pois não usa nenhum dos dois

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

Item.instantiate_from_csv('itens.csv')
print(Item.all)

print(Item.is_integer(14.0))