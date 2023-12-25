from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import test
# from transformers import pipeline

import pickle
# CUDA_LAUNCH_BLOCKING=1 python[app.py]

# load the model from disk
# pipe = pipeline("text-classification", model=r"E:\My Data\Graduation project work\.ipynb_checkpoints\Arabert_model", device=0, return_all_scores=True)
    
filename = 'model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pickle','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/home.html')
def english():
	return render_template('home.html')


@app.route('/homear.html')
def arabic():
	return render_template('homear.html')



@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
	return render_template('result.html',prediction = my_prediction)




@app.route('/predictAr',methods=['POST'])
def predictAr():
	if request.method == 'POST':
		message = request.form['message']
		print(type(message))
		
		# results =pipe(message)
		results = test.test(message)
		fresults=(round(results[0][0]['score'],4),round(results[0][1]['score'],4))
		#round(results[0][0]['score'],4),round(results[0][1]['score'],4)
	return render_template('Ar_result.html', prediction = fresults)	



if __name__ == '__main__':
	app.run(debug=True)