
import random
import string

def sifre_olusturucu(uzunluk,seviye,output=[]):
    chars = string.ascii_letters
    if seviye > 1 :
        chars = "{}{}".format(chars,string.digits)
    if seviye > 2 :
        chars = "{}{}".format(chars,string.punctuation)

    for i in range(uzunluk):
        output.append(random.choice(chars))

    return "".join(output)
print(("-" * 30)+ "\nŞifre Oluşturuluyor\n" +("-" * 30))

pass_uzunluk = int(input("Uzunluk giriniz : "))
pass_seviye = int(input("Seviye belirtiniz : "))

password = sifre_olusturucu(pass_uzunluk,pass_seviye)

print( "Şifren : {}".format(password))
