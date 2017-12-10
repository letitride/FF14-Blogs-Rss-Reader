# FF14-Blogs-Rss-Reader

## install

### setup mysql
`$ docker run --name mysqld -e MYSQL_DATABASE=ff14rssdata -e MYSQL_USER=username -e MYSQL_PASSWORD=userpassword  -e MYSQL_ROOT_PASSWORD=rootpassword -d mysql`
`$ docker run --link  mysqld:mysql -it --rm mysql bash`
`/# env`
　MYSQL_PORT_3306_TCP_ADDR=ここのIPアドレスをメモ

### setup python
`$ pip3 install beautifulsoup4`
`$ pip3 install mysqlclient`

#### setting-db.py
    user='username',
    passwd='userpassword',
    host='***.***.***.***', #メモしたIPアドレス
    db='ff14rssdata'

## run
`python3 download-rss.py`