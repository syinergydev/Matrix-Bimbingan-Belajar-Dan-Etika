# Website Matrix Bimbingan Belajar Dan Etika (demo konsep SynergyDev)

Situs statis multi-halaman: tanpa backend, tanpa database. Siap untuk GitHub Pages.

## Pasang di GitHub Pages
1. Unggah seluruh isi folder ini ke repositori (index.html harus ada di akar).
2. Settings > Pages > Deploy from a branch > pilih branch utama dan folder / (root).

## Mengedit konten
- Teks, tautan, dan susunan halaman: edit `_source/build.py`, lalu jalankan `python3 _source/build.py` (butuh Python + Pillow). Semua halaman .html dibuat ulang.
- Atau edit langsung file .html (header dan footer ada di setiap halaman).
- Warna dan font: bagian `:root` di `assets/css/style.css`.
- Foto: `assets/img/` (versi penuh dan versi kecil berawalan `t-`).
- Nomor WhatsApp, Instagram, dan Google Maps: bagian atas `_source/build.py` dan `assets/js/main.js` (konstanta NUM).
