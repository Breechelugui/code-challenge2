# Remove: from article import Article
# Remove: from author import Author

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be 2-16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be 2-16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        from article import Article
        return [a for a in Article.all_articles if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        return [a.title for a in arts] if arts else None

    def contributing_authors(self):
        authors = [a.author for a in self.articles()]
        counts = {}
        for author in authors:
            counts[author] = counts.get(author, 0) + 1
        result = [author for author, count in counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda m: len(m.articles()))
