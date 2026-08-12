---
video_id: leC-zSMbtfg
title: EEVblog #564 - Tektronix TDS3054 Oscilloscope Teardown Repair
url: https://www.youtube.com/watch?v=leC-zSMbtfg
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 32, "3": 45, "4": 59, "5": 72, "6": 87, "7": 103, "8": 119, "9": 131, "10": 142, "11": 158, "12": 172, "13": 187, "14": 202, "15": 215, "16": 228, "17": 239, "18": 252, "19": 266, "20": 277, "21": 289, "22": 302, "23": 314, "24": 333, "25": 351, "26": 366, "27": 381, "28": 399, "29": 411, "30": 431, "31": 455, "32": 475, "33": 497, "34": 515, "35": 535, "36": 565, "37": 579, "38": 596, "39": 608, "40": 623, "41": 640, "42": 652, "43": 665, "44": 678, "45": 695, "46": 708, "47": 726, "48": 742, "49": 755, "50": 768, "51": 781, "52": 797, "53": 812, "54": 828, "55": 839, "56": 853, "57": 868, "58": 883, "59": 906, "60": 927, "61": 940, "62": 961, "63": 977, "64": 996, "65": 1011, "66": 1030, "67": 1048, "68": 1062, "69": 1082, "70": 1099, "71": 1118, "72": 1136, "73": 1161, "74": 1175, "75": 1189, "76": 1203, "77": 1216, "78": 1234, "79": 1246, "80": 1261, "81": 1279, "82": 1298, "83": 1313, "84": 1325, "85": 1337, "86": 1351, "87": 1367, "88": 1380, "89": 1398, "90": 1415, "91": 1431, "92": 1447, "93": 1467, "94": 1481, "95": 1499, "96": 1515, "97": 1529, "98": 1544, "99": 1561, "100": 1577, "101": 1597, "102": 1608, "103": 1623, "104": 1640, "105": 1658, "106": 1675, "107": 1690, "108": 1704, "109": 1719}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Well, it's actually more of a an attempted repair video cuz I've got this nice Tektronix TDS 3054 four-channel 500 MHz oscilloscope here which I got in the auction score and I've done a video on that which will be

**Dave Jones:** linked down below if you haven't seen it. And this particular one actually has a fault on channel three here and we'll get into a bit of the detail before we crack it open. But anyway, I thought I would actually open this thing up and

**Dave Jones:** you know, at least have a look around. I don't like my chances of being able to repair this thing cuz these Tektronix scopes are famous for having custom ASICs and custom hybrid modules and stuff like that. So if if it's one of

**Dave Jones:** those that's blowing then well, you know, we're pretty much screwed. But certainly it's worth a look and hey, we get a free teardown out of it because I haven't seen inside one of these TDS 305 fours before. So, let's go. Now the

**Dave Jones:** first thing to think of when you find an oscilloscope like this with a problem on one of the channels is is the BNC dodgy? You know, is it loose? Has somebody you know, put force on it, broken it off?

**Dave Jones:** You buy these things on auction, you know, they could be manhandled and you know, generally just beaten around especially in in a one which has come from the military which this one has potentially been brutalized. But there's nothing wrong

**Dave Jones:** with that. There's BNCs at all. So it's especially channel three here, nothing wrong at all. So, not a physical thing to do with the BNC connector. And this isn't like the Tektronix TDS 220s which are famous for their broken BNCs. These ones are really

**Dave Jones:** incredibly rigidly bolted I think into the unit in there. I think I can cut see a couple of screws either side of that. So they're probably bolted into the steel frame of this thing. Probably the metal frame. So, um yeah, they're pretty

**Dave Jones:** darn good. So, it's not a physical fault of the BNC. So, the next thing to consider is, well, have they overloaded uh channel three? And well, we won't know that until we uh crack the thing open, but let's have a look at the

**Dave Jones:** waveform we get. Now, here it is. I'm feeding in the 1 kHz uh calibration signal, and it's weird. It is the correct voltage. Here it is, uh 2 V per division. It's supposed to be 5 V. So, 2

