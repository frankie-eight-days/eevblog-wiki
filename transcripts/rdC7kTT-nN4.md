---
video_id: rdC7kTT-nN4
title: EEVblog #257 - Makerbot Troubleshooting
url: https://www.youtube.com/watch?v=rdC7kTT-nN4
source: youtube-asr
---

**Dave Jones:** Hi, this is Phil. Phil's got a PhD in laser physics and he's a patent attorney, which means he's on the dark side of the force, but he's decided to come to the good side of the force and become the new EE blog apprentice. So,

**Dave Jones:** he's trying to he's got to learn the correct tongue angle. So, going to teach him that. And uh uh hand us the uh the left-handed screwdriver there, Phil. Yep. It's a right-handed one. Man, come on. You got to learn. Let's get this

**Dave Jones:** wrong. Noobs. I don't know. He's got a lot to learn. Anyway, we're going to uh calibrate our Makerbot here and uh print something. Let's go. And here's our finished Makeabot thingamatic. And it's serial number 68 7. There it is. And it looks rather

**Dave Jones:** neat. You've uh seen these before. or it it doesn't light up like some of the other uh ones do. They've obviously installed some um uh lighting inside. Mine doesn't have that. The power supply was really dodgy um to install that, but

**Dave Jones:** uh it's apparently the type supplied with this one. And I've got a the new uh Mark 7 step extruder inside there. And that's the Z axis platform. I haven't cable tied down any of the wires yet. So, all the wiring is uh is all loose in

**Dave Jones:** there because I want to um figure out what the maximum range of the platforms is before I actually do that. But that is a Makeabot thingamatic. It's ready to go. So, we'll uh plug it in, we'll calibrate it, and we'll give it a burl.

**Dave Jones:** And our first print. Wonder what we'll print. H. Now, here's one thing I don't really understand. And they've got these really nice um uh bearings on here that the shafts slide into. But this one on this side doesn't have the bearings on

**Dave Jones:** either side. And there's a bit of play in there. I'm not sure if you can actually see that, but I can actually wiggle that up and down. And I'm not sure why. Um there's no bearings in there. They didn't supply

**Dave Jones:** them and they didn't tell me to actually put them in. Strange. But anyway, that's the uh Y axis platform. There we've got the X-axis platform on top here. That one does have the bearings on either side, and it feels reasonably smooth.

**Dave Jones:** Um, and as you can see, the wiring inside these things is is really just um is just hanging there basically. Um, so it is a bit messy on the inside. And on the top side here is our Z platform

**Dave Jones:** which is this motor here with this worm screw drive there. And that moves this entire platform on the top here. And if we get down and we take a look at the underside of it there, you can see it

**Dave Jones:** see the entire Z axis platform move. And it's got the uh step extruder on there where your uh your filament goes in the top here. It all heats up. Um, it's got a a heater. It's got a heater in there,

**Dave Jones:** a ceramic heater, plus a thermal uh overload and a thermouple as well. There's a safety cutout PCB over here uh which is designed to cut it out if it uh goes over temperature. And that's about uh all there is to the um XY mechanical

**Dave Jones:** platform. It's fairly simple, but the build itself uh is is fairly complicated. It took probably 14 15 hours for the two of us to actually fully assemble this thing. All right, we got our Makeabot switched on and connected to USB and we've updated the

**Dave Jones:** uh firmware. So, we're going to and disconnect. I'm going to reconnect down here and we're using the Replicator G uh program and connect to the unit. And we're connected. We've updated the uh firmware. We've gone through the process

**Dave Jones:** and uh we're going to do the calibration. So, what we do is we go up to file up here and scripts calibration and we run the thingomatic calibration G-code and then we hit the build button. So, the script

**Dave Jones:** is in there. We hit build and now it's telling us move the build platform until the nozzle lies in the center and then turn the threaded rod until the nozzle just touches the surface without pressing onto it. Okay. So, we want

**Dave Jones:** to change that. We want to put it directly in the center there. So, we want to put it the nozzle just a smidgen off the surface. Is that just off? That's just off. Just off. Half a bee's dick off the surface

**Dave Jones:** there. And that looks like it's in the center. Near enough. I'm not sure if you have to do this calibration routine um every time because I'm not sure that the machine knows where the absolute position of those sensors is. Tongue angle fill. All

**Dave Jones:** right. So, what we're going to do is we'll hit yes. And here we go. Woohoo. There it goes.

**Dave Jones:** And it should hit the top micro switch in there, the limit switch. And bang. And this thing. And the build platform is now centering itself. Back to that position. The micro switched on there for the X and the Y.

**Dave Jones:** So our three limit switches clearly work. X, Y, and Z limit switches. And we're done. That's the calibration. Simple. Okay. So, now we're set in the we're in the control panel uh software and we're going to test the tool head

