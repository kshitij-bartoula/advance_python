import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'q': 'Python'})
data
#'q=Python'

url = 'http://duckduckgo.com/html/'
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)
with open('results.html', 'wb') as f:
    f.write(response.read())

# This is pretty straightforward. Basically we want to submit a query to duckduckgo ourselves using Python instead of a browser. 
# To do that, we need to construct our query string using urlencode. Then we put that together to create a fully qualified URL and
#  use urllib.request to submit the form. We then grab the result and save it to disk.