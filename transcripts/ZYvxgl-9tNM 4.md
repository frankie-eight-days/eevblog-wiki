---
video_id: ZYvxgl-9tNM
title: EEVblog #1055 - How to Design a Custom LCD- µSupply Part 16
url: https://www.youtube.com/watch?v=ZYvxgl-9tNM
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 29, "3": 42, "4": 60, "5": 77, "6": 89, "7": 106, "8": 116, "9": 134, "10": 145, "11": 159, "12": 171, "13": 189, "14": 200, "15": 211, "16": 226, "17": 237, "18": 251, "19": 263, "20": 273, "21": 283, "22": 299, "23": 310, "24": 322, "25": 334, "26": 346, "27": 357, "28": 370, "29": 382, "30": 399, "31": 409, "32": 419, "33": 443, "34": 453, "35": 464, "36": 491, "37": 509, "38": 525, "39": 542, "40": 552, "41": 573, "42": 589, "43": 602, "44": 617, "45": 627, "46": 638, "47": 649, "48": 667, "49": 679, "50": 691, "51": 708, "52": 719, "53": 729, "54": 745, "55": 758, "56": 773, "57": 782, "58": 795, "59": 805, "60": 822, "61": 834, "62": 846, "63": 861, "64": 871, "65": 889, "66": 898, "67": 914, "68": 934, "69": 952, "70": 965, "71": 982, "72": 991, "73": 999, "74": 1016, "75": 1033, "76": 1048, "77": 1063, "78": 1079, "79": 1091, "80": 1105, "81": 1115, "82": 1126, "83": 1137, "84": 1155, "85": 1169, "86": 1180, "87": 1201, "88": 1215, "89": 1232, "90": 1245, "91": 1258, "92": 1271, "93": 1286, "94": 1296, "95": 1314, "96": 1324, "97": 1345, "98": 1354, "99": 1362, "100": 1384, "101": 1394, "102": 1408, "103": 1415, "104": 1432, "105": 1444, "106": 1455, "107": 1480, "108": 1491, "109": 1506, "110": 1516, "111": 1530, "112": 1541, "113": 1550, "114": 1561, "115": 1576, "116": 1587, "117": 1595, "118": 1605, "119": 1617, "120": 1631, "121": 1643, "122": 1653, "123": 1671, "124": 1686, "125": 1701, "126": 1712, "127": 1732, "128": 1742, "129": 1755, "130": 1766, "131": 1777, "132": 1784, "133": 1794, "134": 1802, "135": 1815, "136": 1825, "137": 1841, "138": 1857, "139": 1868}
---

**Dave Jones:** Hi, this is the next video in a series of videos on LCD technology and designing in this particular case designing a custom LCD display. In previous videos here we've looked at just LCD technology overview in general and how to drive different types of LCD.

**Dave Jones:** So that'll be linked in at the end of this video and down below if you haven't seen that. But today we're going to have a look at what it takes to design effectively your own custom LCD like this.

**Dave Jones:** In this particular case this is for the new micro supply. Yes, we are working on it again and we're going to design our own custom LCD. Won't necessarily go into the reasons why it's just because we can and we like it.

**Dave Jones:** It's good enough reason and they're cheap. So there's various reasons why you might want to design your own LCD and rather than using off-the-shelf one like a dot matrix LCD or a dual line character based display or something like that.

**Dave Jones:** So in this case we're going to design a fairly complex LCD like this. By complex I mean it's actually got a lot of segments in there and basically as we'll come to see the number of rows and segments dictates not only how complex the LCD is but how complex the LCD driver is as well.

**Dave Jones:** So let's take a look at it. Now I'm kind of actually jumping the gun on this video because I don't actually have an LCD to show you. We haven't actually had this one manufactured yet.

**Dave Jones:** So this video is more about what it what is involved in just specifying up an LCD and then choosing a manufacturer and fingers crossed in the end it's going to work and we'll show you that in a future video.

**Dave Jones:** Now I'm not actually going to recommend a particular LCD manufacturer in this case. I may not even say who we're actually going to get ours manufactured with. It doesn't really matter.

**Dave Jones:** They're just dime a dozen. I mean, just go into Google and type in custom LCD manufacturer and you'll find like a ton of them. And if you go into say Alibaba and just you know, custom LCD, something like that, I'm sure you'll find Here we go.

