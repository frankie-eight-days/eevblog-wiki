---
video_id: TRy755StMak
title: EEVblog #369 - Rigol DS2000 Oscilloscope Playing Around
url: https://www.youtube.com/watch?v=TRy755StMak
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 34, "3": 47, "4": 61, "5": 76, "6": 95, "7": 109, "8": 126, "9": 145, "10": 160, "11": 176, "12": 189, "13": 202, "14": 225, "15": 242, "16": 261, "17": 281, "18": 295, "19": 308, "20": 322, "21": 340, "22": 362, "23": 379, "24": 392, "25": 410, "26": 426, "27": 441, "28": 456, "29": 471, "30": 488, "31": 508, "32": 527, "33": 546, "34": 568, "35": 582, "36": 598, "37": 616, "38": 632, "39": 646, "40": 663, "41": 679, "42": 693, "43": 706, "44": 720, "45": 732, "46": 747, "47": 765, "48": 782, "49": 795, "50": 808, "51": 823, "52": 837, "53": 850, "54": 862, "55": 879, "56": 894, "57": 906, "58": 923, "59": 935, "60": 955, "61": 969, "62": 987, "63": 1001, "64": 1016, "65": 1032, "66": 1050, "67": 1060, "68": 1076, "69": 1088, "70": 1105, "71": 1121, "72": 1142, "73": 1159, "74": 1182, "75": 1200, "76": 1213, "77": 1229, "78": 1243, "79": 1260, "80": 1274, "81": 1289, "82": 1310, "83": 1330, "84": 1350, "85": 1369, "86": 1389, "87": 1402, "88": 1414, "89": 1431, "90": 1446, "91": 1467, "92": 1482, "93": 1506, "94": 1530, "95": 1542, "96": 1555, "97": 1574, "98": 1588, "99": 1606, "100": 1619, "101": 1630, "102": 1644, "103": 1657, "104": 1677, "105": 1692, "106": 1707, "107": 1721, "108": 1739, "109": 1754}
---

**Dave Jones:** Hi, I thought I'd do a quick video just updating the firmware on my Rigol DS 2000 scope. This is the DS 2202, the 200 MHz model and we've got brand new firmware courtesy of John South at Imona. Thanks

**Dave Jones:** John. Apparently fixes some bugs and issues as well as a pretty major oversight, not a huge deal but bit of an oversight on the they swapped the X and Y uh channels on the XY mode. Um so channel one is Y and channel two is X

**Dave Jones:** which is opposite to what the norm is even though they're not actually labeled down there X and Y but still ah, let's um give it a go. So we'll power it on here and did I get it? No.

**Dave Jones:** Ah, that's a bit annoying. It didn't register that first press. Got to press it a bit harder than usual and it'll take its time to boot up. Um I'm not using my lapel mic today. I it ran out of battery and I

**Dave Jones:** don't have a spare one so I'm actually trying out the automatic uh uh well I'm using the internal mic on my Canon HFG10 here and I'm trying out the automatic gain. So I hope this works. Bit of an experiment here. I won't know

**Dave Jones:** until I read it back. So apparently there are two ways to update new firmware on this Rigol scope and depends if you've either got the full licenses or the trial licenses cuz apparently when you buy this puppy it comes pre-installed with the trial

**Dave Jones:** licenses for everything like the serial decoding and all that sort of and the extra big memory and all that sort of stuff. So which is a clever thing on Rigol's part because it sort of sucks you into getting used to having that real big

**Dave Jones:** memory and the serial decode. So they're hoping that you'll pony up and actually buy the uh, option for it. Anyway, so apparently it's different if you've got the, um, full version of the license, you just power it up like this, you put in the

**Dave Jones:** stick, you go into utility and options, and you just update the firmware as normal, which was what we'll do cuz I'm pretty sure if we go into utility, where is it? Options, utility, system, is there another menu there? Options, and then installed

**Dave Jones:** we can official version. So, yeah, I've got the official version. Apparently it says it'll it won't have the if you've only got the trial licenses it won't say official version, it'll say trial licenses or something like that. These are all the licenses by the way.

**Dave Jones:** There they all are. There are There's There's run all the trigger stuff, the decodes, and the memory depth. Now, unfortunately you cannot actually upgrade the bandwidth on these things as just a software option. You've got to do that when you buy it, which is

