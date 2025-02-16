import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import webbrowser

# Beispiel-Projektbeschreibung (Markdown Text Beispiel)
Text = """
# Automatisiertes Plandatenvalidierungstool

Das Planvalidierungstool wurde entwickelt, um die vom Faserplaner erstellten Plandaten auf Konsistenzfehler zu überprüfen. Ziel war es, sicherzustellen, dass keine fehlerhaften Daten in die CM-Datenbank gelangen, und die Datenqualität innerhalb der Deutschen GigaNetz GmbH (DGN) zu erhöhen.

Das Tool implementiert die Regeln, die im Beschriftungskonzept der Deutschen GigaNetz GmbH festgelegt sind. Dieses Konzept wird den Bauunternehmen bereitgestellt und enthält alle vertraglich vereinbarten Standards, die beim Bau eingehalten werden müssen.

Sobald ein Bauunternehmen seine Plandaten erstellt hat, ermöglicht das Tool eine automatische Validierung. Es überprüft die Plandaten auf Konsistenzfehler und erstellt einen detaillierten Fehlerbericht, der alle identifizierten Probleme dokumentiert.

Ich habe das Tool mit Python Dash programmiert. Es bietet eine benutzerfreundliche Oberfläche, die folgende Funktionen umfasst:

- **Hochladen der Initialdaten zur Validierung.**
- **Durchführung der Konsistenzprüfung gemäß den definierten Regeln.**
- **Herunterladen eines Fehlerberichts, sobald die Überprüfung abgeschlossen ist.**

Das Tool trägt maßgeblich zur Verbesserung der Datenqualität und zur Einhaltung der Standards bei, indem es fehlerhafte Daten frühzeitig erkennt und die Weitergabe in die zentralen Systeme verhindert.
"""

text2 = """
# Churn Prediction

Ziel des Projekts war es, vorherzusagen, welche Kunden voraussichtlich ihre Verträge kündigen werden. Diese Vorhersage ermöglicht es, gezielte Maßnahmen zur Reduzierung der Kundenabwanderung zu ergreifen.

## Genutzte Daten

##### Zielvariable (Label): 
- Auftragsstatus (Aktiv, Inaktiv)

##### Features:
- **Personendaten**: Alter, Eigentümertyp (Eigentümer/Mieter)
- **Gebäudedaten**: Anzahl der Wohneinheiten, Ort, Postleitzahl
- **Technische Daten**: Vertragsdetails (z. B. GGNV), genutztes Produkt, Router-Typ

## Methoden

Das Modell wurde mit Python und Machine-Learning-Techniken entwickelt. Eine umfassende explorative Datenanalyse (EDA) unterstützte die Auswahl der wichtigsten Features und das Verständnis der Datenmuster.

Die folgenden Algorithmen wurden mit der Python-Bibliothek scikit-learn trainiert und zur Vorhersage verwendet:
- Logistische Regression
- Entscheidungsbaum (Decision Tree)
- Random Forest
- XGBoost
- CatBoost

## Erkenntnisse aus der Datenanalyse (EDA)

- Private Kunden kündigen häufiger als Firmenkunden.
- Aufträge ohne Grundstücks- und Gebäudenutzungsvertrag (GGNV) sind doppelt so häufig vom Churn betroffen.
- Eigentümer kündigen seltener als Mieter.
- Kunden über 70 Jahre und im Alter von 18–30 Jahren zeigen die höchste Kündigungsrate.
- Bestimmte Produkte und Bestellstrecken haben eine höhere Churn-Wahrscheinlichkeit.

## Ergebnisse der Vorhersage

Das beste Ergebnis wurde mit CatBoost erzielt:
- **Precision**: 0,75
- **ROC-AUC**: 0,80

"""
text3="""
# Automatische Dateiumbenennung

Ich habe eine Azure-Funktion entwickelt, die die Meta-Daten der Bilder ausliest und basierend darauf neue Dateinamen erstellt. Ziel war es, die Dateistruktur zu vereinheitlichen und die Organisation zu verbessern. In diesem Projekt habe ich Cloud-Dienste integriert, Arbeitsabläufe automatisiert und Scripts zur Verarbeitung und Umbenennung von Dateien geschrieben. Es war eine Lösung, die sowohl mein Wissen in Cloud-Technologien als auch meine Programmierkenntnisse erforderte.
"""

