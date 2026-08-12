---
video_id: AozG9DfGVeQ
title: EEVblog #430 - Fluke 91 Scopemeter Teardown
url: https://www.youtube.com/watch?v=AozG9DfGVeQ
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Bit of vintage test gear yet again and it's a Fluke beauty. One of the original Fluke Scopemeter portable oscilloscopes. Uh vintage because it's 1996 or thereabouts. But jeez, you know, seems just like yesterday. '96, you got

**Dave Jones:** to be kidding me. But that was 17 odd years ago. So this thing is pretty ancient. Um you know, comparatively speaking. So this is the series two. Um so there was a series one before this. This is a 50 MHz Fluke 91 Scopemeter.

**Dave Jones:** Here it is. Um scored it on eBay for about 50 bucks. Bargain. Uh wasn't it was advertised as not working, but unfortunately, it does actually appear to work. So I was hoping to get a repair video for this thing. Uh once again,

**Dave Jones:** been foiled. Unbelievable. But anyway, should be really interesting to crack this thing open, have a look inside a 17-year-old portable Scopemeter. Let's go. Mhm. And here it is compared to a Fluke 87 five, which is not a small multimeter in

**Dave Jones:** its own right. So you can see how huge this beast actually is. Absolutely enormous. It's it probably not as heavy as uh you'd expect actually, but jeez, it it is absolutely enormous. I got some uh probes with it.

**Dave Jones:** These weren't uh advertised. Basically uh multimeter probes and oscilloscope probes as well. This is only the one channel model, which we'll take a look at. Um unfortunately, look, check out one of the leads. It's been Look at that. Chopped. Bummer.

**Dave Jones:** And it is the Fluke 91 Scopemeter series two 50 MHz analog bandwidth. Um sample rate? Mhm. Well, I'm actually uh not sure. It doesn't tell you the sample rate in the manual. This was uh back in the day when well, they thought uh

**Dave Jones:** people are a bit scared. They don't understand this sample rate stuff. They want these things to look and work exactly like a real scope. So, well, we won't bother telling you that. But, um so, it doesn't actually list in the

**Dave Jones:** manual on the specs what the sample rate for this thing is. But, based on the uh glitch capture of 40 nanoseconds, um you know, it's I think it's uh presumably that's uh um the sample rate. It's got to be at least 25 MHz or something like

**Dave Jones:** that. So, it's not a real-time uh scope as such in that uh the sample rate is not um you know, at least uh four or five times the input uh bandwidth, for example. But, uh you know, menu-based uh

**Dave Jones:** interface. The screen, it looks huge, but it's only uh 240 by 240 monochrome. No this color garbage. And uh of course, it's got multimeter and scope functionality as well. And if you have a look at the uh top here, um

**Dave Jones:** let's flip that around. You can see that this is only a single-channel model. I didn't actually know they came in a single-channel model, but apparently they do. There you go. And it's got regular uh scope inputs as well. And you

**Dave Jones:** can apparently add a generator output as well. It can generate signals as well. And it's actually CAT III uh rated, which isn't too bad at all. And apparently, you can use the common terminal in combination if you've got

**Dave Jones:** the uh dual inputs like this, you can actually use the common terminal in combination with the dual channels if you want to or something to that effect. So, anyway, um it should be interesting inside this thing to see what sort of

**Dave Jones:** technology it'll be uh um mostly uh predominantly surface mount or mostly almost all surface mount, of course, but probably um not integrated in uh one large chipset. So, there's probably going to be quite a bit inside this thing uh or most likely uh separate

**Dave Jones:** multimeter and uh oscilloscope boards as well. Uh that'd be my guess, but yeah, let's crack it open. Comes with this rubber boot of course, and uh on the back here I've taken off the uh battery cover on the

**Dave Jones:** back. Let's have a look in here. There we go. UL listed Fluke Scope Meter 9444. There you go. Is that the Is that a date code? Maybe? I thought it was uh 96 or thereabouts, but check it out, folks.

