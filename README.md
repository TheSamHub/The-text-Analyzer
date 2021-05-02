# The-text-Analyzer

This is a Flask based Web Application that will convert a paragraph you provide from your favourite book into individual sentences alongwith their sentimental scores (where scores near 0 are negative and moving towards 1 they are positive).
After that the application will provide you the sentiment of the whole paragraph and will also suggest you a topic for that paragraph.
The application provide all the information by redirecting to route "/success".

model.py : It contains the trained model on which a model is trained to predict sentiments of sentences.\

app.py : It contains the flask web application python script.

index.html : An HTML file containing the skeleton of the web application

