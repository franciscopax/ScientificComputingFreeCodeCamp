import copy
import random


class Hat:

    contents = []

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

            
    def draw(self, numberOfBalls):

        contents = copy.copy(self.contents)
        draw = []

        for _ in range(numberOfBalls):
            length = len(contents) 
            index = random.randrange(length)
            ball = contents[index]
            draw.append(ball)
            contents = contents[0:index] + contents[index + 1:]

        self.contents = contents
        return draw


# Second part

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    numberOfOccurences = 0

    # Check that there are enough balls

    for key, value in expected_balls.items():
        if value > hat.contents.count(key):
            return f'Error. You don\'t have enough {key} balls.'

    for _ in range(num_experiments):

        preliminaryResult = 0

        hatCopy = copy.copy(hat)

        currentDraw = hatCopy.draw(num_balls_drawn)

        for key, value in expected_balls.items():

            if currentDraw.count(key) >= value:
                preliminaryResult += 1


        if preliminaryResult == len(expected_balls):
            numberOfOccurences += 1

    return numberOfOccurences / num_experiments




b1 = Hat(blue=4, red=2, green=6)
# print(hat.draw(6))

probability = experiment(
    hat=b1,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=200)

print("Probability:", probability)