**Dave Jones:** Made in Holland. All my viewers from Holland. Beautiful. Um it there does seem to be some corrosion down on the contacts down here, and that's why it was sold as uh not working because the uh guy who sold it apparently um you

**Dave Jones:** know, whacked some uh C-size batteries in it, and uh it didn't work, so he just sold it as is. Now, as you can see, rather curiously, you can see that it's uh got an extra tab down here. This is for the

**Dave Jones:** rechargeable battery pack, so you can put in four regular non-rechargeable C cells, and of course, if it doesn't detect uh using that tab, then it won't um attempt to charge those. So, you can use two different types of packs there,

**Dave Jones:** and also, hey, you'll notice these two here marked 12 V and 0 here. That's for another pack which goes in, which isn't a battery pack, but that uh connects to a 12 V power source like an automotive uh power

**Dave Jones:** source or something like that. And um on the side here, we've got a um a really deep uh DC input jack and an opto-isolated interface as well, just a infrared uh transmitter and receiver via serial, I'm sure. So, yes, although this

**Dave Jones:** is a uh 50 MHz analog bandwidth, uh scope, its single-shot bandwidth is uh going to be pretty poor, unfortunately. Its response is probably going to update rate's going to be uh very poor as well, I'm sure. And the uh sample memory,

**Dave Jones:** woah, hold on to your hat, folks. Uh Uh 512 bytes. Yep, bytes. And that's the uh optional high-res mode, 512 samples. Normally, it's only 256 samples, but you can punch a turbo button and double that. Woohoo! So, let's crack this thing open and uh

**Dave Jones:** we can actually get in here with a flathead, believe it or not. And looks like this panel, this end piece, is going to lift off and that uh and then there's only two other screws, by the looks of it. So,

**Dave Jones:** that should Hop. Yep, there we go. Bingo. Oh, look, we've got little rubber surrounds on there to keep the dust and uh moisture and crap out and uh yeah, definitely the other uh one is certainly not fitted under there.

**Dave Jones:** So, there we go, that's coming apart already. So, it looks like um Oh, by the way, it's only it's only got one screw. It only came with one screw down here. So, maybe somebody's had a had a hack at it or uh something like

**Dave Jones:** that, but I have powered it up and it does actually work. So, there we go, it's apart. It looks like it's going to flop open with a ribbon cable. Here we go. Ta-da! Hey, look at that. Aw, beautiful. All

**Dave Jones:** right, what we've got here, beautifully laid out in two halves. As you can see, all of the uh processing and display stuff all on this side, connected via, you know, a 25-way ribbon cable or something like that, over to the main

**Dave Jones:** power supply part, as you can see, with all the uh caps and all the uh battery management stuff. And uh looks like under here, we've got all the uh shielded scope and multimeter front end. So, uh that it'll be interesting to see.

**Dave Jones:** I'm assuming that's say Maybe analog-to-digital converter is under here and uh then it it's just getting the data back over to the processor side cuz there's no other connections. There's no, you know, high frequency or coax connections from one side to the

**Dave Jones:** other. So, I don't think they're actually, you know, outputting analog stuff on this ribbon cable. So, I can only presume that the ADC and capture side in the multimeter front end is all under there. So, I'll crack that open. We expect to see more

**Dave Jones:** under there, but let's have a look at the processor side. One of the first things I noticed is that they interestingly divided this. You can see it on the silk screen, divided it into a grid base pattern and you know,

**Dave Jones:** o i h g 1 2 3 4 and that's for servicing cross reference and stuff like that. You know, the component is located in, you know, i4 or something like that. So, you know, I don't think it's needed on a product

**Dave Jones:** of this size, but I guess that was Fluke's, you know, internal policy and way of doing things. So, the designers just followed that up and I can see a bit of that on the other board as well, which we'll take a look at. But,

**Dave Jones:** I don't I always see is a couple of custom Fluke chip sets. We'll take a closer look in here. There's another Intel device over here, which we'll look at, but it is nicely modular design like the battery sense circuit around here.

