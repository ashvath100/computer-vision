# -*- coding: utf-8 -*-
"""Modular_Data_Cleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TuNSoT_no-893QbI9RIbIBPwrAOn7Il3
"""

import pandas as pd
import numpy as np
import os
import cv2

def read_csv(PATH):
	df = pd.read_csv(PATH)
	return df

def save_df_to_csv(df, filename):
    try:
        df.to_csv(filename + '.csv')
        print("Data frame saved to csv with name %s "%(filename+'.csv'))
    except exception as e:
        print("Error saving the csv")

######## Test Cases  ########################
# [[{'x': 333.714, 'y': 469.714}, 
# {'x': 331.429, 'y': 130.286}, {'x': 650.286, 'y': 149.714}, {'x': 633.143, 'y': 454.857}]]


# [[{'x': 733.779, 'y': 716.998}, {'x': 803.659, 'y': 39.89},
#   {'x': 1220.526, 'y': 184.468}, {'x': 1109.683, 'y': 704.95}]]

# [[{'x': 153.296, 'y': 341.899}, {'x': 127.821, 'y': 103.24}, {
#     'x': 341.006, 'y': 91.173}, {'x': 358.436, 'y': 311.061}]]

def convert_labels_cordinates(df, column):		
	x_1t = []
	y_1t = []
	x_2t = []
	y_2t = []
	x_3t = []
	y_3t = []
	x_4t = []
	y_4t = []

	labels = df[column]
	label_df = pd.DataFrame()
	label_list = []

	for row in range(len(df)):
	    label = eval(labels[row])
	    if 'objects' in label:
	        object_ = label['objects']
	        gate_count = 0
	        gate_lines = []
	        for obj in object_:
	            obj = eval(str(obj))
	            # print(obj)
	            if (obj["title"] == 'Gate'):
	                gate_count += 1
	                gate_lines.append(obj["line"])
	        
	        if (gate_count == 0):
	            label_list.append("No Gate")
	            x_1t.append(0)
	            y_1t.append(0)
	            x_2t.append(0)
	            y_2t.append(0)
	            x_3t.append(0)
	            y_3t.append(0)
	            x_4t.append(0)
	            y_4t.append(0)

	        # print(gate_lines)
	        else:
	            if(len(gate_lines) > 0):
	                ele_list = gate_lines[0]
	            # print(ele_list)

	                if(len(ele_list) == 2):
	                    x_1t.append(ele_list[0]['x'])
	                    y_1t.append(ele_list[0]['y'])
	                    x_2t.append(ele_list[1]['x'])
	                    y_2t.append(ele_list[1]['y'])

	                    x_3t.append(0)
	                    y_3t.append(0)

	                    x_4t.append(0)
	                    y_4t.append(0)

	                elif(len(ele_list) == 4):
	                    x_1t.append(ele_list[0]['x'])
	                    y_1t.append(ele_list[0]['y'])
	                    
	                    x_2t.append(ele_list[1]['x'])
	                    y_2t.append(ele_list[1]['y'])
	                    
	                    x_3t.append(ele_list[2]['x'])
	                    y_3t.append(ele_list[2]['y'])

	                    x_4t.append(ele_list[3]['x'])
	                    y_4t.append(ele_list[3]['y'])
	                else:
	                    x_1t.append(-1)
	                    y_1t.append(-1)
	                    x_2t.append(-1)
	                    y_2t.append(-1)
	                    x_3t.append(-1)
	                    y_3t.append(-1)
	                    x_4t.append(-1)
	                    y_4t.append(-1)
	                    # print(ele_list)
	        # else:
	        #     label_list.append(gate_lines)

	    else:
	        label_list.append("No Object")
	        x_1t.append(-2)
	        y_1t.append(-2)
	        x_2t.append(-2)
	        y_2t.append(-2)
	        x_3t.append(-2)
	        y_3t.append(-2)
	        x_4t.append(-2)
	        y_4t.append(-2)


	# print(x_1t)
	# print(y_1t)
	# print(x_2t)
	# print(y_2t)
	# print(x_3t)
	# print(y_3t)
	# print(x_4t)
	# print(y_4t)

	# print(len(x_1t))
	# print(len(y_1t))
	# print(len(x_2t))
	# print(len(y_2t))
	# print(len(x_3t))
	# print(len(y_3t))
	# print(len(x_4t))
	# print(len(y_4t))

	# if all the lengths are equal to length of dataframe // Code here for this
	if(len(x_1t) == len(x_2t) == len(x_1t) == len(x_3t) == len(x_4t) == len(y_1t) == len(y_2t) == len(y_3t) == len(y_4t) == len(df)):
		try:
			df['x1'] = np.array(x_1t)
			df['y1'] = np.array(y_1t)

			df['x2'] = np.array(x_2t)
			df['y2'] = np.array(y_2t)

			df['x3'] = np.array(x_3t)
			df['y3'] = np.array(y_3t)

			df['x4'] = np.array(x_4t)
			df['y4'] = np.array(y_4t)

		except exception as e:
			print("Some mistake in converting into dataframe. Please check")

	else:
		print("Some cases are mishandled. Please check the length of lists")

	return df

def show_image_boxes(df, row_range, col, image_dir_path):
    if(row_range[0] >= 0 and row_range[-1] < len(df)):
        start = row_range[0]
        end = row_range[-1]
        images = []

        for i in range(start,end+1):
            image_name = str(df[col][i])      # pick the ith row element from the column
            image_path = os.path.join(image_dir_path, image_name)            

            # print(image_path)

            image_bgr = cv2.imread(image_path, cv2.IMREAD_COLOR)
            image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)


            x1 = float(df['x1'][i])                  # ith row of x1 column
            y1 = float(df['y1'][i])

            x2 = float(df['x2'][i])
            y2 = float(df['y2'][i])

            x3 = float(df['x3'][i])
            y3 = float(df['y3'][i])

            x4 = float(df['x4'][i])
            y4 = float(df['y4'][i] )


            p1=min(x1,x2,x3,x4)                 # top-left pt. is the leftmost of the 4 points
            P2=max(x1,x2,x3,x4)                 # bottom-right pt. is the rightmost of the 4 points
            P1=min(y1,y2,y3,y4)                 # top-left pt. is the uppermost of the 4 points
            P2=max(y1,y2,y3,y4);                # bottom-right pt. is the lowermost of the 4 points

            if(x1>0 and y1>0):
                cv2.rectangle(image, (x1,y1), (x2,y2), (0,0,255), cv2.LINE_AA)
                plt.imshow(image)
                plt.show()
            else:
                print("Empty Image")

    else:
        print("Invalid range of rows")