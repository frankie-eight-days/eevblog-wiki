---
video_id: JDXKrXJloSw
title: EEVblog 1476 - Keithley 515A Wheatstone Bridge TEARDOWN & TUTORIAL
url: https://www.youtube.com/watch?v=JDXKrXJloSw
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 30, "3": 52, "4": 67, "5": 79, "6": 92, "7": 109, "8": 125, "9": 142, "10": 159, "11": 173, "12": 188, "13": 201, "14": 216, "15": 229, "16": 250, "17": 268, "18": 282, "19": 298, "20": 314, "21": 330, "22": 344, "23": 362, "24": 379, "25": 395, "26": 407, "27": 422, "28": 437, "29": 450, "30": 462, "31": 486, "32": 502, "33": 524, "34": 540, "35": 555, "36": 568, "37": 581, "38": 594, "39": 606, "40": 619, "41": 630, "42": 641, "43": 656, "44": 672, "45": 685, "46": 703, "47": 717, "48": 729, "49": 742, "50": 757, "51": 770, "52": 785, "53": 797, "54": 811, "55": 825, "56": 839, "57": 854, "58": 866, "59": 879, "60": 891, "61": 908, "62": 924, "63": 937, "64": 955, "65": 969, "66": 981, "67": 997, "68": 1005, "69": 1025, "70": 1039, "71": 1054, "72": 1069, "73": 1084, "74": 1103, "75": 1120, "76": 1136, "77": 1148, "78": 1165, "79": 1182, "80": 1195, "81": 1209, "82": 1227, "83": 1243, "84": 1255, "85": 1269, "86": 1284, "87": 1301, "88": 1314, "89": 1330, "90": 1345, "91": 1359, "92": 1373, "93": 1389, "94": 1404, "95": 1416, "96": 1431, "97": 1443, "98": 1458, "99": 1471, "100": 1489, "101": 1502, "102": 1516, "103": 1529, "104": 1542, "105": 1555, "106": 1572, "107": 1586, "108": 1599, "109": 1615, "110": 1630, "111": 1644, "112": 1656, "113": 1670, "114": 1685, "115": 1696, "116": 1710}
---

**Dave Jones:** Hi, let's check out this amazing bit of kit I've had sitting in my bunker for like ever. This is a Keithley 515A megaohm bridge. It's a Wheatstone bridge and you might have heard me mention that term in the previous video that I did,

**Dave Jones:** linked in up here if you haven't seen it, where we were solved that resistor cube problem. And check this out. This is just an amazing bit of kit. It dates from the late 1960s, early 1970s. I'm not sure when this one was actually

**Dave Jones:** manufactured, but look at this. We've got not six, but seven decades here with a range multiplier for measuring high resistance values, i.e. in the megaohm region and gigaohms and teraohm region even. Now, Wheatstone bridges were very common before like modern multimeters

**Dave Jones:** were available and you can actually measure quite precisely capacitors, inductors, and resistance values. You can get LCR bridges. This one is a resistance bridge only and it's only designed for high values. Like you can probably do down in like the hundreds of

**Dave Jones:** kiloohms range, but it's really designed for like high amp. I mean, check out this. This is 10 to the power of five, so that's 100K range. Then you got your one meg range, 10 to the power of six.

**Dave Jones:** And then you got 10 to the power of nine, which is your one gig range. And then you've got 10 to the power of 12, which is teraohms range. And then you've got a seven decade resistance box here,

**Dave Jones:** which basically lets you figure out and match using the Wheatstone bridge method, which will go into and explain, then match your device under test. And because we're dealing with really high value resistors, that's why it has this shielded drop down door

**Dave Jones:** here with a triaxial BNC connector down in there. And if you've uh seen my video, I'll link it in uh if you haven't seen it, it's really good on the Keithley electrometer and uh how you triaxial connectors work and how

**Dave Jones:** the art of measuring extremely low currents works. And that's what you need for something like this. You really need the shielded box triaxial connectors which have uh ground and guard connections in there um as well because when you're dealing with extremely large

**Dave Jones:** resistors like gigohms and teraohms, then uh you need like a really properly shielded and properly designed uh test fixture and this has it built in. And it's got calibration modes and there is the null meter for you null meter fan

**Dave Jones:** boys. I know you're out there. And then you can actually uh set the null uh range and stuff. And you can set the bridge voltage. It can do uh internal or external voltages up to 1,000 V. And there's your specs of this bad boy. I

