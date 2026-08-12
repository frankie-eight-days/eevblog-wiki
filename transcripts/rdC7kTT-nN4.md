---
video_id: rdC7kTT-nN4
title: EEVblog #257 - Makerbot Troubleshooting
url: https://www.youtube.com/watch?v=rdC7kTT-nN4
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 25, "3": 39, "4": 56, "5": 70, "6": 90, "7": 105, "8": 122, "9": 130, "10": 144, "11": 158, "12": 170, "13": 183, "14": 201, "15": 213, "16": 231, "17": 244, "18": 263, "19": 277, "20": 292, "21": 311, "22": 332, "23": 350, "24": 365, "25": 374, "26": 387, "27": 401, "28": 414, "29": 425, "30": 439, "31": 451, "32": 464, "33": 480, "34": 494, "35": 509, "36": 528, "37": 547, "38": 562, "39": 576, "40": 596, "41": 607, "42": 629, "43": 642, "44": 657, "45": 673, "46": 687, "47": 697, "48": 711, "49": 727, "50": 747, "51": 762, "52": 779, "53": 794, "54": 811, "55": 822, "56": 850, "57": 871, "58": 885, "59": 900, "60": 917, "61": 939, "62": 957, "63": 974, "64": 991, "65": 999, "66": 1026, "67": 1043, "68": 1058, "69": 1069, "70": 1093, "71": 1104, "72": 1126, "73": 1144, "74": 1165, "75": 1179, "76": 1193, "77": 1208, "78": 1226, "79": 1263, "80": 1275, "81": 1288, "82": 1300, "83": 1309, "84": 1325, "85": 1338, "86": 1352, "87": 1366, "88": 1386, "89": 1403, "90": 1419, "91": 1441, "92": 1455, "93": 1469, "94": 1481, "95": 1490, "96": 1504, "97": 1522, "98": 1535, "99": 1545, "100": 1565, "101": 1574, "102": 1587}
---

**Dave Jones:** Hi, this is Phil. Phil's got a PhD in laser physics and he's a patent attorney, which means he's on the dark side of the force, but he's decided to come to the good side of the force and become the new EE blog apprentice.

**Dave Jones:** So, he's trying to he's got to learn the correct tongue angle. So, going to teach him that. And uh uh hand us the uh the left-handed screwdriver there, Phil.

**Dave Jones:** Yep. It's a right-handed one. Man, come on. You got to learn. Let's get this wrong. Noobs. I don't know. He's got a lot to learn. Anyway, we're going to uh calibrate our Makerbot here and uh print something.

**Dave Jones:** Let's go. And here's our finished Makeabot thingamatic. And it's serial number 68 7. There it is. And it looks rather neat. You've uh seen these before. or it it doesn't light up like some of the other uh ones do.

**Dave Jones:** They've obviously installed some um uh lighting inside. Mine doesn't have that. The power supply was really dodgy um to install that, but uh it's apparently the type supplied with this one.

**Dave Jones:** And I've got a the new uh Mark 7 step extruder inside there. And that's the Z axis platform. I haven't cable tied down any of the wires yet. So, all the wiring is uh is all loose in there because I want to um figure out what the maximum range of the platforms is before I actually do that.

**Dave Jones:** But that is a Makeabot thingamatic. It's ready to go. So, we'll uh plug it in, we'll calibrate it, and we'll give it a burl. And our first print. Wonder what we'll print.

**Dave Jones:** H. Now, here's one thing I don't really understand. And they've got these really nice um uh bearings on here that the shafts slide into. But this one on this side doesn't have the bearings on either side.

**Dave Jones:** And there's a bit of play in there. I'm not sure if you can actually see that, but I can actually wiggle that up and down. And I'm not sure why.

**Dave Jones:** Um there's no bearings in there. They didn't supply them and they didn't tell me to actually put them in. Strange. But anyway, that's the uh Y axis platform. There we've got the X-axis platform on top here.

**Dave Jones:** That one does have the bearings on either side, and it feels reasonably smooth. Um, and as you can see, the wiring inside these things is is really just um is just hanging there basically.

**Dave Jones:** Um, so it is a bit messy on the inside. And on the top side here is our Z platform which is this motor here with this worm screw drive there.

