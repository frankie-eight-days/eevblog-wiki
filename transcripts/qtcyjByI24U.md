---
video_id: qtcyjByI24U
title: EEVblog #800 - Siglent 1000X Oscilloscope Teardown
url: https://www.youtube.com/watch?v=qtcyjByI24U
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Tearown Tuesday. Yes, we're going to take a look at this brand spanking new, hot off the press, practically not available yet, Siglet SDS uh 1000X series oscilloscope. You know what we say here on the AE blog,

**Dave Jones:** don't turn it on again. Take it apart. As with uh most little modern compact uh scopes like this, looks like we got some screws, four screws down the bottom here. And well, where are the matching ones on the top? Well, yeah, under the

**Dave Jones:** handle there. And look, um, this is interesting. They've got no, um, threaded nuts. No, no nuts on the BNC's. That's nice and convenient to take it apart. Beauty. Once again, thanks to Charles at Trio Tested Measurement, who's uh, has kind of reluctantly agreed

**Dave Jones:** to let me um, tear down the only unit in the country. So, yeah, let's hope I don't break it. Is it just me or do those little gold QC pass stickers not instill, you know, QA and QC pass

**Dave Jones:** stickers not instill a lot of confidence? I'm just used to seeing those on, you know, the, you know, the $2 eBay crap items you get. I don't know. It's just gives me a bit of the heebie-jebies. First of all, though,

**Dave Jones:** what I'm going to try and do is get this pesky warranty void if removed uh sticker. Nice little siglant hologram thing there to know that it's uh genuine. And um try and get this off so that Charles will feel a bit better. Or

**Dave Jones:** maybe if he doesn't watch the video, he won't know that we took it apart. And well, hello threaded machine inserts, but I think they might be going into plastic, but they've got some thread locker on there, too. So be

**Dave Jones:** interesting to see once we take it off if there's actually a metal threaded insert in there. That would be impressive. I am in like Flynn Errol. That is all right. So we're in and uh heavy shielding as we've come

**Dave Jones:** to expect on all of these uh type of scopes. Look, we got another uh B and C down there. Unpopulated. I wonder what that is. um a second um ARB channel or something maybe. Anyway, looks like we got some sort of programming header

**Dave Jones:** there and there and there and an unpopulated header down in there. So, anyway, we can see the board down there. Looks like it's made looks like it should be one big one big board under here. So, we should be able to see

**Dave Jones:** everything on it. Hopefully, I don't have to like take the whole thing out, flip it over the other side. But anyway, we'll see. um power supply will be under here. We've got uh the ventilation of course is fine. The fan uh sucks in here

**Dave Jones:** and uh blow well no it sucks um sucks from this side and blows out that side and Bob's your uncle. That's about it. So there uh whether or not there's any additional heat sinking on inside on the um well there won't probably won't be

**Dave Jones:** AS6. There'll be FPGAAS in there. So let's take it off. Um not the best quality metal work I've seen. a little bit. How you doing there? If you can see that, but uh anyway, it's built down to a price. So, there you go. As you can

**Dave Jones:** see, we did get threaded metal inserts in there. Absolutely brilliant. Um other scopes have just got self tappers. Anyway, I'm starting to take the screws out here. Yes, they do have the um thread locker on them, but all this

**Dave Jones:** metal work seems like it's like not lined up properly and sort of squeezed in a little bit. It's almost like they were, you know, half a millimeter out on the drawings or something. Anyway, not a big deal. Just something I noticed. And

**Dave Jones:** there you go. We're in like Flynn. And that's all rather uh neat and tidy. Power supply is smaller than I thought. I expected like a big long one in there, but they've just got like half size in there. Um it's in its own shielded can.

**Dave Jones:** Of course, that's pretty much uh mandatory. Um shake proof uh washer up there. Is it anyway? No, it's not a shake proof washer, but it have the um uh thread locker on there. So, the mains earth has done really

**Dave Jones:** well. Got no problems with that at all. We'll try and get the cover off that power supply and have exquisite it. Just one uh one cable coming over, one cable for the fan, and ta there's the board. Neat. Okay, this looks pretty much uh

