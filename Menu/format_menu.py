from PyQt5.QtGui import QKeySequence,  QTextCharFormat
from PyQt5.QtWidgets import QAction, QMenu, QFontDialog, QColorDialog


def action_font(display, text_widget):
    font, ok = QFontDialog.getFont(text_widget.font(), display)
    if ok:
        # Create a QTextCharFormat object with the new font
        char_format = QTextCharFormat()
        char_format.setFont(font)

        # Apply the format to the entire text in the QTextEdit
        cursor = text_widget.textCursor()
        cursor.select(cursor.Document)
        cursor.setCharFormat(char_format)


def action_color(display, text_widget):
    color = QColorDialog.getColor(text_widget.textColor(), display)
    if color.isValid():
        text_widget.setTextColor(color)

def action_highlight_color(display, text_widget):
    color = QColorDialog.getColor(text_widget.currentCharFormat().foreground().color(), display)
    if color.isValid():
        char_format = QTextCharFormat()
        char_format.setFont(text_widget.font())
        char_format.setForeground(color)
        text_widget.textCursor().setCharFormat(char_format)

def action_indent_code(display, text_widget):
    text_widget.textCursor().insertText("    ")

def action_outdent_code(display, text_widget):
    text_widget.textCursor().removeSelectedText()

def action_line_spacing(display, text_widget):
    text_widget.textCursor().insertText("\n")

def action_paragraph_spacing(display, text_widget):
    text_widget.textCursor().insertText("\n\n")

def create_format_menu(display, text_widget):
    format_menu = QMenu("&Format", display)

    font_action = QAction("Font...", display)
    font_action.setShortcut(QKeySequence("Ctrl+T"))
    font_action.triggered.connect(lambda: action_font(display, text_widget))
    format_menu.addAction(font_action)

    text_color_action = QAction("Text Color...", display)
    text_color_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
    text_color_action.triggered.connect(lambda: action_color(display, text_widget))
    format_menu.addAction(text_color_action)

    highlight_color_action = QAction("Highlight Color...", display)
    highlight_color_action.setShortcut(QKeySequence("Ctrl+Shift+H"))
    highlight_color_action.triggered.connect(lambda: action_highlight_color(display, text_widget))
    format_menu.addAction(highlight_color_action)

    format_menu.addSeparator()

    indent_code_action = QAction("Indent Code", display)
    indent_code_action.setShortcut(QKeySequence("Ctrl+Alt+I"))
    indent_code_action.triggered.connect(lambda: action_indent_code(display, text_widget))
    format_menu.addAction(indent_code_action)

    outdent_code_action = QAction("Outdent Code", display)
    outdent_code_action.setShortcut(QKeySequence("Ctrl+Alt+O"))
    outdent_code_action.triggered.connect(lambda: action_outdent_code(display, text_widget))
    format_menu.addAction(outdent_code_action)

    format_menu.addSeparator()

    line_spacing_action = QAction("Line Spacing...", display)
    line_spacing_action.setShortcut(QKeySequence("Ctrl+Shift+L"))
    line_spacing_action.triggered.connect(lambda: action_line_spacing(display, text_widget))
    format_menu.addAction(line_spacing_action)

    paragraph_spacing_action = QAction("Paragraph Spacing...", display)
    paragraph_spacing_action.setShortcut(QKeySequence("Ctrl+Shift+P"))
    paragraph_spacing_action.triggered.connect(lambda: action_paragraph_spacing(display, text_widget))
    format_menu.addAction(paragraph_spacing_action)

    return format_menu
