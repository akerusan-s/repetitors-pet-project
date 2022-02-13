import sqlite3

bd = sqlite3.connect("repetitors.db")
cur = bd.cursor()

for i in open("2.txt", encoding="UTF-8").read().split("\n"):

    a, b,  = i.split("\t")

    res = cur.execute(f"""INSERT INTO 'pages_subject' VALUES ({a}, '{b}')""")
bd.commit()
bd.close()
