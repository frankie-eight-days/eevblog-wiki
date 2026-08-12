---
video_id: 32-DhE_5wG0
title: EEVblog 1679 - Why Does a Uni-T AWG Cost $5800? - BOM Cost Analysis
url: https://www.youtube.com/watch?v=32-DhE_5wG0
source: youtube-asr
timestamps: {"0": 0, "1": 22, "2": 39, "3": 58, "4": 71, "5": 88, "6": 102, "7": 115, "8": 129, "9": 145, "10": 155, "11": 170, "12": 183, "13": 202, "14": 215, "15": 229, "16": 241, "17": 255, "18": 267, "19": 277, "20": 291, "21": 304, "22": 317, "23": 329, "24": 342, "25": 357, "26": 368, "27": 380, "28": 394, "29": 402, "30": 417, "31": 430, "32": 442, "33": 455, "34": 468, "35": 480, "36": 495, "37": 507, "38": 519, "39": 532, "40": 544, "41": 559, "42": 574, "43": 587, "44": 600, "45": 618, "46": 632, "47": 647, "48": 665, "49": 681, "50": 695, "51": 709, "52": 727, "53": 740, "54": 753, "55": 769, "56": 782, "57": 796, "58": 810, "59": 827, "60": 839, "61": 853, "62": 868, "63": 881, "64": 894, "65": 909, "66": 924, "67": 939, "68": 952, "69": 967, "70": 977, "71": 991, "72": 1004, "73": 1016, "74": 1030, "75": 1044, "76": 1056, "77": 1071, "78": 1084, "79": 1095, "80": 1108, "81": 1122, "82": 1135, "83": 1148, "84": 1164, "85": 1175, "86": 1188, "87": 1202, "88": 1214, "89": 1227, "90": 1244, "91": 1256, "92": 1266, "93": 1279, "94": 1289, "95": 1301, "96": 1317, "97": 1329, "98": 1345, "99": 1358, "100": 1368, "101": 1384, "102": 1399, "103": 1414, "104": 1429, "105": 1448, "106": 1464, "107": 1477, "108": 1490, "109": 1505, "110": 1520, "111": 1533, "112": 1545, "113": 1564, "114": 1578, "115": 1593, "116": 1606, "117": 1618, "118": 1631, "119": 1643, "120": 1656, "121": 1674, "122": 1687, "123": 1704, "124": 1719, "125": 1734, "126": 1754, "127": 1766, "128": 1779, "129": 1792, "130": 1802, "131": 1814, "132": 1823, "133": 1835, "134": 1846, "135": 1859, "136": 1873, "137": 1886, "138": 1900, "139": 1914, "140": 1928, "141": 1939, "142": 1949, "143": 1962, "144": 1973, "145": 1984, "146": 1997, "147": 2010, "148": 2022, "149": 2034, "150": 2053, "151": 2068, "152": 2077, "153": 2089, "154": 2103, "155": 2116, "156": 2128, "157": 2145, "158": 2159, "159": 2170, "160": 2183, "161": 2201, "162": 2213, "163": 2225, "164": 2238, "165": 2250, "166": 2261, "167": 2274, "168": 2284, "169": 2296, "170": 2307, "171": 2323, "172": 2338, "173": 2348, "174": 2358, "175": 2374, "176": 2386, "177": 2398, "178": 2409, "179": 2424, "180": 2437, "181": 2453, "182": 2468, "183": 2480, "184": 2492, "185": 2506}
---

**Dave Jones:** Hi, this is the Unity UTG 9540T arbitrary function waveform generator. And well, it's a pretty cool bit of kit. But the interesting bit about this is that it's over $5,000 for this bad boy. And it's from Unity, a company famous for making, you

**Dave Jones:** know, lowcost test gear. So, why does this thing cost $5,000 or more than that? Well, that's an interesting question. So rather than a normal tear down of this thing, which I guess it'd be interesting in its own right, I thought we'd actually tear it

**Dave Jones:** down and actually have a look and go through at a crude level the bomb cost for this thing and find out why a product like this actually how it can cost $5,000. Might be interesting. Now, I've done an interesting whiteboard video on

**Dave Jones:** the economics of selling hardware, and I'll link that in if you haven't seen it. It's very interesting, but basically, it comes down to that to economically sell hardware and make a profit, um, you've pretty much got to at

**Dave Jones:** least have a sort of like 2.4 2.5 times the bomb cost multiple. Um, but for a test equipment company like this, and specifically for a product like this, that's a higherend product, why does it cost $5,000? The key to why it costs so

**Dave Jones:** much is because this is a 500 megahertz bandwidth, 2 gig samples, 2 and 1/2 gig samples per second. In fact, there's another model of this one, which goes to uh 600 megahertz. And uh pretty much the only other uh function generator on the

**Dave Jones:** market that can go to that sort of uh frequency is a Siglet model. And it costs basically a similar price. I think it's slightly cheaper because it's a smaller use and it doesn't have like a huge big touchcreen like this thing

**Dave Jones:** does, but you know, so taking that into account, they're basically the same price unit. There's basically nothing else available from any of the mainstream manufacturers. There are a few other niche like really high frequency function generators on the

**Dave Jones:** market, but if you have to ask the price of those, trust me, you can't afford it. So this looks absolutely dirt cheap in comparison. So at a basic level, if you take that like 2.5 times multiplier minimum of uh bomb cost to a salailable

