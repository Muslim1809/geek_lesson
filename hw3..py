# Класс Computer (компьютер)
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu  # Приватный атрибут
        self.__memory = memory  # Приватный атрибут

    # Сеттер для cpu
    def set_cpu(self, cpu):
        self.__cpu = cpu

    # Геттер для cpu
    def get_cpu(self):
        return self.__cpu

    # Сеттер для memory
    def set_memory(self, memory):
        self.__memory = memory

    # Геттер для memory
    def get_memory(self):
        return self.__memory

    # Метод для выполнения арифметических вычислений
    def make_computations(self):
        return self.__cpu * self.__memory  # Пример вычислений (произведение cpu и memory)

    # Магический метод __str__ для вывода полной информации об объекте
    def __str__(self):
        return f"Computer: CPU = {self.__cpu}, Memory = {self.__memory}"

    # Перезапись магических методов сравнения для memory
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


# Класс Phone (телефон)
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list  # Приватное поле для сим-карт

    # Сеттер для sim_cards_list
    def set_sim_cards(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Геттер для sim_cards_list
    def get_sim_cards(self):
        return self.__sim_cards_list

    # Метод для симуляции звонка
    def call(self, sim_card_number, call_to_number):
        sim_card_info = self.__sim_cards_list[sim_card_number - 1]  # Понимание нумерации сим-карт
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} ({sim_card_info})")

    # Магический метод __str__ для вывода полной информации о телефоне
    def __str__(self):
        return f"Phone: SIM Cards = {', '.join(self.__sim_cards_list)}"


# Класс SmartPhone (смартфон) наследуется от Computer и Phone
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)  # Инициализация класса Computer
        Phone.__init__(self, sim_cards_list)  # Инициализация класса Phone

    # Метод для использования GPS
    def use_gps(self, location):
        print(f"Строится маршрут до {location}")

    # Переопределение метода __str__
    def __str__(self):
        return f"SmartPhone: CPU = {self.get_cpu()}, Memory = {self.get_memory()}, SIM Cards = {', '.join(self.get_sim_cards())}"


# Создание объектов
computer = Computer(4, 16)
phone = Phone(['Beeline', 'MegaCom', 'O!', 'Alfa'])
smartphone_1 = SmartPhone(8, 32, ['Beeline', 'MegaCom'])
smartphone_2 = SmartPhone(12, 64, ['Beeline', 'O!', 'Alfa'])

# Распечатка информации о объектах
print(computer)
print(phone)
print(smartphone_1)
print(smartphone_2)

# Тестирование методов
print("\nМетоды для компьютера:")
print(computer.make_computations())  # Арифметическое вычисление

print("\nМетоды для телефона:")
phone.call(1, '+996 777 99 88 11')  # Звонок с сим-карты-1

print("\nМетоды для смартфона:")
smartphone_1.use_gps("Bishkek")  # Использование GPS
smartphone_2.use_gps("Almaty")

# Тестирование магических методов
print("\nМагические методы сравнения для компьютеров:")
print(computer == smartphone_1)  # Сравнение по памяти
print(computer < smartphone_2)
print(smartphone_1 >= smartphone_2)
