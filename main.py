import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

# ======================================================================

# folder with images we want to label (don't forget "/" at the end)
input_folder = './data/images1/'

# labels we want to use
labels = ["label1", "label2", "label3"]

# output csv file
output_file = 'output.csv'

# allowed file extensions
file_extensions = ('.jpg', '.png', '.jpeg')


# ======================================================================
def get_img_paths(dir, extensions=''):
    '''
    :param dir: folder with files
    :param extensions: tuple with file endings. e.g. ('.jpg', '.png')
    :return: list of all filenames
    '''

    filenames = []

    for filename in os.listdir(dir):
        if filename.lower().endswith(extensions):
            filenames.append(dir + filename)

    return filenames


class App(QWidget):
    def __init__(self, labels, img_paths, output_file):
        super().__init__()

        # init UI state
        self.title = 'PyQt5 - Annotation tool'
        self.left = 200
        self.top = 200
        self.width = 960
        self.height = 540

        # state variables
        self.counter = 0
        self.img_paths = img_paths
        self.labels = labels
        self.num_labels = len(labels)
        self.num_images = len(img_paths)

        self.label_buttons = []
        self.appended_labels = {}

        # Initialize image variables
        self.image_raw = None
        self.image = None

        # init UI
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.initButtons()

        # apply styles
        sshFile = "./styles/button.qss"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())

    def initButtons(self):

        # Create "Prev Image" and "Next Image" buttons
        prev_im_btn = QtWidgets.QPushButton(self)
        prev_im_btn.setText("Prev")
        prev_im_btn.move(self.width - 190, 20)
        prev_im_btn.clicked.connect(self.set_prev_image)

        next_im_btn = QtWidgets.QPushButton(self)
        next_im_btn.setText("Next")
        next_im_btn.move(self.width - 100, 20)
        next_im_btn.clicked.connect(self.set_next_image)


        # Create label button
        for i, label in enumerate(self.labels):
            self.label_buttons.append(QtWidgets.QPushButton(self))
            button = self.label_buttons[i]
            button.setText(label)
            # 80 is button width, 10 is spacing between buttons
            # button.move((80 + 10) * i + 300, 20)
            button.move(self.width - 190, (45 + 10) * i + 100)

            # https://stackoverflow.com/questions/35819538/using-lambda-expression-to-connect-slots-in-pyqt
            button.clicked.connect(lambda state, x=label: self.set_label(x))

    def set_label(self, label):
        print(f"Label set as: {label}!")

    def set_next_image(self):
        print("loading next image")

    def set_prev_image(self):
        print("loading prev image")

if __name__ == '__main__':
    # get paths to images
    img_paths = get_img_paths(input_folder, file_extensions)

    app = QApplication(sys.argv)
    ex = App(labels, img_paths, output_file)
    ex.show()
    sys.exit(app.exec_())
