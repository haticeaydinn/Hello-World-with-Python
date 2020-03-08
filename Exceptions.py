# örneğin age değerine asd gibi bir string yazılırsa bu integer
# değere dönüştürülemez ve program "Invalid value..." mesajını yazar
# sıfıra bölünme hatası için de except bloğu eklenmiştir
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid value...")
except ZeroDivisionError:
    print("Age can not be zero... Zero division error...")
