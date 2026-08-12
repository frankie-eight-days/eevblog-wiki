---
video_id: VXE_dh38HjU
title: EEVblog #127 - PCB Design For Manufacture Tutorial - Part 1
url: https://www.youtube.com/watch?v=VXE_dh38HjU
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 26, "3": 51, "4": 64, "5": 76, "6": 94, "7": 105, "8": 120, "9": 133, "10": 147, "11": 163, "12": 174, "13": 183, "14": 204, "15": 217, "16": 231, "17": 243, "18": 254, "19": 264, "20": 277, "21": 295, "22": 313, "23": 328, "24": 339, "25": 351, "26": 361, "27": 369, "28": 384, "29": 398, "30": 410, "31": 418, "32": 431, "33": 443, "34": 458, "35": 472, "36": 485, "37": 499, "38": 507, "39": 519, "40": 530, "41": 544, "42": 560, "43": 571, "44": 584, "45": 593, "46": 612, "47": 638, "48": 648, "49": 665, "50": 680, "51": 694, "52": 707, "53": 722, "54": 741, "55": 753, "56": 772, "57": 788, "58": 805, "59": 818, "60": 838, "61": 854, "62": 869, "63": 878, "64": 889, "65": 898, "66": 910, "67": 923, "68": 941, "69": 953, "70": 975, "71": 987, "72": 1003, "73": 1014, "74": 1030, "75": 1043, "76": 1060, "77": 1069, "78": 1081, "79": 1098, "80": 1116, "81": 1126, "82": 1139, "83": 1158, "84": 1172, "85": 1184, "86": 1200, "87": 1211, "88": 1225, "89": 1234, "90": 1258, "91": 1265, "92": 1285, "93": 1301, "94": 1323, "95": 1335, "96": 1357, "97": 1366, "98": 1374, "99": 1387, "100": 1409, "101": 1426, "102": 1436, "103": 1447, "104": 1458, "105": 1472, "106": 1489, "107": 1500, "108": 1520, "109": 1533, "110": 1558, "111": 1576, "112": 1586, "113": 1611, "114": 1631, "115": 1644, "116": 1667, "117": 1690, "118": 1703, "119": 1717, "120": 1730, "121": 1740, "122": 1748, "123": 1761, "124": 1780, "125": 1796, "126": 1807, "127": 1819, "128": 1828, "129": 1848, "130": 1866, "131": 1878, "132": 1896, "133": 1906, "134": 1917, "135": 1928, "136": 1948, "137": 1961, "138": 1971, "139": 1984, "140": 2000, "141": 2010, "142": 2026, "143": 2041, "144": 2056, "145": 2070, "146": 2081, "147": 2094, "148": 2103, "149": 2118, "150": 2143, "151": 2163, "152": 2177, "153": 2192, "154": 2200, "155": 2210, "156": 2223, "157": 2251, "158": 2263, "159": 2275, "160": 2287, "161": 2301, "162": 2326, "163": 2342, "164": 2354, "165": 2366, "166": 2377, "167": 2391, "168": 2401, "169": 2412, "170": 2423, "171": 2439, "172": 2458, "173": 2475, "174": 2487, "175": 2502, "176": 2523, "177": 2538, "178": 2553, "179": 2565, "180": 2581, "181": 2597, "182": 2613, "183": 2626, "184": 2642, "185": 2652, "186": 2663, "187": 2675, "188": 2687, "189": 2697, "190": 2707, "191": 2719, "192": 2733, "193": 2749, "194": 2758, "195": 2778, "196": 2792, "197": 2804, "198": 2819, "199": 2838, "200": 2846, "201": 2857, "202": 2877, "203": 2894, "204": 2905, "205": 2920, "206": 2942, "207": 2954, "208": 2969, "209": 2982, "210": 2994, "211": 3006, "212": 3016, "213": 3027}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi. Now, I know a lot of you out there like designing your own products, and that's fantastic.

**Dave Jones:** Now, let's say you've come up with this great new design, okay? You've got this one-off, you've built it, works great, you've debugged it, fantastic, and you want to make 50 of them, 100, 500, 1,000.

**Dave Jones:** Think big. 10,000, 100,000. What do you do? How do you take your project from a one-off through to volume production? Well, I'm glad you asked. What I'm going to do today is take you step-by-step through the processes, both thought and design processes you need to do to take a one-off project through to volume manufacture.

**Dave Jones:** Let's go. What I'm going to concentrate on today is just the board level stuff, okay? So, I'm not going to get into housings and, you know, designing the overall look and feel of the product.

**Dave Jones:** That requires a whole separate blog. So, this will just be the board level, how you can design and manufacture a high volume PCB. Now, let's start by taking a look at something like this, okay?

**Dave Jones:** It's a through-hole board, traditional through-hole, okay? Green solder mask, you know, pretty basic traditional board. Now, is this suitable for high-volume manufacture? Well, yeah, you can get it done, but it's not going to be very cost-effective.

**Dave Jones:** And for high-volume manufacture, that's what it all comes down to, manufacturing cost and complexity. Now, if you've got a through-hole board like this, it's just not going to cut it these days, okay?

**Dave Jones:** Too expensive to manufacture. Sure, you can labor still a bit cheap in China, but trust me, it's not going to be as cheap as surface mount. So, the first thing you want to look at is converting your through hole design like this into something more like this.

**Dave Jones:** With mostly in almost the goal is to go entirely surface mount because as you'll see that'll save you the most amount of cost. It'll reduce your assembly time and everything will be sweet.

**Dave Jones:** So look at converting every component in your design into surface mount. Now I know this can be almost a total redesign and that's why I've mentioned this before in the blog.

