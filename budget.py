class Category():

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        if amount <= 0:
            raise ValueError("Amount must be more than 0")
        self.ledger.append({"amount":amount, "description": description})
        self.balance += amount
        
    def withdraw(self, amount, description=""):
        if amount > self.balance:
            return False
        else:
            self.ledger.append({"amount":-1*amount, "description": description})
            self.balance -= amount
            return True

    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, destination):
        withdrawal = self.withdraw(amount, description=f"Transfer to {destination.name}")
        if withdrawal == True:
            destination.deposit(amount, description=f"Transfer from {self.name}")
            return True
        else:
            return False

    def show_list(self):
        # first line ****
        if len(self.name)%2 == 0:
            decor1 = decor2 = "*"*int((30-len(self.name))/2)
        else:
            decor1 = "*"*int((30-len(self.name)-3)/2)
            decor2 = "*"*int((30-len(self.name)-1)/2)
        print(decor1, self.name, decor2)

        # all
        for i in range(len(self.ledger)):
            if len(self.ledger[i]["description"]) >= 23:
                print(self.ledger[i]["description"][:24], end="  ")
            else:
                print(self.ledger[i]["description"], end=" "*(30-len(str(self.ledger[i]["amount"]))-len(self.ledger[i]["description"])))
            print(self.ledger[i]["amount"], end="\n")




def create_spend_chart(objects):
    # create a storage for y_axis items
    y_axis = {}
    for i in range(0,110,10):
        y_axis[i] = []
    
    # calculate the number of "o"
    total = 0
    seg = {}
    for category in objects:
        total += category.balance
    for category in objects:
        seg[category.name] = int(category.balance/total*10)
    
    # store "o" into storage
    for category in seg.keys():
        # draw "o"
        for o in range(seg[category]+1):
            y_axis[o*10].append("O")
        # insert empty
        for x in range(seg[category]+1,len(y_axis)):
            y_axis[x*10].append(" ")
    
    # draw the chart
        # def a draw function
    def draw(number):
        for draw in y_axis[number]:
            print(draw, end="\t")
        # y_axis name
    print("Percentage spent by category")
        # draw 100-line
    print("100|", end="\t")
    draw(100)
        # draw 90-10 lines
    for line in range(90,0,-10):
        print("\n "+str(line)+"|", end="\t")
        draw(line)
        # draw 0-line
    print("\n  0|", end="\t")
    draw(0)

        # draw ----- line
    print("\n","-"*30)

        # draw category name (vetical)
    print(" "*4,end="\t")
            # store name (like "o")
    max_length = 0
    for category in objects:
        if len(category.name) >= max_length:
            max_length = len(category.name)
    char = []
    for category in objects:
        char.append(category.name+" "*(max_length-len(category.name)))
    character_list = []
    for line in range(max_length):
        character_list.append([])
        for item in char:
            character_list[line].append(item[line])
            # draw based on character_list
        for letter in character_list[line]:
            print(letter, end="\t")
        print("\n", end=" "*4+"\t")