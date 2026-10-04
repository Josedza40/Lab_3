"""
Program Name: Word Count
Author: Jose Daniel Zambrano
Purpose: Allow the user to select a text file and display the frequency
         of each word in alphabetical order.
Starter Code: Code showed by the instructor during video presentation of the class.
Date: 10/03/2026
"""

from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        translator = str.maketrans("","",string.punctuation)
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError(f"File '{self.__filepath}' does not exist.")
            
            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translator)
                    words = line.split()
                    for word in words:
                        self.__frequencies[word] = self.__frequencies.get(word,0) + 1    
            return True    
            
        except FileNotFoundError as e:
            print(e)
            return False


    def print_report(self):
        words = sorted(self.__frequencies.keys())

        for word in words:
            print(f"{word:<15} :: {self.__frequencies[word]}")