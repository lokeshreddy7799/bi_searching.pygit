class House:
    def __init__(self, rooms, doors, windows):
        self.rooms = rooms
        self.doors = doors
        self.windows = windows

    def describe(self):
        print(f"This house has {self.rooms} rooms, {self.doors} doors, and {self.windows} windows.")

class BeachHouse(House):
    def __init__(self, rooms, doors, windows, deck, ocean_view_windows):
        super().__init__(rooms, doors, windows)
        self.deck = deck
        self.ocean_view_windows = ocean_view_windows

    def describe(self):
        super().describe()
        print(f"It also has a {self.deck} and {self.ocean_view_windows} windows for ocean views.")


generic_house = House(3, 4, 8)
beach_house = BeachHouse(3, 4, 8, "large deck", 10)

generic_house.describe()
beach_house.describe()