**Dave Jones:** There's a receiver / battery sense circuit. There's external RAM contrast circuit around here and they have labeled them and grouped them quite nicely. I like it. And we have six Hitachi LCD dot matrix driver chip sets there. All surface mount, pretty basic

**Dave Jones:** stuff. They've decided to integrate this onto the main board instead of having that separately. You know, there's a bit more engineering work in that. You could have divided it up. Really, you could have divided your workload up and said,

**Dave Jones:** "Right, we're going to put all the display stuff on one board or something like that." But, no, they decided, "Oh, bugger it. We'll just integrate it on a single board, go for broke." And, you know, it's obviously going to

**Dave Jones:** be cheaper to assemble and test and stuff like that and when it's all on the one board, but yeah, they're the design trade-offs when you're starting a design like this. Well, do we make it, you know, a modular

**Dave Jones:** board for the LCD display and associated circuitry and then have a ribbon going over and stuff like that and then you can divvy it up, test them all separately, qualify them all separately, and you know, stuff like that. So,

**Dave Jones:** there's pros and cons both ways. I guess in the end it really comes down to your company's particular methods or an individual design team's individual methods and things like that and what they're trying to achieve. And we found

**Dave Jones:** the date code, folks. 9423 on most of these chips around 94. So, yeah, that serial number on the back of all that date code on the back of the unit was actually correct. Almost 20 years old this sucker. So, the manual

**Dave Jones:** said 1996. So, I guess the manual was last updated in 1996, but actually manufactured in 94 sometime. Now, bingo, we've found the main processor. Here it is, an Intel S83C 196, part of the MCS-96 family of processors. This one's got 8K

**Dave Jones:** ROM built in and goes back copyright 1986. Brilliant. Made in Japan back when they made the bloody things in Japan. Now, if we take a look at the layout on this thing, here's this custom Fluke chip over here. It's the Fluke Well,

**Dave Jones:** it's got Fluke ASIC on it. I have no idea what that stands for at all, but clearly if you look at the memory interface on this, I mean, this thing's like capable of, you know, it has external memory interface, but it

**Dave Jones:** seems, and here are the three and here's the all the flash over here, the program ROM. So, really, that seems tied into the Fluke ASIC down here. So, and then that. So, it looks like it's some sort of memory controller or something, you

**Dave Jones:** know, some sort of ASIC that does memory control or something like that. And it's also connected to the keyboard as well. You'll find that goes over to the front panel keyboard. So, really, that's a like a keyboard and memory interface

**Dave Jones:** controller, perhaps. Something like that with Intel processor running a maximum of 16 MHz, by the way, this thing. And uh Well, we got a 74HC 132 there. Couple of other miscellaneous, got a resistor network going happening around here. But this

**Dave Jones:** main LSI. There it is. It's another Fluke ASIC. It even says it's an ASIC on there. And well, yeah, I don't know how you go about getting info on that. You probably can't. Fluke proprietary. So, yeah, that's running at 25 MHz. So, you

**Dave Jones:** know, you got to wonder what that's doing. It's got some memory interface to it here. So, we've got a known 16-bit processor down here. Not a bad 16-bit processor for its day, really. Kind of what you'd expect to find in a product

**Dave Jones:** of this vintage. And then we got the two ASICs, custom Fluke ASICs around here. And they're both interfaced to memory. This one's interfaced to external SRAM up here. So, and also down to this flash down here. So, you you know, it's almost as if

**Dave Jones:** based on its location to the display driver up here, kind of like that is probably some sort of display processor or uh something like that. That would be my guess, anyway. And then this one down here um is just an external uh memory and

**Dave Jones:** keyboard controller for this processor. So, it's like the processor is maybe, you know, when they're designing this thing, uh this is an oscilloscope, you know, it's got to process a lot of information, do a lot of stuff, update

**Dave Jones:** the screen and, you know, as fast as it can, all that sort of thing. Uh we can't really do that in a processor of this day, really. So, we're going to have to do a custom I know, let's roll our own

**Dave Jones:** custom ASIC up here to do all the uh heavy duty display processing and stuff like that, perhaps, and another one down here to offload um you know, some other tasks or something like that. Uh keyboard and memory uh controller maybe

