---
video_id: gZIRPJt69sM
title: EEVblog 1601 - How VFD (Vacuum Fluorescent) Displays Work
url: https://www.youtube.com/watch?v=gZIRPJt69sM
source: youtube-asr
---

**Dave Jones:** Hi. Today, we're going to take a look at vacuum fluorescent displays or VFDs. Now, this one was um sent into the mailbag uh segment. Sorry, I forgot who uh sent it in, but thank you very much. And it is a complete vacuum fluorescent

**Dave Jones:** display module from a company called uh Babcock here, and it's a custom designed by them. It's like a I don't know, count the number of characters by two lines, and you've no doubt seen these vacuum fluorescent displays. They're common on

**Dave Jones:** audio gear and things like that. Incredibly common in the uh '70s and '80s for all sorts of gear. Old old calculators and things like that used to have vacuum fluorescent displays, and they've got lots of good qualities to

**Dave Jones:** them. They're uh they're really bright, so they can be used in really high ambient uh light environments, but you can dim them uh really low uh as well. And they just look beautiful, I think, vacuum fluorescent displays. So, they've

**Dave Jones:** been still popular even today, although they're quite delicate and uh fragile, and they can age cuz uh hence the name vacuum fluorescent display, they are actually There is a vacuum inside there. You can see that uh port there. That is

**Dave Jones:** the vacuum uh extraction port to uh suck all the air out of these things. And they've got a glass top on them, so yeah, they are a little bit delicate. This one's had a little chip taken out of it, but I believe the vacuum inside

**Dave Jones:** is just fine and dandy. And this one's not only dot matrix, but it's got a uh cursor underneath as well, as you can see under each one. Very quick explanation time here of how vacuum fluorescent displays work if you haven't

**Dave Jones:** seen them before, and we'll be able to physically see the construction of this inside the unit. I'll show you in a minute. Now, what we've got here, please excuse the crudity of this model. Didn't have time to build it to scale or to

**Dave Jones:** paint it. We've got three different elements here to a vacuum fluorescent display. All this stuff is inside a vacuum, hence the name vacuum fluorescent display. Now, on the bottom of the unit here, so this is the bottom, this is the middle, and this red one is

**Dave Jones:** the top here. On the bottom in blue, we've got our anode, and that is a phosphor coated element, phosphor like your fluorescent tubes for your lights, for example. When electrons strike them, they actually fluoresce and generate light, and that's where the light is

**Dave Jones:** coming from. So, that's on the base of the display here, and I've shown like a 3 by 4 dot matrix display, but it can be a 7 segment display. It can be practically any unlimited weird shape you want. You just shape it in whatever

**Dave Jones:** thing you want, and it's a conductive element coated in a fluorescent material. Now, on top of that, we have a grid mesh, a very fine metal mesh, and that has to be as see-through as possible. Otherwise, you won't be able

**Dave Jones:** to see the light coming out from the anode elements on the back here. So, that's why the vacuum fluorescent displays have that sort of wire meshy kind of look, look, you know, that sort of not completely solid look, cuz you're

**Dave Jones:** actually looking through a metal mesh, but it's a very important aspect to it. And then on top, you've probably seen these if you've looked at vacuum fluorescent displays, you'll typically have two wires strung from end to end. In this case, we'll see them actually

**Dave Jones:** run all the way over all of the individual characters on our dot matrix display here. So, these are just two wires on top, and this is the cathode, and they're made of tungsten wire, and they're the things that actually emit

**Dave Jones:** the electrons. So, these things work exactly like old school triode valves. We've got ourselves the cathode filament here, so you put in usually an AC voltage on that, and that generates heats up and generates electrons. They burn off the surface, and then they can

**Dave Jones:** head towards and bounce off the fluorescent material on the anode. So, what we do, I've I've shown these three here in the different, cuz they're physically constructed like this. In this case, the cathode at the top, it's going to be a negative potential

**Dave Jones:** compared to the anode down here. So, we put a positive voltage on here relative to our cathode filament here, and bingo, our electrons peel off here, and if assuming that the grid is not there, and they're attracted towards the positive anode down here.

**Dave Jones:** And of course, when an electron hits that fluorescent material, it glows, and the entire surface of the that particular element or whatever the shape the seven segment display or you know, a little animal or something on there. You can have any

**Dave Jones:** shape you want. So, when you've got a grid here like this in the middle, you put that at the same positive potential as the anode down here, and the electrons are being emitted by the cathode can just go straight through the

