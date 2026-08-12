---
video_id: IQ6xxveRJSw
title: Amazon Kindle Fire Tablet Teardown - EEVblog #219
url: https://www.youtube.com/watch?v=IQ6xxveRJSw
source: youtube-asr
---

**Dave Jones:** Hi, we've got the new Amazon Kindle Fire. 199 US bucks worth of loss leading technology. You know what we say here on the EEVblog, don't turn it on, take it apart. And of course I've already done a very

**Dave Jones:** lengthy review of this thing. Just click up here and you can watch that review video. This ain't going to be a review, it's going to be a teardown. We're going to crack this sucker open and see what's inside and see if it does have 199 US

**Dave Jones:** bucks worth of party in it cuz it's supposed to be Kindle's new loss leader. And if you're wondering what the reflection is, that's my oscilloscope and there's my camera. Can check the hair again. Hey. Anyway, we're going to

**Dave Jones:** take this sucker apart. There are no visible screws or anything so it's obviously some sort of form fit case or some sort of press fit case with the plastic clips, the the retaining clips around the outside. That'd be my guess. So we're going to

**Dave Jones:** use our spudger here and that. See if we can pry the case open along the outside of it there. Hey, heard a click there. There we go. We've got our first click. And there you go. You can really see

**Dave Jones:** those clips along there that you just sort of snap out as you go along and we should have those on all the sides. It looks like it should feels like it should just pop off fairly cleanly.

**Dave Jones:** And there you go. That just popped off real easy. That was as easy or even easier than the original Kindle. So as you can see it's pretty much exactly what we expected. We've got some shielding on the back of the case here

**Dave Jones:** but there were no sticky things actually like double sided tape or anything else sticking it. down. We've got a massive battery in here. That's where all your weight's going. That's where all your 404 g, a good lot of that is, uh, going into it. It's a

**Dave Jones:** lithium-ion battery. We'll go into that. And a small, uh, PCB up here and that That's probably, uh, all she wrote. And as with the Kindle, there's the, uh, RFID tag. You can see the, uh, coil in there which, uh, which connects to the

**Dave Jones:** little, uh, chip inside. And once you add an RFID tag like this to a product, you can do all sorts of, uh, versatile things. It'll contain the serial number. You can track it during the production process and do a whole bunch of stuff

**Dave Jones:** even after you've actually packaged the thing up. And you can see the conductive paint they've got on the, uh, case here. There's the There's the resistance of the normal ABS, uh, case. It's nothing, of course. And if you measure the, uh,

**Dave Jones:** the shielding, there we go. Now, in addition to the, uh, spray-on, uh, shielding stuff, which is pretty darn good, they've added this, uh, metal, uh, plate as well. And they've got another, uh, metal plate, uh, shaped down the

**Dave Jones:** bottom here. And they've really gone to town on the shielding of this. And it's curious to note that they've deliberately left a little square of, um, the case there unshielded. And if you see where that actually lines up, it,

**Dave Jones:** uh, lines up pretty much, um, over this, uh, flat flex cable connector here. And I'm not sure why they've left that little bit there unshielded. I don't know. Go figure. And the battery is a lithium-ion polymer type, of course. Uh,

**Dave Jones:** 3.7 V, so it's a single cell, uh, 4,400 mA hour, uh, 16.28 Wh nominal. Uh, manufacturer, I don't know. Sort of unknown. I don't see, uh, any marks in there. But, uh, the cells are actually, uh, made in China and the pack

**Dave Jones:** is processed in China. And, of course, having a single, um, cell at, uh, 3.7 V is much better than a, uh, multiple series connected, uh, pack because then you don't have any uh, charge balance issues and the cell should last a single

**Dave Jones:** cell should last a lot longer and and be more robust in terms of charge and misuse and that sort of thing than a series connected battery which has two or three cells in series. But they can obviously power this whole thing from

**Dave Jones:** 3.7 volts. I mean there may be some DC to DC converters on there to step it up. And we'll just take out these battery connectors here. This looks like a little flip one. Yep, it is. So that uh

**Dave Jones:** should come out there. We've switched this thing off. We've done a hard switch off. So that should be okay and we can There we go. We can pull it out like that. That one's gone and uh this main battery one here looks like it

**Dave Jones:** can just push out. Eventually, if we wiggle it out like that. Now it seems like they've gone and really stuck this uh battery down under here. It's quite hard to pry this out. I'm having a bit of difficulty. There's seems to be lots of

