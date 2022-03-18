import re

string = "1,2,3,5-11,10"
pattern = r"\d[0-9\-]*"
eps = []

if re.search('[a-zA-Z]', string) is None:
    x = re.findall(pattern, string)
    for i in x:
        num = i.split("-")
        if len(num) == 2:
            for j in range(int(num[0]), int(int(num[1])) + 1):
                eps.append(j)
        else:
            eps.append(int(num[0]))
    eps = list(dict.fromkeys(eps))  # removing dupplicates
    print(eps)
else:
    print("Invalid")

# for i in eps:
#     if i > len(videoUrls):
#         print("the episodes you specified is too much lol")
#         break


# the value you put for episode is not accepatble either leave it blank to download
# all episodes or specify the ones you want.For example:

# 1-5 will downlaod episodes 1 to 5
# 3,7,9 will download episodes 3,7 and 9
# you can also combine them example 1,2,3,4-7,10
# this will download 1,2,3,4 to 7 and 10

