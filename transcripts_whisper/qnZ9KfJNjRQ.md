---
video_id: qnZ9KfJNjRQ
title: EEVblog #1346 - How An Infrared Optical Touch Screen Works
url: https://www.youtube.com/watch?v=qnZ9KfJNjRQ
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 39, "3": 59, "4": 77, "5": 95, "6": 114, "7": 134, "8": 149, "9": 170, "10": 186, "11": 202, "12": 220, "13": 237, "14": 254, "15": 274, "16": 289, "17": 312, "18": 324, "19": 345, "20": 358, "21": 372, "22": 396, "23": 408, "24": 420, "25": 435, "26": 453, "27": 472, "28": 488, "29": 502, "30": 520, "31": 542, "32": 560, "33": 580, "34": 600, "35": 623, "36": 650, "37": 669, "38": 690, "39": 713, "40": 731, "41": 752, "42": 768, "43": 786, "44": 803, "45": 818, "46": 840, "47": 863, "48": 878, "49": 896, "50": 915, "51": 938, "52": 956, "53": 971, "54": 991, "55": 1007, "56": 1024, "57": 1039, "58": 1054, "59": 1070, "60": 1090, "61": 1109, "62": 1125, "63": 1141, "64": 1165, "65": 1178, "66": 1195, "67": 1216, "68": 1234, "69": 1252, "70": 1269, "71": 1286, "72": 1301, "73": 1320, "74": 1337, "75": 1358, "76": 1371, "77": 1388, "78": 1408, "79": 1423, "80": 1438}
---

**Dave Jones:** Hi, it's dumpster teardown time. And if you're not following me on my second channel, EEVblog2, you damn well should be. It's linked up here somewhere. And at the end or down below, if you haven't seen it, this is where I put a lot of my dumpster diving videos and just other miscellaneous videos.

**Dave Jones:** And if you subscribe, you would have seen this the other day. This was a dumpster finder along with an excellent 24-inch Dell monitor as well. This is actually a touchscreen monitor. And you can see that it looks like one of these all-in-one PC things, but it's, you know, it's got this stand which flips out like this.

**Dave Jones:** And that allows it just to give like a, you know, a nice angled surface where you can actually do all touchy-feely stuff. And of course, it plugs into a PC via USB and it just acts as like a Windows touch tablet interface. And a normal HDMI importer screen as well.

**Dave Jones:** But the interesting part about this is that it's none of that capacitive touch rubbish or none of that resistive touch rubbish. This is actually an optical touchscreen. And apparently, I believe, like a lot of people are saying, these are relatively rare. You might find them like industrial applications and things like that.

**Dave Jones:** But in a consumer monitor like this Dell one, fairly rare. So this was a really amazing dumpster find. It's going to be really useful in the lab here. But I thought it'd be interesting to have a teardown of this and see what technology it uses for the optical touch system.

**Dave Jones:** Now, of course, there are basically three or pretty much four kinds of touchscreen displays. You've got your resistive touch, which basically has like two transparent conductive surfaces. And when you actually touch it, it actually forms a resistive path. And then it can figure.

**Dave Jones:** You can figure out the XY location. And they're probably the most common type you'll find. But they have disadvantages in that you can only touch it in one location. So you can't do a gesture, the two-fingered gesture thing, which you can with capacitive touch and with optical touchscreens like this as well.

**Dave Jones:** And, of course, the capacitive touch ones, they've got basically two glass plates on them. And then it detects XY location based on capacitance. And then it can detect the distance of where your finger actually is. And the third one is a bit of a miscule one.

**Dave Jones:** It uses a surface acoustic wave or SOAR screen. So it basically transmits from the side. And it basically, an ultrasonic signal goes across the surface of the screen. And based on where your finger is, it interrupts that. And it can detect it. And I've done like surface acoustic wave video, which I might have to link in.

**Dave Jones:** Because that's like surface acoustic wave delay lines, for example. And that's what I've done. And that's what I've done. And they're quite fascinating. But the other major type is used in a lot of industrial applications. And that is an optical system. So around the edge of this, you're going to, usually they're going to have an infrared.

