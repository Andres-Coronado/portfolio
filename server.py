from statistics import mode
from flask import Flask, redirect, render_template, url_for, request
import csv
app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt',mode='a') as database:
#         email = data['email']
#         subject = data ['subject']
#         message = data['message']
#         file = database.write(f'\n {email},{subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='',mode='a') as database2:
        email = data['email'];
        subject = data ['subject'];
        message = data['message'];
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL);
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'STH went wrong'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# # @app.route('/components.html')
# # def components():
# #     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/project.html')
# def project():
#     return render_template('project.html')

# @app.route('/services.html')
# def services():
#     return render_template('services.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')