**Dave Jones:** par for the course for any modern uh digital scope. We've got our analog front here end here. Hopefully, we'll get the can off that. We've got our uh external uh trigger circuitry over here. A little relay in there. Um as I I think

**Dave Jones:** I when I did the review of this, I didn't hear any relays click in the front section, so I'm not sure if it has any. Anyway, we'll have a squeeze under there. Um this is obviously our main acquisition FPGA um under there. One,

**Dave Jones:** you know, I doubt it's an ASIC. I'm pretty sure it's an FPGA. It looks like um they've uh thermal adhesived that heatsink onto that chip. So, unfortunately, we're not going to get that off. Uh, sorry, folks. I really

**Dave Jones:** want to be careful with this one. It's the only one in the country. Um, anyway, looks like we got our um little sample memory. We'll take a look at um in a minute. And uh anyway, hopefully get the

**Dave Jones:** can off. What else have we got? And totally unpopulated BGA and memory here. Well, no surprises for guessing what that's for. Um here's our logic analyzer connector down here. So they haven't populated any of that. So you can forget

**Dave Jones:** about like hardware enabling, just whacking in the connector, hardware enabling. Of course, they're going to get the price down by, you know, the logic analyzer modules don't have the uh chip, the memory, or any of the passives or anything else uh fitted. So yeah, um

**Dave Jones:** that's actually fairly uh simplistic. We've just got some input protection there. And um unless there's stuff on the other side of the board, uh I don't know whether or not we'll get to that today. But anyway, um fairly simplistic

**Dave Jones:** logic analyzer stuff by the looks of it. Um we've got a little RF connector um down here. Now, what that's doing, I don't know. Some sort of uh uh external reference clock, external uh test connector or something. these, you

**Dave Jones:** know, the these cost a little pretty penny each. So, I don't know why they're populating it there if it's not being used at all. I thought they'd be trying to shave every last uh cent off this puppy. Anyway, all of our DC toDC

**Dave Jones:** converter stuff around there. It's not worth uh it's not worth looking at. We've got ourselves that's uh probably our Ethernet up here. So, Ethernet and USB around there and then nothing doing here. We've got our JTAG header up here.

**Dave Jones:** uh fan control that'll I don't know if it's under firmware control or not or whether or not it's just uh running uh full tilt. Anyway, analog devices uh DSP and we're got ourselves a lattice FPGA. We'll have a take take a closer look.

**Dave Jones:** Dead giveaway what that puppy's doing and the associated uh memory here. That's uh that's our display connector. So, clearly that's our display driver display uh processor. So, this has got a reasonably quick uh display update rate. In fact, in burst mode, it's up to like

**Dave Jones:** a 400,000 waveforms uh per second, but you have to watch my review video to see the caveats with that. Anyway, um so yeah, uh we've got ourselves a front end. Maybe is that our ADC down there? Our dual channel ADC. Anyway, we'll take

**Dave Jones:** a closer look at that. Going in our acquisition engine, there's our capture memory. There's probably duplicate uh chips on the other side, so put could double the amount of memory there. I have to have a squiz. Um, that looks

**Dave Jones:** like our main oscillator in there. And of course, our analog devices DSP up here that'll be doing all the uh the main guey uh type stuff, the operating system and the, you know, USB, the user interface, all that sort of stuff. And

**Dave Jones:** our um display um ASIC/FPGA here. So it'll be funneling uh the data most likely directly from the acquisition ASIC over here into the uh display ASIC here. It'll be totally bypassing this processor. This processor wouldn't be doing uh the waveform

**Dave Jones:** updating, but it' be doing stuff like math and things like that. I don't think uh they're doing that inside the uh display ASIC down here. And there we go. We've got an analog devices black fin DSP. Um, I think it's almost exactly

**Dave Jones:** like the one used in the uh Ryol scope. So, it seems to be uh the go-to device for these uh types of scopes. I wonder why. Is it the uh is it the uh programming environment? Is it the cost?

