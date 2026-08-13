---
video_id: n_gfZsVb-SY
title: EEVblog #843 - David's rPrint 3D Printer Design
url: https://www.youtube.com/watch?v=n_gfZsVb-SY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 40, "3": 55, "4": 77, "5": 94, "6": 109, "7": 122, "8": 136, "9": 151, "10": 173, "11": 188, "12": 201, "13": 218, "14": 240, "15": 257, "16": 273, "17": 290, "18": 303, "19": 314, "20": 328, "21": 345, "22": 360, "23": 376, "24": 395, "25": 406, "26": 423, "27": 440, "28": 459, "29": 480, "30": 497, "31": 511, "32": 523, "33": 539, "34": 553, "35": 573, "36": 588, "37": 599, "38": 612, "39": 624, "40": 640, "41": 664, "42": 679, "43": 699, "44": 719, "45": 735, "46": 755, "47": 775, "48": 792, "49": 810, "50": 829, "51": 846, "52": 864, "53": 880, "54": 896, "55": 914, "56": 933, "57": 945, "58": 960, "59": 977, "60": 997, "61": 1018, "62": 1034, "63": 1049, "64": 1066, "65": 1082, "66": 1096, "67": 1110, "68": 1129, "69": 1149, "70": 1157, "71": 1174, "72": 1190, "73": 1210, "74": 1225, "75": 1243, "76": 1261, "77": 1278, "78": 1292, "79": 1307, "80": 1323, "81": 1339, "82": 1356, "83": 1371, "84": 1386, "85": 1399, "86": 1411, "87": 1424, "88": 1436, "89": 1450, "90": 1464, "91": 1476, "92": 1493, "93": 1506, "94": 1524, "95": 1543, "96": 1565, "97": 1585, "98": 1603, "99": 1621, "100": 1642, "101": 1661, "102": 1679, "103": 1695, "104": 1708, "105": 1725, "106": 1743, "107": 1761, "108": 1776, "109": 1790, "110": 1803, "111": 1822, "112": 1841, "113": 1864, "114": 1884, "115": 1899, "116": 1918, "117": 1940, "118": 1963, "119": 1981, "120": 1997, "121": 2017, "122": 2031, "123": 2046, "124": 2063, "125": 2081, "126": 2104, "127": 2121, "128": 2139, "129": 2164, "130": 2181, "131": 2199, "132": 2218, "133": 2244, "134": 2264, "135": 2283, "136": 2300, "137": 2324, "138": 2340, "139": 2355, "140": 2371, "141": 2389, "142": 2409, "143": 2424, "144": 2440, "145": 2460, "146": 2480, "147": 2494, "148": 2511, "149": 2528, "150": 2547, "151": 2567, "152": 2578, "153": 2598, "154": 2613, "155": 2629, "156": 2644, "157": 2657, "158": 2671, "159": 2685, "160": 2700, "161": 2720, "162": 2743, "163": 2762, "164": 2778, "165": 2794, "166": 2810, "167": 2824, "168": 2838, "169": 2854, "170": 2873, "171": 2891, "172": 2902, "173": 2920, "174": 2938, "175": 2954, "176": 2981, "177": 2996, "178": 3011, "179": 3028, "180": 3042, "181": 3058, "182": 3071, "183": 3085, "184": 3102, "185": 3112, "186": 3127, "187": 3138, "188": 3148, "189": 3160, "190": 3176, "191": 3190, "192": 3210, "193": 3229, "194": 3247, "195": 3263, "196": 3280, "197": 3295, "198": 3311, "199": 3327, "200": 3342, "201": 3355, "202": 3370, "203": 3385, "204": 3398, "205": 3415, "206": 3428, "207": 3441, "208": 3460}
---

**Dave Jones:** It's David. Hello. And if you've been wondering why David has not been in the lab for, I don't know, quite a long time. Yeah, yeah. Many, many months. This is why. It's the R-Print. Yep. And this is what you've been working on. This is your uni project.

**Dave Jones:** Tell us all about it. So, it's basically a 3D printer. I'll make this be quiet. Shush! So, it's basically a 3D printer. FDM. It's designed to be really nice and compact and just fit in places. So, it's designed to fit in shelves. Shelves.

**Dave Jones:** So, basically, like a normal printer. Because it doesn't seem like anyone cares in the 3D printer community where you're actually putting it. Right. Hence the full bubble enclosure. We'll take a good look at it up close soon. But, yeah, we're just going to talk about it.

**Dave Jones:** Extol the virtues of this thing. Why did you do it? I'll make that noise be quiet. And, oh. There we go. Oh. Yeah, no more high-pitched noises. Yeah, so, it's like, it's got a very lightweight extruder. It's a direct-derived one. Because Bowden type extruders have a bit of artifacting.

**Dave Jones:** Because they have the elasticity of the filament or the actual slack inside the Bowden tube. And either way, you end up with this slack, which you kind of have to compensate for. Or you have a bit of elasticity, which you also have to compensate for.

**Dave Jones:** It ends up being okay, but it's kind of irritating for the software. And the whole idea of this was to, like, redo the current software and make it, like, the actual control loops a lot faster. What current software are you specifically talking about?

**Dave Jones:** Well, the RepRaps, they all run on these, like, RAMP things. They're based on, like, Arduinos. And there's also a bunch of libraries, CNCs, which is actually kind of what I was comparing mine to, mostly. I can't remember the name of the library. It's an acronym.

**Dave Jones:** Ah, GRBL. So, the GRBL is a CNC project. It's basically like a, it's a G-code interpreter. Right. And, like, for the most part... And you didn't like it. Oh, well... You thought it could be done better. I thought it could be done better.

**Dave Jones:** Yeah, I definitely thought it... So, this is your uni project. Yeah, yeah. So, it's like a capstone thing. Currently, it's, like, it's a bit loose and stuff. Like, I haven't actually... What is capstone, for those who don't know? It's your final project. Oh, it's like a thesis project.

**Dave Jones:** Right. Some people... I don't know what the word means. Like, I don't... It feels very Egyptian. I've never heard of it. Before you mentioned, I'd never heard of capstone projects. So, it sounds very American to me. Yeah, I hadn't heard it either. So, basically, like, most of the previous generation ones, even the top of the line, they run at, like, 30 kilohertz, the control loop.

**Dave Jones:** Which is slow. It's pretty slow. And there's a lot of reasons for it. So, I tried to tackle them. So, you went better. So, you decided that this was your... Did they groan when you went, Oh, my capstone project, I want to build a 3D printer.

**Dave Jones:** No, no, not a lot of people were doing them. Really? Yeah, a lot of people were making, like... There's a lot of people making, like, remaking, I should say. Remaking RepRaps, and there are a few people who... And most of them are very derivative.

**Dave Jones:** Right. So, like, most 3D printers, like, you see one Delta, you've seen most Deltas. Right, Deltas, yep. You see one RepRap, you've seen 50% of them, and then the rest of them are just slight variations on a theme. So, I pretty much just threw away everything.

