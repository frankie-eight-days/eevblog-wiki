---
video_id: Qjj49bFimoo
title: EEVblog #87 - Let's hop on the Electronics Design Merry-Go-Round
url: https://www.youtube.com/watch?v=Qjj49bFimoo
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 33, "3": 46, "4": 64, "5": 89, "6": 105, "7": 126, "8": 142, "9": 159, "10": 173, "11": 189, "12": 203, "13": 221, "14": 234, "15": 250, "16": 268, "17": 284, "18": 302, "19": 323, "20": 336, "21": 355, "22": 371, "23": 386, "24": 406, "25": 422, "26": 440, "27": 456, "28": 471, "29": 490, "30": 505, "31": 521, "32": 538, "33": 552, "34": 572, "35": 590, "36": 605, "37": 616, "38": 632, "39": 649, "40": 666, "41": 680, "42": 698, "43": 713, "44": 730, "45": 748, "46": 767, "47": 781, "48": 796, "49": 808, "50": 826, "51": 846, "52": 865, "53": 882, "54": 898, "55": 910, "56": 928, "57": 951, "58": 964, "59": 978, "60": 994, "61": 1012, "62": 1033, "63": 1048, "64": 1066, "65": 1083, "66": 1097, "67": 1113, "68": 1129, "69": 1151, "70": 1168, "71": 1190, "72": 1207, "73": 1224, "74": 1243, "75": 1256, "76": 1274, "77": 1296, "78": 1315, "79": 1330, "80": 1348, "81": 1364, "82": 1379, "83": 1394, "84": 1411, "85": 1428, "86": 1448, "87": 1462, "88": 1477, "89": 1498, "90": 1517, "91": 1531, "92": 1547, "93": 1564, "94": 1584, "95": 1602, "96": 1621, "97": 1638, "98": 1656, "99": 1683, "100": 1699, "101": 1710, "102": 1723, "103": 1734, "104": 1751, "105": 1764, "106": 1780, "107": 1798, "108": 1816, "109": 1834, "110": 1845, "111": 1860, "112": 1876, "113": 1891, "114": 1903, "115": 1918}
---

**Dave Jones:** Hi, welcome to the AAVlog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I'm working on a small design at the moment, and I thought I'd just share with you a little glimpse of what it

**Dave Jones:** goes into actually designing something like this and searching for parts. And it's real interesting. I call it the design merry-go-round because once you hop on it, you'll say it's very difficult to get off, and you can spend a typical

**Dave Jones:** design engineer can spend a hell of a lot of time just searching for parts. In fact, that's what they'll spend most of their time doing. So, let's take a look at it. Okay, let's take a very quick look at

**Dave Jones:** the design here. I won't go into details of what it is or what it does, but we have a We have a micro here. Okay, I'm going to need two PWM channels. I'm going to need a couple of ADC channels 10 bits or

**Dave Jones:** thereabouts. Maybe I can get away with eight. I'm not entirely sure. Now, um I need 24 IO channels. That includes PWM and ADC for switches and other various things. So, 24 IO, that's going to be a driving design criteria for the actual

**Dave Jones:** design because that will determine what package what minimum package size I'm going to need for the design. Now, over here, okay, I've got a load. It doesn't really matter what it is, but let's just say I have a load down here,

**Dave Jones:** okay? And then I have what I want is a high-side current monitor because I want to be able to measure the uh um, want to be able to measure the, uh, the the current flowing through the load. So, I I need either a

**Dave Jones:** high-side current monitor. This is, um, plus V up here. It's what's called a high-side current monitor. Or, I could possibly, uh, maybe even do it with a low-side monitor down here like this and just tapping off into a differential,

**Dave Jones:** um, amp or even a single-ended amplifier down here. But, there's, um, so there's various ways I can do this. And depending upon the micro I choose, um, and various other aspects will determine what parts, which way I actually design

**Dave Jones:** this. Cuz you I might find that these high-side current monitors here are are very expensive. Um, or I might find it's cheaper just to roll my own differential, uh, amplifier and do it that way. Or, there's a whole, um, bunch. And that's

**Dave Jones:** only two aspects to design. There are other parts, but we're just going to look at basically the high-side current monitor and the microcontroller. Okay, let's hop in this design merry-go-round, shall we? I've got four tools open here. First one's Digi-Key.

**Dave Jones:** The next one's Mouser. Next one is finechips.com. And the next one is octopart.com. I've mentioned all these before. Now, let's start out with Digi-Key. And let's start out with that, uh, high-side current monitor that we're talking about. So, it's already there.

