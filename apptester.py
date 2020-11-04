from helpers import create_connection

db = create_connection("Bray_Database.db")

# CREADOR DE DROPDOWN
brand_dropdown = []

brand_dropdown_sql = db.execute("SELECT DISTINCT BRAND FROM VALVES ORDER BY BRAND ASC")


for row in brand_dropdown_sql:
    brand_dropdown.append(row)

size_dropdown_sql = db.execute("SELECT DISTINCT SIZE FROM VALVES ORDER BY BRAND ASC")

serie = "BRAY"

series_list_sql = db.execute("SELECT DISTINCT NAME FROM VALVES WHERE BRAND = ?",
                      (serie,))

for row in series_list_sql:
    print(row[0])

print(brand_dropdown)