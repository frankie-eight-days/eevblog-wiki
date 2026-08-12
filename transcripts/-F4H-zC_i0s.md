---
video_id: -F4H-zC_i0s
title: EEVblog #1004 - Owon XDS3202A 14bit Oscilloscope Teardown
url: https://www.youtube.com/watch?v=-F4H-zC_i0s
source: youtube-asr
---

**Dave Jones:** Hi, in a previous video, which I'll link in down below, an unboxing and first impressions of this 01XDS3202A 14-bit oscilloscope. Now, this is a bit of an unusual beast because it's got a 14-bit high-resolution converter, which is what we want to look at. In fact,

**Dave Jones:** it's got a 14-bit, 12-bit, and 8-bit converter in there, which take look arbitrary waveform generator. It is not a mixed signal scope, but it's got touchscreen, it's got Wi-Fi, it's not particularly fast. Uh 200 meg bandwidth with 1 gig sample per second.

**Dave Jones:** Uh that sample rate will drop with the number of bits up to 14 bits, I believe it drops down to like 125 meg sample per second. It's got an arbitrary waveform generator, but it's got like uh CAN, I

**Dave Jones:** squared C, RS232, SPI decoding, touchscreen, VGA, Wi-Fi. It's got an app which you can scan in, and it's got a multimeter as well built in. And it's like 1,200 bucks, so it's it's not exactly an entry-level uh price point.

**Dave Jones:** So, it's in a rather niche market segment where really the only reason that you'd buy this is because of the 14-bit high-resolution converter. You might have seen in my 1,000 video, I did a comparison of uh like 11 different

**Dave Jones:** scopes that I've got here in the lab, and this one performed really well as you'd kind of expect like down in the noise and uh stuff like that. So, haven't done full evaluation on it, but anyway, it it did a you know, had a did

**Dave Jones:** a respectable job as you'd expect from something that has a a 12- or 14-bit converter in it. So, anyway, let's tear this thing apart and see what's inside, shall we? And just a a quick overview, it's like you know, reasonable tilting

**Dave Jones:** feet on there. The thing, it doesn't weigh a huge amount, and it's really really thin. Look at that, and a weird uh you know, concave sort of uh aspect to the back of So, kind of weird. Let's take out a few

**Dave Jones:** screws and whip it apart. Now, there has been some speculation about this thing that it wouldn't use a true 14-bit converter in there, or even a true 12-bit, and that it's just doing oversampling. Well, I'm almost 100% sure

**Dave Jones:** that's not the case, and it is using a real 14-bit converter in there. In fact, the converter, I believe, is an 8-bit, 12-bit, and 14-bit converter combo cuz there's a Hittite part. It's the What is it? The HM CAD 1520.

**Dave Jones:** And it's matches the Not only is it a combined ADC like that up to 8, 12, and 14-bit, but it matches the sample rate of this thing in the different modes precisely. So, I believe that's what it's actually

**Dave Jones:** using. So, I'd be stunned if it's not that Hittite part, unless there's some other uh manufacturer of some compatible part. So, anyway, can we There we go. That's our battery compartment, of course. Forgot all about that. That, of

**Dave Jones:** course, might be handy if you're using this in the field to do, you know, high-resolution logging of something like that. But, you know, probably if you're doing that sort of thing, you'd probably use a dedicated data logger. But, if you needed a

**Dave Jones:** high-resolution scope with battery, this is probably the only one on the market, I think, anyway. Stand to be corrected, but yeah, it'll definitely have a niche there. All right, let's lift this puppy out. It should Yep. Woohoo! There we go.

**Dave Jones:** That's reasonably neat and tidy. See a bit of a How you doing, cap? Just lying on its side like that. I guess they needed some extra capacitance there. But, let's take a squeeze. We've got clearly all single-board construction here. Just

**Dave Jones:** this one main PCB, which does the the end as well. The cans, they might be Oh, no. No, I think we can lift off the cans. They got some shielding over the top part of that. Oh, no. That's No, that's

**Dave Jones:** heat sinking. You can see the little heat sink divots on there. So, they're obviously going to the ADC and probably the FPGA for the main acquisition and everything else and the display and and the main application processor. No, the

