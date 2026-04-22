# 🎮 Offline Game Centre

## 📌 Overview

The **Offline Game Centre** is a locally hosted gaming platform that allows users to play multiple classic games without an internet connection. It integrates a Flask-based interface with locally executed Python games, while storing user scores persistently using SQLite.

This project was built to simulate a mini arcade system that works entirely offline, combining backend development, game logic, and database management into one cohesive system.

---

## 🚀 Features

### 🎯 Core Features

* Multiple playable games:

  * Snake (Easy & Hard modes)
  * Tic-Tac-Toe
  * Tic-Tac-Toe (Human vs AI)
  * Pong (Two Player)
* Username-based session system
* Persistent high score tracking
* Fully offline functionality
* Menu-based navigation using Flask + HTML

### 💾 Data Persistence

* Local **SQLite3 database** (`scores` file)
* Stores usernames and high scores
* Scores automatically saved and retrieved

---

## 🏗️ Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML (templates folder)
* Basic CSS (static folder)

### Game Development

* Pygame (Snake, Pong)
* Tkinter (UI elements for some interactions)

### Database

* SQLite3

---

## 🧩 Project Structure

```
Offline Game Centre
│
├── static/                     # CSS / assets
├── templates/                 # HTML pages
│   ├── index.html
│   ├── about.html
│   ├── pong_menu.html
│   ├── pong_loading.html
│   ├── snake_menu.html
│   ├── snake_loading.html
│   ├── snake_hard_loading.html
│   ├── tic_tac_toe_menu.html
│   ├── tic_tac_toe_loading.html
│   ├── tic_tac_toe_ai_loading.html
│
├── offlinegamecentre.py       # Main Flask application
├── pong_two_player_game.py    # Pong game logic
├── snake_easy_mode.py         # Snake (easy mode)
├── snake_hard_mode.py         # Snake (hard mode)
├── snake_score_database.py    # Snake score handling
├── tic_tac_toe.py             # Basic Tic-Tac-Toe
├── tic_tac_toe_human_vs_AI.py # Tic-Tac-Toe with AI
├── scores                     # SQLite database file
│
├── build/                     # Build artifacts
├── dist/                      # Executable distribution
├── offlinegamecentre.spec     # PyInstaller spec file
│
├── .git/
├── .idea/
├── __pycache__/
```

---

## ⚙️ Installation & Setup

### ✅ Option 1 (Recommended): Run the Packaged Application

No setup required.

1. Download the project
2. Navigate to the `dist/` folder
3. Run the executable:

   ```
   offlinegamecentre.exe
   ```
4. The application will launch and open in your browser

---

### 🛠️ Option 2 (Developer Mode)

Only needed if you want to run or modify the source code.

#### 1. Clone the Repository

```
git clone https://github.com/yourusername/offline-game-centre.git
cd offline-game-centre
```

#### 2. Create Virtual Environment (Optional)

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```
pip install flask pygame
```

#### 4. Run the Application

```
python offlinegamecentre.py
```

---

## 🎮 How It Works

1. Run `offlinegamecentre.py`
2. Open the local Flask server in your browser
3. Enter a username
4. Choose a game from the menu
5. Flask routes trigger the corresponding Python game file
6. Scores are saved into the `scores` SQLite database

---

## 🧠 Key Learning Outcomes

### 🔹 Full-Stack Integration

* Connected Flask routes to external Python game scripts
* Managed navigation between web UI and local applications

### 🔹 Game Development

* Implemented game loops in Pygame
* Built difficulty systems (Snake easy vs hard)
* Created basic AI for Tic-Tac-Toe

### 🔹 Database Management

* Integrated SQLite with Python
* Stored and retrieved user scores

### 🔹 Software Architecture

* Organized project into frontend, backend, and game modules
* Managed separation of concerns across files

---

## ⚠️ Challenges Faced

### 🔸 Launching Games from Flask

Triggering external Python scripts from Flask routes required careful handling (e.g. subprocess usage).

### 🔸 Score Synchronisation

Ensuring all games correctly saved to the same `scores` database.

### 🔸 Restart Logic

Handling restarts without breaking the game loop or duplicating processes.

### 🔸 File Organisation

Keeping multiple game scripts and templates structured and maintainable.

### 🔸 UI Flow

Ensuring smooth transitions between menus, loading screens, and games.

---

## 🔮 Future Improvements

* Add global leaderboard system
* Improve UI design (modern styling)
* Add sound effects and animations
* Refactor into a more scalable architecture
* Package games more cleanly instead of separate scripts

---

## 📷 Screenshots

*Add screenshots here (menus, gameplay, etc.)*

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

* Classic arcade games inspiration
* Built as part of a personal software development journey

---

## 📬 Contact

Add your GitHub or LinkedIn here

---

**Author:** Your Name