**Dave Jones:** a pretty big oversight I think on the part of Rigol. I'm not sure why they did that, maybe they will in the future. I'm not, I'm not entirely sure, but anyway, these are the options available and looks like

**Dave Jones:** my one's fully kitted out. So, we can update the firmware in that, but apparently if you don't have that, you turn it off, and if you got the trial licenses to update the firmware and keep your trial licenses, apparently turn on

**Dave Jones:** the unit and at the same time press the help button. Okay, I'm pressing the help button. And apparently something blinks at you or something. I assume I'll keep holding down the help button. So, let's and see single button is lit. No.

**Dave Jones:** Single button is supposed to be lit up there. No, no, I got some instructions that that was the case. Anyway, it doesn't look to be the case. Oh, well. So, let's just check out this XY swapped mode thing cuz it's rather

**Dave Jones:** hilarious, really. We're in YT mode at the moment and there's roll, of course. There's your traditional roll mode and we've got Oh. XY mode. Let's go in there and let's adjust the um channel one here, which is usually um

**Dave Jones:** you know, sort of by sort of de facto standard the X axis input. So, we expect it to move X. Oops. Oops. It's moving up and down. So, it is certainly Y and there you go. Channel two there is

**Dave Jones:** X. So, yep, they've kind of give that up. Um and there's no like label or anything on there though to tell you Maybe it is in the manual. I haven't actually looked um in the manual. So, uh but there's

**Dave Jones:** nothing Usually there's like an XY there to tell you which channel is what. So, that's maybe a bit of an oversight on the uh design of the front panel really. But anyway, let's update the firmware. Got it uh

**Dave Jones:** the I'm not sure what version it is. So, let's go in and check what version. I'm pretty pretty sure it's like 1.0. So, system system info. There we go. We are hardware version Sorry, hardware version. That'd be like

**Dave Jones:** the FPGA version I would assume. So, the hardware because you've seen if you've looked at the teardown, you've seen the multiple FPGAs in here. So, they're obviously 1.0 and the software itself is 00.00.01. So, there you go. That's uh

**Dave Jones:** pretty fresh. Do you trust it? I don't know. Anyway, let's go. Let's go into utility. So, the instructions are uh USB stick and insert insert USB stick. There we go. We have inserted There you go. It's automatically detected the firmware. It's

**Dave Jones:** automatically detected that I've got 1. uh Sorry, DSP. Okay, so it's only updating the DSP, i.e. the actual firmware itself. That's that Blackfin DSP processor in there. So, it's looks like it's not going to update the FPGAs at

**Dave Jones:** all cuz I've only got one file on the disk there and it's going to update it to 1.00. Well, it's now I've got 01, whereas before it was 00. So, well, maybe it No, maybe it skipped that. Maybe it skipped

**Dave Jones:** 01 at the start and only said 00 01. I don't know. Anyway, never confirm update. So, how do we confirm it? Okay. Let's give it a go. Fingers crossed.

**Dave Jones:** It's uploading. Anyway, I'm using the automatic gain on my mic here. So, I'm standing like maybe six five six inches away from the mic on the top and I'm not talking even if I start whispering now. I can Looking at my VU

**Dave Jones:** meter and my VU meter is almost like minus one minus two dB. It's really up there. Then if I talk loudly, it should not peak. I don't actually see it go into the red. So, I'm talking louder louder louder and if I walk away from

**Dave Jones:** the mic, I'm about a meter away now and now I'm about two meters away. You'll probably hear some echo because I'm in the lab here, of course, and I'm at my teardown bench. I'll walk over here close further away couple of meters,

**Dave Jones:** maybe three meters away at the moment and it should auto gain my voice. So, if this actually works, um, so it it's it might have a compressor and a limiter as well. It seems to have some sort of limiter to limit any, you know,

**Dave Jones:** if I speak loudly, like that, or if I speak softly, like this, at the same distance, it'll have a compressor and a limiter, perhaps working in combination or something like that. Um, anyway, I'll give it a go. Let me know how this

