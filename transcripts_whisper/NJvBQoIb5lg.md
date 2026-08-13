---
video_id: NJvBQoIb5lg
title: EEVblog #980 - RoboMaid Automated Vacuum Cleaner Teardown
url: https://www.youtube.com/watch?v=NJvBQoIb5lg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 33, "3": 49, "4": 69, "5": 89, "6": 109, "7": 129, "8": 145, "9": 165, "10": 181, "11": 201, "12": 229, "13": 249, "14": 265, "15": 281, "16": 297, "17": 313, "18": 329, "19": 353, "20": 373, "21": 397, "22": 425, "23": 441, "24": 461, "25": 485, "26": 509, "27": 529, "28": 545, "29": 565, "30": 577, "31": 601, "32": 617, "33": 641, "34": 661, "35": 681, "36": 697, "37": 713, "38": 737, "39": 761, "40": 777, "41": 793, "42": 805, "43": 825, "44": 841, "45": 849, "46": 869, "47": 881, "48": 901, "49": 913, "50": 929, "51": 945, "52": 973, "53": 989, "54": 1013, "55": 1033, "56": 1053, "57": 1069, "58": 1085, "59": 1097, "60": 1113, "61": 1133, "62": 1149, "63": 1173, "64": 1189, "65": 1209, "66": 1229, "67": 1249, "68": 1273, "69": 1293, "70": 1313, "71": 1329, "72": 1345, "73": 1361, "74": 1377, "75": 1393}
---

**Dave Jones:** Alright, let's check out the robo-made, very quickly, the auto vacuum cleaner. Yeah, this is like a rip-off of the Roomba or whatever. Cheap-ass thing. It's got a little bumper on there. It's got, looks like optical ports around there. If you don't know how these things work, they, I believe, like this is the charging stand.

**Dave Jones:** These are little charging contacts like this. And you might think, well how does it get all around the room, go around and all that sort of stuff and then make its way back precisely to where it charges back up on these pads here.

**Dave Jones:** These are reasonably nice little rubber feet and stuff like that on the wheels here, but it's going to slip and stuff like that, so it can't just drive around the room for hours and hours and then come back to precisely the same spot.

**Dave Jones:** Because if you get any wheel slippage and stuff like that, it wouldn't be accurate. So it's actually got a little like infrared type transmitter on here and it can determine its location in the room and then come back. So it can get roughly back to where it is.

**Dave Jones:** Almost certainly tracking where it's going and stuff like that, but to correct for all the accumulated errors and stuff like that, it can navigate its way back like this and go in and boom, and recharge with the pads on the bottom there. So yeah, what this thing is

**Dave Jones:** I don't know, it looks like an additional transmitter, it's got a lens in there, you can see that, which basically gets a 360, that's a 360 degree lens so it's looking all around the room using that particular lens and there's another little, so does it transmit out there and

**Dave Jones:** receives back? I'm not sure how that fits in the operation of the thing. Hmm. And that's powered from two D-cell batteries, and you'll notice that there is a matching lens on here. Here it is, 360 degree lens. You've probably seen these on the TV

**Dave Jones:** backlight teardown I did this. They did do this, shine a LED right angles off the board and then it reflects outwards like that to give you the nice even backlight pattern on your you know, the back of your LED backlit LCD, but it can also

**Dave Jones:** be used to receive as well. So it can be used to transmit as well as receive in a complete 360 degree rotational 2D map right across your you know, around the robot. Now there's not much inside that, looks like we have a little micro

**Dave Jones:** little like 14 pin jobby, you can tell because it's got a sticker on there so it's obviously programmed. And well, there must be another board up in there. Looks like there's two infrared LEDs in there, one emits out the top, which then of course goes into

**Dave Jones:** the little lens like that. There we go. So your LED actually sits in there and then it emits a pretty even pattern all the way 360 degrees around that. So why does one emits out the front? Yeah, it's some system thing, but yeah, there ain't much in that puppy at all.

**Dave Jones:** And that micro, couldn't be bothered to put the macro lens on, is a Sonic SP25811. It's a little 8 pin micro from Sonics. What? Like a Taiwanese microcontroller manufacturer. What the? They're obviously really pinching the pennies there. Jeez. It's the Schrobot M788 Chong

**Dave Jones:** Dieng version 1.0. Be afraid, be very afraid. Anyway, this is inside the charging dock. That's, you know, that's neat and tidy, there's nothing wrong with that. Put heat shrink over there. You know, they're doing okay, nothing wrong with that at all. So we've got a micro

**Dave Jones:** up on the top board there. Is that also a micro? Let's check the brand out on that. And that's a whole tech job. Why are they not sticking with the one brand of micro? I don't know. Like, jeez. It's making your life harder.

