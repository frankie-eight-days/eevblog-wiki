---
video_id: VXE_dh38HjU
title: EEVblog #127 - PCB Design For Manufacture Tutorial - Part 1
url: https://www.youtube.com/watch?v=VXE_dh38HjU
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 33, "3": 49, "4": 66, "5": 82, "6": 98, "7": 113, "8": 128, "9": 145, "10": 157, "11": 171, "12": 186, "13": 203, "14": 217, "15": 231, "16": 246, "17": 259, "18": 275, "19": 291, "20": 307, "21": 323, "22": 337, "23": 351, "24": 364, "25": 378, "26": 391, "27": 403, "28": 418, "29": 433, "30": 450, "31": 467, "32": 480, "33": 493, "34": 507, "35": 522, "36": 540, "37": 554, "38": 566, "39": 576, "40": 590, "41": 609, "42": 627, "43": 644, "44": 660, "45": 676, "46": 687, "47": 704, "48": 718, "49": 730, "50": 741, "51": 756, "52": 770, "53": 788, "54": 802, "55": 816, "56": 837, "57": 850, "58": 863, "59": 877, "60": 889, "61": 902, "62": 915, "63": 929, "64": 944, "65": 957, "66": 975, "67": 990, "68": 1003, "69": 1017, "70": 1033, "71": 1046, "72": 1060, "73": 1074, "74": 1089, "75": 1107, "76": 1122, "77": 1137, "78": 1150, "79": 1163, "80": 1177, "81": 1192, "82": 1205, "83": 1221, "84": 1234, "85": 1251, "86": 1265, "87": 1280, "88": 1296, "89": 1312, "90": 1325, "91": 1342, "92": 1359, "93": 1373, "94": 1387, "95": 1400, "96": 1412, "97": 1426, "98": 1439, "99": 1451, "100": 1462, "101": 1477, "102": 1489, "103": 1502, "104": 1516, "105": 1533, "106": 1550, "107": 1564, "108": 1576, "109": 1589, "110": 1608, "111": 1620, "112": 1634, "113": 1651, "114": 1665, "115": 1682, "116": 1698, "117": 1714, "118": 1733, "119": 1743, "120": 1756, "121": 1770, "122": 1782, "123": 1796, "124": 1812, "125": 1825, "126": 1842, "127": 1856, "128": 1872, "129": 1888, "130": 1899, "131": 1917, "132": 1934, "133": 1948, "134": 1965, "135": 1981, "136": 1998, "137": 2006, "138": 2019, "139": 2036, "140": 2050, "141": 2067, "142": 2084, "143": 2098, "144": 2111, "145": 2127, "146": 2146, "147": 2160, "148": 2177, "149": 2192, "150": 2205, "151": 2218, "152": 2235, "153": 2252, "154": 2266, "155": 2281, "156": 2293, "157": 2310, "158": 2324, "159": 2340, "160": 2354, "161": 2368, "162": 2386, "163": 2401, "164": 2417, "165": 2431, "166": 2447, "167": 2467, "168": 2483, "169": 2499, "170": 2515, "171": 2531, "172": 2545, "173": 2563, "174": 2577, "175": 2592, "176": 2606, "177": 2622, "178": 2642, "179": 2657, "180": 2669, "181": 2681, "182": 2694, "183": 2707, "184": 2722, "185": 2742, "186": 2756, "187": 2772, "188": 2789, "189": 2804, "190": 2821, "191": 2839, "192": 2855, "193": 2868, "194": 2882, "195": 2899, "196": 2913, "197": 2927, "198": 2942, "199": 2954, "200": 2968, "201": 2981, "202": 2994, "203": 3008, "204": 3021}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi. Now, I know a lot of you out there like designing your own products, and that's fantastic. Now, let's say you've

**Dave Jones:** come up with this great new design, okay? You've got this one-off, you've built it, works great, you've debugged it, fantastic, and you want to make 50 of them, 100, 500, 1,000. Think big. 10,000, 100,000. What do you do? How do

**Dave Jones:** you take your project from a one-off through to volume production? Well, I'm glad you asked. What I'm going to do today is take you step-by-step through the processes, both thought and design processes you need to do to take a

**Dave Jones:** one-off project through to volume manufacture. Let's go. What I'm going to concentrate on today is just the board level stuff, okay? So, I'm not going to get into housings and, you know, designing the overall look and feel of the product. That requires a

**Dave Jones:** whole separate blog. So, this will just be the board level, how you can design and manufacture a high volume PCB. Now, let's start by taking a look at something like this, okay? It's a through-hole board, traditional through-hole, okay? Green solder mask,

**Dave Jones:** you know, pretty basic traditional board. Now, is this suitable for high-volume manufacture? Well, yeah, you can get it done, but it's not going to be very cost-effective. And for high-volume manufacture, that's what it all comes down to, manufacturing

**Dave Jones:** cost and complexity. Now, if you've got a through-hole board like this, it's just not going to cut it these days, okay? Too expensive to manufacture. Sure, you can labor still a bit cheap in China, but trust me, it's not going to be as cheap

**Dave Jones:** as surface mount. So, the first thing you want to look at is converting your through hole design like this into something more like this. With mostly in almost the goal is to go entirely surface mount because as you'll see

**Dave Jones:** that'll save you the most amount of cost. It'll reduce your assembly time and everything will be sweet. So look at converting every component in your design into surface mount. Now I know this can be almost a total redesign and that's why

**Dave Jones:** I've mentioned this before in the blog. During your entire design process, even if you're doing a one-off prototype, if you think there's even remote possibility of making this into a volume product in the future, you need to put a

