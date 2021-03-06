"""
Handles file management tasks like file i/o and generating results.html document
"""


# Creates text file
def create_text_file():
    f = open("results.html", 'w+')  # opens test-file in write mode, returns file object
    return f


# Formats Author object data and prints it into results.html file
def add_prof_data_to_text_file(text_file, final_prof_info):
    if final_prof_info.name:
        text_file.write("<h1>Name: {0}</h1>\n".format(final_prof_info.name.strip()))

    if final_prof_info.portrait_url:
        text_file.write("<img src='{0}'>\n".format(final_prof_info.portrait_url))
    else:
        text_file.write("<h2>No Portrait Included</h2>\n")

    if final_prof_info.affiliation:
        text_file.write("<h2>Affiliation: {0}</h2>\n".format(final_prof_info.affiliation.strip()))
    else:
        text_file.write("<h2>Affiliation: None Given</h2>\n")

    if final_prof_info.research_interests:
        text_file.write("<h3>Primary Research Interest: {0}</h3>\n".format(final_prof_info.research_interests.strip()))
    else:
        text_file.write("<h3>Primary Research Interest: None Given</h3>\n")

    if final_prof_info.bio:
        text_file.write("<p><em>Biography</em>:\n{0}</p>\n".format(final_prof_info.bio.strip()))
    else:
        text_file.write("<p><em>Biography</em>:\n None Given</p>\n")
    text_file.write("\n")


# Formats Work object data and prints it into results.html file
def add_work_data_to_text_file(text_file, final_work_list):
    count = 0
    print("FINAL WORK LIST  is {0}".format(len(final_work_list)))
    for work in final_work_list:
        if count < 10:
            text_file.write("<h3>Title: {0}</h3>\n".format(work.title))
            text_file.write("<h4>Abstract:</h4><p>{0}</p>\n".format(work.abstract))
            text_file.write("<a href='{0}'>Download</a></p>\n".format(work.download_url))
            text_file.write("\n")
            count += 1
