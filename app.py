"""Credit to Bytive on Youtube for helping connecting HTML with Python """
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    result = ""
    import csv
    Time_hour = 0
    Time_minute = 0
    Time_second = 0

    # Open the CSV file for reading
    with open('Key Club Service Hours - 2023-2024 (1).csv', newline='') as csvfile:
        # Create a CSV reader
        csvreader = csv.reader(csvfile)

        # Iterate through each row in the CSV file
        for row in csvreader:
            # Each 'row' is a list of values
            try:
                if type(int(row[0])) == int:
                    if int(row[0]) == int(name):
                        result += "Hello " + row[1] + ", on " + row[4] +  " you participated in " + row[3] + " for a total " + row[7] + " hour(s).\n"
                        Time_broken = row[7].split(":")
                        Time_hour += int(Time_broken[0])
                        Time_minute += int(Time_broken[1])
                        Time_second += int(Time_broken[2])
            except:
                continue

    Time_minute += int(Time_second / 60)
    Time_second = int(Time_second % 60)
    Time_hour += int(Time_minute / 60)
    Time_minute = int(Time_minute) % 60
    result += "Your total hour(s) is " + str(Time_hour) + " hour(s) "+  str(Time_minute) +  " min(s) " + str(Time_second) + " second(s) \n"
    return render_template("index.html", name=result)
if __name__ == '__main__':
    app.run(debug = True, port = 5001)
