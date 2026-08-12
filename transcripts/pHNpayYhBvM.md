---
video_id: pHNpayYhBvM
title: EEVblog #264 - SMD PCB Pick & Place Machine Assembly
url: https://www.youtube.com/watch?v=pHNpayYhBvM
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 31, "3": 47, "4": 67, "5": 87, "6": 103, "7": 122, "8": 137, "9": 158, "10": 177, "11": 227, "12": 243, "13": 257, "14": 276, "15": 293, "16": 307, "17": 322, "18": 337, "19": 353, "20": 369, "21": 384, "22": 397, "23": 420, "24": 436, "25": 451, "26": 468, "27": 485, "28": 500, "29": 515, "30": 532, "31": 549, "32": 570, "33": 585, "34": 597, "35": 611, "36": 630, "37": 649, "38": 666, "39": 680, "40": 694, "41": 713, "42": 728, "43": 741, "44": 761, "45": 776, "46": 795, "47": 811, "48": 825, "49": 840, "50": 857, "51": 873, "52": 887, "53": 900, "54": 912, "55": 927, "56": 943, "57": 959, "58": 974, "59": 992, "60": 1005, "61": 1022, "62": 1040, "63": 1057, "64": 1072, "65": 1086, "66": 1100, "67": 1112, "68": 1123, "69": 1141, "70": 1158, "71": 1175, "72": 1192, "73": 1210, "74": 1227, "75": 1247, "76": 1265, "77": 1280, "78": 1295, "79": 1311, "80": 1325, "81": 1339, "82": 1354, "83": 1369, "84": 1383, "85": 1394, "86": 1410, "87": 1427, "88": 1439, "89": 1453, "90": 1464, "91": 1482, "92": 1500, "93": 1518, "94": 1534, "95": 1549, "96": 1568, "97": 1583, "98": 1599, "99": 1620, "100": 1635, "101": 1652, "102": 1667, "103": 1682, "104": 1697, "105": 1710, "106": 1727, "107": 1744, "108": 1758, "109": 1773}
---

**Dave Jones:** Hi, I'm here at Ramsonic. I'm getting my PCBs assembled by Microcurrent panels that you saw in the design for manufacturing tutorial. So, I'll take you through step-by-step. The audio is not going to be that great. Sorry, it's pretty noisy here in a pick and place

**Dave Jones:** factory environment, but we'll see the steps and a few of the issues that goes into making a assembling a typical surface mount panel. Let's go. And as for the machines we've actually got here, this is an EK All right, this is

**Dave Jones:** our solder paste dispenser and you can see my solder paste stencil in there for my Microcurrent boards and that is a big squeegee that goes across and applies the solder paste and it's got its own control system up here, all software

**Dave Jones:** controlled. And over here we've got a Samsung board feeder and that you slide the board in here and it's conveyor belt system, it's all linked and that will automatically slide the board into the solder paste dispenser and we've got another Samsung

**Dave Jones:** board feeder here and that takes the output of the solder paste dispenser and feeds it into the pick and place machine which is a Samsung SM42 or 421, sorry, and it's got its own control system. We've finished our 20

**Dave Jones:** boards there and we've got another Samsung board feeder. When it comes out of the pick and place machine, it goes into the reflow oven and the reflow oven is a Samsung, I'm not sure of the model number, but it's a

**Dave Jones:** Samsung and it's got the thermal temperature profile and fume extraction here of course because this is a soldering process. And this is quite a big beast. And then it comes out the end here, and that's it. That's the entire

**Dave Jones:** pick and place Well, that's a basic pick and place manufacturing line. They can get more extensive than that in terms of they can automatically go into visual ID inspection systems and things like that. But, this is basically what you will

**Dave Jones:** require to automate board assembly. And the first step is my panel goes into the solder paste automated solder paste dispenser, and it pops up. It lifts up. There's a hydraulic mechanism there, and there's my solder paste stencil down in there, and it

**Dave Jones:** will a squeegee comes across, and it will apply the solder paste. You can see it dripping down in there.

