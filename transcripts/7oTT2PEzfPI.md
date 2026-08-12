---
video_id: 7oTT2PEzfPI
title: EEVblog #248 - LCD Enabled Microcontroller Selection
url: https://www.youtube.com/watch?v=7oTT2PEzfPI
source: youtube-asr
timestamps: {"0": 0, "1": 29, "2": 40, "3": 53, "4": 85, "5": 100, "6": 113, "7": 124, "8": 134, "9": 143, "10": 156, "11": 173, "12": 185, "13": 197, "14": 209, "15": 238, "16": 261, "17": 270, "18": 282, "19": 293, "20": 307, "21": 321, "22": 333, "23": 344, "24": 357, "25": 369, "26": 381, "27": 394, "28": 417, "29": 435, "30": 454, "31": 472, "32": 490, "33": 500, "34": 523, "35": 535, "36": 545, "37": 558, "38": 569, "39": 584, "40": 599, "41": 616, "42": 622, "43": 636, "44": 652, "45": 665, "46": 679, "47": 691, "48": 705, "49": 720, "50": 733, "51": 745, "52": 769, "53": 782, "54": 799, "55": 814, "56": 839, "57": 855, "58": 876, "59": 892, "60": 919, "61": 932, "62": 945, "63": 960, "64": 977, "65": 994, "66": 1009, "67": 1022, "68": 1036, "69": 1057, "70": 1073, "71": 1091, "72": 1105, "73": 1118, "74": 1135, "75": 1161, "76": 1184, "77": 1196, "78": 1212, "79": 1225, "80": 1235, "81": 1254, "82": 1267, "83": 1279, "84": 1296, "85": 1311, "86": 1325, "87": 1334, "88": 1346, "89": 1372, "90": 1396, "91": 1408, "92": 1420, "93": 1435, "94": 1456, "95": 1478, "96": 1492, "97": 1506, "98": 1518, "99": 1528, "100": 1546}
---

**Dave Jones:** Hi. I know there's quite a few people out there who like watching me do these parametric design searches and component selection and things like that. And I was just working on a little project where I needed a couple of three-digit LCD seven-segment LCD LCD display just little PCB mount ones and I needed a microcontroller to actually drive those because if you know about basic seven-segment LCD displays, I'm not

**Dave Jones:** talking about the dot matrix ones here, but the individual segment ones like you get in your wristwatch or or calculator product or something like that, you need special LCD driving circuitry to actually drive all those segments.

**Dave Jones:** So, I thought I'd just show you some parametric searching here on Digikey searching for the LCD and a suitable microcontroller and see if there's any traps in here. So, let's go.

**Dave Jones:** So, let's type LCD into our Digikey search engine here and I can use other sites. I just prefer Digikey at the moment. You can use Mouser or Farnell element 14 or other ones Jameco or something like that if you really want to, but let's go into We want LCD modules LCD OLED character and and numeric and we want Basically, I'd be happy with anything from say a four and a half I only need a

**Dave Jones:** three-digit one, but I'll search up to say four and a half digits and this parametric column here number of digits. So, let's go like that. Let's select from three through to four and a half digits and as a first pass.

**Dave Jones:** So, we apply our filter there and how many have we got? We've got 38 uh 38 entries for that. So, what we'll do is we'll sort by price because once again, big driver is always sorting by price.

**Dave Jones:** So, I'll do by part quantity as a 100 and bingo, it's re-sorted those LCDs and then the cheapest one up there is a Lumex one by the looks of it.

**Dave Jones:** So, let's take a look at that. It's a dollar 61 each in 100 of quantity. Okay, not too bad. The others sort of jump up to $2 uh range over here.

**Dave Jones:** Yeah, okay. So, that's a pretty good uh pretty good price range there. I'm pretty happy with that. So, let's go in and have a look at that one. It's a DIP uh package like this.

**Dave Jones:** So, it's you know, it's you can mount it on the PCB and that should be fairly nice for my needs. So, let's go in and have a look at the um well, how many uh segment Well, we'll find out that.

**Dave Jones:** Let's open the data sheet, shall we? Let's go in and go straight to the Lumex website and here's your data sheet for it. And uh as you can see, one of the important things you need to note about these segment LCDs is how they're actually uh configured.

**Dave Jones:** Now, this pin table uh arrangement you've got in here, let me zoom in on that and uh you'll see that this is a look this looks like a single common uh chip because here it is.

**Dave Jones:** It's they've arranged this uh a bit weird, this table. It should just be in one big long thing, but they've got three rows there with the pin numbers 1 through 24.