**Dave Jones:** Is it the you know what is it? Well, what we've got here for our display processor FPGA. It's kind of uh is it an FPGA? Is it a CLD? It's kind of like a combination of both. It's the Lattis uh

**Dave Jones:** LCMX640. It is part of the uh Mark XO uh family. And uh you won't see around the outside of this, you won't see a uh FPGA, a sorry, a um a flash memory for the uh configurable bitstream because

**Dave Jones:** this is a nonvolatile device. Boots instantly. It doesn't need an external memory to hold the bitstream. Um and it's pretty pedestrian. It's like 10 bucks a Digi Key. guess like 640 lookup tables, not much. 6K of distributed RAM

**Dave Jones:** in there. So, nothing special. Pretty pedestrian FPGA. And it looks like we've got expansion uh flash memory. That X on there would be one of the production operators saying, "Yep, I've firmware programmed that puppy." And the DSP, of

**Dave Jones:** course, has some uh memory coupled onto that. These would be uh logic translators by the looks of it. Haven't even looked at the part number for those, but that would be my guess. dead giveaway that, you know, there's three

**Dave Jones:** of them. It looks like they're, you know, in the IO path. And well, sure enough, at second glance, if you actually uh take out some of the numbers in here, 245 at the end of it, you might recognize, you know, 74

**Dave Jones:** HC245 and AVC there. Well, that's a family. So, this is a 74 AVC 245. So, yep, definitely used for logic level translation. So it seems like those logic level translators uh would be converting between a level for the uh

**Dave Jones:** DSP up here and a level for the FPGA. But these FPGAs are um have all the requisite interfaces, you know, 3.3, 2.5, 1.8, 1.2, blah blah blah. So uh yeah, not sure what the deal is there. Anyway, logic level translation. So

**Dave Jones:** there's our oscillator there. I don't know. Doesn't even seem to have a brand on that puppy. Hm. Got resistors everywhere and lots of unpopulated cap. Don't know that part number off the top of my head. Um, interestingly, look,

**Dave Jones:** battery missing for the real-time clock. Um, yeah. Where is the battery? Does this thing not have a real-time clock in it? I can't remember. I haven't actually checked the uh firmware to see if it has a uh datetime

**Dave Jones:** stamp for any uh function. Maybe it doesn't. H. So, there you go. What is that connector doing there? I mean, this is obviously a little driver for it for outputting whatever signal it happens to be, but they've gone to a gone to a bit

**Dave Jones:** of expense there. And well, I don't know why. So, what we've got here is some uh SRAMM coupled onto the main acquisition uh FPGA here and decoding that part number. I've never heard of Net Soul before. I don't actually uh recall them.

**Dave Jones:** Anyway, we're looking at a 9 megabbit um synchronous pipeline burst uh SRAMM. So, it's designed for, you know, really fast, low latency update, all that sort of stuff. Exactly what this thing needs for that uh you know, that 4,000

**Dave Jones:** waveforms uh updates per second uh uh burst mode that this sampling mode that this sort of that this scope's actually capable of. But, of course, it it's in a 512k bit by 18 bit arrangement. So, um I don't know are they doing a check sum

**Dave Jones:** with the extra uh two bits in there. Anyway, that only works out to 128k uh sample memory for that. So, this is not being used as the main uh sample memory because it's got it's supposed to have 14 megs. So, presumably that's what that

**Dave Jones:** puppy on this side here is for. So, that puppy there. And if you know that that number off the top of your head, well, my hats off to you because it's bloody cryptic. You got to go into the Micron

**Dave Jones:** that that's what the M stands for there. The uh that's the Micron um trademark their logo and you got to go they've got like a part number decoder you whack into their website cuz they got these weird ass part code numbers in there.

**Dave Jones:** Anyway, this is an MT41J64M16JT-15. Of course it is. It's bleedingly obvious. Um, it's a 64 mgbit uh DDR3 uh 1333 uh 666 MHz um yeah uh DDR DRAM. So there you go. Pretty quick. Um so 64 megabits, 8 meg samples

