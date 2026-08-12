---
video_id: DwuZJHk5JV8
title: EEVblog 1437 - Zappi 7kW Electric Car Charger TEARDOWN + EXPERIMENT
url: https://www.youtube.com/watch?v=DwuZJHk5JV8
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 29, "3": 43, "4": 68, "5": 82, "6": 101, "7": 113, "8": 137, "9": 153, "10": 163, "11": 176, "12": 198, "13": 206, "14": 232, "15": 244, "16": 257, "17": 279, "18": 290, "19": 305, "20": 318, "21": 334, "22": 354, "23": 371, "24": 382, "25": 397, "26": 404, "27": 423, "28": 431, "29": 447, "30": 463, "31": 474, "32": 489, "33": 502, "34": 521, "35": 529, "36": 541, "37": 552, "38": 568, "39": 582, "40": 594, "41": 603, "42": 617, "43": 628, "44": 653, "45": 663, "46": 682, "47": 694, "48": 705, "49": 715, "50": 726, "51": 736, "52": 750, "53": 759, "54": 779, "55": 789, "56": 801, "57": 809, "58": 828, "59": 838, "60": 848, "61": 862, "62": 876, "63": 889, "64": 900, "65": 914, "66": 923, "67": 935, "68": 946, "69": 960, "70": 967, "71": 976, "72": 986, "73": 999, "74": 1016, "75": 1027, "76": 1038, "77": 1052, "78": 1067, "79": 1078, "80": 1087, "81": 1103, "82": 1112, "83": 1123, "84": 1137, "85": 1151, "86": 1164, "87": 1174, "88": 1189, "89": 1206, "90": 1215, "91": 1225, "92": 1241, "93": 1254, "94": 1263, "95": 1281, "96": 1293, "97": 1303, "98": 1315, "99": 1330, "100": 1344, "101": 1353, "102": 1367, "103": 1379, "104": 1393, "105": 1406, "106": 1426, "107": 1436, "108": 1446, "109": 1469, "110": 1476, "111": 1487, "112": 1503, "113": 1519, "114": 1532, "115": 1540, "116": 1554, "117": 1565, "118": 1581, "119": 1586, "120": 1598, "121": 1607, "122": 1616, "123": 1626, "124": 1641, "125": 1650, "126": 1661, "127": 1671, "128": 1681, "129": 1693, "130": 1714, "131": 1724}
---

**Dave Jones:** Hi, this one's going to be interesting. We're going to take a look at a level two 7 kW electric car charger. This is the one that I'm going to install to fast charge my Ionic electric car at home.

**Dave Jones:** So, this is an electric car charger in quote marks and we'll get into that. This is the Myenergi Zappi and it's designed and manufactured in the UK. So, hi to all my viewers in the old dart and we're going to take a squiz at this.

**Dave Jones:** We're going to take it apart and I'm going to explain how these electric car chargers work because this is not actually a charger as such. It's what's called an EVSE or an electric vehicle supply equipment.

**Dave Jones:** The charger is actually in the car itself or at least for these AC chargers, which this one is. This is a single-phase AC charger. Does come in a three-phase model, but my home only has single-phase and also my Ionic electric car only has a single-phase charger built in and you'll notice I just said the car has the charger built in cuz this is not the charger.

**Dave Jones:** The charger is actually built in to the car. It's not in here. This basically is just a glorified relay with a 1 kHz generator, but I'm being a bit harsh.

**Dave Jones:** There's a lot more engineering that goes into these EVSEs. So, any AC charger for an electric car like this, be it single-phase, three-phase or just the regular wall outlet one that actually comes supplied with it, just your regular, you know, 240 V 10 amp jobby, none of that Yankee rubbish.

**Dave Jones:** And then these are all AC chargers and it's simply supplying the the AC directly from your grid pretty much into the car and the actual charger itself is built into the car.

**Dave Jones:** Now, this differs for the uh fast charging DC charges. They actually There is no DC charger inside circuitry inside your car. Basically, the car just has a relay in it that connects the internal battery pack through straight to the uh charging connector, and then the external, you know, 50 or 150 kW or whatever the high-powered DC charger is, that actually is an external charger.

