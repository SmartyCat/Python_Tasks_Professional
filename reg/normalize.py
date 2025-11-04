from re import sub, I


def normalize_jpeg(filename):
    return sub(r"(jpe?g$)", r"jpg", filename, flags=I)


print(normalize_jpeg("stepik.jPeG"))
print(normalize_jpeg("mountains.JPG"))
print(normalize_jpeg("windows11.jpg"))
print(normalize_jpeg("jpeg.jpeg"))
