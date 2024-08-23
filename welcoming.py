from PyQt5.QtWidgets import QMessageBox, QCheckBox
from PyQt5.QtCore import QSettings, Qt

def show_initial_message():
    settings = QSettings("MyCompany", "MyNoteBook")
    show_message = settings.value("show_initial_message", True, type=bool)

    if show_message:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Welcome to MyNoteBook!")
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setFixedSize(610, 310)
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #f0f0f0;
                border: none;
            }
            QLabel {
                color: #404040;
            }
            QPushButton {
                background-color: #e0e0e0;
                border: 1px solid #c0c0c0;
                padding: 5px 10px;
            }
            QCheckBox {
                margin-left: 5px;
            }
        """)

        main_text = (
            "<h3>Welcome to MyNoteBook!</h3>"
            "<p>Thank you for choosing MyNoteBook, your new text and code editor. Whether you’re writing text or coding, "
            "MyNoteBook is here to help. Here’s a quick look at what you can do:</p>"
            "<h4>What You Can Do:</h4>"
            "<ul>"
            "<li><b>Edit Text and Code:</b> Write and edit text files or code with syntax highlighting to make things easier.</li>"
            "<li><b>Browse Files:</b> Open and manage files directly from within the app.</li>"
            "<li><b>Use the Calendar:</b> Pick and manage dates with our built-in calendar feature.</li>"
            "<li><b>Explore the Menu:</b> Access all your file operations, editing tools, and more from the menu.</li>"
            "</ul>"
            "<h4>Quick Tips:</h4>"
            "<ul>"
            "<li><b>Saving Your Work:</b> Remember to save your changes through the File menu.</li>"
            "<li><b>Calendar:</b> Utilize the calendar for date selection and management.</li>"
            "</ul>"
        )

        msg_box.setText(main_text)
        dont_show_again_checkbox = QCheckBox("Don’t show this message again")
        msg_box.setCheckBox(dont_show_again_checkbox)
        msg_box.exec_()

        if dont_show_again_checkbox.isChecked():
            settings.setValue("show_initial_message", False)

def reset_welcome_message():
    settings = QSettings("MyCompany", "MyNoteBook")
    settings.setValue("show_initial_message", True)
    QMessageBox.information(None, "Welcome Message Reset", "The welcome message will appear the next time you start MyNoteBook.")