**Dave Jones:** But, this one we're going to take a look at. This is a level two AC charger, and this is just an EVSE or an electric vehicle supply equipment. So, like I said, this is a My Energy as Zappi, uh fairly highly regarded.

**Dave Jones:** They're one of the uh leaders in the industry, and it's Yes, there is nothing in there. This one has a uh fixed lead attached to it. You can get one that actually uh does not have a fixed lead, but I wanted the fixed lead.

**Dave Jones:** I didn't want to uh dick around with that. So, this is the type two AC charger connector, um also known as a Mennekes connector as well, cuz that's the uh company that actually uh first developed this, I believe.

**Dave Jones:** So, this is the standard here in Australia, and also in uh the European Union, as well. And the Yanks have their own uh standard, which is the SAE J uh 1772 standard, which um the signaling, as we'll talk about in a minute, is basically uh the same between them, but the physical connectors and other, you know, slight differences and stuff like that.

**Dave Jones:** Anyway, those Yanks are weird. So, what we've got here is a uh protective earth pin in the middle. We've got neutral here, and we've got the uh active here or the phase one.

**Dave Jones:** If you're using a three-phase, then you've got uh the second phase and the third phase, but uh they're just not fitted in this particular connector. And we've then got two control pins up here, and this one is called the uh PP line, which is the uh proximity pilot pin, and then this one here is the CP or control pilot pin, which basically um tell the car um what

**Dave Jones:** type of charger you've plugged into, how much power is available, um and stuff like that. And we'll go into details of that um after the teardown, and we might uh try and measure some stuff on here.

**Dave Jones:** So, this Mennekes plug is the IEC 62196 standard, and uh the US do actually have this, but it's under the um SAE J3068 standard. I'm not sure what cars in the US use it.

**Dave Jones:** I I'm not up on the a Yankee land, what's happening there. So, basically, what happens is you plug this into your car, then your car looks at um a 1 kHz square wave on the uh control pilot pin here, and the duty cycle of that uh determines uh or tells the car how much what is the maximum power that it can actually draw from this, and then

**Dave Jones:** the internal charger of the car is supposed to obey that and not exceed the limit, so that, you know, you don't blow up um your like your wiring and your cables and blow your fuses and blow the ass out of your EVSE here.

**Dave Jones:** So, these EVSEs actually can be as simple as like just a 1 kHz generator and uh a relay to switch um the mains. And that's you know, there's more to it.

**Dave Jones:** There's the rest of it's like um protection type stuff. So, anyway, it does do a couple of other things, but basically, uh the control pilot uh pin on the um IEC 62196 uh standard uh between here and earth.

**Dave Jones:** If we actually measure that, so this is designed for a single phase uh 32 amp, so uh we'll find that the um standard for this, so it should have a 220 ohm resistor across the proximity pilot pin and the earth here, and we can actually measure that just to verify that what it be.

**Dave Jones:** Have they supplied me the correct model? I hope so. Should get Yep, 220 ohms. Bingo. And you can have various other resistances on there to uh indicate other maximum uh currents available, but this one yeah, designed for a 32 amp single phase 240 volt Aussie outlet.

**Dave Jones:** Just as a bonus, this is what a single phase 32 amp Aussie connector looks like. I don't know is this the standard in your country? But anyway, this is the three pin the three pin one for the single phase and there you go.

**Dave Jones:** That's it. Cool, huh? So I rather like the design of this my energy Zappi here. It comes in a a nice output outdoor weatherproof case. It's got I had to screw this on the bottom.

**Dave Jones:** This is like a cable rack cuz this is a wrap thing cuz this is a fixed thing. So we mount this on the wall of my garage and then I can just wrap the cable around here and then it's just as I said, it's just got the dummy thing in here to just keep that in well place like that.

**Dave Jones:** It doesn't do anything electrically. It just holds it in place so it doesn't flap around in the breeze. Nice touch. There you go. It's made in the old dart.

