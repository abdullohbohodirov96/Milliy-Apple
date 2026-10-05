# Milliy Apple — boshqaruv tizimi va Telegram magazin (v2.1, prototip)

**Milliy Apple** do‘koni uchun (telefon, planshet, aksessuar): kirim va ombor (har bir telefon IMEI bilan), sotuv, nasiya va qarz muddati, qaytarish, kassa, xarajatlar, hisobotlar, xodimlar va parollar, xaridorlar uchun magazin.

Butun ilova bitta `index.html` faylida ishlaydi. Server va baza kerak emas — ma’lumotlar brauzer xotirasida saqlanadi.

## Papka tarkibi

| Fayl | Vazifasi |
|---|---|
| `public/` | **Saytga joylanadigan qism**: `index.html` (ilova), `manifest.webmanifest`, `sw.js`, `icons/` |
| `render.yaml` | Render uchun tayyor sozlama (static site + xavfsizlik sarlavhalari) |
| `vercel.json` | Vercel uchun tayyor sozlama |
| `tests/` | 80 ta avtomatik test: `e2e_test.py` (62 — funksiyalar) va `anim_test.py` (18 — animatsiyalar) |
| `docs/` | Hisob qoidalari va server versiyasi topshirig‘i — saytda ochiq bo‘lmaydi |

## Tez boshlash

1. Ilovani HTTPS manzilda oching (pastdagi joylash usullaridan biri bilan). `index.html`ni kompyuterda shunchaki ochib ko‘rsa ham bo‘ladi.
2. Birinchi ochilishda **asosiy admin** login va parolini o‘zingiz yaratasiz. Parol kamida 8 belgi bo‘lishi va harf hamda raqamdan iborat bo‘lishi kerak. Haqiqiy do‘kon uchun “Demo ma’lumotlar” belgisini qo‘ymang.
3. **Yana → Xodimlar** bo‘limida sotuvchilarni qo‘shing va har biriga login, parol va huquq bering: kirim, qaytarish, tannarxni ko‘rish.
4. **Yana → Egasi kassasi** bo‘limida boshlang‘ich naqd pulni “Pul kiritdi” deb yozing.
5. Tovarlarni **+ Kirim** orqali kiriting va sotuvni boshlang.

## Joylashtirish

Saytga faqat `public/` papka chiqadi. `docs/` va `tests/` ommaga ko‘rinmaydi.

### Render (tavsiya etiladi — bepul Static Site)
1. Papkani GitHub’ga yuklang (yangi repozitoriy → “Upload files” → papka ichidagi hamma narsani sudrab tashlang).
2. dashboard.render.com → **New → Blueprint** → repozitoriyni tanlang → **Apply**. `render.yaml` hamma narsani o‘zi sozlaydi.
3. Bir necha daqiqada `https://milliy-apple.onrender.com` ko‘rinishidagi manzil tayyor bo‘ladi.

Static Site bepul, “uxlab qolmaydi” va o‘z domeningizni (masalan `milliyapple.uz`) bepul ulash mumkin.

### Vercel
vercel.com → New Project → repozitoriy → Deploy. `vercel.json` avtomatik qo‘llanadi.

### Yangilash
GitHub’dagi `public/index.html` faylini almashtirsangiz, sayt o‘zi yangilanadi. Telefonga o‘rnatilgan ilova keyingi ochilishda yangi versiyani oladi.

## Telefonga o‘rnatish

- **iPhone:** Safari’da oching → “Ulashish” → “Bosh ekranga qo‘shish”.
- **Android:** Chrome’da oching → ⋮ → “Ilovani o‘rnatish”.

## Telegram magazin

1. @BotFather → botingiz → **Bot Settings → Menu Button** → URL sifatida `https://SIZNING-MANZIL/#magazin` ni kiriting, tugma nomini `🛍 Magazin` qiling.
2. `#magazin` bilan ochilgan sahifada faqat katalog ko‘rinadi: tannarx, IMEI va ta’minotchi chiqmaydi, admin paneliga qaytish tugmasi ham yo‘q.

**Muhim cheklov:** bu prototipda ma’lumotlar har bir qurilmada alohida saqlanadi. Shuning uchun xaridor yuborgan buyurtma do‘kon telefoniga **avtomatik kelmaydi**. Magazin hozircha katalog sifatida ishlaydi. Buyurtmalar real vaqtda kelishi uchun server versiyasi kerak (`docs/CLAUDE_CODE_TOPSHIRIQ.md`ga qarang).

## Zaxira nusxa — har kuni oling

**Yana → Sozlamalar → Zaxira nusxani olish** tugmasi nusxani buferga ko‘chiradi. Uni Telegram “Saqlanganlar”ga yoki Google Drive’ga joylang. Tiklash uchun **Zaxiradan tiklash** oynasiga shu matnni qo‘ying.

Nusxada parollarning shifrlangan izi bor, shuning uchun uni boshqalarga yubormang.

## Xavfsizlik

Ilovada quyidagi himoyalar bor:

- Parollar PBKDF2-SHA256 (150 000 iteratsiya) bilan saqlanadi, har bir foydalanuvchi uchun alohida tuz ishlatiladi. Ochiq parol hech qayerda saqlanmaydi.
- 5 marta xato kiritilsa, login 5 daqiqaga bloklanadi.
- Sessiya 12 soatdan keyin tugaydi. Parol o‘zgarsa, eski sessiyalar bekor bo‘ladi.
- Huquqlar ham ekranda, ham har bir funksiya ichida tekshiriladi.
- XSS’dan himoya bor: barcha kiritilgan matnlar ekranga chiqarishdan oldin tozalanadi.
- Moliyaviy yozuvlar izsiz o‘chirilmaydi. Bekor qilish yozuvi va amallar jurnali saqlanadi.

**Cheklov:** ma’lumotlar brauzerda saqlangani uchun qurilmaga to‘liq kirgan va dasturlashni biladigan odam ularni o‘zgartirishi mumkin. Telefonni ekran qulfi bilan himoyalang. To‘liq server himoyasi faqat server versiyasida bo‘ladi.

## Testlarni ishga tushirish

```bash
pip install playwright && playwright install chromium
python tests/e2e_test.py
python tests/anim_test.py
```

Natija: 62 + 18 = 80 test — birinchi sozlash, login bloki, xodimlar va parollar, huquqlar, tahrirlash va o‘chirish, qaytim, qarz muddati, bekor qilish, kassa, zaxira, XSS va 360/390/430 px ekranlar.
