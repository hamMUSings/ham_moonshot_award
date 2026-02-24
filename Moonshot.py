# Created by hammusings  - 2/26
# GPL v3
# https://github.com/hamMUSings/ham_moonshot_award

import easygui
import adif_io
from PIL import Image, ImageDraw, ImageFilter, ImageFont

award_chart = [["Moon", 0.0026, "moon"], ["Venus", 0.28, "venus"], ["Mars", 0.52, "mars"], ["Mercury", 0.61, "mercury"],["Sun", 1.0, "sun"],["Asteroid Belt", 1.8,"asteroidbelt"], ["Jupiter", 4.2,"jupiter"], ["Saturn", 8.54,"saturn"], ["Uranus", 18.2,"uranus"], ["Neptune", 29.06,"neptune"], ["Pluto", 38.5,"pluto"]]
awarded_date = [["Moon", ""], ["Venus", ""], ["Mars", ""], ["Mercury", ""],["Sun", ""],["Asteroid Belt", ""], ["Jupiter", ""], ["Saturn", ""], ["Uranus", ""], ["Neptune", ""], ["Pluto", ""]]

msg = "Please enter as you'd like to be printed on your Moonshot Award"
title = "Moonshot Award Operator Information"
fieldNames = ["Name","Call Sign"]
fieldValues = [] 
fieldValues = easygui.multenterbox(msg,title, fieldNames)
NameLine = fieldValues[0]+", "+fieldValues[1]
SeriesFilename = fieldValues[1] +"_MoonshotSeriesAward.jpg"

RAWADIF=easygui.fileopenbox("Select ADIF To Evaluate")
qsos, header = adif_io.read_from_file(RAWADIF, encoding="ISO-8859-15")

AU_KM=149597870.7
KM_MI= 0.621371
awarded_level=-1
award_distance=0

AwardStep=0

for contact in qsos:
    if contact.get("DISTANCE") is not None:
        num_distance=float(contact.get("DISTANCE"))
        award_distance=award_distance+num_distance
        AU_Award=award_distance/AU_KM
        if AU_Award > award_chart[AwardStep][1]:
            AwardStep=AwardStep+1
            awarded_level=awarded_level+1
            date_og=contact.get("QSO_DATE")
            time_og=contact.get("TIME_OFF")
            awarded_date[awarded_level][1]=date_og[4:6]+"/"+date_og[6:8]+"/"+date_og[2:4]+" "+time_og[0:2]+":"+time_og[2:4]

award_distance_decimal = "%.2f" % award_distance
award_distance_mi_decimal = "%.2f" % (award_distance/KM_MI)
award_distance_au_decimal = "%.6f" % AU_Award
print("Distance Traveled:")
print("   "+award_distance_decimal +" km")
print("   "+award_distance_mi_decimal +" mi")
print("   "+award_distance_au_decimal +" AU")

# Overall Award Creation

backim1 = Image.open('./backgrounds/moonshot-solarsystem.jpg')
cert_im = backim1.copy()

with cert_im.convert("RGBA") as base:
    font_choice = ImageFont.truetype("timesbd.ttf", 175)
    font_choice_dates = ImageFont.truetype("times.ttf", 70)
    draw = ImageDraw.Draw(cert_im)

    # Add Text to Each Celestial Body with the date if it exists
    draw.text((1650, 862), NameLine, font=font_choice, fill=(255, 255, 255, 255),anchor="mm")
    draw.text((625, 1840), "The Moon: "+awarded_date[0][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((475, 1390), "The Sun: "+awarded_date[4][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((625, 1540), "Mercury: "+awarded_date[3][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((475, 1690), "Venus: "+awarded_date[1][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((475, 1990), "Mars: "+awarded_date[2][1], font=font_choice_dates, fill=(255, 255, 255, 255)) 
    draw.text((625, 2140), "Asteroid Belt: "+awarded_date[5][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((1725, 1540), "Saturn: "+awarded_date[7][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((1575, 1390), "Jupiter: "+awarded_date[6][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((1575, 1690), "Uranus: "+awarded_date[8][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((1725, 1840), "Neptune: "+awarded_date[9][1], font=font_choice_dates, fill=(255, 255, 255, 255))
    draw.text((1575, 1990), "Pluto: "+awarded_date[10][1], font=font_choice_dates, fill=(255, 255, 255, 255))
 
    # Export actual JPG
    cert_im.save(SeriesFilename, quality=95)

# Individual Award Creation

####### Function Start
def printaward(award_index):
    backimIND = Image.open('./backgrounds/moonshot-background.jpg')
    planetimIND = Image.open('./celestial_bodies/'+award_chart[award_to_print][2]+'.jpg')
    cert_im = backimIND
    cert_im.paste(planetimIND, (2120, 1370))
 
    with cert_im.convert("RGBA") as base:
        font_choice_name = ImageFont.truetype("timesbd.ttf", 175)
        font_choice_cb_title = ImageFont.truetype("timesbd.ttf", 175)
        font_choice_cb_data = ImageFont.truetype("times.ttf", 100)
        draw = ImageDraw.Draw(cert_im)

        kms = round(award_chart[award_to_print][1]*AU_KM)
        mis = round(kms*KM_MI)
        au_line = str(award_chart[award_to_print][1])+" AU"
           
        if award_to_print == 0 or award_to_print == 4:
            celestial_name="The "+award_chart[award_to_print][0]
        else:
            celestial_name=award_chart[award_to_print][0]

        # Put Name on It
        draw.text((1650, 862), NameLine, font=font_choice_name, fill=(255, 255, 255, 255),anchor="mm")
            
        # Put Celestial Body Info on It
        draw.text((1150, 1525), celestial_name, font=font_choice_cb_title, fill=(255, 255, 255, 255),anchor="mm")
        draw.text((1150, 1750), f"{kms:,}"+" km", font=font_choice_cb_data, fill=(255, 255, 255, 255),anchor="mm")
        draw.text((1150, 1900), f"{mis:,}"+" mi", font=font_choice_cb_data, fill=(255, 255, 255, 255),anchor="mm")
        draw.text((1150, 2050), au_line, font=font_choice_cb_data, fill=(255, 255, 255, 255),anchor="mm")
           
        PlanetFilename=fieldValues[1]+"_"+ print_award[0]+"Award.jpg"
        cert_im.save(PlanetFilename, quality=95)

###### FUNCTION OVER

award_to_print=0

# force do print all for testing
#awarded_level=10

for print_award in award_chart:
    print("Checking: "+print_award[0])
    if award_to_print <= awarded_level:
        printaward(award_to_print)
        award_to_print = award_to_print+1


    
