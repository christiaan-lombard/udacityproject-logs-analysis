#!/usr/bin/env python

"""Database for Logs Analysis app

    Requires views 'article_views' and 'log_daily_status'
    as defined in views.sql

"""
__author__ = "Christiaan Lombard <base1.christiaan@gmail.com>"

import psycopg2


MOST_VIEWED_ARTICLES_SQL = '''
select a.id, a.slug, a.title, a.author, v.views
    from articles as a
    join article_views as v on (v.article_slug = a.slug)
    order by v.views desc
    limit %s;
'''

MOST_VIEWED_AUTHORS_SQL = '''
select p.id, p.name, sum(v.views) as sum_views
    from articles as a
    join article_views as v on (v.article_slug = a.slug)
    join authors as p on (p.id = a.author)
    group by p.id
    order by sum_views desc
    limit %s;
'''

HIGH_ERROR_DAYS_SQL = '''
select date, total, client_error, (client_error*100 / total) as error_percent
    from log_daily_status
    where (client_error*100 / total) > 1
    order by error_percent desc;
'''


def get_most_viewed_articles(limit):
    """Get the most viewed articles.

    Arguments:
        limit (integer) -- Limit number of results

    Returns:
        [(id, slug, title, author, views)] -- The results
    """

    return db_fetch_all(MOST_VIEWED_ARTICLES_SQL, [limit])


def get_most_viewed_authors(limit):
    """Get the authors with the most views.

    Arguments:
        limit (integer) -- Limit number of results

    Returns:
        [(id, name, sum_views)] -- The results
    """

    return db_fetch_all(MOST_VIEWED_AUTHORS_SQL, [limit])


def get_high_error_days(limit):
    """Get the days on which more than 1%
    of requests are client errors.

    Arguments:
        limit (integer) -- Limit number of results

    Returns:
        [(date, total, client_error, error_percent)] -- The results
    """

    return db_fetch_all(HIGH_ERROR_DAYS_SQL, [limit])



def db_fetch_all(sql, params):
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    cur.execute(sql, params)
    records = cur.fetchall()
    conn.close()
    return records
