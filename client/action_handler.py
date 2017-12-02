import pynput
import json
from mapping import mapping

class ActionHandler:
    def __init__(self):
        self.mouse = pynput.mouse.Controller()
        self.keyboard = pynput.keyboard.Controller()

    def handle_event(self, json_string):
        json_dict = json.loads(json_string)
        print(json_dict)
        if json_dict["type"] == "EV_REL":
            self.handle_mouse_event(json_dict["payload"])
        elif json_dict["type"] == "EV_KEY":
            if self.mouse_button_for_key(json_dict["payload"]["code"]) is not None:
                self.handle_mouse_event(json_dict["payload"])
            else:
                self.handle_keyboard_event(json_dict["payload"])

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
        if event_dict["value"] == 1:
            self.keyboard.press(mapping[event_dict["code"]])
        else:
            self.keyboard.release(mapping[event_dict["code"]])

        
    def mouse_button_for_key(self, key):
        if key == "BTN_RIGHT":
            return pynput.mouse.Button.right
        elif key == "BTN_LEFT":
            return pynput.mouse.Button.left
        elif key == "BTN_MIDDLE":
            return pynput.mouse.Button.middle
        else:
            return None
    
    # def keyboard_button(self, string):
    #     if string == "":
    #         return pynput.keyboard.Key.alt
    #     elif string == "":
    #         return pynput.keyboard.Key.alt_l
    #     elif string == "":
    #         return pynput.keyboard.Key.alt_r
    #     elif string == "":
    #         return pynput.keyboard.Key.alt_gr
    #     elif string == "":
    #         return pynput.keyboard.Key.backspace
    #     elif string == "":
    #         return pynput.keyboard.Key.caps_lock
    #     elif string == "":
    #         return pynput.keyboard.Key.cmd
    #     elif string == "":
    #         return pynput.keyboard.Key.cmd_l
    #     elif string == "":
    #         return pynput.keyboard.Key.cmd_r
    #     elif string == "":
    #         return pynput.keyboard.Key.ctrl
    #     elif string == "":
    #         return pynput.keyboard.Key.ctrl_l
    #     elif string == "KEY_RIGHTCTRL":
    #         return pynput.keyboard.Key.ctrl_r
    #     elif string == "":
    #         return pynput.keyboard.Key.delete
    #     elif string == "":
    #         return pynput.keyboard.Key.down
    #     elif string == "":
    #         return pynput.keyboard.Key.end
    #     elif string == "KEY_ENTER":
    #         return pynput.keyboard.Key.enter
    #     elif string == "":
    #         return pynput.keyboard.Key.esc
    #     elif string == "":
    #         return pynput.keyboard.Key.f1
    #     elif string == "":
    #         return pynput.keyboard.Key.f2
    #     elif string == "":
    #         return pynput.keyboard.Key.f3
    #     elif string == "":
    #         return pynput.keyboard.Key.f4
    #     elif string == "":
    #         return pynput.keyboard.Key.f5
    #     elif string == "":
    #         return pynput.keyboard.Key.f6
    #     elif string == "":
    #         return pynput.keyboard.Key.f7
    #     elif string == "":
    #         return pynput.keyboard.Key.f8
    #     elif string == "":
    #         return pynput.keyboard.Key.f9
    #     elif string == "":
    #         return pynput.keyboard.Key.f10
    #     elif string == "":
    #         return pynput.keyboard.Key.f11
    #     elif string == "":
    #         return pynput.keyboard.Key.f12
    #     elif string == "":
    #         return pynput.keyboard.Key.f13
    #     elif string == "":
    #         return pynput.keyboard.Key.f14
    #     elif string == "":
    #         return pynput.keyboard.Key.f15
    #     elif string == "":
    #         return pynput.keyboard.Key.f16
    #     elif string == "":
    #         return pynput.keyboard.Key.f17
    #     elif string == "":
    #         return pynput.keyboard.Key.f18
    #     elif string == "":
    #         return pynput.keyboard.Key.f19
    #     elif string == "":
    #         return pynput.keyboard.Key.f20
    #     elif string == "":
    #         return pynput.keyboard.Key.home
    #     elif string == "":
    #         return pynput.keyboard.Key.left
    #     elif string == "":
    #         return pynput.keyboard.Key.page_down
    #     elif string == "":
    #         return pynput.keyboard.Key.page_up
    #     elif string == "":
    #         return pynput.keyboard.Key.right
    #     elif string == "":
    #         return pynput.keyboard.Key.shift
    #     elif string == "KEY_LEFTSHIFT":
    #         return pynput.keyboard.Key.shift_l
    #     elif string == "KEY_RIGHTSHIFT":
    #         return pynput.keyboard.Key.shift_r
    #     elif string == "":
    #         return pynput.keyboard.Key.space
    #     elif string == "":
    #         return pynput.keyboard.Key.tab
    #     elif string == "":
    #         return pynput.keyboard.Key.up
    #     elif string == "":
    #         return pynput.keyboard.Key.insert
    #     elif string == "":
    #         return pynput.keyboard.Key.menu
    #     elif string == "":
    #         return pynput.keyboard.Key.num_lock
    #     elif string == "":
    #         return pynput.keyboard.Key.pause
    #     elif string == "":
    #         return pynput.keyboard.Key.print_screen
    #     elif string == "":
    #         return pynput.keyboard.Key.scroll_lock
    #     else:
    #         return None
        
