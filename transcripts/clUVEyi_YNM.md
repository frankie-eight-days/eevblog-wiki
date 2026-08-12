---
video_id: clUVEyi_YNM
title: EEVblog #717 - How To Hack Vacuum Fluorescent Displays
url: https://www.youtube.com/watch?v=clUVEyi_YNM
source: youtube-asr
---

**Dave Jones:** Hi, today we're going to take a look at vacuum fluorescent displays or VFDs. We're going to have a little quick look at how they work on the whiteboard and then we're going to look at possibly getting a salvaged unit like this

**Dave Jones:** operational. Now, this one was sent into the mailbag segment. Sorry, I forgot who sent it in, but thank you very much and it is a complete vacuum fluorescent display module from a company called uh Babcock here and it's a custom designed

**Dave Jones:** by them. It's like a I don't know, count the number of characters by two lines and you've no doubt seen these vacuum fluorescent displays. They're common on audio gear and things like that. Incredibly common in the '70s and '80s

**Dave Jones:** for all sorts of gear, old old calculators and things like that used to have vacuum fluorescent displays and they've got lots of good qualities to them. They're they're really bright so they can be used in really high ambient light

**Dave Jones:** environments, but you can dim them really low as well and they just look beautiful. I think vacuum fluorescent displays. So, they're even still popular even today although they're quite delicate and fragile and they can age cuz hence the

**Dave Jones:** name vacuum fluorescent display. They are actually there is a vacuum inside there. You can see that port there that is the vacuum extraction port to uh suck all the air out of these things and they've got a glass top on them. So,

**Dave Jones:** yeah, they are a little bit delicate. This one's had a little chip taken out of it, but I believe the vacuum inside is just fine and dandy. So, anyway, you can get these in all sorts of salvage gear that people just toss in the

**Dave Jones:** dumpster and they can be really nice to actually reverse engineer them, get them up and running again and actually program them especially these dot matrix ones. They just look really good and this one's not only dot matrix, but it's got a cursor

**Dave Jones:** underneath as well, as you can see under each one. So, let's take a look at it, and hopefully we can get this puppy up and working and reverse engineer this interface here, figure out the protocol to make it talk. Let's give it a go.

**Dave Jones:** Very quick explanation time here of how vacuum fluorescent displays work, if you haven't seen them before. And we'll be able to physically see the construction of this inside the unit. I'll show you in a minute. Now, what we've got here,

**Dave Jones:** please excuse the crudity of this model, didn't have time to build it to scale or to paint it. We've got three different elements here to a vacuum fluorescent display. All this stuff is inside a vacuum, hence the name, vacuum

**Dave Jones:** fluorescent display. Now, on the bottom of the unit here, so this is the bottom, this is the middle, and this red one is the top here. On the bottom in blue, we've got our anode, and that is a

**Dave Jones:** phosphor-coated element, phosphor like your fluorescent tubes. Uh for your lights, for example, when electrons strike them, they actually fluoresce and generate light, and that's where the light is coming from. So, that's on the base of the display here,

**Dave Jones:** and I've shown like a 3x4 dot matrix display, but it can be a seven-segment display. Could be practically any unlimited weird shape you want. Um you just shape it in whatever thing you want, and it's a conductive element

**Dave Jones:** coated in a fluorescent material. Now, on top of that, we have a grid mesh, a very fine metal mesh, and that has to be as see-through as possible. Otherwise, you won't be able to see the light coming out from the anode elements on

**Dave Jones:** the back here. So, that's why the vacuum fluorescent displays have that sort of wire meshy kind of look look, you know, that sort of not completely solid look, cuz you're actually looking through a metal mesh, but it's a very important

**Dave Jones:** aspect to it. And then on top, you've probably seen these if you've looked at vacuum fluorescent displays, you'll typically have two wires strung from end to end. In this case, we'll see them actually run all the way over all of the

**Dave Jones:** individual characters on our dot matrix display here. So, these are just two wires on top and this is the cathode and they're made of a tungsten wire and they're the things that actually emit the electrons. So, these things work

