# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:57:56 2019

@author: ulb
"""

authors = ["Darwin", "Lovelace", "Hawkin", "Noether"]

output_fh = open("list.html", "w")

scaffold_start ="""<!DOCTYPE html>
<html>
<head>
<title>Titel dieser wunderbaren Seite</title>
</head>
<body>

<h1>Eine grandiose Überschrift</h1>

<p>Ein nicht weniger toller Abschnitt.</p>

<ul>

"""

output_fh.write(scaffold_start)

scaffold_middle =""

for authors in authors:
    scaffold_middle = scaffold_middle + "<li>" + authors + "</li>\n"
    
    
    
output_fh.write(scaffold_middle)
    
#<li>Erstes Element</li>
#<li>Zweites Element</li>

scaffold_end =  """  

</ul>

</body>

</html>"""

output_fh.write(scaffold_end)


output_fh.close()