---
video_id: 32-DhE_5wG0
title: EEVblog 1679 - Why Does a Uni-T AWG Cost $5800? - BOM Cost Analysis
url: https://www.youtube.com/watch?v=32-DhE_5wG0
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 31, "3": 53, "4": 76, "5": 93, "6": 104, "7": 119, "8": 134, "9": 155, "10": 167, "11": 179, "12": 196, "13": 210, "14": 223, "15": 233, "16": 241, "17": 255, "18": 266, "19": 274, "20": 281, "21": 295, "22": 307, "23": 319, "24": 332, "25": 342, "26": 357, "27": 364, "28": 374, "29": 385, "30": 394, "31": 402, "32": 414, "33": 424, "34": 432, "35": 442, "36": 451, "37": 462, "38": 471, "39": 480, "40": 490, "41": 509, "42": 522, "43": 537, "44": 553, "45": 562, "46": 571, "47": 583, "48": 592, "49": 606, "50": 619, "51": 628, "52": 644, "53": 669, "54": 690, "55": 707, "56": 721, "57": 733, "58": 746, "59": 762, "60": 779, "61": 786, "62": 797, "63": 810, "64": 821, "65": 835, "66": 844, "67": 855, "68": 865, "69": 888, "70": 903, "71": 919, "72": 928, "73": 950, "74": 961, "75": 971, "76": 981, "77": 1006, "78": 1022, "79": 1036, "80": 1046, "81": 1055, "82": 1069, "83": 1082, "84": 1090, "85": 1104, "86": 1114, "87": 1125, "88": 1136, "89": 1154, "90": 1167, "91": 1180, "92": 1197, "93": 1209, "94": 1225, "95": 1242, "96": 1260, "97": 1271, "98": 1280, "99": 1289, "100": 1298, "101": 1310, "102": 1321, "103": 1329, "104": 1343, "105": 1352, "106": 1362, "107": 1372, "108": 1389, "109": 1401, "110": 1414, "111": 1429, "112": 1458, "113": 1469, "114": 1481, "115": 1493, "116": 1505, "117": 1515, "118": 1526, "119": 1537, "120": 1550, "121": 1566, "122": 1578, "123": 1593, "124": 1603, "125": 1618, "126": 1635, "127": 1643, "128": 1653, "129": 1664, "130": 1677, "131": 1689, "132": 1701, "133": 1713, "134": 1726, "135": 1739, "136": 1754, "137": 1766, "138": 1776, "139": 1796, "140": 1806, "141": 1819, "142": 1827, "143": 1839, "144": 1846, "145": 1857, "146": 1871, "147": 1882, "148": 1896, "149": 1908, "150": 1920, "151": 1933, "152": 1949, "153": 1964, "154": 1973, "155": 1986, "156": 2004, "157": 2014, "158": 2025, "159": 2047, "160": 2058, "161": 2070, "162": 2077, "163": 2087, "164": 2106, "165": 2114, "166": 2127, "167": 2139, "168": 2147, "169": 2167, "170": 2176, "171": 2195, "172": 2203, "173": 2213, "174": 2223, "175": 2233, "176": 2245, "177": 2256, "178": 2267, "179": 2282, "180": 2296, "181": 2307, "182": 2320, "183": 2338, "184": 2350, "185": 2361, "186": 2371, "187": 2382, "188": 2393, "189": 2403, "190": 2412, "191": 2427, "192": 2443, "193": 2462, "194": 2473, "195": 2494, "196": 2504}
---

**Dave Jones:** Hi, this is the Unity UTG 9540T arbitrary function waveform generator. And well, it's a pretty cool bit of kit. But the interesting bit about this is that it's over $5,000 for this bad boy.

**Dave Jones:** And it's from Unity, a company famous for making, you know, lowcost test gear. So, why does this thing cost $5,000 or more than that? Well, that's an interesting question.

**Dave Jones:** So rather than a normal tear down of this thing, which I guess it'd be interesting in its own right, I thought we'd actually tear it down and actually have a look and go through at a crude level the bomb cost for this thing and find out why a product like this actually how it can cost $5,000.

**Dave Jones:** Might be interesting. Now, I've done an interesting whiteboard video on the economics of selling hardware, and I'll link that in if you haven't seen it. It's very interesting, but basically, it comes down to that to economically sell hardware and make a profit, um, you've pretty much got to at least have a sort of like 2.4 2.5 times the bomb cost multiple.

**Dave Jones:** Um, but for a test equipment company like this, and specifically for a product like this, that's a higherend product, why does it cost $5,000? The key to why it costs so much is because this is a 500 megahertz bandwidth, 2 gig samples, 2 and 1/2 gig samples per second.

**Dave Jones:** In fact, there's another model of this one, which goes to uh 600 megahertz. And uh pretty much the only other uh function generator on the market that can go to that sort of uh frequency is a Siglet model.

**Dave Jones:** And it costs basically a similar price. I think it's slightly cheaper because it's a smaller use and it doesn't have like a huge big touchcreen like this thing does, but you know, so taking that into account, they're basically the same price unit.

**Dave Jones:** There's basically nothing else available from any of the mainstream manufacturers. There are a few other niche like really high frequency function generators on the market, but if you have to ask the price of those, trust me, you can't afford it.

