---
video_id: iWOToL0KIe0
title: EEVblog #380 - Sony CCD Sensor Teardown
url: https://www.youtube.com/watch?v=iWOToL0KIe0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 33, "3": 53, "4": 69, "5": 81, "6": 98, "7": 118, "8": 138, "9": 150, "10": 166, "11": 186, "12": 207, "13": 227, "14": 247, "15": 271, "16": 291, "17": 312, "18": 332, "19": 352, "20": 372, "21": 392, "22": 412, "23": 429, "24": 453, "25": 477, "26": 501, "27": 526, "28": 554, "29": 574, "30": 599, "31": 615, "32": 631, "33": 659, "34": 683, "35": 712, "36": 732, "37": 752, "38": 773, "39": 789, "40": 813, "41": 833, "42": 858, "43": 878, "44": 898, "45": 918, "46": 934, "47": 958, "48": 974, "49": 999, "50": 1023, "51": 1047, "52": 1059, "53": 1088, "54": 1112, "55": 1132, "56": 1148, "57": 1169, "58": 1193, "59": 1205, "60": 1229, "61": 1250, "62": 1278, "63": 1294, "64": 1314, "65": 1342, "66": 1363, "67": 1379, "68": 1395, "69": 1411, "70": 1432, "71": 1452, "72": 1472, "73": 1488, "74": 1504, "75": 1525, "76": 1541, "77": 1565, "78": 1581, "79": 1602, "80": 1626, "81": 1642}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. I'm going to finish off tearing down this vintage 1985 Sony Video 8, the first Video 8 camcorder on the market back in 1985. And you saw me tear down the main guts of this before, and I'll link to the video down below if you

**Dave Jones:** haven't seen that. This is a follow-up where I didn't get time to tear down the CCD mechanism and the lens system like this, so a lot of people ask, can we see the CCD down in there and rip the rest of this apart?

**Dave Jones:** Yep, we can do that. And also the CRT viewfinder as well. Let's go for it. Now this lens mechanism, as we saw when we did the first teardown, is a bit of a work of art. There's a lot involved in this thing, the various motors for the zoom

**Dave Jones:** and for the focus mechanism, and there are four boards no less than four boards sandwiched in this part, in the back down here, five I think actually. So there's quite a lot of circuitry down in there to support the CCD sensor, which is clearly

**Dave Jones:** down in there. So we're going to have to crack open all of these boards one by one. There's four plastic retainers, oh there's two plastic retaining clips there, so we need to pop that off, this board should pop off, then we have to pop off the next one,

**Dave Jones:** the next one, and we should eventually get down to the CCD. Now it looks like I may actually have to cut off these little plastic clips here, it looks like they're not easily going to just squash and then lift the board off. They look like a one-shot

**Dave Jones:** deal almost. So I think I'll just snip that off there, and yep, it just lifts straight off. I've got black gunk over my finger already, not sure where that came from. Another retaining clip down in here, there we go, fold it out, and bingo!

**Dave Jones:** And on that board, more custom Sony stuff of course. Why they've put some celastic down there, I'm not sure. They've gunked, they've just gunked up a few of the pins there, I'm not actually sure why you'd bother to do that. Anyway, there's a couple of trim pots down here, who knows what they're doing.

**Dave Jones:** And check out the number of trim pots on this thing, there's 11 of them, four here, three here, two, one. And thankfully we can actually get a look down at the silkscreen, they have thoughtfully labelled those for us. So let's take a look.

**Dave Jones:** And I have no idea what those ones stand for off the top of my head. LX, R offset, and B offset. Who knows? And those two trim pots there, we've got Iris and AGC, the automatic gain control, and you can see that gunk down there beautifully now.

**Dave Jones:** And I don't know, is there like a little mod under there that they're trying to protect? I don't know. Weird. No sign of any mod under that, so why they've done that, your guess is as good as mine. More adjustments, MRI, MR2, MB1

**Dave Jones:** and MB2. Hmm. No idea. And there we have a good old 4000 series 4052, that's a dual four-way mux. And if you thought 11 adjustments on the other one wasn't enough, here we go! 18 trim pots on this. Check it out. Unbelievable. BM,

