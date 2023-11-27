
def check_choice(choice: str):

    if choice == "1":
        return {
            'noun': 'Enter a Noun: ',
            'verb': 'Enter a Verb: ',
            'noun_2': 'Enter your 2nd noun: ',
            'verb_2': 'Enter your 2nd verb: '

        }

    elif choice == '2':
        return {
            'noun': 'Enter a Noun: ',
            'noun_2': 'Enter your 2nd noun: ',
            'adjective': 'Enter your adjective: '
        }