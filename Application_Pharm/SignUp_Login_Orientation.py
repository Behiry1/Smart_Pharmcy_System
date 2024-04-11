from PySide6.QtWidgets import QVBoxLayout, QWidget

def center_widget_2(main_window, widget):
    # Create a QVBoxLayout to center the widget
    layout = QVBoxLayout()
    layout.addWidget(widget)

    # Create a wrapper widget to hold the layout
    wrapper = QWidget()
    wrapper.setLayout(layout)

    # Set the central widget of the main window to the wrapper
    main_window.setCentralWidget(wrapper)
