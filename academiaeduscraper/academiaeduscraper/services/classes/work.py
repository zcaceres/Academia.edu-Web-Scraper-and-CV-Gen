"""
Work Object for organizing books, papers, talks, etc.
"""

class Work(object):
    def __init__(self, title, abstract, download_url):
        self.title = title
        self.abstract = abstract
        self.download_url = download_url


