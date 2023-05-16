from sqlalchemy import create_engine

engine = create_engine('sqlite:///Zadanie_6_3.db')

result_stations = engine.execute("SELECT * FROM clean_stations LIMIT 5").fetchall()
print("5 wyników z tabeli 'clean_stations':")
for row in result_stations:
    print(row)

result_measure = engine.execute("SELECT * FROM clean_measure LIMIT 5").fetchall()
print("\n5 wyników z tabeli 'clean_measure':")
for row in result_measure:
    print(row)