**Dave Jones:** So you can't see it. They're going to have an infrared transmitter and infrared receiver. And it somehow detects where your finger is. Now, there's actually two, well, at least I know of two ways to actually do this. And this was like used back in the 1980s.

**Dave Jones:** Hewlett-Packard had one of the first touchscreens. Computers back in the world, the HP150, I believe it was, back in the 80s, that used an infrared touch system. It had a bunch of infrared transmitters and like transmitters all down here. Infrared receivers on the other side.

**Dave Jones:** And based on all those, it could detect where your finger interrupts the transmission of the infrared path. Now, unfortunately, you need like for a big, you know, large, like what is this, 22-inch screen? Or something. And you need a decent amount of resolution these days.

**Dave Jones:** Like you have to get, like, if you can see that, that's pretty fine resolution going on there as I move my finger. So you can't really do that with, get that fine resolution with, well, maybe you can. But you'd have to have an awful lot of transmitters and receivers around the edge of this thing

**Dave Jones:** to actually detect where your finger actually is on this thing. So, yeah, that's a bit tricky. And you can see, it can just detect the fine point of my little poker. Here. And really, this does have phenomenal resolution like this. So, yeah, it's, I think something else is going on here.

**Dave Jones:** And one of the other methods I know of that you can actually do this, I still don't know what this monitor uses. It just says it's optical. The other method is to have a optical transmitter and receiver in there. But basically, you only have like a single one or a couple of them.

**Dave Jones:** And the rest, around the outside surface like this, you will have a retro, retro-reflecting surface so that when the infrared lead transmits and it'll bounce back off the retro-reflective surface. Because retro-reflective, it doesn't matter which angle you come in at. If you come in at this angle like that, it'll actually reflect it exactly back at the same angle.

**Dave Jones:** And, of course, this is what they famously used to measure the distance to the moon. The Apollo 11 mission, they left a retro-reflector on the moon. And it doesn't matter which angle you shoot the laser at it from, it comes back. And this is what they use.

**Dave Jones:** It's kind of like safety vests and, you know, signs at night and things like that. So, I suspect that's what might be happening here is this around the outside might be a retro-reflective surface. And they might just use, just use triangulation to try and figure out where your finger or fingers is in this particular case.

**Dave Jones:** You know, we've got two fingers here. And, of course, if I just do a single finger, it's not going to do anything. But I use two and it's going to do that. So, obviously, it's capable of... Getting both in the location of both fingers like that.

**Dave Jones:** So, and if we have a look in here and zoom right in, you can see that it's really quite thick, this bezel. It's six or seven millimeters, something like that in there. So, they've got some sort of thing around and goes right around the edge of this thing.

**Dave Jones:** So, anyway, this could be really interesting. Let's tear this puppy down and see how, in this particular case, an optical touchscreen works. You don't often see these puppies, especially on consumer products. Because they're more, like, industrial. They're very good for, like, you know, out on a big kiosk, consumer kiosk out in the wild or something like that.

**Dave Jones:** And, you know, you can use them with gloves and all sorts of, you know, things like that. So, unfortunately, the optical ones, they can actually get, like, dirt. If they get dirt around the outside and things like that, you have to clean it.

**Dave Jones:** Maybe that's why somebody dumped it. It just, touchscreen wasn't working anymore. Didn't, they didn't know how it works. So, they probably... When I got it, it was filled up with a ton of gunk in there. So, I just got an isopropyl wipe and just wiped around there.

**Dave Jones:** Or do it with a cotton bud or whatever and Bob's your uncle. And I thought I might be able to see something on the camcorder. Some sort of infrared transmitter. That's a LED up there. Don't worry about that. But, no, I can't see anything.

**Dave Jones:** Nope. I'm going to have to tear it apart. But it's got to be infrared. Model number for those playing along at home. E-C. Alright, getting this apart can be a bit tricky. There were three screws there. But apart from that, they're the only screws I could find on this thing.

**Dave Jones:** So, I obviously got around here and I was able to get that off. So, I'm hoping that the whole, this whole top bezel will just come off. And we might be able to see something interesting already. This is really quite tricky business. I really hate these things that are all just put together with plastic clips.