**Dave Jones:** application processor is down here by the looks of it. So, yeah, likely ADC memory and uh the acquisition FPGA. Separate power supply and multimeter board. No, just the multimeter board. Um Yeah, there's a little Wi-Fi module. And this thing I think has the tiniest

**Dave Jones:** power supply I've ever seen in a scope. Here it is here. We'll have a a closer look, but basically um this thing mustn't draw much power at all because the battery it can be battery powered, of course. So, I'm I'm curious to see

**Dave Jones:** how much power this thing draws. Let's have a look. 300 mW in standby, that's awesome. VA is going to be higher, of course. There we go, 3.7 VA, but that's nice. Now, let's switch it on. Yeah, that's not too bad, around about 20 W

**Dave Jones:** and 31 VA. So, 20 W isn't too shabby, I guess. It's I think it's probably one of the lowest power ones I've seen and that's in 14-bit mode. In 8-bit mode, it's basically the same. It makes no difference. If we have a look at the

**Dave Jones:** output caps on this thing, Why men or Shishwoman quality is our life. Yeah. And there's just some other no-name manufacturer there on the primary side caps. There's basically bugger all on this thing. I mean, it's only a single rail, though,

**Dave Jones:** which is why it's a lot smaller than the others. You can actually see 5.5 V DC at 5 A output. So, basically 25 W capable. It's drawing 20 W, so yeah, okay. No worries. Um cute little power supply,

**Dave Jones:** it's okay. Um you know, no name caps, but that's par for the uh course. So, it all looks fairly reasonable for the uh price point, but you know, there's no input uh fuse in. They just put fuse No, they just put a

**Dave Jones:** link where the fuse is supposed to be. Um but we have one for Mr. and that's basically it. There's no uh poly protection or anything like that, but we've got ourselves uh exposed mains wire in here, but that's all completely

**Dave Jones:** covered with the case. Earth going over to the main point, which goes down over to the main through the Wi-Fi board, all the way through to the main plate down here, which is the plate which uh bolts in to the BNC. So, that's all quite uh

**Dave Jones:** reasonable. Interestingly, look, they've got a wire They've got some uh foil tape on the backside of the mains connector and a wire running off. You can bet your bottom dollar. Yeah, where is that? That's running over to Oh, that's our Is

**Dave Jones:** that our mains That's our Wi-Fi antenna. That's our Wi-Fi antenna. What? Okay. Um that's a bit how you doing, isn't it? Just slap it on the side of the mains connector. Oh goodness, I don't know what effect that's going to have on the

**Dave Jones:** performance, but pretty terrible, Muriel. At first, I thought that was like the uh 50 Hz uh like the mains frequency uh pickup. Like I thought they were just using like a capacitive plate and then picking up the 50 Hz that way,

**Dave Jones:** but no, that's the antenna. That's hilarious. Now, let's look at the multimeter PCB or effectively the lack thereof of multimeter. Um it's a real basic implementation with very little input protection at all. This uh thing actually doesn't specify a CAT rating on

**Dave Jones:** it. Might be the manual, I'll look it up. If it is, I'll put it in. But, it basically doesn't specify anything. Like, this is, you know, like cat one low, cat two territory. Like, pretty like it's not independently certified,

**Dave Jones:** nothing. Um as you can see, like there's hardly anything here at all. So, let's have a look at the voltage input over here. Ah, we've got a real Finder income relay. Okay, thumbs up for the Finder income relay. Um but, we've only got one

**Dave Jones:** NTC thermistor here. We've got our two uh high voltage input resistors here in the little mouth package. They have done the right thing. They've cut the uh slots under there. So, yeah, no worries, okay. But, that's basically uh your only

**Dave Jones:** input uh protection there. There are no MOV protection at all. We've got your traditional, which I did in my thousandth video. You've got your uh back-to-back Zener uh clamp with your two uh transistors there. They've also cut the uh uh isolation slot underneath

**Dave Jones:** the relay as well. So, that's quite nice, but there's basically bugger all uh protection on this thing. That's basically it. Now, if we go over here to the amps range, here's our milliamp shunt here. There's no diode protection

**Dave Jones:** on that at all. And our 10 amp shunt here is just our regular nichrome uh wire going across, which is meh, okay. That's your standard, you know, it's a little bit how you doing, but it does the job, right? You just trim it out, no