**Dave Jones:** Custom LCD manufacturers. You go online, talk to them and they'll basically give you a quote on the spot if you've got all the relevant information available. The size, the number of segments and what type you want and things like that.

**Dave Jones:** So, like it's just no shortage of choices. And like from one of the first ones on Google here, I don't recommend them, but this is some well one popped up and they do all sorts of different custom size.

**Dave Jones:** We've got COG, they do OLEDs, they do character-based ones and dot matrix ones, all sorts of custom, almost anything you need for a custom LCD. Tell us the price, son.

**Dave Jones:** All right. This is by far not the lowest start price you could get. We've talked to several manufacturers. They're all in China and basically we chose one of the cheapest ones that our spidey sense told us that wouldn't you know, that could do the job for us.

**Dave Jones:** Some of them just you know, don't communicate properly. Often English language barrier and things like that can be a problem, but sometimes like they you know, if ones are asking the wrong question, do you know, you might just ditch them.

**Dave Jones:** So, this price we just have a one of a single price here that just came from a manufacturer that we were looking at and these were the basic specs that we told them.

**Dave Jones:** We need a positive reflective display, the power supply, the duty cycle, the bias frequency that we're going to we'll have a look at that in a minute, the viewing angle, you know, standard sort of temperature range, what type we want, a pin connection method in this case.

**Dave Jones:** Although we've got the others down here and just a regular black and white with that 0.1 mm uh clearance and minimum track width. And we'll uh talk about that uh shortly.

**Dave Jones:** And basically, um look, here we go. Uh unit price in US uh dollars. What was this uh quantity for, David? Thousand quantity. I thought it might be. Thousand's usually like a nice ballpark uh figure.

**Dave Jones:** And it's not breaking the bank, really. Here it is. So, uh for a regular pin-based one, which is the one that we which we're going to get manufactured, we're going to get one like just your regular LCD custom LCD glass like this with the pins on the side there.

**Dave Jones:** And uh of course, you don't have to have the pins. You can remove the pins, and then you can use the zebra strips as we talked about um in a previous video.

**Dave Jones:** And that I you might save a shave a few cents off the uh cost there if you don't have the pins on there, but it's basically the same uh glass for the pin.

**Dave Jones:** So, a dollar 47 in thousand quantity. And then, it's actually a bit of a jump. It's not usually this much of a jump, but in our case, this is what we were uh quoted, $2.36 for the FPC or the flat flex connector version.

**Dave Jones:** That's a bit strange because it's just basically uh conductive gluing a flat flex onto the glass um as opposed to putting the pins on. So, that was a fair jump to go to that flat flex.

**Dave Jones:** And then uh COG is the chip on glass, which has the LCD driver built onto it. And we could have went for that, but look at the price difference, a dollar $3.71 each quantity versus $1.47.

**Dave Jones:** And as we'll see, we'll take a look at the driver chip that we're actually going to use, and the price just doesn't justify using COG. But it may for your particular purpose.

**Dave Jones:** Depends on the manufacturer. If you don't have space on your PCB to lay um to put your driver chip, for example, especially if you got a lot of segments like we've got on this uh custom LCD, um Um, that could be a real driving price.

**Dave Jones:** Now, the tooling cost, which is a one-off uh uh non-non-recurring NRE, they call it, non-recurring engineering charge or tooling cost, um $230. You know, it's not a big deal.

**Dave Jones:** So, really, what's that? You know, a thousand under two grand for a thousand LCDs, including the tooling cost, and from this particular manufacturer, the turnaround time was uh two to four weeks or something like that.

**Dave Jones:** You probably could get like samples quicker uh if you needed to. And the flat flex one, not much more tooling cost, 285, but it was a big jump up to the chip on glass one, which was 1385.

**Dave Jones:** So, you know, if you try if you're only making a thousand widgets and you have to amortize that uh tooling cost over a thousand units, for example, then that's an extra dollar 38 per unit um bomb cost you've got to amortize over.

**Dave Jones:** So, that, you know, that could be uh fairly substantial. Of course, if you're only making a hundred of something, custom LCD, it might be it might be worth it because it's the only way you can uh get your product design.