**Dave Jones:** There it is. It's come out. It's It's got the solder paste on it. All right. Let it rip.

**Dave Jones:** And it's now sucking the SO8 IC out of the tube there and placing it onto the board and you'll notice that the way it does that is that these tubes are bent upwards like this and they're and they actually

**Dave Jones:** are vibrated out of the tubes using this vibration feeder controller here and that's how they actually suck the devices out of the tubes. They just vibrate the tube and they slide down the tube and pop out the end and the pick

**Dave Jones:** and place nozzle is able to grab that. So there we go. We're doing our battery holder now. And you'll notice it placing the There's some sort of visual alignment device over there which lights up red and well our board is gone. It's

**Dave Jones:** finished before I had enough time to film it. It's done. It's popped out and it's over here. So we've got a problem here with the It's because this reel is actually re-reeled. Is that correct? And the tape and sticky and they just

**Dave Jones:** didn't We're getting no end of issues here because it's only a partial reel. So that's something to remember if you're getting these if you're getting your boards surface mount assembled those partial reels that you get from Digikey and places like

**Dave Jones:** that they they can be troublesome. You'll notice that one's the second board is going in there like that and the other one is just popped out here. So it's fully automated on this conveyor belt uh system here. It goes along and

**Dave Jones:** it'll automatically go into the reflow oven. So there's our assembled board and there it goes. Bang and that will go through various stages and it will preheat and do all sorts of things and it will have a thermal

**Dave Jones:** profile on it. And it's as you can see it's traveling fairly slow because it's got to go all the way through this massive machine here. It's quite long and it will have a thermal temperature profile set for this

**Dave Jones:** particular board. This one looks like it's got nine different zones and the temperature is set up for each one of those zones and you can see the board traveling through. I presume that little green uh symbol there is our little board and

**Dave Jones:** it's flowing through and there should it looks like there's another board still in the process there. So, you can actually see how many boards are in there. See them tracking and it should pop out the other end fully soldered. Magic. And we've just

**Dave Jones:** fed another one in there. You can see the green dot over here in and one's about to pop out the other end. So, let's go down and check it out. It's not terribly fast and you can see a little bit of warpage

**Dave Jones:** on there on the board. Perhaps that's probably due to the uh due to the panelization of the board, but there we go. It has popped out and it is magically soldered. Infrared reflow soldered. Not a problem. Ta-da! Beautiful. And that's our finished

**Dave Jones:** board. Let's take it off here. And it's reasonably hot. So, woo! Yeah, you don't want to hold on to that. You don't want to grab that with both hands. You might be in for a shock and the boards can actually

**Dave Jones:** stay hot for quite some time if you've got like a multi-layer board that's got internal ground planes and things like that. These boards can stay very warm cuz the copper inside, the heat gets trapped on the internal power planes and

**Dave Jones:** yeah, they can stay warm for quite some time, but there's our completed board. Beautiful. And you'll notice there that the solder Um, hasn't applied any paste to these uh large pads here. You can actually decide if you want uh the paste or not. We uh

**Dave Jones:** didn't add the paste to those cuz they're going to be uh hand soldered later, but uh that is the completed board, and it looks really nice. The joints look uh excellent as you'd expect for a reflow um board like this, and I don't see any

**Dave Jones:** tombstone uh components or anything missed or anything like that. Looks quite nice, and you notice that the uh switches aren't installed yet. They need to be hand assembled later. And there's another one. This is happening really quick. These are We're

**Dave Jones:** only talking, you know, a a few minutes between boards really. Just enough time for me to shoot that last clip, and uh this one has just popped out. Oh, yeah, hot. Hot, hot, hot. Woo! But, this is a very quick board.

**Dave Jones:** It's only taking a few minutes to fully assemble my microcurrent board cuz really there's not many uh parts on it. It is a fairly simplistic board, and this is uh quite a relatively uh you know, a mid-to-high-end range machine, and it is