**Dave Jones:** So this looks absolutely dirt cheap in comparison. So at a basic level, if you take that like 2.5 times multiplier minimum of uh bomb cost to a salailable uh product, and it's going to be higher than that for a product like this, but let's just take that at at a $5,000 uh price, even though it's a bit more than that, you're still looking at $2,000 in bomb cost.

**Dave Jones:** Is there 2,000 bucks worth of parts inside this thing? Well, probably not. But is there $1,000 worth? Is it 500 bucks? How much margin are they potentially making on this?

**Dave Jones:** We can't get an exact answer, but let's do a tear down and see if we can have a look and add some things up and, you know, make a few basic assumptions and see if we can come up with a bomb cost for something like this and why it's so expensive.

**Dave Jones:** Oh, yes, please. Beautiful. And we got pretty basic folded metal construction here with uh your BNC screwed into the back terminal. So, just a couple of ribbony cables. Let me get those out.

**Dave Jones:** Got a little coax jobby. And we're in. And here's our main board. I will take high-res photos of this. All my high-res and tearown photos are available on the EE blog flicker account, uh, which is linked in on evblog.com.

**Dave Jones:** So, check that out. And, uh, yeah, we've got one major part here. Um, is that a big Xylink zinc or something like that? I assume it's a ARM processor for doing all the gooey and OS stuff.

**Dave Jones:** Um, surrounded maybe by some FPGA fabric. These here could be your DAX even though it's a four channel unit. We've got three parts. Although this thing, you don't get the full bandwidth on all four channels.

**Dave Jones:** It's only available on two channels. So maybe the three and channels three and four. We should be able to get the heat sink off those to check it out.

**Dave Jones:** We've got some nice cans here. And then we got some uh nice relays here. I'm liking the look of this. Um, so yeah, it's very neat construction. The uh DC to DC converter up here is, look at this multi-stage filter in here.

**Dave Jones:** It's a Bobby Dazzler. You don't usually see something like that. It's remarkable. Oh, no. I could be wrong. That could be the application processor down there cuz it it it's not doing a lot.

**Dave Jones:** It's just, you know, doing some basic gooey level uh stuff and then the rest of it's handled by um, you know, I presume that's a big FPGA under there.

**Dave Jones:** But anyway, we'll take a look at the uh, parts. And it looks like the entire OS is stored on an SD card there. That's just very nice from a developmental uh point of view.

**Dave Jones:** It just makes development really easy and and field firmware like updating really easy. So yeah, that's a smart move. Um oo what does that barcode do? So on the back here we've got a nicely shielded uh PSU.

**Dave Jones:** Um as usual, they probably Unity probably wouldn't have designed that. You'd subcontract that out uh to a manufacturer. Looks like uh probably only the two voltages, you know, it's probably only like 12 volts coming out of there.

**Dave Jones:** Just got a basic fan over here. No uh compliant mounting or anything like that. So really basic cost uh stuff in terms of uh the power supply here and nothing on the backboard uh really.

**Dave Jones:** That's there's just that little one micro coax going over to there for higher frequency stuff and the rest of it just going over the ribbon cable. So um yeah, bare bottom pricing, the earthing's um adequate and everything.

**Dave Jones:** So, you know, it's all neat and tidy, but uh no, they haven't gilded the lily anywhere in here. So, at a first pass, you're looking at the majority of the bomb cost uh like being the semiconductors on this board.

**Dave Jones:** Once again, this is 500 MHz stuff, 2.5 gig samples per second. You're going to be paying a premium, a very sweet premium for the uh DAXs on here and uh the uh like the output amplifiers and and stuff like that.

**Dave Jones:** They're all going to be premium stuff. you're not going to get something from the Shenzen market. All right, let's take a look at the board and the bomb cost here.

**Dave Jones:** This will be greatly simplified, so please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. So, before we get into the main board, let's just have a look.

**Dave Jones:** You've seen the outside metal work as well. We've got the plastic uh front panel molding as well. We've got the front panel keypad membrane PCB. We've got the membrane overlay.

**Dave Jones:** We've got the LCD screen. We've got all that sort of stuff. and the uh back and front um housings which go into this thing. So, it's quite a large bill of materials for this thing.

**Dave Jones:** Let's uh just just take a look here. We've got our power supply. Of course, this is a 100 watt jobby. It's got 100 VA on the back. So, you know, we'll just take that as a ballpark.

**Dave Jones:** Very simplistic uh design here. There's active. If you're wondering where all the active electronics are, they're on the bottom. Sorry. And didn't bother to uh take that out. But very um simple, sparse, large board.

**Dave Jones:** Um, but of course if there's one thing that China do cheap, it's power supply modules. And so yeah, this is like I don't know who manufactured uh this, but it doesn't matter.

**Dave Jones:** And we've got a rear panel PCB up here, which is basically just a bunch of uh BNC connectors and Ethernet over here and just a ribbon cable going over.

**Dave Jones:** Got a mains input here. We've got a just a generic fan. There's nothing special about that. It's not super whisbang, you know, low noise jobby or anything like that.

**Dave Jones:** So nothing special. Just got a simple C cable harness coming out of here. And you can tell this power supply is on the cheaper side because well the caps here we got JW Co.

**Dave Jones:** They're a big Chinese manufacturer, but they're nothing of note. They're nothing like it's like you may not have even ever heard of them before. So yeah, they're complete nothing burger.

