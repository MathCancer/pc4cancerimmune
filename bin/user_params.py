 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='immune_activation_time', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.immune_activation_time = FloatText(
          value=20160,
          step=1000,
          style=style, layout=widget_layout)

        param_name2 = Button(description='number_of_immune_cells', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.number_of_immune_cells = IntText(
          value=125,
          step=10,
          style=style, layout=widget_layout)

        param_name3 = Button(description='save_interval_after_therapy_start', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.save_interval_after_therapy_start = FloatText(
          value=60,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='immune_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.immune_apoptosis_rate = FloatText(
          value=6.944e-5,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name5 = Button(description='oncoprotein_threshold', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.oncoprotein_threshold = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name6 = Button(description='immune_kill_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.immune_kill_rate = FloatText(
          value=0.8762,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='immune_attachment_rate', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.immune_attachment_rate = FloatText(
          value=0.72138388,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='immune_attachment_lifetime', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.immune_attachment_lifetime = FloatText(
          value=90.0,
          step=1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='immune_migration_bias', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.immune_migration_bias = FloatText(
          value=0.679587213,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='immune_motility_persistence_time', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.immune_motility_persistence_time = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='immune_migration_speed', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.immune_migration_speed = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.tumor_radius = FloatText(
          value=250,
          step=10,
          style=style, layout=widget_layout)

        param_name13 = Button(description='tumor_mean_immunogenicity', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.tumor_mean_immunogenicity = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='tumor_immunogenicity_standard_deviation', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.tumor_immunogenicity_standard_deviation = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'

        desc_button1 = Button(description='time at which therapy begins', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='number of immune cells at start of therapy', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='save (output) interval after therapy begins', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='immune cell apoptosis rate (d1)', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='cancer cells are not immunogenic for p below this value (d2)', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='rate that attached immune cells can apoptose cancer cells (d3)', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='rate that immune cells can attach to a cell in close contact (d4)', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='max time immune cells remain attached to a target cell (d5)', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='immune cell migration bias (d6)', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='mean immune cell migration persistence time', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='immune cell migration speed', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='initial tumor radius', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='mean oncoprotein p at start', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='standard deviation of tumor p at start', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'

        row1 = [param_name1, self.immune_activation_time, units_button1, desc_button1] 
        row2 = [param_name2, self.number_of_immune_cells, units_button2, desc_button2] 
        row3 = [param_name3, self.save_interval_after_therapy_start, units_button3, desc_button3] 
        row4 = [param_name4, self.immune_apoptosis_rate, units_button4, desc_button4] 
        row5 = [param_name5, self.oncoprotein_threshold, units_button5, desc_button5] 
        row6 = [param_name6, self.immune_kill_rate, units_button6, desc_button6] 
        row7 = [param_name7, self.immune_attachment_rate, units_button7, desc_button7] 
        row8 = [param_name8, self.immune_attachment_lifetime, units_button8, desc_button8] 
        row9 = [param_name9, self.immune_migration_bias, units_button9, desc_button9] 
        row10 = [param_name10, self.immune_motility_persistence_time, units_button10, desc_button10] 
        row11 = [param_name11, self.immune_migration_speed, units_button11, desc_button11] 
        row12 = [param_name12, self.tumor_radius, units_button12, desc_button12] 
        row13 = [param_name13, self.tumor_mean_immunogenicity, units_button13, desc_button13] 
        row14 = [param_name14, self.tumor_immunogenicity_standard_deviation, units_button14, desc_button14] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.immune_activation_time.value = float(uep.find('.//immune_activation_time').text)
        self.number_of_immune_cells.value = int(uep.find('.//number_of_immune_cells').text)
        self.save_interval_after_therapy_start.value = float(uep.find('.//save_interval_after_therapy_start').text)
        self.immune_apoptosis_rate.value = float(uep.find('.//immune_apoptosis_rate').text)
        self.oncoprotein_threshold.value = float(uep.find('.//oncoprotein_threshold').text)
        self.immune_kill_rate.value = float(uep.find('.//immune_kill_rate').text)
        self.immune_attachment_rate.value = float(uep.find('.//immune_attachment_rate').text)
        self.immune_attachment_lifetime.value = float(uep.find('.//immune_attachment_lifetime').text)
        self.immune_migration_bias.value = float(uep.find('.//immune_migration_bias').text)
        self.immune_motility_persistence_time.value = float(uep.find('.//immune_motility_persistence_time').text)
        self.immune_migration_speed.value = float(uep.find('.//immune_migration_speed').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.tumor_mean_immunogenicity.value = float(uep.find('.//tumor_mean_immunogenicity').text)
        self.tumor_immunogenicity_standard_deviation.value = float(uep.find('.//tumor_immunogenicity_standard_deviation').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//immune_activation_time').text = str(self.immune_activation_time.value)
        uep.find('.//number_of_immune_cells').text = str(self.number_of_immune_cells.value)
        uep.find('.//save_interval_after_therapy_start').text = str(self.save_interval_after_therapy_start.value)
        uep.find('.//immune_apoptosis_rate').text = str(self.immune_apoptosis_rate.value)
        uep.find('.//oncoprotein_threshold').text = str(self.oncoprotein_threshold.value)
        uep.find('.//immune_kill_rate').text = str(self.immune_kill_rate.value)
        uep.find('.//immune_attachment_rate').text = str(self.immune_attachment_rate.value)
        uep.find('.//immune_attachment_lifetime').text = str(self.immune_attachment_lifetime.value)
        uep.find('.//immune_migration_bias').text = str(self.immune_migration_bias.value)
        uep.find('.//immune_motility_persistence_time').text = str(self.immune_motility_persistence_time.value)
        uep.find('.//immune_migration_speed').text = str(self.immune_migration_speed.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//tumor_mean_immunogenicity').text = str(self.tumor_mean_immunogenicity.value)
        uep.find('.//tumor_immunogenicity_standard_deviation').text = str(self.tumor_immunogenicity_standard_deviation.value)