**Dave Jones:** 4 5. So, it's the correct value, but look at all this garbage above, below. All that is jumping all over the place like that. And if I press uh stop on that, and we zoom in, I mean, you know, have a look

**Dave Jones:** at all this garbage. It's almost as if, you know, there's these huge bit errors in there. I don't like that this thing doesn't have a um you can't press the horizontal position button to go back to the start uh to go back to the center.

**Dave Jones:** Anyway, my first uh you know, reaction to this is that it's some sort of uh fault in like the ADC, and there's like a floating bit or something like that, which is causing it to go to jump all over the shop like

**Dave Jones:** that. But it's it really is quite strange. And if I dial back the time base, look, it actually stops. Okay? I can increase the time base like that. Not a problem at all. Okay? But if I go down beyond that,

**Dave Jones:** it just vanishes. I mean, there's nothing wrong with the trigger point. I'm triggering off that channel, and I can do auto setups, and it still it still doesn't work. So, there's it's it really is quite an unusual fault. I

**Dave Jones:** don't think I've ever seen anything like this before. So, I don't know, you know, off the top of my head, I'd say, "Yeah, look, the you know, the front end basically seems to be working." So, the odds of probably an

**Dave Jones:** overload on this blowing it um probably unlikely cuz we're getting the waveform. I mean, I can feed a sine wave into this and I get a sine wave out, but it has that same sort of, you know, huge

**Dave Jones:** like it's almost as if the ninth bit cuz this is a nine-bit ADC in this thing, which is really quite nice and pretty unique about this scope. It's not just your usual eight bits, but it's almost as if like the ninth bit or something is

**Dave Jones:** just doing all sorts of random stuff or something like that. Anyway, cuz that that's just really weird. Look at that. Cuz it's just going way over like that, but I don't know. It's, you know, it it may not be the output of the ADC. It

**Dave Jones:** could be something else. I don't know. Your guess is good as mine. I haven't put much thought into it, but yeah, I don't think it's actually a blown input cuz generally with a blown input you'd, you know, blow

**Dave Jones:** the ass out of the fit or something like that and you'd really get no signal through, but we are getting a signal through on this thing. So, it's more of the sort of, you know, the processing side of it like the ADC or after, you

**Dave Jones:** know, after the ADC or the ADC hybrid. I presume it's a hybrid module in here with these Tektronix. So, because it's five gig samples per second, it's you know, woo, that's, you know, it's pretty darn good. Five gig samples per second.

**Dave Jones:** So, Tektronix would have their own custom ADC hybrid in there for doing this, but yeah, I don't know. It really is a weird fault and why when you drop down in time base like that it just doesn't do

**Dave Jones:** anything. And it changes, by the way, if I go into here and set fast trigger points. Look at that. It just doesn't like it it There it is. It disappears at a further point, but there's look, there's a one line there. You may not be able to

**Dave Jones:** see that, but look, now we're at 10 volts per division. So, it's scaled that back. It's weird. So, the difference between 10 K points and 500 K points is really quite unusual. Now it's not doing anything at all. There we go. So, 10K points. It's

**Dave Jones:** that affects the horizontal where it disappears. Like, for example, it's working there, but I put it on there and it's disappeared. If I turn the time base up, it comes back. So, yeah. I That is really quite strange. There's

**Dave Jones:** something to do with the acquisition engine or acquisition ASIC perhaps. And if I turn dot mode on there instead of vector, as you can see the the dots up there sort of gathering around that position there. If I turn the

**Dave Jones:** waveform intensity right up, cuz this is a DPO display, of course. Um You can just It's just It's very strange. That's with waveform intensity 100%. Very, very strange, this one. All right. Now, according to the service manual of

**Dave Jones:** this thing, um it's a bit tricky to get this off. You have to start with the handle here. You don't undo the screwing there. You take this cap off and there's a little pin in there, which apparently you have to put the

**Dave Jones:** handle upright like this and then pull this pin out about 5 mm. Actually, that is a rather interesting handle mechanism. It's They've gone to quite a bit of effort to uh design that. Not sure why they had to go to that much

**Dave Jones:** effort, but okay. No force required, I guess. Pin ain't budging, and I've got serrated uh pliers here. Oh, no. There we go. Pull it out 5 mm. There we go. Okay. Now, I don't do the other side. I sort of put this back to