**Dave Jones:** effectively. So this thing's got 14 meg samples uh total. So there must be a second one on the other side. And looks like they've got two uh DC toDC converters here locally right next to the SRAMM. Well, they're actually

**Dave Jones:** powering uh not only the uh memory, but powering the main acquisition ASIC as well. And ha, here is the ADC uh wedged in between the main acquisition ASIC there and the uh can which we'll take a look at under

**Dave Jones:** shortly. And I recognize that puppy. That's the HAD 1511. That's from a company called Hitite. Uh we may have seen a Hitite ADC in um in another tear down somewhere. I'm sure we have. Anyway, this is a uh one gig sample per

**Dave Jones:** second as the banner spec on this uh scope says, 1 gig sample per second ADC. Now, it's actually um four ADCs in here, and it interleles those to actually get uh the one gig uh one gig sample per

**Dave Jones:** second uh total rate. So, of course, they've only got the one in here. They haven't got one per channel. So, uh, of course, as I showed in the review, when you actually, um, turn on the second channel, the sample rate drops from, uh,

**Dave Jones:** 1 gig sample per second to 500 meg samples per second. So, yeah, that's the downside of this cuz, you know, these things aren't cheap. It would have been nice to put two in there and then, you know, you got to double the stuff in

**Dave Jones:** your acquisition ASIC and everything else, but eh, they decided, nope, we'll just use the one and have the B. Um the bit rate which is pretty annoying for a 200 megahertz bandwidth scope. As I mentioned 1 gig sample per second is

**Dave Jones:** fine for one channel. It meets that minimum four time uh times four times four multiplier requirement but it doesn't when um you have that to 500 meg samples per second. It effectively limits the usable bandwidth down to about 125 megahertz or so. And for those

**Dave Jones:** playing along at home with the trigger input, just a bit of a pan down there. Not going to go into that. It's uh yeah, knock yourself out. Sorry for the jittery pan here. It's not very professional, is it? Lots of unpopulated

**Dave Jones:** stuff down there. Look at that. Tons of it. What's missing? Where's Wally? And on the side of the can here, we're going to have some uh trigger pickoff uh from the analog uh channels too, presumably. Um look, a

**Dave Jones:** 7905 voltage regulator uh surface mount tucked in here. Is that for the uh low-noise analog front end? Cuz this thing is supposed to have a true 500 uh microvolts per division front end. But uh look at what they have out here in

**Dave Jones:** addition to this uh negative 5V regulator. Look, they got some LP 3878s. I suspected they might. So, I had a closer look at these. These are low-noise adjustable uh dropout um low dropout voltage regulators. So, they're low noise, of course, designed uh to get

**Dave Jones:** the low-noise performance for powering the circuitry on the analog front end. Nice. Although, granted, they've only got two of those um for well, maybe there's one per channel. I'm not sure or whether or not uh two power uh both

**Dave Jones:** channels uh and they're common. In that case, um you might get a bit of little teensy bit of cross talk between channels. Oh, boohoo. If we take a look at the analog front end here, I won't go into a huge amount of detail. I'll post

**Dave Jones:** some uh high-res photos for those who want to look at it, but um it's all passive around here, so maybe there's some active circuitry on the bottom. I'm not going to take this board out today with Yeah. There there could be

**Dave Jones:** something on the bottom. Not sure. But it's all passive networks right up until here. We got a couple of couple of in there by the looks of it. Or are they diodes? Can't see the silks. So diodes, are they D1, D2? Yeah, they could be

**Dave Jones:** diodes instead of uh transistors. Yep. Oh no. Q. There we go. Got a transistor over here. That's Q. So anyway, if we go up here, here's where all the actions happening. This is a uh if we can get that number, trust me,

**Dave Jones:** it's an analog devices AD8370 and that's a uh variable gain amplifier/ADC driver. So that's the puppy that's doing uh most of a good lot of the gain plus the uh main line driver straight to the ADC which isn't far by

**Dave Jones:** the way. It's just got to it's just got to pop across there. No big deal. And that thing down in there, I'm not sure what it is. It's got H1K uh hash 513. So, I'm not exactly sure what that

