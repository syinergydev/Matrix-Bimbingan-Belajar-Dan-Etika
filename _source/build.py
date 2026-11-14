#!/usr/bin/env python3
"""Pembangun halaman Matrix (demo konsep SynergyDev).
Jalankan dari folder _source:  python3 build.py
Semua halaman .html di folder induk dibuat ulang dari file ini.
Teks, foto, dan tautan diedit di sini lalu build ulang, atau edit langsung file HTML-nya.
"""
import os
from urllib.parse import quote
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
IMG = os.path.join(ROOT, 'assets', 'img')

WA = '6281252595566'
WA_SHOW = '0812-5259-5566'
MAPS = 'https://maps.app.goo.gl/MTPPZfdgYqTvsLom7'
IG = 'https://www.instagram.com/matrix554/'
ALAMAT = 'Puri Indah No. HH-39, RT.37/RW.09, Suko, Kecamatan Sidoarjo, Kabupaten Sidoarjo, Jawa Timur 61224'
NAMA = 'Matrix Bimbingan Belajar Dan Etika'
MAPS_EMBED = 'https://www.google.com/maps?q=' + quote('Matrix Bimbingan Belajar Dan Etika Puri Indah HH-39 Suko Sidoarjo') + '&output=embed'


def wa(msg):
    return 'https://wa.me/%s?text=%s' % (WA, quote(msg))


WA_HALO = wa('Halo Matrix Bimbingan Belajar Dan Etika, saya ingin berkonsultasi.')

# ---------- Foto ----------
PH = {
    'belajar-atas': 'Siswa belajar bersama di ruang kelas Matrix, difoto dari sudut atas',
    'belajar-kelas': 'Siswa mengikuti kegiatan belajar di ruang kelas Matrix',
    'kelas-ceria': 'Siswa tersenyum ke kamera di ruang kelas Matrix',
    'belajar-meja': 'Suasana belajar di ruang kelas Matrix dilihat dari atas',
    'kebersamaan': 'Siswa berpose ceria bersama di ruang kelas Matrix',
    'depan-1': 'Siswa berfoto bersama di depan bangunan Matrix',
    'depan-2': 'Siswa berfoto bersama di halaman depan Matrix',
    'depan-3': 'Siswa dan pendamping berfoto di depan Matrix',
    'depan-4': 'Siswa dan pendamping berfoto bersama di depan Matrix',
    'depan-5': 'Siswa berfoto bersama dengan gaya santai di depan bangunan Matrix',
    'depan-6': 'Siswa berpose di jalan depan lokasi Matrix',
    'papan-nama': 'Beberapa orang berdiri di depan papan nama Matrix',
    'tari': 'Kegiatan menari bersama di luar ruangan',
    'lapangan': 'Anak-anak bermain di lapangan dalam ruangan',
    'bangunan': 'Tampak depan bangunan Matrix di Puri Indah, Sidoarjo',
    'poster': 'Poster pendaftaran siswa baru Matrix',
}
CAP = {
    'belajar-atas': 'Suasana kegiatan belajar',
    'belajar-kelas': 'Siswa belajar di kelas',
    'kelas-ceria': 'Wajah-wajah di ruang kelas',
    'belajar-meja': 'Belajar bersama di ruang kelas',
    'kebersamaan': 'Kebersamaan di ruang kelas',
    'depan-1': 'Berfoto bersama di depan Matrix',
    'depan-2': 'Dokumentasi kebersamaan',
    'depan-3': 'Dokumentasi kebersamaan',
    'depan-4': 'Dokumentasi kebersamaan',
    'depan-5': 'Dokumentasi kebersamaan',
    'depan-6': 'Dokumentasi kebersamaan',
    'papan-nama': 'Di depan papan nama Matrix',
    'tari': 'Dokumentasi kegiatan di luar kelas',
    'lapangan': 'Dokumentasi kegiatan bersama',
    'bangunan': 'Tampak depan Matrix',
}


def size(key, thumb=False):
    return Image.open(os.path.join(IMG, ('t-' if thumb else '') + key + '.jpg')).size


def img(key, cls='', thumb=False, lazy=True, par=None, alt=None):
    w, h = size(key, thumb)
    a = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    p = ' data-par="%s"' % par if par else ''
    c = ' class="%s"' % cls if cls else ''
    return '<img src="assets/img/%s%s.jpg" alt="%s" width="%d" height="%d"%s decoding="async"%s%s>' % (
        't-' if thumb else '', key, alt if alt is not None else PH[key], w, h, a, c, p)


