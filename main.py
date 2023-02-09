from recipe_page import RecipePage
from sql_connection import SQLiteConnection

# initialize classes
recipe_page = RecipePage()
conn = SQLiteConnection()

# create cursor
# c = conn.cursor()
c = conn.cursor()

# create table if none exists
c.execute("""CREATE TABLE IF NOT EXISTS recipes (
    Recipe DATATYPE text,
    Type DATATYPE text,
    Step DATATYPE integer,
    Details DATATYPE text
    )""")

# program loop
while True:
    recipe_page.recipe_page_program_loop()
    break

# Close SQL connection
conn.close()