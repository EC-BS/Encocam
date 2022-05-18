#!/usr/bin/env python
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from dash import Dash, dash_table
import pandas as pd
import plotly.express as px
from dash import html
import plotly.graph_objects as go
import base64
from dash.dependencies import Input, Output, State
import plotly.io as pio
import numpy as np
import smtplib,ssl
from datetime import datetime as dt
import json
#import dash_auth


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])
app.config.suppress_callback_exceptions=True
app.config.suppress_callback_exceptions=True
#app login
#VALID_USERNAME_PASSWORD_PAIRS = {'hello': 'world'}
#auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

#-------------Github collated data-----------------
#https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx
#df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Dash%20Components/Dropdown/Urban_Park_Ranger_Animal_Condition.csv")  
# Replace all datasheets with github repository.

refca='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'
refbtank='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'
refatank='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'
refww='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'
refdosing='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'
refdigouts='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'
reftanktemp='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'
aw_test_ref= 'https://www.ukas.com/wp-content/uploads/schedule_uploads/00002/1223Testing-Multiple.pdf'
ww_data_logging='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'
apanel='https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx'

'''
#------------Excel sheet locations for links------------------------
refca='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/EUkeZ_PoVTBPqwK_simA2JABRU2--u8NTzchhqz_WQL3OQ?e=zhk5U5'
refbtank='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/EVF9chUVCklDtLkyQf61h0gBvDhBa7Qih881EqR7DmMV2w?e=N7GxHH'
refatank='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/EbNzWJQ8mFVBp4vqK6KfaGIBRAIukoBM-E4hZ9tJGSlBrw?e=D3bqlk'
refww='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/ESZudTsKYQxHiM4Bo9dKOrsBQtPTx2Rf2kLrc2GMwpEUbA?e=xaXyAf'
refdosing='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/EY5PCMPWgmFCio0WNKDh7x8BOgelA-3tafRXUxBG1YgSrg?e=fIYdZg'
refdigouts='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/EUxAzNqbLctMo-t1R0fKgcQBUHrZifutOtkFnyCFJp5WxA?e=zMbgNH'
reftanktemp='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/ETfEmZh7Q9lFljigwfuSZ8IBMBYpLOMj7CyRWyhy0P_YlA?e=tGfGZQ'
aw_test_ref= 'https://www.ukas.com/wp-content/uploads/schedule_uploads/00002/1223Testing-Multiple.pdf'
ww_data_logging='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/EdcqKqssMZxLpwEcWVklZYkBwLjFZtiatc9T2S1QM01kvQ?e=pZPbTr'
apanel='https://encocam-my.sharepoint.com/:x:/g/personal/nadine_symonds_cellbond_com/EZy-VJ4irLFKju8x1ow6LeEBPw2_fhB-GLQxDqdw6XlDQQ?e=vp6045'
'''

#----------------------Alerts--------------------------
Linkalert=dbc.Alert(["alert test", html.A("example", href=refca , className="alert-link")])

#--------------------------- Bulk data inputs - excel sheets-----------------------
header_list= ["Date", "FR-TA", "FR-pH", "CR-TA", "CR-pH", "1A-FA", "1A-TA", "1A-Al", "1A-Phosphate (ppm)", "1A-Phosphate %", "1A-Fluoride", "1B-FA", "1B-TA", "1B-Al", "1B-Phosphate (ppm)", "1B-Phosphate %", "1B-Fluoride", "DS-TA", "DS-%V", "N104-FA", "N104-TA", "N104-Al"]
df = pd.read_excel('https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx', sheet_name='Chemical_Analysis', skiprows=1, names=header_list, na_values = ['no info', ','])
Date = pd.DatetimeIndex(df.Date).strftime("%Y-%m-%d")
header_1a= ['Batch','Basket','Notes','Weight after','Qty','Authorised by', 'Date','Tank','Quantity','Barrier type','Element type','Core type','Block number','Pre-etch number', 'Prep works order','Etch works order','Final test number','Test number 1','Test number 2','Test number 3','Test number 4','Test number 5','Test number 6','Full dip 1 (min)','Program 1','Others 1','Full dip 2 (min)','Program 2','Others 2','Full dip 3 (min)','Program 3','Others 3','Full dip 4 (min)','Program 4','Others 4','Full dip 5 (min)','Program 5','Others 5','Full dip 6 (min)','Program 6','Others 6','Required crush strength','Average crush strength','Etch program','Weight before', 'Weight difference', 'PASS AFTER FAIL','Temperature','Fluoride','Addition 1','Fluoride 2','Addition 2','Fluoride 3','DX5100 addition','DX5100 addition 2','Water     top-up','Ultrasonic','Skins','Comments']
df1atank = pd.read_excel('https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx', sheet_name='Tank_1A', header=[0], na_values = ['no info', ','])
df1btank = pd.read_excel('https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx', sheet_name='Tank_1B', header=[0], na_values = ['no info', ','])
header_ww=['a', 'b','c','d','e','tss']
dfww = pd.read_excel('https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx', sheet_name='Waste_Water', names=header_ww, na_values=['no info', ','])
header_do=["Date", "Operator", "Tank", "Rinse Tank", "Company", "Trigger number", "Response Time", "Dig out Hours", "Number of Drums", "Baskets since previous digouts", "Measured from top", "1a-added phosphoric acid", "1a-added hf", "1b added phosphoric", "1B-added hf", "comments"]
#dfdigout=pd.read_excel(r'H:\Forms\ET - Etch Bay\F-ET-35 Dig-out information.xlsx',sheet_name='Historic', names=header_do, header=[0], na_values=['no info', ','])
#df["Date"]=(df["Date"], '%d%m%Y')
wwdf=pd.read_excel('https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx', sheet_name='Waste_Water', header=[0], na_values=['no_info', ','])
stock_headers=['Part','Description 1','Description 2','Description 3','UoM','UoO','Purchasing Lead Time','Assembly Lead Time','Prime Supplier','Supplier Part','Material Cost']
stock_data= pd.read_csv(r'C:\Users\nadines\Documents\Python\test\layout\stock.csv', delimiter=',', names=stock_headers)
tanktemp_data=pd.read_excel('https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx', sheet_name='Tank_Temperature', header=[0], na_values=['no info',','])
dosing_data=pd.read_excel('https://github.com/EC-BS/Encocam/blob/main/App_data.xlsx', sheet_name='Dosing', header=[0])


