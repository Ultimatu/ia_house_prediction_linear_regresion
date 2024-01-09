from flask import Flask, render_template, send_file
import secrets
from func.form_conf import PredictionForm
from func.generate_pdf import generate_pdf
from func.model import predict

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    """Page du formulaire de prédiction"""
    form = PredictionForm()
    if form.validate_on_submit():
        return render_template('result.html', form=form, prediction=predict(form))

    return render_template('form.html', form=form)

@app.route('/export/<int:year>/<float:surface>/<int:observations>/<float:prediction>', methods=['GET'])
def export(year, surface, observations, prediction):
    """Exportation des résultats au format PDF"""
    pdf_filename = f'result_export_{year}_{surface}_{observations}.pdf'
    file_path = generate_pdf(pdf_filename, year, surface, observations, prediction)
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
