"""Build the Glad Accountancy concept site (no dependencies).

    python3 _build/pages.py && python3 _build/fonts.py

English at /, Traditional Chinese (Hong Kong usage, written Chinese) at /zh/.
Every string is written as L(english, chinese). Facts and their sources are in README.md.
"""
import json
import os

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
V = "4"  # cache-bust: bump on every CSS/JS change

LANG = "en"


def L(en, zh):
    return en if LANG == "en" else zh


# ------------------------------------------------------------------ facts (sources in README)
BUSINESS = "Glad Accountancy"
PHONE = "07769 391052"
TEL = "+447769391052"
WA = "https://wa.me/447769391052"
EMAIL = "info@gladacc.co.uk"
OFFICIAL = "https://gladacc.co.uk/"
UXC = "https://ux-circles.com/professionals"
BASE = "https://uxcircles.github.io/gladacc/"
HOME = [-2.3526665, 53.4010546]  # 197-201 Manchester Road, Broadheath (OpenStreetMap)
GMAPS = "https://www.google.com/maps/search/?api=1&query=197+Manchester+Road+Altrincham+WA14+5NU"
ROUTES = json.load(open(os.path.join(BUILD, "routes.json")))
TIMP = ROUTES["Timperley"]

LANGS = [("en", "", "English", "en-GB"), ("zh", "zh/", "繁體中文", "zh-Hant-HK")]
HTML_LANG = {"en": "en-GB", "zh": "zh-Hant-HK"}
SEAL = open(os.path.join(BUILD, "seal_glyph.txt")).read()


def seal(cls="seal", label=None):
    """The signature: the 樂 seal from Glad Accountancy's own logo."""
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return (f'<svg class="{cls}" viewBox="0 0 100 100" fill="currentColor" {aria}>'
            '<path d="M30 6H90a4 4 0 0 1 4 4V90a4 4 0 0 1-4 4H22M6 70V10a4 4 0 0 1 4-4h8" fill="none" '
            f'stroke="currentColor" stroke-width="5" stroke-linecap="round"/>{SEAL}</svg>')


def sign(zh, en, num=None, cls=""):
    """A Hong Kong street-name plate: Chinese above English, black on white, inset border."""
    n = f'<span class="sign-no">{num}</span>' if num else ""
    return (f'<span class="sign {cls}"><span class="sign-zh" lang="zh-Hant-HK">{zh}</span>'
            f'<span class="sign-en" lang="en-GB">{en}</span>{n}</span>')


def address(short=False):
    if short:
        return L("Office 5, 197 Manchester Road, Altrincham", "Altrincham 曼徹斯特道 197 號 5 室")
    return L("Office 5, 197 Manchester Road, Altrincham WA14 5NU",
             "Altrincham WA14 5NU，曼徹斯特道（Manchester Road）197 號 5 室")


# ------------------------------------------------------------------ shared pieces
def head(prefix, slug, title, desc, hero=None):
    alts = "".join(
        f'<link rel="alternate" hreflang="{h}" href="{BASE}{d}{"" if slug == "index.html" else slug}">\n'
        for _, d, _, h in LANGS
    )
    zh_pre = ""
    if LANG == "zh":
        zh_pre = f'<link rel="preload" href="{prefix}assets/fonts/chiron-sung-hk-700.woff2" as="font" type="font/woff2" crossorigin>\n'
    pre_img = f'<link rel="preload" as="image" href="{prefix}assets/img/{hero}" fetchpriority="high">\n' if hero else ""
    return f'''<!doctype html>
<html lang="{HTML_LANG[LANG]}" class="l-{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
{alts}<link rel="alternate" hreflang="x-default" href="{BASE}{"" if slug == "index.html" else slug}">
<link rel="icon" href="{prefix}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{prefix}assets/img/apple-touch-icon.png">
<meta name="theme-color" content="#161616">
<link rel="preload" href="{prefix}assets/fonts/red-hat-display.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}assets/fonts/source-sans-3.woff2" as="font" type="font/woff2" crossorigin>
{zh_pre}{pre_img}<link rel="stylesheet" href="{prefix}assets/site.css?v={V}">
<script defer src="{prefix}assets/site.js?v={V}"></script>
</head>
'''


