"""
Generates EN and BN versions of every internal page.

Architecture
------------
- EN pages live at /<slug>/index.html  (depth 1, prefix "../")
- BN pages live at /bn/<slug>/index.html (depth 2, prefix "../../")
- Lang switcher on each page links to its counterpart (not to home).
- Brand tokens (Jaya9, Joya9, Jaya 9, Joya 9) are kept Latin in BN copy.

Each page is defined ONCE as a dict with `en` and `bn` content blocks; the
script renders both versions.
"""

from pathlib import Path

ROOT = Path(__file__).parent
SITE = ROOT


# =============================================================================
# HEADER / FOOTER PARTIALS — language-aware
# =============================================================================

def header(active, lang, prefix, switch_target):
    """
    `active` — top-level slug used for highlight (one of: games, live-casino, app, promotion).
    `lang`   — "en" or "bn" — controls labels & active-state of switcher.
    `prefix` — "../" or "../../" depending on page depth.
    `switch_target` — relative URL of the same page in the OTHER language.
    """
    if lang == "bn":
        login_label = "লগইন"
        signup_label = "সাইন আপ"
        nav_games = "গেম"
        nav_live = "লাইভ ক্যাসিনো"
        nav_app = "অ্যাপ"
        nav_promo = "প্রোমোশন"
        sub_referral = "রেফারেল কোড"
        sub_voucher = "ভাউচার কোড"
        sub_bonus = "বোনাস"
        current_lbl, alt_lbl = "BN", "EN"
    else:
        login_label = "Login"
        signup_label = "Sign Up"
        nav_games = "Games"
        nav_live = "Live Casino"
        nav_app = "App"
        nav_promo = "Promotion"
        sub_referral = "Referral Code"
        sub_voucher = "Voucher Code"
        sub_bonus = "Bonus"
        current_lbl, alt_lbl = "EN", "BN"

    p = prefix

    def cls(name):
        return ' class="is-active"' if name == active else ''

    return f'''<!-- ===== HEADER ===== -->
<header class="site-header">
  <div class="container header-inner">
    <a href="{p}" class="logo">
      <img src="{p}images/logo.webp" alt="Jaya9 Bangladesh logo">
    </a>

    <nav class="main-nav">
      <ul>
        <li><a href="{p}games/"{cls('games')}>{nav_games}</a></li>
        <li><a href="{p}live-casino/"{cls('live-casino')}>{nav_live}</a></li>
        <li><a href="{p}app/"{cls('app')}>{nav_app}</a></li>
        <li class="has-dropdown dropdown-right">
          <a href="{p}promotion/" class="dropdown-trigger">
            {nav_promo}
            <svg width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true">
              <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
          <div class="dropdown-menu">
            <a href="{p}referral-code/">{sub_referral}</a>
            <a href="{p}voucher-code/">{sub_voucher}</a>
            <a href="{p}bonus/">{sub_bonus}</a>
          </div>
        </li>
      </ul>
    </nav>

    <div class="header-actions">
      <a href="{switch_target}" class="lang-switch" title="Switch language">
        <span class="lang-current">{current_lbl}</span>
        <span class="lang-divider">/</span>
        <span class="lang-alt">{alt_lbl}</span>
      </a>
      <span class="currency"><span class="flag">🇧🇩</span> BDT</span>
      <a href="{p}login/" class="btn btn-ghost">{login_label}</a>
      <a href="{p}play-now/" rel="nofollow noindex" class="btn btn-primary">{signup_label}</a>
    </div>
  </div>
</header>
'''


def footer(lang, prefix):
    p = prefix
    if lang == "bn":
        labels = {
            "intro": "Jaya9 হলো বাংলাদেশ-কেন্দ্রিক গেমিং প্ল্যাটফর্ম — BDT-তে ক্যাসিনো, লাইভ ডিলার ও ক্রিকেট-ভিত্তিক স্পোর্টস বেটিং, bKash ও Nagad পেআউট এবং ২৪/৭ সাপোর্ট।",
            "casino": "ক্যাসিনো", "games": "গেম", "live": "লাইভ ক্যাসিনো", "app": "মোবাইল অ্যাপ",
            "promo": "প্রোমোশন", "promotion": "প্রোমোশন", "referral": "রেফারেল কোড",
            "voucher": "ভাউচার কোড", "bonus": "বোনাস",
            "account": "অ্যাকাউন্ট", "login": "লগইন", "signup": "সাইন আপ",
            "about": "Jaya9 সম্পর্কে", "about_us": "আমাদের সম্পর্কে",
            "privacy": "প্রাইভেসি পলিসি", "rg": "দায়িত্বশীল জুয়া",
            "footer_text": "© ২০২৬ Jaya9 বাংলাদেশ। দায়িত্বশীলভাবে খেলুন। জুয়া আসক্তিকর হতে পারে — সাহায্যের প্রয়োজন হলে আপনার এলাকার রেস্পন্সিবল-গেমিং সার্ভিসের সাথে যোগাযোগ করুন।",
        }
    else:
        labels = {
            "intro": "Jaya9 is a Bangladesh-focused gaming platform offering casino, live dealers and cricket-led sports betting in BDT, with bKash and Nagad payouts and 24/7 support.",
            "casino": "Casino", "games": "Games", "live": "Live Casino", "app": "Mobile App",
            "promo": "Promotion", "promotion": "Promotion", "referral": "Referral Code",
            "voucher": "Voucher Code", "bonus": "Bonus",
            "account": "Account", "login": "Login", "signup": "Sign Up",
            "about": "About Jaya9", "about_us": "About Us",
            "privacy": "Privacy Policy", "rg": "Responsible Gambling",
            "footer_text": "© 2026 Jaya9 Bangladesh. Play responsibly. Gambling can be addictive — if you need help, contact responsible-gaming services in your area.",
        }

    return f'''<!-- ===== FOOTER ===== -->
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="foot-col foot-brand">
      <img src="{p}images/logo.webp" alt="Jaya9 logo" class="foot-logo">
      <p>{labels["intro"]}</p>
      <div class="foot-pay">
        <span>bKash</span><span>Nagad</span><span>Rocket</span><span>Bank</span><span>USDT</span>
      </div>
    </div>
    <div class="foot-col">
      <h5>{labels["casino"]}</h5>
      <ul>
        <li><a href="{p}games/">{labels["games"]}</a></li>
        <li><a href="{p}live-casino/">{labels["live"]}</a></li>
        <li><a href="{p}app/">{labels["app"]}</a></li>
      </ul>
    </div>
    <div class="foot-col">
      <h5>{labels["promo"]}</h5>
      <ul>
        <li><a href="{p}promotion/">{labels["promotion"]}</a></li>
        <li><a href="{p}referral-code/">{labels["referral"]}</a></li>
        <li><a href="{p}voucher-code/">{labels["voucher"]}</a></li>
        <li><a href="{p}bonus/">{labels["bonus"]}</a></li>
      </ul>
    </div>
    <div class="foot-col">
      <h5>{labels["account"]}</h5>
      <ul>
        <li><a href="{p}login/">{labels["login"]}</a></li>
        <li><a href="{p}play-now/" rel="nofollow noindex">{labels["signup"]}</a></li>
      </ul>
    </div>
    <div class="foot-col">
      <h5>{labels["about"]}</h5>
      <ul>
        <li><a href="{p}about-us/">{labels["about_us"]}</a></li>
        <li><a href="{p}privacy-policy/">{labels["privacy"]}</a></li>
        <li><a href="{p}responsible-gambling/">{labels["rg"]}</a></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">
    <div class="container">
      <span class="age">18+</span>
      <p>{labels["footer_text"]}</p>
    </div>
  </div>
</footer>
'''


PAGE_TPL = '''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="alternate" hreflang="en" href="{en_canonical}">
<link rel="alternate" hreflang="bn" href="{bn_canonical}">
{noindex}<link rel="icon" type="image/x-icon" href="{p}images/favicon.ico">
<link rel="stylesheet" href="{p}css/style.css">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;400;500;600;700;800&family=Hind+Siliguri:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>

{header_html}

<!-- ===== PAGE HERO ===== -->
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{intro}</p>
  </div>
</section>

<!-- ===== TOC ===== -->
<section class="toc-section">
  <div class="container">
    <div class="toc-box">
      <h2 class="toc-title">{toc_title}</h2>
      <ol class="toc-list">
{toc_items}
      </ol>
    </div>
  </div>
</section>

<!-- ===== PROSE ===== -->
<section class="prose-section">
  <div class="container">
    <article class="prose">
{body}
    </article>
  </div>
</section>

{footer_html}

<script src="{p}js/main.js"></script>
</body>
</html>
'''


# =============================================================================
# RENDER HELPERS
# =============================================================================

def fix_links(body, prefix):
    """Replace absolute /play-now/ with relative path for the page's depth."""
    return body.replace('href="/play-now/"', f'href="{prefix}play-now/"')


def render(page, lang):
    """
    Render one (page, lang) → HTML string + write to disk.
    `page` is a dict with both en and bn versions; see PAGES list.
    """
    slug = page["slug"]
    if lang == "bn":
        out_dir = SITE / "bn" / slug
        prefix = "../../"
        switch_target = f"../../{slug}/"   # BN page → EN counterpart
        en_canonical = f"/{slug}/"
        bn_canonical = f"/bn/{slug}/"
        html_lang = "bn"
    else:
        out_dir = SITE / slug
        prefix = "../"
        switch_target = f"../bn/{slug}/"   # EN page → BN counterpart
        en_canonical = f"/{slug}/"
        bn_canonical = f"/bn/{slug}/"
        html_lang = "en"

    out_dir.mkdir(parents=True, exist_ok=True)
    data = page[lang]
    body = fix_links(data["body"], prefix)
    toc_items = "\n".join(
        f'        <li><a href="#{anchor}">{label}</a></li>'
        for anchor, label in data["toc"]
    )

    html = PAGE_TPL.format(
        html_lang=html_lang,
        title=data["title"],
        description=data["description"],
        eyebrow=data["eyebrow"],
        h1=data["h1"],
        intro=data["intro"],
        toc_title=data["toc_title"],
        toc_items=toc_items,
        body=body,
        header_html=header(page.get("active", ""), lang, prefix, switch_target),
        footer_html=footer(lang, prefix),
        noindex='<meta name="robots" content="noindex, nofollow">\n' if page.get("noindex") else '',
        p=prefix,
        en_canonical=en_canonical,
        bn_canonical=bn_canonical,
    )
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    return out_dir


# =============================================================================
# IMAGE FIGURE BLOCKS — reusable inline images. Each page reuses 2 different
# images from the existing /images/ folder (no new images created).
# Path is relative-to-page; pages 1 level deep use ../images/, 2 levels deep ../../images/.
# We use a placeholder {IMG} that page bodies use, then we string-replace per language at render time.
# =============================================================================

# We won't go that fancy — instead each page body literally writes {IMG_BASE}image-name.webp
# and we replace {IMG_BASE} with the right prefix at render time.
# Actually, since fix_links already runs, let's just have body include {IMG} markers we replace.

# Simpler: use a special marker `{IMG}` for the prefix to images/ and substitute at render.

def _swap_img_prefix(body, prefix):
    return body.replace("{IMG}", f"{prefix}images/")


# Replace `render` to also substitute image prefix.
_original_render = render
def render(page, lang):  # noqa: F811
    """Override that also fixes image paths."""
    slug = page["slug"]
    if lang == "bn":
        out_dir = SITE / "bn" / slug
        prefix = "../../"
        switch_target = f"../../{slug}/"
        en_canonical = f"/{slug}/"
        bn_canonical = f"/bn/{slug}/"
        html_lang = "bn"
    else:
        out_dir = SITE / slug
        prefix = "../"
        switch_target = f"../bn/{slug}/"
        en_canonical = f"/{slug}/"
        bn_canonical = f"/bn/{slug}/"
        html_lang = "en"

    out_dir.mkdir(parents=True, exist_ok=True)
    data = page[lang]
    body = fix_links(data["body"], prefix)
    body = _swap_img_prefix(body, prefix)
    toc_items = "\n".join(
        f'        <li><a href="#{anchor}">{label}</a></li>'
        for anchor, label in data["toc"]
    )

    html = PAGE_TPL.format(
        html_lang=html_lang,
        title=data["title"],
        description=data["description"],
        eyebrow=data["eyebrow"],
        h1=data["h1"],
        intro=data["intro"],
        toc_title=data["toc_title"],
        toc_items=toc_items,
        body=body,
        header_html=header(page.get("active", ""), lang, prefix, switch_target),
        footer_html=footer(lang, prefix),
        noindex='<meta name="robots" content="noindex, nofollow">\n' if page.get("noindex") else '',
        p=prefix,
        en_canonical=en_canonical,
        bn_canonical=bn_canonical,
    )
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    return out_dir


# =============================================================================
# PAGES — each entry has en/bn versions
# =============================================================================
PAGES = []

# -----------------------------------------------------------------------------
# PROMOTION
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "promotion",
    "active": "promotion",
    "en": {
        "title": "Jaya9 Promotion — Promo Code Today | Jaya9 Bangladesh",
        "description": "Jaya9 promotion page lists every running offer — IPL cashback, slot reload, VIP deals and the freshest Jaya9 promo code today for Bangladesh players.",
        "eyebrow": "Promotion",
        "h1": "Jaya9 Promotion Today",
        "intro": "Every active Jaya9 promotion in one place — daily offers, promo codes and VIP deals built for Bangladeshi players.",
        "toc_title": "On This Page",
        "toc": [
            ("guide", "Jaya9 Promotion Full Guide"),
            ("today", "Jaya9 Promotion Today"),
            ("how", "How a Jaya9 Promo Code Works"),
            ("best", "Which Promotion Fits You"),
            ("updated", "Stay Updated"),
        ],
        "body": '''      <h2 id="guide">Jaya9 Promotion — Full Guide for Bangladesh Players</h2>
      <p>The Jaya9 promotion page collects every running offer in one feed — casino cashback, IPL sports bonuses, slot reloads, VIP-only drops. The reason it works for Bangladeshi players is mechanical: every promotion is priced in BDT, no dollar or euro conversion sits in the middle, and payouts settle into bKash, Nagad or Rocket. A new Jaya9 promotion gets added almost every day, so regulars who check this page actually find a fresh deal each visit.</p>
      <p>We know players in Bangladesh don't get won over by big words alone — they read the small print. Each Jaya9 promo code therefore comes with the rules attached on the same screen: minimum deposit, rollover, max withdrawal. Nothing is hidden. If a particular offer doesn't fit your account, the live chat team is online 24/7 in both Bangla and English to walk you through the alternatives.</p>
      <figure class="prose-figure">
        <img src="{IMG}hero-cricket.webp" alt="Jaya9 promotion hero — cricket trophy">
        <figcaption>IPL season is when the deepest Jaya9 promotion stack lands.</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>New player?</strong> Sign up today and grab a ৳1000 free credit on your first deposit.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Join Now</a>
      </div>

      <h2 id="today">Jaya9 Promotion Today — What's Live Right Now</h2>
      <p>Every morning the operations team refreshes the Jaya9 promotion today board. Whatever time you load this page, the codes below are the ones currently active. The list isn't only IPL-driven either — every major cricket window (BPL, T20 World Cup, BCB internationals) gets its own cashback line, and football, kabaddi and tennis carry daily deals year-round.</p>
      <p>The most-redeemed Jaya9 promotion code values are listed in the table below, with their conditions and ceilings. Drop the code into the "Bonus Code" field on the cashier page to activate. The same code can only be used once per account, but codes from different categories stack — you can run a slot reload while a cricket cashback is open.</p>
      <table>
        <thead>
          <tr><th>Promo Code</th><th>Offer</th><th>Max Amount</th><th>Rollover</th></tr>
        </thead>
        <tbody>
          <tr><td>WELCOME1000</td><td>৳1000 free on first deposit</td><td>৳1000</td><td>10x</td></tr>
          <tr><td>IPL10</td><td>IPL cricket cashback 10%</td><td>৳5,000 / day</td><td>3x</td></tr>
          <tr><td>SLOT100</td><td>Slot reload 100% match</td><td>৳10,000</td><td>25x</td></tr>
          <tr><td>LIVE50</td><td>Live dealer 50% match</td><td>৳5,000</td><td>15x</td></tr>
          <tr><td>WEEKEND25</td><td>Weekend reload 25%</td><td>৳3,000</td><td>20x</td></tr>
        </tbody>
      </table>

      <h2 id="how">How a Jaya9 Promo Code Works</h2>
      <p>Each Jaya9 promo code is tied to a specific offer in the back-end. When you drop the string into the cashier and confirm, the system reads which promotion you mean and stages the bonus against your next deposit. The flow is simple enough that a first-time user can follow it without guidance, but if a code refuses to attach, live chat will sort it in under five minutes.</p>
      <p>The rules are short. Your account has to be verified, your deposit has to clear the minimum for the offer, and you have to finish the rollover inside the time window. Players who want regular code drops can sign up for the Telegram channel or the WhatsApp broadcast list — fresh codes go out weekly, and VIP members get exclusive ones that never make it to public channels.</p>
      <figure class="prose-figure">
        <img src="{IMG}pop-fortunetiger.webp" alt="Fortune Tiger slot — popular Jaya9 promotion target">
        <figcaption>Slot-specific Jaya9 promotion codes work best on Pragmatic and PG Soft titles.</figcaption>
      </figure>
      <ul>
        <li><strong>Transparent terms</strong> — every Jaya9 promotion code lists its full rules in plain language.</li>
        <li><strong>Fast credit</strong> — bonus lands in your wallet the moment your deposit confirms.</li>
        <li><strong>Stackable</strong> — codes from different verticals (slots + cricket) can run together.</li>
        <li><strong>Verified account</strong> — clear KYC before claiming and you'll save yourself a withdrawal headache.</li>
      </ul>

      <h2 id="best">Which Promotion Fits Your Style</h2>
      <p>The same offer doesn't suit everyone. If cricket betting is your main thing, IPL cashback and the BPL boost will pay out best. Slot players are better served by reload bonuses and free-spin packs. Live dealer fans should look for the dedicated Andar Bahar and Teen Patti match offers. The list below maps player types to the categories that actually move money for them.</p>
      <ol>
        <li>Cricket bettors → IPL10, BPL cashback, live cricket boost</li>
        <li>Slot players → SLOT100, free-spin packs, provider-specific reloads</li>
        <li>Live casino fans → LIVE50, Andar Bahar match offers</li>
        <li>High-rollers → VIP birthday, personal manager pack</li>
        <li>Weekend players → WEEKEND25, Friday–Saturday specials</li>
      </ol>

      <h2 id="updated">Stay Updated</h2>
      <p>The Jaya9 promotion page refreshes daily, but you don't want to miss the special drops either. The right move is to flip on SMS and email notifications inside your account settings — that way exclusive Jaya9 promo code drops, including the VIP-only ones that never get listed publicly, hit your inbox the moment they go live. Sign up today and the active Jaya9 promotion today is already waiting.</p>
      <div class="prose-cta">
        <p>Don't miss today's deals — <strong>Jaya9 promotion today</strong> is live now.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Claim Promotion</a>
      </div>''',
    },
    "bn": {
        "title": "Jaya9 প্রোমোশন — আজকের প্রোমো কোড | Jaya9 বাংলাদেশ",
        "description": "Jaya9 promotion পেজে আজকের সব Jaya9 promo code এবং চলমান অফার — IPL ক্যাশব্যাক, স্লট রিলোড এবং VIP বোনাস বাংলাদেশের প্লেয়ারদের জন্য।",
        "eyebrow": "প্রোমোশন",
        "h1": "Jaya9 Promotion Today",
        "intro": "বাংলাদেশের প্লেয়ারদের জন্য চলমান প্রতিটি Jaya9 promotion এক জায়গায় — দৈনিক অফার, প্রোমো কোড এবং VIP ডিল।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("guide", "Jaya9 Promotion পূর্ণ গাইড"),
            ("today", "Jaya9 Promotion Today"),
            ("how", "Jaya9 Promo Code কীভাবে কাজ করে"),
            ("best", "কোন প্রোমোশন আপনার জন্য"),
            ("updated", "আপডেটেড থাকুন"),
        ],
        "body": '''      <h2 id="guide">Jaya9 Promotion — বাংলাদেশের প্লেয়ারদের জন্য পূর্ণ গাইড</h2>
      <p>Jaya9 promotion পেজে আপনি পাবেন সব চলমান অফার এক জায়গায় — ক্যাসিনো ক্যাশব্যাক থেকে শুরু করে IPL স্পোর্টস বোনাস পর্যন্ত। আমাদের জনপ্রিয়তার মূল কারণ হলো প্রতিটি প্রোমোশন বিডিটিতে গণনা করা হয়, কোনো ডলার বা ইউরো রূপান্তর নেই, এবং উইথড্রয়াল করা যায় bKash, Nagad কিংবা Rocket-এ। প্রতিদিন নতুন একটি Jaya9 promotion যোগ হয়, ফলে নিয়মিত প্লেয়ার যারা এই পেজ চেক করেন তারা সর্বদা একটি লাইভ ডিল দেখতে পান।</p>
      <p>আমরা জানি বাংলাদেশের ইউজাররা শুধু বড় শব্দ দেখে নয়, বরং রিয়েল ভ্যালু দেখে অফার বেছে নেন। সেজন্য প্রতিটি Jaya9 promo code-এর পেছনে স্পষ্ট নিয়ম থাকে — কত ডিপোজিট, কত রোলওভার, কত ম্যাক্স উইথড্রয়াল। কোনো লুকানো শর্ত নেই, প্রতিটি বোনাস টার্ম পেজে বাংলায় ব্যাখ্যা করা থাকে। যদি কোনো অফার আপনার জন্য কাজ না করে, কাস্টমার সাপোর্ট ২৪/৭ লাইভ চ্যাটে আছেন, আপনি বাংলা বা ইংরেজি যেকোনো ভাষায় কথা বলতে পারবেন।</p>
      <figure class="prose-figure">
        <img src="{IMG}hero-cricket.webp" alt="Jaya9 promotion ব্যানার — IPL ট্রফি">
        <figcaption>IPL সিজনে সবচেয়ে গভীর Jaya9 promotion প্যাকেজ আসে।</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>নতুন প্লেয়ার?</strong> আজই সাইন আপ করুন এবং প্রথম ডিপোজিটে ৳১০০০ ফ্রি ক্রেডিট নিন।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">এখনই যুক্ত হোন</a>
      </div>

      <h2 id="today">Jaya9 Promotion Today — আজকের চলমান অফার</h2>
      <p>প্রতিদিন সকালে আমাদের অপারেশন টিম Jaya9 promotion today লিস্ট আপডেট করে। এর মানে হলো আপনি যখনই এই পেজে আসেন, আপনি দেখবেন সেদিনের সক্রিয় বোনাস। শুধু IPL সিজনে নয়, সারা বছর প্রতিটি বড় ক্রিকেট সিরিজ — BPL, T20 World Cup, BCB ইন্টারন্যাশনাল ম্যাচ — সবগুলোর জন্য আলাদা ক্যাশব্যাক প্রোমো রাখা হয়। ফুটবল, কাবাডি এবং টেনিসেও দৈনিক ডিল চালু থাকে।</p>
      <p>আজকের জনপ্রিয় Jaya9 promotion code গুলো নিচের টেবিলে দেওয়া হলো। প্রতিটি কোডের পাশে সংক্ষিপ্ত শর্ত এবং সর্বোচ্চ পরিমাণ উল্লেখ আছে। এই কোডগুলো ক্যাশিয়ার পেজে "Bonus Code" ফিল্ডে বসিয়ে অ্যাকটিভ করতে হয়। মনে রাখবেন, একই অ্যাকাউন্টে একই কোড একবারই কাজ করে — তবে অন্যান্য টাইপের কোড একসাথে চালু রাখা যায়।</p>
      <table>
        <thead>
          <tr><th>প্রোমো কোড</th><th>অফার</th><th>সর্বোচ্চ পরিমাণ</th><th>রোলওভার</th></tr>
        </thead>
        <tbody>
          <tr><td>WELCOME1000</td><td>প্রথম ডিপোজিটে ৳১০০০ ফ্রি</td><td>৳১০০০</td><td>১০x</td></tr>
          <tr><td>IPL10</td><td>IPL ক্রিকেট ক্যাশব্যাক ১০%</td><td>৳৫,০০০ / দিন</td><td>৩x</td></tr>
          <tr><td>SLOT100</td><td>স্লট রিলোড বোনাস ১০০%</td><td>৳১০,০০০</td><td>২৫x</td></tr>
          <tr><td>LIVE50</td><td>লাইভ ডিলার ৫০% ম্যাচ</td><td>৳৫,০০০</td><td>১৫x</td></tr>
          <tr><td>WEEKEND25</td><td>উইকেন্ড রিলোড ২৫%</td><td>৳৩,০০০</td><td>২০x</td></tr>
        </tbody>
      </table>

      <h2 id="how">Jaya9 Promo Code কীভাবে কাজ করে</h2>
      <p>প্রতিটি Jaya9 promo code একটি নির্দিষ্ট অফারের জন্য বানানো হয়। কোডটি ক্যাশিয়ার পেজে দেওয়ার পর সিস্টেম স্বয়ংক্রিয়ভাবে বুঝতে পারে আপনি কোন প্রোমোশন চালু করতে চাইছেন। এরপর আপনি যেই ডিপোজিট করবেন সেটার সাথে বোনাস যুক্ত হয়ে যায়। প্রক্রিয়াটি এতটাই সহজ যে নতুন ইউজাররাও সাহায্য ছাড়াই করতে পারেন। তবে যদি কখনো কোড গ্রহণ না করে, লাইভ চ্যাটে ম্যানেজার আপনাকে দ্রুত সমাধান দিবেন।</p>
      <p>কোড ব্যবহারের প্রধান নিয়মগুলো খুব সরল — অ্যাকাউন্ট ভেরিফাই থাকতে হবে, মিনিমাম ডিপোজিট পূরণ করতে হবে, এবং রোলওভার শর্ত পালন করতে হবে। নিয়মিত প্রোমো কোড পেতে আমাদের টেলিগ্রাম চ্যানেল কিংবা WhatsApp ব্রডকাস্ট লিস্টে যুক্ত থাকতে পারেন। প্রতি সপ্তাহে নতুন কোড পাঠানো হয়, এবং VIP মেম্বাররা পান এক্সক্লুসিভ কোড যা পাবলিকে শেয়ার হয় না।</p>
      <figure class="prose-figure">
        <img src="{IMG}pop-fortunetiger.webp" alt="Fortune Tiger স্লট — Jaya9 promotion এর জনপ্রিয় টার্গেট">
        <figcaption>স্লট-স্পেসিফিক Jaya9 promotion কোড Pragmatic এবং PG Soft টাইটেলে সবচেয়ে ভালো কাজ করে।</figcaption>
      </figure>
      <ul>
        <li><strong>স্বচ্ছ শর্ত</strong> — প্রতিটি Jaya9 promotion code-এর সম্পূর্ণ টার্ম বাংলায় উপলব্ধ।</li>
        <li><strong>দ্রুত ক্রেডিট</strong> — ডিপোজিট নিশ্চিত হওয়ার সাথে সাথে বোনাস ওয়ালেটে যুক্ত হয়।</li>
        <li><strong>একাধিক কোড</strong> — ভিন্ন ক্যাটাগরির কোড একসাথে চালু রাখা যায় (যেমন স্লট + ক্রিকেট)।</li>
        <li><strong>ভেরিফায়েড অ্যাকাউন্ট</strong> — প্রোমো ক্লেইমের আগে KYC সম্পন্ন থাকা ভালো।</li>
      </ul>

      <h2 id="best">কোন প্রোমোশন আপনার জন্য সেরা</h2>
      <p>সবার জন্য একই অফার ভালো হবে না — আপনি যদি ক্রিকেট বেটার হন, আপনার জন্য IPL ক্যাশব্যাক এবং BPL বুস্ট সবচেয়ে লাভজনক। আপনি যদি স্লট প্লেয়ার হন, রিলোড বোনাস এবং ফ্রি স্পিন প্যাক বেছে নেওয়াই বুদ্ধিমানের কাজ। লাইভ ডিলার পছন্দ করেন? তবে Andar Bahar ও Teen Patti টেবিলের জন্য ডেডিকেটেড লাইভ ক্যাসিনো ম্যাচ অফার নিন। নিচের লিস্টে আমরা প্রতিটি প্লেয়ার টাইপের জন্য উপযুক্ত প্রোমো ক্যাটাগরি দেখিয়েছি।</p>
      <ol>
        <li>ক্রিকেট বেটার → IPL10, BPL ক্যাশব্যাক, লাইভ ক্রিকেট বুস্ট</li>
        <li>স্লট প্লেয়ার → SLOT100, ফ্রি স্পিন প্যাক, প্রোভাইডার স্পেসিফিক রিলোড</li>
        <li>লাইভ ক্যাসিনো ফ্যান → LIVE50, Andar Bahar ম্যাচ অফার</li>
        <li>হাই-রোলার → ভিআইপি বার্থডে, পার্সোনাল ম্যানেজার প্যাক</li>
        <li>উইকেন্ড প্লেয়ার → WEEKEND25, শুক্র-শনি বিশেষ ডিল</li>
      </ol>

      <h2 id="updated">আপডেটেড থাকুন</h2>
      <p>Jaya9 promotion পেজ প্রতিদিন রিফ্রেশ হয়, কিন্তু সব অফার মিস করতে চান না নিশ্চয়ই। সেজন্য আমরা সাজেস্ট করি অ্যাকাউন্ট সেটিংসে গিয়ে SMS এবং ইমেইল নোটিফিকেশন অন রাখুন। বিশেষ Jaya9 promo code শুধু রেজিস্টার্ড ইউজারদের কাছে পাঠানো হয়, এবং কিছু কিছু VIP-অনলি কোড লগইন করা অবস্থাতেই দেখা যায়। আজই সাইন আপ করে আজকের সক্রিয় Jaya9 promotion today উপভোগ করুন।</p>
      <div class="prose-cta">
        <p>আজকের ডিল মিস করবেন না — <strong>Jaya9 promotion today</strong> এখনই সক্রিয়।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">প্রোমো ক্লেইম করুন</a>
      </div>''',
    },
})