**Dave Jones:** And that moves this entire platform on the top here. And if we get down and we take a look at the underside of it there, you can see it see the entire Z axis platform move.

**Dave Jones:** And it's got the uh step extruder on there where your uh your filament goes in the top here. It all heats up. Um, it's got a a heater. It's got a heater in there, a ceramic heater, plus a thermal uh overload and a thermouple as well.

**Dave Jones:** There's a safety cutout PCB over here uh which is designed to cut it out if it uh goes over temperature. And that's about uh all there is to the um XY mechanical platform.

**Dave Jones:** It's fairly simple, but the build itself uh is is fairly complicated. It took probably 14 15 hours for the two of us to actually fully assemble this thing. All right, we got our Makeabot switched on and connected to USB and we've updated the uh firmware.

**Dave Jones:** So, we're going to and disconnect. I'm going to reconnect down here and we're using the Replicator G uh program and connect to the unit. And we're connected. We've updated the uh firmware.

**Dave Jones:** We've gone through the process and uh we're going to do the calibration. So, what we do is we go up to file up here and scripts calibration and we run the thingomatic calibration G-code and then we hit the build button.

**Dave Jones:** So, the script is in there. We hit build and now it's telling us move the build platform until the nozzle lies in the center and then turn the threaded rod until the nozzle just touches the surface without pressing onto it.

**Dave Jones:** Okay. So, we want to change that. We want to put it directly in the center there. So, we want to put it the nozzle just a smidgen off the surface.

**Dave Jones:** Is that just off? That's just off. Just off. Half a bee's dick off the surface there. And that looks like it's in the center. Near enough. I'm not sure if you have to do this calibration routine um every time because I'm not sure that the machine knows where the absolute position of those sensors is.

**Dave Jones:** Tongue angle fill. All right. So, what we're going to do is we'll hit yes. And here we go. Woohoo. There it goes. And it should hit the top micro switch in there, the limit switch.

**Dave Jones:** And bang. And this thing. And the build platform is now centering itself. Back to that position. The micro switched on there for the X and the Y. So our three limit switches clearly work.

**Dave Jones:** X, Y, and Z limit switches. And we're done. That's the calibration. Simple. Okay. So, now we're set in the we're in the control panel uh software and we're going to test the tool head temperature and the heated build platform temperature.

**Dave Jones:** So, it tells us to type in a target temperature of uh 225°C for the tool head. So, we've done that and pressed enter. And as you can see, it's ramped up there.

**Dave Jones:** That's our target temperature. In blue there and red, you can see the temperature is actually ramping up. And it says to do 120°. Is that right, Phil? 120 for the build platform.

**Dave Jones:** So, we type that in, press enter. Our target temperature has jumped up there in yellow. And we'll see the white line there, the build platform current temperature ramping up.

**Dave Jones:** So, both those will eventually ramp up to their set temperatures. And they should they should remain there. They shouldn't uh overshoot or anything like that. So, this could take a few minutes.

**Dave Jones:** And the tool head is uh didn't overshoot. It's maintained. It's ramped up and then maintained the set temperature. The build platform's not quite there yet, but it's on its way.

**Dave Jones:** Okay. Our tool head has reached temperature and now it's telling us to stick the filament into the chosen red cuz red goes faster. Stick it in. And then what, Phil?

**Dave Jones:** Well, it seems that we've got a problem. No matter how hard we push in here, no matter how many times we actuate the motor and uh try and get the filament to grab in there, it's just just not working.

**Dave Jones:** So, I don't know. Plan B. Well, we tried this fluuro green one and we did get it to grab. So, we're supposed to see a thin bead come out of the bottom.

**Dave Jones:** We still up to temperature 225. Oh, yep. There we go. Got it. Woohoo. There we go. Switch it off. Press stop. Awesome. There you go. We got a hanger.

**Dave Jones:** And look at that. There we go. That Well, that's technically that's the first thing we [Laughter] printed. Bit of hot snot. Hey. Yeah. Floss. Floss. Beautiful. Works a treat.

**Dave Jones:** Agreed. Okay, we're ready to print something. We've loaded in Yoda's lightsaber. Very cool. We've put it vertically. We've centered it on the platform and flipped it. What do we do now, Phil?

