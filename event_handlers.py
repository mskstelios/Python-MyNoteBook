from PyQt5.QtWidgets import QMessageBox, QFileDialog

# Global variable to track the last saved content
last_saved_content = ""

def save_file(text_edit, parent_widget):
    global last_saved_content
    options = QFileDialog.Options()
    file_name, _ = QFileDialog.getSaveFileName(parent_widget, "Save File", "", "Text Files (*.txt);;Python Files (*.py)", options=options)
    if file_name:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text_edit.toPlainText())
        last_saved_content = text_edit.toPlainText()
        return True
    return False

def handle_close_event(event, text_edit, parent_widget):
    global last_saved_content
    current_content = text_edit.toPlainText()

    if current_content != last_saved_content:
        reply = QMessageBox.question(
            parent_widget,
            'Unsaved Changes',
            'You have unsaved changes. Do you want to save before exiting?',
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
            QMessageBox.Yes
        )

        if reply == QMessageBox.Yes:
            if save_file(text_edit, parent_widget):
                event.accept()
            else:
                event.ignore()
        elif reply == QMessageBox.No:
            event.accept()
        else:
            event.ignore()
    else:
        event.accept()