**Dave Jones:** lot of thought into what components you choose for your board. But trust me, even if you do have to re- totally redesign your entire board from through hole it through to surface mount or just change half the components on

**Dave Jones:** there to lower the cost, whatever, as you'll see it'll be worth it. So go to the extra effort up front. If you're going to make more than say 50 boards or something, it's worth putting the effort in to redesign it properly. Now the

**Dave Jones:** difference between through hole and surface mount is pretty obvious. Here's a video of a um a through hole assembly line and as you can see the workers sit there, they manually install the components and well, that takes time, effort and labor

**Dave Jones:** and you want to avoid that if at all possible. Whereas here is a modern pick and place machine placing your components from reels and tubes of components onto the board automatically and this can churn out boards much much

**Dave Jones:** quicker with less effort. You set it up once and you push the button and it's all automatic and your boards magically spit out the other end. That's the ultimate goal for high volume manufacture, as little labor as possible.

**Dave Jones:** One of the first things you do is go through every component in your bill of materials in your design and you look at it. Is that component easily manufacturable by the supplier I'm going to choose to assemble my board? Cuz not

**Dave Jones:** all assembly houses are the same. They have different requirements. They have different pick and place machines with different capabilities and not all of them can do what you want. So basically you want to stick, if you can, stick to

**Dave Jones:** large common components cuz that means every assembler out there will be able to do it and do it cheaply. Now, that might mean, okay, 0402 size resistors and capacitors for example. There are some assembly houses out there that

**Dave Jones:** don't have the new machines that can handle components that small. So, think about 0603 instead of 0402. Think about quad flat pack packages instead of BGA or something like that. BGA is going to be a little bit more touchy, harder

**Dave Jones:** to inspect, yields not going to be as high, more critical pad dimensions, all that sort of stuff. So, stick with the common package as I say 0603 and up. 0402's okay. You know, stick with 0.5 mm pin pitch or

**Dave Jones:** larger on your SO type packages and your quad flat packs and stuff like that and you'll be fine. With high volume manufacture, you're going to have to spend a bit more money on components than you anticipate. If you're making, say, 100 boards, well,

**Dave Jones:** you can't just go to Digi-Key and buy 100 resistors loose on the tape like that. The the assemblers are going to hate you for it. Trust me, because they may not say so, okay, but they're going to charge you more because they may have

**Dave Jones:** to manually put these onto what's called reels, okay? This is what you need to buy for all of your components, uh all of your SMD components. Now, reels come in different types. This one might have 5,000 resistors, but they're very cheap.

**Dave Jones:** So, this reel might only cost you five or 10 bucks or something like that. You can get little mini reels like that, or they come in huge reels like this, okay? Or uh when you're talking about ICs, you

**Dave Jones:** might they might come in uh tubes like this, and these automatically slip into the pick and place machine, and the chips shoot out like that, okay? You don't just want to buy them loose in your little Digi-Key packet like that.

**Dave Jones:** That Otherwise, uh if you do that, they'll have to hand-solder them. The efficiency's going to drop, they're going to charge you more, they're going to take longer to assemble them. Pooh, it's hopeless. So, you want all your components um Now, chips need to be in

**Dave Jones:** either tubes, or they need to be uh on You can get chips on reels as well, or they need to be in what's called trays. Now, here's a photo of the trays. Trays generally aren't as good cuz a lot of uh

**Dave Jones:** machines can't support trays. They'll want everything on reels or tubes. So, just be careful there. Let's do a search on Digi-Key for a part to see if we can get it in uh reel or a partial reel or something like that. See

**Dave Jones:** what our options are. Now, let's take an example of the ZXCT1009. And let's do a search for that. And as you can see, three options here have popped up. We want the SOT-23 version, which is here, okay? But look, it's got

**Dave Jones:** three lines It's got three different rows there. It's got three options for the same part. Check out the quantity over here. 114,000 parts they've got in stock. So, that's fantastic, okay? But as you can see, they're all the same uh quantity

**Dave Jones:** um available. So, that tells you it's exactly the same part, exactly the same stock, but three different procurement options. Now, the second the second row here, as you can see, just here it says it's available in cut tape. Now, that's

**Dave Jones:** the version you will typically get um it says minimum quantity over here of one, okay? Now, that's the one you typically get when you buy prototypes. Okay, you only want five parts for a prototype, so you buy five, they cost

**Dave Jones:** you a dollar and 9 cents each, you know, and you pay five bucks and and that's it, okay? Nice and cheap for prototypes, but we want Let's say we want to manufacture 100 boards, okay? You wouldn't buy You wouldn't buy that cut

**Dave Jones:** tape uh version. You wouldn't buy that part number because it comes on the cut tape. It doesn't come with a reel and it doesn't come with the leader tape attached, which the manufacturer your assembly house needs to put that into

**Dave Jones:** the pick and place machine. That's That's pretty useless to your manufacturer. Now, if you look at the top row up here, as you can see, minimum quantity of 3,000. So, that's obviously at that says tape and reel, okay? So, that is one

**Dave Jones:** reel of parts, but you've got to buy five 3,000 of them minimum to get that one reel and they're 43 cents each. Let's go look at that price. Uh sorry, 40 cents each at 3,000, but that's 1,209 dollars. So, you'd have to spend 1,209

**Dave Jones:** dollars there just to get your 100 parts needed for your 100 boards so that the assembler can assemble them. Now, that's just crazy, okay? So, what you want is this third option down here. Now, this isn't available for all parts. So,

