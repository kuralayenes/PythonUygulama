print("ax**2 + bx + c denkleminin ikinci dereceden köklerini hesaplayan program ?")

a = int(input("a sayisini giriniz: "))
b = int(input("b sayisini giriniz: "))
c = int(input("c sayisini giriniz: "))

delta = b**2 -4*a*c

if(delta>0):
    x1=(-b-(delta)**(1/2))/(2-a)
    x2=(-b+(delta)**(1/2))/(2-a)
    print(x1,x2)
elif(delta==0):
    x1=-b/(2*a)
    print(x1)
else:
    print("sanal kök yok")