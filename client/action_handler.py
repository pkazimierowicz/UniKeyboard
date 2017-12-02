import pynput
import json
from enum import Enum

class ActionHandler:
    @staticmethod
    def handle_mouse_event(event_dict):
        mouse = pynput.mouse.Controller()
        if ActionHandler.mouse_button_for_key(event_dict["code"]) is not None:
            if event_dict["value"] == 1:
                mouse.press(ActionHandler.mouse_button_for_key(event_dict["code"]))
            else:
                mouse.release(ActionHandler.mouse_button_for_key(event_dict["code"]))
        elif event_dict["code"] == 8:
            mouse.scroll(0, event_dict["value"])
            pass
        elif event_dict["code"] == 0:
            mouse.move(event_dict["value"],0)
        elif event_dict["code"] == 1:
            mouse.move(0,event_dict["value"])

    @staticmethod
    def handle_keyboard_event(event_dict):
        pass

    @staticmethod
    def handle_event(json_string):
        json_dict = json.loads(json_string)
        if json_dict["type"] == "EV_REL":
            ActionHandler.handle_mouse_event(json_dict["payload"])
        elif json_dict["type"] == "EV_KEY":
            if ActionHandler.mouse_button_for_key(json_dict["payload"]["code"]) is not None:
                ActionHandler.handle_mouse_event(json_dict["payload"])
        else:
            pass

    @staticmethod
    def mouse_button_for_key(key):
        if key == "BTN_RIGHT":
            return pynput.mouse.Button.right
        elif key == "BTN_LEFT":
            return pynput.mouse.Button.left
        elif key == "BTN_MIDDLE":
            return pynput.mouse.Button.middle
        else:
            return None
        
