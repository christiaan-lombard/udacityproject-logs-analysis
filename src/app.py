#!/usr/bin/env python3
#
# Udacity Project - Logs Analysis
#

from flask import Flask, request, redirect, url_for

from app_db import get_most_viewed_articles

print(get_most_viewed_articles(10))