**Dave Jones:** They're not Japanese um caps or anything like that. So the power supply is neat and tiny. It's got all the requisite protections and everything else. There's your output uh filter in there.

**Dave Jones:** Um, incidentally, we got uh 17 1/2 volt power. I thought this would just be a fixed 12 volts. Not plus minus 17 volt power. It's got a power kill there.

**Dave Jones:** It's got minus 8 1/2 volts and plus 6V power. So, obviously that's running all of the digital uh stuff. So, they'd be dropping that down. There's be some five mix of 5V parts on there.

**Dave Jones:** 3.3 and then the FPGA will drop that down even further to your 1vt 1.2 volt rails and stuff like that. Um, but that'll be on the main board. Plus minus 17 volts of course for the analog uh sections and uh plus six volts is just standby for the processor because it's a soft power button jobby.

**Dave Jones:** Um and yeah, nothing fancy. So yeah, I've got a price for that which I'll um show you later. Now let's go over to the main board over here and I've removed the metal shielding around here and uh there's our um FPGA which we take a look at.

**Dave Jones:** It's a Kintex 7 here. Uh main processor over here. We've got our uh waveform memory. We've got our DAX here and here. I only took off these two uh heat sinks because um these two these will be identical parts and you can guarantee that.

**Dave Jones:** And this one over here um is a different DAC part again. So you can see we've got one channel here. Okay, like this which has got one of the uh big um 14 16 bit uh DAXs, the 2.5 gig sample per second.

**Dave Jones:** We've got a 50 ohm output impedance. Then we've got our switching relays for uh different uh levels and and stuff. So um and then it that is duplicated identically again here like this.

**Dave Jones:** So it's laid out a little bit uh differently but trust me if you go look into the details all this circuitry here is exactly the same as this up here.

**Dave Jones:** So those two channels uh channel one and channel two are identical as you'd expect. And then over here we've got channel three which is shielded channel four which is not shielded.

**Dave Jones:** Once again absolutely identical. Uh, if you want to look at the high-res photos, you go over to my Flickr account. This is not a tear down analysis really. It's more of a bomb analysis.

**Dave Jones:** And you can see that these both of these come from this deck over here. And you can see that there like that. Whereas this one has these two have their own dedicated DAC 2.5 gig samples per second.

**Dave Jones:** Channels three and four because they have uh lower bandwidth and uh lower sampling specifications. They're they're sharing a DAC down here. And as you'll see, curiously, they're a different manufacturer.

**Dave Jones:** And these are not what I expected. Just as a little aside, you might be asking, why is there only shielding on two of the channels, channel two and channel 3?

**Dave Jones:** What's so special about them? Why don't channel one and channel 3 get shielding? Well, in this particular case, it's a nice cost cutting measure because UN the designers decided that well, we're not because this is all low impedance stuff, right?

**Dave Jones:** DAXs are really low impedance outputs got, you know, like 50 ohm drive, right? Really low impedance driving out of here. So when you uh talking about something with a low impedance source then it's really difficult to have external interference like external you know EMI um coming in and disturbing that circuit because it's very low impedance and whereas all the stuff coming in is very high impedance so it doesn't really disturb it.

**Dave Jones:** So you don't really need any shielding on a low impedance circuit like this as far as external uh you know influence comes in. you might need it for if you don't want it to radiate um stuff, but that's a different aspect to actually being shielded to protect it from any outside um interference.

**Dave Jones:** So, but why is channel 2 special? It's because because this is low impedance and high voltage swing, huh? When you've got another channel which is right next to this channel is switching could be a big square wave boom, you know, plus minus bloody 12 volts or something, right?

**Dave Jones:** then that can easily couple into the channel next to it. Right? So you want to shield one channel. So this is not from any external thing from the ex any external noise from the instrument.

**Dave Jones:** It's designed to stop coupling between channels like this. It goes in both ways like that. And of course likewise channel three is right next to channel two. So you want to shield that one.

**Dave Jones:** But channel four over here. Well, you want to shield it from channel three and maybe channel two, but you don't need to shield it from channel one, which is quite a significant distance physical distance away here.

**Dave Jones:** So, that's why they can save some cost on the shielding there. So, they definitely have thought about cost in this from right from at the bare PCB design uh level like because I don't see any extra like holes in here for the metal work, right?

**Dave Jones:** There's there's just nothing. It was it was designed look they actually left the copper off there right for these shieldings. You can see the copper being left off. So they actually knew from the get-go that this was just about coupling between channels.

**Dave Jones:** So it's not like they uh you know built this and then tested it and go, "Oh, we can leave off this shielding." They knew that from the get-go when they designed the PCB.

**Dave Jones:** So definite cost cutting there. And I'll just show you a quick uh closeup of one of those um output sections here so you can have a squeeze. I've actually got these uh parts on my spreadsheet.

**Dave Jones:** I'll show you later. Japanese relays, Bobby Dazzler. Right. So, they haven't skimped there. They got good Japanese relays. But apart from that, um yeah, there's not actually a huge cost in this um output uh stage here.

**Dave Jones:** And there's just a closeup of the other um output stage with the uh DAC over here. So yeah, neat layout and I just love all this multi-stage filter in here.

**Dave Jones:** Oh, this is just pornographic. It really is. So they really want to filter out those. They would be the analog relays. We've got an LM337 over here. We've got another jobby there.