**Dave Jones:** mean, they call it standard deviation, but uh it's basically specification from uh basically 0.01% even right up to the teraohms range, you're still talking 1 and 1/2%. Not too shabby, huh? But as you can see on the uh high once you get

**Dave Jones:** to the really extreme, you know, hundreds of you know, tens to hundreds of gigohm uh range and the teraohm range, you really need do need uh the high voltage high bridge voltage in order to get actual sufficient current

**Dave Jones:** that you can actually measure. Now, I don't think anyone would actually be using something like this anymore because it is like 50 years old. Although there are still uses for Wheatstone bridges, not only in like strain gauges and uh other measurement

**Dave Jones:** topology like that, but also in high precision metrology applications. And this is where you would have found this bit of kit. You wouldn't have had it in your ordinary lab. It had I think this one did actually come from a metrology

**Dave Jones:** lab, a measurement lab. All right, let's see this bad boy still works. Power internal. Boing. And our meter's gone all the way. No magic smoke. And this is a bit more complicated than your traditional LCR bridge. So, yeah, let's go zero check.

**Dave Jones:** And there we go. So, we can coarse Can we Yeah, yeah, we can coarse adjust that. There you go. Yeah, so I can I can zero that. So, that's working. So, yeah, and we dial that in. Oh, closer, closer, closer.

**Dave Jones:** So, we get near zero There we go. There we go. Hold the tongue at the right angle. Don't want any of that parallax error rubbish. And uh There you go. Bob's your uncle. We have the instructions here as a Star Wars

**Dave Jones:** crawl. There you go. So, yeah, helps to read the instructions, but hey, I did actually do step two there. So, let's go for step three, standardizing. So, set function switch to standardize, and then multiplier to 10 to the 6, and then set

**Dave Jones:** it to exactly 10 point, which is what that is. Sorry, I assume that's supposed to light up, but yeah, there we go, 10.00. And we'll set that to read position. And we need to bring it to exactly null on here on our standardize

**Dave Jones:** function. So, Yep, yep, yep, there we go. So, it's somewhere in there. There we go. So, it's somewhere like that. There we go. Oh, oh, THAT'S BANG ON. OH, YEAH, BEAUTY. YOU'RE YOU'RE GOING TO GET SOME parallax error, but trust me, that

**Dave Jones:** is bang on. And then, we have to set it to zero check, and then over to calibrate like this, and we adjust the 10 to 6 calibration potentiometer, which is down here. So, I'll put that back to read.

**Dave Jones:** And we need to Oh, whoa, that's that's a bit twitchy. That's twitchy. Definitely turn at the right angle for this. Back a little bit. Whoa. Geez, that's tough. No, I took pressure off it. That's going to have to be good

**Dave Jones:** enough for Australia. Now, ordinarily, we'd have to go through and calibrate all the different ranges here going all the way up. But, we're only going to measure on the megaohm range that we just calibrated. So, yeah. I'm just not going to go

**Dave Jones:** through and bother to do the rest. Next. So, we're going to try and measure this Welwyn 200 meg. That's not 200 milli, it's a 10% uh high voltage high ohmic resistor. So, 200 meg, let's see if we can dial this in. Okay, so I just

**Dave Jones:** adjusted the ground point over here. These are all the same ground point. This is the input and this is an external triaxial input. So, we just use the regular input here and see if we can do that. So, I'll close that up and

**Dave Jones:** there is a micro switch down here so that will actually now enable it. So, let's measure this sucker. So, let's put it back to operate like this. I'm going to have 10 volts here for our Wheatstone voltage and

**Dave Jones:** and we're over. Okay. So, now we have to dial in okay what we need to where we what we think it is 200 meg. So, we're on the megaohm range. So, this is times 100. So, we have to go to 200 there like

**Dave Jones:** that. I'll dial up the sensitivity a bit more like that. And so, right, so we dial in exactly 200 what we think it is and it's on this side. So, that's actually on the low side. So, we have to increase it a bit

**Dave Jones:** and you'll notice that we can bring that into the middle. So, it's somewhere you notice it's gone to the like I can turn the increase the sensitivity. So, you can see how it goes either side of the center there. So, that means it's

**Dave Jones:** somewhere between 230 meg and 220 meg. So, what we'll do is we'll just increase that 220 225 meg or thereabouts. And yeah, the others we can dial in as well, but really you know, you're getting down to sort of

