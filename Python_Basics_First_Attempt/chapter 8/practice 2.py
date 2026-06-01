# open a file called report.txt in write mode
file= open("chapter 8/report.txt", "w")
file.write("python kafi easy h easy programing language i am hard working")
file.close()
#  append mode yani "a" use kry gay mtlb koi cheez over write na ho 
file= open("chapter 8/report.txt", "a")
file.write("i am sehar Ali.i am learning pyrhon")
file.close()
# "x" mode use kry gay koi nai file bny gi agr file allready exit krtu hoi us name ki tw error mil jie ga
file = open("chapter 8/sehar.txt", "w")
file.write("i am sehar Ali.i am learning python.\nIt vert easy it unique.\n i am learning pyhton file handling toppic")
file.close()