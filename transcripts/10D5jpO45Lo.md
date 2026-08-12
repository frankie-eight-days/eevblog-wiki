---
video_id: 10D5jpO45Lo
title: EEVblog #1074  - Custom LCD Design - Part 2 - (µSupply Part 17)
url: https://www.youtube.com/watch?v=10D5jpO45Lo
source: youtube-asr
---

**Dave Jones:** Hi, in a previous video we took a look at designing your own custom LCD and I'll link in that video at the end and down below if you haven't seen it. This is basically a part two follow-up to

**Dave Jones:** that. It's going to be part two of several parts to come and where we left off before is that we actually had designed our own custom LCD and I've done tutorials on LCDs. I'll also link those at the end as well. We designed

**Dave Jones:** our own specified our own custom LCD and went off and got a quote and we're currently getting that manufactured. So as I mentioned in the previous video, you don't really have to go to this sort of detail that David's gone to here to

**Dave Jones:** specify this particular LCD that we're getting for our new micro supply project. We've color-coded all sorts of various things over here. So we gave them this table to fill in here for the pin information and they got reasonably

**Dave Jones:** close to what we wanted, but we'll have a look at the final data sheet that they sent us. So you don't necessarily have to go to that sort of effort to detailed effort to actually specify your LCD. But the more you specify it up

**Dave Jones:** front, the closer it's going to be to exactly what you want. You could almost design it on the back of a napkin with a sketch and they'll pretty much be flexible enough to do that for you. So the next step is is that we said,

**Dave Jones:** "Yep, go ahead." We paid our $140, I think it was $140 US. This includes the tooling charge and we're going to get five samples which we haven't got them yet. So that is just ridiculously cheap. I mean 140 bucks

**Dave Jones:** including the tooling and five LCDs delivered. It When I was a boy anyway, this this you may not be able to get this low cost if you did say the back of the napkin you know type approach. We actually gave

**Dave Jones:** them the full DXF, designed it, the actual segments in the full DXF uh, file, and so they probably had, you know, very little work apart from actually uh, routing the thing and doing up the data sheet. But if they have to

**Dave Jones:** actually design and draw all the segments based on, you know, your napkin sketch or something like that, then they're probably going to charge you extra tooling for the time and effort involved in that. So this uh, second part video is about the data sheet that

**Dave Jones:** they've sent uh, back. Cuz once we send them our uh, drawing for the LCD, then they'll uh, draw it up in their CAD system, whatever it is, uh, and get ready to manufacture it. They will send the data

**Dave Jones:** sheet back to us to actually approve. They want us to, you know, basically sign off on it and say, "Yep, go ahead. That's what we want. We're happy with that. Go ahead and manufacture our samples." So let's take a look at that.

**Dave Jones:** So this is the data sheet that we've uh, sent out. We have blanked uh, some various uh, things on here, and it's a multi uh, page one as we'll uh, see at the moment, but they've uh, sent back

**Dave Jones:** basically uh, the detailed dimensions, um, the individual uh, segments and things like that, the specifications for it's a um, STN uh, positive mode, 1/8 duty cycle, quarter bias, uh, 6:00 viewing direction. I've explained all these uh, specifications in the previous

**Dave Jones:** uh, video. Operating temperature range, uh, -10 to +50, uh, operating voltage 3.3, 64 Hz frame rate, transmissive, uh, and the back polarizer is a reflective, so it's going to be a reflective type LCD, i.e., no backlight on this thing. All right, so they've

**Dave Jones:** sent the uh, full pin table. This is after they've done all their routing inside there. Um, if which we'll show the routing in a minute, and this is the entire uh, pinout for the thing, and they basically got the They pretty much

**Dave Jones:** did most of the grouping that we uh, wanted, but that will be dependent. Like I said in the previous um, uh, video, like if you've got a segment up in this top left uh top right-hand corner here, and you want to connect

**Dave Jones:** that segment over to a pin on the bottom right here, that's just going to screw up your routing and things like that. And then they're basically not going to be able to uh accommodate your uh request for things like that. And um so,

**Dave Jones:** there we've got the full pin table mapping here. We've got the uh 40 pins, 20 down each side. And uh you might notice that these lines across here look at the min and max here, how they've got a line across that. And uh what that

**Dave Jones:** means is that you can't turn on those segments individually. So, it's just like it's the word It's signifying that that's the word min, and it's just one segment to turn on the word min. And you can see that they've also got that uh

**Dave Jones:** down there for the battery symbol uh for example. So, they're they're actually connected together. And like those two uh decimal points um it Well, the colon like in there for like a time uh between those individual uh segments

**Dave Jones:** there. So, that just signifies that they're all tied together. And here's basically their uh routing drawing. Now, not all data sheets actually will show you this, but they've really gone to town. And uh like we can't actually zoom

