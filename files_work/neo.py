from zipfile import ZipFile
from datetime import datetime

with ZipFile("/home/kostya/Загрузки/workbook.zip") as zip_file:
    print(
        *sorted(
            map(
                lambda x: x.filename.split("/")[-1],
                filter(
                    lambda x: not x.is_dir()
                    and datetime(*x.date_time) >= datetime(2021, 11, 30, 14, 22),
                    zip_file.infolist(),
                ),
            )
        ),
        sep="\n"
    )
