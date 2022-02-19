def add_2_num(n1, n2):
    return n1+n2

def subtract_2_num(n1, n2):
    if n1 > n2:
        return n1-n2
    else:
        return n2-n1

def multiple_2_num(n1,n2):
    return n1*n2

def divide_2_num(n1,n2):
    if n2 != 0:
        return n1/n2
    else:
        return -1

if __name__ == "__main__":
    print(add_2_num(2,3))
    print(subtract_2_num(2,3))
    print(multiple_2_num(2,3))
    print(divide_2_num(2,3))
