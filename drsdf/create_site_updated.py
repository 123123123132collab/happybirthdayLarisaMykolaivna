from pathlib import Path
import base64

cat_path = Path("cat.png")
cat_data = base64.b64encode(cat_path.read_bytes()).decode("ascii") if cat_path.exists() else ""

notes = []
for i in range(1, 21):
    tilt = [-2, 1.4, -1.2, 2][(i-1) % 4]
    colors = ["#FFF0B8", "#F8DDE4", "#F8D4BD"]
    color = colors[(i-1) % 3]
    notes.append(
        f'<button type="button" class="note" data-note="{i-1}" aria-label="Відкрити побажання {i}" style="--tilt:{tilt}deg;--paper:{color}">'
        f'<span class="pin"></span><span class="number">{i}</span></button>'
    )

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#fbe9e5">
<title>Happy Birthday, Larisa Mykolaivna!</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">
<style>
:root{--pink:#f8dde4;--peach:#f8d4bd;--yellow:#fff0b8;--rose:#a85f70;--red:#b52f3b}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;color:#76595a;font-family:"DM Sans",sans-serif;background:linear-gradient(135deg,#fffaf6,#fbe9e5 55%,#f7d9ce);overflow-x:hidden}
.hero{min-height:650px;display:flex;align-items:center;justify-content:center;text-align:center;position:relative;padding:55px 18px 35px;overflow:hidden}
.hero:before,.hero:after{content:"✧";position:absolute;color:#d5a19b;font-size:30px;animation:twinkle 3s infinite}
.hero:before{top:22%;left:12%}.hero:after{right:13%;top:34%;animation-delay:1s}
.hero-inner{width:100%;max-width:980px;position:relative;z-index:1;animation:rise 1s both}
.kicker{font-size:.67rem;letter-spacing:.28em;text-transform:uppercase;color:#aa7b7d;font-weight:700}
.paper-title{display:inline-block;position:relative;margin:22px auto 0;padding:8px 28px 18px;background:#f4eee3;color:#302c2a;filter:drop-shadow(0 7px 7px #785a4c35);clip-path:polygon(1% 5%,8% 3%,9% 0,18% 4%,30% 1%,44% 4%,57% 1%,70% 4%,84% 1%,99% 5%,97% 17%,100% 31%,97% 46%,100% 61%,97% 77%,99% 95%,85% 98%,70% 96%,55% 100%,40% 96%,25% 99%,10% 96%,1% 99%,3% 82%,0 67%,3% 50%,0 34%,3% 18%)}
.paper-title h1{font-family:"Playfair Display",Georgia,serif;font-weight:600;font-size:clamp(3.3rem,10vw,7.8rem);line-height:.78;letter-spacing:-.065em;text-transform:lowercase;margin:0;text-align:left}
.paper-title h1 span{display:block}
.name{font-family:"Playfair Display",serif;font-style:italic;color:#a85f70;font-size:clamp(1.55rem,4vw,2.7rem);margin:26px 0 7px}
.subtitle{font-family:"Playfair Display",serif;font-style:italic;color:#a17d7b;font-size:1.05rem;margin:8px 0 0}
.kitty{width:min(390px,78vw);height:auto;display:block;margin:12px auto -12px;filter:drop-shadow(0 16px 20px #98606b30);animation:float 5s ease-in-out infinite}
.scroll{display:inline-block;margin-top:8px;color:#a97579;text-decoration:none;font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;border-bottom:1px solid #d7a6a4;padding-bottom:7px}
.section{max-width:1120px;margin:auto;padding:54px 18px 78px}
.heading{text-align:center;margin-bottom:27px}
.heading .kicker{color:#b47d7d}
h2{font:500 clamp(2rem,5vw,3.3rem) "Playfair Display",serif;color:#895963;margin:9px 0}
.intro{max-width:600px;margin:auto;line-height:1.65;color:#987b79;font-size:.92rem}
.frame{padding:13px;border-radius:5px;background:linear-gradient(135deg,#f2d6b5,#c99566 28%,#e8c39b 55%,#b9845b);box-shadow:0 22px 45px #8a5d4930,inset 0 1px 3px #fff9;position:relative}
.frame:before{content:"";position:absolute;inset:5px;border:1px solid #fff8;pointer-events:none}
.cork{position:relative;overflow:hidden;padding:34px 22px;background-color:#b58a68;background-image:radial-gradient(#79583b36 .8px,transparent 1px),radial-gradient(#f4dfc54a .7px,transparent 1px),linear-gradient(135deg,#c19a78,#a77d5e 55%,#bd9472);background-size:7px 7px,11px 11px,auto;box-shadow:inset 0 0 35px #65442d55}
.cork:after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(120deg,#fff2,transparent 32%,#5d3c2418)}
.grid-area{position:relative;z-index:1}
.threads{position:absolute;inset:0;width:100%;height:100%;z-index:0;pointer-events:none;overflow:visible}
.threads path{fill:none;stroke:#a92f39;stroke-width:3.2;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 1px 1px #57262a88)}
.notes{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-template-rows:repeat(5,112px);gap:22px 18px;z-index:1}
.note{position:relative;align-self:center;justify-self:center;width:min(100%,155px);height:88px;background:var(--paper);box-shadow:0 5px 13px #51352255;display:flex;align-items:center;justify-content:center;transform:rotate(var(--tilt));transition:transform .25s,box-shadow .25s}
.note:hover{transform:rotate(0) translateY(-4px);box-shadow:0 10px 18px #51352266}
.pin{position:absolute;top:-8px;left:calc(50% - 7px);width:14px;height:14px;border-radius:50%;background:radial-gradient(circle at 35% 28%,#ffd5d1 0 14%,#bd3c45 36%,#75252d 100%);box-shadow:0 2px 3px #46212888}
.number{font:600 2rem "Playfair Display",serif;color:#8d6263}
.board-caption{text-align:center;color:#fff0e7;font:italic 1rem "Playfair Display",serif;margin:17px 0 0}
.footer{text-align:center;padding:0 20px 42px;color:#a77c7c;font:italic 1rem "Playfair Display",serif}

.note{border:0;padding:0;cursor:pointer;font:inherit}
.note:focus-visible{outline:3px solid #fff;outline-offset:5px}
.wish-overlay{position:fixed;inset:0;z-index:50;display:none;align-items:center;justify-content:center;padding:3vh 3vw;background:#39272dcc;backdrop-filter:blur(8px)}
.wish-overlay.is-open{display:flex;animation:fade-in .25s ease both}
.wish-card{position:relative;width:min(1100px,96vw);height:min(90vh,850px);overflow:auto;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:clamp(28px,6vw,76px);border:10px solid #e7c5a8;border-radius:8px;background:radial-gradient(circle at top left,#fffdf7,#fff0e8 55%,#f8dce2);box-shadow:0 25px 90px #160d0d88}
.wish-card:before{content:"";position:absolute;inset:9px;border:1px solid #d9b49e;pointer-events:none}
.wish-close{position:absolute;top:18px;right:20px;z-index:1;width:46px;height:46px;border:0;border-radius:50%;background:#f3d8dc;color:#895963;font-size:30px;line-height:1;cursor:pointer}
.wish-number{font-size:.75rem;letter-spacing:.25em;text-transform:uppercase;color:#b47d7d;font-weight:700}
.wish-title{font:500 clamp(2rem,5vw,3.7rem) "Playfair Display",serif;color:#895963;margin:22px 0}
.wish-message{max-width:760px;white-space:pre-line;font:clamp(1.05rem,2.2vw,1.45rem)/1.9 "DM Sans",sans-serif;color:#76595a}
.wish-heart{margin-top:28px;color:#c77d88;font-size:2rem}
@keyframes fade-in{from{opacity:0}to{opacity:1}}
@media(max-width:600px){.wish-overlay{padding:10px}.wish-card{width:100%;height:94vh;padding:55px 25px 35px;border-width:6px}.wish-close{top:12px;right:12px}}

@keyframes rise{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
@keyframes float{0%,100%{transform:translateY(0) rotate(-1deg)}50%{transform:translateY(-10px) rotate(1deg)}}
@keyframes twinkle{0%,100%{opacity:.35;transform:scale(.8)}50%{opacity:1;transform:scale(1.2) rotate(18deg)}}
@media(max-width:600px){.hero{min-height:590px}.kitty{width:min(320px,80vw)}.section{padding:40px 11px 60px}.frame{padding:9px}.cork{padding:23px 9px}.notes{grid-template-rows:repeat(5,86px);gap:12px 7px}.note{height:68px;width:100%;max-width:125px}.number{font-size:1.55rem}.threads path{stroke-width:2.5}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;scroll-behavior:auto!important;transition:none!important}}
</style>
</head>
<body>
<header class="hero">
 <div class="hero-inner">
  <div class="kicker">A special day • A special person</div>
  <div class="paper-title"><h1><span>happy</span><span>birthday</span></h1></div>
  <div class="name">Larisa Mykolaivna</div>
  <p class="subtitle">A little celebration made with love, just for you.</p>
  <img class="kitty" src="data:image/png;base64,CAT_IMAGE_DATA" alt="A fluffy cream kitten holding a bouquet of pink and peach roses">
  <a class="scroll" href="#birthday-board">Discover your birthday wishes ↓</a>
 </div>
</header>
<main id="birthday-board" class="section">
 <div class="heading">
  <div class="kicker">The birthday investigation</div>
  <h2>The Case of a Wonderful Person</h2>
  <p class="intro">Twenty little notes, connected one after another by a single red thread.</p>
 </div>
 <div class="frame">
  <div class="cork">
   <div class="grid-area">
    <svg class="threads" viewBox="0 0 1000 648" preserveAspectRatio="none" aria-hidden="true">
     <path d="M125 56 L375 56 L625 56 L875 56 L875 184 L625 184 L375 184 L125 184 L125 312 L375 312 L625 312 L875 312 L875 440 L625 440 L375 440 L125 440 L125 568 L375 568 L625 568 L875 568"/>
    </svg>
    <div class="notes">
     NOTE_ITEMS
    </div>
   </div>
  </div>
 </div>
 <p class="board-caption">Every number will soon hold a special birthday wish. ♡</p>
</main>
<footer class="footer">Made with ♥ and a little birthday magic</footer>

<div class="wish-overlay" id="wishOverlay" aria-hidden="true">
 <section class="wish-card" role="dialog" aria-modal="true" aria-labelledby="wishTitle" aria-describedby="wishMessage">
  <button class="wish-close" id="wishClose" type="button" aria-label="Закрити">×</button>
  <div class="wish-number" id="wishNumber">ПОБАЖАННЯ №1</div>
  <h2 class="wish-title" id="wishTitle">Теплі слова для вас</h2>
  <p class="wish-message" id="wishMessage"></p>
  <div class="wish-heart">♡</div>
 </section>
</div>

<script>
/*
  РЕДАГУВАННЯ ТЕКСТІВ:
  Для кожного стікера змінюй title (заголовок) і message (основний текст).
  Порядок елементів відповідає цифрам на стікерах: перший = №1, другий = №2 і т.д.
*/
const wishes = [
  { title: "З днем народження!", message: "Бажаю Вам міцного здоров’я, душевного тепла, щирих усмішок і багато щасливих моментів. Нехай кожен день приносить радість!" },
  { title: "Нехай збуваються мрії", message: "Бажаю, щоб навіть найзаповітніші мрії ставали реальністю, а поруч завжди були люди, які підтримують і надихають." },
  { title: "Більше щасливих днів", message: "Нехай у житті буде якомога більше приводів для радості, приємних зустрічей, добрих новин і теплих обіймів." },
  { title: "Міцного здоров’я", message: "Нехай здоров’я ніколи не підводить, сили та енергії вистачає на все задумане, а кожен ранок починається з гарного настрою." },
  { title: "Любові та турботи", message: "Бажаю відчувати любов і турботу близьких, чути найтепліші слова та завжди знати, що Ви дуже важливі й цінні." },
  { title: "Натхнення", message: "Нехай натхнення знаходить Вас у простих речах, а кожна нова ідея приносить задоволення та чудові результати." },
  { title: "Домашнього затишку", message: "Нехай удома завжди панують мир, затишок, сміх, аромат чогось смачного та атмосфера, куди хочеться повертатися." },
  { title: "Приємних несподіванок", message: "Бажаю, щоб життя частіше дивувало приємними подарунками, несподіваними зустрічами та новинами, від яких хочеться усміхатися." },
  { title: "Спокою в душі", message: "Нехай на серці буде легко й спокійно, тривоги минають, а кожен день дарує впевненість у хорошому майбутньому." },
  { title: "Успіхів у всьому", message: "Бажаю, щоб усі справи складалися якнайкраще, зусилля приносили гарні результати, а удача частіше була на Вашому боці." },
  { title: "Щирих людей поруч", message: "Нехай поруч будуть добрі, чесні та щирі люди, з якими можна розділити і радість, і важливі моменти життя." },
  { title: "Часу для себе", message: "Бажаю знаходити час на відпочинок, улюблені заняття, маленькі радощі та все те, що наповнює душу теплом." },
  { title: "Світлих надій", message: "Нехай віра в краще ніколи не згасає, попереду чекають чудові можливості, а кожен новий день відкриває щось прекрасне." },
  { title: "Радості в дрібницях", message: "Бажаю помічати красу навколо: сонячні ранки, квіти, добрі слова, щирі посмішки та маленькі дива кожного дня." },
  { title: "Невичерпної енергії", message: "Нехай вистачає сил на задумане, бажання творити й відкривати нове, а втома завжди змінюється приємним відпочинком." },
  { title: "Миру та добра", message: "Бажаю миру, безпеки, добробуту та впевненості в завтрашньому дні. Нехай добро завжди повертається сторицею." },
  { title: "Багато приводів усміхатися", message: "Нехай усмішка частіше з’являється на обличчі, а приводів для неї буде стільки, що не вистачатиме дня, щоб усі перерахувати." },
  { title: "Здійснення бажань", message: "Нехай усе задумане поступово здійснюється, двері до нових можливостей відчиняються, а мрії знаходять шлях до реальності." },
  { title: "Тепла кожного дня", message: "Бажаю теплих слів, добрих новин, щирих обіймів і відчуття, що життя дарує багато прекрасного." },
  { title: "Ви заслуговуєте на найкраще", message: "Нехай цей рік буде щедрим на щастя, любов, здоров’я та здійснені бажання. Дякую за Вашу доброту. Зі святом! ♡" }
];

const overlay = document.getElementById("wishOverlay");
const wishNumber = document.getElementById("wishNumber");
const wishTitle = document.getElementById("wishTitle");
const wishMessage = document.getElementById("wishMessage");
const closeButton = document.getElementById("wishClose");
let previousFocus = null;

function openWish(index) {
  const wish = wishes[index];
  if (!wish) return;
  previousFocus = document.activeElement;
  wishNumber.textContent = `ПОБАЖАННЯ №${index + 1}`;
  wishTitle.textContent = wish.title;
  wishMessage.textContent = wish.message;
  overlay.classList.add("is-open");
  overlay.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";
  closeButton.focus();
}
function closeWish() {
  overlay.classList.remove("is-open");
  overlay.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
  if (previousFocus) previousFocus.focus();
}
document.querySelectorAll(".note").forEach((note) => {
  note.addEventListener("click", () => openWish(Number(note.dataset.note)));
});
closeButton.addEventListener("click", closeWish);
overlay.addEventListener("click", (event) => {
  if (event.target === overlay) closeWish();
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && overlay.classList.contains("is-open")) closeWish();
});
</script>
</body>
</html>"""
html = html.replace("CAT_IMAGE_DATA", cat_data).replace("NOTE_ITEMS", "\n".join(notes))
out = Path("index_with_clickable_wishes.html")
out.write_text(html, encoding="utf-8")
print(f"Created {out.name} ({out.stat().st_size:,} bytes)")