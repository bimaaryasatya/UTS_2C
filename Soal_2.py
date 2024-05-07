def kabisad():
    tahun = int(input('Masukkan Tahun: '))
    print(f'{tahun} adalah tahun kabisat') if tahun % 4 == 0 or tahun % 100 == 1 or tahun % 400 == 0 else print(f'{tahun} bukan tahun kabisat')

kabisad()