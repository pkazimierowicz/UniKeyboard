import pynput
import json

class ActionHandler:
    def __init__(self):
        self.mouse = pynput.mouse.Controller()

    def handle_mouse_event(self, event_dict):
        if self.mouse_button_for_key(event_dict["code"]) is not None:
            if event_dict["value"] == 1:
                self.mouse.press(self.mouse_button_for_key(event_dict["code"]))
            else:
                self.mouse.release(self.mouse_button_for_key(event_dict["code"]))
        elif event_dict["code"] == 8:
            self.mouse.scroll(0, event_dict["value"])
        elif event_dict["code"] == 0:
            self.mouse.move(event_dict["value"],0)
        elif event_dict["code"] == 1:
            self.mouse.move(0,event_dict["value"])

    def handle_keyboard_event(self, event_dict):
        pass

    def handle_event(self, json_string):
        json_dict = json.loads(json_string)
        if json_dict["type"] == "EV_REL":
            self.handle_mouse_event(json_dict["payload"])
        elif json_dict["type"] == "EV_KEY":
            if self.mouse_button_for_key(json_dict["payload"]["code"]) is not None:
                self.handle_mouse_event(json_dict["payload"])
        else:
            pass

    def mouse_button_for_key(self, key):
        if key == "BTN_RIGHT":
            return pynput.mouse.Button.right
        elif key == "BTN_LEFT":
            return pynput.mouse.Button.left
        elif key == "BTN_MIDDLE":
            return pynput.mouse.Button.middle
        else:
            return None
        