# -----------------------------------------------------------------------------
# REFERRAL CODE
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "referral-code",
    "active": "promotion",
    "en": {
        "title": "Jaya9 Referral Code Free Today | Referral Bonus Bangladesh",
        "description": "Get today's Jaya9 referral code free and earn a Jaya9 referral bonus on every sign-up. Full guide for Bangladeshi players.",
        "eyebrow": "Referral",
        "h1": "Jaya9 Referral Code",
        "intro": "Invite your friends with a Jaya9 referral code today and earn lifetime commission on every active player they bring.",
        "toc_title": "On This Page",
        "toc": [
            ("intro", "What Is a Jaya9 Referral Code"),
            ("free", "Jaya9 Referral Code Free"),
            ("bonus", "Jaya9 Referral Bonus"),
            ("tips", "Tips for Successful Referrals"),
            ("start", "Get Started Today"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Referral Code — Earn by Inviting Friends</h2>
      <p>The Jaya9 referral code is the unique string assigned to every account the moment it's created. When a friend uses your code at sign-up, both of you collect — they get a starter perk, and you collect an ongoing Jaya9 referral bonus on their activity. It's the closest thing to a passive income built into a casino account, and it's the reason a lot of Bangladeshi players treat Jaya9 not just as a place to play, but as a side earner they run from their phone.</p>
      <p>Looking for a Jaya9 referral code today? Yours is already waiting — sign in and you'll find it under your profile menu. You can also generate a personalized link that bakes the code into the URL automatically. Drop that link into WhatsApp, Facebook, Telegram or IMO, and every successful sign-up turns into commission. Rates start at 15% and climb to 40% at the VIP affiliate tier.</p>
      <figure class="prose-figure">
        <img src="{IMG}app-phone.webp" alt="Jaya9 mobile app — share your referral code anywhere">
        <figcaption>Your Jaya9 referral code lives inside the app's profile menu — copy and share in seconds.</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>Get started now</strong> — sign up to claim your free Jaya9 referral code.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Generate My Code</a>
      </div>

      <h2 id="free">Jaya9 Referral Code Free — How to Get One</h2>
      <p>"Jaya9 referral code free" means exactly what it sounds like: there's no fee, no upgrade, nothing to unlock. Open an account, verify the basics, and your referral code is live the same minute. Because it's free, there's also no cap — you can invite as many friends as you want, and every successful sign-up adds commission to your affiliate balance, which you can withdraw whenever you like.</p>
      <p>Players often ask how many referrals they need to bring before commission becomes meaningful. The honest answer: more active referrals matter far more than more total referrals. The tier table below shows how the rate climbs as your active player count grows, so you can target a specific level rather than chase volume blindly.</p>
      <table>
        <thead>
          <tr><th>Tier</th><th>Active Referrals</th><th>Commission Rate</th><th>Weekly Cap</th></tr>
        </thead>
        <tbody>
          <tr><td>Bronze</td><td>1–4 players</td><td>15%</td><td>৳50,000</td></tr>
          <tr><td>Silver</td><td>5–14 players</td><td>20%</td><td>৳1,50,000</td></tr>
          <tr><td>Gold</td><td>15–34 players</td><td>25%</td><td>৳3,50,000</td></tr>
          <tr><td>Platinum</td><td>35–74 players</td><td>30%</td><td>৳6,00,000</td></tr>
          <tr><td>Diamond VIP</td><td>75+ players</td><td>40%</td><td>৳9,99,999</td></tr>
        </tbody>
      </table>

      <h2 id="bonus">Jaya9 Referral Bonus — Where the Money Comes From</h2>
      <p>Your Jaya9 referral bonus arrives in two layers. The first is an instant signing bonus — the moment your friend completes their first deposit, ৳200 lands in your wallet. The second layer is the revenue share, paid weekly: a percentage of everything your invited player wagers comes back to you for as long as they stay active. The second layer is where the real money lives, because an active cricket bettor places a lot of bets across a season.</p>
      <p>If your invited player upgrades to VIP, your commission rate rises with them. That's why it's worth being selective about who you share your Jaya9 referral code today with — one genuine cricket fan or slot regular pays out more than ten dormant accounts. Lifetime commission means as long as they keep playing, you keep earning, which is exactly what makes this program different from one-shot referral payouts at other brands.</p>
      <figure class="prose-figure">
        <img src="{IMG}sports-cricket.webp" alt="Cricket sports betting — fertile ground for Jaya9 referral bonus">
        <figcaption>Cricket bettors are the most valuable referrals — they generate consistent activity all season.</figcaption>
      </figure>
      <ul>
        <li><strong>Lifetime commission</strong> — as long as your referral stays active, you keep earning.</li>
        <li><strong>Fast payouts</strong> — auto-credited every Monday morning.</li>
        <li><strong>No cap on referrals</strong> — invite as many players as you want, no upper limit.</li>
        <li><strong>Real-time dashboard</strong> — every click and conversion shows up in your affiliate panel.</li>
      </ul>

      <h2 id="tips">Tips for Successful Referrals</h2>
      <p>Anyone can copy and paste a code, but the players who actually convert are the ones who frame it well. The successful affiliates don't just dump links — they explain the bonus value, share screenshots of their own wins, and answer questions from prospects in DMs. Most importantly, they target friends who already follow cricket or play casual casino games, not random contacts.</p>
      <ol>
        <li>Share inside WhatsApp groups where cricket discussion already happens.</li>
        <li>Post Telegram messages with your Jaya9 referral code free plus a screenshot.</li>
        <li>Drop your code into Facebook stories alongside a recent win.</li>
        <li>Avoid YouTube comment sections — they're treated as spam and may get the link banned.</li>
      </ol>

      <h2 id="start">Get Started Today</h2>
      <p>Setting up your Jaya9 referral code takes under sixty seconds. Sign up, open your profile, copy the code, share it — and wait for your first commission to land. Bangladeshi affiliates running this program seriously pull anywhere from ৳50,000 to ৳3,00,000 a month, and that's only the public tier. Get in early and grow your network alongside the platform.</p>''',
    },
    "bn": {
        "title": "Jaya9 Referral Code Free Today | রেফারেল বোনাস বাংলাদেশ",
        "description": "আজকের Jaya9 referral code free পান এবং প্রতিটি ইনভাইটে Jaya9 referral bonus অর্জন করুন। বাংলাদেশের প্লেয়ারদের জন্য পূর্ণ গাইড।",
        "eyebrow": "রেফারেল",
        "h1": "Jaya9 Referral Code",
        "intro": "বন্ধুদের ইনভাইট করুন এবং প্রতিটি Jaya9 referral code today থেকে লাইফটাইম কমিশন আয় করুন।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("intro", "Jaya9 Referral Code কী"),
            ("free", "Jaya9 Referral Code Free"),
            ("bonus", "Jaya9 Referral Bonus"),
            ("tips", "সফল রেফারেলের টিপস"),
            ("start", "আজই শুরু করুন"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Referral Code — বন্ধুদের রেফার করে আয় করুন</h2>
      <p>Jaya9 referral code হলো আপনার ইউনিক কোড যা প্রতিটি অ্যাকাউন্টে অটোমেটিকভাবে তৈরি হয়। আপনার বন্ধু যদি সাইন আপের সময় এই কোড ব্যবহার করেন, তবে তিনি তো বটেই, আপনিও পাবেন একটি বিশেষ Jaya9 referral bonus। এটা একটি win-win সিস্টেম — দুজনেই লাভবান হন। বাংলাদেশের প্লেয়ারদের মধ্যে এই রেফারেল প্রোগ্রাম খুবই জনপ্রিয়, কারণ এর মাধ্যমে শুধুমাত্র খেলেই নয়, সোশ্যাল নেটওয়ার্ক ব্যবহার করেও নিয়মিত আয় করা সম্ভব।</p>
      <p>আজকের Jaya9 referral code today খুঁজছেন? আপনার নিজের কোডটি লগইনের পর প্রোফাইল মেনুতে গিয়ে কপি করতে পারেন। আপনি চাইলে পার্সোনালাইজড লিংকও জেনারেট করতে পারেন যেটাতে কোডটি অটোমেটিক যুক্ত থাকে। এই লিংক WhatsApp, Facebook, Telegram অথবা IMO-তে শেয়ার করুন, এবং প্রতিটি সফল সাইনআপের জন্য কমিশন পান। কমিশন রেট ১৫% থেকে শুরু হয়ে VIP লেভেলে ৪০% পর্যন্ত পৌঁছাতে পারে।</p>
      <figure class="prose-figure">
        <img src="{IMG}app-phone.webp" alt="Jaya9 মোবাইল অ্যাপ — যেকোনো জায়গায় রেফারেল কোড শেয়ার করুন">
        <figcaption>আপনার Jaya9 referral code অ্যাপের প্রোফাইল মেনুতে আছে — কপি করে সেকেন্ডে শেয়ার করুন।</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>এখনই শুরু করুন</strong> — সাইন আপ করে আপনার ফ্রি Jaya9 referral code পান।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">কোড জেনারেট করুন</a>
      </div>

      <h2 id="free">Jaya9 Referral Code Free — কীভাবে পাবেন</h2>
      <p>Jaya9 referral code free মানে হলো এই কোড পাওয়ার জন্য আপনাকে কোনো অতিরিক্ত পেমেন্ট করতে হবে না। শুধু একটি অ্যাকাউন্ট খুলুন, প্রোফাইল ভেরিফাই করুন, এবং আপনার রেফারেল কোড সাথে সাথে অ্যাকটিভ হয়ে যাবে। যেহেতু কোডটি ফ্রি, আপনি যত খুশি তত বন্ধুকে ইনভাইট করতে পারেন — কোনো লিমিট নেই। প্রতিটি সফল ইনভাইটে আপনার অ্যাফিলিয়েট ব্যালেন্সে কমিশন যুক্ত হয়, যা আপনি যেকোনো সময় উইথড্র করতে পারেন।</p>
      <p>অনেক ইউজার প্রশ্ন করেন — বন্ধুকে কতবার ইনভাইট করলে কত কমিশন পাব? উত্তরটা সরল: যত বেশি একটিভ প্লেয়ার ইনভাইট করবেন, তত বেশি আপনার টিয়ার লেভেল উপরে যাবে এবং কমিশন রেট বাড়বে। নিচের টেবিলে আমরা প্রতিটি টিয়ার অনুযায়ী কমিশন স্ট্রাকচার দেখিয়েছি যাতে আপনি বুঝতে পারেন কোন লক্ষ্যে এগোচ্ছেন।</p>
      <table>
        <thead>
          <tr><th>টিয়ার</th><th>সক্রিয় রেফারেল</th><th>কমিশন রেট</th><th>সাপ্তাহিক সর্বোচ্চ</th></tr>
        </thead>
        <tbody>
          <tr><td>Bronze</td><td>১–৪ জন</td><td>১৫%</td><td>৳৫০,০০০</td></tr>
          <tr><td>Silver</td><td>৫–১৪ জন</td><td>২০%</td><td>৳১,৫০,০০০</td></tr>
          <tr><td>Gold</td><td>১৫–৩৪ জন</td><td>২৫%</td><td>৳৩,৫০,০০০</td></tr>
          <tr><td>Platinum</td><td>৩৫–৭৪ জন</td><td>৩০%</td><td>৳৬,০০,০০০</td></tr>
          <tr><td>Diamond VIP</td><td>৭৫+ জন</td><td>৪০%</td><td>৳৯,৯৯,৯৯৯</td></tr>
        </tbody>
      </table>

      <h2 id="bonus">Jaya9 Referral Bonus — কোথায় পাবেন</h2>
      <p>প্রতিটি সফল রেফারেলের জন্য Jaya9 referral bonus দুই ধাপে আসে। প্রথম ধাপ হলো ইনস্ট্যান্ট বোনাস — আপনার বন্ধু প্রথম ডিপোজিট করার সাথে সাথে আপনি পান একটি ফিক্সড ৳২০০ ক্যাশ। দ্বিতীয় ধাপ হলো রিভেনিউ শেয়ার — আপনার রেফার করা প্লেয়ার যত খেলবেন, তার একটি অংশ প্রতি সপ্তাহে আপনার অ্যাকাউন্টে আসবে। এই দ্বিতীয় ধাপটাই বড় টাকা আনে, কারণ একজন একটিভ ক্রিকেট বেটার মাসে অনেক বার বেট করেন।</p>
      <p>রেফার করা প্লেয়ার যদি VIP হয়ে যান, তবে আপনার কমিশনও বাড়ে। এজন্যই Jaya9 referral code today শেয়ার করার সময় এমন বন্ধুদের বেছে নিন যারা সত্যিই খেলায় আগ্রহী, কারণ এক একটিভ প্লেয়ার দশ ইনঅ্যাক্টিভ প্লেয়ারের চেয়ে বেশি আয় এনে দেন। লাইফটাইম কমিশন মানে যতদিন তারা একটিভ থাকবেন, ততদিন আপনি পাচ্ছেন রেগুলার কমিশন — এটাই সবচেয়ে আকর্ষণীয় দিক।</p>
      <figure class="prose-figure">
        <img src="{IMG}sports-cricket.webp" alt="ক্রিকেট স্পোর্টস বেটিং — Jaya9 referral bonus এর সবচেয়ে ভাল ক্ষেত্র">
        <figcaption>ক্রিকেট বেটাররা সবচেয়ে মূল্যবান রেফারেল — তারা সারা সিজনে নিয়মিত একটিভিটি জেনারেট করেন।</figcaption>
      </figure>
      <ul>
        <li><strong>লাইফটাইম কমিশন</strong> — যতদিন আপনার রেফারেল একটিভ, ততদিন আপনি কমিশন পান।</li>
        <li><strong>দ্রুত পেআউট</strong> — প্রতি সোমবার সকালে অটোমেটিক ক্রেডিট হয়।</li>
        <li><strong>কোনো ক্যাপ নেই</strong> — যত খুশি প্লেয়ার ইনভাইট করুন, কোনো সর্বোচ্চ সংখ্যা নেই।</li>
        <li><strong>রিয়েল-টাইম ড্যাশবোর্ড</strong> — আপনার অ্যাফিলিয়েট প্যানেলে প্রতিটি ক্লিক ও কনভার্সন দেখা যায়।</li>
      </ul>

      <h2 id="tips">সফল রেফারেলের জন্য টিপস</h2>
      <p>সবাই কোড শেয়ার করতে পারে, কিন্তু সবাই একই রকম রেজাল্ট পায় না। সফল রেফারাররা কয়েকটি জিনিস ভিন্নভাবে করেন — তারা শুধু লিংক পোস্ট করেই থামেন না, বরং বোনাসের সুবিধা ব্যাখ্যা করে দেখান, স্ক্রিনশট শেয়ার করেন, এবং সম্ভাব্য প্লেয়ারদের প্রশ্নের উত্তর দেন। সবচেয়ে গুরুত্বপূর্ণ — তারা শুধু ক্রিকেট ফ্যান বা ক্যাসিনো প্লেয়ার বন্ধুদের টার্গেট করেন, র‌্যান্ডম ইউজারদের নয়।</p>
      <ol>
        <li>WhatsApp গ্রুপে শেয়ার করুন যেখানে ক্রিকেট আলোচনা হয়।</li>
        <li>Telegram-এ Jaya9 referral code free বার্তা সহ স্ক্রিনশট দিন।</li>
        <li>Facebook স্টোরিতে আপনার সাম্প্রতিক উইন শেয়ার করুন কোড সহ।</li>
        <li>YouTube কমেন্ট সেকশন এড়িয়ে চলুন — এটা স্প্যাম হিসেবে ব্যান হতে পারে।</li>
      </ol>

      <h2 id="start">আজই শুরু করুন</h2>
      <p>আপনার Jaya9 referral code পেতে ৬০ সেকেন্ডও লাগে না। সাইন আপ করুন, প্রোফাইলে যান, কোড কপি করুন, শেয়ার করুন — এবং অপেক্ষা করুন আপনার প্রথম কমিশনের জন্য। বাংলাদেশের অনেক প্লেয়ার এই প্রোগ্রাম দিয়ে মাসে ৫০ হাজার থেকে ৩ লাখ টাকা পর্যন্ত আয় করছেন। আপনিও যুক্ত হোন এই গ্রোয়িং নেটওয়ার্কে।</p>''',
    },
})


# -----------------------------------------------------------------------------
# VOUCHER CODE
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "voucher-code",
    "active": "promotion",
    "en": {
        "title": "Jaya9 Voucher Code Free Today | Joya 9 Voucher Bangladesh",
        "description": "Today's Jaya9 voucher code free and joya 9 voucher code today — free credit, free spins and VIP voucher drops for Bangladeshi players.",
        "eyebrow": "Voucher",
        "h1": "Jaya9 Voucher Code Today",
        "intro": "Every Jaya9 voucher code in one place — free credit, free spins and VIP gifts, refreshed daily.",
        "toc_title": "On This Page",
        "toc": [
            ("intro", "Jaya9 Voucher Code Overview"),
            ("free", "Jaya9 Voucher Code Free"),
            ("claim", "Jaya9 Claim Voucher Code"),
            ("today", "Voucher Free Today"),
            ("register", "Sign Up to Use Vouchers"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Voucher Code — The Best Deals for Bangladesh</h2>
      <p>A Jaya9 voucher code is a special alphanumeric string you drop into the cashier to unlock extra bonus or free credit. The difference between a voucher and a regular promo code is that vouchers are usually targeted — issued to specific user groups or events. Plenty of players also search for a joya 9 voucher code, which is the same thing under a different brand spelling. Bangladeshi players use both spellings, and the system recognizes both.</p>
      <p>Internally we run two voucher categories: public and private. Public vouchers go out on our social channels and anyone can redeem them. Private vouchers are issued to VIPs, birthday celebrations or specific events, and they're single-use. Both types carry an expiry, so leaving them sitting in your inbox too long means losing them.</p>
      <figure class="prose-figure">
        <img src="{IMG}slot-1.webp" alt="Sweet Bonanza slot — frequent Jaya9 voucher target">
        <figcaption>Slot vouchers from Pragmatic Play hit your account during big game launches.</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>Want today's free voucher?</strong> Open your account and claim your bonus.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Claim Now</a>
      </div>

      <h2 id="free">Jaya9 Voucher Code Free — How to Get One</h2>
      <p>The easiest way to land a Jaya9 voucher code free is to plug into our official channels. Fresh vouchers post to the Telegram channel every morning, and during big events Facebook and the WhatsApp broadcast list pick up the rest. Many players type "joya 9 voucher code free" into Google — bookmark this page if that's you, because we refresh the listings here daily.</p>
      <p>A smarter move is to switch on SMS and email notifications inside your account settings. The system reads your play pattern and sends personalized vouchers — heavy cricket bettors get IPL-window sport vouchers, slot regulars pick up provider-specific drops at game launches. Each code lands relevant to how you actually play, instead of the same generic blast everyone gets.</p>
      <table>
        <thead>
          <tr><th>Voucher Code</th><th>Denomination</th><th>Use</th><th>Validity</th></tr>
        </thead>
        <tbody>
          <tr><td>VIP500</td><td>৳500 free credit</td><td>One per account</td><td>7 days</td></tr>
          <tr><td>FREESPIN50</td><td>50 free spins</td><td>Pragmatic slots</td><td>3 days</td></tr>
          <tr><td>CRICKET200</td><td>৳200 sports credit</td><td>Cricket bets</td><td>5 days</td></tr>
          <tr><td>BIRTHDAY1K</td><td>৳1000 birthday gift</td><td>VIP members</td><td>14 days</td></tr>
          <tr><td>WEEKEND300</td><td>৳300 weekend boost</td><td>Fri–Sun</td><td>3 days</td></tr>
        </tbody>
      </table>

      <h2 id="claim">Jaya9 Claim Voucher Code — Step-by-Step</h2>
      <p>The Jaya9 claim voucher code flow is short, but for first-time users we'll spell it out anyway. Sign in. Tap "Deposit" or "Cashier" in the top-right of your account. Scroll to the bottom of the cashier screen — there's a field labelled "Voucher Code" or "Bonus Code." Paste your code, hit Apply. The system validates the code and posts the bonus to your wallet.</p>
      <p>Bear in mind every Jaya9 voucher code today comes with its own conditions. Some attach to a deposit, some give straight free credit, some only work on certain game categories. Before you apply a code, run through the checklist below — it covers the four issues that account for nearly every voucher rejection. Get those right and the apply step is a one-tap action.</p>
      <figure class="prose-figure">
        <img src="{IMG}pop-aviator.webp" alt="Aviator crash game — popular voucher destination">
        <figcaption>Cricket-window vouchers stack neatly against fast-round titles like Aviator.</figcaption>
      </figure>
      <ul>
        <li><strong>Verified account</strong> — finish KYC before claiming or you'll fight to withdraw later.</li>
        <li><strong>Correct format</strong> — type the code in upper case with no spaces.</li>
        <li><strong>Watch the expiry</strong> — use the voucher before its validity window closes.</li>
        <li><strong>Game restrictions</strong> — read which games each voucher is allowed on.</li>
        <li><strong>Minimum deposit</strong> — meet the floor for the offer or the code won't attach.</li>
      </ul>

      <h2 id="today">Jaya9 Voucher Free Today — Where to Look</h2>
      <p>Plenty of players try to find a Jaya9 voucher free on third-party sites, but those usually carry stale or fake codes. The safer path is to follow the official channels. The list below covers every official source where a Jaya9 voucher code free today is published. Anything else — verify before pasting, because a fake code can flag your account as a fraud risk.</p>
      <ol>
        <li>Official Telegram channel — daily voucher updates</li>
        <li>Profile inbox — personalized codes triggered by your play pattern</li>
        <li>Email notifications — weekly voucher newsletter</li>
        <li>WhatsApp broadcast list — VIP-only premium codes</li>
      </ol>

      <h2 id="register">Sign Up to Use Vouchers</h2>
      <p>Full access to jaya 9 voucher code drops and the broader Jaya9 voucher inventory needs a verified account. Sign up today, claim a welcome voucher on your first deposit, then plug into the regular voucher rotation. Thousands of Bangladeshi players already run this stack and turn the bonus credit into real BDT every week.</p>''',
    },
    "bn": {
        "title": "Jaya9 Voucher Code Free Today | Joya 9 Voucher | বাংলাদেশ",
        "description": "আজকের Jaya9 voucher code free এবং joya 9 voucher code today পান। বাংলাদেশের প্লেয়ারদের জন্য ফ্রি ক্রেডিট, ফ্রি স্পিন এবং VIP voucher।",
        "eyebrow": "ভাউচার",
        "h1": "Jaya9 Voucher Code Today",
        "intro": "ফ্রি ক্রেডিট, ফ্রি স্পিন এবং VIP গিফটের জন্য সব Jaya9 voucher code এক জায়গায় — প্রতিদিন আপডেট।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("intro", "Jaya9 Voucher Code পরিচিতি"),
            ("free", "Jaya9 Voucher Code Free"),
            ("claim", "Jaya9 Claim Voucher Code"),
            ("today", "Voucher Free Today"),
            ("register", "রেজিস্টার করুন"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Voucher Code — বাংলাদেশের প্লেয়ারদের জন্য সেরা ডিল</h2>
      <p>Jaya9 voucher code হলো একটি বিশেষ অ্যালফানিউমেরিক কোড যা ক্যাশিয়ার পেজে বসিয়ে আপনি অতিরিক্ত বোনাস বা ফ্রি ক্রেডিট আনলক করতে পারেন। সাধারণ প্রোমো কোড থেকে এটার পার্থক্য হলো — voucher code প্রায়ই টার্গেটেড হয়, অর্থাৎ নির্দিষ্ট ইউজার গ্রুপ বা নির্দিষ্ট ইভেন্টের জন্য। কিছু লোক একে joya 9 voucher code নামেও খোঁজেন, যেটা মূলত একই জিনিসের উচ্চারণ ভেরিয়েশন। বাংলায় প্লেয়াররা প্রায়ই দুই বানানে সার্চ করেন, তাই আমরা উভয়ই গ্রহণ করি।</p>
      <p>আমাদের সিস্টেমে jaya9 voucher দুই ধরনের — পাবলিক এবং প্রাইভেট। পাবলিক voucher আমাদের সোশ্যাল মিডিয়া চ্যানেলে শেয়ার হয়, যেকেউ ব্যবহার করতে পারেন। প্রাইভেট voucher VIP প্লেয়ার, বার্থডে সেলিব্রেশন, কিংবা বিশেষ ইভেন্টের জন্য ইস্যু হয় এবং একবারই কাজ করে। দুই ক্ষেত্রেই কোডের ভ্যালিডিটি পিরিয়ড থাকে, তাই দেরি করলে এক্সপায়ার হয়ে যেতে পারে।</p>
      <figure class="prose-figure">
        <img src="{IMG}slot-1.webp" alt="Sweet Bonanza স্লট — Jaya9 voucher এর জনপ্রিয় টার্গেট">
        <figcaption>বড় গেম লঞ্চের সময় Pragmatic Play স্লট ভাউচার অ্যাকাউন্টে আসে।</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>আজকের ফ্রি ভাউচার পেতে চান?</strong> অ্যাকাউন্ট খুলে নিন এবং বোনাস ক্লেইম করুন।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">এখনই ক্লেইম করুন</a>
      </div>

      <h2 id="free">Jaya9 Voucher Code Free — কীভাবে পাবেন</h2>
      <p>Jaya9 voucher code free পাওয়ার জন্য সবচেয়ে সহজ উপায় হলো আমাদের অফিসিয়াল কমিউনিটিতে যুক্ত থাকা। প্রতিদিন সকালে Telegram চ্যানেলে নতুন voucher পোস্ট হয়, আবার সাপ্তাহিক বড় ইভেন্টে Facebook এবং WhatsApp ব্রডকাস্ট লিস্টেও কোড পাঠানো হয়। অনেক প্লেয়ার joya 9 voucher code free খোঁজেন গুগলে — এই পেজটি বুকমার্ক করে রাখলে আপনি সবসময় লেটেস্ট কোড পাবেন কারণ আমরা প্রতিদিন এটি আপডেট করি।</p>
      <p>একটি ভাল উপায় হলো আপনার অ্যাকাউন্টে SMS এবং ইমেইল নোটিফিকেশন অন রাখা। তখন সিস্টেম আপনার অ্যাকাউন্টের প্যাটার্ন দেখে পার্সোনালাইজড voucher পাঠাবে। উদাহরণস্বরূপ, আপনি যদি ক্রিকেট বেটিং বেশি করেন, তবে IPL সিজনে স্পোর্টস-স্পেসিফিক voucher পাবেন। আবার স্লট প্লেয়ার হলে নতুন গেম রিলিজের সাথে স্লট voucher পাবেন। এভাবে প্রতিটি কোড আপনার প্লে স্টাইলের সাথে রিলেভেন্ট হয়।</p>
      <table>
        <thead>
          <tr><th>ভাউচার কোড</th><th>ডিনোমিনেশন</th><th>ব্যবহার</th><th>মেয়াদ</th></tr>
        </thead>
        <tbody>
          <tr><td>VIP500</td><td>৳৫০০ ফ্রি ক্রেডিট</td><td>একবার / অ্যাকাউন্ট</td><td>৭ দিন</td></tr>
          <tr><td>FREESPIN50</td><td>৫০টি ফ্রি স্পিন</td><td>Pragmatic স্লট</td><td>৩ দিন</td></tr>
          <tr><td>CRICKET200</td><td>৳২০০ স্পোর্টস ক্রেডিট</td><td>ক্রিকেট বেট</td><td>৫ দিন</td></tr>
          <tr><td>BIRTHDAY1K</td><td>৳১০০০ বার্থডে গিফট</td><td>VIP মেম্বার</td><td>১৪ দিন</td></tr>
          <tr><td>WEEKEND300</td><td>৳৩০০ উইকেন্ড বুস্ট</td><td>শুক্র–রবি</td><td>৩ দিন</td></tr>
        </tbody>
      </table>

      <h2 id="claim">Jaya9 Claim Voucher Code — ধাপে ধাপে গাইড</h2>
      <p>jaya9 claim voucher code প্রক্রিয়া অত্যন্ত সরল, কিন্তু প্রথমবার ইউজারদের জন্য আমরা ধাপে ধাপে দেখাই। প্রথমে আপনার অ্যাকাউন্টে লগইন করুন। তারপর উপরের ডান কোণে "Deposit" বা "Cashier" বাটনে ক্লিক করুন। ক্যাশিয়ার পেজের নিচের দিকে "Voucher Code" বা "Bonus Code" ফিল্ড দেখতে পাবেন। সেখানে আপনার কোডটি বসান এবং "Apply" বাটনে চাপ দিন। সিস্টেম স্বয়ংক্রিয়ভাবে কোডটি ভেরিফাই করবে এবং বোনাস ওয়ালেটে যুক্ত করবে।</p>
      <p>মনে রাখবেন প্রতিটি jaya9 voucher code today আলাদা শর্তে আসে। কিছু কোড শুধু ডিপোজিটের সাথে কাজ করে, কিছু সরাসরি ফ্রি ক্রেডিট দেয়, এবং কিছু শুধু নির্দিষ্ট গেম ক্যাটাগরিতে ব্যবহার করা যায়। কোড অ্যাপ্লাই করার আগে নিচের চেকলিস্ট ফলো করুন যাতে কোনো জটিলতা না হয়। এই কয়েকটি পয়েন্ট মিলিয়ে দেখলে প্রায় সব ক্ষেত্রেই কোড সফলভাবে কাজ করে।</p>
      <figure class="prose-figure">
        <img src="{IMG}pop-aviator.webp" alt="Aviator ক্রাশ গেম — জনপ্রিয় ভাউচার গন্তব্য">
        <figcaption>ক্রিকেট-উইন্ডো ভাউচার Aviator-এর মতো দ্রুত-রাউন্ড টাইটেলে চমৎকার কাজ করে।</figcaption>
      </figure>
      <ul>
        <li><strong>অ্যাকাউন্ট ভেরিফাই</strong> — KYC সম্পন্ন থাকতে হবে।</li>
        <li><strong>সঠিক ফরম্যাট</strong> — কোড বড় হাতের অক্ষরে লিখুন, কোনো স্পেস না।</li>
        <li><strong>মেয়াদ চেক</strong> — voucher এক্সপায়ারের আগে ব্যবহার করুন।</li>
        <li><strong>গেম রেস্ট্রিকশন</strong> — কোড কোন গেমে কাজ করে সেটা পড়ুন।</li>
        <li><strong>একাউন্ট ব্যালেন্স</strong> — প্রয়োজনীয় ডিপোজিট মিনিমাম পূরণ করুন।</li>
      </ul>

      <h2 id="today">Jaya9 Voucher Free Today — কোথায় খুঁজবেন</h2>
      <p>jaya9 voucher free খুঁজতে অনেক প্লেয়ার বিভিন্ন থার্ড-পার্টি ওয়েবসাইটে যান, কিন্তু সেগুলো সাধারণত পুরাতন বা ভুয়া কোড পোস্ট করে। সবচেয়ে নিরাপদ উপায় হলো অফিসিয়াল চ্যানেল ফলো করা। নিচের লিস্টে আমরা সব অফিসিয়াল সোর্স দিয়েছি যেখান থেকে jaya9 voucher code free today পাওয়া যাবে। অন্য কোনো সোর্স থেকে কোড ব্যবহার করার আগে ভেরিফাই করুন কারণ ফেক কোড অ্যাকাউন্ট ব্লকের কারণ হতে পারে।</p>
      <ol>
        <li>অফিসিয়াল Telegram চ্যানেল — দৈনিক voucher আপডেট</li>
        <li>প্রোফাইল মেসেজ ইনবক্স — পার্সোনালাইজড কোড</li>
        <li>ইমেইল নোটিফিকেশন — সাপ্তাহিক ভাউচার নিউজলেটার</li>
        <li>WhatsApp ব্রডকাস্ট লিস্ট — VIP-অনলি প্রিমিয়াম কোড</li>
      </ol>

      <h2 id="register">সম্পূর্ণ সুবিধা নিতে রেজিস্টার করুন</h2>
      <p>jaya 9 voucher code এবং jaya9 voucher সুবিধা সম্পূর্ণ পেতে আপনার একটি ভেরিফায়েড অ্যাকাউন্ট থাকা জরুরি। আজই সাইন আপ করুন, প্রথম ডিপোজিটে welcome voucher পান, এবং তারপর আমাদের নিয়মিত voucher প্রোগ্রামে যুক্ত হোন। বাংলাদেশের হাজারো প্লেয়ার ইতিমধ্যে এই প্রোগ্রাম থেকে ফ্রি বোনাস উপভোগ করছেন।</p>''',
    },
})


# -----------------------------------------------------------------------------
# BONUS
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "bonus",
    "active": "promotion",
    "en": {
        "title": "Jaya9 Bonus | Joya 9 Best Bonus Today | Bangladesh",
        "description": "Jaya9 bonus stack — ৳1000 welcome, IPL cashback, VIP program and the joya 9 best bonus drops for Bangladeshi players.",
        "eyebrow": "Bonus",
        "h1": "Jaya9 Bonus & VIP Program",
        "intro": "From the ৳1000 welcome credit to VIP birthday gifts — every type of jaya 9 best bonus on a single page.",
        "toc_title": "On This Page",
        "toc": [
            ("intro", "Jaya9 Bonus Overview"),
            ("best", "Joya 9 Best Bonus Comparison"),
            ("how", "How to Get the Best Bonus"),
            ("vip", "Joya 9 Bonus VIP Program"),
            ("start", "Claim Your Bonus Today"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Bonus — Bangladesh's Strongest Bonus Stack</h2>
      <p>The Jaya9 bonus stack is widely considered the most generous in the Bangladesh market, and not by accident. We don't stop at a welcome bonus — the ecosystem runs nine separate promotion families, each tailored to a specific player type. Casino players, cricket bettors, live dealer fans, VIP members — every category has its own dedicated bonus track. Plenty of players also know the program as joya 9 bonus, which is the same stack under a different brand spelling.</p>
      <p>Our bonus philosophy is short: every bonus pays out as real money you can wager and withdraw, not locked credit. A lot of casinos run "bonuses" with rollovers no one can actually clear. We took the opposite path — lower rollover, transparent terms, real withdrawable profit. That's how Jaya9 became the brand Bangladeshi players talk about as the jaya 9 best bonus option.</p>
      <figure class="prose-figure">
        <img src="{IMG}pop-jetx.webp" alt="JetX crash game — bonus credit accelerator">
        <figcaption>Crash games are a fast way to clear rollover on bonus credit.</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>৳1000 welcome bonus</strong> waiting now — sign up to claim it.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Claim Bonus</a>
      </div>

      <h2 id="best">Joya 9 Best Bonus — Which One Fits You</h2>
      <p>The same bonus doesn't suit everyone. A casual cricket bettor wants something different from a high-roller slot player. We built the joya 9 best bonus comparison below so you can match your style to a real promotion instead of guessing. The key thing to remember: you can run multiple bonuses at the same time as long as they're in different categories.</p>
      <table>
        <thead>
          <tr><th>Bonus Type</th><th>Max Amount</th><th>Rollover</th><th>Best For</th></tr>
        </thead>
        <tbody>
          <tr><td>Welcome Bonus</td><td>৳20,000</td><td>15x</td><td>New players</td></tr>
          <tr><td>IPL Cashback</td><td>৳5,000 / day</td><td>3x</td><td>Cricket bettors</td></tr>
          <tr><td>Slot Reload</td><td>৳10,000</td><td>25x</td><td>Slot players</td></tr>
          <tr><td>Live Casino Match</td><td>৳5,000</td><td>15x</td><td>Live dealer fans</td></tr>
          <tr><td>VIP Birthday</td><td>৳15,000</td><td>10x</td><td>VIP members</td></tr>
          <tr><td>Weekly Commission</td><td>৳9,99,999</td><td>—</td><td>Affiliates</td></tr>
        </tbody>
      </table>

      <h2 id="how">Jaya 9 Best Bonus — How to Actually Get It</h2>
      <p>Getting the jaya 9 best bonus working for you takes a few habits. First and most important: complete account verification fully — KYC, email confirmation, mobile verification. Players who skip this often discover they can't withdraw bonus winnings later. Second: read each bonus's terms before claiming. Minimum deposit, rollover, max withdrawal, game contribution — all of these matter and they're all listed on the bonus page.</p>
      <p>Third: learn to stack bonuses across categories. As an example, IPL Cashback (a sports promotion) can run alongside a Slot Reload (a casino promotion) without conflict, because they sit on different product lines. What you can't do is run two sports bonuses at once. The list below collects the practical rules every Jaya9 bonus hunter should know before they start chasing the stack.</p>
      <figure class="prose-figure">
        <img src="{IMG}live-roulette.webp" alt="Lightning Roulette — live casino bonus venue">
        <figcaption>Live dealer match bonuses route most cleanly through Lightning Roulette tables.</figcaption>
      </figure>
      <ul>
        <li><strong>Stack across categories</strong> — sports + casino bonuses can run together.</li>
        <li><strong>Track rollover</strong> — your account shows real-time progress on each promotion.</li>
        <li><strong>Provider weighting</strong> — not every slot contributes equally to rollover, check the list.</li>
        <li><strong>Withdrawal limit</strong> — know the max cash-out before you start.</li>
        <li><strong>Time window</strong> — most bonuses give you 7–14 days to clear rollover.</li>
      </ul>

      <h2 id="vip">Joya 9 Bonus — The VIP Program</h2>
      <p>The most exclusive layer of the joya 9 bonus stack is the VIP program. When your monthly turnover crosses a defined threshold, your account auto-upgrades to a VIP tier. VIPs pick up a personal account manager, custom bonus offers, faster withdrawals, and exclusive gifts on birthdays and big events. None of this is published publicly — it's only visible to members who've reached the relevant tier.</p>
      <ol>
        <li>Bronze VIP — ৳50,000 monthly turnover</li>
        <li>Silver VIP — ৳2,00,000 monthly turnover</li>
        <li>Gold VIP — ৳5,00,000 monthly turnover</li>
        <li>Platinum VIP — ৳15,00,000 monthly turnover</li>
        <li>Diamond VIP — ৳50,00,000+ monthly turnover</li>
      </ol>

      <h2 id="start">Claim Your Bonus Today</h2>
      <p>Joining the Jaya9 bonus program isn't complicated — sign up, verify, deposit. Your first deposit alone delivers ৳1000 free credit plus a 100% match. After that, fresh promotions land daily and you pick the ones that suit how you play. The more active you stay, the higher your bonus tier climbs.</p>''',
    },
    "bn": {
        "title": "Jaya9 Bonus | Joya 9 Best Bonus Today | বাংলাদেশ",
        "description": "Jaya9 bonus সিস্টেম — ৳১০০০ ওয়েলকাম, IPL ক্যাশব্যাক, VIP প্রোগ্রাম এবং joya 9 best bonus অফার বাংলাদেশের প্লেয়ারদের জন্য।",
        "eyebrow": "বোনাস",
        "h1": "Jaya9 Bonus ও VIP প্রোগ্রাম",
        "intro": "৳১০০০ ফ্রি থেকে শুরু করে VIP বার্থডে গিফট — সব ধরনের jaya 9 best bonus এক পেজে।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("intro", "Jaya9 Bonus পরিচিতি"),
            ("best", "Joya 9 Best Bonus তুলনা"),
            ("how", "Jaya 9 Best Bonus পেতে"),
            ("vip", "Joya 9 Bonus VIP"),
            ("start", "আজই উপভোগ করুন"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Bonus — বাংলাদেশের সেরা বোনাস প্রোগ্রাম</h2>
      <p>Jaya9 bonus সিস্টেম বাংলাদেশের অনলাইন গেমিং মার্কেটে সবচেয়ে আকর্ষণীয় হিসেবে পরিচিত। আমরা শুধু একটি ওয়েলকাম বোনাসেই থামি না — আমাদের বোনাস ইকোসিস্টেমে আছে নয় ধরনের প্রোমো, যা প্রতিটি প্লেয়ার টাইপের জন্য আলাদা। ক্যাসিনো প্লেয়ার, ক্রিকেট বেটার, লাইভ ডিলার ফ্যান বা VIP মেম্বার — সবার জন্য ডেডিকেটেড বোনাস ক্যাটাগরি আছে। অনেকে এই প্রোগ্রামকে joya 9 bonus নামেও চিনেন, যেটা একই ব্র্যান্ডের আরেকটি বানান।</p>
      <p>আমাদের বোনাস ফিলোসফি খুব সরল — প্রতিটি বোনাস হতে হবে রিয়েল মানি, লকড ক্রেডিট নয়। অনেক ক্যাসিনো বোনাস দেয় ঠিকই, কিন্তু রোলওভার এতই কঠিন যে কেউই সেটা পূরণ করতে পারে না। আমরা বিপরীত পথে গিয়েছি — কম রোলওভার, স্বচ্ছ শর্ত, এবং রিয়েল উইথড্রয়েবল প্রফিট। সেজন্যই বাংলাদেশের প্লেয়ারদের কাছে jaya 9 best bonus হিসেবে পরিচিত।</p>
      <figure class="prose-figure">
        <img src="{IMG}pop-jetx.webp" alt="JetX ক্রাশ গেম — বোনাস ক্রেডিট অ্যাক্সিলারেটর">
        <figcaption>ক্রাশ গেম বোনাস ক্রেডিটে রোলওভার ক্লিয়ার করার দ্রুততম উপায়।</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>৳১০০০ ওয়েলকাম বোনাস</strong> এখনই অপেক্ষা করছে — সাইন আপ করুন।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">বোনাস ক্লেইম করুন</a>
      </div>

      <h2 id="best">Joya 9 Best Bonus — কোনটি আপনার জন্য</h2>
      <p>সব বোনাস সবার জন্য উপযুক্ত নয়। একজন কেজুয়াল ক্রিকেট বেটার যা চান, একজন হাই-রোলার স্লট প্লেয়ার তা চান না। সেজন্য আমরা joya 9 best bonus গাইড বানিয়েছি যেখানে প্রতিটি প্লেয়ার টাইপের জন্য আলাদা সাজেশন আছে। নিচের তুলনামূলক টেবিল দেখুন এবং নিজের জন্য সবচেয়ে উপযুক্তটা বেছে নিন। মনে রাখবেন আপনি একসাথে একাধিক বোনাস ব্যবহার করতে পারেন যদি সেগুলো ভিন্ন ক্যাটাগরির হয়।</p>
      <table>
        <thead>
          <tr><th>বোনাস টাইপ</th><th>সর্বোচ্চ পরিমাণ</th><th>রোলওভার</th><th>উপযুক্ত</th></tr>
        </thead>
        <tbody>
          <tr><td>Welcome Bonus</td><td>৳২০,০০০</td><td>১৫x</td><td>নতুন প্লেয়ার</td></tr>
          <tr><td>IPL Cashback</td><td>৳৫,০০০ / দিন</td><td>৩x</td><td>ক্রিকেট বেটার</td></tr>
          <tr><td>Slot Reload</td><td>৳১০,০০০</td><td>২৫x</td><td>স্লট প্লেয়ার</td></tr>
          <tr><td>Live Casino Match</td><td>৳৫,০০০</td><td>১৫x</td><td>লাইভ ডিলার ফ্যান</td></tr>
          <tr><td>VIP Birthday</td><td>৳১৫,০০০</td><td>১০x</td><td>VIP মেম্বার</td></tr>
          <tr><td>Weekly Commission</td><td>৳৯,৯৯,৯৯৯</td><td>—</td><td>অ্যাফিলিয়েট</td></tr>
        </tbody>
      </table>

      <h2 id="how">Jaya 9 Best Bonus পেতে কী করবেন</h2>
      <p>jaya 9 best bonus পেতে কয়েকটি স্টেপ ফলো করতে হবে। প্রথম এবং সবচেয়ে গুরুত্বপূর্ণ হলো অ্যাকাউন্ট পুরোপুরি ভেরিফাই করা — KYC, ইমেইল কনফার্মেশন, এবং মোবাইল ভেরিফিকেশন। অনেক প্লেয়ার এই স্টেপ এড়িয়ে যান এবং পরে দেখেন বোনাস উইথড্র করতে পারছেন না। দ্বিতীয়ত, প্রতিটি বোনাসের টার্ম পেজ ভালোভাবে পড়ুন — মিনিমাম ডিপোজিট, রোলওভার, ম্যাক্স উইথড্রয়াল এবং গেম কন্ট্রিবিউশন সবই বোঝা জরুরি।</p>
      <p>তৃতীয়ত, একই সময়ে একাধিক বোনাস চালানোর কৌশল শিখুন। উদাহরণস্বরূপ, IPL Cashback (যেটা স্পোর্টসের) চলাকালীন আপনি Slot Reload (যেটা ক্যাসিনোর) ব্যবহার করতে পারেন কোনো সমস্যা ছাড়া, কারণ এরা ভিন্ন প্রোডাক্ট লাইনে কাজ করে। তবে দুটি স্পোর্টস বোনাস একসাথে চলে না। নিচের লিস্টে আমরা গুরুত্বপূর্ণ টিপস দিয়েছি যেগুলো প্রতিটি jaya9 bonus হান্টারের জানা উচিত।</p>
      <figure class="prose-figure">
        <img src="{IMG}live-roulette.webp" alt="Lightning Roulette — লাইভ ক্যাসিনো বোনাস টেবিল">
        <figcaption>Lightning Roulette টেবিলে লাইভ ডিলার ম্যাচ বোনাস সবচেয়ে ভালভাবে কাজ করে।</figcaption>
      </figure>
      <ul>
        <li><strong>একসাথে ভিন্ন ক্যাটাগরি</strong> — স্পোর্টস + ক্যাসিনো বোনাস একসাথে চালানো যায়।</li>
        <li><strong>রোলওভার ট্র্যাক</strong> — অ্যাকাউন্টে রোলওভার প্রগ্রেস দেখা যায় রিয়েল-টাইমে।</li>
        <li><strong>প্রোভাইডার চয়েস</strong> — সব স্লট সমান কন্ট্রিবিউট করে না, লিস্ট চেক করুন।</li>
        <li><strong>উইথড্রয়াল লিমিট</strong> — বোনাস ক্যাশ আউট করার আগে ম্যাক্স লিমিট জানুন।</li>
        <li><strong>সময়সীমা</strong> — অনেক বোনাস ৭–১৪ দিনের মধ্যে রোলওভার শেষ করতে হয়।</li>
      </ul>

      <h2 id="vip">Joya 9 Bonus VIP প্রোগ্রাম</h2>
      <p>joya 9 bonus সিস্টেমের সবচেয়ে এক্সক্লুসিভ অংশ হলো VIP প্রোগ্রাম। যখন আপনার মাসিক টার্নওভার একটি নির্দিষ্ট লেভেল অতিক্রম করে, তখন আপনাকে অটোমেটিক VIP লেভেলে আপগ্রেড করা হয়। VIP প্লেয়াররা পান পার্সোনাল অ্যাকাউন্ট ম্যানেজার, কাস্টম বোনাস অফার, দ্রুত উইথড্রয়াল, এবং বার্থডে ও বিশেষ ইভেন্টে এক্সক্লুসিভ গিফট। এই সুবিধাগুলো শুধু VIP লেভেলেই পাওয়া যায়, পাবলিকে শেয়ার হয় না।</p>
      <ol>
        <li>Bronze VIP — মাসিক ৳৫০,০০০ টার্নওভার</li>
        <li>Silver VIP — মাসিক ৳২,০০,০০০ টার্নওভার</li>
        <li>Gold VIP — মাসিক ৳৫,০০,০০০ টার্নওভার</li>
        <li>Platinum VIP — মাসিক ৳১৫,০০,০০০ টার্নওভার</li>
        <li>Diamond VIP — মাসিক ৳৫০,০০,০০০+ টার্নওভার</li>
      </ol>

      <h2 id="start">আজই বোনাস উপভোগ করুন</h2>
      <p>Jaya9 bonus সিস্টেমে যুক্ত হতে কোনো জটিল প্রক্রিয়া নেই — শুধু সাইন আপ, ভেরিফাই এবং ডিপোজিট। প্রথম ডিপোজিটেই আপনি পাবেন ৳১০০০ ফ্রি ক্রেডিট প্লাস ১০০% ম্যাচ। এরপর প্রতিদিন নতুন প্রোমো আসবে এবং আপনি আপনার পছন্দ অনুযায়ী বেছে নিতে পারবেন। যত বেশি একটিভ থাকবেন, তত বেশি বোনাস টিয়ার আনলক হবে।</p>''',
    },
})


# -----------------------------------------------------------------------------
# GAMES
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "games",
    "active": "games",
    "en": {
        "title": "Jaya 9 Games — Slot Games Jaya9 & Joya 9 Online Games BD",
        "description": "Jaya 9 games library: 500+ slot games jaya9, live tables and joya 9 online game titles. Full guide for Bangladeshi players.",
        "eyebrow": "Games",
        "h1": "Jaya 9 Games Library",
        "intro": "500+ joya 9 games — slots, crash, live tables and arcade titles on a single platform.",
        "toc_title": "On This Page",
        "toc": [
            ("library", "Jaya 9 Game Library"),
            ("slots", "Slot Games Jaya9"),
            ("mobile", "Joya 9 Online Game Experience"),
            ("features", "Joya 9 Games — Special Features"),
            ("start", "Start Playing"),
        ],
        "body": '''      <h2 id="library">Jaya 9 Game Library — 500+ Titles in One Place</h2>
      <p>The Jaya 9 game library currently runs over 500 active titles, with new releases dropping weekly. Slots, crash, live tables, fishing, lottery, arcade — every category has real depth. Plenty of players also search the library as joya 9 game; the two spellings point at the same lobby. Selection is built around what Bangladeshi players actually open: every game runs smooth on mobile and accepts BDT stakes from ৳10 up.</p>
      <p>The library's biggest strength is breadth. You'll find the Western hits everyone knows, but also the Asia-focused titles built specifically for this market — Andar Bahar, Teen Patti, Dragon Tiger, Sicbo, plus a long shelf of Chinese-themed slots. Every jaya9 game ships with high-resolution graphics, fair RNG, and a verified payout rate. Even on a small screen the assets read crystal clear.</p>
      <figure class="prose-figure">
        <img src="{IMG}slot-2.webp" alt="Fortune Tiger slot — Jaya 9 game library">
        <figcaption>Fortune Tiger leads the Asia-themed slot shelf inside the Jaya 9 lobby.</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>Full joya9 game access</strong> is one sign-up away.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Start Playing</a>
      </div>

      <h2 id="slots">Slot Games Jaya9 — The Biggest Category</h2>
      <p>The slot games jaya9 shelf is the library's biggest section — 300+ titles in slots alone. Major providers include Pragmatic Play, PG Soft, JILI, Habanero and Spadegaming. Each studio brings its own flavour: Pragmatic's Megaways grids, PG Soft's anime art, JILI's Chinese-luck themes, Habanero's classic Vegas vibe. Whatever you like in a slot, the jaya9 slot game shelf carries something close to it.</p>
      <p>The lobby has a smart filter system. Sort by RTP (filter for 96%+ if that's your thing), by volatility (low / mid / high), or by theme (fruit, mythology, adventure, animals). Demo mode is enabled on hundreds of slots, so you can test a title in fake credit before committing real BDT — useful when you're chasing a specific feature like bonus buy.</p>
      <table>
        <thead>
          <tr><th>Slot</th><th>Provider</th><th>RTP</th><th>Volatility</th></tr>
        </thead>
        <tbody>
          <tr><td>Sweet Bonanza</td><td>Pragmatic Play</td><td>96.51%</td><td>High</td></tr>
          <tr><td>Fortune Tiger</td><td>PG Soft</td><td>96.81%</td><td>High</td></tr>
          <tr><td>Gates of Olympus</td><td>Pragmatic Play</td><td>96.50%</td><td>High</td></tr>
          <tr><td>Crazy 777</td><td>JILI</td><td>96.00%</td><td>Medium</td></tr>
          <tr><td>Mahjong Ways</td><td>PG Soft</td><td>96.95%</td><td>Medium</td></tr>
          <tr><td>Wild West Gold</td><td>Pragmatic Play</td><td>96.51%</td><td>High</td></tr>
        </tbody>
      </table>

      <h2 id="mobile">Joya 9 Online Game — Built for Mobile</h2>
      <p>Joya 9 online game play doesn't require a powerful computer — a mobile browser or our native app handles everything. Every title is built in HTML5, which means Android, iOS, and even older smartphones run the games correctly. Graphics auto-adjust to your device's capability, and games typically launch in around 2 seconds. On a 4G connection there's no perceptible lag.</p>
      <p>For mobile users we built a few specific touches — landscape and portrait modes both work, and rotating the screen on a live table swings you into a full-screen view that mirrors the desktop experience. The list below covers the mobile-friendly categories Bangladeshi players open most often.</p>
      <figure class="prose-figure">
        <img src="{IMG}slot-3.webp" alt="Crazy 777 retro slot — Joya 9 online game">
        <figcaption>Classic three-reel titles like Crazy 777 launch instantly on any phone.</figcaption>
      </figure>
      <ul>
        <li><strong>Crash games</strong> — Aviator, JetX, Crash X (one-tap launch)</li>
        <li><strong>Live cards</strong> — Andar Bahar, Teen Patti, Dragon Tiger</li>
        <li><strong>Slot spinners</strong> — Sweet Bonanza, Fortune Tiger, Olympus</li>
        <li><strong>Instant wins</strong> — Mines, Plinko, Goal</li>
        <li><strong>Lottery style</strong> — Keno, Lucky Number, Bingo</li>
      </ul>

      <h2 id="features">Joya 9 Games — Features You Won't Find Elsewhere</h2>
      <p>The joya 9 games platform carries a few unique features missing from most competing casinos. First, "Quick Play" mode — start a demo without signing in, then register later and continue with real money. Second, the "Game Recommender" engine — it watches your play history and suggests titles you'll likely enjoy next. Third, "Tournament Mode" — weekly competitions where you play the same game as everyone else and split the prize pool based on your results.</p>
      <ol>
        <li>Daily Drops & Wins — Pragmatic's global tournament</li>
        <li>JILI Tournament — weekly ৳10 lakh prize pool</li>
        <li>Live Dealer Race — daily top-player leaderboard</li>
        <li>Cash or Crash — monthly crash-game championship</li>
      </ol>

      <h2 id="start">Start Playing Now</h2>
      <p>Full Jaya 9 games library access takes a verified account and a BDT balance. Minimum deposit is ৳200 and slot rounds start at ৳10 a spin. Thousands of Bangladeshi players are already in the lobby every day — pull up the app or the web version and join them.</p>''',
    },
    "bn": {
        "title": "Jaya 9 Games — Slot Games Jaya9 ও Joya 9 Online Games BD",
        "description": "Jaya 9 games লাইব্রেরিতে ৫০০+ slot games jaya9, লাইভ টেবিল এবং joya 9 online game টাইটেল। বাংলাদেশের প্লেয়ারদের জন্য পূর্ণ গাইড।",
        "eyebrow": "গেম",
        "h1": "Jaya 9 Games লাইব্রেরি",
        "intro": "৫০০+ joya 9 games — স্লট, ক্রাশ, লাইভ টেবিল এবং আর্কেড টাইটেল এক প্ল্যাটফর্মে।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("library", "Jaya 9 Game লাইব্রেরি"),
            ("slots", "Slot Games Jaya9"),
            ("mobile", "Joya 9 Online Game"),
            ("features", "Joya 9 Games ফিচার"),
            ("start", "খেলা শুরু করুন"),
        ],
        "body": '''      <h2 id="library">Jaya 9 Game লাইব্রেরি — ৫০০+ টাইটেল এক জায়গায়</h2>
      <p>Jaya 9 game লাইব্রেরিতে এই মুহূর্তে ৫০০+ এর বেশি টাইটেল আছে, এবং প্রতি সপ্তাহে নতুন গেম যোগ হচ্ছে। স্লট, ক্রাশ, লাইভ টেবিল, ফিশিং, লটারি, আর্কেড — প্রতিটি ক্যাটাগরিতে গভীরতা আছে। অনেক প্লেয়ার joya 9 game নামেও সার্চ করেন; এই দুই বানান একই প্ল্যাটফর্মকে নির্দেশ করে। বাংলাদেশের ইউজারদের পছন্দ এবং ডিভাইস ক্যাপাবিলিটি মাথায় রেখে আমাদের গেম সিলেকশন করা হয়েছে — সব গেম মোবাইলে স্মুথ চলে এবং BDT তে স্টেক নেয়।</p>
      <p>আমাদের গেম লাইব্রেরির মূল শক্তি হলো বৈচিত্র্য। শুধু পপুলার পশ্চিমা গেম না, এশিয়ান প্লেয়ারদের জন্য তৈরি করা স্পেশাল টাইটেলও আছে — Andar Bahar, Teen Patti, Dragon Tiger, Sicbo এবং অনেক চাইনিজ থিমড স্লট। প্রতিটি jaya9 game হাই-কোয়ালিটি গ্রাফিক্স, ফেয়ার RNG এবং ভেরিফায়েড পেআউট রেট নিয়ে আসে। ছোট স্ক্রিনেও প্রতিটি গেম ক্রিস্টাল ক্লিয়ার দেখায়।</p>
      <figure class="prose-figure">
        <img src="{IMG}slot-2.webp" alt="Fortune Tiger স্লট — Jaya 9 game লাইব্রেরি">
        <figcaption>Fortune Tiger Jaya 9 লবির এশিয়ান-থিমড স্লট শেলফকে নেতৃত্ব দেয়।</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>সব joya9 game এক্সেস</strong> পেতে আজই অ্যাকাউন্ট খুলুন।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">খেলা শুরু করুন</a>
      </div>

      <h2 id="slots">Slot Games Jaya9 — সবচেয়ে জনপ্রিয় ক্যাটাগরি</h2>
      <p>Slot games jaya9 ক্যাটাগরি হলো আমাদের লাইব্রেরির সবচেয়ে বড় অংশ — ৩০০+ টাইটেল শুধু স্লটেই। জনপ্রিয় প্রোভাইডারদের মধ্যে আছে Pragmatic Play, PG Soft, JILI, Habanero এবং Spadegaming। প্রতিটি প্রোভাইডার নিজস্ব স্টাইল আনে — Pragmatic এর Megaways সিস্টেম, PG Soft এর জাপানি অ্যানিমে স্টাইল, JILI এর চাইনিজ লাকি থিম, এবং Habanero এর ক্লাসিক ভেগাস ভাইব। jaya9 slot game ফ্যানরা প্রতিটি স্বাদে কিছু না কিছু পাবেন।</p>
      <p>স্লট খেলার জন্য আমাদের প্ল্যাটফর্মে আছে স্মার্ট ফিল্টার সিস্টেম। আপনি RTP অনুযায়ী সাজাতে পারেন (৯৬% এর উপরে যেগুলো সেগুলো বেছে নিন), ভোলাটিলিটি অনুযায়ী (লো / মিড / হাই), এবং থিম অনুযায়ী (ফল, মিথোলজি, এডভেঞ্চার, প্রাণী)। ডেমো মোডে যেকোনো স্লট ফ্রিতে চেষ্টা করতে পারেন রিয়েল মানি ছাড়াই — এটা আপনাকে সাহায্য করবে আপনার পছন্দের স্লট খুঁজে পেতে।</p>
      <table>
        <thead>
          <tr><th>স্লট নাম</th><th>প্রোভাইডার</th><th>RTP</th><th>ভোলাটিলিটি</th></tr>
        </thead>
        <tbody>
          <tr><td>Sweet Bonanza</td><td>Pragmatic Play</td><td>৯৬.৫১%</td><td>হাই</td></tr>
          <tr><td>Fortune Tiger</td><td>PG Soft</td><td>৯৬.৮১%</td><td>হাই</td></tr>
          <tr><td>Gates of Olympus</td><td>Pragmatic Play</td><td>৯৬.৫০%</td><td>হাই</td></tr>
          <tr><td>Crazy 777</td><td>JILI</td><td>৯৬.০০%</td><td>মিড</td></tr>
          <tr><td>Mahjong Ways</td><td>PG Soft</td><td>৯৬.৯৫%</td><td>মিড</td></tr>
          <tr><td>Wild West Gold</td><td>Pragmatic Play</td><td>৯৬.৫১%</td><td>হাই</td></tr>
        </tbody>
      </table>

      <h2 id="mobile">Joya 9 Online Game — মোবাইলে নিখুঁত অভিজ্ঞতা</h2>
      <p>Joya 9 online game খেলার জন্য আপনার শক্তিশালী কম্পিউটার দরকার নেই — মোবাইল ব্রাউজার বা আমাদের নেটিভ অ্যাপেই সব কাজ চলে যায়। প্রতিটি গেম HTML5 টেকনোলজিতে তৈরি, যার মানে Android, iOS, এমনকি পুরাতন স্মার্টফোনেও সঠিকভাবে চলে। গ্রাফিক্স অটো-অ্যাডজাস্ট হয় আপনার ডিভাইসের ক্যাপাবিলিটি অনুযায়ী, আর গেম শুরু হয় গড়ে ২ সেকেন্ডের মধ্যে। 4G কানেকশনে কোনো ল্যাগ অনুভব হয় না।</p>
      <p>মোবাইল ইউজারদের জন্য আমরা স্পেশাল ফিচার বানিয়েছি — ল্যান্ডস্কেপ এবং পোর্ট্রেট দুই মোডে গেম প্লে করা যায়। লাইভ টেবিলে স্ক্রিন রোটেট করলে আপনি ফুল-স্ক্রিন ভিউ পাবেন যা ডেস্কটপ অভিজ্ঞতার মতোই। নিচের লিস্টে মোবাইল-ফ্রেন্ডলি গেম ক্যাটাগরিগুলো দেওয়া হলো যেগুলো বাংলাদেশের প্লেয়াররা সবচেয়ে বেশি পছন্দ করেন।</p>
      <figure class="prose-figure">
        <img src="{IMG}slot-3.webp" alt="Crazy 777 রেট্রো স্লট — Joya 9 online game">
        <figcaption>Crazy 777 এর মতো ক্লাসিক থ্রি-রিল টাইটেল যেকোনো ফোনে দ্রুত চালু হয়।</figcaption>
      </figure>
      <ul>
        <li><strong>Crash Games</strong> — Aviator, JetX, Crash X (এক ট্যাপে শুরু)</li>
        <li><strong>Live Cards</strong> — Andar Bahar, Teen Patti, Dragon Tiger</li>
        <li><strong>Slot Spinners</strong> — Sweet Bonanza, Fortune Tiger, Olympus</li>
        <li><strong>Instant Wins</strong> — Mines, Plinko, Goal</li>
        <li><strong>Lottery Style</strong> — Keno, Lucky Number, Bingo</li>
      </ul>

      <h2 id="features">Joya 9 Games এ বিশেষ ফিচার</h2>
      <p>joya 9 games প্ল্যাটফর্মে কয়েকটি ইউনিক ফিচার আছে যা অন্য ক্যাসিনোতে দেখা যায় না। প্রথমত, "Quick Play" মোড — সাইন ইন না করেই আপনি ডেমো গেম শুরু করতে পারেন এবং পরে রেজিস্টার করে রিয়েল মানিতে কন্টিনিউ করতে পারেন। দ্বিতীয়ত, "Game Recommender" AI সিস্টেম যা আপনার প্লে হিস্টরি দেখে সম্ভাব্য পছন্দের গেম সাজেস্ট করে। তৃতীয়ত, "Tournament Mode" — সাপ্তাহিক টুর্নামেন্টে সমান গেম খেলে অন্য প্লেয়ারদের সাথে কম্পিট করুন এবং প্রাইজ পুল থেকে শেয়ার পান।</p>
      <ol>
        <li>Daily Drops & Wins — Pragmatic এর গ্লোবাল টুর্নামেন্ট</li>
        <li>JILI Tournament — সাপ্তাহিক ৳১০ লাখের প্রাইজ পুল</li>
        <li>Live Dealer Race — দৈনিক টপ প্লেয়ার লিডারবোর্ড</li>
        <li>Cash or Crash — মাসিক ক্রাশ গেম চ্যাম্পিয়নশিপ</li>
      </ol>

      <h2 id="start">খেলা শুরু করুন এখনই</h2>
      <p>Jaya 9 games এর সম্পূর্ণ লাইব্রেরি এক্সেস করতে আপনার লাগবে শুধু একটি ভেরিফায়েড অ্যাকাউন্ট এবং BDT ব্যালেন্স। মিনিমাম ডিপোজিট ৳২০০, এবং স্লট রাউন্ড শুরু হয় ৳১০ থেকে। বাংলাদেশের হাজারো প্লেয়ার ইতিমধ্যে আমাদের প্ল্যাটফর্মে প্রতিদিন গেম খেলছেন — আপনিও যুক্ত হোন।</p>''',
    },
})


# -----------------------------------------------------------------------------
# APP
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "app",
    "active": "app",
    "en": {
        "title": "Jaya9 App Download — Joya 9 App APK Bangladesh | VIP App",
        "description": "Download the Jaya9 app and joya 9 app APK. Popular joya9.app casino and sportsbook for Bangladesh, plus the jaya9 vip app.",
        "eyebrow": "Mobile App",
        "h1": "Jaya9 App Download",
        "intro": "The full casino in your pocket — joya 9 app and jaya9 vip app for Bangladeshi players.",
        "toc_title": "On This Page",
        "toc": [
            ("intro", "Jaya9 App Overview"),
            ("install", "Joya 9 App Installation"),
            ("vip", "Jaya9 VIP App"),
            ("security", "Jaya 9 Apps — Security"),
            ("download", "Download Today"),
        ],
        "body": '''      <h2 id="intro">Jaya9 App — The Whole Casino in Your Pocket</h2>
      <p>The Jaya9 app is the native mobile build of the full gaming platform. Casino lobby, live dealer studio, cricket sportsbook, promotions panel — everything packed into a single lightweight APK. The build is under 15 MB, smaller than a single high-resolution photo, but it carries all 500+ games and the complete sportsbook. Plenty of users also search for it as joya 9 app — same product, alternate spelling.</p>
      <p>The app is specifically tuned for Bangladesh's 4G networks. Games typically launch in 2 seconds, and the session stays live in the background — minimize the app and your bet doesn't disappear. We push joya9.app and jaya9.apps updates every two weeks; updates roll in automatically without forcing you to close anything.</p>
      <figure class="prose-figure">
        <img src="{IMG}app-phone.webp" alt="Jaya9 app on a smartphone — Bangladesh casino in your pocket">
        <figcaption>The full Jaya9 app runs on Android phones with as little as 2 GB RAM.</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>Download now</strong> — jaya 9 app, free, secure, fast.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Download APK</a>
      </div>

      <h2 id="install">Joya 9 App Installation Guide</h2>
      <p>Installing the joya 9 app is easy, but we'll walk through the steps for first-time third-party APK users. Note up front: our app isn't on Google Play because Google blocks gambling apps in most markets — so the install runs from our site directly. That's fully safe, since the file is hosted on our own server and signed with SSL.</p>
      <ol>
        <li>Open joya9.app on your Android phone</li>
        <li>Tap "Download APK"</li>
        <li>Settings → Security → enable "Unknown Sources"</li>
        <li>Open the downloaded APK and install</li>
        <li>Log in or sign up and start playing</li>
      </ol>
      <p>iOS users don't get a directly installable app (Apple's policy), but our web app saved to your home screen via Safari's "Add to Home Screen" behaves like a native app. Full-screen experience, push notifications, offline caching — all the features ship in the web build. We call this jaya9.apps because it's effectively a Progressive Web App.</p>

      <h2 id="vip">Jaya9 VIP App — Exclusive Features</h2>
      <p>The jaya9 vip app is an extended build of the regular app, only for VIP members. It adds a separate VIP lobby, priority support line, exclusive games, high-limit tables, and a personal manager chat function. To install the VIP app you first have to reach VIP status on a regular account; the upgrade option then surfaces inside the app itself.</p>
      <p>The biggest practical perk of the VIP app is the fast withdrawal queue — VIP requests jump priority and typically clear in 5 minutes. The table below contrasts the regular and VIP builds.</p>
      <figure class="prose-figure">
        <img src="{IMG}slot-4.webp" alt="Gates of Olympus — VIP app exclusive table preview">
        <figcaption>VIP app users get exclusive tournament access on featured Pragmatic titles.</figcaption>
      </figure>
      <table>
        <thead>
          <tr><th>Feature</th><th>Regular App</th><th>VIP App</th></tr>
        </thead>
        <tbody>
          <tr><td>Game library</td><td>500+ titles</td><td>500+ titles + exclusives</td></tr>
          <tr><td>Withdrawal</td><td>20–60 minutes</td><td>5–10 minutes</td></tr>
          <tr><td>Support response</td><td>2–5 minutes</td><td>Instant</td></tr>
          <tr><td>High-limit tables</td><td>—</td><td>Up to ৳10 lakh</td></tr>
          <tr><td>Personal manager</td><td>—</td><td>WhatsApp / Telegram</td></tr>
          <tr><td>Birthday gift</td><td>Standard</td><td>Premium</td></tr>
        </tbody>
      </table>

      <h2 id="security">Jaya 9 Apps — Security & Features</h2>
      <p>Every jaya 9 apps build (regular and VIP) ships with enterprise-grade security. Data is encrypted in transit with TLS 1.3, passwords are stored as bcrypt hashes, and every transaction is verified against a separate token. On top of that, the app supports biometric login (fingerprint or face ID), so you skip the daily login dance.</p>
      <ul>
        <li><strong>Auto-update</strong> — new versions install in the background</li>
        <li><strong>Push notifications</strong> — line moves on cricket and bonus drops</li>
        <li><strong>Offline mode</strong> — game history is cached inside the app</li>
        <li><strong>Multi-language</strong> — Bangla, English, Hindi in the same build</li>
        <li><strong>Light theme</strong> — easier on the eyes during the day</li>
      </ul>

      <h2 id="download">Download Today</h2>
      <p>Don't wait to start the joya9 apps experience. Pull the APK off our official site, install, log in, and your first game is up in 60 seconds. We're already the most downloaded casino app among Bangladeshi players, and the community grows every day — get in for free.</p>''',
    },
    "bn": {
        "title": "Jaya9 App ডাউনলোড — Joya 9 App APK বাংলাদেশ | VIP App",
        "description": "Jaya9 app এবং joya 9 app APK ডাউনলোড করুন। জনপ্রিয় joya9.app ক্যাসিনো ও স্পোর্টসবুক বাংলাদেশের জন্য, plus jaya9 vip app।",
        "eyebrow": "মোবাইল অ্যাপ",
        "h1": "Jaya9 App ডাউনলোড",
        "intro": "পকেটে পুরো ক্যাসিনো — joya 9 app এবং jaya9 vip app বাংলাদেশের প্লেয়ারদের জন্য।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("intro", "Jaya9 App পরিচিতি"),
            ("install", "Joya 9 App ইনস্টলেশন"),
            ("vip", "Jaya9 VIP App"),
            ("security", "Jaya 9 Apps সিকিউরিটি"),
            ("download", "আজই ডাউনলোড"),
        ],
        "body": '''      <h2 id="intro">Jaya9 App — পকেটে পুরো ক্যাসিনো</h2>
      <p>Jaya9 app হলো আমাদের সম্পূর্ণ গেমিং প্ল্যাটফর্মের নেটিভ মোবাইল ভার্সন। ক্যাসিনো লবি, লাইভ ডিলার স্টুডিও, ক্রিকেট স্পোর্টসবুক, প্রোমোশন প্যানেল — সবকিছু এক হালকা APK ফাইলে। অ্যাপের সাইজ ১৫ MB এর কম, যা একটি হাই-রেজোলিউশন ফটোর চেয়েও ছোট। তবু এই ছোট সাইজে ৫০০+ গেম এবং পূর্ণ স্পোর্টসবুক চালানো যায়। অনেকে অনলাইনে joya 9 app নামেও খোঁজেন — দুটি একই প্রোডাক্টের ভিন্ন বানান।</p>
      <p>অ্যাপটি বিশেষভাবে অপ্টিমাইজ করা হয়েছে বাংলাদেশের ৪G নেটওয়ার্কের জন্য। গেম লোডিং সাধারণত ২ সেকেন্ডের মধ্যে হয়, এবং ব্যাকগ্রাউন্ডে আপনার সেশন একটিভ থাকে — অ্যাপ মিনিমাইজ করলেও বাজি হারায় না। প্রতি দুই সপ্তাহে আমরা joya9.app এবং jaya9.apps আপডেট রিলিজ করি, যেগুলো অটোমেটিক ব্যাকগ্রাউন্ডে ইনস্টল হয়।</p>
      <figure class="prose-figure">
        <img src="{IMG}app-phone.webp" alt="স্মার্টফোনে Jaya9 অ্যাপ — পকেটে বাংলাদেশ ক্যাসিনো">
        <figcaption>Jaya9 অ্যাপ ২ GB RAM এর Android ফোনেও স্মুথ চলে।</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>এখনই ডাউনলোড করুন</strong> jaya 9 app — ফ্রি, নিরাপদ, এবং দ্রুত।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">APK ডাউনলোড করুন</a>
      </div>

      <h2 id="install">Joya 9 App ইনস্টলেশন গাইড</h2>
      <p>joya 9 app ইনস্টল করা অত্যন্ত সহজ, কিন্তু প্রথমবার যারা থার্ড-পার্টি APK ইনস্টল করছেন তাদের জন্য নিচে ধাপে ধাপে গাইড দিচ্ছি। মনে রাখবেন, আমাদের অ্যাপটি Google Play Store এ নেই কারণ Google গ্যাম্বলিং অ্যাপ অনুমতি দেয় না বেশিরভাগ মার্কেটে — তাই সরাসরি আমাদের সাইট থেকে ডাউনলোড করতে হবে। এটি সম্পূর্ণ নিরাপদ, কারণ ফাইলটি আমাদের সার্ভার থেকেই আসছে এবং SSL দিয়ে সাইন করা।</p>
      <ol>
        <li>আপনার Android ফোনে joya9.app সাইটে যান</li>
        <li>"Download APK" বাটনে চাপ দিন</li>
        <li>সেটিংস → সিকিউরিটি → "Unknown Sources" অন করুন</li>
        <li>ডাউনলোড করা APK ওপেন করুন এবং ইনস্টল করুন</li>
        <li>লগইন বা সাইন আপ করে খেলা শুরু করুন</li>
      </ol>
      <p>iOS ইউজারদের জন্য আমরা সরাসরি ইনস্টলযোগ্য অ্যাপ দিই না (Apple এর পলিসির কারণে), কিন্তু আমাদের ওয়েব অ্যাপ Safari এ "Add to Home Screen" করলে অ্যাপের মতোই কাজ করে। ফুল-স্ক্রিন এক্সপেরিয়েন্স, পুশ নোটিফিকেশন এবং অফলাইন ক্যাশিং — সব ফিচারই আছে। আমরা একে jaya9.apps বলি কারণ এটা আসলে একটি Progressive Web App।</p>

      <h2 id="vip">Jaya9 VIP App — এক্সক্লুসিভ ফিচার</h2>
      <p>jaya9 vip app হলো আমাদের রেগুলার অ্যাপের একটি এক্সটেন্ডেড ভার্সন যা শুধু VIP মেম্বারদের জন্য। এটার মধ্যে আছে আলাদা VIP লবি, প্রায়োরিটি কাস্টমার সাপোর্ট লাইন, এক্সক্লুসিভ গেম, হাই-লিমিট টেবিল, এবং পার্সোনাল ম্যানেজার চ্যাট ফাংশন। VIP অ্যাপ ইনস্টল করতে হলে আপনাকে প্রথমে রেগুলার অ্যাকাউন্টে VIP স্ট্যাটাস অর্জন করতে হবে, তারপর অ্যাপের মধ্যেই একটি আপগ্রেড অপশন আসবে।</p>
      <p>VIP অ্যাপের বিশেষ সুবিধা হলো ফাস্ট উইথড্রয়াল কিউ — VIP রিকোয়েস্ট অগ্রাধিকার পায়, সাধারণত ৫ মিনিটের মধ্যে প্রসেস হয়। নিচের তুলনামূলক টেবিলে রেগুলার এবং VIP অ্যাপের মধ্যে পার্থক্য দেখানো হলো।</p>
      <figure class="prose-figure">
        <img src="{IMG}slot-4.webp" alt="Gates of Olympus — VIP অ্যাপ এক্সক্লুসিভ টেবিল প্রিভিউ">
        <figcaption>VIP অ্যাপ ইউজাররা ফিচারড Pragmatic টাইটেলে এক্সক্লুসিভ টুর্নামেন্ট অ্যাক্সেস পান।</figcaption>
      </figure>
      <table>
        <thead>
          <tr><th>ফিচার</th><th>রেগুলার App</th><th>VIP App</th></tr>
        </thead>
        <tbody>
          <tr><td>গেম লাইব্রেরি</td><td>৫০০+ টাইটেল</td><td>৫০০+ টাইটেল + এক্সক্লুসিভ</td></tr>
          <tr><td>উইথড্রয়াল</td><td>২০–৬০ মিনিট</td><td>৫–১০ মিনিট</td></tr>
          <tr><td>সাপোর্ট রেসপন্স</td><td>২–৫ মিনিট</td><td>ইনস্ট্যান্ট</td></tr>
          <tr><td>হাই-লিমিট টেবিল</td><td>—</td><td>৳১০ লাখ পর্যন্ত</td></tr>
          <tr><td>পার্সোনাল ম্যানেজার</td><td>—</td><td>WhatsApp / Telegram</td></tr>
          <tr><td>বার্থডে গিফট</td><td>স্ট্যান্ডার্ড</td><td>প্রিমিয়াম</td></tr>
        </tbody>
      </table>

      <h2 id="security">Jaya 9 Apps — সিকিউরিটি ও ফিচার</h2>
      <p>সব jaya 9 apps (রেগুলার এবং VIP) এন্টারপ্রাইজ গ্রেড সিকিউরিটি দিয়ে সাজানো। ডেটা TLS 1.3 দিয়ে এনক্রিপ্ট হয়, পাসওয়ার্ড bcrypt দিয়ে হ্যাশ করা থাকে, এবং প্রতিটি ট্রানজেকশন আলাদা টোকেন দিয়ে ভেরিফাই করা হয়। এর সাথে আছে বায়োমেট্রিক লগইন (ফিঙ্গারপ্রিন্ট ও ফেস ID), যা প্রতিবার লগইনের ঝামেলা থেকে মুক্তি দেয়।</p>
      <ul>
        <li><strong>Auto-update</strong> — নতুন ভার্সন ব্যাকগ্রাউন্ডে ডাউনলোড হয়</li>
        <li><strong>Push Notifications</strong> — ক্রিকেট ম্যাচের লাইন মুভ এবং বোনাস অ্যালার্ট</li>
        <li><strong>Offline Mode</strong> — গেম হিস্টরি অ্যাপের মধ্যে ক্যাশড থাকে</li>
        <li><strong>Multi-Language</strong> — বাংলা, ইংরেজি, হিন্দি একই অ্যাপে</li>
        <li><strong>Light Theme</strong> — দিনের বেলায় চোখের আরাম</li>
      </ul>

      <h2 id="download">আজই ডাউনলোড করুন</h2>
      <p>joya9 apps এক্সপেরিয়েন্স শুরু করতে অপেক্ষা করার দরকার নেই। আমাদের অফিসিয়াল সাইট থেকে APK ডাউনলোড করুন, ইনস্টল করুন, এবং প্রথম গেম খেলুন ৬০ সেকেন্ডের মধ্যে। বাংলাদেশের শীর্ষ ক্যাসিনো অ্যাপ হিসেবে আমাদের সম্প্রদায় প্রতিদিন বাড়ছে — আপনিও যুক্ত হতে পারেন একদম ফ্রি।</p>''',
    },
})


# -----------------------------------------------------------------------------
# LIVE CASINO
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "live-casino",
    "active": "live-casino",
    "en": {
        "title": "Jaya9 Live Casino Login | Joya 9 Live Casino Bangladesh",
        "description": "Jaya9 live casino — real-dealer Andar Bahar, Teen Patti and Baccarat tables. Jaya9 live casino login plus jaya 9 casino live bonus guide.",
        "eyebrow": "Live Casino",
        "h1": "Jaya9 Live Casino",
        "intro": "Real dealers, real tables, real prizes — full guide from joya 9 live casino to jaya9.com live casino.",
        "toc_title": "On This Page",
        "toc": [
            ("intro", "Jaya9 Live Casino Overview"),
            ("login", "Jaya 9 Casino Live Login"),
            ("bonus", "Jaya 9 Casino Live Bonus"),
            ("app", "Live App & Download"),
            ("start", "Start Playing Live"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Live Casino — Real Dealers, Real Tables</h2>
      <p>The Jaya9 live casino section is the platform's most engaging part — real-time HD streaming with professional dealers, actual cards, and an actual roulette wheel. Plenty of players also call this the joya 9 live casino or the jaya9 casino live floor. The tables Bangladeshi players ask for first — Andar Bahar, Teen Patti, Baccarat, Roulette, Blackjack, Dragon Tiger — all run 24/7. Hindi and English-speaking dealers are both on shift.</p>
      <p>Our live studio partners include Evolution Gaming, Pragmatic Play Live and Ezugi — all three are globally licensed and audited. Their camera setups, lighting, and dealer training all hit global standards. When you join a table at jaya9.com live casino, you're getting the same experience as a brick-and-mortar casino, just from your couch.</p>
      <figure class="prose-figure">
        <img src="{IMG}live-andar.webp" alt="Andar Bahar live dealer table on Jaya9">
        <figcaption>Andar Bahar is the most-played live table in the Jaya9 live casino lobby.</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>Join a live table now</strong> — from Andar Bahar to Lightning Roulette.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Open Live Stream</a>
      </div>

      <h2 id="login">Jaya 9 Casino Live Login — How to Get Started</h2>
      <p>The jaya 9 casino live login flow is the same as any other login. Sign in to your Jaya9 account (username and password). Open the "Live Casino" section from the main menu. You'll see lobbies for each provider — Evolution, Pragmatic Live, Ezugi — click any of them to drop into their game selection. As long as your account has balance, you can sit at any table in one click.</p>
      <p>After jaya9 live casino login your session stays secure — TLS 1.3 encryption protects everything. If you'd rather play live casino through the app, the jaya 9 casino live login app build is faster — your session is cached, so you skip the login screen if biometric verification is on.</p>
      <table>
        <thead>
          <tr><th>Live Game</th><th>Provider</th><th>Min Stake</th><th>Max Stake</th></tr>
        </thead>
        <tbody>
          <tr><td>Andar Bahar</td><td>Ezugi</td><td>৳20</td><td>৳50,000</td></tr>
          <tr><td>Teen Patti</td><td>Ezugi</td><td>৳50</td><td>৳30,000</td></tr>
          <tr><td>Speed Baccarat</td><td>Evolution</td><td>৳100</td><td>৳2,00,000</td></tr>
          <tr><td>Lightning Roulette</td><td>Evolution</td><td>৳50</td><td>৳1,00,000</td></tr>
          <tr><td>Blackjack VIP</td><td>Evolution</td><td>৳200</td><td>৳5,00,000</td></tr>
          <tr><td>Dragon Tiger</td><td>Pragmatic Live</td><td>৳20</td><td>৳75,000</td></tr>
        </tbody>
      </table>

      <h2 id="bonus">Jaya 9 Casino Live Bonus — Exclusive Offers</h2>
      <p>The jaya 9 casino live bonus track is built specifically for live-table players. If you play live tables regularly, you pick up special cashback, live-only reload bonuses, and weekly tournament entries. These don't conflict with slot or sports bonuses — you can stack them as long as the categories differ.</p>
      <ul>
        <li><strong>50% Live Match</strong> — on your first live-table deposit</li>
        <li><strong>5% Daily Cashback</strong> — on any live-table loss</li>
        <li><strong>VIP Live Lounge</strong> — separate tables for high-rollers</li>
        <li><strong>Weekly Leaderboard</strong> — top 10 live players win prizes</li>
        <li><strong>Birthday Live Gift</strong> — ৳5,000 live credit for VIP members</li>
      </ul>

      <h2 id="app">Jaya 9 Casino Live App & Download</h2>
      <p>The jaya 9 casino live app is part of the regular app — no separate download needed. But for players who only want the live tables, there's a lightweight build that loads only the live floor. It's small (8 MB) and runs well on older smartphones. To start a jaya 9 casino live download, hit "Live Only" on the app picker.</p>
      <ol>
        <li>Visit our site and tap "Download App"</li>
        <li>Pick "Standard App" or "Live Only App"</li>
        <li>Open the APK once the download completes</li>
        <li>Enable "Unknown Sources" and install</li>
        <li>Log in and join a live table</li>
      </ol>
      <figure class="prose-figure">
        <img src="{IMG}live-baccarat.webp" alt="Live Speed Baccarat table — Joya 9 live casino">
        <figcaption>Speed Baccarat runs 27-second rounds — the fastest live table in the lobby.</figcaption>
      </figure>

      <h2 id="start">Start Playing Live Today</h2>
      <p>One session at the joya 9 live casino is enough to understand why thousands of Bangladeshi players prefer it over slots or RNG tables. Real dealers, real tables, real interaction — it's a completely different experience. Open an account today and sit at your first live table within a minute.</p>''',
    },
    "bn": {
        "title": "Jaya9 Live Casino Login | Joya 9 Live Casino বাংলাদেশ",
        "description": "Jaya9 live casino — রিয়েল ডিলার Andar Bahar, Teen Patti, Baccarat টেবিল। Jaya9 live casino login এবং jaya 9 casino live bonus গাইড।",
        "eyebrow": "লাইভ ক্যাসিনো",
        "h1": "Jaya9 Live Casino",
        "intro": "রিয়েল ডিলার, রিয়েল টেবিল, রিয়েল প্রাইজ — joya 9 live casino থেকে jaya9.com live casino পর্যন্ত পূর্ণ গাইড।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("intro", "Jaya9 Live Casino পরিচিতি"),
            ("login", "Jaya 9 Casino Live Login"),
            ("bonus", "Jaya 9 Casino Live Bonus"),
            ("app", "Live App ও Download"),
            ("start", "আজই লাইভ অভিজ্ঞতা"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Live Casino — রিয়েল ডিলার, রিয়েল টেবিল</h2>
      <p>Jaya9 live casino হলো আমাদের প্ল্যাটফর্মের সবচেয়ে আকর্ষণীয় অংশ যেখানে আপনি পাবেন রিয়েল-টাইম HD স্ট্রিমিংয়ে প্রফেশনাল ডিলার, প্রকৃত কার্ড এবং প্রকৃত রুলেট হুইল। অনেকে এই সেকশনকে joya 9 live casino কিংবা jaya9 casino live নামেও চিনেন। বাংলাদেশের প্লেয়ারদের সবচেয়ে প্রিয় টেবিলগুলো — Andar Bahar, Teen Patti, Baccarat, Roulette, Blackjack, Dragon Tiger — সবগুলোই এখানে ২৪/৭ চলে। হিন্দি এবং ইংরেজি দুই ভাষাতেই ডিলার পাওয়া যায়।</p>
      <p>আমাদের লাইভ স্টুডিও পার্টনারদের মধ্যে আছে Evolution Gaming, Pragmatic Play Live এবং Ezugi — তিনটিই গ্লোবালি লাইসেন্সড এবং অডিটেড। তাদের ক্যামেরা সেটআপ, লাইটিং এবং ডিলার ট্রেনিং সবই গ্লোবাল স্ট্যান্ডার্ড। যখন আপনি jaya9.com live casino তে কোনো টেবিলে যোগ দেন, আপনি একটি সম্পূর্ণ ব্রিক-অ্যান্ড-মর্টার ক্যাসিনো অভিজ্ঞতা পান — শুধু পার্থক্য হলো আপনি বাড়িতে বসে আছেন।</p>
      <figure class="prose-figure">
        <img src="{IMG}live-andar.webp" alt="Jaya9-এ Andar Bahar লাইভ ডিলার টেবিল">
        <figcaption>Andar Bahar Jaya9 live casino লবির সবচেয়ে বেশি খেলা লাইভ টেবিল।</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>লাইভ টেবিলে যোগ দিন</strong> এখনই — Andar Bahar থেকে Lightning Roulette পর্যন্ত।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">লাইভ স্ট্রিম শুরু</a>
      </div>

      <h2 id="login">Jaya 9 Casino Live Login — কীভাবে শুরু করবেন</h2>
      <p>jaya 9 casino live login প্রক্রিয়া সাধারণ লগইনের মতোই সহজ। প্রথমে আপনার Jaya9 অ্যাকাউন্টে লগইন করুন (ইউজারনেম এবং পাসওয়ার্ড দিয়ে)। এরপর মেইন মেনু থেকে "Live Casino" সেকশনে যান। এখানে আপনি দেখবেন বিভিন্ন প্রোভাইডারের লবি — Evolution, Pragmatic Live, Ezugi — প্রতিটিতে ক্লিক করলে আপনি সরাসরি তাদের গেম সিলেকশনে চলে যাবেন। আপনার অ্যাকাউন্টে যথেষ্ট ব্যালেন্স থাকলে যেকোনো টেবিলে এক ক্লিকেই বসতে পারবেন।</p>
      <p>jaya9 live casino login করার পর আপনার সেশন সিকিউর থাকে — TLS 1.3 এনক্রিপশন আপনার সব ডেটা প্রটেক্ট করে। যদি আপনি অ্যাপের মাধ্যমে লাইভ ক্যাসিনো খেলতে চান, jaya 9 casino live login app ভার্সন আরও দ্রুত — সেখানে আপনার সেশন ক্যাশড থাকে এবং প্রতিবার লগইন করতে হয় না (বায়োমেট্রিক ভেরিফিকেশন অন থাকলে)।</p>
      <table>
        <thead>
          <tr><th>লাইভ গেম</th><th>প্রোভাইডার</th><th>মিনিমাম স্টেক</th><th>সর্বোচ্চ স্টেক</th></tr>
        </thead>
        <tbody>
          <tr><td>Andar Bahar</td><td>Ezugi</td><td>৳২০</td><td>৳৫০,০০০</td></tr>
          <tr><td>Teen Patti</td><td>Ezugi</td><td>৳৫০</td><td>৳৩০,০০০</td></tr>
          <tr><td>Speed Baccarat</td><td>Evolution</td><td>৳১০০</td><td>৳২,০০,০০০</td></tr>
          <tr><td>Lightning Roulette</td><td>Evolution</td><td>৳৫০</td><td>৳১,০০,০০০</td></tr>
          <tr><td>Blackjack VIP</td><td>Evolution</td><td>৳২০০</td><td>৳৫,০০,০০০</td></tr>
          <tr><td>Dragon Tiger</td><td>Pragmatic Live</td><td>৳২০</td><td>৳৭৫,০০০</td></tr>
        </tbody>
      </table>

      <h2 id="bonus">Jaya 9 Casino Live Bonus — এক্সক্লুসিভ অফার</h2>
      <p>jaya 9 casino live bonus প্রোগ্রাম আমাদের লাইভ প্লেয়ারদের জন্য বিশেষভাবে ডিজাইন করা। আপনি যদি লাইভ টেবিলে নিয়মিত প্লে করেন, তবে আপনি পাবেন স্পেশাল ক্যাশব্যাক, লাইভ-অনলি রিলোড বোনাস, এবং সাপ্তাহিক টুর্নামেন্ট এন্ট্রি। স্লট বা স্পোর্টস বোনাস থেকে এগুলো আলাদা — মানে আপনি একসাথে চালাতে পারেন যদি দুটি ভিন্ন ক্যাটাগরির হয়।</p>
      <ul>
        <li><strong>৫০% Live Match</strong> — প্রথম লাইভ টেবিল ডিপোজিটে</li>
        <li><strong>৫% Daily Cashback</strong> — যেকোনো লাইভ টেবিল হারে</li>
        <li><strong>VIP Live Lounge</strong> — হাই-রোলারদের জন্য আলাদা টেবিল</li>
        <li><strong>Weekly Leaderboard</strong> — শীর্ষ ১০ লাইভ প্লেয়ারের প্রাইজ</li>
        <li><strong>Birthday Live Gift</strong> — VIP মেম্বারদের জন্য ৳৫,০০০ লাইভ ক্রেডিট</li>
      </ul>

      <h2 id="app">Jaya 9 Casino Live App ও Download</h2>
      <p>jaya 9 casino live app আমাদের রেগুলার অ্যাপের অংশ — আলাদা ডাউনলোড লাগে না। তবে যারা শুধু লাইভ ক্যাসিনো খেলতে চান, তাদের জন্য একটি লাইট ভার্সন আছে যেটা শুধু লাইভ টেবিল লোড করে। এটা ছোট সাইজ (৮ MB) এবং পুরাতন স্মার্টফোনেও ভালো চলে। jaya 9 casino live download করার জন্য সাইটে গিয়ে "Live Only" অপশন বেছে নিন।</p>
      <ol>
        <li>সাইটে যান এবং "Download App" বাটনে চাপ দিন</li>
        <li>"Standard App" বা "Live Only App" বেছে নিন</li>
        <li>APK ফাইল ডাউনলোড সম্পন্ন হলে ওপেন করুন</li>
        <li>"Unknown Sources" অন করে ইনস্টল করুন</li>
        <li>লগইন করুন এবং লাইভ টেবিলে যোগ দিন</li>
      </ol>
      <figure class="prose-figure">
        <img src="{IMG}live-baccarat.webp" alt="Live Speed Baccarat টেবিল — Joya 9 live casino">
        <figcaption>Speed Baccarat ২৭-সেকেন্ড রাউন্ডে চলে — লবির সবচেয়ে দ্রুত লাইভ টেবিল।</figcaption>
      </figure>

      <h2 id="start">আজই লাইভ অভিজ্ঞতা নিন</h2>
      <p>Joya 9 live casino অভিজ্ঞতা একবার নিলে আপনি বুঝবেন কেন বাংলাদেশের হাজারো প্লেয়ার এই সেকশনকে সবচেয়ে বেশি পছন্দ করেন। রিয়েল ডিলার, রিয়েল টেবিল, রিয়েল ইন্টার‌্যাকশন — সব মিলিয়ে এক অনন্য অভিজ্ঞতা। আজই অ্যাকাউন্ট খুলে আপনার প্রথম লাইভ টেবিলে বসে পড়ুন।</p>''',
    },
})


# -----------------------------------------------------------------------------
# LOGIN
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "login",
    "active": "",
    "en": {
        "title": "Jaya9 Login | Joya9 Login | Jaya9 VIP Login Bangladesh",
        "description": "Jaya9 login simple guide — joya9 login, jaya9 vip login and jaya9 casino login full info for Bangladeshi players.",
        "eyebrow": "Login",
        "h1": "Jaya9 Login",
        "intro": "Sign in with your username and password to jaya 9 login and head straight into the casino and sportsbook.",
        "toc_title": "On This Page",
        "toc": [
            ("intro", "Jaya9 Login Overview"),
            ("steps", "Jaya 9 Login — Step by Step"),
            ("vip", "Jaya9 VIP Login"),
            ("win", "Jaya9 Win Login & Bet Login"),
            ("help", "Login Issues?"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Login — Sign In to Your Account</h2>
      <p>The Jaya9 login flow is simple — drop in your username (or mobile number) and password and you go straight into the lobby. Our system runs a single account for everything: casino, live dealer, sportsbook, and the promotions panel. Plenty of players know it as jaya9 casino login, others search for joya9 login; both spellings point at the same platform.</p>
      <p>Your Jaya9 account syncs across devices — start a session on desktop, pick it up on mobile, with no balance or history loss. If you ever hit a login wall, our 24/7 live chat support has an average response time under 2 minutes. The team works in both Bangla and English, whichever you prefer.</p>
      <figure class="prose-figure">
        <img src="{IMG}live-teenpatti.webp" alt="Teen Patti table — accessed after Jaya9 login">
        <figcaption>One Jaya9 login unlocks every product — casino, live tables, sportsbook.</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>Sign in now</strong> and claim your ৳1000 free credit.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Login / Sign Up</a>
      </div>

      <h2 id="steps">Jaya 9 Login — Step by Step</h2>
      <p>The jaya 9 login flow is five short steps. Open the official site (joya9.com login) or the app. Tap the "Login" button (top-right on most pages). Drop in your username or mobile number. Drop in your password. Hit "Login" — wait one second while the system pulls you into your lobby.</p>
      <ol>
        <li>Open the site or the app</li>
        <li>Click the "Login" button</li>
        <li>Type your username or mobile number</li>
        <li>Type your password</li>
        <li>Hit "Login" and you're in</li>
      </ol>
      <p>If login fails, the cause is usually one of three things — wrong password, locked account, or a connection issue. Tap "Forgot Password" first and reset via the SMS OTP. If your account is locked (this triggers after five wrong password attempts), open live chat — they'll verify ID and unlock the account in minutes.</p>

      <h2 id="vip">Jaya9 VIP Login — Exclusive Access</h2>
      <p>The jaya9 vip login flow is separate from regular login — VIP players get a dedicated URL and app build that drops them straight into the VIP lobby. That lobby has its own game selection, high-limit tables, and a personal manager chat function. Once you complete the joya 9 vip login, the interface looks slightly different — gold theme, priority buttons, VIP-only features. The visual change is intentional: it lets VIP members feel apart.</p>
      <table>
        <thead>
          <tr><th>Login Type</th><th>Access</th><th>Support</th><th>2FA</th></tr>
        </thead>
        <tbody>
          <tr><td>Standard Login</td><td>Full lobby</td><td>Live chat</td><td>SMS optional</td></tr>
          <tr><td>Jaya9 VIP Login</td><td>VIP lobby + exclusives</td><td>Personal manager</td><td>SMS + email</td></tr>
          <tr><td>Mobile App Login</td><td>Full lobby</td><td>Live chat</td><td>Biometric</td></tr>
          <tr><td>Quick Login (Social)</td><td>Full lobby</td><td>Live chat</td><td>OAuth provider</td></tr>
        </tbody>
      </table>

      <h2 id="win">Jaya9 Win Login & Jaya9 Bet Login</h2>
      <p>Plenty of players search for our platform as jaya9 win login because their main focus is winning. Others know it as jaya9 bet login because their priority is sports betting. In practice they all hit the same account — same username and password, same wallet. The only difference is which section you spend most of your time in. Casino and sportsbook share a single wallet, so there's no transfer needed between products.</p>
      <p>After login your balance shows the same number across every section. Win on a slot in the casino and you can stake the same balance on a sports bet without any transfer step. The list below collects the security tips every Jaya9 user should keep in mind.</p>
      <figure class="prose-figure">
        <img src="{IMG}pop-mines.webp" alt="Mines instant-win game — accessible after login">
        <figcaption>Instant-win games like Mines are one click away once you're signed in.</figcaption>
      </figure>
      <ul>
        <li><strong>Strong password</strong> — at least 8 characters, mixed numbers and symbols</li>
        <li><strong>Keep 2FA on</strong> — extra protection at withdrawal</li>
        <li><strong>Avoid public WiFi</strong> — always use your own data when signing in</li>
        <li><strong>Saved passwords</strong> — only on your personal device</li>
        <li><strong>Log out at the end</strong> — close the session when you're done</li>
      </ul>

      <h2 id="help">Login Issues? Read This</h2>
      <p>If login fails, don't panic. The most common cause is a forgotten password — tap "Forgot Password," type the OTP that lands by SMS, set a new one. One minute of work. Second most common: a locked account — five wrong attempts in a row trips the auto-lock, and live chat unlocks it after ID verification. Third: VPN or proxy use can flag you as suspicious — drop the VPN and connect through your normal data instead.</p>''',
    },
    "bn": {
        "title": "Jaya9 Login | Joya9 Login | Jaya9 VIP Login বাংলাদেশ",
        "description": "Jaya9 login সহজ গাইড — joya9 login, jaya9 vip login এবং jaya9 casino login সম্পর্কে সম্পূর্ণ তথ্য বাংলাদেশের প্লেয়ারদের জন্য।",
        "eyebrow": "লগইন",
        "h1": "Jaya9 Login",
        "intro": "ইউজারনেম এবং পাসওয়ার্ড দিয়ে jaya 9 login করুন এবং সরাসরি ক্যাসিনো ও স্পোর্টসবুকে প্রবেশ করুন।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("intro", "Jaya9 Login পরিচিতি"),
            ("steps", "Jaya 9 Login ধাপে ধাপে"),
            ("vip", "Jaya9 VIP Login"),
            ("win", "Win Login ও Bet Login"),
            ("help", "লগইনে সমস্যা?"),
        ],
        "body": '''      <h2 id="intro">Jaya9 Login — অ্যাকাউন্টে প্রবেশ করুন</h2>
      <p>Jaya9 login প্রক্রিয়া অত্যন্ত সরল — শুধু আপনার ইউজারনেম (অথবা মোবাইল নম্বর) এবং পাসওয়ার্ড দিন, এবং আপনি সরাসরি লবিতে চলে যাবেন। আমাদের সিস্টেমে একটাই অ্যাকাউন্ট কাজ করে সবকিছুর জন্য — ক্যাসিনো, লাইভ ডিলার, স্পোর্টসবুক, এবং প্রোমোশন প্যানেল। অনেকে এই প্রক্রিয়াকে jaya9 casino login নামে চিনেন, আবার কেউ joya9 login হিসেবে সার্চ করেন; দুটি একই প্ল্যাটফর্মের ভিন্ন উচ্চারণ।</p>
      <p>আপনার Jaya9 অ্যাকাউন্ট ক্রস-ডিভাইস সিঙ্ক করে — অর্থাৎ আপনি ডেস্কটপে লগইন থেকে শুরু করে মোবাইলে গিয়ে কন্টিনিউ করতে পারেন কোনো ব্যালেন্স বা হিস্টরি হারিয়ে। যদি কখনো লগইনে সমস্যা হয়, আমাদের লাইভ চ্যাট সাপোর্ট ২৪/৭ চালু আছে — গড় রেসপন্স টাইম ২ মিনিটের কম। বাংলায় বা ইংরেজিতে যেকোনো ভাষায় কথা বলতে পারবেন।</p>
      <figure class="prose-figure">
        <img src="{IMG}live-teenpatti.webp" alt="Teen Patti টেবিল — Jaya9 login এর পর অ্যাক্সেসিবল">
        <figcaption>একটি Jaya9 login সব প্রোডাক্ট আনলক করে — ক্যাসিনো, লাইভ টেবিল, স্পোর্টসবুক।</figcaption>
      </figure>
      <div class="prose-cta">
        <p><strong>এখনই লগইন করুন</strong> এবং আপনার ৳১০০০ ফ্রি ক্রেডিট ক্লেইম করুন।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">লগইন / সাইন আপ</a>
      </div>

      <h2 id="steps">Jaya 9 Login — ধাপে ধাপে গাইড</h2>
      <p>jaya 9 login করতে পাঁচটি সহজ ধাপ। প্রথমে অফিসিয়াল সাইট joya9.com login পেজে যান অথবা আমাদের অ্যাপ ওপেন করুন। দ্বিতীয়ত, "Login" বাটনে চাপ দিন (সাধারণত উপরের ডান কোণে)। তৃতীয়ত, ইউজারনেম বা মোবাইল নম্বর দিন। চতুর্থত, পাসওয়ার্ড দিন। পঞ্চমত, "Login" বাটনে চাপ দিন এবং অপেক্ষা করুন এক সেকেন্ড — সিস্টেম আপনাকে আপনার লবিতে নিয়ে যাবে।</p>
      <ol>
        <li>সাইট বা অ্যাপ ওপেন করুন</li>
        <li>"Login" বাটনে ক্লিক করুন</li>
        <li>ইউজারনেম / মোবাইল নম্বর লিখুন</li>
        <li>পাসওয়ার্ড লিখুন</li>
        <li>"Login" চাপ দিন এবং প্রবেশ করুন</li>
      </ol>
      <p>লগইন না হলে কয়েকটি কারণ থাকতে পারে — পাসওয়ার্ড ভুল, অ্যাকাউন্ট লকড, কিংবা ইন্টারনেট সমস্যা। প্রথমে "Forgot Password" বাটনে চেপে নতুন পাসওয়ার্ড সেট করুন। যদি অ্যাকাউন্ট লকড থাকে (পাঁচবার ভুল পাসওয়ার্ড দিলে এমন হয়), লাইভ চ্যাট সাপোর্টে যোগাযোগ করুন — তারা ID ভেরিফিকেশন করে দ্রুত আনলক করে দেবেন।</p>

      <h2 id="vip">Jaya9 VIP Login — এক্সক্লুসিভ এক্সেস</h2>
      <p>jaya9 vip login রেগুলার লগইন থেকে আলাদা — VIP প্লেয়াররা একটি স্পেশাল URL এবং অ্যাপ পান যা তাদের সরাসরি VIP লবিতে নিয়ে যায়। এই লবিতে আছে আলাদা গেম সিলেকশন, হাই-লিমিট টেবিল, এবং পার্সোনাল ম্যানেজার চ্যাট ফাংশন। joya 9 vip login করার পর আপনি দেখবেন ইন্টারফেস কিছুটা ভিন্ন — গোল্ডেন থিম, প্রায়োরিটি বাটন এবং VIP-অনলি ফিচার। এই পার্থক্য VIP মেম্বারদের আলাদা অনুভূতি দেয়।</p>
      <table>
        <thead>
          <tr><th>লগইন টাইপ</th><th>এক্সেস</th><th>সাপোর্ট</th><th>২FA</th></tr>
        </thead>
        <tbody>
          <tr><td>Standard Login</td><td>সম্পূর্ণ লবি</td><td>লাইভ চ্যাট</td><td>SMS অপশনাল</td></tr>
          <tr><td>Jaya9 VIP Login</td><td>VIP লবি + এক্সক্লুসিভ</td><td>পার্সোনাল ম্যানেজার</td><td>SMS + Email</td></tr>
          <tr><td>Mobile App Login</td><td>সম্পূর্ণ লবি</td><td>লাইভ চ্যাট</td><td>বায়োমেট্রিক</td></tr>
          <tr><td>Quick Login (Social)</td><td>সম্পূর্ণ লবি</td><td>লাইভ চ্যাট</td><td>OAuth প্রোভাইডার</td></tr>
        </tbody>
      </table>

      <h2 id="win">Jaya9 Win Login ও Jaya9 Bet Login</h2>
      <p>অনেক প্লেয়ার আমাদের প্ল্যাটফর্মকে jaya9 win login নামে খোঁজেন কারণ তারা মূলত উইন করার জন্য আসেন। অন্যরা jaya9 bet login হিসেবে চেনেন কারণ তাদের ফোকাস স্পোর্টস বেটিং। আসলে এগুলো সবই একই অ্যাকাউন্টের জন্য কাজ করে — আপনার ইউজারনেম এবং পাসওয়ার্ড একই, পার্থক্য শুধু আপনি কোন সেকশন বেশি ব্যবহার করেন। ক্যাসিনো এবং স্পোর্টসবুক একই ওয়ালেট শেয়ার করে, তাই টাকা ট্রান্সফার করার দরকার নেই।</p>
      <p>লগইন করার পর আপনার ব্যালেন্স প্রতিটি সেকশনে একই দেখাবে। আপনি ক্যাসিনোতে স্লট খেলে জিতলে সেই টাকা সরাসরি আপনার স্পোর্টস বেটে ব্যবহার করতে পারবেন কোনো ট্রান্সফার ছাড়া। নিচের লিস্টে নিরাপদ লগইনের জন্য কিছু গুরুত্বপূর্ণ টিপস দিয়েছি।</p>
      <figure class="prose-figure">
        <img src="{IMG}pop-mines.webp" alt="Mines instant-win গেম — লগইনের পর অ্যাক্সেসিবল">
        <figcaption>Mines এর মতো instant-win গেম সাইন ইন করার পর এক ক্লিকে দূরে।</figcaption>
      </figure>
      <ul>
        <li><strong>স্ট্রং পাসওয়ার্ড</strong> — কমপক্ষে ৮ অক্ষর, সংখ্যা ও বিশেষ চিহ্ন</li>
        <li><strong>২FA অন রাখুন</strong> — উইথড্রয়ালের সময় অতিরিক্ত নিরাপত্তা</li>
        <li><strong>পাবলিক WiFi এড়িয়ে চলুন</strong> — সবসময় নিজের ডেটা ব্যবহার করুন</li>
        <li><strong>ব্রাউজার সেভ পাসওয়ার্ড</strong> — শুধু পার্সোনাল ডিভাইসে</li>
        <li><strong>সেশন লগআউট</strong> — ব্যবহারের পর লগআউট করুন</li>
      </ul>

      <h2 id="help">লগইনে সমস্যা? এই গাইড দেখুন</h2>
      <p>কখনো লগইনে সমস্যা হলে ঘাবড়ানোর কিছু নেই। সবচেয়ে সাধারণ সমস্যা হলো ভুলে যাওয়া পাসওয়ার্ড — "Forgot Password" বাটনে চেপে SMS এ আসা OTP দিয়ে নতুন পাসওয়ার্ড সেট করুন, এক মিনিটের কাজ। দ্বিতীয় সাধারণ সমস্যা হলো অ্যাকাউন্ট লক — পাঁচবার ভুল পাসওয়ার্ড দিলে অটোমেটিক লক হয়, লাইভ চ্যাটে যোগাযোগ করুন। তৃতীয়ত, কখনো VPN বা প্রক্সি ব্যবহার করলে সিস্টেম আপনাকে সন্দেহজনক হিসেবে চিহ্নিত করে — সেক্ষেত্রে সরাসরি আপনার মূল ইন্টারনেট ব্যবহার করুন।</p>''',
    },
})


# -----------------------------------------------------------------------------
# ABOUT US (service page, no images)
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "about-us",
    "active": "",
    "en": {
        "title": "About Jaya9 Bangladesh | Online Casino & Sportsbook Brand",
        "description": "About Jaya9 — a Bangladesh-first online casino and sportsbook brand offering casino, live dealers and cricket betting in BDT with bKash and Nagad payouts.",
        "eyebrow": "About Us",
        "h1": "About Jaya9",
        "intro": "A Bangladesh-first gaming brand built around cricket, BDT payments, and 24/7 local support.",
        "toc_title": "On This Page",
        "toc": [
            ("intro", "About Jaya9 Bangladesh"),
            ("market", "Our Approach to the Market"),
            ("values", "What We Stand For"),
            ("team", "The Team Behind Jaya9"),
            ("contact", "Get in Touch"),
        ],
        "body": '''      <h2 id="intro">About Jaya9 Bangladesh</h2>
      <p>Jaya9 launched as a Bangladesh-first online gaming brand with a single goal — give local players the casino, sportsbook, and live dealer experience they actually want, without forcing them to deal with foreign currencies, slow withdrawals, or support agents who don't speak their language. From day one, every product decision has been measured against one question: does it make sense for someone playing from Dhaka, Chattogram, Khulna or Sylhet on a 4G connection?</p>
      <p>The platform is operated under licensed gaming jurisdictions, with all games supplied by certified studios. Every spin, hand and bet runs on independently audited RNG systems, and player funds are kept in segregated accounts separate from operational capital. We don't take shortcuts on these things — they're the foundation of a brand that aims to be around for the long haul.</p>
      <div class="prose-cta">
        <p><strong>Ready to play?</strong> Open an account in under 60 seconds.</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">Sign Up</a>
      </div>

      <h2 id="market">Our Approach to the Bangladesh Market</h2>
      <p>Most international gaming brands treat Bangladesh as an afterthought — a small line item under "Asia." We treat it as our home market. That means cricket isn't just one of many sports we offer; it leads the sportsbook with the deepest market depth on IPL, BPL, T20 World Cup, and BCB matches. It means our payment stack starts with bKash, Nagad and Rocket — not with international cards or crypto. It means our customer support recruits from Bangladesh, speaks Bangla natively, and keeps WhatsApp and IMO open as primary channels.</p>
      <p>Beyond payments and language, we've built our promotion calendar around the rhythm of life in Bangladesh — IPL specials when the tournament starts, weekend reload bonuses tied to local pay cycles, and Eid-period campaigns. Small choices, but they add up to a platform that actually fits how people live and play here, rather than one designed in a London office and translated.</p>

      <h2 id="values">What We Stand For</h2>
      <p>Three principles guide how we run Jaya9, and we measure every decision against them. First, transparency — every bonus has its full terms published in plain language, every withdrawal request has a public processing window, and every game has its RTP listed. Second, fairness — we use only RNG systems audited by recognized labs, and every dispute goes through a documented review process. Third, player protection — we offer self-exclusion tools, deposit limits, and visible links to responsible gambling resources on every page.</p>
      <ul>
        <li><strong>Transparency</strong> — full terms, public processing times, listed RTPs.</li>
        <li><strong>Fairness</strong> — audited RNG, documented dispute resolution.</li>
        <li><strong>Player protection</strong> — self-exclusion, deposit limits, RG resources.</li>
        <li><strong>Local commitment</strong> — Bangla support, BDT pricing, local payment rails.</li>
        <li><strong>Long-term focus</strong> — built to last, not optimized for short-term churn.</li>
      </ul>

      <h2 id="team">The Team Behind Jaya9</h2>
      <p>Jaya9 is operated by a team that combines international online gaming expertise with deep on-the-ground Bangladesh knowledge. Our product, engineering, support, and operations functions all have local representation, which means the people deciding what to build and how to support it actually understand the market they're serving. We work with global game studio partners — Pragmatic Play, Evolution, PG Soft, JILI, Spadegaming and others — but the integration choices, the lobby curation, and the promotion design are all driven locally.</p>
      <table>
        <thead>
          <tr><th>Function</th><th>Focus</th><th>Coverage</th></tr>
        </thead>
        <tbody>
          <tr><td>Product</td><td>Lobby curation, promotion design</td><td>Bangladesh-led</td></tr>
          <tr><td>Engineering</td><td>Platform reliability, mobile performance</td><td>4G-optimized</td></tr>
          <tr><td>Support</td><td>Live chat, WhatsApp, IMO</td><td>24/7 Bangla + English</td></tr>
          <tr><td>Payments</td><td>bKash, Nagad, Rocket, bank transfer</td><td>Local rails first</td></tr>
          <tr><td>Compliance</td><td>KYC, RG, fraud prevention</td><td>Licensed jurisdictions</td></tr>
        </tbody>
      </table>

      <h2 id="contact">Get in Touch</h2>
      <p>If you have a question about your account, a promotion, a payment, or any other aspect of the platform, we'd rather hear from you than have you guess. Live chat is available 24/7 from inside your account, and we also operate WhatsApp and IMO hotlines for players who prefer messengers. For partnerships, affiliate enquiries, or media questions, the support team can route you to the right department. We aim to respond to every channel within minutes, not hours.</p>''',
    },
    "bn": {
        "title": "Jaya9 বাংলাদেশ সম্পর্কে | অনলাইন ক্যাসিনো ও স্পোর্টসবুক ব্র্যান্ড",
        "description": "Jaya9 সম্পর্কে — বাংলাদেশ-কেন্দ্রিক অনলাইন ক্যাসিনো ও স্পোর্টসবুক ব্র্যান্ড, BDT-তে ক্যাসিনো, লাইভ ডিলার ও ক্রিকেট বেটিং, bKash ও Nagad পেআউট সহ।",
        "eyebrow": "আমাদের সম্পর্কে",
        "h1": "Jaya9 সম্পর্কে",
        "intro": "ক্রিকেট, BDT পেমেন্ট ও ২৪/৭ লোকাল সাপোর্ট নিয়ে তৈরি বাংলাদেশ-কেন্দ্রিক গেমিং ব্র্যান্ড।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("intro", "Jaya9 বাংলাদেশ সম্পর্কে"),
            ("market", "মার্কেটের প্রতি আমাদের দৃষ্টিভঙ্গি"),
            ("values", "আমরা যা বিশ্বাস করি"),
            ("team", "Jaya9 এর পেছনের দল"),
            ("contact", "যোগাযোগ করুন"),
        ],
        "body": '''      <h2 id="intro">Jaya9 বাংলাদেশ সম্পর্কে</h2>
      <p>Jaya9 চালু হয়েছে একটি বাংলাদেশ-কেন্দ্রিক অনলাইন গেমিং ব্র্যান্ড হিসেবে — একটাই লক্ষ্য নিয়ে: লোকাল প্লেয়ারদের ক্যাসিনো, স্পোর্টসবুক ও লাইভ ডিলার অভিজ্ঞতা দেওয়া যা তারা সত্যিই চান, বিদেশি কারেন্সি, ধীর উইথড্রয়াল বা ভিন্ন ভাষার সাপোর্ট এজেন্টের ঝামেলা ছাড়াই। প্রথম দিন থেকেই প্রতিটি প্রোডাক্ট সিদ্ধান্ত একটাই প্রশ্নে যাচাই করা হয়েছে: ঢাকা, চট্টগ্রাম, খুলনা বা সিলেট থেকে ৪G কানেকশনে খেলা একজন ইউজারের জন্য এটা কি অর্থপূর্ণ?</p>
      <p>প্ল্যাটফর্মটি লাইসেন্সড গেমিং এখতিয়ারে পরিচালিত হয়, এবং সব গেম সরবরাহ করে সার্টিফায়েড স্টুডিওগুলো। প্রতিটি স্পিন, হ্যান্ড এবং বেট স্বাধীনভাবে অডিটেড RNG সিস্টেমে চলে, এবং প্লেয়ার ফান্ড অপারেশনাল ক্যাপিটাল থেকে আলাদা সেগ্রিগেটেড অ্যাকাউন্টে রাখা হয়। আমরা এসব বিষয়ে শর্টকাট নিই না — এগুলোই দীর্ঘমেয়াদী ব্র্যান্ডের ভিত্তি।</p>
      <div class="prose-cta">
        <p><strong>খেলার জন্য প্রস্তুত?</strong> ৬০ সেকেন্ডের কমে অ্যাকাউন্ট খুলুন।</p>
        <a href="/play-now/" rel="nofollow noindex" class="btn btn-primary">সাইন আপ</a>
      </div>

      <h2 id="market">বাংলাদেশ মার্কেটের প্রতি আমাদের দৃষ্টিভঙ্গি</h2>
      <p>বেশিরভাগ আন্তর্জাতিক গেমিং ব্র্যান্ড বাংলাদেশকে গৌণ মনে করে — "এশিয়া"র অধীনে ছোট একটি লাইন আইটেম। আমরা বাংলাদেশকে আমাদের হোম মার্কেট হিসেবে দেখি। মানে ক্রিকেট আমাদের কাছে অনেকগুলো খেলার একটি নয়; এটি স্পোর্টসবুকের নেতৃত্ব দেয় — IPL, BPL, T20 World Cup এবং BCB ম্যাচগুলোতে সবচেয়ে গভীর মার্কেট সেট সহ। মানে আমাদের পেমেন্ট স্ট্যাক শুরু হয় bKash, Nagad এবং Rocket দিয়ে — আন্তর্জাতিক কার্ড বা ক্রিপ্টো দিয়ে নয়। মানে আমাদের কাস্টমার সাপোর্ট বাংলাদেশ থেকে নিয়োগ করা হয়, বাংলায় স্বাভাবিকভাবে কথা বলে, এবং WhatsApp ও IMO প্রাথমিক চ্যানেল হিসেবে রাখে।</p>
      <p>পেমেন্ট ও ভাষার বাইরেও আমরা প্রোমোশন ক্যালেন্ডার বানিয়েছি বাংলাদেশের জীবনের ছন্দ অনুযায়ী — IPL শুরু হলে IPL স্পেশাল, লোকাল পে সাইকেলের সাথে যুক্ত উইকেন্ড রিলোড বোনাস, এবং ঈদ-পিরিয়ড ক্যাম্পেইন। ছোট ছোট সিদ্ধান্ত, কিন্তু সব মিলিয়ে এমন একটি প্ল্যাটফর্ম তৈরি হয় যা বাস্তবে এখানকার মানুষের জীবনযাপন ও খেলার সাথে মানানসই, লন্ডন অফিসে ডিজাইন করে অনুবাদ করা প্ল্যাটফর্মের চেয়ে।</p>

      <h2 id="values">আমরা যা বিশ্বাস করি</h2>
      <p>তিনটি নীতি আমাদের Jaya9 চালানোর পথ নির্দেশ করে, এবং প্রতিটি সিদ্ধান্ত আমরা এই নীতির বিপরীতে যাচাই করি। প্রথম, স্বচ্ছতা — প্রতিটি বোনাসের সম্পূর্ণ শর্ত সরল ভাষায় প্রকাশিত, প্রতিটি উইথড্রয়াল রিকোয়েস্টের পাবলিক প্রসেসিং উইন্ডো আছে, এবং প্রতিটি গেমের RTP তালিকাভুক্ত। দ্বিতীয়, নিরপেক্ষতা — আমরা শুধু স্বীকৃত ল্যাব দ্বারা অডিটেড RNG সিস্টেম ব্যবহার করি, এবং প্রতিটি বিরোধ ডকুমেন্টেড রিভিউ প্রক্রিয়ার মধ্য দিয়ে যায়। তৃতীয়, প্লেয়ার সুরক্ষা — সেলফ-এক্সক্লুশন টুলস, ডিপোজিট লিমিট এবং প্রতিটি পেজে দায়িত্বশীল জুয়া রিসোর্সের দৃশ্যমান লিংক প্রদান করি।</p>
      <ul>
        <li><strong>স্বচ্ছতা</strong> — সম্পূর্ণ শর্ত, পাবলিক প্রসেসিং সময়, তালিকাভুক্ত RTP।</li>
        <li><strong>নিরপেক্ষতা</strong> — অডিটেড RNG, ডকুমেন্টেড বিরোধ সমাধান।</li>
        <li><strong>প্লেয়ার সুরক্ষা</strong> — সেলফ-এক্সক্লুশন, ডিপোজিট লিমিট, RG রিসোর্স।</li>
        <li><strong>লোকাল প্রতিশ্রুতি</strong> — বাংলা সাপোর্ট, BDT মূল্য, লোকাল পেমেন্ট রেল।</li>
        <li><strong>দীর্ঘমেয়াদী ফোকাস</strong> — টেকসই করে তৈরি, স্বল্পমেয়াদী চার্নের জন্য অপ্টিমাইজ নয়।</li>
      </ul>

      <h2 id="team">Jaya9 এর পেছনের দল</h2>
      <p>Jaya9 পরিচালনা করে একটি দল যারা আন্তর্জাতিক অনলাইন গেমিং দক্ষতা এবং বাংলাদেশের গভীর জ্ঞান একত্রিত করে। আমাদের প্রোডাক্ট, ইঞ্জিনিয়ারিং, সাপোর্ট এবং অপারেশনস ফাংশনগুলোতে লোকাল প্রতিনিধিত্ব আছে, যার মানে যারা সিদ্ধান্ত নিচ্ছেন কী বানাবেন এবং কীভাবে সাপোর্ট দেবেন, তারা আসলেই যে মার্কেটে কাজ করছেন সেটা বোঝেন। আমরা গ্লোবাল গেম স্টুডিও পার্টনারদের সাথে কাজ করি — Pragmatic Play, Evolution, PG Soft, JILI, Spadegaming এবং অন্যরা — কিন্তু ইন্টিগ্রেশন পছন্দ, লবি কিউরেশন এবং প্রোমোশন ডিজাইন সবই লোকালি চালিত।</p>
      <table>
        <thead>
          <tr><th>ফাংশন</th><th>ফোকাস</th><th>কভারেজ</th></tr>
        </thead>
        <tbody>
          <tr><td>প্রোডাক্ট</td><td>লবি কিউরেশন, প্রোমোশন ডিজাইন</td><td>বাংলাদেশ-নেতৃত্বাধীন</td></tr>
          <tr><td>ইঞ্জিনিয়ারিং</td><td>প্ল্যাটফর্ম রিলায়াবিলিটি, মোবাইল পারফরম্যান্স</td><td>৪G-অপ্টিমাইজড</td></tr>
          <tr><td>সাপোর্ট</td><td>লাইভ চ্যাট, WhatsApp, IMO</td><td>২৪/৭ বাংলা + ইংরেজি</td></tr>
          <tr><td>পেমেন্ট</td><td>bKash, Nagad, Rocket, ব্যাংক ট্রান্সফার</td><td>লোকাল রেল প্রথম</td></tr>
          <tr><td>কমপ্লায়েন্স</td><td>KYC, RG, ফ্রড প্রিভেনশন</td><td>লাইসেন্সড এখতিয়ার</td></tr>
        </tbody>
      </table>

      <h2 id="contact">যোগাযোগ করুন</h2>
      <p>আপনার অ্যাকাউন্ট, প্রোমোশন, পেমেন্ট বা প্ল্যাটফর্মের অন্য কোনো বিষয়ে প্রশ্ন থাকলে আমরা চাই আপনি আমাদের জিজ্ঞেস করুন, অনুমান নয়। লাইভ চ্যাট আপনার অ্যাকাউন্টের ভেতর থেকে ২৪/৭ চালু আছে, এবং যারা মেসেঞ্জার পছন্দ করেন তাদের জন্য আমরা WhatsApp এবং IMO হটলাইনও পরিচালনা করি। পার্টনারশিপ, অ্যাফিলিয়েট অনুসন্ধান বা মিডিয়া প্রশ্নের জন্য সাপোর্ট টিম আপনাকে সঠিক বিভাগে পাঠাবে। আমরা প্রতিটি চ্যানেলে মিনিটের মধ্যে সাড়া দেওয়ার লক্ষ্য রাখি, ঘণ্টায় নয়।</p>''',
    },
})


