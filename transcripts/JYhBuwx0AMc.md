---
video_id: JYhBuwx0AMc
title: EEVblog #326 - Makerbot Replicator Teardown
url: https://www.youtube.com/watch?v=JYhBuwx0AMc
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 25, "3": 42, "4": 65, "5": 76, "6": 91, "7": 108, "8": 119, "9": 145, "10": 159, "11": 175, "12": 192, "13": 208, "14": 225, "15": 237, "16": 246, "17": 256, "18": 273, "19": 286, "20": 301, "21": 315, "22": 328, "23": 349, "24": 364, "25": 384, "26": 396, "27": 408, "28": 417, "29": 431, "30": 445, "31": 461, "32": 477, "33": 490, "34": 508, "35": 531, "36": 541, "37": 550, "38": 571, "39": 593, "40": 616, "41": 629, "42": 644, "43": 662, "44": 672, "45": 684, "46": 695, "47": 715, "48": 728, "49": 747, "50": 758, "51": 769, "52": 782, "53": 796, "54": 811, "55": 820, "56": 845, "57": 856, "58": 869, "59": 881, "60": 892, "61": 903, "62": 914, "63": 937, "64": 951, "65": 965, "66": 993, "67": 1007, "68": 1029, "69": 1040, "70": 1054, "71": 1067, "72": 1082, "73": 1091, "74": 1101, "75": 1117, "76": 1126, "77": 1150, "78": 1163, "79": 1176, "80": 1193, "81": 1214, "82": 1222, "83": 1234, "84": 1246, "85": 1262, "86": 1275, "87": 1301, "88": 1311, "89": 1325, "90": 1356, "91": 1371, "92": 1382, "93": 1394, "94": 1412, "95": 1423, "96": 1441, "97": 1454, "98": 1474, "99": 1488, "100": 1501, "101": 1516, "102": 1526, "103": 1541, "104": 1555, "105": 1566, "106": 1576, "107": 1589, "108": 1603, "109": 1615}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Got the MakerBot Replicator here. A few people have asked to see what's under the hood of this puppy cuz it's not do-it-yourself anymore. You don't build it yourself.

**Dave Jones:** It's very consumery. It's still open source, so that means we'll have access or you'll have access to all the info available in this thing. So, I thought I'd flip it upside down and have a look under the hood.

**Dave Jones:** You know what we say here on the EEVblog, don't turn it on. Take it apart. One of the good things is you can't actually just flip it up on one end like this and not a problem at all and it gives you access to the electronics under the bottom panel here and there's clearly this panel here.

**Dave Jones:** There's one screw on top with a uh square nut in there which is uh the technique that they use to uh assemble the whole thing basically, but it's got this panel with uh a with um hooks on here and here and here and here going in opposite direction, so looks like if you take out that screw, this panel is just going to drop down a little bit and lift it and

**Dave Jones:** it should just lift out that way. We should have access to the electronics. Uh clearly the electronics is not mounted on this base plate cuz there's no screws here, but uh let's take it off and see what's under there.

**Dave Jones:** And of course you could easily lose that nut. Yep, I just did. It just dropped down on the floor. Saw where it went. Here we go. So, you know, it'd be better if they had some other system in place, but tada, there it is.

**Dave Jones:** We've just got one board which does the whole lot, which is a big uh difference to the if you see the uh video for the MakerBot uh Thing-O-Matic, the assembly of it, it had multiple boards all over the base plate.

**Dave Jones:** This has been replaced by just one with uh five little daughter boards there which are probably the uh motor drivers. We'll have to have a look at that, but yeah, it's very clean.

**Dave Jones:** And here we go, we finally found the fan in here that makes all that uh racket when the thing's switched on, and no wonder it does. It's only a tiny little piss-ant fan here which uh sucks the air in from I'll show you down here in a second, but uh sucks it from basically uh inside the cabinet here over the electronics and down and out the side here and out these bottom bits.

**Dave Jones:** And there's the fan. What brand is that? I'm trying to read that upside down. A Fonsoning? Fonsonic or something like that? Uh it's a 24-V uh fan, a little tiny piss-ant thing, really.

