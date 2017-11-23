#  Lab 7
#  Manage ticket sales for a theater, OOP
#

from chart import Chart

def main():
   c = Chart()
   buying = 'y'
   while buying == 'y':
      c.buySeat()
      buying = input("Continue to buy seats? y/n: ")

main()