#------------Data Blocks------------------------------
df1a = [df,"1A-FA", "1A-TA", "1A-Al", "1A-Phosphate %", "1A-Fluoride"]
df1b = [df, "1B-FA", "1B-TA", "1B-Al", "1B-Phosphate %", "1B-Fluoride"]
dfds = [df, "DS-TA", "DS-%V"]
df104 = [df, "N104-FA", "N104-TA", "N104-Al"]
dfcr = [df, "CR-TA", "CR-pH"]
dffr = [df, "FR-TA", "FR-pH"]

dig_outs = pd.DataFrame({"Date": ["15 Mar 2022", "19 Apr 2022", "24 May 2022", "28 June 2022", "12 Jul 2022", "02 Aug 2022", "06 Sep 2022", "11 Oct 2022", "15 Nov 2022", "20 Dec 2022"],"Tank": ["1A", "1A", "1A", "1A", "1B", "1A", "1A", "1A", "1A", "1A"],},)

Fluoride1a = [df1atank.tail(3), "Fluoride"]


#----------------------Table------------------------
digoutstable = dbc.Table.from_dataframe(dig_outs, striped=True, bordered=True, hover=True, size = "sm")

cas_table_header=[html.Thead([html.Td(" "), html.Td("Monday"), html.Td("Tuesday"), html.Td("Wednesday"), html.Td("Thursday"), html.Td("Friday")])]
casrow1=html.Tr([html.Td("Fluoride"), html.Td(""), html.Td("Testing"), html.Td(""), html.Td("Testing"), html.Td("")])
casrow2=html.Tr([html.Td("Phosphates"), html.Td(""), html.Td("Testing"), html.Td(""), html.Td("Testing"), html.Td("")])
casrow3=html.Tr([html.Td("Aluminium"), html.Td(""), html.Td("Testing"), html.Td(""), html.Td("Testing"), html.Td("")])
casrow4=html.Tr([html.Td("pH"), html.Td("Testing"), html.Td("Testing"), html.Td("Testing"), html.Td("Testing"), html.Td("Testing")])
casrow5=html.Tr([html.Td("Total Acidity"), html.Td(""), html.Td("Testing"), html.Td(""), html.Td("Testing"), html.Td("")])
casrow6=html.Tr([html.Td("Free Acidity"), html.Td(""), html.Td("Testing"), html.Td(""), html.Td("Testing"), html.Td("")])
casrow7=html.Tr([html.Td("Phosphine"), html.Td(""), html.Td("Testing"), html.Td(""), html.Td("Testing"), html.Td("")])
casrow8=html.Tr([html.Td("Ka Calculated"), html.Td(""), html.Td("Testing"), html.Td(""), html.Td("Testing"), html.Td("")])
cas_table_body = [html.Tbody([casrow1, casrow2, casrow3, casrow4, casrow5, casrow6, casrow7, casrow8])]
cas_table=dbc.Table(cas_table_header + cas_table_body, bordered=True, hover=True)


ww_table_header=[html.Thead([html.Td(" "), html.Td("Consent Limit"), html.Td("Current Average")])]
wwrow1=html.Tr([html.Td("pH"), html.Td("6-10"), html.Td("8.1")])
wwrow2=html.Tr([html.Td("Flow (L/Hr)"), html.Td("N/A"), html.Td("0.32")])
wwrow3=html.Tr([html.Td("TSS (mg/L)"), html.Td("<1000"), html.Td("1060")])
wwrow4=html.Tr([html.Td("Aluminium (mg/L)"), html.Td("<100"), html.Td("147")])
wwrow5=html.Tr([html.Td("Copper (mg/L)"), html.Td("<100"), html.Td("0.472")])
wwrow6=html.Tr([html.Td("Chemical Oxygen Demand"), html.Td("<500"), html.Td("<11.5")])
ww_table_body = [html.Tbody([wwrow1, wwrow2, wwrow3, wwrow4, wwrow5, wwrow6])]
ww_table=dbc.Table(ww_table_header + ww_table_body, bordered=True, hover=True)

results_a = df[["Date", "1A-FA", "1A-TA", "1A-Al", "1A-Phosphate %", "1A-Fluoride"]].tail(5)
results_b =df[["Date", "1B-FA", "1B-TA", "1B-Al", "1B-Phosphate %", "1B-Fluoride"]].tail(5)
results_ds =df[["Date", "DS-TA", "DS-%V"]].tail(5)
results_pt = df[["Date", "N104-FA", "N104-TA", "N104-Al"]].tail(2)
results_cr =df[["Date", "CR-TA", "CR-pH"]].tail(2)
results_fr =df[["Date", "FR-TA", "FR-pH"]].tail(2)
A_table = dbc.Table.from_dataframe(results_a, striped=True, bordered=True, hover=True, size="sm")
B_table = dbc.Table.from_dataframe(results_b, striped=True, bordered=True, hover=True, size="sm")
PT_table = dbc.Table.from_dataframe(results_pt, striped=True, bordered=True, hover=True, size="sm")
DS_table = dbc.Table.from_dataframe(results_ds, striped=True, bordered=True, hover=True, size="sm")
CR_table = dbc.Table.from_dataframe(results_ds, striped=True, bordered=True, hover=True, size="sm")				
FR_table = dbc.Table.from_dataframe(results_ds, striped=True, bordered=True, hover=True, size="sm")