**Dave Jones:** It's uh Hope those uh nuts those square nuts don't uh fall off there. They've used no uh Loctite on that, I don't think, anyway. So, what it's attempting to do here is suck air through uh from the main cavity up the top there through to the fan.

**Dave Jones:** But, of course, there's no um thing There's nothing here actually blocking this off. So, if you wanted to do that properly, you would actually put something that blocks here and over there so the fan So, the uh air is ducted from inside the cavity there through the fan and out.

**Dave Jones:** Otherwise, you've got, you know, recirculation uh stuff happening here, and clearly they've decided that they need uh some fan uh you know, a fan in here cuz they've got like a, you know, motor controllers on here which uh get warm, of course, and uh fair enough.

**Dave Jones:** Maybe they've done some measurements, some calculations, how hot it was, got a fan, but yeah, they haven't implemented that right in two ways. One, there's no duct in there, and two, it takes the air from within the main cavity, of course.

**Dave Jones:** And what have you got inside the main cavity? Well, you've got a massive heated build plate which is heating up tens or 100 W or something. I don't know how much power goes into that, and you've got the hot head and nozzle as well.

**Dave Jones:** So, I'm glad it's actually got these cutouts on the side of the thing. So, you know, you can get some relatively cool air. Imagine if this thing was uh sealed.

**Dave Jones:** If you put some plastic over this or something to I don't know, to make it look funky. It would actually get quite warm inside there and it'd be sucking the hot air through the fan into here.

**Dave Jones:** So, that's a I don't know what Actually, I don't think much thought went into that. So, really, there's an obvious way to do this correctly, and that's to do away with these standoffs here completely.

**Dave Jones:** Don't have that and get rid of your ducting problem at the same time. Get rid of that. Mount the fan directly onto the side of the case like this and laser cut some you know, a big cutout in there with the fan on the side.

**Dave Jones:** So, it sucks the air in from the outside, the cool air Well, the ambient room temperature air into here and over there and you can do away with the standoffs and and you know, you've got 100% ducting from the outside.

**Dave Jones:** So, yeah. I think they've got that a bit wrong. I'm going to flip this sucker up the other way because uh so we can access it cuz this board has the text on up the other way.

**Dave Jones:** So, be careful not to grab the top, of course, as I mentioned you could actually ruin the thing Well, you're not ruin it, but you could potentially bend some of the rods in there, which hold the thing.

**Dave Jones:** So, there we go, and we should be able to access the board and the silk screens the right way up. Actually, I was just thinking this It's almost as if this little fan here was maybe an afterthought and they didn't want to cut holes in the side or maybe they didn't want to cut holes inside for the looks.

**Dave Jones:** I don't know. So they thought they'd use the existing hole going up through the case, but I don't know. I don't like it. Now this main control board here is designed by and we'll show you the silkscreen in a second, Jeremy Blum, who's been on the Amp Hour show.

**Dave Jones:** He's a fellow blogger. So check out his channel, which is I think Sci-Guy 14 on YouTube and he works for MakerBot or did over the summer and he designed this board and he actually tweeted to me when I got this thing, "Please go easy on him for the design."

**Dave Jones:** You're not getting off easily, Jeremy. And there it is, designed by Jeremy Blum based on the Arduino Mega platform and license is GPL version 3 and there's the open source hardware symbol.

**Dave Jones:** Brilliant. And that's one of the things I complained about is that nobody put last time when I did the schematic. Nobody put their name on this thing, but they certainly have this time.

**Dave Jones:** Jeremy has and a whole other bunch of names up here. And there's the design team. I won't you know, actually read them all out, but Bre's name is in there.

**Dave Jones:** Charles Pax who sent this MakerBot to me and a whole bunch of other names I don't recognize, but they're obviously working at MakerBot and it's good to see that they've put some pride in this and they've put their name on there.

**Dave Jones:** In fact, they're the dream team. There you go. Now here's something interesting on the side of the board. There's a micro SD card slot. There's no cutout in the side of the case and I'm not sure why they've done that.

