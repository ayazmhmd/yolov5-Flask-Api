import os
import numpy as np
from flask import Flask, render_template, request
from flask import jsonify
import functions
import random
import torch
import cv2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
app=Flask(__name__,static_folder='static')

@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST': 
	 img = request.files['image']
	 img_path = "static/" + img.filename	
	 img.save(img_path)
	 img=cv2.imread(img_path)
	 img=cv2.resize(img, (416,416))
	 label,bbox,confidence=functions.yolo(img_path)
	 print(label)
	 try:
		 os.remove(img_path)
	 except:
		 pass
	 return jsonify({"label":label},{"bbox":bbox},{"confidence":confidence})
if __name__=='__main__':
    app.run(debug=True)