# ---------- Ikon ----------
def ic_wa(extra=''):
    return ('<svg class="ic ic-wa" viewBox="0 0 24 24" aria-hidden="true"><path class="bub" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z"/>'
            '<path class="ph" transform="translate(6.3 6.1) scale(.5)" d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>')


IC_IG = ('<svg class="ic ic-ig" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
         '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.2" fill="currentColor" stroke="none"/></svg>')
IC_MAP = ('<svg class="ic ic-map" viewBox="0 0 24 24" aria-hidden="true"><path class="pin" d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7z"/><circle class="dot" cx="12" cy="9" r="2.7"/></svg>')
STAR = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2.5 2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
STARS = '<span class="stars" role="img" aria-label="Rating 5 dari 5">' + STAR * 5 + '</span>'
QM = '<svg class="qm" viewBox="0 0 48 48" fill="currentColor" aria-hidden="true"><path d="M10 30c0-9 5-15 13-18l1.6 3C19 17.600 17.500 21 17.300 24H23v14H10zM27 30c0-9 5-15 13-18l1.600 3c-5.600 2.600-7.100 6-7.300 9H40v14H27z"/></svg>'


def soc(kind, href, label):
    ic = {'wa': ic_wa(), 'ig': IC_IG, 'map': IC_MAP}[kind]
    return '<a class="soc %s" href="%s" target="_blank" rel="noopener" aria-label="%s">%s</a>' % (kind, href, label, ic)


def ext(href):
    return 'href="%s" target="_blank" rel="noopener"' % href


def words(text, start=0):
    out = []
    for i, w in enumerate(text.split(' ')):
        out.append('<span class="w"><i style="--i:%d">%s</i></span>' % (start + i, w))
    return ' '.join(out)


LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="9" fill="#C9A45C"/>'
        '<path d="M10 29V11l10 12 10-12v18" fill="none" stroke="#14243A" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"/></svg>')

NAVS = [('index.html', 'Beranda'), ('tentang.html', 'Tentang'), ('program.html', 'Program'),
        ('metode.html', 'Metode & Etika'), ('galeri.html', 'Galeri'), ('testimoni.html', 'Testimoni'), ('kontak.html', 'Kontak')]


