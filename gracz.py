import abilities as a


class Player(a.abilities):
    hp = None
    mana = None
    strength = None
    max_hp = None
    def __init__(self, hp, mana, str):
        self.hp = hp
        self.mana = mana
        self.strength = str
        self.max_hp = hp


def gen_player():
    points = 25
    print(f"Witaj w kreatorze bohatera!, twoja pula punktów do wydania na siłę,"
          f" intelgiencję oraz witalność to {points}. Wybieraj odpowiedzialnie!")
    print("Ile punktów chcesz przeznaczyć na siłę? Siła odpowiada za moc jebnięcia! Wartość podstawowa to 1")
    temp = int(input())
    points -= temp
    strength = 1 + temp
    print(f"Twój wskazink siły wynosi {strength}, twoja pula punktów do wydania to {points},"
          f" ile punktów chcesz przeznaczyć na manę?")
    temp = int(input())
    points -= temp
    mana = 1 + temp
    print(f"Twój wskazink many wynosi {mana}, twoja pula punktów do wydania to {points},"
          f" ile punktów chcesz przeznaczyć na witalność?")
    temp = int(input())
    points -= temp
    hp = 1 + temp
    print(f"Twój wskazink witalności wynosi {hp}, twoja pula punktów do wydania to {points}")
    if points < 0:
        print("Zostało wydane więcej niż 25 punktów, jest to niedozowolone, zacznij od nowa.")
        gen_player()
    else:
        p = Player(hp, mana, strength)
        return p
