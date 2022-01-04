from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class MyScrollView(ScrollView):
    def on_touch_move(self, touch):
        # get touch position in coordinates of the main_box (parent of inner_scroll)
        x,y = self.ids.main_box.to_widget(*self.to_window(*touch.pos))

        # if converted position is within the inner_scroll, send touch to the inner_scroll
        if self.ids.inner_scroll.collide_point(x,y):
            return super(MyScrollView, self).on_touch_move(touch)

        if self.ids.inner_scroll2.collide_point(x,y):
            return super(MyScrollView, self).on_touch_move(touch)

class ScrolltwoApp(MDApp):

    def build(self):
        app=MDApp.get_running_app()
        Clock.schedule_once(self.add_members)
        return app.root

    def add_members(self,dt):
        app=MDApp.get_running_app()
        for i in range(15):
            app.root.ids.main_box.add_widget(Button(text='button'+str(i), size_hint=(1.0, None), height=50,background_color=[0,0,1,1]))
            app.root.ids.horizontal_grid.add_widget(Button(text='button' + str(i), size_hint=(None, None),height=130,width=100,background_color=[0,0,1,1]))
            app.root.ids.horizontal_grid2.add_widget(Button(text='button' + str(i), size_hint=(None, None),height=130,width=100,background_color=[0,0,1,1]))

if __name__ == '__main__':
    Window.show_cursor = True
    Window.size = (360, 680)
    ScrolltwoApp().run()