**Dave Jones:** During your entire design process, even if you're doing a one-off prototype, if you think there's even remote possibility of making this into a volume product in the future, you need to put a lot of thought into what components you choose for your board.

**Dave Jones:** But trust me, even if you do have to re- totally redesign your entire board from through hole it through to surface mount or just change half the components on there to lower the cost, whatever, as you'll see it'll be worth it.

**Dave Jones:** So go to the extra effort up front. If you're going to make more than say 50 boards or something, it's worth putting the effort in to redesign it properly.

**Dave Jones:** Now the difference between through hole and surface mount is pretty obvious. Here's a video of a um a through hole assembly line and as you can see the workers sit there, they manually install the components and well, that takes time, effort and labor and you want to avoid that if at all possible.

**Dave Jones:** Whereas here is a modern pick and place machine placing your components from reels and tubes of components onto the board automatically and this can churn out boards much much quicker with less effort.

**Dave Jones:** You set it up once and you push the button and it's all automatic and your boards magically spit out the other end. That's the ultimate goal for high volume manufacture, as little labor as possible.

**Dave Jones:** One of the first things you do is go through every component in your bill of materials in your design and you look at it. Is that component easily manufacturable by the supplier I'm going to choose to assemble my board?

**Dave Jones:** Cuz not all assembly houses are the same. They have different requirements. They have different pick and place machines with different capabilities and not all of them can do what you want.

**Dave Jones:** So basically you want to stick, if you can, stick to large common components cuz that means every assembler out there will be able to do it and do it cheaply.

**Dave Jones:** Now, that might mean, okay, 0402 size resistors and capacitors for example. There are some assembly houses out there that don't have the new machines that can handle components that small.

**Dave Jones:** So, think about 0603 instead of 0402. Think about quad flat pack packages instead of BGA or something like that. BGA is going to be a little bit more touchy, harder to inspect, yields not going to be as high, more critical pad dimensions, all that sort of stuff.

**Dave Jones:** So, stick with the common package as I say 0603 and up. 0402's okay. You know, stick with 0.5 mm pin pitch or larger on your SO type packages and your quad flat packs and stuff like that and you'll be fine.

**Dave Jones:** With high volume manufacture, you're going to have to spend a bit more money on components than you anticipate. If you're making, say, 100 boards, well, you can't just go to Digi-Key and buy 100 resistors loose on the tape like that.

**Dave Jones:** The the assemblers are going to hate you for it. Trust me, because they may not say so, okay, but they're going to charge you more because they may have to manually put these onto what's called reels, okay?

**Dave Jones:** This is what you need to buy for all of your components, uh all of your SMD components. Now, reels come in different types. This one might have 5,000 resistors, but they're very cheap.

**Dave Jones:** So, this reel might only cost you five or 10 bucks or something like that. You can get little mini reels like that, or they come in huge reels like this, okay?

**Dave Jones:** Or uh when you're talking about ICs, you might they might come in uh tubes like this, and these automatically slip into the pick and place machine, and the chips shoot out like that, okay?

**Dave Jones:** You don't just want to buy them loose in your little Digi-Key packet like that. That Otherwise, uh if you do that, they'll have to hand-solder them. The efficiency's going to drop, they're going to charge you more, they're going to take longer to assemble them.

**Dave Jones:** Pooh, it's hopeless. So, you want all your components um Now, chips need to be in either tubes, or they need to be uh on You can get chips on reels as well, or they need to be in what's called trays.

**Dave Jones:** Now, here's a photo of the trays. Trays generally aren't as good cuz a lot of uh machines can't support trays. They'll want everything on reels or tubes. So, just be careful there.

**Dave Jones:** Let's do a search on Digi-Key for a part to see if we can get it in uh reel or a partial reel or something like that. See what our options are.

**Dave Jones:** Now, let's take an example of the ZXCT1009. And let's do a search for that. And as you can see, three options here have popped up. We want the SOT-23 version, which is here, okay?

**Dave Jones:** But look, it's got three lines It's got three different rows there. It's got three options for the same part. Check out the quantity over here. 114,000 parts they've got in stock.

**Dave Jones:** So, that's fantastic, okay? But as you can see, they're all the same uh quantity um available. So, that tells you it's exactly the same part, exactly the same stock, but three different procurement options.

**Dave Jones:** Now, the second the second row here, as you can see, just here it says it's available in cut tape. Now, that's the version you will typically get um it says minimum quantity over here of one, okay?

**Dave Jones:** Now, that's the one you typically get when you buy prototypes. Okay, you only want five parts for a prototype, so you buy five, they cost you a dollar and 9 cents each, you know, and you pay five bucks and and that's it, okay?

**Dave Jones:** Nice and cheap for prototypes, but we want Let's say we want to manufacture 100 boards, okay? You wouldn't buy You wouldn't buy that cut tape uh version. You wouldn't buy that part number because it comes on the cut tape.

**Dave Jones:** It doesn't come with a reel and it doesn't come with the leader tape attached, which the manufacturer your assembly house needs to put that into the pick and place machine.

**Dave Jones:** That's That's pretty useless to your manufacturer. Now, if you look at the top row up here, as you can see, minimum quantity of 3,000. So, that's obviously at that says tape and reel, okay?

**Dave Jones:** So, that is one reel of parts, but you've got to buy five 3,000 of them minimum to get that one reel and they're 43 cents each. Let's go look at that price.

**Dave Jones:** Uh sorry, 40 cents each at 3,000, but that's 1,209 dollars. So, you'd have to spend 1,209 dollars there just to get your 100 parts needed for your 100 boards so that the assembler can assemble them.

