# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory
from kivy.storage.jsonstore import JsonStore
import datetime

f = open('api.key', 'r')
key = f.readline().strip()
f.close()

def locations_args_converter(index, data_item):
    col = '#2980b9'
    if index % 2:
        col = '#3498db'
    city, country = data_item
    return {'location': (city, country), 'col': col}

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
        #self.search_results._trigger_reset_populate()


class LocationButton(ListItemButton):
    location = ListProperty()
    col = StringProperty()

class CurrentWeather(BoxLayout):
    location = ListProperty(['Seoul', 'KR'])
    conditions = StringProperty()
    conditions_image = StringProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()

    def update_weather(self):
        config = WeatherApp.get_running_app().config
        temp_type = config.getdefault("General", "temp_type", "metric").lower()
        weather_template = \
            "http://api.openweathermap.org/data/2.5/weather?q={},{}&units={}&APPID="+key
        weather_url = weather_template.format(*self.location, temp_type)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        self.conditions = data['weather'][0]['description']
        self.conditions_image = "http://openweathermap.org/img/w/{}.png".format(
                data['weather'][0]['icon'])
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']


class Forecast(BoxLayout):
    location = ListProperty(['Seoul', 'KR'])
    container = ObjectProperty()

    def update_weather(self):
        config = WeatherApp.get_running_app().config
        temp_type = config.getdefault("General", "temp_type", "metric").lower()
        weather_template = \
            "http://api.openweathermap.org/data/2.5/forecast?q={},{}&units={}&cnt=8"+\
            "&APPID="+key
        weather_url = weather_template.format(
                self.location[0], self.location[1], temp_type)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        self.container.clear_widgets()
        cnt = 0
        for day in data['list']:
            if(cnt % 2):
                cnt += 1
                continue
            cnt += 1
            label = Factory.ForecastLabel()
            label.date = datetime.datetime.fromtimestamp(day['dt']).strftime(
                    "%a %b %d")
            label.time = datetime.datetime.fromtimestamp(day['dt']).strftime(
                    "%H:%M:%S")
            label.description = day['weather'][0]['description']
            label.conditions_image = "http://openweathermap.org/img/w/{}.png".format(
                    day['weather'][0]['icon'])
            label.temp_min = day['main']['temp_min']
            label.temp_max = day['main']['temp_max']
            label.temp = day['main']['temp']
            self.container.add_widget(label)


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()
    locations = ObjectProperty()
    add_location_form = ObjectProperty()
    forecast = ObjectProperty()

    def __init__(self, **kwargs):
        super(WeatherRoot, self).__init__(**kwargs)
        self.store = JsonStore("weather_store.json")
        self.add_location_form = Factory.AddLocationForm()
        try:
            current_location = self.store.get("locations")['current_location']
            self.show_current_weather(current_location)
        except:
            self.show_add_location_form()

    def show_current_weather(self, location=None):
        self.clear_widgets()

        if self.current_weather is None:
            self.current_weather = CurrentWeather()
        if self.locations is None:
            self.locations = Factory.Locations()
            if(self.store.exists('locations')):
                locations = self.store.get("locations")['locations']
                self.locations.locations_list.adapter.data.extend(locations)

        if location is not None:
            self.current_weather.location = location
            if location not in self.locations.locations_list.adapter.data:
                self.locations.locations_list.adapter.data.append(location)
                #self.locations.locations_list._trigger_reset_populate()
                self.store.put("locations",
                        locations=list(self.locations.locations_list.adapter.data),
                        current_location=location)

        self.current_weather.update_weather()
        self.add_widget(self.current_weather)
    
    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(self.add_location_form)

    def show_locations(self):
        if self.locations is None:
            self.locations = Factory.Locations()
            if(self.store.exists('locations')):
                locations = self.store.get("locations")['locations']
                self.locations.locations_list.adapter.data.extend(locations)

        self.clear_widgets()
        self.add_widget(self.locations)

    def show_forecast(self, location=None):
        self.clear_widgets()

        if self.forecast is None:
            self.forecast = Factory.Forecast()

        if location is not None:
            self.forecast.location = location

        self.forecast.update_weather()
        self.add_widget(self.forecast)

class WeatherApp(App):
    def build_config(self, config):
        config.setdefaults('General', {'temp_type': "Metric"})

    def build_settings(self, settings):
        settings.add_json_panel("Weather Settings", self.config, data="""
            [
                {"type": "options",
                    "title": "Temperature System",
                    "section": "General",
                    "key": "temp_type",
                    "options": ["Metric", "Imperial"]
                }
            ]"""
            )
    def on_config_change(self, config, section, key, value):
        if config is self.config and key == "temp_type":
            try:
                self.root.children[0].update_weather()
            except AttributeError:
                pass

if __name__ == '__main__':
    WeatherApp().run()
