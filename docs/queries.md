




### Logs grouped by status

```sql
select status, count(*) as num
    from log
    group by status
    order by num desc
    limit 5;
```
```
    status     |   num
---------------+---------
 200 OK        | 1664827
 404 NOT FOUND |   12908
```


### Logs grouped by path

```sql
select path, count(*) as hits
    from log
    group by path
    order by hits desc
    limit 20;
```
```
                path                |  hits
------------------------------------+--------
 /                                  | 479121
 /article/candidate-is-jerk         | 338647
 /article/bears-love-berries        | 253801
 /article/bad-things-gone           | 170098
 /article/goats-eat-googles         |  84906
 /article/trouble-for-troubled      |  84810
 /article/balloon-goons-doomed      |  84557
 /article/so-many-bears             |  84504
 /article/media-obsessed-with-bears |  84383
 /spam-spam-spam-humbug             |    301
 /%20%20%20                         |    290
 /+++ATH0                           |    288
 /article/candidate-is-jerkx        |    161
 /article/candidate-is-jerkq        |    155
 /article/candidate-is-jerkh        |    152
 /article/candidate-is-jerkr        |    148
 /article/candidate-is-jerkg        |    147
 /article/candidate-is-jerke        |    146
 /article/candidate-is-jerkl        |    144
 /article/candidate-is-jerkb        |    144
(20 rows)
```

### Top article logs:

```sql
select path, count(*) as hits
    from log
    where path like '/article/%'
        and method = 'GET'
        and status = '200 OK'
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


### Logs grouped by day, agregating status types

```sql
select
    date(time) as date,
    count(status) filter (where status like '2%') as success,
    count(status) filter (where status like '3%') as redirect,
    count(status) filter (where status like '4%') as client_error,
    count(status) filter (where status like '5%') as server_error,
    count(status) as total
from log
group by date
order by client_error desc
limit 5;
```
```
    date    | success | redirect | client_error | server_error | total
------------+---------+----------+--------------+--------------+-------
 2016-07-17 |   54642 |        0 |         1265 |            0 | 55907
 2016-07-19 |   54908 |        0 |          433 |            0 | 55341
 2016-07-24 |   54669 |        0 |          431 |            0 | 55100
 2016-07-05 |   54162 |        0 |          423 |            0 | 54585
 2016-07-06 |   54354 |        0 |          420 |            0 | 54774
```
