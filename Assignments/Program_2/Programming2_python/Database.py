class Database:

    data = []
    def __init__(self, k, nonzero):

         if nonzero:
            for i in range(k):
                self.data.append(i+1)
         else:
            for i in range(k):
                self.data.append(0)

    def Read(self, k):
        return self.data[k]

    def Write(self, k, w):
        self.data[k] = w
        return 0

    def Print(self):
        print(self.data)
        return 0
