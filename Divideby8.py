
def findAllPerm(x):
    if len(x) == 1:
        return [x];
    
    elif (len(x) == 2):
        return [x, x[-1 :: -1]];
    
    elif (len(x) == 3):
        a, b, c = x[0], x[1], x[2];
        return [x, x[-1 :: -1], a + c + b, b + c + a, b + a + c, c + a + b];
        
    else:
        raise Exception("len(" + x + ") > 3");

eight_div = {}
for i in range(104, 1000, 8):
    i_count = eight_div[i] = {};

    for c in str(i):
        if int(c) in i_count:
            i_count[int(c)] += 1;
        else:
            i_count[int(c)] = 1;



def isDivisibleBy8(s):
    if len(s) < 3:
        return (int(s)%8 == 0) or (int(s[-1 :: -1])%8 == 0);


    s_count = 10*[0];

    for c in s:
        s_count[int(c)] += 1;

    for x in eight_div:
        x_count = eight_div[x];

        for digit in x_count:
            if x_count[digit] > s_count[digit]:
                break;
        return True;
    return False;
        



def isEven(c):
    return int(c)%2 == 0;


for i in range(0, 1000, 8):
    print("no. is", i)
    print("isDivisibleBy8 =", isDivisibleBy8(str(i)));