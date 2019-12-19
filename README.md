Parser for parsing https://news.ycombinator.com
================================================
1.A Post is defined as a combination of rank(s.no),title,author and number of comments.

2.For every Author,we keep a dictionary of Author:Karma

3. Python script using only python stuff to parse the website[All the pages]

4. Only Prerequisite is the python3 requests library i.e you should be able to send an http request through your side to the website.

5. Two shell scripts gives top commented posts and top rated author.


Code Repository :https://github.com/gurpreetsachdeva/ycombinator_news_parser
=================

Screenshots Directory:https://github.com/gurpreetsachdeva/ycombinator_news_parser/screenshots
======================

Issues Faced : 
==========================
1. Sometimes the ycombinator server returns 403 for top page[Author one], made it work by executing it from a US based Ec2 box , instead of local machine. This only happens for the user page and not for posts page.

Corner Cases Handled : 
==========================
1. Comments not entered for a post.2. Parse all the pages for the websites, not just the first page.

Rough Design:
=============================

1. Create Two Prototype classes , Posts and Authors

2. Posts has four fields : Rank(SerialNo), Title , Comments(Can be zero) & Author.
3. Author : Every author has a unique name and a karma value.

4. For every page, till you are getting HTML parse the page to give the objects of Posts and Author.

5. Sort them in decreasing order and return the result.

Test Cases checked & Green:
=======================================


1. When only a single comment is there on the post or no comment cases.

2. Match the count for the total posts with the highest rank in your post list.3. For every author, make sure you get a karma value.4. Make sure that the parser parses the whole website


Shell Scripts 
=======================

No Caching Enabled , Everytime go and parse the website.
1. ./get_top_rated_author.sh :Parses the site and prints the name of top author.

2. ./get_top_rated_authors.sh : Parses the site and print the name of the authors in decreasing order of their karmas.

3. ./sort_by_comments.sh : Parses the site and lists the rank,title,author,comments . These rows are ordered by comments desc.
