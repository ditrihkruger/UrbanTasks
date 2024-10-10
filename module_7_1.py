import os.path


class Product:
    name: str
    weight: float
    category: str

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name: str = 'products.txt'

    def get_products(self) -> str:
        if not os.path.exists(self.__file_name):
            open(self.__file_name, 'w').close()
        file = open(self.__file_name)
        content = file.read()
        file.close()
        return content


    def add(self, *products: Product) -> None:
        content = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if content.find(product.name) != -1:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(str(product) + '\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())