**Dave Jones:** It's a 24-pin device and you'll see pin number one is com. So, how this display operates, it's got the one common terminal for all of the segments and then a separate pin for each one of the segments.

**Dave Jones:** So, each one of those um seven segments there will have its own pin and there's only one common terminal, but not all LCDs uh will operate like that. They might be they might have multiple common terminals and that's important when you go to select uh your LCD driver chip as we'll um see or your or your microcontroller, that's designed to drive um that has a built-in LCD module that's designed to drive

**Dave Jones:** these LCDs. It's got to not only support the number of segments, but also the number of commons as well. So, when we go if we're happy with this LCD, we would go and search for a microcontroller that has LCD capability that has at least one common terminal, supports at least one common terminal, and up to uh 20 Well, actually 23 uh segments.

**Dave Jones:** But uh once again, maybe if you don't need the uh decimal points or something like that, then you could uh eliminate one that maybe only had say uh 21 or 22 segments.

**Dave Jones:** Um and that could be a big driver if you're looking for say a 44-pin microcontroller or something, they may not be able to support the number of common segments you've got.

**Dave Jones:** But anyway, um that looks like not a bad uh uh LCD at all. But uh let's go and have a look at some others here. Let's go back, and uh that's a three-digit display.

**Dave Jones:** Maybe if we went for a uh verytronics one here, that's a four-digit uh display. What have we got? We've got another verytronics one. Let's go in and have a look at this one here.

**Dave Jones:** What does it cost? $2. Okay. Let's go in, have a look, download the data sheet for it. Thankfully, the internet works reasonably quickly. I said well, almost didn't get away with saying that.

**Dave Jones:** Uh you'll notice that this one has um it's a three and a half digit, but it's got the plus minus uh as well. It looks like it's got a little arrow up the top as well.

**Dave Jones:** So, um you can get all these um LCDs coming all sorts of weird and wonderful uh configurations. And you'll notice that this one is also um just a single uh that by the looks of it.

**Dave Jones:** Now, the other thing to consider when you're looking at LCDs like this is whether or not it comes in what type it is. Now, it's got display type up here and this is twisted pneumatic, but that's not what I'm talking about about.

**Dave Jones:** That's more the That's more the actual technology used to manufacture it and used to display it. But, the display type I'm talking about is this reflective type and the transflective type.

**Dave Jones:** And the difference between the reflective one is if the reflective one will not work with the backlight. It means it's got a silver mirrored like reflective back in underneath the segments.

**Dave Jones:** So, you're relying on external light to bounce back off that mirror and and come back to you. There's no ability to put I generally no ability to put a backlight on those.

**Dave Jones:** So, maybe you can get like an edge lit backlight or something like that perhaps, but you actually can't get one behind the surface of the segments. And these are really good if you don't want a backlight and you want the highest possible contrast the highest possible readability in you know in like a daytime type environment.

**Dave Jones:** Whereas the transflective type here, that will um they will actually as the name suggests it's trans reflective. So, it it's semi reflective. It does sort of reflect, but not as good as the true reflective one, but it also allows light to come through from the back.

**Dave Jones:** So, you can actually put a backlight behind it. So, if you do want to integrate a backlight, a transflective type may actually be better for that purpose. And you'll notice that this particular model number Lumix one actually comes in two types and the TR at the end and the TF.

**Dave Jones:** One's reflective, one's transflective. So, you choose the best one based So, we'll just go back here and we'll back to the main selection uh screen up here, and we'll actually choose one that has um more uh digits.

**Dave Jones:** We'll choose one of these 14-segment ones. So, we'll actually reset that, and instead of a seven-segment display, we might have a look at one of these 14-segment ones, cuz then you can get um alpha uh type ability, not just uh numbers on there as well.

**Dave Jones:** But, there you go. That's uh $2.92. There's not too many of them, but here's one in a 100 off. It's $1.82. It's not too bad at all. And that's actually an eight-digit uh 14-segment display.

**Dave Jones:** So, that's quite capable. And maybe um in my product, I might be able to integrate uh both displays into the one if I used this um eight-character display. So, it might actually be uh work out cheaper instead of buying two uh three-digit ones, might be able to buy one of these uh eight-digit ones, and have uh 14-segment uh capability as well.

**Dave Jones:** So, let's go in and uh see if we can find the data sheet for this thing. Product photos, catalog drawing. And no, but that's what it's That's what it looks like.

