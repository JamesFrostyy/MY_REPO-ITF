# -*- coding: utf-8 -*-
"""03.05.2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i8EqIAi_r1-USDe7kIjR7c4spa4plnRK
"""

a = input("değer gir: ")
print("\n çıktı =", a)

a = input("değer gir: \n ")
print(" çıktı =", a)

string.format() metoduyla ilgili derste 4 farklı kullanım şekli göstermiştim. 
Bunlardan birinde değerleri format()'ın içinde değişkene atayarak tanımlamıştık. 
işte o keyword argümana örnektir. Noluyordu orda? Değer format'ın içindeki pozisyonuna (indeksine) göre değil de 
değişken ismine göre süslü parantezlere giriyordu.

Studytonight has 12 characters.

Python is the most widely sought after programming language.

Studytonight has 12 characters in it.

Konumsal argüman bir değerin atanmadan iki taraftada aynı sırayla vermesine denir.Örneğin
my_str = "{} has {} characters." # Formatter with multiple placeholder
print(my_str.format("Studytonight", 12))
ya da numara ile belirtebilirsin
print("{2} is the most widely {3} after {1} {0}".format("language","programming", "Python", "sought"))
0 = language gibi
...
Keyword argument ise değeri assignment(=) ile atanmışsındır.Nereye koyarsan koy o zaten değerini biliyordur. Örneğin:
print("{st}".format(st ="Studytonight"))
print("{st} has {number_of_char} characters in it.".format(st ="Studytonight", number_of_char = 12))

hocam string bir ifade de harf ya da herhangi bir özel karakter olursa(yani sayıdan başka) onu çeviremiyoruz. örnek int("12a")

String haldeki bir float sayı int() ile tam sayıya çevrilemiyor.
Bunun için önce float sonra int çevrimi yapmalısınız.
Örnek: int(float(‘12.34’))

from math import pi
yaricap = 3  #yarıçapı 3 olan dairenin alanı
print ("Yarıçapı "+str(yaricap) + " olan dairenin Alanı :" + str(pi * yaricap**2))

import math 
r = int(input("r degerini giriniz"))
A = math.pi * math.pow(r,2)
print("Dairenin alanı = %.2f" %A)

import math

print("Dairenin alanini hesaplayan programa hos geldiniz.")
r = float(input("Bir yaricap degeri giriniz: "))

alan = str(math.pi*math.pow(r,2))

print(alan[:5])

import math
r = float(input("dairenin yarıçapını girin :"))
alan = math.pi * r * r
print("Dairenin alanı = %.2f" %alan)

#"kenar sayısı verilen bir çokgenin bir iç açısını bulalım."
n = int(input("kenar sayısı giriniz:"))
toplam = (n-2) * 180
print("toplam:", toplam)

polygon_sides = 5
interior_angle = (polygon_sides - 2) * 180 / polygon_sides
print("An interior angle of a pentagon  : ", int(interior_angle))

n = int(input("kenar sayısı giriniz:"))
toplam = (n-2) * 180 // n
print("toplam:", toplam)

a = int(input("a  : "))
b = int(input("b  : "))
c = int(input("c  : "))
delta = pow(b,2) - 4 * a *c
root1 = (-b - pow(delta,0.5)) / (2 * a)
root2 = (-b + pow(delta,0.5)) / (2 * a)
print("First root  : {}\nSecond root  : {}".format(root1,root2))

# kod yazarken ters slash'ı biz ne amaçla kullanıyoruz? Kodumuz uzamasın ve karmaşık gözükmesin diye değil mi. Yani ters slash ile; yazdığımız kodu o satırda kesip alt satırdan devam ettirebiliyoruz. Bu kod yazımı ile ilgili python'un bize sağladığı pratik bir kullanımdır.
# Ekrana çıktı aldıran ise print() fonksiyonudur ve içinde "\n" escape sequence' ı olmadan print() fonksiyonu hep tek satır çıktı verir.
# Örnek:
# print(3, 4, 5, 6, 7, 8)
# print(3, 4, 5, "\n", 6, 7, 8)  # alt satıra geçtiğinde virgülden kaynaklı 1 boşluk koymuş olduğuna dikkat et.
1. Start ve stop'tan herhangi biri pozitif veya negatif indeksle gösterilebilir, farketmez. Fakat ilerleme yönüne doğru start, stoptan önce olacak.  Bu biiir.
2. İlerleme yönü;
    pozitif stepte soldan :arrow_right: sağa doğru ,
    negatif stepte sağdan :arrow_left: sola doğrudur.

# Kodunuz n sayısını alsın ve n dahil n'e kadar olan tüm doğal sayıların karelerinin toplamını versin.
n = int(input('Enter please value:'))
result = (n*(n+1)*(2*n+1))//6
print("result", result)
