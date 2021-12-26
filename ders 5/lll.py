def kontroller(kullanici,parola):
    if kullanici=="admin" and parola=="123456":
        return  True
    else:
        return False
while True:
    kullanici_adi=input("kullanıcı adınız:")
    parola=input("parolanız:")
    if kontroller(kullanici_adi,parola)==True:
        print("giriş yapıldı")
        break
    else:
        print("başarısız giriş")