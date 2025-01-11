import streamlit as st
import pandas as pd
import pickle
import numpy as np

teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 
         'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# Load the trained pipeline (assuming 'pipe.pkl' contains the pre-trained model)
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL Win Predictor')

# Create layout for user inputs
column1, column2 = st.columns(2)

with column1:
    batting_team = st.selectbox('Select the batting team:', sorted(teams))

with column2:
    bowling_team = st.selectbox('Select the bowling team:', sorted(teams))

select_city = st.selectbox('Select host City:', sorted(cities))
target = st.number_input('Target', min_value=1)

# Create layout for score, over, and wickets left
column3, column4, column5 = st.columns(3)

with column3:
    score = st.number_input('Score', min_value=0)

with column4:
    over = st.number_input('Overs completed', min_value=0)

with column5:
    wicket_left = st.number_input('Wickets left', min_value=0, max_value=10)

# Display prediction when the button is clicked
if st.button('Predict Probability'):
    # Check if the selected teams are the same
    if batting_team == bowling_team:
        st.error("You cannot select the same team for both batting and bowling. Please select different teams.")
    else:
        # Calculate remaining runs, balls, and wickets
        runs_left = target - score
        balls_left = 120 - (over * 6)  # 120 balls in total
        wickets = 10 - wicket_left
        crr = score / over if over != 0 else 0  # Handle divide by zero error
        rrr = (runs_left * 6) / balls_left if balls_left != 0 else 0  # Handle divide by zero error
        
        # Preparign input data for the model
        input_data = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [select_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })
        
        # Get prediction probabilities
        #  predict_proba returns a 2d array[][] in a sorted array
        result = pipe.predict_proba(input_data) 
        loss = result[0][0]
        win = result[0][1]       
       
        # Determine the winning and losing team based on the probability
        st.write(f"{batting_team} - {round(win * 100, 2)}%")
        st.write(f"{bowling_team} - {round(loss * 100, 2)}%")
        
       