---
video_id: woI3aQzJfNc
title: EEVblog #278 - Elmo Visual Presenter Teardown
url: https://www.youtube.com/watch?v=woI3aQzJfNc
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 33, "3": 46, "4": 58, "5": 73, "6": 86, "7": 97, "8": 111, "9": 125, "10": 140, "11": 155, "12": 170, "13": 183, "14": 202, "15": 223, "16": 241, "17": 258, "18": 274, "19": 291, "20": 309, "21": 331, "22": 344, "23": 363, "24": 378, "25": 395, "26": 408, "27": 419, "28": 428, "29": 443, "30": 460, "31": 479, "32": 493, "33": 509, "34": 526, "35": 543, "36": 559, "37": 578, "38": 591, "39": 603, "40": 621, "41": 637, "42": 656, "43": 670, "44": 684, "45": 696, "46": 711, "47": 724, "48": 747, "49": 762, "50": 775, "51": 798, "52": 817, "53": 836, "54": 852, "55": 869, "56": 886, "57": 902, "58": 922, "59": 938, "60": 959, "61": 976, "62": 992, "63": 1006, "64": 1026, "65": 1039, "66": 1054, "67": 1069, "68": 1086, "69": 1103, "70": 1120, "71": 1134, "72": 1144, "73": 1159, "74": 1178, "75": 1194, "76": 1220, "77": 1240, "78": 1258, "79": 1274, "80": 1290, "81": 1306, "82": 1327, "83": 1343, "84": 1359, "85": 1371, "86": 1382, "87": 1399}
---

**Dave Jones:** Hi, I've got a rather unusual device here. It's an Elmo. Tickle me, Elmo. Um, it's an Elmo visual presenter. It's a P30S model uh visual presenter, and let's take a look at it. I didn't know these things uh actually

**Dave Jones:** existed, but apparently they're all the rage in the classrooms. And what they are is they're a a mechanical um uh they've got a mechanical uh head here with a very high-quality um optic camera on there. I think it's got

**Dave Jones:** like a times 10 zoom or something like that. And it looks very much like an overhead projector. And it's got two arms on it. So, if we take a look, this arm comes down here to fold in place so

**Dave Jones:** that you can, you know, carry the thing and transport the thing. But, you lift this arm up here, the camera comes up. This, if you're wondering what it is, is a light. It's got uh two LEDs in there. And uh it's an

**Dave Jones:** LED light which lights up anything that you put on here. Usually they're for a page or something like that. And it's for presenting to like a classroom or an audience on a large screen. So, it's got various uh outputs, DVI output, uh

**Dave Jones:** uh S-video output, and RGB output that you can hook on to a big projector type system. And you can actually display things live. So, if you're, you know, going through a document or something, you put your document on here, and it

**Dave Jones:** presents it on the huge screen to the classroom. And it's got an LCD down the bottom here. Um, and an SD card on the side, and you can put in presentations and all sorts of things which overlay on

**Dave Jones:** the video. Apparently, um a little uh 3-in uh uh 3 and 1/2-in maybe uh LCD down here which shows you live what's on the screen. And apparently they're quite expensive, but uh you can pick them up, I think uh

**Dave Jones:** quite cheaply uh second-hand in various models. But, I thought I'd uh try and power this thing up and give it a go. And I thought maybe it'd be good for soldering. Look at the huge big usable range here. And if it does

**Dave Jones:** have a times 10 zoom camera with a great optical ability, maybe it might be good for soldering or something like that. Or maybe I have to bring it down or something like that. I I don't know. Anyway, I thought I'd power it up and give it a

**Dave Jones:** go. And here are the outputs we've got on the back of it. S-video, composite video, DVI, RGB out. It's got RGB in as well. RS-232 control, 12-volt DC power, and some dip switches which I don't know what they do. But the problem we've got

**Dave Jones:** is this DC power connector. And if you have a look at that DC power jack, it's one of those really annoying circular ones with the pin in the center. And I've seen those on various notebooks and laptops and stuff like

