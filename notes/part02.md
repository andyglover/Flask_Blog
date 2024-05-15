part 2: https://youtu.be/QnDWIZuWYW0?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

- use ''' for multiline string:

```
    @app.route("/home")
    def home():
        return '''<!doctype html>
        <html>
        ...etc
        '''
```

- create a templates directory with html files. import render_template

```
def home():
    return render_template('home.html')
```

- variable used in template = data

```
return render_template('home.html', posts=posts)
```

- array of dictionaries to hold posts data

```
posts = [
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
]
```

- loop through array and pull data from each with special syntax.

```
  <body>
    {% for post in posts %}
    <h1>{{ post.title }}</h1>
    <p>By {{ post.author }} on {{ post.date_posted }}</p>
    <p>{{ post.content }}</p>
    {% endfor %}
  </body>
```

- left off @ https://youtu.be/QnDWIZuWYW0?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&t=346