**Dave Jones:** is is it drifted a little bit? 224 meg, something like that on maximum sensitivity. Anyway, there you go. So, the other ones really aren't relevant here. We can probably go up in voltage and we can get some extra range here.

**Dave Jones:** So, let's actually go all the way up to 100 volts, shall we? And at 100 volts it's actually quite quite different. It's somewhere between 200 210. Turn it the right angle. 210.3 or thereabouts. There you go. So, that's

**Dave Jones:** the higher up in the voltage we go the more current that we can get. Well, actually I can go up a precision here and yeah, I wasn't even on maximum sensitivity. There we go. Yeah, now it's it's 210.3

**Dave Jones:** megohms and that's how you measure using a bridge. So, we've got actual resistors in here and to the actual value of 210.3 megohms and we can dial that in even further. And then if our device under test on the

**Dave Jones:** other side of the Wheatstone bridge is exactly the same value it nulls out the current like that. If it's either if it's, you know, more or less it goes either side. Neat, huh? Back in the old days of multimeters, this is how you

**Dave Jones:** actually measured resistances. So, anyway, there you have it. And it does have some satisfying relays in there. Listen to this. Clunk.

**Dave Jones:** I love that center zero needle. It's great. And I can actually measure this here in the lab using my modern Keithley 7 1/2 digit meter here. I don't know the accuracy of this for this particular range, but it's showing 233

**Dave Jones:** megaohms there. And yeah, like I'm keeping short leads here cuz if you put long leads on this and put your hands near it, you're going to come a goner. But there you go, 233. So I don't know which one's what. You know, maybe could

**Dave Jones:** have calibrated the other one a bit better. Maybe it's drifted. I don't know. Look, it's ancient. Right? But as you can see, we dialed in and you remember it also changed with voltage. It was actually at 10 volts it was like 220 odd meg, then

**Dave Jones:** it dropped down to about 210 meg at 100 volts. So, you know, this is measuring much lower than 10. But there you go, that's what we get in. I mean, you know, you can like all these digits are just

**Dave Jones:** BS, right? They're just just there for show, really. It's nowhere near the accuracy that matches that resolution. But there you go. So we'll do a brief look at how Wheatstone bridges work on the whiteboard here. Now, it was

**Dave Jones:** actually invented by Samuel Christie here, but you know, Wheatstone took it and developed it further and he's the one who got all the glory. Anyway, Charles Wheatstone. So it's a bridge configuration which of course you'll know from like a diode bridge

**Dave Jones:** configuration. And it's basically just four resistors like this. This is all it is with a voltmeter in the center or an electrometer in this case because we're measuring extremely low currents with this Keithley device. But basically a voltmeter in the middle. So I've got a

**Dave Jones:** DC voltage source here and you can see that we've basically got two resistor dividers. One here, so this is one point on the divider and here's the other point over here. And you can see that by inspection, as we've talked about in

**Dave Jones:** previous videos, if the ratio of this divider here is the same as the ratio of this divider here, then the voltage difference between these two points is precisely zero. They're equipotential nodes, as I've mentioned in that resistor cube video. So, our device

**Dave Jones:** under test, our DUT, is this resistor here, which we put on our terminals. And then on the other branch over here, we've got our adjustable decade resistors. So, this is a six-decade jobbie, and you put your tongue at the right angle,

**Dave Jones:** and you twiddle these until you actually read off exactly the same value that matches this. And of course, these values up here, these would be your range resistors, and you can actually So, this will be like have a switch in

**Dave Jones:** there with multiple ranges, and this one here can have like little adjustable trimmer in there as well to sort of like tweak all the ranges, and that they were the calibration controls that we saw on the front panel there. So, once you've

**Dave Jones:** actually calibrated this bridge, and you can do that very precisely, then you can actually read off the dials, assuming that these are very precise resistors, but also you can trim these as well. You can calibrate them as accurately as you

**Dave Jones:** want to. Then you can just dial off and read your device under test. When you when that meter gets to zero like that, it means there's zero voltage difference between here. And the great thing about the Wheatstone bridge is that you can

**Dave Jones:** measure incredibly accurate stuff. And the great thing about the bridge configuration as opposed to just like a single voltage divider, you could do a voltage divider and just read off this node here relative to ground point here and with a, you know, a precision

**Dave Jones:** voltmeter and stuff like that. But the bridge configuration allows you to get much greater accuracy. And as I said, in this particular case, this is actually an electrometer in here, so you'll have an amplifier like this, and you can have

