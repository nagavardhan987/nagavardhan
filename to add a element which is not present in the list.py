num=20
list=['1','2','3','4']
for i in list:
    if num not in list:
        list.append(num)
    else:
       continue
print(list)