**Dave Jones:** sounds. Oh, no. There we go. No, it is updating the FPGA configuration. Go figure. So, we'll see if that, uh, hardware version is changed. So, I'll come back when it's all done. All right, it's booted up, and look, it's swapped them.

**Dave Jones:** Two is now on the Let's go out here. I bet that's, uh, I can clearly see that that's, uh, changed. We've got channel two here is Y, and channel one is X. Oops. Anyway, it's fixed, so let's go

**Dave Jones:** into utility, and, uh, system, and system info, and what have I got? There you go, it's still saying hardware version 1.0. So, even though it was updating that, um, said it was updating the FPGA configuration, um, it's, well, yeah, it, uh, still

**Dave Jones:** saying 1.0, but software version is now 01.01 SP 9. There you go. So, that was no problem whatsoever. No issues at all updating the firmware. Pretty darn happy with that. So, let's, uh, switch it back to Hey, there we go. It's, uh, showing some

**Dave Jones:** It wasn't doing that before. Anyway, oh, we're on the Well, we are on 500 microvolts per division for the, uh, second channel there. There we go. So, yeah, if um, you Let's have a look at that, actually. Let's go all the way

**Dave Jones:** down. Some people have asked to see the noise floor on this thing. Well, let's let's go out of roll mode, shall we? Up. Let's go into YT mode again, and this is the noise floor, cuz one of the big

**Dave Jones:** features of this Rigol scope is the 500 microvolts per division. And it's, you know, it's very impressive. I mean, I I had a look at the Tektronix 2225 analog oscilloscope, which I've shown in a video or two, and it's got

**Dave Jones:** 500 microvolts per division, but I think since that day, like, you know, I don't know any scope in the last like 15 years that's had 500 microvolts per division vertical scale. So, anyway, that's 5 mV because it's set to uh

**Dave Jones:** times 10 there. That's one of the more unfortunate things about the scope is it doesn't have auto probe attenuation detection. So, you've got to actually go in there and and set that, and it's got a It's got quite extensive

**Dave Jones:** Oh, the values are wrong wrong knob. We can go times 1,000 down to 0.01. So, we'll It's a bit touchy. Times one. So, we'll lock that in, and we're 500 microvolts per division there, and that's the noise we're getting with

**Dave Jones:** full bandwidth, okay? So, that's at Where's the horizontal? 10 microseconds per division. So, let's take it right down. Let's go down to 2 nanoseconds per division, which is the fastest, and it looks like we're in dot mode there.

**Dave Jones:** So, let me go into maybe display. Yeah, dots. There we go. Let's change it to vectors. There we go. That's better. And and we've got our persistence time. Waveform intensity is only 50% at the moment, so we can turn our waveform

**Dave Jones:** intensity all the way up. Or we can turn it all the way back down. That's nice. It'll be nice to get like a real signal on there, like a video signal or something there that we can have a look at, but you know, I I

**Dave Jones:** normally, you know, as a rule, maybe leave it around 80% or something like that. I find that works pretty well. The display brightness here, um Oh, no, that's the No, that's the brightness of the graticule. There There we go.

**Dave Jones:** There we go. That's the grid in the background. And you can have different types, too. You can just have the crosshairs like that. In fact, I'll turn the brightness up so you can actually see that. There we go.

**Dave Jones:** And uh or you can have nothing. You can turn off the grid. So, there we go. I like my traditional grid there. A bit low. Probably doesn't show up that great on camera here because of the bright lights. By the way, this screen

**Dave Jones:** is uh not the best at looking directly on. Now, that's probably directly on. You can see some glare from the lights there, but if I look at it directly on, it's pretty washed out. It's really designed to be viewed at

**Dave Jones:** an angle coming down like that. So, the screen Um yeah, that's a bit bit of a limitation of the screen on this thing. So, it's not the best, um but still, anyway, uh menu display is infinite where it gets rid of the menu,

**Dave Jones:** stuff like that. Uh this isn't a review. This is just having a little play around with it here. And uh So, what we're going to do? Yes, we're going to look at the uh noise floor. Now, when I first got this thing, I took it

**Dave Jones:** out of the box, and the first thing I did, of course, is check this 500 microvolts per division. And that's pretty darn acceptable noise at the full 200 MHz bandwidth. That's only a division or so there, you know, it's not

