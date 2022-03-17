from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Layout = [Template Name, [Custom Text]]
# Custom Text = ["Area Name": "Text Content"]
my_cert_req = ["Basic Template", [ ("Date", "16/02/1995"), ("Name", "Rose Rfffeade"), ("Sig", "JPNeedham"), ("Description", "Being born!") ]]

# Layout: [template_img_name, { editable areas dictionary }]
# Editable areas dictionary: { "Area Name": [x_pos, y_pos, font_size, font_name] }
cert_templates = {
"Basic Template": 
	[
	"template1.png", 
		{
		"Date":	[1075, 1750, 100, "BebasNeue-Regular.ttf"],
		"Name": [1755, 990, 200, "SansPosterBold.ttf"],
		"Sig": [2460, 1750, 100, "RemachineScript_Personal_Use.ttf"],
		"Description": [1755, 1395, 100, "BebasNeue-Regular.ttf"]
		},
	#LOGO x,y,scale_fac
	[450,350,1],
	],
"Red Template":
	[
	"template2.png",
		{
			"Date":	[866, 1940, 100, "BebasNeue-Regular.ttf"],
			"Name": [1755, 1075, 200, "SansPosterBold.ttf"],
			"Sig": [2590, 1940, 100, "RemachineScript_Personal_Use.ttf"],
			"Description": [1755, 1530, 100, "BebasNeue-Regular.ttf"]
		},
		#LOGO x,y,scale_fac
		[100,2000,1]
		]
}

def draw_text(img, text, font_name, size, pos):
	d1 = ImageDraw.Draw(img)
	myFont = ImageFont.truetype("fonts/"+font_name, size)
	img_w, img_h = img.size
	text_w, text_h = d1.textsize(text, myFont)
	d1.text((pos[0]-(text_w/2), pos[1]-(text_h/2)), text, fill=(0,0,0), font=myFont)
	return img

def draw_cert(cert_req):
	temp = cert_templates[cert_req[0]]
	img = Image.open('cert_templates/'+temp[0])
	for area in cert_req[1]:
		temp_details = temp[1][area[0]]
		draw_text(img, area[1], temp_details[3], temp_details[2], (temp_details[0], temp_details[1]))

	if cert_req[2][1] != "":
		print('F:/Personal Projects/Certificate Generator/user_uploads/'+cert_req[2][1])
		logoimg = Image.open(r'F:/Personal Projects/Certificate Generator/user_uploads/'+cert_req[2][1])
		logoimg.thumbnail((500,500), Image.ANTIALIAS)
		img.paste(logoimg, (temp[2][0], temp[2][1]))

	img.thumbnail((500,500), Image.ANTIALIAS)
	img_io = BytesIO()
	img.save(img_io, 'PNG', quality=70)
	img_io.seek(0)
	return img_io