**Dave Jones:** RM, BY, RY, MPX, RB2, G2, RB1, G1, oh man! What do all these things do? WC, FG, APL? And we're not done yet folks, because if you flip it on its end of course, these ones, there's another 2, 4, 6, 8 trim pots there which are externally accessible.

**Dave Jones:** So it looks like these ones here were designed to be adjustable after sort of the whole assembly was put together. Now I'm not sure what's under this plastic cover here. 238-12 on it. I think I'm going to lift the skirt on that perhaps

**Dave Jones:** and have a look. No, it's not coming willingly. So maybe it is, yeah, it looks like it's some sort of through-hole component. It doesn't look like a large cap or anything like that. It's something different. And there's no shortage of test points on this thing, all those little posts down in there.

**Dave Jones:** So presumably somebody would have got the old scope probe onto those or something. Some test automated test system or something like that perhaps during the setup of this thing. Because I presume they're not just for servicing purposes. I would presume that they're also for

**Dave Jones:** adjustment during production, but there's a number of trimmers in this thing, it's just ridiculous really. And of course I just realized after the fact, as always, that I didn't have to cut off these black retaining clips here because on the bottom of this board there are these retaining clips

**Dave Jones:** down here, that's part of this plastic hinge mechanism here, which then lifts this board up, whoop, stuck down, there we go, it will come off, there we go, it's got a clip, and this just swings up like that for ease of servicing and adjustment.

**Dave Jones:** D'oh! So this is a rather neat system. It pops out like this, and then bingo, this board now folds out like this. Ta-da! Look at that! Beautiful! And looks like we've got some heavy shielding under here for the CCD and the video processing, presumably.

**Dave Jones:** So let's take a look at that, but as you can see, there's a whole bunch of surface mount stuff on the bottom of this board, all wave-soldered by the way as we explained in the previous video. Let's take a look at this board here, is the one that we have to

**Dave Jones:** crack open to get access to that CCD down in there. Hmm. And I was going to de-solder that, but eh, just easier to chop it off with the pair of side cutters. And there is the bottom of our CCD board, and we can see a couple of screws there which should allow us

**Dave Jones:** to pop that lens assembly off. I'm assuming that's the only thing holding that lens assembly onto this board. And it looks like that CCD is actually socketed. If you have a look at the sort of that dual-in-line header down there, you can see the silkscreen around

**Dave Jones:** that. And taking the screws off, and you can sort of see I don't know if you can see down in there, but it looks like there's a socket right down in there that this thing is sitting on. So let's so if I've undone those screws, let's see if this thing

**Dave Jones:** pops out. Oh, yeah! Ta-da! It's out. There it is. Literally is a dual-wipe socket, and the CCD is still down in there. Neat. And it looks like they didn't have enough room on the main board, so they had to squeeze in another couple of little daughter boards around here

**Dave Jones:** with sort of a, one of those ribbon, clear ribbon cables there, board-to-board interconnect, directly soldered in. But these, looks like they do pop out with a plastic retaining clip. So, bingo. And no, that wasn't a heatsink, that was just a metal retaining clip, or you know,

**Dave Jones:** some sort of board mounting clip. And there's two DIP-8 packages on here. These are Texas Instruments SN75361. And I checked, and they're TTL-to-MOS converters. So they convert, you know, 5 volts TTL into MOS logic level. Presumably, the MOS logic level is what is required for the CCD.

**Dave Jones:** So driving the CCD, I presume, because it's not going from MOS to TTL, it's going from TTL to MOS. So maybe they're driving the clock for the CCD or something to that effect. And there's yet another small application, strategic application of gunk. Why?

**Dave Jones:** And we found our main crystal clock driver board, 28.375 MHz main oscillator here with a regular HC49U package, 17.73 447 MHz. And down under there, another 8-pin DIP package, it's a Motorola MMH0026CP1. And that is a dual MOS clock driver. So just like the other MOS TTL-to-MOS

**Dave Jones:** drivers over here, this one is presumably driving the clock to the CCD itself, which would be MOS signal level. And that sucker can drive up to 1.5 amps, so it can drive really highly capacitive MOS loads, which presumably is what the CCD sensor requires.