**Dave Jones:** Like, the custom LCD makes your product. In that case, you've got uh no choice. But, generally, you know, your tooling cost might actually eat away at you in smallish volumes.

**Dave Jones:** Okay, so you've decided you want a custom LCD because it's going to make your product look more professional, gives you something that uh you can't get with a uh dot matrix LCD, gives you better viewing angle, very better contrast, or they were or you're simply trying to uh save cost, which is often a uh dominant reason and why, you know, a one-dollar watch or something, you're buying a

**Dave Jones:** little fighting novelty gadget, and it's got a custom LCD in there because in volume, they you know, they're they're cents each, really, you know, especially if you're making a hundred thousand widgets or whatever.

**Dave Jones:** So, cost is often a big driver. But, anyway, you've decided to do that, and you And the first thing you need to do is know how many segments you've got.

**Dave Jones:** And in our particular case, this is the drawing which we'll go through shortly, but basically we have uh 212 segments on this thing because we have um two four five displays of four digits each with the seven digits each plus you got the decimal points plus we've got a bar graph everything else and miscellaneous annunciators all that sort of stuff.

**Dave Jones:** So 212 segments is actually a lot. So we're basically going to have to look for a driver chip which has a uh basically uh 256 segments. But uh as we've seen in a previous video that you have to separate them into common drivers.

**Dave Jones:** So in this particular case, we basically need a chip which has eight common uh pins as they're known. And we have a pin table here to be filled in by the manufacturer as we'll explain which has um cuz we've got 40 pins.

**Dave Jones:** We just decided to have 40 pins there cuz that's enough to do all of the segments we want in an eight common by uh 32 configurations. So we need to choose a driver chip which has uh eight commons and 32 segments at least.

**Dave Jones:** So that works out to a lot of pins and this is why you might want to go to a COG display chip on glass cuz it has the driver chip built on.

**Dave Jones:** So you can simply talk to it via an I squared C bus or an SPI bus or whatever or the regular um you know Hitachi interface LCD driver or whatever you choose to In this particular case, no because we've just got the pins or the flat flex or the zebra strips, we have to drive every one of these 40 pins.

**Dave Jones:** So that becomes a problem. Now if you course if you've got a relatively small LCD, you can use your existing microcontroller that you already plan to use. Or you can choose a variant of the microcontroller that has a built-in LCD driver.

**Dave Jones:** And a lot of them do. I used it in my 121G W multimeter, for example. I chose a particular ST ARM 32 processor which had a built-in LCD driver that had the number of rows and columns that we needed.

**Dave Jones:** Now, if we go over here and have a look at uh say the ARM ARM STM32 ultra-low power MCU line, which we um happen to be using. And also uh we use this in the 121G W multimeter, as well.

**Dave Jones:** We chose a particular variant with the built-in LCD controller that had enough pins. And you can And uh what I've done here is I've sorted the uh parametric uh table here.

**Dave Jones:** You'll hear this um term a lot, parametric table. And if you don't know what that is, it just means having all these different parameters, hence why it's called parametric table, of the chip.

**Dave Jones:** You know, you've got supply voltage, min max supply current. And you can put operating frequency AD converters. And in this case, we can actually um have whether or not it's got a display controller.

**Dave Jones:** So, I've sorted by the display controller here. And you have to be careful cuz sometimes these aren't particularly accurate, these parametric searches. So, look, if you just look at this first page here, you might think that these STM ARM micros, I think that's the one we're using, the L152, one we're using on the 121G W.

**Dave Jones:** Anyway, it's got like 4 by 16 uh four commons, that's what it means. Four commons by 16 segments. Um but hey, let's just go scroll through a couple of pages.

**Dave Jones:** Aha! 8 by 28. That one there would actually do it. So, let's have a look at the next page. Here we go. It's got uh four commons {slash} 31 or 8 by 28.

**Dave Jones:** And actually, 8 by 28 would do it. Um that would do the 121 pins that we actually need. But, the problem with this is is that it may force you into a much more expensive microcontroller cuz it's got 512K of memory.

**Dave Jones:** Uh or it's got, you know, this and that. It's in a bigger package. It's got more pins. And it it could double the cost of your chip. Your micro might be $1.50, for example, the one you were looking at using.

