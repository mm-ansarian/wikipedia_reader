"""
This module defines the user interface for the Wikipedia Reader application using PyQt6.
"""


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QShortcut, QKeySequence
from bs4 import BeautifulSoup as soup
import requests
import sys
import os


class UiPage(object):
    """
    This class setups every widgets and visible things in the main window such as buttons,
    text boxes, text browsers, etc. 
    """
    def setup_ui(self, main_window: object) -> None:
        _translate = QtCore.QCoreApplication.translate

        # Set the font and size of texts.
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setItalic(True)

        # Setup the "main window".
        main_window.setObjectName("mainWindow")
        main_window.setFixedSize(QtCore.QSize(800, 450))
        main_window.setFont(font)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        if hasattr(sys, "_MEIPASS"):
            icon_path = os.path.join(sys._MEIPASS, "icon.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        main_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=main_window)
        self.centralwidget.setObjectName("centralwidget")

        # Setup the "tab".
        self.tab = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(0, 0, 820, 470))
        self.tab.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tab.setToolTip("")
        self.tab.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tab.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tab.setTabBarAutoHide(False)
        self.tab.setObjectName("tab")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")

        # Setup the "frame" of the "main tab".
        self.frame = QtWidgets.QFrame(parent=self.main_tab)
        self.frame.setGeometry(QtCore.QRect(0, 10, 820, 470))
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        
        # Setup the "url text box" to get the url.
        self.url_text_box = QtWidgets.QLineEdit(parent=self.frame)
        self.url_text_box.setGeometry(QtCore.QRect(5, 0, 220, 40))
        self.url_text_box.setInputMask("")
        self.url_text_box.setText("")
        self.url_text_box.setMaxLength(700)
        self.url_text_box.setFrame(True)
        self.url_text_box.setObjectName("urlInput")
        self.url_text_box.setToolTip(_translate("mainWindow", "URL"))
        self.url_text_box.setPlaceholderText(_translate("mainWindow", "URL"))
        
        # Setup the "search in page" button to start searching in the page.
        self.search_in_page_button = QtWidgets.QPushButton(parent=self.frame)
        self.search_in_page_button.setGeometry(QtCore.QRect(40, 80, 150, 45))
        self.search_in_page_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        if hasattr(sys, "_MEIPASS"):
            icon_path = os.path.join(sys._MEIPASS, "icons/Search.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "icons", "Search.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_in_page_button.setIcon(icon)
        self.search_in_page_button.setObjectName("searchInPageBtn")
        self.search_in_page_button.setToolTip(_translate("mainWindow", "Search in page (Enter)"))
        self.search_in_page_button.setText(_translate("mainWindow", " Search in page"))
        self.search_in_page_button.setShortcut(_translate("mainWindow", "Return"))
        
        # Setup the "clear output button" to clear the output.
        self.clear_output_button = QtWidgets.QPushButton(parent=self.frame)
        self.clear_output_button.setEnabled(False)
        self.clear_output_button.setGeometry(QtCore.QRect(40, 160, 150, 45))
        self.clear_output_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clear_output_button.setAutoFillBackground(False)
        if hasattr(sys, "_MEIPASS"):
            icon_path = os.path.join(sys._MEIPASS, "icons/Trash bin.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "icons", "Trash bin.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.clear_output_button.setIcon(icon)
        self.clear_output_button.setFlat(False)
        self.clear_output_button.setObjectName("clearOutputBtn")
        self.clear_output_button.setToolTip(_translate("mainWindow", "Clear output(F10)"))
        self.clear_output_button.setText(_translate("mainWindow", "Clear output"))
        self.clear_output_button.setShortcut(_translate("mainWindow", "F10"))
        
        # Setup the "result text browser" to show the headers of the page.
        self.results_text_browser = QtWidgets.QTextBrowser(parent=self.frame)
        self.results_text_browser.setGeometry(QtCore.QRect(235, 0, 555, 205))
        self.results_text_browser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.results_text_browser.setTabChangesFocus(False)
        self.results_text_browser.setDocumentTitle("")
        self.results_text_browser.setObjectName("results")
        self.results_text_browser.setPlaceholderText(_translate("mainWindow", "Page headers"))
        
        # Setup the "status text browser" to show the operations.
        self.status_text_browser = QtWidgets.QTextBrowser(parent=self.frame)
        self.status_text_browser.setGeometry(QtCore.QRect(10, 215, 780, 185))
        self.status_text_browser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.status_text_browser.setObjectName("status")
        self.status_text_browser.setPlaceholderText(_translate("mainWindow", "Status"))
        
        # Setup the "settings tab".
        self.tab.addTab(self.main_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")

        # Setup the frame of the "settings tab".
        self.frame2 = QtWidgets.QFrame(parent=self.settings_tab)
        self.frame2.setGeometry(QtCore.QRect(0, 10, 820, 470))
        self.frame2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame2.setObjectName("frame_2")
        
        # Setup the "theme label".
        self.theme_label = QtWidgets.QLabel(parent=self.frame2)
        self.theme_label.setGeometry(QtCore.QRect(5, 0, 230, 50))
        self.theme_label.setObjectName("themeLabel")
        self.theme_label.setText(_translate("mainWindow", "Theme:"))
        
        # Setup the "theme combo box".
        self.theme_combo_box = QtWidgets.QComboBox(parent=self.frame2)
        self.theme_combo_box.setGeometry(QtCore.QRect(100, 5, 200, 40))
        self.theme_combo_box.setObjectName("themeComboBox")
        self.theme_combo_box.addItem("")
        self.theme_combo_box.setToolTip(_translate("mainWindow", "Current theme"))
        self.theme_combo_box.setItemText(0, _translate("mainWindow", "Light"))

        # Call some required functions and methods to prepare the program to run.
        self.setup_signals()
        self.setup_shortcuts()
        self.tab.addTab(self.settings_tab, "")
        main_window.setCentralWidget(self.centralwidget)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.tab, self.url_text_box)
        main_window.setTabOrder(self.url_text_box, self.search_in_page_button)
        main_window.setTabOrder(self.search_in_page_button, self.results_text_browser)
        main_window.setTabOrder(self.results_text_browser, self.clear_output_button)
        main_window.setTabOrder(self.clear_output_button, self.status_text_browser)
        main_window.setTabOrder(self.status_text_browser, self.theme_combo_box)
        main_window.setWindowTitle(_translate("mainWindow", "Wikipedia Reader"))
        self.tab.setTabText(self.tab.indexOf(self.main_tab), _translate("mainWindow", "Main tab"))
        self.tab.setTabText(self.tab.indexOf(self.settings_tab), _translate("mainWindow", "Settings"))
        self.url_text_box.setFocus()

    # A method to setup the signals of some widgets.
    def setup_signals(self) -> None:
        self.search_in_page_button.clicked.connect(
            lambda: UiReactions.search_in_page_reaction(self, url=self.url_text_box.text())
        )
        self.clear_output_button.clicked.connect(
            lambda: UiReactions.clear_output_reaction(self)
        )

    # A method to focus on the next tab.
    def next_tab_shortcut(self) -> None:
        if self.tab.currentIndex() == 0:
            self.tab.setCurrentIndex(1)
        elif self.tab.currentIndex() == 1:
            self.tab.setCurrentIndex(0)

    # A method to focus on the previous tab.
    def previous_tab_shortcut(self) -> None:
        if self.tab.currentIndex() == 1:
            self.tab.setCurrentIndex(0)
        elif self.tab.currentIndex() == 0:
            self.tab.setCurrentIndex(1)

    # A method to setup the shortcut keys of some widgets.
    def setup_shortcuts(self) -> None:
        tab_shortcut1 = QShortcut(QKeySequence("Alt+Right"), self.tab)
        tab_shortcut1.activated.connect(self.next_tab_shortcut)

        tab_shortcut2 = QShortcut(QKeySequence("Alt+Left"), self.tab)
        tab_shortcut2.activated.connect(self.previous_tab_shortcut)


class UiReactions(UiPage):
    """This class setups the reactions of each widget in the window.
    In fact, this class specifies that what should happen if the user took an action
    on the window.
    """
    # Setup the widgets from the "UiPage" class.
    def setup_ui(self, main_window: object) -> None:
        return super().setup_ui(main_window)
    
    # A method to find the headers of a page and show them.
    def search_in_page_reaction(self, url: str) -> None:
        self.results_text_browser.clear()
        self.results_text_browser.setPlaceholderText('Page headers')
        self.status_text_browser.clear()
        self.status_text_browser.setPlaceholderText('Status')
        try:
            response = requests.get(url, timeout=7)
        except requests.exceptions.ConnectTimeout:
            self.status_text_browser.append("!!!  This site can’t be reached  !!!")
        except requests.exceptions.ConnectionError:
            self.status_text_browser.append(
                "!!!  Connection failed, Check WiFi connection and try again  !!!"
            )
        except requests.exceptions.MissingSchema:
            self.status_text_browser.append("!!!  Invalid URL  !!!")
        else:
            if response.status_code == 200:
                # TODO: Improve the performance of "status_text_browser" using multi threading.
                self.status_text_browser.append("Searching...")
                source = soup(response.text, 'html.parser')
                if source.find('h1') is not None:
                    self.results_text_browser.setPlainText(
                        f"{source.find("h1").text}"
                    )
                    exists = False
                    for counter, heading in enumerate(source.find_all('h2')):
                        if heading.text == 'فهرست':
                            exists = True
                            continue
                        else:
                            num = counter if exists else counter + 1
                            self.results_text_browser.append(
                                f"\n    {heading.text[:heading.text.index("[ویرایش]")]} .{num}"
                            ) if '[ویرایش]' in heading.text else (
                                self.results_text_browser.append(
                                    f"\n    {num}. {heading.text}"
                                )
                            )
                            
                    self.status_text_browser.append("\nFinished successfully.")
                    
                else:
                    self.status_text_browser.append("\nNo result found from the page.")
            else:
                self.status_text_browser.append(
                    f"""\n!!!  There is a problem. Status Code:
                    {response.status_code} ,  {response.reason}  !!!"""
                )
        self.results_text_browser.moveCursor(QtGui.QTextCursor.MoveOperation.Start)
        self.status_text_browser.moveCursor(QtGui.QTextCursor.MoveOperation.Start)
        self.url_text_box.setCursorPosition(0)
        self.clear_output_button.setEnabled(True)
 
    # A method to clear everything(inputs and outputs) from the ui page.
    def clear_output_reaction(self) -> None:
        self.results_text_browser.clear()
        self.results_text_browser.setPlaceholderText('Page headers')
        self.status_text_browser.clear()
        self.status_text_browser.setPlaceholderText('Status')
        self.url_text_box.clear()
        self.url_text_box.setPlaceholderText("URL")
        self.clear_output_button.setEnabled(False)
        self.url_text_box.setFocus()
