score = [{'nama' : 'Dummy', 'UTS':'Dummy','UAS':'Dummy','nilai' : 'Dummy','grade':'dummy','keterangan' : 'dummy'},
{'nama' : 'Pixie', 'UTS': 75,'UAS':75,'nilai' : 75.0,'grade':'B','keterangan':'LULUS'},
{'nama' : 'Dixie','UTS':90,'UAS':90,'nilai' : 90.0,'grade':'A','keterangan':'LULUS'}]

def melihatdata() :
    print('\n          NILAI AKADEMIK SISWA IPA 1\n')
    print('{:<5}|{:<10}|{:<8}|{:<8}|{:<8}|{:<8}|{:<15}'.format('No.','Nama','UTS(50%)','UAS(50%)','Nilai','Grade','Keterangan'))
    for i in range (0,(len(score))):
        if i > 0:
            print('{:<5}|{:<10}|{:<8}|{:<8}|{:<8}|{:<8}|{:<15}'.format((i),score[i]['nama'],score[i]['UTS'],score[i]['UAS'],score[i]['nilai'],score[i]['grade'],score[i]['keterangan']))
        else:
            text = '\n              DATA KOSONG'                
    if len(score) == 1:
        print(text)

def caridata(a):
    j = 0
    for i in range (1,len(score)):
        if a == score[i]['nama']:
            j += i
        else: 
            text = '\n     Nama {} Tidak Tersedia'.format(a)

    if a == score[j]['nama']:
        print('\n          NILAI AKADEMIK SISWA IPA 1')
        print('            Atas Nama {}\n'.format(a))
        print('{:<5}|{:<10}|{:<8}|{:<8}|{:<8}|{:<8}|{:<15}'.format('No.','Nama','UTS(50%)','UAS(50%)','Nilai','Grade','Keterangan'))
        print('{:<5}|{:<10}|{:<8}|{:<8}|{:<8}|{:<8}|{:<15}'.format((j),score[j]['nama'],score[j]['UTS'],score[j]['UAS'],score[j]['nilai'],score[j]['grade'],score[j]['keterangan']))

    else:
        print(text)