def concept_bar():
    if LANG == "zh":
        return f'''<div class="concept-bar" role="note">
  <div class="concept-inner">
    <p class="concept-text"><span class="concept-tag">概念</span><span class="concept-long">概念設計展示，並非<a href="{OFFICIAL}" target="_blank" rel="noopener">{BUSINESS}官方網站</a>。</span></p>
    <a class="concept-credit" href="{UXC}" target="_blank" rel="noopener"><span class="concept-by">設計：</span><strong>UX CIRCLES</strong><svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg></a>
  </div>
</div>'''
    return f'''<div class="concept-bar" role="note">
  <div class="concept-inner">
    <p class="concept-text"><span class="concept-tag">Concept</span><span class="concept-long">Redesign concept. Not the <a href="{OFFICIAL}" target="_blank" rel="noopener">official {BUSINESS} website</a>.</span></p>
    <a class="concept-credit" href="{UXC}" target="_blank" rel="noopener"><span class="concept-by">Designed by </span><strong>UX CIRCLES</strong><svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg></a>
  </div>
</div>'''


def concept_note():
    if LANG == "zh":
        return f'<p class="concept-note">非官方概念設計：<a href="{UXC}" target="_blank" rel="noopener">UX CIRCLES</a></p>'
    return f'<p class="concept-note">Unofficial redesign concept by <a href="{UXC}" target="_blank" rel="noopener">UX CIRCLES</a></p>'


def nav_items():
    return [
        ("services.html", L("Services", "服務")),
        ("index.html#about", L("About", "關於我們")),
        ("contact.html", L("Contact", "聯絡")),
    ]


def lang_links(prefix, slug, cls):
    target = "" if slug in ("index.html", "404.html") else slug
    out = []
    for code, d, label, h in LANGS:
        cur = ' aria-current="true"' if code == LANG else ""
        out.append(f'<a href="{prefix}{d}{target}" lang="{h}" hreflang="{h}"{cur}>{label}</a>')
    return f'<div class="{cls}">' + "".join(out) + "</div>"


ICON = {
    "wa": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.8-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3Z"/></svg>',
    "tel": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M3 5h18v14H3zM3 6l9 7 9-7"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></svg>',
}


def header(prefix, pg, slug):
    links = "".join(
        f'<a href="{pg}{h}"{" aria-current=page" if h == slug else ""}>{t}</a>' for h, t in nav_items()
    )
    return f'''<body>
<a class="skip" href="#main">{L("Skip to content", "跳至內容")}</a>
{concept_bar()}
<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="{pg}index.html">
      {seal("brand-seal")}
      <span class="brand-txt"><span class="brand-name">Glad Accountancy</span><span class="brand-sub">{L("Chartered Accountants", "特許會計師")}</span></span>
    </a>
    <nav class="nav" aria-label="{L('Main', '主選單')}">{links}</nav>
    {lang_links(prefix, slug, "langs")}
    <a class="head-wa" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}<span>{PHONE}</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">{L("Menu", "選單")}</button>
  </div>
  <div class="menu" id="menu" hidden>
    <nav class="wrap menu-in" aria-label="{L('Menu', '選單')}">
      {links}
      {lang_links(prefix, slug, "menu-langs")}
    </nav>
  </div>
</header>
'''