**Dave Jones:** Now, that's just crazy, okay? So, what you want is this third option down here. Now, this isn't available for all parts. So, really this is uh you have to choose your parts that go into your design carefully if they have these options.

**Dave Jones:** If you're only going to make 100 of them or or even, you know, 500 and you want them on a reel, they offer what's called a Digi-Reel option. Now, that is the same as the cut tape.

**Dave Jones:** As you can see, you can only buy You can buy just one of them, but they will actually charge you a fee and they'll put it on a reel for you with the leader tape exactly what the manufacturer needs, but you can order any quantity you want.

**Dave Jones:** So, let's go in there and calculate that price. And let's say we only wanted to build our 100 boards. So, we go down here, we type in 100, and we go calculate.

**Dave Jones:** And instead of paying the over $1,000 we had before, our total extended price is $84 plus um plus here it says a $7 reeling fee fee will apply to each reel ordered, but that's cheaper.

**Dave Jones:** Okay, you're still only paying less than $100 for your 100 parts as opposed to over $1,000 for the 3,000 minimum. So, just be careful when you're designing your product, make sure these not only are the parts in stock, but they're available in suitable quantities either reels or tubes or or partial trays or something like that for your particular design.

**Dave Jones:** It's very important. So, you can spend a lot of time just mucking around on Digikey finding or Mouser or It's the same on Mouser and Element 14 and the others.

**Dave Jones:** They all have the same service. You can spend ages just doing this to optimize the manufacturing for your little board for your 100 or 500 boards. It's crazy. So, yes, if you're going to make 100 boards, you might have to buy 500 ICs.

**Dave Jones:** You might have to buy 5,000 resistors, something like that. That is the price you pay for going to high-volume manufacture essentially. So, if you want to get 100 boards made up front, then you need to do the costing based on your entire reels of components.

**Dave Jones:** Just assuming you're only going to make 100. If you're going to make another thousand down the track, great. You'll have most of the reels components on the reels left over, but you have to amortize that cost in to your 100 boards.

**Dave Jones:** Now, the other important thing to remember is that the pick and place machines can only support a certain number of these at any one time. So, a machine might only be able to support 20 reels or 30 reels.

**Dave Jones:** That means you can only have 20 or 30 different components on your board. If you have to do more than that, then they need a second machine either in line with it and the board goes through the first machine on a conveyor through to the second machine.

**Dave Jones:** Not many houses will have that set up. The smaller houses won't have that. So, they'll have to put your board through a second time, reset up the machine. So, if you're manufacturing 100 or 1,000 boards, they put it all through once and when they're finished, they rip off all the reels, they change them over, they have to put your boards all the way through again.

**Dave Jones:** And that costs you money. Try to avoid that. So, go through your design component by component and see if you can consolidate the number of components. Do you really need a 15k pull-up resistor?

**Dave Jones:** If you've got a 10k resistor somewhere else on your board, use a 10k for the pull-up. Consolidate those values. If you need a 20k resistor on the board, it might be better to put two 10k resistors in series in your circuit because you're already using that component 20 times elsewhere on the board.

**Dave Jones:** So, just look at consolidating your components. It's very important. Also, think about pad sizes. There's no point designing a fantastic board if you find that your manufacturer and their process cannot successfully load your component on the board.

**Dave Jones:** They short together because they the solder mask is too you haven't got sufficient solder mask between the pins of an IC, for example, and they put too much paste on, it shorts out, or a resistor tombstones because you don't have thermal reliefs on one pad.

**Dave Jones:** I mean, you've got one pad connected this pad over here of your resistor connected to a big solid ground plane which sucks all the heat away and the other one just going off to a 5 hour track, then well, that resistor can tombstone.

**Dave Jones:** Look at things like that. Sometimes manufacturers will have their own preferred pad styles, but usually if you say stick to the manufacturer's recommended footprint or you use the IPC standard footprints, you'll generally do okay, but you also have to think about the size of the pads.

**Dave Jones:** So the IPC footprints for example come in three sizes, nominal, least and most. So they'll put an N, L or an M on the end of the footprint name in your library and what that means is the it's just the amount of pad the pad size.

**Dave Jones:** L is the least amount of pad size, so the smallest. So if you've got a very high density board with all the components stuffed together, then you'll want to use the least size pad, the the smallest pad you can get.

**Dave Jones:** But then you might find oh, then you can't probe them or you can't solder rework them by hand if you have to or something like that. So you've got to think about those sort of things.

**Dave Jones:** Normally you'd stick to the nominal size footprint, but if you want something if the flying test probes to come down, which is another aspect of your design you've got to think about, testing.

**Dave Jones:** Testing and programming your board can be a big thing. Now, if you've got a microcontroller on there for example and you've got to program it, well, how do you do that?

**Dave Jones:** Okay, it was fine in your design, you might have used a socket for a DIP chip, but if you've got surface mount now, well, you can program the chip before you put it on there, before you give it to the manufacturer, but that's hard and difficult.

**Dave Jones:** It's much better to actually solder your microcontroller for example onto the board and then provide an in-circuit programming header. So you've got to make sure that is designed into the board.

**Dave Jones:** You've got to make sure it's accessible where you can program it. And if you design a little bed of nails which comes down, here's a photo of a typical bed of nails for a board, then you bring it down and you want to be able to get those pogo pins onto those test pads or onto that in-circuit programming header.

**Dave Jones:** So, you've got to think about that sort of stuff when you're designing the board up front. And we haven't even gotten to panelization in the high-volume manufacturing yet. Phew.

