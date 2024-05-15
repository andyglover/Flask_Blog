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

- left off @ https://youtu.be/QnDWIZuWYW0?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&t=346