**Dave Jones:** Penny pinching again, obviously. So that is just driving the LCD on there for all your stuff. We've got another lens on top there. So they're obviously like pulse coding the lead timing information, but you know, I mean, it's the speed of light. It's not like they're using ultrasonics

**Dave Jones:** to, you know, like triangulate position and stuff like that. But yeah, that's some sort of pulse information. Maybe I can power it up and have a look. Once again, they've just got a single lead in there. Infrared lead with the same, exact same lens system.

**Dave Jones:** That's interesting. They've got some sort of lens, and it looks like some sort of lamp in there. Are they doing some sort of detection? Yeah, look, it's right next to, looks like some LEDs here. Or maybe, you know, some photo trennies or something like that.

**Dave Jones:** What are they trying to do there? Is that some sort of like you know, floor type detection? It's not like dirt detection or anything like that, I don't think. Hmm. Actually, they've got the same sensors in three other places around this front edge as well.

**Dave Jones:** So and they're actually angled. Yep, so we have an infrared transmitter and an infrared receiver in there. There's your lithium ion battery pack. It's going to be crusty as. And there's your dust collector. They've got a filter in there and whatnot. But curiously, look,

**Dave Jones:** it's got that infrared type door to match the infrared around the side here. That's interesting. So they're obviously doing some type of, you know, like infrared dust detection or how much is... bleh. But there doesn't really seem to be anything inside there though to

**Dave Jones:** transmit through. Hmm. Surely they've done that for a reason. Here we go. I think I've got all the screws out. Woohoo! And we're in like Flynn. Oh yeah, baby. There we go, messy robot. There's wires everywhere. This is interesting. Check it out. Lift that off.

**Dave Jones:** Ta-da! Look! Piezotransducers that go on the underside. You can probably see the contacts are up in there. And that goes into the cavity of the dust collector thing. So based on how much dust is in there, they're obviously emitting high frequency into there and determining, you know, and the properties change

**Dave Jones:** depending on the dust they want to be using as a transmitter and one as a receiver most likely. And so they can figure out how much dust is in there. It's kind of interesting. Actually that gets more interesting. Check it out. There were actually two boards in here

**Dave Jones:** which go back to back like that, which each one drives a piezotransducer. Those boards look identical. So that's interesting. Like I thought they'd be transmitting on one, maybe using the other one as a receiver you know, as crude as it might be, I thought that could possibly work.

**Dave Jones:** So interesting. So whether or not these are just receivers and they've got a, I guess, like you've got the maybe they're using the motor in there and you know, the dust and everything else, it changes the acoustic properties based on that. But then why would you need two?

**Dave Jones:** You wouldn't really need two then. So it's doing some sort of stereoscopic, you know, type sensing with a piezotransducer element. Oh look, rubber surround on there, they're isolating that as well. So maybe they are doing the acoustic properties based on the motor, and then stereoscopic

**Dave Jones:** Anyway, I'm sure there's lots of software processing behind that. But that is absolutely fascinating. By the way, the chip on there just an LMR324. So yeah, they're not transmitting anything, they're just using these as some sort of sensing and they'd be doing filtering as well on

**Dave Jones:** those two boards. So for those who want to play along at home there we go. And another thing that might back up my theory that they're both detectors is that left D and right D for detector. That'd be my guess. This is the cable going off to the board.

**Dave Jones:** Alright, what else have we got on this thing? We've got two, these would be stepper motors inside here to drive the wheels. This one here just drives the spinny brush thing under there, so it's just a Jobe Logs DC motor. And we've got ourselves two micro switches

**Dave Jones:** there and over there, so it's basically I guess if you hit it straight on it's going to press two, but you get the timing differences between them, or if it just bumped on this side you'd only get the one micro switch activating, etc.

**Dave Jones:** etc. As far as the main board goes, I mean it looks reasonably engineered, there's nothing wrong with that at all. It's certainly not shoddy by any stretch. We've got, once again, that's probably some weird-ass Holtec processor or something like that. We've got another embedded micro over there

**Dave Jones:** controlling, that looks more power stuff. Anyway, we've got some motor drivers over here and you know, this is doing all your heavy-duty processing and figuring everything out. And I know you want to know what that processor is. Let's find out. And that is an NXP ARM

**Dave Jones:** processor LPC2132. For all you LPC fanboys. A LAN EM78P259. What the? And why is it socketed? Like they're using, what, 3 or 4 different types of micros or something in this thing. Crazy. And the top board uses an STMicro 12C5202 or whatever it is.

**Dave Jones:** And yet another brand micro. Like, they've chosen a different micro for every application in this thing. Wow. That's just, it's nuts. Unless they had like different people different groups working on different boards, and they all chose their own flavoured micro or whatever or not they were.

**Dave Jones:** Penny-pinching every cent on every single application inside this thing. I don't know. We've got another motor down in there, just a DC motor for the brush thing. That little brush that just spins around, gets into little nooks and crannies and stuff like that, and then sweeps