**Dave Jones:** temperature and the heated build platform temperature. So, it tells us to type in a target temperature of uh 225°C for the tool head. So, we've done that and pressed enter. And as you can see, it's ramped up there. That's our

**Dave Jones:** target temperature. In blue there and red, you can see the temperature is actually ramping up. And it says to do 120°. Is that right, Phil? 120 for the build platform. So, we type that in, press enter. Our target

**Dave Jones:** temperature has jumped up there in yellow. And we'll see the white line there, the build platform current temperature ramping up. So, both those will eventually ramp up to their set temperatures. And they should they should remain there. They shouldn't uh

**Dave Jones:** overshoot or anything like that. So, this could take a few minutes. And the tool head is uh didn't overshoot. It's maintained. It's ramped up and then maintained the set temperature. The build platform's not quite there yet, but it's on its way. Okay. Our tool head

**Dave Jones:** has reached temperature and now it's telling us to stick the filament into the chosen red cuz red goes faster. Stick it in. And then what, Phil? Well, it seems that we've got a problem. No matter how hard we push in here, no

**Dave Jones:** matter how many times we actuate the motor and uh try and get the filament to grab in there, it's just just not working. So, I don't know. Plan B. Well, we tried this fluuro green one and we did get it to grab. So, we're supposed

**Dave Jones:** to see a thin bead come out of the bottom. We still up to temperature 225. Oh, yep. There we go. Got it. Woohoo. There we go. Switch it off. Press stop. Awesome. There you go. We got a hanger. And look at that. There we go.

**Dave Jones:** That Well, that's technically that's the first thing we [Laughter] printed. Bit of hot snot. Hey. Yeah. Floss. Floss. Beautiful. Works a treat. Agreed. Okay, we're ready to print something. We've loaded in Yoda's lightsaber. Very cool. We've put it vertically. We've centered

**Dave Jones:** it on the platform and flipped it. What do we do now, Phil? Generate G-code. All right. I assume it knows that. Well, it fits within that area. I'm assuming we're going to have enough uh stuff filament and generate

**Dave Jones:** G-code. You have made changes to this model. Any unsaved changes? Ah, no. There we go. Python interpreter. Would you like to visit? Ah, fail. Come on. one. Okay, we've installed the stupid Python interpreter. And I've scaled that down really tiny. We want this thing to

**Dave Jones:** print. I have no idea if this is a good first example, but let's generate the G-code. Save the model. Nope. There we go. It's doing something. Now, what do we do? Oh, how do we set up our Oh, use raft. Okay. Yep. Yeah. Use

**Dave Jones:** prinomatic. Got it. Step layer height.3 mm. The perimeter thicker. Well, default to one. Yep. Feed rate 30 mm/s. Okay. And we're using a 1.75 mm ABS mark. Yep. 7, I'm assuming. Ah, that's the different material. Okay. Well, we're definitely using ABS. We're

**Dave Jones:** not using PLA. So, what is this? Plastic material type ABS. Filament diameter 1.8. I think it is. Yep. I don't know. We'd have to actually get the calipers out and measure that. Between 75 and 1.8. Okay, that'll do. Extruder nozzle

**Dave Jones:** diameter. No idea. 4. Yep. Okay. Done. Do we generate geocodes? Not automatically generate when building. Go. Phil says go. Go. We're going. We're generating. We're almost there for the total number of layers for the inset. The inset procedure. Now we got

**Dave Jones:** to do the fill procedure. How many procedures are there? More than you can poke a stick at. You can see the different processes that goes through. carve process, uh, preface, inset, fill, speed, temperature, and raft procedure. But it's still going. Not done yet. Man,

**Dave Jones:** it's taking all day. And we there were like another there were comb cool procedure, reversal procedure, and it's done. Woohoo. It's printing now. It's moving. It's doing something that the it's given us an estimated build time on the software of

**Dave Jones:** what is it? 1 hour and 28 minutes. A man, we're hoping to do this before Jim. Oh well, have to head home and come back later and uh see if it's finally built. Do I dare leave this thing on its own or

**Dave Jones:** will it replicate and start Skynet? Uh-oh. Something's gone wrong here. It's hitting the end over here and there's no end stop. It just won't go any further. And uh Oh, no. It's Well, yeah, it's printing. It's printing, but it

**Dave Jones:** certainly didn't uh didn't do it in the center. No, no, it's No, didn't center on the pad. Why not? We went through the calibration procedure. No, our first print is a failure. and it uh doesn't stick to the

**Dave Jones:** aluminum surface. If you actually have a look down in there, we probably should have put that myar sheet on, but it's it's all just curled up. So, our that's our first print. It's a Oh, it's a nice pattern though. I rather

**Dave Jones:** like it. But there you go. First print fail. All right. So, what we've done now is we've made the current position zero in the control panel. So, we've moved it so it's in the center. And we've done that and we've we're building again.

