from game import Paladin, Item, Boss

def main():
    print("--- ИГРА НАЧИНАЕТСЯ: ЛЕГЕНДАРНАЯ КОМАНДА ---")
    
    hero = Paladin(name="Артур")
    print(f"Создан герой: {hero.name} (Класс: Паладин, Здоровье: {hero.health}, Атака: {hero.attack_power})")

    legendary_sword = Item(name="Светоносный Меч", attack_bonus=15)
    hero.inventory.append(legendary_sword)
    print(f"В инвентарь добавлен предмет: {legendary_sword.name}")

    hero.use_item("Светоносный Меч")

    boss = Boss(name="Дракон Опустошитель", health=250, attack_power=25)
    print(f"\n⚠️ ВНИМАНИЕ! Появился босс: {boss.name} (Здоровье: {boss.health}, Атака: {boss.attack_power})")
    print("--- НАЧАЛО БОЯ С БОССОМ ---")

    round_counter = 1
    while hero.is_alive() and boss.is_alive():
        print(f"\n--- Раунд {round_counter} ---")

        if round_counter % 2 != 0:
            hero.special(boss)
            boss.take_damage(hero.attack_power)
        else:
            hero.attack(boss)

        if not boss.is_alive():
            break

        boss.attack(hero)
        round_counter += 1

    print("\n--- КОНЕЦ ИГРЫ ---")
    if hero.is_alive():
        print(f"🏆 ПОБЕДА! {hero.name} одолел {boss.name}!")
    else:
        print(f"💀 ПОРАЖЕНИЕ! {hero.name} пал в бою с {boss.name}...")

if __name__ == "__main__":
    main()