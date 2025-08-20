from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('court_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cases
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, case_no TEXT, title TEXT, date TEXT, status TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_no = request.form['case_no']
        message = f"Fetching data for Legal Cases - {case_no}"
        
        # Mock data for demo
        mock_data = {
            "case_no": case_no,
            "title": "State vs John Doe",
            "date": "2025-05-10",
            "status": "Pending"
        }
        
        conn = sqlite3.connect('court_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO cases (case_no, title, date, status) VALUES (?, ?, ?, ?)",
                  (mock_data['case_no'], mock_data['title'], mock_data['date'], mock_data['status']))
        conn.commit()
        conn.close()
        
        return render_template('results.html', case=mock_data, message=message)
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