**Dave Jones:** uh product, and it's going to be higher than that for a product like this, but let's just take that at at a $5,000 uh price, even though it's a bit more than that, you're still looking at $2,000 in

**Dave Jones:** bomb cost. Is there 2,000 bucks worth of parts inside this thing? Well, probably not. But is there $1,000 worth? Is it 500 bucks? How much margin are they potentially making on this? We can't get an exact answer, but let's do a tear

**Dave Jones:** down and see if we can have a look and add some things up and, you know, make a few basic assumptions and see if we can come up with a bomb cost for something like this and why it's so expensive. Oh,

**Dave Jones:** yes, please. Beautiful. And we got pretty basic folded metal construction here with uh your BNC screwed into the back terminal. So, just a couple of ribbony cables. Let me get those out. Got a little coax jobby. And we're in. And here's our main board.

**Dave Jones:** I will take high-res photos of this. All my high-res and tearown photos are available on the EE blog flicker account, uh, which is linked in on evblog.com. So, check that out. And, uh, yeah, we've got one major part here. Um,

**Dave Jones:** is that a big Xylink zinc or something like that? I assume it's a ARM processor for doing all the gooey and OS stuff. Um, surrounded maybe by some FPGA fabric. These here could be your DAX even though it's a four channel unit.

**Dave Jones:** We've got three parts. Although this thing, you don't get the full bandwidth on all four channels. It's only available on two channels. So maybe the three and channels three and four. We should be able to get the heat sink off

**Dave Jones:** those to check it out. We've got some nice cans here. And then we got some uh nice relays here. I'm liking the look of this. Um, so yeah, it's very neat construction. The uh DC to DC converter up here is, look at this multi-stage

**Dave Jones:** filter in here. It's a Bobby Dazzler. You don't usually see something like that. It's remarkable. Oh, no. I could be wrong. That could be the application processor down there cuz it it it's not doing a lot. It's just, you know, doing

**Dave Jones:** some basic gooey level uh stuff and then the rest of it's handled by um, you know, I presume that's a big FPGA under there. But anyway, we'll take a look at the uh, parts. And it looks like the

**Dave Jones:** entire OS is stored on an SD card there. That's just very nice from a developmental uh point of view. It just makes development really easy and and field firmware like updating really easy. So yeah, that's a smart move. Um

**Dave Jones:** oo what does that barcode do? So on the back here we've got a nicely shielded uh PSU. Um as usual, they probably Unity probably wouldn't have designed that. You'd subcontract that out uh to a manufacturer. Looks like uh probably

**Dave Jones:** only the two voltages, you know, it's probably only like 12 volts coming out of there. Just got a basic fan over here. No uh compliant mounting or anything like that. So really basic cost uh stuff in terms of uh the power supply

**Dave Jones:** here and nothing on the backboard uh really. That's there's just that little one micro coax going over to there for higher frequency stuff and the rest of it just going over the ribbon cable. So um yeah, bare bottom pricing, the

**Dave Jones:** earthing's um adequate and everything. So, you know, it's all neat and tidy, but uh no, they haven't gilded the lily anywhere in here. So, at a first pass, you're looking at the majority of the bomb cost uh like being the

**Dave Jones:** semiconductors on this board. Once again, this is 500 MHz stuff, 2.5 gig samples per second. You're going to be paying a premium, a very sweet premium for the uh DAXs on here and uh the uh like the output amplifiers and and stuff

**Dave Jones:** like that. They're all going to be premium stuff. you're not going to get something from the Shenzen market. All right, let's take a look at the board and the bomb cost here. This will be greatly simplified, so please excuse the

**Dave Jones:** crudity of the model. Didn't have time to build it to scale or to paint it. So, before we get into the main board, let's just have a look. You've seen the outside metal work as well. We've got the plastic uh front panel molding as

**Dave Jones:** well. We've got the front panel keypad membrane PCB. We've got the membrane overlay. We've got the LCD screen. We've got all that sort of stuff. and the uh back and front um housings which go into this thing. So, it's quite a large bill

**Dave Jones:** of materials for this thing. Let's uh just just take a look here. We've got our power supply. Of course, this is a 100 watt jobby. It's got 100 VA on the back. So, you know, we'll just take that

**Dave Jones:** as a ballpark. Very simplistic uh design here. There's active. If you're wondering where all the active electronics are, they're on the bottom. Sorry. And didn't bother to uh take that out. But very um simple, sparse, large board. Um, but of course if there's one

**Dave Jones:** thing that China do cheap, it's power supply modules. And so yeah, this is like I don't know who manufactured uh this, but it doesn't matter. And we've got a rear panel PCB up here, which is basically just a bunch of uh BNC

**Dave Jones:** connectors and Ethernet over here and just a ribbon cable going over. Got a mains input here. We've got a just a generic fan. There's nothing special about that. It's not super whisbang, you know, low noise jobby or anything like

**Dave Jones:** that. So nothing special. Just got a simple C cable harness coming out of here. And you can tell this power supply is on the cheaper side because well the caps here we got JW Co. They're a big Chinese manufacturer, but they're

**Dave Jones:** nothing of note. They're nothing like it's like you may not have even ever heard of them before. So yeah, they're complete nothing burger. They're not Japanese um caps or anything like that. So the power supply is neat and tiny.