**Dave Jones:** This is 230 volts although my house and my lab they run about 240 to 245 volts. So I'm getting right up there on the upper limit kind of thing and it's got a residual current basically earth safety thing built in that looks like 6 milliamp and it's also got pen fault isolator.

**Dave Jones:** I don't know if that is a requirement here in Australia. Leave it in the comments if you know, but I believe it is in the UK and some other countries.

**Dave Jones:** Pen basically stands for protected earth and neutral and this basically will detect if there's a earth breakage fault upstream from your house. You know, somewhere in the street or something like that.

**Dave Jones:** It'll actually detect that. I believe like there's various methods to actually detect that and yeah, it will actually trip that because you don't want somebody touching the metal work of the car for example when it's charging and then for the earth to break and you can get all sorts of unbalances.

**Dave Jones:** And yeah, you can I get a little bit of a zappy. Get it? Muriel weak. You can get a zappy from the zappy if if it didn't have pin isolation.

**Dave Jones:** Oh goodness, that's terrible, Muriel. So anyway, let's open up. This is just a protective cover on it and screws to install it. Look at this. Um It's got a a set That is the saddest ass Aussie sticker I've ever seen in my life.

**Dave Jones:** Look, it's cut Look, it's like one of the stars is chopped out and look from the Southern Cross, it's upside down. So all the electrons are going to fall out and it's like not even like it's not trimmed properly.

**Dave Jones:** Oh, that's just No, no, that's an insult. That is an insult. That's gonski. Sacrilege. And you'll find because, as I said, this is not a charger, it's just a basically a glorified a more than a glorified relay, but it's basically just got relays and and protection stuff in it.

**Dave Jones:** There you go. There is not much at all. There's just a main board. It's got a little daughter board there. Not sure what that does. And we got some big ass Oh, look like Look at those.

**Dave Jones:** Panasonic jobbies. Thank you very much. Some big ass relays. What are they rated at? 35 amps. Thank you very much. Um Yeah, so they got three of them and basically power in here.

**Dave Jones:** So single phase in here. The three phase board would be different, of course. It'd It's more expensive. It'd have to be bigger, more relays, everything else. But yeah, your single phase in here and then just your relays to switch it.

**Dave Jones:** Now because of these are double pole single throw jobbies, you can see Well, you can probably just see the pins down there. This is switching both the active and the neutral here, but so is this one as well.

**Dave Jones:** It's also switching the active there and the neutral. And this one up here is switching the earth in. So why they've got effectively two in series and I can't see anything tapping off here.

**Dave Jones:** So, I I can only presume that's for extra safety, I guess, you've got two of them. Um just in case one of them, you know, fuses um shut or something like that.

**Dave Jones:** That would be my guess. So, there's our 6 sq mm copper coming in. I'm probably only I'm going to be drawing a 29 amp uh absolute maximum, I believe.

**Dave Jones:** But anyway, I can you can set it in software on the Zappi to have any sort of maximum uh current you want. And if you want to know why I got this uh Zappi model against others is that this one actually is solar aware.

**Dave Jones:** So, I have got a little uh current clamp here. I'm going to have to uh install that. That'll install on the incoming uh grid connection and you've got to install it the right way around.

**Dave Jones:** It should have an arrow. Yep, there it is. This charger is intelligent in that it knows how much um excess solar power you've got that would normally be going out to the grid and getting paid a pittance for and then it can modulate the charge current uh to the car when it's charging and guarantee that you're only charging your car with excess solar from your own solar

**Dave Jones:** rooftop. And that's just great. I'd love to be able to charge my car knowing, guaranteed, that all of it is coming from the solar. So, the whole idea is you come home and you plug in your car and let's say it's night time.

**Dave Jones:** Then um this thing is going to detect that there's no excess solar available, obviously, cuz it's night. And so, then it's just not going to charge the car. And as soon as the sun comes up at like 7:00 a.m., you start producing some excess solar, all the other appliances in your house are off and stuff like that, um it'll start charging the car at whatever uh rate you have available.

**Dave Jones:** I'm not sure of the grandiosity um of it, but is that a word, grandiosity? Anyway, yeah, it will modulate um the charge rate up to, uh, the full 32 up to the full 32 amp 7 kW.