**Dave Jones:** that. But uh yeah, I don't have anything that fits that. So, I think I'm going to open this thing up and maybe see if I can hack in a different connector. So, I've taken off various screws on the bottom

**Dave Jones:** and it should and on the couple on the top here and it should lift off. Yeah. Yeah, there's nothing holding it down. Ta-da! There we go. We're in. And here's the main PCB and it contains lots of electronicy consumer goodness, I guess.

**Dave Jones:** There's a BGA device there, some memory, another huge big BGA device from someone called I chips, more memory beside that, probably some uh custom well, some video circuitry down here for the various video out options and it seems to be quite a bit on that

**Dave Jones:** board. We've got our SD card board over there and we've got not much else down here. We've got a little keypad PCB there and the LCD screen. Now, curious thing about the LCD screen is that I don't see any

**Dave Jones:** data cable, any parallel data cable going to it at all. All we've got is this tiny little cable here and it runs into this connector down here. So, if you look at that, there's a little shielded cable there plus two other tiny little

**Dave Jones:** wires into this tiny little uh header connector here and well, that must be like a composite um output. So, I guess there's you know, there's power on there plus composite and that's it. So, that there must be a PCB under the

**Dave Jones:** LCD that takes a composite input and converts it directly in into the LCD. I guess that kind of makes sense. I'm just uh think that's a little bit curious. Those little tiny, itty-bitty, teeny-weeny wires on there. And down in there we can see the DC

**Dave Jones:** power jack and that looks suspiciously like a standard footprint or very close to a standard footprint for a 2.5 mm standard DC jack. So, maybe if I take the board out and have a look at that, I might, if I'm lucky, I might be able to

**Dave Jones:** suck that out and replace it with a standard uh 2.5 mm 12-V DC jack. Only one way to find out. Let's take the board out.

**Dave Jones:** Now, I'm pretty sure I've got all the screws out, but I'm not having any luck prying this out at bottom this board out at all. I seem to push on it and it springs back. It's almost as if it's stuck down with

**Dave Jones:** some sort of silastic or something like that. I find it's a real pain in the butt. I don't know what's what's going on here. I hate this. And there you go. It actually required a little bit of uh

**Dave Jones:** percussive maintenance to get that one out. And sure enough, it was uh stuck down with these two pads here. How annoying. But there's some extra stuff on the bottom. This is actually a rather interesting board. And check out the bottom footprint of

**Dave Jones:** the DC jack there. And aha, it looks just like one of these standard DC jacks. This is a uh 5.5 mm outside diameter uh 2.5 mm inside diameter. I should be able to suck that out and solder that back in. Maybe um this pin

**Dave Jones:** on the back here might be a bit big, but uh that's no problem at all. We can trim that down. So, I should be able to replace that annoying DC jack with one that actually I can use. Beautiful.

**Dave Jones:** And we've sucked that connector out by chopping off while it was on the board, chopping off one of the pins on the back there. Sorry, I forgot to hit uh record. I didn't actually get it um cuz it might

**Dave Jones:** be a bit difficult to heat up all three pins at once. So, I did uh chop off the one pin while it was on the top, then I heated up these two pins here, and it just dropped out. Then I was able to

**Dave Jones:** pull the third pin out. And it's okay if you don't want to uh keep the existing Sorry, if you don't want to keep the connector and you don't care about that, then you can actually uh destroy them and uh ensure you don't damage the board

**Dave Jones:** going out. So, unfortunately, as I predicted, the back pin there was a little bit too wide. So, I've had to uh chop chop some of that off. Actually, it turns out I've had to trim all three pins. They didn't quite uh

**Dave Jones:** fit there. but ta-da! There we go. Finally got it to fit, and we now have a beautiful standard DC jack that I should have a power adapter for. And of course, you're going to make sure the polarity is correct. In this case, the center pin