**Dave Jones:** And you decided to do everything from scratch. So, almost everything in here is your own design. Yeah, everything. Everything. The build plate, the extruder is your own design. Yeah, the extruder, even the controller, the front panel thing, the disassembly, every mechanical part. All the firmware, the G-code, you wrote your own G-code interpreter.

**Dave Jones:** Yep, G-code interpreter. It's got, like, ramping stuff in it. It's not actually activated at the moment, because the test you saw just then was just about the worst torture test you can do to a 3D printer. Just on, off, on, off. It's an instantaneous velocity change with zero ramping.

**Dave Jones:** So, like, that was kind of the showpiece that's like, look, I'm not losing position. And is that the main concern with fast, with lack of ramping, is you lose your positional, because there's no positional feedback. Yeah, you lose steps. You lose steps, yeah.

**Dave Jones:** I potentially can have positional feedback. So, this does actually have two linear potentiometers. They're just not wired in. Oh, right. It's actually got a control loop. So, is that actually an aim, to make it fully positional? It wasn't really an aim. I just wanted it to, like, I wasn't trying to make a full positional controller.

**Dave Jones:** I was trying to make it initialize quickly without it headbutting the side of the machine's end stops every time it turns on, which is, like, for some reason, annoys the heck out of me. So, how long did this take you from go to work?

**Dave Jones:** About seven months, eight months, maybe. Seven months. It's hard to tell, because I was, like, doing it at the same time. Like, for a few months, I was unsure about another project which was going on. And so, I started doing two of them simultaneously.

**Dave Jones:** And at that time, it was like, yeah, it was kind of half the time. So, I don't really know how long. Less than a year and more than six months. Right. And that's... That's more than full time. That's more than full time. More than full time.

**Dave Jones:** Yeah. And the other project was much more than full time. This was, like, a relief. How many hours a day would you spend on it sometimes? Sometimes? Yeah, sometimes. Eighteen? Yeah. It doesn't sleep. No. Sometimes. It would be, like, one hour a day.

**Dave Jones:** Sometimes. Yeah. It would be like, a week. Yeah. It's like, a week. It's like, a week. It doesn't sleep. No. Sometimes. It would be like... Like, there'd be certain parts. Like, the electronics, for example. When you're laying out a board and you're kind of, like, in the zone.

**Dave Jones:** You're in the zone. You kind of forget what the hell you're doing. Yep. And it's just like... And when you're optimizing software, too, as painful as it is, you also get in a zone. So, you're just kind of, like, phased out of existence and into codeland or...

**Dave Jones:** Yeah. Awesome. Yeah. Yeah. But you... It's effectively finished now because you've submitted it and you won. Yeah. I won a... I think it was an innovation prize. I think that's what it's called. Cool. Yeah. Excellent. Yeah. Well done. Yeah. Thank you. Yeah. Because it's strange.

**Dave Jones:** Most people don't finish stuff. Like, at all. Most people actually don't make anything at all. Yeah. Most... Oh, they're what? They're a theory project? What are they? Most... I thought the idea was you had to design and you had to implement something practical.

**Dave Jones:** I think that's what it was, like, intended to be. Right. But no one does it. Most people purely report on something. Maybe they'll do a very small portion of a design. So, a capstone project where they only design, for example, that pulley section and they're

**Dave Jones:** really focused on it would be quite typical. Or, like, maybe a few pulleys or something like that. Or a part of it, maybe just that one part. Usually it's a small scale. But it's not... I don't think it's meant to be. I didn't think it was either.

**Dave Jones:** Yeah. Now, it's called the rPrint. Am I pronouncing that correctly? Yeah. Why is it called the rPrint? So, there's kind of a long story behind that. So, products were going to be, and this is, well, it will be when the site's finished, all open source.

**Dave Jones:** So, open source is, like, for everyone. So, it's, like, our print. Our kind. rPrint. rPrint. There you go. That's the rPrint. That's just the thing that says... rPrint. rPrint. The printer for pirates. Beautiful. Now, what are the innovative features of this thing? It stole the virtues.

**Dave Jones:** Yeah. What makes it better than 10 million other 3D printers? So, we've got the extruder. It's the lightest weight direct drive probably ever. But that's really hard to know because no one keeps records. But... Let's get a close up of this. Let's go for the extruder first.

**Dave Jones:** Let's go through... I'll bring it to the front of the machine. The machine's off at the moment. Show us your groovy door. Tell us about the bubble first. Oh, yeah. Tell us about the bubble. Okay. So, this is a PMMA enclosure. What's that?

**Dave Jones:** It's a type of plastic which is cheap to make. Right. This is not what it would be made out of in production. What would it be made out of in production? Polycarbonate. Oh, okay. So, polycarbonate in prototyping is kind of a crazy thing to do.

**Dave Jones:** Right. Because you'll end up paying like a crazy amount of money. So, this is all PMMA. And it was made in sections by these wonderful people in China. And they basically... They've glued them. They've glued them. And they did it in a really cool way.

**Dave Jones:** It's super glue. Awesome. So, each of the seams is glued with super glue. And everyone's like, oh, that's going to be really brittle. Yeah, brittle. But super glue is essentially an acrylic. PMMA is an acrylic. And it ends up being like a solvent.

**Dave Jones:** Right. So, they're not actually using super glue for its gluing. They're using it as a solvent. It's solvent gluing. And you end up with these like really quite strong bonds. Apart from when FedEx threw it off a truck. Right. Yeah. It cost me quite a...

**Dave Jones:** It was a sad moment when it arrived. And it's like, oh, you've ruined everything. Yeah. And show us the door. Tell us about the door. So, the door is meant to be kind of like kind of tricky to take off. Because the machine was designed to move really fast.

**Dave Jones:** And I also wanted it to be in like just anywhere. So, there's all kinds of things where it's like you're not meant to be able to get around things with your fingers. So, it kind of stops you in the enclosure. So, the door does a similar thing.

**Dave Jones:** It's latching. So, you're not meant to be able to pull it out directly. Yep. So, the magnets just, they disagree with that substantially. You're meant to just pull it up. Pull it up. And the curvature in the enclosure just de-latches the door. So, it's quite easy.

**Dave Jones:** And also, the magnets are arranged so that if you do pull it up, it clips in like that. Clips in like that. And you can't put it on the wrong way. No. It's impossible. You might be able to put it on the upside down the wrong way.

**Dave Jones:** Well, maybe. Yeah. Some weirdo. It's probably our combination. The backward, upside down. Upside down backwards. Yeah. So, you can do that. So, there's innovation in the door. Yeah. There's innovation in the bubble. Is anyone else doing a bubble like this for a 3D printer?

**Dave Jones:** Nah. I think it's only in like Saturday's toasters and strange aquariums. Right. Yeah. Alright. So, the next innovation is the extruder. I shall stop and we'll get a close-up of the extruder. Oh, Jesus. Tripods. Bloody tripod. Alright. Tell us about the extruder, which you have designed and built yourself.

