# The-text-Analyzer

This is a Flask-based Web Application that will convert a paragraph you provide from your favorite book into individual sentences along with their sentimental scores (where scores near 0 are negative and moving towards 1 they are positive).
After that, the application will provide you the sentiment of the whole paragraph and will also suggest you a topic for that paragraph.
The application provides all the information by redirecting to route "/success".

model.py : It contains the python script model of a model that is trained to predict sentiments of sentences.

app.py : It contains the flask web application python script.

index.html : An HTML file containing the skeleton of the web application.

The_Text_Analyzer.ipynb : This is the colab notebook where different ML algorithms are applied and tested over the data to get the best model for predicting sentiments of        
                          sentences. Also, all the models and algo's for segmentation of paragraph and topic suggestion have been trained and designed here.

                           