**Dave Jones:** really this is uh you have to choose your parts that go into your design carefully if they have these options. If you're only going to make 100 of them or or even, you know, 500 and you want them on a reel, they

**Dave Jones:** offer what's called a Digi-Reel option. Now, that is the same as the cut tape. As you can see, you can only buy You can buy just one of them, but they will actually charge you a fee and they'll

**Dave Jones:** put it on a reel for you with the leader tape exactly what the manufacturer needs, but you can order any quantity you want. So, let's go in there and calculate that price. And let's say we only wanted to build

**Dave Jones:** our 100 boards. So, we go down here, we type in 100, and we go calculate. And instead of paying the over $1,000 we had before, our total extended price is $84 plus um plus here it says a $7 reeling fee fee

**Dave Jones:** will apply to each reel ordered, but that's cheaper. Okay, you're still only paying less than $100 for your 100 parts as opposed to over $1,000 for the 3,000 minimum. So, just be careful when you're designing your product, make sure these not only

**Dave Jones:** are the parts in stock, but they're available in suitable quantities either reels or tubes or or partial trays or something like that for your particular design. It's very important. So, you can spend a lot of time just mucking around on Digikey

**Dave Jones:** finding or Mouser or It's the same on Mouser and Element 14 and the others. They all have the same service. You can spend ages just doing this to optimize the manufacturing for your little board for your 100 or 500 boards. It's crazy.

**Dave Jones:** So, yes, if you're going to make 100 boards, you might have to buy 500 ICs. You might have to buy 5,000 resistors, something like that. That is the price you pay for going to high-volume manufacture essentially. So, if you want to get 100

**Dave Jones:** boards made up front, then you need to do the costing based on your entire reels of components. Just assuming you're only going to make 100. If you're going to make another thousand down the track, great. You'll have most of the

**Dave Jones:** reels components on the reels left over, but you have to amortize that cost in to your 100 boards. Now, the other important thing to remember is that the pick and place machines can only support a certain number of these at any one

**Dave Jones:** time. So, a machine might only be able to support 20 reels or 30 reels. That means you can only have 20 or 30 different components on your board. If you have to do more than that, then they need a second machine either in line

**Dave Jones:** with it and the board goes through the first machine on a conveyor through to the second machine. Not many houses will have that set up. The smaller houses won't have that. So, they'll have to put your board through a second time, reset

**Dave Jones:** up the machine. So, if you're manufacturing 100 or 1,000 boards, they put it all through once and when they're finished, they rip off all the reels, they change them over, they have to put your boards all the way through again.

**Dave Jones:** And that costs you money. Try to avoid that. So, go through your design component by component and see if you can consolidate the number of components. Do you really need a 15k pull-up resistor? If you've got a 10k

**Dave Jones:** resistor somewhere else on your board, use a 10k for the pull-up. Consolidate those values. If you need a 20k resistor on the board, it might be better to put two 10k resistors in series in your circuit because you're already using

**Dave Jones:** that component 20 times elsewhere on the board. So, just look at consolidating your components. It's very important. Also, think about pad sizes. There's no point designing a fantastic board if you find that your manufacturer and their process cannot successfully load your

**Dave Jones:** component on the board. They short together because they the solder mask is too you haven't got sufficient solder mask between the pins of an IC, for example, and they put too much paste on, it shorts out, or a resistor tombstones

**Dave Jones:** because you don't have thermal reliefs on one pad. I mean, you've got one pad connected this pad over here of your resistor connected to a big solid ground plane which sucks all the heat away and the other one just going off to a 5 hour

**Dave Jones:** track, then well, that resistor can tombstone. Look at things like that. Sometimes manufacturers will have their own preferred pad styles, but usually if you say stick to the manufacturer's recommended footprint or you use the IPC standard footprints, you'll generally do okay, but you also

**Dave Jones:** have to think about the size of the pads. So the IPC footprints for example come in three sizes, nominal, least and most. So they'll put an N, L or an M on the end of the footprint name in your

**Dave Jones:** library and what that means is the it's just the amount of pad the pad size. L is the least amount of pad size, so the smallest. So if you've got a very high density board with all the components stuffed

**Dave Jones:** together, then you'll want to use the least size pad, the the smallest pad you can get. But then you might find oh, then you can't probe them or you can't solder rework them by hand if you have to or something like that. So you've got

**Dave Jones:** to think about those sort of things. Normally you'd stick to the nominal size footprint, but if you want something if the flying test probes to come down, which is another aspect of your design you've got to think about, testing.

**Dave Jones:** Testing and programming your board can be a big thing. Now, if you've got a microcontroller on there for example and you've got to program it, well, how do you do that? Okay, it was fine in your design, you might have used a socket for

**Dave Jones:** a DIP chip, but if you've got surface mount now, well, you can program the chip before you put it on there, before you give it to the manufacturer, but that's hard and difficult. It's much better to actually solder your

**Dave Jones:** microcontroller for example onto the board and then provide an in-circuit programming header. So you've got to make sure that is designed into the board. You've got to make sure it's accessible where you can program it. And if you design a little bed of nails

**Dave Jones:** which comes down, here's a photo of a typical bed of nails for a board, then you bring it down and you want to be able to get those pogo pins onto those test pads or onto that in-circuit programming header. So, you've got to

**Dave Jones:** think about that sort of stuff when you're designing the board up front. And we haven't even gotten to panelization in the high-volume manufacturing yet. Phew. One of the most useful things you can do when you're designing a high-volume

**Dave Jones:** product is to get a spreadsheet of all the components, your entire bill of materials into a spreadsheet, put them in the the descriptions, the footprints, the quantities, and the manufacturer's part number, and then the supplier part number, and usually an alternate

