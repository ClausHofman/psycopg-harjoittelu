# TEST THE CONNECTION TO POSTGRESQL SERVER ON LOCALHOST

# LIBRARIES AND MODULES
import psycopg2  # For PostgreSQL

# Properties of the connection string
database = "hirviporukka1"
user = "postgres"
password = "Q2werty"
host = "localhost"
port = "5432"

# Try to establish a connection to DB server
try:
    # Create a connection object
    dbaseconnetion = psycopg2.connect(database=database, user=user, password=password,
                                      host=host, port=port)
    
    # Create a cursor to execute commands and retrieve result set
    cursor = dbaseconnetion.cursor()
    
    # excecute SQL command to call a procedure
    command =  "CALL public.add_jakoryhma(1, 'Testiryhmä 2');"
    cursor.execute(command)

    # commit the transaction
    dbaseconnetion.commit()
    print("Tietue päivitettiin proseduurin avulla")

# Throw an error if connection or cursor creation fails                                     
except(Exception, psycopg2.Error) as e:
    print("Tietokantayhteydessä tapahtui virhe", e)

# If or if not successfull close the cursor and the connection   
finally:
    if (dbaseconnetion):
        cursor.close()
        dbaseconnetion.close()
        print("Yhteys tietokantaan katkaistiin")