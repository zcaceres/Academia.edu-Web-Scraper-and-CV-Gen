from pyramid.view import view_config
from .services import create_cv
from .services.utility.validation import validate_url
import os

@view_config(route_name='home', renderer='templates/home.pt', request_method="GET")
def home(request):
    # print("called my view!")
    return {"error": None, "cv_generated": None}


@view_config(route_name='home', renderer='templates/home.pt', request_method="POST")
def make_cv(request):
    url = request.POST.get('url')
    if url:
        error_check = validate_url(url)
        if error_check:
            print("Error Returned: {0}".format(error_check))
            return {"error": error_check, "cv_generated": None}
        else:
            print("Passed Validation")
            cv_generated = create_cv.process_input_to_request_pdf(url)
            # create file here with proper name to pass to user for D/Ling
            return {"error": None, "cv_generated": cv_generated}
    else:
        return {"error": "Please input a URL!", "cv_generated": None}
