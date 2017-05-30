import json
import urllib, urllib2
import sys
from keys import BING_API_KEY
from py_ms_cognitive import PyMsCognitiveWebSearch

def run_query(search_terms):
    try:
        print "BING_API_KEY: ", (BING_API_KEY)
        search_service = PyMsCognitiveWebSearch(BING_API_KEY, search_terms)
        response = search_service.search(limit=10, format='json')
        print "response[0].__dict__: %s \n" % (response[0].__dict__)

        results = []
        for item in response:
            results.append({
                'title': item.title,
                'summary': item.snippet,
                'link': item.url, })
        print "results: %s \n" % (results)

    except :
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    return results

def run_query_debug(search_terms):
    try:
        print "BING_API_KEY: ", (BING_API_KEY)
        search_service = PyMsCognitiveWebSearch(BING_API_KEY, search_terms)
        result = search_service.search(limit=10, format='json')
        print "result[0].snippet: %s \n" % (result[0].snippet)
        print "result[0].__dict__.keys(): %s \n" % (result[0].__dict__.keys())
        print "result[0].__dict__: %s \n" % (result[0].__dict__)
        print "result[3]: %s \n" % result[3]
        print "result[1].__dict__[\"name\"]: %s \n" % result[1].__dict__["name"]
        print "result[2].display_url: %s \n" % result[2].display_url
        print "result: %s \n" % result

        result_list = []
        for item in result:
            result_list.append({
                'title': item.title,
                'summary': item.snippet,
                'link': item.url, })
        print "result_list: %s \n" % (result_list)

    except :
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    return result_list


def run_query2(search_terms):

    # Specify the base
    root_url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    source = 'Web'

    # Specify how many results we wish to be returned per page.
    # Offset specifies where in the results list to start from.
    # With results_per_page = 10 and offset = 11, this would start from page 2.
    results_per_page = 10
    offset = 0

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''


    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, BING_API_KEY)
    print "Bing API Key: ", BING_API_KEY

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to Bing's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)

        # Loop through each page returned, populating out results list.
        print "json_response: ", json_response
        for result in json_response['d']['results']:
            results.append({
            'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description']})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the Bing API: ", e

    # Return the list of results to the calling function.
    return results


def test_search():
    search_term = 'benjamin frankin'
    run_query(search_term)
    return


if __name__ == '__main__':
    test_search()
