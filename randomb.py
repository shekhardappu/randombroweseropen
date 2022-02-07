import random
import time
import webbrowser
while True:
	sites=random.choice(['youtue.com','instagram.com'])
	visit='https://{}'.format(sites)
	webbrowser.open(visit)
	time.sleep(2)