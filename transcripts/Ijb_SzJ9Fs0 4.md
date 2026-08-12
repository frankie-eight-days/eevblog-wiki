---
video_id: Ijb_SzJ9Fs0
title: EEVBlog #805 - Siglent SDG2122X Arb Generator Teardown
url: https://www.youtube.com/watch?v=Ijb_SzJ9Fs0
source: youtube-asr
timestamps: {"0": 0, "1": 37, "2": 60, "3": 79, "4": 96, "5": 116, "6": 148, "7": 177, "8": 210, "9": 234, "10": 257, "11": 270, "12": 299, "13": 325, "14": 351, "15": 369, "16": 402, "17": 432, "18": 453, "19": 473, "20": 503, "21": 526, "22": 564, "23": 582, "24": 615, "25": 633, "26": 668, "27": 694, "28": 729, "29": 761, "30": 780, "31": 814, "32": 831, "33": 856, "34": 885, "35": 901, "36": 943, "37": 980, "38": 1020, "39": 1052, "40": 1069}
---

**Dave Jones:** Hi, welcome to another test equipment teardown. This is the brand spanking new barely released Siglent SDG 2100 X series. I believe this is once again the only one in the country and thanks to Charles from Trio Test and Measurement for loaning me this one. I hope I don't break it. Anyway, very impressive specs on this thing. 1.2 gig sample per second, 120 megahertz. It comes in a 40 megahertz and I think 60 megahertz variety or something like that. The 40 megahertz model starts at $499 US dollars, I think just below that

**Dave Jones:** in euros. But this is the higher end model, the 120 megahertz version. I'm not sure if it's the same hardware inside and it's just software. It's not software upgradeable, I don't believe. So it could very well have different hardware inside the thing. Hope it's not just a firmware difference. Anyway, this top of the line one $899 US dollars. But for the specs, absolutely incredible.

**Dave Jones:** It's got a touch screen interface. I might be able to you've seen it in a previous video, a brief mention of it. Dual channel capability, 20 volts peak to peak output, 80 dB dynamic range claimed and that's 16-bit 16-bit converter. So they reckon we'll take a look at the converter they're using.

**Dave Jones:** DAC that is. 1.2 gig samples per second. Woohoo! You know what we say here on the EE V blog, don't turn it on, take it apart. And it looks and feels decent quality. Decent tilting bail on the thing by the way.

**Dave Jones:** Typical sort of they're pretty stiff rubber surrounds. Don't mind them anyway. It means that you can drop the damn thing onto the floor and it's you're not going to bust your knob. Nothing worse than busting your knob, let me tell you. And on the back here, once again these cheap ass QC plastic is I don't know. It doesn't instill a lot of confidence.

**Dave Jones:** Anyway, um come standard with Ethernet as most things do these days. Uh USB, looks like it has external frequency counter, auxiliary in out, not sure what the auxiliary is uh doing, probably some sort of trigger out um in or out and uh a 10 MHz reference if you've got a lab standard, that's very nice. And it should very easily slide off. We've got some torques screws in here. These would be metal threaded inserts, no worries at all. And uh the thing we're thing we're interested in is of course the uh DAC. What DAC

**Dave Jones:** they're using in? What 16-bit DAC uh they're using for the claimed um 1.2 gigasample per second. So, it looks like uh maybe a screw on the bottom. The front uh we don't have to take off. Um there's one screw on the back here. If we take that off, um it should just slide off. And I had to take the tilting bail as well off, but uh no worries there whatsoever. Once again, you know, Siglent don't do metal work that well.

**Dave Jones:** Siglent metal work is never impressive, but uh yeah, no, there's no rust. Um but yeah, it just seems like, you know, rough and ready. Doesn't instill a lot of confidence, but Siglent products are built down a price. You get real big bang for your buck. And tada, look inside. Wow, that's nice and clean, well laid out. I like that. That really is rather clean. What they've got is uh Once again, first thing I always uh notice about these sort of things, um you know, air flow and uh stuff like that. Got a

