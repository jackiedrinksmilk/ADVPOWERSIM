class Bus:

    counter = 0

    def __init__(self, name: str):

        self.name: str = name
        self.index: int = Bus.counter

        Bus.counter = Bus.counter + 1