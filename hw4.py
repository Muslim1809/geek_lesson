import random

# Класс героя
class Hero:
    def __init__(self, name, health, attack, defense, special_ability=None):
        self.name = name
        self._health = health  # Приватное поле для здоровья
        self.attack = attack
        self.defense = defense
        self.special_ability = special_ability

    # Геттер для здоровья
    @property
    def health(self):
        return self._health

    # Сеттер для здоровья
    @health.setter
    def health(self, value):
        self._health = max(0, value)  # Обеспечиваем, чтобы здоровье не могло быть меньше 0

    # Геттер для проверки, жив ли герой
    @property
    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage):
        self.health -= damage  # Используем сеттер для изменения здоровья

    def deal_damage(self, target):
        damage = max(self.attack - target.defense, 0)
        target.take_damage(damage)

    def use_special_ability(self, target, allies, boss):
        if self.special_ability:
            self.special_ability(self, target, allies, boss)


# Класс босса
class Boss:
    def __init__(self, health, attack, defense):
        self._health = health  # Приватное поле для здоровья
        self.attack = attack
        self.defense = defense

    # Геттер для здоровья
    @property
    def health(self):
        return self._health

    # Сеттер для здоровья
    @health.setter
    def health(self, value):
        self._health = max(0, value)  # Убеждаемся, что здоровье не может быть меньше 0

    # Геттер для проверки, жив ли босс
    @property
    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage):
        self.health -= damage  # Используем сеттер для изменения здоровья

    def attack_heroes(self, heroes):
        for hero in heroes:
            if hero.is_alive:
                damage = max(self.attack - hero.defense, 0)
                hero.take_damage(damage)

# Специальные способности героев
def witcher_special(hero, target, allies, boss):
    # Способность Ведьмака: пожертвовать собой для воскрешения первого погибшего
    if len(allies) > 0:
        first_dead = next((ally for ally in allies if ally.health == 0), None)
        if first_dead:
            sacrifice_health = hero.health
            hero.health = 0
            first_dead.health = sacrifice_health
            print(f"{hero.name} sacrificed himself to resurrect {first_dead.name}!")

def magic_special(hero, target, allies, boss):
    # Способность Мага: увеличить атаку всех героев на 10 единиц
    increase_attack = 10
    for ally in allies:
        if ally.is_alive:
            ally.attack += increase_attack
            print(f"{ally.name}'s attack increased by {increase_attack}!")

def hacker_special(hero, target, allies, boss):
    # Способность Хакера: забрать у босса 20 здоровья и передать герою
    damage_to_boss = 20
    target.take_damage(damage_to_boss)
    print(f"{hero.name} stole {damage_to_boss} health from the boss!")

def golem_special(hero, target, allies, boss):
    # Способность Голема: поглощать часть урона
    if hero.is_alive:
        absorbed_damage = 0.2 * boss.attack  # Голем поглощает 20% урона босса
        hero.health += absorbed_damage
        print(f"{hero.name} absorbed {absorbed_damage} damage!")

def avrora_special(hero, target, allies, boss):
    # Способность Авроры: она может войти в невидимость на 2 раунда
    # и возвращать урон обратно боссу после невидимости
    if hero.is_alive:
        invisibility_rounds = 2
        for i in range(invisibility_rounds):
            if i == invisibility_rounds - 1:
                damage_returned = 50  # Пример отраженного урона
                boss.take_damage(damage_returned)
                print(f"{hero.name} returned {damage_returned} damage to the boss after invisibility!")

def thor_special(hero, target, allies, boss):
    # Способность Тора: шанс оглушить босса
    if random.random() < 0.25:  # 25% шанс оглушить
        print(f"{hero.name} stunned the boss!")
        boss.attack = 0  # Босс пропускает следующий раунд

def kamikadze_special(hero, target, allies, boss):
    # Способность Камикадзе: наносит урон себе для атаки
    if random.random() < 0.8:  # 80% шанс попадания
        damage = hero.health * 2
        boss.take_damage(damage)
        print(f"{hero.name} sacrificed himself and dealt {damage} damage to the boss!")
    else:
        damage = hero.health / 2
        boss.take_damage(damage)
        print(f"{hero.name} missed the target and dealt {damage} damage!")

# Основной игровой цикл
def game_round(heroes, boss):
    print("\n--- New Round Starts ---")
    for hero in heroes:
        if hero.is_alive:
            hero.deal_damage(boss)
            print(f"{hero.name} attacked the boss!")

    # Босс атакует героев
    boss.attack_heroes(heroes)

    # Применяем суперспособности героев
    for hero in heroes:
        if hero.is_alive:
            hero.use_special_ability(hero, heroes, boss)

    # Проверка, жив ли босс
    if not boss.is_alive:
        print("The boss has been defeated!")
        return True

    # Проверка на живых героев
    all_dead = all(not hero.is_alive for hero in heroes)
    if all_dead:
        print("All heroes have died!")
        return True

    return False

# Инициализация героев
heroes = [
    Hero("Witcher", 100, 0, 10, witcher_special),
    Hero("Magic", 80, 20, 5, magic_special),
    Hero("Hacker", 70, 10, 5, hacker_special),
    Hero("Golem", 200, 15, 50, golem_special),
    Hero("Avrora", 90, 25, 10, avrora_special),
    Hero("Thor", 90, 30, 10, thor_special),
    Hero("Kamikadze", 100, 0, 30, kamikadze_special)
]

# Инициализация босса
boss = Boss(500, 40, 10)

# Игровой цикл
round_number = 1
while True:
    print(f"\n--- Round {round_number} ---")
    round_number += 1
    game_over = game_round(heroes, boss)
    if game_over:
        break
