import os
import datetime
# Global variables

rootdir = '.'
episode_anchor = '<div class="anchor" id="axx"></div>'
episode_end = '</p>\n\n<!-- episode break -->\n\n'
series_year = {
	'1': '2005',
	'2': '2006',
	'3': '2007',
	'4': '2008',
	'4-5': '2008-2010',
	'5': '2010',
	'6': '2011',
	'7': '2012-2013',
    '8': '2014',
	'9': '2015'
}

hidden_menu = '<li id="xx"><a class="icon-toggle" href="#axx">EPISODE</a></li>\n'

side_menu = '<li><a href="#axx">EPISODE</a></li>\n'

HEADER = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="../images/favicon.ico">

    <title>Doctor Who Archives - (New) Series x</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
	<link href="css/dashboard.css" rel="stylesheet">
  </head>

  <body data-spy="scroll" data-target=".bs-docs-sidebar">
	<!-- begin the top fixed bar -->
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">		        
          <a class="navbar-brand" href="index.html">Doctor Who Archives</a>
          <button type="button" class="navbar-toggle icon-toggle">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
		</div>
				<div class="menu initiallyHidden">
          <ul class="nav">
            HIDDEN_MENU
          </ul>
		</div>

  	  </div><!--/.navbar-collapse -->
	
	<!-- Main jumbotron for the title section -->

	  <div class="jumbotron">
        <div class="container">
          <h1>Doctor Who Series x</h1>
         <p>Episodes from the series in xxxx</p> 
        </div>
      </div>
    </div> 
	<!-- end the top fixed bar-->
	
	<!-- Fixed Sidebar -->	
 <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar bs-docs-sidebar">
          <ul class="nav nav-sidebar">
            SIDEBAR
          </ul>
         </div>
      </div>
 </div>
 

 <!-- /container -->
 <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
    <div class="container-fluid">
'''

FOOTER = '''<!-- Footer -->
	<footer>
	<hr>
	<div class="row">
		<div class="col-xs-6 col-md-6"><p>&copy; Cazellie YEAR</p></div>
		<div class="col-xs-6 col-md-6" align="right"><p><a href="acknowledgements.html">Acknowledgements</a></p></div>
	</div>
	</footer>
 
	</div>
 </div>	
	
	
	
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="js/bootstrap.js"></script>
	<script src="js/docs.min.js"></script>
	<script src="js/menu.js"></script>

	<script>
	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

	ga('create', 'UA-55594701-1', 'auto');
	ga('send', 'pageview');
	</script>
	

  </body>
</html>
'''

# Traverses the series directories and creates webpage for each series
		
for dirName, subdirList, fileList in os.walk(rootdir):
	print 'Found directory: %s' % dirName
	
	# exclude the root directory as there are no series files
	
	if dirName == '.':
		continue
		
	series_filename = dirName + '.html'
	series_file = open('..\\' + series_filename,'w')
	series_file.truncate()
	print 'File created: ' + series_filename				
	
	series_number = dirName[4:].replace('.txt','').replace('0','')
	
	series_hidden_menu = ""
	series_side_menu = ""
	
	series_output = HEADER.replace('Series x', 'Series ' + series_number).replace('series in xxxx', 'series in ' + series_year[series_number])
	
	for file in fileList:
		file_path = os.path.join(dirName, file)
		current_file = open(file_path)
		print 'Opening series file: ' + file_path

		title = current_file.readline()
		current_file.seek(0, 0)
		
		series_hidden_menu += hidden_menu.replace('xx', file).replace('.txt', '').replace('EPISODE', title.strip())
		series_side_menu += side_menu.replace('xx', file).replace('.txt', '').replace('EPISODE', title.strip())		
		
		local_episode_anchor = episode_anchor.replace('xx', file).replace('.txt', '') + '\n'

		series_input = '<h3 class="page-header">' + current_file.read() 
		series_working = series_input.replace('\n\n', '</h3>\n<p>',1).replace('\n\n', '</p>\n\n<p>')

		series_output += local_episode_anchor + series_working + episode_end

	FOOTER = FOOTER.replace('YEAR', str(datetime.datetime.now().year))

	series_output = series_output.replace('HIDDEN_MENU', series_hidden_menu).replace('SIDEBAR', series_side_menu)
	series_output += FOOTER
	series_file.write(series_output)	
	series_file.close()
		