**Dave Jones:** fan on the side. Um it's not particularly loud uh blowing out this side, sucking in. They've got a grill in there. They've got There you go, between the uh power supply and just a big uh a big cut out on the other side. So, air flow, they've, you know, yeah, it's not the best thing I've seen, but it's probably adequate. Not Not sure why you'd need a fan in something like this.

**Dave Jones:** How many watts does it take? I might have to actually power the thing up and have a look. There you go, almost 18 watts for this thing. I mean, how many uh you know, a 31 VA power factor is not that uh terrific at uh 0.56. You know, why do you need like 18 watts to run a you know, a sig gen? I ah.

**Dave Jones:** But yes, it has a real clunking power switch on it, so it doesn't draw anything when you switch it off. Beauty. But anyhow, it is very neat and tidy inside and I like the uh there's the main FPGA down there by the looks of it.

**Dave Jones:** And like the the fan is like sucking the air straight across that heat sink. Beautiful. Um they're blocking the vents up here though with the uh all the ribbon cables there. That's a bit meh. But you know, it doesn't matter cuz we're not talking about much power at all. Anyway, um not sure why they've got the two separate uh uh boards here. I don't think they're opto-isolated. We'll have a good look down there, but uh maybe they've got like a generic uh it looks like a generic uh processor board

**Dave Jones:** that maybe they use for different uh instruments and things like that. And of course, that you've got your main um uh DAC and you know, your DAC will be down That's probably the DAC right there, I'd be saying. And uh your output relays and all your output uh amps and stuff like that. So, that's our whole uh analog board. So, I don't know. Generic uh probably got a JTAG interface down there by the looks of it um to program the main processor. So, let's take a

**Dave Jones:** look at some detail, but power supply in here looks quite neat. We'll have a look at that first. Power supply is not too uh shabby at all. They've got a uh the earth cable coming up here, heat shrunk on there. I would have preferred to uh see that you know, just got the spade lug. Would have preferred to see a proper nut and washer interface, but meh, nothing doing. Um they've got a protected dark glass shoes down there, like a protective uh uh cover over it.

**Dave Jones:** Looks like maybe mauve protection down there, is it? Can't quite see. Anyway, they put some Silastic on that. Uh, nice big um mains wiring going over here to the front panel switch over there. I like that. They ran out of room to obviously route that on the board and to keep their mains um voltage clearance and stuff like that.

**Dave Jones:** So, they've jumpered a cable over there. That's even got heat shrink on it. Gee, you know, they've gone to a bit of trouble to uh tie them together there. Um, all the output caps have been Silastic'd down, and it's just uh rather neat and tidy. It's got all the uh requisite stuff you'd expect. And our main input filter cap, Rubicon. Thank you very much. They haven't skipped there. Very nice. And it looks like almost all of the output caps are Rubicon. Thank you very much. And got a

**Dave Jones:** proper isolation slot down there, routed out around the mains connector front panel switch, because, you know, this is the Here's the 240-V mains, and here's the um output uh secondary side. So, yeah, you've got to have that isolation slot. But, that is a rather neat and tidy power supply. Looks like it's using quality parts. It's got all the requisite stuff. Um, yeah, so thumbs up to that. And the main processor down there, I don't think I've seen one of these puppies before. This is a Texas

**Dave Jones:** Instruments AM3352. It's part of the uh Sitara family processor. I don't know what Sitara means. Just um um wank word they've pulled out of their backside. Anyway, it's a basically an ARM Cortex A8. It's got some image processing built in. It's uh supports Linux and Android, those, you know, high-end operating systems.

**Dave Jones:** Got Ethernet MAC built in and all the requisite um stuff. And this one is the uh ZCZ, which is the uh can go from well, I think 60 on the end there is the 600 MHz model, but it can go up to 1 gig. So, pretty speedy processor.