**Dave Jones:** But, uh maybe we should put down some myar tape. But, uh why is it going back up to start? Well, there you go. Okay, we're at least getting somewhere now. We haven't figured out how to um center it

**Dave Jones:** properly on the pad yet, but um we managed to stick on some myar very quickly before we started this print job. I think it's probably laying down some sort of base maybe cuz that doesn't look like our object.

**Dave Jones:** So, not sure what it's doing there, but it seems to it's almost like printing out too much. No, that's doing a small amount. There we go. Okay, so it is controlling the amount of And now it's decided that it needs to

**Dave Jones:** do another print on the other side. What What's going on here? Wow. I no idea what it's doing. It's almost as if it's printing it down sideways.

**Dave Jones:** sideways, you know. Oh, fail. Look at that. It's just picked up the whole lot of it and dragged it across. This is pretty awful. I think we have some sort of calibration issue, some sort of programming issue. Look at that. That's just It's

**Dave Jones:** just ridiculous. What's it doing? crazy. And we've got the heated build. We've got the proper heated build platform and the myar tape. And it just looks nothing like the orientation that's on the uh unit itself. Crazy. Oh, it's building a bait. It's probably

**Dave Jones:** building a It's building At least it's sticking now, right? It wasn't sticking before. Yeah. Well, that's looking good cuz it is sticking. So, I'm pretty happy with that. Although, if that's 0.3 mm on my monkeykey's uncle, it seems a bit more

**Dave Jones:** than that. Oh, see, it's lifting up. It's doing all sorts of weird and wacky stuff. It's like It's almost like it's putting out Yeah. nasty sounds. It's like it's putting out too much um stuff and not moving and not

**Dave Jones:** stepping high enough. So, I think we need to tweak some of those values. Hey, tada. A that's pathetic. I think we should probably That's our best bet though is to take that off and file it down better and tweak

**Dave Jones:** that. Yeah, I can see it go a bit slack there. I think the belt went a bit slack possibly. [Music] So, I think that's our I think we'll find that's probably our culprit in there. So, there's our second

**Dave Jones:** print and that is a complete and utter fail. It was supposed to be a Space Invader character, but uh nothing. But look, it built this what looks like that zigzag base there. It built that lovely, but then it sort of just ran into it

**Dave Jones:** itself and it did all sorts of weird stuff. So, we think it's actually slipping. The belt must be slipping somehow to give that. But why it gave that perfect zigzag pattern to start off with, uh, we're not sure. But I think

**Dave Jones:** we'll probably take off the X-axis and uh try and tweak it, I guess. All right. So, we've taken it back out there. We're taking the X platform, the build platform off, and we're going to try and file down uh these bits in here a little

**Dave Jones:** bit bigger cuz we think that's where it's uh getting caught up or something like that and maybe causing it to slip on the cogs. Maybe. Fingers crossed. No, scratch that. We think that this cog is possibly too high up cuz it's much

**Dave Jones:** higher than the cog in there, which you probably can't see, but uh due to the light. But yeah, we think maybe we'll try that first rather than go to the effort to file out uh that some more because

**Dave Jones:** really that's I it's going to have a hard time slipping when you've got a nice tooththed uh belt like that in a proper cog and it's all tightened up. So possibly the height of that uh might be doing something. So we'll try and lower

**Dave Jones:** that first. I think we're still squirting out too much, if that's the correct terminology. Extruding too much, squirting out too much. Never takes your fancy tape. Yeah. All right. But that's more promising though. Well, at least we've gotten further.

**Dave Jones:** Right. The bu the base is the base is a lot further and it's like and it is in the center whereas before it it was it was way off. It sort of did. Yeah. It started from here actually rather than

**Dave Jones:** it started over one side I think. Yeah. But it's not filling in that as a complete square. So, I'm not sure what's going on there. But this is good. This is very happy with this. Yeah, that seems to have made a

**Dave Jones:** made a big difference. Yeah, that's very promising. I like that. Oh yeah, that's smooth, fast, brilliant. I think that was our issue. Wow, that's all it was. Yeah, it's looking good. Here we go. Here we go. It's drawing our pack. It's drawing

**Dave Jones:** our Space Invader. Oh, brilliant. Oh, brilliant. Oh, now we're excited. Oh, yes. Perfect. Woohoo! [Music] winner. Now, I wish we printed something more exciting than a space invader. Anyway, we could print anything now. This is great. That's why That's why cuz

**Dave Jones:** it's already cooled and then it goes back in the other direction. So, it deliberately puts those ones like vertical and then starts drawing the thing horizontal. So, the base horizontal. I think that that's the reason. See, that's definitely looking

**Dave Jones:** like it's basic now. Yep. We get no slippage at all. That works perfectly. Actually, no. I think it's out. You reckon? Unless it's like a it like it's staggered. You see the layers there? Yeah, they're staggered. I think

