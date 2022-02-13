import sqlite3

s = {
    1: 5,
    2: 4.8,
    3: 4.9,
    4: 4.7,
    5: 4.6,
    6: 4.3,
    7: 4.4,
    8: 4.5,
    9: 3.3,
    10: 4.1,
    11: 4.2,
    12: 3.9,
    13: 3.8,
    14: 4,
    15: 3.6,
    16: 3.7,
    17: 3.4,
    18: 2.5,
    19: 2.2,
    20: 2.9,
    21: 3.5,
    22: 3.1,
    23: 0,
    24: 2.7,
}

bd = sqlite3.connect("repetitors.db")
cur = bd.cursor()
id_ = 0
for i in open("1.txt", encoding="UTF-8").read().split("\n"):
    id_ += 1
    a, b, c, d, e, f = i.split("\t")

    jj = ""
    for j in d:
        if j in "0123456789":
            jj += j
    kk = ""
    for k in e:
        if k in "0123456789":
            kk += k
    if "дист" in f.lower() and "у" in f.lower():
        t = 0
    elif "у" in f.lower():
        t = 1
    else:
        t = 2
    res = cur.execute(f"""INSERT INTO 'pages_teacher' VALUES ({id_}, '{c}', {s[int(b)]}, {kk}, {t}, {a}, {jj})""")
bd.commit()
bd.close()
