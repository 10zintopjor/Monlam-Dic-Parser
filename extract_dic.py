import sqlite3
import csv


def extract_db():
    archaic_words = []
    con = sqlite3.connect("database.sqlite")
    cur = con.cursor()
    archaic_word ="བརྡ་རྙིང་།"
    with open("dic.csv","w") as f:
        writer = csv.writer(f)
        for row in cur.execute('SELECT word text,result text FROM table_en_ind'):
            word,desc = row     
            writer.writerow([word,desc])
            if desc and archaic_word in desc:
                archaic_words.append(word)
    con.close()

    return archaic_words


if __name__ == "__main__":
    extract_db()