**Dave Jones:** It's got all the requisite protections and everything else. There's your output uh filter in there. Um, incidentally, we got uh 17 1/2 volt power. I thought this would just be a fixed 12 volts. Not plus minus 17 volt power. It's got a power

**Dave Jones:** kill there. It's got minus 8 1/2 volts and plus 6V power. So, obviously that's running all of the digital uh stuff. So, they'd be dropping that down. There's be some five mix of 5V parts on there. 3.3 and then the FPGA will drop that down

**Dave Jones:** even further to your 1vt 1.2 volt rails and stuff like that. Um, but that'll be on the main board. Plus minus 17 volts of course for the analog uh sections and uh plus six volts is just standby for

**Dave Jones:** the processor because it's a soft power button jobby. Um and yeah, nothing fancy. So yeah, I've got a price for that which I'll um show you later. Now let's go over to the main board over here and I've removed the metal

**Dave Jones:** shielding around here and uh there's our um FPGA which we take a look at. It's a Kintex 7 here. Uh main processor over here. We've got our uh waveform memory. We've got our DAX here and here. I only

**Dave Jones:** took off these two uh heat sinks because um these two these will be identical parts and you can guarantee that. And this one over here um is a different DAC part again. So you can see we've got one

**Dave Jones:** channel here. Okay, like this which has got one of the uh big um 14 16 bit uh DAXs, the 2.5 gig sample per second. We've got a 50 ohm output impedance. Then we've got our switching relays for uh different uh levels and and stuff. So

**Dave Jones:** um and then it that is duplicated identically again here like this. So it's laid out a little bit uh differently but trust me if you go look into the details all this circuitry here is exactly the same as this up here. So

**Dave Jones:** those two channels uh channel one and channel two are identical as you'd expect. And then over here we've got channel three which is shielded channel four which is not shielded. Once again absolutely identical. Uh, if you want to

**Dave Jones:** look at the high-res photos, you go over to my Flickr account. This is not a tear down analysis really. It's more of a bomb analysis. And you can see that these both of these come from this deck over here. And you can see that there

**Dave Jones:** like that. Whereas this one has these two have their own dedicated DAC 2.5 gig samples per second. Channels three and four because they have uh lower bandwidth and uh lower sampling specifications. They're they're sharing a DAC down here. And as you'll see,

**Dave Jones:** curiously, they're a different manufacturer. And these are not what I expected. Just as a little aside, you might be asking, why is there only shielding on two of the channels, channel two and channel 3? What's so special about them? Why don't channel

**Dave Jones:** one and channel 3 get shielding? Well, in this particular case, it's a nice cost cutting measure because UN the designers decided that well, we're not because this is all low impedance stuff, right? DAXs are really low impedance outputs got, you know, like 50 ohm

**Dave Jones:** drive, right? Really low impedance driving out of here. So when you uh talking about something with a low impedance source then it's really difficult to have external interference like external you know EMI um coming in and disturbing that circuit because it's

**Dave Jones:** very low impedance and whereas all the stuff coming in is very high impedance so it doesn't really disturb it. So you don't really need any shielding on a low impedance circuit like this as far as external uh you know influence comes in.

**Dave Jones:** you might need it for if you don't want it to radiate um stuff, but that's a different aspect to actually being shielded to protect it from any outside um interference. So, but why is channel 2 special? It's because because this is

**Dave Jones:** low impedance and high voltage swing, huh? When you've got another channel which is right next to this channel is switching could be a big square wave boom, you know, plus minus bloody 12 volts or something, right? then that can

**Dave Jones:** easily couple into the channel next to it. Right? So you want to shield one channel. So this is not from any external thing from the ex any external noise from the instrument. It's designed to stop coupling between channels like

**Dave Jones:** this. It goes in both ways like that. And of course likewise channel three is right next to channel two. So you want to shield that one. But channel four over here. Well, you want to shield it from channel three and maybe channel

**Dave Jones:** two, but you don't need to shield it from channel one, which is quite a significant distance physical distance away here. So, that's why they can save some cost on the shielding there. So, they definitely have thought about cost

**Dave Jones:** in this from right from at the bare PCB design uh level like because I don't see any extra like holes in here for the metal work, right? There's there's just nothing. It was it was designed look they actually left the copper off there

**Dave Jones:** right for these shieldings. You can see the copper being left off. So they actually knew from the get-go that this was just about coupling between channels. So it's not like they uh you know built this and then tested it and

**Dave Jones:** go, "Oh, we can leave off this shielding." They knew that from the get-go when they designed the PCB. So definite cost cutting there. And I'll just show you a quick uh closeup of one of those um output sections here so you

**Dave Jones:** can have a squeeze. I've actually got these uh parts on my spreadsheet. I'll show you later. Japanese relays, Bobby Dazzler. Right. So, they haven't skimped there. They got good Japanese relays. But apart from that, um yeah, there's not actually a huge cost in this um

**Dave Jones:** output uh stage here. And there's just a closeup of the other um output stage with the uh DAC over here. So yeah, neat layout and I just love all this multi-stage filter in here. Oh, this is just pornographic. It really is. So they

**Dave Jones:** really want to filter out those. They would be the analog relays. We've got an LM337 over here. We've got another jobby there. I don't know if I can't remember if I included that in the spreadsheet, but yeah, these are just, you know,

