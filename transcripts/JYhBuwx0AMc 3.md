---
video_id: JYhBuwx0AMc
title: EEVblog #326 - Makerbot Replicator Teardown
url: https://www.youtube.com/watch?v=JYhBuwx0AMc
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 29, "3": 42, "4": 57, "5": 69, "6": 83, "7": 97, "8": 113, "9": 128, "10": 142, "11": 159, "12": 175, "13": 189, "14": 205, "15": 218, "16": 233, "17": 246, "18": 256, "19": 273, "20": 286, "21": 301, "22": 317, "23": 334, "24": 348, "25": 359, "26": 375, "27": 392, "28": 408, "29": 423, "30": 435, "31": 450, "32": 466, "33": 481, "34": 495, "35": 510, "36": 526, "37": 538, "38": 550, "39": 565, "40": 576, "41": 596, "42": 613, "43": 625, "44": 647, "45": 666, "46": 680, "47": 695, "48": 711, "49": 728, "50": 744, "51": 759, "52": 773, "53": 789, "54": 802, "55": 820, "56": 835, "57": 848, "58": 861, "59": 874, "60": 884, "61": 896, "62": 911, "63": 930, "64": 947, "65": 968, "66": 984, "67": 1000, "68": 1013, "69": 1026, "70": 1037, "71": 1054, "72": 1070, "73": 1086, "74": 1099, "75": 1114, "76": 1125, "77": 1139, "78": 1155, "79": 1171, "80": 1186, "81": 1201, "82": 1216, "83": 1229, "84": 1241, "85": 1256, "86": 1272, "87": 1287, "88": 1305, "89": 1321, "90": 1337, "91": 1356, "92": 1373, "93": 1389, "94": 1403, "95": 1416, "96": 1430, "97": 1447, "98": 1461, "99": 1477, "100": 1490, "101": 1504, "102": 1520, "103": 1534, "104": 1550, "105": 1566, "106": 1580, "107": 1594, "108": 1608}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Got the MakerBot Replicator here. A few people have asked to see what's under the hood of this puppy cuz it's not do-it-yourself anymore. You don't build it yourself. It's very consumery. It's still open source, so that means we'll

**Dave Jones:** have access or you'll have access to all the info available in this thing. So, I thought I'd flip it upside down and have a look under the hood. You know what we say here on the EEVblog, don't turn it

**Dave Jones:** on. Take it apart. One of the good things is you can't actually just flip it up on one end like this and not a problem at all and it gives you access to the electronics under the bottom panel here and there's

**Dave Jones:** clearly this panel here. There's one screw on top with a uh square nut in there which is uh the technique that they use to uh assemble the whole thing basically, but it's got this panel with uh a with um hooks on here and here and

**Dave Jones:** here and here going in opposite direction, so looks like if you take out that screw, this panel is just going to drop down a little bit and lift it and it should just lift out that way. We should have access to the electronics.

**Dave Jones:** Uh clearly the electronics is not mounted on this base plate cuz there's no screws here, but uh let's take it off and see what's under there. And of course you could easily lose that nut. Yep, I just did. It just dropped down on

**Dave Jones:** the floor. Saw where it went. Here we go. So, you know, it'd be better if they had some other system in place, but tada, there it is. We've just got one board which does the whole lot, which is

**Dave Jones:** a big uh difference to the if you see the uh video for the MakerBot uh Thing-O-Matic, the assembly of it, it had multiple boards all over the base plate. This has been replaced by just one with uh five little daughter boards

**Dave Jones:** there which are probably the uh motor drivers. We'll have to have a look at that, but yeah, it's very clean. And here we go, we finally found the fan in here that makes all that uh racket when the thing's switched on, and

**Dave Jones:** no wonder it does. It's only a tiny little piss-ant fan here which uh sucks the air in from I'll show you down here in a second, but uh sucks it from basically uh inside the cabinet here over the electronics and down and out

**Dave Jones:** the side here and out these bottom bits. And there's the fan. What brand is that? I'm trying to read that upside down. A Fonsoning? Fonsonic or something like that? Uh it's a 24-V uh fan, a little tiny piss-ant thing,

