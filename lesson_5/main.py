import sqlite3

conn = sqlite3.connect('database.db')


def main():
    # Your code here

    # querry = "SELECT * FROM worker"
    # for worker in conn.execute(querry):
    #     print(worker)

    ...


if __name__ == '__main__':
    main()
    conn.close()
    