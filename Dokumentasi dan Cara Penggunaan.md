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
  Disini user bisa memilih login sebagai admin, login sebagai pengunjung dan keluar dari program.
  
   ![Screenshot 2024-05-01 085420](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/9688638f-b3c8-4ce7-b49e-6eb81deeb98c)



## Menu Pengunjung

- Jika pilih "1" maka akan menuju ke login pengunjung
  
  ![Screenshot 2024-04-30 085209](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/917fecd4-2db8-45fc-9114-0865b3512dce)


- Didalam menu login pengunjung terdapat 3 pilihan. jika pilih "1" maka akan muncul tampilan registrasi akun pengunjung yang dimana pengunjung akan memasukkan nama, jenis      kelamin, dan usia. jika registrasi berhasil maka pengunjung akan mendapatkan ID akun untuk dipakai pengunjung pada saat login.
  
  ![Screenshot 2024-04-30 085301](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/0a666f0a-5b5b-4836-ad00-ade887a3d70c)


- Jika pengunjung telah memiliki atau membuat akun maka bisa login dengan memilih pilihan "2" yang dimana pengunjung dapat login menggunakan nama lengkap dan ID pengunjung     yang didapatkan saat registrasi

  ![Screenshot 2024-04-30 085406](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/52b0c54f-8b0d-4f8d-99f0-2755de863b50)


- Didalam menu pengunjung terdapat 6 pilihan yang dapat dipilih. Yang pertama pengunjung dapat mencari tempat wisata dengan memasukkan nama wisata yang ingin dicari

  ![Screenshot 2024-05-01 085639](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/06ec7c3a-633b-436c-97e2-209d100a15ee)



- Didalam Pilihan "2" yaitu lihat wisata memungkinkan pengunjung untuk melihat daftar wisata yang ada di Kalimantan Timur

  ![Screenshot 2024-05-01 085717](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/6baae0d1-f0dd-4c4a-82eb-6743cf26b4f7)



- Pada Pilihan "3" yaitu Urutkan wisata. Pengunjung dapat mengurutkan wisata berdasarkan nama dari awalan A-Z dan Z-A

  ![Screenshot 2024-05-01 085746](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/ef955653-8093-4c4b-9057-ea626e318a2d)


  ![Screenshot 2024-05-01 085803](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/eae97141-3cde-454d-9824-d03952254ef8)


- Didalam pilihan "4" ada bookmark yang berguna untuk menyimpan tempat wisata yang pengunjung inginkan. Jika pilih "1" maka pengunjung bisa melihat tempat wisata yang telah ditambahkan ke bookmark

   ![Screenshot 2024-04-30 101945](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/aea0ffc5-8c9e-47d7-8998-318499bf0097)

  jika pilih "2" maka pengunjung bisa memasukkan tempat wisata yang       diinginkan ke dalam bookmark

   ![Screenshot 2024-04-30 102014](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/dfa49650-5f56-4af6-9b36-24698715c252)


- Pada pilihan "5" pengunjung bisa melihat profil mereka yang berisi ID pengunjung, nama pengunjung, jenis kelamin, dan usia.

   ![Screenshot 2024-04-30 101903](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/ce3d3aad-8837-4831-bcd1-b5dec52242b2)


## Menu Admin

- Untuk masuk kedalam menu admin maka admin harus login terlebih dahulu dengan memasukkan username dan password admin.

  ![Screenshot 2024-04-30 151847](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/c30ebc07-d6a3-49fa-a952-14fb81c5f32b)

  jika telah berhasil login maka akan muncul 8 pilihan yang dapat dipilih


- Pilihan yang pertama yaitu tambah wisata. Admin dapat menambahkan tempat wisata dengan memasukkan ID, nama, deskripsi, dan lokasi

  ![Screenshot 2024-04-30 152550](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/ec6c3bc3-38ae-43bf-b4ed-87c06c9d7339)


- Pilihan yang kedua yaitu Lihat wisata. Admin dapat melihat daftar wisata yang telah dimasukkan ke dalam program

   ![Screenshot 2024-05-01 085717](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/ccf8f8f9-4a23-4e79-b294-498dde92f128)



- pilihan yang ketiga yaitu edit wisata. Dibagian ini admin dapat merubah informasi dari daftar wisata yang telah tersedia. Admin dapat mengganti nama, deskripsi, dan lokasi baru

  ![Screenshot 2024-04-30 153149](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/abf03502-5891-4562-9a8c-b16fd2cc008a)


- Pilihan yang keempat yaitu hapus wisata. Admin dapat menghapus wisata dengan memasukkan ID wisata yang ingin dihapus.

  ![Screenshot 2024-04-30 153301](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/2e9defb5-c071-4a30-af30-f90547d9b706)


- Pilihan yang kelima yaitu cari wisata. Admin dapat mencari tempat wisata dengan mencari menggunakan nama wisata.

  ![Screenshot 2024-05-01 085639](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/09aa957f-c420-4614-ae6b-2c34d70501be)



- Pilihan yang kelima yaitu urutkan wisata. Didalam pilihan ini admin dapat mengurutkan wisata berdasarkan nama dari awalan A-Z dan Z-A

  ![Screenshot 2024-05-01 085746](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/15435bc8-206e-4e09-8765-6263f9553a46)


  ![Screenshot 2024-05-01 085803](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/b1ee49a6-926c-4f96-a4bf-3823190a1da2)


- Pilihan yang ke tujuh yaitu hubungi sponsor. Admin dapat lihat daftar sponsor dan menghubungi pihak-pihat tertentu untuk bisa melakukan sebuah kerja sama untuk meningkatkan daya tarik dari wisata yang ada di Kalimantan Timur.
  
  Pilihan "1" untuk melihat daftar sponsor

  ![Screenshot 2024-04-30 153939](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/5b917b64-9062-480e-a987-cd283c5b97fd)

  pilihan "2" untuk menghubungi sponsor dengan memasukkan nama instansi yang dituju, kontak sponsor, alamat, dan deskripsi penawaran kerja sama

  ![Screenshot 2024-04-30 154223](https://github.com/PA-CAPSTONE-KELOMPOK4/PA-A23-KELOMPOK4/assets/144673468/b99b0dbc-92f4-44da-b98e-e83843496b14)

- Pilihan ke delapan yaitu untuk keluar dari program







  