**Dave Jones:** And then when you search for one that has the built-in LCD as well, bigger package, whatever, it might force you into another model. Or whatever, it could double the price to $3, for example.

**Dave Jones:** So, you're effectively paying in that example, $1.50 for the LCD uh controller. And uh we could actually uh find one that actually did the job for us here. Any one of these 8 by 28 ones would actually do the business.

**Dave Jones:** And probably, if you went and see the data sheet, you could choose a different package size to get that, perhaps. Um and it's the same across any any or, you know, a lot of these microcontroller manufacturers, similar sort of uh story.

**Dave Jones:** Same story effectively across them. But, you know, $1.50 extra, for example, or it could be 50 cents, whatever. But, if you can get a separate LCD controller for less than that, then you're ahead on your bomb cost.

**Dave Jones:** You're you know, you're winning. And of course, having a separate LCD controller chip can also uh have advantages in that you can physically place the chip somewhere else on the board, like actually under your LCD itself.

**Dave Jones:** So, you get a nice routing of your pins and everything. Uh you know, if they fan out quite nicely to the pins of your LCD, for example. Whereas, if you with your micro, you might need that somewhere else on your board.

**Dave Jones:** And then route And then your LCD might be up here, and your micro needs to be down here for other reasons, you know, cuz it's got the ADCs built in that you're using and you want And you you got to get all these LCD lines right across the PCB.

**Dave Jones:** Can be a pain in the butt. So, often decisions like that may drive you to use a separate LCD controller, like we've got here. In our case, it was just cheaper to get an external LCD controller than to use one built into the micro that we wanted to get.

**Dave Jones:** So, we can go over to Digikey, we can search for our LCD or Mouser or whoever your favorite parametric provider is, and allows you to like, you know, search by columns and all the different characteristics and stuff like that.

**Dave Jones:** So, we can I've already drilled down to regular segments. Well, look, we can go down. We need like at least 215 segments. So, we need at least those. Wow, 600 segments, that's huge.

**Dave Jones:** So, we can apply the filter and have a look at the chips available and they're going to be really reasonably large pin count LCDs. Now, LCD drivers. Now, here's one from NXP, for example, the PCF8545.

**Dave Jones:** That's an old Philips thing. I think old Philips part number, you know, 80 and I've sorted by price here, so lowest one first. So, it looks like the lowest one that might do the job, 80 by 4.

**Dave Jones:** No, that's not going to do it. 80 by you know, 87 cents, a dollar 40. Getting a bit pricey, but I happen to know that I they don't sell them on Digikey, but let's go over and see the display controller which we've actually chosen.

**Dave Jones:** It's actually a Holtek and Holtek manufacture little cheap like 8051 compatible micros and things like that you that you'll often find in fairly novelty toys and stuff like that.

**Dave Jones:** And they also do a range of LCD controllers here. And we're we're actually going to use the HT16 22 here and it happens to have eight coms and 32 segments and that's perfect for our eight common display here.

**Dave Jones:** And the other thing about this Holtek LCD driver is that it's quite uh reasonably priced. I think we got some uh quotes somewhere like um AliExpress, you know, you've got to wheel and deal with uh people on AliExpress, but you know, it could be as little as 10 cents in lowish uh volume.

**Dave Jones:** So, we you know, we shouldn't shouldn't pay, you know, a huge amount. So, as you saw before with the uh the cost uh breakdown of this thing, this COG thing at $3.71 a piece compared to $1.47 here, um then you know, that it's easily paid for this chip.

**Dave Jones:** 20 and 40 cents, it was pretty cheap. So, you know, considering that our um LCD only costs, you know, $1.47 in quantity once we've amortized that $230 cost, but that's not a big deal.

**Dave Jones:** Um you know, it it comes in under $2 for that LCD solution. And I know a lot of people might say, "Well, I can go on eBay and I can get a you know, a one of those old Nokia phone LCD things for a couple of bucks." Well, good on you.

**Dave Jones:** If that suits your project, fine. Do that. Um you know, more power to you, but if you want, there's very good reasons why you might want to design a custom LCD.

**Dave Jones:** As I said, the look and feel um and all that sort of thing, the view angle, the contrast, all that sort of stuff. And really in volume, it can get cheaper.

