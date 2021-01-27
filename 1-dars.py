def nam1():
    num_one=5
    num_two=4
    sum=num_one+num_two
    return sum

nam1()
f=open('num1.txt','w')
f.write(str(nam1()))