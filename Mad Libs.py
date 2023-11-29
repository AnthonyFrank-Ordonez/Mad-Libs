import json
import time
from question_processor import *


def get_story(choice: str, templates: dict):
    """
    Get the storyboard based on the ask input from the user

    :param choice: The user choice of story on the list of choices
    :param templates: Dictionary containing the list of storyboards
    :return: str or None
    """
    if choice in templates.keys():
        return templates.get(choice)

    else:
        return  # return None type or the story is not on the templates


def create_storyboard(templates: dict):
    """
    Create the mad lab story with the inputted noun and verbs

    :param templates: Dictionary that contains the story templates
    :return: None
    """
    # initialize an empty list and ask the user for storyboard input from the choices
    user_inputs: dict = {}

    # walrus operator to continually get user input from the user after creating the storyboard
    while (story_choice := input(initial_question)) not in ('exit', "Exit"):

        # if statement to check if  the user choice of story is on the list
        if story := get_story(story_choice, templates):

            # iterate the questions that will be asked based on the user story choice
            for keyword, questions in check_choice(story_choice).items():

                # ask the user base on the question on the dictionary values that is return and add it to the
                # user_inputs dictionary with the keys of keyword and the value with the user input from the question
                question: str = input(questions)
                user_inputs[keyword] = question

                # check if there are digits or white space inputted of the user
                if question.isdigit() or question in (' ', ""):
                    print("-" * 80)
                    print('Invalid input! there are errors upon checking, please try again')
                    print('-' * 80)
                    create_storyboard(templates)

            else:
                # Create the storyboard using format method
                output = story.format(**user_inputs)
                print()  # add space
                print('-' * 45, 'YOUR STORY', '-' * 45)
                print(output)
                print('-' * 101, '\n')

        else:
            # if the user input is not on the valid choice
            print('KEY ERROR: INVALID CHOICE!\n')

    else:
        print('Exiting the system please wait...')
        time.sleep(3)


def main():
    """Main Function"""

    # Extract the story templates in the json file
    with open('story_template.json', 'r') as temp_file:
        templates = json.load(temp_file)

        story_boards = templates.get('templates')
        create_storyboard(story_boards)


if __name__ == '__main__':
    initial_question = ("Story Choice:\n\n1: Basic Story: A Great Time \n2: Three Wishes \n\n"
                        "What story do you want to create from the choices: ")
    main()