**Dave Jones:** the horizontal position and then, apparently, you can pop out pop out the whole hub assembly. Let's spin the hub assembly inside there. Hmm. Hmm. There we go. It finally popped out. I didn't pull the pin out far enough,

**Dave Jones:** apparently. Yeah, go figure. Look at that. Ugh, unbelievable. Here we go. The other one should pop out. Tada! There we go. Ugh, yeah, piece of cake once you know. And then the handle lifts off, but jeez, that's really convoluted. What were you

**Dave Jones:** thinking, Tektronix? Now, of course, one of the most satisfying things of any repair like this, voiding the calibration seal. You bet. There we go. It's goneski. Now, of course, there are ways to try, you know, attempt to get this off and uh and put

**Dave Jones:** it back on, but hey, this isn't a warranty thing, so we don't give a toss. All right. Now, we need a Torx driver to undo this screw here, and we'll take out the comms module. There we go. Tada! We're out. All right. Now,

**Dave Jones:** this back chassis should pop off. That's uh that's the plan. There are no other screws, I believe. So, here we go. Tada! And yes, wait for it, folks. We're in like Flynn. Whoa, I don't Yeah, there we go.

**Dave Jones:** Can't let that rest on the floppy there. You got to flip it over. That's just flapping in the breeze. Look at that. And there we go. That looks pretty clean. know, uh happy with that. I don't mind the construction at all. This isn't

**Dave Jones:** too rigid on top here though up though, but I don't mind the arrangement of the power supply on there. It looks like we can probably unclip that top chassis. It's basically uh single board really down in there. We

**Dave Jones:** got the main board there the um There's the shield for the front cans. You can see the dividers there. So, we have to take that off and eventually get into the front end there, but yeah, I'm not keen on that floppy. Just look

**Dave Jones:** that's just flop around. Maybe it Hang on. Does that go into the case there anything? Yeah, there's some I think there's some uh sort of you know um matching parts of the case in there to hold that floppy drive, but the

**Dave Jones:** interesting thing is is that you can probably replace this thin line floppy drive. Looks really easy. Uh replace it with a modern um flash unit cuz you can get these. You can get slimline versions of these that have a

**Dave Jones:** USB port on here and it's got the same interface assuming it's got the um same ribbon cable interface and it's not some sort of pin interface off hand. I don't know 100% on that, but I know you can

**Dave Jones:** buy these things for you know, they're about I don't know 40 bucks on eBay or something and they've got a USB stick in there and they operate and interface exactly like a floppy drive. So, that would you know, if you got one of these

**Dave Jones:** things, it'd be a worthwhile addition. You know, cuz floppies are bloody hopelessly obsolete now. Much better if you can just plug a USB key into the thing and save your files that way and you shouldn't have to change the firmware.

**Dave Jones:** This is interesting. Just notice this. Check out this uh regulator down there. They've got this heat sink. Oh yeah, it's a PCB mount type, but it's like a am, you know, you don't often see just flimsy metal like that acting as a

**Dave Jones:** heat sink. Usually it's a proper, you know, nice little black anodized one or something like that. So, yeah, that's a bit how you doing. Liking the look of this power supply section down in here. Looks really beefy. Nice big fat

**Dave Jones:** SMD diodes down in there. Huge big inductor bob and stuff. Look at that. Massive. I like it. That's really quite neat. And what brand caps have they got in there? I'm not sure. Nippon Chemicon. Ta-da! That one is. There you go. Nippon

**Dave Jones:** Chemicon. Absolutely first class as you'd expect in a you know, this is a real expensive Tektronix scope or it was back in the day. Well, even today. It's well, the modern version of this. This is like the older model. I think it's

**Dave Jones:** the 3054B now series. But as you'd expect, they haven't cut any corners. And there we go. We have our back light driver down in there. That's one of the complaints I have with this scope. Especially if you buy it old. I'm not

**Dave Jones:** you know, I don't have a brand new one to compare it with. But yeah, really the back light I think fades with age. It's pretty horrible and dim and maybe it was like that brand new. I don't know. My

