from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
db = client["octofit_tracker"]

# Sample data for users
users = [
    {"name": "Alice", "age": 16, "email": "alice@example.com", "team": "Team A"},
    {"name": "Bob", "age": 17, "email": "bob@example.com", "team": "Team B"},
    {"name": "Charlie", "age": 15, "email": "charlie@example.com", "team": "Team A"}
]

# Sample data for activities
activities = [
    {"user": "Alice", "type": "Running", "duration": 30, "calories_burned": 200},
    {"user": "Bob", "type": "Cycling", "duration": 45, "calories_burned": 300},
    {"user": "Charlie", "type": "Walking", "duration": 60, "calories_burned": 150}
]

# Sample data for teams
teams = [
    {"name": "Team A", "points": 100},
    {"name": "Team B", "points": 80}
]

# Insert sample data into the database
db.users.insert_many(users)
db.activities.insert_many(activities)
db.teams.insert_many(teams)

print("Sample data has been added to the database.")
