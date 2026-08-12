---
video_id: pHNpayYhBvM
title: EEVblog #264 - SMD PCB Pick & Place Machine Assembly
url: https://www.youtube.com/watch?v=pHNpayYhBvM
source: youtube-asr
timestamps: {"0": 0, "1": 31, "2": 69, "3": 91, "4": 114, "5": 135, "6": 177, "7": 227, "8": 261, "9": 279, "10": 311, "11": 329, "12": 363, "13": 394, "14": 412, "15": 449, "16": 485, "17": 509, "18": 534, "19": 570, "20": 600, "21": 620, "22": 642, "23": 666, "24": 703, "25": 731, "26": 752, "27": 790, "28": 817, "29": 837, "30": 870, "31": 892, "32": 915, "33": 947, "34": 982, "35": 1006, "36": 1029, "37": 1047, "38": 1066, "39": 1086, "40": 1101, "41": 1114, "42": 1125, "43": 1164, "44": 1196, "45": 1219, "46": 1244, "47": 1265, "48": 1280, "49": 1296, "50": 1311, "51": 1328, "52": 1353, "53": 1371, "54": 1392, "55": 1414, "56": 1430, "57": 1443, "58": 1458, "59": 1474, "60": 1513, "61": 1548, "62": 1573, "63": 1606, "64": 1627, "65": 1646, "66": 1661, "67": 1679, "68": 1708, "69": 1744, "70": 1775}
---

**Dave Jones:** Hi, I'm here at Ramsonic. I'm getting my PCBs assembled by Microcurrent panels that you saw in the design for manufacturing tutorial. So, I'll take you through step-by-step. The audio is not going to be that great. Sorry, it's pretty noisy here in a pick and place factory environment, but we'll see the steps and a few of the issues that goes into making a assembling a typical surface mount panel. Let's go. And as for the machines we've actually got here, this is an EK All right, this is

**Dave Jones:** our solder paste dispenser and you can see my solder paste stencil in there for my Microcurrent boards and that is a big squeegee that goes across and applies the solder paste and it's got its own control system up here, all software controlled. And over here we've got a Samsung board feeder and that you slide the board in here and it's conveyor belt system, it's all linked and that will automatically slide the board into the solder paste dispenser and we've got another Samsung board feeder here and that takes the

**Dave Jones:** output of the solder paste dispenser and feeds it into the pick and place machine which is a Samsung SM42 or 421, sorry, and it's got its own control system. We've finished our 20 boards there and we've got another Samsung board feeder.

**Dave Jones:** When it comes out of the pick and place machine, it goes into the reflow oven and the reflow oven is a Samsung, I'm not sure of the model number, but it's a Samsung and it's got the thermal temperature profile and fume extraction here of course because this is a soldering process.

**Dave Jones:** And this is quite a big beast. And then it comes out the end here, and that's it. That's the entire pick and place Well, that's a basic pick and place manufacturing line. They can get more extensive than that in terms of they can automatically go into visual ID inspection systems and things like that.

**Dave Jones:** But, this is basically what you will require to automate board assembly. And the first step is my panel goes into the solder paste automated solder paste dispenser, and it pops up. It lifts up. There's a hydraulic mechanism there, and there's my solder paste stencil down in there, and it will a squeegee comes across, and it will apply the solder paste. You can see it dripping down in there.

**Dave Jones:** There it is. It's come out. It's It's got the solder paste on it. All right. Let it rip.

**Dave Jones:** And it's now sucking the SO8 IC out of the tube there and placing it onto the board and you'll notice that the way it does that is that these tubes are bent upwards like this and they're and they actually are vibrated out of the tubes using this vibration feeder controller here and that's how they actually suck the devices out of the tubes. They just vibrate the tube and they slide down the tube and pop out the end and the pick and place nozzle is able to grab that.

**Dave Jones:** So there we go. We're doing our battery holder now. And you'll notice it placing the There's some sort of visual alignment device over there which lights up red and well our board is gone. It's finished before I had enough time to film it.

**Dave Jones:** It's done. It's popped out and it's over here. So we've got a problem here with the It's because this reel is actually re-reeled. Is that correct? And the tape and sticky and they just didn't We're getting no end of issues here because it's only a partial reel. So that's something to remember if you're getting these if you're getting your boards surface mount assembled those partial reels that you get from Digikey and places like that they they can be troublesome.