**Dave Jones:** really. It's uh Hope those uh nuts those square nuts don't uh fall off there. They've used no uh Loctite on that, I don't think, anyway. So, what it's attempting to do here is suck air through uh from the main cavity up the top there

**Dave Jones:** through to the fan. But, of course, there's no um thing There's nothing here actually blocking this off. So, if you wanted to do that properly, you would actually put something that blocks here and over there so the fan So, the uh air

**Dave Jones:** is ducted from inside the cavity there through the fan and out. Otherwise, you've got, you know, recirculation uh stuff happening here, and clearly they've decided that they need uh some fan uh you know, a fan in here cuz they've got like a, you know, motor

**Dave Jones:** controllers on here which uh get warm, of course, and uh fair enough. Maybe they've done some measurements, some calculations, how hot it was, got a fan, but yeah, they haven't implemented that right in two ways. One, there's no duct

**Dave Jones:** in there, and two, it takes the air from within the main cavity, of course. And what have you got inside the main cavity? Well, you've got a massive heated build plate which is heating up tens or 100 W or something. I

**Dave Jones:** don't know how much power goes into that, and you've got the hot head and nozzle as well. So, I'm glad it's actually got these cutouts on the side of the thing. So, you know, you can get some relatively cool air.

**Dave Jones:** Imagine if this thing was uh sealed. If you put some plastic over this or something to I don't know, to make it look funky. It would actually get quite warm inside there and it'd be sucking the hot air

**Dave Jones:** through the fan into here. So, that's a I don't know what Actually, I don't think much thought went into that. So, really, there's an obvious way to do this correctly, and that's to do away with these standoffs here

**Dave Jones:** completely. Don't have that and get rid of your ducting problem at the same time. Get rid of that. Mount the fan directly onto the side of the case like this and laser cut some you know, a big cutout in

**Dave Jones:** there with the fan on the side. So, it sucks the air in from the outside, the cool air Well, the ambient room temperature air into here and over there and you can do away with the standoffs and and you know, you've got 100% ducting

**Dave Jones:** from the outside. So, yeah. I think they've got that a bit wrong. I'm going to flip this sucker up the other way because uh so we can access it cuz this board has the text on up the other way. So, be

**Dave Jones:** careful not to grab the top, of course, as I mentioned you could actually ruin the thing Well, you're not ruin it, but you could potentially bend some of the rods in there, which hold the thing. So, there we go, and we should be able to

**Dave Jones:** access the board and the silk screens the right way up. Actually, I was just thinking this It's almost as if this little fan here was maybe an afterthought and they didn't want to cut holes in the side or maybe they didn't

**Dave Jones:** want to cut holes inside for the looks. I don't know. So they thought they'd use the existing hole going up through the case, but I don't know. I don't like it. Now this main control board here is designed by

**Dave Jones:** and we'll show you the silkscreen in a second, Jeremy Blum, who's been on the Amp Hour show. He's a fellow blogger. So check out his channel, which is I think Sci-Guy 14 on YouTube and he works for MakerBot or did over the

**Dave Jones:** summer and he designed this board and he actually tweeted to me when I got this thing, "Please go easy on him for the design." You're not getting off easily, Jeremy. And there it is, designed by Jeremy Blum based on the Arduino Mega platform and

**Dave Jones:** license is GPL version 3 and there's the open source hardware symbol. Brilliant. And that's one of the things I complained about is that nobody put last time when I did the schematic. Nobody put their name on this thing, but they certainly

**Dave Jones:** have this time. Jeremy has and a whole other bunch of names up here. And there's the design team. I won't you know, actually read them all out, but Bre's name is in there. Charles Pax who sent this MakerBot to me and a whole

**Dave Jones:** bunch of other names I don't recognize, but they're obviously working at MakerBot and it's good to see that they've put some pride in this and they've put their name on there. In fact, they're the dream team. There you

**Dave Jones:** go. Now here's something interesting on the side of the board. There's a micro SD card slot. There's no cutout in the side of the case and I'm not sure why they've done that. It's something called Club Mate. I have no