**Dave Jones:** One of the most useful things you can do when you're designing a high-volume product is to get a spreadsheet of all the components, your entire bill of materials into a spreadsheet, put them in the the descriptions, the footprints, the quantities, and the manufacturer's part number, and then the supplier part number, and usually an alternate supplier part number.

**Dave Jones:** So, you might put in the Digi-Key part number, the Mouser, the Element 14 part number, or something like that as your supplier. And then you'll have a might have another column uh based on um how many components are on a reel.

**Dave Jones:** For example, there's 5,000 per reel. So, if you go to the effort and and cost as well, you put the item cost, you can total them all up, see what it's going to cost you to manufacture 100 boards even though you've got to buy 5,000 resistors in all these reels.

**Dave Jones:** So, a spreadsheet is handy. Putting the effort in up front pays dividends in the long run. Trust me. Okay, so you've done all the hard work. You've got your board.

**Dave Jones:** You've gone through all the processes I just mentioned, and it's all ready to go. Well, no. Sorry, it's not. If you just try and get one individual board like this, or a hundred or a thousand of these manufactured just on its own like that, it's not very economical.

**Dave Jones:** Why? The reason it's not economical to get just one board like this, manufactured individually, is because well, it goes through the machine, the pick and place just does that one board, and it spits it out.

**Dave Jones:** And there's all sorts of handling issues with the board as well as it goes through the machine and stuff like that. So, what you want to do is what's called panelize it, and that's take your one design and step and repeat it onto a PCB panel such as this.

**Dave Jones:** Now, there are certain panel sizes which we'll go into, but basically, you just want to step and repeat it like that. So, in this case, we've got 12 boards on the one panel.

**Dave Jones:** So, they set up the machine, the board goes in, and bingo, they can assemble 12 boards at once. Well, components have to be placed one by one, but it just means it's much more efficient.

**Dave Jones:** You can just churn multiple boards through the process much quicker, and that adds up to real savings in high-volume manufacture. Now, there's a conflicting requirement with panels because your bare board PCB manufacturer, they will have standard panel sizes.

**Dave Jones:** Now, it's very tempting to fit as many of your designs as you can onto that maximum size panel that they do, but you have to be cautious doing that because you have to ask, can my PCB assembler actually physically handle a board that big?

**Dave Jones:** Their machine, their particular machines they use might have a limit on the maximum size of the board, and it might be a lot smaller than the maximum panel size the PCB manufacturer can supply.

**Dave Jones:** Now, a typical bare board PCB panel might be 18 in by 24 in or 450 by 600 mm. Now, a lot of assemblers might not be able to handle that size board.

**Dave Jones:** Now, I generally stick with like an A4 size panel because I I I find, you know, pretty much everyone can handle an A4 size, but ask your manufacturer what they can handle because you don't want to get your boards manufactured and then find, "Oops, it's 10 mm too big for the machine." Uh you're screwed.

**Dave Jones:** You got to go to a more expensive manufacturer. Watch out for it. Let's take a look at a typical panel. I've got one here. Now, uh there's many different ways to do a panel, which we'll go into, but a panel will have these basic requirements.

**Dave Jones:** It will have what's called a tooling strip top and bottom. This is this bit down here. Now, what that does is allows the uh pick and place machine to actually grab hold of it.

**Dave Jones:** It can either sit in rails like this, and it can go physically be uh automatically moved through the machine like that. Now, what the tooling strip must have um it By the way, it should be about 10 mm wide top and bottom like that.

**Dave Jones:** If it's any smaller than that, then the machine may not be able to automatically handle the board. The other thing you will have in these tooling strips are the tooling holes.

**Dave Jones:** Now, you typically have four of them like this, a minimum of four, and they're typically a 4-mm diameter hole. And they're used um to get uh little um There's little uh sprigots uh cogs in there that physically move the board along the panel.

**Dave Jones:** So, it should have tooling holes. The size isn't that critical, um but 4 mm is a bit of an industry standard tooling hole, and it must have fiducials as well.

**Dave Jones:** Fiducials uh marks as well, uh which we'll go into in more detail later. And a panel must also have a way to break the boards out. So, it must either have uh routing, which is like this one with breakout tabs, or V-groove, and we'll go into those, but they're the basic re- requirements of a panel.

**Dave Jones:** Now, even if you've got a huge design like this one, this one's almost A4 uh size, and really, as you can see, only one of them fits on a panel.

**Dave Jones:** Now, we can manufacture this is just an individual board or what's called a loose board or a fully routed board without any tooling strips, but then there's limits to how close you can components can come to the edge of the board because it needs to physically hold it.

**Dave Jones:** So, even with a board like this that's large, you would still put tooling strips top and bottom and a way to break the board out. And here's an example of a more advanced panel that has three extra features, which I'll show you.

**Dave Jones:** One of them is a bad board marker. Now, if you take a look here, as you can see, it's just on the it's in the part of the dead part of the panel, but it's a marker that the assembler can actually mark that indicating when they do an automated test that this particular board is bad out of you know, if you got 20 boards on there.

**Dave Jones:** That can be really important. So, you know, don't bother using that board. It's failed. Now, another item that's it's got is what's called an impedance test strip because this is a controlled impedance PCB.

**Dave Jones:** So, in the tooling strip here, we've added an impedance test coupon. It's called. And what that does is just allows you when the bare boards manufactured, it allows you to test that the controlled impedance is exactly what you want it to be.

**Dave Jones:** The third item this board has is what's called a test stack. Now, what this does is it brings the internal copper layers because this is an eight-layer board, I think it is.

**Dave Jones:** It brings the copper to the edge. Now, this could be tricky to try and get on camera here, but as you can see, the copper's right on the edge.

