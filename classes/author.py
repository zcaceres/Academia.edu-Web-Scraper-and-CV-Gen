"""
Class for organizing author (professor/research) info
"""

class Author(object):
    def __init__(self, name, affiliation, research_interests, portrait_url, bio):
        self.name = name
        self.affiliation = affiliation
        self.research_interests = research_interests
        self.portrait_url = portrait_url
        self.bio = bio



