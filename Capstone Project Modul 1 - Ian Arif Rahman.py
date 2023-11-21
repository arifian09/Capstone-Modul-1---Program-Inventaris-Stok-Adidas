# Nama : Ian Arif Rahman
# JCDSOL-012


#FITUR PENGEMBANGAN : LOGIN (username:ian , password : 123)
def login(): 
     while True:
      print("############# PROGRAM INVENTARIS STOK ADIDAS #############")
      print("######################### WELCOME ########################")
      username = input('masukan user name : ').lower()
      password = input('masukan password : ')
      if username == 'ian' and password == '123':
        print('>>>> Login Sukses!')
        break
      else:
          print('<<<< Password/username salah, silahkan input ulang!\n')
login()

Menu = ['1. READ REPORT',
        '2. CREATE ITEM',
        '3. UPDATE ITEM',
        '4. DELETE ITEM',
        '5. EXIT'] 

stok = [{'SKU' : 'IE1767','nama': 'sepatu ultraboost light','varian':'green','jumlah':3, 'lokasi':'S01'},
         {'SKU' : 'IF5605','nama': 'sepatu trae young 3','varian':'black','jumlah':8, 'lokasi':'S02'},
         {'SKU' : 'DY6592','nama': 'jersey 3G speed reversibel','varian':'grey','jumlah':5,'lokasi':'J01'},
         {'SKU' : 'IL4789','nama': 'jaket own the run','varian':'white','jumlah':4,'lokasi':'K01'},
         {'SKU' : 'IN9366','nama': 'bola euro 24 training football','varian':'multicolor','jumlah':7,'lokasi':'B01'}]


def Main_Menu () :
    MainMenu = True
    while MainMenu != '5' :
        print ("================ INVENTARIS STOK ADIDAS ================")
        for i in Menu :
            print (i)
        MainMenu = input('Pilih Menu (1/2/3/4/5) : ')
        if MainMenu == '1' :
            Read_Menu()
        elif MainMenu == '2' :
            Create_Menu()
        elif MainMenu == '3' :
            Update_Menu()
        elif MainMenu == '4' :
            Delete_Menu()    
        elif MainMenu == '5':
            print ('--- Thank You ---')
            break 

#READ REPORT
def Read_Menu () : 
    ReadMenu = True
    while ReadMenu != '3' :   
        print ('\n---------- READ REPORT ----------')
        print ('1. Laporan seluruh Data')
        print ('2. Laporan Stok item tertentu')
        print ('3. Kembali ke Menu Utama')
        print ('-----------------------------') 
        ReadMenu = input('Silakan pilih Sub Menu Laporan Data (1/2/3) : ')

        if ReadMenu == '1':
            if len(stok) !=0 :
                print('')
                print ('Daftar Stok item :')
                print('_'*110)
                for j, i in enumerate (stok):
                    print (f"|{j+1}| SKU : {i['SKU']} | nama : {i['nama']:<35}| varian : {i['varian']:<10}| jumlah : {i['jumlah']} | lokasi : {i['lokasi']} | ")
                    print('_'*110)
            else :
                print ('Stok item tidak ada!')

            continue

        elif ReadMenu == '2' :
            if len(stok) !=0 :
                std = input('Masukkan SKU Item : ').upper()
                print (f"Data Item dengan SKU : {std}")
                for j, i in enumerate(stok):
                    if i ['SKU'] == std :
                        print (f"{j+1}. SKU : {i['SKU']}, nama : {i['nama']}, varian : {i['varian']}, jumlah : {i['jumlah']}, lokasi : {i['lokasi']} ") 
                        break
                else :
                    print ('Item tidak Terdaftar!')
            else :
                print ('Item tidak ada!')
        elif ReadMenu == '3':
            break
        else :
            print ('Pilihan Menu tidak ada!')

#CREATE ITEM
def Create_Menu () :
    while True :
        print ('\n----------- CREATE ITEM -----------')
        print ('1. Tambah Data Item')
        print ('2. Kembali ke Menu Utama')
        print('-----------------------------')
        CreateMenu = input('Silakan pilih Sub-Menu add item (1/2) : ')     

        if CreateMenu == '1':
            if len(stok) !=0 :
                addSKU = input('Masukkan SKU item : ').upper()
                for j, i in enumerate (stok):
                    if addSKU == i['SKU'] :
                        print ('item sudah ada!')
                        break

                else : 
                    addNama = input('Masukkan Nama item : ').upper()
                    addVarian = input('Masukkan varian : ').upper()
                    addJml = input('Masukkan Jumlah : ').upper()
                    addLok = input('Masukkan Lokasi : ').upper()

                    tambahan = {
                        'SKU' : '{}'.format(addSKU),
                        'nama' : '{}'.format(addNama),
                        'varian' : '{}'.format(addVarian),
                        'jumlah' : '{}'.format(addJml),
                        'lokasi' : '{}'.format(addLok),
                    }
                    print('item yang ditambahkan adalah : ',tambahan)
                    checkerCreate = input('Apakah sudah benar ? (Y/N) : ').upper()
                    if checkerCreate == 'Y':
                        stok.append(tambahan)
                        print('item berhasil ditambahkan')
                    elif checkerCreate == 'N':
                        print('item tidak ditambahkan')
                    else:
                        continue                


        elif CreateMenu == '2':
            break        

        else :
            print ('Pilihan Menu tidak ada')

