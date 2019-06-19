file = open("human18S.txt").read() # you need to run this with the human gene file and then with the bacteria gene file
output = open("human18S.html", 'w') # after writing the human file you'll run it again with the bacteria file and then if you open the html files you'll be able to have a pretty good comparison between the two

count = {}

# using this for loop to get all the different combinations of RNA bases
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        count[i+j] = 0

# Cleaning up the line breaks the file has
file = file.replace('\n', '')

# counting the number of times each pair appears in the list and adding 1 to its value in the dictionary
for i in range(len(file)-1):
    try:
        count[file[i] + file[i+1]] += 1
    except KeyError:
        print('Key not found in dic.')  # not sure why yet but getting some key error, file still needs formatting prob
        continue

# print(count)

z = 1
print(count)
for i in count:
    density = count[i]/max(count.values()) # writing a html file with squares colored based on the number of times each pair appears
    output.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px;"
                 "float:left; background-color:rgba(0, 0, 0, "+str(density)+"')>"+i+"</div>")

    if z % 4 == 0: # making it 4x4
        output.write("<div style='clear:both'></div>")
    z += 1

output.close()