**Dave Jones:** worries. But, there's basically none of your traditional diode bridge protection or anything like that. And there's certainly no fuse protection on this thing at all. Let alone HRC fuses. We don't even have glass fuses. So, yeah, like you shouldn't even be using this on

**Dave Jones:** anything to do with the mains or anything, any high-powered stuff at all. It's strictly, you know, bench type measurement stuff. And this little down here, that one's doing the uh isolation. So, it's just doing uh power supply isolation to get an

**Dave Jones:** isolated power supply for the multimeter chipset, which is a pretty standard uh Fortune uh uh semiconductor part. You can go look that up. We might have some extra diode uh clamping protection here and here. Uh maybe that that's for the

**Dave Jones:** uh maybe the current uh ranges, but they're not going to protect like it's not even fused. I mean give me a break. That's a fail on the multimeter. Like why do they even bother having multimeter in there? Now, those keen viewers might have

**Dave Jones:** spotted that there's no fan in this thing. Oh, yes, there is. Where's the fan? Where's Wally? It's not under the case. No, siree, Bob. By the way, there's no side vents, which you'll see is might be kind of important at the

**Dave Jones:** moment. Then there's only these uh vents on the back of the concave part here. So, where's the fan? Can you spot it? Can you spot it? Where's Wally? Where's Wally? Right under there. That's probably the worst implement thermal

**Dave Jones:** implementation of an fan in an oscilloscope I've ever seen. That is awful. It's like I believe it's sucking in this way and it's pushing down probably that way and under the board and then where does the where does

**Dave Jones:** the hot air have to go? It's got to spread over here. It's got to come up, dribble up the sides here, and then out the vents here. Like on the I hear it like it's absolutely ridiculous. Who did that? Stevie Wonder? By the way,

**Dave Jones:** they have done the right thing by having this uh insulating sheet on the uh multimeter and also on the uh power supply as well. Fortunately, to get a good look at this including getting the heat sink plate off is that we've got to

**Dave Jones:** I've got to undo the base plate here. The BNCs are tied into the base plate under there. So, I've got to take the whole thing out, take off all that front uh metal work stuff or bottom metal work

**Dave Jones:** stuff, and then get to the bottom side of the screws here cuz two of them are screwed from the bottom side, two are screwed from the top. So, this is definitely a Stevie Wonder design and like Anyway, here we go.

**Dave Jones:** Can we get that? Oh, yes. Yes. Where? Almost in like Flynn. Bloody hell, backlight. That's the LCD display for you display aficionados. I know you're out there. And is that the part number for the display? Electrons are falling

**Dave Jones:** out. And what that thing was originally designed for, I've got no idea. There it is on the front of the unit, but it doesn't light up, doesn't do anything. So, there's the front guts of the main unit and you see they got a separate

**Dave Jones:** board down here for the times 10 detection down here. Got a little ribbon cable going off, so that's all just part of the keyboard matrixes and the rotary encoder matrixes. All just detecting that. Not sure about the brand on these uh

**Dave Jones:** encoders though. So, I'm not exactly sure what the LJV is it? Not sure what the marking is on that puppy. If I find it, I'll link it in. There's the backside of the main board and we can go through it in detail and

**Dave Jones:** I'm sure we will, but now I can whack the heatsink off. All right, here we go. Oh, we got some goop. We won't be able to Okay, there's no just thermal pads. Good. Excellent. Don't have to goop it. Don't

**Dave Jones:** have to clean it up. We can read that. There's our FPGA. Now, I was going to examine this board with the Tagarno microscope as I would normally do, but unfortunately bloody Windows 10 installed some stupid update on my lab

**Dave Jones:** machine here and it's just killed it. Got the blue screen of death and it just simply keeps trying to repair itself, repair itself and it doesn't bloody work. So, uh a for the macro lens. If you don't know what macro lens I use for

**Dave Jones:** most of my shots, uh um except for the Tegano, I use an Opteka * 10 macro lens that just screws on the front of my camera like this. If I can get the thread to line up. It's really hard to get these numbers.

**Dave Jones:** You got to get light at the right angle. I'm going to shine my torch on it, but yes, I picked it. It's a Had 1520. That's a Hittite part for 8/12/14 bit ADC. And you can see it is actually

**Dave Jones:** a true combined 8, 12, and 14 bit converter. It's got a precision mode which does 14 bit. Actually has a 16 bit data output, but it's only claims to be a true 14 bit converter and four channels up to 105 megasamples per

