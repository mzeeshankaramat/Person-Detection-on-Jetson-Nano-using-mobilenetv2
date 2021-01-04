# Intruder-Detection-using-Jetson-Nano
## Author: M.Zeeshan Karamat
On laptop:
Intruder detection Mobilenetv2 notebook is used for training. I have used pretrained mobilenetv2 model. 
You can use any other model available in torch pakage
Other file which is test.ipynb is used for testing on random images to test accuracy and inference


On Jetson
Same files can be used on Jetson device
Training using Jetson will be slow



## Data collection:
I collected public datasets from different websites and online competitions on Kaggle. I downloaded video footages to make dataset. 

## Extracting frames from video:
As neural network is trained using images so I had to take snapshots/frames from these footages. I used OpenCV to extract frames and save from videos. It extracts frame every 2 seconds.Taking snapshot from video has been added to extract frames from video files.In case you want to generate your own data. Use this files to generate image dataset
  
## Data labelling and cleaning:
After I extracted data, I labelled data for every image that contained person in it while no person for others. I cleaned data to remove redundant data because that affects the accuracy of model.

## Image Processing:
Neural networks has great hunger for data. For good accuracy large amount of data is required. I preprocessed data by applying different transformation like rotation, scaling, resizing and normalizing
 
## Transfer Learning:
To improve accuracy I used pretrained Mobilenetv2 model. This model is already trained on ImageNet dataset which contain millions of images. I replaced last 2 layers of model with my layers and trained the model on my data. 

## Results:
After training for 40 epochs I got an accuracy of 96% which is quite good given that I had very less data. I tested the model on a footage using OpenCV. 