**Dave Jones:** exactly like old school triode valves. We've got ourselves the cathode filament here. So, you put in a usually an AC voltage on that and that generates heats up and generates electrons. They burn off the surface and then they can head

**Dave Jones:** towards and bounce off the fluorescent material on the anode. So, what we do I've I've shown these three here in the different cuz they're physically constructed like this. In this case, the cathode at the top, it's going to be

**Dave Jones:** negative potential compared to the anode down here. So, we put a positive voltage on here relative to our cathode filament here and bingo, our electrons peel off here and if assuming that the grid is not there and doing anything and

**Dave Jones:** they're attracted towards the positive anode down here and of course when an electron hits that fluorescent material, it glows and the entire surface of that that particular element or whatever the shape the seven segment display or you know a little animal or

**Dave Jones:** something on there. You can have any shape you want. So, when you've got a grid here like this in the middle, you put that at the same positive potential as the anode down here and the electrons being emitted by the cathode can just go

**Dave Jones:** straight through the grid and fluoresce the anode. But, aha, if you want to turn that particular segment off, i.e. that dot off on your seven segment display or on your dot matrix character display, then you just put that to the same negative

**Dave Jones:** potential as the cathodes and then the electrons are still coming off here, but they're just going to bounce back like that. They're not going to get through to the anode, so the anode doesn't glow. And bingo, by controlling the voltage on

**Dave Jones:** your grid here, this inner material, then you can uh determine whether or not you're going to turn your your individual elements of your anodes are going to turn off or on. And what sort of voltages are we talking about

**Dave Jones:** here? Well, this filament here will be typically around about 4.5 V RMS for example might be a typical filament supply value. And so that is an AC signal there to generate the electrons. What do we need to the anode? Well, the this positive

**Dave Jones:** potential here relative to this cathode up here, you're talking about 20 V or thereabouts, maybe up to 30 V, maybe as low as 15, maybe 15 to 30 is about a typical range for that. Now, the voltages can actually be a bit higher

**Dave Jones:** here and they can be lower here for the filament drive voltage, for example. We're just talking like ballpark examples here. And as you might suspect, the filament current here, because it's just a tungsten wire, is going to be

**Dave Jones:** quite high current. So, it's going to be responsible for the main current draw of one of these vacuum fluorescent displays. And of course, on something like a dot matrix display here, you're going to be driving these as a

**Dave Jones:** multiplexed display. You're not going to drive these statically with each one. So, maybe like a seven set a single seven segment display you might drive statically, for example, but even when you got say, you know, 10 seven segment

**Dave Jones:** display characters, then you're pretty much going to drive a multiplex just like you would a regular LED display. But of course, the problem with the high voltages here is that you can't drive these with your typical TTL logic. You

**Dave Jones:** probably can't even drive these with 4000 series CMOS up to 15 V, for example. You might be able to get away with it. I think some people have actually done that, but you pretty much need discrete high voltage transit

**Dave Jones:** either individual transistor drivers for these things or dedicated VFD display driver chips, which you'll find typically on one of these things. They won't be using discrete transistors here. So, that's the annoying part about vacuum fluorescent displays is that if

**Dave Jones:** you don't actually have the controller attached or it and actually as we're going to try and do here actually reverse engineer the controller and figure out how to drive it, then if you've just got the vacuum fluorescent display with the bare pins sticking out,

**Dave Jones:** then you're really got your work cut out for you. You've got to do the high voltage drivers, the multiplex, you've got to do the fill AC filament supply and all that sort of stuff. And well, it's you can argue it's not really worth

**Dave Jones:** the effort. That's why we're just going to do one that's sort of like an off-the-shelf full like controller even though we have no idea how you know, no specs, no data sheet for it. But, the good thing is is

**Dave Jones:** that they've got the drivers built in. Typically, they're going to be like a serial or a parallel digital interface with some sort of microcontroller, especially in the case of this one here where we've got a you know, a 40

