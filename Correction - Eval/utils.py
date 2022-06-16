import random


class Utils:

    def check_odd_or_even(self, nbr_marbles_of_enemy, choice):
        if nbr_marbles_of_enemy % 2 == 0:  # odd number
            if choice == 2:
                return True  # means I was right
        else:  # even number
            if choice == 1:
                return True  # means I was right
        return False

    ##
    ## Return a random value
    ##
    def random_values(self, min_value, max_value):
        return random.randint(min_value, max_value)
