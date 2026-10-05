# Hisob-kitob qoidalari

Bu qoidalar prototipda ishlaydi va testdan o‘tgan. Server versiyasida ham aynan shular saqlanishi kerak.

## Pul
- Barcha summalar butun so‘mda saqlanadi, float ishlatilmaydi. Server versiyasida `NUMERIC` ishlatiladi.
- Dollarda kirim bo‘lsa, o‘sha kundagi kurs bilan so‘mga o‘giriladi. Kurs va asl summa ham saqlanadi. Keyin kurs o‘zgarsa, eski kirim o‘zgarmaydi.

## Tannarx
- **Telefon va planshet:** har bir IMEI o‘z tannarxiga ega. Tannarx = xarid narxi + qo‘shimcha kirim xarajati.
- **Aksessuar:** FIFO usuli. Avval eng eski partiyadan sotiladi, tannarx o‘sha partiyalardan olinadi.
- Tovar xaridi xarajat hisoblanmaydi. U omborga aktiv bo‘lib kiradi va faqat sotilganda tannarxga o‘tadi.

## Foyda
- Sof savdo tushumi = sotuv summasi − chegirmalar − qaytarishlar.
- Yalpi foyda = sof savdo tushumi − sotilgan tovar tannarxi.
- Hisoblangan sof natija = yalpi foyda − operatsion xarajatlar − hisobdan chiqarilgan tovar.
- Soliq hisoblanmaydi, shuning uchun bu “soliqdan keyingi foyda” emas.

## Pul va foyda alohida
- Nasiya savdoning foydasi savdo kunida hisoblanadi. Pul esa to‘langan kuni kassaga tushadi.
- Qarz to‘lovi faqat kassaga tushadi. U qayta savdo yoki foyda hisoblanmaydi.
- Egasining pul kiritishi yoki olishi daromad ham, xarajat ham emas. U faqat pul harakatida ko‘rinadi.

## Qaytim
- Mijoz savdo summasidan ko‘p naqd bersa, farq qaytim hisoblanadi. Kassaga faqat savdo summasi yoziladi.
- Karta summasi savdodan oshib keta olmaydi.

## Qaytarish va bekor qilish
- Qaytarish asl savdoga bog‘lanadi. Qaytarilgan summa va tannarx shu kunning hisobotidan ayriladi.
- Mijoz to‘lagan pul yangi summadan oshsa, farq pul qaytarish sifatida yoziladi. Agar qarz bo‘lsa, avval qarz kamayadi.
- Tovar ikki yo‘ldan biriga ketadi:
  - Sotuvga qaytadi. Telefonning asl kirim sanasi saqlanadi, qaytgan sana alohida yoziladi.
  - Nosoz deb belgilanadi. Nosoz aksessuar darhol yo‘qotish sifatida yoziladi.
- Savdoni bekor qilish = barcha qolgan tovarlarni qaytarish va pulni qaytarish. Savdo o‘chmaydi, “bekor qilingan” belgisi va sababi bilan qoladi.
- Qarz to‘lovi yoki ta’minotchi to‘lovi bekor qilinganda asl yozuv qoladi va unga qarshi manfiy yozuv qo‘shiladi.

## Tuzatishlar
- Faqat **ombordagi va hech qachon sotilmagan** qurilmaning IMEI, narxi va sanasi tahrirlanadi. Bunda ta’minotchi hisobi avtomatik tuzatiladi.
- Sotilgan qurilma tahrirlanmaydi, aks holda o‘tgan hisobotlar buziladi.
- Aksessuar partiyasi faqat undan hali sotilmagan bo‘lsa tahrirlanadi.
- O‘chirilgan xarajat yashirinadi, lekin amallar jurnalida iz qoladi.

## Kassa
- Naqd = barcha naqd to‘lovlar + egasi kiritgan − egasi olgan − naqd xarajatlar − ta’minotchiga naqd to‘lovlar − pul qaytarishlar ± kassa farqlari.
- Kassani yopishda sanalgan summa kiritiladi. Farq (kamomad yoki ortiqcha) alohida yoziladi, kassa qoldig‘i sanalgan summaga tenglashadi.

## Eslatmalar
- Har bir sotilmagan telefon uchun 15 va 30 kunda bir martadan eslatma chiqadi. Kunlar Toshkent vaqti bo‘yicha hisoblanadi.
- Qarz muddati o‘tganda har bir savdo uchun bir marta eslatma chiqadi.