**Dave Jones:** character by two line dot matrix character display. There's got to be some sort of microcontroller in there to drive that. So, the interface should be relatively straightforward. So, that's the plan. Haven't actually tried it yet. So, I guess if it doesn't work, you might

**Dave Jones:** not see this video, but anyway, let's go over to the bench, see if we can actually get this get some characters on the display of this thing. So, if we have a look inside this Babcock vacuum fluorescent display, we'll see exactly

**Dave Jones:** the same elements that we were talking about on the whiteboard there. There you go, you can clearly see the cathode tungsten wires going across the top like that. You can see that they're physically on the top due to the

**Dave Jones:** parallax there. And you can see that they're all joined down to this metal strip here. So, they're all electrically connected and also to the ones up here. They've just got three going across like that. Um, it's very common to have uh

**Dave Jones:** two, for example, but these are relatively high, so they've decided to put three on here. So, we're obviously going to have one pin on the vacuum fluorescent display, probably on the corner here. If we have a spin it

**Dave Jones:** around, aha, there we go. It's likely that one. You can see some metal branching off there and then through. So, that's very, very likely to be the uh the top part of that uh cathode filament there. And that is confirmed if

**Dave Jones:** we flip it over like this. Ta-da! There's that thicker trace going all the way with LBJ across here and down to this part of the circuit. And there we go. That's our generator. There's our It looks like we've got ourselves a little

**Dave Jones:** uh transformer there, do we? Yep, so that's generating our uh likely AC uh supply voltage for our um cathode there. And the other one, bingo, is likely to be that corner pin there. So, no surprises whatsoever. And that would be a typical pinout on one of

**Dave Jones:** these vacuum fluorescent displays. Of course, you're going to have the uh cathode either side like this. So, you're going to have one pin here and one pin on the other side. Pretty easy to find those. And then the other really

**Dave Jones:** interesting thing is that you can see the grid down in there really very clearly. And each one is separate. You can see electrically isolated between these two characters. So, these two characters on the top and bottom display are sharing the one grid there. And if

**Dave Jones:** you move the display around like that, you can actually see that the grid is actually sandwiched between the anode and the cathode as we saw on the whiteboard. And then the anode driver chips are Texas Instruments TL4810 and I'll link in the data sheet uh down

**Dave Jones:** below. These are nominal uh 60 V output uh rated, I think 40 mA uh current uh capability as well. So, these are, you know, typical VFD uh display driver chips. They've got uh five of those here um outside the display and hidden under

**Dave Jones:** the display, which we can't see, there's another seven of them, I believe. So, on the board itself, we have the vacuum fluorescent display module, which is all uh socketed, very nice. You could actually lift that out, but imagine the

**Dave Jones:** pin force actually required to uh lift that out. Geez, without uh breaking off the uh um breaking the glass uh top on there, I wouldn't like to attempt to do that only if you had to. You certainly wouldn't just lever it up at one end and

**Dave Jones:** woo, hope it comes out. That is an absolute monster. We've got our um filament and uh high-voltage uh display driver over here. We've got a bodged sort of heat sink um just bent over the edge there like that. Anyway, this is designed to

**Dave Jones:** go into a bit of gear, so it doesn't really matter. Uh power input, which we'll take a look at. We've got those display drivers I talked about. There's another seven under there by the looks of it. So, there you go. There's a whole

**Dave Jones:** bunch of them. They're just um and by the way, uh serial input uh latched output uh driver chips, 10 individual outputs. And then we've got ourselves a processor here, which is a um a Babcock uh branded one. By the way, the

**Dave Jones:** date code of this board and the chips on here um end of 1989. So, yeah, a good 25 years old this board, but hey, I think she's still going to work. Um 12 MHz crystal. This is probably like this will

**Dave Jones:** not be a an a Babcock uh custom ASIC. It'll just be like a uh programmed micro uh controller from the era 8051 or something of that equivalent. So, the first thing we need to do is figure out how to power this thing. I did show this

