import pynput
import json
from enum import Enum

class ActionHandler:
    @staticmethod
    def handle_mouse_event(event_dict):
        mouse = pynput.mouse.Controller()
        if ActionHandler.mouse_button_for_key(event_dict["code"]) not None:
            if event_dict["value"] == 1:
                mouse.press(ActionHandler.mouse_button_for_key(event_dict["code"]))
            else:
                mouse.release(ActionHandler.mouse_button_for_key(event_dict["code"]))
        else if event_dict["code"] == 8:
            mouse.scroll(0, event_dict["value"])
            pass
        else if event_dict["code"] == 0:
            mouse.move(event_dict["value"],0)
        else if event_dict["code"] == 1:
            mouse.move(0,event_dict["value"])

    @staticmethod
    def handle_keyboard_event(event_dict):
        pass

    @staticmethod
    def handle_event(json):
        dict = json.loads(json)
        if dict["type"] == "EV_REL":
            ActionHandler.handleMouseEvent(dict["payload"])
        else if dict["type"] == "EV_KEY":
            if ActionHandler.mouse_button_for_key(dict["payload"]["code"]) not None:
                ActionHandler.handle_mouse_event(dict["payload"])
        else:
            pass

    @staticmethod
    def mouse_button_for_key(key):
        if key == "BTN_RIGHT":
            return pynput.mouse.Button.right
        else if key == "BTN_LEFT":
            return pynput.mouse.Button.left
        else if key == "BTN_MIDDLE":
            return pynput.mouse.Button.middle
        else:
            return None
        
