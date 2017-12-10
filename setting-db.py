import MySQLdb

conn = MySQLdb.connect(
    user='username',
    passwd='userpassword',
    host='172.17.0.3',
    db='ff14rssdata'
)

cur = conn.cursor()
cur.execute( '''
    create table rss_history (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        title TEXT,
        link  TEXT,
        posted_datetime DATETIME,
        uptedated DATETIME default current_timestamp,
        created DATETIME default current_timestamp
    )
    ''')