import random
from collections import Counter


class Greed:
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func

    def roll_dice(self):
        dice = []
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))

        return dice

    # Calculate the score
    def calculate_score(self, dice):
        total = 0
        cnt = Counter(dice)
        # for num in dice:
        #     cnt[num] += 1
        # cnt

        print(cnt)
        print("")

        one = 100
        five = 50

        for key, value in cnt.items():

            # Straight Score
            if (
                value == 1
                and value == 2
                and value == 3
                and value == 4
                and value == 5
                and value == 6
            ):
                total += 1500
                break

            # One Score
            if key == 1:
                if value == 6:
                    total += one * 40
                elif value == 5:
                    total += one * 30
                elif value == 4:
                    total += one * 20
                elif value == 3:
                    total += one * 10
                else:
                    total += value * one

            # Two Score
            if key == 2:
                if value == 6:
                    total += 800
                elif value == 5:
                    total += 600
                elif value == 4:
                    total += 400
                elif value == 3:
                    total += 200
                else:
                    total += 0

            # Three Score
            if key == 3:
                if value == 6:
                    total += 1200
                elif value == 5:
                    total += 900
                elif value == 4:
                    total += 600
                elif value == 3:
                    total += 300
                else:
                    total += 0

            # Four Score
            if key == 4:
                if value == 6:
                    total += 1600
                elif value == 5:
                    total += 1200
                elif value == 4:
                    total += 800
                elif value == 3:
                    total += 400
                else:
                    total += 0

            # Five Score
            if key == 5:
                if value == 6:
                    total += five * 40
                elif value == 5:
                    total += five * 30
                elif value == 4:
                    total += five * 20
                elif value == 3:
                    total += five * 10
                else:
                    total += value * five

            # Six Score
            if key == 6:
                if value == 6:
                    total += 2400
                elif value == 5:
                    total += 1800
                elif value == 4:
                    total += 1200
                elif value == 3:
                    total += 600
                else:
                    total += 0
            
        return total    

        print(total)

    def play(self, user_response=None):
        self._print("Welcome to Game of Greed!")
        response = self._input("Wanna play? ")

        if response == "y" or user_response == "y":
            self._print("Great! Check back tomorrow!")
        else:
            self._print("OK. Maybe another time")


if __name__ == "__main__":
    game = Greed()
    game.play()