**Dave Jones:** Then we've got our firmware flash memory and just some SDRAM surrounding that. Nothing much doing on there at all. It's all pretty boring. And hello, microSD card socket down there by the looks of it. That allows them to you know, boot stuff on here, probably program it, do some development and stuff like that, but it's not Well, there's nothing in there. So, they obviously, you know, they paid for that connector. They've put it on in production. So, obviously they're using it. If they didn't intend to use it

**Dave Jones:** during the production process in somehow, then, you know, you wouldn't pay the money to actually populate it. And I presume we've got a JTAG interface there. And this little five-pin job, could that be some sort of serial monitor interface, perhaps? I know what you're saying, Dave. Show us the DAC. Well, here it is. And yes, they're not lying.

**Dave Jones:** It's a TX DAC from Analog Devices. It's the 1891 22. And it does the business as it says on the front. This is a dual-channel 16-bit DAC, high dynamic range, 1.2 gig samples per second. This puppy goes for about Well, I know Digi-Key at least goes for 60 bucks in 2,000 quantities. It's not a cheap chip that you are designing willy-nilly. And in terms of power consumption, this thing takes about 1 and 1/2 W on its own operating at the full 1 gig sample per second. So, and it really is a very

**Dave Jones:** professional, high-end DAC. And I'll link in the data sheet, of course, for all you DAC aficionados, and you can drool over the specs for yourself. But yep, they're not lying. It does the business. And looks like we've got some anti-aliasing output filters next to it.

**Dave Jones:** That's That's what you'd expect. They've got that all all discrete. You can see the little blue parts there are the inductors. You should be able to see the windings on those perhaps. And yeah, they're That's a complex network if there ever was one. And of course, as you'd expect, there's two of those. So, two identical networks. Couple of missing parts there. I'm not sure what the business is there. There we go. So, where's Wally? And the accuracy and stability is going to depend upon that puppy.

**Dave Jones:** I don't know who's who's that manufacturer of that 10 MHz reference oscillator, but as you saw on the back, if you've got a much better lab frequency reference standard 10 MHz reference standard, plug it in and use that for this high-end instrument cuz really this is quite a high-spec unit.

**Dave Jones:** And you know, if you want to get the performance out of it, probably worthwhile sticking in an external reference. And they've got decent relay switching on the output as well. NEC, thank you very much. No one hung low rubbish in here. And there's our output amplifiers. Two of them there mounted on a little thermal pad on the back by the looks of it. These are Texas Instruments THS3095 high-bandwidth current feedback operational amplifiers. And you can see the 49.90 output resistors there on the other side. And these are spected over

**Dave Jones:** 200 MHz bandwidth. So, yeah, um presumably whether or not they use these in the 40 MHz model or whether they use lower spec parts, I don't know. We'll have to get somebody else to do a teardown of the 40 MHz model. And although both connectors are down here, they've got two of those per channel because it's all duplicated, all the relays, everything else. There we go.

**Dave Jones:** We've got another two output amplifiers up there. So, it's got to go a fair way to the output connector. And although I can't get that heatsink off because it's uses thermal adhesive and tell you what FPGA they're using in there unless they hook up to the JTAG and try and get the ID and stuff like that. We can tell, maybe, by this puppy here, which is the EN2342 4 amp buck converter. This is recommended by Altera. So, this is like Altera have a application note on this,

**Dave Jones:** how to power their Altera FPGAs with this puppy. So, almost certainly they're going to have an Altera FPGA in there. Which one? Nah, does it really matter? Anyway, that's just chewing most of the power in this thing, but look at the pin pitch on that bastard, would you? Look at it. That is evil. And that's a 0.5 mm pin pitch, but thankfully, almost most of those pins are not used. They're just not connected or they're grouped together. And this package is really interesting here.

**Dave Jones:** Here's some data for it. It's actually got a really big ground power pads on the bottom around about this location here. You can see it's a really thick package, so I'm not sure what the business is there with the die in that inside of it, but it's very interesting.

