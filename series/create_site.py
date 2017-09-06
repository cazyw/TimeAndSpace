# Python script to build the Doctor Who Archives
# Builds the episode review pages for each series
# 
# Requires:
# - text files per episode in series folders
# 
# Creates a page per series in the parent folder
#
# Updated: 3 March 2016



import os
import datetime


# Global variables

rootdir = '.'

# anchor at the top of each episode review
episode_anchor = '    <span class="anchor" id="axx"></span>'

# divider ending each episode review
episode_end = '</p>\n\n    </div>\n  </section>\n\n<!-- episode break -->\n\n'

# hash for series number and year
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

# link to episode review in small screen drop-down
hidden_menu = '           <li id="xx"><a href="#axx">EPISODE</a></li>\n'

# link to episode review in side bar
side_menu = '    <li><a href="#axx">EPISODE</a></li>\n'

# start of each section/episode review
section_start = '  <section class="row">\n'

# header section before the episode reviews
HEADER = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Doctor Who Archives - (New) Series x</title>
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <link href="css/styles.css" rel="stylesheet"  type="text/css">
</head>

<header>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <!-- Brand -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#episodes" aria-expanded="false">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          </button>
            <a class="navbar-brand" href="index.html">Doctor Who Archives</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div id="episodes" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
HIDDEN_MENU
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->

      <div class="jumbotron">
        <div class="container-fluid">
          <h1>Doctor Who Series x</h1>
          <p>Episodes from the series in xxxx</p> 
        </div><!-- /.container-fluid --> 
      </div><!-- /.jumbotron -->    
      <div id="buffer"></div>    
    </nav> 
</header>

<body data-spy="scroll" data-target="#episode-list">
<div id="main-content" class="container-fluid">


<!-- sidebar -->

<div id="episode-list" class="sidebar list-group">
  <ul class="nav nav-sidebar">
SIDEBAR
  </ul>
</div>

<!-- episode review -->

<div class="episode-review">
'''

# footer section after the episode reviews
FOOTER = '''</div><!-- /.episode review--> 
</div><!-- /.main content container--> 

<!-- Footer -->
<footer class="series-footer">
    <hr>
    <div class="container-fluid">
        <div class="row">
            <div class="col-xs-6 col-sm-6 col-md-6"><p>&copy; Caz YEAR</p></div>
            <div class="col-xs-6 col-sm-6 col-md-6" align="right"><p><a href="acknowledgements.html">Acknowledgements</a></p></div>
        </div>
    </div>
</footer>

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


$(document).ready(function () {
  $(".navbar-nav li a").click(function(event) {
    $(".navbar-collapse").collapse('hide');
  });
});
</script>
</body>
</html> 
'''

# Traverses the series directories and creates webpage for each series
		
for dirName, subdirList, fileList in os.walk(rootdir):
	print ('Found directory: %s' % dirName)
	
	# exclude the root directory as there are no series files
	
	if dirName == '.':
		continue
		
	series_filename = dirName + '.html'
	series_file = open('..\\' + series_filename,'w')
	series_file.truncate()
	print ('File created: ' + series_filename				)
	
	series_number = dirName[4:].replace('.txt','').replace('0','')
	
	series_hidden_menu = ""
	series_side_menu = ""
	
	series_output = HEADER.replace('Series x', 'Series ' + series_number).replace('series in xxxx', 'series in ' + series_year[series_number])
	

    # uses the file names and content in series folders 
    # to dynamically build the anchors and links in menus
	for file in fileList:
		file_path = os.path.join(dirName, file)
		current_file = open(file_path)
		print ('Opening series file: ' + file_path)

		title = current_file.readline()
		current_file.seek(0, 0)
		
		series_hidden_menu += hidden_menu.replace('xx', file).replace('.txt', '').replace('EPISODE', title.strip())
		series_side_menu += side_menu.replace('xx', file).replace('.txt', '').replace('EPISODE', title.strip())		
		
		local_episode_anchor = episode_anchor.replace('xx', file).replace('.txt', '') + '\n'

		series_input = '    <div class="col-xs-12">\n      <h3 class="page-header">' + current_file.read() 
		series_working = series_input.replace('\n\n', '</h3>\n      <p>',1).replace('\n\n', '</p>\n\n      <p>')

		series_output += section_start + local_episode_anchor + series_working + episode_end

	FOOTER = FOOTER.replace('YEAR', str(datetime.datetime.now().year))

	series_output = series_output.replace('HIDDEN_MENU', series_hidden_menu).replace('SIDEBAR', series_side_menu)
	series_output += FOOTER
	series_file.write(series_output)	
	series_file.close()
		