**Dave Jones:** a uh direct um ADC to memory uh controller or something like that. So, maybe the data's coming directly in from the ADC side of things and this ASIC not being processed by the not being handled by the processor, but maybe being dumped

**Dave Jones:** straight to sample memory or something like that. Yeah, definitely uh controlling the display cuz you can see the traces snaking their way around here like this, going over to the uh uh the display driver chips around here. And of course, they're all um

**Dave Jones:** interconnected. So, that is the best guess that that handles all of the uh graphics uh processing and maybe um you know, taking the samples and directly displaying it. So, the processor is not responsible for the uh update uh rate and stuff like that. It's

**Dave Jones:** all handled by the ASIC. Oh, how cute. We've got an LM324 and an old uh 4093 quad uh Schmitt NAND gate. Classic. And that looks like it's somehow that's like the RAM power. That's what it's got there. So, I don't know. May what's it doing?

**Dave Jones:** Is it, you know, I your guess this good as mine. I don't know. but if we lift this board out of here, let's have a look on the bottom. Yeah, I didn't expect to see anything on the bottom at all, and sure enough we

**Dave Jones:** don't. We just get some test pads down there. You can see the manufacturing test pads down in there. All those gold contacts are that contacts there, little gold pads. So, that would have gone down onto a bed of

**Dave Jones:** nails production tester and possibly used to program all the flash memories once they're in circuit and stuff like that. And looks like just have a bit of a shielded grid down here pattern on the bottom of the membrane down there and yep, there you

**Dave Jones:** go. Nothing special, but yeah, they've decided to do that as a um uh mesh base one instead of a solid ground. And down here we've got our soft latch on off power circuit, which would be continuously monitoring the on off

**Dave Jones:** membrane switch on the front panel. Now, let's take a look at what's going on on the battery side of things here, and we've got some serious capacitance happening around here. Looks like we might have a big inductor or common mode

**Dave Jones:** choke or something like that in there. Looks like there is a common mode choke there for our DC power in and underneath this little shielded can, I see two inductors down in there. They're actually identical looking inductors to

**Dave Jones:** these things here. They don't look like inductors, but they just got tape on the outside of that, but there you can see the windings on the ferrite core there. So, yeah, we've got a decent amount of switch mode stuff happening there. These

**Dave Jones:** would be low ESR caps presumably top quality. What are they? Let's have a look. Does it say? What is that? A sexy brand capacitor. Well, they are very sexy. SXE. And it turns out that's not not actually the brand, that's the type

**Dave Jones:** and they're from Nippon Chemico. Absolute top quality as you'd expect. And of course I missed that, that's the Nippon Chemico symbol down in there and the SXE is the series model of the capacitor and these are high temperature low ESR caps as I

**Dave Jones:** suspected. And we have ourselves a current sense resistor folks, there it is. 0.1 ohms, 5%. That's in series with the battery pack down there. And I can't quite see the uh Murata part number down in there, but it's a Murata part and looks like we've

**Dave Jones:** got four ferrite beads there with a filter cap. So if you look at the Dave CAD drawing here, it just looks like that in series with the DC input jack. And if we get the shield off and look under the skirt,

**Dave Jones:** there it is. Hey, nothing under there. Not much at all. But once again we've got that silk screen component grid happening, which tells you where the parts are. There must be more stuff on the bottom down in there.

**Dave Jones:** We've got a couple of relays up there, we'll take a good close look at that, but looks like that board's going to have to come out to see the goodness on the bottom. Now on these portable scopes, if you haven't seen them before

**Dave Jones:** you might think this is just a fancy red painted BNC you know, a just a regular BNC painted red and you might think, "Well, how can it make electrical contact when it's got that red paint on there?" Well,

**Dave Jones:** check this out folks. It bends. Not sure if you can see that. I'll get in there with the screwdriver. There we go. It's flexible. It's not metal folks, it's plastic. And if you have a look deep down inside you can see the real

