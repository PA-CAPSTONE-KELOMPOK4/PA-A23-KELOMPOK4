# PA-A23-KELOMPOK4

# Sistem Informasi Tempat Wisata di Kalimantan Timur
--------------------------------------------------------------------------------------
## Deskripsi Program
Program Sistem Informasi Tempat Wisata di Kalimantan Timur merupakan aplikasi wisata digital yang dirancang untuk memudahkan pengunjung menjelajahi berbagai destinasi menarik di Kalimantan Timur dengan mengakses informasi lengkap tentang tempat wisata. Aplikasi ini mengintegrasikan konten dari berbagai sponsor kemitraan, seperti pemerintah, influencer, hotel, dan agen perjalanan, untuk memberikan opsi wisata dan akomodasi. Fitur utama aplikasi ini adalah sistem bookmark, yang memungkinkan pengguna untuk menyimpan dan melihat daftar wisata yang ingin mereka kunjungi. Dengan begitu, program ini diharapkan dapat mempermudah pengunjung untuk menemukan wisata yang ingin dikunjungi.

Program ini dibuat dengan menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List. Program ini juga menggunakan sebuah database, yaitu database Mysql yang digunakan untuk menyimpan data akun Pengunjung dan admin serta data tempat wisata dan data bookmark.

## Struktur Project
1. Folder Controller: Berisi file-file controller yang akan mengatur alur program serta mengambil data dari model dan menampilkan ke view.
   - File Controller Account, sebagai file controller yang berisi logika untuk memanajemen akun admin dan pengunjung, seperti registrasi akun dan login, serta profil user.
   - File Controller Bookmark, sebagai file controller yang berisi logika untuk memanajemen data bookmark yang telah ditandai oleh pengunjung mengenai wisata yang disimpan.
   - File Controller Linked List, sebagai file controller yang berisi logika untuk memanajemen data wisata dalam bentuk linked list, yang di mana data dalam linked list diambil dari database yang telah dibuat.
   - File Controller User, sebagai file controller yang berisi logika untuk memanajemen data admin dan pengunjung seperti logika menambahkan wisata ke bookmark.
   - File Controller Wisata, sebagai file controller yang berisi logika untuk memanajemen data wisata yang dikelola oleh admin berupa nama wisata, lokasi, dan deskripsi wisata.

2. Folder Model: Berisi file-file model yang berisi fungsi-fungsi untuk mengakses database dan memproses data.
   - File Database, sebagai file yang berisi class untuk menghubungkan Python dan Database.
   - File Wisata, sebagai file yang berisi definisi class Wisata yang digunakan untuk mempresentasikan sebuah node pada struktur data Linked List.

3. Folder View: Berisi file-file view yang berisi tampilan antarmuka aplikasi yang akan dilihat oleh si pengguna.
   - File Main, sebagai file utama yang berfungsi untuk menjalankan program.
   - File Admin, sebagai halaman untuk menampilkan informasi Admin dan melakukan CRUD, Searching, dan Sorting terhadap wisata oleh Admin.
   - File User, sebagai halaman untuk menampilkan informasi Pengunjung dan melihat wisata yang ada, menambahkan daftar wisata yang ingin dikunjungi ke dalam bookmark Pengunjung, mencari serta mengurutkan wisata.

## Fitur
### Pada program ini terdapat library yang digunakan, yaitu berupa PrettyTable, Datetime, MySql, dan os.
1. PrettyTable merupakan library atau pustaka dalam python yang digunakan untuk membuat/mengeluarkan data dalam bentuk tabel.
2. Datetime adalah sebuah library atau modul yang dipanggil jika Anda membutuhkan segala operasi yang berhubungan dengan waktu.
3. MySql berupa sistem manajemen basis data yang digunakan di dalam program dengan data disimpan dalam bentuk tabel yang terkait satu sama lain dengan kunci asing yang memungkinkan pengguna untuk mengakses dan mengelola data dengan cara yang terstruktur. 
4. Modul os dapat digunakan untuk berinterkasi dengan sistem operasi dan melakukan operasi pada file dan folder.

### Beberapa fitur yang terdapat pada program ini, yaitu:
- User Pengunjung
  1. Melihat wisata: Pengunjung dapat melihat semua daftar wisata.
  2. Melakukan bookmark: Pengunjung dapat menambahkan daftar wisata yang ingin dikunjungi ke dalam bookmark Pengunjung.
  3. Mencari wisata: Pengunjung dapat mencari wisata yang diinginkan untuk mengunjungi wisata tersebut.
  4. Mengurutkan wisata: Pengunjung dapat mengurutkan wisata berdasarkan abjad awal dari a-z atau z-a.
  5. Melihat profil: Pengunjung dapat melihat profil yang berisi data diri.
     
- Admin
  1. Melakukan CRUD: Admin dapat membuat, melihat, memperbarui, dan menghapus wisata yang dikelola.
  2. Melakukan Searching: Admin dapat melakukan pencarian wisata yang diinginkan.
  3. Melakukan Sorting: Admin dapat melakukan pengurutan wisata sesuai abjad dari huruf a-z atau z-a.
  4. Menghubungi sponsor: Admin dapat menghubungi sponsor untuk melakukan kerjasama untuk membantu mempromosikan wisata dengan melakukan kesepakatan yang telah disetujui antar kedua belah pihak.

## Fungsionalitas 
1. Login dan Logout (Exit). User Admin dapat login ke dalam sistem menggunakan username dan password. Sedangkan User Pengunjung dapat login ke dalam sistem menggunakan username dan ID. User Admin dan Pengunjung juga dapat keluar dari program dengan memilih pilihan Exit.
2. Registrasi Pengunjung. Pengunjung dapat melakukan pendaftaran untuk masuk ke dalam sistem untuk dapat melihat wisata, bookmark wisata, mencari dan mengurutkan wisata. Pengunjung harus memberikan informasi pribadi seperti nama, jenis kelamin, dan usia.
3. Melakukan bookmark. Pengunjung dapat menambahkan daftar wisata yang ingin dikunjungi ke dalam bookmark.


### Cara Penggunaan
- tampilan menu utama
  ![Screenshot 2024-04-30 085200](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/9ea8986f-46a0-4870-85e6-16318f8677bb)

- Jika pilih "1" maka akan menuju ke login pengunjung
  ![Screenshot 2024-04-30 085209](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/917fecd4-2db8-45fc-9114-0865b3512dce)

- jika pilih "1" maka akan muncul tampilan registrasi akun pengunjung yang dimana pengunjung akan memasukkan nama, jenis kelamin, dan usia. jika registrasi berhasil maka pengunjung akan mendapatkan ID akun untuk dipakai pengunjung pada saat login. 
![Screenshot 2024-04-30 085301](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/0a666f0a-5b5b-4836-ad00-ade887a3d70c)


