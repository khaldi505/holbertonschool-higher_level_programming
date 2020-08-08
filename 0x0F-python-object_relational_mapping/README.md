_______         _______  ___________  __________          __  .__                              ________ ___.        __               __                           .__          __  .__                     .__                                 .__                
\   _  \ ___  __\   _  \ \_   _____/  \______   \___.__._/  |_|  |__   ____   ____             \_____  \\_ |__     |__| ____   _____/  |_          _______   ____ |  | _____ _/  |_|__| ____   ____ _____  |  |     _____ _____  ______ ______ |__| ____    ____  
/  /_\  \\  \/  /  /_\  \ |    __)     |     ___<   |  |\   __\  |  \ /  _ \ /    \    ______   /   |   \| __ \    |  |/ __ \_/ ___\   __\  ______ \_  __ \_/ __ \|  | \__  \\   __\  |/  _ \ /    \\__  \ |  |    /     \\__  \ \____ \\____ \|  |/    \  / ___\ 
\  \_/   \>    <\  \_/   \|     \      |    |    \___  | |  | |   Y  (  <_> )   |  \  /_____/  /    |    \ \_\ \   |  \  ___/\  \___|  |   /_____/  |  | \/\  ___/|  |__/ __ \|  | |  (  <_> )   |  \/ __ \|  |__ |  Y Y  \/ __ \|  |_> >  |_> >  |   |  \/ /_/  >
 \_____  /__/\_ \\_____  /\___  / /\   |____|    / ____| |__| |___|  /\____/|___|  /           \_______  /___  /\__|  |\___  >\___  >__|            |__|    \___  >____(____  /__| |__|\____/|___|  (____  /____/ |__|_|  (____  /   __/|   __/|__|___|  /\___  / 
       \/      \/      \/     \/  \/             \/                \/            \/                    \/    \/\______|    \/     \/                            \/          \/                    \/     \/             \/     \/|__|   |__|           \//_____/  
                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                  ## introduction

In this project, you will link two amazing worlds: Databases and Python!

## Object-relational Mappers

<p>An object-relational mapper (ORM) is a code library that automates the transfer of data
stored in relational database tables into objects that are more commonly used in application code.</p>

<img
src="https://www.fullstackpython.com/img/visuals/orms-bridge.png">

<p>
In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (dont ask me how to pronounce it) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be What can I do with my objects and not How this object is stored? where? when?. You wont write any SQL queries only Python code. Last thing, your code wont be storage type dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
</p>

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With an ORM:


```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always
