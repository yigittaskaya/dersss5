kullanici=""
parola=""
while kullanici!="admin" or parola!="123456":
    kullanici=input("kullanıcı adınız: ").lower()
    parola=input("parolanız:")
    if kullanici=="admin"and parola=="123456":
        print("hoşgeldin")
print("sisteme giriş yapıldı")