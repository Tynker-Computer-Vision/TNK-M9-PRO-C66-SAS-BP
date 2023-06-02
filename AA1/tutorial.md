Set the Different Colors for Different Class
============================================

In this activity, you will learn to show the objects of different classes in different colors.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10482737/pasted-from-clipboard.png" width = "480" height = "320">

Follow the given steps to complete this activity:

1. ### Add different colors to the labels

* Open the main.py file.

* Check if the label is a person, then set the color to blue.

    `if (label == "person"):`
    `color = (0, 150, 0)`

* Check if the label is a bench, then set the color to green.

  `if (label == "bench"):`
    `color = (150, 0, 0)`

* Check if the label is a bicycle, then set the color to red.

  `if (label == "bicycle"):`
      `color = (0, 0, 150)`

  `cv2.putText(img,"Goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)`

* Save and run the code to check the output.