**Dave Jones:** idea what that is. I'm sure it means something inside the MakerBot team or within the MakerBot community perhaps and it's um, for refined palettes. There you go, I love it. So, uh, clearly this is, um, put in there as

**Dave Jones:** a deliberate design decision, uh, for, you know, people in the know who maybe want to, uh, hack this thing or, you know, customize it in some certain way. You can put a micro SD, solder in a micro SD card. There you'd have to take

**Dave Jones:** out the board to, uh, put in the, uh, thing. Anyway, um, to slide the card in, but clearly you can able to do that and maybe do some customy type stuff. I like it. And the main controller here is an

**Dave Jones:** ATmega 1280 and as we, uh, saw on the silk screen, it's based on the ATmega platform cuz clearly, uh, you know, they didn't want to, uh, use an Arduino mega in here cuz that, costs extra money. It's an extra board,

**Dave Jones:** an extra complexity, etc., etc. You got to build shields and, uh, it turned, you know, it's it's the thing, it's the previous thingamajig. So, they decided to consolidate and that's the beautiful thing about source hardware is that because all, you're, uh, the design info

**Dave Jones:** is all out there, you can download it, you can customize it, but the main important thing about open source hardware is that it doesn't use the non-commercial license. And there's a lot of people out there that say, "Oh,

**Dave Jones:** why doesn't open source hardware, you know, allow you to use the non-commercial license? If you want to use the logo here, the open source hardware logo, why can't you have the right to have the non-commercial license? Well, here

**Dave Jones:** is a classic case. Um, the Arduino, uh, guys designed the Arduino and boards in the Arduino mega in this case which this design's based on, but if MakerBot wanted to do this, which they they clearly have, they wanted to customize

**Dave Jones:** it for their own purposes and use it and sell it commercially, if it had that non-commercial clause in there, they wouldn't be able to do that. The community wouldn't grow, you know, and And one would be able to build upon

**Dave Jones:** other things. They wouldn't want to cuz they know they can't use it commercially. So, that is why the open source hardware community do not allow and do not tolerate the having a non-commercial clause in a license. And they've got two six-pin standard

**Dave Jones:** ICSP in-circuit serial programming headers. One here is as it says on the label, one's for the 1280, that's the main ATmega device. And this one here is labeled 8U2, and that goes to the 8U2 device over here, which handles the USB

**Dave Jones:** port just like on the new generation Arduino Megas. And here we go, this is called the Mighty Board Rev E. I don't know if there's a more recent version, we need to check it out. They've put in the web address,

**Dave Jones:** makerbot.com/docs/mightyboard. I love open source hardware. There's the info. Woohoo, we can check it out. We can modify this thing, do whatever we want. Brilliant. Houston, we have a botch. Classic solder botch between two pins on what looks like an optocoupler. And

**Dave Jones:** there's another botch. We've got a mod wire here and a classic sliced trace there, cut straight through, and bridge between these two power devices. One's an LM340 low drop out voltage regulator. I'm familiar with that one, and the other

**Dave Jones:** one, can't quite see the number. But there you go. Botches, couple of botches on the board. Never send a human to do a machine's job. Agent Smith. We are living in the matrix, folks. And over here we have the HBP, the heated

**Dave Jones:** build platform. That's those wires going off there. We've got an extra, not sure what that is. And once again, LEDs for all the FETs up there. I'm interested to see the circuit for that. Is that it just tells you if the FET is uh switched

**Dave Jones:** on uh basically. I assume that's uh that's what it means there and and then we've got a fan which drives the little puppy down in the corner. And here we've got some expansion headers for the UART and the I squared C bus and presumably

**Dave Jones:** are some spare IO from the uh main ATmega processor. Excellent. And a couple of more status LEDs for uh that are unlabeled. And there's a circuitry and the connector driving the wanky RGB LED strip but and it says 24 volts only

**Dave Jones:** with an exclamation mark. So presumably it's designed to drive uh large uh numbers of uh series connected LEDs only. And there's a thermocouple uh input for I've only got the single extruder. So if you had the dual extruder, you'd be