**Dave Jones:** uh it's not it's not huge at all. Oops. Accidentally That's another thing. One of the These buttons up here, they're a little bit annoying because they're up here and often I'll put my hand like on the scope here when I'm just I don't

**Dave Jones:** know talking or thinking about something or doing something and I'm always accidentally hitting these buttons, which is really kind of annoying. I really do like the look of them there, but from a practical aspect point of view, that is just like I've I've done

**Dave Jones:** it ti- almost every time I use this scope. I've naturally put my hand there on the corner of the scope like that and I'm I'm I'm stop and turn to single shot mode all the time. It's really rather

**Dave Jones:** annoying. Ah, boy. Anyway, the first time I got this scope turned it on and wanted to check out the 500 microvolts per division and there was quite an offset. There was a couple of divisions offset or three divisions or four divisions

**Dave Jones:** offset or something. It was quite large. Um, so the DC offset by default from the factory out of the box seemed to be really quite large, but then I ran the calibration function, which is in here somewhere. I won't go through it now cuz

**Dave Jones:** it does take some time, but I ran the uh Oh, I No. Okay, so I won't go through it, but I ran the self cal and it got rid of the DC offset there. And so we'll exit that and as you can see

**Dave Jones:** that one's sort of spot on the center and that one's sort of lifted up a little bit from the center there, but not a not a huge deal. Of course, this will vary with temperature and you know, time and all sorts of stuff. So if

**Dave Jones:** you're really working at down at that 500 microvolt run your self cal every now and then, I think. So it'd be interesting to test that over temperature, actually. To sort of cool this thing down, sort of put it in the thermal chamber. Although,

**Dave Jones:** my thermal chamber's not uh uh uh capable of uh cooling down uh the scope at the when it's operational, but I could cool it down and then maybe power it up and see if that changes. I won't do that for this

**Dave Jones:** video, um but it could be interesting. Anyway, that's uh 500 microvolts per division, and the screen is quite nice, by the way. It would this large wide screen, and you'll notice it's got 1 2 3 4 5 6 7. It's got 14 divisions

**Dave Jones:** across the screen. You may not see that there. That's quite unusual, but that's what you get with these wide screen um scopes. They've gone the way of video, you know, they've gone with 16:9 wide screen video. We're getting wide screen

**Dave Jones:** oscilloscopes now. Go figure. But, that is the noise floor. So, that's the noise floor over right down at the lowest value. And I've got nothing connected to the input, and that's down at, you know, 1 ms per division. So, that's that's

**Dave Jones:** pretty darn good, but if we turn our input bandwidth limit on, we've actually got a 100 meg and 20 meg options there. So, if we uh choose 20 meg, oh, you can see it's instantly dropped. There you go.

**Dave Jones:** You don't even have to accept that figure for it to jump into that mode. So, there you go. At 100 meg, you can see the difference in the noise floor, because, of course, the noise floor is go- going to be dependent upon the

**Dave Jones:** bandwidth. The higher the bandwidth of the oscilloscope, the uh higher the residual noise floor. That's just the way it works, but there you go. So, that's pretty good. If you put on 20 meg bandwidth limit, that noise floor is under

**Dave Jones:** a division there with a floating input. Pretty darn impressive. I really like it. Now, there's another thing that I really find annoying on this scope, and that's the status LEDs on the buttons down there. Check it out, right? There That's it There's actually

**Dave Jones:** an LED in there. You can see it if I shadow it like that. You can see it, but you know, it's really washed out to the point where that's not just a camera That's not just an on trick camera there

**Dave Jones:** with the light. I can barely see that with my eyes. It's just But, turn it off. Boom. You know, it it really is quite terrible. And channel two's on there, but you wouldn't know it. It's so dim. And a similar sort of thing, and

**Dave Jones:** you know, it's a little bit better on the run stop button there. The The The red's all right, but the green is just really washed out and horrible to look at. So, they really need to, I think, up

**Dave Jones:** uh the current on those LEDs because it's really not acceptable at all. Now, one of the really nice features of this scope, which I really love, is this waveform uh preview of this waveform capture and playback feature that

**Dave Jones:** they've got here. This big knob over here, you know, a lovely springy sort of knob, and they've got a record. So, here it is. They've got a record button there, and uh they've got a play pause button, and a stop button. And it

