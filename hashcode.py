import math

def min_signup_library(signup_time_list):
    min_s_l = math.inf
    min_time = math.inf
    for i in range(len(signup_time_list)):
        if signup_time_list[i] < min_time:
            min_time = signup_time_list[i]
            min_s_l = i
    return min_s_l


f = open("d_tough_choices.txt", "r")
all_input = f.readlines()

for i in range(len(all_input)):
    all_input[i] = list(map(int, all_input[i][:-1].split()))

maxdays = all_input[0][2]
bookscores = all_input[1]

signup_time = []
shipping_limit = []
booksavail = []

for library_no in range(all_input[0][1]):
    #input for 1st lib starts at line 2, 2nd starts at line 4, etc
    signup_time.append(all_input[2*(library_no+1)][1])
    shipping_limit.append(all_input[2*(library_no+1)][2])
    booksavail.append(all_input[2*(library_no+1)+1])

'''
print(signup_time)
print(shipping_limit)
print(booksavail)'''

time = 0
countselected = 0
output = []
seenbooks = []

while min_signup_library(signup_time) != math.inf:
    library = min_signup_library(signup_time)
    booksavail[library] = [booknumber for booknumber in booksavail[library] if booknumber not in seenbooks]
    #print(library)
    temp = time
    time += signup_time[library]
    timeinqueue = 0
    if len(booksavail[library]) != 0:
        if time + math.ceil(len(booksavail[library])/shipping_limit[library]) <= maxdays:
            timeinqueue += math.ceil(len(booksavail[library])/shipping_limit[library])
            print(library, "in")
            countselected += 1
            output.append([library,len(booksavail[library])])
            output.append(booksavail[library])
            seenbooks.extend(booksavail[library])
        else:
            print(library,"not in")
            #print(time, math.ceil(len(booksavail[library])/shipping_limit[library]))
            time += timeinqueue
            if time >= maxdays:
                time = temp
            else:
                countselected += 1
                no_ofbooks_choose = (maxdays - time)*shipping_limit[library]
                output.append([library, no_ofbooks_choose])
                output.append(booksavail[library][:no_ofbooks_choose])
                seenbooks.extend(booksavail[library][:no_ofbooks_choose])

    signup_time[min_signup_library(signup_time)] = math.inf
#print(output)

for i in range(len(output)):
    output[i] = " ".join(str(j) for j in output[i])

f = open("output.txt", "w")
f.writelines(str(countselected))
f.writelines("\n")
f.writelines("\n".join(output))
f.close()