def footer(prefix, pg, slug):
    return f'''<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      {seal("foot-seal")}
      <p class="foot-tag">{L("Genuine business partner for small enterprises", "小企業的真誠業務夥伴")}</p>
    </div>
    <div>
      <h2 class="foot-h">{L("Office", "辦公室")}</h2>
      <p>{address()}</p>
      <p>{L("Open 09:00–17:00", "辦公時間 09:00–17:00")}</p>
    </div>
    <div>
      <h2 class="foot-h">{L("Contact", "聯絡")}</h2>
      <p><a href="tel:{TEL}">{PHONE}</a> · <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <h2 class="foot-h">{L("Pages", "頁面")}</h2>
      <p><a href="{pg}services.html">{L("Services", "服務")}</a> · <a href="{pg}contact.html">{L("Contact", "聯絡")}</a> · <a href="{pg}privacy.html">{L("Privacy", "私隱政策")}</a></p>
      {lang_links(prefix, slug, "foot-langs")}
    </div>
  </div>
  <div class="wrap foot-legal">
    <p>{L("Glad Accountancy Limited, registered in England and Wales, company number 05728991. Registered office: Office 18, The Generation Centre, Dane Street, Rochdale OL12 6XB.",
         "Glad Accountancy Limited，於英格蘭及威爾斯註冊，公司編號 05728991。註冊辦事處：Office 18, The Generation Centre, Dane Street, Rochdale OL12 6XB。")}</p>
    <p>{L("Photos of Hong Kong from the Glad Accountancy website. Altrincham photos: DS Pugh and Richard Sutcliffe, CC BY-SA 2.0, via Geograph.",
         "香港照片取自 Glad Accountancy 網站。Altrincham 照片：DS Pugh、Richard Sutcliffe，CC BY-SA 2.0，來源 Geograph。")}</p>
    {concept_note()}
  </div>
</footer>
<nav class="mbar" aria-label="{L('Quick contact', '快速聯絡')}">
  <a href="tel:{TEL}">{ICON["tel"]}<span>{L("Call", "致電")}</span></a>
  <a href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}<span>WhatsApp</span></a>
  <a href="{pg}contact.html#enquiry">{ICON["mail"]}<span>{L("Enquire", "查詢")}</span></a>
</nav>
</body>
</html>
'''


def img(prefix, name, w, h, alt, cls="", lazy=True, sizes=None):
    extra = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    s = f' sizes="{sizes}"' if sizes else ""
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{prefix}assets/img/{name}" width="{w}" height="{h}" alt="{alt}"{s}{extra}>'


# ------------------------------------------------------------------ content
def services():
    return [
        ("accounting", L("Accounting", "會計"), "會計道", "Accounting Road", [
            L("Set up an accounting system that fits a small business", "為小企業建立合適的會計系統"),
            L("Keep your computerised accounting records", "代為處理電腦化會計紀錄"),
            L("Tidy up past years' records", "整理過往年度的帳目"),
            L("Train your staff in basic bookkeeping", "培訓員工處理基本簿記"),
        ], L("Systems, records, catch-up and staff training.", "會計系統、帳目紀錄、整理舊帳及員工培訓。")),
        ("reporting", L("Reporting", "財務報告"), "報告街", "Reporting Street", [
            L("Annual accounts filed at Companies House", "向公司註冊處（Companies House）提交年度帳目"),
            L("Detailed management accounts for the owners", "為管理層編製詳細的管理帳目"),
            L("Accounts sent to HMRC with your Company Tax Return", "連同公司稅表把帳目提交英國稅務海關總署（HMRC）"),
        ], L("Annual accounts and management reports.", "年度帳目及管理報告。")),
        ("tax-vat", L("Tax and VAT", "稅務及增值稅"), "稅務徑", "Tax Path", [
            L("Corporation Tax Return (CT600)", "公司稅報稅表（CT600）"),
            L("iXBRL tagging of accounts and tax returns", "帳目及報稅表的 iXBRL 標記"),
            L("VAT registration", "增值稅（VAT）登記"),
            L("Making Tax Digital VAT returns", "以「數碼稅務」（Making Tax Digital）提交增值稅申報"),
        ], L("CT600, iXBRL, VAT registration and MTD returns.", "CT600、iXBRL、增值稅登記及數碼申報。")),
        ("payroll", L("Payroll", "薪俸"), "薪俸里", "Payroll Lane", [
            L("PAYE registration", "PAYE 僱主登記"),
            L("Real Time Information (RTI) submissions", "即時資料（RTI）申報"),
            L("Payslips", "編製糧單"),
            L("Workplace pension registration and support", "職場退休金登記及支援"),
            L("Statutory returns for employees and the company", "僱員及公司的法定申報"),
        ], L("PAYE, RTI, payslips and workplace pensions.", "PAYE、RTI、糧單及職場退休金。")),
        ("self-assessment", L("Self Assessment", "個人自我評稅"), "評稅坊", "Self Assessment Square", [
            L("Registration for Self Assessment", "登記自我評稅"),
            L("Tax returns for the self-employed", "自僱人士報稅"),
            L("Accounts for sole traders", "為獨資經營者編製帳目"),
            L("Non-resident landlord registration", "非居英業主（Non-resident landlord）登記"),
        ], L("Registration, returns, sole trader accounts, landlords.", "登記、報稅、獨資帳目及業主。")),
    ]