**Dave Jones:** basically allows you to capture and replay all of your waveforms on the fly. So, at the moment, let me demonstrate. We're 5 ms per division here. So, 5 ms per division, and we're at 100 megasamples per second, and we're capturing 7

**Dave Jones:** megapoints of We're going to use 7 megapoints of memory there. Now, that 7 megapoint points is important because this scope has a maximum of well, with the extended option that I've got 56 meg of memory. So, why is it only using 7

**Dave Jones:** meg points? Aha, it's doing that because when you turn on the product Sorry, the waveform replay function over here, it will actually capture 7 meg lots of the waveform. So, you know how scopes have the waveform update rate, you know, a million waveforms per

**Dave Jones:** second. 50 This one has 50,000 maximum or you know, a real cheap Rigol 1000 series might have 7 800 waveforms per second. This will capture a complete snapshot of those 7 meg points to fill up that 56 meg point memory. So, let me

**Dave Jones:** demonstrate. What I'll do is I'll tap like I'll just get some 50 hertz here. Okay, I'll just sort of play around with this. So, what I'll do is I'll capture this. I'll press record here and while it's updating that, instead of

**Dave Jones:** losing all that data once it's popped up on the screen, bang, it's vanished and lost, it'll automatically capture that and we can replay it. So, it'll capture about seven or eight complete snapshots of waveform there in the 56 meg of

**Dave Jones:** memory. So, let me turn it on. Here we go. Record and it's recording. You can see it's counting up. Ah, see, it recorded seven snapshots of the 7 meg point memory. Now, what we can do is use this

**Dave Jones:** knob here. We can either use the springy one that it will replay all of those waveforms or the center one just allows you to scroll through one by one and you can see that it's captured each waveform like that. Brilliant and

**Dave Jones:** it's captured the 7 meg points. So, then we can zoom Hang on, how do we zoom into it? No, we can't do it with the horizontal. We've got to zoom in with Ah, no, we've got to use the dual

**Dave Jones:** waveform, do we? No. Ah, no, fail. This is the first time I've actually tried to zoom in on the waveform. I thought I'd been thought I'd been smart there. Hang on, there should be a way to zoom in

**Dave Jones:** on that sucker. That's center position. That's dual time base, the dual waveform view. Ah, there we go, it just didn't update. Okay, is that a firmware? That could be like a firmware issue or something. So, there's something going on there.

**Dave Jones:** So, if we scroll through, no, it's not it's not updating. It's not updating this waveform. Look, that window's moving over there. What's going on here? No, see, we should be able to see the kink in that waveform. So, it's not

**Dave Jones:** Ah, I was getting all excited over this feature and I'm not sure what's going on there. That There we go, it's updated. Now, it's updated the screen. So, there seems to be a screen update issue here. It doesn't update when you scroll

**Dave Jones:** that along. That's really That's really rather dodgy. Anyway, I do like the capability itself because it allows you to Let's go out of dual time base. You just See? And then it The waveform has vanished here. And it'll come back. It's still in

**Dave Jones:** memory. We can still look at it. But, it doesn't update. So, there's Oh, there's some There's still a firmware issues there. Wow, I just discovered that. There you go, When you start trying out playing around with stuff like this, this is what you find.

**Dave Jones:** That's I don't think it's supposed to work like that. That That just is counterintuitive. It It should update the screen as you go into dual time base. You hit the center. I love all these buttons are pushable, of course.

**Dave Jones:** And you can go into the dual time base. It adjusts it. There's the little display window, but there's no waveform until I update that. Give me a break.

**Dave Jones:** Anyway, there, what I wanted to show was that this waveform capture feature, I'm not actually sure what it's called. Um that it at it relies upon how many waveforms it captures relies upon the memory depth and the horizontal time base that you've

**Dave Jones:** currently got it set to. Now, I've got this now set to very fast. It's set to 50 ns per division there. And you can see we're only going to capture 700 points. And that's will double if we turn off channel two there. Bang, we can

**Dave Jones:** get 1.4 K points, okay? So, but let's turn channel two back on. So, it'll capture both of these channels 700 points. It'll capture Well, let's let's get the calculator out here. What's 56 56 meg divided by um 700 point Actually, it'll be 1.4 K

