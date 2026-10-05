# Milliy Apple — server versiyasi uchun Claude Code topshirig‘i

Do‘kon nomi: **Milliy Apple**. Brend: qora-oq monoxrom uslub, logotip `icons/icon-512.png` da. Sarlavha shrifti Montserrat.

Ushbu faylni to‘liq Claude Code’ga yuboring. Loyiha papkasidagi `index.html` — tayyor prototip. Server versiyasi interfeys va hisob-kitob qoidalarini undan olsin.

---

## 0. Prototip asosida ishlash (eng muhim)

1. Repozitoriydagi `index.html` — ishlaydigan va testdan o‘tgan prototip. Uni o‘qib chiq. Ekranlar, oqimlar, matnlar, dizayn tokenlari va hisob-kitob funksiyalarini (`createSale`, `returnCore`, `refundExtra`, `report`, `kassa`, `fifoTake`) asos qilib ol.
2. `docs/HISOB-QOIDALARI.md` — hisob qoidalarining manbasi. Backend shu qoidalarga to‘liq mos bo‘lsin va har bir qoida uchun test yozilsin.
3. `tests/e2e_test.py` dagi stsenariylar server versiyasida ham o‘tishi kerak.
4. Prototipda bor quyidagi imkoniyatlar server versiyasida ham saqlansin:
   - Birinchi ishga tushishda xavfsiz admin yaratish. Default parol bo‘lmasin.
   - Xodimlar: login va parol, rollar, alohida huquqlar (kirim, qaytarish, tannarx ko‘rish). Hisobni o‘chirib qo‘yish yoki butunlay o‘chirish. Oxirgi adminni o‘chirib bo‘lmasin. Parol o‘zgarsa, sessiyalar bekor bo‘lsin.
   - Barcha yozuvlarni tahrirlash, o‘chirish yoki arxivlash prototipdagi qoidalar bilan. Moliyaviy yozuvlar faqat bekor qilish yozuvi orqali tuzatilsin.
   - Qaytim, kassa qoldig‘i (naqd va karta), kassani yopish, qarz muddati va muddati o‘tgan qarzlar.
   - Aksessuar va nosoz qurilmani hisobdan chiqarish.
   - `#magazin` havolasi bilan faqat katalog.
5. Prototipda bo‘lmagan, server talab qiladigan qismlar:
   - Umumiy baza. Magazin buyurtmalari real vaqtda do‘konga kelsin.
   - Telegram bot, initData tekshiruvi, admin chatiga kunlik hisobot.
   - Object storage’da rasmlar.
   - Kundalik avtomatik backup.
   - Prototipdagi brauzer zaxira nusxasini (JSON) yangi bazaga import qiladigan migratsiya skripti. Parol izlari PBKDF2-SHA256, 150 000 iteratsiya, tuz base64 — shu formatni qabul qilsin.

---

## Asl texnik topshiriq

Sen tajribali full-stack dasturchi va mobil interfeys dizaynerisan. Menga telefon, planshet va aksessuar sotadigan bitta do‘kon uchun ishlaydigan boshqaruv tizimi hamda shu bazaga ulangan Telegram Mini App magazin yarat.

Faqat reja yoki chiroyli demo bilan cheklanma. Haqiqiy bazaga ulangan, amallarni saqlaydigan, foydalanishga tayyor loyiha qil. Avval mavjud repositoryni tekshir: loyiha bo‘lsa, uning ishlaydigan qismlarini saqlab rivojlantir. Loyiha bo‘lmasa, quyidagi talablarga mos yarat.

### 1. Maqsad va asosiy tamoyillar

Do‘kon egasi telefonidan quyidagilarni boshqara olsin:

- Tovar kirimi va ombor.
- Telefonlar, planshetlar, aksessuarlar.
- Sotuvlar, qaytarishlar, to‘lovlar.
- Mijoz va ta’minotchi qarzlari.
- Xarajatlar, yalpi foyda va sof natija.
- Sotilmay turgan telefonlar.
- Xodimlarning amallari.
- Xaridorlarga ko‘rinadigan Telegram magazin.

Dastur o‘zbekcha, sodda, tez va telefonda juda qulay bo‘lsin. Keraksiz murakkab ERP interfeysi, ulkan kartochkalar va ortiqcha animatsiyalar bo‘lmasin.

Bir do‘kon, dastlab 2–3 xodim uchun loyihala. Kelajakdagi kengayishni butun tizimni qayta yozmasdan amalga oshirish mumkin bo‘lsin, lekin hozirdan keraksiz murakkablik qo‘shma.

### 2. Texnologiya va joylashtirish

