from recipe_page import RecipePage
from sql_connection import SQLiteConnection
from recipe_list import RecipeList

# initialize classes
program_start = RecipeList()
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
    program_start.recipe_list_program_loop()
    break

# Close SQL connection
conn.close()