**Dave Jones:** grid and fluoresce the anode. But aha, if you want to turn that particular segment off, then you just put that to the same negative potential as the cathodes, and then the electron electrons are still coming off here, but they're just going to bounce

**Dave Jones:** back like that. They're not going to get through to the anode, so the anode doesn't glow. And what sort of voltages are we talking about here? Well, this filament here will be typically around about 4.5 volts RMS for example might be a typical

**Dave Jones:** filament supply value. And so, that is an AC signal there to generate the electrons. What do we need to the anode? Well, this positive potential here relative to this cathode up here, you're talking about 20 volts or thereabouts, maybe up

**Dave Jones:** to 30 volts, maybe as low as 15, maybe 15 to 30 is about a typical range for that. Now, the voltages can actually be a bit higher here, and they can be a lower here for the filament drive

**Dave Jones:** voltage for example. We're just talking like ballpark examples here. And as you might suspect, the filament current here because it's just a tungsten wire, is going to be quite high current. So, it's going to be responsible for the main

**Dave Jones:** current draw of one of these vacuum fluorescent displays. And of course, on something like a dot matrix display here, you're going to be driving these as a multiplexed display. You're not going to drive these statically with each one. So, maybe like a seven set a

**Dave Jones:** single seven segment display, you might drive statically, for example. But even when you got say, you know, 10 seven segment display characters, then you're pretty much going to drive a multiplex just like you would a regular LED display. But of course, the problem with

**Dave Jones:** the high voltages here is that you can't drive these with your typical TTL logic. You probably can't even drive these with 4000 series CMOS up to 15 volts, for example. You might be able to get away with it. I think some people have

**Dave Jones:** actually done that. But you pretty much need discrete high voltage transit either individual transistor drivers for these things or dedicated VFD display driver chips, which you'll find typically on one of these things. They won't be using discrete transistors

**Dave Jones:** here. So, that's the annoying part about vacuum fluorescent displays is that if you don't actually have the controller attached or and actually as we're going to try and do here, actually reverse engineer the controller and figure out how to drive it, then if you've just got

**Dave Jones:** the vacuum fluorescent display with the bare pins sticking out, then you've really got your work cut out for you. You've got to do the high voltage drivers, the multiplex, you've got to do AC filament supply and all that sort of

**Dave Jones:** stuff. And well, it's you can argue it's not really worth the effort. So, if we have a look inside this Babcock vacuum fluorescent display, we'll see exactly the same elements that we were talking about on the whiteboard there. There you go. You can clearly see

**Dave Jones:** the cathode tungsten wires going across the top like that. You can see that they're physically on the top due to the parallax there. and you can see that they're all joined down to this metal strip here. So, they're all electrically connected and

**Dave Jones:** also to the ones up here. They've just got three going across like that. Um it's very common to have two for example, but these are relatively high so they've decided to put three on here. And the other really interesting thing

**Dave Jones:** is that you can see the grid down in there really very clearly and each one is separate. You can see electrically isolated between these two characters. So, these two characters on the top and bottom display are sharing the one grid

**Dave Jones:** there. And if you move the display around like that, you can actually see that the grid is actually sandwiched between the anode and the cathode as we saw on the whiteboard. And then the anode driver chips are Texas Instruments

**Dave Jones:** in the data sheet uh down below. These are nominal 60-V output rated, I think 40-mA current capability as well. So, these are you know typical VFD display driver chips. They've got five of those here outside the display and hidden under the display which we

**Dave Jones:** can't see, there's another seven of them I believe. So, on the board itself, we have the vacuum fluorescent display module which is all socketed, very nice. You could actually lift that out, but imagine the pin force actually required

**Dave Jones:** to lift that out. Geez, without breaking the glass top on there, I wouldn't like to attempt to do that only if you had to. You certainly wouldn't just lever it up at one end and hope it comes out. That is an absolute

**Dave Jones:** monster. We've got our filament and high voltage display driver over here. We've got a bodged sort of heat sink just bent over the edge there like that. Anyway, this is designed to go into a bit of gear so it doesn't

**Dave Jones:** really matter. Power input which we'll take a look at. We've got those display drivers I talked about. There's another seven under there by the looks of it. So, there you go. There's a whole bunch of them. They're just And the way serial

**Dave Jones:** input latched output. Look, it's going into a test sequence where it just writes all the characters. But anyway, if you like that, please give it a big thumbs up cuz that helps a lot. And if you want to discuss it, jump on over the

**Dave Jones:** EVBlog forum and leave YouTube comments, leave EVBlog.com comments, all that sort of stuff. Catch you next time.