**Dave Jones:** I've already searched for stuff like that. So, let's try Digi-Key and a high-side current monitor like that. There's 479 of them, current regulation and management. Got to make sure you choose the right category there. Otherwise, um, you A good idea is to choose the one

**Dave Jones:** with the most, um, numbers on them there. So, that one's got 479 items. That's only demo boards and things. So, but it gets more complex for other fields. Anyway, let's go in. I'm not too concerned and here's the

**Dave Jones:** parametric data, okay? All this parametric data here is what you can use to sort your parts sort your parts down because we're looking at 479 parts at the moment and that's a lot. Now, I'm not really too concerned about the case

**Dave Jones:** and the package at the moment. Accuracy, I'd like 2% or less. Let's say 2.5% or less. So, let's highlight that and go apply filter and it looks like here we go. We've got 255 items now. That's still quite a lot. So,

**Dave Jones:** let's go in stock parts only. Apply filter and 62 items. That's very manageable. So, let's go into view page and see what we've got here. Now, you might have to scroll off the side here cuz often this can be very

**Dave Jones:** wide to get the price over here. But as you can see, it's given us a whole bunch of parts. Most of them are a Diodes Inc. and Zetex brand. Now, there Zetex make good little parts. I've used them before, so I'm happy with

**Dave Jones:** that. Now, let's look at price here. I mean, I'm looking at things like a dollar $2.28 each 68 cents in 3,000 quantity. Now, Digikey, they do actually sort by price here, but it's not as good as Mouser because

**Dave Jones:** it it intermixes quantities and all sorts of stuff in there. I'll show you later that Mouser is actually better to search for if you really want price. But that looks like what we're up for for a high side

**Dave Jones:** current monitor is roughly maybe you know, 80 cents. Let's Let's go in and take a look at one. Shall we? Let's take a look at the 1010 part here and that's a sot23-5 package. I'm fairly happy with that and

**Dave Jones:** look the price breakdown for 100 quantity is like 94 cents. That isn't too bad. So we're probably up for 80 cents to a dollar for a high side current monitor. Now that's a that's you know, that's a fair chunk of my price

**Dave Jones:** budget for this thing because it's like half the price of the microcontroller I'm going to be using which might be the most one of the most expensive parts. So it's a quite an expensive little beast but and we can go

**Dave Jones:** straight in and jump straight to the data sheet and actually check out the part. And it's hard to get this in frame here but let me try.

**Dave Jones:** There we go and it's we've got a simple high side current monitor there. It's got a single resistor. It's got a current sense resistor external and it just senses that and gives you a current output which convert to a voltage by putting a

**Dave Jones:** single resistor there and that's very nice. That's that's pretty much exactly what I want. Supply voltage 2.5 volts to 20 volts perfect for this application. Although the minimum side here 2.5 volts means I probably can't use it on the lower side

**Dave Jones:** hence hence the name really. It's a high side current monitor but I'll go into that later. So that looks like a suitable part. I'm quite happy with that. I think we've found a generic high side current monitor. Now let's just do one more additional

**Dave Jones:** thing here for the high side current monitor. As you can see diodes Intersil Tech's are the major manufacturers down in the price category. Linear technology down here, but they're like ouch, five bucks a pop. That's really expensive, but let's just double check this on

**Dave Jones:** Mouser, shall we? Uh high side current Well, let's just search for high side current and semiconductors down here. As you can see, integrated circuits, power management ICs. That's it down there and current and power monitors and regulators. As you

**Dave Jones:** can see, 55. Don't choose any of the others because well, they're obviously they've got a lower parts count number, which means that then it's not really what you want to look for. So, current and power monitors and regulators. Let's go into that.

**Dave Jones:** And let's see what Now, good thing about Mouser is that Mouser allows you to actually sort by price here. So, if you hit this button here, okay, we've got uh how many parts have we got? We've got 55 parts um just up

**Dave Jones:** front. So, not as many as we got from Digi-Key, but here we go. It's once again the Z Tech's ones or diodes Inc. have popped up with the ZXCT series again. They look like the cheapest. There's an Exar one down here.

**Dave Jones:** Let's see what they they're they're like a dollar each in quantity. The Z Tech's ones are a bit cheaper. Um look, there you go, 83 cents. So, that's cheaper than Digi-Key. So, I like that. The uh let's go for the

