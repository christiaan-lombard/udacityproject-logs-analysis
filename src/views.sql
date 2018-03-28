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