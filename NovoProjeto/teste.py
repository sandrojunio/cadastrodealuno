from Home import home_db

def main():
    a = home_db()
    sql = a.selectAluno()

    for i in sql:
        print(i)

main()