**Dave Jones:** really Joe Blogs are regulators, but they really wanted to filter the absolute crap. They've left out a couple of inductors there, but they decided, oh, keep the caps in. And there's a couple of extra um stuff filter in here,

**Dave Jones:** missing here. I'm not sure why, but anyway. Um yeah, they've gone to a lot of trouble to um filter those um analog rails. And up here, they've got I love the little modular block, little pro PCB tip. Yeah. Um add little block sections

**Dave Jones:** like that. But extra pro tip, label them, please. like they haven't really labeled this like what is the function obviously that's a that's an oscillator with a uh you know a PLL um hooked on there or something and this is a I

**Dave Jones:** believe this is a comparator cuz this goes off to the rear panel it's got like a frequency counter um stuff built in so it's got all that functionality um so yeah they just broken that but you know not a huge cost in uh this sort of stuff

**Dave Jones:** now if you know anything about semiconductors and pricing you'll know that the two biggies in this thing the two cod costliest parts are going to be your gigantic big ass FPGA here. It's a Xylen Kintex 7. That's one of their big

**Dave Jones:** daddies. And also the uh 2.5 gig sample per second uh DAX in this thing because these are what 14 16 bit uh jobbies, right? Huge. Um this here, by the way, that's just a uh that's the clock uh gen

**Dave Jones:** there. I've included this in the uh spreadsheet. And also there's the main reference oscillator over there. And that's actually a temperature uh compensated um oscillator as a digitally temperature uh compensated oscillator there. So yeah, there's going to be a

**Dave Jones:** huge cost. So ZX Kintex 7 and XC 7K 160T for those playing along at home with the extra part numbers because you can double or triple the price based on what that extra stuff on the end is. So

**Dave Jones:** obviously what we got is a really big fast Kint 7 FPGA. I thought this might have been a xylink zinc or something like that which contains the processor but that's not the case. This um AM 3354 it's upside down so all the electrons

**Dave Jones:** are going to fall out. That is the main processor. That's a TI jobby over here. So they've gone for a TI jobby. So on one hand you've already seen how they tried to like shave cost on um like the

**Dave Jones:** shielding on uh some of the output uh circuitry but then they don't try and save cost. They use a TI part and as you'll see it's reasonably expensive a TI processor over here instead of one of the Asian sourced ones which um should

**Dave Jones:** be you know much cheaper but anyway yeah that's separate and then we got very fast DDR3 um SRAMM here another DDR3 SRAMM but that's coupled into the processor so these are obviously our waveform memory and of course because

**Dave Jones:** this is an arbitrary waveform generator um yeah this has to be really really super quick it has to keep up with the two and a half gig sample per second um DAX over here. So that's why they need a

**Dave Jones:** big grunty fast and massive FPGA over here coupled to some fast DDR memory over here. Um and everything runs on the SD card over here, which is uh pretty groovy. I like that. Um not exactly if you're shaving every cent off your

**Dave Jones:** design, you probably don't want to do that, but from just a design flexibility point of view, yeah, that's a winner. And interestingly, I couldn't get any info on this jobby here. um and OT8618. I assume it's maybe some sort of

**Dave Jones:** flash which is coupled into the processor over here. But yeah, so what I've done is a bomb cost spreadsheet here. Again, didn't have time to build it to scale or to paint it. Very rough analysis of what it's going to cost. And

**Dave Jones:** I'm pricing everything based on 1,000 uh quantity here because that's a nice you can get uh that number from uh the component distributors and stuff like that. And really they're not making tens of thousands of these things. You go to

**Dave Jones:** the Unity direct because UN will sell you this direct from their own website and they've got stock of like 50 of them. Like 50 units. This is not, you know, it's like it's almost $6,000 unit. They're not going to be selling tens of

**Dave Jones:** thousands of these things. They're going to be selling like maybe thousands tops. I don't know. If you think I'm wrong, put in the comments down below. Could be more than that. They could sell tens of thousands, but I doubt it. Right there.

**Dave Jones:** This is a high margin um low quant low quantity product. It's not like manufacturing a three $400 scope that they're going to sell in massive uh volume. It's a more niche item. So thousand quantity I think is really

**Dave Jones:** quite decent. So I've put in some various major parts here. Obviously I'm not going to put in absolutely everything. So this is the uh processor here. Um that's that TI jobby. It's a 1 gig ARM uh Satara uh microcontroller

**Dave Jones:** from TI. And all this pricing is in US dollars, by the way. Yankee Freedom Bucks. Um, so that's actually $11 for that processor, which, you know, it's pretty pricey. And then they've got that part there, which I said I couldn't

**Dave Jones:** identify, which I think might be a program flash or whatever. I just put in, I don't know, two bucks or whatever. Then here is, of course, the major cost. And we have to guess at this. So that Kintex um 7 FPGA I've put in a price of

**Dave Jones:** 260 bucks because if you go and uh look this up I've gone it's basically double that for a oneoff price. Now of course you get like you can't get volume pricing on these things unless you specifically go and do a deal with the

**Dave Jones:** manufacturer or via one of their distributors who will deal um for you. And if you're a good customer, if you're in their good books, you know, you might get substantial discounts. And for most of these pricings, I'm going to use

