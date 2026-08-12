---
video_id: t6pLlA5YfSs
title: EEVblog #182 - Rode Videomic Shotgun Microphone Hack
url: https://www.youtube.com/watch?v=t6pLlA5YfSs
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EEV blog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host Dave Jones. Hi. Now, this episode might sound a little bit different. It's because I'm not using my regular shotgun video mic

**Dave Jones:** because, well, I'm going to mod it for this episode. So, I'm using my old shotgun, my real cheap ass JR1 that I uh used to use very early on in the blog. But this is the one I've been using for

**Dave Jones:** a long time now. It's a road video mic uh designed and built in Australia here in Sydney. Fantastic. It's one of the best quality uh video microphones for your camcorder you can get on the market. Professional, semi-professional, whatever. It's awesome quality and it's

**Dave Jones:** cheap. It's only like 150 bucks or something. It's an absolute bargain. And uh there's one real annoying aspect with it for video bloggers like myself who sit in front of the camera all the time. I'm hardly ever behind the camera. Uh

**Dave Jones:** not when I'm not when I got my head on the uh on the box anyway. And that is the uh the power LED on it. Something as simple as that. Now on the back here, it's um got an onoff switch. There it

**Dave Jones:** is. and a um a highpass filter as well to take out uh low frequency uh you know rumble and stuff like that if you're using it driving along in a car or something. It's got a filter and well

**Dave Jones:** anyway you switch it on and uh sure enough it uh it goes it goes red at first but then it goes green to tell you that your battery is good and you don't have to worry about your microphone

**Dave Jones:** level at all. And if the lead goes um red, then well, you know, to change your battery because your mic levels could drop because you don't have headphones on. Well, I don't when I'm actually monitoring this blog. So, I'm just

**Dave Jones:** hoping that the video is good. And sometimes I sit here in front of the camera and I forgot to switch the damn mic on because I can't see the power LED or I forget to switch it off afterwards

**Dave Jones:** and I drain the battery. It's got a pretty good battery life anyway. It's like 100 plus hours or something. I get like, you know, 40 episodes or something out of one battery. It's pretty good. Um, but it's just annoying. So, I

**Dave Jones:** thought I'd mod it to put an LED on the front so that I could see it. There it is. I've already done the mod, but uh we'll actually see that. So, I've added that little green LED on the front

**Dave Jones:** there. Very simple mod, but anyway, I thought I'd take it apart and just uh show you the mod. So, here goes. And uh if you're After a video mic like this, I highly recommend it for your camcorder. It's got a standard 3 and a half mm uh

**Dave Jones:** attachment. Best quality on the market. Uh really hard to beat. It's got these lovely It's got this lovely uh rubber O-ring shock mount system like this. There's actually I think there's just a brand new one on the market. Um not sure

**Dave Jones:** if it replaces this, but it's the Video Mic Pro. So, uh check that one out. sort of like a shorter type thing because this thing can look pretty damn intimidating when I got it sitting on top of my tiny little camcorder which is

**Dave Jones:** my Seno camcorder which is only about that long. Um, so it looks really out of proportion to my camera. But hey, when's that ever been a problem, right? Anyway, here we go. And I've taken it apart. It required a fair bit of effort. There's a

**Dave Jones:** few uh clips and things you got to undo. And there's an a uh sticker on the back here which has um which has the where where the switch actually protrudes and that's actually uh stuck on to the back

**Dave Jones:** half uh to the other half of the unit here. So um you can actually just sort of hinge it off while it's still attached. But I just decide to um unstick that from the other side just so it comes permanently

**Dave Jones:** apart. And if you're wondering what's inside one of these shotgun mics, well here it is. No surprises, just a discrete uh transistor preamp circuit. You don't need much at all. Going off to the microphone insert, which is actually

**Dave Jones:** just in the back here. This um tube up here literally is just a tube. I don't know if you can probably don't know if we can actually get the camera down in there, but the um element is actually

**Dave Jones:** right down this end of the tube. And the tube just literally is a uh hollow tube or or it is actually designed with um slots inside like that. So yeah, I don't know the acoustic uh pattern of how all

**Dave Jones:** that works. You'd have to really be an acoustics expert to uh understand the lobe patterns and all that sort of stuff. But anyway, um there's not much in a basic shotgun mic at all. It does have um a three-stage um sort of like a

**Dave Jones:** filter on the front like that. So, it's that actually uh wedges and that actually slides in the front there. And of course, the windshield just pops over the whole thing. And here's our preamp board here. And what we interested in is

**Dave Jones:** the LED, which is under this light pipe here, which actually uh bends the the LEDs, the surface mount PLC package on the board. And these light pipes just uh trap the light inside and then bend them around and focus them and they shine out

**Dave Jones:** the end here. That's how you can get an LED on the end of your panel without actually having to bend it up off your board or mount on the back panel and wire it across. These are very popular,

**Dave Jones:** these light pipes. They come in all sorts of uh shapes and sizes. And as you can see, it's um it just uh actually clips into two holes on the board. And bingo, there is our uh PLC package LED.

**Dave Jones:** It's a standard uh four pin PLC package. It's got red and green because it's got uh this device has multiple colors and to show you the state of the battery. Green is full and red is low battery. Now, if we plug our battery in here,

**Dave Jones:** you'll see that there's two physically two dyes inside there. The top one is the red one. If you see that little die inside the device, that top one there is the red and the bottom one is the green.

**Dave Jones:** Now, the pin outs for these, if you actually look through, you'll be able to see the bonding under a microscope, you'll be able to see the bonding wires go across from the internal uh dye in there over to the external pad. So, the

