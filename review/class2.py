class Item:
    
    pay_rate = 0.8 #Pagamento com 20% de desconto

    #Fazendo uma lista com todas as instâncias
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        
        #Condições para o programa rodar (preço e quantidades não negativas)
        assert price >= 0, "The price must be greater or equal to zero"
        assert quantity >= 0, "The quantity must be greater or equal to zero"

        #Pode-se declarar da seguinte maneira def __init__(self, name, price = 0, quantity = 0), dessa forma
        #apenas os valores não definidos serão recebidos como parâmetro pois price e quantity já tem valor definido temporariamente
        self.name = name
        self.price = price
        self.quantity = quantity

        #Adicionanto a instancia a lista de todas as instancias
        Item.all.append(self)

    #Modificaremos o método a seguir, ele recebe a instância logo podemos retornar diretamente a mutiplicação dos atributos 
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    #__repr__ define como será representado as instancias quando printarmos
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', {self.quantity})"

item_1 = Item('Phone', 2000, 25)
item_2 = Item('Laptop', 3000, 20)
item_3 = Item('Joystick', 200, 50)
item_4 = Item('VideoGame', 5000, 10)
item_5 = Item('Mouse', 50, 10)

#printando todos os nomes das instancias usando Item.all
for instance in Item.all:
    print(instance.name)

#Simplificando a representação das instancias
print(Item.all)