**Dave Jones:** one 1009, shall we? Let's check Oh, look, it's a SOT23-3 package as opposed to the SOT23-5 that we had before. So, let's look at the data sheet for that and check it out. Yep, that one's much simpler. It's only a three-pin

**Dave Jones:** uh package. Much, much easier. And as you can see, it's the same voltage range, 2.5 to 20 V, which is perfect for the application, 1% typical accuracy, and a nice um easy-to-use SOT23 package. It's not too small, it's easy to hand solder. Um

**Dave Jones:** and we'll go into the uh you know, I need to investigate the technical specs and stuff like that, but definitely I found I'm going to stick with that as a first shot. Um I'm going to use this model as my high-side current monitor.

**Dave Jones:** Now, just as a double-check, when I choose a part like that, what I'm going to do is I'm then going to use FindChips or Octopart to see the price. So, I just copy and paste the part number, I put it

**Dave Jones:** into FindChips, and it'll search all the different manufacturers. Um whoop. I shouldn't have hit that. And here they are. Mouser, there we go, 83. It shows you um it doesn't show you It usually shows you if you have if they have stock. And if

**Dave Jones:** we go over here, they're actually on order. They're not actually in stock. So, the 1009 in the SOT23 package um is not in stock from there, but I think we could probably get it from Mouser anyway. Uh findchips.com,

**Dave Jones:** uh it's available from Future. They have no stock. Um Quest Components have 79. Um so, it's it's available from not available from Digi-Key, it says actually, but if you search for the more generic number, take out the FTA on the end, you'll find

**Dave Jones:** that you get more hits. There we go, um in stock. There we go, Mouser have that uh in stock, and you can get direct links straight to the Mouser website. So, if I hit that, it'll actually take me straight there again. Once again,

**Dave Jones:** that's not the SOT23-5 package, but um still they they have that in stock, and as you can see um it's 98 cents from Arrow. Newark have don't have any stock, but it's reasonably priced from them as well. Digi-Key actually have it in stock.

**Dave Jones:** There it is. So, if we hit that, we can jump straight to the relevant Digi-Key page. Once again, it's not the SOT23-5 package, but um I can optimize that later. But So, I just wanted to show on here that when you when you're picking a

**Dave Jones:** part, it's good just to go to FindChips or Octopart so that you can um find and to actually see if that part is actually available. Um from different suppliers or not. And and and at what price. So, that's very

**Dave Jones:** important criteria when you're optimizing your design for price and availability. Okay, let's try the same thing again, but now we want to find our microcontroller. I'm going to go straight to Mouser this time, and I'm going to type in microcontroller.

**Dave Jones:** Now, um you could argue that I should have done the microcontroller first, but it doesn't really matter. Now, semiconductors down here, we've got microcontrollers and microprocessors. There's the category I want. 27,000 parts. Fantastic. Um a subcategory, microcontrollers. Yes,

**Dave Jones:** 19,000 parts, which is really quite amazing when you think about it. Now, here we go. I can limit it to just a particular manufacturer. So, if I'm you know, a fan if I want to use a Microchip part, there's 7,600. If I want to use

**Dave Jones:** Atmel, there's 2,100 up there. But I don't I'm not fussy about the manufacturer at this stage. What I am fussy about is uh price and package and pin count. Pin count's very important cuz I don't want one with too few, and I

**Dave Jones:** don't want one with too many cuz pins because the package will be too big. Now, so I know I've got 24 I need a minimum of 24 I/O. So, I'll go to number of programmable IO on the parametric

**Dave Jones:** search here. And this is the great thing about parametric search. Now, um I probably might be able to handle say up to 40 pins, say a 44-pin PLCC package or um quad flat pack or something like that. So, I'll go from 24 to 40 and I'll apply

**Dave Jones:** the filter. And we've got 19,000 parts at the moment. We're down to 5,600. Okay. You know, we're getting down there, but even with 5,600, Digi-Key allows you uh sorry, Mouser um allows you to once again come down here and just bang, sort from lowest to

**Dave Jones:** highest price. So, let's take a look. Curious curiosity what which uh manufacturers are going to show up? Well, Microchip uh right up the top. That's not surprising with a PIC16F59 uh part. And that's a $1.32 in 100 quantity. Um but look at that, there's

**Dave Jones:** an NXP uh Cortex 32-bit ARM processor down there, but look at the package. Don't like it at all. Um I'm not very happy with that. And really, Microchip, there's a couple of Freescale ones down here. NXP, but um