**Dave Jones:** Generate G-code. All right. I assume it knows that. Well, it fits within that area. I'm assuming we're going to have enough uh stuff filament and generate G-code. You have made changes to this model.

**Dave Jones:** Any unsaved changes? Ah, no. There we go. Python interpreter. Would you like to visit? Ah, fail. Come on. one. Okay, we've installed the stupid Python interpreter. And I've scaled that down really tiny.

**Dave Jones:** We want this thing to print. I have no idea if this is a good first example, but let's generate the G-code. Save the model. Nope. There we go. It's doing something.

**Dave Jones:** Now, what do we do? Oh, how do we set up our Oh, use raft. Okay. Yep. Yeah. Use prinomatic. Got it. Step layer height.3 mm. The perimeter thicker. Well, default to one.

**Dave Jones:** Yep. Feed rate 30 mm/s. Okay. And we're using a 1.75 mm ABS mark. Yep. 7, I'm assuming. Ah, that's the different material. Okay. Well, we're definitely using ABS. We're not using PLA.

**Dave Jones:** So, what is this? Plastic material type ABS. Filament diameter 1.8. I think it is. Yep. I don't know. We'd have to actually get the calipers out and measure that.

**Dave Jones:** Between 75 and 1.8. Okay, that'll do. Extruder nozzle diameter. No idea. 4. Yep. Okay. Done. Do we generate geocodes? Not automatically generate when building. Go. Phil says go. Go.

**Dave Jones:** We're going. We're generating. We're almost there for the total number of layers for the inset. The inset procedure. Now we got to do the fill procedure. How many procedures are there?

**Dave Jones:** More than you can poke a stick at. You can see the different processes that goes through. carve process, uh, preface, inset, fill, speed, temperature, and raft procedure. But it's still going.

**Dave Jones:** Not done yet. Man, it's taking all day. And we there were like another there were comb cool procedure, reversal procedure, and it's done. Woohoo. It's printing now. It's moving.

**Dave Jones:** It's doing something that the it's given us an estimated build time on the software of what is it? 1 hour and 28 minutes. A man, we're hoping to do this before Jim.

**Dave Jones:** Oh well, have to head home and come back later and uh see if it's finally built. Do I dare leave this thing on its own or will it replicate and start Skynet?

**Dave Jones:** Uh-oh. Something's gone wrong here. It's hitting the end over here and there's no end stop. It just won't go any further. And uh Oh, no. It's Well, yeah, it's printing.

**Dave Jones:** It's printing, but it certainly didn't uh didn't do it in the center. No, no, it's No, didn't center on the pad. Why not? We went through the calibration procedure.

**Dave Jones:** No, our first print is a failure. and it uh doesn't stick to the aluminum surface. If you actually have a look down in there, we probably should have put that myar sheet on, but it's it's all just curled up.

**Dave Jones:** So, our that's our first print. It's a Oh, it's a nice pattern though. I rather like it. But there you go. First print fail. All right. So, what we've done now is we've made the current position zero in the control panel.

**Dave Jones:** So, we've moved it so it's in the center. And we've done that and we've we're building again. But, uh maybe we should put down some myar tape. But, uh why is it going back up to start?

**Dave Jones:** Well, there you go. Okay, we're at least getting somewhere now. We haven't figured out how to um center it properly on the pad yet, but um we managed to stick on some myar very quickly before we started this print job.

**Dave Jones:** I think it's probably laying down some sort of base maybe cuz that doesn't look like our object. So, not sure what it's doing there, but it seems to it's almost like printing out too much.

**Dave Jones:** No, that's doing a small amount. There we go. Okay, so it is controlling the amount of And now it's decided that it needs to do another print on the other side.

**Dave Jones:** What What's going on here? Wow. I no idea what it's doing. It's almost as if it's printing it down sideways. sideways, you know. Oh, fail. Look at that. It's just picked up the whole lot of it and dragged it across.

**Dave Jones:** This is pretty awful. I think we have some sort of calibration issue, some sort of programming issue. Look at that. That's just It's just ridiculous. What's it doing? crazy.

**Dave Jones:** And we've got the heated build. We've got the proper heated build platform and the myar tape. And it just looks nothing like the orientation that's on the uh unit itself.

