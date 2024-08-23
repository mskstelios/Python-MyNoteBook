from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction, QMenu, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QAction
from event_handlers import save_file

def create_file_menu(parent_widget, text_edit):
    file_menu = QMenu("File", parent_widget)
    save_action = QAction("Save", parent_widget)
    save_action.triggered.connect(lambda: save_and_update_content(text_edit, parent_widget))
    file_menu.addAction(save_action)

    return file_menu

def save_and_update_content(text_edit, parent_widget):
    if save_file(text_edit, parent_widget):
        print("File saved successfully.")

def action_new(display, text_widget):
    reply = QMessageBox.question(
        display,
        "SyntaxPad",
        "Do you want to delete everything?",
        QMessageBox.Yes | QMessageBox.No
    )
    if reply == QMessageBox.Yes:
        text_widget.clear()
    else:
        text_widget.setFocus()

def action_open(display, text_widget):
    file_filter = "Text Files (*.txt);;Python Files (*.py);;All Files (*.*)"
    file_path, _ = QFileDialog.getOpenFileName(display, "Open File", "", file_filter)
    if file_path:
        try:
            with open(file_path, "r", encoding='utf-8') as file:
                text_widget.setText(file.read())
        except Exception as e:
            print(f"Error opening file: {e}")

def action_save(display, text_widget):
    file_filter = "Text Files (*.txt);;Python Files (*.py);;All Files (*.*)"
    file_path, _ = QFileDialog.getSaveFileName(display, "Save File", "", file_filter)
    if file_path:
        try:
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(text_widget.toPlainText())
        except Exception as e:
            QMessageBox.critical(display, "Error", f"Error saving file: {e}")

def action_save_as(display, text_widget):
    file_filter = "Text Files (*.txt);;Python Files (*.py);;All Files (*.*)"
    file_path, _ = QFileDialog.getSaveFileName(display, "Save File As...", "", file_filter)
    if file_path:
        try:
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(text_widget.toPlainText())
        except Exception as e:
            QMessageBox.critical(display, "Error", f"Error saving file: {e}")

def action_exit(display, text_widget):
    reply = QMessageBox.question(
        display,
        "SyntaxPad",
        "Do you want to exit?",
        QMessageBox.Yes | QMessageBox.No
    )
    if reply == QMessageBox.Yes:
        display.close()
    else:
        text_widget.setFocus()



def create_file_menu(display, text_widget):
    files = QMenu("&Files", display)

    # New action
    new_action = QAction("New", display)
    new_action.setShortcut(QKeySequence("Ctrl+N"))
    new_action.triggered.connect(lambda: action_new(display, text_widget))
    files.addAction(new_action)

    # Open action
    open_action = QAction("Open...", display)
    open_action.setShortcut(QKeySequence("Ctrl+O"))
    open_action.triggered.connect(lambda: action_open(display, text_widget))
    files.addAction(open_action)

    files.addSeparator()

    # Save action
    save_action = QAction("Save", display)
    save_action.setShortcut(QKeySequence("Ctrl+S"))
    save_action.triggered.connect(lambda: action_save(display, text_widget))
    files.addAction(save_action)

    # Save As action
    save_as_action = QAction("Save As...", display)
    save_as_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
    save_as_action.triggered.connect(lambda: action_save_as(display, text_widget))
    files.addAction(save_as_action)

    files.addSeparator()

    # Exit action
    exit_action = QAction("Exit", display)
    exit_action.setShortcut(QKeySequence("Ctrl+Q"))
    exit_action.triggered.connect(lambda: action_exit(display, text_widget))
    files.addAction(exit_action)

    return files