**Dave Jones:** Yeah. It's been tested outside the machine. It hasn't really been tested inside it yet. Right. It's been tested on the print bed, but in an external jig. Got it. Yeah. So, basically, it's just about 100 grams, which is lighter than the motors alone of

**Dave Jones:** most other systems. Extruders, really? Yeah. Right. All of the NEMA 17 extruders, I'm really nitpicking on the NEMA 17s because they're really easy to target. It's like, stop using those. Anyway, all of those are like 200 and something grams on just the motor.

**Dave Jones:** Yeah. So, this thing's like just about 100. It varies on some things. For example, this wheel here is actually a temporary part. The material we made it from broke in the FedEx incident. And we must say, it doesn't have all the cable guides and stuff like that on it yet.

**Dave Jones:** No, there's some missing. There's some parts that aren't in there yet. It has to be refined a bit. So, how does it work? How does it compare with other extruders? So, the extrusion rate's pretty comparable. Most of the extruders don't really peak out near that.

**Dave Jones:** So, was your design goal just to go for the lightest weight extruder possible so that you get the maximum velocity? Yeah, I was trying to get all the advantages of a Bowden extruder except with the weight, but with the direct drive. So, you can use elastic filaments and just not care.

**Dave Jones:** Got it. You can just be like, yes, go, elastic filament, and just not care. Yeah, so everything's designed to be just light. And it's also, I've got like, most extruders don't have position feedback for the actual filament. Or some of them do via encoders on the motors or encoders on the wheels.

**Dave Jones:** So, it's got positional feedback for the filament. Yeah, see this little tiny thing? That's a quadrature encoder. Why do you need positional? What's the advantage of having positional feedback for the filament? So, whatever you do, it's going to slip a little bit. Right, yes, yes.

**Dave Jones:** Whatever you do. And that might be negligible. So, is it for flow rate reasons? Not really. Well, yeah, flow rate control. Right. Or, like, you can control the amount you've done. And you can also, like, it's good for tuning the actual system. Like, the user wouldn't have to do that.

**Dave Jones:** But for people who are, like, tuning the machine and software and stuff, that's really good. Because you can know exactly, like, if your ramping of the extrusion is causing slippage or at what heats cause slippage. And you can just avoid them entirely. It basically gives you data that you can do stuff with.

**Dave Jones:** Yeah, data good. Data's good. Yep. Absolutely. Look up table. Good. Not really. Right, but apart from that, it's got a heatsink on it. It's got a fan, just like other extruders. Yeah, it's got, um, yeah, it's like 60 watts or something. And I can show you the nozzle on the bottom.

**Dave Jones:** It's just a teeny tiny top nozzle. Yeah, it's just a, it's very standard. It's lighter and I think it looks pretty cool, but it's just lighter. There we go. There it is. Pretty standard looking nozzle in there. Yep, it is a standard nozzle.

**Dave Jones:** Is that brass looking thing? Yeah, I was half tempted to redo the nozzles because I wanted them to, like, kind of, like, mix the filament a bit as it goes in. Right. But then I thought, nah, nah, I'm going to hate myself if I do this because

**Dave Jones:** every time I need a new, a new nozzle, I'm going to have to buy a new one from the manufacturer directly and instead of paying, like, four bucks, I'll have to fork out, like, way more for the custom part. Any thought for a dual extruder?

**Dave Jones:** Nah. Nah. I'm not, I'm not, I'm not big on dual extruders. I don't really care about the color. Right. Well, you can get two different types of material as well. Yeah, I care much more about material, but this is purely for prototyping and in that circle, like, when you're not trying to make, like,

**Dave Jones:** models or figurines, you really just want a really good print, which is printed quickly. Speed is the main thing with this thing. Speed is the thing. It's a prototyping machine. It's not, it would do Yoda's head excellently, I'm sure, but it is definitely not for Yoda's head.

**Dave Jones:** It's for, you know, for, you know, the mouse. Making 3D parts. A mouse body or something. Yeah, right. It's for that kind of thing. And you don't, like, when you do stuff like this, you don't care about the color. No. You could never get the finish on a 3D print you'd want

**Dave Jones:** for a prototype anyway. You'd have to do an after, a second process to do that. So I just, nope, not dual nozzle. Nope. All right. Yeah. Now, we've got the bed. Tell us about the bed because I, this is something I've not seen on others.

**Dave Jones:** You've got these supports down, oh, do that again. That was sexy. I'll bring it back up. All right. Notice that I'm actually spinning the motor forcefully and it doesn't matter because my controller is, like, not going to destroy itself. I was going to mention that.

**Dave Jones:** Yeah. Okay, ready? Yep, go. Oh. Hopefully you see through the bubble. The bubble's a problem. There's a hole. There is a hole. There is a hole? Well, move your laptop. Yeah, wait. Spin it around. Here we go. Let's have another look. So this is called a Saris linkage.

**Dave Jones:** Traditionally, the… Saris linkage. A Saris linkage. It's ancient. Right. It's, like, not this. It's not ancient. But the actual, like, idea of it is quite ancient. And it basically keeps a bed level using a bunch of hinges. It's great. And it means that I can put a motor in the back of it

**Dave Jones:** and not need to put another one in. I forgot that was there. It's see-through. Anyway, I don't have to put one in the front or the sides. A lot of 3D printers have two motors for the bed, which I think is crazy. Or big stiffener arms and things to hold the bed.

**Dave Jones:** Yeah, you have to buy the aftermarket ones. They're a pain in the ass. Yeah, it's kind of silly. No, it's terrible. Yeah, I much preferred just putting the back out of the way and it's all clear. Very, very nice. So, you've got a glass bed.

**Dave Jones:** Well, it's not… What type of glass is it? It's borosilicate glass, which is Pyrex, I think. I believe it is something like that. Yeah, I can take it out. It comes out. It comes out. Any reason to make it removable? You can remove your object.

**Dave Jones:** You don't have to whip. Is that the idea? Yeah, it's actually not the finished bed. I need one more substrate at the bottom. So, this isn't just a PCB. This is a bonded thing. Ah, right. Okay. So, I'm going to put like a silicon type thing here

**Dave Jones:** so it doesn't slip. Got it. So, you can just remove it. But yeah, there's lots of reasons to make it removable. You don't necessarily want a heated bed. So, if you don't want one, why pay for one? No. Don't pay for one is the answer.

**Dave Jones:** But is there a big... There's not a big cost in there. It's a PCB with an axe as a resistor. No. No, no, no. It doesn't... I don't know. That's just my philosophy. If you don't need something, don't buy it. Like, save $20, get a flurry of...

**Dave Jones:** I don't know. So, you designed almost every part of this system, right? Including the cogs and everything? Yeah. Actually, there's a funny story about the cogs. Tell us. So, people know about... Anyone who knows about Gates Corporation will know... Gates? Or Gates... It might not be called.

**Dave Jones:** But Gates Rubber or whatever, they make these pulleys and timing things. And you just cannot get... There's patents that you can read. They're open. But they are ridiculous. Yeah, they're kind of irritating. So, you end up having to get the pulley stock from a Gates distributor or manufacturer or something.

