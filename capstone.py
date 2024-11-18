import textwrap
# Penjualan barang toko matrial Gudang Jaya

keyNama = 'nama'
keyStok = 'stok'
keySatuan = 'satuan'
keyHarga = 'harga'
keySku = 'sku'

listBarang = [
    {
        keySku: 1001,
        keyNama: 'Keramik',
        keyStok: 10,
        keySatuan: 'dus',
        keyHarga: 40000,
    },
    {
        keySku: 1002,
        keyNama: 'Semen',
        keyStok: 20,
        keySatuan: 'sak',
        keyHarga: 50000,
    },
    {
        keySku: 1003,
        keyNama: "Pasir",
        keyStok: 50,
        keySatuan: "kubik",
        keyHarga: 30000,
    },
    {
        keySku: 1004,
        keyNama: "Bata Merah",
        keyStok: 100,
        keySatuan: "buah",
        keyHarga: 500,
    }
]

def formatPrompt(prompt):
    return textwrap.dedent(prompt).strip()

def readFeature() :
    while True:
        read = input(formatPrompt('''
                List Fitur Show:
                1. Menampilkan Semua Barang
                2. Menampilkan Satu Barang
                3. Back

                Masukkan angka fitur yang ingin dijalankan : '''))
        if read.isdigit():
            match read:
                case "1":
                    showAllItem()
                case "2":
                    showChoosenItem()
                case "3":
                    break
                case default:
                    showFeatureInvalid()
        else:
            showFeatureInvalid()

def showAllItem():
    if not listBarang:
        showDataNotExist()
    else:
        print('Daftar Semua Barang\n')
        print('No\t| SKU  \t| Nama  \t| Stok  \t| Harga')
        for i in range(len(listBarang)):
            item = listBarang[i]
            print(f'{i+1}\t| {item[keySku]}\t| {item[keyNama]}  \t| {item[keyStok]} {item[keySatuan]} \t| {formatRupiah(item[keyHarga])}')

def inputSKU():
    while True:
        inputan = input('Masukkan SKU barang: ')
        if inputan.isdigit():
            break
        else:
            showInputInvalid()
    return int(inputan)


def inputNamaBarang():
    while True:
        inputan = input('Masukkan Nama barang: ')
        if inputan.isalpha():
            break
        else:
            showInputInvalid()
    return inputan


def inputStok():
    while True:
        inputan = input('Masukkan Stok barang: ')
        if inputan.isdigit():
            if int(inputan) >= 0:
                break
            else:
                showInputInvalid()
        else:
            showInputInvalid()
    return int(inputan)


def inputSatuan():
    while True:
        inputan = input('Masukkan Satuan barang: ')
        if inputan.isalpha():
            break
        else:
            showInputInvalid()
    return inputan

def inputHarga():
    while True:
        inputan = input('Masukkan Harga barang: ')
        if inputan.isdigit():
            if int(inputan) >= 0:
                break
            else:
                showInputInvalid()
        else:
            showInputInvalid()
    return int(inputan)

def inputDecision(decision):
    while True:
        inputan = input(f'{decision}? (ya/tidak): ').lower()
        if inputan.isalpha():
            if inputan == "ya" or inputan == "tidak":
                break
            else:
                showInputInvalid()
        else:
            showInputInvalid()
    return inputan

def getItem(sku):
    return next((item for item in listBarang if item[keySku] == sku), None)

def showData(sku):
    data = getItem(sku)
    if not data:
        showDataNotExist()
    else:
        print('Nama  \t\t| Stok  \t| Harga')
        print(f'{data[keyNama]}  \t| {data[keyStok]} {data[keySatuan]} \t| {formatRupiah(data[keyHarga])}')
    
def showChoosenItem():
    if not listBarang:
        showDataNotExist()
    else:
        sku = inputSKU()
        showData(sku)

def checkSKU(sku):
    return any(item for item in listBarang if item[keySku] == sku)

