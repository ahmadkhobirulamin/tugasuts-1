
class menukopi:
    def __init__(self, kopi):
        self.kopi = kopi
        

p1 =menukopi("ES Kopi Susu : Rp 11.000")
p2 =menukopi("ES Kopi Coklat : Rp 12.000")
p3 =menukopi("ES Kopi Hitam : Rp 11.000")
p4 =menukopi("Ice Americano : Rp 14.000")

print('Selamat datang!')
while True:
    print('---Menu---')
    print('1.Kopi susu')
    print('2.Kopi coklat')
    print('3.Kopi Hitam')
    print('4.Ice Americano')
    
    menu = int(input('Pilih Menu: '))
    jumlahpesan=int(input("masukkan jumlah pesanan : "))
    
    
    if menu == 1:
        print(p1.kopi)
        harga = 11000 * jumlahpesan
        print("Total yang harus di bayar Rp." +str(harga))
        
    elif menu == 2:
        print(p2.kopi)
        harga = 12000 * jumlahpesan
        print("Total yang harus di bayar Rp." +str(harga))
        
    elif menu == 3:
        print(p3.kopi)
        harga = 11000 * jumlahpesan
        print("Total yang harus di bayar Rp." +str(harga))
        
    elif menu == 4:
        print(p4.kopi)
        harga = 14000 * jumlahpesan
        print("Total yang harus di bayar Rp." +str(harga))
        
        print("--------------------------")
        print("khobir Coffe")
        print("--------------------------")
        print("Jumlah Pesan :", jumlahpesan)
        print("--------------------------")
        print("Jumlah Bayar :", harga)
        print("--------------------------")
        pilihan=input("apakah anda ingin order kembali Y/N =")  
            