**Dave Jones:** metal is somewhat um inset right back down in that connector and that is is of course for our safety because you don't want to be um you know having you don't want to be able to touch any of the ground apart of

**Dave Jones:** the circuitry because this the idea of these uh handheld meters is that they can take floating measurements. So, you don't want the idiot user to be able to touch them. There you go, that's a better view of how uh

**Dave Jones:** deep inside the real shield part of that BNC connector is. So, while that looks like a BNC connector, smells like a BNC connector, it ain't one, folks. So, you can't just go and use a regular um scope probe on that and think you're

**Dave Jones:** going to get it to work. And yeah, it's just got the regular outputs here. There's the center conductor. There's the ground. Incidentally, the ground is wrapped in this uh capacitor, wrapped tightly around that uh lovely, beautiful. Look at that. Someone's gone

**Dave Jones:** to a lot of trouble, eh? Beautiful uh work and they soldered that onto the ground connector and that's AC coupling the ground or the negative input on that BNC through to presumably signal common and this internal shielding. And let's see if that's circuit ground.

**Dave Jones:** So, we'll go between the shield over here and well, let's go between the common terminal uh the uh negative terminal up here of the multimeter and yeah, it that's actually connected through to the negative terminal. Okay, so the ground

**Dave Jones:** circuit ground and let's let's just take this choke here. We can No, doesn't like that. Other side? Yeah, there we go. It's connected through to the negative uh of the DC input jack and the negative of the rest of the circuit here.

**Dave Jones:** But of course, the negative on the uh BNC over here is not. It's AC coupled through to there and doesn't directly connect. As you can see, it's only it's 515 ohms. And I believe there's an option in the software to

**Dave Jones:** either ground that input or not via one of the relays there. So, that's all you know, that depends on the measurement configuration that you're actually trying to do. And on the multimeter side, of course, there's not much happening there at all.

**Dave Jones:** There's a couple of relays in there. That one I think might be the one I just mentioned switching the ground in, but we've got a mob there. We've got a high voltage cap and a resistor through a resistor. And well, that's about it.

**Dave Jones:** There's not much on the top of this thing at all. Boring as the proverbial bat And here we go. I took the two screws in here out. And I do like the design of this. Very minimalist in terms of

**Dave Jones:** screws. So, absolutely chock-a-block. Look at that. Look at that. It's a thing of beauty. A real steel plate. Love it. And we have got a fair about going on on this board. Here's our analog front end up here, which we'll

**Dave Jones:** take a look at in a bit more detail. The unpopulated Well, almost unpopulated. The chips are Chips are certainly there to duplicate that second channel, but the BNC's not there and the relays and other stuff on the top side of the board aren't

**Dave Jones:** populated in there to uh do the second channel. So, it's partially there. So, I'm not sure what's going on there. And got our ADC up here, which I recognize. We'll get on to that. Got some power stuff happening over here

**Dave Jones:** and some looks like we've got some quad analog switches happening you know, 744000 series CMOS type stuff and another mysterious chip in here. Let's take a look. The largest device on here, I don't quite know what that is. I tried Googling that. No

**Dave Jones:** you know, nothing uh turned up at first pass. So, I'm going to have to another crack at that one. It's a Philips. Yeah, like OQ0308T. 34004ME. I don't know. Maybe if I find anything, I'll annotate this later. Then we got

**Dave Jones:** some 74HC stuff for the data. And here's an old friend, the Philips TDA8703. And I instantly recognize this because I've used this chip before in my own digital storage oscilloscope design, the DSA Mark III. Uh way back um so, a

**Dave Jones:** year or two after this, I think I did that in about '95 or thereabouts. It would I think it was published in '97 or something like that in Electronics Australia magazine. Anyway, here's a TDA8703. It's a flash 8-bit analog-to-digital

**Dave Jones:** converter primarily designed for video type applications, but you could certainly um use it for an oscilloscope. And I did, and it looks like Fluke have as well. But you'll notice that it's only got a single ADC. There is no second one. And it's a

