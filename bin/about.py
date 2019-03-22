#import os
#from ipywidgets import HTML
from ipywidgets import Output
#from IPython.display import IFrame
from IPython.display import display, HTML

#from IPython.core.display import display, HTML

class AboutTab(object):

    def __init__(self):
        # IFrame(src="about.html", width=700, height=700)
#        display(HTML('<h1>Hello, world!</h1>'))
        self.tab = Output()
        self.tab.append_display_data(HTML(filename='doc/about.html'))
        
