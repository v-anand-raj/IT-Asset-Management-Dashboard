from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# READ CSV
df = pd.read_csv("employees.csv")

# CLEAN COLUMN NAMES
df.columns = df.columns.str.strip().str.replace(r'\s+', ' ', regex=True)

# PRINT COLUMN NAMES
print(df.columns)

# ---------------- HOME PAGE ----------------

@app.route('/')
def home():
    return render_template('login.html')


# ---------------- LOGIN ROUTE ----------------

@app.route('/login', methods=['POST'])
def login():

    # GET FORM DATA
    name = request.form['name'].strip()
    password = request.form['password'].strip()

    # CLEAN CSV COLUMNS
    names = df['Name'].astype(str).str.strip()

    pno = df['P. No.'].astype(str) \
                      .str.replace('.0', '', regex=False) \
                      .str.strip()

    staffno = df['Staff No.'].astype(str) \
                            .str.replace('.0', '', regex=False) \
                            .str.strip()

    # AUTHENTICATION CHECK
    user = df[
        (names == name) &
        (
            (pno == password) |
            (staffno == password)
        )
    ]

    # LOGIN SUCCESS
    if not user.empty:

        return render_template('home.html')

    # LOGIN FAILED
    else:

        return "Invalid Credentials"


# ---------------- SEARCH ROUTE ----------------

@app.route('/search', methods=['POST'])
def search():

    # GET SEARCH QUERY
    query = request.form['query'].strip()

    # CLEAN COLUMNS
    names = df['Name'].astype(str).str.strip()

    pno = df['P. No.'].astype(str) \
                      .str.replace('.0', '', regex=False) \
                      .str.strip()

    staffno = df['Staff No.'].astype(str) \
                            .str.replace('.0', '', regex=False) \
                            .str.strip()

    # SEARCH LOGIC
    result = df[
        (names.str.lower().str.contains(query.lower())) |
        (pno == query) |
        (staffno == query)
    ]

    # REMOVE NaN VALUES
    result = result.fillna("")

    # CONVERT TO JSON
    employees = result.to_dict(orient='records')

    return jsonify(employees)


# ---------------- RUN APP ----------------

if __name__ == '__main__':
    app.run(debug=True)