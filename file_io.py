f= open("file.txt")

data = f.read()
print(data)
f.close()
st = "Hello i am going to write in this file now"

f= open("myfile.txt", "w")

f.write(st)

f.close()