**Dave Jones:** Crazy. Oh, it's building a bait. It's probably building a It's building At least it's sticking now, right? It wasn't sticking before. Yeah. Well, that's looking good cuz it is sticking.

**Dave Jones:** So, I'm pretty happy with that. Although, if that's 0.3 mm on my monkeykey's uncle, it seems a bit more than that. Oh, see, it's lifting up. It's doing all sorts of weird and wacky stuff.

**Dave Jones:** It's like It's almost like it's putting out Yeah. nasty sounds. It's like it's putting out too much um stuff and not moving and not stepping high enough. So, I think we need to tweak some of those values.

**Dave Jones:** Hey, tada. A that's pathetic. I think we should probably That's our best bet though is to take that off and file it down better and tweak that. Yeah, I can see it go a bit slack there.

**Dave Jones:** I think the belt went a bit slack possibly. [Music] So, I think that's our I think we'll find that's probably our culprit in there. So, there's our second print and that is a complete and utter fail.

**Dave Jones:** It was supposed to be a Space Invader character, but uh nothing. But look, it built this what looks like that zigzag base there. It built that lovely, but then it sort of just ran into it itself and it did all sorts of weird stuff.

**Dave Jones:** So, we think it's actually slipping. The belt must be slipping somehow to give that. But why it gave that perfect zigzag pattern to start off with, uh, we're not sure.

**Dave Jones:** But I think we'll probably take off the X-axis and uh try and tweak it, I guess. All right. So, we've taken it back out there. We're taking the X platform, the build platform off, and we're going to try and file down uh these bits in here a little bit bigger cuz we think that's where it's uh getting caught up or something like that and maybe causing it to slip

**Dave Jones:** on the cogs. Maybe. Fingers crossed. No, scratch that. We think that this cog is possibly too high up cuz it's much higher than the cog in there, which you probably can't see, but uh due to the light.

**Dave Jones:** But yeah, we think maybe we'll try that first rather than go to the effort to file out uh that some more because really that's I it's going to have a hard time slipping when you've got a nice tooththed uh belt like that in a proper cog and it's all tightened up.

**Dave Jones:** So possibly the height of that uh might be doing something. So we'll try and lower that first. I think we're still squirting out too much, if that's the correct terminology.

**Dave Jones:** Extruding too much, squirting out too much. Never takes your fancy tape. Yeah. All right. But that's more promising though. Well, at least we've gotten further. Right. The bu the base is the base is a lot further and it's like and it is in the center whereas before it it was it was way off.

**Dave Jones:** It sort of did. Yeah. It started from here actually rather than it started over one side I think. Yeah. But it's not filling in that as a complete square.

**Dave Jones:** So, I'm not sure what's going on there. But this is good. This is very happy with this. Yeah, that seems to have made a made a big difference. Yeah, that's very promising.

**Dave Jones:** I like that. Oh yeah, that's smooth, fast, brilliant. I think that was our issue. Wow, that's all it was. Yeah, it's looking good. Here we go. Here we go.

**Dave Jones:** It's drawing our pack. It's drawing our Space Invader. Oh, brilliant. Oh, brilliant. Oh, now we're excited. Oh, yes. Perfect. Woohoo! [Music] winner. Now, I wish we printed something more exciting than a space invader.

**Dave Jones:** Anyway, we could print anything now. This is great. That's why That's why cuz it's already cooled and then it goes back in the other direction. So, it deliberately puts those ones like vertical and then starts drawing the thing horizontal.

**Dave Jones:** So, the base horizontal. I think that that's the reason. See, that's definitely looking like it's basic now. Yep. We get no slippage at all. That works perfectly. Actually, no.

**Dave Jones:** I think it's out. You reckon? Unless it's like a it like it's staggered. You see the layers there? Yeah, they're staggered. I think there's something wrong there potentially. Otherwise, or it's designed like that.

**Dave Jones:** Or is it? No. Does it look staggered? It's a flat object. I I think it's I think it's out. Either that or we have a calibration issue with like how much it extrudes and temperature and stuff like that we need to tweak but generally though pretty darn.

**Dave Jones:** Hey finished. Tada. There's our space invader. And there it is. That's our very first Makeabot print. It's a Space Invader. It doesn't seem that uh solid. There seems to be something about it almost as if maybe a calibration issue perhaps in in regards to uh setting the uh setting the uh temperature or the amount of product which is extruded cuz it the layers don't seem to uh line up.

