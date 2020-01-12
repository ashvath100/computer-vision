# -*- coding: utf-8 -*-
"""Data_YOLO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kLvICOo3H_u3Vw7yEyi_tqDCzGNg4Q5C

# Data Cleaning for YOLO v3

# Mounting the Google Drive
"""

from google.colab import drive

drive.mount('/content/drive')

"""# Cleaning the CSV"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

df = pd.read_csv(r'/content/drive/My Drive/VAUV Dataset/json_csv/fixed_final_data_cleaned.csv')
image_dir = r'/content/drive/My Drive/VAUV Dataset/Clipped Images/2018_VID_1_3'

df.head(2)

def get_max_min(df):
    ''' Note that this works only for the cases where we have all four cordinates'''
    df['x_min'] = -1.
    df['y_min'] = -1.
    df['x_max'] = -1.
    df['y_max'] = -1.

    for i in range(len(df)):
        df['x_min'][i] = min(df['x1'][i], df['x2'][i], df['x3'][i], df['x4'][i]).astype('float32')
        df['x_max'][i] = max(df['x1'][i], df['x2'][i], df['x3'][i], df['x4'][i]).astype('float32')

        df['y_min'][i] = min(df['y1'][i], df['y2'][i], df['y3'][i], df['y4'][i]).astype('float32')
        df['y_max'][i] = max(df['y1'][i], df['y2'][i], df['y3'][i], df['y4'][i]).astype('float32')

    return df

def fill_class_id(df):
    df['class_id'] = 1
    return(df)

def check_dims(df):
    for i in ['1', '2', '3', '4']:
        print(np.max(df[f'x{i}']), end=' ')
        print(np.max(df[f'y{i}']), end=' ')
        print()

check_dims(df)

def show_points(img_path, ):
    # img = cv2.imread(img_path)
    # img = cv2.circle(img, (int(df['x1']), int(df['y1'])), 2, (0,0,255), 8)
    # plt.imshow(img[...,::-1])

    # need to work with this

# def complete_gate(df):
#     for i in range(len(df)):
#         if(df['x1'] == 0 and df['x2'] == 0 and df['y1'] == 0 and df['x2'] == 0 and df['y2'] == 0):
            
            # Means gate is incomplete

def resize_column(df, column_list, img_shape=(720, 1280), resize_shape=(416, 416)):

    #  Need to work on this. Naive division does not work.
    x_div = img_shape[1]
    y_div = img_shape[0]

    target_x = resize_shape[1]
    target_y = resize_shape[0]

    for cl in column_list:
        if(cl[0] == 'x'):
            new_column = cl + '_resized'
            df[new_column] = 1.
            
            for i, val in enumerate(df[cl]):
                val = (val / x_div) * target_x
                df[new_column][i] = val

        elif(cl[0] == 'y'):
            new_column = cl + '_resized'
            df[new_column] = 1.
            for i, val in enumerate(df[cl]):
                val = (val / y_div) * target_y
                df[new_column][i] = val

    return df

df = get_max_min(df)

df = fill_class_id(df)

column_resized = ['x1', 'x2', 'x3', 'x4', 'y1', 'y2', 'y3', 'y4', 'x_min', 'y_min', 'x_max', 'y_max']
df = resize_column(df, column_resized)

df.head(3)

"""# Testing an Image with cordinates

Originally
"""

img = cv2.imread('/content/2018_VID_1_3_frame325.jpg')
print(img.shape)

img = cv2.circle(img, (293, 427), 5, (0,0,255), 8)

plt.imshow(img[...,::-1])

img = cv2.circle(img, (290, 106), 5, (0,0,255), 8)

plt.imshow(img[...,::-1])

img = cv2.circle(img, (590,	125), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])

img = cv2.circle(img, (581, 414), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])

"""After resizing

1 2 Case
"""

img = cv2.imread('/content/2018_VID_1_3_frame854.jpg')
print(img.shape)

img = cv2.circle(img, (290, 636), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

"""Another 4 cord case"""

img = cv2.imread('/content/2018_VID_1_3_frame373.jpg')
print(img.shape)
img = cv2.circle(img, (333, 469), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (331, 130), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

# 650 	149.714 	633.143 	454.857 	
img = cv2.circle(img, (650, 149), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (633, 454), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

"""Vauge Case

