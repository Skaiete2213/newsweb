from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup # SAU SCRAPY FRAMEWORKS!!! ASTA E MAI BUN
import pprint

#@app.route('/<username>/<int:post_id>')
#def hello_world(username = None, post_id = None):
    #return render_template('./index.html', name = username, post_id=post_id)


@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def heyhey(): # ASTA E PENTRU A LUA O VARIABILA DIN SUBTIM MESSAGE SI SA O PUI PE PAGINA!!!!{{}}
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        em = request.form['username']
        username = em
        write_to_csv(data)
        return render_template('./thankyou.html', username=username)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as dtsb2:
        name = data['username']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(dtsb2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])

def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        return redirect('/thankyou.html')
    else:
        'something went wrong! Try again'



if __name__ == '__main__':
 app.run(debug=True)