**Dave Jones:** supplier part number. So, you might put in the Digi-Key part number, the Mouser, the Element 14 part number, or something like that as your supplier. And then you'll have a might have another column uh based on um how many components are on a reel. For

**Dave Jones:** example, there's 5,000 per reel. So, if you go to the effort and and cost as well, you put the item cost, you can total them all up, see what it's going to cost you to manufacture 100 boards even though you've got to buy 5,000

**Dave Jones:** resistors in all these reels. So, a spreadsheet is handy. Putting the effort in up front pays dividends in the long run. Trust me. Okay, so you've done all the hard work. You've got your board. You've gone through all the processes I just

**Dave Jones:** mentioned, and it's all ready to go. Well, no. Sorry, it's not. If you just try and get one individual board like this, or a hundred or a thousand of these manufactured just on its own like that, it's not very economical. Why? The

**Dave Jones:** reason it's not economical to get just one board like this, manufactured individually, is because well, it goes through the machine, the pick and place just does that one board, and it spits it out. And there's all sorts of handling issues with the board

**Dave Jones:** as well as it goes through the machine and stuff like that. So, what you want to do is what's called panelize it, and that's take your one design and step and repeat it onto a PCB panel such as this.

**Dave Jones:** Now, there are certain panel sizes which we'll go into, but basically, you just want to step and repeat it like that. So, in this case, we've got 12 boards on the one panel. So, they set up the machine, the board goes in, and bingo,

**Dave Jones:** they can assemble 12 boards at once. Well, components have to be placed one by one, but it just means it's much more efficient. You can just churn multiple boards through the process much quicker, and that adds up to real savings in

**Dave Jones:** high-volume manufacture. Now, there's a conflicting requirement with panels because your bare board PCB manufacturer, they will have standard panel sizes. Now, it's very tempting to fit as many of your designs as you can onto that maximum size panel that they

**Dave Jones:** do, but you have to be cautious doing that because you have to ask, can my PCB assembler actually physically handle a board that big? Their machine, their particular machines they use might have a limit on the maximum size of the

**Dave Jones:** board, and it might be a lot smaller than the maximum panel size the PCB manufacturer can supply. Now, a typical bare board PCB panel might be 18 in by 24 in or 450 by 600 mm. Now, a lot of

**Dave Jones:** assemblers might not be able to handle that size board. Now, I generally stick with like an A4 size panel because I I I find, you know, pretty much everyone can handle an A4 size, but ask your manufacturer what

**Dave Jones:** they can handle because you don't want to get your boards manufactured and then find, "Oops, it's 10 mm too big for the machine." Uh you're screwed. You got to go to a more expensive manufacturer. Watch out for it.

**Dave Jones:** Let's take a look at a typical panel. I've got one here. Now, uh there's many different ways to do a panel, which we'll go into, but a panel will have these basic requirements. It will have what's called a tooling strip

**Dave Jones:** top and bottom. This is this bit down here. Now, what that does is allows the uh pick and place machine to actually grab hold of it. It can either sit in rails like this, and it can go physically be uh automatically moved

**Dave Jones:** through the machine like that. Now, what the tooling strip must have um it By the way, it should be about 10 mm wide top and bottom like that. If it's any smaller than that, then the machine may not be able to automatically handle the

**Dave Jones:** board. The other thing you will have in these tooling strips are the tooling holes. Now, you typically have four of them like this, a minimum of four, and they're typically a 4-mm diameter hole. And they're used um to get uh little um

**Dave Jones:** There's little uh sprigots uh cogs in there that physically move the board along the panel. So, it should have tooling holes. The size isn't that critical, um but 4 mm is a bit of an industry standard tooling hole, and it

**Dave Jones:** must have fiducials as well. Fiducials uh marks as well, uh which we'll go into in more detail later. And a panel must also have a way to break the boards out. So, it must either have uh routing, which is like this one with breakout

**Dave Jones:** tabs, or V-groove, and we'll go into those, but they're the basic re- requirements of a panel. Now, even if you've got a huge design like this one, this one's almost A4 uh size, and really, as you can see, only

**Dave Jones:** one of them fits on a panel. Now, we can manufacture this is just an individual board or what's called a loose board or a fully routed board without any tooling strips, but then there's limits to how close you can

**Dave Jones:** components can come to the edge of the board because it needs to physically hold it. So, even with a board like this that's large, you would still put tooling strips top and bottom and a way to break the board out. And here's an

**Dave Jones:** example of a more advanced panel that has three extra features, which I'll show you. One of them is a bad board marker. Now, if you take a look here, as you can see, it's just on the it's in the part of the dead

**Dave Jones:** part of the panel, but it's a marker that the assembler can actually mark that indicating when they do an automated test that this particular board is bad out of you know, if you got 20 boards on there. That can be really

**Dave Jones:** important. So, you know, don't bother using that board. It's failed. Now, another item that's it's got is what's called an impedance test strip because this is a controlled impedance PCB. So, in the tooling strip here, we've added an

**Dave Jones:** impedance test coupon. It's called. And what that does is just allows you when the bare boards manufactured, it allows you to test that the controlled impedance is exactly what you want it to be. The third item this board has is what's

**Dave Jones:** called a test stack. Now, what this does is it brings the internal copper layers because this is an eight-layer board, I think it is. It brings the copper to the edge. Now, this could be tricky to try and get on camera here, but as you can

**Dave Jones:** see, the copper's right on the edge. Now, you would probably need a microscope to look at that, but what it just allows you to inspect the uh layers on that board after it's been manufactured. So, that and and they're