**Dave Jones:** channel. So, they're they've got two chips in here. So, they're only using the one channel here. Interesting. And they're claiming actually 11.8 effective number of bits at the 105 megasample per second in presumably the 14 bit mode. Oh, no. Actually dual 8 bit

**Dave Jones:** output, is it? Right next to that is a national semiconductor LMX 2581 and that's the VCO, of course, that generates the sample clock. And interestingly, check out this board here. They've actually got a daughter board for the oscillator. They've got a

**Dave Jones:** regular larger oscillator footprint here, but they've decided to put a smaller one on there. Mount you know, design this little daughter board and have that surface mounted on there with a little five pin SO-23. What is that a little regulator or something

**Dave Jones:** like that to they might have had an issue with there with the stability of the oscillator or or some such thing perhaps. Hmm, interesting. And by the way, they do have actually one Had 1520 per channel. So, yeah, that's not going to be cheap.

**Dave Jones:** And above the ADCs there, we've got a Spartan-6 FPGA. You can check out the number for those playing along at home. So, that's the acquisition ASIC with the uh memory either side of that thing. It looks like there would have one chip per

**Dave Jones:** channel, I would be guessing. We'll just check out that part number there and put up the data sheet. But, interestingly, above that and coupled in to the main acquisition ASIC, they've got another Spartan-6 FPGA. Doesn't look as grunty,

**Dave Jones:** but that's obviously driving uh the arbitrary waveform generator. Cuz we've got two Burr-Brown DACs there, and then that goes over we've got some more some analog and some relay goodness there, and that BNC there would be the uh

**Dave Jones:** output would be the uh arbitrary waveform generator outputs. And we've got a main application processor from TI. Let's check that one out. And this is a Texas Instruments uh Sitara processor, one of these ARM Cortex-A8 jobbies, and it's got

**Dave Jones:** everything that you could possibly want inside. It's about like less than 10 bucks in volume, but it's got the uh LCD uh controller which you want built in. It's got the touchscreen controller which you want built in, and Ethernet,

**Dave Jones:** and all the bells and whistles. So, yeah. So, they're running I don't know what sort of OS they're running, maybe some flavor of Linux, who knows. Below that, we've got some more Hynix memory, and then what have we got? And

**Dave Jones:** then the VGA output there is handled by this ChronTel part. I don't think I've seen one of these before, the 7026B. So, all right, there's the data sheet. Normally, we've uh seen it driven by the application processor directly or by a

**Dave Jones:** um some display uh FPGA in the past, typically. So, in this case, the VGA output didn't come for free. Like, it didn't come at just the cost of the VGA connector on the back and some and a couple of uh passives. It, you know,

**Dave Jones:** came at the cost of yet another chip in the bomb. And as for the uh fixed power input here, uh as we saw before, it's actually 5.5 volts. I haven't actually measured it, but that's what it says on the power

**Dave Jones:** supply. So, they're obviously allowing for like a diode drop. So, I don't see a big ass diode there to bring in the battery. So, they've obviously got some regulation stuff and that cap on its side, the Zonda Zonda cap. Yeah, great. It's like

**Dave Jones:** just bodged on there. So, they've got very little, you know, bulk decoupling on this thing actually. It's basically just the two caps on the power supply plus this one and that's pretty much it. There's a fair bit on the

**Dave Jones:** bottom if I flip it over here. There you go. So, here's the battery input contacts and you can see that there's some, you know, battery charging stuff probably, you know, all integrated into this thing and there's probably a

**Dave Jones:** chipset that handles the power supply switch over there. There's our ethernet port and is that our ethernet chipset on the bottom? Can't quite see that one. And I won't bother taking off the shield on the bottom. There's just going to be a whole

**Dave Jones:** bunch of passives under there unless we want to reverse engineer the analog front end and it's not a huge deal because I have to that's actually a can soldered down there. More relays on the bottom, lot more passive stuff around

**Dave Jones:** here which is the DAC up here for the arbitrary waveform generator. So, they've gone to a lot of bill of materials expense for the arb gen output. I can't remember the specs on that, but jeez, there's a lot

