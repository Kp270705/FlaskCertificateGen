from flask import Flask, render_template, jsonify, request, flash, redirect
from werkzeug.utils import secure_filename
import os, uuid
from csvFunc import WorkoutData

UPLOAD_FOLDER = 'csvUploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}


csvData = []

app=Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def ProcessData():  # which get data from csv files:
    i=0
    workoutdata = WorkoutData()
    csvData = WorkoutData()
    print(f"First object calories is: {workoutdata[0].calories}")
    for wd in csvData:
        i+=1
        print(f"\n==========\n\nData of Row{i}:-\n----------\na>. Duration of workout: {wd.duration}\nb>. Total number of calories burned during workout: {wd.calories}\nc>. Average Pulse-rate during workout: {wd.pulse}\nd>. Maximum pulse-rate achieved during workout: {wd.maxpulse}")
    print(f"\n\tThere are {i} rows of data in given csv file.\n")



@app.route('/csv', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            ProcessData()
            return render_template("ack.html")

    return render_template("home.html")



@app.route("/csvFile")
def showcsv():
    return render_template("yourData.html")


@app.route("/")
def home():
    return render_template("home.html")

if __name__  ==  "__main__":
    app.run(debug=1, port=5001)
    
    
    