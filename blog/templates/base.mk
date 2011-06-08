<!doctype html>
<!--[if lt IE 7 ]> <html lang="en" class="no-js ie6"> <![endif]--><!--[if IE 7 ]>    <html lang="en" class="no-js ie7"> <![endif]--><!--[if IE 8 ]>    <html lang="en" class="no-js ie8"> <![endif]--><!--[if IE 9 ]>    <html lang="en" class="no-js ie9"> <![endif]--><!--[if (gt IE 9)|!(IE)]><!--> <html lang="en" class="no-js"> <!--<![endif]--><head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	
	<title><%block name="page_title"/></title>
	<meta name="description" content="">
	<meta name="author" content="">
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<link rel="shortcut icon" href="${request.static_url('blog:static/favicon.ico')}">
	<link rel="apple-touch-icon" href="${request.static_url('blog:static/apple-touch-icon.png')}">
	<link rel="stylesheet" href="${request.static_url('blog:static/css/style.css')}">
	<link rel="stylesheet" media="handheld" href="${request.static_url('blog:static/css/handheld.css')}">
</head>
<body>
	<div id="container">
		<header id="header">
			<!-- <h1> Prudhvi&quot;s Blog </h1> -->
			<a href="${request.route_url("home")}" alt="Home">Home</a>
		</header>

		<div id="main" role="main">
		<%block name="page_content"/>
		</div>

		<footer>
			&copy; 2011 Prudhvi Krishna Surapaneni.
		</footer>
	</div>

	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js"></script>
	<script>!window.jQuery && document.write(unescape('%3Cscript src="${request.static_url('blog:static/js/libs/jquery-1.5.1.min.js')}"%3E%3C/script%3E'))</script>
	<script src="${request.static_url('blog:static/js/plugins.js')}"></script>
	<script src="${request.static_url('blog:static/js/script.js')}"></script>
	<!--[if lt IE 7 ]>
	<script src="${request.static_url('blog:static/js/libs/dd_belatedpng.js')}"></script>
	<script> DD_belatedPNG.fix('img, .png_bg');</script>
	<![endif]--></body>
</html>
