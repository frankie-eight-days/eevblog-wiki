---
video_id: v4iFgukMwsI
title: EEVblog #715 - Mailbag
url: https://www.youtube.com/watch?v=v4iFgukMwsI
source: youtube-asr
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag, where I open my mail. Let's get straight into it. This one is from uh the United States of America, the United States Postal Service, Ever Reliable, Zapa, whoever Zapa is. Anyway, let's open it up. Thank you very much,

**Dave Jones:** Zapa. And we have Woohoo! t-shirts. Plus, I love it when you get a static shielding bag inside t-shirts. What have we got? Oh, excellent. Oh, it's a little Sean t-shirt. Excellent. Little Sean YouTube t-shirt. Awesome. And what else have we got? I

**Dave Jones:** don't actually I think I might have a crappy YouTube uh shirt somewhere, but these ones I quite like. Look at that. Brilliant. Considering that I make my living on YouTube, you'd think I'd like have all the merch, right? Nope. Black

**Dave Jones:** and red. Perfect. Thank you very much. Zapda. It is Zapda. That's his name. Uh, he's from Silicon Valley. Hopefully my Crocodile Dundee knife didn't slash the T-shirts. Yes. By the way, for those who are wondering, yes, this is the

**Dave Jones:** Crocodile Dundee knife. You know, that's not a knife. That's a knife. Yeah. and he's also into ARM processors and uh well he moved from AVR to ARM and now he's got himself a um designed a little um ARM mini

**Dave Jones:** development board [Music] and I have a little itty bitty chip but I have no board A a ha fell on the floor. Some keen eyed viewers no doubt saw that. Let's take a look. And here you go. This is what

**Dave Jones:** Zap's done. He got the board actually reviewed by uh the members on the EE blogger forum and he will actually uh supply this to anyone on the forum who uh pings him. So, it's a little um ARM uh mini board, the ARM Pro Mini based on

**Dave Jones:** presumably exactly the same identical pin out to the Arduino Pro Mini. And uh minimal design, integrated um uh USB serial, so you don't need the uh FTD external FTDI uh dongle. And uh optional $20 debugger, 64K of flash, 8K RAM, 4K

**Dave Jones:** squared PROM, 48 MHz. Oh, screaming along. um M0 core. So there you go. Um in a little 3D printed case by the looks of it. And I cannot get it out of there. So I don't know if it's like stuck down

**Dave Jones:** into it or whatever. I'm not sure what the deal is there. But um yeah, I can't get the damn thing out. So how am I supposed to put it on my breadboard? Not sure what's going on there. Hope I don't break

**Dave Jones:** it. And there's the schematic for it. and it uses the LPC 11 uh 11U series. There you go. That's the main MCU in it. Next up, one from the old dart. It doesn't say who it's from at all. So, uh

**Dave Jones:** I've got no real idea. Let's have a look. From anonymous. Thank you very much, Anonymous. Postcard. Oh, look at that. It's an Avro Vulcan. Ah, from Doncaster in the old dart, of course. Yes, the Vulcan famous um big delta

**Dave Jones:** wing. Uh the Vulcan. Here we go. Greetings from the UK. Pleasing find a random car accessory which I've yet to see anybody use. Um Sean B uh from the forum uh kindly funded getting this to you. Ah, thank you very much Sean. Uh

**Dave Jones:** keep up the good work, Orbus. Thank you very much, Orvis. So, I love planes, by the way. So, what do I do with the Yeah, it's on the front. The Yes, the Vulcan. Very nice. The Vulcan was like uh Cold

**Dave Jones:** War stuff. It was like the UK's um you know uh deep um penetration Soviet penetration bomber I think. Anyway, um we have one of these little um keyring torches. It's like a little snowmobile or something weird. Um an illuminating

**Dave Jones:** car message sign. Check it out. It's one of the smiley face on the stick it on the back of your car. Awesome. A battery powered display module for the back window. Wireless remote for the front. Pre-program messages. Easy suction cup.

