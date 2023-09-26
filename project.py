from fuzzywuzzy import fuzz
from datetime import datetime
import csv
from datetime import datetime


filepath = "dict.csv"  #! Database for questions


def main():
    print(
        "Hi, i'm StarStreamBot Python Library! I'm usually integrated with a DiscordServer, but you can use me standalone here:"
    )
    while True:
        message = input("What do you wan't to look up?: ").lower()

        if message == "":
            print("No question was made, try again?")
        else:
            break

    answer = fuzz_ratio(message)
    if len(answer) == 3:
        keyword, desc, syntax_other = answer
        print(
            f"Keyword: {keyword}\nDescription:\n  {desc}\nSyntax/Other information:\n  {syntax_other}"
        )
    else:
        print(f"I can't find anything related to: {message}")
        write_file(message)


def read_file(filepath):
    answers = {}
    with open(filepath, "r", encoding="utf-8") as file:
        filereader = csv.reader(file, delimiter=";")
        next(filereader, None)
        line_count = 0
        for row in filereader:
            line_count += 1

            if len(row) >= 3:
                question, answer, syntax = row[0], row[1], row[2]

                if syntax == "":
                    syntax = f"Sorry, no more info about {question} yet!"

                answers[question] = f"{answer}", f"{syntax}"
            else:
                print(f"Ignorerar raden: {line_count}\nFel på databasformat!")

    return answers


def write_file(message):
    try:
        with open("requests.csv", "a", encoding="utf-8") as file:
            add_request = f"{message};1;{datetime.now()}\n"
            file.write(add_request)
            print(f"'{message}' is added to requests for learning purposes")
            return True
    except Exception as e:
        print(f"Fel vid skrivning till fil: {e}")
        return False


def fuzz_ratio(message):
    answers = read_file(filepath)

    best_match = ("", "")
    max_match = 0

    for question, (answer, syntax_use) in answers.items():
        pattern_question = fuzz.token_set_ratio(message, question, syntax_use)
        match_pattern = fuzz.token_set_ratio(message, answer, syntax_use)

        if pattern_question > max_match:
            best_match = (question, answer, syntax_use)
            max_match = pattern_question

        if match_pattern > max_match:
            best_match = (question, answer, syntax_use)
            max_match = match_pattern

    if max_match > 50:  #! Accuracy, default is 50
        return best_match
    else:
        return question


def requests(message):
    add_request = "fuzz_ratio(message)"


if __name__ == "__main__":
    main()
