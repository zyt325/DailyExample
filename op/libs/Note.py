def save_article(filename, title, article_id,body_html):
    article_body_html_content = """<!DOCTYPE html>
  <html lang="zh">
  <head>
    <meta charset="utf-8" />
    <title>{0}</title>
    <link rel="stylesheet" href="/static/css/note_html.css" />
  </head>
  <body>
  <div id="container">
  <div id="article_header">
      <header>
        <span><button article_id="{1}" onclick="article_edit(this)">Edit</button></span>
      </header>
    </div>
    <div id="article_sort">
    </div>
    <div id="article_list" class="markdown-body editormd-preview-container" previewcontainer="true">
      {2}
  </div>
  <script src="/static/js/article.js"></script>
  </body>
  </html>
    """.format(title, article_id,body_html)
    from django.conf import settings
    import os
    upload_path = settings.MEDIA_ROOT + '/note/'
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    article_path = upload_path + filename
    with open(article_path, 'wb') as f:
        f.write(article_body_html_content.encode("utf-8"))