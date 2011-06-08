<%inherit file="base.mk"/>

<%block name="page_title">Welcome</%block>

<%block name="page_content">
%for entry in entries:
	<h2>${entry['title'] | h,trim,unicode }</h2>
	<p>Posted by ${entry['username'] | h} on ${entry['datetime'].strftime("%A, %d %B %Y at %I:%M %p")}</p>
	<p>${entry['content'] | h,trim,unicode }</p>
	<p>Tags:${",".join(entry['tags'])}</p>
%endfor
</%block>