**Dave Jones:** Now, you would probably need a microscope to look at that, but what it just allows you to inspect the uh layers on that board after it's been manufactured. So, that and and they're different lengths.

**Dave Jones:** There's many different ways to do this, but that's just an example of how you can inspect the board um after it's manufactured. Now, a lot of um companies when they bare board manufacturers when they assemble your panel, they will provide you with a uh what's called a core sample, and they will actually cut off a part of one of your boards, and they'll give it to you um so you can actually

**Dave Jones:** inspect that under a microscope yourself, but this just allows you to do that just in case they don't provide you with that core sample. There's another important thing I forgot to mention, not only for the individual bare board, but um it relies it it uh has the same thing on panels as well.

**Dave Jones:** Now, when you um when you lay out your board, you should add what's called pullback to the copper. Now, as you can see, the copper doesn't go all the way to the edge, and that includes those internal layers as well.

**Dave Jones:** If you've got an eight-layer board, don't bring your copper all the way to the edge cuz it can short out and cause all sorts of problems. So, have have say 1 mm pullback or something like that.

**Dave Jones:** At least allow something so the copper doesn't go right to the edge. There's one other thing you can do with panels as well. If you've got a lot of boards like this, it's a fairly unique requirement.

**Dave Jones:** Uh everyone won't need it, but I'll just mention it. It allows you to actually see these little breakouts in the corner here. Okay, you can actually route out um you can actually route out uh tracks out of there and bring the tracks out of each panel.

**Dave Jones:** So, you might want to bring out uh test tracks out of each panel like this, and you might have a test connector on one side of your board or some interface for some sort of test jig, and you might want to test all of your boards in situ in the one panel.

**Dave Jones:** Um it's it it it's not a common requirement, but you can actually do that. Now, let's get into how you break the boards out. How do you get them out of the panel after they're assembled?

**Dave Jones:** This has got four individual boards in it, okay? Quite complex. How do you break it out? Now, there's two different uh methods to do it. One is called V-grooving, which I'll show you up close, and the other is called uh routing and uh breakouts with tab breakouts.

**Dave Jones:** Now, this is an example of a V-grooved board. As you can see, it's got these score marks, or what's called a V-groove. I'll show them up close later, but along like this, and both vertical and horizontal.

**Dave Jones:** Now, here's another uh board, which is another example of V-grooving as well, okay? Now, this works really well on completely square boards. If your board is completely square, and you don't have any components overhanging the end, which can often be a problem uh because when you get this board um after it's assembled, they have to break these out.

**Dave Jones:** Now, normally what they do is they run along with a little wheel along there, which actually top and bottom, which then does a nice clean cut on it. Um but, if you've got components overhanging the edge, for example, like you like like you have a connector or something like that overhanging the board, well, you can't actually get in there to break it off.

**Dave Jones:** So, you might have to break it off by hand. But, what a V-groove allows is allows you to easily just snap the board off, and I'll show you. Here it is.

**Dave Jones:** Boop. See? But, what you get, okay, once you do that, is you I probably can't show that on camera, but you get a pretty rough pretty rough edge. It gets hairs It get gets uh little little fiberglass hairs on it, and it's it's just not a very clean way to actually uh do a board, but you can just snap them off.

**Dave Jones:** Even if they've got component overhangs, you can sort of wiggle them a bit and they'll come apart really easily. That's V-grooving. Now, it's pretty hard to get in there and actually show you what a V-groove looks like, but what it basically involves is if your board is like this, the drill actually drills down into your board like that.

**Dave Jones:** That's the top of the board and this is the bottom of the board and it goes like that. They drill at top and bottom, okay? And it leaves just a little bit of fiberglass actually connecting in the middle like that.

**Dave Jones:** And that allows you to just snap the boards off really easily. And that's V-grooving. Now, you can actually specify the angle of the actual groove in there like that if you want to get fancy and or you know, if you're someone like Apple and you're really designing, you know, a million or a billion of these things, then all that sort of stuff might actually matter.

**Dave Jones:** But, um generally, you just say, "I want V-grooving, please." and they'll just do V-grooving. Now, I mentioned copper pull back before. Now, because a V-groove actually has a distance between it, which can be a bit variable, then you have to be very careful to actually pull back your copper so that it's not exposed when they do the V-groove.

**Dave Jones:** So, if you have continuous copper going across like this and you take it right to the edge of your board, then well, you're just going to get exposed copper when they go in and they drill it for the V-groove.

**Dave Jones:** Just be careful of that. Now, the other type of panelization is what's called routing with these tab That's a tab breakout, okay? Now, you just specify the routing path around your board.

**Dave Jones:** This is really good for odd-shaped boards, which I'll show you in a minute. But, basically, there's industry standard tooling sizes for these routes. Now, 2.4 mm is a standard routing tool width.

**Dave Jones:** So, you just specify that as an outline, and they will do it. You can actually tell them to do it, but it's better to specify yourself, so you know exactly what you're going to get.

**Dave Jones:** But, these tab breakouts, these can be a bit tricky. These can be an art in itself. Now, this is this board is hard to actually push out by hand.

**Dave Jones:** Sometimes, you can break the board, and especially when it's loaded with components, you don't do that. So, you might get in there with a pair of side cutters, for example, side cutters like that, and actually cut the board out.

**Dave Jones:** Now, you have to design these tab cutouts in such a way that it allows the board to be held in there fairly firmly, okay? Cuz you can't If you've got a very large board like this, which I'll go into, you can't just have one on the corner over here, one on here, because the damn thing will warp.

