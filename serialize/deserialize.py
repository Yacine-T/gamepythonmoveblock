import pickle

input = open("level1.dat","rb")

data2 = pickle.load(input)
print(data2)
input.close()
for i in data2 :
    print(i)