Yangi loyiha bo‘lsa:

- Frontend: React + TypeScript + Vite.
- Interfeys: Tailwind CSS, kerak bo‘lsa yengil komponentlar kutubxonasi.
- Backend: Node.js + TypeScript, sodda va ishonchli API.
- Baza: Neon PostgreSQL, migratsiyalar va connection pooling.
- Render’da frontend buildini ham beradigan bitta backend servis orqali ishlash imkoniyati.
- Telegram bot: webhook orqali.
- Bir backend va bir umumiy baza: boshqaruv paneli, veb-katalog va Telegram Mini App uchun.
- Telefon bosh ekraniga qo‘shish uchun PWA.

Agar mavjud loyihada boshqa yaxshi stack bo‘lsa, uni asossiz almashtirma.

Tarif limitlarini kodga doimiy haqiqat sifatida qotirib qo‘yma. Ishlab chiqarish uchun bepul hosting uzluksizligini kafolatlama. Bepuldan pulli tarifga ma’lumotlarni yo‘qotmasdan o‘tish mumkin bo‘lsin.

### 3. Mobil interfeys — eng muhim talab

Interfeysni avval telefon uchun loyihala, keyin kompyuterga moslashtir.

- 360, 390 va 430 px kengliklarda gorizontal scroll bo‘lmasin.
- iPhone Safari va Telegram ichida yaxshi ishlasin.
- Safe area, pastki navigatsiya va ochilgan klaviaturani hisobga ol.
- Asosiy navigatsiya: Bosh sahifa, Tovarlar, Sotuv, Hisobot, Yana.
- Admin tovarlar ro‘yxatining asosiy ko‘rinishi ixcham ro‘yxat bo‘lsin.
- Oddiy telefon ekranida, klaviatura yopiq holatda, yuqori boshqaruvlar bilan birga taxminan 4–6 ta mahsulot ko‘rinsin.
- Bir mahsulot kartochkasi yarim ekranni egallamasin.
- Ro‘yxat qatori taxminan 72–96 px: kichik rasm, model, xotira, holat, sotuv narxi va qoldiq.
- Kerakli tafsilotlar qator bosilganda ochilsin.
- Xaridor katalogida ixcham ikki ustunli grid va ro‘yxatga almashtirish bo‘lsin.
- Mahsulot rasmlari kichik va optimallashtirilgan bo‘lsin.
- Matnni haddan tashqari kichraytirib sig‘dirma. O‘qilishi va bosilishi qulay bo‘lsin.
- Forma inputlari iPhone’da zoom bo‘lib ketmaydigan o‘lchamda bo‘lsin.
- Tugma bosish maydonlari qulay, lekin vizual bloklar ixcham bo‘lsin.
- Uzun jadvallarni mobil ekranga siqma, mos ro‘yxatga aylantir.
- Qidiruv va filtrlar yuqorida qulay joylashsin.
- Muhim amallarda aniq holat ko‘rsat: saqlanmoqda, saqlandi, xato.
- Bo‘sh sahifa, yuklanish, xatolik va internet yo‘q holatlari chiroyli ishlansin.
- Qaytarib bo‘lmaydigan amallarda tasdiq so‘ra, oddiy amallarda ortiqcha modal chiqarma.

Dizayn: oq yoki yumshoq kulrang fon, to‘q matn, bitta asosiy aksent rang, sodda ikonalar. Telefon do‘koniga mos professional ko‘rinish.

### 4. Kirish va huquqlar

Ilovaning o‘zida login bo‘lsin.

Rollar:

1. Egasi/admin: barcha ma’lumotlar, foyda, tannarx, sozlamalar va xodimlar.
2. Sotuvchi: ruxsat berilgan kirim, sotuv va mijoz amallari.
3. Xaridor: faqat ochiq katalog va o‘z buyurtmasi.

Sotuvchi tannarx va foydani ko‘ra olishini admin boshqarsin. Ruxsatni faqat interfeysda yashirma, backendda ham tekshir.

Ochiq API javoblariga tannarx, foyda, IMEI, ichki izohlar, ta’minotchi va boshqa mijozlarning ma’lumotlari chiqmasin.

Parollar hash qilinsin, xavfsiz sessiyalar va login urinishlariga limit bo‘lsin. Default admin paroli yoki kodda saqlangan secret bo‘lmasin.

### 5. Mahsulotlar va ombor modeli

Mahsulot modeli bilan alohida jismoniy telefonni ajrat:

