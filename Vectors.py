class Vector:
    def __init__(self,key):
        self.value =key
        self.nextValue = None

    def insertValue(self,key):
        if self.value is None:
            self.value = key
        else:
            self.nextValue = Vector(key)
        return self

    def inorder(self,test):
        if test:
            print(test.value)
            test.inorder(test.nextValue)
        else:
            print('done')


testing = Vector(1)

testing.insertValue(12)
testing.nextValue.insertValue(122)
testing.nextValue.nextValue.insertValue(1500)
testing.inorder(testing)