# -----------------------------------------------------------------------------
# PRIVACY POLICY (service page, no images)
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "privacy-policy",
    "active": "",
    "en": {
        "title": "Privacy Policy | Jaya9 Bangladesh",
        "description": "Privacy Policy for Jaya9 Bangladesh — how we collect, use, store and protect player data, and the rights you have over your information.",
        "eyebrow": "Legal",
        "h1": "Privacy Policy",
        "intro": "How Jaya9 handles your personal data — what we collect, why we collect it, and the rights you have.",
        "toc_title": "On This Page",
        "toc": [
            ("overview", "Privacy Policy Overview"),
            ("collect", "Information We Collect"),
            ("use", "How We Use Your Information"),
            ("security", "Data Security & Retention"),
            ("rights", "Your Rights"),
        ],
        "body": '''      <h2 id="overview">Privacy Policy Overview</h2>
      <p>This privacy policy describes how Jaya9 collects, uses, and protects the personal information of players who register accounts on our platform. We take this seriously because we have to — operating a regulated gaming service requires meeting strict data-handling standards, and beyond that, we believe player trust is worth far more than any short-term data we could otherwise extract. The principles below apply to every interaction you have with the platform: signing up, depositing, playing, withdrawing, and contacting support.</p>
      <p>If you create an account on Jaya9, you accept the practices outlined here. We update this document occasionally to reflect changes in regulations, in our platform, or in industry best practice — when we make a meaningful change we notify active users by email and through an in-account banner. The current version always lives at this URL, and previous versions are archived and available on request through customer support.</p>
      <div class="prose-cta">
        <p><strong>Have a privacy question?</strong> Contact our support team any time.</p>
        <a href="/login/" class="btn btn-primary">Open Live Chat</a>
      </div>

      <h2 id="collect">Information We Collect</h2>
      <p>We collect information in three broad categories. First, account information you provide directly when you sign up — name, date of birth, email, mobile number, country of residence, and chosen currency. Second, verification information collected during KYC checks, which can include a copy of a government ID, proof of address, and a selfie comparison for higher-tier verification. Third, gameplay and transaction information generated as you use the platform — bets placed, games played, deposits, withdrawals, login times, and IP addresses.</p>
      <p>We also collect technical information automatically through cookies and similar technologies — your device type, browser version, operating system, and the pages you visit on our site. This is standard for any modern web platform and lets us optimize performance, detect fraud, and personalize the experience. You can control cookies through your browser settings, though disabling them may break some platform features.</p>
      <ul>
        <li><strong>Account data</strong> — name, DOB, email, mobile, address.</li>
        <li><strong>KYC documents</strong> — government ID, proof of address, selfie verification.</li>
        <li><strong>Transaction data</strong> — deposits, withdrawals, bets, payment methods.</li>
        <li><strong>Technical data</strong> — IP address, device, browser, session logs.</li>
        <li><strong>Communications</strong> — emails, chat transcripts, support tickets.</li>
      </ul>

      <h2 id="use">How We Use Your Information</h2>
      <p>The information we collect serves specific operational purposes — we don't gather data "just in case" or for unspecified future use. Account information lets us identify you, communicate with you, and tailor the platform to your preferences. KYC information is required by anti-money-laundering and responsible-gambling regulations; without it we can't legally operate, and without verifying it before withdrawals we can't protect your account from being drained by anyone who steals your password. Transaction information powers the bonus system, the loyalty program, and the dispute resolution process.</p>
      <table>
        <thead>
          <tr><th>Purpose</th><th>Data Used</th><th>Legal Basis</th></tr>
        </thead>
        <tbody>
          <tr><td>Account creation</td><td>Name, DOB, email, mobile</td><td>Contract</td></tr>
          <tr><td>KYC / AML compliance</td><td>ID documents, address proof</td><td>Legal obligation</td></tr>
          <tr><td>Payment processing</td><td>Transaction data, payment method</td><td>Contract</td></tr>
          <tr><td>Fraud prevention</td><td>IP, device, behavioral patterns</td><td>Legitimate interest</td></tr>
          <tr><td>Marketing (opt-in)</td><td>Email, gameplay preferences</td><td>Consent</td></tr>
          <tr><td>Customer support</td><td>All available account data</td><td>Contract</td></tr>
        </tbody>
      </table>

      <h2 id="security">Data Security & Retention</h2>
      <p>All data flowing between your device and our servers is encrypted with TLS 1.3 — the same standard used by online banks. Passwords are stored as bcrypt hashes, never as plaintext. KYC documents are kept in segregated, encrypted storage with access restricted to compliance staff who have completed specific training and signed individual NDAs. We retain transaction data for the period required by gaming and financial regulations (typically five to ten years depending on the data type), after which it is securely deleted. Account data tied to closed accounts is anonymized after the regulatory retention window expires.</p>
      <ol>
        <li>TLS 1.3 encryption on all client-server traffic</li>
        <li>Bcrypt-hashed passwords with per-user salt</li>
        <li>Segregated KYC storage with access logs</li>
        <li>Regulatory retention periods, then deletion</li>
        <li>Annual third-party security audits</li>
      </ol>

      <h2 id="rights">Your Rights & How to Exercise Them</h2>
      <p>Depending on your jurisdiction, you may have the right to access the personal data we hold about you, correct inaccurate data, request deletion (subject to legal retention requirements), object to certain processing activities, and request a portable copy of your data. To exercise any of these rights, contact our data protection officer through live chat or by emailing the support team. We respond to verified requests within 30 days. If you disagree with how we've handled a privacy request, you can escalate to the relevant data protection authority in your jurisdiction.</p>''',
    },
    "bn": {
        "title": "প্রাইভেসি পলিসি | Jaya9 বাংলাদেশ",
        "description": "Jaya9 বাংলাদেশের প্রাইভেসি পলিসি — আমরা কীভাবে প্লেয়ার ডেটা সংগ্রহ, ব্যবহার, সংরক্ষণ ও সুরক্ষা করি, এবং আপনার তথ্যের উপর আপনার অধিকার।",
        "eyebrow": "আইনি",
        "h1": "প্রাইভেসি পলিসি",
        "intro": "Jaya9 কীভাবে আপনার ব্যক্তিগত ডেটা পরিচালনা করে — আমরা কী সংগ্রহ করি, কেন করি, এবং আপনার কী অধিকার আছে।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("overview", "প্রাইভেসি পলিসি ওভারভিউ"),
            ("collect", "আমরা যে তথ্য সংগ্রহ করি"),
            ("use", "তথ্য কীভাবে ব্যবহার করি"),
            ("security", "ডেটা সুরক্ষা ও ধরে রাখা"),
            ("rights", "আপনার অধিকার"),
        ],
        "body": '''      <h2 id="overview">প্রাইভেসি পলিসি ওভারভিউ</h2>
      <p>এই প্রাইভেসি পলিসি বর্ণনা করে Jaya9 কীভাবে প্ল্যাটফর্মে অ্যাকাউন্ট রেজিস্টার করা প্লেয়ারদের ব্যক্তিগত তথ্য সংগ্রহ, ব্যবহার ও সুরক্ষা করে। আমরা এটি গুরুত্বের সাথে নিই কারণ আমাদেরকে নিতে হয় — একটি নিয়ন্ত্রিত গেমিং সেবা পরিচালনার জন্য কঠোর ডেটা-হ্যান্ডলিং স্ট্যান্ডার্ড পূরণ করতে হয়, এবং তার বাইরেও, আমরা মনে করি প্লেয়ার বিশ্বাস স্বল্পমেয়াদী ডেটার চেয়ে অনেক বেশি মূল্যবান। নিচের নীতিগুলো প্ল্যাটফর্মের সাথে আপনার প্রতিটি ইন্টার‌্যাকশনে প্রযোজ্য: সাইন আপ, ডিপোজিট, খেলা, উইথড্রয়াল এবং সাপোর্টে যোগাযোগ।</p>
      <p>আপনি যদি Jaya9 এ অ্যাকাউন্ট খুলেন, তবে আপনি এখানে বর্ণিত পদ্ধতিগুলো গ্রহণ করছেন। নিয়ন্ত্রণ পরিবর্তন, প্ল্যাটফর্মের পরিবর্তন, বা ইন্ডাস্ট্রি বেস্ট প্র্যাকটিস প্রতিফলিত করতে আমরা মাঝে মাঝে এই ডকুমেন্ট আপডেট করি — যখন আমরা একটি গুরুত্বপূর্ণ পরিবর্তন করি, আমরা ইমেইল এবং অ্যাকাউন্টের ব্যানারের মাধ্যমে সক্রিয় ইউজারদের জানাই। বর্তমান ভার্সন সবসময় এই URL এ থাকে, এবং পূর্ববর্তী ভার্সনগুলো সংরক্ষণাগারে আছে যা কাস্টমার সাপোর্টের মাধ্যমে অনুরোধে পাওয়া যাবে।</p>
      <div class="prose-cta">
        <p><strong>প্রাইভেসি সম্পর্কিত প্রশ্ন আছে?</strong> যেকোনো সময় আমাদের সাপোর্ট টিমের সাথে যোগাযোগ করুন।</p>
        <a href="/login/" class="btn btn-primary">লাইভ চ্যাট খুলুন</a>
      </div>

      <h2 id="collect">আমরা যে তথ্য সংগ্রহ করি</h2>
      <p>আমরা তিনটি বিস্তৃত ক্যাটাগরিতে তথ্য সংগ্রহ করি। প্রথম, অ্যাকাউন্ট তথ্য যা আপনি সাইন আপের সময় সরাসরি প্রদান করেন — নাম, জন্ম তারিখ, ইমেইল, মোবাইল নম্বর, বসবাসের দেশ এবং নির্বাচিত কারেন্সি। দ্বিতীয়, KYC চেকের সময় সংগৃহীত ভেরিফিকেশন তথ্য, যার মধ্যে থাকতে পারে একটি সরকারি ID-র কপি, ঠিকানার প্রমাণ এবং উচ্চ-স্তরের ভেরিফিকেশনের জন্য সেলফি তুলনা। তৃতীয়, প্ল্যাটফর্ম ব্যবহারের সময় তৈরি গেমপ্লে এবং লেনদেনের তথ্য — বেট, খেলা গেম, ডিপোজিট, উইথড্রয়াল, লগইন সময় এবং IP ঠিকানা।</p>
      <p>আমরা কুকিজ এবং অনুরূপ প্রযুক্তির মাধ্যমে স্বয়ংক্রিয়ভাবে প্রযুক্তিগত তথ্যও সংগ্রহ করি — আপনার ডিভাইসের ধরন, ব্রাউজার ভার্সন, অপারেটিং সিস্টেম এবং আপনি আমাদের সাইটে যেসব পেজ ভিজিট করেন। এটি যেকোনো আধুনিক ওয়েব প্ল্যাটফর্মের জন্য মান এবং আমাদের পারফরম্যান্স অপ্টিমাইজ করতে, ফ্রড সনাক্ত করতে এবং অভিজ্ঞতা ব্যক্তিগত করতে দেয়। আপনি ব্রাউজার সেটিংসের মাধ্যমে কুকিজ নিয়ন্ত্রণ করতে পারেন, যদিও সেগুলো অক্ষম করলে কিছু প্ল্যাটফর্ম ফিচার ভেঙে যেতে পারে।</p>
      <ul>
        <li><strong>অ্যাকাউন্ট ডেটা</strong> — নাম, DOB, ইমেইল, মোবাইল, ঠিকানা।</li>
        <li><strong>KYC ডকুমেন্ট</strong> — সরকারি ID, ঠিকানার প্রমাণ, সেলফি ভেরিফিকেশন।</li>
        <li><strong>লেনদেন ডেটা</strong> — ডিপোজিট, উইথড্রয়াল, বেট, পেমেন্ট পদ্ধতি।</li>
        <li><strong>প্রযুক্তিগত ডেটা</strong> — IP ঠিকানা, ডিভাইস, ব্রাউজার, সেশন লগ।</li>
        <li><strong>যোগাযোগ</strong> — ইমেইল, চ্যাট ট্রান্সক্রিপ্ট, সাপোর্ট টিকিট।</li>
      </ul>

      <h2 id="use">তথ্য কীভাবে ব্যবহার করি</h2>
      <p>আমরা যে তথ্য সংগ্রহ করি সেগুলো নির্দিষ্ট অপারেশনাল উদ্দেশ্যে ব্যবহৃত হয় — আমরা "কেস হলে" বা অনির্দিষ্ট ভবিষ্যৎ ব্যবহারের জন্য ডেটা সংগ্রহ করি না। অ্যাকাউন্ট তথ্য আমাদের আপনাকে সনাক্ত করতে, যোগাযোগ করতে এবং আপনার পছন্দ অনুযায়ী প্ল্যাটফর্ম সাজাতে দেয়। KYC তথ্য অ্যান্টি-মানি লন্ডারিং এবং দায়িত্বশীল জুয়া নিয়ন্ত্রণের জন্য প্রয়োজন; এটি ছাড়া আমরা আইনত পরিচালনা করতে পারি না, এবং উইথড্রয়ালের আগে এটি ভেরিফাই না করলে আপনার অ্যাকাউন্ট আপনার পাসওয়ার্ড চুরি করা যেকেউ থেকে রক্ষা করতে পারি না। লেনদেনের তথ্য বোনাস সিস্টেম, লয়্যালটি প্রোগ্রাম এবং বিরোধ সমাধান প্রক্রিয়াকে শক্তি দেয়।</p>
      <table>
        <thead>
          <tr><th>উদ্দেশ্য</th><th>ব্যবহৃত ডেটা</th><th>আইনি ভিত্তি</th></tr>
        </thead>
        <tbody>
          <tr><td>অ্যাকাউন্ট তৈরি</td><td>নাম, DOB, ইমেইল, মোবাইল</td><td>চুক্তি</td></tr>
          <tr><td>KYC / AML কমপ্লায়েন্স</td><td>ID ডকুমেন্ট, ঠিকানার প্রমাণ</td><td>আইনি বাধ্যবাধকতা</td></tr>
          <tr><td>পেমেন্ট প্রসেসিং</td><td>লেনদেনের ডেটা, পেমেন্ট পদ্ধতি</td><td>চুক্তি</td></tr>
          <tr><td>ফ্রড প্রিভেনশন</td><td>IP, ডিভাইস, আচরণগত প্যাটার্ন</td><td>বৈধ স্বার্থ</td></tr>
          <tr><td>মার্কেটিং (অপ্ট-ইন)</td><td>ইমেইল, গেমপ্লে পছন্দ</td><td>সম্মতি</td></tr>
          <tr><td>কাস্টমার সাপোর্ট</td><td>সব উপলব্ধ অ্যাকাউন্ট ডেটা</td><td>চুক্তি</td></tr>
        </tbody>
      </table>

      <h2 id="security">ডেটা সুরক্ষা ও ধরে রাখা</h2>
      <p>আপনার ডিভাইস এবং আমাদের সার্ভারের মধ্যে প্রবাহিত সব ডেটা TLS 1.3 দিয়ে এনক্রিপ্ট করা হয় — অনলাইন ব্যাংকের মতোই একই স্ট্যান্ডার্ড। পাসওয়ার্ড bcrypt হ্যাশ হিসেবে সংরক্ষণ করা হয়, কখনোই প্লেইন-টেক্সট হিসেবে নয়। KYC ডকুমেন্ট সেগ্রিগেটেড, এনক্রিপ্টেড স্টোরেজে রাখা হয় যেখানে অ্যাক্সেস কমপ্লায়েন্স স্টাফদের মধ্যে সীমাবদ্ধ যারা নির্দিষ্ট ট্রেনিং সম্পন্ন করেছেন এবং পৃথক NDA সাইন করেছেন। আমরা গেমিং এবং ফাইন্যান্সিয়াল রেগুলেশন দ্বারা প্রয়োজনীয় সময়ের জন্য (সাধারণত ডেটা টাইপ অনুযায়ী পাঁচ থেকে দশ বছর) লেনদেনের ডেটা ধরে রাখি, এর পরে এটি নিরাপদে মুছে ফেলা হয়। বন্ধ অ্যাকাউন্টের সাথে যুক্ত অ্যাকাউন্ট ডেটা নিয়ন্ত্রক ধরে রাখার উইন্ডো শেষ হওয়ার পরে বেনামি করা হয়।</p>
      <ol>
        <li>সব ক্লায়েন্ট-সার্ভার ট্র্যাফিকে TLS 1.3 এনক্রিপশন</li>
        <li>প্রতি-ইউজার সল্ট সহ Bcrypt-হ্যাশড পাসওয়ার্ড</li>
        <li>অ্যাক্সেস লগ সহ সেগ্রিগেটেড KYC স্টোরেজ</li>
        <li>নিয়ন্ত্রক ধরে রাখার সময়, এরপর মুছে ফেলা</li>
        <li>বার্ষিক থার্ড-পার্টি সিকিউরিটি অডিট</li>
      </ol>

      <h2 id="rights">আপনার অধিকার ও সেগুলো প্রয়োগ</h2>
      <p>আপনার এখতিয়ারের উপর নির্ভর করে, আপনার আমাদের কাছে থাকা ব্যক্তিগত ডেটা অ্যাক্সেস করার, ভুল ডেটা সংশোধন করার, মুছে ফেলার অনুরোধ করার (আইনি ধরে রাখার প্রয়োজনীয়তা সাপেক্ষে), নির্দিষ্ট প্রসেসিং কার্যক্রমে আপত্তি জানানোর এবং আপনার ডেটার পোর্টেবল কপি অনুরোধ করার অধিকার থাকতে পারে। এই অধিকারগুলোর যেকোনোটি প্রয়োগ করতে, লাইভ চ্যাটের মাধ্যমে আমাদের ডেটা প্রটেকশন অফিসারের সাথে যোগাযোগ করুন বা সাপোর্ট টিমকে ইমেইল করুন। আমরা যাচাইকৃত অনুরোধে ৩০ দিনের মধ্যে সাড়া দিই। আমরা কীভাবে একটি প্রাইভেসি অনুরোধ পরিচালনা করেছি তাতে আপনি অসন্তুষ্ট হলে, আপনি আপনার এখতিয়ারের সংশ্লিষ্ট ডেটা প্রটেকশন কর্তৃপক্ষের কাছে এসকেলেট করতে পারেন।</p>''',
    },
})