**Dave Jones:** It's something called Club Mate. I have no idea what that is. I'm sure it means something inside the MakerBot team or within the MakerBot community perhaps and it's um, for refined palettes.

**Dave Jones:** There you go, I love it. So, uh, clearly this is, um, put in there as a deliberate design decision, uh, for, you know, people in the know who maybe want to, uh, hack this thing or, you know, customize it in some certain way.

**Dave Jones:** You can put a micro SD, solder in a micro SD card. There you'd have to take out the board to, uh, put in the, uh, thing. Anyway, um, to slide the card in, but clearly you can able to do that and maybe do some customy type stuff.

**Dave Jones:** I like it. And the main controller here is an ATmega 1280 and as we, uh, saw on the silk screen, it's based on the ATmega platform cuz clearly, uh, you know, they didn't want to, uh, use an Arduino mega in here cuz that, costs extra money.

**Dave Jones:** It's an extra board, an extra complexity, etc., etc. You got to build shields and, uh, it turned, you know, it's it's the thing, it's the previous thingamajig. So, they decided to consolidate and that's the beautiful thing about source hardware is that because all, you're, uh, the design info is all out there, you can download it, you can customize it, but the main important thing about open source

**Dave Jones:** hardware is that it doesn't use the non-commercial license. And there's a lot of people out there that say, "Oh, why doesn't open source hardware, you know, allow you to use the non-commercial license?

**Dave Jones:** If you want to use the logo here, the open source hardware logo, why can't you have the right to have the non-commercial license? Well, here is a classic case.

**Dave Jones:** Um, the Arduino, uh, guys designed the Arduino and boards in the Arduino mega in this case which this design's based on, but if MakerBot wanted to do this, which they they clearly have, they wanted to customize it for their own purposes and use it and sell it commercially, if it had that non-commercial clause in there, they wouldn't be able to do that.

**Dave Jones:** The community wouldn't grow, you know, and And one would be able to build upon other things. They wouldn't want to cuz they know they can't use it commercially. So, that is why the open source hardware community do not allow and do not tolerate the having a non-commercial clause in a license.

**Dave Jones:** And they've got two six-pin standard ICSP in-circuit serial programming headers. One here is as it says on the label, one's for the 1280, that's the main ATmega device. And this one here is labeled 8U2, and that goes to the 8U2 device over here, which handles the USB port just like on the new generation Arduino Megas.

**Dave Jones:** And here we go, this is called the Mighty Board Rev E. I don't know if there's a more recent version, we need to check it out. They've put in the web address, makerbot.com/docs/mightyboard.

**Dave Jones:** I love open source hardware. There's the info. Woohoo, we can check it out. We can modify this thing, do whatever we want. Brilliant. Houston, we have a botch. Classic solder botch between two pins on what looks like an optocoupler.

**Dave Jones:** And there's another botch. We've got a mod wire here and a classic sliced trace there, cut straight through, and bridge between these two power devices. One's an LM340 low drop out voltage regulator.

**Dave Jones:** I'm familiar with that one, and the other one, can't quite see the number. But there you go. Botches, couple of botches on the board. Never send a human to do a machine's job.

**Dave Jones:** Agent Smith. We are living in the matrix, folks. And over here we have the HBP, the heated build platform. That's those wires going off there. We've got an extra, not sure what that is.

**Dave Jones:** And once again, LEDs for all the FETs up there. I'm interested to see the circuit for that. Is that it just tells you if the FET is uh switched on uh basically.

**Dave Jones:** I assume that's uh that's what it means there and and then we've got a fan which drives the little puppy down in the corner. And here we've got some expansion headers for the UART and the I squared C bus and presumably are some spare IO from the uh main ATmega processor.

**Dave Jones:** Excellent. And a couple of more status LEDs for uh that are unlabeled. And there's a circuitry and the connector driving the wanky RGB LED strip but and it says 24 volts only with an exclamation mark.

**Dave Jones:** So presumably it's designed to drive uh large uh numbers of uh series connected LEDs only. And there's a thermocouple uh input for I've only got the single extruder. So if you had the dual extruder, you'd be using the second channel thermocouple there.