ph_probe_header=[html.Thead([html.Td("Probe ID"), html.Td("Type"), html.Td("WI number"), html.Td("Location"), html.Td("Purchase Date"), html.Td("Installation Date"), html.Td("Calibration Date"), html.Td("Maintenance Notes")])]
ph_row1=html.Tr([html.Td("PR1-0014"), html.Td("xtype"), html.Td("WI-CR-11/10"), html.Td("IBC 1 pH Meter"), html.Td("TBD"), html.Td("28/01/2022"), html.Td("08 Feb 22"), html.Td("LTH Service 03 Mar 22")])
ph_row2=html.Tr([html.Td("PR1-0006"), html.Td("xtype"), html.Td("WI-CR-11/10"), html.Td("IBC 2 pH Meter"), html.Td("TBD"), html.Td("Date"), html.Td("08 Feb 22"), html.Td("LTH Service 03 Mar 22")])
ph_row3=html.Tr([html.Td("PR9-0007"), html.Td("xtype"), html.Td("WI-CR-11/10"), html.Td("Pipe Out pH Meter"), html.Td("TBD"), html.Td("28/01/2022"), html.Td("08 Feb 22"), html.Td("LTH Service 03 Mar 22")])
ph_row4=html.Tr([html.Td("PR3-0012"), html.Td("xtype"), html.Td("WI-PT-48/26"), html.Td("CC pH Meter"), html.Td("TBD"), html.Td("28/09/2020"), html.Td("07 Mar 22"), html.Td("N/A")])
ph_row5=html.Tr([html.Td("CC2600"), html.Td("xtype"), html.Td("WI-PT-49/36"), html.Td("Printer pH Meter"), html.Td("TBD"), html.Td("TBD"), html.Td("07 Mar 22"), html.Td("N/A")])
ph_row6=html.Tr([html.Td("CC2600"), html.Td("xtype"), html.Td("WI-PT-49/36"), html.Td("Printer pH Meter"), html.Td("TBD"), html.Td("TBD"), html.Td("07 Mar 22"), html.Td("N/A")])
ph_row7=html.Tr([html.Td("CC2720"), html.Td("xtype"), html.Td("WI-PT-49/36"), html.Td("Printer pH Meter"), html.Td("TBD"), html.Td("TBD"), html.Td("07 Mar 22"), html.Td("N/A")])
ph_body=[html.Tbody([ph_row1, ph_row2, ph_row3, ph_row4, ph_row5, ph_row6, ph_row7])]
ph_table=dbc.Table(ph_probe_header + ph_body, bordered=True, hover=True)

tanktemp_header=[html.Thead([html.Td("Probe Id"), html.Td("Type"), html.Td('Location'), html.Td("Purchase Date"), html.Td("Installation Date"), html.Td("Maintenance Notes")])]
tanktemp_row1=html.Tr([html.Td("CC2613"), html.Td("Infrared"), html.Td("1A"), html.Td("TBD"),  html.Td("03/02/2022"), html.Td("N/A")])
tanktemp_row2=html.Tr([html.Td("CC2673"), html.Td("Thermocouple"), html.Td("1A"), html.Td("TBD"),  html.Td("TBD"), html.Td("N/A")])
tanktemp_row3=html.Tr([html.Td("CC4483"), html.Td("Infrared"), html.Td("1B"), html.Td("TBD"),  html.Td("11/03/2021"), html.Td("N/A")])
tanktemp_row4=html.Tr([html.Td("CC2673"), html.Td("Thermocouple"), html.Td("1B"), html.Td("TBD"),  html.Td("TBD"), html.Td("N/A")])
tanktemp_body=[html.Tbody([tanktemp_row1, tanktemp_row2, tanktemp_row3, tanktemp_row4])]
tanktemp_table=dbc.Table(tanktemp_header + tanktemp_body, bordered=True, hover=True)

faas0 = dbc.Row([dbc.Col(html.H4(children="Technique : Perkin Elmer Flame Atomic Absorption Spectrometer", style={'fontSize':20, 'textAlign':'center'}))])
faas1 = dbc.Row([dbc.Col(html.H4(children="Atomic absorption spectroscopy (AAS) is a spectroanalytical procedure for the quantitative determination of chemical elements using the absorption of optical radiation (light) by free atoms in the gaseous state. Atomic absorption spectroscopy is based on absorption of light by free metallic ions.", style={'fontSize': 15}))])
faas2 = dbc.Row([dbc.Col(html.H4(children="Associated Work Instructions: ", style={'fontSize': 15})), dbc.Col(html.H4(children="WI-CA-01, WI-CA-02, WI-CA-03, WI-CA-04", style={'fontSize': 15}))])
faas3 = dbc.Row([dbc.Col(html.H4(children="PPE required: ", style={'fontSize': 15})), dbc.Col(html.H4(children="Lab Coat, Lab spectacles, and gloes are to be worn at all times", style={'fontSize': 15}))])

