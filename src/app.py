#!/usr/bin/env python

from app_db import (get_most_viewed_articles,
                    get_most_viewed_authors,
                    get_high_error_days)

from datetime import datetime

"""Udacity Project - Logs Analysis"""
__author__ = "Christiaan Lombard <base1.christiaan@gmail.com>"


# gather database results
articles = get_most_viewed_articles(10)
authors = get_most_viewed_authors(10)
error_days = get_high_error_days(10)

print("# LOGS ANALYSIS")
# print top articles header
print
print("## Top 10 most viewed articles of all time are:")
print

# print top articles
if(len(articles) > 0):
    for i, (id, slug, title, author, views) in enumerate(articles, start=1):
        print("  %s. \"%s\" (%s views)" % (i, title, views))
else:
    print("No articles to report")


# print top authors header
print
print("## Top 10 authors with the most views are:")
print

# print top authors
if(len(authors) > 0):
    for i, (id, name, sum_views) in enumerate(authors, start=1):
        print("  %s. %s (%s views)" % (i, name, sum_views))
else:
    print("  No authors to report")


# print error days header
print
print("## Days where more than 1% of requests led to errors:")
print

# print error days
if(len(error_days) > 0):
    for i, (date, total, client_error, error_percent) \
            in enumerate(error_days, start=1):
        pretty_date = date.strftime('%d %b, %Y')
        print("  %s. %s (%s%% errors)" % (i, pretty_date, error_percent))
else:
    print("  No days to report")

print
