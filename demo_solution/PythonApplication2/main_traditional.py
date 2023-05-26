# Import PyQt5 and other modules
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import logic_traditional

# Create a class for the main window of the prototype
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Green AI Framework Prototype (Traditional Way)")
        self.resize(600, 400)
        # Create and add widgets to the layout
        self.create_widgets()
        self.add_widgets_to_layout()
        # Set the layout to the window
        self.setLayout(self.layout)

    # Define a function for creating widgets
    def create_widgets(self):
        # Create a label for the title
        self.title_label = QLabel("Green AI Framework Prototype (Traditional Way)")
        # Set the font and alignment of the title label
        self.title_label.setFont(QFont("Arial", 24))
        self.title_label.setAlignment(Qt.AlignCenter)
        # Create a label for the description
        self.description_label = QLabel("This prototype allows you to train and deploy AI models locally using traditional way.")
        # Set the font and alignment of the description label
        self.description_label.setFont(QFont("Arial", 16))
        self.description_label.setAlignment(Qt.AlignCenter)
        # Create a label for the task selection
        self.task_label = QLabel("Select a task:")
        # Set the font of the task label
        self.task_label.setFont(QFont("Arial", 14))
        # Create a combo box for the task selection
        self.task_combo = QComboBox()
        # Add some sample tasks to the combo box
        self.task_combo.addItems(["Digit Recognition", "Image Classification", "Sentiment Analysis"])
        # Set the font and size of the combo box
        self.task_combo.setFont(QFont("Arial", 14))
        self.task_combo.setFixedSize(200, 40)
        # Create a button for training and deploying the AI model locally using traditional way
        self.train_deploy_button = QPushButton("Train and Deploy Locally")
        # Connect the button to the logic function
        self.train_deploy_button.clicked.connect(self.train_deploy)
        # Set the font and size of the button
        self.train_deploy_button.setFont(QFont("Arial", 14))
        self.train_deploy_button.setFixedSize(200, 40)
        
    # Define a function for adding widgets to the layout
    def add_widgets_to_layout(self):
         # Create a vertical layout for the title and description labels
         self.title_layout = QVBoxLayout()
         # Add the title and description labels to the title layout
         self.title_layout.addWidget(self.title_label)
         self.title_layout.addWidget(self.description_label)
         # Create a horizontal layout for the task widget
         self.task_layout = QHBoxLayout()
         # Add the task widget to the task layout
         self.task_layout.addWidget(self.task_label)
         self.task_layout.addWidget(self.task_combo)
         # Create a horizontal layout for the train deploy button 
         self.train_deploy_layout = QHBoxLayout()
         # Add the train deploy button to the train deploy layout 
         self.train_deploy_layout.addWidget(self.train_deploy_button) 
         # Create a vertical layout for the main window 
         self.layout = QVBoxLayout() 
         # Add the title layout, the task layout, and the train deploy layout to the main layout 
         self.layout.addLayout(self.title_layout) 
         self.layout.addLayout(self.task_layout) 
         self.layout.addLayout(self.train_deploy_layout)

        # Define a function for training and deploying locally using traditional way 
    def train_deploy(self): 
       # Get the selected task from the combo box 
       task = self.task_combo.currentText() 
       # Call the logic function with our solution flag set to False 
       logic_traditional.train_deploy(task)

# Create an application instance 
app = QApplication([]) 
# Create a main window instance 
window = MainWindow() 
# Show the main window 
window.show() 
# Run the application loop 
app.exec_()

       # Get t