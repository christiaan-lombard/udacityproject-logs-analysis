#!/usr/bin/env python

"""Database for Logs Analysis app

    Requires view 'article_views':

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


"""
__author__ = "Christiaan Lombard <base1.christiaan@gmail.com>"

import psycopg2

conn = None

MOST_VIEWED_ARTICLES_SQL = '''
select a.id, a.slug, a.title, a.author, v.views
    from articles as a
    join article_views as v on (v.article_slug = a.slug)
    order by v.views desc
    limit %d;
'''

MOST_VIEWED_AUTHORS_SQL = '''
select p.id, p.name, sum(v.views) as sum_views
    from articles as a
    join article_views as v on (v.article_slug = a.slug)
    join authors as p on (p.id = a.author)
    group by p.id
    order by sum_views desc
    limit %d;
'''


def get_most_viewed_articles(limit):
    """Get the most viewed articles.

    Arguments:
        limit (integer) -- Limit number of results

    Returns:
        [(article_slug, views, unique_views)] -- The results
    """

    return db_fetch_all(MOST_VIEWED_ARTICLES_SQL, [limit])



def get_most_viewed_authors(limit):
    """Get the authors with the most views.

    Arguments:
        limit (integer) -- Limit number of results

    Returns:
        ([article_slug, views, unique_views]) -- The results
    """

    return db_fetch_all(MOST_VIEWED_AUTHORS_SQL, [limit])


def db_fetch_all(sql, params):
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, params)
    records = cur.fetchall()
    conn.close()
    return records