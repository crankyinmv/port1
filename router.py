from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
#@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    print('PAGE',page_name)
#    if page_name == 'favicon.ico':
#        return
    return render_template(page_name)

@app.route("/blog")
def hello_world2():
    return "<p>Blogs poo</p>"

@app.route('/user/<username>')
def hello_world3(username=None):
    return render_template('index.html', name=username)

@app.route('/user/<username>/<int:post_id>')
def hello_world4(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        block = ''
        fields = []
        vals = []
        for field in data:
            fields.append(field)
            vals.append(data[field])
            #block += field+': '+data[field]+'\n'
        csv_writer = csv.writer(database2, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(vals)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        header,value = '','';
        for field in data:
            if(header != ''):
                header += ','
                value += ','
            header += field
            value += data[field]
        file = database.write(f'{header}\n{value}\n')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('landing.html')
        except:
            return 'db shit the bed'
    return 'oh poo'

