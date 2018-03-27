# Newsdata


## Tables
```
\dt

 Schema |   Name   | Type  |  Owner
--------+----------+-------+---------
 public | articles | table | vagrant
 public | authors  | table | vagrant
 public | log      | table | vagrant
```

### Table Articles

```
\d articles

 Column |           Type           |        Modifiers
--------+--------------------------+-------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     |
 body   | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)
```

```sql
select id, slug, author, time
    from articles
    limit 5;
```
```
 id |         slug         | author |             time
----+----------------------+--------+-------------------------------
 23 | bad-things-gone      |      3 | 2016-08-15 18:55:10.814316+00
 24 | balloon-goons-doomed |      4 | 2016-08-15 18:55:10.814316+00
 25 | bears-love-berries   |      1 | 2016-08-15 18:55:10.814316+00
 26 | candidate-is-jerk    |      2 | 2016-08-15 18:55:10.814316+00
 27 | goats-eat-googles    |      1 | 2016-08-15 18:55:10.814316+00
(5 rows)
```

### Table Authors

```
\d authors

 Column |  Type   |    Modifiers
--------+---------+------------------
 name   | text    | not null
 bio    | text    |
 id     | integer | not null default
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)
```

```sql
select id, name
    from authors
    limit 5;
```
```
 id |          name
----+------------------------
  1 | Ursula La Multa
  2 | Rudolf von Treppenwitz
  3 | Anonymous Contributor
  4 | Markoff Chaney
(4 rows)
```

### Table Logs

```
\d log

 Column |           Type           |      Modifiers
--------+--------------------------+-------------------------
 path   | text                     |
 ip     | inet                     |
 method | text                     |
 status | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)

```

```sql
select id, path, date(time) as date, ip
    from log
    limit 5;
```

```
   id    |             path              |    date    |       ip
---------+-------------------------------+------------+----------------
 1678923 | /                             | 2016-07-01 | 198.51.100.195
 1678924 | /article/candidate-is-jerk    | 2016-07-01 | 198.51.100.195
 1678925 | /article/goats-eat-googles    | 2016-07-01 | 198.51.100.195
 1678926 | /article/goats-eat-googles    | 2016-07-01 | 198.51.100.195
 1678927 | /article/balloon-goons-doomed | 2016-07-01 | 198.51.100.195
```

Top ten article logs:

```sql
select path, count(*) as hits
    from log
    where path like '/article/%'
        and method = 'GET'
    group by path
    order by hits desc
    limit 10;
```
```
                path                |  hits
------------------------------------+--------
 /article/candidate-is-jerk         | 338647
 /article/bears-love-berries        | 253801
 /article/bad-things-gone           | 170098
 /article/goats-eat-googles         |  84906
 /article/trouble-for-troubled      |  84810
 /article/balloon-goons-doomed      |  84557
 /article/so-many-bears             |  84504
 /article/media-obsessed-with-bears |  84383
 /article/candidate-is-jerkx        |    161
 /article/candidate-is-jerkq        |    155
```

```sql
select path, ip, count(path) as hits
    from log
    where path like '/article/%'
        and method = 'GET'
    group by path, ip
    order by hits desc
    limit 10;
```

```
            path            |       ip       | hits
----------------------------+----------------+------
 /article/candidate-is-jerk | 192.0.2.59     |  541
 /article/candidate-is-jerk | 192.0.2.171    |  523
 /article/candidate-is-jerk | 198.51.100.251 |  512
 /article/candidate-is-jerk | 203.0.113.107  |  511
 /article/candidate-is-jerk | 198.51.100.60  |  510
 /article/candidate-is-jerk | 192.0.2.80     |  507
 /article/candidate-is-jerk | 198.51.100.140 |  506
 /article/candidate-is-jerk | 203.0.113.79   |  503
 /article/candidate-is-jerk | 203.0.113.80   |  502
 /article/candidate-is-jerk | 192.0.2.154    |  502
```