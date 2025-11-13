from author import Author
from magazine import Magazine
from article import Article

# Create authors
a1 = Author("Alice")
a2 = Author("Bob")

# Create magazines
m1 = Magazine("TechToday", "Technology")
m2 = Magazine("HealthDaily", "Health")

# Create articles
art1 = a1.add_article(m1, "AI in 2025")
art2 = a1.add_article(m2, "Healthy Eating")
art3 = a2.add_article(m1, "Quantum Computing")
art4 = a1.add_article(m1, "Future of Robotics")
art5 = a2.add_article(m1, "Cybersecurity Trends")
art6 = a1.add_article(m1, "Blockchain Revolution")

# Testing relationships
print("Alice Articles:", [a.title for a in a1.articles()])
print("Alice Magazines:", [m.name for m in a1.magazines()])
print("TechToday Articles:", [a.title for a in m1.articles()])
print("TechToday Contributors:", [a.name for a in m1.contributors()])
print("Alice Topic Areas:", a1.topic_areas())
print("TechToday Article Titles:", m1.article_titles())
print("TechToday Contributing Authors:", [a.name for a in m1.contributing_authors()])
print("Top Publisher:", Magazine.top_publisher().name)