**Dave Jones:** They're going to be the characters. Um as as you can see, instead of your standard seven-segment, it's actually got that uh 14-segment, also known as a starburst uh type display as well.

**Dave Jones:** And with those, you can display uh letters as well as uh numbers and other uh symbols, which is really quite neat. But, I don't seem to be able to get the data sheet for this one.

**Dave Jones:** Well, just for a bit of a change, I'm going to actually search uh Mouser here, and uh type LCD into here, and we'll go into LCD displays. They've got 4,040 of them.

**Dave Jones:** I'll just see what they've got. They might have uh something slightly different. We'll go into LCD displays. We don't want modules. We don't want drivers cuz our we're going to have a microcontroller to drive this thing and we want a numeric display, not a character-based display.

**Dave Jones:** So, we'll click 361 of them and let's uh once again select number of digits from 3 to say 4 and 1/2. Let's apply that filter and see what we get.

**Dave Jones:** We get 79 matches and then what we'll do, we've got our pricing column here. We'll sort via ascending price. So, we want the cheapest first. Um unfortunately, it's not unlike unlike the Digi-Key one, it doesn't let you um put in a quantity.

**Dave Jones:** Say, you know, I want the price for 1,000 and up or 100 and up. Um but at least it does give you the price uh breaks in the column here.

**Dave Jones:** And woah, look at this first one. There's no photos, but in 100 of quantity with 95 cents. Woah. Now we're talking. Transflective available in reflective, it's a Lumex one.

**Dave Jones:** Again, it's the S401 instead of the S301. And there's that same S301 that we had before from Digi-Key. And it looks actually a bit cheaper from Mouser there. There you go, $1.30 in 50 of uh quantity, $1.27 in 50 of quantity down in there.

**Dave Jones:** But let's go and have a look at this one up here. They've only got 89 in stock. Not a huge amount of stock for the transflective one there. Um and they've got uh non-stock here, a lead time of 9 weeks.

**Dave Jones:** Ouch. For the uh reflective type, so you'd have to be careful to design if you wanted to design that one in, uh you'd have to be very careful about uh stock and things like that, looking for alternative supplies.

**Dave Jones:** This one down here, which we've been uh playing with, no problems at all. There's 1,197 in stock, 4,333 of the reflective um type. So, there's quite a big difference.

**Dave Jones:** Anyway, I want to go in and I want to look at the data sheet for this top one up here, the bingo, the LCD S401. There you go. It's only got It's through-hole once again, but it's only on one side.

**Dave Jones:** Very low pin count, which means it's probably going to multiplex the commons or it has to. Let's go right down. Look at the display here. It's uh got megapascals, kilopascals, uh PSI.

**Dave Jones:** So, um obviously this is like a a one designed for um some sort of pressure gauge or something like that. But, if you didn't want to use that, you could just start disable those segments, of course, not not drive them and use it as a four-digit uh display.

**Dave Jones:** No problems at all all as long as it met your uh size requirements. And here we go. Here's the pinout table, and this is what I'm talking about. There you go.

**Dave Jones:** COM0 there. Once again, pin numbers 1 through to 13. And uh common zero, common one, common two, and common three. So, it's got four common pins. So, if you want to drive this display, you, as we'll see later, you'll need a microcontroller that can drive up to a four common segments with up to um uh what have we got?

**Dave Jones:** 1 2 3 4 5 6 7 8 9 uh segments. So, you need four commons by nine segments to drive this display. And it's a very attractive uh price point for that one.

**Dave Jones:** But, well, I think just for uh argument's sake, we'll go back to this one here. It's a safer uh choice, and we'll try and find a microcontroller that has a single common and can support up to 23 segments.

**Dave Jones:** So, in Digi-Key here, we'll type in microcontroller. We're going to be very broad. I could go to the direct to the manufacturers if I was a Microchip fan boy or an Atmel fan boy or a TI fan boy, I could go directly to their websites and do parametric searches there, but I'm not too fussed about the brand.

**Dave Jones:** So, I'm going to go in and search 32,000 different microcontrollers here. There it is. 32,651 of them. And I'm going to try and use the parametric search. Now, the problem with this is you're not always going to get it right because Digikey may not always capture the correct um uh information in the peripheral column here for the chip.

**Dave Jones:** So, you could miss out um on the odd device, but I need to go through. Unfortunately, there's no column where I can just select LCD. So, I've got to go through and look for any one of these that actually have LCD in them in the parametric search.

**Dave Jones:** So, I go through da da da LCD LCD and this all means it'll have an LCD module in it. And uh we should It's a bit tedious. So, I might skip through this part and I've tediously selected all the ones through there.