**Dave Jones:** adhesion under there. But if we take a look at the two battery connectors, then um obviously this one here is clearly uh this one's clearly a power. There's your power and well your ground and your power there and maybe some sense lines

**Dave Jones:** for temperature. But this connector here must be some sort of I'm guessing some sort of maybe ID. And if you have a look in there, we're up to rev F of the PCB. So they've gone through quite a

**Dave Jones:** few spins of this board to get it just right. Presumably manufacturing you know, not so much development passes. I suspect there'd be a few manufacturing passes so that they can get their cost down and things like that because

**Dave Jones:** you often need to respin these boards because you might find another chip that's you know slight that's you know point one cents cheaper or something like that when you're buying a couple of million of these things that all adds up

**Dave Jones:** so you can afford to respin the board a couple of times to optimize your your parts cost and your bill of materials and things like that. Let's flip up a few more of these connectors once we've undone those screws there and

**Dave Jones:** flip it open. Bingo what do we have a flat pack on the flat flex board here that what's that presumably to drive the LCD we'll take a closer look at that one. Well, it turns out that's actually a elite tech brand

**Dave Jones:** touchscreen controller a 2107 qs 001 k device and it looks like this foam pad in here is covering a device under there. I can see it. Let's rip that off and see what's underneath. Well, that's rather interesting. Turns out those pins

**Dave Jones:** weren't anything but an unpopulated expansion connector and we've got a BGA device under here. That's almost certainly the flash and up the top here next to our wireless LAN device. We've got our micro UFL coax connector so they're easy to pop

**Dave Jones:** off and get that out of the way so we should be able to get that board out now.

**Dave Jones:** And you can see that flat flex board to board interface connector there got there. Once you got that off the board should just lift out of these stuck down by a bit of gunk but we should have no

**Dave Jones:** troubles. Just lever in that board out. And there's the back of the board. Uh there's a few interesting things to note. Um they've got some uh silicon uh sticky silicon pad here to stick it down. And uh interestingly on the USB connector

**Dave Jones:** there, they've got some um some some metallic uh mesh uh cloth stuff which then mates down into the matching uh shielding uh metal down in there. And it looks like it goes all throughout there on the base of that right in. Wow,

**Dave Jones:** they're really um trying to uh just absolutely kill any problems with um and EMC uh compliance and RFI and stuff like that. They've really tried to nail this one. And underneath that uh silicon uh pad there, there's not really much of

**Dave Jones:** interest, just the uh decoupling and a lot of unpopulated decoupling um parts and and other uh passive type parts under the uh main uh under the main processor there and the main uh SRAM. Now, let's take a look at the uh main

**Dave Jones:** processor section here. And you might think this is the main processor just by the sheer size of it, but it ain't. Here's the processor over here. It's uh a uh TI um OMAP uh processor running at uh 1 GHz. It's a

**Dave Jones:** 4430, I I believe it is. And the uh large device here is um a Hynix brand. Uh that's your uh that's your RAM memory. That's uh 512 MB. And there's not much else in there, of course, a crystal oscillator by the looks of it.

**Dave Jones:** And uh just some uh power supply stuff surrounding the processor. And on the backside of that, you got a whole bunch of uh passive uh parts as well as we uh saw before. Now, they've actually got this in a metal can

**Dave Jones:** cuz it's quite high frequency all the stuff in there because you have to have a parallel bus running between these things and you know, when you get a you know, a very fast processor like that with a with a big parallel bus in

**Dave Jones:** there, you need some shielding. They haven't put the shielding on the top because that's taken care of by the case. Now, all these gold pads here all these little donut pads here of course all of course test points for the bed of

**Dave Jones:** nails tester or the flying probe tester that they use when they mass assemble these PCBs. They've got to have some way to test them, some way to program them. So, you can bet they're unlabeled of course, but they they know exactly what

**Dave Jones:** they do when they set up these jigs. They don't need to label them on the silk screen not that there's really any room to label them on the silk screen anyway. But, you can bet your bottom dollar some of those in there would be the JTAG

**Dave Jones:** interface to actually program the OMAP and test and program the OMAP processor. And over here we have our Micron brand flash memory. I don't know the number, but that would be the 8 GB of flash. And that device in there is a Texas

**Dave Jones:** Instruments LVDS 83B bus transmitter. And on the bottom of the board here once again Texas Instruments. They love Texas Instruments. They probably got a really sweet deal buying millions of TI parts of various types. Anyway, this is a TLV

