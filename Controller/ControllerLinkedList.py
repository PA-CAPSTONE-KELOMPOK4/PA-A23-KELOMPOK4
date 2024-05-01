from Model.Database import Database
from Model.Wisata import WisataLinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def reset_data(self):
        self.head = None

    def refresh(self):
        self.reset_data()
        results = self.get_data()
        for result in results:
            id_wisata = result ["ID_Wisata"]
            nama_wisata = result ["Nama_Wisata"]
            deskripsi = result["Deskripsi"]  
            lokasi = result["Lokasi"] 
            self.add_wisata(id_wisata, nama_wisata, deskripsi, lokasi)

    def get_data(self):
        db = Database()
        return db.get_wisata()

    def lihat_wisata(linked_list):
        current_node = linked_list.head
        if not current_node:
            print("Tidak ada data wisata.")
            return

        while current_node:
            print("--------------------------------------------------------------")
            print("ID Wisata   :", current_node.id_wisata)
            print("Nama Wisata :", current_node.nama_wisata)
            print("Lokasi      :", current_node.lokasi)
            # hanya menampilkan 50 karakter dari deskripsi
            preview_desc = current_node.deskripsi[:50] + "..." if len(current_node.deskripsi) > 50 else current_node.deskripsi
            print("Deskripsi   :", preview_desc)
            
            user_input = input("Ingin lihat deskripsi lengkap? (y/t): ").lower()
            if user_input == 'y':
                print("Deskripsi Lengkap:", current_node.deskripsi)
                print("--------------------------------------------------------------")
            
            continue_choice = input("Tekan 'k' untuk berhenti melihat wisata, atau tekan enter untuk melanjutkan... ").lower()
            if continue_choice == 'k':
                print("Keluar dari daftar wisata.")
                break

            current_node = current_node.next
        print("--------------------------------------------------------------")

    def lihatWisataBookmark(linked_list) :
        current_node = linked_list.head
        while current_node:
            print("ID         :", current_node.id_wisata)
            print("Nama Wisata:", current_node.nama_wisata)
            print("Lokasi     :", current_node.lokasi)
            print("--------------------------------------------------------------")
            current_node = current_node.next

    def add_wisata(self, id_wisata, nama_wisata, deskripsi, lokasi):
        wisata_baru = WisataLinkedList(id_wisata, nama_wisata, deskripsi, lokasi)
        if not self.head:
            self.head = wisata_baru
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = wisata_baru

    def delete_wisata(self, id_wisata):
        current_node = self.head
        if current_node and current_node.id_wisata == id_wisata:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_node.id_wisata != id_wisata:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        previous_node.next = current_node.next
        current_node = None

    def find_wisata(self, id_wisata):
        current_node = self.head
        while current_node:
            if current_node.id_wisata == id_wisata:
                return current_node
            current_node = current_node.next
        return None

    def update_wisata(self, id_wisata, nama_wisata, deskripsi, lokasi):
        current_node = self.find_wisata(id_wisata)
        if current_node:    
            if nama_wisata:
                current_node.nama_wisata = nama_wisata
            if deskripsi:
                current_node.deskripsi = deskripsi
            if lokasi:
                current_node.lokasi = lokasi
            print(f"Wisata dengan ID {id_wisata} telah diperbarui.")
        else:
            print(f"Wisata dengan ID {id_wisata} telah diperbarui.")

    def quickSortNamaWisata(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        smaller_head = None
        equal_head = pivot
        larger_head = None
        current = head.next
        while current is not None:
            next_node = current.next
            if current.nama_wisata < pivot.nama_wisata:
                current.next = smaller_head
                smaller_head = current
            elif current.nama_wisata == pivot.nama_wisata:
                current.next = equal_head
                equal_head = current
            else:
                current.next = larger_head
                larger_head = current
            current = next_node
        smaller_head = self.quickSortNamaWisata(smaller_head)
        larger_head = self.quickSortNamaWisata(larger_head)
        if smaller_head is not None:
            temp = smaller_head
            while temp.next is not None:
                temp = temp.next
            temp.next = equal_head
        else:
            smaller_head = equal_head
        pivot.next = larger_head if larger_head is not None else None
        self.head = smaller_head
        return smaller_head

    def sortAscendingNamaWisata(self):
        self.head = self.quickSortNamaWisata(self.head)

    def sortDescendingaNamaWisata(self):
        self.sortAscendingNamaWisata()
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def JumpSearchNamaWisata(self, nama_wisata):
        self.refresh()
        if not self.head:
            print("Tidak ada tempat wisata yang bisa dicari karena data kosong.")
            return None
        
        # Menghitung jumlah total elemen dalam linked list
        total_elemen = 0
        current_node = self.head
        while current_node:
            total_elemen += 1
            current_node = current_node.next
        
        # Menentukan ukuran blok untuk melakukan jump
        ukuran_blok = int(total_elemen ** 0.5)

        current_node = self.head
        prev_node = None

        # Melakukan lompatan ke depan hingga ditemukan blok yang mungkin mengandung elemen yang ingin dicari
        while current_node and current_node.nama_wisata < nama_wisata:
            prev_node = current_node
            for i in range(min(ukuran_blok, total_elemen)):
                if current_node.next:
                    current_node = current_node.next
                else:
                    break

        # Melakukan pencarian linear di dalam blok yang telah ditemukan
        while prev_node:
            if prev_node.nama_wisata == nama_wisata:
                return prev_node
            prev_node = prev_node.next

        # Melanjutkan pencarian secara linear dari current_node jika masih tidak ditemukan di dalam blok
        while current_node:
            if current_node.nama_wisata == nama_wisata:
                return current_node
            current_node = current_node.next

        print(f"Tidak ditemukan tempat wisata dengan nama '{nama_wisata}'. Pastikan penulisan dan penggunaan huruf kapitalnya benar.")
        return None
