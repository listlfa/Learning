from itertools import count


x=object()
y=object()

x_list=[x]*10
y_list=[y]*10
big_list=x_list+y_list

print("x_list has %i objects" % len(x_list))
print("y_list has %i objects" % len(y_list))
print("b_list has %i objects" % len(big_list))

if x_list.count(x)==10 and y_list.count(y)==10:
    print("almost there")
if big_list.count(x)==10 and big_list.count(y)==10:
    print("greeat")

#print(x)
#print(y)
#print(big_list)

