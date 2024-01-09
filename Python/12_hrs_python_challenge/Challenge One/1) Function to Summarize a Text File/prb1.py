def summarize_text_file(filename):
    """  # My Solution without Optimisation and forgot to include the space value here
    with open(filename, 'r') as text_file:
    # No of Lines
        content = text_file.readlines()
        no_of_lines = len(content)

        # No of Words
        words = []
        for line in content:
            words += line.split()
        no_of_words = len(words)

        # No of Character's
        no_of_character = 0
        for word in words:
            i = 0
            while i < len(word):
                no_of_character += 1
                i += 1
    """

    with open(filename, 'r') as text_file:
        content = text_file.read()

        lines = content.split('\n')
        no_of_lines = len(lines)

        words = content.split()
        no_of_words = len(words)

        char = list(content.replace('\n', ''))
        no_of_character = len(char)

        print("No of lines: " + str(no_of_lines))
        print("No of words: " + str(no_of_words))
        print("No of characters: " + str(no_of_character))


name = str(input("Enter file name: "))
summarize_text_file(name)
