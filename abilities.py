
class skills:
    ReqCqSkill = None
    ReqMagSkill = None
    Attack = None
    Result = None
    Name = None

    def __init__(self, cq, mag, Result, Type, Name):
        self.ReqCqSkill = cq
        self.ReqMagSkill = mag
        self.Type = Type #0/1 Pancerze, zoabczę czy dodam typu magiczny i fizyczny
        self.Result = Result
        self.Name = Name


class abilities(skills):
    global sf1
    global sf2
    global sf3
    global sm4
    global sm5
    global sm6
    sf1 = skills(0, 0, -1, 0, "Uderzenie wręcz")
    sf2 = skills(5, 0, -3, 0, "Uderzenie bronią")
    sf3 = skills(15, 0, -5, 0, "Zaawansowane uderzenie bornią")
    sm4 = skills(0, 0, 3, 0, "Leczenie")
    sm5 = skills(5, 0, -5, 0, "Fireball")
    sm6 = skills(15, 0, -10, 0, "Blood sucking")
    def walka(self, e, gracz):
        print(f"Statystki gracza:\n HP: {gracz.hp}\n Combat Skill: {gracz.strength},\n Magick Skill: {gracz.mana}")
        print("Wybierz element do castowania")
        print(f"1.{sf1.Name}, wymagane Combat Skill to:{sf1.ReqCqSkill}, wymagane Magick Skill to: {sf1.ReqMagSkill}\n"
              f"2.{sf2.Name}, wymagane Combat Skill to:{sf2.ReqCqSkill}, wymagane Magick Skill to: {sf2.ReqMagSkill}\n"
              f"3.{sf3.Name}, wymagane Combat Skill to:{sf3.ReqCqSkill}, wymagane Magick Skill to: {sf3.ReqMagSkill}\n"
              f"4.{sm4.Name}, wymagane Combat Skill to:{sm4.ReqCqSkill}, wymagane Magick Skill to: {sm4.ReqMagSkill}\n"
              f"5.{sm5.Name}, wymagane Combat Skill to:{sm5.ReqCqSkill}, wymagane Magick Skill to: {sm5.ReqMagSkill}\n"
              f"6.{sm6.Name}, wymagane Combat Skill to:{sm6.ReqCqSkill}, wymagane Magick Skill to: {sm6.ReqMagSkill}\n")
        temp = int(input())
        match temp:
            case 1:
                if gracz.strength > sf1.ReqCqSkill:
                    e.hp = e.hp + sf1.Result
                else:
                    print(f"Próbowałeś wykonać {sf1.Name}, lecz nie udało Ci się tracisz turę!")
            case 2:
                if gracz.strength > sf2.ReqCqSkill:
                    e.hp = e.hp + sf2.Result
                else:
                    print(f"Próbowałeś wykonać {sf2.Name}, lecz nie udało Ci się tracisz turę!")
            case 3:
                if gracz.strength > sf3.ReqCqSkill:
                    e.hp = e.hp + sf3.Result
                else:
                    print(f"Próbowałeś wykonać {sf3.Name}, lecz nie udało Ci się tracisz turę!")
            case 4:
                if gracz.mana > sm4.ReqMagSkill:
                    if gracz.max_hp < gracz.hp:
                        gracz.hp = gracz.hp + sm4.Result
                    else:
                        gracz.hp = gracz.max_hp
                        print("Uleczono do wartości maksymalnej")
                else:
                    print(f"Próbowałeś wykonać {sm4.Name}, lecz nie udało Ci się tracisz turę!")
            case 5:
                if gracz.mana > sm5.ReqMagSkill:
                    e.hp = e.hp + sm5.Result
                else:
                    print(f"Próbowałeś wykonać {sm5.Name}, lecz nie udało Ci się tracisz turę!")
            case 6:
                if gracz.mana > sm6.ReqMagSkill:
                    e.hp = e.hp + sm6.Result
                else:
                    print(f"Próbowałeś wykonać {sm6.Name}, lecz nie udało Ci się tracisz turę!")
            case _:
                print("Wybrano umiejętność spoza listy, to znaczy że nie wykonujesz żadnej czynności :)")
    def walka_ai(self, e, gracz):
        mana = e.mana
        cq = e.CqFightAbiliy
        hp = e.hp
        if hp < (hp*0.25):
            e.hp = hp + sm4.Result
            print("Przeciwnik użył leczenie!")
        elif cq > sf3.ReqCqSkill:
            gracz.hp = gracz.hp + sf3.Result
            print(f"Przeciwnik użył {sf3.Name} i zadał {sf3.Result} obrażeń")
        elif cq > sf2.ReqCqSkill:
            gracz.hp = gracz.hp + sf2.Result
            print(f"Przeciwnik użył {sf2.Name} i zadał {sf2.Result} obrażeń")
        elif mana > sm5.ReqMagSkill:
            gracz.hp = gracz.hp + sm5.Result
            print(f"Przeciwnik użył {sm5.Name} i zadał {sm5.Result} obrażeń")
        elif mana > sm6.ReqMagSkill:
            gracz.hp = gracz.hp + sm6.Result
            print(f"Przeciwnik użył {sm6.Name} i zadał {sm6.Result} obrażeń")
        else:
            gracz.hp = gracz.hp + sf1.Result
            print(f"Przeciwnik użył {sf1.Name} i zadał {sf1.Result} obrażeń")
    def __str__(self):
        return f"Opis zmiennych ReqCqSkill - wymagana wartość walki wręcz" \
               f"ReqMagSkill - wymagana wartość magii" \
               f"Attack - czy umiejętność służąca do ataku 0 nie, 1 tak" \
               f"Reult - Wynik, +100, -50, +5, planowana możliwość wyboru co zostanie zmodyfikiowane, tj. dany skill " \
               f"czy może życie." \
               f"Klasa ta odpowidoa za generowanie umiejętności możliwych do użycia przez bohatera i przeciwników" \
               f", zależynych od wymaganych umiejętności walki wręcz i posługiwania się magią."




#chuj ci w pizde



















"""
    def AbilitiyFired(self):
        if self.ReqCqSkill < self.CasterPlaceHolder[0]:
            if self.Attack == 0:
                self.SubjectPlaceHolder[1] += self.Result
            else:
                self.SubjectPlaceHolder[1] += self.Result
        elif self.ReqMagSkill < self.CasterPlaceHolder[0]:
            if self.Attack == 0:
                self.SubjectPlaceHolder[0] += self.Result
            else:
                self.SubjectPlaceHolder[1] += self.Result
"""