**Dave Jones:** different range resistors also in here like this, and you can select that was that sensitivity adjustment that we'll apply in around with. So, we've basically got an amplifier with an electrometer in there. So, you can even measure more

**Dave Jones:** precise values close down to 0 V. And you can use the Wheatstone bridge configuration for not only measuring resistors, but as I showed before, uh inductors, capacitors, and you can put other devices in here like uh light-dependent resistors, and you can

**Dave Jones:** measure uh you know, light intensity. And but one of the big applications these days for Wheatstone bridges, they don't really use them except for really as I mentioned really precise metrology uh measurements uh these days. But one of the common uses for this is in strain

**Dave Jones:** gauges uh like inside a load cell or something like that that measures uh like tension or uh like weight scales and stuff like that. And they use the bridge configuration cuz you can get extreme accuracy instead of just using

**Dave Jones:** one branch. So, instead of using just one arm like this, you use two arms, and then you can actually measure uh the difference when like a strain gauge, for example, you might put a flat resistive uh strain gauge on like a metal bar, and

**Dave Jones:** then you can detect when it's actually bending, and then you can get a voltage measure the voltage difference out of here. So, you'll typically in like a weight scale or a strain gauge, you'll actually uh put a very precise amplifier

**Dave Jones:** in here, and then you can uh sample that digitally. And that zero check function we're playing around with on the uh front panel, that's just a simply a switch which shorts out these two terminals. So, you can trim it uh uh uh

**Dave Jones:** to measure precisely zero right in the center. And just as an aside, because we're measuring megaohms and gigaohms and teraohms here, we're using an electrometer, very small currents we're talking about, then the grounding matters. So, here's the uh diagram for

**Dave Jones:** that's actually used in the uh Keithley manual, and you'll see that there's basically a shield around here. There's a guard shield like this, and it includes the voltmeter like this. Includes the electrometer. So, all of that is shielded. It doesn't

**Dave Jones:** matter. All this uh uh this other branch over here is can be outside the shield, but all of this high impedance node stuff, you really want that inside a guarded shield. So, that's why you use a three-terminal triaxial connector. So,

**Dave Jones:** you might have like chassis mains earth out here like this, but inside this is actually our grounded guard terminal. And that eliminates leakage and other interference issues from your precise electrometer here. And you've seen that in my Keithley picoammeter teardown as

**Dave Jones:** well. I'll link that one in, too. But, anyway, Wheatstone bridges, they're very cool devices and they're still used today, even though not really for any mainstream measurement. As I said, really precise metrology stuff. You can get incredible precision with these

**Dave Jones:** things, but you've got to take the time to set them up, calibrate them, do everything else. But, once you do that, yeah, you can get way better than you know, almost any modern instrumentation. So, let's take this bad boy apart and

**Dave Jones:** see what's inside. For those playing along at home, made in the UNITED STATES OF AMERICA, CLEVELAND, OHIO. And I actually checked the address in the original manual from this from like 1970 is still the Keithley address today. They're still in

**Dave Jones:** the same building. I wonder if it's still the same phone number and everything. Anyway, what we've got in the back, we've got the external input. That's that you know, if you want to feed up to 1,000 V cuz it's only got 100

**Dave Jones:** V internal. There's an accessory outlet, so you can power other mains stuff with it. And a good old-fashioned switching rubbish. Got a good old-fashioned transformer with voltage selection. And you might think given the vintage of this designed in '68 and first like sold

**Dave Jones:** in like early 1970s, you might think that this is like valve you know, it might have some valves in it. But, no, this is the fancy pantsy modern A model which is all transistor. They did have the non-A version before this which

**Dave Jones:** dates back to I think around 1960, 1961 and yeah, they use valves or JFETs with pilot lights as they're affectionately known. But yeah, this will be all all modern transistor stuff. One thing I'm expecting in this is a lot of space.

**Dave Jones:** I mean, how many rack unit high is this? Have you ever seen anything that big? It's just absolutely enormous, but yeah, anyway, oh no, we're going to have to break going to have to break the cal seal. Oh, it's a great tragedy.

**Dave Jones:** All right, let's have a squeeze in here and ta-da! Ah, so high. My camera's not up high enough, but here you go. Oh, look at that. Yep, it's mostly empty space. Hi. So just check out the beautiful wire

**Dave Jones:** looming inside this thing. Very nice indeed. And of course, anything that needs to is shielded. There's very careful guard stuff, but check out this. That's actually an open-air high voltage relay. And you can see the coax going off the bottom here.

