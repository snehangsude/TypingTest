from data import data
import random
import math


class TypeBrain:
    """
    TypeBrain class that initializes the WPM and the CPM count based on the minutes provided in the detailing of the
    program in the UI module. Initializes the score and the selected typing data from the data module.

    Additionally keeps track of the score and helps check the user input typing with the actual selection
    """

    def __init__(self):
        """
        Initializes the TypingBrain class with :
        WPM - Words per minute
        CPM - Char count
        Score - score
        Typing Text = Actual Selection
        """
        self.words_per_min = 0
        self.char_count = 0
        self.score = self.score_update()
        self.actual_selection = None

    def select_stanza(self):
        """
        Function to select a random typing data from the data module
        :return:
        The string to the selected text in the data module
        """
        self.actual_selection = random.choice(data)
        return self.actual_selection

    def calculate_result(self, user_data: str):
        """
        Function that helps check the user entered data with the original data, while also updating the score
        if the score is higher than the previous score
        :param user_data: Takes a string input of the user entered text
        :return: Returns a tuple of CPM, WPM and length of user_data
        """
        original_char_count = len(user_data)
        split_user_data = user_data.split()
        split_original = self.actual_selection.split()
        for words in range(len(split_user_data)):
            if split_user_data[words] == split_original[words]:
                for _ in split_user_data[words]:
                    self.char_count += 1
        self.words_per_min = math.ceil(self.char_count / 5)
        with open('score.py', mode='r+') as file:
            if self.score < str(self.words_per_min):
                file.write(str(self.words_per_min))
        return (self.char_count + len(split_user_data)), self.words_per_min, original_char_count

    def score_update(self):
        """
        Opens in read only mode the scoring file and reads the data
        :return: Returns a string value
        """
        with open('score.py') as file:
            current_score = file.readline()
            return current_score
