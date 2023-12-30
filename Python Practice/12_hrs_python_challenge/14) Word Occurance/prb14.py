def word_occurrence(sentence, word):
    return sentence.lower().split().count(word.lower())


print(word_occurrence("Hi Im Vamsi Hi", "hi"))
