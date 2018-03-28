#!/usr/bin/env python

"""Udacity Project - Logs Analysis"""
__author__ = "Christiaan Lombard <base1.christiaan@gmail.com>"

from app_db import get_most_viewed_articles, get_most_viewed_authors, get_high_error_days
from datetime import datetime

print("# LOGS ANALYSIS")
print
print("## Top 10 most viewed articles of all time are:")
print

articles = get_most_viewed_articles(10)
if(len(articles) > 0):
    for i, (id, slug, title, author, views) in enumerate(articles, start=1):
        print("  %s. \"%s\" (%s views)" % (i, title, views))
else:
    print("No articles to report")

print
print("## Top 10 authors with the most views are:")
print

authors = get_most_viewed_authors(10)
if(len(authors) > 0):
    for i, (id, name, sum_views) in enumerate(authors, start=1):
        print("  %s. %s (%s views)" % (i, name, sum_views))
else:
    print("  No authors to report")

# print error days

print
print("## Days where more than 1% of requests led to errors:")
print

error_days = get_high_error_days(10)

if(len(error_days) > 0):
    for i, (date, total, client_error, error_percent) in enumerate(error_days, start=1):
        pretty_date = date.strftime('%d %b, %Y')
        print("  %s. %s (%s%% errors)" % (i, pretty_date, error_percent))
else:
    print("  No days to report")

print