**Dave Jones:** And as for the axes limit switches here, they've got uh a Z axis minimum and the Y axis minimum. They're not Oh, sorry. And the Z maximum uh ones they're there.

**Dave Jones:** They're designed in but they don't utilize them. And there's our five stepper motor boards. One of them's not uh utilized and we'll have to take these off and see what's on there.

**Dave Jones:** And no surprises, there's just a stepper motor uh driver which is in this case an Allegro uh 4982 and a couple of uh support con- components and that's uh all she wrote.

**Dave Jones:** And this is an intelligent device. It's not just a grunty uh motor driver. It's a serial in so it accepts uh serial commands or serial step commands from the main Arduino processor and it's designed to take the burden off that processor.

**Dave Jones:** So the processor just sends through a serial uh pulse or a serial command saying, "I just want you to advance one step on your stepper motor, please." And uh this chip handles all of the logistics of doing that.

**Dave Jones:** And it's the MakerBot BotStep 17E. Huh, is it Rev at 17? I don't know. It's a Rev E V E. I'm not sure why they call it 17, but uh there you go.

**Dave Jones:** They've decided to put them on uh separate boards as opposed to the main board. Um the design decision uh for that would probably uh be based on the fact that, you know, you want to separate Um it's not a bad design choice to separate your motor control from from your processing uh board, cuz then you can design your processor board real quick, get everyone up and working on the software, and then

**Dave Jones:** you can refine your motor stepper board. And if you want to change your uh stepper motors or anything like that, you can change the board in the future instead of having to change the main board.

**Dave Jones:** So, that was probably the de- the design decision there to put it on a separate board. And they may have even had somebody who knows uh you know, a thing or two about uh stepper motors to design this board.

**Dave Jones:** And you can see the uh the chip obviously has a thermal pad under it um cuz that's where the chip is, and you've got uh the nine uh vias there going from one side to the other, classic thermal coupling.

**Dave Jones:** And that would have had solder paste on the bottom of the chip and a thermal pad on there to get all the heat out. And they use all the uh copper flood uh fill here, which is uh yes, it is grounded.

**Dave Jones:** There it is, you can see it uh thermally relieved to the ground pin there. And uh that's used as a heat sink. My only issue with this would be the uh symmetry of the board.

**Dave Jones:** I.E., you can put it in that way, or you can put it in uh that way. And presumably, if you put it in upside down, well, something's going to release the magic smoke.

**Dave Jones:** Woohoo! Hey, there's a little uh well, a big ass tantalum under there as well. And here's the data sheet for the A4982 microstepping driver from Allegro MicroSystems Inc. And uh it's I highly recommend you uh check it out if you're interested in uh how these sorts of uh stepper motor driver controllers work.

**Dave Jones:** Very good bedtime reading these sorts of data sheets. Features and benefits, it's got low RDS, yeah, automatic current delay, uh mixed and slow current delay, synchronous rectification for brilliant.

**Dave Jones:** Um in internal uh undervoltage lockout as well, crossover current protection, uh works from 3.3 and 5-V uh compatible logic, um available in QFN and TSSOP packages. Boo. Anyway, uh par for the course.

**Dave Jones:** Um it's got built-in thermal shutdown, short-to-ground protection, short-at-load protection, so you know, everything doesn't blow up. And what I love, no smoke, no fire compliance. I love it. What that means is it tells you um over here, here it is, uh the ET package meets customer requirements for no smoke, no fire designs by adding no connect pins between critical output sense and supply pins.

**Dave Jones:** So, in case of a pin-to-adjacent pin short, the device does not cause smoke or fire. Doesn't let out the magic smoke. I love it. Um additionally, the device does not cause smoke or fire when any pin is shorted to ground or left open.

**Dave Jones:** So, you know, if you're using that lead-free soldering as most stuff is these days, and you've and you've got some tin whiskers or something like that, which grow, uh look it up, Google it if you don't know what it is, uh tin whiskers between two adjacent pads, which is a little uh short which can grow between two pads, bingo, this thing's not going to blow up because if