**Dave Jones:** you know, Microchip really um do show up there. So, I'm going to show and I know Microchip are some of the cheapest micros on the market, but we'll try Atmel later. But let's go up and just limit our search to Microchip. Now,

**Dave Jones:** what's once again the 16F59? Now, I know from memory that that one's actually not going to do the job. It doesn't have the um ADC and oh, I don't think it has the ADC and the PWMs I need and stuff like

**Dave Jones:** that. The 16F722, that might do the job. Okay. Now, what uh package is that in? If we scroll over here, it's an SSOP package. Uh not too happy with that. There's a SOIC 28. Yep, there we go. That one's available in SOIC 28. So, I

**Dave Jones:** like that. Let's look at the um 16 uh F722. If we open the data sheet, let's check it out. Um now, what have we got here? Let's zoom in and uh we've got um Oh, look look at that. The

**Dave Jones:** analog-to-digital converter is only 8-bit resolution. It does have an internal voltage reference, but 8 bits really isn't going to cut it for me. I really need uh you know, say 10 bits or something like that. 12 is a bit

**Dave Jones:** overkill, but I could maybe get away with eight, but I really want um 10. Now, um so that that really rules it out, even though um there's two PWM modules down here, so it meets my requirements for the number of PWM

**Dave Jones:** modules. Let's scrap that, because that part is not suitable at all. It doesn't have the ADC. Now, let's go down. Aha, there's another one. PIC16F822. Let's check that out, shall we? The 882. There we go. Let's Let's try that one.

**Dave Jones:** The 882. So, let's go in here and check it out. Now, AD converter, there we go. 10-bit resolution, 11-14 channels. I only need a couple of channels, so um that's fine, but it's 10-bit resolution. Now, does it have the

**Dave Jones:** number of PWM channels? Capture, compare, PWM module. Um there's a 16-bit one down here. Enhanced capture, compare, uh 10-bit PWM with one, two, or four output channels. Fantastic. So, um it basically there's a suitable microchip part there. I I like it. I'll

**Dave Jones:** use the um I probably need the 884 or something like that. You'll have to go into packages uh later. Here we go. If we go over here, um let's say the 884 and I need about 4K of flash memory. It's got some e-squared

**Dave Jones:** prom, which is great. It's got 35 IO. It's got uh uh two 8-bit timers plus a 16-bit timer, which is the PWM as well. So, bingo. I think I've found a suitable Microchip part for my design. The 16F

**Dave Jones:** uh 88 388 or 88X series. Um I need to go into more details than that, but off the bat, um that looks like a very suitable uh part and it's only a $1.81 each in 100 quantity. Excellent. Now, because

**Dave Jones:** I'm optimizing this design for price, I don't just want to limit myself to Microchip. So, let's hit the back key here and let's go down to Atmel cuz I have the tools for Atmel and I don't mind Atmel. So, let's go. There's 695

**Dave Jones:** parts from Atmel and let's Once again, it's all it's already sorted by price, yes, as you can see. Little button there. Now, let's take a look at uh what we've got here. The ATtiny 48. Now, it's a $1.63,

**Dave Jones:** which is a bit cheaper than the Microchip one. It's uh that's in a PDIP package, but it's available in a TQFP-44. That's adequate. So, it's got the correct uh number of IO I need and it's got 4K of flash memory. So, let's take a

**Dave Jones:** look at that. The ATtiny 48. And wait, here it is. Okay. Oops. Now, uh what do we got here? We got um yeah, we got e-squared prom. That's enough. I only need a few. We've got 4K or 8K. Uh

**Dave Jones:** we've got um uh six or eight channels of 10-bit ADC. Great. Now, the Atmel's have this ADC noise reduction mode as well, which can be handy. So, that's really good. Now, so it has the ADC I need, but,

**Dave Jones:** does it have the, oh, look at that, it's available in a 32-lead TQFP. Fantastic. That's a nice size device, but does it have the PWMs? On-chip programmable, where are we? It doesn't really, uh, one 16-bit timer counter, one 8-bit timer counter.

**Dave Jones:** I might have to drill further down into the details. It's It's really quite annoying when it doesn't tell you up front what the, what the parts actually have. Okay, now let's try that again. Let's go to atmel.com cuz I want to, uh, use the

**Dave Jones:** parametric search on their website because I'm not going to, um, get as great a parametric search typically on Digikey or Mouser as you can get, uh, in the individual manufacturer's website. So, let's go into their microcontrollers, AVR 8-bit 32. It's not