**Dave Jones:** LCSC, which is basically um China's equivalent to Digi Key, Mouser, Farnels, that kind of thing. Um, element 14. So, it's there like catalog distributor, but you can get a lot of Asian sourced components there. So, when you're doing

**Dave Jones:** bomb cost and analysis like this, it's probably better to use this than Digi Key Mouser because this is kind of like you can get like a cheaper Asian uh pricing often. But of course, there is no second source for these FPGAs. And if

**Dave Jones:** you have a look at like Digi Key price in here, once again, I'm not sure I've got the exact part here because all those letters and numbers at the end of it like means something. So, you know, like 750 Yankee bucks oneoff price and

**Dave Jones:** everything. But, of course, you're not going to be paying that in volume and it depends on the uh the customer relationship you have with the manufacturer or your dealer, you know, official uh XYlinks dealer and everything else. But anyway, I've gone

**Dave Jones:** for like 260 bucks, which is roughly half of the oneoff estimate. Now, it could be cheaper than this um based on the exact part number, but it's hard to actually search for the exact the exact absolute one based on that. So, there

**Dave Jones:** could be subtleties in there and it could change the price quite a lot. But anyway, I've gone for 260 bucks. It's it's an expensive part, but even if I have got that wrong and you even take a hundred bucks off that, then uh we can

**Dave Jones:** see that at the you know, just take a 100 bucks off the final uh pricing that we look at. But yeah, anyway, it it's hard to get a price on that, but it's the most expensive component on the

**Dave Jones:** board. And then throw in a couple of uh DDR3s RAMs here, you know, couple of bucks, it all adds up. You got a flat link LCD driver there. Then you've got a couple of high-speed uh Peekle uh comparators in here. They were in that

**Dave Jones:** big block that I saw with all the multiple blocks in there. I think they were in there. Um, you know, and they're two bucks 50, you know, it's not cheap. Um, then we've got a FI here. That's for

**Dave Jones:** the um Ethernet FI um thing. And then we've got a uh I found a low noise op amp there. I don't know. I just put Y. Um and then I found another relay. There's 25 cents. All adds up. And then

**Dave Jones:** uh that that 10 MHz temperature uh controlled C temperature compensated uh crystal oscillator digitally temperature compensated crystal oscillator. It's five bucks uh for example. And then I've just added on some miscellaneous chips at 10 bucks and the SD card socket and

**Dave Jones:** ribbon cables and connectors and fans and heat sinks and stuff like that. Right. But we haven't even looked at the output driver yet, which is where the second most expensive uh part will come in. And that's the 2.5 gig sample per

**Dave Jones:** second 14bit DAC. And this one's interesting because it's not a manufacturer that I've heard of. The part number is CBM 97D39. And this is an Asian manufacturer I'd never heard of. And there's two of those, of course. Um, channel one and

**Dave Jones:** channel 2, and they're 40 bucks US a pop. And you can actually get that on LCSC. Check it out. They do actually have it here. Digital to analog converters. Oh yeah, there it is. There. and they've got 30 off uh pricing. So, I

**Dave Jones:** just actually lowered that. Um you know, when you're buying a,000 of these things um or in this particular case, 2,000. I just assume that maybe you might be able to get it for 40 bucks. I don't know. I

**Dave Jones:** might be under charging there. But, uh yeah, they actually sell this digital to analog converter. And we can take a look at the data sheet. It's from a company called Corbay Micro Electronics. And well, I like who had any clue? So, I

**Dave Jones:** just assumed that the core.com I just assumed that this would have been a TI or analog devices jobby or whatever. You know, one of the biggies I assume, but no. Um, it's it's it's not. It's from this company that specializes in look

**Dave Jones:** high-speed opairs. They do a whole bunch of stuff. They do analog and stuff like that, but they do uh DAX, high-speed DAC converters, quadroulure ones, precision D2As, DDS's and stuff like that. So, Corbay, there you go. I love doing these

**Dave Jones:** tear downs. You learn something new every day. And we can download the data sheet for this jobby. And here it is. 14 bit 2.5 gig sample per second and DAC 14 bits direct RF synthesis blah blah blah DC to 1.25 gig in bassband uh to 3 gig

**Dave Jones:** in mix mode. Um LVDS interface. It's got DDR clocking and programmable output uh currents and broadband communications. military radar activation sim tests the system equipment instruments and automated test and yeah who knew I was very surprised to find this Asian source

**Dave Jones:** DAC in here unbelievable and channels three and four they have saved a bit of cost here by not having those high sample rate uh DAXs there so this is an analog devices jobby it's an AD 9122 but it's still 10 bucks but at least you

**Dave Jones:** share you know one of those between channel 3 and channel And as you can see, we can get that from um LCSC. 100 of quantity, nine bucks. And once again, it it quite it depends on like the grade

**Dave Jones:** you get or whatever. Um here. So yeah, but we can download the data sheet for that. Um Oh, thanks Chinese. Anyway, you get the point. It's a um 1.2 gig 16 bit uh DACA. So you do get the greater

**Dave Jones:** resolution on channels uh three and uh four there. Then we've got an analog devices uh clock gen here. That's 2.5 GHz. Um that's our sample clock. That's $7. So that's not cheap. Um and then we've got all those output um signal uh

