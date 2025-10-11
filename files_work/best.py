from zipfile import ZipFile


with ZipFile("/home/kostya/Загрузки/workbook.zip") as zip_file:
    name_file, size = None, None
    for i in filter(lambda x: x.file_size != 0 and not x.is_dir(), zip_file.infolist()):
        result = (i.compress_size / i.file_size) * 100
        if name_file is None or result < size:
            name_file, size = i.filename, result
    print(name_file.split("/")[-1])


with ZipFile("/home/kostya/Загрузки/workbook.zip") as zip_file:
    result = min(
        list(
            filter(lambda x: not x.is_dir() and x.file_size != 0, zip_file.infolist())
        ),
        key=lambda x: (x.compress_size / x.file_size) * 100,
    ).filename
    print(result.split("/")[-1])