**Dave Jones:** Damn it. Yeah, look. Two plastic clips down there and it's going to be all the way around. Ugh. Ugh. No. It's all integrated into the frame. Get the whole screen out and then get the frame out. There you go. It's really solid. I like the...

**Dave Jones:** Wow, look at the spring mechanism for that stand at the back. That's really quite something. That's really beefy. But, you know, it needs to be. It needs to take a fair bit of abuse as a touch screen because, you know, you get frustrated.

**Dave Jones:** Damn it. I've got some tape holding this together. And it's an extra screw under here, which is ridiculous. I don't know what they were smoking there. Why couldn't they just have left a little cutout in there like that? I don't know. It's dumb.

**Dave Jones:** But non-symmetrical. I hate non-symmetry in design. Our T-Con driver board. So, that's for the LCD, of course. Made in Korea. Hello to all my Korean viewers. So, yeah. Dell monitors. Well, at least this one. LG display. So, that's clearly our backlight driver. You know, cold cathode backlight on the thing.

**Dave Jones:** That's got nothing to do with the optical touch. So, we've got to look further. Got another ribbon cable going off there. These are definitely all LCD flat flex connections. Got another one going off there and another one going off there. So, maybe that's where it's doing the business.

**Dave Jones:** And for those playing along at home, this was first released. In December 2011. So, it's not new. Top right corner. And there's two there. I reckon one is a transmitter. One is a receiver. And if we go over to the other top corner up here.

**Dave Jones:** Got to get the right angle to see it. There it is. It's the same thing. But the other corners down the bottom here, I'm not seeing the dual windows. So, I reckon. That's just some retro-reflective tape there in the corner. If I hold my hand over here.

**Dave Jones:** You can see it's actually reflecting on my hand. This surface along the edge is actually reflective. So, it doesn't appear to be a retro-reflectus. And of course, that now makes total sense with these flat flex here. This is the corner that has that dual element.

**Dave Jones:** Sensor. There's that little flat flex going off there. And same in the other corner down here. Although, not sure what that one's doing. And that's it there. Little six-pin SOT23. Requires delicate removal of the outer frame here. This is an IPS display as well for those playing along at home.

**Dave Jones:** Frame separated from the panel. So the panel's just all the basic column drivers there. Chip on board. I can show you a bit closer. There's our row drivers. So that's all, you know, that's your standard monitor. But what adds the touch magic is the outer frame.

**Dave Jones:** Somebody has individually tested that. And as you can see, there's nothing in it. Except, aha, they got the one. Hopefully, that shows up. It's got like the two splits. It surfaces, as we've seen. The other one down in this corner, it's got the same.

**Dave Jones:** And the one in this corner has got the same. But this one down here has nothing. So that's interesting. I expected either four or two. I didn't expect three, hmm. There you have it. All three sensors do look identical. So are they, as I said, a transmitter

**Dave Jones:** and a receiver, or is one like a transmitter? And the other's a CMOS line camera or something? I don't know. All right, let's have a look at this thing under the Togano, shall we? And zoom right in. Oh, I love this. Beautiful. Oh, look at that.

**Dave Jones:** There's two distinct elements down there. They're different shapes, different sizes. That's really interesting. Can we-- they are certainly very different beasts. So there you go. So I'd say one's a transmitter, and one's a-- oh, see, look. Look, you can see the pattern. That looks retro-reflective to me.

**Dave Jones:** Yep. Bingo. We got you. A bit crusty burger down there, but there's the other end. That's the one that doesn't have anything going to it. There's another one. I think you're going to find that they're all identical. I still can't get back to that retro-reflective.

**Dave Jones:** Oh, yeah, there it is. There it is. I reckon that's a retro-reflective surface. See the individual elements in there. Just need to get that at the right angle. So the laser that was bouncing off, just the sort of semi-reflective outer part of that.

**Dave Jones:** Gee, you get all sorts of problems when you try and view a frame like this. This is just insane. So yeah, short of getting those outer there, which is probably going to destroy the functionality of this thing-- and I don't want to do it, because it's a working frame.

**Dave Jones:** I don't want to upset the alignment. The corner piece there looks like it's glued onto the two side pieces, and then the sensor is sort of stuck on top of that with the flat flex. There we go. Two, four, six, eight, nine. So nine conductors.

