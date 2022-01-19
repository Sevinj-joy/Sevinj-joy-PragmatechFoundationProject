# task1- Üç müxtəlif a, b, c ədədləri verilmişdir. Onlardan qiymətcə orta olanı tapın.
# def orta_eded(a, b, c):
#     netice = float((a+b+c) % 3)
#     print("Daxil etdiyiniz 3 ededin ededi ortasi :",netice)
# a = int(input("Birinci ededi daxil edin .."))
# b = int(input("Ikinci ededi daxil edin .."))
# c = int(input("Ikinci ededi daxil edin .."))
# orta_eded(a ,b ,c )

# task2- Proqramlaşdırma olimpiadasının ikinci turu bitdikdən sonra olimpiada iştirakçıları
# bu hadisəni qeyd etmək qərarına gəldilər. Bu məqsədlə düzbucaqlı formada bir böyük tort sifarış verildi.
# Bu zaman iştirakçıların ətrafına toplaşdıqları masa dairəvi idi. Təbii ki, onlarda sual yarandı: 
# Düzbucaqlı tort masadan qırağa çıxmamaq şərti ilə masaya yerləşəcəkdirmi?
#  Tortun ölçülərini və masanın radiusunu bilərək, bu sualı cavablandırmalısınız.
# Üç natural ədəd: masanın r (1 ≤ r ≤ 1000) radiusu, tortun w eni və l uzunluğu (1 ≤ w ≤ l ≤ 1000).
# Tort masaya yerləşirsə YES, əkshalda NO çap edin.
# def tort_sahesi(w, l ,r):
#     if w >= 1 and w <= 1000 and w <=l:
#         sahe = w * l
#         print("Sahesi budur:" , sahe)
#     if sahe <= r and r <= 1000 and r >= 1:
#         print("Yes tort masaya yerlesir")
        
#     else:
#         print("NO Tort masaya yerlesmir")

# w = input("Tortun enini daxil edin:")
# l = input("Tortun uzunlugunu daxil edin:")
# r = input("Masanin radiusunu daxil edin:")
# tort_sahesi(int(w), int(l) ,int(r))

# task3 - Heyvanxanada n qəfəs bir sırada düzülmüşdür. Heyvanxanada digər sakinlərlə yanaşı, 
# iki əntər meymun - Slava və Yura da yaşayırdılar. Slava və Yura həmişə yaxşı dost olmuşdular və
# qonşu qəfəslərdə əyləşirdilər. Lakin indi onlar küsülü idilər və bir-birini görmək istəmirdilər.
# Heyvanlara qulluq edən baxıcı də onları arzularına uyğun olaraq köçürmək istəyirdi,
# lakin problem yaranmışdı. Slava və Yura çox savadlı meymunlar idilər (onların hər biri cəmi 8 sinif
# qurtarmışdı!). Onlar bilmək istəyirdilər ki, onların qəfəslərinin qonşu olmaması üçün neçə köçürmə üsulu var 
# və əlbəttə onların xanaları müxtəlif olmalıdır. Belə hesab etmək olar ki, heyvanxananın 
# digər sakinləri hara lazımdırsa köçürülməyə hazırdırlar, yəni bütün n hücrə əlyetərlidir.
# Heyvanlara qulluq edən əvvəlcə özü bunu hesablamaq istədi, haradasa begemotların ərazisində hesabı itirdi.
#  Tamamilə aydındır ki, sizin köməyiniz olmadan o bunun öhdəsindən gələ bilməyəcək!
# Giriş verilənlərin birinci sətrində heyvanxanadakı qəfəslərin sayı olan n (2 ≤ n ≤ 100) ədədi yerləşir.



# task4 -m natural ədədi n ədədinin o zaman bərabər böləni adlanır ki, n-nin m-ə bölünməsindən alınan
# tam və qalıq bərabər olsun. Verilmiş n natural ədədinə görə onun bərabər bölənlərinin sayını tapın.
# Müsbət n tam ədədi (1 ≤ n ≤ 106).
m = input("Eded daxil edin")
n = input("Eded daxil edin")