**Dave Jones:** in on this, so it's not like the real routing, you know, the actual uh photo imageable routing path like your Gerber files for your PCB for example. It's not actually that. Um and then it actually shows where the segments Look,

**Dave Jones:** it shows that the uh the common over here, okay, goes to these uh pins one through to pin eight there. They're our common pins, and the rest of them are the individual segments. But it basically shows you how they all tie

**Dave Jones:** together. And like it shows that uh this seven-segment digit up here, for example, is all on the one uh line like that, and that's how they multiplex. And you'll see that reflected in the uh mapping pin mapping and segment mapping

**Dave Jones:** table that we uh saw before. But that's kind of rather groovy. It just shows how they actually do the routing inside something like this. And there you know, it's there's a lot of work that goes into this. This is a fairly complex

**Dave Jones:** custom LCD with lots of segments, lots of pins with eight commons and like 30 odd segments as well. Um so, it's you know, it's getting up there in terms of being able to route this thing efficiently um on just the two layers

**Dave Jones:** there. And it looks like we've actually had like a PDF rendering type um error here from AutoCAD or whatever it is the CAD package that they're uh rendering from. The segments are all showing like all uh joined together here. And we've

**Dave Jones:** confirmed with them, yeah, that's obviously not how the final um LCD is going to look. So, they kind of like just goofed up a little bit there. But, uh as you can see, um they supplied this uh full data sheet for the thing. And

**Dave Jones:** this is going to match the uh samples that we're going to get. Okay. So, what we're going to need now is uh some sort of uh driver and demo board or your final product board, whatever it happens to be, to actually drive this LCD when

**Dave Jones:** we get these samples in. As I said, we don't have the samples yet. They're on their way, but we'll get a board uh manufactured and we'll have something ready to go. So, that when we get the LCD, we'll be able to plug it in.

**Dave Jones:** Because we're going to need because this is a quite a complex LCD with eight commons um and a hun- over 100 uh segments, we can't just drive it directly with the um STM32 um micro that we're actually looking to use in our

**Dave Jones:** final product here. So, we need obviously to use an LCD uh driver chip. And I've mentioned this previously. So, we've decided on the uh Holtek 1622. So, let's go take a look at that one. The advantage of this is that it basically

**Dave Jones:** only needs three lines for the microcontroller. It's basically an SPI interface. So, we have our our clock, MOSI, and uh chip select. Uh this chipset can actually read the data back out as I'll explain in a minute, but

**Dave Jones:** we're not using that functionality. We're just driving the LCD, and we don't really care to get any data back. That's a really in this particular product and this particular implementation that we're doing here, there's just no value in doing that. So, you might as well

**Dave Jones:** save a line. So, as I'm sure I mentioned in a uh previous video that there's a trade-off between trying to um either find a microcontroller, even if you can find one, that can support your particular uh LCD that you're trying to

**Dave Jones:** do. In this case, there are microcontrollers available uh that do have the eight commons and the number of um segments required to drive this LCD, but they typically push you into a much bigger pin package uh microcontroller, which usually has more memory than what

**Dave Jones:** you need and more other resources and everything else. A bigger, badder-ass micro that you're going to pay a lot more for it. So, often it's actually cheaper to use a simpler microcontroller with no built-in LCD controller and use

**Dave Jones:** an external LCD controller like this Holtek one here. So, this is the Holtek HT1622, and it does a bit more than uh LCD uh driving, as we'll actually see here. And it's uh yeah, you can even buy it like

**Dave Jones:** on AliExpress for less than a dollar in one-off quantity, and you know, they're we've got other sources that can actually get this quite um cheaply. And the it's actually cheaper to get this Holtek driver chip than it is to buy

**Dave Jones:** uh spend the more on the microcontroller to get the model that has all those pins required, as I said. So, it's from a cost uh point of view, it's better, and also from a uh PCB layout point of view

**Dave Jones:** as as well. You can actually put the driver chip next to your LCD, right next to the pins. You can route out the pins properly. It might mean you can uh use a two-layer board instead of a four-layer board, for example. So, those

**Dave Jones:** sort of uh factors can influence the final uh cost of your design. Um you know, cuz you you saving cents here and there kind of matters in uh you know, not even uh like high-end uh consumer type stuff in the millions, but sort of

**Dave Jones:** at the lower end as well. The higher margin that you can uh get in your product, the bomb cost versus the um basically the uh retail or sale price of it, then the better off you're going to be. And you can spend money on a better

**Dave Jones:** case or better switches or better overlays or you know, something else. So, if you can save money, do it where you can. Uh but also from as I said a layout point of view, if your micro your microcontroller can be over on this side