**Dave Jones:** puppy's uh doing, but apart from that, nothing special. I mean, we've got a 74HC, you know, 595 up here that's just doing some uh driving stuff. We've got a um uh Cosmo solid state uh relay there. So, that's not uncommon. find those all

**Dave Jones:** the time in these uh front ends. Not sure what uh that puppy there is. Can't quite make out the uh part number on that, I'm afraid. So, yeah, there's not too much else exciting there. Yeah. So, unfortunately, there's nothing in there

**Dave Jones:** that's telling me that they're doing anything special for the 500 microvolt uh front end. Got a couple of NEC relays. Of course, I was uh wrong on the relays. I got three of those puppies under there. Spared no expense. NEC's,

**Dave Jones:** they're not one hung low. NEC's make pretty good relays. Yeah, but apart from that, unless there's stuff on the bottom side, but yeah, as I said, I probably don't want to take the whole board out today, unfortunately. And right next to our ADC

**Dave Jones:** here, no surprises for finding the ADF 4360-7. This is a uh VCO. It's the uh PLLL for to generate the ADC clock. And you can see some inductors in there. Look at those puppies. There we go. Few of them there. So hopefully they've got

**Dave Jones:** it. They're all the loop filter uh components around here and whatnot um to enable that. So hopefully they've done that right unlike Ryol who uh goofed up their um loop filter um values. And uh yeah, they got uh jitter. So there was a

**Dave Jones:** jitter problem on the rials which they fixed by tweaking the uh luckily for them by tweaking the coefficients inside this thing. Um so they were able to fix it anyway. Um so unless well somebody can actually reverse engineer that and

**Dave Jones:** have a look at but we don't know the exact values. I'm not going to go in there and measure them. Let's assume it works. Well hello sailor. Here's the power supply. At first glance, this looks pretty well done. Nice and clean

**Dave Jones:** and tidy. Got our huge bypass cap, but there's the first uh thing. Leelon brand fail. Um anyway, we got our bridge rectifier in there. We've got our uh our common mode choke in there. We've got uh yeah, our suppression caps. Is that a

**Dave Jones:** mauv in there as well? But look at all the salastic sticking down those output caps. They really don't want those flapping around in the breeze. Got our optooupler. Nice isolation slots there. I'm sure they've all got the requisite

**Dave Jones:** rated components. Another isolation slot down in there. They're doing the business. That's not too shabby at all. And there's the primary side switch in. Nice looking heat sink there. Nice looking uh copper strap over the uh main transform main switching transformer

**Dave Jones:** there. And that's pretty decent. Check out the uh little heat sinks. They've um bit of attention to detail there. They probably don't want it to run too hot, but they probably didn't want it um you know, put any major probably didn't

**Dave Jones:** require any major heat sink work in there. But yeah, that is a neat little power supply. What are those output caps? Are they Rubicons? I think they're I think they're Rubicons. They've done a decent brand there. Why haven't they

**Dave Jones:** done a decent brand for the main uh input cap? What a bummer. But apart from that, that is a neato looking power supply. Siglet branded. Whether or not they actually did it themselves or uh farmed it out as is most uh common in

**Dave Jones:** the industry to do, we don't know. So, there you have it. That's a not a total look inside the new Siglet 1000X series, but it's probably as far as I'm going to go today. I don't want to have to take

**Dave Jones:** out the you rip off the tape uh for this and get the flat flexes out and take it all out and sorry I want this thing that's the only one in the country. Yeah, I'm a scaredy-cat anyway. No, I

**Dave Jones:** just couldn't be bothered. I'm actually running out of time. So, yeah, we're not going to see a huge amount. You know, for people who want to analyze the front ends and stuff like that, well, I'm sure somebody else will do a more thorough

**Dave Jones:** tear down with more professional pictures once they get one. No big deal. We know there's an extra memory chip on the back of there. There's probably an extra uh one of those on the back of there. Nothing too much doing. Um else

