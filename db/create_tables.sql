create table posts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  slug VARCHAR(30) NOT NULL,
  title VARCHAR(255) NOT NULL,
  body TEXT
);

create table comments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  post_id INT,
  body TEXT,
  author VARCHAR(30),
  FOREIGN KEY(post_id) REFERENCES posts(id)
);

-- -- id AUTOINCREMENT version
-- create table posts (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   slug VARCHAR(30) NOT NULL,
--   title VARCHAR(255) NOT NULL,
--   body TEXT
-- );

-- create table comments (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   post_id INT,
--   body TEXT,
--   author VARCHAR(30),
--   FOREIGN KEY(post_id) REFERENCES posts(id)
-- );