**Dave Jones:** in the mailbag video. I did actually power it up. And well, there's only one input connector here unless you count power coming through here, which I don't think so. I think it is completely powered from here. It's a dead giveaway,

**Dave Jones:** the big pins and the big filter cap. So, how do you determine the pin out on here? There's no silk screen like this. Well, you look at the cap. You can see the negative of the cap. It's the pin on

**Dave Jones:** this side. You can see that that trace is going over to this pin. So, this pin is going to be the negative input. This pin here is going to be the positive input on the left here. So, there's no

**Dave Jones:** input protection there at all. And then, what voltage are we going to have here? Well, it's pretty darn obvious. I don't see much in the way of regulation, although something like this could be a discrete transistor regulator, but I don't think

**Dave Jones:** so. I think that's driving the transformer up in there. So, really, I think it's going straight across the chip. And what we can do is get the 5-V. Of course, we're talking like, you know, a 1989 vintage chip here. Nothing's

**Dave Jones:** going to be 3.3 V on here. It's all going to be 5-V logic. The micro, of course, is going to be 5-V. So, it's a safe bet to say that this is a dedicated 5-V in. But, you can

**Dave Jones:** actually measure that. So, our positive input there, pin 40 of this micro here, which is most likely There we go, to be 5-V and bingo, it is. And then, you can check the ground over here between the ground pin and bingo. So, our input here

**Dave Jones:** is directly across this chip. You know, it's going to absolutely be 5-V. No worries at all. So, how would you power up a board you've never powered up before safely? Well, we go to channel three here. We've set it to 5-V, of

**Dave Jones:** course. And then, our current limit, look, I if you wanted to be game, you'd set it to 1 amp, say. But, hey, let's go 0.1 amps like that. So, that'll set our current current limit. and then we can

**Dave Jones:** switch this sucker on. And we can see that No, it's dropped down to 5 V. So, it's hitting that 100 mA current limit there. And well, you know, it obviously needs more current than that. A huge vacuum fluorescent display like this is

**Dave Jones:** going to draw a whole lot more. So, hey, switch that off, and then we'll whack that back up to 1 amp current limit. Switch it on. And yeah, we've got a 5 V. It's drawing you know, 777 mA there.

**Dave Jones:** That's a nice number. I like that. And tada! Let's have a look. It is flashing. Look at that. We've got our digit over here. Be careful of the uh high voltage uh circuitry on this side. Don't want to go poking around there.

**Dave Jones:** But look, we've got ourselves a blinking cursor. So, that's obviously to do that uh requires that this uh micro actually work here. That So, it powers up. It's doing something. It's driving all the serial drivers. It's doing the right

**Dave Jones:** thing. And you wouldn't get that if the vacuum in here was uh uh you know, leaked out and there was no more vacuum. So, the vacuum fluorescent display is working. The micro is working. Everybody's happy. All now we've got to do is figure out the uh

**Dave Jones:** interface over here. So, let's take a look at this card edge connector here, and it's going to either be a serial or a parallel interface. Um not likely to be both. But look, you can see all the pins on this top side are all shorted

**Dave Jones:** together. Look at that. All except that one going off over there to a little jumper link E7 E5 E6, whatever the hell that means. But anyway, there's a jumper link in there. Maybe we can experiment with that later. But all of those uh

**Dave Jones:** shorted out, so they're likely ground. We can measure those, of course, before we go hooking up to the thing. And look what we've got here. This is our micro, of course, on the bottom. And we've got 1 2 3 4 5 6 7 8 8 pins going off to the

**Dave Jones:** micro in one bus. Bingo, that's going to be an 8-bit IO port on the micro. Absolutely no doubt about it. So, and then we've got these ones here going off. That's actually a pull-up resistor network there. Oops, better be careful

**Dave Jones:** flinging this thing around, flipping it over. You can hear the tungsten wires inside go twang. So, we've skipped a pin on our micro there, and these other ones up they've got presumably pull-up resistors. Once again, we can measure that to see where