**Dave Jones:** Of course, my, uh, solar, um, home solar system is nominal 8 kW. So, in the middle of summer, I should be producing, you know, at peak, about 8 kW or so.

**Dave Jones:** So, assuming I chew less than a kW in my house, I should have the full 7 kW available to, um, charge my car up. But, yeah, anyway, I thought that was really cool.

**Dave Jones:** And everyone recommends this. It's really good. It's well made. It's made in the old dart. Anyway, as you can see, uh, the cables are terminated in the ferrules here, which then go into the big, uh, cage clamp terminal box.

**Dave Jones:** They've got proper cage clamps, not that little leaf spring rubbish. Can show you that here. There you go. Proper cage clamp. Beautiful. And this is how it's doing its, um, RCD.

**Dave Jones:** You can see the active and neutral are both going through this, uh, clamp here. And then it's able to measure any imbalance in that. So, under normal non-fault conditions, of course, all your current flows from your active through to your neutral.

**Dave Jones:** So, if you've got current flowing in this direction like this, and then this direction like this out out out the other wire in a full loop, they cancel each other out.

**Dave Jones:** So, this, uh, current clamp is going to measure zero. There's going to be zero output from it. But, as soon as, um, some fault condition occurs, some earth leakage, you know, rain got in somewhere or somebody's touched something, something's failed somewhere, then there's going to be an imbalance in the current between the active and the neutral.

**Dave Jones:** And then, uh, you will get either a positive depend on which way, um, you'll get either a positive negative output from your, uh, current clamp here. So, it's able to measure that.

**Dave Jones:** And it's calibrated to, uh, do to trip at, uh, 6 mA. And you can see that the, uh, protective earth here has its own current clamp as well. So, I assume that's part of the, uh, pen protection, uh, system.

**Dave Jones:** So, anyway, that's all very nice and dandy. So, you can see there's is four wires going in on a charging cable, uh, active, neutral, earth, and then the uh, CP or control pilot.

**Dave Jones:** So, the proximity pilot here, and you can see that labeled down on the board there, PP. PP. The proximity pilot pin is not connected. So, that 220 ohm resistor we measured before, that must be physically within the connector.

**Dave Jones:** This goes off to our front panel LCD, which I'll show you in a minute. This says it's a protection board, so I'll take you out take that out and show you in a sec.

**Dave Jones:** But, there you go, that's a just a 405 something. So, that's just analog marks, and yeah, they've just got some little passive stuff around there, little op-amps or something like that.

**Dave Jones:** So, yeah, that's doing some of the measurement. Now, over here, look at this. This looks schmick and expensive. This is a Recom DC-to-DC converter module. 20 It's probably one of those potted brick jobbies.

**Dave Jones:** 24 volts 830 milliamps there. So, that's basically powering this thing. And they've got another transformer there, so I don't know what that's doing. They've got a big-ass MOV in there, so that's nice to see.

**Dave Jones:** Beautiful. So, is that a common mode choke and X and Y class caps there? And curiously, there is a little relay there and an optocoupler. So, I don't know.

**Dave Jones:** I'll have to reverse engineer this to have a squeeze at what's going on there. I'm not going to do that in this video, but anyway, that's interesting. AC input terminal block, and then this is another e-sense thing.

**Dave Jones:** This has lots of options. In fact, it has a wireless current sensor option, although it comes with the wired one. So, it supports up to three current clamps here, and it can actually measure your supply as well, so it can give you that sort of detail.

**Dave Jones:** But, it it's basic operation, it only needs the one current clamp, which goes on the grid side there. So, there's that protection board. I can't read that on the LCD here.

**Dave Jones:** Um why it's got a little bit of like Kapton tape over that, I'm not entirely sure. But anyway, so obviously they're off-boarding their uh protection uh circuitry onto this dedicated board.

**Dave Jones:** And that probably makes sense cuz the protection is probably is based on regulations which could vary from country to country. So, you don't want to go, you know, changing your main board or anything like that for different countries.

