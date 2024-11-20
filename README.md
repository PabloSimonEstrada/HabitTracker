# Pixela API Gym Tracker

Pixela API Gym Tracker is a Python-based application designed to help users track and visualize their daily gym attendance. By interacting with the Pixela API, the application allows users to log their gym visits, update entries, and monitor their progress through a personalized graph.

## Features

- **Daily Gym Tracking**: Log gym attendance with a simple input interface.
- **Visualization**: Automatically updates a graph on Pixela to visualize attendance habits.
- **CRUD Operations**:
  - **Create**: Add new gym attendance records.
  - **Read**: View recorded data through the Pixela dashboard.
  - **Update**: Modify existing entries as needed.
  - **Delete**: Remove incorrect or unnecessary entries.

## Technologies Used

- **Programming Language**: Python
- **API Integration**: Pixela API
- **Libraries**:
  - `requests` for HTTP requests to the Pixela API.
  - `datetime` for managing dates and times.

## Setup and Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/PabloSimonEstrada/HabitTracker.git
   cd HabitTracker
   ```

2. **Install Dependencies**  
   Make sure you have Python installed on your system. Install the required libraries by running:  
   ```bash
   pip install requests
   ```

3. **Set Up Pixela Account**  
   - Create an account on [Pixela](https://pixe.la/).
   - Generate a token and username, which will be used to authenticate API requests.

4. **Configure the Script**  
   - Open the script file and update the following variables with your Pixela credentials:
     ```python
     PIXELA_USERNAME = "your_username"
     PIXELA_TOKEN = "your_token"
     ```

5. **Run the Application**  
   Execute the script:
   ```bash
   python pixela_tracker.py
   ```

## Usage

1. **Log Attendance**  
   - Run the script to input your gym attendance for the day.  
   - The script sends the data to your Pixela graph, updating it in real time.

2. **Update Entries**  
   - Use the script's update function to modify specific dates.

3. **Delete Entries**  
   - Remove data for incorrect entries by specifying the date.

## Example Output

When you log your attendance, the script will display:
```bash
Gym attendance logged successfully for 2024-11-20.
```

## Future Enhancements

- Add a GUI for easier interaction.
- Provide weekly and monthly summaries of gym attendance.
- Include notifications for missed days.

## Contribution

Feel free to fork the repository, open issues, or submit pull requests. Contributions are always welcome!