**Dave Jones:** You'll notice that one's the second board is going in there like that and the other one is just popped out here. So it's fully automated on this conveyor belt uh system here. It goes along and it'll automatically go into the reflow oven. So there's our assembled board and there it goes.

**Dave Jones:** Bang and that will go through various stages and it will preheat and do all sorts of things and it will have a thermal profile on it. And it's as you can see it's traveling fairly slow because it's got to go all the way through this massive machine here. It's quite long and it will have a thermal temperature profile set for this particular board. This one looks like it's got nine different zones and the temperature is set up for each one of those zones and you can see the board traveling

**Dave Jones:** through. I presume that little green uh symbol there is our little board and it's flowing through and there should it looks like there's another board still in the process there. So, you can actually see how many boards are in there. See them tracking and it should pop out the other end fully soldered. Magic. And we've just fed another one in there. You can see the green dot over here in and one's about to pop out the other end. So, let's go down and check it out. It's not terribly fast and

**Dave Jones:** you can see a little bit of warpage on there on the board. Perhaps that's probably due to the uh due to the panelization of the board, but there we go. It has popped out and it is magically soldered.

**Dave Jones:** Infrared reflow soldered. Not a problem. Ta-da! Beautiful. And that's our finished board. Let's take it off here. And it's reasonably hot. So, woo! Yeah, you don't want to hold on to that. You don't want to grab that with both hands. You might be in for a shock and the boards can actually stay hot for quite some time if you've got like a multi-layer board that's got internal ground planes and things like that. These boards can stay very warm cuz the copper inside, the heat gets trapped on the internal

**Dave Jones:** power planes and yeah, they can stay warm for quite some time, but there's our completed board. Beautiful. And you'll notice there that the solder Um, hasn't applied any paste to these uh large pads here. You can actually decide if you want uh the paste or not. We uh didn't add the paste to those cuz they're going to be uh hand soldered later, but uh that is the completed board, and it looks really nice. The joints look uh excellent as you'd expect for a reflow um board like this, and I don't see any

**Dave Jones:** tombstone uh components or anything missed or anything like that. Looks quite nice, and you notice that the uh switches aren't installed yet. They need to be hand assembled later. And there's another one. This is happening really quick. These are We're only talking, you know, a a few minutes between boards really. Just enough time for me to shoot that last clip, and uh this one has just popped out.

**Dave Jones:** Oh, yeah, hot. Hot, hot, hot. Woo! But, this is a very quick board. It's only taking a few minutes to fully assemble my microcurrent board cuz really there's not many uh parts on it. It is a fairly simplistic board, and this is uh quite a relatively uh you know, a mid-to-high-end range machine, and it is pretty darn quick.

**Dave Jones:** And as you can see, the number of uh feeders here, this can take uh 60 different feeders on each side. There's actually two sides to this machine, so we're only using like a dozen feeders here, but it can actually fit 60 along here. So, that's a a massive number of um uh components. And if we go around the backside of the machine around here, we'll find that it will take another 60 uh uh reels uh going along here as well.

**Dave Jones:** There we go. They're all numbered 1 through to 60, and it looks like they've got uh some ICs set up on a tray in there. Let's have a look at that. This is where the tray components go. In there, if you buy your components on trays, they just sit on this tray holder in there, and the pick-and-place machine is able to come down and suck those devices off. They aren't mine, so they're obviously still set up for another job, and there's a tray there for dodgy parts, excess parts that it

**Dave Jones:** couldn't place or something like that. It will actually dump them into there. And that black box you see in the middle there will actually light up red. That's a camera system that allows it to identify components when they're on the nozzle. So, this is a rear-side view of my microcurrent board being assembled.

**Dave Jones:** And it is relatively quick. It's a a very large XYZ Well, XY axis system that does travel very quickly indeed. Not as fast as some machines I've seen go. Maybe they're actually limiting the rate. Oh, and there's that visual alignment device down there.

**Dave Jones:** It decided it lit up red. It needed to come over here. And it's doing that for There we go. It's doing that for the CR23 CR 25 battery holder. And this board's almost done, I think. It's probably about shoot out.

**Dave Jones:** Yeah, two more sockets left two more battery holders left, and bang, there we go. Our board's You missed Didn't have the camera at the right angle, but that board just shot out, and it's starting And you can see my stainless steel stencil here. It's got the There it is, the microcurrent. This is This costs a couple hundred dollars. You can actually get cheaper ones, but really, if you're manufacturing a high-volume stainless steel is the thing that works and that's the that's based on your paste overlay file that's generated from your

