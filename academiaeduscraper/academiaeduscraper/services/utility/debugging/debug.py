"""
Methods used for debugging that shouldn't clutter up primary classes!
"""

def print_prof_data(prof):
    print ("–––––– New Professor ––––––")
    print ("Name: {0}".format(prof.name))
    print ("Affiliation: {0}".format(prof.affiliation))
    print ("Research Interest: {0}".format(prof.research_interests))
    print ("Portrait URL: {0}".format(prof.portrait_url))
    print ("Biography: {0}".format(prof.bio))


def print_work_data(work):
    print("–––––– New Work ––––––")
    print("Title: {0}".format(work.title))
    print("Abstract: {0}".format(work.abstract))
    print("Download URL: {0}".format(work.download_url))