**Dave Jones:** different lengths. There's many different ways to do this, but that's just an example of how you can inspect the board um after it's manufactured. Now, a lot of um companies when they bare board manufacturers when they assemble your panel, they will provide

**Dave Jones:** you with a uh what's called a core sample, and they will actually cut off a part of one of your boards, and they'll give it to you um so you can actually inspect that under a microscope yourself, but this just allows you to do

**Dave Jones:** that just in case they don't provide you with that core sample. There's another important thing I forgot to mention, not only for the individual bare board, but um it relies it it uh has the same thing on panels as well.

**Dave Jones:** Now, when you um when you lay out your board, you should add what's called pullback to the copper. Now, as you can see, the copper doesn't go all the way to the edge, and that includes those internal layers as well. If you've got

**Dave Jones:** an eight-layer board, don't bring your copper all the way to the edge cuz it can short out and cause all sorts of problems. So, have have say 1 mm pullback or something like that. At least allow something so the copper

**Dave Jones:** doesn't go right to the edge. There's one other thing you can do with panels as well. If you've got a lot of boards like this, it's a fairly unique requirement. Uh everyone won't need it, but I'll just mention it. It allows you

**Dave Jones:** to actually see these little breakouts in the corner here. Okay, you can actually route out um you can actually route out uh tracks out of there and bring the tracks out of each panel. So, you might want to bring out uh test

**Dave Jones:** tracks out of each panel like this, and you might have a test connector on one side of your board or some interface for some sort of test jig, and you might want to test all of your boards in situ

**Dave Jones:** in the one panel. Um it's it it it's not a common requirement, but you can actually do that. Now, let's get into how you break the boards out. How do you get them out of the panel after they're assembled? This

**Dave Jones:** has got four individual boards in it, okay? Quite complex. How do you break it out? Now, there's two different uh methods to do it. One is called V-grooving, which I'll show you up close, and the other is called uh

**Dave Jones:** routing and uh breakouts with tab breakouts. Now, this is an example of a V-grooved board. As you can see, it's got these score marks, or what's called a V-groove. I'll show them up close later, but along like this, and both

**Dave Jones:** vertical and horizontal. Now, here's another uh board, which is another example of V-grooving as well, okay? Now, this works really well on completely square boards. If your board is completely square, and you don't have any components overhanging the end,

**Dave Jones:** which can often be a problem uh because when you get this board um after it's assembled, they have to break these out. Now, normally what they do is they run along with a little wheel along there, which actually top and bottom, which

**Dave Jones:** then does a nice clean cut on it. Um but, if you've got components overhanging the edge, for example, like you like like you have a connector or something like that overhanging the board, well, you can't actually get in

**Dave Jones:** there to break it off. So, you might have to break it off by hand. But, what a V-groove allows is allows you to easily just snap the board off, and I'll show you. Here it is. Boop. See? But, what you get, okay, once

**Dave Jones:** you do that, is you I probably can't show that on camera, but you get a pretty rough pretty rough edge. It gets hairs It get gets uh little little fiberglass hairs on it, and it's it's just not a very clean way to

**Dave Jones:** actually uh do a board, but you can just snap them off. Even if they've got component overhangs, you can sort of wiggle them a bit and they'll come apart really easily. That's V-grooving. Now, it's pretty hard to get in there

**Dave Jones:** and actually show you what a V-groove looks like, but what it basically involves is if your board is like this, the drill actually drills down into your board like that. That's the top of the board and this is the bottom of the

**Dave Jones:** board and it goes like that. They drill at top and bottom, okay? And it leaves just a little bit of fiberglass actually connecting in the middle like that. And that allows you to just snap the boards off really easily. And that's

**Dave Jones:** V-grooving. Now, you can actually specify the angle of the actual groove in there like that if you want to get fancy and or you know, if you're someone like Apple and you're really designing, you know, a million or a billion of

**Dave Jones:** these things, then all that sort of stuff might actually matter. But, um generally, you just say, "I want V-grooving, please." and they'll just do V-grooving. Now, I mentioned copper pull back before. Now, because a V-groove actually has a distance between it, which can be

**Dave Jones:** a bit variable, then you have to be very careful to actually pull back your copper so that it's not exposed when they do the V-groove. So, if you have continuous copper going across like this and you take it right to the edge of your board,

**Dave Jones:** then well, you're just going to get exposed copper when they go in and they drill it for the V-groove. Just be careful of that. Now, the other type of panelization is what's called routing with these tab That's a tab breakout, okay? Now, you

**Dave Jones:** just specify the routing path around your board. This is really good for odd-shaped boards, which I'll show you in a minute. But, basically, there's industry standard tooling sizes for these routes. Now, 2.4 mm is a standard routing tool width. So, you just specify

**Dave Jones:** that as an outline, and they will do it. You can actually tell them to do it, but it's better to specify yourself, so you know exactly what you're going to get. But, these tab breakouts, these can be a

**Dave Jones:** bit tricky. These can be an art in itself. Now, this is this board is hard to actually push out by hand. Sometimes, you can break the board, and especially when it's loaded with components, you don't do that. So, you might get in

**Dave Jones:** there with a pair of side cutters, for example, side cutters like that, and actually cut the board out. Now, you have to design these tab cutouts in such a way that it allows the board to be held in

**Dave Jones:** there fairly firmly, okay? Cuz you can't If you've got a very large board like this, which I'll go into, you can't just have one on the corner over here, one on here, because the damn thing will warp. So, you have to have

