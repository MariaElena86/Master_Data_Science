
class Employee:
    def __init__(self, name, salary):
        self._name = name #protected
        self.__salary = salary#private

    @property#Getter, para leer el atributo protected
    def name(self):
        return self._name

    @property#Getter, para leer el atributo private
    def salary(self):
        return self.__salary

    @salary.setter#para modificar el atributo privado
    def salary(self, amount):
        if amount < 0:
            print("❌ Error: El salario no puede ser negativo.")
        else:
            print(f"✅ Salario actualizado a {amount}")
            self.__salary = amount

    @staticmethod
    def calculate_tax(amount):
        return amount * 0.15
