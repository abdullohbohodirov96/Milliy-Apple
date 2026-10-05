"""Animatsiyalar testi: har biri ishga tushadi, tugaydi va iz qoldirmaydi."""
import asyncio, pathlib
from playwright.async_api import async_playwright
F=(pathlib.Path(__file__).resolve().parent.parent/'public'/'index.html').as_uri()
res=[]
def ok(n,c,i=''): res.append(('✅' if c else '❌',n,str(i)[:150]))
async def main():
  async with async_playwright() as P:
    b=await P.chromium.launch();errs=[]
    pg=await b.new_page(viewport={'width':390,'height':844},is_mobile=True,has_touch=True);pg.on('pageerror',lambda e:errs.append(str(e)))
    ev=lambda js:pg.evaluate(js)
    await pg.goto(F);await ev('localStorage.clear()');await pg.reload();await pg.wait_for_timeout(1800)
    await pg.fill('#su_name','Abdulloh');await pg.fill('#su_login','admin');await pg.fill('#su_pw','Milliy2026a');await pg.fill('#su_pw2','Milliy2026a');await pg.check('#su_demo');await pg.click('#su_btn');await pg.wait_for_timeout(150)
    # 1. sahifaga kirish va raqamlar
    ok('Bosh sahifa animatsiya bilan ochildi', await ev("document.getElementById('app').classList.contains('enter')"))
    mid=await ev("document.querySelector('[data-n]').textContent")
    await pg.wait_for_timeout(1000)
    fin=await ev("(()=>{const e=document.querySelector('[data-n]');return [e.textContent,sp(+e.dataset.n)+(e.dataset.s||'')]})()")
    ok('Raqamlar sanab chiqadi va aniq qiymatda to‘xtaydi', fin[0]==fin[1], f'oraliq: {mid} → yakun: {fin[0]}')
    # 2. Kirim → tovarlar ro‘yxatida yashil yonadi
    await ev("kirimSheet()");await pg.fill('#kb','Apple');await pg.fill('#km','iPhone 17');await pg.fill('#kpr','15000000');await pg.fill('#kcost','13000000');await pg.fill('#kimei','359999000000001')
    await pg.click('text=Kirimni saqlash');await pg.wait_for_timeout(120)
    st=await ev("({tab:S.ui.tab,flash:document.querySelector('#plist .row.flash .t1')?.textContent,ok:!!document.querySelector('.okfx')})")
    ok('Kirimdan keyin Tovarlarga o‘tadi, yangi mahsulot yonadi',st['tab']=='prod' and 'iPhone 17' in (st['flash'] or ''),st)
    ok('Muvaffaqiyat belgisi (✓) chiqdi',st['ok'])
    await pg.wait_for_timeout(700)
    bg=await ev("getComputedStyle(document.querySelector('#plist .row.flash')).backgroundColor")
    ok('Yangi mahsulot qatori haqiqatan yashil rangda yonadi',bg.replace(' ','') in ('rgb(229,244,234)',),bg)
    await pg.wait_for_timeout(1400);ok('✓ belgisi o‘zi yo‘qoladi',await ev("!document.querySelector('.okfx')"))
    # 3. modal yopilishi
    await ev("prodSheet(S.products[0].id)");await ev("closeSheet()")
    c=await ev("({closing:document.querySelectorAll('.ov.closing').length,ids:document.querySelectorAll('.ov.closing [id]').length})")
    await pg.wait_for_timeout(300);gone=await ev("document.querySelectorAll('.ov').length")
    ok('Modal sirpanib yopiladi va o‘chadi',c['closing']==1 and c['ids']==0 and gone==0,(c,gone))
    # 4. Savatcha qatori
    await ev("go('sale');addUnitToCart(S.units.find(u=>u.imei1==='359999000000001').id)")
    ok('Savatchaga qo‘shilgan qator animatsiya bilan chiqadi',await ev("!!document.querySelector('#scart .cl.pop')"))
    await ev("addAccToCart(S.products.find(p=>p.cat==='acc'&&stock(p.id)>0).id)");await ev("rmLine(1)")
    ok('O‘chirilayotgan qator chetga suriladi',await ev("!!document.querySelector('#scart .cl.out')"))
    await pg.wait_for_timeout(300);ok('…va keyin ro‘yxatdan chiqadi',await ev("S.ui.scart.length")==1)
    # 5. Sotuv → tarixda yonadi
    await pg.click('text=Hammasi naqd');await pg.click('#sbtn');await pg.wait_for_timeout(700)
    ok('Sotuvdan keyin ✓ va tarixdagi savdo yonadi',await ev("!!document.querySelector('.okfx')&&!!document.querySelector('.list .row.flash')"))
    await ev("closeSheet()");await pg.wait_for_timeout(1500)
    # 6. Magazin: savatchaga uchish
    await ev("openShop()");await pg.wait_for_timeout(500)
    await pg.locator('.card .add').first.click();await pg.wait_for_timeout(200)
    fly=await ev("document.querySelectorAll('.fly').length")
    sw=await ev("document.documentElement.scrollWidth")
    await pg.wait_for_timeout(800)
    after=await ev("({fly:document.querySelectorAll('.fly').length,bump:document.querySelector('button[aria-label=Savatcha]').classList.contains('bump'),dot:document.querySelector('button[aria-label=Savatcha] .dot')?.textContent})")
    ok('Mahsulot rasmi savatchaga uchib boradi',fly==1,fly)
    ok('Uchish tugagach element o‘chadi, savatcha “sakraydi”, son 1',after['fly']==0 and after['bump'] and after['dot']=='1',after)
    ok('Uchish paytida gorizontal scroll yo‘q',sw<=390,sw)
    # 7. Yana ko‘rsatish
    await ev("""for(let i=0;i<30;i++){const p={id:nid(),cat:'acc',brand:'Test',model:'G‘ilof '+i,mem:'',color:'',cond:'new',price:50000+i,desc:'',img:null,min:0,archived:false};S.products.push(p);S.batches.push({id:nid(),pid:p.id,qty:5,left:5,cost:20000,base:20000,ext:0,inDate:Date.now(),sup:S.suppliers[0].id})};S.ui.sl=20;save();render()""")
    await pg.click('text=Yana ko‘rsatish');await pg.wait_for_timeout(50)
    n=await ev("({pop:document.querySelectorAll('.card.pop').length,all:document.querySelectorAll('.card').length})")
    ok('“Yana ko‘rsatish”da faqat yangi kartalar animatsiya bilan chiqadi',n['pop']==n['all']-20 and n['pop']>0,n)
    # 8. Toast
    await ev("toast('test')");await pg.wait_for_timeout(2900);ok('Xabar (toast) silliq yo‘qoladi',await ev("!!document.querySelector('.toast.out')"))
    # 9. Kam harakat rejimi
    await pg.emulate_media(reduced_motion='reduce');await ev("closeShop();go('home')")
    t=await ev("(()=>{const e=document.querySelector('[data-n]');return [e.textContent,sp(+e.dataset.n)+(e.dataset.s||'')]})()")
    await ev("openShop()");await pg.locator('.card .add').first.click();fl=await ev("document.querySelectorAll('.fly').length")
    ok('“Kam harakat” yoqilsa animatsiyalar o‘chadi',t[0]==t[1] and fl==0,(t,fl))
    ok('JS xatolar yo‘q',not errs,errs[:2])
    await b.close()
asyncio.run(main())
f=sum(r[0]=='❌' for r in res)
for r in res:print(*r)
print(f'\nJAMI: {len(res)} test, {len(res)-f} o‘tdi, {f} xato')
