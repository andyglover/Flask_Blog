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

- use if statements to set title, if it is specified in the route

```
@app.route("/about")
def about():
    return render_template('about.html', title='About')
```

```
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% if title %}
    <title>Flask Blog - {{ title }}</title>
    {% else %}
    <title>Flask Blog</title>
    {% endif %}
  </head>
```

- Template inheritance - in templates folder, create layout.html. In the part that you want each page to be able to change (the body of the html), put a content block:

```
  <body>
    {% block content %}{% endblock %}
  </body>
```

- In pages that enherit,

```
{% extends "layout.html" %}
{% block content %}
put content here
{% endblock content %}
```

- You don't have to put the "content" after "endblock" - its optional for clarity.
- Also, you can call it whatever you want. doesn't have to be "content"

- Bootstrap: there is a flask extension that you can use, but you can also just use it directly. Only need to make change to the one template that every page inherits from.
- From the starter template: https://getbootstrap.com/docs/4.3/getting-started/introduction/
- Grab the meta tags and head css, as well as the javascript.
- Put layout page content in a div with class container (bootstrap class)
- Hard refresh = Ctrl + Shift + R = will also clear the cache

- left off @ https://youtu.be/QnDWIZuWYW0?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&t=1201