**Dave Jones:** goes down to the third one there through a poly switch goes down to the what's clearly the positive input with the poly switch down there, and the other two are connected down through ground as they should be. So,

**Dave Jones:** that should work fine. Now, I know you're curious to know which devices are on the board, but unfortunately, finding info on these is very few and far between. We've got this BGA device here, which is a new core

**Dave Jones:** SIP 1280 DV. And obviously, that's because that's hooked on directly to the camera here. That's some some sort of video capture chipset. And there's the memory surrounding it. Possibly, this one might be tied over to here. I don't know, but

**Dave Jones:** certainly, that is like a memory for that and maybe a ROM as well. And over here, we have an IChips IP 00C 726. Now, I found the company website, and I found info on a 762 device, which is a

**Dave Jones:** high-end video display HD processor. And they make deinterlace chips and all sorts of things, but I can't find any info on the 726. But I found info on the 762. It's definitely 726 there. Go figure. Once again, we've got some memory, we've got

**Dave Jones:** some ROM here. It's obviously got a code on there to indicate that that device has been that flash device has been programmed. And over here, we've got a Lattice Semiconductor CPLD. Once again, it's been silk-screened on the uh, top to indicate that, uh, or

**Dave Jones:** stamped on the top to indicate that it's been programmed with whatever. That's just some sort of glue logic or something like that. And down here, the, uh, trying to read the device on here is incredibly difficult, but I've got NEC

**Dave Jones:** something or other, and I think it's in some sort of NEC, uh, processor or something like that. And And once again, that's been marked on the top possibly to indicate that it's been programmed because it's a programmable, uh, device,

**Dave Jones:** no doubt, like a microprocessor and {slash} micro controller. And, um, up here we have a device from, uh, Focus. It's an FS401LF. Once again, can't find any info on that at all. It's just, uh, you know, these are, well, you know, obviously, uh, got

**Dave Jones:** something to do with, you know, display, uh, drivers and things like that. And on, on the bottom here, and here we have an Analog Devices, uh, ADV7123. That's a high-speed, uh, video triple DAC. No surprises there. 10-bit, uh,

**Dave Jones:** video DAC. And this device here is a TI, uh, TFP410. And it's a, uh, PanelBus display driver IC. And, uh, we've got, um, some LVDS, uh, driver devices. That's an LVDS, uh, driver up there. That's a, uh, THC63,

**Dave Jones:** um, LVDF. And that's a dead giveaway. That's an LVDS, uh, driver. So, apart from that, uh, this board is, uh, rather, you know, it would be interesting if we could actually get the specific, uh, data sheets for these

**Dave Jones:** devices. But anyway, it is really, you know, essentially a, uh, reasonably high-end, um, HD video, uh, capture cuz here's our video input, video input connector here coming from the camera. It's the multi-way connector. It's got the big shielded cable running up to

**Dave Jones:** the, uh, camera on the top arm. So, that's obviously some sort of video capture and it buffers it, does all sorts of things. We've got a video display processor with some memory, maybe a micro uh doing some stuff here.

**Dave Jones:** We've got and then various uh drivers to drive the various displays and things like that. So, yeah, it's um pretty much what you'd expect, but uh I hate it when you can't find info on devices. It's really annoying. All right, I found a plug

**Dave Jones:** back. It says it requires uh 12 V at 1.9 amps. I've only got uh 1.25 amps here. Uh fingers crossed. Let's give it a try. What's the worst that can happen? It hiccups or it just doesn't work. Here we

**Dave Jones:** go. Woohoo! Hey, we have light. We have flashing. LCD doing Elmo. Beautiful. It works. Hey, there's my hand on the LCD. Brilliant. And there you go. You can see my hand on the LCD in Is it real time?

**Dave Jones:** Uh no, there's a bit of lag there, I think. I think there is a little bit of lag in that. That's a bit of a bit of a bummer, but uh yeah, it seems to work. I wonder how this

