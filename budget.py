class Category:

    def __init__(self, name):
        self.name = name
        self.balance = 0.00
        self.ledger = []

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        if self.balance - amount >= 0:
            return True
        else:
            return False    

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": amount * -1, "description": description})
            self.balance -= amount
            return True

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

    def __str__(self):

        asterisks = int((30 - len(self.name)) / 2)
        printable = ('*' * asterisks) + self.name + '*' * (30 - (asterisks + len(self.name))) + '\n'

        for item in self.ledger:

            formattedDescription = ''
            formattedAmount = '%.2f' % item['amount']
            extraSpaceForNumber = ' ' * (7 - len(str(formattedAmount)))

            if len(item['description']) > 23:
                formattedDescription = item['description'][:23]
            else:
                formattedDescription = item['description'] + ' ' * (23 - len(item['description']))

            printable += f'{formattedDescription}{extraSpaceForNumber}{formattedAmount}\n'
            
            # formattedDescription + ' ' + str(item['amount']) + '\n'

        printable += f'Total: {self.balance}'

        return printable


# Todo

def create_spend_chart(categories):

    sums = {}

    # ---------------------
    # Calculate totals of each category

    for category in categories:

        sums[category.name] = 0
        
        for item in category.ledger:

            if item['amount'] < 0:

                sums[category.name] += abs(item['amount'])

        sums[category.name] = int(sums[category.name])

    # ---------------------
    # Calculate actual total

    sums['Total'] = 0

    for category in categories:

        sums['Total'] += sums[category.name]

    # ---------------------
    # Turn totals into percentages

    percentageTotals = {}

    for category in categories:

        percentageTotals[category.name] =  int( ( sums[category.name] / sums['Total'] ) * 100 )

        # Round numbers 
         
        if percentageTotals[category.name] > 10:
            if percentageTotals[category.name] % 10 >= 5:
                percentageTotals[category.name] = percentageTotals[category.name] + (10 - (percentageTotals[category.name] % 10))
            else:
                percentageTotals[category.name] = percentageTotals[category.name] - (percentageTotals[category.name] % 10)
        else: 
            percentageTotals[category.name] = percentageTotals[category.name] 


    # ---------------------
    # Create the graph

    # Which of the categoris has the longest name

    names = []

    for category in categories:
        names += [category.name]

    # Calculate Iterations

    yAxis = 100
    iterations = int(yAxis / 10 + 2 + len(max(names, key=len)))

    # Variables for graph plotting

    graph = 'Percentage spent by category\n'
    letterIterator = 0

    while iterations > 0:

        iterations -= 1

        # Y Axis numbers

        if yAxis == 100:
            graph += str(yAxis) + '|'
        elif yAxis > 0:
            graph += ' ' + str(yAxis) + '|'
        elif yAxis == 0:
            graph += '  ' + str(yAxis) + '|'
        elif yAxis < 0:
            graph += '    '

        # This should only be done while there's a y axis

        if yAxis >= 0:

            for _,value in percentageTotals.items():
                if value >= yAxis:
                    graph += ' o '
                elif value > yAxis:
                    graph += '   '
                else:
                    graph += '   '

            graph += ' \n'

        if yAxis == -10:

            graph += '---' * len(names) + '-\n'

        # The names of the categories

        if yAxis < -10:
        
            for name in names:

                graph += ' '

                try:
                    graph += name[letterIterator]
                except:
                    graph += ' '

                graph += ' '

            
            if iterations > 0:
                graph += ' \n'
            else: 
                graph += ' '

            letterIterator += 1

        yAxis -= 10
        
    return graph


entertainment = Category("Entertainment")
entertainment.deposit(700)

food = Category("Food")
food.deposit(900)
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)

print(food)
print(entertainment)



# food = Category("Food")
# entertainment = Category("Entertainment")
# business = Category("Business")
# business.deposit(900, 'deposit')
# business.withdraw(10.99)
# food.deposit(900, 'deposit')
# food.withdraw(105.55)
# entertainment.deposit(900)
# entertainment.withdraw(33.40)

# print(food, business, entertainment)



# print(create_spend_chart([business, food, entertainment]))




# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# # print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)

# print(create_spend_chart([food, clothing, auto]))

# print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")



# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# self.food.withdraw(105.55)
# self.entertainment.withdraw(33.40)
# self.business.withdraw(10.99)
# actual = create_spend_chart([self.business, self.food, self.entertainment])