**Dave Jones:** None are bigger than the other. That is identical for one in each corner. Three of them, not four. Weird. There's the main processor board. Didn't expect to find anything interesting on there. There's the main chip that goes to the panel down there, and of course, these touch sensors

**Dave Jones:** are connected through to that panel via those little six-pin SOT23 chips. So that's really the only interface there. So really, there's no clue how that works, really. So meh. All right. Let's get the scope out. Let's probe some signals. I had to put it basically all back together, including the front panel.

**Dave Jones:** I've got to like switch it on and stuff, and I've hooked it up to the PC at the back there, and I had to because I was getting no signals out of this thing unless I actually hooked up the USB. So that seems to enable the touchscreen.

**Dave Jones:** So it's got to do the USB enumeration and all that sort of jazz. Anyway, let's probe a signal here. Yes, it is mains earth reference. It makes no difference whether I go to signal ground or here, the signal integrity. I haven't probed all the signals yet, but there is one.

**Dave Jones:** Let's check. We're 500 millivolts per division. So let's look at that. We have a sync pulse here. You can see that that's some sort of synchronization pulse. That doesn't change at all with my finger on the touchscreen. But this other one, there are test pads for these.

**Dave Jones:** And here it is. It looks very much like an analog video signal. If I move my finger, look at that. It changes. So I'm moving my finger vertically along the screen. So that axis, that, there you go, it depends on the location. It's changing this analog signal like this.

**Dave Jones:** Why it's like messy like that, why it's got a big dip in there, I don't know. But it is certainly an analog system. X direction, then it does that too, but only because like it doesn't go. All the way. It's limited range. So it's in view of the sensor.

**Dave Jones:** So that is some sort of analog image sensor. Like you know, as I said before, like a probably like a single line thing. It's not like you're a proper, you know, it's not like a 640 by 480 little CMOS camera or something like that.

**Dave Jones:** I think it's just a single line jobby. And if I probe the other one here, we've got, there's three signals here. We've got our trigger signal, which doesn't change at all. Our video signal. Now once again, I'll go vertical, and that's changing. It looks like the same signal really, doesn't it?

**Dave Jones:** Well, I can store that. All right, I've set that as a reference waveform. I've done a complete video on this, which actually got bugger all views. Well, for my channel, it had like 24,000 views or something. Come on, I'll link it in. Anyway, I've saved that as a reference waveform.

**Dave Jones:** So that's that second channel. Let's go back to the original channel we looked at. There you go. Neither. They are, look, it's almost, it's kind of opposite, isn't it? It's kind of got like an opposite peak there. But yeah, so different orientations. There you go.

**Dave Jones:** So I superimpose it over the reference waveform. And if I put a fatter finger in there, let's say the tip of my pinky like that, it's really narrow. And if I don't touch it, I'm not touching the screen. You notice it just dips down a little bit there.

**Dave Jones:** But if I touch it like that, and then if I roll my finger like that, to give a bigger footprint, and if I put my whole hand on there. Wow, look at that. I can block out the whole sensor. So if I actually block out the sensor, there it is.

**Dave Jones:** I mean, it's basically Gonski. I'm covering the entire sensor there. Do that again. There you go. I'm covering that whole sensor. You might be able to see the PC moving up there as I do the touch. But yeah, it's definitely an analog image sensor.

**Dave Jones:** And if we zoom out, there is nothing else there. It's just continually repeating that image pattern. Cool, huh? But wait, there's one more signal here, which I didn't see on the other one. That one, that looks like a clockety-doodah. There we go, that's a 100 kilohertz clock.

**Dave Jones:** Ah, that's interesting. I expected it to be significantly higher than that, but there you go. So there it seems to be, once again, that won't change with my finger. There's 100, you can see the screen in the background. They're scrolling. So obviously, those things, signals are going back over the main connection here.

**Dave Jones:** And presumably, back into the main processor there, cuz there doesn't seem to be anything else on here. There's a couple of other chippies, but they go off to the LCD here. All right, so I'll attempt to explain what I think's happening here. I'll probe this sensor down in this corner here.