**Dave Jones:** relays as well. So there's actually 20 of those. There's 20 of them. Um cuz yeah, there's a lot of those. And at 50 cents each, there's another $10, right, for those Japanese relays. Then there's actually an analog devices uh FET op amp

**Dave Jones:** in there um in each output uh channel. So, there's four of those. They're a buck 80 um each. And I said, well, why do they need such an expensive op amp? I don't know. Low offset or something. Looks like it's an 80 microvolt 20 MHz

**Dave Jones:** part here. Precision, very low noise. Yeah. So, you're going to pay, you know, a premium for that. So, they got one of those in the um output uh channel for doing all the offsetty stuff. But, you've got to have all these grunty

**Dave Jones:** drivers. Remember, you can't just drive from the deck directly uh to your 50 ohm output. So, you need these 900 MHz current feedback amps. And there's 12 of these. These are ths 3491s. There's 12 of those at $7 a pop. $7 a pop. That's

**Dave Jones:** That's actually technically more cost than the DAX. So, they spent more on the output drivers, potentially more on the output drivers than they have on the DAX. Unbelievable. And check it out. Visa LCSC pricing at a,000 of quantity

**Dave Jones:** here. like seven bucks. Sure, they'd be ordering like tens of thousands uh because you need a whole bunch of these um to make a thousand uh units all up. And you can see how this can go anywhere from seven bucks up to

**Dave Jones:** $18, right? 18 bucks for exactly the same part, but it's just got those different letters on the end because it's a different grade. So, like you can you can have a look at the uh data sheet. They often don't give you the

**Dave Jones:** English one. Sorry, I won't go bother looking for the English one. But um yeah, all these different grade uh parts. Yeah, but you can often get parts like this specified in various uh speed and offset grades and all sorts of

**Dave Jones:** things. And you can pay a premium depending on which actual um part that you're actually uh getting. But it could also be like a package thing. If it's in some rare package that you decide to design into your board, then well, you

**Dave Jones:** know, you could pay like double for it or something like that um for some weird ass package. So beware. So I'm not going to look into the details, but like yeah, it's the same part number just with different letteries on the end. So, and

**Dave Jones:** they both got I. So that indicates industrial uh temperature range instead of C. Commercial. That's common that you'll see. You'll see a C in the part number or like after the part number or an I. Um that's just a different uh

**Dave Jones:** temperature uh range thing obviously, but they're expensive parts. More expensive than the DAC. Who would have thought? So these are actually these parts here, right? One, two, three, four, right? There's four per channel. So like this adds up. And they even use

**Dave Jones:** them on the on the lower frequency channels, three and four over here. So maybe they are getting them um cheaper than that. But you know, an LCSC is a pretty cheap supplier, but they might be, you know, cuz they're probably

**Dave Jones:** ordering like tens of thousands of these. So, um, yeah, they I'm probably getting them directly from the manufacturer, but yeah, there's there's four of those per channel. Pricey little buggers. And then another pricey part is an LMHR65652 here. Need four of those. So,

**Dave Jones:** there's one of those uh per channel and they're like seven bucks a pop as well. Um, so yeah, 28 uh total. Damn, that adds up. So, there you go. 100 off quantity, $760 there. And we can it's a

**Dave Jones:** single uh 1.5 gig fully uh differential amplifier here. So it's basically a very high-speed um single-ended to differential driver. So you got to have one of those unfortunately. So, if we actually sum up um just that output um

**Dave Jones:** stage there, you can see that there's 200 sorry, $237. $237 bucks just in just the output stage with the DAX and the drivers and whatnot. Unbelievable. Then we've got various uh power supply stuff that's on uh the main board that you could go to

**Dave Jones:** town with this. Um, so yeah, I won't go through details, but like they've got linear technology parts in there. So they haven't tried to skimp even though they're like two bucks. I put big big letter difference in cuz I found a big

**Dave Jones:** price differentiation in that part. You can go look it up for yourself or stuff like that. Couple of bucks for passage. Anyway, it like yeah, doesn't matter. I didn't want to spend any more time on that. But let's get down into uh some uh

**Dave Jones:** more stuff here. We've got the mains uh power supply unit. So that um 100 watt brick uh power supply I put in a nominal 10 Yankee bucks here um I don't know whatever you probably you might get it a

**Dave Jones:** bit under that you might get a bit over depending but you know I've just put in around 10. I've just rounded off quite a few of these numbers. Metal work here. Now I did actually put um quite a few of

**Dave Jones:** these things into uh Grock to give me a price breakdown rather than do extensive research myself. I just got a summary from Grock. So I'll put up uh some summary overlays here. But I did some uh stuff on the metal work for the amount

**Dave Jones:** of like for the sizes and everything and the you know the thickness and the gauges and the fold in and all the rest of it. Um I think I got about 20 bucks um something like that for the metal

**Dave Jones:** work. I don't know. Mechanical engineers leave it down below. Is that a order of magnitude out? Nah, it's only a couple of bucks Dave or no. That's a bit cheap Dave. You know all that metal work costs money. Didn't you know? Um and then

**Dave Jones:** we've got that output PCB with the uh with the actual connectors and the ribbon cable going over. It's just B and C cables. There's no circuitry on that. So, he's put five bucks. Um, and then you got the front panel plastics. I

**Dave Jones:** forgot the rear panel plastics. Um, so it could actually be double that. So, I might actually put in two there. Um, there you go. So, uh, yeah, you got the front panel uh, plastic moldings and the rear panel. Of course, you'll have um,