**Dave Jones:** So, I I suspect that's why they whacked that on the uh on the dedicated board like that. So, for different countries they can just whack in whatever uh protection circuitry it might have, you know, different current uh trip ratings or whatever it is.

**Dave Jones:** Um and that would be programmed in there. So, that's got its own micro order handle all that by the looks of it. It'll do its own measurement and do its own thing.

**Dave Jones:** Nice. So, you'll notice that there wasn't really a processor apart from the uh protection board there. That's cuz the processor must be on this main uh display and button board up here.

**Dave Jones:** Yes, that is a little antenna there because it has I as I said a wireless clamp interface and it's called um Harvey. I'm not sure what standard they use or whatever.

**Dave Jones:** But anyway, um yeah, so if you don't want to run your cable or it's, you know, too hard, you can't do it over, you can actually get a uh which is quite novel cuz it's actually powered from the current clamp itself, which is really interesting.

**Dave Jones:** It's basically an energy harvesting uh thing which powers the transmitter and this is the receiver here and it can just receive the uh current clamp. And there you go, it's just got a little uh light window here and uh the you can see that the LEDs on there they'll light up different colors and uh that just uh like charge indication and stuff like that.

**Dave Jones:** But apart from that, it's there you go. Um yeah, it's one big ass graphical LCD. It displays like a little car and stuff. And there you go, there's the uh wireless connection up there.

**Dave Jones:** I got no idea what that is, but, you know, leave it in the comments if you want to know. Little backup battery there for real time clock and the micro oh, must be hidden under there.

**Dave Jones:** PIC24F for the win. All the Microchip fanboys go wild. And the good thing about that is that you can probably still buy those in the current component crisis. So, yeah, winner.

**Dave Jones:** Right, so let's just power this up on the bench here and see if we can measure stuff. It's in. Verifying. My energy's up. OCB board test start up. We're in.

**Dave Jones:** And that's a pretty nice display. EV disconnect, yep, no electric vehicle. No grid, no nothing. So, I haven't read the manual on this, but yeah, it's in fast mode at the moment, which time out.

**Dave Jones:** Fast mode at the moment, which means that it'll it doesn't have to follow that eco like the solar thing, which is eco mode. So, I don't know, is it yeah, eco mode, there you go.

**Dave Jones:** So, in or I think yeah, eco plus mode is where it guarantees that it only uses energy from your grid. Whereas if you want to, you know, the sun's not out or it's night time, you just need a charge at the fastest possible rate, then there it is.

**Dave Jones:** You put it in fast mode, Bob's your uncle. Does have a stop mode. I didn't think it did, but charge settings, you should be able to set like the maximum charge.

**Dave Jones:** I don't know. Yeah, there we go. Eco plus settings, manual boost, smart boost. And the range here, well, that's going to vary between vehicles. So, I think you could you maybe hopefully you can program that.

**Dave Jones:** So, I have to program that for the Ionic. Eco plus settings, minimum green level, there you go, start stop delay, plug-in charger, eco plus, look at that, you can start and stop at different import and export powers.

**Dave Jones:** That's that's rather nice. And then you've got like timer modes as well. That's really nice. Oh, there you go. It tells you your pilot PWM. That's fantastic. I was going to actually have a look at that, but that isn't that nice.

**Dave Jones:** It'll it'll actually tell us what the PWM is. And presumably that's measured or well, cuz it's generating it it knows what it's generating, I guess. Whether or not it like measures that as a feedback, I don't know.

**Dave Jones:** Here you go. This is nice. This is my lab voltage, generating consumption and stuff like that if you put the extra current clamps on, importing. It's pretty cool. What was that that that had Aussie something?

**Dave Jones:** Oh, yeah, Australian Eastern Standard Time. So, that's pretty comprehensive. Yeah, there's that Harvey thing, the remote uh current clamp. Okay, what I've done now is I've just removed the input earth on this thing.

**Dave Jones:** I just want to see what happens if I power this up. do do do do do do RCB door it's yep. No. No error whatsoever. It has no problem with the lack of earth on the input.

**Dave Jones:** But I guess it's not surprising cuz if you go through Oh, jeez, I'd have to Jeez, there's a half hour whiteboard tutorial in its own right how all this sort of stuff works.