**Dave Jones:** I mean, this is not a particular particularly cheap quote. We could have got we can almost certainly get uh cheaper than this quote if we shop around. All right, so we're going to need to know several things in order to provide this information to the manufacturer so that they can give a proper quote on our custom LCD.

**Dave Jones:** So, in this particular case, uh we've got like a quarter uh this the chip that we're actually using uh uses quarter bias, eighth duty cycle, and the uh refresh rate or frame frequency of uh 64 hertz here.

**Dave Jones:** So, um then we can translate that back over to our manufacturing drawing, and this is where your manufacturing drawing comes in. We've We've kind of gone to town a little bit on this one, so you don't have to get as fancy pansy as what we've done here.

**Dave Jones:** I'm using Inkscape here. David did this one. I didn't draw this up cuz my Inkscape skills are non-existent. But, he basically went in and drew a vector-based graphics for all of these character displays here.

**Dave Jones:** And we've got a manufacturing table. It's similar to when you get a PCB manufactured. Very Very similar, and I've done videos on this about um actually providing manufacturing information in the Gerber files.

**Dave Jones:** And this is a similar thing what's going on here in our PDF manufacturing document here. We're given We've got our display area here, 50 by 54, our physical area.

**Dave Jones:** Um So, the display area is actually the glass area that they need to manufacture. The physical area allows for pins or whatnot. And we're saying we can the length that is modifiable by the manufacturer if they want.

**Dave Jones:** You know, things like that. Just give them If you give them real hard constraints, then they may actually pad the quote up because they they don't have the flexibility to do whatever they want.

**Dave Jones:** It might be harder for them. So, just be aware of that. Give them as much flexibility as you can. But, we're we're saying a nominal power supply of 3.3.

**Dave Jones:** We're saying the duty cycle of 1/8, the bias of 1/4, which I've covered in the previous video, and the frequency 54 hertz. And the viewing angle. Now, this is an interesting thing.

**Dave Jones:** This 600 bottom, this is actually kind of confusing, but it's kind of an industry standard kind of thing. Let's have a look at this. This is a Handtronix uh explanation of the LCD angle.

**Dave Jones:** And uh basically what it comes down to is are you going to Here's your product. Are you going to look at your LCD from the bottom? So, if it's lying on a table like a calculator like this, you're looking from the bottom.

**Dave Jones:** So, uh we would choose the six the 6:00 bottom position, and they work in terms of time on a clock. So, that's just how they do it. Um, so that you would specify that.

**Dave Jones:** You basically want your optimum viewing angle in the lower like looking from the bottom. But, if you're designing a rack mount thing that's sitting low or something like that, or you've you know, you're installing it uh where somewhere person might have to walk by and look down on the LCD uh for example, then you would uh specify the 12:00 top position.

**Dave Jones:** So, we're just specifying cuz our particular one we're going to be looking from that angle. Um, now you can actually adjust justice, of course, uh using the contrast. So, if you have it set to the center, you can actually use the contrast to adjust either way.

**Dave Jones:** And you've no doubt seen that on products that have adjustable uh viewing angles. You can actually adjust them above and below the plane. But, you want to specify if you know you're going to use it in particular orientation, specify in our particular case the bottom orientation there.

**Dave Jones:** So, uh that's what we've specified there. And the operation temperature range is pretty uh basic. And uh connection method, we've got FPC ribbon. We don't want that. David, we have to fix our drawing.

**Dave Jones:** We want pin. I don't think this is the final one. Anyway, um and optional including quote the COG. So, there's just some information there for the manufacturer so they have it in a document.

**Dave Jones:** You can provide this in the email or the chat with them or whatever. But, you know, it's just nice to have a the like that. And we've actually specified a pin here, and we've gone to rough pin dimensions, but just leave it up to the manufacturer.

**Dave Jones:** You don't have to include um any fancy pantsy stuff like this. Now, we've given them a table here to fill in. Uh we could, of course, specify hard specify which segment we want connected to which pin.

**Dave Jones:** Um but then it's like PCB routing. Um you can't just do it willy-nilly. You can't have one over here going like two segments over here and then go into opposite sides.

