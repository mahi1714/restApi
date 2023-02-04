from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def tktk():
    return "hello Mahi"
@app.route('/squar')
def squar():
    stdInfo = [
        {
        'Name': "Mobinul Islam Mahi",
        'Roll': 593314,
        'Department': 'Computer'
        },
        {
        'Name': "Sadid Rahin Nohan",
        'Roll': 593316,
        'Department': 'Computer'
        },
        {
        'Name': "Tarek Rahman",
        'Roll': 585641,
        'Department': 'Civil'
        },
        {
        'Name': "Efti Mahmud Jishan",
        'Roll': 545659,
        'Department': 'Food'
        },
        {
        'Name': "Yeasrif Rashid Tamim",
        'Roll': 585692,
        'Department': 'Computer'
        },
        {
        'Name': "Tanvir Rafi",
        'Roll': 593329,
        'Department': 'Computer'
        },
        {
        'Name': "Shahedul Islam",
        'Roll': 659845,
        'Department': 'Food'
        },
        {
        'Name': "Mohammad Shahin",
        'Roll': 585462,
        'Department': 'Food'
        },
        {
        'Name': "Mohammad Imran",
        'Roll': 545963,
        'Department': 'Food'
        },
        {
        'Name': "Sadek Hossen",
        'Roll': 593954,
        'Department': 'Computer'
        },
        {
        'Name': "Md Fahim",
        'Roll': 593341,
        'Department': 'Computer'
        },
        {
        'Name': "Mohammad Ibrahim",
        'Roll': 584623,
        'Department': 'Computer'
        },
        {
        'Name': "Mohammad Saimon",
        'Roll': 593356,
        'Department': 'Computer'
        },
        {
        'Name': "Mohammad Tarek",
        'Roll': 593335,
        'Department': 'Computer'
        },
        {
        'Name': "Shahariar Emon",
        'Roll': 593342,
        'Department': 'Computer'
        },
        {
        'Name': "Mohammad Kajol",
        'Roll': 593338,
        'Department': 'Computer'
        },
        {
        'Name': "Saiful Islam",
        'Roll': 585459,
        'Department': 'Computer'
        },

    ]
    return jsonify(stdInfo)
if __name__ == '__main__':
    app.run(debug=true)