**Dave Jones:** NRE uh, tooling on that. I haven't actually put any NRE tooling for that, but I think that's included in the Grock uh, pricing. So, I got some Grock uh pricing for like an equivalent size uh kind of thing here. Um so, yeah. Yeah,

**Dave Jones:** the plastics, you know, don't come cheap. The LCD, it's a 1280 by 800 touchscreen LCD doesn't come uh cheap. So, I did some Grock pricing on that and was like, "Yeah, 35 bucks. It's not, you know, maybe you can get it cheaper. Um

**Dave Jones:** something like that. Maybe, maybe not. I don't know. Leave it in the comments." Um the keypad PCB and uh the membrane overlay sheet and everything, not hugely expensive, so I whacked in five bucks. Um, and then, uh, every unit of course

**Dave Jones:** must be calibrated and, uh, tested. And so there's labor, labor cost for that. Um, I've just put in 10 bucks round figure, something like that. I don't know. Um, a PCB assembly. You know, you know, this isn't this is quite a big

**Dave Jones:** board, right? This is a large size board with lots of complex um, fine pitch um, you know, stuff on it. Big BGAs and and other things. So, it's not cheap to assemble this. And there's a ton of passive parts on here. Okay, so um I

**Dave Jones:** think I included like a nominal cost per per component build out of um China or whatever. So it's 10 bucks. I don't know. Leave it in the comments. Is it more than that? Is it less than it? It

**Dave Jones:** could easily be more than that. Like it like you're not going to get it for a couple of bucks when you get your tiny little widget assembled um in China at JLC or whoever, you know, PCB way for

**Dave Jones:** like the super cheapest chips. Um, you got to remember this isn't like a huge serious production board with thousands and thousands of parts on it. Um, so yeah, it's it's it's time consuming and uh and you've got to load up multiple uh

**Dave Jones:** machines because you can't fit all the reels on the one machine. So it's got to go through pass through multiple machines to get all the assembly and it's like yeah. Okay. So 10 bucks could actually be cheap there. um the bare

**Dave Jones:** PCB. This is at least a six layer jobby. Could be eight layers because you could got to fan out the big FPGA and um and the other stuff. I just cheat and got Grock to give me a breakdown on that

**Dave Jones:** rather than go to the manufact manufacturers and do that. Um 10 bucks, you know, so I'm just like like ballparking um these kind of costs. Now, of course, you got NRE. Um, so we have to include some NRE, which is

**Dave Jones:** nonrecurring engineering, which is the one-off costs that it can include tooling, but it also includes the design of this thing. You got to pay engineers for like a year or a couple of years to actually develop uh this thing. And um

**Dave Jones:** so once again, I've assumed that they've got like 10 employees working on this. you know, you're going to have an FPGA person, you're going to have a software per people person or two, you're going to have, you know, a PCB layout person,

**Dave Jones:** you know, you're going to have the designer of the SK is designing all the schematics. You're going to have a manufacturing engineering, right? There's, you know, I I've got at least 10 employees, right, working on this sucker for a year. Um and I actually got

**Dave Jones:** uh once again Grock to give me a base ballpark of um what a development um salary for a an engineer in China is actually worth and it's actually $50,000 a year. So multiply by 10 employees um you're looking at a total cost of f you

**Dave Jones:** know half a million bucks for the development of this thing that this doesn't include management or other company overhead at all. So, it could be, you know, it's at least 500,000 Yankee bucks to design um this thing just in terms of like labor and company

**Dave Jones:** overhead. It could be a million bucks more, could be a couple of million bucks. Leave it in the comments what your best guess is that if you've worked in the Chinese uh company, for example, and you know what the exact costs are,

**Dave Jones:** let us know. I've assumed that we're going to manufacture. I know I've done pricing for a,000 units, but I've assumed that we're going to make 5,000 uh units. That's just a, you know, a decent number uh to work from. So you've

**Dave Jones:** got to what's called amatize that M cost. That means basically spread across. Amatize means like take that oneoff cost and spread it across each individual unit. So over 5,000 units that half a million bucks works out to a

**Dave Jones:** h 100red bucks per unit because you have to pay for the development. The company's got to make their money back, right? So there's a hundred bucks, 100 Yankee bucks per unit just on NRE. And then I've got test jigs down here. You

**Dave Jones:** could easily um like spend 50 grand on some oneoff test jigs and stuff like that. So you amatize that over the 5,000 units. There's 10 bucks a unit just for you to you know that's where I come from. Come from the test engineering

**Dave Jones:** industry is nothing to spend like 50 grand on an automated production tester. I've spent like 10 times that on automated production um testing equipment and stuff like that. So, um, yeah, and that's just not hardware, but it also includes software and, you know,

**Dave Jones:** all sorts of other, uh, things as well. So, we've got a total here. Oh, look at that. Round it out pretty well. Um, $800 US for the bomb cost. So, there you go. Like, once again, leave it in the

**Dave Jones:** comments down below if you think that's double what it should be or that's half what you think it uh should be because it might be a lot more, something like that. So that adds up to, you know, there's a lots of little stuff missing

**Dave Jones:** and stuff like that, but they kind of come out in the wash. So even if I'm out on like that FPGA, I'm, you know, assuming double or triple. Like, you know, you're still, you're well over five, 600 bucks, you're into your 800,