**Dave Jones:** of the board up here and your LCD controller can be up on this side and you've only got those three lines going that SPI bus going between it and the micro might be over here cuz you might be using the analog-to-digital

**Dave Jones:** converters in it or something else and they might be near your analog uh parts for example and your LCD can be separated right up here. So, there's lots of advantages to using a dedicated chip. Um and they're often just easy to

**Dave Jones:** use. You don't have to dick around. Some of the microcontrollers are quite complicated in the way they drive their LCDs and programming them and things like that. So, this is quite a reasonable solution. So, we're using the HT1622 with eight commons and at 32

**Dave Jones:** segments. And this is actually a pretty groovy little uh part. Not only does it have a watchdog timer and uh time base generator, but it's got a a uh buzzer generator as well, which we're going to use for you know, hook up a buzzer to it

**Dave Jones:** and it can actually generate two different frequencies. So, that's really good. 2 kHz and 4 kHz. So, you can get different uh tones and stuff like that. Um so, it's very simple uh to use. Now, the interesting thing about this 1622 is

**Dave Jones:** that's actually available in three different packages, a 44-pin LQFP, a 52-pin LQFP, and a 64-pin LQFP. Um and why, I hear you ask? Well, different uh sizes for different uh technology products. For example, like you might think think that the 64-pin LQFP is

**Dave Jones:** bigger, but it's actually not. It's a 7 mm by 7 mm. If you have a look at here at the dimensions, E here, that's the uh dimension of the pin pitch. If you go down here, none of this inches rubbish,

**Dave Jones:** we want millimeters. Look at this, 0.4 mm pitch pin pitch. What a pain in the ass. Um 0.5 is quite small. 0.4 is starting to get, you know, really pain in the ass category. Um but the other ones up here,

**Dave Jones:** for example, the 52-pin is a 14 by 14 mm. So, it's actually uh four times the area than the 7 by 7 mm one. Uh the 7 by 7 is actually 1/4 the physical uh size of the other one. So,

**Dave Jones:** you know, a huge difference for the same uh chip. Obviously, um some of the pins are not going to be used on the different uh configurations. And then the And that one, by the way, is a 1 mm

**Dave Jones:** pitch. So, there you go. If you want to solder those by hand, 1 mm. Geez, Stevie Wonder could solder a 1 mm pitch uh LQFP. No worries. Um and the 44-pin LQFP up here is once again, it's a bit

**Dave Jones:** smaller again uh than the 14 by 14 mm. So, if you physically got less board area, then uh you could uh potentially choose this one, and you're a 0.8 mm pin pitch. So, it's still quite reasonable. So, but hey, you might not

**Dave Jones:** be able to get all of these with the same sort of availability. So, you're maybe stuck with the one that you can get, but you can come a gutser when you in your bill of materials if you actually order the wrong part. You know,

**Dave Jones:** you may go to a supplier that says, "Oh, yeah, I've got I've got a ton of those. I've got 10,000 of those H21622s. I could do you a good deal on them." And they send them to you, and you find that

**Dave Jones:** you get the completely wrong pin pitch, and you're just screwed. So, But, you've got to be careful. This is where you have to specify the exact configuration. Where is it? Let's have a look. Actually, this one's further interesting

**Dave Jones:** in that it doesn't give you an exact bomb part like a like a ordering part number on here to actually get this right. So, you would have to actually specify it and double and triple check with your supplier that

**Dave Jones:** you're actually getting the right one. Normally, in data sheets like this, there's like a table that actually you know, gives you the exact orderable part number so you cannot make a mistake, you know, with the extra digits. So, it'll

**Dave Jones:** be HT HT1622 with, you know, some weird digits on the end to order that particular package. But, in this case, they don't actually have that, which is really kind of annoying. Uh Holtek. Anyway, just watch out for your um

**Dave Jones:** your pin pitch on your packages and what type of package you've got cuz if you go to BGA, for example, that's a a different uh might change your assembly requirements somewhat. Um so, that can add to cost and yield and um all sorts

**Dave Jones:** of things like that. So, this is quite neat. We got pad coordinates. We don't care about all that. But, here's the pins for the sucker. So, we've got our chip select. We've got our read pin, which as I said, we're not actually

**Dave Jones:** connecting in this particular circuit cuz we don't need to read back uh the RAM contents and things like that. Only if you want to store use the RAM inside this chip to store the data so that you don't have to store

**Dave Jones:** it inside your microcontroller. That can be handy if you've got a real tiny microcontroller that's memory limited and stuff like that. You can use the mapping the RAM mapping inside the LCD driver chip and then to hold all that

**Dave Jones:** data and then just read it back if you need to manipulate it or do whatever, read it back later. So, but we you don't have to use that. You can just push out the data. So, the right pin, the data,

