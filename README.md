# Udacity Project - Logs Analysis

This is my project submission for the Udacity Fullstack Developer Nanodegree, Backend Module, Logs Analysis Project.

In this project SQL is used to make sense of a request logs table and draw reports on popular news articles.

See [Report Notes](docs/reports.md) for more info.
See [Example Output](output.md) to see result.


## Install & Run

### VM

To run the application inside a VM, install [Vagrant]() and run:

```sh
vagrant up
vagrant ssh
```

In the vm shell go to the synced folder:

```sh
cd /vagrant
```

### Install

Download the data, [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), and unzip `newsdata.sql` in the repository root.

Run the `psql` commands to seed the database from `newsdata.sql`.

```sh
createdb news       # if news database not created already

psql -d news -f newsdata.sql    # install seed data
psql -d news -f ./src/views.sql # install views
```

Alternatively create the views as below:

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


### Run

Run the application:

```sh
python3 ./src/app.py
```

Output result to markdown file:

```sh
python3 ./src/app.py > output.md
```


### Test PEP8

```sh
pycodestyle ./src/app.py ./src/app_db.py
```


## Docs & Resources

 - [Query Notes](docs/queries.md)
 - [Report Notes](docs/reports.md)
 - [Data Structure Notes](docs/tables.md)
 - [Example Output](output.md)
 - [newsdata.sql seed data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)



## Udacity Project Specifications

Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

### So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

**1. What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

 - "Princess Shellfish Marries Prince Handsome" — 1201 views
 - "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
 - "Political Scandal Ends In Political Scandal" — 553 views

**2. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

 - Ursula La Multa — 2304 views
 - Rudolf von Treppenwitz — 1985 views
 - Markoff Chaney — 1723 views
 - Anonymous Contributor — 1023 views

**3. On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

 - July 29, 2016 — 2.5% errors

### Good coding practices

#### SQL style

Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the where clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

In building this tool, you may find it useful to add views to the database. You are allowed and encouraged to do this! However, if you create views, make sure to put the create view commands you used into your lab's README file so your reviewer will know how to recreate them.

#### Python code quality

Your code should be written with good Python style. The PEP8 style guide is an excellent standard to follow. You can do a quick check using the pep8 command-line tool.