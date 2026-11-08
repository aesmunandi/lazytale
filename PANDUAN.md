# Lazy Tale Studio: website + dashboard

Website ini punya dashboard (CMS) gratis di **Pages CMS**. Dari situ kamu bisa menambah karya, mengubah teks, dan mengatur banner showreel tanpa menyentuh kode.

## Isi folder

| Folder / file | Isinya |
|---|---|
| `index.html` | Halaman website |
| `content/projects.json` | Daftar karya (diedit lewat dashboard) |
| `content/showreel.json` | Urutan gambar di banner showreel |
| `content/site.json` | Email, Discord, Instagram, dan teks intro |
| `images/` | Semua gambar. Upload baru masuk ke `images/uploads/` |
| `.pages.yml` | Pengaturan dashboard. Jangan dihapus |
| `.github/workflows/` + `scripts/` | Otomatis mengecilkan gambar baru ke 1.400 px dan memberi watermark |

## Pemasangan (sekali saja)

1. **GitHub.** Buat akun di github.com, lalu buat repository baru, misalnya `lazytale-site`.
2. **Upload isi folder ini** ke repository tersebut: *Add file → Upload files*, lalu drag semua isi folder (termasuk folder `.github` dan file `.pages.yml`). Klik **Commit changes**.
   - Kalau folder berawalan titik tidak ikut terupload lewat browser, pakai aplikasi **GitHub Desktop** (gratis): *Add → Add existing repository*, pilih folder ini, lalu **Publish**.
3. **Izinkan watermark otomatis.** Di repository: *Settings → Actions → General → Workflow permissions* → pilih **Read and write permissions** → **Save**.
4. **Hosting gratis.** Masuk ke Netlify atau Cloudflare Pages dengan akun GitHub, pilih repository ini, lalu deploy. Build command dikosongkan, output folder `/` (root).
5. **Dashboard.** Buka **app.pagescms.org**, login dengan GitHub, izinkan akses ke repository `lazytale-site`, lalu pilih repository itu. Dashboard langsung muncul.
6. **Domain (opsional).** Sambungkan domainmu di Netlify atau Cloudflare.

## Pemakaian sehari-hari

**Menambah karya baru**
1. Buka app.pagescms.org → pilih repository → **Portfolio**.
2. Klik tombol **+ Add** di bagian bawah daftar untuk menambah karya.
3. Isi judul, pilih kategori (Book Covers, Game Art, Comic & Webtoon, World Building), lalu upload gambar utama.
4. Opsional: tag, deskripsi, cerita proyek, **Other sizes / versions** (contohnya capsule Steam berbagai ukuran), dan **Process images** (sketsa, studi warna, WIP).
5. Klik **Save**. Sekitar 1–2 menit kemudian website ter-update. Gambar yang baru diupload otomatis dikecilkan dan diberi watermark.

**Mengatur urutan:** urutan di dashboard sama dengan urutan di galeri. Seret item (ikon titik-titik di sampingnya) untuk memindahkannya.

**Menyembunyikan karya:** centang **Hide from website**. Karya tidak dihapus, hanya tidak tampil.

**Banner showreel:** menu **Banner showreel**. Tambah atau hapus gambar, pilih gerakan kamera, dan centang *Neon logo wipe* untuk efek sapuan neon.

**Kontak & intro:** menu **Contact & intro**.

## Catatan

- Upload gambar dengan resolusi biasa saja. Sistem otomatis mengecilkannya ke 1.400 px dan memberi watermark "© LAZY TALE STUDIO", jadi file aslimu tetap aman.
- Kalau gambar baru belum muncul, tunggu 1–2 menit lalu refresh. Website diperbarui dua kali: sekali saat upload, sekali setelah watermark selesai.
- File website ini perlu dibuka lewat alamat web (Netlify/Cloudflare). Kalau `index.html` dibuka langsung dari komputer, galerinya tidak akan muncul.