**Dave Jones:** pretty darn quick. And as you can see, the number of uh feeders here, this can take uh 60 different feeders on each side. There's actually two sides to this machine, so we're only using like a dozen feeders here, but it can actually fit 60 along

**Dave Jones:** here. So, that's a a massive number of um uh components. And if we go around the backside of the machine around here, we'll find that it will take another 60 uh uh reels uh going along here as well.

**Dave Jones:** There we go. They're all numbered 1 through to 60, and it looks like they've got uh some ICs set up on a tray in there. Let's have a look at that. This is where the tray components go. In there, if you buy your components on

**Dave Jones:** trays, they just sit on this tray holder in there, and the pick-and-place machine is able to come down and suck those devices off. They aren't mine, so they're obviously still set up for another job, and there's a tray there

**Dave Jones:** for dodgy parts, excess parts that it couldn't place or something like that. It will actually dump them into there. And that black box you see in the middle there will actually light up red. That's a camera system that

**Dave Jones:** allows it to identify components when they're on the nozzle. So, this is a rear-side view of my microcurrent board being assembled. And it is relatively quick. It's a a very large XYZ Well, XY axis system that does travel

**Dave Jones:** very quickly indeed. Not as fast as some machines I've seen go. Maybe they're actually limiting the rate. Oh, and there's that visual alignment device down there. It decided it lit up red. It needed to come over here. And it's doing that for There we go.

**Dave Jones:** It's doing that for the CR23 CR 25 battery holder. And this board's almost done, I think. It's probably about shoot out.

**Dave Jones:** Yeah, two more sockets left two more battery holders left, and bang, there we go. Our board's You missed Didn't have the camera at the right angle, but that board just shot out, and it's starting And you can see my stainless steel

**Dave Jones:** stencil here. It's got the There it is, the microcurrent. This is This costs a couple hundred dollars. You can actually get cheaper ones, but really, if you're manufacturing a high-volume stainless steel is the thing that works and that's

**Dave Jones:** the that's based on your paste overlay file that's generated from your CAD system and you'll note that we haven't done the external connectors. It's just the you can see the large holes there are the battery holder and the small you can see the SO8 there plus

**Dave Jones:** a few passives and that's it'll only apply paste through those holes in this stainless steel uh stencil very durable so they can last for you know many many thousands or tens of thousands of boards or something like that but they will

**Dave Jones:** actually eventually wear out if you're you know if you're manufacturing millions of boards you might have to go through a a few solder paste stencils. Let's have a look at our solder paste stencil in here. This is inside the

**Dave Jones:** machine and you can see the squeegee there and some excess solder paste which is already already on there. And there it is there's my microcurrent panel rev 3 that got me I don't know who actually manufactured that the

**Dave Jones:** the assembler takes care of that they've got a a particular stencil manufacturer which they use so there's not a huge amount inside a solder paste stencil machine but it has got a hydraulic ram on the bottom which actually lifts

**Dave Jones:** the board up and actually presses the board against the stencil there but yeah it'll align the board with a fiducial camera and it will lift it up hydraulically and actually it'll compress the board against the solder paste stencil and then it will

**Dave Jones:** the squeegee will come across and just wipe the solder paste across the board and this is a lead-free board so this is lead-free solder paste. And there we go we just pressed a button and we dumped a whole bunch of uh

**Dave Jones:** solder paste onto that. And what do we do? We've just got it in it We put it back. You You can actually reuse this stuff. Yep. Yeah, two or three days fine. Two Two or three days worth and then

**Dave Jones:** Right, but but that's about the shelf life. Two or three days. Brand new paste. Mm, yum. And there we go. That's the solder paste that we're actually uh using. Comes from Chemtools. You'll see those chips actually sliding down the

**Dave Jones:** tube there. That was the uh That was the vibration feeder. Based on the angle of the uh the angle of the tube. And once again, we're really churning through these boards now. Uh they're uh going through at a rate of knots and

