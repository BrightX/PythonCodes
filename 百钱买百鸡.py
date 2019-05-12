for x in range(1,20):
    for y in range(1,34):
        for z in range(1,100):
            if x+y+z==100 and 5*x+3*y+z/3==100 and z%3==0:
                print("公鸡{}只，母鸡{}只，小鸡{}只".format(x,y,z))
                break
# 暴力求解
