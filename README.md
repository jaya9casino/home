# Jaya9 Bangladesh — Полный сайт

Бренд Jaya9, рынок Бангладеш. Главная страница на английском, внутренние страницы на бенгали.

## Структура файлов

```
jaya9-site/
├── index.html                       # Главная (EN)
├── promotion/index.html             # BN
├── referral-code/index.html         # BN
├── voucher-code/index.html          # BN
├── bonus/index.html                 # BN
├── games/index.html                 # BN
├── app/index.html                   # BN
├── live-casino/index.html           # BN
├── login/index.html                 # BN
├── about-us/index.html              # EN
├── privacy-policy/index.html        # EN
├── responsible-gambling/index.html  # EN
├── play-now/index.html              # JS-редирект на оффер (noindex)
├── robots.txt                       # Запрет индексации /play-now/
├── css/style.css
├── js/main.js
├── images/                          # все .webp + favicon
└── build_pages.py                   # генератор внутренних страниц
```

## Pretty URLs

Все страницы открываются без `.html` на конце благодаря структуре `slug/index.html`. Любой статический сервер (Apache, Nginx, Cloudflare Pages, Netlify, GitHub Pages) подхватит это автоматически — `/promotion/` → `/promotion/index.html`.

## Как менять редирект на оффер

Откройте `play-now/index.html` и поменяйте константу `REDIRECT_URL`:

```js
const REDIRECT_URL = "https://jaya9bd.com/?affiliate=YOUR_ID";
```

Скрипт сам форвардит параметры `ref`, `sub`, `subid`, `click_id`, `clickid`, `utm_source`, `utm_medium`, `utm_campaign` если они пришли на `/play-now/?...`.

## Все ссылки на /play-now/ закрыты от индексации

- `<meta name="robots" content="noindex, nofollow">` на самой странице `/play-now/`
- `rel="nofollow noindex"` на всех ссылках, ведущих туда
- `Disallow: /play-now/` в `robots.txt`

## SEO-страницы и ключи

Каждая внутренняя страница оптимизирована под список ключей. Структура каждой страницы:

1. Hero с H1 и intro
2. Оглавление (5 пунктов, decimal)
3. Тело: 5+ заголовков H2, минимум 1 таблица, 2-3 списка (ul/ol), CTA-блоки внутри текста

## Меню

**Хедер**: Promotion (с дропдауном) · Games · Live Casino · App · Login · Sign Up
- Дропдаун Promotion: Promotion / Referral Code / Voucher Code / Bonus
- Sign Up ведёт на `/play-now/` (закрыт от индекса)

**Футер**: 5 колонок — Brand · Casino · Promotion · Account · About Jaya9

## Как пересобрать страницы

Если нужно отредактировать тексты или верстку внутренних страниц — правьте `build_pages.py` и запускайте:

```
cd jaya9-site
python3 build_pages.py
```

Главная страница `index.html` редактируется напрямую, она не генерится скриптом.

## Палитра бренда

- Фон: deep purple `#1a1452` → orange `#ff8a1a`
- Акцент: orange→yellow gradient
- Карточки: `#1c1659`
- Текст: white + `#c9c4f0`
- Бенгальский шрифт: Hind Siliguri (Google Fonts)