**Dave Jones:** But yeah, just the earth on the input itself because there's no fault current or anything like that, it's doesn't know there's an issue yet. Actually, I just checked to see if they have any info on this.

**Dave Jones:** I did actually find a video with the one of the R&D engineers or someone at My Energy talking about very extensive, very detailed about all the various protection modes that this goes into.

**Dave Jones:** So, I'll link that up here and down below. I haven't watched the full thing, but like whoa, overload. It's probably got all the detail you could possibly want on all the various standards and protection modes that this thing covers under.

**Dave Jones:** It's just absolutely incredible. Okay, so what I'm going to do now is I'm going to experiment with this sucker and see if we can get it to actually simulate a car plugging in.

**Dave Jones:** Now, as I said, it all happens on the CP or control pilot pin here and this is basically outputs a 1 kHz square wave. And as I said, the duty cycle of that will then indicate to the car what the maximum charge current it can take is.

**Dave Jones:** And there's a formula for that. I'll put it up here. Here you go. So, now here's a diagram of from stole it from Wikipedia about basically what's going on here in terms of the car.

**Dave Jones:** So, basically, it's the control pilot pin relative to earth here. So, I've got two wires sticking out. You'll notice I've got a diode over here and my decade resistance box.

**Dave Jones:** So, it's basically a diode and resistance in there. And then the EVSE here will be able to determine what that the car's actually plugged in based on the value of resistance on there.

**Dave Jones:** So, it's a nominal 2.7 K here after the diode here. And the reason that they got the diode is because let's say that you got water, you know, it's raining or something, you got water into your connector here, then of course that can simulate a resistance.

**Dave Jones:** That can appear as a resistance and then that could actually turn on your it can activate the relays in here and can switch the power through and attempt to charge the car and you don't want that.

**Dave Jones:** So, the diode just adds some asymmetry in here to the waveform and we might be able to see that. I'll try and hook a scope up as well. Just can't get it all in one shot.

**Dave Jones:** That's all. But anyway, so that's the reason for the diode and then it switches a 1.3 K in parallel with that, which gives you about 880. So, let's dial that up to 880, something like that.

**Dave Jones:** And then we'll be able to switch between those two basically. Right, so I'm going to power this on and I've got it just set to 10 meg here. So, it'll just appear open to the charger.

**Dave Jones:** It won't know the difference. So, let's power it up. do do do It's very 8-bit. I love it. Right, so I set this uh just uh 2.8. I think that's going to be near enough to Oh, we can go down to 2.7.

**Dave Jones:** There you go. Okay, so I'll release the 1 meg um the 10 meg here. There you go. Ta-da! I've got waiting for EV. Okay, so it's detected that it's plugged in, but it's now waiting for the car.

**Dave Jones:** Okay, so if we uh go back uh to give about 880. Here we go. Ta-da! There we go. It's switched on. It's green. It's RCD checking, charging. It's now charging, but the car's not actually taking anything, as you can see over here on the display, but in theory, the car should be taking power.

**Dave Jones:** And then if we go back, um I'm not sure at what point it like unbalances, but you know, whoop. Cha- charge delayed. Okay, uh I think that's a software thing.

**Dave Jones:** It's got a charge delay thing in there, which yeah, I don't know. I haven't set this thing up. We haven't RTFM'd yet. Charge delayed. I don't know. The relay clicked again.

**Dave Jones:** Something's going on. I don't know. Yeah, but anyway, there you go. Cool, huh? You saw how that um just the diode and the resistance value on there uh detected that the car was plugged in uh with the uh 2.7 K, and then once you put the 1.3 K in parallel with that, then it determines that, which is 880 ohms through the diode, then it determines that uh yeah, well, let's

**Dave Jones:** start charging. So, it switches the relays inside this, switches the mains through, and that's basically, you know, all this thing does. It's just a a smart relay, pretty much.

**Dave Jones:** And there we go. We're in waiting for EV mode with the uh 2.7 K. And there you go. You can see the Oh, oh, no. It's the No, it's cuz it just went into restart mode.

