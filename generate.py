import json

raw_data = open("data.json", "r")
data = raw_data.read()

print data[]

mooc = '''
			<div class="mooc">
				<h2>{{title}}</h2>
				<a href={{link}}><img src={{image}}></a>
				<p>
					{{text}}
				</p>
			</div>'''