**Dave Jones:** you have a look at the uh package, I'm sure we can go down and have a look at the pinouts, usually right at the end. So, if I jump down to the end here, uh we should have the pin outs.

**Dave Jones:** Here we go. And uh it should have no connect pins between the various outputs. Here it is. Uh yes, the ET package. If you get the LT package here, um you don't get that uh extra protection.

**Dave Jones:** But, the ET package here, if we have a look at it, we can see that the uh between all the critical pins, out 1B and VBB here, they've got NC, no connect.

**Dave Jones:** So, there's that physical um spacing between those two pins. And using the thing's really easy. It's just got a very simple uh interface here to microcontroller. It doesn't use that many uh pins.

**Dave Jones:** It's got a sleep mode. You don't have to enable that if you don't want, but it's basically got a step control input. It's got a direction input, you know, forwards or backwards.

**Dave Jones:** It's got an enable and a reset. And uh MS1 and MS2 there, they're uh just the uh step selection pins. You could have those fixed or come from the microcontroller.

**Dave Jones:** That just tells you how far it's going to step with each pulse on the step input. Um so, very easy to drive with a microcontroller. And it takes all the burden away from the uh software in the microcontroller.

**Dave Jones:** It doesn't They don't doesn't have to be any phase look up tables or anything. It doesn't need to know or care about how to drive the step motor. All it needs is which All All the software needs to know is which direction you want to go and step.

**Dave Jones:** Bang. That's it. And the chip takes care of everything. So, that's the beautiful part about using an external uh controller like this, which is a bit more intelligent than just your regular uh you know, then just driving a H-bridge directly uh from your microcontroller, where you've got to take all that stuff for driving a particular step motor into account.

**Dave Jones:** So, that's a really um nice design decision there. I like it. And here's a simplified internal uh diagram. We've got a couple of DACs here. We've got our serial inputs, got regulators up here.

**Dave Jones:** It's got a charge pump for generating the required voltages. And uh it's got a built-in um uh built-in H-bridge. And uh it gets that name from the shape of the circuit.

**Dave Jones:** If you picture where my cursor is there going down like that, these two these four these two MOSFETs down this side, the two MOSFETs down here, and then the motor which is physically connected outside, but usually it's drawn with the motor in between there, and it forms a letter H.

**Dave Jones:** That's why it's called a H-bridge. And it's a very uh versatile and powerful way to uh drive a motor like this. So, it's got a dual H-bridge like that, all the required control circuitry to drive it, all some current sense resistors RS1 and RS2 here, and uh supply which is uh they've called VBB.

**Dave Jones:** And one of the things I love about these data sheets and why they make excellent reading is it's got typical layout information about how you lay out the boards.

**Dave Jones:** People ask, "Well, how should I lay out a particular circuit? Well, how do I learn it?" Well, read data sheets like this and follow these example layouts. And it tells you why various things are important.

**Dave Jones:** Look at this. It's got the uh thermal vias going with here, the thermal pad under there to get the heat out. It'll probably have some calculations on that. And uh it shows you where you have to play the place the capacitors.

**Dave Jones:** In this case uh we've got some bulk capacitance here. And interestingly, um if you remember that uh uh the image of the the board we looked at, it doesn't have any huge bulk capacitance on that board on the plug-in motor control board.

**Dave Jones:** It was actually looks like the bulk capacitance is that uh large uh tantalum capacitor, that the yellow one you saw like a deep package tantalum on the main on the main Maker Bot board.

**Dave Jones:** It wasn't on this motor control board and I think that's a bit of a mistake. It It certainly deserves and should be on this main board. Of course, you will have a high frequency ceramic bypass cap there as well, which might be C6 or something like that down in there, but you know, those bulk capacitances can be further away from the particular chip because they don't handle the high

**Dave Jones:** frequency current spikes. So, the inductance the longer traces doesn't as matter as much. So, you know, they can get away with having it on the main board, but it's not good design practice.

**Dave Jones:** It should the bulk capacitance should have certainly been on this board. And in my previous video, a few people mentioned that they noticed that the LCD backlight or something happened to the LCD.

