import random
from random import randint
import enemy as e
import abilities
import gracz as p

# 0 - niewygenerowane
# 1 - start
# 2 - ścieżka
# 3 - ściana
# 5 \058D - portal
global map
global max_index
global dist_map
global player

class lvl:
    lvl = 1
    def add(self):
        self.lvl += 1

def gy():
    global map
    global max_index
    global dist_map
    global player
    max_index = 10
    player_start = int(max_index / 2)
    map = [[0 for x in range(max_index)] for y in range(max_index)]

    map[player_start][player_start] = 'S'

    dist_map = [[0 for x in range(max_index)] for y in range(max_index)]
    dist_map[player_start][player_start] = 1
    player = [player_start, player_start]
gy()



def gen(x, y, distance):
    if x == 0 or x == (max_index - 1) or y == 0 or y == (max_index - 1):
        map[x][y] = 3
    if map[x][y] == 0:
        temp = randint(0, 100)
        print(distance)
        if temp > (30 + 3 * distance):
            map[x][y] = 2
            dist_map[x][y] = distance + 1
        else:
            temp = randint(0, 100)
            if temp > 5 + (distance * 3):
                map[x][y] = 3
            else:
                map[x][y] = 5
    if map[x][y] == 'I':
        map[x][y] = 2


def checkIfPath(x, y):
    return map[x][y]


def Statystki(gracz):
    print(f"Statystki gracza:\n HP: {gracz.hp}\n Combat Skill: {gracz.strength},\n Magick Skill: {gracz.mana}")


def move(gracz):
    print()
    print("1 góra, 2 prawo, 3 dół, 4 lewo, 0 statystki, 9 leczenie ")
    inp = int(input())
    match inp:
        case 1:
            if checkIfPath(player[0] - 1, player[1]) == 2:
                player[0] -= 1
                generate(player[0], player[1])
                encounter(gracz)
            elif checkIfPath(player[0] - 1, player[1]) == 5:
                print("Portal do nowej komanty czy chcesz przejść dalej? y/n")
                temp = input()
                if temp == 'y':
                    lvl.add(lvl)
                    gy()
                    generate(player[0], player[1])
            else:
                print("Unable to comply, wall in the way")
        case 2:
            if checkIfPath(player[0], player[1] + 1) == 2:
                player[1] += 1
                generate(player[0], player[1])
                encounter(gracz)
            elif checkIfPath(player[0], player[1] + 1) == 5:
                print("Portal do nowej komanty czy chcesz przejść dalej? y/n")
                temp = input()
                if temp == 'y':
                    lvl.add(lvl)
                    gy()
                    generate(player[0], player[1])
            else:
                print("Unable to comply, wall in the way")
        case 3:
            if checkIfPath(player[0] + 1, player[1]) == 2:
                player[0] += 1
                generate(player[0], player[1])
            elif checkIfPath(player[0] + 1, player[1]) == 5:
                print("Portal do nowej komanty czy chcesz przejść dalej? y/n")
                temp = input()
                if temp == 'y':
                    lvl.add(lvl)
                    gy()
                    generate(player[0], player[1])
            else:
                print("Unable to comply, wall in the way")
        case 4:
            if checkIfPath(player[0], player[1] - 1) == 2:
                player[1] -= 1
                generate(player[0], player[1])
                encounter(gracz)
            elif checkIfPath(player[0], player[1] - 1) == 5:
                print("Portal do nowej komanty czy chcesz przejść dalej? y/n")
                temp = input()
                if temp == 'y':
                    lvl.add(lvl)
                    gy()
                    generate(player[0], player[1])
            else:
                print("Unable to comply, wall in the way")
        case 0:
            Statystki(gracz)
        case 9:
            gracz.hp = gracz.max_hp
            print("Użyto leczenia!")
        case _:
            print("The numbers Mason, what do they mean!")


def Random_Enemy():
    r = random.randint(0, 4)
    x = lvl.lvl
    match r:
        case 0:
            p = e.Przeciwnik(5*x, 20*x, 40*x, "Gremlin", 3*x)
            return p
        case 1:
            p = e.Przeciwnik(10*x, 60*x, 20*x, "Czarodziej Goblin", 4*x)
            return p
        case 2:
            p = e.Przeciwnik(52*x, 0*x, 5*x, "Ogr", 5*x)
            return p
        case 3:
            p = e.Przeciwnik(10*x, 40*x, 40*x, "Kultysta", 6*x)
            return p
        case 4:
            p = e.Przeciwnik(15*x, 60*x, 10*x, "Czeladnik Kultysta", 7*x)
            return p


def generate(x, y):
    gen(x - 1, y, dist_map[x][y])
    gen(x + 1, y, dist_map[x][y])
    gen(x, y - 1, dist_map[x][y])
    gen(x, y + 1, dist_map[x][y])
    map[x][y] = 'I'


def wygrana(gracz, exp):
    Statystki(gracz)
    print(f"Którą ze statysyk chcesz rozwinąć o dostępny XP {exp}: 1.HP, 2.Combat Skill, 3. Magick Skill")
    temp = int(input())
    match temp:
        case 1:
            gracz.max_hp = gracz.max_hp + exp
        case 2:
            gracz.strength = gracz.strength + exp
        case 3:
            gracz.mana = gracz.mana + exp
        case _:
            print("wybrano złą umiejęntość spróbuj jeszcze raz!")
            wygrana(gracz, exp)


def encounter(gracz):
    temp = randint(0, 100)
    e = Random_Enemy()
    if temp > 75:
        print(f"Walka! Walczsz z {e.name}")
        while temp > 75:
            abilities.abilities.walka(abilities, e, gracz)
            abilities.abilities.walka_ai(abilities, e, gracz)
            if e.hp < 0:
                print("Przeciwnik został zabity brawo!")
                wygrana(gracz, e.xp)
                break
            elif gracz.hp < 0:
                print("Przegrałeś zacznij od nowa!")
                exit()


def printmap():
    for line in map:
        for element in line:
            if element == 0:
                print(' ', end=' ')
            elif element == 3:
                print('\u2588', end=' ')
            elif element == 2:
                print('\u2261', end=' ')
            elif element == 5:
                print("\u058d", end=' ')
            else:
                print(element, end=' ')
        print()





def main():
    gracz = p.gen_player()
    generate(player[0], player[1])
    while True:
        printmap()
        move(gracz)


main()