**Dave Jones:** the resistor network goes there. But, so we've got 1, 2, 3, 4, 4 other inputs here. So, it's got to be some sort of parallel interface. So, there's going to be a parallel interface, there's going to be like a parallel 8-bit data port like

**Dave Jones:** this, which will no doubt take the ASCII character. You would do it in ASCII just because like if I was the design engineer and they said, "Design us a VFD module with an interface like this that I'll have to hook up to something else,

**Dave Jones:** you know, in parallel whatever." How would you do it? Well, you got to the ASCII code, the 8-bit ASCII code or 7-bit, 8-bit ASCII code straight on there. Bingo. You'd most likely have some sort of latch load line for

**Dave Jones:** example, something like that. You would probably have a reset line in there that reset the whole display because this micro is of course going to have the buffer inside. It's going to buffer all the characters that you send to it.

**Dave Jones:** And then a couple of other pins, I don't know what they're doing. Maybe there's some other serial interface, but no, I mean, I doubt it. I don't know what the other pin's for, but anyway, I think there's got to be some sort of

**Dave Jones:** latch load pin with an 8-bit interface and a reset line at a minimum. And a very quick check, is that a pull-up or a pull-down network? It is a pull-up network, no surprises. That would have been my guess. And I soldered some pins

**Dave Jones:** on there. The good thing about a card edge connector, exactly 0.1 in. So, um some more usable headers uh because these are all ground pins on here. I've actually um put on three ground pins here. That's just handy. You never know

**Dave Jones:** when you have to attach uh various, you know, like logic analyzer grounds and uh things like that. So, it's worth putting a couple more on there. Didn't want to do the whole row, but at least have more than one. And I said before I don't

**Dave Jones:** think any of those uh pins on the side are outputs here, but uh hey, just to probe them cuz we don't want to go uh injecting signals into this thing without uh uh you know, at least start doing some

**Dave Jones:** basic checks. So, um of course those data pins there uh they're all going to be inputs. So, I'll check the other ones. There's our 5 V. No, that's just the uh pull-up. So, it's not I'm pretty darn sure it's not

**Dave Jones:** actually outputting that uh uh 5 V. Otherwise, there'd be no reason to have a pull-up there. The reason you'd have a pull-up is because it's an input. So, um oh, we've got a curious-looking one. Look at that. We're getting getting

**Dave Jones:** some frequency there. What is that? It doesn't uh it's not it's not telling me. It's not displaying that uh frequency. We can AC uh couple that. There we go. I've AC coupled the uh input channel here and bingo, bang on 12 MHz.

**Dave Jones:** Aha, let's trace this sucker. I think I know what this is. Now, the pin is actually on the bottom side there and it pops up through this via and you can see the trace goes around here, around here,

**Dave Jones:** snaking its way around there, around the crystal. And I I lose it after that point, but I was able to buzz it out and it actually goes to pin uh 39 there of this uh 40-pin micro. So, it's no surprises that we actually see

**Dave Jones:** 12 MHz on here. What we're getting is just some stray capacitive coupling between that trace and because it's running right near the crystal there. And obviously, it's an input because if it was an output, it'd be fairly, you

**Dave Jones:** know, it'd be low impedance drive on the output. So, it wouldn't be the just a stray capacitive coupling wouldn't be enough to get that sort of amplitude which we're seeing which was, you know, 300 400 mV or something like that I

**Dave Jones:** think it was. Um on pin. So, that one is most likely an input pin rather than an output. Would you believe it? Would have been absolutely perfect just to plug an Arduino straight onto there like that on this pin header, but it's the bloody

**Dave Jones:** incorrect 0.1 mm pin spacing there that screws it up. Damn it. But hey, nothing you can't fix by simply resoldering those on a staggered arrangement with that pin there. And there we go, it fits on nicely. There's just enough room there staggered wise to

**Dave Jones:** actually get those pins and solder directly in. So, that's a really neat solution. Look at that. I can just drive those digital inputs directly. All I got to do is hook up a ground. Awesome. And check it out. That is the complete