**Dave Jones:** So we'll get that. We'll stop that. Okay, so what we got here, obviously, this is like one continuous line scale. We've got the scan of the sensor. And the reason that we're getting this waveform, just ignore the beginning. I might be able to explain the beginning, perhaps.

**Dave Jones:** Anyway, right, our sensor's in this corner here. So let's say that this start point is the first line on this sensor. What it's doing is the reason that this slopes down like this is because the attenuation of the signal coming back. So there's the lead emitter here.

**Dave Jones:** I still don't know if they multiplex the lead emitters. I don't think so. I think they just flood fill it all, and they're just looking for the detection shadows, basically. Believe that's all they're doing. So if you've got your sensor over here like this, okay?

**Dave Jones:** So let's say your infrared LED is shooting out. It's bouncing back off that retro reflector like this, okay? It's a relatively short path here, isn't it, right? So this is gonna be this bit here, and then at some point, it's gonna start attenuating cuz it's getting further and

**Dave Jones:** further away until it's bouncing right off the opposite corner over there, which would have to be that. And then it would start, then the leads are like pointing, let's just say, right? They don't actually, leads don't actually scan like this, but just like for the sake of argument, like the beam angle, right?

**Dave Jones:** Where as it gets towards here, then it ramps back up because it's a shorter path in here, and that corner, and here, and here. So it's bouncing back off that far wall over there, right back to this sensor. And that's why we saw the two waveforms swapped over,

**Dave Jones:** in terms of their bottom peak here, when we switch from this sensor, measuring this one, to this one over here. Because they're physically different orientations, but they're gonna have the same effective pattern, but sort of like a mirror image, based on the geometry.

**Dave Jones:** Cool. Actually, this is interesting, I'm pairing a test point called power, lead power. So I think what's happening here is a negative on here is actually the lead turning on. So the lead is on for all of that period, and then when it goes high,

**Dave Jones:** it actually is the lead switching off. So that makes sense. I don't know why you wouldn't leave it on all the time, but maybe they're, I don't know, they're doing some little magic in there. And for those who wanna see the circuitry, the signals I was probing here, that one was the video signal.

**Dave Jones:** That one was the sync, and that one was the 100 kilohertz clock. They're just three series jumpers there. So yeah, I was able to measure those. And it's the same over here, they've got test points. That was the video test point, and this was the sync test point.

**Dave Jones:** Okay, so what I'm gonna do now is I'm probing this sensor down in this bottom corner. So if my theory's correct, the bottom of that, or the bottom peak here, should be this corner over here. So I'm gonna stick my finger in there, and yep, wiggle, wiggle.

**Dave Jones:** See the little wiggle, wiggle, yeah? And if I get closer, well, if I go like that, there you go. It changes around that point. So my theory was correct, that this sensor, of course, if I put my finger right across there like that, goes all the way up.

**Dave Jones:** And yeah, slightly changed, just look at that little tiny, tiny point there. So there you go, theory correct. So that goes to show that the odd wave shape we've got here is just the non-linearity in the attenuation of the reflections across the screen for the particular sensor.

**Dave Jones:** In this case, this one down here. But it's the same if you've got this one up here or this one up here. You're gonna see a similar waveform. So if we were probing this one up here, then the space would've, it might be over here.

**Dave Jones:** And then that one would dip if I put my finger right in that corner. So, there you go, that proves the theory. It's not too hard to figure out when you just start probing around. So there you go, that's absolutely fascinating. I never looked at these optical screens before.

**Dave Jones:** And it looks like they use an optical image sensor, a line-based one, cuz you wouldn't need anything otherwise. And it gets like an analog signal out, and they use three of them. Now, I do believe you can probably do this with just two sensors on the top side.

**Dave Jones:** But they've obviously decided that they need three for better resolution or whatever. I don't know, I haven't really given it much thought. But if you're in the know about how they actually process this, or you've got a link to a data sheet or a paper or

**Dave Jones:** whatever it is, how they actually do this, please leave it in the comments down below. So I hope you found that as interesting as I did. Please did. Please give it a big thumbs up. As always, discuss down below and check out all my alternative platforms.

**Dave Jones:** Catch you next time. Thank you.
