def remove_marks(text, marks):
    remove_marks.count += 1
    return "".join(t for t in text if t not in marks)


remove_marks.count = 0