**Dave Jones:** of stuff happening in there. And speaking of relays, there's like relays everywhere. The front end, four relays per front end, another relay over here and no less than five, six, seven, eight relays for the arbitrary waveform generator and the pass fail Uh, outputs.

**Dave Jones:** Absolutely amazing. But, you know I'm a relay fanboy. And And they are NEC ones, so yeah. But, they just solved all their problems with relays, and there's nothing wrong with that. I like it. And we won't actually do a detailed analysis

**Dave Jones:** of the analog front end, but it looks like, you know, your typical modern uh 200 meg analog front end. You know, you've got your programmable gain amp up here, and just, you know, all your regular uh tran you know, discrete transistor

**Dave Jones:** stuff with some uh relay switching. And you know, it's all pretty basic. There's going to be some extra stuff on the bottom. We've got our uh solid state relay down there. And yeah, it's pretty typical. If you want to reverse engineer

**Dave Jones:** it, go for it. So, really, there's nothing hugely special on here apart from the Had 1520 14-bit uh ADCs. You know, it's got to a Spartan-6 like uh FPGA for processing like, you know, most other low-end scopes do. It seems to be

**Dave Jones:** the uh FPGA of choice. It's got an applications processor, which not nothing hugely special. It's got, you know, a basic 200 MHz analog front end like, you know, any other uh Rigol or Siglent uh you know, four sub $400 scope does. But, this is a

**Dave Jones:** $1,200 scope. So, you got to wonder where all the money's going. You would hope it would be going into the firmware and and, you know, the software interface and everything else. But, as we've seen, out of the box it, you know,

**Dave Jones:** was not a good experience at all. It was pretty much a you know, lots of features missing, failed, didn't work properly. And that was just mucking around out of the box, let alone a detailed uh you know, a performance review of this

**Dave Jones:** thing. I mean, there is a lot of stuff on here, probably more than your average low-end scope in terms of, you know, your $400 scope in terms of bomb parts, but nothing that justifies the price tag of this thing really. So, they're

**Dave Jones:** really, you know, you're paying for the specs. I'm not sure how much the Had 1520 ADCs are, but so without doing a detailed bomb cost analysis, you know, it looks like it should cost about half what it does. So, I think they're

**Dave Jones:** charging a premium for that 14-bit ADC, and there's nothing wrong with that. You know, as long as it's you know, everything's there, and the battery option and all that sort of stuff, you know. But, like because there's not much on the else on the

**Dave Jones:** market, if anything on the market like it, so I guess they can figure they can charge a premium for it. But, and I think they're justified in doing so if it's a you know, a good solid capable scope.

**Dave Jones:** And the hardware's okay, but the thermal design of it's pretty poor. Just the way it was all assembled was a little bit how you doing. It wasn't nearly as spitting polished as other scopes that we've seen tear downs of.

**Dave Jones:** So, not hugely impressed by it, really. I mean, it's it's I mean, it's not slapped together. It's not junk, but yeah, nothing really makes me want to write home about it.

**Dave Jones:** All right, will it boot? Come on. Yes! Winner, winner, chicken dinner. And the touchscreen works. No worries. So, there you have it. That's the 01 XDS3202A8. And as you've seen in my unboxing video, like first impressions not good. Lots of

**Dave Jones:** firmware issues and other usability issues. And I as I said, I don't see where the where the value is in this in terms of actual what you know, component and build cost for the $1,200. Apart from those ADCs, the 14-bit ADCs. And

**Dave Jones:** granted, the performance of it does look quite good if you're after a 14-bit ADC. In fact, there might be nothing else on the market like it, um, anywhere near this sort of price point. But, yeah, I like it's nothing spectacular. Like in

**Dave Jones:** 8-bit, it's 1 gig sample per second, 200 MHz, uh, bandwidth. It, you know, it And there's no mixed signal capability. Uh, the Arb Gen looks like it's got a fair bit of hardware in it, but, you know, and it's touchscreen. Yeah, might have

**Dave Jones:** Wi-Fi and an app, which I haven't tried, but I, like all wanky stuff, really. Anyway, not going to write home about it, but there you go. Anyway, as always with these teardowns, I hope you learned something and you found it interesting.

**Dave Jones:** If you did, please give it a big thumbs up. Catch you next time. Oh, as always, high-res photo teardown photos of this available on evblog.com, linked down below. Catch you next time.
