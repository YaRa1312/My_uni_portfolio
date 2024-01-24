import re
import sqlite3

with open(r"D:\\ВИШ\\3 курс\\1-ий семестр\\Т та К л-ія\\Ukr lexicon.md", "r", encoding="utf-8") as f:
    f = f.read()

line_pattern = re.compile(r"\n\n(?=\*{2,3})")
f = line_pattern.split(f)

parse_line_pattern = \
    re.compile(r"^\*{2,3}(.+)\*{2,3} (?:\[?\*([^А-ЯІЄЇҐ]+)\*\[? )?([\s\S]+?)(?=\n\n(?!\*{2,3})([\s\S]+?))?$")
list = list()

for line in f:
    line = parse_line_pattern.findall(line)
    list = list + (line)

connection = sqlite3.connect("Ukr_lexicon.db")
def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close
if __name__ == '__main__':
    create_connection(r"C:\Users\Ирина\PycharmProjects\Програмування\venv\Ukr_lexicon.db")

connection.execute("""CREATE TABLE Ukr_lexicon (
             Word TEXT,
             Grammar TEXT,
             Dictionaries TEXT,
             Addition TEXT
             )""")

for line in list:
    connection.execute(f"""
    INSERT INTO Ukr_lexicon VALUES
    {line}
    """)

for row in connection.execute('SELECT * FROM Ukr_lexicon'):
    print(row)

connection.commit()

connection.close()