**Dave Jones:** So, that have LCD in them and you cross your fingers that Digikey have done their jobs. The Oompa Loompas at Digikey have imported all this data correctly and we've got 2,306 microcontrollers of all of these different manufacturers.

**Dave Jones:** Atmel, Cirrus, Cypress, and Energy Micro, Freescale, Fujitsu, Maxim, Microchip, blah blah blah blah blah, Renesas, Sharp, Micron, ST, Toshiba, Zilog, it's all there. So, no shortage of manufacturers who make microcontrollers with LCD drivers in them, but we care about A, the price and B, that it supports the number of digits we're after and we need a couple of other features.

**Dave Jones:** I want an ADC built in, a couple of channels, say, you know, two or three channels of ADC would be nice as well, well, pretty essential, actually. So, what we'll do is we'll search for price over here and unit price.

**Dave Jones:** Let's do say 100 of, which is a nice sort of round value to give you an idea for sort of, you know, short run prototypes or first run prototypes.

**Dave Jones:** And what have we got? Uh first up, it looks like the cheapest one we've got here is a Freescale RS uh 08, but will that have the number of IO required number of IO 26?

**Dave Jones:** Well, I know for a fact that it's not going to do it, so we actually need um probably up here to search for a higher number of IO, cuz we need at least 23 uh segments plus the uh pin as well.

**Dave Jones:** So, if we go up, so we need it. So, there's 24 pins right there that we need. So, let's start from say 30 upwards uh cuz really if we you know, max out at say 102 or something like that, I don't want a device that big.

**Dave Jones:** It'll probably be overkill and too expensive, but we've narrowed that down even further, and let's do our um uh well, our price search is already there, and the first one up the top is a PIC16F19 34.

**Dave Jones:** So, there you go. The cheapest one on the market, according to Digikey, cheapest microcontroller you can get. Too bad if you're an Atmel or a TI fanboy, sorry. Um yeah, they're not even don't even register on the first page.

**Dave Jones:** If we go to the next page, they're PICs, PICs, PICs. Uh we get just get into an NXP there. There we go. That that would um LPC, it looks like an ARM uh device.

**Dave Jones:** It is. It's a 32-bit ARM Cortex M0. How much does that one go for? That's a whopping $3.00 and $0.13. Thank you very much. Massively expensive compared to if we go back and go back, we've got our 16LF Oh, sorry.

**Dave Jones:** Let's go forward. Our 16F1934 there is only a $1.68. What a bargain. So, let's go in and take a look at that. I really want that sucker. And let's go in and have a look at the product brief for it.

**Dave Jones:** And PIC PIC16F1930X device, presumably just different memory features. Yes, here it is. The 1934 has 4K of program memory, 256 bytes of EEPROM. I didn't mention that. I will need some EEPROM, I think.

**Dave Jones:** Um 36 I/O, uh which should be enough. And bingo, over here. This is what we care about, this column over here, the LCD segments and commons. As you can see, ah perfect.

**Dave Jones:** Supports up to 24 segments with four commons. So, we could drive four of those displays we've been looking at with this one $1.60 in 100 quantity PIC chip. Awesome.

**Dave Jones:** I love it. It's got It's got I²C, UARTs for 8-bit timers. And once again, it's got 14 channels of 10-bit analog-to-digital converter. Heaps. So, there's no reason why we can't use that.

**Dave Jones:** Or is there? Now, as I'm sure I've mentioned before, one of the traps with using and selecting microcontrollers like this is that a lot of or most of the functionality of these devices like the else all the built-in peripherals, the LCDs, the the timers, the ADCs, and the I squared Cs, and all the peripherals and things like that, PWM outputs, capture compare modules, comparators, whatever.

**Dave Jones:** A lot of them share uh pin functionality. So, you can't use both of them. Often, you can't use two competing things at the same time. So, we might this thing might very well Well, I guarantee you it'll be able to drive these 24 segments at up to four displays, but do those pins map to some of the analog to 14 analog to digital channels that we want to use?

**Dave Jones:** So, if they do, we're screwed. We won't be able to do both. If those If we want to use an I squared C port, for example, are those I squared C interface pins overlapping our LCD segments?

**Dave Jones:** It's very likely, but um you know, odds are you're going to get a couple of analog to digital convert converters which don't share the same pin. So, really um that's my main requirement moment, I think, is my analog to digital converters and the LCDs.