**Dave Jones:** it back under for the main collection. Why do they have to light up the bottom of this thing? I, like, I don't know. I mean it comes out the bottom there. These sensors here are infrared sensors. We can take one of those out, we've got 4 of those as I said, but just lighting up

**Dave Jones:** that part there, what does that achieve? I don't know. And we've got 4 of those little transmitter and receiver boards, that'd be infrared, so infrared LED, infrared training. And looks like they've got a little speaker tucked away in there to make it go beep!

**Dave Jones:** Bing! And there's our main drive wheel. That's a complicated little thing, complete with all original hair. Pioneer rubber belt co, I guess. Um, yeah. Anyway, there is our stepper motor that drives the wheel. So yeah, obviously they know how many turns it's gone, and then they've got the reduction mechanism.

**Dave Jones:** There is sensing, look, there's another infrared transmitter and receiver. Ah, that makes more sense. There you go, they're counting the revolutions there. See the little slots in there, and we've got an infrared, well a photo, LED and a photo transistor there, and that just counts

**Dave Jones:** the number of pulses. Don't rely on the belt, belt could slip. Oh, there's the part number for the motor for those playing along at home. So there you have it, that's inside the, what is it? The Robo Made. Um, yeah, Roomba ripoff I guess.

**Dave Jones:** It's reasonably well engineered, there's nothing you know, it's kind of, it's built down to a price somewhat, but you know, it seems to be half reasonable quality. I don't know what it's performance would be like. I mean, Tom said it broke on him

**Dave Jones:** so you know, probably got cheap-ass plastics or whatever in it, but yeah, they've gone to a lot of effort to do that. All the different micros in there, that was absolutely fascinating, but obviously the main NXP micro in here is taking care of business.

**Dave Jones:** It's tracking exactly where it's gone, it's handling the communications with the transmitter and the charging station to get it back there to automatically charge up to know where it's gone back to. And as I said, there's going to be slippage on these wheels, so

**Dave Jones:** you can't just go, okay, I'm going to step X amount this direction, turn X amount this direction. Because by the time you go around the room ten times, sweeping everything, taking a couple of hours, all those errors are going to accumulate up and up and up, and bingo, you're going to miss your charging station

**Dave Jones:** if you try and backtrack. Even though you're recording all the steps, try and backtrack it, you find that you're, I don't know, a metre out or half a metre out from your charging station or something like that. Or you could be on the other side of the room.

**Dave Jones:** It could be that bad. So yeah, you've got to have those transmitters, where are they? Yeah, those transmitter, infrared transmitters transmitting all over the room with the 360 degree sensor on top to know where it is and how to get back. Because that's the idea.

**Dave Jones:** I mean, the whole idea is that it's completely autonomous apart from having to empty the thing occasionally. It's supposed to go back to its charging station, charge itself up, and then, you know, go to sleep and then wake up the next morning and go off and do its chore again.

**Dave Jones:** I don't know. Does anyone use these things? I, like, apparently the Roombas or Roomba, whatever you call it, are okay. I don't know. Are these cheapies any good? Let us know in the comments if you've got one and if they're actually useful. Hmm.

**Dave Jones:** And the bottom of that board, we've got our classic extra tinning on the trace there just to increase the, sorry, decrease the resistance increase the current handling capability of that trace going right around from one side to the other. Just by a tad.

**Dave Jones:** Done a video on that somewhere. What the hell? What are they using this thing for? It's got to be obvious. It's just not coming to me. Oh, alright. I'll probe one of the driving transistors for one of the LEDs there. I've got it set.

**Dave Jones:** There's like three different modes on this thing. I've got the switch down and there's, I don't know is that, like, full half off? I don't know. Anyway, I've got it all the way down and that's what we're getting spaced about, oh, 150 milliseconds.

**Dave Jones:** Well, there we go. 150 milliseconds apart or something like that. And no surprises for finding a typical 38.5k infrared carrier in there. That's typical of infrared carrier frequencies. But that really doesn't seem to change. Not really. Anyway, you could go into great depth, but no, it's pretty much

**Dave Jones:** pretty consistent. If we put the LED up to the middle, sorry, the switch up to the middle position, has that changed? Now it's down, back down no, it looks very similar. There might be subtle differences in there. This is right up the top full

**Dave Jones:** so, you know, yeah, the counts could be subtly different in there, but no, I don't see it. Aha! I figured it out. That's the infrared, basically the power. Look at this. The amplitude drops, so that's full down the bottom and then I'm just adjusting that switch there, so that looks just like

**Dave Jones:** it's a amplitude thing, because that would correspond I'm measuring directly across the LED now, so that would correspond directly to the current through the LED. So that would be, yeah. That's the output. So that's all she's doing. Alright, I'm probing both LEDs here, because if you remember, we had

