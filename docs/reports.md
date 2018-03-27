# Reports


## 1. What are the most popular three articles of all time?
Which articles have been accessed the most?

```sql
select path, count(path) as hits, count(distinct ip) as unique_hits
    from log
    where path like '/article/%'
        and method = 'GET'
        and status = '200 OK'
    group by path
    order by hits
    limit 10;

select ip, count(*)
    from log
    where path like '/article/%'
        and method = 'GET'
        and status = '200 OK'
    group by ip
    limit 20;



```

## 2. Who are the most popular article authors of all time?

That is, when you sum up all of the articles each author has written, which authors get the most page views?

## 3. On which days did more than 1% of requests lead to errors?

