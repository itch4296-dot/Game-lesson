class Item:
    def __init__(self, name, attack_bonus=0, heal_bonus=0):
        self.name = name
        self.attack_bonus = attack_bonus
        self.heal_bonus = heal_bonus

    def __str__(self):
        return self.name


class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.inventory = []  # Задание 2: Предметы хранятся в Inventory

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"💥 {self.name} получает {damage} урона. Осталось здоровья: {self.health}")

    def attack(self, target):
        damage = self.attack_power
        print(f"⚔️ {self.name} атакует {target.name} на {damage} урона!")
        target.take_damage(damage)

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                if item.attack_bonus > 0:
                    self.attack_power += item.attack_bonus
                    print(f"🗡️ {self.name} экипирует {item.name}! Атака выросла на +{item.attack_bonus} (Текущая: {self.attack_power})")
                if item.heal_bonus > 0:
                    self.health = min(self.max_health, self.health + item.heal_bonus)
                    print(f"🧪 {self.name} выпивает {item.name}! Здоровье восстановлено до {self.health}")
                self.inventory.remove(item)
                return
        print(f"Предмет {item_name} не найден в инвентаре.")


class Paladin(Hero):
    def __init__(self, name, health=140, attack_power=20):
        super().__init__(name, health, attack_power)
        self.shield_charges = 2  # Количество использований щита

    def special(self, target):
        if self.shield_charges > 0:
            heal_amount = 30
            self.health = min(self.max_health, self.health + heal_amount)
            self.attack_power += 5
            self.shield_charges -= 1
            print(f"✨ {self.name} использует SPECIAL() 'Святой Щит'! +{heal_amount} к ОЗ и +5 к атаке! (Зарядов осталось: {self.shield_charges})")
        else:
            print(f"💨 У {self.name} не осталось зарядов для щита! Бьем обычной атакой.")
            self.attack(target)


class Boss:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"👹 {self.name} ранен! Осталось здоровья: {self.health}")

    def attack(self, target):
        print(f"🔥 {self.name} наносит сокрушительный удар по {target.name}!")
        target.take_damage(self.attack_power)