**Dave Jones:** points, will it? 1,400 points. It'll capture maybe 40,000 waveforms or something. So, let's once again, this is a real dicky way to test this. I should test it properly, but it'll allow us to do it. And you'll I'll

**Dave Jones:** turn on the recording function now, and you'll see it. It should count It should capture like 40,000 waveforms. Let's do it. Boom, there it goes. It's counting up. 20,000. 30,000. 40,000 waveforms, 45, 50,000. Woah! 60,000 waveforms. Brilliant. There we

**Dave Jones:** go, 65,000 waveforms it's recorded. There you go, you probably can't see that. There we go, you can see it now. So, it's recorded 65,000 waveforms, which now you can see why you need this uh uh replay ring here. Now, you can see it like it's

**Dave Jones:** scrolling through, okay? So, you can see I'm just sort of touching that ring and and you can sort of go through slowly, like I'm counting down maybe three per second there. Or if I move tweak it a little bit more, hold my tongue at the

**Dave Jones:** right angle, it's doing maybe 20 a second. Or then you can go to 100, you know, add more springiness in there. And you can see in real time what I was touching. See? You can see the real time

**Dave Jones:** of how I was touching that probe. And it's great. And if I turn it all the way to max, look at that, it's counting down 40 40,000. 35,000, 30,000. And it replays all of those waveforms that And bang, we've gone down to caption

**Dave Jones:** number one. And of course, if you want to scroll through one by one, you can use the center knob there. But there you go. That's It's an absolute brilliant feature. Parameters over range. I look You get this message for a lot of stuff.

**Dave Jones:** Parameters over range. Crazy. What does that mean? Ridiculous error message. Pointless. Just scares people. Geez, oh no, my parameters have over ranged. What does that mean? Panic, panic, quick. My scope's buggered. Hopeless. I don't know. Anyway, so it's

**Dave Jones:** got a few quirks this thing, but that is an incredibly powerful waveform capture and replay function. I really like it. It takes up a hell of a lot of space on the front panel there. I would have preferred to have a nice big that is the

**Dave Jones:** nice big horizontal knob over here. Instead, the horizontal knob is the same size as the vertical. Eh. Give me the old days when you had a nice big horizontal knob on there and you could, you know, tweak the thing cuz

**Dave Jones:** that's the main thing you're going to use. Not too keen on that, but anyway, I thought I'd show you that waveform replay feature cuz cuz I'm quite excited about that. And you can't get that on this $850 scope or whatever. Even in Australia,

**Dave Jones:** that's how much it costs. Granted, it's only 70 MHz version, but jeez, it's pretty impressive. And but the standard one doesn't come with the 56 meg memory like this one does. It is smaller, but for the first month or so, you'll have

**Dave Jones:** that trial option. You can play with the really deep memory and that waveform replay feature. Check that out. That's just screaming through absolutely screaming through those waveforms. Look at that. 10,000 and you can see the bang bang all the way up.

**Dave Jones:** You can I was touching that probe and mucking around. And that's really neat. And I believe you can also go in and dump that stuff to memory as well if you go into storage. So, I hit the storage button

**Dave Jones:** here and you can store what What do we want to store? We can store a picture, CSV, we can store all of the setups, the waveform, the traces. So, the traces that are on the screen or um or maybe the waveforms. I I assume

**Dave Jones:** because there's two different options there. I haven't read the manual. So, don't quote me on this. Um but one of those would be the full waveform dumps, I'm assuming, or maybe the CSV gives you the full waveform dumps so you can get You should be able

**Dave Jones:** to get all that raw data out. By the way, different picture types, bitmap, PNG, JPEG, and TIFF are supported. Really is quite nice. I like that. Oh, default. No, I hit something. Anyway, there you go. That's a quick, uh,

**Dave Jones:** firmware update and play around with the new Rigol 2000 series scope. I'll eventually do a full review on this thing, but what's this video gone? 20, 25 minutes or something? And I just played around with a few features, and there's a hell of a

**Dave Jones:** lot more in here. Let me see. I just noticed something. Look at this. You've got to be kidding me. 0.00000000 picoseconds. Woohoo! Catch you next time.