text4="""
# Automatisierte Medienüberwachung
In diesem Projekt habe ich eine Azure-Funktion in Python entwickelt, die täglich Google News nach Artikeln durchsucht, in denen unser Unternehmen erwähnt wird. Die Funktion extrahiert relevante Informationen wie das Veröffentlichungsjahr, den Titel und den Link des Artikels und speichert diese in einer Datei, die täglich automatisch aktualisiert wird.  

Die Lösung nutzt APIs zur News-Suche und ist vollständig automatisiert, wodurch der manuelle Aufwand zur Überwachung der Medienberichterstattung erheblich reduziert und die Effizienz gesteigert wurde. Dieses Projekt hat meine Fähigkeiten in der Automatisierung, der Verarbeitung von Web-Daten und der Nutzung von Cloud-Technologien weiter vertieft.
"""
# Deine angepasste Projektliste
projekte = [
    {"id": 1, "Zeitraum": "02/2022 – 09/2024", "Titel": "Automatisiertes Plandatenvalidierungstool",
     "Rolle": "Die Entwicklung des Planvalidierungstool mit Dash-Python", "Software": "Python", 
     "Auftraggeber": "Unternehmensprojekt", "Arbeitgeber": "Deutsche Giganetz GmbH", 
     "Projektbeschreibung": Text},
     
     {"id": 11, "Zeitraum": "01/2023 – 09/2024", "Titel": "Churn Prediction",
     "Rolle": "Entwicklung und Implementierung von Machine-Learning-Algorithmen, einschließlich der Datenaufbereitung (Explorative Datenanalyse, Preprocessing), des Modelltrainings und der Vorhersage", "Software": "Python", 
     "Auftraggeber": "Unternehmensprojekt", "Arbeitgeber": "Deutsche Giganetz GmbH", 
     "Projektbeschreibung": text2},

     {"id": 111, "Zeitraum": "06/2024 – 09/2024", "Titel": "Automatische Dateiumbenennung",
     "Rolle": "Programmierung einer Python-Funktion in Azure zur automatischen Umbenennung von Fotos", "Software": "Azure-Funktion-Python", 
     "Auftraggeber": "Unternehmensprojekt", "Arbeitgeber": "Deutsche Giganetz GmbH", 
     "Projektbeschreibung": text3},

     {"id": 1111, "Zeitraum": "03/2024 – 05/2024", "Titel": "Automatisierte Medienüberwachung",
     "Rolle": "Programmierung einer Azure-Funktion in Python zur automatisierten Medienüberwachung", "Software": "Azure-Funktion-Python", 
     "Auftraggeber": "Unternehmensprojekt", "Arbeitgeber": "Deutsche Giganetz GmbH", 
     "Projektbeschreibung": text4},

    {"id": 2, "Zeitraum": "02/2017 – 04/2018", "Titel": "Monitoring the Evolution and Benefits of Responsible and Innovation (MoRRI)",
     "Rolle": "Multivariate Analyse der Aktivitäten und Einstellungen bezüglich Responsible Research and Innovation in Online Surveys",
     "Software": "Stata", "Auftraggeber": "Europäische Kommission", "Arbeitgeber": "Fraunhofer ISI", 
     "Projektbeschreibung": "https://www.isi.fraunhofer.de/de/competence-center/politik-gesellschaft/projekte/super-morri.html"},

    {"id": 3, "Zeitraum": "01/2015 – 04/2018", "Titel": "Erhebung Modernisierung der Produktion (EMS)",
     "Rolle": "Implementierung und Durchführung von Bereinigungs- und Plausibilitätsregeln in SPSS-Syntax für die EMS-Befragungsdaten",
     "Software": "SPSS", "Auftraggeber": "Strategisches Eigenforschungsprojekt", "Arbeitgeber": "Fraunhofer ISI", 
     "Projektbeschreibung": "https://www.isi.fraunhofer.de/de/themen/wertschoepfung/erhebung-modernisierung-produktion.html"},

    {"id": 4, "Zeitraum": "07/2013 – 04/2018", "Titel": "Erhebung des Innovationsverhaltens der Unternehmen",
     "Rolle": "Mitarbeit am jährlichen Indikatorenbericht zur Innovationserhebung", "Software": "Stata", 
     "Auftraggeber": "ZEW Zentrum für Europäische Wirtschaftsforschung GmbH", "Arbeitgeber": "Fraunhofer ISI",
     "Projektbeschreibung": "https://www.isi.fraunhofer.de/de/competence-center/innovations-wissensoekonomie/projekte/mip4.html#1"},

    {"id": 5, "Zeitraum": "03/2017 – 12/2017", "Titel": "Industrie 4.0 in Kasachstan: Potential, perspectives and role of policy",
     "Rolle": "Mikro-ökonometrische Analyse zur Einschätzung der sozioökonomischen Wirkung der Industrie 4.0 Strategie", 
     "Software": "Stata", "Auftraggeber": "Kasachisches Institut für industrielle Entwicklung", "Arbeitgeber": "Fraunhofer ISI",
     "Projektbeschreibung": "https://www.isi.fraunhofer.de/de/competence-center/politik-gesellschaft/projekte/kasachstan.html#1"},

    {"id": 6, "Zeitraum": "01/2014 – 10/2015", "Titel": "Entwicklung eines Produktionsmesskonzeptes für wissensintensive Dienstleister",
     "Rolle": "Ökonometrische Analyse der Determinanten der Innovation und ihr Einfluss auf die Produktivität", 
     "Software": "Stata", "Auftraggeber": "BMBF", "Arbeitgeber": "Fraunhofer ISI", "Projektbeschreibung": text2},  # Kein Link und keine Beschreibung

    {"id": 7, "Zeitraum": "08/2013 – 09/2014", "Titel": "Innovationsindikator",
     "Rolle": "Erstellen der Indikatoren und Durchführung der Sensitivitätsanalyse", "Software": "R", 
     "Auftraggeber": "BDI und Acatech", "Arbeitgeber": "Fraunhofer ISI", 
     "Projektbeschreibung": "https://www.innovationsindikator.de"},
]

