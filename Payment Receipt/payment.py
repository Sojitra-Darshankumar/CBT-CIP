# imports module 
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle , Image
from reportlab.lib.units import inch
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Register the custom font
pdfmetrics.registerFont(TTFont('NewAmsterdam-Regular', 'fonts/NewAmsterdam-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Exo', 'fonts/Exo-VariableFont_wght.ttf'))
pdfmetrics.registerFont(TTFont('Playfair_Display', 'fonts/PlayfairDisplay-VariableFont_wght.ttf'))
pdfmetrics.registerFont(TTFont('Roboto', 'fonts/Roboto-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Bold', 'fonts/Roboto-Bold.ttf'))


DATA = [ 
	[ "RECEIPT" , "", "","",""], 
	[ "", "", "","",""],
	[ "RECEIPT NUMBER :" , "DATE OF ISSUE :", "","",""], 
	[ 
		"0001", 
		"DD/MM/YYYY", 
		"",  
        "",
        ""
	], 
	[ "", "", "","",""],
	[ "BILLED TO :", "YOUR COMPANY NAME :", "", "",""], 
	[ "client name", "building name", "+91 12345 xxxxx", "",""], 
	[ "123 your street", "123 your street", "youremail@gmail.com", "",""], 
	[ "City, State, Country", "City, State, Country", "www.yourwebsite", "",""], 
	[ "Zip code", "Zip code", "", "",""], 
	[ "Phone", "Phone", "", "",""],
	[ "", "", "","",""],
	[ "", "", "","",""],
	[ "Desciption", "", "Unit Cost","QTY","Amount"],
	[ "", "", "","",""],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "Your item name", "", "0.00","1","0.00"],
	[ "", "", "","",""],
	[ "", "", "","",""],
	[ "", "", "","Sub Total","0.00"],
	[ "", "", "","Disconut","0.00"],
	[ "", "", "","Tax rate","0%"],
	[ "", "", "","Tax","0.00"],
	[ "", "", "","",""],
	[ "TERMS", "", "","","PAID"],
	[ "Please pay invoice by DD/MM/YYYY", "", "","","0.00"],
    
] 

image_path = "image/logoforpdf.jpg"

DATA[0][4] = photo = Image(image_path, width=1.5*inch, height=1.5*inch)

pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 

styles = getSampleStyleSheet() 

hex_color = colors.HexColor("#8d99ae")

style = TableStyle( 
	[ 
        ( "SPAN", (0, 0), (3, 0)),
		( "ALIGN" , ( 0, 0 ), ( 0, 0 ), "LEFT" ), 
		( "FONT" , ( 0, 0 ), ( 0, 0 ), "Roboto", 25 ), 
		( "TEXTCOLOR" , ( 0, 0 ), ( 0, 0 ), hex_color ), 
		( "TEXTCOLOR" , ( 1, 0 ), ( -1, 0 ), colors.black ), 
		( "FONT" , ( 0, 2 ), ( 3, 2 ), "NewAmsterdam-Regular", 11 ),
		( "TEXTCOLOR" , ( 0, 2 ), ( -1, 2 ), hex_color ),
		( "FONT" , ( 0, 5 ), ( 3, 5 ), "NewAmsterdam-Regular", 11 ),  
		( "TEXTCOLOR" , ( 0, 5 ), ( -1, 5 ), hex_color ),
        ( "SPAN", (4, 0), (4, 4)),
        ('SPAN', (0, 13), (1, 13)),
		( "FONT" , ( 0, 13 ), ( -1, 13 ), "Roboto-Bold",10 ), 
		( "BACKGROUND" , ( 0, 13 ), ( -1, 13 ), colors.lightblue ), 
        ('LINEBELOW', (0, 13), (-1, 13), 1, colors.black),
		( "BACKGROUND" , ( 0, 15 ), ( -1, 15 ), colors.lightgrey ), 
        ('SPAN', (0, 15), (1, 15)),
        ('SPAN', (0, 16), (1, 16)),
		( "BACKGROUND" , ( 0, 17 ), ( -1, 17 ), colors.lightgrey ), 
        ('SPAN', (0, 17), (1, 17)),
        ('SPAN', (0, 18), (1, 18)),
		( "BACKGROUND" , ( 0, 19 ), ( -1, 19 ), colors.lightgrey ), 
        ('SPAN', (0, 19), (1, 19)),
        ('SPAN', (0, 20), (1, 20)),
		( "BACKGROUND" , ( 0, 21 ), ( -1, 21 ), colors.lightgrey ), 
        ('SPAN', (0, 21), (1, 21)),
        ('SPAN', (0, 22), (1, 22)),
		( "BACKGROUND" , ( 0, 23 ), ( -1, 23 ), colors.lightgrey ), 
        ('SPAN', (0, 23), (1, 23)),
        ('SPAN', (0, 24), (1, 24)),
		( "BACKGROUND" , ( 0, 25 ), ( -1, 25 ), colors.lightgrey ), 
        ('SPAN', (0, 25), (1, 25)),
        ( "ALIGN" , ( 0, 13 ), ( 1, 25 ), "LEFT" ),
        ( "ALIGN" , ( 2, 13 ), ( -1, 25 ), "RIGHT" ),
        ('LINEBELOW', (0, 26), (-1, 26), 1, colors.black),
        ( "ALIGN" , ( 3, 28 ), ( -1, 31 ), "RIGHT" ),
		( "FONT" , ( 0, 33 ), ( 0, 33 ), "Roboto", 8 ), 
        ( "ALIGN" , ( 4, 33 ), ( 4, 33 ), "RIGHT" ),
        ( "FONT" , ( 4, 33 ), ( 4, 33 ), "Roboto-Bold", 13 ),
        ('SPAN', (0, 34), (1, 34)),
		( "FONT" , ( 0, 34 ), ( 0, 34 ), "Roboto", 8 ), 
        ( "ALIGN" , ( 4, 34 ), ( 4, 34 ), "RIGHT" ),
        ( "FONT" , ( 4, 34 ), ( 4, 34 ), "Roboto-Bold", 13 ),

	] 
)

table = Table( DATA , style = style ) 

pdf.build([ table  ]) 
