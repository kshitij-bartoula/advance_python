from urllib.parse import urlparse
result = urlparse('https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa')
print (result)
#ParseResult(scheme='https', netloc='duckduckgo.com', path='/', params='', query='q=python+stubbing&t=canonical&ia=qa', fragment='')

print (result.netloc)
#'duckduckgo.com'

print (result.geturl())
#'https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa'

print (result.port)
#None

#The urllib.parse library is your standard interface for breaking up URL strings and combining them back together
#you can get the port information (None in this case), the network location, path and much more.