**Dave Jones:** CAD system and you'll note that we haven't done the external connectors. It's just the you can see the large holes there are the battery holder and the small you can see the SO8 there plus a few passives and that's it'll only apply paste through those holes in this stainless steel uh stencil very durable so they can last for you know many many thousands or tens of thousands of boards or something like that but they will actually eventually wear out if you're you know if you're manufacturing

**Dave Jones:** millions of boards you might have to go through a a few solder paste stencils. Let's have a look at our solder paste stencil in here. This is inside the machine and you can see the squeegee there and some excess solder paste which is already already on there.

**Dave Jones:** And there it is there's my microcurrent panel rev 3 that got me I don't know who actually manufactured that the the assembler takes care of that they've got a a particular stencil manufacturer which they use so there's not a huge amount inside a solder paste stencil machine but it has got a hydraulic ram on the bottom which actually lifts the board up and actually presses the board against the stencil there but yeah it'll align the board with a fiducial camera and it will lift it up hydraulically and actually

**Dave Jones:** it'll compress the board against the solder paste stencil and then it will the squeegee will come across and just wipe the solder paste across the board and this is a lead-free board so this is lead-free solder paste. And there we go we just pressed a button and we dumped a whole bunch of uh solder paste onto that. And what do we do? We've just got it in it We put it back.

**Dave Jones:** You You can actually reuse this stuff. Yep. Yeah, two or three days fine. Two Two or three days worth and then Right, but but that's about the shelf life. Two or three days. Brand new paste. Mm, yum. And there we go. That's the solder paste that we're actually uh using. Comes from Chemtools.

**Dave Jones:** You'll see those chips actually sliding down the tube there. That was the uh That was the vibration feeder. Based on the angle of the uh the angle of the tube. And once again, we're really churning through these boards now. Uh they're uh going through at a rate of knots and it's placing our battery holder again. I love watching the battery holder cuz you can actually see the parts uh being assembled where little, you know, 0603 or little passive components, you can't actually see what it's actually

**Dave Jones:** doing there. Oh, there we go. This is actually a dual head machine. I thought it was doing it a bit quick. There you go. It's actually got uh two parts. I It's actually clearly got two nozzles and it can pick up two components at once. So, that's because a lot of your time will be wasted in your XY return.

**Dave Jones:** So, if you've got a uh dual nozzle head machine, then uh you can pick up both components at once and then you don't have to go and waste time doing that XY axis again. You can just start place those two components at almost the same We can't place them at the same time, but at least it doesn't have to return back to the position again.

**Dave Jones:** This uh machine, I stand corrected. It's got six nozzles. You may be able to see the multiple It's hard to get a shot in here. Sorry about that, but it does actually have six nozzles and it can actually pick up it's only picking up two of my uh Oh, there we go. It's only picking up two of my uh battery holder, but it's a capable of picking up uh six components at once. So, that's how it can really um churn out these boards. If you're picking up six passive components at one

**Dave Jones:** time and placing them, that's a real time advantage. And if you're curious to know how long a a full uh microcurrent panel takes, I just timed it and it was a smidgen under 1 minute and 40 seconds from when the board uh slid under the uh pick and place uh head until it uh spat it out the other side. So, that's uh pretty quick for assembling 10 boards like that. This mean build time for these uh boards is 119.4 seconds per board. Brilliant. And you'll notice it's going through the final

**Dave Jones:** stage of doing the doing the pick and place connector there and it's showing it's 99% complete for this board. There we go. Banged. And uh we start again. So, what we're doing is just we're counting how many left on that uh Yeah, because that's the last because It's the last reel. Now, it's the it it it's the end of the reel, is it? So, we have to be careful.

**Dave Jones:** Yeah, yeah. These machines always need tweaking. Rarely do they run continuously for like your uh or you'll get a a stuck feeder or something like that and you've always got to constantly attend these machines. There we go. We've just put a few more chips manually down into that tube down there.

**Dave Jones:** And just doing a few little tweaks. And that's our dead component tray. I'll do one for you.

**Dave Jones:** And there's our compa- there's our tray of No. Oh, they're they're one. Oh, only that one. So, So, we only lost the one component. pitch. Oh, okay. When you're pitching. All right. Oh, okay. Yeah, we lost a couple of uh lost a couple of battery holders, but yeah.

