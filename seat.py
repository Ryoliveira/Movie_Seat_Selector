# Ryan Oliveira
# Lab 7

class Seat():
    def __init__(self, price=0, taken=0):
        """ Initializes Price and Taken
            @param: price, taken
            @return: None"""
        self._price = price
        self._taken = taken

    def getPrice(self):
        """Returns price of seat
            @param: Self
            @return: self._price"""
        return self._price

    def isTaken(self):
        """Returns True or False
            @param: self
            @return: """
        return bool(self._taken)

    def selected(self):
        """Changes taken to true and marks
            location with 'X'
            @param: self
            @return: none
        """
        self._taken = 1
        self._price = 'X'

    def getExtra(self):
        """Abstract method for super class
            @param: self
            @return: NotImplementedError Error"""
        raise NotImplementedError


class Premium(Seat):
    def __init__(self, price):
        """Initializes superclass variables
            @param: price, taken
            @return: none"""
        super().__init__(price)

    def getExtra(self):
        """Returns perks for Premium seat
           @param: self
           @return: string
        """
        return "Your Swag bag and food discount are available at will call"


class Choice(Seat):
    def __init__(self, price):
        """Initializes superclass variables.
                    @param: price, taken
                    @return: none
        """
        super().__init__(price)

    def getExtra(self):
        """Returns perks for Premium seat.
                   @param: self
                   @return: string
        """
        return "Your Drink discount is available at will call"


class Regular(Seat):
    def __init__(self, price):
        """Initializes superclass variables.
                    @param: price, taken
                    @return: none
        """
        super().__init__(price)

    def getExtra(self):
        """Returns perks for Premium seat.
                   @param: self
                   @return: string
        """
        return "Drinks and snacks are available for purchase at intermission"