**Dave Jones:** there's something wrong there potentially. Otherwise, or it's designed like that. Or is it? No. Does it look staggered? It's a flat object. I I think it's I think it's out. Either that or we have a calibration issue with like how much it extrudes and

**Dave Jones:** temperature and stuff like that we need to tweak but generally though pretty darn. Hey finished. Tada. There's our space invader. And there it is. That's our very first Makeabot print. It's a Space Invader. It doesn't seem that uh solid.

**Dave Jones:** There seems to be something about it almost as if maybe a calibration issue perhaps in in regards to uh setting the uh setting the uh temperature or the amount of product which is extruded cuz it the layers don't seem

**Dave Jones:** to uh line up. They seem a bit uh a bit staggered. So maybe we have some more belt slippage or something like that perhaps. There's some of the very fine weaves. Ra what is it? A raft. And yeah,

**Dave Jones:** I think we still got layer alignment issues. Yeah, it definitely looks like we got a Y build issue. Y is in this direction. X is across here like this. And if you see the edge of it is fine.

**Dave Jones:** These walls on the side here are perfectly aligned. And that indicates to me that there's no error in the X. There's no slip in the X axis motor, but the Y axis. This is why we can't see through the eyes of the well, I guess

**Dave Jones:** you could say the eyes of the Space Invader character there. And why these sides here are not smooth as they should be. They should be perfectly smooth. So that we think our motor is slipping somehow in this Y direction like that

**Dave Jones:** perhaps or there's something going on there. Okay, we're printing out the uh cylinder now to test our um uh test our XY uh capability. And I think we've got it. I think it was just our um belt uh

**Dave Jones:** tensionings that were slightly off. It seems to be fairly critical, but this cylinder is now looking very, very good. I love that sound when it draws a circle. It's brilliant. But this is really I think we've cracked it. I think

**Dave Jones:** we have an absolute winner here. And uh there's supposed to be no flat sides, Phil. No flat sides on the cylinder cuz that indicates a loose belt apparently. So I think we've cracked it and this will be our

**Dave Jones:** first real successful successful print. So now we just don't touch it, right? We don't breathe on it again or at least don't touch the belts.

**Dave Jones:** Um, there's that cool noise going around the and it's building up this thing and I'm pretty darn happy with that. So, we'll show you that when it's [Music] finished. And there is our first our very first our very first print. And it

**Dave Jones:** looks absolutely perfect. Woohoo. I've cracked it, Phil. That's a winner. That has winner written all over it. That is absolutely beautiful. There's no XY um stepper uh backlash or anything. We're getting no flat sides. So, I think we have

**Dave Jones:** absolutely flooked the uh tensioning on these belts because that's all it was really was the uh tensioning of the belts. And the uh cylinder test is a very good test to do to as a first print to show you that uh that you're getting

**Dave Jones:** no uh backlash or uh or overtightening or undertightening of your belts. Beautiful. Well, looks like we spoke too soon. Our cylinder was absolutely perfect. So, we tried to print our um Space Invader uh symbol again, and we got this silly stepped thing again.

**Dave Jones:** First one still looks like the best. So, it's Yeah, our first print. That's our first print actually looks better than this print we just did. And we didn't change any settings at all. Um our feed rate was still the

**Dave Jones:** same and all sorts of stuff. So really um that's all we can assume is that the it was much more of a jaggy motion. So all we can assume is that the really the jagged violent motion required to

**Dave Jones:** actually print this is actually offsetting um causing an offset in our y axis in this direction like this. Cuz once again, the X-axis is perfect cuz these walls, sidewalls here are perfectly well, you know, fine, as good as, you know, as good as you can expect.

**Dave Jones:** But uh and but the cylinder when that was printed, that was a um a very smooth motioned uh print. There was very silent, no um jerky motion or vibration of the machine at all. But printing this thing was very jerky and the thing jerks

**Dave Jones:** around and makes a lot of noise and does violent movements. So really there's something wrong there. Maybe we have to drop the uh the rate even further. And you can see the um what is it? The raft. Raft. Raft on the bottom. That uh is

**Dave Jones:** what they build upon. So, you'd have to uh cut that off or sand it off or slice it off or something to get your nice smooth surface on the bottom like you do on the top, but that it it actually

**Dave Jones:** prints that so it doesn't stick to the uh heated build platform. But there you go. Anyway, I think we've uh increase the speed. Crack that. I think that's probably what we'll try. Yeah, I think we'll Yeah, we'll try and decrease the

**Dave Jones:** speed. But yeah, I think uh we'll call it quits because that is technically a win. It's just that the machine works beauty. It's only a matter of just uh tweaking a few numbers and things like that. It will be sweet. So, we'll catch

**Dave Jones:** you next time.