def map_block(prefix):
    data = {
        "home": HOME,
        "mark": f"{prefix}assets/img/seal.svg",
        "label": "Glad Accountancy",
        "routes": [{"name": L("Timperley Metrolink", "Timperley 電車站"), "short": "Timperley",
                    "start": TIMP["start"], "min": TIMP["min"], "coords": TIMP["coords"]}],
    }
    return f'''<div class="map" data-map data-src="{prefix}assets/vendor/maplibre/maplibre-gl.js" data-css="{prefix}assets/vendor/maplibre/maplibre-gl.css" data-mapjs="{prefix}assets/map.js?v={V}">
  <div class="map-fallback">
    {seal("map-fallback-seal")}
    <p>{address()}</p>
    <a href="{GMAPS}" target="_blank" rel="noopener">{L("Open in Google Maps", "在 Google 地圖開啟")}</a>
  </div>
  <script type="application/json" id="map-data">{json.dumps(data, ensure_ascii=False)}</script>
</div>'''


def visit_card():
    return f'''<dl class="facts">
  <div><dt>{L("Address", "地址")}</dt><dd>{address()}</dd></div>
  <div><dt>{L("Hours", "辦公時間")}</dt><dd>09:00–17:00</dd></div>
  <div><dt>{L("By tram", "乘電車")}</dt><dd>{L(f"Timperley Metrolink stop, about {TIMP['min']} minutes' walk", f"Metrolink Timperley 站，步行約 {TIMP['min']} 分鐘")}</dd></div>
  <div><dt>{L("Phone and WhatsApp", "電話及 WhatsApp")}</dt><dd><a href="tel:{TEL}">{PHONE}</a></dd></div>
</dl>
<p class="btns"><a class="btn btn-ink" href="{GMAPS}" target="_blank" rel="noopener">{L("Directions", "路線")}{ICON["arrow"]}</a><a class="btn btn-line" href="mailto:{EMAIL}">{EMAIL}</a></p>'''


