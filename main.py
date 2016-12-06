import requests
from bs4 import BeautifulSoup

from classes import author, work
from utility import file_management, parse_paths, pdf_generation

"""
            ACADEMIA.EDU WEB SCRAPER and AUTOMATIC (Basic) PDF CV GENERATOR
                    A PYTHON-A-THON 2016 PROJECT by ZACHARY CACERES
                                www.python-a-thon.com
"""

def get_user():
    url = input("Please paste the URL of the Academia.edu page: ")
    return url

def query_website(username) :
    r = requests.get('{0}'.format(url))
    return r.text

def convert_html_to_soup(site_text):
    html = site_text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_prof_data(soup):
    name = None
    affiliation = None
    interests = None
    portrait_url = None
    bio = None

    # Get Professor Name
    prof_name = soup.select(parse_paths.PROF_NAME_PATH)
    for p in prof_name:
        name = p.text

    #Get Affiliations
    affiliations = soup.select(parse_paths.PROF_AFFILIATION_PATH)
    for aff in affiliations:
        affiliation = aff.text

    #Get Research Interests
    research_interests = soup.select(parse_paths.PROF_RESEARCH_INTERESTS_PATH)
    for interest in research_interests:
        interests = interest.text

    # Get Url to Portrait
    portrait = soup.select(parse_paths.PROF_PORTRAIT_PATH)
    for p in portrait:
        if p.has_attr('src'):
            portrait_url = p['src']
            print("PORTRAIT: {0}".format(portrait_url))

    # Get Biography
    biography = soup.select(parse_paths.PROF_BIO_PATH)
    for b in biography:
        bio = b.text

    # Makes a new Author object
    make_author(name, affiliation, interests, portrait_url, bio)
    return name


def extract_work_data(soup):
    # Lists to assemble top ten works on Academia.edu
    total_titles = []
    total_abstracts = []
    total_download_urls = []

    # Get Total Works
    total_works = soup.select(parse_paths.WORKS_PATH)
    print ("–––––– AUTHOR HAS {0} TOTAL WORKS ––––––––".format(len(total_works)))
    for work in total_works:

        # Get Titles
        title = work.select(parse_paths.TITLES_PATH)
        for t in title: # Number of titles determines number of works on the author's page
            total_titles.append(t.text)

            # Get Abstracts
            abstract = work.select(parse_paths.ABSTRACT_UNTRUNCATED_PATH)
            """
            Looks through list of elements at work abstracts and download_urls path in
            parse_paths module. If element is found, append text to total_abstracts and
            total_download_urls list if not, append None type so that lists are created with
            proper number of elements.
            """
            if len(abstract) == 0:
                total_abstracts.append(None)
            else:
                for a in abstract:
                    total_abstracts.append(a.text)

            # Get Download URLS
            download_urls = work.select(parse_paths.DOWNLOAD_URL_PATH)
            if len(download_urls) == 0:
                total_download_urls.append(None)
            else:
                for link in download_urls:
                    if link.has_attr('href'):
                        total_download_urls.append(link['href'])
                    else:
                        total_download_urls.append(None)
                        print("WARNING: Link was found but has NO HREF!")
    print("––––– AUTHOR OVERVIEW –––––––")
    print("Total Titles is: {0}".format(len(total_titles)))
    print("Total Abstracts length is: {0}".format(len(total_abstracts)))
    print("Total Download URLs is: {0}".format(len(total_download_urls)))
    generate_work_lists(total_titles, total_abstracts, total_download_urls)


def generate_work_lists (total_titles, total_abstracts, total_download_urls):
    counter = 0
    for t in total_titles:
        print ("Making work at index {0} with title {1}".format(counter, t))
        temp_abs = total_abstracts[counter]
        temp_download = total_download_urls[counter]
        make_work(t, temp_abs, temp_download)
        counter += 1


def make_author(name, affiliation, interests, portrait_url, bio):
    prof = author.Author(name, affiliation, interests, portrait_url, bio)  # Construct new author object
    file_management.add_prof_data_to_text_file(html_results_file, prof)


def make_work(title, abstract, download_url):
    new_work.append(work.Work(title, abstract, download_url))
    print("NEW WORK is {0}".format(len(new_work)))




if __name__ == '__main__':
    new_work = []
    html_results_file = None
    html_results_file = file_management.create_text_file()
    url = get_user()
    site_text = query_website(url)
    soup = convert_html_to_soup(site_text)
    prof_name = extract_prof_data(soup)
    extract_work_data(soup)
    file_management.add_work_data_to_text_file(html_results_file, new_work)
    html_results_file.close()  # File must be closed for PDFKit to print
    pdf_generation.generate_pdf(prof_name)