**Dave Jones:** And here it is, here's what everyone wanted to see, the Sony CCD sensor. It's an IU021KAA, if that means anything to you if you want to do a Google search perhaps. And you can see it looks like a standard ceramic DIP package in there, with the

**Dave Jones:** side-mounted pins like that, you can see the gold pins coming out. So this is just a clamp mechanism to hold that chip in place on the back there. So if we undo these screws here, we should pop out and we should get a CCD with a window on the top of it.

**Dave Jones:** It may not even have a window, it may actually not be windowed at all, it may be just totally exposed. And here it is, they've got a couple of long threaded screws in there, and that should lift off. Ta-da! Oh, look at that!

**Dave Jones:** No, it's still got another housing protecting it in there. Geez. I'll take out more screws. Alright, let's lift the skirt on this thing, and see, ta-da! Ah, look at that! Beautiful. And it looks like we have a rubber surround here, which just lifts off, and that gives us

**Dave Jones:** the glass-windowed CCD. Look at that! It's certainly not a standard DIP package, it's got integrated screw mounts and everything else. It's really super-specialized. I wonder how much it cost to manufacture this sucker in 1999. And there you have it, a Sony CCD sensor chip

**Dave Jones:** state-of-the-art for 1985. Look at that! Beautiful. And if we pop it over, we've got 621026 on the bottom, no idea what that means, but there you go, that is a beautiful little 240 lines resolution CCD sensor. And that's totally crazy. And that's totally crotch-moistening state-of-the-art technology

**Dave Jones:** for 1985. Ha ha! And I was able to just pop off the polycarbonate cover there. No, it's not actually glass, it is some sort of polycarbonate material. And we're getting closer down into the main die down in there, but I doubt we're actually going to be able to

**Dave Jones:** see anything down in there anyway. Here I'm using my Mantis Elite microscope, 3D microscope at the moment, I'm sticking my camera through the viewfinder here, and of course you don't get the 3D effect that this Mantis scope is capable of. And it's only a x10 lens, unfortunately, so that's the best

**Dave Jones:** I could do. I tried using my x40 Olympus stereo microscope, and I was able to use that with my eyes, and it looked quite good, but unfortunately I couldn't get any decent video through that, so I'm using my Mantis here. And there's the entire sensor array, and I'm not

**Dave Jones:** sure if you'll be able to see it, but you should eventually be able to see if you zoom in close enough, I'm using the camcorder zoom at the moment, you should be able to see the individual red, green, blue color lines. Maybe not.

**Dave Jones:** I was thinking if you counted them all up, you would actually get that 240 lines or something claimed by Sony for this CCD camera. Ah, bingo! Check it out, I was able to finally get it under my stereo Olympus microscope. So if we zoom out,

**Dave Jones:** there we go, look at that! You can see the individual red, green, and blue elements. The greens are done as lines, and the looks like the red and the blue are done as looks like little two, looks like group of two elements. Now I'll show you the setup that I'm using here.

**Dave Jones:** I'm using my secondary camcorder, which is a Canon HF-M400, and this is my main camcorder of course, which is the Canon HF-G10, and there's my Opteka x10 macro lens on there, and it's pushed right up against the x10 eyepiece of my Olympus SZ series stereo

**Dave Jones:** microscope. This is a really nice stereo microscope, mentioned it before if you can pick them up on eBay. And there's the sensor down there, and I've got a x2 Barlow lens on there, so normally this is 0.7 times, if you have it there, 0.7 times

**Dave Jones:** with the x10 eyepiece up here, it's normally 7 times to 40 times around there, so it's 4 x 10 is 40 times, but I've got the 2 x Barlow lens on there, so I've got a combined magnification of 80 times on the Olympus SZ

**Dave Jones:** stereo microscope. And although I've got the x10 Barlow lens on the Canon here, if I zoom right out, of course that just allows me to, you know, I really have to zoom in x10 like that to get a look at the individual pixels like that, but there you go, you can

**Dave Jones:** see that, and the interesting thing is, I'm not using my ring light here. I've got the ring light for the thing, but I turn it on, and actually, I'll turn it on, let me, I'll show you the display here now, I'll turn it on, there we go,