**Dave Jones:** interface. We've got all our lines. We've got this is the ground line running over here like that. And we've got all of our digital lines there. And we've got that extra input that we saw that had the floating

**Dave Jones:** line that went next to the clock. That one's going all the way all the way over there like that. So, this is really neat and tidy. We can just plug our USB straight into there, our 5-V power on

**Dave Jones:** the main board, and wow, Bob's your uncle. Away we go. And we've figured out the reset pin on here without even doing anything. Look, I got it turned on. There's our cursor. And we haven't even got the Arduino plugged in, but

**Dave Jones:** look, there we go. So, we're resetting. So, it looks like that extra pin over there is like some sort of reset/blanking line, something like that. And if you're curious to see what the uh filament supply voltage is, well, we can measure

**Dave Jones:** straight across that, but um be very careful when you're probing around uh non-ground referenced uh circuits like this. At the moment, we don't have the Arduino hooked up to the USB here. So, this is and it's hooked up to well, a uh

**Dave Jones:** floating Rigol supply. So, it's completely floating uh system relative to mains earth. So, we can safely put our ground point on any part our ground clip lead of our silloscope, which is connected to mains earth, here. But, if

**Dave Jones:** we once we plug in the computer here, I've done a whole video on this. It's called how not to blow up your silloscope, and this is one way to do it. When you plug in your USB on here,

**Dave Jones:** the ground is uh mains earth referenced most likely for through your computer, unless you're completely using an isolated uh battery-powered laptop. So, anyway, we can get in here, and we can probe. These are the two pins on our uh

**Dave Jones:** filament. There we go. And the average value you can see in the bottom uh left-hand corner there, 6.8 volts. That's actually uh reasonably high for a an RMS uh uh voltage. Anyway, you can see it's not a sine wave. It's just a uh square wave,

**Dave Jones:** that's which is just fine. That's very typical. And bingo, look at that. I found our flashing cursor. You have to look through all the pins. Of course, it's going to be in the physical vicinity down here. It had to be sort of

**Dave Jones:** on this end of the display where it's actually flashing. And uh sure enough, there we go. There's our lip lip lip. And of course, it's going to be a multiplex display, so that's why we're getting the frequency there. And that's

**Dave Jones:** being multiplexed at the like a you know, 60 hertz or something like that. So, there you go. You can see the on-off burst like that. And uh of course, it's multiplexed in that part down in there, and then it's just completely switched

**Dave Jones:** off down in that part. So, there you go. And of course, by adjusting the uh duty cycle and the frequency in there, you can adjust the uh brightness of the display. Oh, and I forgot to mention the voltage um we're at 20 V per divisions

**Dave Jones:** here. So, this is a particularly high-voltage board. So, it's like 40 Look at that, like 45 V or thereabouts. So, yeah, pretty high. By the way, I just wanted to mention, even if you couldn't figure out like the uh proto-

**Dave Jones:** the interface protocol to this micro or uh anything like that, um you know, it's not as long as you work out it, you should be able to get it. But let's assume you can't. Hey, you can just suck

**Dave Jones:** that thing out. And as I said, these are just serial input uh VFD drivers. So, we have the data on these. We've got the pinouts. We can just figure out where the input chain is to the serial thing

**Dave Jones:** and just drive them directly with our own micro or with our Arduino or whatever you want to use. So, you know, you don't really have to reverse engineer this if you don't want to. Now, check it out. This is my first shot at

**Dave Jones:** an Arduino sketch here. And I've just uh basically put the uh letter H on the uh data line here. And I haven't even got in there and um set all the pins. But uh by default, because of that pull-up

**Dave Jones:** resistor on there, those are what I think are those four uh control lines. I've only done um uh pin number one on the Arduino there. I've just set it low four times. I haven't even um I just uploaded it, and look what I got. Ta-da!

**Dave Jones:** I got lucky. Look. Um it looks like that pin one is some sort of test pin or something. Obviously, when you pull it low, when I first hooked up the Arduino, powered it on, it didn't do anything. All I got was the cursor, because that

