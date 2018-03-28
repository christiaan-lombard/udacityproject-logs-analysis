# Reports


## 1. What are the most popular three articles of all time?
Which articles have been accessed the most?

### Agregate number of views for each article:

Create a view `article_views` to get the total number of views and unique views (by ip) for each article.

```sql
create view article_views as
    select
        substring(path from 10) as article_slug,
        count(path) as views,
        count(distinct ip) as unique_views
    from log
    where
        path like '/article/%'
        and method = 'GET'
        and status = '200 OK'
    group by path;
```
```
       article_slug        | views  | unique_views
---------------------------+--------+--------------
 bad-things-gone           | 170098 |          762
 balloon-goons-doomed      |  84557 |          762
 bears-love-berries        | 253801 |          762
 candidate-is-jerk         | 338647 |          762
 goats-eat-googles         |  84906 |          762
 media-obsessed-with-bears |  84383 |          762
 so-many-bears             |  84504 |          762
 trouble-for-troubled      |  84810 |          762
(8 rows)
```

### Join views with articles table

```sql
select a.id, a.slug, a.title, a.author, v.views
    from articles as a
    join article_views as v on (v.article_slug = a.slug)
    order by v.views desc
    limit 10;
```
```
 id |           slug            |        title          | author | views
----+---------------------------+-----------------------+--------+--------
 26 | candidate-is-jerk         | Candidate is jerk, al |      2 | 338647
 25 | bears-love-berries        | Bears love berries, a |      1 | 253801
 23 | bad-things-gone           | Bad things gone, say  |      3 | 170098
 27 | goats-eat-googles         | Goats eat Google's la |      1 |  84906
 30 | trouble-for-troubled      | Trouble for troubled  |      2 |  84810
 24 | balloon-goons-doomed      | Balloon goons doomed  |      4 |  84557
 29 | so-many-bears             | There are a lot of be |      1 |  84504
 28 | media-obsessed-with-bears | Media obsessed with b |      1 |  84383
(8 rows)
```

## 2. Who are the most popular article authors of all time?

That is, when you sum up all of the articles each author has written, which authors get the most page views?

### Join views with articles table group by author

```sql
select p.id, p.name, sum(v.views) as sum_views
    from articles as a
    join article_views as v on (v.article_slug = a.slug)
    join authors as p on (p.id = a.author)
    group by p.id
    order by sum_views desc
    limit 10;
```
```
 id |          name          | sum_views
----+------------------------+-----------
  1 | Ursula La Multa        |    507594
  2 | Rudolf von Treppenwitz |    423457
  3 | Anonymous Contributor  |    170098
  4 | Markoff Chaney         |     84557
(4 rows)
```

## 3. On which days did more than 1% of requests lead to errors?


### Agregate daily logs

```sql
create view log_daily_status as
    select
        date(time) as date,
        count(status) filter (where status like '2%') as success,
        count(status) filter (where status like '3%') as redirect,
        count(status) filter (where status like '4%') as client_error,
        count(status) filter (where status like '5%') as server_error,
        count(status) as total
    from log
    group by date;
```

### Select days where more than 1% client error

```sql
select date, total, client_error, (client_error*100 / total) as error_percent
    from log_daily_status
    where (client_error*100 / total) > 1
    order by error_percent desc;

```
```
    date    | total | client_error | error_percent
------------+-------+--------------+---------------
 2016-07-17 | 55907 |         1265 |             2
```