**Dave Jones:** So, you have to have You might have to have multiple tab multiple breakout tabs along the edge of your board, depending on how big it is. And you have to make them so that they When you cut them out, they don't have any burrs, as well.

**Dave Jones:** Here's an example of a very wide breakout tab that supports a very large board such as this. And it has multiple holes spread in an arc like that, which allows you to actually break it out.

**Dave Jones:** So, you put these unplated holes around there in an arc, and it breaks out, and it leaves just like a little indent in your board when you break it out.

**Dave Jones:** Here's a good example of a panel with an odd-shaped board. As you can see, we've got the tooling holes, the fiducials over here, but it's got It's routed out, okay?

**Dave Jones:** It's routed out around here. Now, and all the way around like that. Now, this is a good example, because it has a combination of V-grooving and routing. So, if you've got an you can see that the board has a weird shape on the on the bottom here and the top.

**Dave Jones:** So, you route out the weird shape ones, but it's straight on the edges. So, you do V-grooving on the edges like that. So, that allows you to snap easily snap out that board while giving you the giving you the advantages of the odd shape board with the routing.

**Dave Jones:** And this is just a fairly simple example. Actually, there's much more convoluted ways you can actually do this. And it's almost an art actually figuring out how to snap a board out of panel.

**Dave Jones:** What combination of V-grooving you use, what combination of routing as well. One very important thing to remember is how stiff is the board cuz often it will only be supported along the along the top and bottom edge here by the machine.

**Dave Jones:** And the pick and place machine comes in and it places the component down and you don't want this to happen. What? Look at this board, okay? And granted, this is a 0.8 mm board.

**Dave Jones:** It's half the size of a standard 1.6 mm board, but look at how much that board warps, okay? Fantastic. That's normal FR4. I kid you not, okay? But that's 0.4 mm.

**Dave Jones:** That can make you seasick almost, really. Okay? So, you've got to take that you've got to take the rigidity of your board into account when you're actually designing a panel.

**Dave Jones:** And here's an example of a panel that just has a V-grooving along the top and bottom edge and vertical routing like that. Once again, you could have done that as a V-groove, but in this case we wanted to get a really nice edge cuz this is what this is what routing gives you.

**Dave Jones:** Routing gives you a beautifully clean and smooth edge on your board with no burrs whatsoever. Whereas a V-grooved edge will be It'll be sharp. It'll be It won't be completely flat.

**Dave Jones:** And it It's just, you know, it's not a clean edge at all. You may even have to file it down afterwards. So, from that point of view, routing is preferred.

**Dave Jones:** But here's an example of a board that, because there's no central support in here, okay, it's routed all the way from top to bottom like that, okay, this can actually This can warp, as you can see.

**Dave Jones:** When you place the components in the middle, that board can actually warp like that. So, cuz there's no rigid support in the middle to actually cross-brace it. So, this board doesn't have components in the middle, so you didn't have to worry about it.

**Dave Jones:** They're only on the top and bottom. But if you start putting it in the middle, it can flex a lot, and that can be a problem. And here's yet another board where it's fully routed around, and it's got tab breaks like that.

**Dave Jones:** But in this case, it's got the tab break in the in the middle as well, so that helps form a rigid structure for the board. So, it's not going to warp nearly as much as that other board that didn't have any central support in it.

**Dave Jones:** Here's an example of a panel that has many different designs in it. And generally, this is okay for prototyping, but for production, it's generally frowned upon. You don't want to have to load multiple individual designs onto the one panel.

**Dave Jones:** It just confuses things. You can exceed the number of reels you've got and stuff like that. So, really, you want to stick to one design per panel. Now, that little thing there on the panel is what's called a fiducial mark.

**Dave Jones:** Now, these are very important to not only put on your panel, but on your actual board as well. Now, as you can see, this board will actually have actually four fiducials on the panel itself.

**Dave Jones:** Now, typically, you only need two. you put them in opposite corners of the panel. Now, the reason these are important is because when the board's manufactured, its dimensional tolerance, i.e.

**Dave Jones:** from a reference point over here to over here, it may be slightly out. Now, that's not a problem. When they assemble a board, uh they take a reference point, which will be this fiducial mark down here.

**Dave Jones:** What it does is a camera comes over and it looks at it looks at that fiducial mark. Now, a fiducial mark is typically 1 mm in diameter or a couple of millimeters in diameter.

**Dave Jones:** It's copper with the um solder mask pulled back. Now, it's very important to have the solder mask pulled back so there's a lot of contrast between the um copper color on there and the surrounding solder mask.

**Dave Jones:** But, the reason you have two is they they align it down here like this at this point, and then the camera goes over there and gets the other fiducial, and it knows from the files you've given it how far that dimension and that dimension is, and it actually can uh rescale the board to um uh take into account any minor direction directional tolerances on the bare board manufacture.

**Dave Jones:** If you've got fine pitch components like this BGA, for example, as you can see, what you do is you put what's called a local fiducial into here. So, you see there's a little fiducial there, and there's a little fiducial at opposite corners of this high pin count device.

**Dave Jones:** So, if you look at if you look at that device, there's the little tiny there's the little fiducial there. There it is. And on the opposite side, so you want to put those on very high density devices like BGAs.

**Dave Jones:** Typically for SO packages and everything else, you just don't bother. You just rely on the two fiducials on the panel. But, local fiducials can be important to get extra dimension and tolerance in that particular area of the board.

**Dave Jones:** And one very important thing not to forget, if you're loading components on the top and the bottom of the board, make sure you add the fiducial marks on the bottom as well.

**Dave Jones:** Otherwise, they won't be able to succeed they may not be able to successfully load that side of the board. So, make sure you do fiducials on both. Now, I know what you're thinking.

