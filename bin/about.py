from ipywidgets import Output
from IPython.display import display, HTML

class AboutTab(object):

    def __init__(self):
        self.tab = Output()
        self.tab.append_display_data(HTML(filename='doc/about.html'))
        
