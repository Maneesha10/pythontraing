no1 = int(input("Enter no1"))
no2= int(input ("Enter no2"))
if(no1 < no2):
    sum  = no1+no2
    print(sum)
elif(no1> 5):
    sub = no1-no2
    print(sub)
else:
    print("Hello")

#sets practice
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)


for d in Days:
  print(d)

Days.add("Sun")
print(Days)

Days.discard("Mon")
print(Days)

#tuples
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0]);
print ("tup2[1:5]: ", tup2[1:5]);

tup3 = tup1 + tup2;
print(tup3);