**Dave Jones:** I don't know if I can't remember if I included that in the spreadsheet, but yeah, these are just, you know, really Joe Blogs are regulators, but they really wanted to filter the absolute crap.

**Dave Jones:** They've left out a couple of inductors there, but they decided, oh, keep the caps in. And there's a couple of extra um stuff filter in here, missing here. I'm not sure why, but anyway.

**Dave Jones:** Um yeah, they've gone to a lot of trouble to um filter those um analog rails. And up here, they've got I love the little modular block, little pro PCB tip.

**Dave Jones:** Yeah. Um add little block sections like that. But extra pro tip, label them, please. like they haven't really labeled this like what is the function obviously that's a that's an oscillator with a uh you know a PLL um hooked on there or something and this is a I believe this is a comparator cuz this goes off to the rear panel it's got like a frequency counter um stuff built in so

**Dave Jones:** it's got all that functionality um so yeah they just broken that but you know not a huge cost in uh this sort of stuff now if you know anything about semiconductors and pricing you'll know that the two biggies in this thing the two cod costliest parts are going to be your gigantic big ass FPGA here.

**Dave Jones:** It's a Xylen Kintex 7. That's one of their big daddies. And also the uh 2.5 gig sample per second uh DAX in this thing because these are what 14 16 bit uh jobbies, right?

**Dave Jones:** Huge. Um this here, by the way, that's just a uh that's the clock uh gen there. I've included this in the uh spreadsheet. And also there's the main reference oscillator over there.

**Dave Jones:** And that's actually a temperature uh compensated um oscillator as a digitally temperature uh compensated oscillator there. So yeah, there's going to be a huge cost. So ZX Kintex 7 and XC 7K 160T for those playing along at home with the extra part numbers because you can double or triple the price based on what that extra stuff on the end is.

**Dave Jones:** So obviously what we got is a really big fast Kint 7 FPGA. I thought this might have been a xylink zinc or something like that which contains the processor but that's not the case.

**Dave Jones:** This um AM 3354 it's upside down so all the electrons are going to fall out. That is the main processor. That's a TI jobby over here. So they've gone for a TI jobby.

**Dave Jones:** So on one hand you've already seen how they tried to like shave cost on um like the shielding on uh some of the output uh circuitry but then they don't try and save cost.

**Dave Jones:** They use a TI part and as you'll see it's reasonably expensive a TI processor over here instead of one of the Asian sourced ones which um should be you know much cheaper but anyway yeah that's separate and then we got very fast DDR3 um SRAMM here another DDR3 SRAMM but that's coupled into the processor so these are obviously our waveform memory and of course because this is an arbitrary waveform generator

**Dave Jones:** um yeah this has to be really really super quick it has to keep up with the two and a half gig sample per second um DAX over here. So that's why they need a big grunty fast and massive FPGA over here coupled to some fast DDR memory over here.

**Dave Jones:** Um and everything runs on the SD card over here, which is uh pretty groovy. I like that. Um not exactly if you're shaving every cent off your design, you probably don't want to do that, but from just a design flexibility point of view, yeah, that's a winner.

**Dave Jones:** And interestingly, I couldn't get any info on this jobby here. um and OT8618. I assume it's maybe some sort of flash which is coupled into the processor over here.

**Dave Jones:** But yeah, so what I've done is a bomb cost spreadsheet here. Again, didn't have time to build it to scale or to paint it. Very rough analysis of what it's going to cost.

**Dave Jones:** And I'm pricing everything based on 1,000 uh quantity here because that's a nice you can get uh that number from uh the component distributors and stuff like that. And really they're not making tens of thousands of these things.

**Dave Jones:** You go to the Unity direct because UN will sell you this direct from their own website and they've got stock of like 50 of them. Like 50 units. This is not, you know, it's like it's almost $6,000 unit.

**Dave Jones:** They're not going to be selling tens of thousands of these things. They're going to be selling like maybe thousands tops. I don't know. If you think I'm wrong, put in the comments down below.

**Dave Jones:** Could be more than that. They could sell tens of thousands, but I doubt it. Right there. This is a high margin um low quant low quantity product. It's not like manufacturing a three $400 scope that they're going to sell in massive uh volume.

**Dave Jones:** It's a more niche item. So thousand quantity I think is really quite decent. So I've put in some various major parts here. Obviously I'm not going to put in absolutely everything.

**Dave Jones:** So this is the uh processor here. Um that's that TI jobby. It's a 1 gig ARM uh Satara uh microcontroller from TI. And all this pricing is in US dollars, by the way.

**Dave Jones:** Yankee Freedom Bucks. Um, so that's actually $11 for that processor, which, you know, it's pretty pricey. And then they've got that part there, which I said I couldn't identify, which I think might be a program flash or whatever.

**Dave Jones:** I just put in, I don't know, two bucks or whatever. Then here is, of course, the major cost. And we have to guess at this. So that Kintex um 7 FPGA I've put in a price of 260 bucks because if you go and uh look this up I've gone it's basically double that for a oneoff price.

**Dave Jones:** Now of course you get like you can't get volume pricing on these things unless you specifically go and do a deal with the manufacturer or via one of their distributors who will deal um for you.

**Dave Jones:** And if you're a good customer, if you're in their good books, you know, you might get substantial discounts. And for most of these pricings, I'm going to use LCSC, which is basically um China's equivalent to Digi Key, Mouser, Farnels, that kind of thing.