# Dash App Setup
dash.register_page(__name__, order=3)


def layout():
    return dbc.Row([
        dbc.Col([
            html.Br(),
            html.H3("Meine Projekte (Auswahl)", className="text-center"),
            html.Br(),
            #Das erste Projekt
            dbc.Accordion([
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 1), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 1), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 1), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 1), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button1", color="secondary", className="mt-2"),

                    dbc.Modal([
                        dbc.ModalHeader("Deutsche Giganetz GmbH"),
                        dbc.ModalBody(dcc.Markdown(Text)),
                        dbc.ModalFooter(
                            dbc.Button("Schließen", id="close-markdown1", className="ml-auto")
                        ),
                    ], id="markdown-modal1", is_open=False)
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] == 1), None))),

                # Das zweite Projekt#################################################################################
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 11), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 11), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 11), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 11), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button2", color="secondary", className="mt-2"),

                    dbc.Modal([
                        dbc.ModalHeader("Deutsche Giganetz GmbH"),
                        dbc.ModalBody(dcc.Markdown(text2)),
                        dbc.ModalFooter(
                            dbc.Button("Schließen", id="close-markdown2", className="ml-auto")
                        ),
                    ], id="markdown-modal2", is_open=False)
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] == 11), None))),
                #######################################################################################################

                # Das dritte Projekt#################################################################################
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 111), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 111), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 111), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 111), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button3", color="secondary", className="mt-2"),
                   
                    dbc.Modal([
                        dbc.ModalHeader("Deutsche Giganetz GmbH"),
                        dbc.ModalBody(dcc.Markdown(text3)),
                        dbc.ModalFooter(
                            dbc.Button("Schließen", id="close-markdown3", className="ml-auto")
                        ),
                    ], id="markdown-modal3", is_open=False)
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] == 111), None))),
                #######################################################################################################

                # das vierte Projekt
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 1111), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 1111), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 1111), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 1111), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button4", color="secondary", className="mt-2"),

                    dbc.Modal([
                        dbc.ModalHeader("Deutsche Giganetz GmbH"),
                        dbc.ModalBody(dcc.Markdown(text4)),
                        dbc.ModalFooter(
                            dbc.Button("Schließen", id="close-markdown4", className="ml-auto")
                        ),
                    ], id="markdown-modal4", is_open=False)
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] == 1111), None))),

                # das fünfte Projekt################################################################################
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 2), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 2), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 2), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 2), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button5", color="secondary", className="mt-2")
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] ==2), None))),

                # Das 6. Projekt####################################################################################
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 3), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 3), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 3), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 3), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button6", color="secondary", className="mt-2")
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] ==3), None))),

                # das 7. Projet###########################################################################################
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 4), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 4), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 4), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 4), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button7", color="secondary", className="mt-2")
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] ==4), None))),

                # das 8. Projekt ######################################################################################
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 5), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 5), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 5), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 5), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button8", color="secondary", className="mt-2")
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] ==5), None))),

                 # das 9. Projekt ######################################################################################
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 6), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 6), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 6), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 6), None)}"),
                    
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] ==6), None))),

                # das 10. Projekt ######################################################################################
                dbc.AccordionItem([
                    html.P(f"Zeitraum: {next((projekt['Zeitraum'] for projekt in projekte if projekt['id'] == 7), None)}"),
                    html.P(f"Software: {next((projekt['Software'] for projekt in projekte if projekt['id'] == 7), None)}"),
                    html.P(f"Auftraggeber: {next((projekt['Auftraggeber'] for projekt in projekte if projekt['id'] == 7), None)}"),
                    html.P(f"Arbeitgeber: {next((projekt['Arbeitgeber'] for projekt in projekte if projekt['id'] == 7), None)}"),
                    dbc.Button("Mehr erfahren", id="markdown-button9", color="secondary", className="mt-2")
                ], title=html.H5(next((projekt["Titel"] for projekt in projekte if projekt["id"] ==7), None))),


            ], start_collapsed=True, className="mt-3"),
        ], width=12)
    ], justify="center")