def createItem():
    sku = inputSKU()
    isSkuExists = checkSKU(sku)
    if isSkuExists:
        showDataAlreadyExist()
    else:
        nama = inputNamaBarang()
        stok = inputStok()
        satuan = inputSatuan()
        harga = inputHarga()
        isSave = inputDecision('Simpan') == "ya"
        if isSave:
            listBarang.append({
                keySku: sku,
                keyNama: nama,
                keyStok: stok,
                keySatuan: satuan,
                keyHarga: harga
            })
            print('Data successfully saved')

def createFeature():
    while True:
        create = input(formatPrompt('''
                List Fitur Add:
                1. Tambah Barang
                2. Back

                Masukkan angka fitur yang ingin dijalankan : '''))
        if create.isdigit():
            match create:
                case "1":
                    createItem()
                case "2":
                    break
                case default:
                    showFeatureInvalid()
        else:
            showFeatureInvalid()

def updateItem():
    sku = inputSKU()
    data = getItem(sku)
    if data:
        showData(sku)
        isUpdate = inputDecision('Update')
        if isUpdate:
            while True:
                column = input(f'Pilih satu nama kolom yang ingin diubah ({keyNama}/{keyStok}/{keySatuan}/{keyHarga}): ')
                value = data[column]
                if column != keyNama or column != keyStok or column != keySatuan or column != keyHarga:
                    print(f'Kolom {column} akan diubah dengan value {value}')
                    newValue = input(f'Input value baru: ')
                    if column == keyStok or column == keyHarga:
                        newValue = int(newValue)
                    isUpdateValue = inputDecision(f'Update kolom {column} dengan value baru {newValue}')
                    if isUpdateValue:
                        for item in listBarang:
                            if item[keySku] == sku:
                                item[column] = newValue
                                print('Data successfully updated')
                                break
                    break
                else:
                    print('Nama kolom tidak ditemukan')
    else:
        showDataNotExist()

def updateFeature():
    while True:
        update = input(formatPrompt('''
                    List Fitur Update:
                    1. Update Barang
                    2. Back

                    Masukkan angka fitur yang ingin dijalankan : '''))
        
        if update.isdigit():
            match update:
                case "1":
                    updateItem()
                case "2":
                    break
                case default:
                    showFeatureInvalid()
        else:
            showFeatureInvalid()

def deleteItem():
    sku = inputSKU()
    isSkuExists = checkSKU(sku)
    if isSkuExists:
        showData(sku)
        isDelete = inputDecision('Delete')
        if isDelete:
            global listBarang
            listBarang = [item for item in listBarang if item[keySku] != sku]
            print('Data successfully deleted')
    else:
        showDataNotExist()

def deleteFeature():
    while True:
        delete = input(formatPrompt('''
                    List Fitur Delete:
                    1. Hapus Barang
                    2. Back

                    Masukkan angka fitur yang ingin dijalankan : '''))

        if delete.isdigit():
            match delete:
                case "1":
                    deleteItem()
                case "2":
                    break
                case default:
                    showFeatureInvalid()
        else:
            showFeatureInvalid()

def showFeatureInvalid():
    print('The option you entered is not valid')

def showDataNotExist():
    print('Data does not exist')

def showDataAlreadyExist():
    print('Data already exist')

def showInputInvalid():
    print('Input Invalid')

def formatRupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")

while True:
    feature = input(formatPrompt('''
            Selamat Datang di Toko Bangunan - Gudang Jaya

            List Fitur :
            1. Menampilkan Barang
            2. Menambah Barang
            3. Mengubah Barang
            4. Menghapus Barang
            5. Keluar

            Masukkan angka fitur yang ingin dijalankan : '''))
    if feature.isdigit():
        match feature:
            case "1":
                readFeature()
            case "2":
                createFeature()
            case "3":
                updateFeature()
            case "4":
                deleteFeature()
            case "5":
                break
            case default:
                showFeatureInvalid()
    else:
        showFeatureInvalid()
    