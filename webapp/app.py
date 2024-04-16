from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model from the pickle file
with open('static/datasets/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=["GET"])
def student_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    # Get form data
    cgpa = float(request.form['CGPA'])
    internships = int(request.form['Internships'])
    projects = int(request.form['Projects'])
    workshops = int(request.form['Workshops/Certifications'])
    aptitude_score = int(request.form['AptitudeTestScore'])
    soft_skills = float(request.form['SoftSkillsRating'])
    extracurricular_yes = 1 if request.form['ExtracurricularActivities'] == "Yes" else 0
    extracurricular_no = 1 if request.form['ExtracurricularActivities'] == "No" else 0
    placement_training_yes = 1 if request.form['PlacementTraining'] == "Yes" else 0
    placement_training_no = 1 if request.form['PlacementTraining'] == "No" else 0
    ssc_marks = int(request.form['SSC_Marks'])
    hsc_marks = int(request.form['HSC_Marks'])
    
    # Make predictions using the model
    features = [[cgpa, internships, projects, workshops, aptitude_score, soft_skills, ssc_marks, hsc_marks, extracurricular_no, extracurricular_yes, placement_training_no, placement_training_yes]]

    predicted_value = model.predict(features)

    print(predicted_value)
    
    # Render a template with the predicted value
    return render_template('index.html', PlacementStatus="Likely to be placed" if predicted_value[0] else "Not Likely to be placed")

if __name__ == '__main__':
    app.run(debug=True)