**Dave Jones:** memory is not that great on using these things back in the day. But yeah, a separate driver and maybe you could replace it with a nice super bright LED back light or something like that maybe. That'd be a nice upgrade. And this is

**Dave Jones:** interesting. Check this out. They got a little two-pin header down on the main board there with these two wires. What they've done is they've put them inside heat shrink surround and just you know, over the mains wire in there. Active and

**Dave Jones:** neutral wires. And what that's doing is just there's no electrical contact in there. They're just putting it next to there in some length inside that heat shrink tube. So, the AC mains capacitively couples over and that's how they gets in and that's

**Dave Jones:** detected by the processor and it can measure your mains frequency and adjust for that automatically. So, that's often a cheaper and safer solution than actually having the circuitry on the power supply somewhere in here actually electrically, you know, tapping off the

**Dave Jones:** signal and then have it coming through the cable over here. But, you do have that extra manufacturing step of having to heat shrink all that stuff in there, but hey, you can't complain about the isolation, that's for sure. So, I'm not

**Dave Jones:** a fan of how this extender board here, this is the battery connector down in there sort of is not supported here. It may be inside the case, of course, but when you click on that power button on the front, you know, there is a bit of

**Dave Jones:** stress on that board, but so unless that's really anchored well inside the other half of the case, yeah, I don't know, that's not the greatest. And took a couple of screws off the top here. Uh, disconnected the ribbon cable for

**Dave Jones:** the ancient parallel port and uh looks like I can probably just get rid of a couple of other connectors here. Here we go, I can disconnect that from there and bring that up through there and then I should be able to disconnect

**Dave Jones:** the power supply connector over here and ta-da! We're in. There is a ground connection left stubbornly attached to the chassis. Now, here's all the main circuitry and all I'm seeing here essentially is a bunch of probably custom part numbers. I mean, what's this

**Dave Jones:** huge device? It's National Semiconductor, obviously ADG360C. I can find a couple of references to that, but no data sheet on on first glance and then they've got ADG365B, ADG3618. Probably an ADC per channel, and that's probably some sort of mux which is

**Dave Jones:** getting it into some sort of that's probably the uh pro the acquisition engine up there as a custom device. We've got some memory surrounding that, of course. More memory over here, and then the main uh processor driving the

**Dave Jones:** screen and everything else is a um Motorola / Freescale um XPC860 or you know, MPC860 uh network communications processor as they call it. And well, there's not too much else on there. So, you know, you got to think that ADC per

**Dave Jones:** channel because I'm pretty sure that's how this uh tech operates. I haven't double-checked that. So, four channels, four ADCs, um something bridging those together. Main acquisition engine, yep, I think that's probably it. Now, some good news on this

**Dave Jones:** front-end shielding can here. While the While the walls are soldered in there, it looks like it's a two-part, and I can just probably bend these, and I should be able to lift off that top cover. That's the plan, anyway.

**Dave Jones:** And so, all the uh dividers will still be in there, but uh yeah, I might have to leave a this thing up this thing up. Yeah, it may not come up easily. Uh let me do this. Now, here we go. It is

**Dave Jones:** going to come up there gently. And not easy, but yeah, it popped out, and I should eventually be able to get all that off. Holy hybrids, Batman. Look at that. I knew there'd be hybrids in there of uh some description, custom ASICs,

**Dave Jones:** and hybrids, but jeez, look at that. The whole damn thing is a hybrid module soldered onto the board with these with these connectors around there and with the pins around the outside of there. Wow, and yeah, it does look like a

**Dave Jones:** custom tech ASIC in there, of course. It's got May Tech's US. I'm not sure Max Tech, sorry. I'm not sure who they are, but yeah, tech part number on there. They've obviously rolled their own front end there and it

**Dave Jones:** is actually really quite impressive. There might be some RF voodoo there on the PCBs as well. Look here, this is rather fascinating. Are these distributed element filters which I've looked at in previous RF well videos in RF units cuz cuz remember

**Dave Jones:** this is a 500 MHz front end 5 gig sample per second. So, have they been doing something special there? But look at that. I mean, there's definitely a hybrid module. There's like a hybrid resistor or capacitor over there. I'm