**Dave Jones:** it's placing our battery holder again. I love watching the battery holder cuz you can actually see the parts uh being assembled where little, you know, 0603 or little passive components, you can't actually see what it's actually doing there.

**Dave Jones:** Oh, there we go. This is actually a dual head machine. I thought it was doing it a bit quick. There you go. It's actually got uh two parts. I It's actually clearly got two nozzles and it can pick up two components at

**Dave Jones:** once. So, that's because a lot of your time will be wasted in your XY return. So, if you've got a uh dual nozzle head machine, then uh you can pick up both components at once and then you don't

**Dave Jones:** have to go and waste time doing that XY axis again. You can just start place those two components at almost the same We can't place them at the same time, but at least it doesn't have to return back

**Dave Jones:** to the position again. This uh machine, I stand corrected. It's got six nozzles. You may be able to see the multiple It's hard to get a shot in here. Sorry about that, but it does actually have six nozzles and it can actually pick up

**Dave Jones:** it's only picking up two of my uh Oh, there we go. It's only picking up two of my uh battery holder, but it's a capable of picking up uh six components at once. So, that's how it can really um

**Dave Jones:** churn out these boards. If you're picking up six passive components at one time and placing them, that's a real time advantage. And if you're curious to know how long a a full uh microcurrent panel takes, I just timed it and it was a smidgen under

**Dave Jones:** 1 minute and 40 seconds from when the board uh slid under the uh pick and place uh head until it uh spat it out the other side. So, that's uh pretty quick for assembling 10 boards like that. This mean build time for

**Dave Jones:** these uh boards is 119.4 seconds per board. Brilliant. And you'll notice it's going through the final stage of doing the doing the pick and place connector there and it's showing it's 99% complete for this board. There we go. Banged. And uh

**Dave Jones:** we start again. So, what we're doing is just we're counting how many left on that uh Yeah, because that's the last because It's the last reel. Now, it's the it it it's the end of the reel, is it? So,

**Dave Jones:** we have to be careful. Yeah, yeah. These machines always need tweaking. Rarely do they run continuously for like your uh or you'll get a a stuck feeder or something like that and you've always got to constantly attend these machines.

**Dave Jones:** There we go. We've just put a few more chips manually down into that tube down there. And just doing a few little tweaks.

**Dave Jones:** And that's our dead component tray. I'll do one for you. And there's our compa- there's our tray of No. Oh, they're they're one. Oh, only that one. So, So, we only lost the one component. pitch. Oh, okay. When you're pitching.

**Dave Jones:** All right. Oh, okay. Yeah, we lost a couple of uh lost a couple of battery holders, but yeah. Apart from that, why is that? Why would we lose them these suction cup these suction gauges? you need to pick up a couple of

**Dave Jones:** components Yep. to teach the machine how to do it. Right. Okay. Yeah. to see the pins of the component, to see the height of the component, the color of the components. When you That's why you need to pick up a couple.

**Dave Jones:** Right. Okay. So, yeah. a couple of components in the beginning, but once you Yep. teach it, it's finished. Next time when you do them It's And that's all saving software. How How long would it take you to set up

**Dave Jones:** this machine for this board here? It depends. For this one? For this board, a couple of hours maybe. A couple of hours? 6-7 hours. 6-7 hours? It takes a whole day, almost a whole day to set up. Wow.

**Dave Jones:** And And And this is a simple board, too. Yeah. Right. Yeah, when you get to a bigger board, um and that takes two or three days. Two or three days to set up a big board. Wow. But, you only have to do that once.

**Dave Jones:** Yeah. So, yeah. Mhm. So, you would document where you've placed these reels. It Would the software tell you where these reels need to go? So, when you load the job back up, it would Yep. Okay. And the uh excess waste on these battery

**Dave Jones:** holders is getting quite quite large, but we're still got a lot left on our reel there. Check out our reel. I think that was five uh No, uh Was it I don't know, on a reel or something like that? So,