**Dave Jones:** Um, element 14. So, it's there like catalog distributor, but you can get a lot of Asian sourced components there. So, when you're doing bomb cost and analysis like this, it's probably better to use this than Digi Key Mouser because this is kind of like you can get like a cheaper Asian uh pricing often.

**Dave Jones:** But of course, there is no second source for these FPGAs. And if you have a look at like Digi Key price in here, once again, I'm not sure I've got the exact part here because all those letters and numbers at the end of it like means something.

**Dave Jones:** So, you know, like 750 Yankee bucks oneoff price and everything. But, of course, you're not going to be paying that in volume and it depends on the uh the customer relationship you have with the manufacturer or your dealer, you know, official uh XYlinks dealer and everything else.

**Dave Jones:** But anyway, I've gone for like 260 bucks, which is roughly half of the oneoff estimate. Now, it could be cheaper than this um based on the exact part number, but it's hard to actually search for the exact the exact absolute one based on that.

**Dave Jones:** So, there could be subtleties in there and it could change the price quite a lot. But anyway, I've gone for 260 bucks. It's it's an expensive part, but even if I have got that wrong and you even take a hundred bucks off that, then uh we can see that at the you know, just take a 100 bucks off the final uh pricing that we look at.

**Dave Jones:** But yeah, anyway, it it's hard to get a price on that, but it's the most expensive component on the board. And then throw in a couple of uh DDR3s RAMs here, you know, couple of bucks, it all adds up.

**Dave Jones:** You got a flat link LCD driver there. Then you've got a couple of high-speed uh Peekle uh comparators in here. They were in that big block that I saw with all the multiple blocks in there.

**Dave Jones:** I think they were in there. Um, you know, and they're two bucks 50, you know, it's not cheap. Um, then we've got a FI here. That's for the um Ethernet FI um thing.

**Dave Jones:** And then we've got a uh I found a low noise op amp there. I don't know. I just put Y. Um and then I found another relay. There's 25 cents.

**Dave Jones:** All adds up. And then uh that that 10 MHz temperature uh controlled C temperature compensated uh crystal oscillator digitally temperature compensated crystal oscillator. It's five bucks uh for example.

**Dave Jones:** And then I've just added on some miscellaneous chips at 10 bucks and the SD card socket and ribbon cables and connectors and fans and heat sinks and stuff like that.

**Dave Jones:** Right. But we haven't even looked at the output driver yet, which is where the second most expensive uh part will come in. And that's the 2.5 gig sample per second 14bit DAC.

**Dave Jones:** And this one's interesting because it's not a manufacturer that I've heard of. The part number is CBM 97D39. And this is an Asian manufacturer I'd never heard of. And there's two of those, of course.

**Dave Jones:** Um, channel one and channel 2, and they're 40 bucks US a pop. And you can actually get that on LCSC. Check it out. They do actually have it here.

**Dave Jones:** Digital to analog converters. Oh yeah, there it is. There. and they've got 30 off uh pricing. So, I just actually lowered that. Um you know, when you're buying a,000 of these things um or in this particular case, 2,000.

**Dave Jones:** I just assume that maybe you might be able to get it for 40 bucks. I don't know. I might be under charging there. But, uh yeah, they actually sell this digital to analog converter.

**Dave Jones:** And we can take a look at the data sheet. It's from a company called Corbay Micro Electronics. And well, I like who had any clue? So, I just assumed that the core.com I just assumed that this would have been a TI or analog devices jobby or whatever.

**Dave Jones:** You know, one of the biggies I assume, but no. Um, it's it's it's not. It's from this company that specializes in look high-speed opairs. They do a whole bunch of stuff.

**Dave Jones:** They do analog and stuff like that, but they do uh DAX, high-speed DAC converters, quadroulure ones, precision D2As, DDS's and stuff like that. So, Corbay, there you go. I love doing these tear downs.

**Dave Jones:** You learn something new every day. And we can download the data sheet for this jobby. And here it is. 14 bit 2.5 gig sample per second and DAC 14 bits direct RF synthesis blah blah blah DC to 1.25 gig in bassband uh to 3 gig in mix mode.

**Dave Jones:** Um LVDS interface. It's got DDR clocking and programmable output uh currents and broadband communications. military radar activation sim tests the system equipment instruments and automated test and yeah who knew I was very surprised to find this Asian source DAC in here unbelievable and channels three and four they have saved a bit of cost here by not having those high sample rate uh DAXs there so this is an

**Dave Jones:** analog devices jobby it's an AD 9122 but it's still 10 bucks but at least you share you know one of those between channel 3 and channel And as you can see, we can get that from um LCSC.

**Dave Jones:** 100 of quantity, nine bucks. And once again, it it quite it depends on like the grade you get or whatever. Um here. So yeah, but we can download the data sheet for that.

**Dave Jones:** Um Oh, thanks Chinese. Anyway, you get the point. It's a um 1.2 gig 16 bit uh DACA. So you do get the greater resolution on channels uh three and uh four there.

**Dave Jones:** Then we've got an analog devices uh clock gen here. That's 2.5 GHz. Um that's our sample clock. That's $7. So that's not cheap. Um and then we've got all those output um signal uh relays as well.

**Dave Jones:** So there's actually 20 of those. There's 20 of them. Um cuz yeah, there's a lot of those. And at 50 cents each, there's another $10, right, for those Japanese relays.

