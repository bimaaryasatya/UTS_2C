def hargabarang():
        jumlah_barang = int(input('Masukkan Jumlah Barang: '))
        harga_barang = int(input('Masukkan Jumlah Barang: '))
        Total = jumlah_barang * harga_barang
        print(f'Jumlah Barang = {jumlah_barang}\n',f'Harga Barang = {harga_barang}\n',f'Total Belanjaan = Rp.{Total:,.2f}')

hasil = hargabarang()
print(hasil)
