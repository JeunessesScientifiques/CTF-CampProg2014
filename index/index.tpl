<%
from parse import *
import csv

%>
<html>
	<header>

		<title>{{title}}</title>

		<style>{{cssfile}}</style>

	</header>
	<body link="#FFFFFF" vlink="FF0000">
		<H1>{{title}}</H1>
		<H3><kbd>Equipe {{name}}</kbd></H3>
		
		% challenges = []
		% #print(title)
		% with open('challenges.csv', 'r') as f:
    	% reader = csv.reader(f)
    	<kbd>
    	<table id="scores">
    		% for grp in groups:
    			<tr>
    				<td>{{!grp.name}} : &nbsp; </td><td>{{!grp.score}}</td>
    			</tr>
    		% end
   		</table>
   		</kbd>
   		<hr/>
    	<table>
    	% for row in reader:
    	%	id 		= row[0]
    	%	title 	= row[1]
    	%	lien 	= row[2]
    	%	secret 	= row[3]
    	%	max_point	= row[4]
    	%	point = ""
    	% #mission = mission_ok.split("\n")
    	% #print("'"+mission_ok+"'")
    		<tr>
    			<form action="/Challenge/{{!id}}" method="post" >
    			<input type="hidden" name="name" value="{{name}}"/>
    			<input type="hidden" name="id" value="{{!id}}"/>
    			<td>Mission {{!id}} :</td><td><a underline="none" href={{!lien}}>{{!title}}</a>&nbsp;&nbsp;&nbsp;&nbsp;</td><td>secret : </td><td><input name="secret"/></td><td><input type="submit"/></td><td><!--{{!point}}/-->{{!max_point}} points</td>
    			</form>
    		</tr>
        % end
		</table>
	</body>
</html>