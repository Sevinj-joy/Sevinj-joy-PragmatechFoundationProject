# sual -Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.
# task1
# a = int(input("Dordbucaqlinin enini daxil edin:"))
# b = int(input("Dordbucaqlinin uzunlugunu daxil edin:"))
# # perimetr = 2 * (a+b)
# sahe_kvadrat = a ** 2
# sahe_duzbucaqli = a * b
# if a == b:
#     print("Bu dordbucaqli kvadratdir ve sahesi:" , sahe_kvadrat)
# else:
#     print("Bu dordbucaqli kvadrat deyil ve sahesi:",sahe_duzbucaqli )


# sual -Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.
#task2
# numbers = (22 , -18 , 0, 18)
# maximum = max(numbers)
# print("Ededlerden en boyuyu:", maximum)

# sual -Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.
# task3
# meyveler = ["alma","armud ","banan","ananas","kivi","ciyelek"]
# print ("Bu meyvelerden hansi meyveni isteyirsiniz?" , meyveler)
# user_choosen = input("Meyveni daxil edin:")
# # user_choosen = meyveler.index(input("Meyveni daxil edin:"))
# qiymet = ["1kg = 3 AZN","1kg = 5 AZN", "1kg = 2 AZN","1kg = 4 AZN","1kg = 7 AZN","1kg = 14 AZN"]
# if user_choosen == "alma":
#     print(qiymet[0])
# elif user_choosen == "armud":
#     print(qiymet[1])
# elif user_choosen == "banan":
#     print(qiymet[2])
# elif user_choosen == "ananas":
#     print(qiymet[3])
# elif user_choosen == "kivi":
#     print(qiymet[4])
# elif user_choosen == "ciyelek":
#     print(qiymet[5])
# else:
#     print("Bele meyve yoxdur")

# task4
# name = input("Adinizi daxil edin:")
# mail = "@gmail.com"
# # age =input("Yasinizi daxil edin:")
# if len(name) > 3 and len(name) < 11:
#     surname = input("Soyadinizi daxil edin:")
#     if len(surname) > 5 and len(surname) < 15:
#         year = input("Doguldugunuz ili daxil edin:")
#         if len(year) == 4:
#              email = input("Mail unvaninizi daxil edin:")
#              bolgu =mail.split("@")
#             if len(email) > 10 and len(email) < 22 and email in mail and bolgu[1] == "gmail.com":
#                  password = input("Parolu daxil edin")
#                 if len(password) > 6 and len(password)< 13:
#                     tesdiq = input('Parolu tesdiqle: ')
#                     if password == tesdiq :
#                         print('Qeydiyyat tamamlandi!')
#                         yoxla = input('Qeydiyyat detallarini gormek isteyirsiz? ')
#                         if yoxla == 'he' :
#                             print(f'Ad: {name} Soyad: {surname} Yas: {year} Email: {email} Parol: {password}')
#                         elif yoxla == 'yox':
#                             print('Murad Əliyev, Uğurlar!')


# else:
#     print("Ad normalara uygun deyil")