**Dave Jones:** apart from that on the back side, I'm sure. So, yeah, don't get all upset that you didn't see the bottom side. There you go. It was just too easy to access this top side. And anyway, that is quite

**Dave Jones:** a nice little design. I don't mind it at all. Um, you know, apart from the uh sample rate of course, which you know is an issue with this thing. It's a 200 MHz bandwidth, 1 gig sample per second, not

**Dave Jones:** shared. Apart from that, you know, they haven't got much horsepower. I'm surprised the amount of or the lack of horsepower they got to drive the screen. There's not much there at all. Not much doing it. And once again, sorry, but we

**Dave Jones:** don't know what's under there. I, you know, that that thermal adhesive is really tough to get off. I really stand a good chance of damaging that puppy if I take it off. Shame they don't have it down with a clip or anything like that.

**Dave Jones:** But yeah, it's a fairly simplistic design. You can see how it's been built down to a a cost. Although they haven't really skimped um you know a huge amount. Once again, they got you know stuff like this connector and that

**Dave Jones:** circuitry populated for no apparent reason. And yeah, it's not like you know madman months has got in there and uh ripped out you know components until it stopped working and then put the last one back in and said ship it, you know.

**Dave Jones:** So yeah, they've done a reasonable amount of uh engineering. And by the way, if you don't know who Madman Muntz is, I recommend you Google it. that's in there for the old-timers. All right, just for kicks, I've powered this thing

**Dave Jones:** up. We got a little flashing heartbeat light there. We got one over here. And uh we'll get the flur on this puppy. And take a look at the thermal profile of this. Here we go. No surprises for finding a

**Dave Jones:** uh hot little regulator over there. So, that's part of the switch mode. 36 odd degrees, you know, not much doing on the uh on the main video processor chip there. Uh the main DSP. Not much doing up there. 32°. No surprises for finding

**Dave Jones:** all the actions happening down here. That's the real hot spot there, which I'm probably now is at 50°. Um no fan, by the way. I haven't got the fan turned on, so there's no air flow. So, this is

**Dave Jones:** not a fair uh you know, real world test. It' actually be uh probably, you know, at least 10° lower than this or something like that. Um, and then around, you can see all the board as well around the main uh FPGA there, the

**Dave Jones:** acquisition FPGA. The reason why the FPGA looks cool is cuz that's the emissivity of the um uh the silver heat sink there. So, yeah, it's not calibrated for that emissivity. So, it appears cooler than it actually is. If

**Dave Jones:** that was a black heat sink, uh, we'd have black anodized heat sink. It would show up just fine. But anyway, ADC is the real hot puppy in there. And the board surrounding that is, you know, a good 10° cooler. So, not quite sure what

**Dave Jones:** the uh, FPGA up here is. Is that Oh, I can keep my finger on there. So, it's under 50. It's It's in the high for it's in the mid to high 40s, maybe. So anyway, that's not too shabby at all.

**Dave Jones:** Just did that for a bit of fun. [Music] It was a salesman. Oh, yeah. Yeah. Yeah. Hang on. I've got that upside down. What a what a knob. What a woolly. Fair income. And check it out. The sticker's back. No

**Dave Jones:** one will be none the wiser. Look at that beauty. Let's power this puppy up. See, she still works. By the way, that power supply, it might look decent inside, but bloody hell. Takes, as I showed in the thing,

**Dave Jones:** it takes like eight watts or something on standby. Absolutely ridiculous. And it's got like one of those stupid heartbeat lead things which is always running. Oh god. eight watts just to do a heartbeat lead. Got to be kidding me.

**Dave Jones:** Anyway, there we go. It's booting up. We have my old homemade clock here from the 1980s. Winner winner chicken dinner. So, as always, uh, tear down high-res tearown photos available on evvblog.com and forum links and leave YouTube comments and all that sort of jazz. And

**Dave Jones:** as always, if you like it, please give it a big thumbs up, rate, comment, subscribe. Support me on Patreon and all that sort of stuff. Follow me on Twitter, blah blah blah blah blah. Buy the merch, you know. Nah. Catch you next

**Dave Jones:** time.
