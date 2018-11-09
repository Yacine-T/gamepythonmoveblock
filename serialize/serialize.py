import pickle

data1 =  [ [1,  1,  1,  1,  1,  1,  1,  1],
           [1,  100, 1,  50,  0, 10,  0,  1],
           [1,  0,  1,  0,  0,  0,  0,  1],
           [1,  0,  1,  0,  0,  0,  0,  1],
           [1,  0,  1,  0,  0,  0,  0,  1],
           [1,  0,  1,  1,  1,  1,  0,  1],
           [1,  0,  0,  0,  0,  0,  0,  1],
           [1,  1,  1,  1,  1,  1,  1,  1] ]
output = open("level1.dat","wb")
print(data1)
print("----------")
pickle.dump(data1,output)

output.close()

input = open("level1.dat","rb")

data2 = pickle.load(input)
print(data2)
input.close()
