from PyQt5.QtWidgets import QAction, QMenu
from PyQt5.QtCore import QSettings
from welcoming import reset_welcome_message

def action_light_theme(text_widget):
    text_widget.setStyleSheet("background-color: white; color: black;")

def action_dark_theme(text_widget):
    text_widget.setStyleSheet("background-color: black; color: white;")

def create_settings_menu(display, text_widget):
    settings = QMenu("&Settings", display)

    light_theme_action = QAction("Light Theme", display)
    light_theme_action.triggered.connect(lambda: action_light_theme(text_widget))
    settings.addAction(light_theme_action)

    dark_theme_action = QAction("Dark Theme", display)
    dark_theme_action.triggered.connect(lambda: action_dark_theme(text_widget))
    settings.addAction(dark_theme_action)

    restore_message_action = QAction("Restore Welcome Message", display)
    restore_message_action.triggered.connect(lambda: reset_welcome_message())
    settings.addAction(restore_message_action)

    return settings