# -----------------------------------------------------------------------------
# RESPONSIBLE GAMBLING (service page, no images)
# -----------------------------------------------------------------------------
PAGES.append({
    "slug": "responsible-gambling",
    "active": "",
    "en": {
        "title": "Responsible Gambling | Jaya9 Bangladesh",
        "description": "Responsible gambling at Jaya9 — recognize warning signs, use account self-management tools, and find support resources.",
        "eyebrow": "Player Protection",
        "h1": "Responsible Gambling",
        "intro": "Tools, warning signs, and support resources to keep gambling safe and entertaining.",
        "toc_title": "On This Page",
        "toc": [
            ("intro", "Responsible Gambling at Jaya9"),
            ("signs", "Recognizing the Warning Signs"),
            ("tools", "Tools Built Into Your Account"),
            ("support", "If You Need More Support"),
            ("age", "Player Age & Verification"),
        ],
        "body": '''      <h2 id="intro">Responsible Gambling at Jaya9</h2>
      <p>Gambling should be entertainment. For most people it stays that way — a few hours of cricket bets during the IPL, a slot session on a Friday evening, the occasional live table game with friends. But for a small percentage of players, gambling stops being entertainment and becomes a problem that affects finances, relationships and mental health. Jaya9 takes this reality seriously, and we've built tools and policies into the platform to help every player keep gambling on the entertainment side of the line.</p>
      <p>Our approach has three parts: education, so players understand what problem gambling looks like before it develops; tools, so players can put limits on their own behaviour while they still have full control; and intervention, so we can step in when warning signs appear. None of this works perfectly — gambling problems are real and serious — but we'd rather invest in protecting our players than ignore the issue and pretend it doesn't exist.</p>
      <div class="prose-cta">
        <p><strong>Need to talk to someone?</strong> Live chat support is available 24/7 in Bangla and English.</p>
        <a href="/login/" class="btn btn-primary">Open Live Chat</a>
      </div>

      <h2 id="signs">Recognizing the Warning Signs</h2>
      <p>Problem gambling rarely starts with one big incident — it builds gradually. The earlier you spot the warning signs in yourself or someone close to you, the easier it is to step back and reset. Below are some of the patterns mental health professionals associate with developing gambling problems. If three or more of these feel familiar to your situation, it's worth taking a serious look at your relationship with gambling, even if you don't think you have a "real" problem.</p>
      <ul>
        <li><strong>Chasing losses</strong> — betting bigger to recover what you've lost.</li>
        <li><strong>Spending more than planned</strong> — repeatedly going over your set budget.</li>
        <li><strong>Hiding the activity</strong> — being less than open with family or friends about gambling.</li>
        <li><strong>Borrowing to play</strong> — using credit, loans, or money meant for bills.</li>
        <li><strong>Emotional impact</strong> — feeling anxious or low about gambling.</li>
        <li><strong>Loss of control</strong> — unable to stop even when wanting to.</li>
      </ul>

      <h2 id="tools">Tools Built Into Your Account</h2>
      <p>Every Jaya9 account has a set of self-management tools you can activate at any time, without needing to contact support. These are designed to give you control over your own gambling behaviour while you're still in a position to make rational decisions — which is the right time to set limits, not after a bad session. The tools are accessible from your account profile under the "Responsible Gambling" tab, and once you set them, our system enforces them automatically.</p>
      <table>
        <thead>
          <tr><th>Tool</th><th>What It Does</th><th>Reset Window</th></tr>
        </thead>
        <tbody>
          <tr><td>Deposit Limit</td><td>Caps daily / weekly / monthly deposits</td><td>24 hours to lower, instant to raise</td></tr>
          <tr><td>Loss Limit</td><td>Caps net losses over a period</td><td>24 hours to lower, instant to raise</td></tr>
          <tr><td>Wager Limit</td><td>Caps total stake amount</td><td>24 hours to change</td></tr>
          <tr><td>Session Limit</td><td>Logs out after set play time</td><td>Instant</td></tr>
          <tr><td>Reality Check</td><td>Pop-up reminders during play</td><td>Instant</td></tr>
          <tr><td>Time-Out</td><td>Locks account 1, 7, or 30 days</td><td>Cannot be reversed early</td></tr>
          <tr><td>Self-Exclusion</td><td>Locks account 6 months to permanent</td><td>Cannot be reversed early</td></tr>
        </tbody>
      </table>

      <h2 id="support">If You Need More Support</h2>
      <p>The tools above are useful preventive measures, but if gambling has already become a serious problem for you or someone close to you, professional support is the right next step. There are dedicated organizations that specialize in helping people work through gambling addictions, and contacting them is free, confidential, and not tied to your Jaya9 account in any way. You don't have to be in crisis to reach out — having a conversation with a counselor before things get worse is often the most effective intervention.</p>
      <ol>
        <li>GamCare — international gambling support and counseling resources</li>
        <li>BeGambleAware — self-help tools, self-assessment, and helpline contacts</li>
        <li>Gambling Therapy — free online support and counseling in multiple languages</li>
        <li>Gamblers Anonymous — peer support meetings (online and in-person globally)</li>
      </ol>
      <p>If you'd like to talk to someone at Jaya9 first, our live chat support team is trained to handle responsible gambling conversations confidentially. They can walk you through the self-exclusion process, refer you to professional services, and put a hold on your account immediately if that's what you need. There's no judgement and no pressure to keep playing — quite the opposite.</p>

      <h2 id="age">Player Age & Account Verification</h2>
      <p>Jaya9 is strictly an 18+ platform. We verify the age of every player during the KYC process, and any account found to belong to someone under 18 is closed immediately, with all funds returned. We also use behavioural signals and pattern analysis to flag potentially under-age accounts that slipped through initial KYC, and we re-verify on suspicion. If you suspect that someone under 18 is using your device or your Jaya9 account, please contact support immediately and consider installing parental control software on shared devices.</p>''',
    },
    "bn": {
        "title": "দায়িত্বশীল জুয়া | Jaya9 বাংলাদেশ",
        "description": "Jaya9-এ দায়িত্বশীল জুয়া — সতর্কতা সংকেত চিনুন, অ্যাকাউন্ট সেলফ-ম্যানেজমেন্ট টুল ব্যবহার করুন এবং সাপোর্ট রিসোর্স খুঁজুন।",
        "eyebrow": "প্লেয়ার সুরক্ষা",
        "h1": "দায়িত্বশীল জুয়া",
        "intro": "জুয়াকে নিরাপদ ও বিনোদনমূলক রাখার জন্য টুলস, সতর্কতা সংকেত এবং সাপোর্ট রিসোর্স।",
        "toc_title": "এই পেজে যা পাবেন",
        "toc": [
            ("intro", "Jaya9-এ দায়িত্বশীল জুয়া"),
            ("signs", "সতর্কতা সংকেত চেনা"),
            ("tools", "অ্যাকাউন্টে নির্মিত টুলস"),
            ("support", "যদি আরও সাপোর্ট প্রয়োজন হয়"),
            ("age", "প্লেয়ার বয়স ও ভেরিফিকেশন"),
        ],
        "body": '''      <h2 id="intro">Jaya9-এ দায়িত্বশীল জুয়া</h2>
      <p>জুয়া বিনোদন হওয়া উচিত। বেশিরভাগ মানুষের জন্য এটা তেমনই থাকে — IPL এর সময় কয়েক ঘণ্টার ক্রিকেট বেট, শুক্রবার সন্ধ্যায় একটি স্লট সেশন, বন্ধুদের সাথে মাঝে মাঝে একটি লাইভ টেবিল গেম। কিন্তু কিছু প্লেয়ারের জন্য জুয়া বিনোদন থেকে বেরিয়ে এমন একটি সমস্যায় পরিণত হয় যা অর্থনীতি, সম্পর্ক এবং মানসিক স্বাস্থ্যকে প্রভাবিত করে। Jaya9 এই বাস্তবতা গুরুত্বের সাথে নেয়, এবং আমরা প্রতিটি প্লেয়ারকে জুয়াকে বিনোদনের পাশে রাখতে সাহায্য করার জন্য প্ল্যাটফর্মে টুলস এবং নীতি তৈরি করেছি।</p>
      <p>আমাদের দৃষ্টিভঙ্গির তিনটি অংশ আছে: শিক্ষা, যাতে প্লেয়াররা সমস্যাযুক্ত জুয়া কেমন দেখায় তা বিকাশের আগেই বুঝতে পারে; টুলস, যাতে প্লেয়াররা পূর্ণ নিয়ন্ত্রণ থাকা অবস্থায় নিজের আচরণে সীমা সেট করতে পারে; এবং ইন্টারভেনশন, যাতে আমরা সতর্কতা সংকেত দেখা গেলে হস্তক্ষেপ করতে পারি। এর কোনোটিই নিখুঁতভাবে কাজ করে না — জুয়ার সমস্যা বাস্তব এবং গুরুতর — কিন্তু আমরা সমস্যাকে উপেক্ষা করার চেয়ে আমাদের প্লেয়ারদের রক্ষায় বিনিয়োগ করতে চাই।</p>
      <div class="prose-cta">
        <p><strong>কারো সাথে কথা বলতে চান?</strong> লাইভ চ্যাট সাপোর্ট ২৪/৭ বাংলা ও ইংরেজিতে উপলব্ধ।</p>
        <a href="/login/" class="btn btn-primary">লাইভ চ্যাট খুলুন</a>
      </div>

      <h2 id="signs">সতর্কতা সংকেত চেনা</h2>
      <p>সমস্যাযুক্ত জুয়া খুব কমই একটি বড় ঘটনা থেকে শুরু হয় — এটি ধীরে ধীরে গড়ে ওঠে। আপনি যত আগে নিজের বা আপনার কাছের কারো মধ্যে সতর্কতা সংকেত খুঁজে পান, তত সহজ পিছিয়ে আসা এবং রিসেট করা। নিচে কিছু প্যাটার্ন আছে যা মানসিক স্বাস্থ্য পেশাদাররা জুয়ার সমস্যা বিকাশের সাথে যুক্ত করেন। যদি এর তিনটি বা তার বেশি আপনার পরিস্থিতির সাথে পরিচিত মনে হয়, এমনকি যদি আপনি মনে না করেন আপনার "প্রকৃত" সমস্যা আছে, তবু জুয়ার সাথে আপনার সম্পর্ক গুরুত্বের সাথে দেখার মূল্য আছে।</p>
      <ul>
        <li><strong>লোকসান ধরা</strong> — হারানো টাকা পুনরুদ্ধার করতে বড় বাজি ধরা।</li>
        <li><strong>পরিকল্পনার বেশি খরচ</strong> — বারবার নির্ধারিত বাজেটের ওপরে যাওয়া।</li>
        <li><strong>কার্যকলাপ লুকানো</strong> — পরিবার বা বন্ধুদের কাছে জুয়া সম্পর্কে কম খোলামেলা থাকা।</li>
        <li><strong>খেলার জন্য ধার নেওয়া</strong> — ক্রেডিট, ঋণ বা বিলের জন্য রাখা টাকা ব্যবহার।</li>
        <li><strong>আবেগগত প্রভাব</strong> — জুয়া সম্পর্কে উদ্বিগ্ন বা বিষণ্ণ অনুভব করা।</li>
        <li><strong>নিয়ন্ত্রণ হারানো</strong> — চাইলেও থামতে না পারা।</li>
      </ul>

      <h2 id="tools">অ্যাকাউন্টে নির্মিত টুলস</h2>
      <p>প্রতিটি Jaya9 অ্যাকাউন্টে সেলফ-ম্যানেজমেন্ট টুলসের একটি সেট আছে যা আপনি সাপোর্টের সাথে যোগাযোগ ছাড়াই যেকোনো সময় সক্রিয় করতে পারেন। এগুলো এমনভাবে ডিজাইন করা হয়েছে যাতে আপনি যৌক্তিক সিদ্ধান্ত নিতে পারেন এমন অবস্থায় থাকতে আপনার নিজের জুয়ার আচরণ নিয়ন্ত্রণ করতে পারেন — যা সীমা সেট করার সঠিক সময়, খারাপ সেশনের পরে নয়। টুলসগুলো আপনার অ্যাকাউন্ট প্রোফাইলের "Responsible Gambling" ট্যাব থেকে অ্যাক্সেসযোগ্য, এবং একবার সেট করলে আমাদের সিস্টেম স্বয়ংক্রিয়ভাবে সেগুলো প্রয়োগ করে।</p>
      <table>
        <thead>
          <tr><th>টুল</th><th>কী করে</th><th>রিসেট উইন্ডো</th></tr>
        </thead>
        <tbody>
          <tr><td>Deposit Limit</td><td>দৈনিক / সাপ্তাহিক / মাসিক ডিপোজিট সীমিত করে</td><td>কমাতে ২৪ ঘণ্টা, বাড়াতে তাৎক্ষণিক</td></tr>
          <tr><td>Loss Limit</td><td>একটি সময়কালে নেট লোকসান সীমিত করে</td><td>কমাতে ২৪ ঘণ্টা, বাড়াতে তাৎক্ষণিক</td></tr>
          <tr><td>Wager Limit</td><td>মোট স্টেক পরিমাণ সীমিত করে</td><td>পরিবর্তন করতে ২৪ ঘণ্টা</td></tr>
          <tr><td>Session Limit</td><td>নির্ধারিত খেলার সময়ের পরে লগ আউট</td><td>তাৎক্ষণিক</td></tr>
          <tr><td>Reality Check</td><td>খেলার সময় পপ-আপ রিমাইন্ডার</td><td>তাৎক্ষণিক</td></tr>
          <tr><td>Time-Out</td><td>১, ৭, বা ৩০ দিনের জন্য অ্যাকাউন্ট লক</td><td>আগে রিভার্স করা যায় না</td></tr>
          <tr><td>Self-Exclusion</td><td>৬ মাস থেকে স্থায়ীভাবে অ্যাকাউন্ট লক</td><td>আগে রিভার্স করা যায় না</td></tr>
        </tbody>
      </table>

      <h2 id="support">যদি আরও সাপোর্ট প্রয়োজন হয়</h2>
      <p>উপরের টুলসগুলো দরকারী প্রতিরোধমূলক ব্যবস্থা, কিন্তু যদি জুয়া ইতিমধ্যেই আপনার বা আপনার কাছের কারো জন্য একটি গুরুতর সমস্যায় পরিণত হয়ে থাকে, পেশাদার সাপোর্ট পরবর্তী সঠিক ধাপ। নির্দিষ্ট সংস্থা আছে যারা মানুষকে জুয়ার আসক্তি কাটিয়ে উঠতে সাহায্য করতে বিশেষজ্ঞ, এবং তাদের সাথে যোগাযোগ ফ্রি, গোপনীয় এবং কোনোভাবেই আপনার Jaya9 অ্যাকাউন্টের সাথে যুক্ত নয়। যোগাযোগ করতে আপনাকে সংকটে থাকতে হবে না — পরিস্থিতি আরও খারাপ হওয়ার আগে কাউন্সেলরের সাথে কথা বলা প্রায়ই সবচেয়ে কার্যকর হস্তক্ষেপ।</p>
      <ol>
        <li>GamCare — আন্তর্জাতিক জুয়া সাপোর্ট ও কাউন্সেলিং রিসোর্স</li>
        <li>BeGambleAware — সেলফ-হেল্প টুলস, সেলফ-অ্যাসেসমেন্ট এবং হেল্পলাইন যোগাযোগ</li>
        <li>Gambling Therapy — একাধিক ভাষায় ফ্রি অনলাইন সাপোর্ট ও কাউন্সেলিং</li>
        <li>Gamblers Anonymous — পিয়ার সাপোর্ট মিটিং (অনলাইন এবং বিশ্বব্যাপী ব্যক্তিগত)</li>
      </ol>
      <p>আপনি যদি আগে Jaya9-এর কারো সাথে কথা বলতে চান, আমাদের লাইভ চ্যাট সাপোর্ট টিম দায়িত্বশীল জুয়া কথোপকথন গোপনীয়ভাবে পরিচালনা করতে প্রশিক্ষিত। তারা আপনাকে সেলফ-এক্সক্লুশন প্রক্রিয়ার মধ্য দিয়ে নিয়ে যেতে পারে, পেশাদার সেবার কাছে পাঠাতে পারে, এবং আপনার প্রয়োজন হলে সাথে সাথে আপনার অ্যাকাউন্ট হোল্ড করতে পারে। কোনো বিচার নেই এবং খেলা চালিয়ে যাওয়ার কোনো চাপ নেই — বরং উল্টোটাই।</p>

      <h2 id="age">প্লেয়ার বয়স ও অ্যাকাউন্ট ভেরিফিকেশন</h2>
      <p>Jaya9 কঠোরভাবে ১৮+ প্ল্যাটফর্ম। আমরা KYC প্রক্রিয়ার সময় প্রতিটি প্লেয়ারের বয়স ভেরিফাই করি, এবং ১৮ বছরের কম বয়সী কারো অ্যাকাউন্ট পাওয়া গেলে সাথে সাথে বন্ধ করে দেওয়া হয়, সব ফান্ড ফেরত দেওয়া হয়। আমরা প্রাথমিক KYC এড়িয়ে যাওয়া সম্ভাব্য কম-বয়সী অ্যাকাউন্ট ফ্ল্যাগ করতে আচরণগত সংকেত এবং প্যাটার্ন বিশ্লেষণও ব্যবহার করি, এবং সন্দেহে পুনরায় ভেরিফাই করি। আপনি যদি সন্দেহ করেন যে ১৮ বছরের কম বয়সী কেউ আপনার ডিভাইস বা আপনার Jaya9 অ্যাকাউন্ট ব্যবহার করছে, অনুগ্রহ করে সাথে সাথে সাপোর্টে যোগাযোগ করুন এবং শেয়ার করা ডিভাইসে প্যারেন্টাল কন্ট্রোল সফটওয়্যার ইনস্টল করার কথা বিবেচনা করুন।</p>''',
    },
})


