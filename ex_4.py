
import psycopg2

def connect():
    try:
        """ Connect to the PostgreSQL database server """
        conn = psycopg2.connect(
            host="localhost",
            database="pagila",
            user="postgres",
            password="asd")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute("""
                SELECT * from public."address";
                """)

        # display the result of executed SQL query
        # you can also use fetchone() and fetchmany() according to your need
        #info = cur.fetchone()
        #info = cur.fetchall()
        info = cur.fetchmany(50)
        print(info)

        # close the communication with the PostgreSQL
        cur.close()

        conn.commit()

    # catch the exception and print
    except (Exception) as error:
        print(error)

    finally:
        # close the connection at the end
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()