def page_home(prefix, pg):
    svc = "".join(
        f'''<li><a href="{pg}services.html#{sid}">{sign(zh, en)}<span class="svc-t">{t}</span><span class="svc-d">{short}</span></a></li>'''
        for sid, t, zh, en, _, short in services()
    )
    return f'''<main id="main">
<section class="hero">
  {img(prefix, "hk-tram.webp", 1600, 1066, L("A Hong Kong tram on a busy street, from the Glad Accountancy website", "香港電車駛過繁忙街道，照片取自 Glad Accountancy 網站"), "hero-img", lazy=False)}
  <div class="wrap hero-in">
    <div class="hero-sign" aria-hidden="true">{sign("曼徹斯特道", "Manchester Road", "197", "sign-xl")}</div>
    <h1>{L("Hong Kong chartered accountants on Manchester Road", '<span class="nw">香港人創辦的會計師行，</span><span class="nw">就在曼徹斯特道</span>')}</h1>
    <p class="lede">{L("Accounts, tax, VAT and payroll for small enterprises in Altrincham. Honest, quick and responsive.", "為 Altrincham 小企業處理會計、稅務及薪俸。")}</p>
    <p class="btns"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp {PHONE}</a><a class="btn btn-ghost" href="{pg}services.html">{L("Our services", "服務範圍")}</a></p>
    <p class="hero-proof">{L(address(True), "曼徹斯特道 197 號")} · 09:00–17:00</p>
  </div>
</section>

<section class="svc wrap" aria-labelledby="svc-h">
  <h2 id="svc-h">{L("Five things we handle", "五項服務")}</h2>
  <ul class="svc-grid">{svc}</ul>
</section>

<section class="neon" aria-label="{L('Mong Kok', '旺角')}">
  {img(prefix, "mong-kok-neon.webp", 1200, 767, L("Neon signs over a Mong Kok street at dusk, from the Glad Accountancy website", "黃昏時旺角街頭的霓虹招牌，照片取自 Glad Accountancy 網站"), "neon-img")}
  <div class="wrap neon-in"><p class="neon-line">{L("Honest, quick and responsive", "誠實．快捷．有回應")}</p></div>
</section>

<section class="about wrap" id="about" aria-labelledby="about-h">
  <figure class="about-fig">
    {img(prefix, "lion-rock.webp", 635, 391, L("Lion Rock above Kowloon housing estates, from the Glad Accountancy website", "九龍屋邨背後的獅子山，照片取自 Glad Accountancy 網站"))}
    <figcaption>{L("Lion Rock, Kowloon", "九龍獅子山")}</figcaption>
  </figure>
  <div class="about-txt">
    <h2 id="about-h">{L("Founded by Hongkongers", "由香港人創辦")}</h2>
    <p>{L("Glad Accountancy was founded by Hong Kong chartered accountants. We bring Hong Kong's working values to your books: personal, professional and efficient.", "Glad Accountancy 由香港特許會計師創辦，把香港人的做事方式帶到你的帳簿：貼身、專業、有效率。")}</p>
    <ul class="ticks">
      <li><strong>{L("Experienced", "經驗豐富")}</strong> {L("with businesses in many industries", "服務過不同行業的企業")}</li>
      <li><strong>{L("Simple", "簡單易明")}</strong> {L("accounts you can read", "帳目一看就明白")}</li>
      <li><strong>{L("Regular", "定期")}</strong> {L("reports and updates", "提供報告及進度")}</li>
    </ul>
  </div>
</section>

<section class="two-cities" aria-labelledby="tc-h">
  <div class="wrap">
    <h2 id="tc-h">{L("From Victoria Harbour to Altrincham", "由維多利亞港到 Altrincham")}</h2>
    <div class="strip">
      <figure>{img(prefix, "star-ferry.webp", 640, 480, L("A Star Ferry crossing Victoria Harbour, from the Glad Accountancy website", "天星小輪橫渡維多利亞港，照片取自 Glad Accountancy 網站"))}<figcaption>{L("Victoria Harbour", "維多利亞港")}</figcaption></figure>
      <figure>{img(prefix, "metrolink-altrincham.webp", 1200, 801, L("A Metrolink tram at Altrincham station", "Altrincham 站的 Metrolink 電車"))}<figcaption>{L("Metrolink, Altrincham line", "Metrolink Altrincham 線")}</figcaption></figure>
      <figure>{img(prefix, "altrincham-market-house.webp", 1200, 900, L("Altrincham Market House among red-brick roofs", "紅磚屋頂之間的 Altrincham Market House"))}<figcaption>{L("Market House, Altrincham", "Altrincham Market House")}</figcaption></figure>
    </div>
  </div>
</section>

<section class="visit wrap" aria-labelledby="visit-h">
  <div class="visit-txt">
    <h2 id="visit-h">{L("Visit us at 197 Manchester Road", "歡迎到訪曼徹斯特道 197 號")}</h2>
    {visit_card()}
  </div>
  {map_block(prefix)}
</section>
</main>
'''


def page_services(prefix, pg):
    band = f'<figure class="svc-band">{img(prefix, "altrincham-market-house.webp", 1200, 900, L("Altrincham Market House among red-brick roofs", "紅磚屋頂之間的 Altrincham Market House"))}<figcaption>{L("Altrincham, where our office is", "我們的辦公室位於 Altrincham")}</figcaption></figure>'
    parts = [f'''<section class="svc-block" id="{sid}" aria-labelledby="{sid}-h">
  <div class="svc-sign">{sign(zh, en)}</div>
  <div>
    <h2 id="{sid}-h">{t}</h2>
    <ul class="ticks">{"".join(f"<li>{i}</li>" for i in items)}</ul>
  </div>
</section>''' for sid, t, zh, en, items, _ in services()]
    blocks = "".join(parts[:3]) + band + "".join(parts[3:])
    return f'''<main id="main">
<section class="page-hero">
  {img(prefix, "mong-kok-neon.webp", 1200, 767, L("Neon signs over a Mong Kok street, from the Glad Accountancy website", "旺角街頭的霓虹招牌，照片取自 Glad Accountancy 網站"), "page-hero-img", lazy=False)}
  <div class="wrap page-hero-in">
    <h1>{L("Services", "服務範圍")}</h1>
    <p class="lede">{L("Everything a small enterprise needs from an accountant, from the first ledger to the year-end returns.", "小企業需要的會計服務，由第一本帳簿到年終申報。")}</p>
  </div>
</section>
<div class="wrap svc-list">{blocks}</div>
<section class="cta wrap">
  <h2>{L("Not sure which one you need?", "不肯定需要哪一項？")}</h2>
  <p>{L("Send us a WhatsApp message with a line about your business.", "用 WhatsApp 簡單告訴我們你的業務。")}</p>
  <p class="btns"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp {PHONE}</a><a class="btn btn-line" href="{pg}contact.html#enquiry">{L("Send an enquiry", "提交查詢")}</a></p>
</section>
</main>
'''


