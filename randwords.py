def randwords(numOfWords, minLetters, maxLetters):
    from random import randint
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    wordList = []
    for i in range(numOfWords):
        word = ''
        for j in range(randint(minLetters, maxLetters)):
            word += allLetters[randint(0,25)]
        wordList.append(word)
    return wordList

##print(randwords(100,2,8))
            
