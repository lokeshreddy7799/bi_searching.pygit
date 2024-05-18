class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

# Usage
my_iterator = MyIterator([1, 2, 3, 4, 5,6,7,8,])
for item in my_iterator:
    print(item)