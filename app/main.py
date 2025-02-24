class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __del__(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    @staticmethod
    def print_alive() -> list:
        return [{"Name": animal.name,
                 "Health": animal.health,
                 "Hidden": animal.hidden}
                for animal in Animal.alive]

    def __str__(self) -> str:
        return str(self.print_alive())


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                del herbivore