**Dave Jones:** So, I had to get this pulley stock. And then I had to send this to my manufacturer. And then they had to mill it. And then I had to bring it back. And then I had to test it. And it was like, that was fine.

**Dave Jones:** I was lucky. But... Good job. Yeah. So, it ended up working first time. But it's its own little clamping mechanism. I think it's the most compact collet system. So, that's out there. So, if you want to save some weight in your 3D printer...

**Dave Jones:** Yep. You might be able to get some of these from me one day. Cool. In the near future. It'll just... Yep. And you've got a slider in there. You can see a... I haven't seen that done before. Where it's a linear slider on a big...

**Dave Jones:** One big machined aluminium plate. Yeah, that's for its resonant frequency. That's for... Do tell. Well, partly. You want a lower frequency. Because they're easier to deal with. If it's really high, it'll be audible. And everyone will hate you. Yeah. And that's actually why there's two...

**Dave Jones:** Like half the... There's two reasons for the dual motors. Here and here. There's not dual motors here and here. There's one set of dual motors. And they are here and here. Anyway. So, that's one of the reasons of the dual motors. It increases the weight of this thing.

**Dave Jones:** Because it is elevated. So, you actually want the weight up here. Of course. So, that the resonant frequency is lower. And that means it's a lot easier to deal with noise. And, yeah. Hence the thick metal... Yeah. That's like what? 8 millimeters thick or something.

**Dave Jones:** It is. 6 millimeters? Yeah. It's cheap. It's almost like... I think it cost me like $12, that part. It's really cheap. But it increases the weight. And you want that. Because that is a stationary part. It doesn't matter if it's heavy. And you actually want it to be heavier.

**Dave Jones:** In fact, the whole chassis. Look. You've got the metal. You've got the aluminium rod. The support rods. And then the complete aluminium base. Are they welded down the bottom? That's an epoxy. Right. It does look like an epoxy. Yeah. Yeah. That's an... How have you held those in the top there?

**Dave Jones:** Epoxy as well. Epoxy. So, you can actually use epoxy with aluminium. If you like treat the surfaces right. Right. You just have to make sure it doesn't oxidize. Which is just about instant on aluminium. Actually, it is instant. So, there's some things you...

**Dave Jones:** Some fancy things you do. You wouldn't do that in production though. I can... You don't use... Golden rule about you avoid glues in production. Yeah. Where humanly possible. Yeah. You'd avoid glues. Yeah. Or you'd have some kind of like thing that... It's an unnecessary thing.

**Dave Jones:** So, you might have the glue. But you don't need it. Got it. So, it holds without it. And what about the main extruder arm? Ah, yeah. This guy. So, this guy is... It's got a linear feedback sensor down the back. It's a linear potentiometer on the bottom.

**Dave Jones:** Oh, it's a potentiometer. It's not a capacitive location sensor. Resistive are less... I don't actually remember the reason. This was like six months ago. But I think the reason was it's like less sensitive to electric fields. Oh, of course. Yeah. The resistive ones.

**Dave Jones:** Well, they're not... They don't... Of course. They just don't care. They're lowish impedance and they're... Yeah. Yeah. And in my head... I'm stretching my memory, which I don't have. I don't have a memory, really. So, this thing's definitely being PWMed, right? Yep. So, if this is like...

**Dave Jones:** I don't want it to couple to the capacitive sensor. Got it. And the machine's like, where am I? I'm over here. Now I'm there. Yep. Boy, I moved quickly. It's like... Yeah. And you've used another linear rail on the top. So, what's the support bar?

**Dave Jones:** So, we've got an aluminium... The black one. There's a black aluminium. Yep. So, there's a standardised aluminium bar on the bottom and then on the top of it is a HiWin linear guideway. These things have, like, support in all... In, like, this way, that way.

**Dave Jones:** And they're very rigid. So, I can't really show you because the whole machine ends up moving. But... Oh, right. No, no. But I can... Right. Because that's a problem with a lot of those sliders is that there is give in them. There is...

**Dave Jones:** Yeah. That's... A lot of the time that's to do with the way they use the pulleys and stuff is there's slack. So, I haven't actually tensioned my belts yet. You'll notice there's slack in mine as well. Yep. Because I just haven't tensioned the belts yet.

**Dave Jones:** It's got a tensioning mechanism in the belt. Well, I notice you didn't go with the spring tensioner. No. Which seems to be common these days. Yeah, I went for a ratcheting tensioner. Actually, there's two versions of it. Don't you worry about it getting...

**Dave Jones:** Over time, it actually gets loose and you'll keep having to adjust it. That's the idea of the spring tensioner. According to... Yeah. According to Gates, that shouldn't happen. That shouldn't happen. Oh, well, you know. We'll see. I have two different versions of it.

**Dave Jones:** You fool. Believe in the data sheet. Yeah. Yeah, that shouldn't happen. But, you know, it's not a big deal to just undo that and you just go one click and it's done. And there's a few different versions of it which support different belt pitches and...

**Dave Jones:** Got it. Yeah. I see two fans in the back. Yeah. Why is that? To get heat out? So... Because you want... You don't want... Air flow is a bad thing. Yeah. You don't want air flow inside these. Hence why the bubble is actually good.

**Dave Jones:** Hence why the bubble is good. Because it prevents any drafts coming through the room. Yeah. Actually de-layering the print. Yeah. Yeah. And it's also important to have a consistent environment. So, if you do have air flow, you want it to just keep going.

**Dave Jones:** At a very slow rate, ideally. Right. Yep. So, the fans do two things. One, at the end of the print, before you open the door, you might want it to go and cool down the enclosure. Right. And then, the other thing is, you can actually use it to control the whole temperature of

**Dave Jones:** the enclosure. Oh, I was going to say, yes you can. You can keep, because there's advantages to keeping the whole enclosure at a higher temperature. And you can control what that temperature is. Yes. Because the whole thing has... So, all my sensors, the analog ones, like the potentiometer, have precision current loops.

**Dave Jones:** Actually, I've got a really cool picture. So, that's our controller board. What processor? That's a TMS 320... You are a TMS fanboy. I like them. They're good. F28069. And then, we've got a whole bunch of current loops up here. There's eight of them.

**Dave Jones:** Yep. You've got some limit switch inputs. I only use two of them. But, this board is not a 3D printer controller. It's a robot... It's designed to be a robot controller, 3D printer controller, CNC controller. In fact, it's got thermal provisions on the bottom where you can add extra heat sinks

**Dave Jones:** and all kinds of stuff. So, it can be used for other things. Cool. You have a CNC as well, and I just want to use this as well. It's a lot easier. So, around here, we've got four power FETs. The FETs themselves are rated at 40 amps, but I'm running them at 5 or 6 or something.

**Dave Jones:** I think it's 6 amps top, before the traces start heating up. But then, that's not actually a big deal. Yep. Heating up, when you put it into the ANSI calculators, you're only calculating the temperature rise of the trace. So, it's actually okay if they rise a bit, if you can deal with that.

