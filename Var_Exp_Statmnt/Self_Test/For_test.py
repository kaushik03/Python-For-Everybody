
#3
i = 10
a = []
while i > 1:
    mul = 14 * i
    a.append(mul)
    i = i-1

print(a)

#2
i = 4
while i <= 4:
    print("*" *i)
    i = i+1

#3
a = []
b = []
for i in range(1,101):
    if i%2 == 0:
        a.append(i)
    else:
        b.append(i)
        i = i+1
print(a)
print(b)
#4
a = [1,2.0,"Kaushik"]
inte = []
fl = []
st = []
for i in a:
    if type(i) == int:
        inte.append(i)
    elif type(i) == float:
        fl.append(i)
    elif type(i) == str:
        st.append(i)
print(inte)
print(fl)
print(st)