# a = int(input())
# b = int(input())
# c = int(input())
# if a > b :
#     a,b=b,a
# if a > c:
#     a,c=c,a
# if b > c :
#     b,c=c,b
#     print(a,"<",b,"<",c)


# sposob 2

a = float(input())
b = float(input())
if a<b:
    b,a=a,b
c = float(input())
if b<c:
    c,b=b,c
    if a<b:
        b,a=a,b
print(a, "-", b,"-",c)