- Mahsulot kartasi: brend, model, kategoriya, xotira, rang, tavsif, rasmlar.
- Jismoniy telefon/planshet: alohida ID, IMEI1/IMEI2 yoki serial, holat, kirim sanasi, ta’minotchi, tannarx, sotuv holati.
- Bir xil modeldan kelgan har bir telefon alohida hisobga olinsin.
- IMEI/serial kiritilsa, takroriy qiymatga yo‘l qo‘yma.
- Aksessuarlar dona va kirim partiyalari bilan yuritilsin.
- Aksessuar tannarxi uchun izchil usul, masalan FIFO, qo‘llansin va hujjatlashtirilsin.

Maydonlar:

- Nomi, kategoriya, brend/model.
- Xotira va rang, tegishli bo‘lsa.
- Yangi yoki ishlatilgan.
- Ishlatilgan telefonda ixtiyoriy battery health va holat izohi.
- Xarid narxi, xarid valyutasi, kirimdagi kurs.
- Mahsulotga ajratilgan qo‘shimcha kirim xarajati.
- Tavsiya etilgan sotuv narxi.
- Ta’minotchi, kirim sanasi.
- Rasmlar — majburiy emas.
- IMEI/serial va ichki izohlar — ommaga ko‘rinmasin.

Rasm bo‘lmasa, sifatli placeholder ko‘rsat. Telefonda kamera yoki galereyadan rasm yuklash mumkin bo‘lsin. Yuklashdan oldin siqish, o‘lchamni kamaytirish, fayl turi va hajmini tekshirish bo‘lsin.

Qidiruv: model, SKU/shtrixkod va xodimlar uchun IMEI bo‘yicha.
Filtrlar: kategoriya, mavjud/sotilgan, yangi/ishlatilgan, narx, kirim sanasi, 15/30 kundan oshgan.

Sotilgan tovar bazadan o‘chmasin, uning tarixi saqlansin.

### 6. Sotuv va hisob-kitob

Sotuv jarayoni telefonda tez bajarilsin:

1. Tovar yoki IMEI tanlash.
2. Narx, chegirma va kerak bo‘lsa mijozni kiritish.
3. To‘lov turini tanlash.
4. Tasdiqlash.

Qo‘llab-quvvatla:

- Bitta sotuvda bir nechta mahsulot.
- Naqd, karta va aralash to‘lov.
- Qisman to‘lov va qarz/nasiya.
- Qarz savdosida mijoz va aloqa ma’lumoti majburiy.
- Qarzni keyinchalik qisman yoki to‘liq yopish.
- Sotuvga bog‘langan to‘lov tarixi.
- Sotuvchi va vaqtni avtomatik yozish.
- Chegirma limitlari va tannarxdan past sotishda ogohlantirish/admin ruxsati.
- Oddiy chop etiladigan savdo hujjati. Fiskal integratsiyasiz uni fiskal chek deb atama.

Hisoblar:

- Sof savdo tushumi = sotuv summasi − chegirmalar − tegishli qaytarishlar.
- Sotilgan tovar tannarxi aniq telefon/partiya tannarxidan olinsin.
- Yalpi foyda = sof savdo tushumi − sotilgan tovar tannarxi.
- Davrning hisoblangan sof natijasi = yalpi foyda − davr operatsion xarajatlari.
- Pul kelib tushishi va foyda alohida ko‘rsatilsin.
- Qarzni undirish ikkinchi marta savdo yoki foyda sifatida hisoblanmasin.
- Tovar xaridi ikki marta xarajatga yozilmasin: omborga kirim va keyinchalik sotilgan tovar tannarxi to‘g‘ri ajratilsin.
- Nasiyaga sotilgan savdoning foydasi va amalda tushgan puli aralashtirilmasin.
- Soliq to‘liq hisoblanmasa, natijani soliqlardan keyingi sof foyda deb noto‘g‘ri belgilama.

Pul hisobida float ishlatma: PostgreSQL NUMERIC/Decimal yoki mos aniq hisoblash ishlat.

UZS asosiy hisobot valyutasi bo‘lsin. USD’da kirim/sotuv kerak bo‘lsa, amaldagi operatsiya kursini saqla. Keyingi kurs o‘zgarishi eski operatsiya natijasini o‘zgartirmasin.

### 7. Qaytarish, tuzatish va parallel sotuv