**Dave Jones:** It just screws up the routing on the uh glass cuz they base it essentially is like a PCB layout, and they manufacture these using layers just like on PCBs and the photographic method with the conductive uh paths in on the actually etched onto the glass itself.

**Dave Jones:** Now, uh so generally it's best to leave it up to them. And you don't even have to give them this table. They will simply provide you with a final table when they ship you a unit.

**Dave Jones:** Here it is. Here's your pinout. Just leave it up to them to decide which ones uh which is connected to the where based on their particular routing. And the thing is the more you know, if you've got a really tight LCD where the segments are right near the edges like on this particular one, um then they may be very constrained.

**Dave Jones:** They will be very constrained in the routing that they can do to this. So, you may not get what you asked for in that particular uh routing case. And it depends on whether the pins are at the top or at the bottom.

**Dave Jones:** That can make a heck of a difference um or whether or not you've only got pins on one side or connecting you want to come out one side depending on your system design.

**Dave Jones:** Then, you know, it it becomes quite um complicated. So, but we've basically given given them a color-coded uh chart here saying, "If you can, pretty please, um group them the commons into these particular ones." So, exactly you know, this red one up here maybe common one.

**Dave Jones:** And so, when you go to refresh the screen, uh it's easier both in software and from a visual refresh point of view to have each uh sort of group.

**Dave Jones:** In this particular case, we have these group of eight um seven segment displays that form a one number. It's better to have them in one common if you can because then your LCD can update and drive that one uh common.

**Dave Jones:** But, you know, and either way it's going to work. It's it's just uh nicer if we could have them grouped. And we're just saying if you can do that, pretty please.

**Dave Jones:** Now, we've actually um done this in Inkscape, of course, and we've given Well, we'll be able to give them an SVG uh file, a vector-based uh file. But, a lot of these um LCD manufacturers are very old school, just like a lot of PCB manufacturers are quite old school.

**Dave Jones:** And they might want a DXF uh AutoCAD file, for example. So, you may have to convert whatever format you have into DXF and actually give it to them. And really, you don't have to get as complicated as this.

**Dave Jones:** Uh you don't have to specify it precisely. You could draw it on the back of a napkin if you wanted to. And, you know, give them that and say, "Hey, make us one of these LCDs." And they'll just draw it up or whatever.

**Dave Jones:** Like, they might even, you know, touch this up a little bit, shuffle things here, you know, shave a little bit off in there because um just remember, when you're actually getting these manufactured, this segment in here, for example, you have to actually allow enough gap in between here not only to route that trace out to ensure that it doesn't touch the others, to actually route out that trace, that

**Dave Jones:** conductive trace from this inner one, but then you've got to allow the clearance as well. So, that's why we said before, typical uh spacing and uh trace width might be 0.1 mm and 0.1 mm.

**Dave Jones:** So, you know, that total in there would have to be 0.3 mm if you wanted to squeeze through a 0.1 mm conductive trace with uh that. And then you've got to of course route it out to a particular pin.

**Dave Jones:** So, you can see why if you wanted this segment here connected over to here, they're just going to we can't do it. Um you know, what do these idiots want?

**Dave Jones:** You know, they're they're just going to absolutely scream at that sort of thing. And um basically they might say they can't do it or they might have a process to do it or whatever, but yeah, just be aware routing is a big issue with uh something like this.

**Dave Jones:** And of course you can't uh just manufacture um you know, something like you couldn't have these solid segments for example. You have to have the gap between the particular segments.

**Dave Jones:** And in this case, look we've got an inverse one here. And uh and you can see how that we've uh specified this and we'll fill this in the table before we uh send it away.

**Dave Jones:** Like C N, that's the segment name for that whole thing. So, they would know that all of that content is basically the one. The M I N N is just the one particular uh segment.

**Dave Jones:** So, they wouldn't do those separately. But down here for example, with the M J W and H, they wouldn't know whether or not you wanted W and H as separate segments or whether or not you wanted uh it it as just one segment with W H.

**Dave Jones:** So, you have to specify that. So, we've specified that as four separate things there. And of course we've got like the inverse uh ones here that just give a nice high contrast.

**Dave Jones:** And on stuff like this, like uh you may be wondering, "Well, how can this in the middle of the O for example, how can they turn on that segment?

