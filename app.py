from flask import Flask, request, render_template
import pyodbc

app = Flask(__name__)

# SQL Server connection details
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=your_sql_server_Chanto;'
    'DATABASE=MuntunkundiDB;'
    'UID=marie;'
    'PWD=Amahoro321;'
    'TrustServerCertificate=yes;'
)
cursor = conn.cursor()

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]

    cursor.execute("INSERT INTO Users (Name, Phone, Email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()

    return "Data saved successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
app