**Dave Jones:** just tweaking the vibrator there, applying some percussive maintenance. That is the technical technical term of uh giving it a little bit of a bang there to get the chip down. And if you're interested to have a look inside one of these, there's the uh

**Dave Jones:** there's the worm drive for that side there, and so I can zoom in on the Let's zoom in on the stepper motor over here. Look at that huge worm shaft on that. And there's the actuator. Sorry, it's a bit dark in

**Dave Jones:** here. You may not actually be able to see it, but there's the six um uh suction nozzles, so you can see the actuators in the vacuum, and there's the uh trailing cable there. Here's another drive down in here.

**Dave Jones:** Another stepper motor with a huge drive rod. And uh that's why these things cost hundreds of thousands of dollars. And there we go. You can actually see the uh see the head there. That's the head itself with the six

**Dave Jones:** uh vacuum nozzles on it. And how many different nozzle heads would this machine have? which component Ah, which component. So, you would set up the nozzle heads in there based on Okay. Yep. There you go. That's a six That's a

**Dave Jones:** six-nozzle pick and place head. Very complicated bit of kit. And uh that's obviously the uh I believe that's the camera, possibly. Fiducial camera. That's the fiducial camera, yep. So, it aligns the fiducial marks on the board, and I'll show you those on my PCB.

**Dave Jones:** And there you go. There's the fiducial marks uh on my panel there. They're in that corner. Uh sorry, that one up there. And they're in three locations like that, so it knows how to align those align the boards. You'll program it in.

**Dave Jones:** Oh, look, we've got a uh we've got a bottleneck here. We've got a bottleneck. It's churning out these boards so fast, we don't know what to do. Wow, and I think we're done. I think we've done all our 20

**Dave Jones:** panels. That's it. That's complete. And this didn't take long at all. I've only been here for like an an hour or something like that. And uh uh that's how long it took to assemble my 20 uh panels or my 200 microcurrent boards.

**Dave Jones:** And that includes uh fixing the uh problems with the machine and that sort of stuff and around with it. So, um that was pretty darn quick. And now it'll be on to um after some uh visual inspection, of course, it'll be on to

**Dave Jones:** some hand soldering for the uh switches. I've got uh two switches here. And we'll go on to the connectors, as well. And of course, to satisfy all the different jobs you need this many feeders. And of course, they cost a

**Dave Jones:** couple of thousand bucks a pop. So, they're uh very expensive things to actually have. And they'll come in different widths and different types for all the different uh components. There's some vibration feeders down in there. There they are. They've actually got the

**Dave Jones:** uh the uh vibration controller actually attached to them. And there's a uh tray over there for tray-based components. And you've got to have uh see, the reels are already in here for all various uh jobs that they've got in line, of

**Dave Jones:** course. So, these are all ready to go. And they've finished my boards. And uh they're ready to go on another job, I guess. Yeah, we've got all of that engine here to to to be able to assemble any

**Dave Jones:** different component on the market. Mhm. Even even new component on the market and new engineered component should be all be done here because we got all different tooling here for that. And you've got very wide ones here as

**Dave Jones:** well. Okay, that's all very big component. Yep. That could be for example a socket, simple small socket. So we do that for special customer in medical. Right. And we needed a wide one for ours because we have we needed a fairly wide feeder

**Dave Jones:** for the uh surface mount uh CR2032 battery holder here. That's the clever engineer. Remember the design. Because I designed on it. Yeah, exactly. Without thinking about uh what I really need, yeah. But I But some There are some machines

**Dave Jones:** who that may not have these small reels though. Uh yeah, yeah, all right. Also uh in in we have to modify the actually we have to modify the modify the machine to fit for special capacitors. It's sort of

**Dave Jones:** uh capacitor electrolytic capacitor, surface mount, very difficult to get. We have to modify the whole machine to handle the height of the capacitor because 2 mm isn't the standard. Right. We modify the machine for that. So how much did all these machines cost,

**Dave Jones:** Ramiz? Uh really if I start talking about them, I'm going to get high blood pressure again. High blood pressure, yeah. But you're talking about a lot of money here. About a half million bucks. at least The machine on its own about

