for i in range(90):
    if i == 10:
        continue

    print("{:02d}".format(i), end=", " if i < 89 else "")