**Dave Jones:** Oh, great. Distract the drivers in the back so that they slam right up your ass. That's a good idea. There you go. It's one of those um Yeah, it's got a lead matrix in there. It's not a Don't

**Dave Jones:** know if you can see that, but it's not like a complete matrix. It's uh well we'll crack that open. That's a 2-minute tear down. Let's go. Aha. It only has a set of uh like predefined functions here. Back off. Sorry. Thanks. And

**Dave Jones:** smiley face or wink. Jeez. Excellent. Let's have a look. And it's just got like an infrared uh thing here. There's an infrared on the back here. So, I have to like point against the wall and uh bounce it off. So, let's go. Smiley

**Dave Jones:** face. Tada. Look at that. Or wink. or back off, dude. I mean it. Sorry. Didn't mean to cut in. Didn't see you there. And thank you, So, yeah. But sorry, that's just a complete failure. As um Orbus said, he's never seen anyone

**Dave Jones:** actually using one of these things cuz yeah, they're just like a complete gimmick, distracting. H I don't think anyone would be caught dead with one of these things. And check it out. Completely old school. Everything through hole. Oh man. Rock bottom price.

**Dave Jones:** Rev 4.9. Jeez. What? At the design review meeting, they had to go, "Well, I don't I think we should add a wink in here." So, let's respin the board. Hey, that'll be fantastic. No AVR in this. It's an

**Dave Jones:** AT89C 2051. Really old school. Jeez, can you even get those anymore? And then apart from that, we've just got two uh uln 203 Darlington drivers there for the high current drive. But yeah, just all through hole singlesider board as well

**Dave Jones:** with all those jumper links. I've got to shave a few cents off. Actually, just imagine if these things were popular and they did take off like the, you know, stick on Garfield craze in the 80s, uh, for example, and every car had one. Oh

**Dave Jones:** man, couldn't you have fun with the um you know, just stick an infrared transmitter on your car and set everyone's silly little flashing lead side off. And of course, there ain't nothing doing on the bottom there. Just all a single-sided layout. They're done

**Dave Jones:** reasonably well actually to uh get the layout on there with as few jumpers as possible. There's our little infrared receiver just flapping around in the breeze there. And uh actually that's interesting. They've got, look, they've got two like they've

**Dave Jones:** got a a a proper actual uh receiver in there which has the um 37 kHz filter in it. And then what I mean it doesn't transmit back. I didn't think so. It must be another um infrared uh photo

**Dave Jones:** receiver there. Weird. Actually, that's an okay little uh platform. Just uh reconfigure that. But I mean, you can just uh reconfigure the um 8051 up here and uh well, you can't get to say anything, but I don't know, you get it

**Dave Jones:** to do something a bit more useful than the uh useless task that it was originally designed for. Anyway, so thank you very much, Orbus and Sha B. Hold on to your hats. There are different models. Look at this. We've

**Dave Jones:** got the uh you can get five different faces. This is the one we've got. It includes the sorry thing. This is my personal favorite. It's got the middle finger. Yes. And that animating bloody messages. What do you want? Freaking

**Dave Jones:** animated emoticons like you're on a bloody forum when you're driving. And the plot thickens. Here we go. The drive motion it's called is an AU limited product. This mob Aumy are one of these companies who uh design, manufacture,

**Dave Jones:** promote, and distribute products. So, if you're an inventor in quote marks and you've come up with this brilliant idea, which obviously somebody did, the drive motion illuminating car message sign, then you uh you know, you have no idea. You you're you're the inventor.

**Dave Jones:** Oh, you know, you just leave it up to the Oompa Loompas of the world to you know, figure out how to um you know, design and manufacture and do everything. You know, you're just the ideas person. You don't need to worry

**Dave Jones:** about that practical crap. So you go to a company like this, you pay them a buttload of money and they design, manufacture, and promote and do everything. So yeah, I suspect the only winner in this is this company who took

**Dave Jones:** all that sucker's money, who came up with the concept of this thing. Next up, one from Hum. Hyum Fairbanks. Thank you very much, Hyum. That's what I'll call you. Um, sorry if I've got it wrong. Everyone knows I am