def page_contact(prefix, pg):
    opts = "".join(
        f'<label class="chk"><input type="checkbox" name="svc" value="{t}"><span>{t}</span></label>'
        for _, t, *_ in services()
    )
    return f'''<main id="main">
<section class="wrap contact-top">
  <div>
    <h1>{L("Contact Glad Accountancy", "聯絡 Glad Accountancy")}</h1>
    <p class="lede">{L("We are honest, quick and responsive. WhatsApp is usually fastest.", "我們誠實、快捷、有回應。WhatsApp 通常最快。")}</p>
    <p class="btns"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp</a><a class="btn btn-line" href="tel:{TEL}">{ICON["tel"]}{PHONE}</a></p>
    {visit_card()}
  </div>
  <form class="enquiry" id="enquiry" novalidate data-wa="{WA}" data-email="{EMAIL}">
    <h2>{L("Send an enquiry", "提交查詢")}</h2>
    <fieldset><legend>{L("What do you need help with?", "需要哪方面的協助？")}</legend><div class="chks">{opts}</div></fieldset>
    <label class="fld"><span>{L("Your name", "姓名")}</span><input name="name" autocomplete="name" required></label>
    <label class="fld"><span>{L("Phone or email", "電話或電郵")}</span><input name="contact" autocomplete="email" required></label>
    <label class="fld"><span>{L("Your business, in a line or two", "簡單介紹你的業務")}</span><textarea name="msg" rows="3"></textarea></label>
    <p class="form-err" role="alert" hidden>{L("Please add your name and a phone number or email.", "請填寫姓名及電話或電郵。")}</p>
    <div class="btns"><button class="btn btn-wa" type="submit" value="wa">{ICON["wa"]}{L("Send by WhatsApp", "以 WhatsApp 傳送")}</button><button class="btn btn-line" type="submit" value="email">{L("Send by email", "以電郵傳送")}</button></div>
    <p class="small">{L("This opens WhatsApp or your email app with your answers filled in. Nothing is stored on this website.", "按下後會開啟 WhatsApp 或電郵程式並填好內容，本網站不會儲存任何資料。")}</p>
  </form>
</section>
<section class="wrap contact-map">{map_block(prefix)}</section>
<figure class="band">{img(prefix, "metrolink-altrincham.webp", 1200, 801, L("A Metrolink tram at Altrincham station", "Altrincham 站的 Metrolink 電車"))}</figure>
</main>
'''