**Dave Jones:** Here's a photo of the thing. And some details. You can see there's a huge ground pad on the bottom and they give you footprint recommendations. There's thermal pads and everything and it's a rather obscure package. One you're definitely not going to get the footprint for in any CAD package on the planet. So, you you know, you would have to roll this one your own unless they specifically had all the Enpirion parts already done for you. But, yeah, it's pain in the from a PCB layout point of

**Dave Jones:** view, you go, "Do I have to use that package? Really?" Uh anyway, breaks the monotony. Anyway, just this uh converter chip alone uh more than 10 bucks in, you know, a couple of hundred quantity. So, it's not a cheap puppy either. And then we got lots of linear regs all around here.

**Dave Jones:** There we go. You know they're not uh switching converters by the uh look, by the lack of inductors around there. And uh it's common to get those um five-pin uh packages like that for various adjustable linear uh regs. But, um yeah. So, lots of power supply. That's the problem. When you start talking FPGAs like this and other logic and stuff like that, you know, you need to get all these different rails.

**Dave Jones:** So, they're going to have uh this is 20 V peak-to-peak. So, they're probably going to have uh plus-minus uh 12 or plus-minus 15 uh V rails here for the analog section. They're going to want to keep that quiet. So, that's all going to be separate. They'd have uh separate, you know, 5 or 3.3 V digital. Then they'll have the various uh core voltages. I mean, obviously the the main switch we looked at uh down here is actually uh the doing the main core uh for for the FPGA main core

**Dave Jones:** voltage there. But, yeah, I mean, you just need lots of power supply stuff. Just look at the board. I mean, you know, 1/3 of it is bloody power supplies. And right next to the analog in filter, there's a little puppy there.

**Dave Jones:** The H1K513. And I don't know what that sucker is. I've just Is that some sort of uh diff amp? And then on top of that, we've got ourselves a Texas Instruments OPA695. That's a bit of a beast. That's a ultra high bandwidth current feedback op amp and it's got like you know 1.2 gig bandwidth at a gain of two. So, pretty schmicky device and once again these two chips are duplicated on the other side right down there if my damn thing will focus. There we go.

**Dave Jones:** So, clearly what's going on here with the one channel like I got our DAC here and this is a current output DAC by the way. So, we've got ourselves a massive any Allison passive network here and this is got to be a current to voltage amplifier and then we've got our real high bandwidth voltage amplifier here which we looked at and then probably I haven't looked at these two but I'm guessing um maybe some DC offset stuff happening around here and then there's our two output drivers there.

**Dave Jones:** So, that's duplicated exactly down on the second channel as well. Yep, I just checked these two puppies here are AD8512A's. They're just you know some sort of like almost jelly bean low noise JFET op amps. So, as I suspected most likely doing DC offset functionality. So, there you have it not much else to it. That's a look inside the new Siglent SDS2000X series. Let's go to Thanks Charles at Trio Test and Measurement for loaning this one letting us have a look and starting at 499 bucks for the specs.

**Dave Jones:** Jeez, it looks pretty schmick let me tell you. It's built fairly well. I got no issues with that at all. It looks like it'll do the business. So, as always if you like that please give it a big thumbs up and hopefully I'll do some more stuff with this before I have to send back. It's only a demo loaner unit and well, hopefully probably compare it with the existing Siglent one I've got and the Rigol one as well. Hopefully. So if you want to discuss it, forum link down below, blog,

**Dave Jones:** YouTube comments, all that sort of jazz. Follow me on Twitter, blah blah blah. Support me on Patreon. Thank you to all my Patreon and other financial supporters. It's what keeps the blog going and yeah, buy my merch and you know, all that sort of stuff or I don't know. If you don't like any of that, don't do any of that. That's fine, too.

**Dave Jones:** Thanks for watching. Catch you next time.
