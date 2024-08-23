from PyQt5.QtWidgets import QAction, QMenu, QMessageBox

def show_about_me(display):
    about_message = (
        "<h2>Welcome to MyNoteBook!</h2>"
        "<p>MyNoteBook is a versatile text editor and organizer designed to help you manage your notes, "
        "calendar, and files with ease.</p>"
        "<h3>Key Features:</h3>"
        "<ul>"
        "<li><b>Rich Text Editing:</b> Format your text with various styles and options.</li>"
        "<li><b>File Management:</b> Easily open and manage .txt and .py files from your directory.</li>"
        "<li><b>Integrated Calendar:</b> Keep track of your important dates and events.</li>"
        "</ul>"
        "<p><b>Developed by:</b> Stelios Miskedakis</p>"
        "<h3>Contact Us:</h3>"
        "<p>For more information, support, or feedback, visit our website or contact us at:</p>"
        "<p><b>Website:</b> <a href='http://www.mynotebookapp.com'>www.mynotebookapp.com</a></p>"
        "<p><b>Email:</b> <a href='mailto:support@mynotebookapp.com'>support@mynotebookapp.com</a></p>"
    )

    msg_box = QMessageBox(display)
    msg_box.setWindowTitle("About MyNoteBook")
    msg_box.setText(about_message)
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()



def show_thanks(display):
    thanks_message = (
        "Thank you for using MyNoteBook!\n\n"
        "We sincerely appreciate your support and feedback. Your suggestions help us improve and "
        "make MyNoteBook even better.\n\n"
        "If you have any comments, feature requests, or encounter any issues, please don't hesitate to "
        "reach out to us. We are always here to help!\n\n"
        "Stay tuned for future updates and new features."
    )

    QMessageBox.information(
        display,
        "Thanks for Your Support",
        thanks_message,
        QMessageBox.Ok
    )


def create_about_menu(display):
    about = QMenu("&About", display)

    about_me_action = QAction("About Me", display)
    about_me_action.triggered.connect(lambda: show_about_me(display))
    about.addAction(about_me_action)

    thanks_action = QAction("Thanks", display)
    thanks_action.triggered.connect(lambda: show_thanks(display))
    about.addAction(thanks_action)

    return about
