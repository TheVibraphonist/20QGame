class Simpledb:
    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return '<' + self.__class__.__name__ + '   file= ' + self.filename + '>'

    def insert(self, filename, key, value):
        f = open(filename, 'a')
        f.write(key + '|  @  |' + value + '\n')
        f.close()

    def select_one(self, filename, key):
        f = open(filename, 'r')
        for row in f:
            (k, v) = row.split('|  @  |', 1)
            if k == key:
                return v[:-1]
        f.close()

    def delete(self, filename, key):
        f = open(filename, 'r')
        rslt = open('rslt.txt', 'w')
        for (row) in f:
            (k, v) = row.split('|  @  |', 1)
            if k != key:
                rslt.write(row)
        f.close()
        rslt.close()
        import os
        os.replace('rslt.txt', filename)

    def update(self, filename, key, value):
        f = open(filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('|  @  |', 1)
            if k == key:
                result.write(key + '|  @  |' + value + '\n')
            else:
                result.write(row)
        f.close()
        result.close()
        import os
        os.replace('result.txt', filename)