**Dave Jones:** It dimmed or something when I manually moved physically moved the motors on the you know, on one of the axes and they said that could be due to possibly they've left out the reverse protection or the what's called a catch diode in in the H bridge motor driver circuit and in the data sheet here I sure enough it shows you all the um the pin configurations what's inside each pin

**Dave Jones:** and here's the motor outputs down here of course and and of course, there are two diodes in here. These two here. There are two catch diodes there, but they are the the parasitic as it actually mentions there.

**Dave Jones:** They're the parasitic diode which is inherent in the physical construction of the MOSFET and I've done a tutorial video on this before. So, you can go look that one up.

**Dave Jones:** And uh um often they are adequate uh for the task, but uh you've got to be very careful um in in terms of uh specking them to, you know, to really know if they are suitable or not.

**Dave Jones:** You certainly may still need um external catch diodes, and I'm not going to go into a detailed analysis of uh all their Maker Bot design and the motors and everything else to uh tell you if they're if their external ones were actually required, but they're clearly not using external uh catch diodes.

**Dave Jones:** I don't see any on the uh board here. Uh haven't checked the haven't checked the schematic yet, but there's physically none there, so they're obviously relying on the internal uh diodes in parasitic ones inside the device.

**Dave Jones:** And you can see there's a couple of other uh parasitic uh ones here as well, and uh other ones built into the various control pins. And of course, there's lots of juicy info on uh the motor drive uh waveforms here and the different uh modes they can drive it in.

**Dave Jones:** So, this makes really good reading, and there's the uh uh step sequence uh table for the various uh phases and how they step and whether you've got it in full step mode, half step, quarter step, or, you know, 1/16 step mode.

**Dave Jones:** There those two pins uh that we saw MS1, MS2, they would select um these these four different uh modes here. And uh that is, you know, all the stuff which uh ordinarily uh your software might have had to take care of, but it's much easier to just design in a chip.

**Dave Jones:** That's all handled for you. Make no mistakes. Spend your design effort somewhere else where it's needed. And if you have a look under the stepper motor boards here, you can see these three vias here, and they've left those uh untinted.

**Dave Jones:** So, they've removed the solder mask. You can see the other vias on the board, they're all tinted, of course, but these ones deliberately left it off, and they've labeled them, see Y enable and then there's the Z ones over here, step and direction.

**Dave Jones:** Um they are presumably look like classic uh test point access. So, they might have a uh bed of nails uh tester for this board to uh individually um check the channel.

**Dave Jones:** So, they plug this board into a big test jig, presumably. Um or it might even be a debugging thing. I don't know if if it's actually a production uh test thing, but uh it could certainly be either.

**Dave Jones:** Um and it allows you to probe the signals uh from either side of the board because the solder mask is uh left exposed there. And I do like boards that have ground points there, so you can solder in a pin or a loop there.

**Dave Jones:** So, when you're uh debugging this thing during development, um you've got a very convenient ground access point for your oscilloscope. So, overall, that's not a bad uh little board.

**Dave Jones:** It's a nice consolidation, nice example of consolidating uh the existing Thing-O-Matic. I'll have to compare the schematics, you know, to see how uh different it is to the Thing-O-Matic.

**Dave Jones:** It's going to be very uh similar. How to combine all those uh different boards together. The Thing-O-Matic had like five or six boards in it into the one unit.

**Dave Jones:** And because it's open source hardware, they were able to do that, and it's done quite neat. So, uh Jeremy, your reputation is intact there there. Um you know, there's a few little issues, but that's a nice uh nice little layout.

**Dave Jones:** I like it. And as far as the cable management in here goes, I mean, it's not uh perfect, but it's uh certainly uh more than adequate. They've done a good uh job at going up to the main uh extruder head, of course.

**Dave Jones:** I noted that on the review and unboxing there, but you know, uh generally considering that it's uh uh, most of the time. There's a few loosies around here, but uh yeah, they've generally done a quite a good job.

**Dave Jones:** It's certainly a lot better than the Thingamajig.