**Dave Jones:** Why is this board gold? Why are is everything gold plated? All the pads and everything. Well, not only does it look funky, you know, nice gold highlights around the edge, but gold can be made extremely extremely flat surface.

**Dave Jones:** So, when you got a high pin count BGA device like this, it's it's very important, in fact, it's vital to use gold because if you use solder or tin coated board, sure they can air level them, which is what's called hot air leveling on on a copper on a tin finish, it's going to be nowhere near as flat as this.

**Dave Jones:** So, it's very important for solder mask layering and for for the tolerances when the balls go on there and it and the solder reflows. So, I'd recommend even for simple boards, gold plate doesn't cost that much extra.

**Dave Jones:** I'd recommend you get gold plate. I use them on all my personal boards as well. Costs a few cents extra. Now, there are going to be times when well, you just can't panelize a board.

**Dave Jones:** One example of this is my micro watch board, which because it it sits on your wrist and the board is exposed, you can actually see it. I I wanted really nice cleanly routed edges.

**Dave Jones:** I didn't want to have to V-groove it and then file them off to get a nice edge. That sucks. So, I got them individually routed. So, this is what's called supplied loose or individually routed from the PCB supplier.

**Dave Jones:** And that's great if you want beautifully uh milled and machined edges. And that's okay. If you have to just do an individual board like this, it's it's fine. They can What the PCB assemblers can do, they'll charge you for it though, is they'll make up a custom little carrier module that's you know, routed to the shape of your board and they will actually mount them in that.

**Dave Jones:** There'll be an extra tooling cost but it might be worth it if you want a beautifully routed board. Now, I'm sure everyone recognizes this. It's the Arduino. Now, did the Arduino guys actually get these assembled as individual boards or did they actually panelize it and snap it out later?

**Dave Jones:** Well, there's a couple of telltale signs. All you got to do is run your finger along there and you can tell it's as rough as guts. That means it's been V-grooved and snapped out on all four sides.

**Dave Jones:** And if you actually get in there and take a look at it, it might be hard to see it but it's actually a V It's It's actually a V-shaped edge on it.

**Dave Jones:** You can see where it's been V-grooved and snapped out but this bit over here has been routed. Check it out. That's smooth as a baby's butt in there but it's rough up here.

**Dave Jones:** So, they routed out that little bit, V-grooved everywhere else. There you go. Okay, now let's actually take a look at a board. Now, assume this is your design, okay?

**Dave Jones:** You've got it finished and you're proud of it and it's lovely and it looks great in 3D mode. Check it out. There we go. It does everything you want.

**Dave Jones:** Now, uh what you have to look for is that A, we talked about this before, you've pulled back the uh the copper from the edges of the board, okay?

**Dave Jones:** Very important uh for when you do V-grooving cuz we're going to V groove this design because it's a nice uh square uh board. So and we don't need uh fully routed nice clean edges.

**Dave Jones:** We're happy to just V groove it, okay? So what we do is we flip it over to our panel and we do a separate This will usually be a separate uh PCB and you've duplicated this board multiple times.

**Dave Jones:** Now this is Altium Designer. It'll automatically uh do this for you. You can actually place multiple designs. But as you can see we've created a panel size here. We've created uh tooling strips top and uh bottom and we've actually uh put in the tooling holes.

**Dave Jones:** There it is. It's a 3.2 mm hole as you can see. We've created the fiducial here like this which is basically just a pad um with a uh This one has fiducials top and bottom but it's a pad um that just has the solder mask expanded on it.

**Dave Jones:** So if you go into 3D mode here, let's check it out. It all looks really groovy and you can see that the uh copper has doesn't touch between boards like that.

**Dave Jones:** So there's enough room to actually do the uh the V grooving in there and you can actually see that the fiducial looks like a real fair dinkum fiducial. It's got the gold um plated pad in there with the solder mask expansion.

**Dave Jones:** So that will provide a nice high contrast. There's the uh tooling holes up there and it all looks very good and panelized. Now if we go back to 2D mode, what you do is you actually create um you actually create a separate uh Well, I I call it fab notes but you can call it anything you like.

**Dave Jones:** A separate layer that just has uh the particular tooling information you want. In this case you just put a line in there that shows I want V-grooving all the way down there, and I want V-grooving across the middle like that.

**Dave Jones:** And it's easy. And the manufacturer will just interpret that. It's not actually part of your board layout, but it'll appear on the Gerber files, and that gives them the information they need to manufacture this panel with V-grooving.

**Dave Jones:** Now, an often overlooked aspect of board design, it's not just a panel base, but for any board, but particularly when you're going to manufacture, is you want good solder mask expansion around in your pads.

**Dave Jones:** Now, this is a standard quad flat pack 44-pin microcontroller with a reasonable pin pitch. But, let's go to 3D view here. And what you want, there's the chip, and you want the solder mask expansion between these pads.

**Dave Jones:** You want You don't want this solder mask in here, this little slither of solder mask so thin that it actually disappears when they go to manufacture it. There's a minimum width it needs to be, and that's probably about four or five thou before it starts becoming unusable and it breaks.

**Dave Jones:** If you don't have solder mask between your pins, you end up You can get shorts easily on your pins. So, you want a reasonable distance of solder mask. It's very important to check this before you send your boards out to be manufactured and then loaded.

**Dave Jones:** Now, as you can see here, we've actually got an expansion of 1.5 thou on or 1.5 mil as it's called, 1.5 thou on the solder mask expansion, and that's what we get here.

**Dave Jones:** Now, we can actually go in there and actually measure that distance between the measure that solder mask width in there. And as you can see, it's 5.5 mil. So, this one is more than adequate to be manufactured.

