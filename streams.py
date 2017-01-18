##def processor(reader, converter, writer):
##    while True:
##        data = reader.read()
##        if not data: break
##        data = converter(data)
##        writer.write(data)
##def converter(data):
##    return data.upper()

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)
    def converter(self, data):
        assert False, "converter must be defined!"

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()
    
class HTMLize:
    def write(self, data):
        print('<PRE>{}</PRE>'.format(data.rstrip()))

if __name__ == '__main__':
    import sys
##    reader = open('mytxt.txt', 'w')
##    reader.write('jklasfh asfjkdfhasd asj\nlaskjdf safjasdkfjlk\na sfha sjfj skdjf\n')
##    reader.close()
##    reader = open('mytxt.txt')
##    writer = sys.stdout
##    processor(reader, converter, writer)
    p = Uppercase(open('mytxt.txt'), sys.stdout)
    p.process()
    p1 = Uppercase(open('mytxt.txt'), HTMLize())
    p1.process()
    
