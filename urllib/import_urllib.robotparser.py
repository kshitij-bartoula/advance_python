import urllib.robotparser
robot = urllib.robotparser.RobotFileParser()
print (robot.set_url('http://arstechnica.com/robots.txt'))
#None

print (robot.read())
#None

print (robot.can_fetch('*', 'http://arstechnica.com/'))
#True

print (robot.can_fetch('*', 'http://arstechnica.com/cgi-bin/'))
#False
#Here we import the robot parser class and create an instance of it. Then we pass it a URL that specifies where the website’s 
# robots.txt file resides. Next we tell our parser to read the file. Now that that’s done, we give it a couple of different URLs to 
# find out which ones we can crawl and which ones we can’t. We quickly see that we can access the main site, but not the cgi-bin.