**Dave Jones:** Oh, okay. Yeah, no, there it is again. There's your 1 kHz square wave. There you go. You can see that the duty cycle 53% there, which I think corresponds to the full 7 kW, which is what it's set up to by default or uh they're basically 32 amps.

**Dave Jones:** Aha, in the advanced settings here, you can set up the supply grid for the device itself. Ah, yeah, 31.8 amps. There you go. Let's just say 10.2 amps, shall we?

**Dave Jones:** All right, let's try that again. Ah, there we go. Got it. Got it. Ha, you didn't believe me, did you? There you go. So, the duty cycle is now only 17% there.

**Dave Jones:** So, that that tells the car, "Please, do not exceed uh that, you know, 10 amps or whatever based on that uh formula." You know, there's a bit of give or take there.

**Dave Jones:** Uh bit of how you're doing, but, you know, it's it's going to the whole idea is that it doesn't exceed the maximum wiring limitation, maximum fusing limitation, and whatever installation that you've got and the uh charger.

**Dave Jones:** Oops, it's There you go, it's vanished. It's got some, yeah, dot turd delay restart thing, but there you go. Cool, huh? Okay, so what I want to do now is just check what happens if I remove uh the diode.

**Dave Jones:** See if there's any uh fault detection on here. All right, there you go. Um nothing. It's hasn't detect It's just detected that, well, there's nothing there. It's not giving me any error, but the good thing is is that it's not going to um start the charging.

**Dave Jones:** Yeah, it doesn't matter if I go to 880 or whatever. Yep, it's just not going to keep doing it. So, yeah, it's doing its job. So, there you go.

**Dave Jones:** That's the basics of how the uh control pilot uh signal works there on the IEC 62196 and SAE J uh 1772 or whatever it is and the SAE J 3068 standards.

**Dave Jones:** There's all these different standards for different countries, but I believe like all that is very similar. There could be like uh you know, minor differences, and but that's how it all works.

**Dave Jones:** If you disconnect it, it knows it's disconnected like that. When you when you plug it in with the uh 2.8 K, it knows it's uh you know the There we go.

**Dave Jones:** Waiting for EV to do its thing, and then we can put that into charge mode. Cool bananas, huh? So, there you go. I hope you enjoyed that video, found it interesting.

**Dave Jones:** Um but I I would This is my first time playing around with uh one of these EVSE um chargers. So, it's really I mean, you know, I've been using my little uh piddly uh 10 amp 240 V jobby at home, but I haven't like played around with the signals and stuff like that.

**Dave Jones:** So, that's really cool. And like in theory, yeah, you could actually design and build your own one of these really, you know, fairly simply. In fact, there is an open um it's the Open EVSE um it's called.

**Dave Jones:** And reason I didn't get that one is cuz like it kind of sort of might have integration with the solar and stuff. I'm not sure like it's all just around.

**Dave Jones:** This one's everyone recommends this. Everyone says it's really nice. And yes, I thought I'd go with this. But I do have um the physical connector now. So, I could actually play around with the Open EVSE.

**Dave Jones:** If you want to be too, I can simply disconnect uh this one cuz it's not going to be permanently uh wired installed, and I can play around with um either do-it-yourself stuff with Open EVSE.

**Dave Jones:** But, yeah, there's not too much more to play around with here. This is just the basics of um of how it works. It's pretty simple. It's just a smart relay with, you know, ground fault protection and residual current protection and stuff like that.

**Dave Jones:** And this one's a little bit smarter in that uh it can use your excess solar based on a uh current clamp on the grid. So, anyway, yeah, subscribe to my EV Blog 2 channel if you want to um see like just like after I've installed this, I might actually um see if like that that wiring heats up, how much it I know it's going to heat up in the um the roof, like how

**Dave Jones:** much it heats up. Put that sort of videos on my second channel. I think I'm like just hundreds of subs away from 100k subscribers. I get my YouTube silver awards for my second channel.

**Dave Jones:** That's if they'll give it to me, anyway. Um so, yeah, over on EV blog, too. Catch you next time.