**Dave Jones:** and it makes very little, if any, difference at all to the light that's actually on the image. But what makes a difference, right? Let me switch off my main LED lights up here, and you'll find that the image will completely vanish. So I've got my remote control here, switch off my lights,

**Dave Jones:** and bingo! The image has completely vanished, even though I've got that ring light on there trying to light that thing up. So the light is actually coming through the second eyepiece here. And if you don't believe me, let me switch it back on.

**Dave Jones:** Okay, got my main LED lights back on, I'll switch off the ring light here, and watch this. I can't get it both in shot, look, I'll move my hand over, look, over that eyepiece. Look, if I completely cover up that eyepiece, there's nothing!

**Dave Jones:** So I'm actually getting the reflected light coming through that second eyepiece. That's the thing that actually makes or breaks this thing. Go figure, it's like it's working reverse to how an ordinary stereo microscope could, should, and normally does work in terms of having the ring light on the actual object.

**Dave Jones:** But for this particular setup, it needs the light coming through here, and if I get my ring light here, I can make it really really bright by putting it near the lens, that second eyepiece there. Look at that! Amazing! And I found that it really

**Dave Jones:** doesn't matter how close I get that ring light or whether or not I attach it, you know, properly to the bottom under there, because this has to be real close. I took it off there, I was originally getting issues, and I found that I didn't

**Dave Jones:** actually need the thing. What I needed was light through that second eyepiece. And I can really get some rather ghostly artifacts actually by playing around with the ring light on the other side of this thing. Look at that! I'm putting the ring light probably a centimeter away

**Dave Jones:** from the other eyepiece there, and it's it is rather unusual optical phenomenon. I think it's really quite neat. So if I put the ring light directly into the eyepiece and I adjust the brightness, I can adjust the brightness of the displayed image as well.

**Dave Jones:** So that's rather neat. Clearly the light's reflecting down there and going through the stereo optics and bouncing back out. And let's get back to the main lens mechanism here. Another board under here with a Ricoh chip down in there. It's not a Sony chip, which most

**Dave Jones:** of the chips in this thing have been Sony, but that's some sort of Ricoh device. I'm not actually sure what. Let's get in there. It's a Ricoh RF5L01, whatever the hell that is. And we've got our motors for the zoom. That would be the zoom.

**Dave Jones:** Yep, that would be the zoom. No, sorry. That's, yes, that's the zoom motor there. And here we would have our focus motor. There it is. So that, argh! Eventually, very high torque thing there. There we go. That's a, there we go, you can see it

**Dave Jones:** really spinning fast around in there if I move the focus. There we go. So that's a high torque gearbox there. And down in here we have our little iris motor. It's a four-wire job down in there, and that sets, it's only like a quarter, like an eighth turn

**Dave Jones:** or something like that. You can see that armature on there, perhaps. I don't know, it's a bit dark down in there. But it only turns like a quarter of a turn, and that sets your iris. So let's have a look down the lens here.

**Dave Jones:** And I can open and close the iris. Check it out. Ta-da! Fully open, and all the way closed. Neat. And I don't think there's any point taking that lens apart. There's no electronics in there, it's just a typical zoom lens assembly, really. But that is, that is quite neat.

**Dave Jones:** And that would have been state-of-the-art for 1985. And of course I just love the electronics construction, all this foldy construction like this. Really very, very nice. That's almost a work of art. You could just sit that up on the bench and just admire the beauty of that all day long.

**Dave Jones:** Now let's take a squiz at this electronic viewfinder. It's powered from 5 volts, it's a model VF-206, and it's got a multi-pin weird-ass little sort of DIN-type adapter there, but presumably this will just accept 5 volts in and send a regular composite video signal, and

**Dave Jones:** it should have a little miniature CRT in there, and just take that composite signal and have the electronics in it to decode it and drive the CRT. And it's going to have the high voltage stuff as well required for any one of, you know, those

**Dave Jones:** CRTs. We do have a brightness adjust pot down in there, but apart from that, yeah, there's not much there at all. So it's operation should be pretty simple. And ta-da! Yep, it's going to pop open. Here we go. Hey, there we go. Oh look at that!

