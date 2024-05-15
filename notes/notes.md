# helpful info:

part 1: https://youtu.be/MwZwr5Tvyxo?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

- pip install flask
- https://flask.palletsprojects.com/en/3.0.x/
- for UNIX, "export FLASK_APP=flaskblog.py"
- for windows, this worked: $env:FLASK_APP = "flaskblog.py"
- flask run
- http://127.0.0.1:5000/ or "localhost" will open app.
- Ctrl + C stops webserver.
- $env:FLASK_DEBUG=1
- (now you don't have to restart web server to see changes)
- This lets you run with python directly:

```
if __name__ == '__main__':
    app.run(debug=True)
```

```
python flaskblog.py
```

- left off @ https://youtu.be/MwZwr5Tvyxo?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&t=848
