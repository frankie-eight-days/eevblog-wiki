---
video_id: 1ngqB4mxZOI
title: Smeg Oven Goes Clunkedy Clunk + Capacitor Go Poop
url: https://www.youtube.com/watch?v=1ngqB4mxZOI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 39, "3": 55, "4": 74, "5": 91, "6": 108, "7": 128, "8": 148, "9": 166, "10": 180, "11": 206, "12": 224, "13": 243, "14": 261, "15": 288, "16": 305, "17": 325, "18": 348, "19": 367, "20": 387, "21": 404, "22": 417, "23": 447, "24": 467, "25": 490, "26": 504, "27": 525, "28": 543, "29": 561, "30": 585, "31": 603, "32": 622, "33": 645, "34": 669, "35": 688, "36": 709, "37": 723, "38": 736, "39": 757, "40": 783, "41": 808, "42": 824}
---

**Dave Jones:** Hi, just taking a look at a PCB from a faulty Smeg oven that we've got. It's, I think it's an OPA330X, something like that. So, yeah, this is one of the, well, I guess this is the main control board in the thing, and the symptom is that it's, there's an auto-lock-in mechanism.

**Dave Jones:** It's got like a physical interlock for the front door, so when you're cleaning the thing, it would like automatically lock the door, so you can't open it, because the cleaning mode is really hot, high-intensity, kind of, you know. So it automatically locks it for safety and for the child lock as well.

**Dave Jones:** You can set like a child lock so kids can't open the oven and stuff. And it's got a big physical mechanical army thing. I'll try and insert a photo here. And, yeah, that interlock has failed and it keeps going clunk, clunk, clunk, clunk, clunk, clunk.

**Dave Jones:** Yeah, it just gives an F33, after a minute of going clunk, it gives an F33 error message, and then just doesn't do anything, locks up. So, yes, I've tried turning it off and on again, and that doesn't fix it. The capacitive touch display has, like, once or twice, I think, has actually got,

**Dave Jones:** like, a couple of buttons have actually locked up on it, and just power cycling it fixes that. But power cycling is what caused this issue. Like, it was working fine, and we were trying to fix the button problem, and we power cycled it, and then this interlock thing comes on.

**Dave Jones:** Anyway, really annoying. Now, this board, I believe, has been replaced before. I was not involved in this, Mrs. EEVblog did it, but apparently it went, it released the magic smoke, went kaput when it was in that pyro cleaning mode, that high-temperature pyro cleaning mode.

**Dave Jones:** And there's a big black mark, I'll put a photo here, a big black Ernie Bernie mark, which is actually, it's in this orientation here, and the Ernie Bernie mark is under these relays here. But as you can see, this is not, there's nothing that's burned on here.

**Dave Jones:** It's not caused by this board. So I would presume that this board was swapped in the last repair. And we've had a quote on this thing, and it's like 500 bucks, just for the board, apparently. It's ridiculous. Anyway, I'm going to have a look at this, just have a look at the board,

**Dave Jones:** although I think it's more likely to be a mechanical issue, because once again, I'll put up the photo here of this big interlock motor thing with two microswitches on it, and I can actually see it rotating inside, it seems to be slipping, and like, there's something,

**Dave Jones:** I suspect there could be something wrong with that, but it could be driven by one of these relays, and the wiring inside is quite complicated, couldn't get a service manual for it, really annoying. So yeah, like tracing the thing out is like, meh.

**Dave Jones:** Anyway, can you spot a potential problem here? Not that I think this is causing the problem, probably not, but it indicates a problem. So, yeah, look! Ta-da! Look! The magic fluid has escaped, right? This cap, look! Right, it's right under there, and this cap was actually bent over like that,

**Dave Jones:** so it's actually come out and it's, all the magic fluid has, the magic electrolyte has escaped. It has escaped. And what brand are these? The board's too high, it's not going to focus. Not sure what that is. What's that symbol? I don't know, offhand?

**Dave Jones:** That's not ringing a bell. Anyway, I did measure these caps in circuit, and they seemed okay, even this one actually seemed okay. But, of course, the cap can still read okay, but its ESR has gone through the roof. So, yeah, it's series resistant.

**Dave Jones:** So, anyway, that seems to be that cap, it's directly connected across here, and this, what is this? Let's have a squiz. Now, not that, um, please forgive me, this probably will not be a repair video, this will just be a inspecting the board kind of video.

**Dave Jones:** So, that's some sort of MOSFET-y, switch-y thing. What's an I per, it's an ST, jobby, VI per 22A? Aha! It's a VIPER 22A. Low power offline switch mode primary, primary switcher, there you go. 60 kilohertz switching frequency. So, there you go, it's got a built-in MOSFET.

**Dave Jones:** That's an interesting part, isn't it? Yeah, so it's like a primary side, yeah, primary side switching controller, in this particular case, for a battery charger. Huh, interesting, but, you know, you could use it for a ton of different applications. So, obviously, they're not charging a battery here.

**Dave Jones:** Internal controls, drain, source, right? So, anyway, that cap, so assume that that cap is like C, equivalent to C5 there, which is like the power rail. So, drain at the top, source down there, and VDD. So, if we go back to the videotape here,

**Dave Jones:** yeah, the cap is across the source and VDD there, there you go. So, it's across the rail, but, yeah, I don't, like, I don't see how that's related to driving this interlock mechanism, because the interlock mechanism goes ka-clunk, ka-clunk, ka-clunk, like it's slipping, the cogs are slipping in there,

**Dave Jones:** but whether or not it's got some relay driving, C2 interlock microswitches on the top, and this whole, that whole arm with the with the Teflon thing there, it rotates, and, like, you can't force it. It's really, like, a lot of force on this thing.