**Dave Jones:** 100K, but every feeder about $2,000. $2,000 a feeder. At least, yeah. Okay. You get the machine a bit cheaper, but individually you pay a lot more. And here's my partial reel of my 1K 0.1% resistors there and it wasn't a full

**Dave Jones:** reel. I didn't buy it cuz these are, you know, they're they're not 0.01 cents each cuz they're a precision 0.1% resistor. So I bought them based on that re-reeling surface service. I actually uh purchased 210 of them. There they are and Digi-Key

**Dave Jones:** reeled those for me and unfortunately, these are real re-reeled components do actually cause an issue. So, just something to watch out for, but once we got the machine set up and tweaked and everything like that, it seemed to work fairly well and that's

**Dave Jones:** what a typical feeder mechanism looks like. And they've got a second machine over here, which is just a Samsung. It's a stand-alone one and it can be used as a secondary machine to do a second job if the main machine is

**Dave Jones:** fully occupied. And this one, they don't actually have the feeders to do like a 0402 and those smaller components. If they really want to do those, they're going to put it on the main assembly line here. Okay, what we're going to do is we're

**Dave Jones:** going to load another board here and we'll see that it should actually change the width of the conveyor belt system. There we go. It's changing the width of the board all the way out for a 300 mm height board there or 300 mm width

**Dave Jones:** board. So, you don't actually have to go in and manually change that. But these ones you have to actually change manually. You see now it's actually not actually aligned there, so that one will get tweaked manually and the oven

**Dave Jones:** the thermal oven there, we just up manually control the conveyor belt width like that to match that one out there. There you go. And there you can actually see the camera on the fiducial mark itself. That's actually a view from the

**Dave Jones:** from the camera on that particular board and uh setting the center position of the fiducial. And there we go. We're actually manually aligning the fiducial the moment there and set the center, bang. So, you program in the three fiducials.

**Dave Jones:** Doing a manual tweak again. And you'd only have to do this once, of course, to set up your boards. And this is how fast it's actually capable of of going. We've set it up for a dummy run here, and it's really

**Dave Jones:** it's really screaming along, and it's just actually pretending to pick up these components. So, it's it's really capable of phenomenal speed. And if you know that it's picking up six components at once, obviously it'd be a bit slower if it has to actually pick up

**Dave Jones:** the components, actually suck them up with the vacuum, and then place them down, but uh that's physically how fast it's this machine is capable of moving. And that speed is is really determined by the particular type of component you

**Dave Jones:** have. Like, if we've got our surface mount battery holder here, you can't just fly that across and pick it up at maximum speed and just fly it across the machine, cuz it'll just start fall off. The vacuum won't be able to hold it. So,

**Dave Jones:** that's all programmed in the software up here. When you actually program your board, you'll program in the not only the velocity of the pick up, the individual component pick up, like these 0603 caps and resistors. They'll be, you

**Dave Jones:** know, you can pick those up reasonably quickly and fly them across the board, but a high mass component like a a connector or this battery holder, or say leads or something like that. Leads have to be picked up very

**Dave Jones:** delicately, cuz you don't want to damage them. So, really, that's all totally dependent upon each component, and each board, and each job. And you'll see here that the tape is actually pulled back. These are how these feeders actually work. So, only the last

**Dave Jones:** component there is actually exposed to the pick and place machine. But, the So, they peel back all of the all of the tape here for these particular ones and the last components down in there exposed so the machine can actually pick

**Dave Jones:** and place head can get in there and pick them up and place them. And when you finish with it with this type of battery holder here with this type of reel you're you're losing one component. So, there'll be one that

**Dave Jones:** battery holder we saw in there, bingo, it's wasted. And with these smaller components over here you're going to waste six of them with the peeling the tape back. So, if they're very expensive components, well, you're going to waste some of them and

**Dave Jones:** that's what you have to factor in when you get these machines when you get your board machine assembled as opposed to hand assembled.
