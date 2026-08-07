<div align="center">

<img src="assets/logo/cubepilot-logo.svg" alt="CubePilot" width="420">

### رایگان. حرفه‌ای. چندسکویی.

یک Workspace مدرن برای مدیریت تمام سرورهای شما — SSH، SFTP، Docker، Kubernetes، تونل‌ها و مانیتورینگ، همه در یک برنامه، برای **اندروید** و **ویندوز**.

[![Status](https://img.shields.io/badge/status-in%20development-8B5CF6?style=for-the-badge)](docs/roadmap.md)
[![Latest release](https://img.shields.io/github/v/release/cubepy/CubePilot?style=for-the-badge&color=3B6EF6&label=latest)](https://github.com/cubepy/CubePilot/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/cubepy/CubePilot/total?style=for-the-badge&color=22D3EE)](https://github.com/cubepy/CubePilot/releases)
[![Platforms](https://img.shields.io/badge/platforms-Android%20%7C%20Windows-3B6EF6?style=for-the-badge)](docs/installation.md)
[![License](https://img.shields.io/badge/license-Freeware%20EULA-8B5CF6?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/cubepy/CubePilot?style=for-the-badge&color=22D3EE)](https://github.com/cubepy/CubePilot/stargazers)

**[English](README.md)** · [دانلود](#-دانلود) · [قابلیت‌ها](#-قابلیتها) · [نقشه راه](docs/roadmap.md) · [سؤالات متداول](docs/faq.md) · [گفتگوها](https://github.com/cubepy/CubePilot/discussions)

</div>

---

> **توجه:** CubePilot در حال توسعهٔ فعال است و هنوز اولین نسخهٔ عمومی آن منتشر نشده. این ریپازیتوری محل انتشار نسخه‌ها، مستندات و پیگیری مشکلات است. برای باخبر شدن از انتشار `v0.1.0` روی Watch 👁 یا Star ⭐ بزنید.

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

<details open>
<summary><b>ترمینال</b></summary>

سشن‌های Multi Tab · Split View · مدیریت سشن‌ها · جستجو داخل ترمینال · بوکمارک · Copy Mode · Paste History · Command Palette · زوم · رنگ‌بندی حرفه‌ای · انتخاب فونت و Cursor Style
</details>

<details>
<summary><b>مدیریت سرورها</b></summary>

کارت سرور با نمایش سیستم‌عامل، کشور، IP، پینگ، CPU، RAM، دیسک، Uptime، وضعیت آنلاین، آخرین اتصال و Tagها · جستجو · Folder · Workspace · Smart Groups · Favorites · Pin
</details>

<details>
<summary><b>مدیریت فایل SFTP</b></summary>

نمای دو پنلی · Drag & Drop · آپلود و دانلود · Rename، Delete و ویرایش در محل · ویرایشگر Permission · پیش‌نمایش فایل · محاسبهٔ حجم پوشه · جستجو
</details>

<details>
<summary><b>Docker</b></summary>

Containers، Images، Networks و Volumes · Start، Stop و Restart · لاگ زنده · Shell داخل کانتینر · Stats منابع · Delete
</details>

<details>
<summary><b>Kubernetes</b></summary>

Pods، Deployments، Services، Namespaces، ConfigMaps و Secrets · لاگ · ترمینال exec
</details>

<details>
<summary><b>Port Forward</b></summary>

Local Forward · Remote Forward · Dynamic SOCKS5 · HTTP Proxy · ذخیره و مدیریت تونل‌ها
</details>

<details>
<summary><b>مانیتورینگ</b></summary>

نمایش لحظه‌ای CPU، RAM، دیسک، شبکه، دما، پهنای باند، پینگ، Uptime و Load Average به‌همراه نمودارهای تمیز
</details>

<details>
<summary><b>Command Library و Snippets</b></summary>

دستورهایی که واقعاً استفاده می‌کنید را ذخیره کنید — ری‌استارت Nginx، ری‌استارت Docker، بروزرسانی سیستم، بکاپ، git pull، Deploy — و با یک کلیک اجرایشان کنید. به‌همراه کتابخانهٔ آمادهٔ Snippet برای SSH، Git، Docker، Kubernetes، Nginx و لینوکس.
</details>

<details>
<summary><b>Log Viewer</b></summary>

خروجی لاگ با رنگ‌بندی · جستجو · Regex · بوکمارک · Export
</details>

<details>
<summary><b>مدیریت کلید SSH</b></summary>

RSA، ED25519 و ECDSA · Import، Export و Generate · نمایش Fingerprint · پشتیبانی از Passphrase · نگهداری کلیدها در Secure Storage سیستم‌عامل
</details>

<details>
<summary><b>امنیت</b></summary>

باز کردن با اثر انگشت · Windows Hello · PIN · قفل خودکار · دیتابیس محلی رمزنگاری‌شده · Secure Key Vault
</details>

<details>
<summary><b>بکاپ، بدون نیاز به حساب کاربری</b></summary>

خروجی و ورودی گرفتن از یک فایل بکاپ رمزنگاری‌شده. داده‌های شما مال خودتان می‌ماند — هیچ سرور ابری‌ای برای CubePilot وجود ندارد و چیزی جایی آپلود نمی‌شود.
</details>

### ویژگی‌های اختصاصی هر پلتفرم

| اندروید | ویندوز |
| --- | --- |
| Material You با Dynamic Color | Fluent Design |
| ویجت صفحه اصلی | سطوح Mica و Acrylic |
| Quick Settings Tile | آیکون Tray |
| ترمینال شناور | میان‌بر سراسری |
| اعلان Session | Multi Window |
| پشتیبانی از Split Screen | پشتیبانی از چند مانیتور |

## 🎨 طراحی

تم‌های Dark، Light، OLED و Glass بر پایهٔ پالت آبی → بنفش با اکسنت فیروزه‌ای. Glassmorphism، Acrylic Blur، Floating Cards، سایه‌های نرم و انیمیشن‌هایی که روی نمایشگرهای پشتیبانی‌شده تا ۱۲۰ هرتز روان می‌مانند.

## 📥 دانلود

تمام نسخه‌ها از طریق **[GitHub Releases](https://github.com/cubepy/CubePilot/releases)** منتشر می‌شوند — این تنها کانال رسمی توزیع است.

| پلتفرم | فایل | حداقل نیاز |
| --- | --- | --- |
| اندروید | `.apk` | اندروید ۸.۰ (API 26) یا بالاتر |
| ویندوز | نصاب `.exe` یا `.msix` | ویندوز ۱۰ نسخهٔ ۱۸۰۹ یا بالاتر، ۶۴ بیتی |

راهنمای گام‌به‌گام نصب، شامل نصب APK خارج از Play Store و عبور از هشدار SmartScreen ویندوز، در **[docs/installation.md](docs/installation.md)** آمده است.

> CubePilot را فقط از بخش Releases همین ریپازیتوری دانلود کنید. نسخه‌هایی که جای دیگری منتشر می‌شوند از ما نیستند و نباید کلیدهای SSH خود را به آن‌ها بسپارید.

## 📸 تصاویر محیط برنامه

<table>
  <tr>
    <td width="33%"><img src="assets/screenshots/01-dashboard.jpg" alt="داشبورد"><br><sub><b>داشبورد</b></sub></td>
    <td width="33%"><img src="assets/screenshots/02-servers.jpg" alt="سرورها"><br><sub><b>سرورها</b></sub></td>
    <td width="33%"><img src="assets/screenshots/04-timeline.jpg" alt="تایم‌لاین سرور"><br><sub><b>تایم‌لاین سرور</b></sub></td>
  </tr>
  <tr>
    <td width="33%"><img src="assets/screenshots/06-tunnels.jpg" alt="تونل‌ها"><br><sub><b>تونل‌ها</b></sub></td>
    <td width="33%"><img src="assets/screenshots/07-keys.jpg" alt="کلیدهای SSH"><br><sub><b>کلیدهای SSH</b></sub></td>
    <td width="33%"><img src="assets/screenshots/08-settings.jpg" alt="تنظیمات"><br><sub><b>تنظیمات</b></sub></td>
  </tr>
</table>

> تصاویر ترمینال و SFTP هنوز اضافه نشده‌اند — هر دو به یک سشن زنده نیاز
> دارند و سرورهای دموی عمداً غیرقابل‌دسترس‌اند.
>
> همهٔ سرورهای این تصاویر ساختگی‌اند: آدرس‌ها از بازه‌های مستندسازی
> RFC 5737 و RFC 2606 گرفته شده‌اند، پس هیچ زیرساخت واقعی‌ای در آن‌ها
> دیده نمی‌شود. [docs/screenshots.md](docs/screenshots.md) را ببینید.

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
