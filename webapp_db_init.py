import sqlite3


def execute_script(cursor, script_file):
    with open(script_file, encoding='utf-8') as f:
        query = f.read()
    cursor.executescript(query)


if __name__ == '__main__':
    conn = sqlite3.connect('dog_db.sqlite')
    cursor = conn.cursor()

    execute_script(cursor, 'sql/dog_create.sql')
    execute_script(cursor, 'sql/dog1_init.sql')
    execute_script(cursor, 'sql/dog2_init.sql')
    execute_script(cursor, 'sql/dog3_init.sql')
    execute_script(cursor, 'sql/dog4_init.sql')

    conn.commit()
    conn.close()
