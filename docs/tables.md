# Tables

```
\dt

 Schema |   Name   | Type  |  Owner
--------+----------+-------+---------
 public | articles | table | vagrant
 public | authors  | table | vagrant
 public | log      | table | vagrant
```

## Table Articles

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

## Table Authors

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

## Table Log

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
select id, path, status, date(time) as date
    from log
    limit 5;
```

```
   id    |             path              | status |    date
---------+-------------------------------+--------+------------
 1678923 | /                             | 200 OK | 2016-07-01
 1678924 | /article/candidate-is-jerk    | 200 OK | 2016-07-01
 1678925 | /article/goats-eat-googles    | 200 OK | 2016-07-01
 1678926 | /article/goats-eat-googles    | 200 OK | 2016-07-01
 1678927 | /article/balloon-goons-doomed | 200 OK | 2016-07-01
```
