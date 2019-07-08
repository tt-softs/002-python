# 002 - python

Task for today: 2 apps.

1st app:
- takes path to json file on file system as first script argument
- reads the file
- send the content of the file to some flask endpoint, i.e. `localhost:5000/api/add`
- use requests module

2nd app:
- is a flask app
- has two endpoints `/api/add` and `/api/list`
- `/api/add` accepts json payload and adds it to list (will be a list of dictionaries)
- `/api/list` return a html page that displays the list of currently stored jsons
- use jinja2 template for displaying the contents