**Dave Jones:** You might have to have multiple tab multiple breakout tabs along the edge of your board, depending on how big it is. And you have to make them so that they When you cut them out, they don't have any burrs, as well.

**Dave Jones:** Here's an example of a very wide breakout tab that supports a very large board such as this. And it has multiple holes spread in an arc like that, which allows you to actually break it out. So, you put these unplated

**Dave Jones:** holes around there in an arc, and it breaks out, and it leaves just like a little indent in your board when you break it out. Here's a good example of a panel with an odd-shaped board. As you can see, we've got the tooling holes,

**Dave Jones:** the fiducials over here, but it's got It's routed out, okay? It's routed out around here. Now, and all the way around like that. Now, this is a good example, because it has a combination of V-grooving and routing. So, if you've

**Dave Jones:** got an you can see that the board has a weird shape on the on the bottom here and the top. So, you route out the weird shape ones, but it's straight on the edges. So, you do V-grooving on the edges like

**Dave Jones:** that. So, that allows you to snap easily snap out that board while giving you the giving you the advantages of the odd shape board with the routing. And this is just a fairly simple example. Actually, there's much more convoluted

**Dave Jones:** ways you can actually do this. And it's almost an art actually figuring out how to snap a board out of panel. What combination of V-grooving you use, what combination of routing as well. One very important thing to remember is

**Dave Jones:** how stiff is the board cuz often it will only be supported along the along the top and bottom edge here by the machine. And the pick and place machine comes in and it places the component down and you

**Dave Jones:** don't want this to happen. What? Look at this board, okay? And granted, this is a 0.8 mm board. It's half the size of a standard 1.6 mm board, but look at how much that board warps, okay? Fantastic. That's normal FR4. I kid you not, okay?

**Dave Jones:** But that's 0.4 mm. That can make you seasick almost, really. Okay? So, you've got to take that you've got to take the rigidity of your board into account when you're actually designing a panel. And here's an example of a panel that just

**Dave Jones:** has a V-grooving along the top and bottom edge and vertical routing like that. Once again, you could have done that as a V-groove, but in this case we wanted to get a really nice edge cuz this is what this is what routing gives

**Dave Jones:** you. Routing gives you a beautifully clean and smooth edge on your board with no burrs whatsoever. Whereas a V-grooved edge will be It'll be sharp. It'll be It won't be completely flat. And it It's just, you know, it's not a clean edge at

**Dave Jones:** all. You may even have to file it down afterwards. So, from that point of view, routing is preferred. But here's an example of a board that, because there's no central support in here, okay, it's routed all the way from top to bottom like that,

**Dave Jones:** okay, this can actually This can warp, as you can see. When you place the components in the middle, that board can actually warp like that. So, cuz there's no rigid support in the middle to actually cross-brace it. So, this board

**Dave Jones:** doesn't have components in the middle, so you didn't have to worry about it. They're only on the top and bottom. But if you start putting it in the middle, it can flex a lot, and that can be a

**Dave Jones:** problem. And here's yet another board where it's fully routed around, and it's got tab breaks like that. But in this case, it's got the tab break in the in the middle as well, so that helps form a rigid structure for the board. So, it's

**Dave Jones:** not going to warp nearly as much as that other board that didn't have any central support in it. Here's an example of a panel that has many different designs in it. And generally, this is okay for prototyping, but for production, it's generally

**Dave Jones:** frowned upon. You don't want to have to load multiple individual designs onto the one panel. It just confuses things. You can exceed the number of reels you've got and stuff like that. So, really, you want to stick to one design

**Dave Jones:** per panel. Now, that little thing there on the panel is what's called a fiducial mark. Now, these are very important to not only put on your panel, but on your actual board as well. Now, as you can see, this board will actually have

**Dave Jones:** actually four fiducials on the panel itself. Now, typically, you only need two. you put them in opposite corners of the panel. Now, the reason these are important is because when the board's manufactured, its dimensional tolerance, i.e. from a reference point over here to

**Dave Jones:** over here, it may be slightly out. Now, that's not a problem. When they assemble a board, uh they take a reference point, which will be this fiducial mark down here. What it does is a camera comes over and it looks at it looks at that

**Dave Jones:** fiducial mark. Now, a fiducial mark is typically 1 mm in diameter or a couple of millimeters in diameter. It's copper with the um solder mask pulled back. Now, it's very important to have the solder mask pulled back so there's a lot

**Dave Jones:** of contrast between the um copper color on there and the surrounding solder mask. But, the reason you have two is they they align it down here like this at this point, and then the camera goes over there and gets the other fiducial,

**Dave Jones:** and it knows from the files you've given it how far that dimension and that dimension is, and it actually can uh rescale the board to um uh take into account any minor direction directional tolerances on the bare board manufacture. If you've

**Dave Jones:** got fine pitch components like this BGA, for example, as you can see, what you do is you put what's called a local fiducial into here. So, you see there's a little fiducial there, and there's a little fiducial at

**Dave Jones:** opposite corners of this high pin count device. So, if you look at if you look at that device, there's the little tiny there's the little fiducial there. There it is. And on the opposite side, so you want to put those on very high density

**Dave Jones:** devices like BGAs. Typically for SO packages and everything else, you just don't bother. You just rely on the two fiducials on the panel. But, local fiducials can be important to get extra dimension and tolerance in that particular area of the board.

**Dave Jones:** And one very important thing not to forget, if you're loading components on the top and the bottom of the board, make sure you add the fiducial marks on the bottom as well. Otherwise, they won't be able to succeed they may not be