**Dave Jones:** the world's best, uh, website. Let's go into devices and here we go, parametric table. So, let's go into the parametric table for their microcontrollers. Now, we only want, let's say, the tiny range of AVRs because really, um, my design is tiny, so their name is

**Dave Jones:** quite apt. Now, here's the tiny, here's all the tiny AVR devices down here and they fit on one screen, which is pretty excellent, but you have to scroll right across if you want to see packages and things like that. Now,

**Dave Jones:** once again, the parametric search is really good cuz you can sort by number of IO pins. So, let's do that, shall we? Let's sort search sort from, uh, highest to lowest on the IO pins. Oops, it's done it the other way around. Anyway,

**Dave Jones:** the only ATtiny device we've got is the 24 28 IO. Perfect. It's available in a TQFP32 as we saw on the Mouser website. Fantastic. So, the ATtiny48 looks like a very suitable part, but let's go over to here where PWM

**Dave Jones:** channels. Okay, down here. Oops, there we go. One PWM channel. That's no good. So, I have to rule out that ATtiny device. What a shame cuz that was that was really cheap part. It just doesn't have the PWM channels. Now, if it looks

**Dave Jones:** like every other ATtiny device with the exception of that one has at least two PWM channels. So, I don't know why these ATtiny48s only have one. Oh, what a shame. Oh, well, you can't always win. Anyway, let's look at

**Dave Jones:** some of the others. But, the others in the number of pins down here, it's only got 18 IO. The max number of IO pins. That's just not enough. So, I really um Atmel, it looks like off the bat do not have a suitable part in their

**Dave Jones:** ATtiny range for my design. I just can't get the IO I need with the number of PWM channels. What a shame. So, let's go to the ATmega range up here, but I know the ATmega range are more expensive. Um

**Dave Jones:** So, let's look at the number of IO down here. These packages down here, they've all got the uh PWM channels. Oh, these ones here don't have any PWMs at all, but everything else, it looks like there's none with

**Dave Jones:** just one PWM tech like in the ATtiny range. So, that's really good. But, um the ATmegas, even if we go for say an ATmega8, um which I know is one of their lower sort of end parts, or the 8A, I think it

**Dave Jones:** is. It's only got 8K of flash. It's a bit It's a bit overkill, but um it's got three PWM channels. So, let's go to the ATmega8A, uh and take a look at that. Um in fact, I know it's going to do the job uh

**Dave Jones:** pretty much, but um it's in a TQFP32 package. Fantastic. Um I know it's got the PWMs and ADCs I need, but uh let's go in and look at um to see what the actual prices are. So, let's go in and search for the

**Dave Jones:** findchips.com, and let's take a look. Mouser and Newark have it. Mouser have it at a dollar 68, but that's a 780 pricing. They don't actually have it uh in stock. And if you look at Newark, Newark are usually pretty well priced

**Dave Jones:** for their parts, but look, uh for a one to for a 100 to 299, it's $2.55. It's It's more expensive than the equivalent Microchip parts. So, I think that's just, you know, you're you're paying more for that extra 4 KB internal flash,

**Dave Jones:** and it's just It's a bit too expensive. A dollar 99 down here from Arrow, but they don't have it in stock. 18 weeks lead time. Yeah, have blow it out my ass. Really. Um So, uh that's a that's a real shame. So,

**Dave Jones:** it looks like um the ATmegas range have probably priced themselves out of this gig. Now, I can maybe squeeze in one of the ATtiny parts uh if I look at um limiting or redesigning my IO architecture to actually uh change to limit the number

**Dave Jones:** of IO. So, I can use like an external serial 74HC serial chip to actually to minimize the number of IO. And I might be able to then use one of these smaller ATtiny parts like maybe the ATtiny4313 down here.

**Dave Jones:** That's got 18 IO. So, I might be able to squeeze that one in. But you've got to weigh up the cost of that and the benefits versus that external chip compared to the microchip the actual microchip design. So, that

**Dave Jones:** extra external chip might cost you an extra you know 20 cents or something like that. And you have to weigh those sort of things up and extra board space as well. Now, there is something that I did remember though. I've used the ATtiny26

**Dave Jones:** part before. It looks like it's no longer available. But it looks like they do have a 261A which is the upgrade to that or the 461A which is the 4K part. Now, let's look at that for a second because I know this had a

**Dave Jones:** rather interesting aspect to it. Let's let's open the data sheet here. Okay, here we go. The ATtiny261A. Now, what it's actually got let's have a look here. Yeah, three high frequency PWM outputs. Excellent. Okay, so it's got the number of PWMs. But check this

