from kivy.gesture import GestureDatabase, Gesture
from kivy.uix.boxlayout import BoxLayout

gesture_strings = {
    'left_to_right_line': 'eNp900tME0EYB/AtrwqioCLyUMEHuqggvgEfDL7GtxUEVhAolIU2SOFrtwIxXygBSfBENTHoBY7ABS4m6AUvnkw0RDEh0QQPJh4lchAuOjPZNaElM5nspP/5fZ0v3Wkw2tXqedid36L7jYBPT6DmCkpuL9gQolQtSVEUc7u+w9feFHAZEE2J/c9UTubvai2ebRvtD3Rfg9elQwwtef2Cj5daHNtw654WtwGxlBQqfCRrsezZ6Wky3BBHSV9QpFoMe3gb2nSwa/wzrNPsbPEbvvZW3Q/xtZCwZpflAiTAetZrIsIGVUvkZS6frns72j1eww8bayFJpaTqrTiIkoCTr7YBSKZEnLUq3ERJNQkPN1NSI8ptLHSI3QHYQkld0JLEDFMocf4vzzbDrZS4Rq1QMb8zlZJm63Tj418+BmAbJa2WNEbN8jRKOqzmDacZplPi/xUeZlDSabVkWKdnUvLIYYWKGW6npKcjPNxBSe9weLiTvaPC8DCLkv4ImU3J4zEz9C+Y4S5KBrTwcDcLneHhHhZ2hYd7dXGJzFeZUwv71DXvgYODBNjProGKkKtqNlbVBQfozNeKWAebIuiGg7Tk+Wxb6mxbdqDRzfUhhDzVzdz8ULptKD3KzcSzwUI2g6bIRzgsxNxyVmg56ykXg4sj6YsjxBQFCEfk4ijCMSE+x5EmNrkI8vNsljiOcEKID6K9NC48HAwppjiJcEouChGKhHiXVzaXV/aFiZnW3unM3mlLFCOcloszCGeFeOWt/OGt/BkpziGUyAVBKJWL8wgXuCjpKV3KKl1SuOi3kRQbsX6PiwiX5OIyApWLKwhXhXizMjmxMjnGxZPQeEZo3BLXEK7LxQ2Em3JxC+G2EO/tBX57gREpHAh35KIMoVwu7iJUCPFpgjcyFSkqEarkQkO4JxfVCDVycR+hVoh5xRGrOGIiRR1CvVw4ERqE+NY3XNQ3XBwpGhFcctGEoAuxEFSjgmo0F0Oh+ORQvPXPbkZokQs3gkeI76MrSWyuEnqgsSHQmP8PRFZYWQ==',
    'right_to_left_line': 'eNp91X1MVWUcwPGLoghpIGqhpl4L9EoImCXaGz/M+mVlogheQN4uHLm8yOV3X3iLRy4i+FIo+VIJlm6uOdYf4dq02AyMylVMcS7mnBVpbA1bsVFbW2v13Kd7mT0/xvnjnsvnfM95nj3nXI53amFZSVVtfLHhcnucRhj692Ra0UhBgqZYrOEmk8l/OK/S6SjyFLppKkJo09U5tw9ctIbKw25HueEsqCg0KBiTPznh29qt0+UBu1FSbHfTNIQok9qs0+RHdUmR207TEfba/8Ng+VFRsMugEKvvb5phDZE7l9vpKDNcFJpDYRPOMk0FYXSfnOtMQbMs1pm+0wqdhlFR6SipcLvo/hwKtyC0nFYDIbiv/uPbWihCYlsAR9WXFpotscaPHrUPaqFIiXYd50jM13GuRAhghP+a8yRG6PgAQvPPOj4osUvHKImVOs6XaNJxgVxPNvpChCazjg8hNI7quAjBO6TjYoSGXh2XIOxmo5sR6lN1XIpQx/BhhNo2HR+RuETdmnvWMxqhpku/RzESA+vpHvLjMoRqr47LEapGdZQPQ1W+jivkoL06xko06/io/J6qYxyCi42+EsHZpWM8AjFMkMimlCjRpOMqhMo2HR+TyOa5GsEBOj6OUMHwCYRdbPQ1COUN/tsxjkkIZWqVgu7BtRLZPNchlLJfx5MIJewWP4Vgz9cfhqcRisefOrMfn5EIOj6LsJOVyRJNOgJC0ZCOKRJZuR7BNn7NBP+/i+cQCoZ03CDRrOPzCPleHV9AyGPXRIRcVr6IkMNwo0TQ8SWEHT2B9QzgyxJN/ns0jq8gZPfquAkhi03pVYls9M0ImaxMlcimtAXBatJxK8J2VqYhZLByG0I6GyhdIjs9A2Ebw+0IaQytCFvZNTMlstGzELawMttQ7zH/22RHDuVYJnwVpfqCMMqVb6I8QfkWa5A8q4YKMPmnUtvI52diFdSSDXuq2wdWJZ73emx2X10oqMhil92djTfutu5YY7dhctIXkVE1vSZ/YQjaqYofvw/dn/NLHS+KBdlVMdQ19qfYWMSLEkGlqvju5tkUa2cTL8oElU9e7BJUoYqbS9dunr35Ii8cgionL0iQUxWD/TG35w7+zQuXIPfkhUdQlSqud6ZcuHjlEi+qBdWoYmCkO/Lc2VZe1AqqU0X/waOLRmmCVX9NUP3khRC0WxVfbvj6q/X5n/KiQZBXFX0jpzobFxzhRaOgPaq4FBcV7B7LlUXPzsUN4Z2xgaJJ0F5VdA9vjc5eHecrKD3k1p73A09Qs6AWVXw4WGxOj/uYF/sE7VdFR8ehzEt1A7w4IOigKurvzFqQMM/Ei9cFveEres6Yjx0+Nz+CF62CDqnig979wWZHFy8OC2pTxXlvUlXDoXpevCnoiCp6zLEjvw5H8+KooGOq+Gx4+W3X3VRfkRZzq789IrBixwW9pYrLU8aypi9b7Fv1vBnGjUFnoHhb0Duq+KZ5YcadlN95cUJQuyqu3FzZ90P3R76iPLzv+OXMQNEh6KQqriVeWNd77S9evCvoPVVcTz75x4HfbLw4Jei0Kr71+n64m/5XGB5bgccW/y9mdeBH',
    'bottom_to_top_line': 'eNpt1Wtsk1UYwPFy3UVkKOPiABkDpFwcG4MNEG1BsNzEAgIdo+zSvWvL2Nqna3c/W8egDhgDZRtsKO6DkgVjLEwweOsiCZBA3OaUi9yGxMAHRqbBRJSg5z08Jz55pR/W8uv/9Jz3vKfUP8CW6ywsibcrBV6fR4k04TPoplZBPwb99ZYonU6Hb6e7Pa5sn80LA0zG8IjCYGnokCWCv+11bVU8mfk2BQaaDKea1EezZTB/w6E47Q4vDDIZy/w69WEZxP8UObO9DhhsMibqnuBA/ic/M0+BMIv6bwi3hPGnAq/HlasUQIQVIp+6yrUiiIRn+FqHMHhWbxmiDrN5FCXf7XLmewtgqBWi9CZjsVFMZDKmhv5RHwEYRnBjJeJzBNPa1ef+AXie4Cbxol8AhhO0itGPAxBNcLMfyxEEM+REIyn2iBcBGEUwKxaHjyZoi8XyBYLZ6fiZMQQVOdEYjhmIOR8ijuXoR7TL2cdxbEF0ZuDsL3IMIm65icPHc+xE3CqXFMuxBzGvBXECwXw5PI6gOwHLiRz7JHYiTiII+xAnE/TI4S9RlMOnECzwI+oJeuXip1JsR5xG0CevaDpZfKEBr2gGx3aJnbh1L5OtK0pAjCebXCQnmkmxDzGB3CO8gwFI5K/dEuVJnkVucYnckCSKcvGzOZoRS3WIczgmSJQTJVPcixOlcIxFLJMTzaUoz/w8ivJ2zCdYLnf+FYpuxAUU5fBXCTI5+2sU5QkxUJTH20iwwoy4kKLcpUUEK+UuvU5RrnMxxSDiEorybr7BcRiiPxzRRHE04lKKcpeWUZTXvpyjTuJSxBUU5WWupCgX/ybFYsRVFOVX5i2KcpPNFFsRV/MDLL8d/nOIayjKu7mW4l3EtynKrVtH8U/E9Yr4ecH/5DdYwaJ/6i+EWQ0iIZX/QGxkkKa39OOjimGTKeSwjV+yYqZOQAlYTaHbidZlhy8n+7Icar2ZQbre8V/n4MWtBz//cfH4X1hkMMj8XzHCdaenfwwWWQxs2qJnYs7BUN4ULLIZKNriemttWPPZ41jkMLCrhSH1+JmxD++L4mrk8usnT0Rj4WDgFEVJ5O/H4upEcaWh94z79mEstjDIFcWOH5t6q81Gtbh0adTR6qobWGxlkCeKXeXTUh6tE59xcfTCusbYOCzyGbhEUT8vb3fbMb9a/PDr0LSse/excDMAbdHlPrZ43JhSLDwMCrRFh+2kOZ3fqieFl4FPFI175gT7ktrV4kLpowndnbVYFDIo0hZnohu+ytsyCYtiBiXa4vT0q7W3zi7AopRBmbYI/WZus+qHYVHOgGmLz1fZH8a/78aigkGltmhds773ROs+LPwMqrRX27T5mn3ofB0W2xhUi2LvxC+3+VJFAW0r00/u92OxncEOzZ0zHC67M/KDx/IzAgzeEYWr6KO5mRHqnTME78dsbKppx6KGwU7NCTKcGr7+Wq+5D4tdDHaLU+jzB1MOtKjrMLSHbTiyOvcBFrUM9oiioqPzws6j4jNOd5T/0h36Gos6Bnu1xbkZ9fqPZ4/FYh+Dd7XF+fSzaZftK7F4j8F+bdGpv7uuvEKewnoGDdqi68634LwpT3IjgwPaovt8V9QnEd9hcZBBkyi2RxUHv7kirvanz25/ei/pCBbNDA6JouaL8L+Tb4hdv3Rq1vdVk/m3UvFlZfqy4v8FYXKY7w==',
    'top_to_bottom_line': 'eNp901tIFFEYwPHxWtq9LO2qWel22zW7l+bYbbIytbLGVVN3Hd1tdXe/3R1N4qP1Ict6sYioKDLoQuFDQQUhsV0elArywahMLCiigsqHoB6Cmpm+gcMQcx5mZv/nN3POw9lwjNPjbmqx1kvBkByQEgW6Aze/FaIQoi3iOI7jaLrKH/DVys4QxAh8fNKa4cxcu5igTId8DVKgxuuUIFbIu3dWHefEeGXCJbnrXSGIE3jkOXWIccql2V0bckG8wKdz/2KscvHWNEowQlR/w0hxhHILhgI+jxSEhEpI/O8ud2kgEUYpex2NMMYijlZfcwYkyev3ub2hIIythHEWgW9O0xYS+NZf2kMbjGfjO4oT2NhLcSIbb1KcpEROj0cpJrGxmuJkNqZQnCLwTcMUw58oJrNR/2YKG7MoTmXiIX2haUzEPorTldhH8aC++RlMbOmgOJOJzfo3ZzFRTqOYysTAH220QRoT/frqs5nYGCGZzkR3J8k5TKx7QHEuE2t5ivOY6NC2FNUGGUys1mUmE/eFSSqHoekmxQp9S/OV2EmxXFs9ug0WKLFDjxzFhUy06/tcJGmHnY7c4kqwWv57XotVkAg25bhmISyxiFHKWwcgW8hr/fGbK1zPa6EFlgp5Q9Z424vISdnhUvUyhOUWl+ICrrffpzaEXYp4c2rwQs7paBIrEFZqwll87dmth5wqXh/pfmqTrSRWIaw2ipfvL7Uft38jsQZhrVH0Z9fJA6kDJHIQcs3FOoQ8o+jrsT3yfs4gwSPkqyJS5Rzf1Tmkid78J90ncsMk1iNsMBcbETaZi80IglHc/+L50F7iJ7EFocBcbEXYZhRXjgXTe9dlkdiOUGgudiAUGUTk0quY2HMrh0kUI5SYi50Iu8zFboRSo+g+vDDp46YzJPYg7DUXIkKZUfSUWm/Hdeur2BHKzUUFQqVRPH9+tyK84TyJfQhV5qIaocZcOBCcRtHvmeN4vD+KRC2CZC7qEOqN4mVH6Z1P53eTcCG4jWJge+uBy73JJPYjeMxFA0KjUQxevHrj59cCEl4En1EMdfVg3NgZJPwIoImWssGc60Xqfz/yruJHZntys+yQZEeN7LD+BaE+oFM=',
}

gestures = GestureDatabase()
for name, gesture_string in gesture_strings.items():
    gesture = gestures.str_to_gesture(gesture_string)
    gesture.name = name
    gestures.add_gesture(gesture)

class GestureBox(BoxLayout):
    def __init__(self, **kwargs):
        for name in gesture_strings:
            self.register_event_type('on_{}'.format(name))
        super(GestureBox, self).__init__(**kwargs)

    def on_left_to_right_line(self):
        pass
    def on_right_to_left_line(self):
        pass
    def on_bottom_to_top_line(self):
        pass
    def on_top_to_bottom_line(self):
        pass

    def on_touch_down(self, touch):
        touch.ud['gesture_path'] = [(touch.x, touch.y)]
        super(GestureBox, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud['gesture_path'].append((touch.x, touch.y))
        super(GestureBox, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        #print(touch.ud['gesture_path'])
        if 'gesture_path' in touch.ud:
            gesture = Gesture()
            gesture.add_stroke(touch.ud['gesture_path'])
            gesture.normalize()
            match = gestures.find(gesture, minscore=0.85)
            if match:
                print("{} happened".format(match[1].name))
                self.dispatch('on_{}'.format(match[1].name))
        super(GestureBox, self).on_touch_up(touch)
