from sys import argv
def aver():
    a = argv[1]
    b = argv[2]
    print(a.capitalize(), b.capitalize() )
    print(a.upper(),b.upper())
    print(a[0],a[-1],b[0],b[-1])
    print(len(a),len(b))
    print(a+b)
aver()