**Dave Jones:** It's okay. You're not going to vaporize your trace until quite a way up. In fact, the industry rule of thumb is a 10°C rise. That's what you pick your nominal figure at, for a 10°C rise. Yeah, it's a rule of thumb. And then, we've got four stepper motor controllers here, drivers here.

**Dave Jones:** These are the DRV. What number was it? 8825 or 8816? There's an 88, one of those is a DC motor driver. And the other one is that. That's the DC motor driver. It's a dual half H-bridge, which is a weird name for something.

**Dave Jones:** It seems like it's a full H-bridge. Yeah. So, it has an SD card. It supports that file system and stuff, which is a real pain. It's got some error logic around here. They're literally just OR gates. So, you're doing hardware error detection? Yeah.

**Dave Jones:** Yeah, it detects when it flips out. The stepper motors detect errors. Right, okay. And so does the DC motor thing there, or brushless, or whatever you've decided to put the control strategy in for. It's just a dual half H-bridge, you can use it for anything.

**Dave Jones:** Yeah. It's also got quadrature encoder inputs, which can go low speed or high speed. Right. Which is actually kind of a thing. When you're doing a quadrature encoder controller, if it's high speed, it's actually a ridiculous amount of overhead for a processor, for a high resolution quadrature encoder.

**Dave Jones:** So, you've got 2,000 steps around an encoder, and it's going 2,000 RPM. You can see how that adds up quite quickly. Yep. Because when you hit one pulse, you've actually counted two, because you need the direction. And then you've done some checking, which one's on and which one's off.

**Dave Jones:** Of course. It's quite a lot of overhead. So, usually people do it for a low speed or a high speed, not both. Right. This does both. Cool. It swaps modes, basically. That's in hardware of the TMS320. That's actually one of the reasons I selected it.

**Dave Jones:** Oh, because it's got some hardware functionality built in. Yep. So, there's no software overhead for that. Yeah, none. Nice. Just about. I have to initialize it. Oh, yeah, well. And then I read, where am I? Right, yes. And I do some resetting. But apart from that, yes.

**Dave Jones:** It's like nothing. It's done by a complete separate hardware logic in there. Yeah. Sweet. So, this thing's powered by like, it can be powered by a single ATX power supply. But you'd modify the connector. Because I've done this very, very intentionally to make the ATX connector incompatible.

**Dave Jones:** Right. Because it has a different power rail. And that power rail can be isolated. And I didn't want someone to plug in a whole bunch of random non-isolated rails into this and just be like, let's break things. Got it. So, it has the ability to have isolated rails.

**Dave Jones:** In this case, it does. As you can see, it's a separate supply coming over from here. But in many cases, people won't care at all. It's still got the protection for the controller, so it will protect it. Yep. Yeah. So, it's isolated between here and here, and here and here.

**Dave Jones:** There are a few things which I'm going to change to improve the isolation. But for the most part, it's pretty well isolated, yeah. So, that's in the base of the metal enclosure that we see here? Yep. Yep. So, we've got this nice Flex ATX.

**Dave Jones:** This is galvanised steel. Oh. There are a few different types of galvanised steel. You can get the ones with the funny pattern, and you can also get this one. I just don't like the funny pattern. I don't like the shininess of it either.

**Dave Jones:** This one, it didn't really matter. It was a prototype. Actually, the final unit would be aluminium. It's just way cheaper. And you're, aren't you running... Actually, it was only cheaper at the time I bought it. You're actually running a limit on your micro of the G-code, aren't you?

**Dave Jones:** It's getting so complex, your own G-code. Yeah, yeah. You're running out of memory. What, you've got 128K in there? No, I've got 100K, kind of. 100K is your current code size? Kind of. It's kind of confusing with micro, because it's got certain sections for the math,

**Dave Jones:** like look-up tables, and it's got all these things. You kind of have the memory. You don't. It's way less. It's less than 50K. Yeah, the data sheet in one place says 50K, and in another place it says 100K. So it's like, yeah. So it's more like, it's got 100, but it's kind of more like 50.

**Dave Jones:** So the G-code interpreter, you end up, when you have all of nice S-curve speed stuff, then you've got trapezoidal options. And when you add all the options, it definitely won't fit. Right. So that said, I haven't put full optimization on, because when you do, it's impossible to debug.

**Dave Jones:** Your breakpoints are like, I'm somewhere. It doesn't even behave the same. Your timing will change if you're doing, I'm not doing that type of timing, I'm doing it with timers, but if you were doing just single line timing, it would be completely different.

**Dave Jones:** Hey. You're going to tell us all about your, something you're very proud of, your optimized algorithms. You reckon they're super duper quick. Yeah, they're pretty fast. I'm not sure if they're like, they do everything the other ones do, because I don't really know how normal algorithms are so slow.

**Dave Jones:** What algorithms are we talking about? In the standard libraries, you get... G-code libraries we're talking about? No, standard C++ libraries. Oh, standard C++ libraries. And Boost libraries, and actually there's a lot of them. But is this compiler dependent? Pretty much. They're pretty equivalent in the standard libraries.

**Dave Jones:** You get broad-spectrum performance hits in some of them. They're pretty much all over the board. Some of them are optimized for very particular things. But, where is that test picture? Anyway, yeah, so the ATOF function, and STOD is a string to double. ATOF is ASCII to floating point.

**Dave Jones:** ATOI is ASCII to integer. Pretty basic stuff. You thought they'd get right. Yeah, you think it'd be fast, but that ends up being a massive speed hit on a parser. Of course, because it's text, right? So you're trying to parse text and then convert it to integers and floating point.

**Dave Jones:** You hardly keep up with the SD card's data rate. Wow. Just because the SPI port doesn't run. You're not going to run the SPI port at full speed. You put it down a bit so you don't stuff up. And then you're hardly getting the throughput you need.

**Dave Jones:** And then you've got this thing that's processing the string, and it's just in time only. And that's actually probably where most of the limitations in the controller are. But maybe are they optimizing how they've written these routines? Maybe they're optimizing them for size instead of speed.

**Dave Jones:** Yeah, they might be. I've tried different optimization options. I've tried all of the available ones. They have just went in the optimizer. And none of them were good enough, so you wrote your own. Yeah. Bugger it. These regular C libraries are for pussies.

**Dave Jones:** Yeah. They're good. So how much faster are yours? I'll show you. I'll run it. Awesome. Yeah. Okay, so you're going to run like a billion loops or something on the regular routine. Yeah, I'll check that. And then you're going to use your whiz-bang one.

**Dave Jones:** I'm going to run that many blank loops. And then each time I run through a parser, I'm going to run it that many times. Is this code that we're allowed to see? Not yet. Okay. Not until I release it. Oh, no, but we're recording now.

**Dave Jones:** Oh, this part's fine. I've been careful where I'm showing. Okay. Right, so we haven't shown the magic yet. No. No. That'll be released when it's perfect. Do you have a funky name for your algorithm? The type parse. No, that's lame. No. Better. It's very descriptive.