**Dave Jones:** pretty basic flash 8-bit flash converter. Really, it needs like external voltage references and stuff, external level shifters, and all sorts of things, you know, to make the thing work. But you know, it's not bad. It's 40 meg samples per second

**Dave Jones:** at maximum. So, that's the upper sample rate of this thing. Obviously, I'm not sure if it does actually get to 40. But curiously, I believe the uh minus 3dB input frequency range of this thing only extends to just under 20 MHz. So, it's

**Dave Jones:** puzzling how they're getting a 50 MHz bandwidth using this converter. So, what's actually going on with this ADC? I'm not sure because it's minus 3dB bandwidth is only 20 MHz. yet this is a 50 MHz analog bandwidth uh

**Dave Jones:** scope. So, you know, uh somewhere there needs to be an ADC capable of handling that. So, the I can only presume that the only way they're doing it is some sort of sample and hold circuitry around here. Um

**Dave Jones:** maybe, you know, based on this analog uh switch here that is um sampling and then which is obviously uh sample and holding the value and then it's been uh converted at a slower rate by the ADC when it's not

**Dave Jones:** in real-time mode, i.e., when it's doing equivalent time uh sampling, which is sampling at a slower uh sample rate than uh Nyquist. So, really I think that's what must be happening there. Um otherwise, I can't see how they're

**Dave Jones:** getting uh that minus 3 dB 50 MHz bandwidth on this thing. Hmm, go figure. Anyway, there's definitely uh the only the one ADC there uh being um used to uh sample both channels unless this particular device is another ADC

**Dave Jones:** which is uh you know, uh sampling at which has a higher bandwidth or uh something like that. I don't know. We need to find out what that sucker is. If anyone's got the schematic for this thing or the service manual, uh please

**Dave Jones:** let us know in the comments or on the EEVblog forum. And we've got a 74HC uh 4316. That's a quad analog switch and there's quite a few of those uh placed around the board in various locations. So, lots of analog switching

**Dave Jones:** and that's what's they're using the same one over on the analog uh front end over here as well. So, it looks like we've got our analog um then it looks like we've got our input uh amp there. We'll take a look at

**Dave Jones:** that plus all the analog switching for the range stuff, I presume. And our input amplifier is a National Semiconductor LF453. No surprises there whatsoever. That's a um BiFET uh input uh high-speed, uh, precision op-amp, designed, you know, almost ideally suited to an, um, an

**Dave Jones:** application like a, uh, ADC or a scope front end in this sort of class. And you'll notice down in here that they've cut a couple of isolation slots there and there, and those components which are bridging them like that are actually

**Dave Jones:** ceramic caps. Down in there, there they are, four of them there, three of them there. So, they're isolating the signals between the, uh, input section over here and the rest of the part of the measurement circuitry. And here we have a 27, uh,

**Dave Jones:** MCAC. It's actually a, uh, TLC, a Texas Instruments TLC27M2AC, and that's a, uh, precision amplifier. They've got one sort of there, in the middle of the board, then they've got another one. Curiously, I thought this was a matching, uh,

**Dave Jones:** LF 453 to up here, but it's not. On channel two, down here, uh, they haven't got the matching device down there. It's that TLC device. So, I don't know what's going on. We certainly don't have a true, um, channel one, channel two mirrored

**Dave Jones:** circuit configuration here. And incidentally, you'll notice the larger solder pads on these outer pins of all of these chips, and they're, uh, solder thieves. Uh, they go under various, uh, names, but this is designed to be wave soldered, and you can tell this board

**Dave Jones:** has been, uh, wave soldered instead of reflow soldered. You know, if you look over some of the, uh, power stuff over here, it's clearly, you know, had the molten wave just go right over this thing. And the idea of these, uh,

**Dave Jones:** uh, they're so obviously all the components need to be glued, uh, down for that to take place and then these just ensure that you don't get solder dags happening between pads. You just get as a solder wave goes over this

**Dave Jones:** thing, you actually get a larger pad on the end allows you to capture any excess solder that's coming off like that.