**Dave Jones:** They seem a bit uh a bit staggered. So maybe we have some more belt slippage or something like that perhaps. There's some of the very fine weaves. Ra what is it?

**Dave Jones:** A raft. And yeah, I think we still got layer alignment issues. Yeah, it definitely looks like we got a Y build issue. Y is in this direction. X is across here like this.

**Dave Jones:** And if you see the edge of it is fine. These walls on the side here are perfectly aligned. And that indicates to me that there's no error in the X.

**Dave Jones:** There's no slip in the X axis motor, but the Y axis. This is why we can't see through the eyes of the well, I guess you could say the eyes of the Space Invader character there.

**Dave Jones:** And why these sides here are not smooth as they should be. They should be perfectly smooth. So that we think our motor is slipping somehow in this Y direction like that perhaps or there's something going on there.

**Dave Jones:** Okay, we're printing out the uh cylinder now to test our um uh test our XY uh capability. And I think we've got it. I think it was just our um belt uh tensionings that were slightly off.

**Dave Jones:** It seems to be fairly critical, but this cylinder is now looking very, very good. I love that sound when it draws a circle. It's brilliant. But this is really I think we've cracked it.

**Dave Jones:** I think we have an absolute winner here. And uh there's supposed to be no flat sides, Phil. No flat sides on the cylinder cuz that indicates a loose belt apparently.

**Dave Jones:** So I think we've cracked it and this will be our first real successful successful print. So now we just don't touch it, right? We don't breathe on it again or at least don't touch the belts.

**Dave Jones:** Um, there's that cool noise going around the and it's building up this thing and I'm pretty darn happy with that. So, we'll show you that when it's [Music] finished.

**Dave Jones:** And there is our first our very first our very first print. And it looks absolutely perfect. Woohoo. I've cracked it, Phil. That's a winner. That has winner written all over it.

**Dave Jones:** That is absolutely beautiful. There's no XY um stepper uh backlash or anything. We're getting no flat sides. So, I think we have absolutely flooked the uh tensioning on these belts because that's all it was really was the uh tensioning of the belts.

**Dave Jones:** And the uh cylinder test is a very good test to do to as a first print to show you that uh that you're getting no uh backlash or uh or overtightening or undertightening of your belts.

**Dave Jones:** Beautiful. Well, looks like we spoke too soon. Our cylinder was absolutely perfect. So, we tried to print our um Space Invader uh symbol again, and we got this silly stepped thing again.

**Dave Jones:** First one still looks like the best. So, it's Yeah, our first print. That's our first print actually looks better than this print we just did. And we didn't change any settings at all.

**Dave Jones:** Um our feed rate was still the same and all sorts of stuff. So really um that's all we can assume is that the it was much more of a jaggy motion.

**Dave Jones:** So all we can assume is that the really the jagged violent motion required to actually print this is actually offsetting um causing an offset in our y axis in this direction like this.

**Dave Jones:** Cuz once again, the X-axis is perfect cuz these walls, sidewalls here are perfectly well, you know, fine, as good as, you know, as good as you can expect. But uh and but the cylinder when that was printed, that was a um a very smooth motioned uh print.

**Dave Jones:** There was very silent, no um jerky motion or vibration of the machine at all. But printing this thing was very jerky and the thing jerks around and makes a lot of noise and does violent movements.

**Dave Jones:** So really there's something wrong there. Maybe we have to drop the uh the rate even further. And you can see the um what is it? The raft. Raft. Raft on the bottom.

**Dave Jones:** That uh is what they build upon. So, you'd have to uh cut that off or sand it off or slice it off or something to get your nice smooth surface on the bottom like you do on the top, but that it it actually prints that so it doesn't stick to the uh heated build platform.

**Dave Jones:** But there you go. Anyway, I think we've uh increase the speed. Crack that. I think that's probably what we'll try. Yeah, I think we'll Yeah, we'll try and decrease the speed.

**Dave Jones:** But yeah, I think uh we'll call it quits because that is technically a win. It's just that the machine works beauty. It's only a matter of just uh tweaking a few numbers and things like that.

**Dave Jones:** It will be sweet. So, we'll catch you next time.