**Dave Jones:** I did actually get it just to rotate the once, and now it's, the oven's actually permanently locked. Now the door's locked. So, yeah, it was open before, now it's locked. But, yeah, the magic electrolyte has escaped from there. So, but I suspect that's not related.

**Dave Jones:** I'd actually be quite surprised. But, yeah, without, like, a wiring diagram and tracing this out, I don't know how these, like, because there's lots of, there's just a lot of interconnection wires actually joined onto that motor thing, just that interlock thing, because it's got to,

**Dave Jones:** you know, it's got to disable stuff, it's got to, you know, like, anyway. For those fanboys, here you go, here you go. You want to know what the micro is down here? Of course you do, of course you do. Here you go. The ST fanboys go wild.

**Dave Jones:** So ST72C254. So anyway, all the joints look good. Like, there's nothing, like, there's no, you know, all the relay, relays look really good. Nothing else looks, nothing else looks blown or anything. Now, interestingly, the only connection, the only connection is here. This is the only connection to, well,

**Dave Jones:** apart from all of the, you know, apart from all the relays, the only, like, logic stuff is actually this connection down here, which is interesting. And it's only a four-pin jobby. It looks like this connection over here comes from the micro, one of the micro switches

**Dave Jones:** on that interlock mechanism. Yeah, it's, so that's all, that all looks like it's controlled via the micro. The ST micro is controlling the, oh, look, you can see the dots. The ST micro is actually controlling the, how that interlock works, right? Well, look, you can see the two little dots there.

**Dave Jones:** They put down the glue. That is the glue that holds these components in place when they flip the board upside down and put it through the wave soldering machine. So there you go. So yeah, but once again, you can see that again there.

**Dave Jones:** They put the dots there, but they decide to unpopulate that. But yeah, single-sided boards, single-sided boards. You save cost. Seriously, in appliance manufacture like this, even your, you know, $10,000 plasma TV, you'll still find a single-sided power supply board, for example. And none of that FR4 rubbish, right?

**Dave Jones:** Phenolic base, right? Because they saved, you know, they saved a dollar on the board or whatever. So anyway, yeah, I'm greatly doubting that will fix it by replacing that cap. Anyway, let's suck it and see, actually. We can actually measure that in circuit.

**Dave Jones:** That's a 33 mic. There you go. 27 mic, so it's a bit under. Bit under, but that's in circuit, you know. I did actually measure the other ones. Is this the same? No, this is 22 mic. That's 19 mic. You might actually, you know,

**Dave Jones:** you might recap these as a matter of course. But there's 1,000 mic. Are we going to be able to get that in circuit? Yep. Yeah, that's good enough for Australia. This bad boy's 100 mic. 86. 47 microfarads. Now, of course, you have to suspect caps

**Dave Jones:** because this is literally an oven. I know it's outside the shell, but it gets hot in there, right? So the last thing you... Oh, 4 mic. 4 mic, really? Let's swap the leads. Have I got the right pins? 4 mic. 4 microfarads, really?

**Dave Jones:** Oh yeah, yeah. 4.7, 400 volts. Okay, I didn't know they had mains on there. Okay, there you go. Before I take that out, I'll just mark the negative pin there because this does not have a silkscreen on it. So, yeah, don't want to come a-gutso with that.

**Dave Jones:** There he is. There he is. Can't see anything down in there, but there's no way that you get a stain like that right under your cap without that being the electrolyte. That's 28 microfarads. Dissipation factor of 0.22. Let's put it in ESR mode.

**Dave Jones:** I should measure that at 100 kilohertz, shouldn't we? 0.8 ohms. That actually seems okay. Now, I don't actually have a 33 microfarad 50 volt jobby, so, yeah, I'm going to have to either get one or attempt to scrounge from somewhere. But, yeah, unfortunately,

**Dave Jones:** I don't keep a big stock of electrolytic caps. I should, but, you know, I'm not in the repair business. Anyway, it could be a while until this is back up and running, but, in fact, we've just found a replacement oven, which is cheap.

**Dave Jones:** Like the same oven, which is cheaper than getting a replacement board. But, like I said, I don't think this is going to fix it. I think we have an issue with the motor drive for the interlock on the front panel. Front panel interlock on there.

**Dave Jones:** So, yeah, I think this is just a furphy. I just wanted to show you the PCB. These are interesting, and they've got integral right angle PCB mount spade lugs in there, which then go in. Made in the EU, thank you very much. Finder brand.

**Dave Jones:** Like I said, I don't suspect anything there. Like, you go in, and you could, like, buzz out to make sure, like, at least there are relay contacts there, you know, and stuff like that. But, yeah, like I said, I don't think this boards the issue.

**Dave Jones:** I think it's more likely to be a stuck-duck mechanical problem. And, nope, that didn't fix it. I did find a replacement cap. Slightly higher in value. That's all right. And, no, I'm not sure if you can see that, but down there is that watch.

**Dave Jones:** That cog down in there. Maybe you can see that it's trying to go. See that cog down on the bottom edge and bottom there? It's trying. It's trying its heart out, but it's sort of, like, flickering, stuttering back and forth there. So that, for all the world, to me,

**Dave Jones:** looks like some sort of problem with that mechanism there. That is designed to drive this interlock arm, which has this, you can see there, has this little Teflon spacer on it. And it's doing the auto-lock thing. And, yeah, it's not a happy camper.

**Dave Jones:** Not a happy camper at all. And there we go. And we've got our, oh, was it FO3 or F33 last time? FO3. FO3, there you go. Same fault. So there you go. That didn't fix it. I suspected that cap was, yeah, it was faulty,

**Dave Jones:** should have been replaced, but it wasn't related to that fault. So I don't know. Catch you next time.
