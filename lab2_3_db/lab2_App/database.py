import MySQLdb as mdb
import os

class Database:

    def __init__(self):
        self.con = None

    def connect(self):
        self.con = mdb.connect('127.0.0.1', 'dbuser', 'abacaba123', 'ticketSell_database')

    def add_customer(self, name, surname , phone_number , VIP):
        try:
            if not self.con:
                self.connect()

            cur = self.con.cursor()
            cur.execute("INSERT INTO customer(name,surname,phone_number, VIP) VALUES('%s','%s','%s', case '%s' when 'true' then 'true' else 'false' end)" % (name, surname, phone_number, VIP))
        except mdb.Error:
            if self.con:
                self.connect().rollback()



    '''def create(self):
        if not self.con and not self.con.open:
            self.connect()
        with self.con:
            cur = self.con.cursor()
            cur.execute("DROP TABLE IF EXISTS Writers")
            cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                         Name VARCHAR(25))")
            cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
            cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
            cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
            cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
            cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")'''


    def select(self):
        if not self.con:
            self.connect()
        with self.con:
            #cur = self.con.cursor()
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM customer")

            rows = cur.fetchall()
            print(rows)
            '''for row in rows:
                print(row)'''
            return rows

    def select_games(self):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT game_id,team1_team2, game_data_time, ticket_price FROM games")
            rows = cur.fetchall()
            return rows

    def select_stadium(self):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM stadiums")
            rows = cur.fetchall()
            return rows

    def select_vip_customers(self):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT name,surname, phone_number FROM customer where VIP = 'true'")
            rows = cur.fetchall()
            return rows

    def add_game(self, teams, stadium_id, datatime, price):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor()
            cur.execute("INSERT INTO games(team1_team2, stadium_id, game_data_time, ticket_price) VALUES(\"%s\",'%s',\"%s\",'%s')" % (teams, stadium_id, datatime, price))

    def add_fact(self, name,surname ,game_id):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor()
            cur.execute("SELECT cust_id FROM customer WHERE name = \"%s\" and surname = \"%s\"" % (name,surname))
            cust_id = cur.fetchall()
            cur.execute("INSERT INTO facts(cust_id,game_id,sell_data_time) VALUES('%s','%s',now())" % (cust_id[0][0], game_id))


    def edit_game(self, game_id, stadium_id, datatime, price):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor()
            cur.execute("update games set stadium_id = '%s', game_data_time = \"%s\", ticket_price = '%s' WHERE game_id = '%s'" % (stadium_id, datatime, price, game_id))

    def select_games_range(self, froms='20', to='130'):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute("select team1_team2 from games where (ticket_price >= '%s') and (ticket_price <='%s')" % (froms,to))
            rows = cur.fetchall()
            return rows

    def fulltext_find_word(self, word):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM stadiums WHERE MATCH(adress) AGAINST(+'%s' IN BOOLEAN MODE)" % (word))
            rows = cur.fetchall()
            return rows

    def fulltext_find_str(self, stt):
        if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM stadiums WHERE MATCH(adress) AGAINST('\"%s\"' IN BOOLEAN MODE)" % (stt))
            rows = cur.fetchall()
            return rows

    def load_dump(self):
        '''if not self.con:
            self.connect()
        with self.con:
            cur = self.con.cursor()
            cur.execute("DELETE FROM facts")
            cur.execute("DELETE FROM games")
            cur.execute("DELETE FROM stadiums")
            cur.execute("DELETE FROM customer")'''
            #cur.execute("LOAD XML LOCAL INFILE '/home/raynem_0/stadiums.xml' INTO TABLE ticketSell_database.stadiums")
            #cur.execute("LOAD XML LOCAL INFILE '/home/raynem_0/games.xml' INTO TABLE ticketSell_database.games")
        os.system("mysql -udbuser -pabacaba123 --xml -e \"LOAD XML LOCAL INFILE '/home/raynem_0/stadiums.xml' INTO TABLE ticketSell_database.stadiums\"")
        os.system("mysql -udbuser -pabacaba123 --xml -e \"LOAD XML LOCAL INFILE '/home/raynem_0/games.xml' INTO TABLE ticketSell_database.games\"")