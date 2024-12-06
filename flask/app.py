from flask import Flask, request, render_template
import pickle
import numpy as np
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/static-visualizations')
def static_visualizations():
    return render_template('static-visualizations.html')

@app.route('/interactive-visualizations')
def interactive_visualizations():
    return render_template('interactive-visualizations.html')

@app.route('/intvisualization1')
def interactive_visualization1():
    return render_template('intvisualization1.html')

@app.route('/highlight-ratings')
def scatter_p():
    return render_template('highlight_ratings.html')

@app.route('/predict-score', methods=['GET', 'POST'])
def predict_score():
    prediction = None
    if request.method == 'POST':
        Parental_Education_Level = request.form.get('Parental_Education_Level')
        Teacher_Quality = request.form.get('Teacher_Quality')
        Access_to_Resources = request.form.get('Access_to_Resources')
        Tutoring_Sessions = request.form.get('Tutoring_Sessions')
        Parental_Involvement = request.form.get('Parental_Involvement')
        Family_Income = request.form.get('Family_Income')
        Motivation_Level = request.form.get('Motivation_Level')
        Extracurricular_Activities = request.form.get('Extracurricular_Activities')
        Peer_Influence = request.form.get('Peer_Influence')
        Internet_Access = request.form.get('Internet_Access')
        Learning_Disabilities = request.form.get('Learning_Disabilities')
        Distance_from_Home = request.form.get('Distance_from_Home')
        Physical_Activity = request.form.get('Physical_Activity')
        Previous_Scores = float(request.form.get('Previous_Scores'))
        Attendance = float(request.form.get('Attendance'))
        Hours_Studied = float(request.form.get('Hours_Studied'))

        # For each categorical variable, we create a one-hot vector
        # Initialize a dictionary to hold the one-hot values
        feature_values = {}

        # Helper function to set one-hot values
        def one_hot(prefix, categories, chosen):
            for cat in categories:
                key = f"{prefix}_{cat}"
                feature_values[key] = 1 if cat == chosen else 0

        # One-hot for Parental Education Level
        one_hot('Parental_Education_Level', ['College', 'High School', 'Postgraduate'], Parental_Education_Level)

        # One-hot for Teacher Quality
        one_hot('Teacher_Quality', ['High', 'Low', 'Medium'], Teacher_Quality)

        # One-hot for Access to Resources
        one_hot('Access_to_Resources', ['High', 'Low', 'Medium'], Access_to_Resources)

        # One-hot for Tutoring Sessions
        # Categories: 0 through 7
        one_hot('Tutoring_Sessions', [str(i) for i in range(8)], Tutoring_Sessions)

        # One-hot for Parental Involvement
        one_hot('Parental_Involvement', ['High', 'Low', 'Medium'], Parental_Involvement)

        # One-hot for Family Income
        one_hot('Family_Income', ['High', 'Low', 'Medium'], Family_Income)

        # One-hot for Motivation Level
        one_hot('Motivation_Level', ['High', 'Low', 'Medium'], Motivation_Level)

        # One-hot for Extracurricular Activities
        one_hot('Extracurricular_Activities', ['No', 'Yes'], Extracurricular_Activities)

        # One-hot for Peer Influence
        one_hot('Peer_Influence', ['Negative', 'Neutral', 'Positive'], Peer_Influence)

        # One-hot for Internet Access
        one_hot('Internet_Access', ['No', 'Yes'], Internet_Access)

        # One-hot for Learning Disabilities
        one_hot('Learning_Disabilities', ['No', 'Yes'], Learning_Disabilities)

        # One-hot for Distance from Home
        one_hot('Distance_from_Home', ['Far', 'Moderate', 'Near'], Distance_from_Home)

        # One-hot for Physical Activity
        one_hot('Physical_Activity', [str(i) for i in range(7)], Physical_Activity)

        # Now we have all one-hot features in `feature_values`.
        # Add the numeric features:
        feature_values['Previous_Scores'] = Previous_Scores
        feature_values['Attendance'] = Attendance
        feature_values['Hours_Studied'] = Hours_Studied

        # Create the input vector in the correct order:
        feature_order = [
            'Parental_Education_Level_College',
            'Parental_Education_Level_High School',
            'Parental_Education_Level_Postgraduate',
            'Teacher_Quality_High',
            'Teacher_Quality_Low',
            'Teacher_Quality_Medium',
            'Access_to_Resources_High',
            'Access_to_Resources_Low',
            'Access_to_Resources_Medium',
            'Tutoring_Sessions_0',
            'Tutoring_Sessions_1',
            'Tutoring_Sessions_2',
            'Tutoring_Sessions_3',
            'Tutoring_Sessions_4',
            'Tutoring_Sessions_5',
            'Tutoring_Sessions_6',
            'Tutoring_Sessions_7',
            'Parental_Involvement_High',
            'Parental_Involvement_Low',
            'Parental_Involvement_Medium',
            'Family_Income_High',
            'Family_Income_Low',
            'Family_Income_Medium',
            'Motivation_Level_High',
            'Motivation_Level_Low',
            'Motivation_Level_Medium',
            'Extracurricular_Activities_No',
            'Extracurricular_Activities_Yes',
            'Peer_Influence_Negative',
            'Peer_Influence_Neutral',
            'Peer_Influence_Positive',
            'Internet_Access_No',
            'Internet_Access_Yes',
            'Learning_Disabilities_No',
            'Learning_Disabilities_Yes',
            'Distance_from_Home_Far',
            'Distance_from_Home_Moderate',
            'Distance_from_Home_Near',
            'Physical_Activity_0',
            'Physical_Activity_1',
            'Physical_Activity_2',
            'Physical_Activity_3',
            'Physical_Activity_4',
            'Physical_Activity_5',
            'Physical_Activity_6',
            'Previous_Scores',
            'Attendance',
            'Hours_Studied'
        ]

        # Build the feature vector
        X = np.array([feature_values[feat] for feat in feature_order]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(X)

        return render_template('predict-score.html', prediction=prediction)
    return render_template('predict-score.html', prediction=prediction)
    
if __name__ == "__main__":
    app.run(debug=True)