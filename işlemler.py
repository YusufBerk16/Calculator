print("""

Hesap Makinası

Toplama İşlemi Yapmak İçin 1 'e Basın.
Çıkarma İşlemi Yapmak İçin 2 'e Basın.
Çarpma İşlemi Yapmak İçin 3 'e Basın..
Bölme İşlemi Yapmak İçin 4 'e Basın.
Modunu Almak için 5 'e Basın.
Üssünü Almak için 6'ya Basın.

""")

islem = str(input("İşlem seçiniz: "))

if islem == "1":
    sayi1 = int(input("1. Sayıyı giriniz: "))
    sayi2 = int(input("2. Sayıyı giriniz: "))
    print("Sonuç:", sayi1 + sayi2)
    
elif islem == "2":
    sayi1 = int(input("1. Sayıyı giriniz: "))
    sayi2 = int(input("2. Sayıyı giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
    
elif islem == "3":
    sayi1 = int(input("1. Sayıyı giriniz: "))
    sayi2 = int(input("2. Sayıyı giriniz: "))
    print("Sonuç:", sayi1 * sayi2)
    
elif islem == "4":
    sayi1 = int(input("1. Sayıyı giriniz: "))
    sayi2 = int(input("2. Sayıyı giriniz: "))
    print("Sonuç:", sayi1 / sayi2)
    
elif islem == "5":
    sayi1=int(input("Bir Sayi Giriniz : "))
    sayi2=int(input("Mod için Bir sayı giriniz: "))
    print("Sonuç: ", sayi1 % sayi2)
    
elif islem == "6":
    sayi1=int(input("Üssünü bulmak istediğiniz sayıyı giriniz: "))
    print("Sonuç: ", sayi1 ** 2 )
    
else:
    print("geçersiz işlem girdiniz...")