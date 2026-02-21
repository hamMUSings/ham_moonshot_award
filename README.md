# Introduction

Ham radio operators love their awards.  Some are very serious and require confirmation of QSOs like ARRL DXCC Award and there are other less prestigious club awards where it may be enough to sign a form saying you have QSL confirmation but do not need to prove it.

The one thing most of them have in common is awards are based on number of entities contacted in some given region or classification.  IARU Region 3, Worked All US States, DXCC, etc and then often a breakdown into bands like IARU Region 3 on 12 meters for example.  I enjoy other odd duck awards or processes.  Almost a different way of graphing activity. And I like stunning images or awards.  Turns out nature had done most of my work for me I just had to look up.

The Moonshot Award

Measuring how far you have two communicated via radio in comparison to celestial bodies in our solar system.

After making an HF contact almost 1/2 way around the earth I realized anything Earth Based for distances wasn't going to cut it -- but the moon and pluto are very far away! AND NASA has some nice images we could use.

This script will produce one high resolution jpeg for an overall award which will list each celestial body AND the date/time you transmitted past it! 

> [!NOTE]
> There is no sort feature in the software so the date of 'passing' each celestial body is dependent upon the order of the entries in the ADIF file.  <br> <br> This was tested with an export from CloudLog and WaveLog but I assume most other software will also export in time order but that isn't tested nor even confirmed with CloudLog.  <br> <br>  If it is working as you add contacts the dates for each object should stay the same. If the dates slowly creep forward my assumption is wrong and a sort filter will need to be coded in.

It will also produce an award for each celestial body you have transmitted past.

![Overall award demo image](/examples/CALLSIGN_MoonshotSeriesAward.jpg)


![The Moon award demo image](/examples/CALLSIGN_MoonAward.jpg)

## Garbage In, Garbage out

This award is completely on the honor system as in no one will even been tracking who 'receives' it online.  It is entirely calculated and produced locally on your machine.  

With the solar system distances I also decided to not worry about if they were confirmed or not.  If you want to play on hard mode just make sure you only exported confirmed contacts to the ADIF file.  But for example, the moon is 0.0026 Astronomical Units (AU) from the Earth.  Pluto is 38.5 AU.  So 'cheat' away and count every radio contact you make if you like! 

On that same note the award isn't limited to only HF or any other boundaries.  You decided what boundaries you want for your award.  The easiest way to do this is to export a ADIF file from your logging software with only the QSO/QSLs you want to count.  If you want to include HF only and you have some say Satellite VHF contacts in your log: only export the HF ones. Same goes for band, mode, confirmation, etc.  

# ADIF Prerequisites

> [!IMPORTANT]
> Your ADIF needs to include distance for each contact.  

This software doesn't calculate the distance of a contact it solely reads it from the ADIF file. So any contact that is missing the DISTANCE tag in the ADIF data is skipped.

> [!NOTE]
> Ideally, the ADIF will have exported in chronological order.  If it doesn't then the date/times for the overall award may change and be incorrect.  If you notice this and your ADIF is in order please open an issue in github and I may try to resolve it.

# Technical Prerequisites

- Python 
-- Following Libraries
--- EasyGUI
--- adif_io
--- pillow

- ADIF Export File
-- With Distances calculated
-- ALL QSOs are included so pre-filter

> [!TIP]
> For users without a pre-existing python environment I recommend using [Thonny](https://thonny.org/) and installing the Libraries via it's plugin manager.  No CLI for python to learn!

# To use

Once the libraries are installed.

Open the Moonshot.py in Thonny and click Run

A GUI Will pop up asking for your Name and Callsign.  This is what is printed on the certificates.
![EAsyGUI Operator information collection screen](/examples/Op_Info.png)

> [!NOTE]
> If your name or callsign are to long it will go off the page on both sides.  You can resolve this by either A) Shorting the name/call to print or B) Changing the Text size in the script

A GUI will pop up for you to select your exported ADIF file.

It will then calculate and generate any earned award certificates in the folder the python script lives in.

# Credits

- All photos are courtesy of NASA via [NASA Image and Video Library](https://images.nasa.gov/)
- Certificate Border Image by [OpenClipart-Vectors](https://pixabay.com/users/openclipart-vectors-30363/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=147541) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=147541)