**Dave Jones:** not sure what and what this arrangement is in here, this multi-layered thing with these, you know, that looks for all the world like you know, some form of distributed element filter system right there and then what's underneath. There seems to be some maybe

**Dave Jones:** some printed hybrid components under that and then they got that happening down there as well. And then they've just got regular you know, a regular cap down in there. But that is that is really quite interesting. Look at that. Then they've

**Dave Jones:** got these long carbon, you know, these long like carbon traces on the top there. So, this is a really interesting hybrid construction. So, that's very very fascinating. If anyone's got any details on this uh Tektronix hybrid, then please leave it

**Dave Jones:** in the comments cuz I'm sure a lot of people would be interested in knowing exact details of what's going on here. And you can see the B and C connector. That's the third channel there popping up into the hybrid. And as I said, well,

**Dave Jones:** that's clearly not uh broken. And of course, it's as I said, uh solidly connected um down into the chassis down in there. So, there's nothing wrong with that connection, otherwise we wouldn't be getting any signal um on this thing

**Dave Jones:** whatsoever. So, I I don't know if there's anything under the hybrid. I can't know that unless I actually take the hybrid out, but it's unlikely. It looks like it is flush mounted to the PCB. Now, I can actually get my torch down in

**Dave Jones:** there. Sorry, this doesn't show up on camera, but there is uh basically nothing that I can see on the PCB under there. I can see pretty clearly down in there. So, on the main PCB, there's nothing under that hybrid module. And

**Dave Jones:** there doesn't seem to be any um at least uh you know, non-printed uh components on the bottom of that hybrid. So, yeah, that's uh it looks like all the magic does happen on that hybrid. So, hmm, what's left? So, if that hybrid looks

**Dave Jones:** like it's doing absolutely everything on the front end, then we're pretty sure our issue is on the front end somewhere. Of course, I will check the uh third channel chip over here. It doesn't look to be anything wrong there. I mean, this

**Dave Jones:** is all perfectly reflowed. You wouldn't expect any issues with uh any of you know, there's a couple of little miscellaneous devices down in there, little sot 23s, stuff like that. You wouldn't expect anything to happen on the main board, but the thing with these

**Dave Jones:** hybrid modules is that um these are on a ceramic base, and these have These are very temperature stable, so they, you know, have a low coefficient of expansion versus heat, much larger than the PCB. So, you've got this mounted onto the PCB, which has a

**Dave Jones:** different thermal expansion coefficient. So, you can actually end up with possibly a cracked solder joints on the hybrid, although the big springy leads on that would actually take out all of that, you would think. But, really, I mean, that's

**Dave Jones:** you know, at first guess, that's really all I'm left with, that there's some sort of, you know, a dodgy joint either on the hybrid module itself or going down to the main PCB. And unfortunately, it's not easy to inspect the side of

**Dave Jones:** that, cuz these damn metal walls are in the way, and I can't take those out without, you know, ripping the whole board out and then desoldering it, and uh it's just horrible. Getting out these shields is just awful. So, I don't know.

**Dave Jones:** I'm just going to have to go around with the microscope and inspect. This is actually channel three here I'm looking at. So, I have to go around and inspect every one of these joints around the outside and see if I can find anything

**Dave Jones:** funny. I can't obviously see anything, you know, blowing as such on that hybrid module. It looks in looks in pretty good nick, as does the main chip up there. But, as I said, you know, that must be working. It must be

**Dave Jones:** doing something, otherwise we wouldn't get our main waveform. So, you know, there could just be one dodgy joint somewhere. What could it be? So, I'd like to think that it's sort of more on this half of the side towards the ADC up there than

**Dave Jones:** it is on, you know, the front end hybrid down here, cuz as I said, you know, it seems to work, and we're getting the correct amplitude and all that sort of stuff. So, I think I'd probably be wasting my time looking around all the

**Dave Jones:** bottom half of the hybrid module up here. I think it's, you know, probably from here up to probably up to the main ADC and maybe into this whatever this chip is here. It's not too hard to work out where your differential output is on