def page_privacy(prefix, pg):
    S = [
        (L("Who we are", "我們是誰"), [L(
            "Glad Accountancy Limited (company number 05728991) is the controller of the personal data described here. Contact: info@gladacc.co.uk.",
            "Glad Accountancy Limited（公司編號 05728991）是本政策所述個人資料的控制者。聯絡：info@gladacc.co.uk。")]),
        (L("What we collect", "我們收集的資料"), [L(
            "Contact details you send us; information needed to prepare accounts, tax returns and payroll; identity documents required by anti-money laundering rules.",
            "你提供的聯絡資料；編製帳目、報稅表及薪俸所需的資料；反洗錢規定要求的身份證明文件。")]),
        (L("Why we use it", "使用目的"), [L(
            "To provide the services you engage us for, to meet our legal duties (including anti-money laundering and tax law), and to reply to enquiries.",
            "提供你委託的服務、履行法律責任（包括反洗錢及稅務法例），以及回覆查詢。")]),
        (L("Who we share it with", "與誰分享"), [L(
            "HMRC, Companies House and pension providers when filing for you, and software providers that hold records for us. We do not sell personal data.",
            "代你申報時與英國稅務海關總署（HMRC）、公司註冊處及退休金機構分享，以及為我們儲存紀錄的軟件供應商。我們不會出售個人資料。")]),
        (L("How long we keep it", "保存期限"), [L(
            "For as long as the law requires, usually six years after our work for you ends.",
            "按法律要求保存，一般為服務結束後六年。")]),
        (L("Your rights", "你的權利"), [L(
            "Under the UK GDPR and the Data Protection Act 2018 you can ask for a copy of your data, correct it, or object to its use. You can also complain to the Information Commissioner's Office (ico.org.uk).",
            "根據英國《通用資料保障規例》（UK GDPR）及《2018 年資料保障法》，你可要求索取、更正個人資料或反對使用。你亦可向資訊專員辦公室（ico.org.uk）投訴。")]),
        (L("This website", "本網站"), [L(
            "This concept website sets no cookies and stores nothing you type. The map loads tiles from OpenFreeMap.",
            "本概念網站不使用 cookies，亦不會儲存你輸入的內容。地圖圖塊由 OpenFreeMap 提供。")]),
    ]
    body = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in S)
    return f'''<main id="main" class="wrap prose">
<h1>{L("Privacy notice", "私隱政策")}</h1>
<p class="note">{L("Draft for Glad Accountancy to review. It updates the current notice to UK GDPR wording.", "供 Glad Accountancy 審閱的草稿，已按英國 UK GDPR 的用語更新。")}</p>
{body}
</main>
'''


def page_404(prefix, pg):
    return f'''<main id="main" class="wrap nf">
<div aria-hidden="true">{sign("此路不通", "No Through Road", None, "sign-xl")}</div>
<h1>{L("This page isn't here", "找不到這一頁")}</h1>
<p class="lede">{L("The link may be old. Try the homepage or send us a WhatsApp message.", "連結可能已經過時，請返回主頁或以 WhatsApp 聯絡我們。")}</p>
<p class="btns"><a class="btn btn-ink" href="{pg}index.html">{L("Homepage", "主頁")}</a><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp</a></p>
</main>
'''


PAGES = [
    ("index.html", page_home, lambda: L("Glad Accountancy | Hong Kong chartered accountants in Altrincham", "Glad Accountancy｜Altrincham 香港會計師行"),
     lambda: L("Accounts, tax, VAT, payroll and Self Assessment for small enterprises, from Hong Kong chartered accountants on Manchester Road, Altrincham.", "香港特許會計師在 Altrincham 為小企業處理會計、稅務、增值稅、薪俸及自我評稅。"), "hk-tram.webp"),
    ("services.html", page_services, lambda: L("Services | Glad Accountancy", "服務範圍｜Glad Accountancy"),
     lambda: L("Accounting, reporting, tax and VAT, payroll and Self Assessment.", "會計、財務報告、稅務及增值稅、薪俸及自我評稅。"), "mong-kok-neon.webp"),
    ("contact.html", page_contact, lambda: L("Contact | Glad Accountancy", "聯絡｜Glad Accountancy"),
     lambda: L("WhatsApp 07769 391052 or visit Office 5, 197 Manchester Road, Altrincham.", "WhatsApp 07769 391052，或到訪 Altrincham 曼徹斯特道 197 號 5 室。"), None),
    ("privacy.html", page_privacy, lambda: L("Privacy | Glad Accountancy", "私隱政策｜Glad Accountancy"),
     lambda: L("How Glad Accountancy uses personal data.", "Glad Accountancy 如何使用個人資料。"), None),
]


def build():
    global LANG
    for code, d, _, _ in LANGS:
        LANG = code
        prefix = "../" if d else ""
        out_dir = os.path.join(ROOT, d)
        os.makedirs(out_dir, exist_ok=True)
        for slug, fn, title, desc, hero in PAGES:
            html = head(prefix, slug, title(), desc(), hero) + header(prefix, "", slug) + fn(prefix, "") + footer(prefix, "", slug)
            open(os.path.join(out_dir, slug), "w", encoding="utf-8").write(html)
    # 404 at root, English, with absolute-from-root links so it works at any depth
    LANG = "en"
    p = "/gladacc/"
    html = head(p, "404.html", "Page not found | Glad Accountancy", "Page not found.") + header(p, p, "404.html") + page_404(p, p) + footer(p, p, "404.html")
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(html)
    print("built")


if __name__ == "__main__":
    build()