**Dave Jones:** Apart from that, why is that? Why would we lose them these suction cup these suction gauges? you need to pick up a couple of components Yep. to teach the machine how to do it. Right. Okay. Yeah. to see the pins of the component, to see the height of the component, the color of the components. When you That's why you need to pick up a couple.

**Dave Jones:** Right. Okay. So, yeah. a couple of components in the beginning, but once you Yep. teach it, it's finished. Next time when you do them It's And that's all saving software. How How long would it take you to set up this machine for this board here?

**Dave Jones:** It depends. For this one? For this board, a couple of hours maybe. A couple of hours? 6-7 hours. 6-7 hours? It takes a whole day, almost a whole day to set up. Wow. And And And this is a simple board, too.

**Dave Jones:** Yeah. Right. Yeah, when you get to a bigger board, um and that takes two or three days. Two or three days to set up a big board. Wow. But, you only have to do that once. Yeah. So, yeah.

**Dave Jones:** Mhm. So, you would document where you've placed these reels. It Would the software tell you where these reels need to go? So, when you load the job back up, it would Yep. Okay. And the uh excess waste on these battery holders is getting quite quite large, but we're still got a lot left on our reel there. Check out our reel. I think that was five uh No, uh Was it I don't know, on a reel or something like that? So, just tweaking the vibrator there, applying some percussive maintenance.

**Dave Jones:** That is the technical technical term of uh giving it a little bit of a bang there to get the chip down. And if you're interested to have a look inside one of these, there's the uh there's the worm drive for that side there, and so I can zoom in on the Let's zoom in on the stepper motor over here. Look at that huge worm shaft on that. And there's the actuator. Sorry, it's a bit dark in here. You may not actually be able to see it, but there's the six

**Dave Jones:** um uh suction nozzles, so you can see the actuators in the vacuum, and there's the uh trailing cable there. Here's another drive down in here. Another stepper motor with a huge drive rod. And uh that's why these things cost hundreds of thousands of dollars.

**Dave Jones:** And there we go. You can actually see the uh see the head there. That's the head itself with the six uh vacuum nozzles on it. And how many different nozzle heads would this machine have? which component Ah, which component. So, you would set up the nozzle heads in there based on Okay.

**Dave Jones:** Yep. There you go. That's a six That's a six-nozzle pick and place head. Very complicated bit of kit. And uh that's obviously the uh I believe that's the camera, possibly. Fiducial camera. That's the fiducial camera, yep. So, it aligns the fiducial marks on the board, and I'll show you those on my PCB.

**Dave Jones:** And there you go. There's the fiducial marks uh on my panel there. They're in that corner. Uh sorry, that one up there. And they're in three locations like that, so it knows how to align those align the boards. You'll program it in.

**Dave Jones:** Oh, look, we've got a uh we've got a bottleneck here. We've got a bottleneck. It's churning out these boards so fast, we don't know what to do. Wow, and I think we're done. I think we've done all our 20 panels.

**Dave Jones:** That's it. That's complete. And this didn't take long at all. I've only been here for like an an hour or something like that. And uh uh that's how long it took to assemble my 20 uh panels or my 200 microcurrent boards.

**Dave Jones:** And that includes uh fixing the uh problems with the machine and that sort of stuff and around with it. So, um that was pretty darn quick. And now it'll be on to um after some uh visual inspection, of course, it'll be on to some hand soldering for the uh switches.

**Dave Jones:** I've got uh two switches here. And we'll go on to the connectors, as well. And of course, to satisfy all the different jobs you need this many feeders. And of course, they cost a couple of thousand bucks a pop. So, they're uh very expensive things to actually have. And they'll come in different widths and different types for all the different uh components. There's some vibration feeders down in there.

**Dave Jones:** There they are. They've actually got the uh the uh vibration controller actually attached to them. And there's a uh tray over there for tray-based components. And you've got to have uh see, the reels are already in here for all various uh jobs that they've got in line, of course. So, these are all ready to go.

**Dave Jones:** And they've finished my boards. And uh they're ready to go on another job, I guess. Yeah, we've got all of that engine here to to to be able to assemble any different component on the market. Mhm. Even even new component on the market and new engineered component should be all be done here because we got all different tooling here for that.

**Dave Jones:** And you've got very wide ones here as well. Okay, that's all very big component. Yep. That could be for example a socket, simple small socket. So we do that for special customer in medical. Right. And we needed a wide one for ours because we have we needed a fairly wide feeder for the uh surface mount uh CR2032 battery holder here.

