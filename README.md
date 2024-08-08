Project-Link: [https://dilesh-bisen-recommend.streamlit.app](https://dilesh-bisen-recommend.streamlit.app)

# <b>Movie Recommender System</b>
Welcome to the Movie Recommender System! This project is a web-based application that helps users discover new movies based on their preferences. Built using Streamlit and Python, this app fetches movie recommendations and displays them with posters, ensuring an engaging user experience.

## <b>Features</b>
- Movie Selection: Choose a movie from the sidebar to get personalized recommendations.
- Movie Recommendations: Receive a list of recommended movies based on the selected movie.
- Movie Posters: View movie posters for the recommended titles.
- Responsive Design: The interface is designed to be user-friendly and visually appealing.

## <b>Technologies Used</b>
- Python: The programming language used for the backend logic.
- Pandas: For data manipulation and analysis.
- Requests: For making HTTP requests to fetch movie data.
- Streamlit: For creating the interactive web application.
- Pickle: For loading pre-saved models and datasets.

## <b>Setup and Installation</b>
### Prerequisites
- Python 3.6 or higher
- Virtual environment (recommended)
### Installation Steps
1. Clone the Repository:
git clone [https://github.com/Dilesh-Bisen/movie-recommender-system.git](https://github.com/Dilesh-Bisen/recommender-system.github.io.git)
cd movie-recommender-system
2. Create and Activate Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Required Packages
pip install -r requirements.txt
4. Add API Key
Make sure to replace the placeholder API key in fetch_poster function with your own API key from 'The Movie Database API'.
5. Run the Application
streamlit run app.py
This will start the Streamlit server and open the application in your default web browser.

## <b>Usage</b>
- Open the application in your web browser.
- Use the sidebar to select a movie.
- Click the "Recommend" button to fetch and display recommendations.
- Browse through the recommended movies and their posters.

## <b>Files and Directories</b>
- app.py: Main Streamlit application file.
- movies.pkl: Pickled movie dataset.
- similarity.pkl: Pickled similarity matrix.
- requirements.txt: List of Python dependencies.

## <b>Contributing<b>
Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.

## <b>Contact<b>
For any questions or feedback, please reach out to [Dilesh-Bisen](https://github.com/Dilesh-Bisen) at [2dileshbisen@gmail.com](2dileshbisen@gmail.com).