phos0 = dbc.Row([dbc.Col(html.H4(children="Technique: Palintest 7500", style={'fontSize':20, 'textAlign':'center'}))])
phos1 = dbc.Row([dbc.Col(html.H4(children="This is measured via colorimetric methods using the Palintest photometer 7500. One tablet is added to the sample containing aluminium molybdate in the presence of ammonium vanadate, this forms the yellow compound Phosphovanadomolybdate. The intensity of the colour produced is directly proportional to the phosphate concentration.", style={'fontSize':15}))])
phos2 = dbc.Row([dbc.Col(html.H4(children="Associated Work Instructions: ", style={'fontSize': 15})), dbc.Col(html.H4(children="WI-CA-04", style={'fontSize': 15}))])
phos3 = dbc.Row([dbc.Col(html.H4(children="PPE required: ", style={'fontSize': 15})), dbc.Col(html.H4(children="Lab Coat, Lab spectacles, and gloes are to be worn at all times", style={'fontSize': 15}))])

fluor0 = dbc.Row([dbc.Col(html.H4(children="Technique : Lineguard 101D Meter", style={'fontSize':20, 'textAlign':'center'}))])
fluor1 = dbc.Row([dbc.Col(html.H4(children="The Lineguard ion-selective electrode is a metal transducer (or sensor) that converts the activity of flurodie ions dissolved in a solution into an electrical potential", style={'fontSize': 15}))])
fluor2 = dbc.Row([dbc.Col(html.H4(children="Associated Work Instructions: ", style={'fontSize': 15})), dbc.Col(html.H4(children="WI-ET-80", style={'fontSize': 15}))])
fluor3 = dbc.Row([dbc.Col(html.H4(children="PPE required: ", style={'fontSize': 15})), dbc.Col(html.H4(children="Lab Coat, Lab spectacles, and gloes are to be worn at all times", style={'fontSize': 15}))])

dfdosehf=dosing_data[dosing_data['Chemical'].str.contains("HF")]
dfdosecum=dfdosehf[(dfdosehf['Date'] > '01/03/2022')]
dffcumhf=dfdosecum.groupby('Chemical')['Actual Dose (L)'].sum()
dfdosephos=dosing_data[dosing_data['Chemical'].str.contains("PHOS")]
dfdosecumphos=dfdosephos[(dfdosephos['Date'] > '01/03/2022')]
dffcumphos=dfdosecumphos.groupby('Chemical')['Target Dose (L)'].sum()
currenthf = [3362]
totalhf= currenthf-dffcumhf
currentphos = [1660]
totalphos= currentphos-dffcumphos

dosend=dosing_data.tail(80)
hfsum=(dosend.groupby(['Chemical']).sum().groupby(level=[0]).cumsum().reset_index())


stock0 = dbc.Row([dbc.Col(html.H4(children="Chemical", style={'fontsize':20})), dbc.Col(html.H4(children="Storage Limit", style={'fontsize':20})), dbc.Col(html.H4(children="Current Monthly Usage", style={'fontsize':20})), dbc.Col(html.H4(children="Current Calculated Stock Level", style={'fontsize':20}))])
stock1 = dbc.Row([dbc.Col(html.H4(children="Hydrogen Fluoride 50%", style={'fontSize':15})), dbc.Col(html.H4(children="3362 L (3 IBC's)", style={'fontSize':15})), dbc.Col(html.H4(children=dffcumhf, style={'fontSize':15})), dbc.Col(html.H4(children=totalhf, style={'fontSize':15}))])
stock2 = dbc.Row([dbc.Col(html.H4(children="Phosphoric Acid 75%", style={'fontSize':15})), dbc.Col(html.H4(children="1660 L (2 IBC's)", style={'fontSize':15})), dbc.Col(html.H4(children=dffcumphos, style={'fontSize':15})), dbc.Col(html.H4(children=totalphos, style={'fontSize':15}))])
stock3 = dbc.Row([dbc.Col(html.H4(children="Bonderite C-IC 302", style={'fontSize':15})), dbc.Col(html.H4(children="2 IBC's", style={'fontSize':15})), dbc.Col(), dbc.Col()])
stocktable= html.Div([stock0, stock1, stock2, stock3])


#--------------dropdown menu items are where we specify the conents--------------------------
items = [dbc.DropdownMenuItem('Pre-Treatment'), dbc.DropdownMenuItem('Tank 1A'), dbc.DropdownMenuItem('Tank 1B'), dbc.DropdownMenuItem('Desmut'), dbc.DropdownMenuItem('Common Rinse'), dbc.DropdownMenuItem('Final Rinse')]
#Dropdown = dbc.Row([dbc.DropdownMenu(label = "Tank", size = "lg", color="secondary", children=items, className="mb-3")])

Dropdown = dcc.Dropdown(id='my_dropdown', options=[{'label': '1A-Al', 'value': '1A-Al'},
                     {'label': '1B-Al', 'value': '1B-Al'},{'label': 'Cr-TA', 'value': 'Cr-TA'}],clearable=True, multi=False, searchable=False, placeholder='Select Tank', style= dict(width="40%", display="inline-block",verticleAlign="middle"))
