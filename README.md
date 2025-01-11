# IPL-Winning-Predictor


IPL Win Predictor Web App

The IPL Win Predictor is a web application that predicts the likely winner of an IPL match based on factors such as the city, overs left, and wickets remaining. This interactive app uses machine learning algorithms, along with the power of Python libraries like Streamlit, NumPy, Pandas, and Matplotlib, to make predictions and visualize match data.

---

Features

- **Input Parameters**:
- - Teams (batting and bowling)
  - City of the match
  - Overs left in the match
  - Wickets remaining
  - 
- Prediction Output:
  - Predicts the winning team based on the provided parameters

---

Technologies Used

- Streamlit: For creating the web interface and making the app interactive.
- NumPy: For numerical operations and handling match data.
- Pandas: For data manipulation and analysis.
- Matplotlib: For data visualization, including graphs and plots for match statistics.

---


Steps

1. Clone the Repository:
   Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/your-username/ipl-win-predictor.git
   ```

2. Navigate to the Project Directory:
   Go to the directory where the project was cloned:
   ```bash
   cd ipl-win-predictor
   ```

3. Install Dependencies:
   If you don't already have the required libraries installed, you can install them using `pip`:
   ```bash
   pip install streamlit numpy pandas matplotlib
   ```

4. Run the Streamlit App:
   Start the Streamlit app using the following command:
   ```bash
   streamlit run app.py
   ```
   Replace `app.py` with the name of your main Python file if it's different.

5. Access the Web App:
   After running the above command, Streamlit will automatically start the app and provide a local URL (usually `http://localhost:8501`). Open your browser and go to the URL to start using the app.

---

Usage

1. Enter the city, overs left, and wickets remaining on the input form.
2. Click on the "Predict Probability" button to get the predicted winner of the match.
3. View the prediction result and explore the data visualizations that show the trends.

---
