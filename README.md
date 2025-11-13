📰 Magazine Articles Management System
A simple Python-based object-oriented program that models the relationships between Authors, Articles, and Magazines.
This project is part of the Moringa Phase 3 Code Challenge.

🧩 Project Overview
This system simulates how authors write articles for different magazines. It uses three main classes:


Author – represents a writer who can publish articles in magazines.


Magazine – represents a publication that contains multiple articles.


Article – represents a single article written by an author and published in a magazine.


Each class contains relationships and helper methods that allow you to easily:


Retrieve all articles written by an author


Get all magazines an author contributes to


View contributors to a magazine


Identify top publishers, and more!



🏗️ Project Structure
code-challenge/
├── lib/
│   ├── author.py
│   ├── article.py
│   ├── magazine.py
│   ├── debug.py
│
├── Pipfile
├── Pipfile.lock
└── README.md


⚙️ Setup Instructions


Clone the repository (if not already):
git clone <your-repo-url>
cd code-challenge



Install dependencies with Pipenv:
pipenv install



Activate the virtual environment:
pipenv shell



Navigate to the lib folder:
cd lib



Run the debug/test script:
python debug.py




🧠 Class Relationships
Author


Attributes: name


Methods:


articles() → list of Article instances by this author


magazines() → list of Magazines the author has written for


add_article(magazine, title) → creates a new Article


topic_areas() → unique list of magazine categories




Magazine


Attributes: name, category


Methods:


articles() → list of all Articles in this magazine


contributors() → unique list of Authors who’ve written for this magazine


article_titles() → list of article titles


contributing_authors() → authors who’ve written > 2 articles


top_publisher() → class method that returns the magazine with the most articles




Article


Attributes: title, author, magazine


Relationships:


belongs to both an Author and a Magazine





💡 Example Usage
from author import Author
from magazine import Magazine
from article import Article

# Create authors
alice = Author("Alice")
bob = Author("Bob")

# Create magazines
tech_today = Magazine("TechToday", "Technology")
health_daily = Magazine("HealthDaily", "Health")

# Create articles
alice.add_article(tech_today, "AI in 2025")
alice.add_article(health_daily, "Healthy Eating")
bob.add_article(tech_today, "Quantum Computing")

# Check data
print(alice.articles())        # Alice's articles
print(tech_today.contributors())  # Authors contributing to TechToday
print(tech_today.article_titles())  # Titles published in TechToday


🧪 Testing
You can verify functionality by running:
pytest

Or, if you only want to manually test relationships:
python lib/debug.py


🚀 Key Concepts Covered


Object-Oriented Programming (OOP)


Class relationships (One-to-Many and Many-to-Many)


Encapsulation using getters and setters


Data validation and error handling


Circular import management in Python



📚 Technologies Used


Python 3.8+


Pipenv for virtual environment and dependency management


Pytest (optional) for testing



👩🏽‍💻 Author
Brenda Chelugui