**Dave Jones:** awful with pronunciations. And I do like what's inside here. It's one of my favorite mailbag items to get. Let's have a look. It is Oh, for all you fanboys or you TI fanboys, it's a TI Voyager calculator. That's the Yeah, the Voy

**Dave Jones:** Voyage. Sorry. The Voyage 200. I'll get a whole bunch of hate mail if I get it wrong um from the TI fanboys. That's one of their um top line I think is is it late 90s? I think the Voyage 200. I'm

**Dave Jones:** not entirely sure. We have the um serial cable. Looks like RS232 with a TRS jack on it. And Nano Beam. What is Nanobam? They got some nice little Well, I have to show the those up close, but uh we got some nice

**Dave Jones:** little stuff for assembling some sort of frame, something like that. Got to read the note. And here's Hyram's Nano Beam. Check this out. This is a Kickstarter uh that he did. He raised only was asking for like 12 grand. He raised like 27

**Dave Jones:** grand. So, it was a success. I assume it is the world's smallest T- slot construction beam. Look at that. It is absolutely tiny. It weighs practically nothing. It's pretty darn strong. Yeah, I could probably bend that if I really

**Dave Jones:** wanted to. Um but it's it's wickedly strong for its um size and weight. Very nice. And it comes with all these tiny little um you know, plates and screws and brackets just like your regular um T-lot stuff. Even comes with a little

**Dave Jones:** screwdriver. Check it out. And uh check out his Kickstarter video. It's really interesting. He's made like a little robot out of this. He was here's his uh dragoon. There it is. Um made just out of this. Just, you know, a couple of um

**Dave Jones:** slots of this. You can cut it, of course. You don't have to buy it in um in in, you know, pre-cut lengths. You can easily just hacksaw that. Um and you can build pretty much anything. He shows like building a little mini picture

**Dave Jones:** frame with it. isn't even says you could uh do your own do-it-yourself um smartwatch um case. It's that tiny. Yeah, you probably could be a little bit bulky, but jeez. And by the way, it does ta I'm sure, not by not by coincidence,

**Dave Jones:** fit a 1.6 mm PCB in there. Nice. Look at that. So, you could actually, you know, make make your own custom uh make your own custom box out of this thing with the angle and then manufacture the PCB,

**Dave Jones:** the sides and the front panel, the back panel, the top, and everything else. You can actually manufacture your own cases out of that. That's really quite nice. I like that. I'll link it in down below. Check it out. The Nano Beam. And for all

**Dave Jones:** you TI calculator fanboys out there, I know there's a lot. This is the uh Voyage 200. Let's take a quick twominute tear down of this 19 uh 2002 vintage ump. Sorry, it takes a bunch of uh AAA four AAA batteries in there. Got a

**Dave Jones:** backup coin cell. Let's check out inside. Um absolutely useless as a day-to-day C because look, no exponent button at all. Hopeless. You got to well, you got to do shift, you know, second to do your bloody exponent. Ah,

**Dave Jones:** screw that. And there you go. very typical construction of these types of uh calculators in this sort of vintage. They haven't gone for like any chip on board or anything like that or quad flat packs. And it looks like its code name

**Dave Jones:** was Sylvester. There you go. This is a RevG. So, I'm sure that is the uh that is the code name for it. Let's have a look. And there's the main ASIC chip. It's the TI ref. And this is used in several of uh

**Dave Jones:** TI's uh calculators, but that is a custom ASIC. But look, the main CPU is actually down here. And that's a Motorola 68,000. And there it is up close for all you 68,000 fanboys. Ah, old school. Then all the other beasts on

**Dave Jones:** here, all these Toshiba parts, they're just LCD drivers. Dead giveaway, of course. All the huge tracks going off there. They're all over the place. Um, that's just uh some sponge there for the uh back of the batteries. And there's