**Dave Jones:** That's the clever engineer. Remember the design. Because I designed on it. Yeah, exactly. Without thinking about uh what I really need, yeah. But I But some There are some machines who that may not have these small reels though.

**Dave Jones:** Uh yeah, yeah, all right. Also uh in in we have to modify the actually we have to modify the modify the machine to fit for special capacitors. It's sort of uh capacitor electrolytic capacitor, surface mount, very difficult to get.

**Dave Jones:** We have to modify the whole machine to handle the height of the capacitor because 2 mm isn't the standard. Right. We modify the machine for that. So how much did all these machines cost, Ramiz? Uh really if I start talking about them, I'm going to get high blood pressure again.

**Dave Jones:** High blood pressure, yeah. But you're talking about a lot of money here. About a half million bucks. at least The machine on its own about 100K, but every feeder about $2,000. $2,000 a feeder. At least, yeah. Okay. You get the machine a bit cheaper, but individually you pay a lot more.

**Dave Jones:** And here's my partial reel of my 1K 0.1% resistors there and it wasn't a full reel. I didn't buy it cuz these are, you know, they're they're not 0.01 cents each cuz they're a precision 0.1% resistor. So I bought them based on that re-reeling surface service. I actually uh purchased 210 of them. There they are and Digi-Key reeled those for me and unfortunately, these are real re-reeled components do actually cause an issue. So, just something to watch out for, but once we got the machine set up and tweaked and

**Dave Jones:** everything like that, it seemed to work fairly well and that's what a typical feeder mechanism looks like. And they've got a second machine over here, which is just a Samsung. It's a stand-alone one and it can be used as a secondary machine to do a second job if the main machine is fully occupied. And this one, they don't actually have the feeders to do like a 0402 and those smaller components. If they really want to do those, they're going to put it on the main assembly line here.

**Dave Jones:** Okay, what we're going to do is we're going to load another board here and we'll see that it should actually change the width of the conveyor belt system. There we go. It's changing the width of the board all the way out for a 300 mm height board there or 300 mm width board. So, you don't actually have to go in and manually change that.

**Dave Jones:** But these ones you have to actually change manually. You see now it's actually not actually aligned there, so that one will get tweaked manually and the oven the thermal oven there, we just up manually control the conveyor belt width like that to match that one out there. There you go. And there you can actually see the camera on the fiducial mark itself. That's actually a view from the from the camera on that particular board and uh setting the center position of the fiducial.

**Dave Jones:** And there we go. We're actually manually aligning the fiducial the moment there and set the center, bang. So, you program in the three fiducials. Doing a manual tweak again. And you'd only have to do this once, of course, to set up your boards.

**Dave Jones:** And this is how fast it's actually capable of of going. We've set it up for a dummy run here, and it's really it's really screaming along, and it's just actually pretending to pick up these components. So, it's it's really capable of phenomenal speed.

**Dave Jones:** And if you know that it's picking up six components at once, obviously it'd be a bit slower if it has to actually pick up the components, actually suck them up with the vacuum, and then place them down, but uh that's physically how fast it's this machine is capable of moving.

**Dave Jones:** And that speed is is really determined by the particular type of component you have. Like, if we've got our surface mount battery holder here, you can't just fly that across and pick it up at maximum speed and just fly it across the machine, cuz it'll just start fall off.

**Dave Jones:** The vacuum won't be able to hold it. So, that's all programmed in the software up here. When you actually program your board, you'll program in the not only the velocity of the pick up, the individual component pick up, like these 0603 caps and resistors. They'll be, you know, you can pick those up reasonably quickly and fly them across the board, but a high mass component like a a connector or this battery holder, or say leads or something like that.

**Dave Jones:** Leads have to be picked up very delicately, cuz you don't want to damage them. So, really, that's all totally dependent upon each component, and each board, and each job. And you'll see here that the tape is actually pulled back. These are how these feeders actually work. So, only the last component there is actually exposed to the pick and place machine. But, the So, they peel back all of the all of the tape here for these particular ones and the last components down in there exposed so the machine can actually pick

**Dave Jones:** and place head can get in there and pick them up and place them. And when you finish with it with this type of battery holder here with this type of reel you're you're losing one component. So, there'll be one that battery holder we saw in there, bingo, it's wasted. And with these smaller components over here you're going to waste six of them with the peeling the tape back. So, if they're very expensive components, well, you're going to waste some of them and that's what you have to factor in when

**Dave Jones:** you get these machines when you get your board machine assembled as opposed to hand assembled.