**Dave Jones:** Then there's actually an analog devices uh FET op amp in there um in each output uh channel. So, there's four of those. They're a buck 80 um each. And I said, well, why do they need such an expensive op amp?

**Dave Jones:** I don't know. Low offset or something. Looks like it's an 80 microvolt 20 MHz part here. Precision, very low noise. Yeah. So, you're going to pay, you know, a premium for that.

**Dave Jones:** So, they got one of those in the um output uh channel for doing all the offsetty stuff. But, you've got to have all these grunty drivers. Remember, you can't just drive from the deck directly uh to your 50 ohm output.

**Dave Jones:** So, you need these 900 MHz current feedback amps. And there's 12 of these. These are ths 3491s. There's 12 of those at $7 a pop. $7 a pop. That's That's actually technically more cost than the DAX.

**Dave Jones:** So, they spent more on the output drivers, potentially more on the output drivers than they have on the DAX. Unbelievable. And check it out. Visa LCSC pricing at a,000 of quantity here.

**Dave Jones:** like seven bucks. Sure, they'd be ordering like tens of thousands uh because you need a whole bunch of these um to make a thousand uh units all up. And you can see how this can go anywhere from seven bucks up to $18, right?

**Dave Jones:** 18 bucks for exactly the same part, but it's just got those different letters on the end because it's a different grade. So, like you can you can have a look at the uh data sheet.

**Dave Jones:** They often don't give you the English one. Sorry, I won't go bother looking for the English one. But um yeah, all these different grade uh parts. Yeah, but you can often get parts like this specified in various uh speed and offset grades and all sorts of things.

**Dave Jones:** And you can pay a premium depending on which actual um part that you're actually uh getting. But it could also be like a package thing. If it's in some rare package that you decide to design into your board, then well, you know, you could pay like double for it or something like that um for some weird ass package.

**Dave Jones:** So beware. So I'm not going to look into the details, but like yeah, it's the same part number just with different letteries on the end. So, and they both got I.

**Dave Jones:** So that indicates industrial uh temperature range instead of C. Commercial. That's common that you'll see. You'll see a C in the part number or like after the part number or an I.

**Dave Jones:** Um that's just a different uh temperature uh range thing obviously, but they're expensive parts. More expensive than the DAC. Who would have thought? So these are actually these parts here, right?

**Dave Jones:** One, two, three, four, right? There's four per channel. So like this adds up. And they even use them on the on the lower frequency channels, three and four over here.

**Dave Jones:** So maybe they are getting them um cheaper than that. But you know, an LCSC is a pretty cheap supplier, but they might be, you know, cuz they're probably ordering like tens of thousands of these.

**Dave Jones:** So, um, yeah, they I'm probably getting them directly from the manufacturer, but yeah, there's there's four of those per channel. Pricey little buggers. And then another pricey part is an LMHR65652 here.

**Dave Jones:** Need four of those. So, there's one of those uh per channel and they're like seven bucks a pop as well. Um, so yeah, 28 uh total. Damn, that adds up.

**Dave Jones:** So, there you go. 100 off quantity, $760 there. And we can it's a single uh 1.5 gig fully uh differential amplifier here. So it's basically a very high-speed um single-ended to differential driver.

**Dave Jones:** So you got to have one of those unfortunately. So, if we actually sum up um just that output um stage there, you can see that there's 200 sorry, $237.

**Dave Jones:** $237 bucks just in just the output stage with the DAX and the drivers and whatnot. Unbelievable. Then we've got various uh power supply stuff that's on uh the main board that you could go to town with this.

**Dave Jones:** Um, so yeah, I won't go through details, but like they've got linear technology parts in there. So they haven't tried to skimp even though they're like two bucks. I put big big letter difference in cuz I found a big price differentiation in that part.

**Dave Jones:** You can go look it up for yourself or stuff like that. Couple of bucks for passage. Anyway, it like yeah, doesn't matter. I didn't want to spend any more time on that.

**Dave Jones:** But let's get down into uh some uh more stuff here. We've got the mains uh power supply unit. So that um 100 watt brick uh power supply I put in a nominal 10 Yankee bucks here um I don't know whatever you probably you might get it a bit under that you might get a bit over depending but you know I've just put in around 10.

**Dave Jones:** I've just rounded off quite a few of these numbers. Metal work here. Now I did actually put um quite a few of these things into uh Grock to give me a price breakdown rather than do extensive research myself.

**Dave Jones:** I just got a summary from Grock. So I'll put up uh some summary overlays here. But I did some uh stuff on the metal work for the amount of like for the sizes and everything and the you know the thickness and the gauges and the fold in and all the rest of it.

**Dave Jones:** Um I think I got about 20 bucks um something like that for the metal work. I don't know. Mechanical engineers leave it down below. Is that a order of magnitude out?

**Dave Jones:** Nah, it's only a couple of bucks Dave or no. That's a bit cheap Dave. You know all that metal work costs money. Didn't you know? Um and then we've got that output PCB with the uh with the actual connectors and the ribbon cable going over.

**Dave Jones:** It's just B and C cables. There's no circuitry on that. So, he's put five bucks. Um, and then you got the front panel plastics. I forgot the rear panel plastics.