**Dave Jones:** How can they route you know, do that?" Like how do they get the trace out? Well, because it's the one segment, if you wanted two separate segments there, you might like you're screwed.

**Dave Jones:** Um but you know, they would have to have a a in there and have the trace coming out. But, because it's the same, they would simply add a very thin conductive trace in there that you couldn't see, and you get all that one segment.

**Dave Jones:** Like, it's the same over here with this battery one, for example, the little plus and minus in there is all part of that one segment. So, they just put the little conductive traces in there.

**Dave Jones:** Just leave it up to them. They are going to modify things anyway. They're going to use cuz they've got their own internal tools, their own processes, everything else. So, you can go to town.

**Dave Jones:** Um you know, on with these sorts of data sheets specifying everything, and they just might redo the whole thing. But, at least it's clear when you explain it to them.

**Dave Jones:** But, of course, one of the main reasons you might want to go to town and specify the document here and the one and the reason we've did it we we we could have told them that just told them that, "Hey, we wanted, you know, six different seven-segment displays and stuff like that." And then they would have just used their own font for the seven-segment display.

**Dave Jones:** They would have used their own font for the characters and things like that. And you may not like what they choose and produce, or you might not. So, by actually specifying it like this, they will try and get as absolute close to possible as possible to your particular font here.

**Dave Jones:** It like in theory, it should be exact, but there's going to be some translation from whatever file format you've got into their particular package. But, you can pretty much guarantee that's going to be extremely close to what you specify.

**Dave Jones:** Otherwise, if you leave it up to them, you could get the seven segments that tilt over like this, that are thin and skinny, or short and fat, whatever. It's It's nicer if you can specify it, but you don't have to.

**Dave Jones:** If you've just got a simple product you want to churn out, just leave it up to them. Draw it on the back of a packet. And the other reason you might want to specify your own one as well, like in this much detail to the manufacturer, is that you can swap manufacturers cuz they might not give you they're not they're not going to give you their in-house files for

**Dave Jones:** manufacturing this thing usually. So, you know, it's not like you can take those files and go to another house, you know, and to get the thing manufactured. They go out of business, you might you know, want to have multiple sources or whatever.

**Dave Jones:** If the more detail you put into your drawing and specify your LCD, the more chance the better chance you have of just simply going to different manufacturers and getting pretty much close to the same LCD produced.

**Dave Jones:** There's going to be manufacturing differences between them in terms of, you know, the liquid crystal technology and the twist and all that sort of stuff which goes into the technology of actually producing them.

**Dave Jones:** So, this one might have a slightly better contrast than another one or slight have a might have a slightly better view angle or something like that. But at least they should be pretty close.

**Dave Jones:** So, there you go. I hope you enjoyed that look at designing your own LCD. It's not particularly hard. It depends on how much effort you want to put into it.

**Dave Jones:** The more effort you put into your design documentation and designing the segments and all that. It actually took David quite a while to actually render those segments and design them and things like that and tweak them.

**Dave Jones:** We needs to be a little bit fatter here and a little bit thinner there and whatnot. And we actually did a bit of this on the EV blog forum as well.

**Dave Jones:** I think we put it in the supporters section and asked for feedback and stuff like that. And of course everyone's got their own comments on what it should look and feel like, you know.

**Dave Jones:** But anyway, you've got to make a decision. So, we're going to get this manufactured. We haven't get a lot of manufactured yet. So, that will no doubt be another part of this video coming up soon.

**Dave Jones:** As I said, it's like two to four weeks delivery time or something like that. You probably can get shorter if you really need you know, express samples. But just be aware that samples that they produce, they might be able to produce you a sample in a week, but it may not be exactly the same as the production version.

**Dave Jones:** Maybe in terms of contrast, viewing angle, whatever. But hey, at least it gives you a you know, a look and feel prototype that you can physically use, power up, and get get your product you know, like an early prototype your product working for some dog and pony show you need to take it to or something.

**Dave Jones:** Anyway, if you like that video, please give it a big thumbs up. And the other videos are linked in somewhere here. Yeah, somewhere up here at the end of the video.

**Dave Jones:** Check it out. Don't forget to subscribe and all that sort of jazz. EV blog forum down below. Catch you next time.