**Dave Jones:** using the second channel thermocouple there. And as for the axes limit switches here, they've got uh a Z axis minimum and the Y axis minimum. They're not Oh, sorry. And the Z maximum uh ones they're there. They're designed

**Dave Jones:** in but they don't utilize them. And there's our five stepper motor boards. One of them's not uh utilized and we'll have to take these off and see what's on there. And no surprises, there's just a stepper motor uh driver which is in this

**Dave Jones:** case an Allegro uh 4982 and a couple of uh support con- components and that's uh all she wrote. And this is an intelligent device. It's not just a grunty uh motor driver. It's a serial in so it accepts uh serial

**Dave Jones:** commands or serial step commands from the main Arduino processor and it's designed to take the burden off that processor. So the processor just sends through a serial uh pulse or a serial command saying, "I just want you to

**Dave Jones:** advance one step on your stepper motor, please." And uh this chip handles all of the logistics of doing that. And it's the MakerBot BotStep 17E. Huh, is it Rev at 17? I don't know. It's a Rev E V E. I'm not sure why they call

**Dave Jones:** it 17, but uh there you go. They've decided to put them on uh separate boards as opposed to the main board. Um the design decision uh for that would probably uh be based on the fact that, you know, you want to separate Um it's

**Dave Jones:** not a bad design choice to separate your motor control from from your processing uh board, cuz then you can design your processor board real quick, get everyone up and working on the software, and then you can refine your motor stepper board.

**Dave Jones:** And if you want to change your uh stepper motors or anything like that, you can change the board in the future instead of having to change the main board. So, that was probably the de- the design decision there to put it on a

**Dave Jones:** separate board. And they may have even had somebody who knows uh you know, a thing or two about uh stepper motors to design this board. And you can see the uh the chip obviously has a thermal pad under it um

**Dave Jones:** cuz that's where the chip is, and you've got uh the nine uh vias there going from one side to the other, classic thermal coupling. And that would have had solder paste on the bottom of the chip and a

**Dave Jones:** thermal pad on there to get all the heat out. And they use all the uh copper flood uh fill here, which is uh yes, it is grounded. There it is, you can see it uh thermally relieved to the ground pin

**Dave Jones:** there. And uh that's used as a heat sink. My only issue with this would be the uh symmetry of the board. I.E., you can put it in that way, or you can put it in uh that way. And presumably, if you put it

**Dave Jones:** in upside down, well, something's going to release the magic smoke. Woohoo! Hey, there's a little uh well, a big ass tantalum under there as well. And here's the data sheet for the A4982 microstepping driver from Allegro MicroSystems Inc. And uh it's I highly

**Dave Jones:** recommend you uh check it out if you're interested in uh how these sorts of uh stepper motor driver controllers work. Very good bedtime reading these sorts of data sheets. Features and benefits, it's got low RDS, yeah, automatic current delay, uh mixed

**Dave Jones:** and slow current delay, synchronous rectification for brilliant. Um in internal uh undervoltage lockout as well, crossover current protection, uh works from 3.3 and 5-V uh compatible logic, um available in QFN and TSSOP packages. Boo. Anyway, uh par for the course. Um

**Dave Jones:** it's got built-in thermal shutdown, short-to-ground protection, short-at-load protection, so you know, everything doesn't blow up. And what I love, no smoke, no fire compliance. I love it. What that means is it tells you um over here, here it is,

**Dave Jones:** uh the ET package meets customer requirements for no smoke, no fire designs by adding no connect pins between critical output sense and supply pins. So, in case of a pin-to-adjacent pin short, the device does not cause smoke or fire. Doesn't let out the magic

**Dave Jones:** smoke. I love it. Um additionally, the device does not cause smoke or fire when any pin is shorted to ground or left open. So, you know, if you're using that lead-free soldering as most stuff is these days, and you've and you've got

**Dave Jones:** some tin whiskers or something like that, which grow, uh look it up, Google it if you don't know what it is, uh tin whiskers between two adjacent pads, which is a little uh short which can grow between two pads, bingo, this

