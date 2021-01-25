import flask
from testing import property_prediction
from visualization import viz
import base64

app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        SMILES = flask.request.form['SMILES']
        Property = flask.request.form['property']
        


        prediction = round(float(property_prediction(SMILES,Property)),3)
        img= viz(SMILES,Property)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        
        return flask.render_template('main.html',
                                     original_input={'SMILES':SMILES,
                                                     'property':Property},
                                     result=prediction,
                                     plot_url= plot_url,
                                     
                                     )
if __name__ == '__main__':
    app.run()