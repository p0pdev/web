from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('database.db')
c = conn.cursor()

@app.route('/')
def index():
    c.execute("SELECT * FROM pages")
    pages = c.fetchall()
    return render_template('index.html', pages=pages)

@app.route('/<page_id>')
def page(page_id):
    c.execute("SELECT * FROM pages WHERE id=?", (page_id,))
    page = c.fetchone()
    return render_template('page.html', page=page)

if __name__ == '__main__':
    app.run(debug=True)