def header(cur):
    li = ''.join('<li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if h == cur else '', t) for h, t in NAVS)
    mm = ''.join('<li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if h == cur else '', t) for h, t in NAVS)
    return f'''<a class="skip" href="#main">Lewati ke konten</a>
<header class="hd"><div class="wrap in">
<a class="logo" href="index.html" aria-label="Matrix Bimbingan Belajar Dan Etika, ke beranda">{LOGO}<span><b>Matrix</b><small>Bimbingan Belajar dan Etika</small></span></a>
<ul class="nav">{li}</ul>
<a class="btn btn-gold" href="konsultasi.html">Konsultasi</a>
<button class="burger" aria-label="Buka menu" aria-expanded="false" aria-controls="mm"><span></span><span></span><span></span></button>
</div></header>
<div class="mm" id="mm" aria-hidden="true"><ul>{mm}<li><a href="konsultasi.html"{' aria-current="page"' if cur == 'konsultasi.html' else ''}>Konsultasi</a></li></ul>
<div><a class="btn btn-gold" href="{WA_HALO}" target="_blank" rel="noopener">{ic_wa()} Chat WhatsApp</a>
<div class="soc-row">{soc('wa', WA_HALO, 'WhatsApp Matrix')}{soc('ig', IG, 'Instagram Matrix')}{soc('map', MAPS, 'Lokasi Matrix di Google Maps')}</div></div></div>'''


def footer():
    li = ''.join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in NAVS + [('konsultasi.html', 'Konsultasi')])
    return f'''<footer class="ft dark"><div class="wrap"><div class="grid">
<div><a class="logo" href="index.html">{LOGO}<span><b>Matrix</b><small>Bimbingan Belajar dan Etika</small></span></a>
<p>Pusat belajar di Sidoarjo, Jawa Timur. Belajar lebih mudah, tumbuh dengan etika.</p>
<div class="soc-row">{soc('wa', WA_HALO, 'WhatsApp Matrix')}{soc('ig', IG, 'Instagram Matrix')}{soc('map', MAPS, 'Lokasi Matrix di Google Maps')}</div></div>
<div><h3>Halaman</h3><ul>{li}</ul></div>
<div><h3>Hubungi Matrix</h3><ul>
<li>{ALAMAT}</li>
<li><a href="{WA_HALO}" target="_blank" rel="noopener">WhatsApp {WA_SHOW}</a></li>
<li><a {ext(IG)}>Instagram @matrix554</a></li>
<li><a {ext(MAPS)}>Buka di Google Maps</a></li></ul></div>
</div>
<p class="legal">&copy; <span id="yr">2026</span> {NAMA}. Situs ini adalah demo konsep dari SynergyDev. Seluruh informasi, program, foto, dan desain akan diperbarui setelah mendapat persetujuan dan informasi resmi dari pengelola Matrix.</p>
</div></footer>
<a class="fab" href="{WA_HALO}" target="_blank" rel="noopener" aria-label="Konsultasi lewat WhatsApp">{ic_wa()}</a>'''


def cta(title='Ingin tahu lebih dekat cara belajar di Matrix?'):
    return f'''<section class="sec dark cta"><div class="wrap"><div class="rule rv"></div>
<h2 class="d2 rv">{title}</h2>
<p class="lede mt2 rv" style="--d:.1s">Sampaikan kebutuhan belajar anak Anda. Pengelola akan membantu menjawab melalui WhatsApp.</p>
<div class="btn-row rv" style="--d:.2s"><a class="btn btn-gold" href="konsultasi.html">Konsultasi Sekarang</a>
<a class="btn btn-line" href="{WA_HALO}" target="_blank" rel="noopener">{ic_wa()} Chat WhatsApp</a></div></div></section>'''


def page(fname, title, desc, body, extra_head=''):
    html = f'''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#14243A">
<meta property="og:type" content="website"><meta property="og:locale" content="id_ID">
<meta property="og:site_name" content="{NAMA}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add('js')</script>
{extra_head}</head>
<body>
{header(fname)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, fname), 'w', encoding='utf-8') as f:
        f.write(html)


def phero(h1, lede, photo=None):
    ph = '<div class="photo rv" style="--d:.15s">%s</div>' % img(photo, lazy=False) if photo else ''
    return f'''<section class="phero"><div class="wrap"><div class="grid"><div>
<h1 class="d1" style="font-size:clamp(2.4rem,7vw,6.25rem)">{h1}</h1><p class="lede fade-in" style="--d:.7s">{lede}</p></div>{ph}</div></div></section>'''


# ================= BERANDA =================
Q = [
    'Cara mengajarnya mudah dipahami, banyak rumus-rumus simpel yg diajarkan.',
    'Les di matrix itu seru banget saya faham yang di jelaskan pak Agus.',
    'Seru,asik temen temen nya pada baik pak Agus nya juga sangat baik seru dan asik.',
]

jsonld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"EducationalOrganization","name":"%s","address":{"@type":"PostalAddress","streetAddress":"Puri Indah No. HH-39, RT.37/RW.09, Suko","addressLocality":"Sidoarjo","addressRegion":"Jawa Timur","postalCode":"61224","addressCountry":"ID"},"telephone":"+6281252595566","sameAs":["%s"],"aggregateRating":{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"49"}}</script>
''' % (NAMA, IG)

marq = ''.join(img(k, thumb=True) for k in ['belajar-kelas', 'depan-1', 'kebersamaan', 'belajar-meja', 'tari', 'depan-5', 'kelas-ceria', 'lapangan'])
quotes_html = ''.join(
    '<figure class="q%s">%s<blockquote>&ldquo;%s&rdquo;</blockquote><figcaption>Ulasan siswa di Google Maps</figcaption></figure>' % (' on' if i == 0 else '', QM, t)
    for i, t in enumerate(Q))

home = f'''<section class="hero">
<div class="hero-media" aria-hidden="false">{img('belajar-atas', lazy=False)}</div>
<div class="wrap"><div class="hero-copy">
<h1 class="d1"><span style="display:block">{words('Belajar Lebih Mudah,', 0)}</span><span class="l2" style="display:block">{words('Tumbuh dengan Etika.', 3)}</span></h1>
<p class="lede fade-in" style="--d:1.1s">Ruang belajar yang menghadirkan pengalaman pembelajaran menyenangkan, mudah dipahami, dan menanamkan nilai-nilai etika dalam proses belajar.</p>
<div class="btn-row fade-in" style="--d:1.3s"><a class="btn btn-gold" href="konsultasi.html">Konsultasi Sekarang</a><a class="btn btn-line" href="tentang.html">Kenali Matrix</a></div>
</div>
<div class="facts fade-in" style="--d:1.5s">
<a class="fact" {ext(MAPS)}><span class="big"><span data-count="5" data-dec="1">5,0</span></span><span>{STARS}<small>5,0/5,0 dari 49 ulasan Google</small></span></a>
<a class="fact" {ext(MAPS)}><span class="soc map" style="width:44px;height:44px">{IC_MAP}</span><span><strong>Suko, Sidoarjo</strong><small>Puri Indah No. HH-39</small></span></a>
<a class="fact" href="{WA_HALO}" target="_blank" rel="noopener"><span class="soc wa" style="width:44px;height:44px">{ic_wa()}</span><span><strong>{WA_SHOW}</strong><small>Konsultasi lewat WhatsApp</small></span></a>
</div></div></section>

<section class="sec" id="perkenalan"><div class="wrap split">
<div><div class="rule rv"></div><h2 class="d2 rv" style="font-size:clamp(2rem,5vw,4.25rem)">Tempat belajar yang membuat materi terasa lebih dekat.</h2>
<p class="lede mt2 rv" style="--d:.1s">{NAMA} adalah pusat belajar di Sidoarjo, Jawa Timur. Dari ulasan para siswa, belajar di sini terasa nyaman dan seru, penjelasannya mudah diikuti, dan pelajaran sesekali diselingi cerita agar tidak membosankan.</p>
<div class="facts-s rv" style="--d:.2s"><div>Kategori<span>Pusat Belajar</span></div><div>Lokasi<span>Suko, Sidoarjo</span></div><div>Konsultasi<span>Melalui WhatsApp</span></div></div>
<p class="mt3 rv"><a class="link" href="tentang.html">Baca tentang Matrix</a></p></div>
<div class="frame tall offset rvi">{img('kelas-ceria', par='.05')}</div></div></section>

<section class="sec dark"><div class="wrap">
<h2 class="big-st rv">Siswa yang nyaman lebih mudah memahami pelajaran.</h2>
<div class="trio">
<div class="rv"><h3 class="h3">Berani bertanya</h3><p>Suasana yang akrab membuat siswa tidak ragu menyampaikan apa yang belum dimengerti.</p></div>
<div class="rv" style="--d:.1s"><h3 class="h3">Fokus lebih terjaga</h3><p>Belajar yang tidak tegang membantu perhatian bertahan lebih lama dan materi lebih mudah diserap.</p></div>
<div class="rv" style="--d:.2s"><h3 class="h3">Belajar terasa ringan</h3><p>Saat prosesnya menyenangkan, siswa lebih terdorong untuk kembali belajar dengan semangat.</p></div>
</div></div></section>

<section class="sec"><div class="wrap">
<div class="split"><div><h2 class="d2 rv" style="font-size:clamp(2rem,5vw,4.25rem)">Pengalaman belajar yang dirasakan siswa.</h2></div>
<p class="lede rv" style="--d:.1s">Tiga hal yang paling sering muncul dalam ulasan Google Maps tentang Matrix.</p></div>
<div class="rows mt4">
<div class="rv"><h3 class="h3">Dijelaskan dengan sederhana</h3><p>Ulasan menyebut cara mengajar yang mudah dipahami, dengan rumus-rumus yang disampaikan secara sederhana sehingga siswa merasa terbantu memahami materi.</p></div>
<div class="rv"><h3 class="h3">Diselingi cerita dan candaan</h3><p>Pembelajaran kadang diselingi cerita dan candaan, sehingga suasana kelas terasa seru dan tidak membosankan.</p></div>
<div class="rv"><h3 class="h3">Etika ikut tumbuh</h3><p>Nilai-nilai baik diperkenalkan dalam proses belajar. Salah satu ulasan bahkan menyebut pembelajaran yang diselingi cerita Islami.</p></div>
</div>
<p class="mt3 rv"><a class="link" href="metode.html">Lihat metode belajar dan etika</a></p></div></section>

<section class="sec-sm"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap;margin-bottom:32px">
<h2 class="h2 rv">Dokumentasi kegiatan</h2><a class="link rv" href="galeri.html">Lihat semua foto</a></div></div>
<div class="marq" role="region" aria-label="Foto dokumentasi kegiatan Matrix"><div class="marq-t">{marq}</div></div></section>

<section class="sec dark"><div class="wrap">
<h2 class="h2">Kata mereka yang belajar di Matrix</h2>
<div class="quotes" aria-live="off">{quotes_html}</div>
<div class="dots" role="group" aria-label="Pilih ulasan"><button aria-label="Ulasan 1" aria-current="true"></button><button aria-label="Ulasan 2" aria-current="false"></button><button aria-label="Ulasan 3" aria-current="false"></button></div>
<p class="mt2"><a class="link" href="testimoni.html">Baca semua testimoni</a></p></div></section>

<section class="sec"><div class="wrap split rev">
<div><div class="rule rv"></div><h2 class="d2 rv" style="font-size:clamp(2rem,5vw,4.25rem)">Datang dan lihat sendiri suasananya.</h2>
<p class="lede mt2 rv" style="--d:.1s">{ALAMAT}.</p>
<div class="btn-row mt3 rv" style="--d:.2s"><a class="btn btn-navy" href="{WA_HALO}" target="_blank" rel="noopener">{ic_wa()} Konsultasi via WhatsApp</a>
<a class="btn btn-ink" {ext(MAPS)}>{IC_MAP} Buka Google Maps</a></div>
<div class="btn-row mt2 rv" style="--d:.3s">{soc('ig', IG, 'Instagram Matrix')}{soc('map', MAPS, 'Lokasi Matrix di Google Maps')}{soc('wa', WA_HALO, 'WhatsApp Matrix')}</div></div>
<div class="frame offset rvi">{img('bangunan', par='.04')}</div></div></section>
'''
page('index.html', 'Matrix Bimbingan Belajar Dan Etika | Pusat Belajar di Sidoarjo',
     'Matrix Bimbingan Belajar Dan Etika, pusat belajar di Suko, Sidoarjo. Belajar lebih mudah, tumbuh dengan etika. Rating Google 5,0 dari 49 ulasan.', home, jsonld)

# ================= TENTANG =================
tentang = phero('Mengenal Matrix', 'Pusat belajar di Sidoarjo yang percaya bahwa materi lebih mudah dipahami ketika siswa merasa nyaman, dan bahwa etika layak tumbuh bersama ilmu.', 'papan-nama') + f'''
<section class="sec"><div class="wrap split">
<div><div class="rule rv"></div><h2 class="d2 rv" style="font-size:clamp(2rem,5vw,4.25rem)">Pusat belajar yang akrab di Suko, Sidoarjo.</h2>
<p class="lede mt2 rv" style="--d:.1s">{NAMA} berada di Puri Indah, Suko, Sidoarjo. Ulasan siswa menggambarkan tempat belajar yang menyenangkan, dengan penjelasan yang mudah dipahami dan teman-teman yang baik.</p>
<p class="mt2 rv" style="--d:.15s;color:var(--muted)">Bagi Matrix, belajar bukan hanya soal menyelesaikan soal. Belajar adalah proses yang sebaiknya membuat siswa merasa dihargai, berani bertanya, dan ingin terus mencoba.</p></div>
<div class="frame tall offset rvi">{img('kebersamaan', par='.05')}</div></div></section>

<section class="sec dark"><div class="wrap">
<h2 class="big-st rv">Belajar yang baik dimulai dari rasa nyaman dan dipahami.</h2>
<div class="trio">
<div class="rv"><h3 class="h3">Mudah dipahami</h3><p>Materi dan rumus dijelaskan dengan cara sederhana, agar siswa mengerti alurnya, bukan sekadar menghafal.</p></div>
<div class="rv" style="--d:.1s"><h3 class="h3">Akrab dan menyenangkan</h3><p>Suasana kelas dibuat hangat. Cerita dan candaan sesekali hadir agar belajar tidak terasa membosankan.</p></div>
<div class="rv" style="--d:.2s"><h3 class="h3">Etika sebagai bekal</h3><p>Nilai-nilai baik ikut diperkenalkan dalam proses belajar, karena ilmu bermanfaat saat dibawa dengan adab yang baik.</p></div>
</div></div></section>

<section class="sec"><div class="wrap split rev">
<div><h2 class="d2 rv" style="font-size:clamp(2rem,5vw,4.25rem)">Etika bukan pelajaran tambahan, melainkan bagian dari belajar.</h2>
<p class="lede mt2 rv" style="--d:.1s">Pendidikan yang utuh tidak berhenti pada nilai. Sikap menghargai guru dan teman, kejujuran, serta kebiasaan baik tumbuh lewat contoh dan percakapan sehari-hari di kelas.</p>
<div class="btn-row mt3 rv" style="--d:.2s"><a class="btn btn-navy" href="metode.html">Lihat metode belajar</a><a class="btn btn-ink" href="galeri.html">Lihat galeri</a></div></div>
<div class="frame offset rvi">{img('depan-4', par='.04')}</div></div></section>
''' + cta()
page('tentang.html', 'Tentang Matrix | Matrix Bimbingan Belajar Dan Etika',
     'Kenali Matrix Bimbingan Belajar Dan Etika di Sidoarjo: suasana belajar yang akrab, penjelasan yang mudah dipahami, dan nilai etika dalam proses belajar.', tentang)

# ================= PROGRAM =================
PROG = [
    ('Bimbingan Belajar', 'Pendampingan belajar dalam suasana yang akrab, agar siswa lebih berani bertanya dan memahami pelajaran dengan caranya sendiri.', 'belajar-kelas'),
    ('Pendampingan Materi Sekolah', 'Membantu siswa memahami materi yang sedang dipelajari di sekolah, dijelaskan dengan bahasa yang sederhana dan mudah diikuti.', 'belajar-meja'),
    ('Pembelajaran dan Pemahaman Rumus', 'Rumus tidak sekadar dihafal. Pengajar menyampaikannya dengan cara yang sederhana, seperti yang disebut dalam ulasan siswa.', 'belajar-atas'),
    ('Pembelajaran Berbasis Nilai dan Etika', 'Nilai-nilai baik diperkenalkan di sela kegiatan belajar, melalui cerita dan teladan, sesuai pendekatan yang diterapkan Matrix.', 'kebersamaan'),
]
prog_html = ''
for n, dsc, k in PROG:
    link = wa('Halo Matrix Bimbingan Belajar Dan Etika, saya ingin berkonsultasi tentang program %s.' % n)
    prog_html += f'''<article class="prog"><div class="frame rvi">{img(k, par='.03')}</div>
<div class="rv"><h2 class="h2">{n}</h2><p class="lede">{dsc}</p>
<a class="btn btn-navy" href="{link}" target="_blank" rel="noopener">{ic_wa()} Konsultasi program ini</a></div></article>'''
program = phero('Program bimbingan belajar', 'Empat bidang pendampingan yang menjadi arah belajar di Matrix.', 'belajar-kelas') + f'''
<section class="sec"><div class="wrap">{prog_html}
<p class="lede mt3 rv">Jenjang, mata pelajaran, jadwal, dan biaya dapat ditanyakan langsung melalui WhatsApp. Pengelola akan menjelaskan pilihan yang sesuai dengan kebutuhan siswa.</p></div></section>
''' + cta('Bingung memilih program yang tepat?')
page('program.html', 'Program Bimbingan Belajar | Matrix Bimbingan Belajar Dan Etika',
     'Program Matrix Bimbingan Belajar Dan Etika di Sidoarjo: bimbingan belajar, pendampingan materi sekolah, pemahaman rumus, dan pembelajaran berbasis nilai dan etika.', program)

# ================= METODE =================
metode = phero('Cara Matrix mengajar', 'Mudah dipahami, tidak membosankan, dan tetap berpegang pada etika. Inilah yang paling sering dirasakan siswa.', None) + f'''
<section class="sec dark" style="padding-top:0"><div class="wrap stick">
<div class="side"><div class="frame rvi">{img('kelas-ceria')}</div></div>
<div>
<div class="blk rv"><h2 class="h2">Dijelaskan dengan cara yang mudah dipahami</h2><p>Materi disampaikan runtut dan bersahabat, supaya siswa mengerti alurnya dan merasa terbantu.</p>
<q>Cara mengajarnya mudah dipahami, banyak rumus-rumus simpel yg diajarkan.</q></div>
<div class="blk rv"><h2 class="h2">Rumus dan konsep yang sederhana</h2><p>Rumus dijelaskan dengan cara yang disederhanakan, sehingga tidak terasa menakutkan dan lebih mudah diingat.</p></div>
<div class="blk rv"><h2 class="h2">Santai, seru, tidak membosankan</h2><p>Suasana belajar dibuat lebih santai. Pembelajaran dapat diselingi cerita dan candaan agar siswa tetap bersemangat.</p>
<q>Les di matrix itu seru banget saya faham yang di jelaskan pak Agus.</q></div>
<div class="blk rv"><h2 class="h2">Etika tumbuh lewat cerita</h2><p>Nilai etika dan cerita Islami dapat diperkenalkan di sela belajar, sesuai pendekatan yang diterapkan Matrix. Detail pelaksanaannya dapat ditanyakan langsung kepada pengelola.</p></div>
</div></div></section>

<section class="sec"><div class="wrap"><div class="split rev">
<div><h2 class="d2 rv" style="font-size:clamp(2rem,5vw,4.25rem)">Belajar yang membuat siswa ingin kembali.</h2>
<p class="lede mt2 rv" style="--d:.1s">Lihat sendiri suasana kegiatan belajar di Matrix lewat dokumentasi kegiatan.</p>
<div class="btn-row mt3 rv" style="--d:.2s"><a class="btn btn-navy" href="galeri.html">Buka galeri</a><a class="btn btn-ink" href="testimoni.html">Baca testimoni</a></div></div>
<div class="frame offset rvi">{img('belajar-meja', par='.04')}</div></div></div></section>
''' + cta('Ingin anak merasakan cara belajar seperti ini?')
page('metode.html', 'Metode Belajar dan Etika | Matrix Bimbingan Belajar Dan Etika',
     'Metode belajar Matrix: materi dan rumus dijelaskan sederhana, suasana santai dan tidak membosankan, serta nilai etika yang diperkenalkan dalam proses belajar.', metode)

# ================= GALERI =================
GAL = [
    ('belajar', 'belajar-atas'), ('kebersamaan', 'depan-1'), ('belajar', 'kelas-ceria'), ('lokasi', 'bangunan'),
    ('kebersamaan', 'kebersamaan'), ('kegiatan', 'tari'), ('belajar', 'belajar-kelas'), ('kebersamaan', 'depan-5'),
    ('lokasi', 'papan-nama'), ('belajar', 'belajar-meja'), ('kebersamaan', 'depan-2'), ('kegiatan', 'lapangan'),
    ('kebersamaan', 'depan-3'), ('kebersamaan', 'depan-4'), ('kebersamaan', 'depan-6'),
]
gi = ''.join(f'''<figure class="gi" data-c="{c}"><button type="button" data-full="assets/img/{k}.jpg" aria-label="Perbesar foto: {CAP[k]}">{img(k, thumb=True)}</button><figcaption>{CAP[k]}</figcaption></figure>''' for c, k in GAL)
galeri = phero('Galeri kegiatan', 'Dokumentasi asli suasana belajar dan kebersamaan di Matrix. Klik foto untuk memperbesar.', None) + f'''
<section class="sec-sm"><div class="wrap">
<div class="filters" role="group" aria-label="Filter kategori foto">
<button data-f="all" aria-pressed="true">Semua</button><button data-f="belajar" aria-pressed="false">Belajar</button><button data-f="kebersamaan" aria-pressed="false">Kebersamaan</button><button data-f="kegiatan" aria-pressed="false">Kegiatan</button><button data-f="lokasi" aria-pressed="false">Lokasi</button></div>
<p class="g-status" role="status" style="position:absolute;left:-999px">Menampilkan {len(GAL)} foto</p>
<div class="masonry">{gi}</div></div></section>
''' + cta('Tertarik melihat langsung suasananya?')
page('galeri.html', 'Galeri Kegiatan | Matrix Bimbingan Belajar Dan Etika',
     'Galeri foto kegiatan belajar dan kebersamaan di Matrix Bimbingan Belajar Dan Etika, Sidoarjo.', galeri)

# ================= TESTIMONI =================
tq = ''.join(f'<figure class="tq rv"><blockquote>&ldquo;{t}&rdquo;</blockquote><cite>Ulasan siswa di Google Maps</cite></figure>' for t in Q)
testi = phero('Kata mereka yang belajar di Matrix', 'Kutipan langsung dari ulasan Google Maps, ditampilkan apa adanya.', None) + f'''
<section class="sec"><div class="wrap">
<div class="rate rv"><div class="num"><span data-count="5" data-dec="1">5,0</span></div>
<div>{STARS}<p class="mt1" style="font-weight:700;font-size:1.2rem">Rating Google Maps 5,0 dari 49 ulasan</p></div>
<a class="btn btn-gold" {ext(MAPS)}>{IC_MAP} Lihat di Google Maps</a></div>
<div class="mt4">{tq}</div>
<div style="border-top:1px solid var(--line)"></div></div></section>
''' + cta('Giliran anak Anda merasakan belajar yang seru.')
page('testimoni.html', 'Testimoni | Matrix Bimbingan Belajar Dan Etika',
     'Ulasan siswa Matrix Bimbingan Belajar Dan Etika di Google Maps: rating 5,0 dari 49 ulasan.', testi)

# ================= KONSULTASI =================
opts = ''.join('<option>%s</option>' % o for o in [n for n, _, _ in PROG] + ['Belum yakin, ingin berdiskusi dulu'])
kons = phero('Konsultasi dan pendaftaran', 'Isi formulir singkat ini. Pesan Anda akan otomatis tersusun di WhatsApp Matrix.', None) + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
<form class="form" id="form-konsultasi" novalidate>
<div class="two"><div class="fld"><label for="nama">Nama orang tua atau siswa</label><input id="nama" name="nama" autocomplete="name" required aria-describedby="e-nama"><p class="err" id="e-nama" role="alert"></p></div>
<div class="fld"><label for="hp">Nomor WhatsApp</label><input id="hp" name="hp" type="tel" inputmode="tel" autocomplete="tel" placeholder="0812xxxxxxx" required aria-describedby="e-hp"><p class="err" id="e-hp" role="alert"></p></div></div>
<div class="fld"><label for="kelas">Jenjang atau kelas <small>(opsional)</small></label><input id="kelas" name="kelas" placeholder="Contoh: kelas 7"></div>
<div class="fld"><label for="kebutuhan">Kebutuhan belajar</label><select id="kebutuhan" name="kebutuhan" required aria-describedby="e-kebutuhan"><option value="">Pilih kebutuhan belajar</option>{opts}</select><p class="err" id="e-kebutuhan" role="alert"></p></div>
<div class="fld"><label for="pesan">Pesan tambahan <small>(opsional)</small></label><textarea id="pesan" name="pesan" placeholder="Ceritakan kebutuhan atau pertanyaan Anda"></textarea></div>
<div><button class="btn btn-navy" type="submit">{ic_wa()} Kirim lewat WhatsApp</button><p class="note">Setelah dikirim, WhatsApp akan terbuka dengan pesan yang sudah terisi. Pesan baru terkirim setelah Anda menekan kirim di WhatsApp.</p><p class="status mt1" role="status"></p></div>
</form>
<aside><div class="poster rvi">{img('poster')}</div>
<p class="note">Poster dari Matrix. Jenjang, mata pelajaran, jadwal, dan biaya dapat dikonfirmasi langsung melalui WhatsApp.</p></aside>
</div></section>'''
page('konsultasi.html', 'Konsultasi dan Pendaftaran | Matrix Bimbingan Belajar Dan Etika',
     'Konsultasi dan pendaftaran Matrix Bimbingan Belajar Dan Etika di Sidoarjo. Isi formulir dan lanjutkan percakapan lewat WhatsApp.', kons)

# ================= KONTAK =================
kontak = phero('Kontak dan lokasi', 'Hubungi pengelola untuk bertanya tentang program dan jadwal, atau kunjungi Matrix di Puri Indah, Suko, Sidoarjo.', None) + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
<div><div class="cards">
<a class="cc rv" href="{WA_HALO}" target="_blank" rel="noopener"><span class="soc wa">{ic_wa()}</span><span><small>WhatsApp</small><strong>{WA_SHOW}</strong></span></a>
<a class="cc rv" {ext(IG)} style="--d:.05s"><span class="soc ig">{IC_IG}</span><span><small>Instagram</small><strong>@matrix554</strong></span></a>
<a class="cc rv" {ext(MAPS)} style="--d:.1s"><span class="soc map">{IC_MAP}</span><span><small>Alamat</small><strong>{ALAMAT}</strong></span></a></div>
<p class="note mt2">Untuk informasi jadwal, calon siswa dapat menghubungi pengelola melalui WhatsApp.</p>
<div class="btn-row mt3"><a class="btn btn-navy" href="konsultasi.html">Konsultasi Sekarang</a><a class="btn btn-ink" {ext(MAPS)}>{IC_MAP} Buka Google Maps</a></div></div>
<div><div class="map rv"><iframe title="Peta lokasi Matrix Bimbingan Belajar Dan Etika" src="{MAPS_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<div class="frame mt2 rvi">{img('bangunan')}</div></div></div></section>'''
page('kontak.html', 'Kontak dan Lokasi | Matrix Bimbingan Belajar Dan Etika',
     'Alamat, WhatsApp, dan Instagram Matrix Bimbingan Belajar Dan Etika di Puri Indah, Suko, Sidoarjo, Jawa Timur.', kontak)

print('Selesai: 8 halaman dibuat.')