**Dave Jones:** which is a bi-directional thing. We've got power, oscillate the from an external clock source, so we've got a clock on that. And the LCD operating voltage, which is you generally hook up, I'll show you the example circuit in a minute, you just

**Dave Jones:** generally hook it up to a pot there, so you can adjust it or a digital pot if you want to adjust it digitally. And there's three a four three unconnected pins there. So, let's go down and have a look at it's got

**Dave Jones:** timing diagrams and all sorts of things. It's got watchdog, which can send there's an interrupt pin as well, which can interrupt your microcontroller. That might be handy for various system applications, we won't go into that. And there's the example application circuit,

**Dave Jones:** and this is it's patented. They make you aware of that on every single page, thank you very much. And you just put a variable resistor, it's basically just a pull-up, so you can put a fixed resistor or a pot in there, it's typically like a

**Dave Jones:** 10k pot or something. We've got our piezo buzzer on there. Make sure it's actually a piezo transducer cuz there's a difference between a buzzer and a transducer. A piezo transducer is just a transducer, there's no building oscillator, so it

**Dave Jones:** needs the oscillator built in to either your microcontroller or this particular thing. But a buzzer actually has the oscillator built in, so all you've got to do is apply 3.3 volts, for example, an output logic high on your

**Dave Jones:** microcontroller and it starts to buzz at the predetermined frequency. The good thing about the piezo is that you can basically drive it at any frequency you want, so you can get different tones and whatnot. Whereas that's what this chip

**Dave Jones:** actually supports, 2 kHz and 4 kHz tones. But if you're driving your piezo directly with your microcontroller, then you could in theory just drive it at any frequency. You could sweep it, produce tones, and play music, and do all sorts

**Dave Jones:** of wonderful weird and wonderful stuff. Make it talk. I don't know. Maybe. How would a piezo sound decent? You'd need a decent uh uh DAC on there to do that anyway. It's a non sequitur. Um so, that's that's all

**Dave Jones:** there is to it. And then you just hook the LCD directly up to the common and segment drivers. It handles all the biasing cuz the biasing for a multi-segment LCD is actually quite complicated for an eight-common one like

**Dave Jones:** this. And as I've mentioned in uh previous videos, although I probably have to do a dedicated video on multiplexed uh LCD driving. It's quite complicated. They're actually multi-voltage levels like this. So, this is uh for example, a common This is a just a

**Dave Jones:** Microchip application uh note here. It's got quite some decent information. But, there are all these different voltage levels in here. And your LCD driver has got to be able to generate all these different levels because as I've mentioned before, if you uh the whole

**Dave Jones:** idea is that you have effectively over time, you want to have a net DC level of zero on your LCD. Otherwise, it could uh potentially damage your LCD. So, that's what these uh dedicated drivers um actually take care of all this. They

**Dave Jones:** generate the bias voltages. They do everything else. Beautiful. You don't have to worry about it. And for all you math nerds out there, let's go and have a look at this. I try to say maths maths like we're supposed to say in Australia,

**Dave Jones:** but I can't say it. My tongue just doesn't let me do it. So, I have to cop out and use the American math. math Um you can actually there's formulas to calculate uh what's called the discrimination ratio, which is basically

**Dave Jones:** your you know, calculating the DC uh values, your RMS values in there of on and off segments. And look, it can get quite complicated for a seven-segment for a seven-common um LCD like that. So, you know, it's It like I said, if you want to uh

**Dave Jones:** um if you want to try and drive the LCD yourself using your own circuitry, this is the all the sort of stuff you have to do. Whereas, this is why you use a dedicated LCD driver chip, either the

**Dave Jones:** Holtek one which we've got here, or ones that are built-in multi-segment multi-common ones that are built into your microcontrollers. They handle all this stuff, and it's all taken care of for you. Oh, wackers! And it could even get more complicated. You might have to

**Dave Jones:** like bypass them with some caps as well. So, that's, you know, quite significant added uh components to your PCB. It doesn't really cost a huge amount, but there's uh cost in terms of assembly time of placing the parts, bill of

**Dave Jones:** materials, and all that sort of stuff. Not to mention the uh component space on your PCBs. But, the Holtek we've got um it doesn't need any of this. It generates it all internally. Brilliant. So, there you have it. That's

**Dave Jones:** just a uh sort of like a follow-up video, an intermediate step uh required to get your custom LCD manufactured. So, hopefully in the third part of this custom LCD uh video series, we'll get the real samples back. We'll power them

**Dave Jones:** up. See how they work. So, if you like that video, and if you like the series, please give it a big thumbs-up, cuz that always helps a lot. As always, discuss down below at eevblog.com. Links and all that sort of stuff. You can support me

**Dave Jones:** on Patreon. Links always down below. All that YouTube stuff. Bell icon. Do that. Catch you next time.