**Dave Jones:** No. It parses types. Why not name it after yourself? That's, you know. Oh, it's not necessarily original. It's just like... Oh, right. It's like I just kept micro-optimizing. Oh, okay. And once you get to a point where you can't micro-optimize anymore, and then once you've finished, once you go to that point,

**Dave Jones:** actually macro ones are a bit more obvious. Macro optimization, so you end up going... And then you try to reduce size to make it like... Size is speed. Right. Especially on x86. So did you code this in Assembler or it's all in... It's in C++.

**Dave Jones:** Okay. It actually didn't seem to be worthwhile doing it in Assembler. All right. Yeah. Okay. Well, let's run it. So this isn't in debugging mode because that would be catastrophic because one of them is a pre-compiled library. So it's going to compare the standard libraries to my ones.

**Dave Jones:** So I'll just go run it now. Usually I'd run it like 10 million times for a better test, but, like, this is a video. I can't run it forever. Okay. So my library converted 12 point... Yep. We've picked some values. So it converted 12.3035 in 4 milliseconds, 100,000 times,

**Dave Jones:** whereas the STOD did it in 30. Oh, okay. Yep. It did it with floats in an immeasurable amount of time. In an immeasurable amount of time, instantly. That does not mean zero. And it actually, like, that may actually not be immeasurable. It could have been, like, a side effect of something else.

**Dave Jones:** All right. But it's way small. So you're talking, considering the least significant bit area, you're talking 15 to 30 times faster on that one. Yeah. Yeah. I don't know. It could be. This one's probably running really slow, and this one will probably run fast in this case.

**Dave Jones:** But in the general case, it's about 7.5 times faster, or 750% faster. Nice. You can't improve on these ones very easily, integers and unsigned and stuff like that. So I've only got small improvements. These are just immeasurable because I've only run it 100,000 times.

**Dave Jones:** I should run it several million. I probably could. I'll see how fast it goes. It'll be 10 times, so. Nice commenting there. Thank you. Unlike some companies, I know. Workful. So, yeah. So here's the conversion results, just comparing them. This is doing values to strings.

**Dave Jones:** So I did it both ways. This is a both-way conversion library. Yep. But no one really cares about that direction. This direction, the speed doesn't matter, so I didn't benchmark that. But here we go. In this case, it was 4.61 milliseconds. It varies a lot depending on the computer's activity.

**Dave Jones:** Current state of, yep. Yeah, because the process has actually changed clock speed. So that's 4.61, and this is 3.1 seconds. So you end up actually saving, that is a ridiculous amount of time to save in code. Cool, yeah. Most people would not bother thinking

**Dave Jones:** that you could even improve on those things. They can all be improved. Because you're a nerd, and that's what you do. Yeah. Like, standard library guys, they're also trying to solve a different problem. Like, they are trying to make it the jack-of-all-trades of parsing.

**Dave Jones:** They're trying to set exceptions, and they're trying to deal with all these kinds of things that are slow, they slow it down. So lean is kind of the way I've gone. Right. Yep. Yeah. Sweet, well done. Thanks. By the way, that is not the way you should benchmark your code.

**Dave Jones:** Just a clarification there, just in case we get flame mail. Yeah, this is a really simple demo, which was put together in about 10 seconds. But you should run all kinds of values, a huge variety of them. You should actually run it in a full application

**Dave Jones:** to see how it interacts with other things. Because especially on x86, you end up having, it's all about the cache. Yes. Everything's about the cache. Oh no, it just flushed me. Not only that, if your stuff, you get cache misses, and each cache is like 10 times slower than the other one,

**Dave Jones:** the one before it. So L0 is like awesome, and then you're like 10 times slower, 10 times slower, 10 times slower, 10 times slower. And if your algorithm doesn't fit into L0, or whatever data you're using in your algorithm, I should say, doesn't fit, then it's slower.

**Dave Jones:** That's a reason to do it in assembly, is it not? Because then you can guarantee it stays in the L0, or will the operating system kind of... I don't really know. I don't know how Windows handles that, because you're always a layer above the operating system.

**Dave Jones:** In assembly, you could probably put it wherever you want. Right. But when you're in an operating system, it is different. But you're not actually running... You wouldn't run assembly in Windows. You'd be running assembly on the processor while running Windows. Right. Yeah. Is that right?

**Dave Jones:** Maybe you could dedicate your own core. You could steal a core. Maybe you could dedicate a core. Yeah, that's the way to do it. You're still sharing RAM if you're using any at all. But that is mostly operating system stuff, probably not. Yeah.

**Dave Jones:** You really went to town on this, went for broke, when you didn't have to. You could have easily passed your thesis project by doing one-tenth the amount of work you did here. Yep. Nerd. And the same with money. How much did this thing cost you?

**Dave Jones:** Tell us. So I will preempt this with most people would spend like over $10,000 on just the bubble. So plastic tooling is stupendously expensive. So to get this same sort of bubble made, you'd have to spend $10,000. A lot of people would end up spending a lot of money

**Dave Jones:** if they didn't figure out lots of things with manufacturers or their manufacturers weren't awesome. What the process capabilities were capable of and all that sort of jazz. Yeah, if you don't hand... I'm sure they'd be stoked. They will take your money. They will take your shithouse design and they will take your money

**Dave Jones:** and they will produce it. But yeah, if you don't do it right, you end up paying a huge amount. And it's not necessarily doing it right. You also have to have really nice, good people to work with, with prototyping. Otherwise, you end up handing it back to them like 35 times

**Dave Jones:** because they're like, I didn't understand what you were saying. Yep. So how much did you spend? Tell us the price, son. I think it was about something above $11,000. All up? All up. Wow. That's with huge excess purchasing too. So they're a risk...

**Dave Jones:** So you had to buy a thousand or something. Yeah. When you're using a few hundred bolts, for example, you don't buy them in small packs. Especially... I used particular types of bolts, which you don't find on eBay. Oh. I did. I did a lot of the time.

**Dave Jones:** Oh, it's just... Gilding the lily. Look, they all look the same. They all match. Bitch, you can just go to Bunnings and buy ones that all match. Oh, yeah. But they're not button cap, socket cap, countersunk. I do know you are a socket cap fan, boy.

**Dave Jones:** I am. Yeah, and they're not socket cap, and they're not neat, and they're not countersunk, which they had to be for this. Yep. For a lot of reasons. Like this thing would fold into the other side of the bolt if it wasn't, and there'd be all kinds of self-collision type stuff.

**Dave Jones:** Yeah, but not only that, like the electronics, you end up getting into all kinds of traps where you're like, I have to get a hundred. Like, I have to get a hundred. Or like, especially... So you've got a hundred blank boards, do you, lying around?

**Dave Jones:** Oh, I don't have a hundred blank boards. I've only got like six of those. But with certain parts, you get stuck. Oh, yeah, exactly. Especially nice op-amps, and the nice parts are unkind. Haven't you heard of Digi-Key? Oh, the one of everything. Yeah, no, I went to...

