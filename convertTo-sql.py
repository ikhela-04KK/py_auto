import sqlite3
import csv

# first table: rank,prev_rank,name,league,off,def,spi

# second table: rank,name,confed,off,def,spi

#season,date,league_id,league,team1,team2,spi1,spi2,prob1,prob2,probtie,proj_score1,#proj_score2,importance1,importance2,score1,score2,xg1,xg2,nsxg1,nsxg2,adj_score1,#adj_score2
#
#fourth table: season,date,league_id,league,team1,team2,spi1,spi2,prob1,prob2,probtie,proj_score1,proj_score2,importance1,importance2,score1,score2,xg1,xg2,nsxg1,nsxg2,adj_score1,adj_score2


# file type : C:/Users/ikhela/Downloads/soccer-spi
# file to convert : spi_global_rankings.csv,spi_global_rankings_intl.csv, spi_matches.csv ,spi_matches_latest.csv

conn =sqlite3.connect('C:\sql & base de donné\projet DB\koffi.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS spi_matches_latest')

fname_4 = "C:/Users/ikhela/Downloads/soccer-spi/spi_matches_latest.csv"

cur.execute("DROP TABLE spi_matches_lastest")
cur.executescript('''CREATE TABLE spi_matches_lastest(
    "season" TEXT,
    "date" date,
    "league_id" INT,
    "league" TEXT,
    "team1" TEXT,
    "team2" TEXT,
    "spi1" REAL,
    "spi2" REAL, 
    "prob1" REAL,
    "prob2" REAL,
    "probtie" REAL,
    "proj_score1" REAL,
    "proj_score2" REAL,
    "importance1" REAL,
    "importance2" REAL,
    "score1" REAL,
    "score2" REAL,
    "xg1" REAL,
    "xg2" REAL,
    "nsxg1" REAL,
    "nsxg2" REAL,
    "adj_score1" REAL,
    "adj_score2" REAL
    );
''')
with open(fname_4) as csv_file:
    csv_reader =csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        season =row[0]
        date =row[1]
        league_id =row[2]
        league =row[3]
        team1 =row[4]
        team2 =row[5]
        spi1 =row[6]
        spi2 =row[7]
        prob1 =row[8]
        prob2 =row[9]
        probtie =row[10]
        proj_score1 =row[11]
        proj_score2 =row[12]
        importance1 =row[13]
        importance2 =row[14]
        score1 =row[15]
        score2 =row[16]
        xg1 =row[17]
        xg2 =row[18]
        nsxg1 =row[19]
        nsxg2 =row[20]
        adj_score1 =row[21]
        adj_score2 =row[22]
        
        cur.execute('''
                    INSERT INTO spi_matches_lastest (season, date, league_id, league, team1, team2, spi1, spi2,prob1, prob2, probtie, proj_score1 ,proj_score2, importance1, importance2, score1, score2, xg1, xg2, nsxg1, nsxg2, adj_score1, adj_score2) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ''',(season,date,league_id,league,team1,team2,spi1,spi2,prob1,prob2,probtie,proj_score1,proj_score2,importance1,importance2,score1,score2,xg1,xg2,nsxg1,nsxg2,adj_score1,adj_score2))
        conn.commit()