**Dave Jones:** maybe even $1,000 base cost to actually, all things considered, to design, develop, test, and assemble each one of these units. Then on top of that, you've got like packaging as well. You got to package it uh nicely. You got to include all the

**Dave Jones:** accessories. Didn't even didn't even think about those. You know, the mains cable, any uh test cables or whatever comes with it, manuals and things like that. They all have to be included. And then um you've got to um of course have

**Dave Jones:** dealers as well. So you got to have quite a margin in there for the dealers. The dealers aren't going to be making five or 10% on this instrument, right? They're going to make make significantly more than that. I'm not sure what the

**Dave Jones:** Unity uh dealer margins are, but you know, you know, no one's going to be working for 5%. T equipment here, right? They're they're selling it for the $5,800. They're not going to be making like 5% on this thing. I'm sure they're

**Dave Jones:** going to be making, you know, quite a reasonable uh margin on these uh products. And of course, UNICE also sell it direct. I think you can buy it directly uh from their website. But the dealer, the margin for the dealers has

**Dave Jones:** got to be in there as well. And then you've got all the support costs as well because you got to have support engineers to support this thing. And then you know and then you might have failure rates in there. So you might

**Dave Jones:** have you know a scrappage percentage in there. You know they wouldn't probably wouldn't scrap entire boards at this sort of uh price level. You would if you're manufacturing say a multimeter and the bare board costs like 50 bucks

**Dave Jones:** in parts to assemble. Well, you're probably not going to be, you know, if one of those fails your uh, you know, your automated uh, testing, you're probably not going to troubleshoot or repair that. But an expensive board like

**Dave Jones:** this at like five or 800 bucks for a board, you know, well, bare boards a bit cheaper than that. But, you know, many hundreds of dollars, it might be worth, you know, half hour or an hour of somebody's time to go in there and

**Dave Jones:** figure out what the uh, issue is. Like, you wouldn't just scrap boards, but anyway, you got to factor all that sort of stuff into your uh, cost analysis of this thing. Then you got to have the margin in there for the company to make

**Dave Jones:** a profit of course obviously. So that's what that 2.5 multiplier cost multiplier is which I had in my uh analysis video which you should go and uh watch but you know bigger companies have different margins and stuff like that. So yeah, we

**Dave Jones:** don't know exactly what the only UN would know exactly what the manufacturing cost for this thing is, but you can see why, you know, if it's $800, um like you can see why it's going to cost like3 4,000 5,000 $6,000 something

**Dave Jones:** like that at the final retail price. You got to have room to of course uh you know have specials and lower um you know lower prices and stuff like that if it's not selling. So you know you're not

**Dave Jones:** going to start selling the thing at a loss. So, you can see why. Yeah. I when I before I started this, I thought, "Oh, yeah, it's got to at least cost 500 to a,000 bucks." And that's what popped

**Dave Jones:** down in my spreadsheet, it was that like $800. Don't know if that's accurate, but it's not going to be 80 bucks and it's not going to be $2,000. So, yeah, I think somewhere, thousand bucks is, you know, a decent cost for this thing. Um,

**Dave Jones:** it may even be significantly more than maybe over a,000 bucks. We don't know. But um yeah, cuz I don't make a huge lot of this. Anyway, it's longer than I thought. Hope you found that interesting and if you

**Dave Jones:** did, please give it a big thumbs up. As always, you can just start discuss down below in the comments or where everyone talks about test equipment over on the EE blog forum. Biggest test equipment uh section on the interwebs because

**Dave Jones:** everyone loves their test gear over there. But if you have a better insight, because I've been out of the production game for quite some time. If you got better, more precise insight for stuff like this or things that I uh missed. I

**Dave Jones:** didn't cover everything. Um I just slapped together something. And I think I'm in the ballpark. What do you reckon? Let me know. And don't forget to check out the evblog.store um for all of my merch because the manufacturers sell these at a uh free

**Dave Jones:** onboard cost, a fob cost to me, and I make my margin. And that's where I make a good majority of the money that keeps me in business here as the evlog.store. So check it out. And yeah, it's all

**Dave Jones:** about margins, which is why you don't see me selling like a, you know, a $20 un multimeter. Um because the margins and the smaller you get, the smaller those mar the lower cost you get, the smaller those final retail margins get.

**Dave Jones:** So, um yeah, so you don't see me selling like a cheaper lower-end um stuff because I'm just, you know, the manufacturer margins aren't there, especially in the higher volume cutthroat business. But yeah, for more expensive uh stuff like this, um yeah,

**Dave Jones:** there's got to be quite some margin there. But yeah, just because it's made in China, you can't churn out something like this for 50 bucks. It just doesn't work because those semiconductors, they cost a lot of money and all the rest of

**Dave Jones:** the rigmmoral that goes into this. Not to mention the development of such a complex bit of kit, you know, like your modern oscilloscopes and even this is just a function gen, but the amount of software and engineering development

**Dave Jones:** that goes into this is is is quite huge. So, yeah, hats off to companies who uh design the advanced products we take for granted these days, even if they are pretty expensive, at least for a function gen. But hey, this one's cheap.

**Dave Jones:** You can pay an order of magnitude more than that for a function gen. Catch you next time. [Music]
