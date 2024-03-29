from flask import Flask, render_template, request


app = Flask(__name__, static_folder="templates/css")
print(app.static_url_path + "style.css")

# Variables (combined and adjusted for consistency)
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
time_range = range(1, 25)
wind_speed_range = range(0, 1000)
wind_directions = ["N", "S", "W", "E"]
site_names = ["Le Tacque", "Plemont", "La Pulante"]
winter_months = ["November", "December", "January", "February", "March"]
summer_months = ["April", "May", "June", "July", "August", "September", "October"]
yes_no_responses = ["yes", "no", "y", "n"]

# Functions (adapted for web interactions)
def _get_decision(name, month, time, windspeed, winddirection, sitename):
    # Enhanced decision-making logic (example for one site)
    if (
        month in winter_months
        and 7 <= time < 16
        and 5 <= windspeed < 38
        and winddirection == "W"
        and sitename == "Le Tacque"
    ):
        return f"Dear {name}, flying at {sitename} in {month} at {time}:00, with windspeed of {windspeed} km/h and wind blowing from {winddirection} indicates flyable conditions!"
    elif (
        month in winter_months
        and 7 <= time < 16
        and 5 <= windspeed < 38
        and winddirection == "N"
        and sitename == "Plemont"
    ):
        return f"Dear {name}, flying at {sitename} in {month} at {time}:00, with windspeed of {windspeed} km/h and wind blowing from {winddirection} indicates flyable conditions!"
    elif (
        month in winter_months
        and 7 <= time < 16
        and 5 <= windspeed < 38
        and winddirection == "S"
        and sitename == "La Pulante"
    ):
        return f"Dear {name}, flying at {sitename} in {month} at {time}:00, with windspeed of {windspeed} km/h and wind blowing from {winddirection} indicates flyable conditions!"
    
    elif (
        month in summer_months
        and 6 <= time < 21
        and 5 <= windspeed < 38
        and winddirection == "W"
        and sitename == "Le Tacque"
    ):
        return f"Dear {name}, flying at {sitename} in {month} at {time}:00, with windspeed of {windspeed} km/h and wind blowing from {winddirection} indicates flyable conditions!"
    elif (
        month in summer_months
        and 6 <= time < 21
        and 5 <= windspeed < 38
        and winddirection == "N"
        and sitename == "Plemont"
    ):
        return f"Dear {name}, flying at {sitename} in {month} at {time}:00, with windspeed of {windspeed} km/h and wind blowing from {winddirection} indicates flyable conditions!"
    elif (
        month in summer_months
        and 6 <= time < 21
        and 5 <= windspeed < 38
        and winddirection == "S"
        and sitename == "La Pulante"
    ):
        return f"Dear {name}, flying at {sitename} in {month} at {time}:00, with windspeed of {windspeed} km/h and wind blowing from {winddirection} indicates flyable conditions!"
    else:
        return f"Dear {name}, flying at {sitename} in {month} at {time}:00, with windspeed of {windspeed} km/h and wind blowing from {winddirection} NOT ADVISABLE!"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        name = request.form['name']
        month = request.form['month'].title()  # Ensure month is capitalized
        time = int(request.form['time'])  # Convert time to integer
        windspeed = int(request.form['windspeed'])  # Convert windspeed to integer
        winddirection = request.form['winddirection']
        sitename = request.form['sitename']

        # Comprehensive input validation
        if month not in month_names:
            raise ValueError("Invalid month name")
        if time not in time_range:
            raise ValueError("Invalid time")
        if windspeed not in wind_speed_range:
            raise ValueError("Invalid windspeed")
        if winddirection not in wind_directions:
            raise ValueError("Invalid wind direction")
        if sitename not in site_names:
            raise ValueError("Invalid site name")

        decision = _get_decision(name, month, time, windspeed, winddirection, sitename)
        return render_template('index.html', name=name, decision=decision)
    except ValueError as e:
        return render_template('index.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