**Dave Jones:** thing's not going to blow up because if you have a look at the uh package, I'm sure we can go down and have a look at the pinouts, usually right at the end. So, if I jump down to the end here,

**Dave Jones:** uh we should have the pin outs. Here we go. And uh it should have no connect pins between the various outputs. Here it is. Uh yes, the ET package. If you get the LT package here, um you don't get that

**Dave Jones:** uh extra protection. But, the ET package here, if we have a look at it, we can see that the uh between all the critical pins, out 1B and VBB here, they've got NC, no connect. So, there's that physical

**Dave Jones:** um spacing between those two pins. And using the thing's really easy. It's just got a very simple uh interface here to microcontroller. It doesn't use that many uh pins. It's got a sleep mode. You don't have to enable that if you don't

**Dave Jones:** want, but it's basically got a step control input. It's got a direction input, you know, forwards or backwards. It's got an enable and a reset. And uh MS1 and MS2 there, they're uh just the uh step selection pins. You could have

**Dave Jones:** those fixed or come from the microcontroller. That just tells you how far it's going to step with each pulse on the step input. Um so, very easy to drive with a microcontroller. And it takes all the burden away from

**Dave Jones:** the uh software in the microcontroller. It doesn't They don't doesn't have to be any phase look up tables or anything. It doesn't need to know or care about how to drive the step motor. All it needs is which All

**Dave Jones:** All the software needs to know is which direction you want to go and step. Bang. That's it. And the chip takes care of everything. So, that's the beautiful part about using an external uh controller like this, which is a bit

**Dave Jones:** more intelligent than just your regular uh you know, then just driving a H-bridge directly uh from your microcontroller, where you've got to take all that stuff for driving a particular step motor into account. So, that's a really um nice design decision

**Dave Jones:** there. I like it. And here's a simplified internal uh diagram. We've got a couple of DACs here. We've got our serial inputs, got regulators up here. It's got a charge pump for generating the required voltages. And uh it's got a built-in um

**Dave Jones:** uh built-in H-bridge. And uh it gets that name from the shape of the circuit. If you picture where my cursor is there going down like that, these two these four these two MOSFETs down this side, the two MOSFETs down here, and then the

**Dave Jones:** motor which is physically connected outside, but usually it's drawn with the motor in between there, and it forms a letter H. That's why it's called a H-bridge. And it's a very uh versatile and powerful way to uh drive a motor

**Dave Jones:** like this. So, it's got a dual H-bridge like that, all the required control circuitry to drive it, all some current sense resistors RS1 and RS2 here, and uh supply which is uh they've called VBB. And one of the things I love about these

**Dave Jones:** data sheets and why they make excellent reading is it's got typical layout information about how you lay out the boards. People ask, "Well, how should I lay out a particular circuit? Well, how do I learn it?" Well, read data sheets

**Dave Jones:** like this and follow these example layouts. And it tells you why various things are important. Look at this. It's got the uh thermal vias going with here, the thermal pad under there to get the heat out. It'll probably have some

**Dave Jones:** calculations on that. And uh it shows you where you have to play the place the capacitors. In this case uh we've got some bulk capacitance here. And interestingly, um if you remember that uh uh the image of the the board we looked

**Dave Jones:** at, it doesn't have any huge bulk capacitance on that board on the plug-in motor control board. It was actually looks like the bulk capacitance is that uh large uh tantalum capacitor, that the yellow one you saw like a deep package

**Dave Jones:** tantalum on the main on the main Maker Bot board. It wasn't on this motor control board and I think that's a bit of a mistake. It It certainly deserves and should be on this main board. Of course, you will have a high frequency

**Dave Jones:** ceramic bypass cap there as well, which might be C6 or something like that down in there, but you know, those bulk capacitances can be further away from the particular chip because they don't handle the high frequency current spikes. So, the inductance the

**Dave Jones:** longer traces doesn't as matter as much. So, you know, they can get away with having it on the main board, but it's not good design practice. It should the bulk capacitance should have certainly been on this board. And in my previous video, a few people