**Dave Jones:** another one over there. Um, there's actually five of those uh total on there for the LC for the dot matrix LCD display. And not much else. There's an interface connector up there. And uh, yeah, all miscellaneous support stuff.

**Dave Jones:** Got to have a 74HC 244 in there. Of course you do. Jeez. LM324. What next? A triple 5 timer. Getting close. Got a nan gate. Got a couple of voltage regs down in there, I'm sure. And uh that's about all she

**Dave Jones:** wrote. There we go. There's our watch crystal in there. That'll be handling our real time clock. And it's about all. So, thank you very much, Hyram, for both of those items. And uh that's a quick look inside an old school TI calculator.

**Dave Jones:** There's a bit of a uh flame war going on on the EV logger forum about, oh, what use of bloody calculators, etc., etc. Well, you know, why don't you just use your smartphone? Oh, goodness sake. These things actually get long battery

**Dave Jones:** life. They've got excellent built-in functionality and they're dedicated to the task and they're they sell them for like more than, you know, a a decade or something like that. They still support them. So, that's, you know, valuable in

**Dave Jones:** like a um a classroom specified into a classroom curriculum and things like that. When teachers write a curriculum, they don't want to write it around some bloody smartphone app that may not be there in a couple of years time. No,

**Dave Jones:** they want to dedicate it to a calculator, something like this, the Voyage 200. Whether or not you support, you know, whether or not people should be forced to buy calculators like this for learning math in schools, eh, that's

**Dave Jones:** a different argument entirely. But that's why these sorts of things still exist. And well, they existed then and in 2002, and they still exist these days in a slightly more advanced form factor, although they're many generations behind in terms of like, you know, LCD,

**Dave Jones:** display, processing power, all that sort of stuff. H, you're missing the point. Next up, looks like our friends at Elector have sent us something again. We've had a few Elector things on here before. Please excuse the crude opening

**Dave Jones:** of that. Ah, another shirt. Jeez, I'm rolling in t-shirts. The wife complains about that. I've got too many t-shirts and I leave them scattered around the place. What What do we got? T-board by Elector Labs. I guess we're going to get a T-board. It

**Dave Jones:** is a T-shaped PCB. I wonder what it does. And Tetris. Yes, there you go. It is a T-shaped board. Why? Um, I'm not entirely sure. I guess they And I got a couple of other little T-shaped boards here. I guess they all joined together

**Dave Jones:** in a Tetrislike arrangement, hence the t-shirt. Huh. Further investigation required. And here's the Elector Tardo 80 at Mega 328. And you can see where this is going. Yes, it's an Arduino breadboard thing, which just um breadboard friendly. It's designed to,

**Dave Jones:** you know, if you want to step up from the breadboard, for examp uh from the Arduino, for example, but you want to just deal directly with the raw microcontroller and you don't, you know, and you want to interface stuff to it.

**Dave Jones:** This just gives you an easier way to do it. Plug it into your breadboard, things like that. So, we got the power, the voltage rag, and the um serial programming interface as well. They've got different types, they've got smaller

**Dave Jones:** ones, and they got the little eightpin jobby as well. So, they're kind of neat. But yeah, every man this dog's doing a different uh variant on, you know, how to transition from an Arduino over to your own custom prototype. This is yet

**Dave Jones:** another way. And it's not bad. And it does actually fit on a breadboard. Neat. Next up, one that's been sitting around for a while. Sorry to Lincoln uh Wsham. He's from San Jose in California. I don't mind San Jose. A nice little uh

**Dave Jones:** nice little city. Or is it? Yeah, it's a city, isn't it? San Jose, the city of San Jose. It's not really a town. It's big enough to be a a city. Anyway, it's the heart of Silicon Valley, of course.

**Dave Jones:** And uh they did have quite a bit of art there on the streets when I was there, wandering through San Jose. I rather some random art just scattered around, but I like San Jose. So, thank you very much, Lincoln.

**Dave Jones:** Include a couple of factory samples. Ooh, okay. Let's have a look. What have we got? Oh, look at this. Texas Instruments linear products when they used to give you the chips on the front. Check it out. And then they'd give you