**Dave Jones:** bottom one is the green one and the top one's the red. So, the the two pads on the bottom will be the green. So, and the two pads on the top will be for the red. They're two separate LEDs in the

**Dave Jones:** one package. And clearly uh these two these two surface mount resistors here are the uh lead dropper resistors. The top one for the red and the bottom one for the green. But I'll just measure that with the multimeter just to make

**Dave Jones:** sure there's continuity there. I think I can see it. There you go. You can see the little trace there even on this camera. So I'm pretty darn sure they're the dropper resistors. So what we need to do is attach a um is attach our LED

**Dave Jones:** with its own dropper resistor from here across to here. So uh because you never wire LEDs directly in parallel because they're a nonlinear element and they'll have different voltage drops depending on uh which changes with the current and

**Dave Jones:** if they're not matched up one LED can hog all the current and it takes all the it'll it'll appear bright and the other one might appear dull or even completely off. So that's why it should have its own dropper resistor so that you

**Dave Jones:** adequately share the current between the two LEDs. So I'm wiring these LEDs in parallel but with their own dropper resistor. Now what I'm going to do is measure that dropper resistor value in there and also the voltage across it. So

**Dave Jones:** I will know how much current uh each LED or the green LED is drawing. I don't really care about the uh red. I just care about the green. So uh here is where I've got to hold it. Here's a

**Dave Jones:** tricky situation. I've got to sort of use a third hand holding the battery at the same time as probing uh two points holding the battery and watch the display at the same time. So, here's where your auto hold function on

**Dave Jones:** something like a Fluke meter really comes in handy. So, let's give that a go. And I don't even have to watch the meter. I can just concentrate on holding that battery in place with one finger and probing it with another. Let's get

**Dave Jones:** the probes around the right way just so we don't end up with a negative sign, shall we? Not that it matters. So, I'll put my probe on there. And bingo. 4.343 uh 4.534 vol. And uh if we measure the

**Dave Jones:** resistance, we'll do that with the power turned off. It's a 1k dropper resistor. And the resistor above it is yeah a 1k as well. So uh 4.5 volts across uh a 1k resistor. That means that LED is uh uh consuming 4.5 milliamps of

**Dave Jones:** current. They're driving it with 4.5 milliamps which is rather high for a uh 9volt battery but the battery life on this thing is quite decent. Anyway, so here's a basic Davec drawing of what we've got here. We've got our uh four

**Dave Jones:** pin PLCC uh dual red green diode here. Red up the top, green down the bottom. We've got two dropper resistors and uh some switch some switch over here, a transistor switch on this side over here to actually switch uh each one off and

**Dave Jones:** on. And we're just going to put another uh green LED here in parallel with it and with its own dropper resistor. As I said, we don't put them directly in parallel with that. And I've measured these at 1K each with 4 and a half volts

**Dave Jones:** drop across it. That means there's 4.5 milliamps uh flowing through the LED like that for it. You fly to the moon on that amount. So u this one I think I'll up it to maybe uh 2k2 or something like

**Dave Jones:** that. So I only get a tiny little 2 milliamps flowing through the LED. And that should be uh more than good enough. uh the little le 3 mm LED I plan on using. It should work at 2 milliamps.

**Dave Jones:** So, my goal is to stick a 3 mm LED on the front here, which means I've got to drill a hole, a 3 mm hole through this case here. And is there enough room on the other side? Well, if you open it up

**Dave Jones:** and you uh look in here, there's actually a wall. There's the uh there's the battery. There's a wall there that actually holds the battery in place, but there's enough room, I think, to actually put the LED in there and bend

**Dave Jones:** the leads immediately at right 90° and take them behind this wall here like Well, that they'll go behind the wall. It'll bend at 90° and I should be able to wire up through here onto my LED. Let's give it a go. There you go. You

**Dave Jones:** can never trust 3 mm leads these days. 3.05 05 mm. So, I think I'll use a 3.2 mm drill bit for that. Should work a treat. Right about there ought to do it. And that's just about perfect. I

**Dave Jones:** like it. And there you go. I've installed my LED with uh some heat shrink on the back of the wires. Bent it over there. And I put my uh 2K2 in series here in the lead. And heat shrunk

**Dave Jones:** that and let's turn it on and give it a go. Tada. There we go. Lights up green. No problems at all. And we're only wasting about an extra 2 milliamps from the battery to light up the LED on the

**Dave Jones:** front. Beauty. And when you're doing mods like this, sometimes you can't actually solder directly onto the point you want to. I couldn't solder uh directly onto the LED because it was under this light pipe. So, I had to just

**Dave Jones:** uh trace out where the track went. And I found the point over here on that SOT 23 package. So I use that one and also the top of the dropper resistor in there. There's one novel construction aspect to

**Dave Jones:** this. There's two screws which um hold the uh base of well actually screw into the base of the shock mount uh unit. And uh what they what they do is they actually use these little brass um inserts here and they actually slide

**Dave Jones:** down in there and line up with the hole in the bottom of the case. And it's really quite a nice little uh design concept. So, they just slide into these little uh recesses like that and they line up and then these come over and

**Dave Jones:** allow the screw uh to go through the shock mount unit which this attaches to into that brass insert. And it all snapped back together rather nicely. And you can see one of the uh wires up there. And it's quite neat. It just

**Dave Jones:** tucks in there like that. And let's try it out. Put it in. Got to put it in the right way. Tada. Green and green. Too easy. Check it out. Made in Australia. You bloody ripper. [Music]