**Dave Jones:** mentioned that they noticed that the LCD backlight or something happened to the LCD. It dimmed or something when I manually moved physically moved the motors on the you know, on one of the axes and they said that could be due to

**Dave Jones:** possibly they've left out the reverse protection or the what's called a catch diode in in the H bridge motor driver circuit and in the data sheet here I sure enough it shows you all the um the pin configurations what's inside each pin

**Dave Jones:** and here's the motor outputs down here of course and and of course, there are two diodes in here. These two here. There are two catch diodes there, but they are the the parasitic as it actually mentions there. They're the parasitic diode which is

**Dave Jones:** inherent in the physical construction of the MOSFET and I've done a tutorial video on this before. So, you can go look that one up. And uh um often they are adequate uh for the task, but uh you've got to be very

**Dave Jones:** careful um in in terms of uh specking them to, you know, to really know if they are suitable or not. You certainly may still need um external catch diodes, and I'm not going to go into a detailed analysis of uh all their Maker Bot

**Dave Jones:** design and the motors and everything else to uh tell you if they're if their external ones were actually required, but they're clearly not using external uh catch diodes. I don't see any on the uh board here. Uh haven't checked the

**Dave Jones:** haven't checked the schematic yet, but there's physically none there, so they're obviously relying on the internal uh diodes in parasitic ones inside the device. And you can see there's a couple of other uh parasitic uh ones here as well, and uh other ones

**Dave Jones:** built into the various control pins. And of course, there's lots of juicy info on uh the motor drive uh waveforms here and the different uh modes they can drive it in. So, this makes really good reading, and there's the uh uh step sequence uh

**Dave Jones:** table for the various uh phases and how they step and whether you've got it in full step mode, half step, quarter step, or, you know, 1/16 step mode. There those two pins uh that we saw MS1, MS2, they would select um

**Dave Jones:** these these four different uh modes here. And uh that is, you know, all the stuff which uh ordinarily uh your software might have had to take care of, but it's much easier to just design in a chip. That's all handled for you. Make

**Dave Jones:** no mistakes. Spend your design effort somewhere else where it's needed. And if you have a look under the stepper motor boards here, you can see these three vias here, and they've left those uh untinted. So, they've removed the

**Dave Jones:** solder mask. You can see the other vias on the board, they're all tinted, of course, but these ones deliberately left it off, and they've labeled them, see Y enable and then there's the Z ones over here, step and direction. Um they are

**Dave Jones:** presumably look like classic uh test point access. So, they might have a uh bed of nails uh tester for this board to uh individually um check the channel. So, they plug this board into a big test jig, presumably. Um or it might even be

**Dave Jones:** a debugging thing. I don't know if if it's actually a production uh test thing, but uh it could certainly be either. Um and it allows you to probe the signals uh from either side of the board because the solder mask is uh left

**Dave Jones:** exposed there. And I do like boards that have ground points there, so you can solder in a pin or a loop there. So, when you're uh debugging this thing during development, um you've got a very convenient ground access point for your

**Dave Jones:** oscilloscope. So, overall, that's not a bad uh little board. It's a nice consolidation, nice example of consolidating uh the existing Thing-O-Matic. I'll have to compare the schematics, you know, to see how uh different it is to the Thing-O-Matic.

**Dave Jones:** It's going to be very uh similar. How to combine all those uh different boards together. The Thing-O-Matic had like five or six boards in it into the one unit. And because it's open source hardware, they were able to do that, and

**Dave Jones:** it's done quite neat. So, uh Jeremy, your reputation is intact there there. Um you know, there's a few little issues, but that's a nice uh nice little layout. I like it. And as far as the cable management in

**Dave Jones:** here goes, I mean, it's not uh perfect, but it's uh certainly uh more than adequate. They've done a good uh job at going up to the main uh extruder head, of course. I noted that on the review and unboxing there, but you know, uh

**Dave Jones:** generally considering that it's uh uh, most of the time. There's a few loosies around here, but uh yeah, they've generally done a quite a good job. It's certainly a lot better than the Thingamajig.
