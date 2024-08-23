from PyQt5.QtGui import QPixmap, QTextCursor, QImage
from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction, QMenu, QMessageBox, QInputDialog, QFileDialog

def action_word_count(display, text_widget):
    words = text_widget.toPlainText().split()
    all_words = text_widget.toPlainText()
    QMessageBox.information(display, "Word Count", f"The text contains (Words: {len(words)} / characters: {len(all_words)}).")

def action_align_left(display, text_widget):
    text_widget.setAlignment(Qt.AlignLeft)

def action_align_center(display, text_widget):
    text_widget.setAlignment(Qt.AlignCenter)

def action_align_right(display, text_widget):
    text_widget.setAlignment(Qt.AlignRight)

def action_align_justify(display, text_widget):
    text_widget.setAlignment(Qt.AlignJustify)

def action_insert_link(display, text_widget):
    url, ok = QInputDialog.getText(display, "Insert Link", "Enter the URL:")
    if ok and url:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        text_widget.insertHtml(f'<a href="{url}">{url}</a>')


def action_insert_image(display, text_widget):
    file_filter = "Image Files (*.png *.jpg *.jpeg *.gif);;All Files (*.*)"
    file_path, _ = QFileDialog.getOpenFileName(display, "Open Image File...", "", file_filter)

    if file_path:
        pixmap = QPixmap(file_path)

        if pixmap.isNull():
            QMessageBox.warning(display, "Insert Image", "Failed to load the image.")
            return

        # Resize the image
        desired_width = 200
        desired_height = 200
        scaled_pixmap = pixmap.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatio)

        cursor = text_widget.textCursor()
        cursor.beginEditBlock()

        # Insert the resized image into the document
        cursor.insertImage(scaled_pixmap.toImage())

        cursor.endEditBlock()

def create_tools_menu(display, text_widget):
    tools = QMenu("&Tools", display)

    # Word Count Action
    word_count_action = QAction("Word Count", display)
    word_count_action.setShortcut(QKeySequence("Ctrl+W"))
    word_count_action.triggered.connect(lambda: action_word_count(display, text_widget))
    tools.addAction(word_count_action)

    tools.addSeparator()

    # Alignment Actions
    align_left_action = QAction("Align Left", display)
    align_left_action.setShortcut(QKeySequence("Ctrl+L"))
    align_left_action.triggered.connect(lambda: action_align_left(display, text_widget))
    tools.addAction(align_left_action)

    align_center_action = QAction("Align Center", display)
    align_center_action.setShortcut(QKeySequence("Ctrl+E"))
    align_center_action.triggered.connect(lambda: action_align_center(display, text_widget))
    tools.addAction(align_center_action)

    align_right_action = QAction("Align Right", display)
    align_right_action.setShortcut(QKeySequence("Ctrl+R"))
    align_right_action.triggered.connect(lambda: action_align_right(display, text_widget))
    tools.addAction(align_right_action)

    align_justify_action = QAction("Justify", display)
    align_justify_action.setShortcut(QKeySequence("Ctrl+J"))
    align_justify_action.triggered.connect(lambda: action_align_justify(display, text_widget))
    tools.addAction(align_justify_action)

    tools.addSeparator()

    # Insert Link Action
    insert_link_action = QAction("Insert Link", display)
    insert_link_action.triggered.connect(lambda: action_insert_link(display, text_widget))
    tools.addAction(insert_link_action)

    # Insert Image Action
    insert_image_action = QAction("Insert Image", display)
    insert_image_action.triggered.connect(lambda: action_insert_image(display, text_widget))
    tools.addAction(insert_image_action)

    return tools