**Dave Jones:** And there's a Signetics SG3524D pulse width modulation power controller. So that's just you know, powering some DC to DC converter stuff around here and LM285 1.2 volt voltage reference. And of course there's one thing you'll notice lacking around the multimeter inputs or

**Dave Jones:** anywhere on this board is your traditional Fluke multimeter type functionality. It doesn't have that Fluke input custom switching chip and all that sort of stuff. So they're just using the regular scope ADC here for the multimeter functionality. They're just switching it

**Dave Jones:** in on a different channel and that's pretty much it and that's and you can see the result of that in the specs. The specs for the multimeter on this are pretty darn ordinary. But that's pretty much all she wrote for

**Dave Jones:** the analog and multimeter part of the circuit. I don't know. I was expecting something a bit better than that just a you know, a 8703 ADC you know, shared between the channels if it has the dual channels and

**Dave Jones:** still don't know what that one is but yeah, there's not much happening there. It's all just you know, data the 8-bit data output and the clocks and things just coming from the processor board through that ribbon and that's all she

**Dave Jones:** wrote. Few little trim few little trim pots around here just to uh uh compensate the well, they're not even near the input of dividers. So, they're not and not for compensating input divider, but they're looks like they're somewhere near like compensating this

**Dave Jones:** uh, high voltage isolation part of this here. So, they're doing a few tweaks there. There's some diode protection going on there for the multimeter stuff, I'm presuming. And there's a amplifier for the multimeter. And you know, pretty ordinary.

**Dave Jones:** And they really have minimized the number of screws on this thing. Look, they've got the the attention to detail. They've put the little PCB catches in a like holder spaces integrated on the battery compartment there. So, the board

**Dave Jones:** sits under there. So, we've got you know, spaces under there which hold it in place. And you only need the two screws over the four here, but it keeps all this front panel stuff in place. Really is quite elegant. All right, I'll

**Dave Jones:** probably get lynched if I don't power this beastie up. So, I've got it hooked up to my uh, bench supply up there. So, it's uh, let's switch this sucker on. Beep. Woohoo! And we're straight on. There we go. Now, one of the real problems with

**Dave Jones:** this is that the screen is just totally washed out. I'm not sure what technology they were using back then. It may not even be you know, STN or something like that. I'm not sure, but it definitely I'm pretty sure it's faded.

**Dave Jones:** You know, because if this was its original contrast, then well, you know, it's not that great at all. And we can change the contrast like that. It reminds me of like the old TDS 210 scopes kind of thing that

**Dave Jones:** you know, that really washed out very low contrast look on it. So, I don't know if anyone remembers using these back in the day, but I'm sure that they do age. It's pretty horrible. Anyway, there's our There's our waveform. We can actually

**Dave Jones:** move it around and we can feed signals into it and it does actually work. It's as slow as a wet week. Absolutely terrible. The menu system is absolutely atrocious. We've got the like the scope meter, we can actually change it to meter mode like

**Dave Jones:** this and it actually displays our waveform plus our multimeter at the top here. That's not too bad at all. That works reasonably well and then we've got ohms mode. There it is. Whoop-dee-doo. We've got diode mode and external millivolts.

**Dave Jones:** Yeah, I think. So, you know, it it's not that great of a multimeter really in terms of our specs. They've just added it in as a bonus. I mean, the combined multimeter and the multimeter by the way has got a 5 MHz bandwidth.

**Dave Jones:** So, it's pretty it's pretty good actually in terms of uh what a meter is capable of in terms of bandwidth. So, that's one of the awesome aspects of using the 8-bit ADC. But then, you know, the multimeter, well,

**Dave Jones:** it's only using a crappy 8-bit ADC. It's not that good. Actually, come to think of it, that's probably what that other chip on the board was that I couldn't quite get the number for. Maybe it's another higher resolution ADC just for

**Dave Jones:** the DMM part of it. Not entirely sure. So, anyway, what we have here folks is uh let's say we're in scope mode then we can get into submenus and then we've got to use the menu keys to Hang