**Dave Jones:** They've got to be separate. So, let's go down and see if we can actually find the pin mapping information. That's the 28-pin device. We don't want that. We're going to be using the 40-pin Oh, it comes in a There you go.

**Dave Jones:** It comes in a PDIP package. But I'm was pretty sure the Digikey one is Yep, a quad flat pack. Probably can get it in other packages, perhaps. I don't know.

**Dave Jones:** 40-pin DIP No, UQFN. No. Looks like Digikey aren't going to stock that sucker in at least not in this price range, anyway. The the DIP 16 19 37. Anyway, let's not muck around with that.

**Dave Jones:** Let's have a look at the pin allocation table, cuz that's going to tell us everything we need to know. And here we go. This is the 40/44 pin allocation table for the 16F1934.

**Dave Jones:** And you're going to choose your right device, and it can get complicated. And here's the column we want here, the LCD uh column, and once again, the segments, it tells you which pins over here, the RA0 pin is segment 12, for example.

**Dave Jones:** Um and we go through, and there's some various uh LCD voltage uh pins as well that it requires. So, let's see if they interfere with our analog to digital column.

**Dave Jones:** Here's our analog to digital column down here, and as you can see, segments, they overlap. I Okay, no, I I N4, segment 5, I N12. Uh-oh, this ain't looking promising.

**Dave Jones:** Um well, hey, no, look, there we go, com 1. We're not using com 1, so we could get one analog to digital channel on RB5, pin RB5 there, which is analog channel 13 on com 1.

**Dave Jones:** So, if we're No, sorry, we're going to drive two displays. Well, I could use one of the other common pins. Okay, I don't have to use com 0 and com 1.

**Dave Jones:** Could actually use com 0 and com 3, I guess. So, um looks like we might be able to squeeze out an analog pin there, but the others uh mapping the segments down here.

**Dave Jones:** And if we want our decimal points, there's segment 23. If we want both decimal points, oh, we're struggling. Maybe if we dropped one of those decimal points, if we didn't if we only needed the one fixed decimal point, and we can might be able to squeeze out a second analog to digital channel, AN7 on pin RE2 there, but that's it.

**Dave Jones:** What do you know? Murphy screws us around again. It ensured that almost all of these analog to digital converter pins were mapped to the LCD pins. And that I think that's going to have to rule out this device right there cuz I really wanted um uh probably three uh analog-to-digital uh converter um channels there.

**Dave Jones:** So, really ah not that happy with that at all. We might have to scrap this device right there. Let alone looking further into if you want uh PWM outputs or something like that.

**Dave Jones:** Here's our capture compare module, CCP3 capture compare um uh modules there. And you'd have to look to see if they correlate to the LCD pins. But, that's that's really tricky business.

**Dave Jones:** As you can see, just uh selecting the right device unless we completely go overkill and we get like a 100-pin device or something, then you're yeah, you're almost guaranteed that you're going to get the functionality you need on that.

**Dave Jones:** But, I think we're going to have to rule this one out perhaps. What a bummer. But, that's the detail. If you rushed in and bought some of these devices based on just the uh you know, the based on the feature set um up here and that yeah, it has all these segments and meets all my specs, rushed out and bought that, designed that into your product, into

**Dave Jones:** your board, then well, you could find yourself uh yourself up the uh proverbial creek without a paddle. So, I won't bore you with the details of actually going through and trying to find the correct microcontroller here because it could take all day and I've got to go back and check my specs and see which ones are a little bit flexible here and there, what my uh sort of toss around my price targets,

**Dave Jones:** what they're going to be and things like that and sort of trade a few things off perhaps. And yeah, it will literally could take all day or several days just to do this and select the correct uh microcontrol microcontrol for this particular product.

**Dave Jones:** And this is And I hope you can appreciate this. This is only for two the detail that we've had to go into here for just two simple parameters like LCD and ADC trade-off versus price at a low price point.

**Dave Jones:** Imagine if you're trying to, you know, juggle five different peripherals you need built into your um microcontroller. You can't just choose the top of the range one cuz you're trying to meet a price target and maybe a pin target as well.

**Dave Jones:** You don't want to use a, you know, a huge couple hundred pin device or a BGA device which requires you to have a an a different assembler who can handle that pitch BGA.

**Dave Jones:** You know, if you choose one of those um uh those cheap integrated arm devices or something. Well, it's a big can of worms. I just uh thought I'd show you that just this simple case and how, well, things aren't always as they as they seem with microcontroller selection.

**Dave Jones:** Anyway, I might have an update uh on this project in the future, but until then, catch you next time.