**Dave Jones:** out. It's not only does it have a 10-bit ADC, 11 single-ended channels, but it's got 16 differential ADC pairs. So, it's actually got differential amplifier in there. And this is really fantastic for this sort of design I'm doing which has

**Dave Jones:** high side or current monitoring because basically what you want is a differential amplifier across the current sense resistor. And it's also got programmable gain. Check it out. Times 1, times 8, times 20, and times 32. Now, that's really inviting.

**Dave Jones:** Um now, unfortunately, though, it's only available with 16 IO lines. So, it's very limiting. It's a 20-pin um SOIC package. So, it it doesn't meet the number of IOs, which is a real shame. But, I might be willing to go

**Dave Jones:** back and look at my design to see if I can make use of uh the uh the differential 80 the differential ADC and the programmable gain, cuz I might be able to completely eliminate my high-side current monitoring chip. Now,

**Dave Jones:** the ATtiny461, let's go and take a look at that uh price-wise from Fine Chips, ATtiny461A, and let's have a look. Mouser, it's a $1.88 for 690 pricing sale. It's not it's not too bad at all. Now, as you saw in that, we found that

**Dave Jones:** um this high-side current monitor is going to cost like um maybe 80 cents to a dollar or something like that or really, you know, 80 cents it's going to cost. And, that's that's half the cost of this micro, which is which is crazy,

**Dave Jones:** really. So, I'm going to have to go into details to see whether I can use a spare op-amp, cuz I know I've got going to have one op-amp left over. I've got like a quad op-amp uh package in the design,

**Dave Jones:** and there's going to be one spare. So, maybe I can do a low-side current sensor or something like that. But, the problem with that is that um then it actually raises this voltage here uh by the voltage drop in the

**Dave Jones:** resistor. And, that can be about 0.1 V or something like that, cuz I want to use a 1 amp in the current anyway. Uh the details aren't really important, but um I don't know if I can actually do

**Dave Jones:** this low side um current monitoring because of this uh increased voltage here. I might be able to do some weird arrangement with the grounds. So, this um this ADC uh ground I might be able to, you know, uh tie into here, but the power ground I

**Dave Jones:** might be able to tie into there or something like that, but I've got to look into all those details, but um yeah, I you know, 80 cents for that little part I'm I'm a bit offended by that, really. So, um I'm going to have

**Dave Jones:** to, you know, I I might have to use it, but uh there's the you know, it's the design merry-go-round. Just reiterate this design, and I'm only looking at uh you know, two aspects to it. It's crazy. So, even though this was a quick example, as

**Dave Jones:** you can see, um I've spent a lot of time in these parameter using these parametric search tools, and uh these uh price comparison price and availability websites, and they're all very uh powerful tools that allow you to optimize your designs uh for whatever

**Dave Jones:** requirement you're after, be it um uh price, availability, package, size, performance, uh things like that. There's no end to these, and I've only used two parts as an example, the high side current monitor and the microcontroller. And I can assure you I,

**Dave Jones:** you know, I haven't finished this uh search. It could go on for days um opt where I optimize my design and then I reiterate my design based on things that I find uh on these websites, suitable parts. I I might even even add in a part

**Dave Jones:** to my design by doing that. I might be able to reduce the cost, or I might consolidate uh parts to to the cost, or I might find that one package is, you know, it's a only available in a

**Dave Jones:** horrible BGA part or something like that, so I can't I I don't really want to use that in my design. And it just goes on and on. This design merry-go-round, it can you can it can be an end until it's so until itself. It

**Dave Jones:** really can. It can get crazy, and you can get so caught up in it even for a basic design. I mean, you know, if you're just designing something that has you know, a a very basic requirement. You're just going to make one of, then

**Dave Jones:** you probably wouldn't care about this. You wouldn't care about cost or anything like that. You wouldn't, you know, you'd just get the easiest to use package. But there are other designs where you can spend days and weeks just mucking around with

**Dave Jones:** all these tools. And really, a design engineer's job, you might think is drawing circuits and laying out stuff. No, it's not. Probably 80% of your time, I just pulled that number out of my ass, but it's going to be

**Dave Jones:** quite high. You know, 80 90% of your time might be spent just doing these parametric searches and bill of materials and optimizing your cost and all sorts of things. It's just one big merry-go-round, and once you hop on, it

**Dave Jones:** can be difficult to get off.
