from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory

f = open('api.key', 'r')
key = f.readline().strip()
f.close()


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        search_template = \
                "http://api.openweathermap.org/data/2.5/find?q={}&type=like&APPID="+key
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        cities = [(d['name'], d['sys']['country'])
                for d in data['list']]
        self.search_results.item_strings = cities
        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()

    def args_converter(self, index, data_item):
        col = '#2980b9'
        if index % 2:
            col = '#3498db'
        city, country = data_item
        return {'location': (city, country), 'col': col}

class LocationButton(ListItemButton):
    location = ListProperty()
    col = StringProperty()

class CurrentWeather(BoxLayout):
    location = ListProperty(['New York', 'US'])
    conditions = StringProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()

    def update_weather(self):
        weather_template = \
            "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&APPID="+key
        weather_url = weather_template.format(*self.location)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        self.conditions = data['weather'][0]['description']
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']

class WeatherApp(App):
    pass

class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()
    add_location_form = ObjectProperty()

    def show_current_weather(self, location=None):
        self.clear_widgets()

        if self.current_weather is None:
            self.current_weather = CurrentWeather()

        if location is not None:
            self.current_weather.location = location
        self.current_weather.update_weather()
        self.add_widget(self.current_weather)
    
    def show_add_location_form(self):
        self.clear_widgets()
        if self.add_location_form is None:
            self.add_location_form = AddLocationForm()
        self.add_widget(self.add_location_form)

if __name__ == '__main__':
    WeatherApp().run()