**Dave Jones:** thing works. Maybe I should read the manual. Well, let's see if we can zoom in on a board here. It's got the zoom control up on the top head of the and you can hear it if you listen closely.

**Dave Jones:** Hang on. Listen to this. So, we can zoom in a long way on these devices. Looks like it's going digital now. That zoom and that's the like I'm trying to there they should be surface mount components, but I can't make heads or

**Dave Jones:** tails out of that. So, obviously, the focus system isn't working that great at those massive zooms. I mean, it's supposed to have auto focus this thing. Um hang on. No, no. Let me zoom in. Oh, pushed the button. Oh, there we go.

**Dave Jones:** There we go. You got to push the button. So, you zoom in. That's as far it looks like. That's as far as it will go. But, gee, I tell you what. That's not There we go. It takes a little bit of

**Dave Jones:** settling down, but I tell you what. That's not too shabby, I guess. Um considering that this thing's what? A good uh 50 cm away. The um actual camera itself is about 50 cm away from the board. That's a That's a long

**Dave Jones:** distance. So, that's not That's not too bad at all. If we zoom out on that, maybe it will keep focus as we zoom out, but Yeah. It's rather interesting. I don't I don't mind that at all. I wonder if we can uh

**Dave Jones:** get closer and um maybe even get a soldering iron under this thing. And here it is connected to my 22-in PC monitor, and it does look really really good when it's uh displayed on a large screen like this. Much better than the

**Dave Jones:** piss-poor resolution uh 3 and 1/2-in uh screen on the unit itself. And it does seem to work really well. And if I uh zoom in here and whoop, zoom in. Let's zoom in on the board. You need to press the auto focus button

**Dave Jones:** once it's zoomed in. If I press it, there we go. And it hunts around a bit, but uh it does zoom in rather nicely. And after that, I think that might be a digital zoom after that. So, but it it really is quite nice

**Dave Jones:** considering that the distance. That's a Oh, that's probably an 0603 uh component there on the screen, but that is really quite nice. I'm very very impressed with this thing given the uh half a meter distance that it's away

**Dave Jones:** from. And uh it does work really quite nicely. And if I give that a little poke under there, that is in real time. Unlike the I thought there was lag on the LCD before, but there's not. That's Uh if there is lag, it's very difficult

**Dave Jones:** to uh to see it. So, I'm You could really use this thing as a uh quite a nice uh real-time soldering aid, I think. And there it is zoomed into its absolute best. And uh you can see as I

**Dave Jones:** pull the light over it, you can you can really see the uh the compression uh artifacts on there. It's not that great, but uh it's certainly good enough for uh soldering work even at this distance. I mean, you

**Dave Jones:** know, it's not as good as a nice uh stereo microscope, perhaps, but uh well, certainly it's not as good as that, but jeez, it's not bad at all. And I really like the display produced when I move the head down like that. It

**Dave Jones:** really is re- really is quite nice. Um I don't think it's going to autofocus properly at these particular angles or not, but Oh, yeah. There it goes. Yeah, it did.

**Dave Jones:** That's It really is quite neat. You can have a quite a bit of fun with this. I like it. Imagine if it was on a big uh proper um you know, movable boom arm. That'd would be rather neat. Now, let's see what

**Dave Jones:** happens if I halve the distance here. I've really bent it down and uh put it in place like that. Obviously, it's off the uh platform, you know, it's sort of uh it's just on the platform, but uh let's see if we can zoom in on that.

**Dave Jones:** No, hang on. No, it's not going to let us zoom in on It's not going to let us zoom in on that at all at that sort of distance. So, unfortunately, there is a limit to how close you can

**Dave Jones:** get this head and these optics to your board. So, that's probably a bit too distance is a bit close for that sort of That's about the limit. Not sure what zoom level that is, but uh yeah, it's not It's not huge. So, you

**Dave Jones:** can't obviously get uh close too close with this thing. The optics are optimized for that sort of uh half distance uh half half meter working distance with the times 10 zoom. And I just tried it with an SD card and it

