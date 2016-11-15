TITLE = 'CNC M97 Lx calculator'

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class Form(GridLayout):
    K=10
    def calculate(self):
        try:
            stock = self.K*float(self.length.text)
            chuck = float(self.chuck.text)
            detail = float(self.detail.text)
            res = '%.2f'%((stock-chuck)/detail)
        except:
            res = 'error'
        self.M.text='M97 P1000 L%s'%res
    def doM(self,inst):
        self.calculate()
    def cmmm(self,inst):
        if self.mm.text=='mm':
            self.mm.text='Cm'
            self.mm.state='down'
            self.K=10.
        else:
            self.mm.text='mm'
            self.mm.state='normal'
            self.K=1. 
        self.calculate()
        
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.cols=3
        # stock
        self.add_widget(Label(text='Length:'))
        self.length = TextInput(text='123',multiline=False)
        self.add_widget(self.length)
        self.mm = Button(text='Cm',state='down')
        self.mm.bind(on_press=self.cmmm)
        self.add_widget(self.mm)
        # detail
        self.add_widget(Label(text='Detail:'))
        self.detail = TextInput(text='45',multiline=False)
        self.add_widget(self.detail)
        self.add_widget(Label(text='mm'))
        # chuck
        self.add_widget(Label(text='Chuck:'))
        self.chuck = TextInput(text='100',multiline=False)
        self.add_widget(self.chuck)
        self.add_widget(Label(text='mm'))
        # result
        self.M = Label(text='M97 P1000 Lx')
        self.add_widget(self.M)
        # calc
        self.calc = Button(text='Calc')
        self.calc.bind(on_press=self.doM)
        self.add_widget(self.calc)
        # default calc
        self.calculate()

class My(App):
    def build(self):
        return Form()

My().run()