**Dave Jones:** on. Wait, how do we No. More scope. Then we can jump around in here and there's our our capture length. We can set that to 10 or 20 divisions. Glitch detect, 40 nanosecond glitch detect. That's okay. And whether we want you want averaging,

**Dave Jones:** whether or not you want persistence and stuff like that. So, you got to use that and then you got to go select item and then you got to scroll down again and you can get infinite and you can change

**Dave Jones:** the width of the trace and you can do do all sorts of stuff but yeah, really convoluted sort of operation menu operation for this sort of thing. It's pretty I mean we do have dedicated range keys down here. So as

**Dave Jones:** you can see it goes down to 20 10 millivolts per division with a times 10 probe. There all the way up to 5 volts per 10 volts 20 volts per division 50 volts per 100 volts per division 200 volts per division 500

**Dave Jones:** a kilovolt per division with a 10 to 1 probe and the time base goes down to 10 nanoseconds per division in equivalent time sampling mode of course it's not a real-time sampling scope below I think 100 nanoseconds per

**Dave Jones:** division. But of course obviously you're only going to get that one kilovolt per division with the optional high voltage probe for this thing. And I actually got the three of these PM 8918 10 to 1 scope probes with it. Really

**Dave Jones:** quite neat. One of them as you saw had a big cut in it but let's see if we can feed in a signal here. See what we get. All right, I'm feeding in a 1 kilohertz 5 volt peak to peak sine wave. So let's

**Dave Jones:** press the dreaded auto set button, shall we? You can hear the relays going click click click click and yeah, there we go. There's our Can I move it? I can move it up if I hold down the button. There's yeah, there's overshoot

**Dave Jones:** on the wave like it sort of you have to be very delicate. You can't hold down the move button but you can see at 1 volt per division there it is bang on. Five divisions. Awesome. And then if we

**Dave Jones:** go down here to user options and go into meter mode it should pop up with our waveform which is off the screen there, hasn't scaled that correctly and it can't measure it presumably because it's off the screen. And there we go, I just ranged it down a

**Dave Jones:** bit and we're getting 1.75 volts RMS AC. That's at 1 kHz. Let's up the frequency and see what we get. There we go, there's the same waveform again at 4 MHz because as I said in meter mode it's

**Dave Jones:** only got a bandwidth of 5 MHz, so let's put that up to five. See if it can measure that. Yeah, it can. Let's go up to six. See if it can still measure that. No, overload. There's our 6 MHz

**Dave Jones:** sine wave there, so let's bump that up to uh say 25 MHz, shall we? And see what we get. And there's our 25 MHz sine wave at 10 ns per division and let's drop the time base right down and we'll probably

**Dave Jones:** see some aliasing here as we drop down. Yeah, you can see it's going to start to do it. Here we go. There we go, drop the time base down. Yeah, there we go. It looks perfect, doesn't it? You would think, "Aha, look

**Dave Jones:** at that perfect sine wave at 50 microseconds per division." What? Nope, that's aliasing. And there's a 10 MHz square wave. It's not handling that too bad at all given the bandwidth. So yeah, this thing isn't exactly a user-friendly modern scope, that's for

**Dave Jones:** sure, but it is, you know, a 19 early '90s and '94 vintage, almost 20-year-old uh oscilloscope technology here in a handheld form factor and incredibly useful for its day, especially with the 50 MHz um bandwidth and you know, the basic multimeter

**Dave Jones:** functionality and stuff like that. Very popular little units these Fluke scopemeters were. So, if you've got any further info on these, um service manuals, stuff like that, I'm sure everyone would love to see them. So, please post them in the comments or jump on

**Dave Jones:** over to the EEVblog forum where you can discuss this ancient stuff. I love it. Vintage test gear. Vintage. 1990 4? You kidding? Vintage? Unbelievable. Anyway, if you like teardown Tuesday, please give it a big thumbs up. Catch you next time.

**Dave Jones:** Hi. Welcome to Teardown Tuesday. It's another bit of vintage test gear, and it's a Fluke. Woohoo! One of the first handheld multimeters.

**Dave Jones:** Multimeter. It's a bloody oscilloscope.