#-----------figures--------------------------------------
dfpre=df.tail(5)
dfhist=df.tail(10)
figpre= px.bar(dfpre, x="Date", y="N104-TA", title="Total Acidity N104")
fig1a_al = px.scatter(dfpre, x="Date", y="1A-Al", title="Total Aluminium Tank 1A (ppm)", hover_data={"Date"})
fig1a_ta = px.scatter(dfpre, x="Date", y="1A-TA", title="Total Total Acidity 1A (Mol)", hover_data={"Date"})
fig1a_fa = px.scatter(dfpre, x="Date", y="1A-FA", title="Total Free Acidity 1A (Mol)", hover_data={"Date"})
fig1a_ph = px.scatter(dfpre, x="Date", y="1A-Phosphate %", title="Total Phosphate Content 1A (%)", hover_data={"Date"})
fig1b_al = px.scatter(dfpre, x="Date", y="1B-Al", title="Total Aluminium Tank 1B (ppm)", hover_data={"Date"})
fig1b_ta = px.scatter(dfpre, x="Date", y="1B-TA", title="Total Total Acidity 1B (Mol)", hover_data={"Date"})
fig1b_fa = px.scatter(dfpre, x="Date", y="1B-FA", title="Total Free Acidity 1B (Mol)", hover_data={"Date"})
fig1b_ph = px.scatter(dfpre, x="Date", y="1B-Phosphate %", title="Total Phosphate Content 1B (%)", hover_data={"Date"})
figds = px.scatter(dfpre, x="Date", y="DS-TA", title="Desmut total acidity")
figcr = px.bar(dfpre, x="Date", y="CR-pH", title="Common Rinse pH")
figfr = px.bar(dfpre, x="Date", y="FR-pH", title="Final Rinse pH")



tss=[2.6, 1667.53, 794.81, 506.49]
figww=go.Figure()
figww.add_trace(go.Line(x=[7,8,9], y=[1667.53, 794.81, 506.49],name="Site Data"))
figww.add_trace(go.Line(x=[7,8,9], y=[1000,1000,1000],name="Anglia Water limit"))
dffront=df.tail(1)
figww1=px.scatter(wwdf, x='Date', y='TSS (mg/l)')
figww2=px.scatter(wwdf, x='Date', y='Aluminium (mg/L)')


#-------------- Alarms styling------------------
aff = html.Div(
        dbc.Alert([html.I(className="bi bi-exclamation-triangle-fill me-2"),"Date of last flash fire: 11/02/2022",],
            color="warning",className="d-flex align-items-center",),)
bff = html.Div(
        dbc.Alert([html.I(className="bi bi-exclamation-triangle-fill me-2"),"Date of last flash fire: 21/03/202",],
            color="warning",className="d-flex align-items-center",),)
cw = html.Div(
        dbc.Alert([html.I(className="bi bi-exclamation-triangle-fill me-2"),"Issues with spectrometer: Under Investigation",],
            color="secondary",className="d-flex align-items-center",),)
#Button
CA_button=dbc.Button("Chemical Analysis Data", href=refca, color="info")
ATankbutton=dbc.Button("1A Tank Records", href=refatank, color="info")
BTankbutton=dbc.Button("1B Tank Records", href=refbtank, color="info")
WW_button=dbc.Button("Waste Water Internal Analysis", href=refww, color="info")
dosing_button=dbc.Button("Chemical Dosing", href=refdosing, color="info")
tank_temps=dbc.Button("Tank Temperature Readings", href=reftanktemp, color="info")
aw_button=dbc.Button("Anglia Water Testing Procedure", href=aw_test_ref, color="info")
ww_data_button=dbc.Button("Waste Water pH and Dosing Record", href=ww_data_logging, color="info")
apanel_button=dbc.Button("Alarm Panel Record", href=apanel, color="info")

#------total dosing----


# ----------------images-----------------------
encocam_file = 'tankimage.png'
encoded_image = base64.b64encode(open(encocam_file, 'rb').read()).decode('ascii')
waste_pic = 'waste.png'
waste_image = base64.b64encode(open(waste_pic, 'rb').read()).decode('ascii')
ec_pic = 'ec.png'
ec_image = base64.b64encode(open(ec_pic, 'rb').read()).decode('ascii')
faas_pic = 'pe.jpg'
faas_image = base64.b64encode(open(faas_pic, 'rb').read()).decode('ascii')
phosv_pic = 'pt.png'
phosv_image = base64.b64encode(open(phosv_pic, 'rb').read()).decode('ascii')
lg_pic = 'lg1.png'
lg_image = base64.b64encode(open(lg_pic, 'rb').read()).decode('ascii')

# ------------------Homepage card------------------
Home=(dbc.CardImg(src="https://www.encocam.com/wp-content/themes/encocam/img/logos/encocam.svg", top=True), dbc.CardBody([html.H4("Encocam Data", className="card-title"), html.P("Encocam data collection and production information hub.", className="card-text")], style={"width": "18rem"}))
CA_Card=(dbc.CardBody([html.H4("Chemical Anaysis", className="card-title", style={'font-size':'20px'}), html.H6("F-CA-0001", className="card-subtitle"), html.P("On site chemical analysis. Editable Document.", className="card-test"), dbc.CardLink("F-01-001", href=refca)]))
Tank_Card=(dbc.CardBody([html.H4("Tank Records", className="card-title", style={'font-size':'20px'}), html.H6("F-ET-28, F-ET-29", className="card-subtitle"), html.P("Live updated tank records. No Editing available.", className="card-test"), dbc.CardLink("1A Tank Records", href=refatank), dbc.CardLink("1B Tank Records", href=refbtank)], ))
A_fluoride_average= dbc.Card([dbc.CardHeader("Target Value: 1000ppm"), dbc.CardBody([html.H4("Current Weekly Average: 1111ppm"), html.P("Standard deviation: 198ppm")]),], style={"width":"18rem"})
A_phosphate_average = dbc.Card([dbc.CardHeader("Target Value: 3.8%"), dbc.CardBody([html.H4("Current Weekly Average: 3.5%"), html.P("Standard deviation: 0.48")])], style={"width":"18rem"})
A_temp_average = dbc.Card([dbc.CardHeader("Target Value: 42 \u00B0C"), dbc.CardBody([html.H4("Current Weekly Average: 42.5 \u00B0C"), html.P("Standard deviation: 1.6 \u00B0C"),])], style={"width":"18rem"},)
B_fluoride_average= dbc.Card([dbc.CardHeader("Target Value: 1000ppm"), dbc.CardBody([html.H4("Current Weekly Average: 1011ppm"), html.P("Standard deviation: 59ppm")]),], style={"width":"18rem"})
B_phosphate_average = dbc.Card([dbc.CardHeader("Target Value: 3.8%"), dbc.CardBody([html.H4("Current Weekly Average: 3.3%"), html.P("Standard deviation: 0.47")])], style={"width":"18rem"})
B_temp_average = dbc.Card([dbc.CardHeader("Target Value: 42 \u00B0C"), dbc.CardBody([html.H4("Current Weekly Average: 41.9 \u00B0C"), html.P("Standard deviation: 0.4 \u00B0C"),])], style={"width":"18rem"},)


