import json

with open("data.json") as f:
	all_moocs = json.load(f)

all_html = ""
for section in all_moocs:
	if section["section"].lower() == "programs":
		class_name = section["section"].lower()
	else:
		class_name = "year_" + section["section"].lower()
	all_html += '''
		<!-- This is where the section for ''' + section["section"].lower() + ''' begins -->
		<section class="''' + class_name + '''">
			<div class="year">
				<h1>''' + section["section"] + '''</h1>
			</div>'''
	for mooc in section["moocs"]:
		all_html += '''
			<div class="mooc">
				<h2>''' + mooc["name"] + '''</h2>
				<a href="''' + mooc["link"] + '''" target="_blank"><img src="''' + mooc["image"] + '''"></a>
				<p>
					''' + mooc["text"] + '''
				</p>
			</div>'''
	all_html += '''
		</section>'''

print all_html


raw_json_mooc_structure = '''
			{
				"name" : "",
				"image" : "certificates/.jpg",
				"link" : "certificates_big/.pdf",
				"text" : "",
				"platform" : "",
				"institution" : "",
				"date" : {
					"start" : "",
					"end" : ""
				}
			}
'''
# could query the Coursera API for course start dates! https://tech.coursera.org/app-platform/catalog/