from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_string(
'''
<ScrollApp>:
    ScrollView:
        size_hint: 1.0, 0.76
        pos_hint: {'center_y':0.5}
        bar_width: 10
        scroll_type: ['bars', 'content']
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, None
            height: self.minimum_height
            padding: 22, 0, 22, 50
            spacing: 50
            canvas:
                Color:
                    rgba: .15, .15, .15, .9
                Rectangle:
                    size: self.size
                    pos: self.pos
            Button:
                size_hint: None, None
                width: 100
                height: 100
                on_press: print('This button does not overlap the menu above')

            # "ScrollViews containers"
            Custom
            Custom
            Custom
            Custom
            Custom
    BoxLayout:
        size_hint: 1, 0.12
        pos_hint: {'y':0}
        Button:
            on_press: print("This menu at the bottom is not affected by the problem that occurs with the top one")
    BoxLayout:
        size_hint: 1, 0.12
        pos_hint: {'top':1.0}
        Button:
            text: 'Fixed Menu'
            on_press: print('This button stops working if there is a horizontal scrollview "behind"')


<Custom@BoxLayout>:
    orientation: 'vertical'
    size_hint: 1, None
    height: self.minimum_height
    Label:
        size_hint: None, None
        size: self.texture_size
        id: label
        font_size: 20
        text: 'Teste'
    ScrollView:
        do_scroll: True, True
        size_hint: 1, None
        height: 150

        GridLayout:
            id: grid
            size_hint: None, 1.01
            width: self.minimum_width
            spacing: 5
            cols: 3
            Button:
                text: 'button 1'
                size_hint: None, None
                size: 400, 150
                on_press: print('ScrollView button pressed')
            Button:
                text: 'button 2'
                size_hint: None, None
                size: 400, 150
                on_press: print('ScrollView button pressed')
            Button:
                text: 'button 3'
                size_hint: None, None
                size: 400, 150
                on_press: print('ScrollView button pressed')
''' )


class ScrollApp(FloatLayout):
    pass


class Test(App):
    def build(self):
        return ScrollApp()

Test().run()
