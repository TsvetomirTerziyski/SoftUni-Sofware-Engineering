def cast_spell(name_of_hero, mp_needed, name_of_spell, heroes_dict):
    if heroes_dict[name_of_hero][1] >= mp_needed:
        heroes_dict[name_of_hero][1] -= mp_needed
        return f"{name_of_hero} has successfully cast {name_of_spell} and now has {heroes_dict[name_of_hero][1]} MP!"
    return f"{name_of_hero} does not have enough MP to cast {name_of_spell}!"


def take_damage(name_of_hero, damage_dealt, attacker_name, heroes_dict):
    heroes_dict[name_of_hero][0] -= damage_dealt
    if heroes_dict[name_of_hero][0] > 0:
        return f"{name_of_hero} was hit for {damage_dealt} HP by {attacker_name} " \
               f"and now has {heroes_dict[name_of_hero][0]} HP left!"
    else:
        del heroes_dict[name_of_hero]
        return f"{name_of_hero} has been killed by {attacker_name}!"


def recharge(name_of_hero, recharge_amount, heroes_dict):
    heroes_dict[name_of_hero][1] += recharge_amount
    if heroes_dict[name_of_hero][1] > 200:
        recharge_amount = recharge_amount - (heroes_dict[name_of_hero][1] - 200)
        heroes_dict[name_of_hero][1] = 200
    return f"{name_of_hero} recharged for {recharge_amount} MP!"


def heal(name_of_hero, heal_amount, heroes_dict):
    heroes_dict[name_of_hero][0] += heal_amount
    if heroes_dict[name_of_hero][0] > 100:
        heal_amount = heal_amount - (heroes_dict[name_of_hero][0] - 100)
        heroes_dict[name_of_hero][0] = 100
    return f"{name_of_hero} healed for {heal_amount} HP!"


number_of_heroes = int(input())
heroes = {}

for hero in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = [int(hit_points), int(mana_points)]

command = input().split(' - ')

while command[0] != 'End':
    if command[0] == 'CastSpell':
        hero_name, mana_points_needed, spell_name = command[1], int(command[2]), command[3]
        print(cast_spell(hero_name, mana_points_needed, spell_name, heroes))
    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        print(take_damage(hero_name, damage, attacker, heroes))
    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])
        print(recharge(hero_name, amount, heroes))
    elif command[0] == 'Heal':
        hero_name, amount = command[1], int(command[2])
        print(heal(hero_name, amount, heroes))

    command = input().split(' - ')

for hero, hp_mp in heroes.items():
    print(f'{hero}')
    print(f'  HP: {hp_mp[0]}')
    print(f'  MP: {hp_mp[1]}')