**Dave Jones:** This actually goes off to the high voltage external connector on the rear of it. So yeah, they've just like stuck it in the open there. I had to get my weird ass Yankee Allen key set out so that yeah, this is like a

**Dave Jones:** 5/64ths. Whatever that means. All right, but it fits. Oh, there's the back of it. Isn't it beautiful? I should have actually done this teardown in 4K, but yeah, sorry about that. Too late now, really. And there's your inputs down here and

**Dave Jones:** check out how they've just got it flapping around in the breeze here. Here is the input here and it's going up like just completely out in the open like this, but of course, it's in a shielded box, so no worries, but they kept it

**Dave Jones:** away from absolutely everything else. Goes up into this shielded box up the top here and then it's just incredible. And here's the triaxial input here. You'll notice that the input of course goes over to the duplicate input over here, but then this

**Dave Jones:** resistor here connects the ground of this over to the center guard of the external connection like this and then of course this is connected and then the main part of the triaxial connector is connected to the mains ground chassis.

**Dave Jones:** And then the ground over here, the mains earth, that actually goes over to the terminals all the way along here. You can see just the bus bar connecting all those. So we were actually using a single-ended earth measurement before,

**Dave Jones:** but if we want to do higher values that are more critical, we could have actually used the triaxial connector with its proper guard connection. And they all run back including the guard connection into the wiring loom, but because it's all inside, like you know,

**Dave Jones:** you don't need to shield any of this cuz it's inside a shielded box. There's our trimmer calibration pots on the front and our range resistors. And anyway, these God, I'm going to have to lift the tripod up. These wires come up here and they bugger

**Dave Jones:** off, they bugger off, they bugger off right along here. They go along this arm and then they go into finally the back of this shielded box that we've got here. So this is all of our measurement stuff inside this box here. And then

**Dave Jones:** down here there's our mains power supply. We'll have a quick look. Well, no. I thought a mains power supply would be in there, but no, it's just the voltage selection. So no, there's the mains power supply hidden away in plain

**Dave Jones:** sight there on the top because this is so tall. It's hard to like see inside this thing. So anyway, look at that. Isn't that that just looks beautiful, doesn't it? And Mallory, all the Mallory fanboys go wild. Look at

**Dave Jones:** that cap. It's a beauty. Still works after all this time. Of course it does, made in the USA. That is a very nice old school power supply, isn't it? Really like it. We've got some RCA jobbies down here. Look at those. Aw, Bobby dazzlers.

**Dave Jones:** No date code on them though. Uh not that plastic package rubbish, metal can all the way. Um that's our main uh transformer. Looks like like a modern switching uh semi-modern transformer, but it's not. This is a purely linear uh jobby. And it does look

**Dave Jones:** like it is two stage because this can go up to 100 volts. This is probably like giving the high volt out. We've got another bridge in here. So we've got one bridge over there, another one here which is a secondary one um for uh like

**Dave Jones:** the lower voltage uh stuff over here. That's for you wafer switch efficientados. There you go. They still looking really good Nick after all these years. We still don't know how many years that is though, but uh yeah. Anyway, these are all the uh decade

**Dave Jones:** range resistors. So this is where all your precision resistors are. Here's your switches and resistors for your uh voltage range. And as you can see, they're only like 1% jobbies, but you know, 4.02k. They you know, they they dialed that one

**Dave Jones:** in. Ha. I'm here all week. Check it out. On the outside of this box, look at this. They've got a uh real This is an external the coil they wanted for the relay they wanted to keep outside of the

**Dave Jones:** box so it doesn't interfere with any of the stuff inside. Nice attention to detail. And that would basically be a uh reed switch in the center of that. And then that's just a a coil around the outside to activate the reed switch

**Dave Jones:** inside. Check out the axial cap in there with its own bracket. Beautiful. So there's all our decade resistors with the highest values up there. you can see them. They're the glass tube ones. And then they've got a Davin brand. I don't

**Dave Jones:** think I've ever heard of Davin precision resistors. Anyway, these are your 0.01% jobbies, and they get smaller and smaller smaller as they go up. But yeah, that's where all the precision and once you get to the other end, these ones are

**Dave Jones:** only like 1% jobbies. They don't have to be anything special cuz they're so far down the chain that you really don't need the high tolerance. You really need the high tolerance on the upper end resistors. You can really see those

