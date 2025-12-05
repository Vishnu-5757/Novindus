# ✈️ Django Machine Test: Flight Route System

This project is a Django web application that solves the three core graph/data structure questions outlined in the technical test, using an Airport and FlightRoute database model.

## 🔗 Repository URL
`https://github.com/Vishnu-5757/Novindus`

## ⚙️ Setup and Installation

Follow these steps to set up and run the project locally:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Vishnu-5757/Novindus.git](https://github.com/Vishnu-5757/Novindus.git)
    cd Novindus/airport_system
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows PowerShell
    # source venv/bin/activate  # On Linux/macOS/Git Bash
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Populate Initial Data:**
    The network diagram (Airport A -> B, A -> C) is loaded using this script.
    ```bash
    python routes/populate_data.py
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    Access the dashboard at `http://127.0.0.1:8000/`.

## ✅ Solution Summary

| Question | Implementation | Weight |
| :--- | :--- | :--- |
| **Q1: Find Nth Node** | Implemented a directional traversal in `routes/utils.py` to recursively follow the 'LEFT' or 'RIGHT' route N steps from a start node. | Graph Traversal |
| **Q2: Longest Duration** | Solved using a Django ORM query with optimization (`.order_by('-duration_mins').first()`) in `routes/utils.py`. | Database Optimization |
| **Q3: Shortest Path** | Implemented **Dijkstra's Algorithm** from scratch in `routes/utils.py` to find the path with the minimum total `duration_mins` between two selected airports. | Pathfinding Algorithm |

***

## 3. Commit and Push the New Files

After creating `requirements.txt` and `README.md`, you must commit and push them to your repository to complete the submission.

1.  **Stage the new files:**
    ```bash
    git add .
    ```

2.  **Commit the files:**
    ```bash
    git commit -m "Added README.md and requirements.txt for setup instructions"
    ```

3.  **Push the changes:**
    ```bash
    git push
    ```

This final push will update your GitHub repository, and your project will be fully documented and ready for review.