**Dave Jones:** It was Digi-Key, but I still had to like... There are high-risk parts, too. Like, if I wasn't 100% sure about my design, which, of course, I wasn't until I tested it, but then, you know, I'd get more of them because I'm more likely to break them while debugging.

**Dave Jones:** I'm more likely to go through more parts, so I get more of those parts and less of others. Yeah, so like all my linear rails, I have twice as many as I need Like, for example, the balls in that lead screw there, one that I forgot to tighten,

**Dave Jones:** one of the bolts that holds into the motor, and I was putting it in there, and the whole thing just went, whoop! And anyone who knows about ball screws would have just had a heart attack because, yes, yes, the ball bearings came out.

**Dave Jones:** Yeah, so there's actually... I didn't put a ball back in. I couldn't get a ball back in, but there are two ball bearings or something just sitting there. Yeah, right. Just as a reminder to put them back in. It's just a pain in the arse to do.

**Dave Jones:** And you are not happy. You're not a happy camper with this LCD down the front. Why? Oh, are you talking about the Wi-Fi module inside it? Yeah, I don't know. You were bitching about something the other day in this LCD module. Tell us.

**Dave Jones:** There's a few things. So I designed this module to be like... So the printer isn't designed to be plugged into your computer. It's wireless. These are debugging leads. Right. It's wireless. It's meant to be only wireless because I guess I was just... Because you can.

**Dave Jones:** It's cool. There's no leads. I guess I was just being kind of ridiculous, being only wireless, but I actually kind of think that should be the way things go. Well, why wouldn't you these days? I mean, why have the cable plugged in? Yeah, it also means you can seat it right up against the wall,

**Dave Jones:** and that's really nice. Anyway, the CC3200 has this... And which processor is it? That's one of the TI Internet of Things... Wanky things. Yeah, yeah. It's a CC3200, I think it is. Again, it was like four months, this one, when I did that.

**Dave Jones:** So the actual processor has a JTAG port, and when I see a JTAG port, because I'm a newbie, I think, okay, I can program everything. Wrong! Wah, wah, wah. Wah, wah, wah. Yeah, JTAG doesn't mean that at all. In this case, you needed a separate flash programmer.

**Dave Jones:** Like, entirely separate. And you can't manually program the flash, which was my backup plan. I actually had access to it, because it uses this proprietary file system, which you don't know how to program. And it ended up being like a real nightmare. So I think I'm just going to change microprocessor.

**Dave Jones:** It just made me that annoyed. Right, you're going to change it on principle. I'm going to change it on principle, because I want TI to upgrade it slightly, and then I'd be so happy. If I can influence that just a little bit, I would be just stoked.

**Dave Jones:** It would be the greatest thing ever. Now, I see some limit switches in there, but you haven't used them. Yeah, no, this one here. It's actually the only limit switch the device needs. So a 3D printer, every single time it's turned on, unless you're resuming a job,

**Dave Jones:** which is just a memory thing. It should go to the top, because you only start prints at the bed. Of course. So there'd be literally, like, there's no savings made, in terms of startup time, if you put a linear thing on that axis.

**Dave Jones:** Right. So you might as well just go all the way to the top. Yep. Yeah, so that's what the limit switch is for. At the moment, it literally just forcibly stops it, and then the motor sends an error. Yeah, right. I think that's what it does.

**Dave Jones:** It's not plugged in. I can see it. There's no cables coming out. Yep, not plugged in. Unless it's a wireless limit switch. New technology, though. Patent pending. Yeah, yeah, what a waste of energy. But yeah, no, the moment just forces it to stop.

**Dave Jones:** But yeah, that's what that does. So what stuff have you learnt from this, making your own 3D printer, that other people out there need to know, because it's just dull. Do you have any dull moments, like, that was stupid, that was... I thought that'd work, and it didn't.

**Dave Jones:** What happened? Or did it all work, because you're a genius? I don't want to say that, but it did all work. It did all work. Stole the JTAG. Yeah, right. Okay, that's it. That didn't work. I literally stopped programming it, on principle. I had, like, a month for it.

**Dave Jones:** It's just evil looking. Yeah. Yeah. Awesome. Yeah, so I literally just stopped programming that when I found that out. But in terms of the mechanicals and all that sort of stuff, do you still think it's a good, usable implementation for a 3D printer?

**Dave Jones:** You still think it's as good as you hoped it would be? Yeah, yeah, I think it's going to be as good as I hope. Yep. Polycarbonate would be better. This gets scratched a bit. Oh, that's just the case. We don't care about the case.

**Dave Jones:** We care about how it works. Yeah. No, I think extruder tests were good. Yep. No, everything went really well. Yeah, everything was great. Yeah, it was okay. You just spent 18-hour days on it. That's it. Yeah, for a very, very long time. Yeah.

**Dave Jones:** Yeah. Yeah, so I guess press fit bearings. Yep. When you do press fit bearings and you anodize, make sure the anodizing is the right thickness or, like, it penetrates the right amount because otherwise the anodizing is a lot harder than what you'd normally be press fitting bearings into.

**Dave Jones:** So it doesn't, it's not the same. Ah, right, of course. It's not the same. It changes the properties of the surface. Yeah, it's like, I think it's just super oxidized, which oxide layers are typically pretty hard. I think, I don't know. I'm pretty sure it's, like, put in a really strong acid.

**Dave Jones:** I think that's the whole process. Right. Yeah, so don't do that. Don't anodize press fit bearings. It'll save you some time not doing that. Other than that, never let a ball screw leave its lead screw. That is a nightmare. Oh, yeah, this wire, PET wire.

**Dave Jones:** Oh, you, like, have wet dreams over this stuff. It was amazing. I'm like, this is so great value and it can, like, almost be on fire. Not really. I'm exaggerating. This is hyperbole. Yeah, but it, like, it's really good properties, but then, like,

**Dave Jones:** It's a bitch to strip. It's horrible. Like, usually you can do this with your nails. It's immortal. Like, yeah, it's, like, so, like, you're trying to strip it and you end up cutting through the wires and you short all the cores and, yeah.

**Dave Jones:** Buy a proper tool for it. Buy one of the 500, yeah, the 500 double tool. You can get the Alibaba equivalent. Oh, right, okay. That'll work. That'll work, but it's less time. So, what are the plans for the Yar print? Yar print. I don't know.

**Dave Jones:** If I can get over a thousand people to be, like, yeah, I'm super interested. I want one. Hey, I'll tell you what. There's this thing they've invented. It's called crowdfunding. Yeah, but I don't want to, I don't want to, I don't know. You don't want to take people's money.

**Dave Jones:** I don't, I don't want to do that. You, like me, you just don't want to take people's money. I don't want to take money. I would rather people just, I don't mind people doing, like, banks. That's what banks are for. Yeah, because you don't care if a bank loses their money,

**Dave Jones:** whereas you care if people lose their money, right? Well, I care if the bank loses their money, but they can handle it, and they've factored that into their risk. Right. And they've probably got hedges and insurance against that anyway. Yeah, they've factored that into their risk,

