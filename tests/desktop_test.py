"""Noutbuk/planshet ko‘rinishi: 768–1440 px da joylashuv, menyu va scroll."""
import asyncio, pathlib
from playwright.async_api import async_playwright
F=(pathlib.Path(__file__).resolve().parent.parent/'public'/'index.html').as_uri()
res=[]
def ok(n,c,i=''): res.append(('✅' if c else '❌',n,str(i)[:160]))
async def main():
  async with async_playwright() as P:
    b=await P.chromium.launch();errs=[]
    pg=await b.new_page(viewport={'width':1280,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)));ev=pg.evaluate
    await pg.goto(F);await ev('localStorage.clear()');await pg.reload();await pg.wait_for_timeout(1800)
    ok('Noutbukda kirish sahifasi ikki qismli (logo + forma)',await ev("getComputedStyle(document.querySelector('.login')).gridTemplateColumns.split(' ').length")==2)
    await pg.fill('#su_name','Abdulloh');await pg.fill('#su_login','admin');await pg.fill('#su_pw','Milliy2026a');await pg.fill('#su_pw2','Milliy2026a');await pg.check('#su_demo');await pg.click('#su_btn');await pg.wait_for_timeout(1500)
    vis=lambda sel:ev(f"(()=>{{const e=document.querySelector('{sel}');return !!e&&getComputedStyle(e).display!=='none'}})()")
    ok('Noutbukda chap menyu ko‘rinadi, pastki menyu yashiringan',await vis('.side') and not await vis('.bn'))
    ok('Ma’lumot kartalari 4 ustunda',await ev("getComputedStyle(document.querySelector('.kp')).gridTemplateColumns.split(' ').length")==4)
    await pg.click('.side >> text=Tovarlar');await pg.wait_for_timeout(300)
    ok('Chap menyudan bo‘lim almashadi',await ev("S.ui.tab")=='prod' and 'Tovarlar' in await pg.inner_text('.ptl'))
    ok('Tovarlar ro‘yxati 2 ustunda',await ev("getComputedStyle(document.getElementById('plist')).gridTemplateColumns.split(' ').length")==2)
    await pg.click('.side >> text=Kassa');await pg.wait_for_timeout(300);ok('Chap menyudan “Kassa” oynasi ochiladi',await pg.locator('.sh h2:has-text("Kassa")').count()==1);await ev('closeSheet()')
    await ev("go('sale');addUnitToCart(S.units.find(u=>u.status==='stock').id)");await pg.wait_for_timeout(300)
    w=await ev("(()=>{const r=document.querySelector('.sale-r').getBoundingClientRect(),l=document.querySelector('.sale-l').getBoundingClientRect();return [Math.round(l.width),Math.round(r.width),r.left>l.right]})()")
    ok('Sotuv: chapda savatcha, o‘ngda to‘lov',w[0]>300 and w[1]>300 and w[2],w)
    await pg.click('text=Hammasi naqd');await pg.click('#sbtn');await pg.wait_for_timeout(800)
    ok('Noutbukda sotuv to‘liq ishlaydi',await ev("S.sales.length")==5);await ev('closeSheet()')
    await ev("go('rep')");ok('Hisobot bo‘limlari 2 ustunda',await ev("getComputedStyle(document.querySelector('.rgrid')).gridTemplateColumns.split(' ').length")==2)
    # barcha o‘lchamlarda gorizontal scroll yo‘qligi
    for W in (768,1024,1280,1440,1920):
        await pg.set_viewport_size({'width':W,'height':900});bad=[]
        for t in ['home','prod','sale','rep','more']:
            await ev(f"go('{t}')")
            if await ev('document.documentElement.scrollWidth')>W: bad.append(t)
        for sh in ['usersSheet()','settingsSheet()','kassaSheet()','custDebtSheet()','supSheet()','profileSheet()','kirimSheet()']:
            await ev(sh)
            if await ev("document.querySelector('.sh').scrollWidth>document.querySelector('.sh').clientWidth"): bad.append(sh)
            await ev('closeSheet()')
        await ev("openShop()")
        if await ev('document.documentElement.scrollWidth')>W: bad.append('magazin')
        await ev("closeShop()")
        side=await vis('.side');bn=await vis('.bn')
        ok(f'{W}px: scroll yo‘q; menyu: {"chapda" if side else "pastda"}',not bad and (side==(W>=1024)) and (bn==(W<1024)),bad)
    await pg.set_viewport_size({'width':1440,'height':900});await ev("openShop()")
    n=await ev("getComputedStyle(document.querySelector('.grid')).gridTemplateColumns.split(' ').length")
    ok('Magazin noutbukda 5 ustunli katalog',n>=5,n)
    await pg.set_viewport_size({'width':390,'height':844});await ev("closeShop()")
    ok('Telefonga qaytsa — pastki menyu, chap menyu yo‘q',await vis('.bn') and not await vis('.side'))
    ok('JS xatolar yo‘q',not errs,errs[:2])
    await b.close()
asyncio.run(main())
f=sum(r[0]=='❌' for r in res)
for r in res:print(*r)
print(f'\nJAMI: {len(res)} test, {len(res)-f} o‘tdi, {f} xato')
