#Iniciaremos usando 4 variáveis diferentes que se relacionam entre si simulando uma loja

'''
item_1 = 'Phone'
item_1_price = 2000
item_1_quantity = 25
item_1_total_price = item_1_price * item_1_quantity
'''

#Declararemos a primeira classe no mesmo estilo das variáveis acima

class Item:
    #Funções dentro de classes passam a ser métodos, criaremos nosso primeiro método
    #self é sempre chamado nos métodos, pois o objeto é sempre dado como parâmetro

    def calculate_total_price(self, x, y):
        return x * y


item_1 = Item()
item_1.name = 'Phone'
item_1.price = 2000
item_1.quantity = 25

total_price = item_1.calculate_total_price(item_1.price, item_1.quantity)


#Usaremos agora o método __init__ que nos permite declarar uma instancia de maneira mais otimizada com todos os atributos

class Better_Item:
    
    #class atribute: É compartilhado por todos as instancias a não ser que seja declarada um valor diferente para uma instancia específica
    #Ao procurar um atributo e não achar o programa procura as class atributes e retorna

    #Exemplo de class atribute
    pay_rate = 0.8 #Pagamento com 20% de desconto

    def __init__(self, name: str, price: float, quantity: int):
        
        #Condições para o programa rodar (preço e quantidades não negativas)
        assert price >= 0, "The price must be greater or equal to zero"
        assert quantity >= 0, "The quantity must be greater or equal to zero"

        #Pode-se declarar da seguinte maneira def __init__(self, name, price = 0, quantity = 0), dessa forma
        #apenas os valores não definidos serão recebidos como parâmetro pois price e quantity já tem valor definido temporariamente
        self.name = name
        self.price = price
        self.quantity = quantity

    #Modificaremos o método a seguir, ele recebe a instância logo podemos retornar diretamente a mutiplicação dos atributos 
    def calculate_total_price(self):
        return self.price * self.quantity


item_1 = Better_Item('Phone', 2000, 25)
item_2 = Better_Item('Laptop', 3000, 20)
item_3 = Better_Item('Joystick', 200, 50)
item_4 = Better_Item('VideoGame', 5000, 10)


# __dict__: mostra todos os atributos de uma instancia ou 
# Mostra todos os métodos e class atributes de uma classe
print(Better_Item.__dict__)
print(item_1.__dict__)