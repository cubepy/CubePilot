<div align="center">

<img src="assets/logo/cubepilot-logo.svg" alt="CubePilot" width="420">

### رایگان. حرفه‌ای. چندسکویی.

یک Workspace مدرن برای مدیریت تمام سرورهای شما — SSH، SFTP، Docker، Kubernetes، تونل‌ها و مانیتورینگ، همه در یک برنامه، برای **اندروید** و **ویندوز**.

[![Status](https://img.shields.io/badge/status-beta-8B5CF6?style=for-the-badge)](docs/roadmap.md)
[![Latest release](https://img.shields.io/github/v/release/cubepy/CubePilot?style=for-the-badge&color=3B6EF6&label=latest)](https://github.com/cubepy/CubePilot/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/cubepy/CubePilot/total?style=for-the-badge&color=22D3EE)](https://github.com/cubepy/CubePilot/releases)
[![Platforms](https://img.shields.io/badge/platforms-Android%20%7C%20Windows-3B6EF6?style=for-the-badge)](docs/installation.md)
[![License](https://img.shields.io/badge/license-Freeware%20EULA-8B5CF6?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/cubepy/CubePilot?style=for-the-badge&color=22D3EE)](https://github.com/cubepy/CubePilot/stargazers)

**[English](README.md)** · [دانلود](#-دانلود) · [قابلیت‌ها](#-قابلیتها) · [نقشه راه](docs/roadmap.md) · [سؤالات متداول](docs/faq.md) · [گفتگوها](https://github.com/cubepy/CubePilot/discussions)

</div>

---

> **نسخهٔ v0.1.15 منتشر شد** — Jump Host، برای اندروید و ویندوز. از بخش [Releases](https://github.com/cubepy/CubePilot/releases/latest) بگیرید. هنوز بتاست: برای استفادهٔ روزمره پایدار است ولی آزمایش گسترده نشده. برای باخبر شدن از نسخهٔ بعدی روی Watch 👁 یا Star ⭐ بزنید.

---

## 🧊 CubePilot چیست؟

بیشتر کلاینت‌های SSH یک ترمینال به شما می‌دهند و همان‌جا تمام می‌شوند. CubePilot بر پایهٔ ایدهٔ متفاوتی ساخته شده: سرورهای شما به یک **Workspace** نیاز دارند، نه یک پنجرهٔ اتصال.

با باز کردن برنامه وارد یک داشبورد می‌شوید — چند سرور دارید، کدام‌ها آنلاین‌اند، آخرین بار روی چه چیزی کار کردید، کدام تونل‌ها فعال‌اند. از همان‌جا تنها یک کلید تا ترمینال، انتقال فایل، ری‌استارت یک کانتینر، یا تاریخچهٔ کامل هر اتفاقی که تا امروز روی آن ماشین افتاده فاصله دارید.

CubePilot **کاملاً رایگان** است؛ بدون حساب کاربری، بدون اشتراک، بدون تله‌متری و بدون قابلیت قفل‌شده پشت پرداخت. سورس آن **منتشر نمی‌شود (Closed Source)** و این ریپازیتوری فقط شامل مستندات و نسخه‌های منتشرشده است — هرگز کد.

## 🕒 Server Timeline — ویژگی امضای CubePilot

این همان بخشی است که هیچ کلاینت SSH دیگری درست انجامش نداده.

هر سرور در CubePilot یک **تاریخچهٔ کامل و قابل‌جستجو از فعالیت‌های خودش** نگه می‌دارد:

- اولین و آخرین اتصال
- هر Session به‌همراه مدت زمان آن
- Commandهایی که اجرا کرده‌اید
- فایل‌هایی که با SFTP آپلود یا دانلود شده‌اند
- تغییرات Permission فایل‌ها
- سرویس‌ها و Docker Containerهایی که ری‌استارت کرده‌اید
- تونل‌هایی که ساخته یا حذف شده‌اند
- خطاهای مهم و تغییر وضعیت سرور
- یادداشت‌های خودتان، دقیقاً روی لحظه‌ای که ثبت شده‌اند

می‌توانید جستجو کنید، فیلتر بزنید، برچسب‌گذاری و بوکمارک کنید. سه هفته بعد که چیزی خراب شد، دیگر لازم نیست به یاد بیاورید چه کرده‌اید — کافی است تایم‌لاین را بالا ببرید و بخوانید.

## ✨ قابلیت‌ها

این README مسیری را توصیف می‌کند که CubePilot به سمت آن می‌رود. هر بخش با
نسخه‌ای که در آن منتشر شده علامت خورده — هرچه علامت دارد در نسخه‌ای است که همین
حالا می‌توانید دانلود کنید؛ بقیه در [نقشه راه](docs/roadmap.md) آمده‌اند.

<details open>
<summary><b>ترمینال</b> — <code>v0.1.0</code></summary>

سشن‌های چندتبی در یک پنجره · Split View، دو سرور کنار هم یا زیر هم · Jump Host،
رسیدن به سرور از طریق یک bastion · مدیریت سشن‌ها · اتصال مجدد خودکار بدون از دست رفتن خروجی · پشتیبانی از ۲۵۶ رنگ ·
رنگ‌آمیزی سمت کلاینت روی خروجی سادهٔ سرور · جستجو در خروجی سشن · کپی، پیست و
انتخاب متن · نوار کلیدهای Esc، Tab، Ctrl، Alt و جهت‌نما · Command Palette با
`Ctrl+K` · رنگ‌بندی‌های حرفه‌ای · انتخاب اندازهٔ فونت

<sub>در برنامه: بوکمارک · Paste History</sub>
</details>

<details>
<summary><b>مدیریت سرورها</b> — <code>v0.1.0</code>، <code>v0.1.11</code></summary>

Folder · Favorite · Pin · جستجو · Tag · گروه‌های هوشمند که سرورها را با قاعده
جمع می‌کنند نه با بایگانی کردن · اتصال یک‌بارهٔ کل گروه · پروکسی HTTP و SOCKS5
برای هر سرور، برای میزبان‌هایی که مستقیم در دسترس نیستند

<sub>در برنامه: کارت سرور زنده با نمایش سیستم‌عامل، کشور، پینگ، CPU، RAM، دیسک و
Uptime</sub>
</details>

<details>
<summary><b>مدیریت فایل SFTP</b> — <code>v0.1.0</code></summary>

مرور · آپلود · دانلود · Rename · Delete · ویرایشگر Permission

<sub>در برنامه: نمای دو پنلی · Drag &amp; Drop · ویرایش در محل · پیش‌نمایش فایل ·
محاسبهٔ حجم پوشه · جستجو</sub>
</details>

<details>
<summary><b>Port Forward</b> — <code>v0.1.0</code></summary>

Local Forward · Remote Forward · Dynamic SOCKS5 · ذخیره و مدیریت تونل‌ها
</details>

<details>
<summary><b>Command Library و Snippets</b> — <code>v0.1.0</code></summary>

دستورهایی که واقعاً استفاده می‌کنید را ذخیره کنید — ری‌استارت Nginx، ری‌استارت
Docker، بروزرسانی سیستم، بکاپ، git pull، Deploy — و با یک ضربه اجرایشان کنید.
به‌همراه ۲۶ Snippet آماده برای لینوکس، Nginx، Docker، Git، Kubernetes و SSH.
</details>

<details>
<summary><b>مدیریت کلید SSH</b> — <code>v0.1.0</code></summary>

RSA، ED25519 و ECDSA · Import و Generate · نمایش Fingerprint · پشتیبانی از
Passphrase · نگهداری کلیدها در Secure Storage سیستم‌عامل
</details>

<details>
<summary><b>امنیت</b> — <code>v0.1.0</code></summary>

باز کردن با اثر انگشت · PIN · قفل خودکار · Vault رمزنگاری‌شده با AES-256-GCM و
کلید اصلی در Keystore سیستم‌عامل · تأیید Host Key

<sub>در برنامه: Windows Hello</sub>
</details>

<details>
<summary><b>بکاپ، بدون نیاز به حساب کاربری</b> — <code>v0.1.0</code></summary>

خروجی و ورودی گرفتن از یک فایل بکاپ رمزنگاری‌شده. داده‌های شما مال خودتان
می‌ماند — هیچ سرور ابری‌ای برای CubePilot وجود ندارد و چیزی جایی آپلود نمی‌شود.
</details>

<details>
<summary><b>Docker</b> — <code>v0.1.4</code>، <code>v0.1.9</code></summary>

کانتینرها، در حال اجرا و متوقف · Start، Stop و Restart · لاگ · Shell داخل
کانتینر · Delete · CPU، حافظه و شبکهٔ زندهٔ هر کانتینر · Imageها، Networkها و
Volumeها با امکان حذف. روی همان اتصال SSH که دارید کار می‌کند، پس نه چیزی نصب
می‌شود و نه کلید و رمز دومی ذخیره می‌شود.
</details>

<details>
<summary><b>Kubernetes</b> — <code>v0.1.8</code></summary>

Podها، Deploymentها، Serviceها، ConfigMapها و Secretها · یک Namespace یا همه ·
لاگ Pod و Shell داخل آن · rollout restart و تغییر تعداد replica. از طریق همان
سروری که بهش وصلید و با kubeconfig خودش اجرا می‌شود، پس هیچ credential کلاستری
روی گوشی نمی‌رود.

<sub>Secretها فقط با نام و نوع فهرست می‌شوند — CubePilot هیچ‌وقت محتوایشان را
نمی‌خواند.</sub>
</details>

<details>
<summary><b>Log Viewer</b> — <code>v0.1.7</code></summary>

ژورنال systemd، فایل‌های معمول در `/var/log`، `dmesg` یا هر مسیری که بنویسید ·
خواندن انتهای فایل یا دنبال کردن زنده · رنگ‌بندی خطوط بر اساس شدت · فیلتر ساده
یا با عبارت باقاعده · بوکمارک · خروجی از آنچه نمایش داده شده
</details>

<details>
<summary><b>مانیتورینگ</b> — <code>v0.1.5</code>، <code>v0.1.10</code></summary>

نمایش لحظه‌ای CPU، RAM، دیسک و پهنای باند شبکه روی داشبورد، به‌همراه دما،
Load Average، Uptime، نام میزبان و توزیع لینوکس — هرکدام با نمودار دو دقیقهٔ
اخیر، روی همان اتصالی که باز است.
</details>

### ویژگی‌های اختصاصی هر پلتفرم

تا اینجا فقط اعلان Session منتشر شده؛ بقیه بخشی از هدف v1.0.0 هستند.

| اندروید | ویندوز |
| --- | --- |
| اعلان Session — `v0.1.0` | Fluent Design |
| Material You با Dynamic Color | سطوح Mica و Acrylic |
| ویجت صفحه اصلی | آیکون Tray |
| Quick Settings Tile | میان‌بر سراسری |
| ترمینال شناور | Multi Window |
| پشتیبانی از Split Screen | پشتیبانی از چند مانیتور |

## 🎨 طراحی

تم‌های Dark، Light، OLED و Glass بر پایهٔ پالت آبی → بنفش با اکسنت فیروزه‌ای. Glassmorphism، Acrylic Blur، Floating Cards، سایه‌های نرم و انیمیشن‌هایی که روی نمایشگرهای پشتیبانی‌شده تا ۱۲۰ هرتز روان می‌مانند.

## 📥 دانلود

تمام نسخه‌ها از طریق **[GitHub Releases](https://github.com/cubepy/CubePilot/releases)** منتشر می‌شوند — این تنها کانال رسمی توزیع است.

| پلتفرم | فایل | حداقل نیاز |
| --- | --- | --- |
| اندروید | `.apk` | اندروید ۸.۰ (API 26) یا بالاتر |
| ویندوز | `.zip` (قابل حمل) | ویندوز ۱۰ نسخهٔ ۱۸۰۹ یا بالاتر، ۶۴ بیتی |

راهنمای گام‌به‌گام نصب، شامل نصب APK خارج از Play Store و عبور از هشدار SmartScreen ویندوز، در **[docs/installation.md](docs/installation.md)** آمده است.

> CubePilot را فقط از بخش Releases همین ریپازیتوری دانلود کنید. نسخه‌هایی که جای دیگری منتشر می‌شوند از ما نیستند و نباید کلیدهای SSH خود را به آن‌ها بسپارید.

## 📸 تصاویر محیط برنامه

<table>
  <tr>
    <td width="33%"><img src="assets/screenshots/01-dashboard.jpg" alt="داشبورد"><br><sub><b>داشبورد</b></sub></td>
    <td width="33%"><img src="assets/screenshots/02-servers.jpg" alt="سرورها"><br><sub><b>سرورها</b></sub></td>
    <td width="33%"><img src="assets/screenshots/03-terminal.jpg" alt="ترمینال"><br><sub><b>ترمینال</b></sub></td>
  </tr>
  <tr>
    <td width="33%"><img src="assets/screenshots/04-timeline.jpg" alt="تایم‌لاین سرور"><br><sub><b>تایم‌لاین سرور</b></sub></td>
    <td width="33%"><img src="assets/screenshots/05-sftp.jpg" alt="مدیریت فایل SFTP"><br><sub><b>SFTP</b></sub></td>
    <td width="33%"><img src="assets/screenshots/06-tunnels.jpg" alt="تونل‌ها"><br><sub><b>تونل‌ها</b></sub></td>
  </tr>
  <tr>
    <td width="33%"><img src="assets/screenshots/07-keys.jpg" alt="کلیدهای SSH"><br><sub><b>کلیدهای SSH</b></sub></td>
    <td width="33%"><img src="assets/screenshots/08-settings.jpg" alt="تنظیمات"><br><sub><b>تنظیمات</b></sub></td>
    <td width="33%"></td>
  </tr>
</table>

> همهٔ سرورهای این تصاویر ساختگی‌اند: آدرس‌ها از بازه‌های مستندسازی
> RFC 5737 و RFC 2606 گرفته شده‌اند، پس هیچ زیرساخت واقعی‌ای در آن‌ها
> دیده نمی‌شود. تصاویر ترمینال و SFTP استثنا هستند: هر دو به یک سشن زنده
> نیاز دارند که سرورهای دمو عمداً نمی‌توانند فراهم کنند، پس از یک سرور
> واقعی گرفته شده‌اند و نام میزبان در آن‌ها پاک شده است.
> [docs/screenshots.md](docs/screenshots.md) را ببینید.

## 🗺 نقشه راه

برنامهٔ کارها و آنچه در حال حاضر روی آن کار می‌شود در **[docs/roadmap.md](docs/roadmap.md)** آمده است.

## 📝 تغییرات نسخه‌ها

تمام نسخه‌های منتشرشده در **[CHANGELOG.md](CHANGELOG.md)** مستند می‌شوند.

## 🐞 گزارش باگ

۱. اول [ایشوهای موجود](https://github.com/cubepy/CubePilot/issues?q=is%3Aissue) را جستجو کنید — ممکن است کسی زودتر به آن برخورده باشد.
۲. یک **[Bug report](https://github.com/cubepy/CubePilot/issues/new/choose)** باز کنید و قالب را کامل پر کنید: نسخهٔ برنامه، پلتفرم، نسخهٔ سیستم‌عامل، مراحل بازتولید.
۳. **هرگز کلید خصوصی SSH، پسورد، Passphrase یا IP واقعی سرور را داخل ایشو نگذارید.** آن‌ها را با مقدار جایگزین بنویسید. برای گزارش خصوصی مشکلات امنیتی [SECURITY.md](SECURITY.md) را ببینید.

مشکلی دارید که شاید باگ نباشد؟ اول **[docs/troubleshooting.md](docs/troubleshooting.md)** را ببینید.

## 💡 ارسال پیشنهاد

یک **[Feature request](https://github.com/cubepy/CubePilot/issues/new/choose)** باز کنید، یا اگر می‌خواهید قبل از تبدیل‌شدن به درخواست رسمی دربارهٔ آن گفتگو شود، در **[Discussions → Ideas](https://github.com/cubepy/CubePilot/discussions)** موضوع را مطرح کنید. مشکلی که با آن روبه‌رو شده‌اید را بنویسید، نه فقط راه‌حلی که در ذهن دارید — معمولاً به قابلیت بهتری می‌رسد.

## ❤️ حمایت از پروژه

CubePilot رایگان است و رایگان می‌ماند — همهٔ قابلیت‌ها، روی هر دو پلتفرم، بدون نسخهٔ pro و بدون تبلیغات. این وعده تغییر نمی‌کند.

اگر برایتان مفید بوده و دوست دارید در هزینه‌های هاست، گواهی امضا و دستگاه‌های تست سهیم شوید، دونیشن کریپتو با آغوش باز پذیرفته می‌شود — و کاملاً اختیاری است.

**از داخل ایران:** [حمایت ریالی از طریق دونوفا](https://donofa.com/Cube/) — کارت‌به‌کارت، بدون نیاز به کیف‌پول کریپتو.

**از خارج ایران:**

<a href="https://nowpayments.io/donation?api_key=8f7c86ca-bc8e-4f2f-bf8a-6e8397c836ab" target="_blank" rel="noreferrer noopener">
  <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="دونیشن کریپتو با NOWPayments" width="200">
</a>

راه‌های رایگان حمایت هم به همان اندازه ارزش دارند: ⭐ ستاره دادن به ریپازیتوری، ثبت یک گزارش باگ خوب، یا معرفی برنامه به کسی که هنوز با چهار پنجرهٔ ترمینال سروکله می‌زند.

## 📄 لایسنس

استفاده از CubePilot برای همه رایگان است، شخصی و تجاری، تحت یک لایسنس اختصاصی کاربر نهایی. سورس کد منتشر نمی‌شود. **[LICENSE](LICENSE)** را ببینید.

---

<div align="center">

بخشی از اکوسیستم **Cube** · [cubesystem.top](https://cubesystem.top)

</div>