**Dave Jones:** the little data sheets. All the data sheets inside there. And uh Yeah. Jeez, that's dating and back. Wow. Those were the days. That would have been Yeah. late 80s, early 90s perhaps. Awesome. And more linear products. Advanced Lin

**Dave Jones:** Camos op amps. Terrific. And a look at this. This could be a two-minute tear down. It's a data precision multimeter. Get my face tracking off. Look at that. There it is. Wonder if it works. And Lincoln is from Yes. USA. USA. USA. He's

**Dave Jones:** got here. Um and he was um uh worked at um he was an intern at uh the Ames NASA uh research place at uh Moffett Field there and uh he scored a whole bunch of um stuff from a guy who used to work

**Dave Jones:** there and these data precision multimeters. He got this on eBay and it didn't work and he said there's too much to fix. Quote end quote. So yeah, we'll just have a two-minute tear down and see what's inside them. Jeez, data

**Dave Jones:** precision multimeters. I don't make them anymore. They're a bit really, you know, they're very sort of um like that's like a pack tech case. That's like a standard Pack Tech model or brand uh case. They just sort of, you know, build them. Back

**Dave Jones:** in the day, they used to build multimeters. No, none of this custom stuff. They just build them in these like offthe-shelf uh cases and just due to the uh punched and silk screen front chassis. And that's about all she

**Dave Jones:** wrote. 2-minute tear down time. And let's take a look inside Lincoln's Data Precision 2480R multimeter. And oh, I wish this was smellvision. Oh, that's got the real old school smell. Look at that. I'm surprised they've gone with the big uh

**Dave Jones:** metal shield there. Anyway, everything's nicely uh labeled. They've got the adjustment uh trim pot and trimmers for your high frequency adjusting your other uh uh resistor trimmers down there. And very old school taped uh double-sided. And of course, your classic for the era,

**Dave Jones:** by the way, which is, tada, 1978. What a good year that was. And uh yeah, your classic uh rolled tin board and then solder coated, hence you get the crinkly uh stuff. You can't really see it down on that one. There's a few

**Dave Jones:** places where it does that, but yeah, very typical of the era. And what's the bet? There's an IC multimeter chipset under there, and that's pretty much it. No, it's not. What is that puppy? an SC TR40. Never heard of. Is that some sort

**Dave Jones:** of uh uh data precision custom job or is it some other uh manufacturer that we've never heard of? Anyway, there's an LF351 and there's not much else in there. Look at all that classic hand taped layout. A love it. 74 Couble O. Gez, you don't see

**Dave Jones:** much of 74 C series stuff anymore. Oh, look at that little little piss ant transformer down in there. It doesn't need much more than that, of course. But yeah, just a bridge rectifier linear power supply and Bob's your uncle.

**Dave Jones:** There's your multimeter. I don't know what the specs of this thing were, but yeah, like yeah, 4 and a half digit. And the spec was pretty darn schmick on this thing, actually. 4 and a half digit. 03 uh% plus one digit oneyear spec. Pretty

**Dave Jones:** darn impressive for the era. This would have been a top-of-the-line multimeter back in the day would have cost a fortune, I'm sure. And even on the ohms range, um, the best range there was like a 0.05% plus a couple of digits.

**Dave Jones:** Unbelievable beauty. Thank you very much, Lincoln, for sending that in. Excellent. A classic old school multimeter. If I can find info or anyone's got info on that chipset, let us know. And it's not every day we get one from Spain. So, hi to all my Spanish

**Dave Jones:** viewers. I don't know where Spain ranks on my uh YouTube uh scheme of things for number of viewers, but I think it's right down there. But there is certainly a contingent. This one comes from Ivan um Araka Stain. Got it wrong. Um Aedia Aedia in

**Dave Jones:** Spain. So awesome. Thank you, Marvan. Let's have a look. Ah, that was that was pretty piss poor. Ah, because I hit the um I hit the tape. That's why. And it just didn't miss it. So much for the

