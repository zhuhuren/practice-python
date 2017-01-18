#!mymod.py
"""
lesson learned: when using input(), the input typed in shouldn't be quoted.
for example, if the file name is article.txt, it shouldn't be typed as 'article.txt'
"""

def countLines(name):
    try:
        with open(name) as file:
            return len(file.readlines())
    except:
        print(name, ' is not opened.')

def countChars(name):
    try:
        with open(name) as file:
            return len(file.read())
    except:
        print(name, ' is not opened.')

def test(name):
    print('There are {} lines in {}'.format(countLines(name), name))
    print('There are {} characters in {}'.format(countChars(name), name))

if __name__ == '__main__':
    name = input('Enter a file name: ')
    test(name)

# fo = open('filename.ext')
# fo.read() # reads the whole file
# fo.seek(0,0) or fo.seek(0) # rewind the file to offset 0, the beginning
# fo.seek(a, b), a is the offset where it rewinds to, b has 3 options, 0 - absolute offset, 1 - relative to last offset, 2 - from the end
# when b = 1 or 2, a can only be 0