733.779 	716.998 	803.659 	39.890 	1220.526 	184.468 	1109.683 	704.950
"""

img = cv2.imread('/content/2018_VID_1_3_frame116.jpg')
print(img.shape)
img = cv2.circle(img, (733, 716), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (803, 39), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (1220, 184), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (1109, 704), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

"""This is confirmed 1-2, 1-2 case checked from labelbox"""

img = cv2.imread('/content/2018_VID_1_3_frame867.jpg')
print(img.shape)

for i in range(len(df)):
    if(df['External ID'][i] == '2018_VID_1_3_frame867.jpg'):
        print(df['x1'][i], df['y1'][i], df['x2'][i], df['y2'][i], df['x3'][i], df['y3'][i], df['x4'][i], df['y4'][i])

img = cv2.circle(img, (37, 556), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (6, 424), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (266, 178), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (286, 642), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()



"""# Scaled Image testing

## 1234 Case
"""

img = cv2.imread('/content/2018_VID_1_3_frame373.jpg')
print(img.shape)

img = cv2.circle(img, (333, 469), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])

img = cv2.circle(img, (331 , 130), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])

# 650.286 	149.714
img = cv2.circle(img, (650, 149), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])

img = cv2.circle(img, (633, 454), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
# 633.143 	454.857

img_resized = cv2.resize(img, (416, 416))
plt.imshow(img_resized[...,::-1])

# 108.457050 	271.390311 	
img_resized = cv2.circle(img_resized, (108, 271), 5, (0,255,0), 8)
plt.imshow(img_resized[...,::-1])

# 107.714425 	86.501422 	
img_resized = cv2.circle(img_resized, (107, 75), 5, (0,255,0), 8)
plt.imshow(img_resized[...,::-1])

img_resized = cv2.circle(img_resized, (211, 86), 5, (0,255,0), 8)
plt.imshow(img_resized[...,::-1])

img_resized = cv2.circle(img_resized, (205,262), 5, (0,255,0), 8)
plt.imshow(img_resized[...,::-1])

img_resized = cv2.circle(img_resized, (107, 75), 5, (255,0,255), 8)
plt.imshow(img_resized[...,::-1])

img_resized = cv2.circle(img_resized, (211, 271), 5, (255,0,255), 8)
plt.imshow(img_resized[...,::-1])

"""Stuff seems to be fine.
- The minor mistakes in cordinates are due to taking int() 
- That is opencv problem
"""



"""## 12 Case Before Gate Completion"""

img = cv2.imread('/content/2018_VID_1_3_frame854.jpg')
plt.imshow(img[...,::-1])
plt.show()

# 290.056 	636.872 	247.151 	190.391 	
img = cv2.circle(img, (290, 636), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])

img = cv2.circle(img, (247, 190), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])

img_resized = cv2.resize(img, (416, 416))
plt.imshow(img_resized[...,::-1])

img_resized = cv2.circle(img_resized, (94, 367), 5, (0,255,255), 8)
plt.imshow(img_resized[...,::-1])

img_resized = cv2.circle(img_resized, (80, 110), 5, (0,255,255), 8)
plt.imshow(img_resized[...,::-1])

"""# 12 12 Case"""

img = cv2.imread('/content/2018_VID_1_3_frame867.jpg')
print(img.shape)

for i in range(len(df)):
    if(df['External ID'][i] == '2018_VID_1_3_frame867.jpg'):
        print(df['x1'][i], df['y1'][i], df['x2'][i], df['y2'][i], df['x3'][i], df['y3'][i], df['x4'][i], df['y4'][i])

        print(df['x1_resized'][i], df['y1_resized'][i], df['x2_resized'][i], df['y2_resized'][i], df['x3_resized'][i], 
        df['y3_resized'][i], df['x4_resized'][i], df['y4_resized'][i])
        
        print(df['x_max_resized'][i], df['x_min_resized'][i])

img = cv2.circle(img, (37, 556), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (6, 424), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (266, 178), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img, (286, 642), 5, (0,0,255), 8)
plt.imshow(img[...,::-1])
plt.show()

"""12.25705 321.57435555555554 2.228525 244.9777777777778 86.54294999999999 103.00968888888887 93.22852500000002 371.09857777777773"""

img_resized = cv2.resize(img, (416, 416))

img = cv2.circle(img_resized, (12, 321), 5, (0,255,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img_resized, (2, 224), 5, (0,255,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img_resized, (86, 103), 5, (0,255,255), 8)
plt.imshow(img[...,::-1])
plt.show()

img = cv2.circle(img_resized, (93, 371), 5, (0,255,255), 8)
plt.imshow(img[...,::-1])
plt.show()