**Dave Jones:** glass encapsulated higher value resistors that we've got on our top times 100 decade there. Very similar to the Welwyn one that we actually tested, but yeah, they're very nice. I mean, you know, like if you didn't want to use

**Dave Jones:** this thing anymore, you would gut them for the precision resistors. They'd still be good. You know, in fact, the stability probably goes up with age. You know, they're probably still good like 45, years later. One thing I really

**Dave Jones:** love, this is actually the potentiometer that we're adjusting, the null adjust potentiometer. And you'll see maybe down in there, the how the shaft, it's got it's just a regular like slot cut into it and then they've got the little

**Dave Jones:** shafty thing on there. Let's see if I can rotate that. Check it out, they've actually got a pin which goes in there and just rotates that from So, they've got the wafer switch on the bottom and then it just got the center

**Dave Jones:** goes through. That's that's beautiful. Thing of beauty is a joy forever. Look inside our can here. These are our range selection resistors. Look at that. You've got the high value glass tube jobbies. That is just gorgeous, isn't it? But you can see

**Dave Jones:** that they're only like 1% jobbies. They don't need to be hugely accurate. It's the decade switches which are the ones that have to be really accurate, but uh, jeez, look at this. Look, it's just it's just beautiful. Look at it, it's all

**Dave Jones:** interconnected. Look at this, with penetrators. Those white things look like penetrators, but there's not actually anything connected to them, so that's interesting. Although they do penetrate, there's nothing connected to this top side. They're just using those as as connection points for the

**Dave Jones:** resistors on there, but um, yeah, look, all of our proper star grounding everything else, right? Or star guarding. This would probably be the guard uh, most likely go back to the guard uh, terminal, and then they've got that, and

**Dave Jones:** that goes off to uh, down here, which is our function selection switch. So, that's where we were selecting uh, the operate mode, the calibrate mode, and whatnot. And there's our reed switch in there. Look, beautiful. Uh, they put

**Dave Jones:** some tape on that. I'm not sure exactly why, but um, yeah, anyway, they're able to get the the cuz the coil that coil's on the other side here, you can just see it, and they get uh, the magnetization

**Dave Jones:** to come through on these screws, by the looks of it, and that's what activates the um, reed switch internally, so that they don't have to bring so that they A, don't have to have that magnetic coil inside the box, and uh, B, they don't

**Dave Jones:** have to have the reed switch actually penetrating going outside the box, because it's obviously a high impedance node. And what it's it's it does look guard switching. Actually, I'm not sure if this is actually the guard terminal, whether or not this is actually the

**Dave Jones:** measure could be the measurement terminal. I'm not sure, anyway, you'd have to uh, look at the schematic diagram, linked it down below, by the way, full service manual, all the parts, all the schematics, everything, like they used to. You'll notice that there's

**Dave Jones:** hardly any circuitry in here at all. There's a couple of uh, discrete transistors there on the uh, Teflon standoffs, but you can see these penetrators here, and these screws hold on a can that's actually on the backside of the case and that's where um, the

**Dave Jones:** like amplifier circuitry must be cuz it's not inside here. So, link in the service manual and schematic for this down below and I'll whack it up here briefly. You can see that there's actually not much in this. It's just a Wheatstone bridge, you know,

**Dave Jones:** a high voltage source and that's you know, and some amplifier stuff to get your you know, your null ranges and stuff like that. But apart from that it's incredibly simple and as you can see it's mostly empty space. So, they

**Dave Jones:** certainly didn't need to make it that big. But it was made for a particular market. As I said, this is not designed to be like a desktop instrument or anything like that. But there's really a lot of art that's gone into this,

**Dave Jones:** especially in terms of like we could really spend hours looking at how all the guarding system works and stuff like that and just the layout of the wiring and the shielding and the guarding to prevent leakage and all sorts of other

**Dave Jones:** stuff interfering with incredibly low current measurements, which is what you get when you try to measure you know, megaohms, gigaohms, teraohms value resistors. And you take it for granted these days, but you know, back then this was pretty much the only way to do it.

**Dave Jones:** So, that's a very unusual old school bit of kit and I hope you really liked that. I will put some high res photos over on my EVBlog Flickr account. They're linked in down below if you want to see a bit

**Dave Jones:** more detail and zoom in and stuff. But this is absolutely fascinating. Now, this one sitting around for a while and glad I finally got around to it. It's a thing of beauty, joy forever. If you liked it and if you liked it, give it a big

**Dave Jones:** thumbs up and as always discuss down below. Catch you next time.