**Dave Jones:** does save HD images or uh semi HD 1280 by 720. Very uh nice, saves them as JPEGs, but unfortunately, it doesn't seem to uh uh have any video recording capability to SD card. So, that's a tad disappointing. Uh not too happy with

**Dave Jones:** that. What's actually wrong on the optical zoom on this thing? It is actually a 16 time optical zoom with a four times uh digital, but it's a shame it just can't get closer like that, but it does allow you um part of the feature

**Dave Jones:** of this, it does allow you to get 3D views of objects. So, you can tilt this thing all the way over. Well, you know, this slicer, this angle of it anyway. It doesn't let you go this direction, but

**Dave Jones:** you could rotate your objects like that and uh you could zoom in and get video. Now, I've um tried the SD card in here and you can actually save uh uh HD images and well, HD being a thousand

**Dave Jones:** being 1280 by 720. You know, sort of the low-end HD, but it's got the camera is 30 frames per second updating. So, it really is, you know, quite a powerful little beastie, but unfortunately, it saves really good quality images. Now, unfortunately,

**Dave Jones:** there doesn't seem to be any video recording capability with this. So, if I wanted to do that, I'd have to plug video some sort of a video recorder into my RGB or S-video output, one of those sampling capture video capture

**Dave Jones:** cards or dongles for your PC. So, that's a bit unfortunate, but And because I know there will be people who are curious to see what's inside the video head here and I won't take it apart any further than that because the it's

**Dave Jones:** basically just contains an optical uh lens system in there, which is the 16 time optical zoom. There'll be a motor in there to drive the optical zoom. There's a PCB up on top there and another PCB down here for the auto focus and the

**Dave Jones:** um zoom control as well and that's about it. So, yeah, sorry. I'm not going to delve into the inner details of this. I want to keep it in one piece until I decide what to do with it. Now, the main board had these and

**Dave Jones:** these are these little um they call them test points, but they're actually grounding clips and they're spring loaded grounding clips and where if you lift that board up there there's a little spring mechanism in there that sort of lifts a lever up like that. It's

**Dave Jones:** rather quite nice. I haven't seen anything like that before. It's rather complex just for the operation of grounding something through to a back panel. And they've got like four of those on this board. It's crazy. And you can see the cable down in there at the

**Dave Jones:** bottom that huge multi-way shielded cable which goes all the way down the arm back to the main processor board. And they've got uh some ribbon cables and other stuff in there. You can probably just see the motor down in there which has that flat

**Dave Jones:** flex cable. That's probably the zoom motor perhaps. And uh bottom side of the presumably uh custom PCB. This would be a whole custom assembly specifically designed for uh by or for Elmo, I'm sure. I'm not I doubt they've used just used an off-the-shelf

**Dave Jones:** uh webcam type thing and just adapted some optics to it. I think it would actually be custom manufactured. I don't know. It's It's just rather neat. I like it. There's got to be a real good use for this. It's a shame

**Dave Jones:** that um the uh the working distance on this thing needs to be uh rather large cuz it's got that 16 time optical zoom in there. So, I don't know. Maybe you can put a secondary objective uh lens on there to halve that perhaps.

**Dave Jones:** I don't know. I like actually halve the working distance or something like that. But yeah, it's I don't know. If you can figure out what I can do with this thing, maybe a way to hack it and uh you

**Dave Jones:** know, rip off the camera, put it on a movable arm, and rip out the processor board, and embed it on the back of a screen or something. And I don't know. I reckon it's got to be usable for

**Dave Jones:** something neat. Perhaps PCB soldering cuz the update rate is near instant. So, it works really quite well. I like it. Hmm, I don't know. If you get any got any good ideas for it, let me know. And if you like the video, give it a thumbs

**Dave Jones:** up. If you like teardown Tuesday, it's not quite a it's a bit more than a teardown. It's sort of a you know, investigation into perhaps what this thing is capable of. Tickle me, Elmo. Catch you next time.