**Dave Jones:** one that was 360 degrees which is the top one, and then we had the other one which just transmits out the front Now the yellow waveform, channel one there, is the 360 degree one. And you'll notice that they are different. There's a difference in there.

**Dave Jones:** This has got an extra sort of packet in here, so it's decoded different. So whether or not we can check that these might be different at each period, they're bloody touch screens. But you know, we could go in there and decode to our

**Dave Jones:** hearts content. But yeah, it's interesting that the front emitter is different from the 360 degree emitter, but that makes sense, otherwise why would you have two? So yeah, it wouldn't surprise me if they're subtly different, doesn't look like it on the surface, but

**Dave Jones:** you never know your luck in the big city. So that's obviously sitting there like well, you turn it on, and you just leave it on all the time. It's just continually transmitting. I mean, there's a lead, what was the burst frequency? I can't remember.

**Dave Jones:** Anyway, it's not taking that huge amount of current to use those two big D-cells in there, so they would last for a long time, maybe a year or something, I don't know. For just transmitting periodically like that, they should get reasonable battery life.

**Dave Jones:** So that's interesting. So even if this data is exactly the same each time, then that could still be useful, because you could have one okay, it knows it's the front emitter, so it's obviously got a different code to the 360 degree emitter, bloody touchscreens again.

**Dave Jones:** So it, you know, that gives it essentially a positional, like you know, line of sight type positional data. Am I actually facing the sensor? You know, if it's getting this front emitter one, then it knows it's facing the sensor. If it's getting only getting this one, it knows it's on the other side, etc.

**Dave Jones:** So you know, even that's useful. And this data could be individually coded per unit and matched per machine, transmitter and robot. So you know, you can have different robots in different rooms and, or different areas, and these transmitters wouldn't interfere. That's the theory anyway.

**Dave Jones:** Now if we power up and have a look at the charger transmitter board, it's got two IR transmitters here, slightly angled. Curiously, like there's a clear window over here, clear window over there, but it doesn't seem it sort of seems lined up with the edge of the, that blocking

**Dave Jones:** plastic there. So that's rather unusual. Anyway, we've got ourselves two LEDs again, let's check that out. And bingo, this is what we get. Basically, very similar to what we get before. It looks like the data's not really changing, is it? Do you see a little bit of jittery

**Dave Jones:** on that? There's basically bugger all in that. So if we scroll across like this, you can see that it's different here. So that's, that's certainly different. And there's our carrier of course, that's 41.3 kilohertz. I didn't measure the other one that precisely, I don't think.

**Dave Jones:** Did I? Anyway, oh yeah, yeah I did. So this is a different carrier frequency, okay? So it obviously knows that that is different, and the code is slightly different, but as I said it seems to be the same each time. There's nothing in that, that's just your regular

**Dave Jones:** jitter. So that, yeah. They're both identical. So both the, like I call it the mobile transmitter, that you I guess strategically place somewhere else in the room that you want done, and the base station are just outputting two different LEDs to output just two different

**Dave Jones:** codes, and that's it. And they appear to be a slightly different carrier frequency. So that's all significantly less sophisticated than I thought it would be. Basically all it's doing is relying of course on recording how many steps it takes on each wheel and it can backtrack its entire thing like that.

**Dave Jones:** And then there's just that homing infrared receiver on the charging station that has that interesting dead window. I guess that's quite a novel, simple way to do it. It's like a line following robot. It wiggles its way back and forth between those two codes either side, and it goes

**Dave Jones:** and heads all the way back to the center of the docking station. So it's crude, but simple and probably works quite well. I don't know about the Roomba one, I've never looked at it, never used it, or other ones on the market, but hey, it looks like they can

**Dave Jones:** do this, no problems at all. Because once the robot just goes autonomously on its own going around, and once it reaches the manual says 15% of the battery life left, then it goes into return to base mode. So it just goes hunting around for that

**Dave Jones:** transmitter coming from the base station. Now of course the base station was a different carrier frequency to that mobile virtual wall transmitter. And of course the virtual wall transmitter had that, the 360 degree one on top would stop the robot actually bumping into it

**Dave Jones:** and then screwing up. Because you don't want your robot bumping into your transmitter which you strategically set up to point across a doorway or something like that to prevent access to that doorway. So it's all fairly crude, but rather interesting. It probably works half reasonably well.

**Dave Jones:** I don't know if you've got one of these RoboMades and did it work reasonably well for you? If you've got a Roomba or other brand, let us know in the comments down below. But yeah, I'm just surprised by the simplicity of it all, really.

**Dave Jones:** But that's all you need I guess. So I hope you enjoyed that more detailed look at that teardown. Thanks very much for Tom for sending that in. If you liked it, please give it a big thumbs up. Catch you next time.