#UPDATE ITEM
def Update_Menu () :
    UpdateMenu = True
    while UpdateMenu != '2' :   
        print('\n---------- UPDATE ITEM ----------')
        print ('1. Ubah Data Stok item')
        print ('2. Kembali ke Menu Utama')
        print('-----------------------------') 
        UpdateMenu = input('Silakan pilih Sub-Menu edit (1/2) : ')     

        if UpdateMenu == '1':
           if len(stok) !=0 :
                updtSKU = input('Masukkan SKU item : ').upper()

                for i in range(len(stok)):
                    if updtSKU == stok[i]['SKU'] :
                        print ('item yang ingin diedit : ', stok[i])
                        nameupdt = input('Masukkan kolom yang ingin diedit  : ').lower()

                        if nameupdt == 'SKU' :
                            ubahSKU = input('Update SKU : ').upper()
                            confSKU = input('Apakah Data item diubah ? (Y/N) : ').lower()
                            if confSKU == 'y' :
                                stok[i]['SKU'] = ubahSKU
                                print('Data item berhasil diubah')
                                break
                            elif confSKU == 'n' :
                                print('Data tidak diubah')    

                        if nameupdt == 'nama' :
                            ubahNama = input('Update Nama : ').upper()
                            confNama = input('Apakah Data item diubah ? (Y/N) : ').lower()
                            if confNama == 'y' :
                                stok[i]['nama'] = ubahNama
                                print('Data berhasil diubah')
                                break
                            elif confNama == 'n' :
                                print('Data tidak diubah')

                        if nameupdt == 'varian' :
                            ubahVarian = input('Update varian : ').upper()
                            confVarian = input('Apakah Data varian diubah ? (Y/N) : ').lower()
                            if confVarian == 'y' :
                                stok[i]['varian'] = ubahVarian
                                print('Data berhasil diubah')
                                break
                            elif confVarian == 'n' :
                                print('Data tidak diubah')  

                        if nameupdt == 'jumlah' :
                            ubahJmlh = input('Update jumlah : ').upper()
                            confJml = input('Apakah Data jumlah diubah ? (Y/N) : ').lower()
                            if confJml == 'y' :
                                stok[i]['jumlah'] = ubahJmlh
                                print('Data berhasil diubah')
                                break
                            elif confJml == 'n' :
                                print('Data tidak diubah') 

                        if nameupdt == 'lokasi' :
                            ubahLok = input('Update Lokasi : ').upper()
                            confLok = input('Apakah Data lokasi diubah ? (Y/N) : ').lower()
                            if confLok == 'y' :
                                stok[i]['lokasi'] = ubahLok
                                print('Data berhasil diubah')
                                break
                            elif confLok == 'n' :
                                print('Data tidak diubah')

                    else :
                        print ('Data tidak ada!')   
                        break      
                else :
                    print ('Pilihan Menu tidak ada')             

#DELETE ITEM
def Delete_Menu () :
    DeleteMenu = True
    while DeleteMenu != '2' :
        print('\n---------- DELETE ----------')   
        print ('1. Hapus Stok item')
        print ('2. Kembali ke Menu Utama')
        print('-----------------------------') 
        DeleteMenu = input('Silakan pilih Sub Menu Laporan Data (1/2/3) : \n')

        if DeleteMenu == '1':
            if len(stok) !=0 :
                delCode = input('Masukkan kode SKU yang ingin dihapus : ').upper()
                for i in range (len(stok)):
                    if delCode == stok[i]['SKU']:
                        print('item yang ingin dihapus adalah : ', stok[i])
                        confDel = input('Apakah yakin ingin menghapus data ini ? (Y/N) : ').lower()
                        if confDel == 'y' :
                            del stok[i]
                            print('item berhasil dihapus')
                            break
                        elif confDel == 'n':
                            print('item tidak terhapus')
                            break
                        else :
                            print('Menu yang anda masukkan salah')
                            break
                else :
                    print ('item tidak ditemukan')
                    break
            else :
                print ('item sudah tidak ada stok')
        elif DeleteMenu == '2':
            break        
        else :
            print ('Pilihan Menu tidak ada')

Main_Menu()