**Dave Jones:** able to successfully load that side of the board. So, make sure you do fiducials on both. Now, I know what you're thinking. Why is this board gold? Why are is everything gold plated? All the pads and everything. Well, not only does it look

**Dave Jones:** funky, you know, nice gold highlights around the edge, but gold can be made extremely extremely flat surface. So, when you got a high pin count BGA device like this, it's it's very important, in fact, it's vital to use gold because if

**Dave Jones:** you use solder or tin coated board, sure they can air level them, which is what's called hot air leveling on on a copper on a tin finish, it's going to be nowhere near as flat as this. So, it's very important for solder

**Dave Jones:** mask layering and for for the tolerances when the balls go on there and it and the solder reflows. So, I'd recommend even for simple boards, gold plate doesn't cost that much extra. I'd recommend you get gold plate. I use them

**Dave Jones:** on all my personal boards as well. Costs a few cents extra. Now, there are going to be times when well, you just can't panelize a board. One example of this is my micro watch board, which because it it sits on your

**Dave Jones:** wrist and the board is exposed, you can actually see it. I I wanted really nice cleanly routed edges. I didn't want to have to V-groove it and then file them off to get a nice edge. That sucks. So,

**Dave Jones:** I got them individually routed. So, this is what's called supplied loose or individually routed from the PCB supplier. And that's great if you want beautifully uh milled and machined edges. And that's okay. If you have to just do

**Dave Jones:** an individual board like this, it's it's fine. They can What the PCB assemblers can do, they'll charge you for it though, is they'll make up a custom little carrier module that's you know, routed to the shape of your board and

**Dave Jones:** they will actually mount them in that. There'll be an extra tooling cost but it might be worth it if you want a beautifully routed board. Now, I'm sure everyone recognizes this. It's the Arduino. Now, did the Arduino guys actually get these assembled as

**Dave Jones:** individual boards or did they actually panelize it and snap it out later? Well, there's a couple of telltale signs. All you got to do is run your finger along there and you can tell it's as rough as guts. That means it's been V-grooved and

**Dave Jones:** snapped out on all four sides. And if you actually get in there and take a look at it, it might be hard to see it but it's actually a V It's It's actually a V-shaped edge on it. You can see where

**Dave Jones:** it's been V-grooved and snapped out but this bit over here has been routed. Check it out. That's smooth as a baby's butt in there but it's rough up here. So, they routed out that little bit, V-grooved everywhere else. There you go.

**Dave Jones:** Okay, now let's actually take a look at a board. Now, assume this is your design, okay? You've got it finished and you're proud of it and it's lovely and it looks great in 3D mode. Check it out. There we go. It does everything you

**Dave Jones:** want. Now, uh what you have to look for is that A, we talked about this before, you've pulled back the uh the copper from the edges of the board, okay? Very important uh for when you do V-grooving cuz we're going

**Dave Jones:** to V groove this design because it's a nice uh square uh board. So and we don't need uh fully routed nice clean edges. We're happy to just V groove it, okay? So what we do is we flip it over to our panel

**Dave Jones:** and we do a separate This will usually be a separate uh PCB and you've duplicated this board multiple times. Now this is Altium Designer. It'll automatically uh do this for you. You can actually place multiple designs. But as you can see we've created a panel

**Dave Jones:** size here. We've created uh tooling strips top and uh bottom and we've actually uh put in the tooling holes. There it is. It's a 3.2 mm hole as you can see. We've created the fiducial here like this which is basically just a pad

**Dave Jones:** um with a uh This one has fiducials top and bottom but it's a pad um that just has the solder mask expanded on it. So if you go into 3D mode here, let's check it out. It all looks really groovy and you can see

**Dave Jones:** that the uh copper has doesn't touch between boards like that. So there's enough room to actually do the uh the V grooving in there and you can actually see that the fiducial looks like a real fair dinkum fiducial. It's

**Dave Jones:** got the gold um plated pad in there with the solder mask expansion. So that will provide a nice high contrast. There's the uh tooling holes up there and it all looks very good and panelized. Now if we go back to 2D mode, what you do is you

**Dave Jones:** actually create um you actually create a separate uh Well, I I call it fab notes but you can call it anything you like. A separate layer that just has uh the particular tooling information you want. In this case you just put a

**Dave Jones:** line in there that shows I want V-grooving all the way down there, and I want V-grooving across the middle like that. And it's easy. And the manufacturer will just interpret that. It's not actually part of your board layout, but it'll appear on the Gerber

**Dave Jones:** files, and that gives them the information they need to manufacture this panel with V-grooving. Now, an often overlooked aspect of board design, it's not just a panel base, but for any board, but particularly when you're going to manufacture, is you want

**Dave Jones:** good solder mask expansion around in your pads. Now, this is a standard quad flat pack 44-pin microcontroller with a reasonable pin pitch. But, let's go to 3D view here. And what you want, there's the chip, and you want the

**Dave Jones:** solder mask expansion between these pads. You want You don't want this solder mask in here, this little slither of solder mask so thin that it actually disappears when they go to manufacture it. There's a minimum width it needs to

**Dave Jones:** be, and that's probably about four or five thou before it starts becoming unusable and it breaks. If you don't have solder mask between your pins, you end up You can get shorts easily on your pins. So, you want a reasonable distance

**Dave Jones:** of solder mask. It's very important to check this before you send your boards out to be manufactured and then loaded. Now, as you can see here, we've actually got an expansion of 1.5 thou on or 1.5 mil as it's called, 1.5 thou on the

**Dave Jones:** solder mask expansion, and that's what we get here. Now, we can actually go in there and actually measure that distance between the measure that solder mask width in there. And as you can see, it's 5.5 mil. So, this one is more than adequate to be

