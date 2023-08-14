### ML4AI_COTAIPROJECT2

## DEPENDENCIES

After cloning the Github repository, you can run "pip install -r requirements.txt" to install all of the project's dependencies.

## INSPIRATION

Our program comes from the idea of breaking the language barrier. We want everyone, disabled or not, to be able to speak a globalized language that anyone can understand. Our program aims to popularize the sign language and break these aforementioned barriers.

## DATASET

The files in the GitHub link have already included 624 images (564 for training, 60 for validation) and five labels, including “Hello”, “I Love You”, “Yes”, “No” and “Thank You”.

However, if you would want to create your own dataset and expand your labels, you can follow these steps:

1.  Now you need to access and open the DatasetCollector.py file in the Project_ML4AI_ALT folder.
    You should find lines of code like this:
    IMAGES_PATH = 'images'
    labels = ["Hello", "Thanks", "Yes", "No", "ILoveYou"]
    num_imgs = 110
    This is where you tell the program the amount of labels, as well as the number of images you want to take for each label.
    For example, in this default program, there are 5 labels and I want to take 110 images for each of them. You are free to change the amount of labels and the number of images for each labels to your liking. 2.

2.  Once you are done modifying the DatasetCollecor.py file, you can run the program using the command: "python DatasetCollector.py"
    There should be a new window pop up, with the image captured from your webcam. The program will take an image every 2 seconds (you can also change this in the DatasetCollector.py file), and you can change your pose between them. The program will keep taking images until it is done taking images for all labels.
    To keep track of your current label, there should be a line in terminal telling you which label you are currently taking images for, like this:

        Taking images for Hello
        Taking images for ILoveYou
        Taking images for Yes

3.  After you are done taking the images, the program will close automatically and you should
    find all your taken images in the
    “images” folder. It is recommended to extract all the taken images into a single folder (through copy-pasting, for example) to save time labelling these images later.

4.  When you're done extracting all the images into one folder, execute this command: "labelImg". A new window will pop up that will allow you to draw a box around your hand after you chose the folder that contains all your images.

5.  If labelImg crashes constantly with this message:

        Traceback (most recent call last):
        File "[YOUR DIRECTORY]", line 530, in paintEvent
        p.drawLine(self.prev_point.x(), 0, self.prev_point.x(), self.pixmap.height())
        TypeError: arguments did not match any overloaded call:
        drawLine(self, l: QLineF): argument 1 has unexpected type 'float'
        drawLine(self, x1: int, y1: int, x2: int, y2: int): argument 1 has unexpected type 'float'
        drawLine(self, p1: QPoint, p2: QPoint): argument 1 has unexpected type 'float'
        drawLine(self, p1: Union[QPointF, QPoint], p2: Union[QPointF, QPoint]): argument 1 has unexpected type 'float'
        You need to access the "[YOUR DIRECTORY]" file and replace lines 517-531 with this:

         if self.current is not None and len(self.line) == 2:
             left_top = self.line[0]
             right_bottom = self.line[1]
             rect_width = right_bottom.x() - left_top.x()
             rect_height = right_bottom.y() - left_top.y()
             p.setPen(self.drawing_rect_color)
             brush = QBrush(Qt.BDiagPattern)
             p.setBrush(brush)
             p.drawRect(int(left_top.x()), int(left_top.y()), int(rect_width), int(rect_height))

         if self.drawing() and not self.prev_point.isNull() and not self.out_of_pixmap(self.prev_point):
             p.setPen(QColor(0, 0, 0))
             p.drawLine(int(self.prev_point.x()), 0, int(self.prev_point.x()), int(self.pixmap.height()))
             p.drawLine(0, int(self.prev_point.y()), int(self.pixmap.width()), int(self.prev_point.y()))

6.  In order to prevent overfitting our model, we need some images to validate and test our results, which we will take from the taken images earlier. When you navigate the “labels” folder. You need to take some images in your images folder (just a bit) and their respective .txt document in the “labels” folder and put them into the “val” folder, which can be found in the “Project_ML4AI_ALT” folder. (Remember to put their images in the “images” folder and labels in the “labels” folder)

7.  Now put all your remaining images and labels into the “train” folder. (Remember to format them “images” and “labels” like the “val” folder) If you did all the steps correctly, both the “train” and “val” folder should have two sub-folders named “images” and “labels”, containing their respective images and labels. Finally, cut the “train” and “val” folders (Shortcut is Ctrl+X) into the directory:

    [WHERE YOU COPIED THE PROJECT_ML4AI_ALT FOLDER]\yolov7\data

## MODEL

1. Our program utilizes the top-notch YOLO (You Only Look Once) model to effectively track objects on webcam in real-time. The datasets and labels for the model are entirely customizable, creating accessibility and flexibility to our program. 2. You can download the Yolo model here: https://drive.google.com/file/d/1CdBR-rVhncJKZ1JNuD91bW2nMFDHOs8W/view?usp=sharing and then unzip it into the project's folder.

2. YOLOv7 has multiple models with different capabilities for you to choose. However, if your PC’s specifications are not good enough,it is recommended to train the tiny version of YOLOv7. Head to https://github.com/WongKinYiu/yolov7, navigate until this part like this screenshot and download the weights for the model you want to train.

3. After you have downloaded the weights for the model, remember to paste them at:
   …\Project_ML4AI_ALT\yolov7

Now you need to change the number of classes and their labels. Firstly, you need to access the custom_data.yaml file which can be found at:
…\Project_ML4AI_ALT\yolov7\data\custom_data.yaml

Upon opening the file, you will see these lines of code:

    train: ./data/train

    val: ./data/val

    # number of classes

    nc: 5 _CHANGE HERE_

    # class names

    names: [ 'Hello', 'I Love You', 'No', 'Thanks', 'Yes']
    _CHANGE HERE_

Change the “5” value in “nc” to the number of labels you made
Change the “names” list into the names of your labels in the order like in the “images” and “labels” folder

6. Afterwards, you need to go to this directory:
   …\Project_ML4AI_ALT\yolov7\cfg\training

Here you can see the .yaml files for all the available YOLOv7 models. Depending on the name of the weights model you downloaded earlier, make a copy of that file and name it “yolov7-custom.yaml” (replacing the old one)

For example: If I downloaded the yolov7.pt file earlier, I will make a copy of the yolov7.yaml file and name it yolov7-custom.yaml

    # parameters

    nc: 5 # number of classes _CHANGE HERE_
    depth_multiple: 1.0 # model depth multiple
    width_multiple: 1.0 # layer channel multiple

Open the yolov7-custom.yaml file you created and change the “5” value in “nc” (on line 2) to the number of labels you made.

7. To train your model, execute this command:

    python train.py --batch-size 16 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --weights yolov7-tiny.pt --name yolov7

Note:
For “--batch-size”, it is recommended to use smaller sizes (4 or 8) if you have a PC with worse specifications.
For “--weights”, the code is using the tiny version of YOLOv7, you need to change it to the model which you downloaded before (i.e. yolov7.pt)
YOLOv7 is most efficiently trained on GPUs, but this training command is optimized for CPUs only, if you want training commands that is compatible to GPUs, you can look at links here, here and here.