# =============================================================================
# RENDER ALL PAGES
# =============================================================================

print("Building EN + BN versions of every page…\n")
for page in PAGES:
    render(page, "en")
    print(f"  ✓ /{page['slug']}/")
    render(page, "bn")
    print(f"  ✓ /bn/{page['slug']}/")


# =============================================================================
# PLAY-NOW (single, EN-only, noindex, JS redirect)
# =============================================================================
PLAYNOW_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Redirecting...</title>
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/x-icon" href="../images/favicon.ico">
<link rel="stylesheet" href="../css/style.css">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script>
/* ============================================================
   PLAY-NOW REDIRECT CONTROLLER
   ------------------------------------------------------------
   Edit REDIRECT_URL below to point at your affiliate offer.
   Pass ?ref=xxx, ?sub=xxx or UTM params on /play-now/ and they
   will be forwarded to the offer URL automatically.
   ============================================================ */
const REDIRECT_URL = "https://jaya9bd.com/?affiliate=YOUR_ID";

function buildFinalUrl() {
  try {
    const incoming = new URL(window.location.href);
    const out = new URL(REDIRECT_URL);
    ["ref","sub","subid","click_id","clickid","utm_source","utm_medium","utm_campaign"].forEach(function(p){
      if (incoming.searchParams.has(p)) {
        out.searchParams.set(p, incoming.searchParams.get(p));
      }
    });
    return out.toString();
  } catch(e) {
    return REDIRECT_URL;
  }
}

window.location.replace(buildFinalUrl());
</script>
</head>
<body>
<div style="display:flex;align-items:center;justify-content:center;min-height:100vh;flex-direction:column;gap:20px;text-align:center;padding:20px;">
  <img src="../images/logo.webp" alt="Jaya9" style="height:60px;">
  <p style="color:#fff;font-size:18px;">Taking you to Jaya9...</p>
  <p style="color:#c9c4f0;font-size:14px;">If you are not redirected automatically, <a href="#" id="manual-link" style="color:#ff8a1a;">click here</a>.</p>
</div>
<script>
document.getElementById("manual-link").href = buildFinalUrl();
</script>
</body>
</html>
'''
play_dir = SITE / "play-now"
play_dir.mkdir(exist_ok=True)
(play_dir / "index.html").write_text(PLAYNOW_HTML, encoding="utf-8")
print("\n  ✓ /play-now/")

# robots.txt
robots = """User-agent: *
Disallow: /play-now/
Disallow: /play-now

Sitemap: /sitemap.xml
"""
(SITE / "robots.txt").write_text(robots, encoding="utf-8")
print("  ✓ robots.txt")

print("\nAll pages built.")