**Dave Jones:** and, like, this is relatively low risk because it's all, like, it's all right, but, like, and if you have a thousand things, I'd rather people just be, like, I agree to send this money on purchase, on delivery, or not on delivery, on shipment or something.

**Dave Jones:** So if you had a thousand IOUs, you'd do it? Yeah, sure. There you go, folks. Sign up for one. Have you got a sign-up page? Maybe later. I might. There will be a website coming. Okay. It's easy. Leave it in the comments. I'll buy one.

**Dave Jones:** Yeah, yeah, yeah, but those people, I don't trust them. Oh, right, yeah, dodgy YouTube comment. Yeah. Those anonymous trolls on YouTube. Yeah, I get myself in a bit of trouble. That's where Kickstarter's good because it's real money. Yeah, it's real money. Maybe you'd have, like, a deposit.

**Dave Jones:** Right. Maybe a deposit system. Does Kickstarter work with deposits? No, it doesn't. No, you've got to pay the whole lot. Ah. Yep. Yeah, maybe, like, a small deposit because then, you know, people aren't just, like, It's serious, yeah. Woo, dude. I promise. Pay entire kickers, yeah.

**Dave Jones:** Yeah, yeah, yeah, exactly. Like, yeah. But then you get the people who think that, oh, it's only ten bucks. It was a good idea at the time. What's ten bucks, you know? It's true. Now you've got to make it, like, a hundred or something serious.

**Dave Jones:** Yeah, I wouldn't want to, like, I don't like taking people's money and then having them, like, forget what they purchased and be like, oh, I bought that, right. Twelve months later, yeah. Yeah, because that's what it would be. Oh, it's still working. That's what it would be.

**Dave Jones:** Like, it's, like, the machine, this is a working machine. Like, all the parts are separately tested. But it's not a finished product you would want to ship to people. No, no. There's, like, custom headers which I need to make and in the back, there's a part

**Dave Jones:** which cables would certainly, like, they would cut. There's a place for the header, but custom headers are irritating. It's very irritating. I've made all this custom and I'm stuck on a custom header and I'm just like, I'm not doing that. They're irritating, especially for the mold guys.

**Dave Jones:** So I'm not doing that. That would have to be later. And there's all kinds of things, like the limit switch wiring. I'd want a more organized wiring strategy and I'd want the cable guide. My first print was going to be a spool holder,

**Dave Jones:** but you'd need to ship that with it. There are things like that. More anodizing. Yep. Anodizing's great. Terrific. Well, well done, David. Thanks. Awesome. Arr, print. The printer for pirates. Yeah, I think you need, like, to etch, like, a skull and crossbones in the top.

**Dave Jones:** What do you think? I don't know. Yeah. It's got to be. Limited edition pirate version. Cool. It is the funkiest looking 3D printer I've seen. That bubble is really. Where's the door gone? Oh, yeah. Oh, there we go. There we go. Yep. It's worth every cent.

**Dave Jones:** Yeah. It would be. It wouldn't be, like, one of the cheapest 3D printers. No. No, you wouldn't be targeting low-cost if speed and performance. This is for, like, consultancies and people who want to prototype their products. This is, like, a few steps below the, like,

**Dave Jones:** real high end when you have to change topology. Right. This is the high end of FDM. Right. Yeah, so it's the high end of FDM. How much? Do you have any ballpark figure of what it would potentially sell for in $1,000? I have.

**Dave Jones:** Have you done costing? Yeah, I've done costing. So, the parts in this cost about $1,400. Right. In 1,000 odd quantity? In 1,000. Wow. So, you end up paying, you know, $2,000 or something. Yep. At least. Well, you've got to multiply. Let's say you use the regular.

**Dave Jones:** Two is at least. Two is at least. Regularly, 2.5 times multiplier. Yeah. So, that, like, you're looking. So, I'm looking at $2,500, mate. $3,000. That's in Australian dollars. Oh, Aussies. All the people who are shocked about their US dollar. Right. Multiply that by 0.7.

**Dave Jones:** Yeah, no, we're 0.6. Oh, no. Oh, yeah, it's just plummeting. It's plummeting like a rock. We're having bad days in Australia. Yeah. Well, us in product development are, because we're probably just having costs of. Hey, dude, I can remember when it was 50 cents,

**Dave Jones:** okay, and it could get there again. I dearly hope not. Yeah. Yep. It's like we're literally losing money while working. It's like this is what you have. Yep. Yeah, that can actually happen. Yeah, if you've got money in the bank, you're just losing money

**Dave Jones:** because it's in Australian dollars. Yeah, especially because we have to import, like, everything. That's pretty much. Yeah. That's pretty much every currency except the U.S. dollar. So. Well done, United States. You sorted yourselves out well. Yep. Yeah. Everything's so tied in. Yeah. Yeah, the deal with U.S.

**Dave Jones:** dollars. It's good to be the de facto standard. Yeah. Yeah. Anyway. So we're looking at, yep, about three grand Australian, two and a half, three grand Australian or something. Yeah, something like that. And then you have to sell for. Some parts have come down.

**Dave Jones:** Yep. None of them are going to go up. So the price probably wouldn't be that much higher. Yep. It could be a bit lower. But. Yeah. All right. Yeah. Cool. Well done. Thanks. Are you going to stick around and answer comments in the video

**Dave Jones:** for people who want to ask? Yeah. We should. We should run this live. Whoops. Yeah. Oops. Oh, well. Yeah. Yeah. I'll stick around for a bit answering comments. I'll do it. My phone and stuff. I'll do it for the next day or something.

**Dave Jones:** Sweet. Yeah. So you're done here. You'll be spending more time at the lab. Maybe. Yeah. Yeah, no. I've been spending more time in the lab apart from food poisoning. I was like, I'm coming back this week. And then I got like food poisoning on the Monday.

**Dave Jones:** It's like, I'm not coming back this week. So this baby, the ARR apprentice is the one you haven't seen. Yeah. David Mutch. Yeah. Yeah. He's still here. Cool. Yeah. Thanks, David. Thank you. I'm trying to not call you Dave. I'm trying to, but it's hard

**Dave Jones:** because I hate David. It helps us too because then we're different. It does. We're Dave and David. Yeah. A lot of people have said, why David 2? And I don't know. It started out Dave 2 and then I found out, yeah, so I started out calling you Dave 2

**Dave Jones:** and then I found out you didn't like Dave. It's like, so it's David 2 and now it's like, I think there's people out there saying, no, you shouldn't be called David 2. You should be just David. I like your community. They're lovely. They're pretty cool.

**Dave Jones:** You do know you have a lot of people, you have a few fans out there who have, yes, a lot of people actually, I think, want to be your children. Oh. Yes. Yes. They're, yes, they're that, yes. Well, that's, they're that much of a fan.

**Dave Jones:** That's a nice gesture, I guess. Cool. Thanks David. Say, catch you next time. Catch you next time. Bye. Bye. Bye. Bye. Bye.