#-----Input/output------------


# --- Dropdown graphs ---
atankdd=(html.Div(dcc.Dropdown(id='tanka-my-dropdown', multi=True, options=[{'label':'1A Aluminium Content', 'value':'1A-Al'}, {'label':'1A Phosphate Content', 'value':'1A-Phosphate %'}, {'label':'1A Free Acidity', 'value':'1A-FA'}, {'label':'1A Total Acidity', 'value':'1A-TA'}, {'label':'1A Fluoride', 'value':'1A-Fluoride'}])),html.Button(id='tanka-my-button', n_clicks=0, children='Show Selection'), html.Div(dcc.Graph(id="tanka-graph-output", figure={})))
btankdd=(html.Div(dcc.Dropdown(id='tankb-my-dropdown', multi=True, options=[{'label':'1B Aluminium Content', 'value':'1B-Al'}, {'label':'1B Phosphate Content', 'value':'1B-Phosphate %'}, {'label':'1B Free Acidity', 'value':'1B-FA'}, {'label':'1B Total Acidity', 'value':'1B-TA'}, {'label':'1B Fluoride', 'value':'1B-Fluoride'}])),html.Button(id='tankb-my-button', n_clicks=0, children='Show Selection'), html.Div(dcc.Graph(id="tankb-graph-output", figure={})))
dose = (html.Div([dcc.DatePickerRange(id='table-date-range', calendar_orientation='horizontal',day_size=39,end_date_placeholder_text="Return", with_portal=False, first_day_of_week=0, reopen_calendar_on_clear=True, is_RTL=False, number_of_months_shown=1, min_date_allowed=dt(2020, 1, 1),max_date_allowed=dt(2022, 6, 20), start_date=dt(2020, 8, 7).date(),end_date=dt(2022, 5, 15).date(), display_format='MMM Do, YY',month_format='MMMM, YYYY', minimum_nights=2, persistence=True, persisted_props=['start_date'],persistence_type='session', updatemode='singledate'), html.H3("Sidewalk Café Licenses and Applications", style={'textAlign': 'center'}), dash_table.DataTable(id='dosetable')]))


#----- play ----
dosing=(html.Div(dcc.Dropdown(id='dose-my-dropdown', multi=True, options=[{'label':x, 'value':x} for x in sorted(dosing_data.Chemical.unique())], value=["HF 1A", "HF 1B", "PHOS 1A", "PHOS 1B"])),html.Button(id='dose-my-button', n_clicks=0, children='Show Selection'), html.Div(dcc.Graph(id="dose-graph-output", figure={})))
cumdosing=(html.Div(dcc.Dropdown(id='cum-my-dropdown', multi=True, options=[{'label':x, 'value':x} for x in sorted(dosing_data.Chemical.unique())], value=["HF 1A", "HF 1B", "PHOS 1A", "PHOS 1B"])),html.Button(id='cum-my-button', n_clicks=0, children='Show Selection'), html.Div(dcc.Graph(id="cum-graph-output", figure={})))


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}



# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Encocam", className="display-4"),
        html.Hr(),
        html.P(
            "Navigation", className="lead"
        ),
        dbc.Nav(
            [
		
                dbc.NavLink("Chemical Overview", href="/page-1", active="exact"),
                dbc.NavLink("Environmental", href="/page-2", active="exact"),
                dbc.NavLink("Chemical Stock", href="/page-3", active="exact"),
                dbc.NavLink("Equiptment List", href="/page-4", active="exact"),
            ],
           vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

    # If the user tries to reach a different page, return a 404 message

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])

