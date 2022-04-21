import dearpygui.dearpygui as dpg
import webbrowser
import os


def server():
 os.system("python -m flask run")

def git():
 webbrowser.open("https://github.com/Zordon1337/simple-http-server")


dpg.create_context()

dpg.create_viewport()

dpg.setup_dearpygui()




with dpg.window(label="simple http server - example build") as main_window:
    
    dpg.add_text("Note: this is example build")
    dpg.add_button(label="Run server", callback=server)
    dpg.add_button(label="Git Repository", callback=git)
    dpg.add_text("Created by Zordon1337")


dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()