**Dave Jones:** 320AIC3110 low power audio codec. And it's got a 1.3 W class D amplifier as well. That's for driving the headphone jack and the speakers. And there's a couple of other miscellaneous devices scattered around here. One of them will be like a a power

**Dave Jones:** management controller and they're probably a few little transceiver ICs scattered around the place as well. But apart from that, it is surprisingly minimal. And this tiny little BGA package down in here will be some sort of a battery management controller,

**Dave Jones:** power controller, or something like that handling the battery. It's a dead giveaway cuz it's right next to the power input connector. And in general, there's quite a few unpopulated parts on this board, especially this connector down here. I'm not not sure

**Dave Jones:** what's doing down at that connector, but we've seen these sort of missing components and missing connectors on Amazon products before. And of course, we have our Wi-Fi chipset down here, which is a Georgian WG7310. And of course, what's interesting is

**Dave Jones:** that they've gone for a double-sided load as opposed to the single-sided load, which we saw on the third-generation Kindle teardown. And what's the significance of that? Well, it costs it costs more to actually assemble a double-sided load like this, and it

**Dave Jones:** takes longer to assemble because you've got to actually put your boards through at least twice through the pick-and-place machine to assemble the components on there. And if you were shooting for the lowest absolute rock-bottom possible price, then you'd

**Dave Jones:** try to avoid designing a double-sided load board at all costs, really. And I've taken off the screws for the speaker assembly, and you can see that here. They've got the the two speakers either side there. Not terribly exciting. Some more exciting

**Dave Jones:** stuff is the Wi-Fi antenna on the top of the case here. Once again, you can see strapping here for the shielding. Now, there's one thing I didn't see on here, and that was the accelerometer for the sensing. So, I reckon that must be this

**Dave Jones:** little board down here with this ribbon cable going out here. And I think it looks like that's what this is over here. So, this this one up here. So, I wasn't I was incorrect that that actually went to

**Dave Jones:** the battery. It looks like that goes under the battery somehow and ends up at this board down here. And it looks like we can get the basic frame out by undoing five screws around here. Let's see if we can pop it out. And it looks

**Dave Jones:** like this just lifts out. Yep, there we go. Once you cut that uh shielding tape that's holding down that. And uh bingo. Be careful of the antenna cable. You can take that out, but there you go. There you go. It doesn't look

**Dave Jones:** like an accelerometer board. It looks like some sort of light sensor which goes through the front panel. Now, why you'd actually go to all the trouble to have a separate PCB for that, put it up right in that corner, have the cable

**Dave Jones:** going right under the battery, over, you got connectors, and extra cost, and stuff. Why you couldn't have engineered that to put that on the main board, I don't know. And there's the LCD display manufactured by LG. And if I'm not

**Dave Jones:** mistaken, that's almost the exact same display used in the Barnes & Noble Nook 7-in tablet. So, it looks like LG have cornered the market there. And you see that the battery is not one cell, but two separate cells. And they'd be they'd

**Dave Jones:** be paralleled up with some circuitry on there to handle the shared load and the shared charging. And each one 7.7 W hours at nominal 3.7 V. So, there you go. That's the teardown. Not too many uh major surprises in all that. I guess I

**Dave Jones:** was expecting say a single-sided load board to try and keep that cost down, but there's no sort of looks like very few if any custom parts are all off-the-shelf packages or commercially available COTS, as they call it, commercially available off the

**Dave Jones:** shelf devices. Uh no surprises at all they get the cost down by pure bargaining power. They've actually system engineered this thing quite well. I'm quite impressed with the system engineering of it and the flat flex cables and the board-to-board

**Dave Jones:** interconnects. I I can't help but think that in quite a few places they could have optimized the cost a bit more. They could have cut some more corners. But they've gone obviously gone through quite a few quite a few spins of the PCB and

**Dave Jones:** probably the all of the mechanical stuff as well. There'd be quite a few spins involved in that before they actually got production units out the door. But they've done a really good job. So my hats off to design team that have designed the

**Dave Jones:** Kindle Fire. It's quite nice. I like it. And it looks like it still works. We're Kindle firing. Firing up. Haven't put the back on, but uh yeah, touch screen works. Sweet as. Beautiful. And if you like my don't forget to

**Dave Jones:** subscribe. There's a subscribe link after this. Visit eevblog.com. And if you want to chat about electronics and technical stuff, the best place to do it is the eevblog electronics engineering community forum. Check it out. eevblog.com/forum. And it's got countless users on there

**Dave Jones:** who chat about everything to do with electronics. You name it, it's on there. Catch you later.
