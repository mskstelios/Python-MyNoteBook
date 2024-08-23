from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction, QMenu, QInputDialog, QMessageBox

def action_undo(text_widget):
    text_widget.undo()

def action_redo(text_widget):
    text_widget.redo()

def action_cut(text_widget):
    text_widget.cut()

def action_copy(text_widget):
    text_widget.copy()

def action_paste(text_widget):
    text_widget.paste()

def action_select_all(text_widget):
    text_widget.selectAll()

def action_find(text_widget):
    search_term, ok = QInputDialog.getText(text_widget, "Find", "Find:")
    if ok and search_term:
        cursor = text_widget.textCursor()
        # Search for the term
        cursor = text_widget.document().find(search_term, cursor)
        if not cursor.isNull():
            text_widget.setTextCursor(cursor)
            text_widget.setFocus()
        else:
            QMessageBox.information(text_widget, "Find", "Text not found.")

def action_find_and_replace(text_widget):
    search_term, ok = QInputDialog.getText(text_widget, "Find and Replace", "Find:")
    if ok and search_term:
        replace_term, ok = QInputDialog.getText(text_widget, "Find and Replace", "Replace with:")
        if ok:
            cursor = text_widget.textCursor()
            found_any = False
            while True:
                cursor = text_widget.document().find(search_term, cursor)
                if cursor.isNull():
                    break
                found_any = True
                cursor.insertText(replace_term)
                cursor.movePosition(cursor.StartOfBlock)
            if not found_any:
                QMessageBox.information(text_widget, "Find and Replace", "Text not found.")


def create_edit_menu(display, text_widget):
    edit = QMenu("&Edit", display)

    undo_action = QAction("Undo", display)
    undo_action.setShortcut(QKeySequence("Ctrl+Z"))
    undo_action.triggered.connect(lambda: action_undo(text_widget))
    edit.addAction(undo_action)

    redo_action = QAction("Redo", display)
    redo_action.setShortcut(QKeySequence("Ctrl+Y"))
    redo_action.triggered.connect(lambda: action_redo(text_widget))
    edit.addAction(redo_action)

    edit.addSeparator()

    cut_action = QAction("Cut", display)
    cut_action.setShortcut(QKeySequence("Ctrl+X"))
    cut_action.triggered.connect(lambda: action_cut(text_widget))
    edit.addAction(cut_action)

    copy_action = QAction("Copy", display)
    copy_action.setShortcut(QKeySequence("Ctrl+C"))
    copy_action.triggered.connect(lambda: action_copy(text_widget))
    edit.addAction(copy_action)

    paste_action = QAction("Paste", display)
    paste_action.setShortcut(QKeySequence("Ctrl+V"))
    paste_action.triggered.connect(lambda: action_paste(text_widget))
    edit.addAction(paste_action)

    select_all_action = QAction("Select All", display)
    select_all_action.setShortcut(QKeySequence("Ctrl+A"))
    select_all_action.triggered.connect(lambda: action_select_all(text_widget))
    edit.addAction(select_all_action)

    edit.addSeparator()

    find_action = QAction("Find...", display)
    find_action.setShortcut(QKeySequence("Ctrl+F"))
    find_action.triggered.connect(lambda: action_find(text_widget))
    edit.addAction(find_action)

    find_and_replace_action = QAction("Find and Replace...", display)
    find_and_replace_action.setShortcut(QKeySequence("Ctrl+H"))
    find_and_replace_action.triggered.connect(lambda: action_find_and_replace(text_widget))
    edit.addAction(find_and_replace_action)


    return edit