**Dave Jones:** Um, so it could actually be double that. So, I might actually put in two there. Um, there you go. So, uh, yeah, you got the front panel uh, plastic moldings and the rear panel.

**Dave Jones:** Of course, you'll have um, NRE uh, tooling on that. I haven't actually put any NRE tooling for that, but I think that's included in the Grock uh, pricing. So, I got some Grock uh pricing for like an equivalent size uh kind of thing here.

**Dave Jones:** Um so, yeah. Yeah, the plastics, you know, don't come cheap. The LCD, it's a 1280 by 800 touchscreen LCD doesn't come uh cheap. So, I did some Grock pricing on that and was like, "Yeah, 35 bucks.

**Dave Jones:** It's not, you know, maybe you can get it cheaper. Um something like that. Maybe, maybe not. I don't know. Leave it in the comments." Um the keypad PCB and uh the membrane overlay sheet and everything, not hugely expensive, so I whacked in five bucks.

**Dave Jones:** Um, and then, uh, every unit of course must be calibrated and, uh, tested. And so there's labor, labor cost for that. Um, I've just put in 10 bucks round figure, something like that.

**Dave Jones:** I don't know. Um, a PCB assembly. You know, you know, this isn't this is quite a big board, right? This is a large size board with lots of complex um, fine pitch um, you know, stuff on it.

**Dave Jones:** Big BGAs and and other things. So, it's not cheap to assemble this. And there's a ton of passive parts on here. Okay, so um I think I included like a nominal cost per per component build out of um China or whatever.

**Dave Jones:** So it's 10 bucks. I don't know. Leave it in the comments. Is it more than that? Is it less than it? It could easily be more than that. Like it like you're not going to get it for a couple of bucks when you get your tiny little widget assembled um in China at JLC or whoever, you know, PCB way for like the super cheapest chips.

**Dave Jones:** Um, you got to remember this isn't like a huge serious production board with thousands and thousands of parts on it. Um, so yeah, it's it's it's time consuming and uh and you've got to load up multiple uh machines because you can't fit all the reels on the one machine.

**Dave Jones:** So it's got to go through pass through multiple machines to get all the assembly and it's like yeah. Okay. So 10 bucks could actually be cheap there. um the bare PCB.

**Dave Jones:** This is at least a six layer jobby. Could be eight layers because you could got to fan out the big FPGA and um and the other stuff. I just cheat and got Grock to give me a breakdown on that rather than go to the manufact manufacturers and do that.

**Dave Jones:** Um 10 bucks, you know, so I'm just like like ballparking um these kind of costs. Now, of course, you got NRE. Um, so we have to include some NRE, which is nonrecurring engineering, which is the one-off costs that it can include tooling, but it also includes the design of this thing.

**Dave Jones:** You got to pay engineers for like a year or a couple of years to actually develop uh this thing. And um so once again, I've assumed that they've got like 10 employees working on this.

**Dave Jones:** you know, you're going to have an FPGA person, you're going to have a software per people person or two, you're going to have, you know, a PCB layout person, you know, you're going to have the designer of the SK is designing all the schematics.

**Dave Jones:** You're going to have a manufacturing engineering, right? There's, you know, I I've got at least 10 employees, right, working on this sucker for a year. Um and I actually got uh once again Grock to give me a base ballpark of um what a development um salary for a an engineer in China is actually worth and it's actually $50,000 a year.

**Dave Jones:** So multiply by 10 employees um you're looking at a total cost of f you know half a million bucks for the development of this thing that this doesn't include management or other company overhead at all.

**Dave Jones:** So, it could be, you know, it's at least 500,000 Yankee bucks to design um this thing just in terms of like labor and company overhead. It could be a million bucks more, could be a couple of million bucks.

**Dave Jones:** Leave it in the comments what your best guess is that if you've worked in the Chinese uh company, for example, and you know what the exact costs are, let us know.

**Dave Jones:** I've assumed that we're going to manufacture. I know I've done pricing for a,000 units, but I've assumed that we're going to make 5,000 uh units. That's just a, you know, a decent number uh to work from.

**Dave Jones:** So you've got to what's called amatize that M cost. That means basically spread across. Amatize means like take that oneoff cost and spread it across each individual unit. So over 5,000 units that half a million bucks works out to a h 100red bucks per unit because you have to pay for the development.

**Dave Jones:** The company's got to make their money back, right? So there's a hundred bucks, 100 Yankee bucks per unit just on NRE. And then I've got test jigs down here.

**Dave Jones:** You could easily um like spend 50 grand on some oneoff test jigs and stuff like that. So you amatize that over the 5,000 units. There's 10 bucks a unit just for you to you know that's where I come from.

**Dave Jones:** Come from the test engineering industry is nothing to spend like 50 grand on an automated production tester. I've spent like 10 times that on automated production um testing equipment and stuff like that.

**Dave Jones:** So, um, yeah, and that's just not hardware, but it also includes software and, you know, all sorts of other, uh, things as well. So, we've got a total here.

**Dave Jones:** Oh, look at that. Round it out pretty well. Um, $800 US for the bomb cost. So, there you go. Like, once again, leave it in the comments down below if you think that's double what it should be or that's half what you think it uh should be because it might be a lot more, something like that.

**Dave Jones:** So that adds up to, you know, there's a lots of little stuff missing and stuff like that, but they kind of come out in the wash. So even if I'm out on like that FPGA, I'm, you know, assuming double or triple.