while True :
    pilihmenu = input('''
SELAMAT DATANG DI NILAI AKADEMIK SISWA IPA 1
    
List Menu:
1. Menampilkan Nilai Siswa
2. Menambah Nilai Siswa
3. Mengupdate Nilai Siswa
4. Menghapus Nilai Siswa
5. Keluar
    
Masukan angka Menu yang ingin dijalankan : ''')

    if pilihmenu == '1':
        while True :
            lihatdata = input('''
Berikut List Menu Menampilkan Nilai Siswa
        
List Menu:
1. Menampilkan Seluruh Nilai Siswa
2. Mencari Nilai Siswa
3. Kembali ke Menu Utama
        
Silahkan masukan angka Menu yang ingin dijalankan : ''')
        
            if lihatdata == '1':
                melihatdata()
  
            elif lihatdata == '2':
                carisiswa = input('\nSilahkan Cari Nama Siswa :')
                captsiswa = carisiswa.capitalize()
                caridata(captsiswa)
                                          
            elif lihatdata == '3':
                Menuutam = input('\nKembali ke Menu Utama? Y/N : ')
                captmenutam = Menuutam.capitalize()
                if captmenutam == 'Y':
                    break
                elif captmenutam == 'N':
                    continue
                else : print('\nPilihan Yang Anda Masukan Salah!')
                
    elif pilihmenu == '2':
        while True :
            tambahdata = input('''
Berikut List Menu Menambah Nilai Siswa
        
List Menu:
1. Menambah Nilai Siswa
2. Kembali ke Menu Utama
        
Silahkan masukan angka Menu yang ingin dijalankan : ''')
    
            if tambahdata == '1':
                namasiswa = input('\nSilahkan Masukan Nama Siswa yang ingin ditambah : ')
                captnamasiswa = namasiswa.capitalize()
                j= 0
                for i in range (1,len(score)):
                    if captnamasiswa == score[i]['nama']:
                        j += i
                    else:
                        text= '\nNama {} Sudah Ada'.format(captnamasiswa)
                        
                if captnamasiswa != score[j]['nama']:
                    print('\nSilahkan Lengkapi Data Berikut:')
                    utssiswa = int(input('\nSilahkan Masukan Nilai UTS Siswa  :'))
                    uassiswa = int(input('\nSilahkan Masukan Nilai UAS Siswa  :'))
                    nilaisiswa = (utssiswa + uassiswa)/2   
                    if nilaisiswa >= 85: 
                        nilaigrade = 'A'
                        status = 'LULUS'
                    elif (nilaisiswa >= 70 and nilaisiswa <= 84): 
                        nilaigrade = 'B'
                        status = 'LULUS'
                    elif (nilaisiswa >= 60 and nilaisiswa <= 69) :
                        nilaigrade = 'C'
                        status = 'LULUS'
                    else : 
                        nilaigrade ='D'
                        status = 'TIDAK LULUS'
                    
                    save = input('\nApakah Data Ingin Disimpan? Y/N: ')
                    captsave = save.capitalize()
                    if captsave == 'Y':
                        print('\nData Berhasil Disimpan!')
                        score.append({
                        'nama': captnamasiswa,
                        'UTS':utssiswa,
                        'UAS':uassiswa,
                        'nilai': nilaisiswa,
                        'grade': nilaigrade,
                        'keterangan': status
                        })
                                  
                    elif captsave == 'N':
                        continue
                    else: 
                        print('\nPilihan Yang Anda Masukan Salah!')
                else: 
                    print(text)
                    continue
                    
                melihatdata()

            elif tambahdata == '2':
                Menuutam = input('\nKembali ke Menu Utama? Y/N : ')
                captmenutam = Menuutam.capitalize()
                if captmenutam == 'Y':
                    break
                elif captmenutam == 'N':
                    continue
                else : print('\nPilihan Yang Anda Masukan Salah')

    elif pilihmenu == '3':
        while True :
            updatedata = input('''
Berikut List Menu Mengupdate Nilai Siswa
        
List Menu:
1. Mengupdate Nilai Siswa
2. Kembali ke Menu Utama
        
Silahkan masukan angka Menu yang ingin dijalankan : ''')

            if updatedata == '1':
                updatesiswa = input('\nSilahkan Masukan Nama Siswa yang ingin diupdate : ')
                captupdatesiswa = updatesiswa.capitalize()
                j = 0
                for i in range (1,len(score)):
                    if captupdatesiswa == score[i]['nama']:
                        j += i
                    else: 
                        text = '\nNama {} Tidak Tersedia'.format(captupdatesiswa)

                if captupdatesiswa == score[j]['nama']:
                    print('\n          NILAI AKADEMIK SISWA IPA 1')
                    print('            Atas Nama {}\n'.format(captupdatesiswa))
                    print('{:<5}|{:<10}|{:<8}|{:<8}|{:<8}|{:<8}|{:<15}'.format('No.','Nama','UTS(50%)','UAS(50%)','Nilai Total','Grade','Keterangan'))
                    print('{:<5}|{:<10}|{:<8}|{:<8}|{:<8}|{:<8}|{:<15}'.format((j),score[j]['nama'],score[j]['UTS'],score[j]['UAS'],score[j]['nilai'],score[j]['grade'],score[j]['keterangan']))
    
                    update = input('\nApakah ingin melanjutkan update Data Atas Nama {}? Y/N = '.format(captupdatesiswa))
                    cupdate = update.capitalize()
                    if cupdate == 'Y':
                        print('\nSilahkan Update Data Berikut:')
                        uputs = int((input('\nSilahkan isi Update Nilai UTS Atas Nama {} : '.format(captupdatesiswa))))
                        upuas = int((input('\nSilahkan isi Update Nilai UAS Atas Nama {} : '.format(captupdatesiswa))))
                        updata = (uputs+upuas)/2
                        ups = input('\nApakah Data Ingin diupdate? Y/N = ')
                        cups = ups.capitalize()
                        if cups == 'Y':
                            print('\nData Atas Nama {} Berhasil di Update!'.format(captupdatesiswa))
                            score[j]['UTS'] = uputs
                            score[j]['UAS'] = upuas
                            score[j]['nilai'] = updata
                            if updata >= 85: 
                                nilaigrade = 'A'
                                status = 'LULUS'
                            elif (updata >= 70 and updata <= 84): 
                                nilaigrade = 'B'
                                status = 'LULUS'
                            elif (updata >= 60 and updata <= 69) :
                                nilaigrade = 'C'
                                status = 'LULUS'
                            else : 
                                nilaigrade ='D'
                                status = 'TIDAK LULUS'    
                            score[j]['grade'] = nilaigrade
                            score[j]['keterangan'] = status
                        elif cups == 'N':
                            continue
                        else:
                            print('\nPilihan Yang Anda Masukan Salah!')
                    elif cupdate == 'N':
                            continue
                    else:
                        print('\nPilihan Yang Anda Masukan Salah')
                else:
                    print(text)
                    continue

                melihatdata()
                      
            elif updatedata == '2':
                Menuutam = input('\nKembali ke Menu Utama? Y/N : ')
                captmenutam = Menuutam.capitalize()
                if captmenutam == 'Y':
                    break
                elif captmenutam == 'N':
                    continue
                else : print('\nPilihan Yang Anda Masukan Salah!')

    elif pilihmenu == '4':
        while True :
            hapusdata = input('''
Berikut List Menu Menghapus Nilai Siswa
        
List Menu:
1. Menghapus Nilai Siswa
2. Kembali ke Menu Utama
        
Silahkan masukan angka Menu yang ingin dijalankan : ''')

            if hapusdata == '1':
                Idsiswa = input('\nSilahkan Masukan Nama Siswa yang ingin dihapus :')
                captid = Idsiswa.capitalize()
                j = 0
                for i in range (1,len(score)):
                    if captid == score[i]['nama']:
                        j += i
                    else: 
                        text = '\nNama {} Tidak Tersedia'.format(captid)
                
                if captid == score[j]['nama']:
                    print('\n          NILAI AKADEMIK SISWA IPA 1')
                    print('            Atas Nama {}\n'.format(captid))
                    print('{:<5}|{:<10}|{:<8}|{:<8}|{:<8}|{:<8}|{:<15}'.format('No.','Nama','UTS(50%)','UAS(50%)','Nilai Total','Grade','Keterangan'))
                    print('{:<5}|{:<10}|{:<8}|{:<8}|{:<8}|{:<8}|{:<15}'.format((j),score[j]['nama'],score[j]['UTS'],score[j]['UAS'],score[j]['nilai'],score[j]['grade'],score[j]['keterangan']))
                
                    haps = input('\nApakah ingin menghapus Data Atas Nama {}? Y/N = '.format(captid))
                    chaps = haps.capitalize()
                    if chaps == 'Y':
                        print('\nData Atas Nama {} Berhasil Dihapus!'.format(captid))
                        del score[j] 
                    elif chaps == 'N':
                        continue
                    else:
                        print('\nPilihan Yang Anda Masukan Salah')
                else: 
                    print(text) 
                    continue
                
                melihatdata()

            elif hapusdata == '2':
                Menuutam = input('\nKembali ke Menu Utama? Y/N : ')
                captmenutam = Menuutam.capitalize()
                if captmenutam == 'Y':
                    break
                elif captmenutam == 'N':
                    continue
                else : print('\nPilihan Yang Anda Masukan Salah!')
                
    elif pilihmenu == '5':
        exit = input('\nApakah Ingin Keluar Dari Program? Y/N : ')
        captexit = exit.capitalize()
        if captexit == 'Y':
            break
        elif captexit == 'N':
            continue
        else: print('\nPilihan Yang Anda Masukan Salah!')