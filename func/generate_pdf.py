from reportlab.platypus import Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import os 

def generate_pdf(filename, year, surface, observations, prediction):
    """Génère un document PDF avec les résultats de la prédiction"""
    pdf_filepath = os.path.join('static', 'pdf', filename)
    pdf = SimpleDocTemplate(pdf_filepath, pagesize=letter)

    # Styles pour le document PDF
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = ParagraphStyle('Heading1', parent=title_style, fontSize=18, spaceAfter=12)
    body_style = styles['BodyText']

    # Contenu du PDF
    content = []
    title = Paragraph("Résultat de la Prédiction du Prix Mensuel de la Maison", heading_style)
    content.append(title)

    content.append(Spacer(1, 12))  # Espace

    # Informations sur la prédiction
    prediction_data = [
        ["Année de Construction", str(year)],
        ["Surface Habitable (m²)", str(surface)],
        ["Nombre d'Observations", str(observations)],
        ["Prix Mensuel Moyen Prédit (€)", str(prediction)],
        ["Loyer Annuel Prédit (€)", str(prediction * 12)]  # Ajout du loyer_annuel
    ]

    # Création du tableau
    prediction_table = Table(prediction_data, colWidths=[200, 100], rowHeights=30)
    
    # Style du tableau
    prediction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),  # Couleur de fond pour la ligne d'en-tête
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Couleur du texte pour la ligne d'en-tête
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alignement centré
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Police en gras pour la ligne d'en-tête
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Ajoute de l'espace en bas de la ligne d'en-tête
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Couleur de fond pour les autres lignes
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Ajoute des bordures au tableau
    ]))

    # Ajout du tableau au contenu
    content.append(prediction_table)

    # Enregistre le PDF
    pdf.build(content)

    return pdf_filepath
