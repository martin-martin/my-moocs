import json
import os

raw_data = open("data.json", "r")
data = raw_data.read()

#print data[]

# this could automate typing (part of) the names; regex could do it all...
path_to_cert = os.path.relpath("certificates/")
# instead of "/text" just put the name of the file (and replace the rest as needed)
with open(path_to_cert + "/text" + ".txt") as f:
	for line in f:
		print line




print path_to_cert

mooc = '''
			<div class="mooc">
				<h2>{{title}}</h2>
				<a href={{link}}><img src={{image}}></a>
				<p>
					{{text}}
				</p>
			</div>'''