- Savdo, qoldiq va to‘lov yozilishi bitta bazaviy transaction ichida bajarilsin.
- Ikki sotuvchi bitta IMEI’ni bir paytda sota olmasin.
- Tugmani ikki marta bosish yoki qayta yuborilgan so‘rov savdoni takrorlamasin: idempotency ishlat.
- “Sotildi” faqat server tasdiqlagandan keyin chiqsin.
- Qaytarish asl sotuvga bog‘lansin.
- Qaytarilgan tovar tekshirilgandan keyin sotuvga qaytarilishi yoki nosoz holatga o‘tishi mumkin bo‘lsin.
- Qaytarishda pul, qarz, tannarx va foyda to‘g‘ri qayta hisoblanishi kerak.
- Yakunlangan moliyaviy yozuvlarni izsiz o‘chirib yoki almashtirib yuborma; tuzatish/bekor qilish tarixi bo‘lsin.
- Boshlang‘ich pul qoldig‘i va egasining pul kiritishi/olishi savdo daromadi yoki operatsion xarajat bilan aralashmasin.

### 8. Dashboard va hisobot

Bugun, kecha, 7 kun, oy va ixtiyoriy sana oralig‘i bo‘lsin.

Ixcham dashboard:

- Nechta telefon sotildi.
- Nechta planshet va aksessuar sotildi.
- Sotuvlar soni va tushum.
- Amalda kelib tushgan pul.
- Yalpi foyda, xarajat va sof natija.
- Mijozlardan olinadigan qarz.
- Ta’minotchilarga beriladigan qarz.
- Ombordagi dona soni va tannarx bo‘yicha qiymati.
- Uzoq turib qolgan tovarlar.

Hisobotlar:

- Model/kategoriya va sotuvchi bo‘yicha.
- Eng ko‘p sotilgan va eng ko‘p foyda keltirgan mahsulotlar.
- Qaytarishlar va chegirmalar.
- Kam qolgan aksessuarlar.
- Davr bo‘yicha pul harakati.
- CSV eksport.

Vaqt zonasi Asia/Tashkent. “Bugun” va kunlik hisobotlar shu zona bo‘yicha hisoblansin.

### 9. 15 va 30 kunlik eslatmalar

Har bir sotilmagan telefonning omborga kelgan sanasidan vaqt hisobla:

- 15 kun to‘lganda sariq belgi va eslatma.
- 30 kun to‘lganda qizil belgi va kuchliroq eslatma.
- Ro‘yxatda “18 kundan beri omborda” kabi matn.
- Sotilgan telefonlarga eslatma chiqmasin.
- Qaytarilgan telefonda asl kirim sanasi saqlansin, qaytgan sana alohida yozilsin.

Admin panelda bildirishnoma markazi bo‘lsin. Telegram bog‘langan bo‘lsa, adminning shaxsiy chatiga kunlik umumlashtirilgan eslatma yuborilsin.

Bir xil chegara uchun qayta-qayta spam qilma. Eslatmalarni bazada qayd qil. Uxlaydigan serverdagi setInterval’ga tayanma: himoyalangan scheduled endpoint va tashqi scheduler uchun sozlash yo‘riqnomasi bo‘lsin. Jadval ishlamagan bo‘lsa, keyingi ishga tushishda o‘tkazib yuborilgan eslatmalar tekshirilsin.

Telegram sozlanmagan bo‘lsa ham, ilova ichidagi eslatmalar ishlasin.

### 10. Telegram Mini App magazin

Botda “🛍 Magazin” tugmasi bilan ochilsin.

Xaridor:

- Mavjud mahsulotlar va rasmlarni ko‘rsin.
- Qidiruv, kategoriya, narx va yangi/ishlatilgan filtrlaridan foydalansin.
- Mahsulot tafsilotlarini ochsin.
- Savatchaga qo‘shib buyurtma so‘rovi yuborsin.
- Ismi, telefoni va olib ketish/yetkazish istagini kiritishi mumkin bo‘lsin.
- O‘z buyurtma holatini ko‘rsin.

Buyurtma yuborilishi darhol sotuv va foyda bo‘lib hisoblanmasin. Sotuvchi buyurtmani tasdiqlab, savdoga aylantirsin. Savdoga aylantirganda mavjudlik yana tekshirilsin.

Buyurtma holatlari: yangi, bog‘lanildi, tasdiqlandi, yakunlandi, bekor qilindi.

Telegram initData backendda tekshirilsin, eskirgan yoki soxta ma’lumot qabul qilinmasin. Telegram foydalanuvchi ID’sini bilishning o‘zi admin kirishi uchun yetarli bo‘lmasin.

Telegram bo‘lmasa ham, ochiq veb-katalog ishlasin. Xaridor Telegram hisobidan boshqa mijozlarning buyurtmalariga kira olmasin.

### 11. Rasmlar va resurs tejamkorligi