**Dave Jones:** manufactured. That will be no problems at all. We get good um mask between our individual pins and we shouldn't get shorts. Um there's a very low likelihood of getting shorts on those pins. That's what you want. So now you've finished your panel

**Dave Jones:** design, it's all fantastic, you've got your tooling scripts and dooshals and la-di-la-di-la. You've got it all. What do you do? Well, you've got to supply the correct files to not only the bare board manufacturer, but to the PCB

**Dave Jones:** assembler as well. Let's take a quick look at that. Okay, so we've created our PCB panel. Now let's generate the Gerbers. Now, as you can see, I'm going to generate this is only a two-layer board, so I've got

**Dave Jones:** the top overlay, I've got the top paste uh mask, which will go to the assembler. It won't You don't have to send that to the PCB manufacturer, they don't care about the paste. Uh you've got the top solder mask, top layer, bottom layer,

**Dave Jones:** bottom solder mask, bottom paste, bottom overlay, if you've got an overlay on the bottom of your board. I uh actually create a separate uh mechanical layer for the PCB boundary. That's just the outline, the outer outline of the board, and I've got the

**Dave Jones:** fab notes, as I said before. Now the fab notes can include all sorts of stuff about the detail of board, like it's 1.6 mm FR4 and you want gold plate and ya-di-ya-di-ya-da and tented vias and all that sort of stuff. But this uh fab

**Dave Jones:** notes only just has the V-groove information cuz I'll supply a text file with all that other information separately. So we'll just generate uh some Gerbers there. And bingo, it's done. Here it is. And there is There's our Gerber information. So

**Dave Jones:** it's got These are all supplied as separate layers. So here we go, it's generated all of the layers. This shows them all overlaid, but as you can see, it would do it separately. There's that separate V-groove thing I showed you before.

**Dave Jones:** Here's the origin marker down the bottom. That's the reference origin and these are the different layers. There's my board outline, there's my uh PCB that's the top and sorry, the bottom solder mask, and and that's the paste file, but that goes to the assembler,

**Dave Jones:** and there's the overlay, and there's the top solder mask, and the bottom layer, and so forth. So, as you can see, it just generates information for the panel so that the manufacturer knows what to do. They know you want V-grooving all through that

**Dave Jones:** board. And it's the same thing if you do routing. Now, there's one other thing that you have to supply to the PCB manufacturer. We've done the Gerber files, but you need to supply the NC drill files. Now, let's just generate those.

**Dave Jones:** And bingo, they're done. And there they are. There's all our different holes used in our design. As you can see, some of them are actually slots there, but others are these are supposed to be square. They It doesn't

**Dave Jones:** render properly, but that generates industry standard NC drill file, which goes along with your Gerbers, and that provides all the information the manufacturer needs in terms of drill sizes, how many drills, and where to drill them. And of course, there's one vital thing

**Dave Jones:** which the assembly house is going to need, and that is the pick and place files to know exactly where to put what component. So, we can generate pick and place files here. Let's do it as a text file. And here's the pick and place file

**Dave Jones:** which is generated. This is a text one. It can be a CSV or other formats as well. Manufacturers will can pretty much accept anything you give them. Here's the designator down in this column down here, and then we've got the footprint,

**Dave Jones:** and then we've got the actual location of the component relative to a particular reference point, which is usually the bottom left-hand corner, but it doesn't always have to be. And this is the file that the manufacturer needs to feed into their pick and place

**Dave Jones:** machine to assemble your board. And of course, you would also give the assembler the overlay diagram as well, showing where all the parts go with the reference designators. And also an important thing to also give them is a

**Dave Jones:** physical sample of the board, exactly how you want it built, cuz they aren't mind readers. Usually, they do a pretty darn good job. They do know what they're doing, but nothing beats them actually having a real physical sample in their hands that

**Dave Jones:** they can actually compare the board when it comes off the machine or when they're loading and setting up their machine. And after having gone through all that information, you can just say, "Well, I don't want to do that. Just give your

**Dave Jones:** board and just the Gerber's for the individual board, your bill of materials, everything else to the assembly house." And some assembly houses will do all that panelization and everything else, the fiducials, the tooling, and the pick and place, and all

**Dave Jones:** that for you. It's called a turnkey solution. They will take just your individual board, and you don't even have to send them the components. You don't have to worry about the reels and all that sort of stuff, getting them in

**Dave Jones:** tubes, trays, and quantities. You just say, "I want a thousand of these, please." And they'll go, "Yes, sir. No problem." But, they'll charge you a lot more money for it. And you also don't keep individual control like when you do

**Dave Jones:** your own panel and you do everything yourself. You supply the parts. They might get the parts from the gray market. Who knows? So, just something to watch out for. You can get the assembly houses to do the whole shebang, but

**Dave Jones:** whether or not you want to, I don't know. It's up to you. So, there you go. That's a pretty much a quick overview of how to design your product for high-volume manufacture. And there's more that goes into it as well.

**Dave Jones:** There's more smaller little things which are applicable to niche designs and stuff like that, but the golden rule is talk to your PCB assembler first before you go and design your panel and everything else. Because you might put

**Dave Jones:** all the money buying your components and designing your board and then find oh, might find it hard to get an assembler or the assembler you like to do your board. So, just be careful and you will probably have to do a second spin as

**Dave Jones:** well or a third spin of the board. It's not uncommon whatsoever. So, just budget that in. You're not always going to get it. Even the professionals don't always get it right the first time. Catch you next time.
