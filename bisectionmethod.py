import math
def f(x):
    # return math.cos(x)-math.sin(x) question1 x[0,1]
    return math.cos(x) - x * math.exp(x)
    #return x**4-x-10 #x[1.5,2] #question2

x_l=0
x_r=1
x=(x_l+x_r)/2
#finding root nearest to 0.001 accuracy
while (abs(f(x))>0.001):

    print(x_l,x_r)
    x=(x_l+x_r)/2
    if f(x_l)<0 and f(x)>0:
        x_r=x

    elif f(x_r)>0 and f(x)<0:
        x_l=x

    elif (x_l)>0 and f(x)<0:
        x_r=x

    elif f(x_r)<0 and f(x)>0:
        x_l=x



print("root of the equation:",x)