**Dave Jones:** That will be no problems at all. We get good um mask between our individual pins and we shouldn't get shorts. Um there's a very low likelihood of getting shorts on those pins.

**Dave Jones:** That's what you want. So now you've finished your panel design, it's all fantastic, you've got your tooling scripts and dooshals and la-di-la-di-la. You've got it all. What do you do?

**Dave Jones:** Well, you've got to supply the correct files to not only the bare board manufacturer, but to the PCB assembler as well. Let's take a quick look at that. Okay, so we've created our PCB panel.

**Dave Jones:** Now let's generate the Gerbers. Now, as you can see, I'm going to generate this is only a two-layer board, so I've got the top overlay, I've got the top paste uh mask, which will go to the assembler.

**Dave Jones:** It won't You don't have to send that to the PCB manufacturer, they don't care about the paste. Uh you've got the top solder mask, top layer, bottom layer, bottom solder mask, bottom paste, bottom overlay, if you've got an overlay on the bottom of your board.

**Dave Jones:** I uh actually create a separate uh mechanical layer for the PCB boundary. That's just the outline, the outer outline of the board, and I've got the fab notes, as I said before.

**Dave Jones:** Now the fab notes can include all sorts of stuff about the detail of board, like it's 1.6 mm FR4 and you want gold plate and ya-di-ya-di-ya-da and tented vias and all that sort of stuff.

**Dave Jones:** But this uh fab notes only just has the V-groove information cuz I'll supply a text file with all that other information separately. So we'll just generate uh some Gerbers there.

**Dave Jones:** And bingo, it's done. Here it is. And there is There's our Gerber information. So it's got These are all supplied as separate layers. So here we go, it's generated all of the layers.

**Dave Jones:** This shows them all overlaid, but as you can see, it would do it separately. There's that separate V-groove thing I showed you before. Here's the origin marker down the bottom.

**Dave Jones:** That's the reference origin and these are the different layers. There's my board outline, there's my uh PCB that's the top and sorry, the bottom solder mask, and and that's the paste file, but that goes to the assembler, and there's the overlay, and there's the top solder mask, and the bottom layer, and so forth.

**Dave Jones:** So, as you can see, it just generates information for the panel so that the manufacturer knows what to do. They know you want V-grooving all through that board. And it's the same thing if you do routing.

**Dave Jones:** Now, there's one other thing that you have to supply to the PCB manufacturer. We've done the Gerber files, but you need to supply the NC drill files. Now, let's just generate those.

**Dave Jones:** And bingo, they're done. And there they are. There's all our different holes used in our design. As you can see, some of them are actually slots there, but others are these are supposed to be square.

**Dave Jones:** They It doesn't render properly, but that generates industry standard NC drill file, which goes along with your Gerbers, and that provides all the information the manufacturer needs in terms of drill sizes, how many drills, and where to drill them.

**Dave Jones:** And of course, there's one vital thing which the assembly house is going to need, and that is the pick and place files to know exactly where to put what component.

**Dave Jones:** So, we can generate pick and place files here. Let's do it as a text file. And here's the pick and place file which is generated. This is a text one.

**Dave Jones:** It can be a CSV or other formats as well. Manufacturers will can pretty much accept anything you give them. Here's the designator down in this column down here, and then we've got the footprint, and then we've got the actual location of the component relative to a particular reference point, which is usually the bottom left-hand corner, but it doesn't always have to be.

**Dave Jones:** And this is the file that the manufacturer needs to feed into their pick and place machine to assemble your board. And of course, you would also give the assembler the overlay diagram as well, showing where all the parts go with the reference designators.

**Dave Jones:** And also an important thing to also give them is a physical sample of the board, exactly how you want it built, cuz they aren't mind readers. Usually, they do a pretty darn good job.

**Dave Jones:** They do know what they're doing, but nothing beats them actually having a real physical sample in their hands that they can actually compare the board when it comes off the machine or when they're loading and setting up their machine.

**Dave Jones:** And after having gone through all that information, you can just say, "Well, I don't want to do that. Just give your board and just the Gerber's for the individual board, your bill of materials, everything else to the assembly house." And some assembly houses will do all that panelization and everything else, the fiducials, the tooling, and the pick and place, and all that for you.

**Dave Jones:** It's called a turnkey solution. They will take just your individual board, and you don't even have to send them the components. You don't have to worry about the reels and all that sort of stuff, getting them in tubes, trays, and quantities.

**Dave Jones:** You just say, "I want a thousand of these, please." And they'll go, "Yes, sir. No problem." But, they'll charge you a lot more money for it. And you also don't keep individual control like when you do your own panel and you do everything yourself.

**Dave Jones:** You supply the parts. They might get the parts from the gray market. Who knows? So, just something to watch out for. You can get the assembly houses to do the whole shebang, but whether or not you want to, I don't know.

**Dave Jones:** It's up to you. So, there you go. That's a pretty much a quick overview of how to design your product for high-volume manufacture. And there's more that goes into it as well.

**Dave Jones:** There's more smaller little things which are applicable to niche designs and stuff like that, but the golden rule is talk to your PCB assembler first before you go and design your panel and everything else.

**Dave Jones:** Because you might put all the money buying your components and designing your board and then find oh, might find it hard to get an assembler or the assembler you like to do your board.

**Dave Jones:** So, just be careful and you will probably have to do a second spin as well or a third spin of the board. It's not uncommon whatsoever. So, just budget that in.

**Dave Jones:** You're not always going to get it. Even the professionals don't always get it right the first time. Catch you next time.