**Dave Jones:** pin was being pulled high by that resistor network there. But um obviously, when I've pulled that pin one low, look, it's going into a test sequence where it just writes all the characters. So, that's not my Arduino sketch doing that. That's the building

**Dave Jones:** processor in there actually got a test routine. So, bingo, I found what one of the pins does. Pin one on my Arduino, I got to figure out which pin on there. But anyway, that is the test pin. Awesome. Sometimes you get lucky like

**Dave Jones:** that. In fact, that probably should have been Well, it sort of was going to be my first step is to actually just start toggle each one of those pins low and high. But I just downloaded the sketch to make sure the Arduino worked and it

**Dave Jones:** was all hooked up to my Arduino and bang, I got lucky. Beauty. So, what I'll do is I'll just change that here from low to high and I'll recompile, re-download that and we should see that actually stop. And bingo, yep, it's stopped and now

**Dave Jones:** it's it's doing Wait. Look, every Yeah, it was doing something funny there cuz the Arduino was pulsing all the lines, etc., etc. So, but look, it's actually stopped updating that now and if I put that back low, this is a crude way

**Dave Jones:** to do it. Of course, you could, you know, have buttons or do do whatever. Um, but let's just download that again. And they It's downloading the sketch. Doing silly stuff. See it pulsating there and bingo, we're back to the

**Dave Jones:** scrolling test mode. Awesome, where it prints out all the ASCII characters embedded in that thing. Fantastic. So, processor is definitely working as we suspected where it would, of course. We got the cursor there and it's printing out the entire

**Dave Jones:** character set. Absolutely brilliant. See, I wouldn't have immediately guessed that one of those was a test line. It's Yeah, it's something that the designer may or may not have included and it's not something that you'd first guess, but hey, sure enough, it's Hey, the

**Dave Jones:** designer was thinking, I need to test these things in production, of course. So, hey, what do you do? Have a pin. Just strap it low on on there to test the modules in production. Of course, you got to have a a test routine like

**Dave Jones:** that built in. But yeah, we found it. No worries. It's pin number one on the Arduino, whatever it goes to. Now, I'll go in and toggle the other pins and see what happens. And like I said, I expect

**Dave Jones:** another line to be say a data latch line or something like that. So, it's not latching any data at the moment. It's just toggling that one pin. Bingo, check it out. I'm starting to write there. And what I did there is I just uh

**Dave Jones:** uh started out like each pin I just toggled low for 100 milliseconds there. And I finally got to the point where it well, pin three on the Arduino, that's the thing that actually latched in the individual data. So, I should be able to

**Dave Jones:** get this to display anything. I still don't know about the other pins. I was just sort of randomly I tried setting them high first. So, I had all of the all of the control lines high and then I was

**Dave Jones:** toggling each one low and that didn't seem to work. But it seems that if I keep them low, they're all of them low and then toggle pin three high, bingo. That's the data latch pin just as I expected. And of

**Dave Jones:** course, I'm only putting in a H at the moment. And yes, it is an ASCII character cuz I put in at the top of the Arduino sketch I put in the binary representation on the data port pins over here for the upper

**Dave Jones:** case H. So, which is 72 decimal I think it is. So, there you go. I should be now able to just produce any text I want on the screen. So, I know what the reset pin is. We figured that out before we even hooked

**Dave Jones:** up the Arduino. We now know what the test pin is. We now know what the latch pin is. I've still got to figure out what the other ones are. But each time you latch in a data, it just shifts the character to the next

**Dave Jones:** location. That's pretty much how I expected something like this to work. It could be a really dumb display. Like there may be no like a control thing as I said where you can actually set the cursor location. Um I don't know. But at least I've got

**Dave Jones:** it up and running so I can clear the screen and display text. That's the main thing. That's basically working. And of course you don't need an Arduino to experiment like this. I could have just wired on some dip switches or some

**Dave Jones:** toggle switches on onto a panel and then just you know toggle all the switches until I until I got it to do something. You know, so whatever floats your boat. And of course I was writing data to it very slowly

