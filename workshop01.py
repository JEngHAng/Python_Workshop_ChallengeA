def inputdata():
    #word = str(input("Input TexT only : ").split(","))
    input0 = str(input("Input TexT only : "))
    list0 = input0.split()
    print (list0)
    x = list0.count(list0[])
    print (f"{list0} = {x}")
    return x , list0 , input0

inputdata()