from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as file:
        if not args:
            file.extractall()
        else:
            for a in args:
                file.extract(a)