**Dave Jones:** before and by default I was pulsing the latch line like for 100 milliseconds as I said. Like you start off really slow like that because you don't know on these unknown systems that you're trying to debug how fast or how capable they

**Dave Jones:** are of actually processing those as I suspected an input latch. So you start out something really slow, you know, like 100 milliseconds, something like that. Now I've dropped it down to 10 milliseconds and it's still latching the data just fine and you can push it and

**Dave Jones:** push it and push it until you find the limits if you want to actually you know push the speed limits of updating this thing. But it's just a display, it doesn't matter. But that is relevant to other things you're trying to debug

**Dave Jones:** though. And by the way I still haven't figured out whether or not it's actually a low to high transition of that pin or high to low. I haven't figured out the polarity. You'd have to you know play around with the code on a one off basis

**Dave Jones:** to see when it actually updates. But yeah, that's no problem. And of course I just happened to guess the correct order of the bits like for the data bus. So what which was the least significant bit, which was the most significant bit. Used

**Dave Jones:** a bit of intuition there in that it'd be in a certain direction based on the layout and stuff like that. If I actually figured out exactly what that chip is and you could have got it'd be on an 8-bit data bus port most likely

**Dave Jones:** can figure out uh, way. But yeah, I mean it would have fairly obvious if I started writing in data in there which was, um, sort of, you know, garbage but the same each time, then I would have flipped the bits and and figured it out

**Dave Jones:** that way. So, it's not too hard. I got relatively lucky based on an educated guess. And how do I know if I've got the, uh, polarity of that clock pin wrong? Well, I've written my, uh, little string passing routine here and I'll

**Dave Jones:** restart this thing and you'll see that here we go. Ta-da! It's missing the H at the front. So, obviously, the, uh, bits aren't toggled correctly. So, I've to get that first byte. So, it's fine after that. So, yeah, I obviously got that, uh,

**Dave Jones:** clock pin. It's not active low. It looks like it clocks the data in on active high. So, I've changed that around and bingo, there it is. Hello world hacked by the EEVblog. We got our H right at the start. So, that's how I knew I had

**Dave Jones:** those, uh, bits um, the edge there back to front. No worries. So, there you go. I'm pretty, uh, happy with this that yeah, we basically hacked this thing and easily figured out, uh, the, uh, well, some simple protocol here. It was just a

**Dave Jones:** parallel data, uh, input latched. As I suspected, it could have been much trickier than that. But, hey, you know, I I put the odds at like, you know, 80 90% pretty high that that's what it was going to be. Why? Because that's how I

**Dave Jones:** would have designed it. Now, I've had a bit of a play around with the other, uh, control pins on here and I can't really get it to do anything obvious. Tried all various combinations and, well, yeah, I don't think I want to spend too much,

**Dave Jones:** uh, time on it at the moment. Maybe if I had a really good, uh, use for this thing that I'd actually, um, pursue that and figure out exactly what those, uh, pins do. They may do nothing. Hey, it

**Dave Jones:** may just have that simple ability to, uh, reset the cursor like that and just, uh, wrap from the 40th character over to the 41st and that's it. So, you know, you could try and you know, debug this thing until

**Dave Jones:** the cows come home to figure out what those extra pins do and they may do well and truly nothing. So, anyway, I've got it to a usable point because you can always print a string of 40 characters there even if you want you know, just

**Dave Jones:** something here and then something here or something in the middle. You can just do that in software. So, as it stands it's completely hack completely usable. So, I'm very happy with that. So, I'll leave it at that. So, I hope you enjoyed

**Dave Jones:** that little reverse engineering / hack video of getting a VFD up and running. Anyway, the video's been much longer than I intended. So, there you go. I waffle on too much. I am the waffle master. But anyway, if you like

**Dave Jones:** that, please give it a big thumbs up cuz that helps a lot and if you want to discuss it, jump on over the EVblog forum. Leave YouTube comments, leave EVblog.com comments, all that sort of stuff. Catch you next time.
