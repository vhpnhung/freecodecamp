import random

class Hat:
    def __init__(self, red=0, orange=0, black=0, blue=0, pink=0, striped=0, green=0):
        if red == orange == black == blue == pink == striped == 0:
            raise ValueError("At least 1 ball")
        else:
        # create contents instance attribute
            self.contents = []
            for _ in range(red):
                self.contents.append("red")
            for _ in range(orange):
                self.contents.append("orange")
            for _ in range(black):
                self.contents.append("black")
            for _ in range(blue):
                self.contents.append("blue")
            for _ in range(pink):
                self.contents.append("pink")
            for _ in range(striped):
                self.contents.append("striped")
            for _ in range(green):
                self.contents.append("green")


    
    def draw(self, number):
        # get a list of picked balls
        self.pick = []
        if number > len(self.contents):
            self.pick = self.contents
        else:
            for _ in range(number):
                self.pick.append(self.contents.pop(random.randrange(0,len(self.contents),1)))
        # count the number of balls picked of each color
        self.appeared = {}
        for color in self.pick:
            if color in self.appeared.keys():
                self.appeared[color]+=1
            else:
                self.appeared[color] = 1
        return self.appeared
            

def experiment(hat, num_balls_draw, expected_balls, num_experiments):
    bingo = 0               # represent the number of times the event occurs
    for _ in range(num_experiments):
        got_1_time = 0      # represent if a specific color is picked correctly as expected
        pick_result = hat.draw(num_balls_draw)
        for color in pick_result.keys():    # check each color if the number of balls picked satisfies expectation or not
            if color in expected_balls.keys():
                if pick_result[color] >= expected_balls[color]:
                    got_1_time+=1
        if got_1_time == len(expected_balls):   # if all colors expected are satisfied, the event occurs (bingo += 1)
            bingo+=1
    return bingo/num_experiments    # probability