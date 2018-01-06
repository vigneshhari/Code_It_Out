import random

file1 = open("1" , "r+")
file1.write("100\n")
for i in range(100):
    file1.write(str(random.randint(900, 950)) + " ") 
file1.close()


file2 = open("2" , "r+")
file2.write("1000\n")
for i in range(1000):
    file2.write(str(random.randint(500, 715)) + " ") 
file2.close()


file3 = open("3" , "r+")
file3.write("1000\n")
for i in range(1000):
    file3.write(str(random.randint(3300, 3500)) + " ") 
file3.close()


file4 = open("4" , "r+")
file4.write("10000\n")
for i in range(10000):
    file4.write(str(random.randint(7000, 8000)) + " ") 
file4.close()


file5 = open("5" , "r+")
file5.write("10000\n")
for i in range(10000):
    file5.write(str(random.randint(154000, 155000)) + " ") 
file5.close()
