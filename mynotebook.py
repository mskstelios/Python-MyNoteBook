import sys
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QCalendarWidget,
    QListWidget, QSizePolicy, QMenuBar, QLabel, QPushButton, QFileDialog, QMenu, QAction
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# Import your custom modules
from welcoming import show_initial_message, reset_welcome_message
from Menu.file_menu import create_file_menu
from Menu.edit_menu import create_edit_menu
from Menu.tools_menu import create_tools_menu
from Menu.format_menu import create_format_menu
from Menu.settings_menu import create_settings_menu
from Menu.about_menu import create_about_menu
from event_handlers import handle_close_event

def load_files_in_list(list_widget, directory):
    list_widget.clear()
    text_extensions = {'.txt', '.py', '.cpp', '.h', '.c', '.java', '.html', '.css', '.js', '.json', '.xml', '.md', '.ini', '.bat', '.sh', '.ini'}

    if os.path.isdir(directory):
        index = 1
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if any(filename.endswith(ext) for ext in text_extensions):
                    full_path = os.path.join(root, filename)
                    list_item_text = f"{index}. {filename}"
                    list_item = list_widget.addItem(list_item_text)
                    list_widget.item(list_widget.count() - 1).setData(Qt.UserRole, full_path)
                    index += 1  # Increment the index
    else:
        list_widget.addItem("No files found or directory does not exist.")


def display_file_content(item, text_edit):
    full_path = item.data(Qt.UserRole)
    if full_path and os.path.exists(full_path):
        with open(full_path, 'r') as file:
            content = file.read()
            text_edit.setPlainText(content)
    else:
        text_edit.setPlainText(f"Error: File '{item.text()}' not found.")

def setup_text_editor():
    text_edit = QTextEdit()
    text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    text_edit.setPlaceholderText("Start writing or editing here...")
    text_edit.setStyleSheet("""
        QTextEdit {
            background-color: #f5f5f5;
            color: #333;
            border: 1px solid #d0d0d0;
            font-family: Arial;
            font-size: 14px;
            padding: 10px;
        }
    """)
    return text_edit

def setup_calendar():
    calendar = QCalendarWidget()
    calendar.setStyleSheet("""
        QCalendarWidget {
            background-color: #ffffff;
            border: 1px solid #cccccc;
        }
        QCalendarWidget QAbstractItemView {
            selection-background-color: #0078d7;
            selection-color: #ffffff;
        }
    """)
    calendar.setFixedSize(350, 250)
    return calendar

def setup_file_list():
    """Setup the file list widget."""
    list_widget = QListWidget()
    list_widget.setStyleSheet("""
        QListWidget {
            background-color: #ffffff;
        }
        QListWidget::item {
            padding: 8px;
            font-family: Arial;
            font-size: 14px;
        }
        QListWidget::item:selected {
            background-color: #0078d7;
            color: white;
        }
    """)
    list_widget.setFixedSize(300, 450)

    # Create context menu
    list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
    list_widget.customContextMenuRequested.connect(lambda pos: show_context_menu(list_widget, pos))

    return list_widget

def show_context_menu(list_widget, pos):
    menu = QMenu()
    pin_action = QAction("Pin to Top", menu)
    delete_action = QAction("Delete File", menu)
    reveal_action = QAction("Reveal in Explorer", menu)

    menu.addAction(pin_action)
    menu.addAction(delete_action)
    menu.addAction(reveal_action)

    action = menu.exec_(list_widget.mapToGlobal(pos))

    if action == pin_action:
        selected_item = list_widget.currentItem()
        if selected_item:
            pin_file_to_top(list_widget, selected_item)
    elif action == delete_action:
        selected_item = list_widget.currentItem()
        if selected_item:
            delete_file_from_list(list_widget, selected_item)
    elif action == reveal_action:
        selected_item = list_widget.currentItem()
        if selected_item:
            reveal_file_in_explorer(selected_item)

def pin_file_to_top(list_widget, item):
    list_widget.takeItem(list_widget.row(item))  # Remove the item from its current position
    list_widget.insertItem(0, item)  # Add it to the top

def delete_file_from_list(list_widget, item):
    list_widget.takeItem(list_widget.row(item))

def reveal_file_in_explorer(item):
    """Reveal the file in the file explorer."""
    full_path = item.data(Qt.UserRole)
    if full_path and os.path.exists(full_path):
        if sys.platform == "win32":
            subprocess.run(["explorer", "/select,", full_path])
        elif sys.platform == "darwin":  # macOS
            subprocess.run(["open", "-R", full_path])
        elif sys.platform == "linux":  # Linux
            subprocess.run(["xdg-open", full_path])

def setup_header_label():
    """Setup the header label for the file list."""
    header_label = QLabel("Current files in your directory:")
    header_label.setStyleSheet("""
        font-size: 16px;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
    """)
    return header_label

def setup_menu_bar(display, text_edit):
    menubar = QMenuBar(display)
    menubar.addMenu(create_file_menu(display, text_edit))
    menubar.addMenu(create_edit_menu(display, text_edit))
    menubar.addMenu(create_tools_menu(display, text_edit))
    menubar.addMenu(create_format_menu(display, text_edit))
    menubar.addMenu(create_settings_menu(display, text_edit))
    menubar.addMenu(create_about_menu(display))
    return menubar

def custom_close_event(event, text_edit, display):
    handle_close_event(event, text_edit, display)

def main():
    # Configuration
    app = QApplication([])
    display = QWidget()
    display.setGeometry(100, 100, 1200, 800)
    display.setWindowIcon(QIcon(os.path.join('Assets', 'icon.png')))
    display.setWindowTitle("MyNoteBook")

    show_initial_message()

    # Setup Widgets
    text_edit = setup_text_editor()
    calendar = setup_calendar()
    list_files = setup_file_list()
    header_label = setup_header_label()

    # Load button to open directory dialog
    load_button = QPushButton("Select Directory and Load Files")
    load_button.setStyleSheet("""
        QPushButton {
            background-color: #0078d7;
            color: white;
            padding: 5px 10px;
            font-size: 14px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #005fa3;
        }
    """)

    def open_directory_dialog():
        """Opens a file dialog to select a directory and load files."""
        directory = QFileDialog.getExistingDirectory(display, "Select Directory", os.getcwd())
        if directory:
            load_files_in_list(list_files, directory)

    load_button.clicked.connect(open_directory_dialog)

    # Layouts
    calendar_and_list_layout = QVBoxLayout()
    calendar_and_list_layout.addWidget(calendar)
    calendar_and_list_layout.addWidget(header_label)
    calendar_and_list_layout.addWidget(list_files)
    calendar_and_list_layout.addWidget(load_button)

    main_layout = QVBoxLayout()
    main_layout.addWidget(setup_menu_bar(display, text_edit))  # Add menu bar here
    layout_h = QHBoxLayout()
    layout_h.addWidget(text_edit)
    layout_h.addLayout(calendar_and_list_layout)
    main_layout.addLayout(layout_h)
    main_layout.setContentsMargins(10, 10, 10, 10)

    display.setLayout(main_layout)

    # Load initial files into the list widget
    load_files_in_list(list_files, os.getcwd())

    # Connect list item click to display file content
    list_files.itemClicked.connect(lambda item: display_file_content(item, text_edit))

    # Event handling
    display.closeEvent = lambda event: custom_close_event(event, text_edit, display)
    display.show()
    app.exec_()

if __name__ == "__main__":
    main()