- Rasmlarni PostgreSQL ichida base64 sifatida saqlama.
- Render’ning vaqtinchalik lokal diskini doimiy rasm ombori sifatida ishlatma.
- Doimiy object storage ishlat; provayderni environment orqali sozlash mumkin bo‘lsin.
- Thumbnail, WebP kabi optimallashtirish va lazy loading.
- Rasm xizmati sozlanmagan bo‘lsa, rasmsiz tovar qo‘shish va qolgan tizim ishlasin.
- Telegram bot tokenini frontendga yoki rasm URL’lariga chiqarmaslik.

Katalog sahifalansin, barcha tovarlar birdan yuklanmasin. Ochiq katalog uchun qisqa kesh ishlat, kirim/sotuv/narx o‘zgarishida yangilansin. Buyurtma va sotuvda qoldiq doim bazadan tekshirilsin.

Har bir mijoz kirishida barcha hisobotlar qayta hisoblanmasin. Cheksiz polling bo‘lmasin. Qidiruv debounce, kerakli indekslar va optimallashtirilgan so‘rovlar ishlat.

Health-check bazaga so‘rov yubormasin. Bazani sun’iy ravishda 24/7 uyg‘oq saqlaydigan ping qo‘shma.

### 12. Ishonchlilik va zaxira

- Internet uzilganda aniq ogohlantirish.
- Saqlanmagan savdoni muvaffaqiyatli deb ko‘rsatma.
- Dastlab offline sotuv qo‘shma; PWA keshida maxfiy API javoblari saqlanmasin.
- Telefon almashtirilsa ham ma’lumotlar bazada qolsin.
- Muhim amallar uchun audit: kim, qachon, nima o‘zgartirdi.
- Input validation, fayl yuklash xavfsizligi, rate limit va ruxsat tekshiruvlari.
- Shaxsiy ma’lumotlar va secretlar logga chiqmasin.
- Kundalik zaxira nusxa olish va boshqa xavfsiz joyga yozish uchun script hamda scheduler sozlamasi.
- Zaxiradan qayta tiklash yo‘riqnomasi va tekshiruvi.
- Faqat CSV eksportni to‘liq database backup deb hisoblama.

### 13. Tayyorlik mezoni

Quyidagi asosiy oqimlarni tekshir:

1. Rasmsiz va rasmli telefon qo‘shish.
2. Bir xil modeldagi ikki IMEI’li telefonni alohida hisoblash.
3. To‘liq va qisman to‘lovli savdo.
4. Qarzni yopish foydani takror hisoblamasligi.
5. Qaytarishdan keyin qoldiq, qarz va foyda.
6. Ikki sotuvchining bir IMEI’ni parallel sotishga urinishida bittasi rad etilishi.
7. Takroriy so‘rovda takroriy savdo yaratilmasligi.
8. 15/30 kunlik eslatmalar va takror yuborilmasligi.
9. Xaridor API’sida tannarx va maxfiy ma’lumotlar yo‘qligi.
10. 360/390/430 px ekranlarda overflow bo‘lmasligi va ro‘yxatda 4–6 mahsulot ko‘rinishi.

Moliyaviy hisob va parallel sotuv uchun mazmunli avtomatik testlar yoz. Mobil interfeysni real brauzer o‘lchamlarida tekshir. Qila olmagan tekshiruvingni bajarildi deb aytma.

### 14. Yakuniy topshirish

Menga quyidagilarni tayyorla:

- Ishlaydigan frontend va backend.
- Database schema va migratsiyalar.
- Maxfiy qiymatlarsiz .env.example.
- Xavfsiz birinchi admin yaratish usuli.
- Alohida development/demo ma’lumotlari; production bazaga soxta savdo qo‘shma.
- Render, Neon, object storage, Telegram bot va scheduler uchun aniq yo‘riqnoma.
- Backup va restore yo‘riqnomasi.
- Test natijalari va qolgan real cheklovlar.

Oddiy texnik qarorlarni o‘zing hal qil, har qadamda mendan so‘rama. Faqat secret, tashqi hisob yoki jiddiy biznes qarori kerak bo‘lsa so‘ra. Secret yo‘qligi sabab butun ishni to‘xtatma: kodni va sozlash joylarini tayyorla, qaysi ulanish ishlamaganini aniq ko‘rsat.

Mavjud production ma’lumotlarini ruxsatsiz o‘chirma, pullik xizmatni ruxsatsiz yoqma. Qolgan lokal va qaytariladigan ishlarni oxirigacha bajar.

Birinchi navbatda to‘g‘ri ishlaydigan kirim → ombor → sotuv → to‘lov → foyda oqimini qur. Keyin mobil interfeysni sayqalla va shu tizimga Mini App’ni ula. Natija sodda, ixcham va telefonda kundalik ishlatishga qulay bo‘lsin.
