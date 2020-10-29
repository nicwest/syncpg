import asyncio
import asyncpg


class ConnectionWrapper:

    def __init__(self, _conn, _loop):
        self._conn = _conn
        self._loop = _loop

    def execute(self, *args, **kwargs):
        return self._loop.run_until_complete(
            self._conn.execute(*args, **kwargs))

    def fetch(self, *args, **kwargs):
        return self._loop.run_until_complete(
            self._conn.fetch(*args, **kwargs))

    def close(self, *args, **kwargs):
        return self._loop.run_until_complete(
            self._conn.close(*args, **kwargs))


def connect(*args, **kwargs):
    loop = asyncio.get_event_loop()
    conn = loop.run_until_complete(asyncpg.connect(*args, **kwargs))
    return ConnectionWrapper(conn, loop)


def run():
    conn = connect(
        user='postgres',
        password='password',
        database='postgres',
        host='127.0.0.1',
    )
    conn.execute("""
    CREATE TABLE IF NOT EXISTS foo (
        id uuid NOT NULL,
        bar varchar,
        n int,
        f float,
        PRIMARY KEY (id)
    )""")
    conn.execute("TRUNCATE TABLE foo")
    conn.execute("""
    INSERT INTO foo VALUES (
        'fff182fd-8050-44fb-b078-9eae103561c6',
        'pew',
        10,
        3.142
    ),
    (
        'b726ef2c-2065-4b08-856a-01445c7a633b',
        'pew',
        3,
        10.29384756
    )
    """)
    values = conn.fetch('''SELECT * FROM foo''')
    conn.close()
    print(values)


if __name__ == '__main__':
    run()

