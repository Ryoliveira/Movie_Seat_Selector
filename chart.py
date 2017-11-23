# Ryan Oliveira
# Lab 7
from seat import Seat, Premium, Choice, Regular


class Chart():

    def __init__(self):
        """ reads in seating chart from a file and creates seat object accordingly
                for each price in file, then prints chart to screen
                    formatted chart to screen
                        @param: None
                        @return: None
        """
        self._chart = []  # Stores chart in a list of lists
        while True:
            filename = input("Enter file name or hit Enter for default lab7input2.txt: ")
            if filename == "":
                filename = "lab7input2.txt "  # Default file if nothing is entered
            try:
                with open(filename, "r") as fileObj:
                    firstRow = fileObj.readline().strip().split()
                    for row in fileObj:
                        self._chart.append(row.strip().split())
                    for i, seatRow in enumerate(self._chart):
                        for j, eachSeat in enumerate(seatRow):
                            if eachSeat == firstRow[0]:
                                self._chart[i][j] = Premium(eachSeat)
                            if eachSeat == firstRow[1]:
                                self._chart[i][j] = Choice(eachSeat)
                            if eachSeat == firstRow[2]:
                                self._chart[i][j] = Regular(eachSeat)

                break
            except FileNotFoundError:
                print("Can't open", filename)
        Chart.print(self)

    def print(self):
        """ Prints seating chart to screen
                    @param: Self
                    @return: None
        """
        print("    " * (len(self._chart[0]) // 2) + "   Price Chart")
        print("     " * (len(self._chart[0]) // 2) + "Columns")
        print("      ", end="")
        for col in range(len(self._chart[0])):
            print(col + 1, end="    ")
        print("")
        print("Row " + ("=====" * len(self._chart[0])))
        for row in range(len(self._chart)):  # Print each Row
            print(" " + str(row + 1) + " |  ", end="")
            for col in range(len(self._chart[0])):  # Print each column
                if self._chart[row][col].isTaken():
                    print("" + self._chart[row][col].getPrice(), end="    ")
                else:
                    print("$%-4s" % int(self._chart[row][col].getPrice()), end="")
            print("")

    def buySeat(self):
        """ Lets user select desired seats, will display error message
                and reprompt user for input if seat is already selected
                    @param: Self
                    @return: None
        """
        savedSeats = []  # Seats selected saved as a list of tuples
        total = 0  # Price of all seats selected added together
        numSeats = 0  # Number of seats selected by user
        seatChoice = ""  # Users seat selection input
        while seatChoice != "0":
            seatChoice = input("Enter row,col for seat " + str(numSeats + 1) + " or enter 0 to end:")
            if seatChoice == "0":
                continue
            try:
                rowChoice, colChoice = seatChoice.split(",")
                if int(rowChoice) < 1 or int(colChoice) < 1:
                    print("Invalid row or column")
                    continue
                if self._chart[int(rowChoice) - 1][int(colChoice) - 1].isTaken():
                    print("Seat is already taken, make another selection")
                    continue

            except (IndexError, ValueError):
                print("Invalid row or column")
                continue
            numSeats += 1
            total += int(self._chart[int(rowChoice) - 1][int(colChoice) - 1].getPrice())
            self._chart[int(rowChoice) - 1][int(colChoice) - 1].selected()
            savedSeats.append((rowChoice, colChoice))
        print("Your total: $" + str(total))
        print("For your", numSeats, "seat(s) at: ")
        for seat in savedSeats:
            print("Row", seat[0], "Column", seat[1] + ":", self._chart[int(seat[0]) - 1][int(seat[1]) - 1].getExtra())
        print("Your seats are marked with 'X'")
        Chart.print(self)
