from zipfile import ZipFile
from datetime import datetime

with ZipFile("/home/kostya/Загрузки/workbook.zip") as zip_file:
    results = []
    for i in sorted(
        (i for i in zip_file.infolist() if i.filename.split("/")[-1]),
        key=lambda x: x.filename.split("/")[-1],
    ):
        result = f"{i.filename.split("/")[-1]}\n  Дата модификации файла: {datetime(*i.date_time)}\n  Объем исходного файла: {i.file_size} байт(а)\n  Объем сжатого файла: {i.compress_size} байт(а)\n"
        results.append(result)
    results[-1] = results[-1].rstrip()
    print(*results, sep="\n")
