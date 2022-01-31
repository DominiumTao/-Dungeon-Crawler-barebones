
class Przeciwnik:
    hp = None
    mana = None
    CqFightAbiliy = None
    name = None
    xp = None
    def __init__(self, hp, mana, cq, name, xp):
        self.hp = hp
        self.mana = mana
        self.CqFightAbiliy = cq
        self.name = name
        self.xp = xp
    def __str__(self):
        return f"Klasa odpowiadająca za generowanie i przydzielanie umiejętności przeciwników"