**Dave Jones:** Like, you know, you're still, you're well over five, 600 bucks, you're into your 800, maybe even $1,000 base cost to actually, all things considered, to design, develop, test, and assemble each one of these units.

**Dave Jones:** Then on top of that, you've got like packaging as well. You got to package it uh nicely. You got to include all the accessories. Didn't even didn't even think about those.

**Dave Jones:** You know, the mains cable, any uh test cables or whatever comes with it, manuals and things like that. They all have to be included. And then um you've got to um of course have dealers as well.

**Dave Jones:** So you got to have quite a margin in there for the dealers. The dealers aren't going to be making five or 10% on this instrument, right? They're going to make make significantly more than that.

**Dave Jones:** I'm not sure what the Unity uh dealer margins are, but you know, you know, no one's going to be working for 5%. T equipment here, right? They're they're selling it for the $5,800.

**Dave Jones:** They're not going to be making like 5% on this thing. I'm sure they're going to be making, you know, quite a reasonable uh margin on these uh products. And of course, UNICE also sell it direct.

**Dave Jones:** I think you can buy it directly uh from their website. But the dealer, the margin for the dealers has got to be in there as well. And then you've got all the support costs as well because you got to have support engineers to support this thing.

**Dave Jones:** And then you know and then you might have failure rates in there. So you might have you know a scrappage percentage in there. You know they wouldn't probably wouldn't scrap entire boards at this sort of uh price level.

**Dave Jones:** You would if you're manufacturing say a multimeter and the bare board costs like 50 bucks in parts to assemble. Well, you're probably not going to be, you know, if one of those fails your uh, you know, your automated uh, testing, you're probably not going to troubleshoot or repair that.

**Dave Jones:** But an expensive board like this at like five or 800 bucks for a board, you know, well, bare boards a bit cheaper than that. But, you know, many hundreds of dollars, it might be worth, you know, half hour or an hour of somebody's time to go in there and figure out what the uh, issue is.

**Dave Jones:** Like, you wouldn't just scrap boards, but anyway, you got to factor all that sort of stuff into your uh, cost analysis of this thing. Then you got to have the margin in there for the company to make a profit of course obviously.

**Dave Jones:** So that's what that 2.5 multiplier cost multiplier is which I had in my uh analysis video which you should go and uh watch but you know bigger companies have different margins and stuff like that.

**Dave Jones:** So yeah, we don't know exactly what the only UN would know exactly what the manufacturing cost for this thing is, but you can see why, you know, if it's $800, um like you can see why it's going to cost like3 4,000 5,000 $6,000 something like that at the final retail price.

**Dave Jones:** You got to have room to of course uh you know have specials and lower um you know lower prices and stuff like that if it's not selling. So you know you're not going to start selling the thing at a loss.

**Dave Jones:** So, you can see why. Yeah. I when I before I started this, I thought, "Oh, yeah, it's got to at least cost 500 to a,000 bucks." And that's what popped down in my spreadsheet, it was that like $800.

**Dave Jones:** Don't know if that's accurate, but it's not going to be 80 bucks and it's not going to be $2,000. So, yeah, I think somewhere, thousand bucks is, you know, a decent cost for this thing.

**Dave Jones:** Um, it may even be significantly more than maybe over a,000 bucks. We don't know. But um yeah, cuz I don't make a huge lot of this. Anyway, it's longer than I thought.

**Dave Jones:** Hope you found that interesting and if you did, please give it a big thumbs up. As always, you can just start discuss down below in the comments or where everyone talks about test equipment over on the EE blog forum.

**Dave Jones:** Biggest test equipment uh section on the interwebs because everyone loves their test gear over there. But if you have a better insight, because I've been out of the production game for quite some time.

**Dave Jones:** If you got better, more precise insight for stuff like this or things that I uh missed. I didn't cover everything. Um I just slapped together something. And I think I'm in the ballpark.

**Dave Jones:** What do you reckon? Let me know. And don't forget to check out the evblog.store um for all of my merch because the manufacturers sell these at a uh free onboard cost, a fob cost to me, and I make my margin.

**Dave Jones:** And that's where I make a good majority of the money that keeps me in business here as the evlog.store. So check it out. And yeah, it's all about margins, which is why you don't see me selling like a, you know, a $20 un multimeter.

**Dave Jones:** Um because the margins and the smaller you get, the smaller those mar the lower cost you get, the smaller those final retail margins get. So, um yeah, so you don't see me selling like a cheaper lower-end um stuff because I'm just, you know, the manufacturer margins aren't there, especially in the higher volume cutthroat business.

**Dave Jones:** But yeah, for more expensive uh stuff like this, um yeah, there's got to be quite some margin there. But yeah, just because it's made in China, you can't churn out something like this for 50 bucks.

**Dave Jones:** It just doesn't work because those semiconductors, they cost a lot of money and all the rest of the rigmmoral that goes into this. Not to mention the development of such a complex bit of kit, you know, like your modern oscilloscopes and even this is just a function gen, but the amount of software and engineering development that goes into this is is is quite huge.

**Dave Jones:** So, yeah, hats off to companies who uh design the advanced products we take for granted these days, even if they are pretty expensive, at least for a function gen.

**Dave Jones:** But hey, this one's cheap. You can pay an order of magnitude more than that for a function gen. Catch you next time. [Music]
