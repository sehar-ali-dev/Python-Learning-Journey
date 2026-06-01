# creat class student that takes 3 marks and has a method average().
class students():

    def __init__(self, name, listofmarks):
        self.name= name
        self.listofmarks= listofmarks
# (self) ki jgha '@staticmethod' ye likh skty h function yani method k upr ye likh dy tw kam ho jie ga jues k 
    #@staticmethod
    def average(self):
        sum=0
        for eachvalue in self.listofmarks:
            sum= sum+eachvalue
        average= sum/3
        print("average  is:", average)


students1= students("sehar", [23, 32, 24])
students1.average()

