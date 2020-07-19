from flask import Flask, render_template

flask = Flask(__name__)


@flask.route('/', methods=["GET"])
def get_main_page():
    return render_template('main.html')


@flask.route('/new_test', methods=["GET"])
def get_new_test_page():
    return render_template('new_test.html')


if __name__ == '__main__':
    flask.run(host="127.0.0.1", port="7000", debug=True, threaded=True, use_reloader=False)