"""
Paths to Academia.edu Sections for BeautifulSoup Parsing
"""

# Professor/Author Info
PROF_NAME_PATH = ".InlineList-item"
PROF_AFFILIATION_PATH = ".Affiliation-text--affiliation"
PROF_RESEARCH_INTERESTS_PATH = ".Affiliation-text--researchInterests"
PROF_PORTRAIT_PATH = ".profile-avatar"
PROF_BIO_PATH = ".js-profile-about"

# Works Info
TITLES_PATH = ".js-work-strip-work-link.text-gray-darker"
WORKS_PATH = ".media-body"
TOP_LEVEL_WORKS_PATH =".media.work.js-work-strip"
DOWNLOAD_URL_PATH = ".work-download"

ABSTRACT_TRUNCATED_PATH = ".js-work-more-abstract-truncated" #currently unused
ABSTRACT_UNTRUNCATED_PATH = ".js-work-more-abstract-untruncated"