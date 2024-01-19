def write_html(rejected=False):
  # TODO: Display the post the user is commenting on, and the existing comments
  html = f"""<html>
<head>
  <title>Create a Post</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
<body>
  <h1>&lt;yourname&gt;'s Web Journal</h1>
  <div class="create-post">
    <h2>Create a Post</h2>"""
  
  if rejected:
    html += """
    <h3 class="error">Oops, wrong password!</h3>"""

  html += """
    <form method="post">
      <label for="title">Title</label>
      <input name="title"></input>
      <label for="body">Post Body</label>
      <textarea name="body"></textarea>
      <label for="password">Secret Password</label>
      <input type="password" name="password"></input>
      <input type="submit" name="submit" value="Create Post"></input>
    </form>
  </div>
  <a href="/">Home</a>
</body>
</html>"""

  return html