**Dave Jones:** Beautiful. And that is exactly what you'd expect to see in this. There's the CRT assembly that just pops right out there. Pretty much works like a standard CRT, except it's just super-duper miniature. And once again the, you know, high voltage safety rules apply here, wouldn't have the same amount of energy

**Dave Jones:** that a, you know, like a CRT monitor or a TV would have, but just got to be careful nonetheless. So we pop the PCB out here. Yeah, not much on that at all. All through-hole stuff. Nice and surface mount on the back of course, but yeah, there's not much to it.

**Dave Jones:** And of course these miniature CRTs work exactly like their big brothers you get in TVs, monitors, your oscilloscope, or whatever. They're going to work exactly the same. There's going to be like a heater up here, there's going to be a cathode here to generate the electrons,

**Dave Jones:** then there's going to be a couple of anode grids in there, and you're going to have your X and Y deflection coils in here, and your phosphor screen up the top here, and that's, you know, pretty much works exactly like, does work exactly like a regular

**Dave Jones:** CRT, except it's just miniature. And well, it's cute! Look at it! I like it! You can see there's a couple of adjustment pots on here on the other side of the board, but they've got access holes on the bottom here, so we've got like a horizontal frequency, we've got vertical hole, we've got

**Dave Jones:** vertical size, we've got focus down here somewhere, yeah, focus, we've got contrast, and stuff like that. So a few little adjustments you'd expect to find on something like this. And on the other side of the board, we've got one main chip that controls it all, a Hitachi HA11141

**Dave Jones:** and a few large electrodes, a few trim pots, and a metal can, the high voltage multiplier for the tube. As you can see, the high voltage wire going over to the CRT. So that is pretty much all she wrote, there's not much in that

**Dave Jones:** at all. And if you're wondering what these wires are doing going up into here, I believe they're for little indicator lights inside, here you go, it tells you that there's three little indicator lights that show up within the screen to tell you that you've got low light and your

**Dave Jones:** low run battery is going bad, and your white balance as well. So they're three LED indicators, so they'd be three little LEDs somewhere in there, I'm not sure, oh yeah, there they are. There they are, you can probably see it, there they are, down there, so they

**Dave Jones:** would reflect onto the image. But that's all there is in this thing, it's just there's the front of the CRT there, and there's a mirror which just reflects it directly out here, and then there's got an eye adjust as well. Not much to it.

**Dave Jones:** Now unfortunately I don't actually remember this working from the unit itself, so there could actually be a fault with this thing, and well, I haven't got time for today, so I am going to leave this thing. I've done a preliminary power-up of it,

**Dave Jones:** I think I've found the 5 volt input, it's a little bit hard to trace these boards with all the silkscreen on there, it's a bit of a pain in the butt actually, but I think I've found the 5 volt input, and I've powered it up, it's drawing about 120 milliamps

**Dave Jones:** or so, which I don't know, seems about right I guess. But yeah, nothing happens, so really this is going to require some work for another video. But these little miniature CRTs are fun little things if you salvage an old video camera. Camcorder, they were still using these up into the

**Dave Jones:** 2000s I think, these little miniature CRTs, well definitely into the 2000s, these little miniature CRTs. So they're really quite nice, you can use them for lots of novel little projects, I really like them. So hopefully I can get this one up and running.

**Dave Jones:** So if anyone's got the full schematic for this viewfinder, please let me know, it is a Sony VF-206 electronic viewfinder, so that would be most helpful if we could get a schematic for this thing, and hopefully try and get this CRT working, and hopefully it's not

**Dave Jones:** busted, you know, irreversibly busted. Hopefully it either works or there's just something wrong with the circuit, or something perhaps we'll have to see. So there you have it, that's a look inside a 1985 vintage state-of-the-art Sony camcorder and its CCD sensor, and the electronics in the little CRT

**Dave Jones:** viewfinder. And if you like Teardown Tuesday, please give it a big thumbs up, and if you want to discuss it, the best place to do that is not in the YouTube comments, although you can certainly do that. The best place to interact and discuss all my videos is over at the EEVblog forum.

**Dave Jones:** The link is below. Catch you next time.