**Dave Jones:** this front end hybrid amp down here. It's obviously these two caps here coming out and it's a dead giveaway because those two traces are fatter by a controlled impedance and they run as a differential pair from the hybrid there

**Dave Jones:** over to the ADC here. And check this out. I'm viewing this through my Mantis, so please forgive the crudity of the image here. You can see that mark, that L-shaped mark down in there. That looks for all the world

**Dave Jones:** like a laser trim mark. I reckon they've trimmed that and there's a couple of components that have, you can see that one there, has it, and this component down here has it. They all have Well, a lot of them have these little

**Dave Jones:** marks on them and uh yep, I reckon they're a laser trim. And check out that one there. Look at that. It's got multiple marks in that long trace there. Fascinating. And there we go. There's our solder joints down in there and I'm

**Dave Jones:** having a hard time seeing any issues with that at all. It's a, you know, it's a lot brighter and clearer through my Mantis scope than what I'm picking up on the camera here and really I've looked around all of those joints. This is on

**Dave Jones:** the third module and I can't see anything. There's the hybrid serial number. Woohoo! So, yes, I can't see a single thing wrong with any of those joints on the hybrid module there. I'm The good thing is you've got the other

**Dave Jones:** hybrid modules to compare it with. Just nothing wrong at all. Nothing looks like it's been blown or stressed or anything like that. Both the solder joints on the top of the module, on the both on the top of the ceramic substrate

**Dave Jones:** there and down on the PCB look okay. I can get a much better result through the Mantis than a bigger, brighter, you know, more three-dimensional display than what you're seeing on camera here and and really I can't see anything. So

**Dave Jones:** that's the main ASIC there and you know, it's not a of course that's not the ADC. That's just the you know, that's just the main uh front end ASIC and that would have a differential driver output which then

**Dave Jones:** would go over into the ADC. And once again, the ADC here, I did notice a couple of maybe little crusty uh you know, a bit of you know, fluff and crap around the pins of of that presumably ADC up there for

**Dave Jones:** channel three and I've sort of brushed that away but yeah, I man. I'm not seeing anything wrong with this. Damn it. I was hoping that you know, there'd be something really obvious but there's not. All the solder and iron was

**Dave Jones:** right there so went around and reheated all of the joints on that channel three hybrid module and well, no. Same result. So just to double check here, what I'm going to do is take out the entire way board.

**Dave Jones:** There we go. There was just a couple of screws here. I like the fact that this holds whoop, there we go. I like the fact that you know, this comes out as one separate module. You don't have individual little piss ant screws on the

**Dave Jones:** front. That's really nice. I like that and that just comes out as one module. And well, we can have a look on the bottom. And well, look, there's really not much on the bottom. There's some ground plane and well, not much else to

**Dave Jones:** go wrong. So, well, I'm left wondering what the hell I can do. You know, there's just the hybrid module. That's it. And I can't even get access to the side unless I really take out all this this shield on the bottom. I might have

**Dave Jones:** to suck that out from the multi-layer board. It's just not nice at all. And really, I don't see what I have to gain for that. And there's nothing obvious on that third module there at all. And well, I've reflowed the pins and

**Dave Jones:** jeez, what's left? I've you know, there's some gunk around the third channel chip there. I cleaned that off. I don't know. Left holding an empty bag. Not sure if you can see that, but the fifth pin from the right there and the fifth and

**Dave Jones:** the sixth and the seventh pin, there seems to be some sort of you know, they seem to be bent or have possibly some sort of short between them. Now, this is on the presumably ADC chip, but it's not on

**Dave Jones:** channel three. It's on channel four. So, could be a completely red herring, but I'm definitely going to measure that and just clean it up a bit and just make sure that's not shorted. Well, there you go. The EEVblog repair curse strikes

**Dave Jones:** again. Found nothing obvious at all in this stupid thing. So, I don't know. If you got any good ideas, please leave it in the comments because well, I don't know. There's not much there apart from the hybrid and the ADC really.

**Dave Jones:** I don't know. Unless I missed it, maybe someone will will have spotted something watching this in HD or something like that. So, if you have or if you have any better ideas, please share it. Uh well, catch you next time.