# das erste Projekt###############################################################
@dash.callback(
    Output("markdown-modal1", "is_open"),
    [Input("markdown-button1", "n_clicks"), Input("close-markdown1", "n_clicks")],
    [State("markdown-modal1", "is_open")]
)
def toggle_markdown(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open
###################################################################################

# das zweite Projekt###############################################################
@dash.callback(
    Output("markdown-modal2", "is_open"),
    [Input("markdown-button2", "n_clicks"), Input("close-markdown2", "n_clicks")],
    [State("markdown-modal2", "is_open")]
)
def toggle_markdown(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open
###################################################################################

# das dritte Projekt###############################################################
@dash.callback(
    Output("markdown-modal3", "is_open"),
    [Input("markdown-button3", "n_clicks"), Input("close-markdown3", "n_clicks")],
    [State("markdown-modal3", "is_open")]
)
def toggle_markdown(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open
###################################################################################

# das vierte Projekt###############################################################
@dash.callback(
    Output("markdown-modal4", "is_open"),
    [Input("markdown-button4", "n_clicks"), Input("close-markdown4", "n_clicks")],
    [State("markdown-modal4", "is_open")]
)
def toggle_markdown(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open
###################################################################################

# das fünfte Projekt
@dash.callback(
    Output("markdown-button5", "n_clicks"),
    Input("markdown-button5", "n_clicks"),
    prevent_initial_call=True
)
def open_google(n_clicks):
    webbrowser.open(next((projekt["Projektbeschreibung"] for projekt in projekte if projekt["id"] ==2), None))  # Öffnet die Seite im Standardbrowser
    return 0  # Reset n_clicks, um mehrfaches Klicken zu ermöglichen


# das 6. Projekt###########################################################
@dash.callback(
    Output("markdown-button6", "n_clicks"),
    Input("markdown-button6", "n_clicks"),
    prevent_initial_call=True
)
def open_google(n_clicks):
    webbrowser.open(next((projekt["Projektbeschreibung"] for projekt in projekte if projekt["id"] ==3), None))  # Öffnet die Seite im Standardbrowser
    return 0  # Reset n_clicks, um mehrfaches Klicken zu ermöglichen


# das 6. Projekt###########################################################
@dash.callback(
    Output("markdown-button7", "n_clicks"),
    Input("markdown-button7", "n_clicks"),
    prevent_initial_call=True
)
def open_google(n_clicks):
    webbrowser.open(next((projekt["Projektbeschreibung"] for projekt in projekte if projekt["id"] ==4), None))  # Öffnet die Seite im Standardbrowser
    return 0  # Reset n_clicks, um mehrfaches Klicken zu ermöglichen

# das 7. Projekt###########################################################
@dash.callback(
    Output("markdown-button8", "n_clicks"),
    Input("markdown-button8", "n_clicks"),
    prevent_initial_call=True
)
def open_google(n_clicks):
    webbrowser.open(next((projekt["Projektbeschreibung"] for projekt in projekte if projekt["id"] ==5), None))  # Öffnet die Seite im Standardbrowser
    return 0  # Reset n_clicks, um mehrfaches Klicken zu ermöglichen

# das 8. Projekt###########################################################
@dash.callback(
    Output("markdown-button9", "n_clicks"),
    Input("markdown-button9", "n_clicks"),
    prevent_initial_call=True
)
def open_google(n_clicks):
    webbrowser.open(next((projekt["Projektbeschreibung"] for projekt in projekte if projekt["id"] ==7), None))  # Öffnet die Seite im Standardbrowser
    return 0  # Reset n_clicks, um mehrfaches Klicken zu ermöglichen