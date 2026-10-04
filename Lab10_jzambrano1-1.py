"""
Program Name: Word Count
Author: Jose Daniel Zambrano
Purpose: Allow the user to select a text file and display the frequency
         of each word in alphabetical order.
Starter Code: Based on code examples demonstrated by the instructor during the class video.
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

def main():
    base_path = Path(__file__).parent

    files = {
        "1": base_path / "monte_cristo.txt",
        "2": base_path / "princess_mars.txt",
        "3": base_path / "Tarzan.txt",
        "4": base_path / "treasure_island.txt"
    }
    
    menu = """
--- Word Analyzer ---
Please select a file to analyze:

1. Monte Cristo
2. Princess of Mars
3. Tarzan
4. Treasure Island
5. Exit
"""
    while True:
        print(menu)
        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting the program.")
            break

        if choice not in files:
            print("Invalid choice. Please select from 1-5.")
            continue

        print(f"\nProcessing '{files[choice].name}'...")

        analyzer = WordAnalyzer(files[choice])
        if analyzer.process_file():
            analyzer.print_report()
        input("\nPress Enter to continue...")

    if __name__ == "__main__":
        main()    