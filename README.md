# Exercise 3: A Weblog

5 points

**DUE: Friday, April 14 by 5:30pm**

### Instructions

One very common kind database-driven web application is a Content Management
System, or CMS. A CMS provides an interface for users to write content—posts,
articles, whole web pages—that is stored in a database, and then creates web
pages from those entries, without the author needing to know any HTML. And by
far the most popular CMS, [WordPress](https://wordpress.com/),is a PHP
application.

We're going to make our own very simple CMS for a web journal, with posts and
comments. The assignment this week is to modify the `.php` files in `exercise_3`
to make the pages display posts and comments that are stored in a database, and
to enable users to create new posts and leave new comments.

First you'll need your own working version of our modified LAMP stack, with
SQLite replacing MySQL, and your laptop's OS replacing Linux, and PHP's built-in
web server instead of Apache.

<details>
    <summary><b>Mac Instructions</b></summary>

    - Install PHP: https://www.php.net/manual/en/install.macosx.packages.php)
    - SQLite is already installed
</details>

<details>
    <summary><b>Windows Instructions</b></summary>

    - Install Windows Subsystem Linux (WSL): https://learn.microsoft.com/en-us/windows/wsl/install
    - Inside WSL, install php:
      `sudo apt-get install -y git php8.2 php8.2-curl php8.2-xml php8.2-mbstring php8.2-gd php8.2-sqlite3`
    - Download SQLite: https://www.sqlite.org/download.html
</details>

From the root our your exercise directory (ie this one), launch PHP's
[built-in web server](https://www.php.net/manual/en/features.commandline.webserver.php):

`php -S localhost:8000`

You should be able to see your pages at e.g. http://localhost:8000/weblog.php

From there:
1. You can connect to the SQLite3 database in `db/weblog.sqlite3`. It has
  already been set up to have tables for posts and comments by running the
  commands in `create_tables.sql`.
1. Modify `weblog.php` to fetch posts and their associated comments from the
    database and display them to visitors.
    - Use no more than two queries to get the existing posts and their comments
      (it's possible to do this in one query).
    - Display posts in reverse chronological order. That is, with the newest
      (highest id) posts at the top. Display Comments in chronological order from
      lowest id to highest.
    - Put the `id` of posts in the appropriate HTML attributes to enable
      linking to individual posts on the page and to comment pages for each post.
    - When displaying user-entered information like titles, posts, or usernames, use
      the [htmlspecialchars](https://www.php.net/manual/en/function.htmlspecialchars.php)
      function to make sure special characters like < and > render correctly in HTML.
    - Replace `<yourname>` with your name.
1. Modify `create_post.php` to insert a new row in the `posts` table.
    - Be sure to add a secret password in the PHP code, and only add a row if the
      password the user entered matches! For ease in grading, use the password `punpernickel`
    - Use the `id` attribute to our posts and include it as a
      [URL Fragment](https://en.wikipedia.org/wiki/URI_fragment) in our links to
      let us deep link to a specific post.
    - Because we're accepting content from users, be sure to
      [sanitize your inputs](https://xkcd.com/327/) using prepared statements to
  do the inserts rather than creating queries with string concatenation.
1. Modify `leave_comment.php` to enable users to leave comments on posts.
    - We'll get a `post_id` as a query param. Fetch the post and any existing
      comments from the database in a single query (you'll have to use a `JOIN`).
    - We'll let any users post comments without authentication. It's become clear
      that's a bad idea on the real internet, but it's fine for this exercise.
    - When a user posts a new comment, add a new row to the `comments` table,
      sanitizing as before.

Don't worry about mobile layouts for this exercise, about or about features like
previewing or editing. When you are done, push the `exercise-3` folder to your
class repository on GitLab.

Remember to include in your submission any classmates you collaborated with and
any materials you consulted.

### Rubric

One point each for:
- Correctly retrieves a single post or comment from the the database with SELECT
- Uses one query with a JOIN to fetch a post and any of its
  comments for the leave_comment page.
- Uses no more than two queries to fetch all the posts and all their comments
  for the main page. (It's possible to do this in one query, though it does make
  looping over the results more complicated).
- Server-side rendering: Correctly builds main page from fetched data: loops to
  write Post and Comment divs. Displays newest Posts at the top, and Comments in
  chronological order.
- Correctly builds the leave_comment.php page, displaying the text of the post,
  and other comments posted so far in the thread.
- Form submission: Correctly handles POSTing new posts and comments and parses
  them out of the `$_POST` supervariable.
- INSERT: Correctly inserts posted comments and posts to the database. Comments
  have the correct relationship to posts.
- Escaping: Correctly uses `htmlspecialchars` when rendering the content of posts
  and comments, which are usedr-generated.
- Correctly sanitizes user-provided data for posts by binding values to prepared 
  statements.
- Correctly sanitized user-provided data for comments by binding values to prepared 
  statements.