**Dave Jones:** crocodile undy knife. I'm not wielding it properly. What's Ivan sent? Oh, it's a um a test board accepts RF energy from 60 Hz to 66 gig and converts the signal to a DC voltage. So, it's like an RF

**Dave Jones:** energy harvesting um uh doodad. Awesome. Hey, you can do some experiments on that. Definitely. I wonder if that's his Wonder if that's his design. A look at There he is. There he is. Good day, Ivan. Look at that. Ah, beautiful. Wish

**Dave Jones:** I was there. That's That's fantastic. Wow. Never been to Spain. Ah, missed it on my world trip. Definitely have to get there one day. And it turns out that Ivan does some pretty funky woodworking stuff. Look at this. He's got a wooden

**Dave Jones:** um and info wood info panel. He's got a a sound dock, a massive sound dock for an iPhone. Is that like the world's biggest sound dock? I don't know. Look at this awesome wooden bike. That's just great stuff. I'll link in uh these down

**Dave Jones:** below. Or you could scan in the barcode if you're that keen. And a um touch sensitized furniture. And look at that notebook. and not operational, of course. But hey, that looks jazzy. Fool people in the park. I love it. Anyway,

**Dave Jones:** he works as an electronics engineer for Technalica, um, if I'm pronouncing that correctly. Um, and he wants to specialize in energy harvesting and, uh, he sent in this board, which I have to do a separate video on so that we can, it's basically

**Dave Jones:** RF in, as I said, up to, uh, 6 gig, um, 60 Hz to 6 gig, RF in, and then basically DC out. We'll have to have a look at the, uh, chipset. I'll link in the, um, data sheet for that. But yeah,

**Dave Jones:** I'll do a separate video on that. I'm interested in energy harvesting stuff. And he wants to know what uh path to follow, courses, conferences, tutorials, um that sort of stuff to get him on his way. Well, I don't know offh hand. So,

**Dave Jones:** I'm going to throw that over to the uh audience to help out Ivan. If you know of any good like online um courses and things like that for energy uh harvesting, then please leave it in the comments and Ivan can check them out.

**Dave Jones:** Thanks, Ivan. Next up, we got one from Conrad. uh mayor and he's from uh Constance in Deutseland, Germany. Man, do we get so many mailbags from Germany. It's unbelievable. It's not it's not uh terribly surprising because um Germany

**Dave Jones:** is like my second or third top um viewership. And he has sent in tada carefully wrapped up in tissue paper. Tada! An Arduino Mega. Thank you very much. I think I remember this. He um realized I didn't have one, so he

**Dave Jones:** decided to send me one. And that's the Here we go. Dear Dave, that's the Arduino Mega for the BAM and dice package because Conrad is from, as we've seen before, he's from the uh print, it's chopped off, but the print to beta

**Dave Jones:** mob. There we go. Printo beta. I'll link him in down below. They're the ones who did the 3D printer control board thingy. Link down below. Thanks, Conrad. Awesome. Don't have an Arduino Mega. So, that goes into the kit. So, there you

**Dave Jones:** have it. That concludes another mailbag Monday. Thank you for everyone who uh sends these in. Much appreciated. Keeps the segment going and people seem to love it as so. If you like it, please give it a big thumbs up or you can give

**Dave Jones:** it a thumbs down if you really want to. I know there's a core group of haters that thumbs down every video out there, but like within a minute of me uploading. Thank you very much. Always keeps me amused. Anyway, um let's take a

**Dave Jones:** look at this thing. I'm just gonna Yeah, old school data sheets with some chips. Ah, beautiful. I love it. Anyway, if you want the t-shirt, ta, there it is. I'll link it in down below. Warranty void if not removed shirt. And I'm

**Dave Jones:** wondering what happens if I send in this reply paid info card. I wonder if they're still there. A man, these were the days back when you had the magazines. You could actually Which of these following parameters would you

**Dave Jones:** like? I wonder if they're still running the survey and can send in the card from Hey, 91 expires. Ah, September 1st, 91. Damn it.
