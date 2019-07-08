from flask import Flask, request, render_template

app = Flask(__name__)
list_of_dict = []

@app.route('/api/add', methods=['POST'])
def add():

    try:
        if request.method == 'POST':
            # data =request.json()
            data = request.get_json()
            print(str(request) + "\n***********\n"+str(data)+"\n***********\n")
            list_of_dict.append(data)
    except:
        print("This didn't work.")
    print(str(list_of_dict)+"\n***********\n")
    return ""


@app.route('/api/list', methods=['GET'])
def return_all_jsons():
    return render_template("index_all.html",
                           title='Task for flask',
                           list_of_dict=list_of_dict)


@app.route('/')
def hello_world():
    return 'Task for flask'


if __name__ == '__main__':
    app.run()