def render_page_content(pathname):
    if pathname == "/page-1":
        return html.Div([dcc.Tabs([
        dcc.Tab(label='Tank 1A', children=[html.Div([CA_button, ATankbutton, tank_temps]), html.Div(aff), html.Div(cw),html.Div(dbc.Row([dbc.Col(A_fluoride_average), dbc.Col(A_phosphate_average), dbc.Col(A_temp_average)]), style={'padding': 20, 'flex': 1}), dbc.Row([dbc.Col(html.Div(atankdd)), dbc.Col(html.Div([html.H4('1A Latest Chemical Analysis', style={'padding':50, 'fontSize':20}), html.Div(A_table, style={'padding':50}), html.H4(children="Current Batch: 123.\n  Current basket: 149", style={'padding':50, 'textAlign':'center', 'fontSize':15, 'whitespace':'pre'})]))]), html.H4(children='Temperature Probe Comparison'), html.Div(dcc.Dropdown(id='atemp-my-dropdown', multi=True, options=[{'label':'Temperature: Infrared', 'value':'Infrared T (⁰C)'}, {'label':'Temperature: Thermocouple', 'value':'Thermocouple T (⁰C)'}])), html.Button(id='atemp-button', n_clicks=0, children='Show Breakdown'), html.Div(dcc.Graph(id="atemp-graph-output", figure={})), html.Div([html.H4(children='Dig out Dates', style={'fontSize':20, 'size':'sm'}),digoutstable])]), 
        dcc.Tab(label='Tank 1B', children=[html.Div([CA_button, BTankbutton, tank_temps]), html.Div(bff), html.Div(cw),html.Div(dbc.Row([dbc.Col(B_fluoride_average), dbc.Col(B_phosphate_average), dbc.Col(B_temp_average)]), style={'padding': 20, 'flex': 1}), dbc.Row([dbc.Col(html.Div(btankdd)), dbc.Col(html.Div([html.H4('1B Latest Chemical Analysis', style={'padding':50, 'fontSize':20}), html.Div(B_table, style={'padding':50}), html.H4(children="Current Batch: 123.\n  Current basket: 149", style={'padding':50, 'textAlign':'center', 'fontSize':15})]))]), html.H4(children='Temperature Probe Comparison'), html.Div(dcc.Dropdown(id='btemp-my-dropdown', multi=True, options=[{'label':'Temperature: Infrared', 'value':'Infrared T (⁰C)'}, {'label':'Temperature: Thermocouple', 'value':'Thermocouple T (⁰C)'}])), html.Button(id='btemp-button', n_clicks=0, children='Show Breakdown'), html.Div(dcc.Graph(id="btemp-graph-output", figure={})), html.Div([html.H4(children='Dig out Dates', style={'fontSize':20, 'size':'sm'}),digoutstable])]), 
		dcc.Tab(label='General Chemical Information', children=[dbc.Row([dbc.Col(html.H4(children="Testing Schedule.\n \n   Current testing schedule increased as a result of the recent flash fires.\n \n   See below for a description of test methods used for analysis.", style={'padding':50, 'fontSize':15, 'white-space':'pre'})), dbc.Col(html.Table(cas_table, style={'padding':50, 'textAlign':'center', 'fontSize':13, 'size':'sm', 'marginLeft': 'auto', 'marginRight': 'auto'}), style={'padding':50})]), html.Div(dcc.Dropdown(id='a-my-dropdown', multi=True, options=[{'label':'1A Aluminium Content', 'value':'1A-Al'}, {'label':'1A Phosphate Content', 'value':'1A-Phosphate %'}, {'label':'1A Free Acidity', 'value':'1A-FA'}, {'label':'1A Total Acidity', 'value':'1A-TA'}, {'label':'1A Fluoride', 'value':'1A-Fluoride'}, {'label':'1B Aluminium Content', 'value':'1B-Al'}, {'label':'1B Phosphate Content', 'value':'1B-Phosphate %'}, {'label':'1B Free Acidity', 'value':'1B-FA'}, {'label':'1B Total Acidity', 'value':'1B-TA'}, {'label':'1B Fluoride Content', 'value':'1B-Fluoride'}, {'label':'Desmut Total Acidity', 'value':'DS-TA'}, {'label':'Pre-Treatment Total Acidity', 'value':'PT-TA'}, {'label':'Pre-Treatment Free Acidity', 'value':'PT-FA'}, {'label':'Pre-Treatment Aluminium Content', 'value':'PT-Al'}, {'label':'Common Rinse pH', 'value':'CR-pH'}, {'label':'Final Rinse pH', 'value':'FR-pH'}])),  
		html.Button(id='a-my-button', n_clicks=0, children='Show Breakdown'), html.Div(dcc.Graph(id="a-graph-output", figure={})), 
		dbc.Row([dbc.Col(html.Div(html.Img(src='data:image/png;base64,{}'.format(faas_image), style={'padding':30, 'textAlign': 'center', 'height':'50%', 'width':'50%'}))), dbc.Col(html.Div([faas0, faas1, faas2, faas3], style={'padding':30}))]),
		dbc.Row([dbc.Col(html.Div(html.Img(src='data:image/png;base64,{}'.format(phosv_image), style={'padding':30, 'textAlign': 'center', 'height':'50%', 'width':'50%'}))), dbc.Col(html.Div([phos0, phos1, phos2, phos3], style={'padding':30}))]),
		dbc.Row([dbc.Col(html.Div(html.Img(src='data:image/png;base64,{}'.format(lg_image), style={'padding':30, 'textAlign': 'center','height':'50%', 'width':'50%'}))), dbc.Col(html.Div([fluor0, fluor1, fluor2, fluor3], style={'padding':30}))]),
		html.H4(children="Latest Results Tank A", style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(A_table),html.H4(children="Latest Results Tank B", style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}),  html.Div(B_table), html.H4(children="Latest Results Desmut", style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(DS_table), html.H4(children="Latest Results Pre-Treatment", style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(PT_table), html.H4(children="Latest Results Common Rinse", style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(CR_table), html.H4(children="Latest Results Final Rinse", style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(FR_table),dbc.Row([dbc.Col(html.Div(apanel_button))]), dbc.Row([dbc.Col(html.Div(CA_Card)), dbc.Col(html.Div(Tank_Card))])])])])
     
    elif pathname == "/page-2":
        return html.H1(children="Waste Water Results", style={'fontSize': 30}), html.Div(dbc.Row([dbc.Col(html.Div(WW_button)), dbc.Col(html.Div(ww_data_button))])), html.Div(html.Img(src='data:image/png;base64,{}'.format(waste_image), style={'height':'50%', 'width':'50%'}), style={'textAlign':'center'}), html.H2(children='Anglian Water Test Results', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(ww_table, style={'size':'sm', 'fontSize':15}),html.H2(children='Internal Test Results', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(dbc.Row([dbc.Col(html.Div(dcc.Graph(id='plotww', figure=figww1))), dbc.Col(html.Div(dcc.Graph(id='plotww', figure=figww2)))]))
     
    elif pathname == "/page-3":
        return html.H1(children="Chemical Stock", style={'fontSize':30, 'padding':30}), html.H4(children="Last 80 Dose Summation: "), html.Div(dbc.Table.from_dataframe(hfsum)), html.H4(children= "Daily Dosing Data", style={'textSize':20, 'textAlign': 'center'}), dbc.Row([dbc.Col(html.Div(dosing)), dbc.Col(html.Div(cumdosing))])
    # If the user tries to reach a different page, return a 404 message
    elif pathname == "/page-4":
        return html.H1(children="Equiptment in Use", style={'fontSize':30}), html.Div(html.Img(src='data:image/png;base64,{}'.format(encoded_image), style={'height':'50%', 'width':'50%'}),style={'textAlign':'center'}), html.H4(children="Temperature Probes", style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(tanktemp_table), html.H4(children="*Note: 4-6 spares on site to be recorded", style={'textAlign': 'left', 'color': 'grey', 'fontSize': 10}), html.H4(children="pH Probes", style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}), html.Div(ph_table), html.H4(children="*Note: 7 spares on site to be recorded", style={'textAlign': 'left', 'color': 'grey', 'fontSize': 10})
    # If the user tries to reach a different page, return a 404 message 
    return dbc.Jumbotron(
        [html.Div(html.Img(src='data:image/png;base64,{}'.format(ec_image))),
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

#----tank a/b dropdown graph----
@app.callback(Output(component_id='tanka-graph-output', component_property='figure'), [Input(component_id='tanka-my-button', component_property='n_clicks'), State(component_id='tanka-my-dropdown', component_property='value')])

def update_my_graph(n_clicks, val_chosen):
	dff=dfhist
	fig=px.scatter(dff, x="Date", y=val_chosen)
	return fig

@app.callback(Output(component_id='tankb-graph-output', component_property='figure'), [Input(component_id='tankb-my-button', component_property='n_clicks'), State(component_id='tankb-my-dropdown', component_property='value')])

def update_my_graph(n_clicks, val_chosen):
	dff=dfhist
	fig=px.scatter(dff, x="Date", y=val_chosen)
	return fig	
	
#--- temperature readings graph----
@app.callback(Output(component_id='btemp-graph-output', component_property='figure'), [Input(component_id='btemp-button', component_property='n_clicks'), State(component_id='btemp-my-dropdown', component_property='value')])

def update_my_graph(n_clicks, val_chosen):
	dff=tanktemp_data
	fig=px.scatter(dff, x="Date", y=val_chosen)
	return fig

@app.callback(Output(component_id='atemp-graph-output', component_property='figure'), [Input(component_id='atemp-button', component_property='n_clicks'), State(component_id='atemp-my-dropdown', component_property='value')])

def update_my_graph(n_clicks, val_chosen):
	dff=tanktemp_data.tail(150)
	fig=px.scatter(dff, x="Date", y=val_chosen)
	return fig



@app.callback(Output(component_id='a-graph-output', component_property='figure'), [Input(component_id='a-my-button', component_property='n_clicks'), State(component_id='a-my-dropdown', component_property='value')])

def update_my_graph(n_clicks, val_chosen):
	dff=dfhist
	fig=px.bar(dff, x="Date", y=val_chosen, barmode="group")
	return fig
	
#---Phosphate calculation------
@app.callback(
    Output('phosphateA', 'children'),
    Input('num-multia', 'value'))
def callback_a(x):
    return round(((2571-((x*0.08635)/100)*67675.44)/12.0849),2)
	
@app.callback(
    Output('phosphateB', 'children'),
    Input('num-multib', 'value'))
def callback_a(x):
    return round(((5510-((x*0.08635)/100)*145018.8)/12.0849),2)
#-------------------------------

#----chemical stock functions----

@app.callback(
	Output(component_id='dose-graph-output', component_property='figure'), 
	[Input(component_id='dose-my-dropdown', component_property='value')])
def update_test_graph(val_chosen):
	df_dose=dosing_data.tail(60)
	dff_dose=df_dose[df_dose["Chemical"]. isin(val_chosen)]
	fig=px.bar(dff_dose, x="Date", y="Target Dose (L)", color="Chemical", barmode='group')
	return fig
	
@app.callback(
	Output(component_id='cum-graph-output', component_property='figure'), 
	[Input(component_id='cum-my-dropdown', component_property='value')])
def update_test_graph(val_chosen):
	df_dose=dosing_data.tail(80)
	dff_dose=df_dose[df_dose["Chemical"]. isin(val_chosen)]
	fig=px.ecdf(dff_dose, x="Date", y="Target Dose (L)", color="Chemical", marginal="histogram", ecdfnorm=None)
	return fig
	
	

@app.callback(
    Output('dosetable', 'data'),
    [Input('table-date-range', 'start_date'),
     Input('table-date-range', 'end_date')]
)
def update_output(start_date, end_date):
    dff = dosing_data.loc[start_date:end_date]
    dosetab=(dff.groupby(['Chemical']).sum().groupby(level=[0]).cumsum().reset_index())
   # dosetab=dosetab.to_json(orient="records")
   # parsed = json.loads(dosetab)
   # dosetab=json.dumps(parsed, indent=4)
    return dosetab.to_dict('records')
#---------- email -------
#port = 465
#password=input("Kob14458")
#context = ssl.create_default_context()

#with smtplib.SMTP_SSL("nadine.symonds@cellbond.com", port, context=context) as server:
#	server.login("my@cellbond.com", password)
# https://realpython.com/python-send-email/#including-html-content

	
if __name__ == '__main__':
    app.run_server(debug=True)    
