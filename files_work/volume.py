from zipfile import ZipFile


with ZipFile("/home/kostya/Загрузки/workbook.zip") as zip_file:
    l = zip_file.infolist()
    print(
        f"Объем исходных файлов: {sum(i.file_size for i in l)} байт(а)",
        f"Объем сжатых файлов: {sum(i.compress_size for i in l)} байт(а)",
        sep="\n",
    )
