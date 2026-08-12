---
video_id: RwVzLOI4cmA
title: EEVblog #1307 - TUTORIAL: PCB BOM Consolidation
url: https://www.youtube.com/watch?v=RwVzLOI4cmA
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 21, "3": 43, "4": 60, "5": 80, "6": 90, "7": 101, "8": 126, "9": 146, "10": 160, "11": 173, "12": 185, "13": 200, "14": 208, "15": 217, "16": 240, "17": 251, "18": 271, "19": 283, "20": 293, "21": 309, "22": 324, "23": 337, "24": 357, "25": 382, "26": 407, "27": 431, "28": 457, "29": 475, "30": 488, "31": 501, "32": 514, "33": 530, "34": 542, "35": 553, "36": 562, "37": 578, "38": 594, "39": 603, "40": 619, "41": 627, "42": 638, "43": 653, "44": 669, "45": 682, "46": 689, "47": 701, "48": 718, "49": 734, "50": 746, "51": 762, "52": 774, "53": 790, "54": 800, "55": 819, "56": 840, "57": 854, "58": 862, "59": 878, "60": 890, "61": 902, "62": 916, "63": 928, "64": 945, "65": 957, "66": 979, "67": 990, "68": 998, "69": 1017, "70": 1027, "71": 1045, "72": 1056, "73": 1066, "74": 1076, "75": 1087, "76": 1101, "77": 1116, "78": 1142, "79": 1167, "80": 1183, "81": 1207, "82": 1226, "83": 1236, "84": 1247, "85": 1261, "86": 1277, "87": 1293, "88": 1307, "89": 1316, "90": 1327, "91": 1337, "92": 1348, "93": 1356, "94": 1367, "95": 1376, "96": 1384, "97": 1396, "98": 1405, "99": 1419, "100": 1431, "101": 1440, "102": 1457, "103": 1470, "104": 1484, "105": 1494, "106": 1514, "107": 1527, "108": 1538, "109": 1560, "110": 1574, "111": 1585, "112": 1594, "113": 1604, "114": 1621, "115": 1637, "116": 1659, "117": 1680, "118": 1697, "119": 1716, "120": 1731, "121": 1745, "122": 1761, "123": 1774, "124": 1788, "125": 1803, "126": 1814, "127": 1829, "128": 1847, "129": 1858, "130": 1883, "131": 1891, "132": 1912, "133": 1927, "134": 1940, "135": 1948, "136": 1963, "137": 1987, "138": 1996, "139": 2005, "140": 2018, "141": 2028, "142": 2040, "143": 2058, "144": 2069, "145": 2078, "146": 2097, "147": 2105, "148": 2117, "149": 2135, "150": 2160, "151": 2175, "152": 2199, "153": 2216, "154": 2235, "155": 2249, "156": 2258, "157": 2278, "158": 2295}
---

**Dave Jones:** Hi, let's talk about bomb consolidation because it can be quite an important subject when you're designing your product. Now, I've done uh videos on schematics uh before and I'll link them in down below and at the end if you haven't seen them.

**Dave Jones:** One is uh creating a nice readable uh schematic here and another is what is schematic ERC and I've done other videos on design rule checking and things like that.

**Dave Jones:** So, designing a your widget like this is a multi-step uh process. Typically, you'll uh design your schematic first and then you'll do your electrical rules testing your ERC, then you'll lay out your PCB and you'll do your design rules uh checking and then you'll do uh the generate the manufacturing uh files for it and then you typically get it assembled and everything else.

**Dave Jones:** And I've done many videos on uh design for manufacturing uh for example, but there's a step in there which I have mentioned in and you know, off and on in a few videos, but I've never done a dedicated video on it and it can actually be quite important.

**Dave Jones:** It's bomb consolidation. What's bomb consolidation? Well, let's find out. Now, bomb consolidation, whilst there are multiple parts to it and there's more aspects than just the bomb itself, it is basically done at the uh product schematic design stage or after you've uh designed your schematic.

**Dave Jones:** After you design it, you'll do the electrical rules checking of course, but before you do that, you want to do some bomb consolidation. Now, this is actually uh there's four aspects to this.

**Dave Jones:** It's not necessarily just about the bomb, but that's pretty much what we're going to get at in this video. So, you can think of it more in terms of like a product parts consolidation uh for example.

**Dave Jones:** However, you we'll just call it bomb consolidation for the purposes of this video. So, let's just assume that you've already uh designed your schematic. You've laid it out, you've it's beautiful and you're about to do your ERC, but before you do that, you want to think about this is part of the start of your design for manufacturing steps that you're going to do to can actually design and build your

**Dave Jones:** product. Okay, if you're just making a couple of them, it, you know, it doesn't really matter. BOM consolidation's not for every project. But, if you get more and more serious in your designs, and especially if you're going to high-volume manufacture, and especially with large or complicated boards that we're going to look at today, or even larger ones like the ones you see behind me, these motherboards, and just these

**Dave Jones:** enormous boards like this, BOM consolidation can be really important. In fact, one of the most vital aspects of designing your board. Now, there's potentially four parts to this, and we'll go through them.

**Dave Jones:** And they're kind of intermixed, and some of them may or may not be relevant, depending upon your circumstances as we're talking to. But, the first one, after you've designed your schematic, is to consolidate your values.

**Dave Jones:** I.e., the parts values. And we'll get into this in detail in terms of, say, the resistors. If you how many different types of resistors are you using? How many different types of capacitors?

**Dave Jones:** I can you actually change any values on your schematic to match some other part that you're also using on the design. Now, the second part is parts consolidation. This is where you might want to reuse your parts on your schematic.

**Dave Jones:** You may not have thought about this as you're designing your schematic, but you should have in terms of, like, can I reuse this component somewhere else in the design?

**Dave Jones:** Have I got two different types of diodes? Can I get away with one? Have I got, you know, five different types of transistors? Can I get away with two or three different types, and share them, for example?

**Dave Jones:** And the third type of optimization, which is essentially what we're doing here, we're optimizing the design. The third type is to consolidate your footprints. And we'll go into detail why you actually might want that, because, well, if you don't know about uh design for manufacturing and assembly, you could really come a gutser where it could actually uh cost you more money to get your uh device manufactured.

**Dave Jones:** And the fourth type of optimization is cost optimization. Can you actually substitute in parts that have lower cost and things like that? And we won't really cover that in this video.

**Dave Jones:** What we're going to look at in this design is really can we actually reuse uh component values? You know, can get away with using all 10K resistors, the holy grail of electronics design, by the way, is to use one value of resistor and one value of capacitor in your entire design.

**Dave Jones:** It's possible. Give it a go. Anyway, so we won't be looking at uh cost, although we might touch on that. So, anyway. Anyway, let's get to the first optimization or consolidation type, which is trying to consolidate our values.

**Dave Jones:** Right? So, I'm just going to go to the uh KiCad website here and just get a random project. Not necessarily random. I wanted a complex uh project. So, I found this one, the CIAA.

**Dave Jones:** I've mentioned this one before. I've used this in uh some KiCad examples and it's a 12-layer uh design. So, hats off to the team uh that's done this. It uses a Xilinx Zynq processor and it's a hugely populated a large number of parts both front and back, as we'll see.

**Dave Jones:** And uh view project takes you over to the GitHub here. I'll link this in down below. So, it's a really good example. If you're looking uh to like hone your skills uh for example, like laying out boards, for example, and you think you're getting really good, well, give this one a go.

**Dave Jones:** You know, like import the schematic, it's all ready to go, and then try and lay out the board yourself and see how you go. So, anyway, that's bit of a tangent there, but people keep asking that.

**Dave Jones:** How can I get better better at uh PCB design? How can I improve my skills? Have it better on my resume and things like that? Well, it's by taking a design an existing design like this, a fast track way take an existing design and then start laying out the boards just like blank the board start from scratch see if you can do it and preferably build up make sure it works

**Dave Jones:** but anyway here's the GitHub here and it's got the uh KiCad file and anyway it generates a bill of materials like this this is what most uh CAD programs will uh generate they'll generate a Excel uh file like this is CSV uh file of all the components you know the number the quantity you've got uh the uh component reference designator the description and then maybe like supplier part numbers manufacturer part

**Dave Jones:** numbers and all that uh sort of jazz footprints and values and all that sort of stuff now we won't use the Excel one today because the uh KiCad had this has this awesome plugin of an interactive uh bomb it like it can generate these you got to it doesn't come standard with KiCad you got to uh install it but this project actually already came with this it's a HTML file and it's interactive so

**Dave Jones:** this is the bomb for this particular uh project here which is like a general computing uh educational computing platform I believe it is and it this is actually great for you can see that it highlights the components on the board here both front and back as well as we go down so this is handy for like manual pick and placing and uh stuff like that so this

**Dave Jones:** is just so hats off to whoever wrote this uh plugin it's really fantastic but I chose this example because it's a really complicated project if we go up here now if we have a look at the stats for this board it's got 225 components on the front 344 components mounted on the backside most of those are probably bypass uh caps 569 components total uh you know that's that's a huge number of

**Dave Jones:** parts but of course it's still nothing compared to like enormous motherboards and you know hugely other complex uh industrial uh bits of kit. But, it's a really good example of a relatively uh you know, complex modern board that you might want to have to get uh manufactured once you get uh serious if you're designing, you know, serious uh products.

**Dave Jones:** And look at all the parts down here. Here they are. As we said, here it is. There's 161 different components on this thing. Why does that matter? 161 Hmm.

**Dave Jones:** That's interesting. This is where for manufacture comes into it. Now, of course, you have to get your little Assume this is this board. Uh you have to get this board pick and place assembled cuz you're not going to hand assemble something like this.

**Dave Jones:** That's just like I've done it and don't don't subject yourself to that. Anyway, you're going to get your widget. Uh you're designing this thing for high-volume manufacture. It's going to be pick and place machine assembled.

**Dave Jones:** Well, you've got to know all about pick and place machines in particular what your particular assembly house has. And you should actually uh choose and talk to your assembly house even at the design stage, even when you're designing the schematic if you're serious about this sort of stuff.

**Dave Jones:** Not Well, not necessary Yeah, if you're Apple and you're designing a new iPhone, of course, yeah, that's absolutely essential to do something like that or extremely high-volume, you know, farting novelty gadget in the billions or whatever.

**Dave Jones:** Yeah, it can really matter, but most designs you probably don't have to talk to the manufacturer, but you should keep some basic rules of thumb uh involved with pick and place machines.

**Dave Jones:** Now, let's have a look at a typical pick and place machine, shall we? Stick with me because this actually guides a lot of our things that we're going to uh talk about in our bomb consolidation.

**Dave Jones:** So, buckle up, Dorothy. Kansas is going bye-bye. So, I just picked this one, Yamaha, one of, you know, the best in the business. This is a It's a Ultra high-speed, 200,000 CPH, which is components per hour.

**Dave Jones:** That's the rating that they have in here. Basically, knowing what your assembly house might typically have, and if they've only got one of these machines, then what what what what you can come a gutser on this board already, even if they have two of these machines.

**Dave Jones:** You can come a gutser already. Why? Because, if you go down here, it actually supports If you go down here and check out the specs down here, here it is.

**Dave Jones:** It's got a maximum of 80 feeders. Now, you've seen these before. These are reels that your components come on. All your resistors, capacitors, diodes, transistors, your ICs, and even your battery uh holders, for example, your CR2032 coin cells.

**Dave Jones:** They all come Everything pretty much comes on reels. You can get trays, but let's not worry about that. Now, these have to go into a feeder into the machine.

**Dave Jones:** And you can physically see these feeders up here, and these are cassettes that they that hold these reels and insert. So, they've only got a maximum of these feeders, but aha, fine print, 8 mm tape width uh type.

**Dave Jones:** So, this is an 8 mm type uh one which holds, you know, typical resistors and capacitors. And it can only hold a maximum of 80 of these in the machine, or even less if you have wider parts, like a like a CR2032 battery, for example.

**Dave Jones:** That could be like a really wide tape, and that'll take up several slots in there. So, what that means is that your assembly uh line that you're using at whatever manufacturer will be limited to how many of these reels they can hold.

**Dave Jones:** So, if your design here has more than 80 parts, absolute maximum for that particular uh machine, then it's not that you can't get it manufactured. It's just that they'll have to put it through multiple passes.

**Dave Jones:** Then they'll have to either use different lines, or they'll have to have two of these machines in series. It can pass through one machine, then can pass through another.

**Dave Jones:** And some big assembly houses will have multiple ones of these machines, but just remember this can be a big limitation for your design. And they'll charge Yes, they'll manufacture the board for you and they often won't even tell you.

**Dave Jones:** They'll just give you quote you a price and it's going to be a much higher price to assemble your board cuz they know they have to pass it through two or three times cuz you're using 160 160 different types of components which all have to come on their own reel.

**Dave Jones:** But not only that, then you have to actually go out and buy and source all of these different types of parts. And just missing one part out of those 160 parts, you might not be able to get your product manufactured.

**Dave Jones:** Or you could get it almost all manufactured except for one part. So, the more parts you different types of parts you use on your design, the higher the risk, the greater the potential assembly cost, and like all sorts of issues to do with that.

**Dave Jones:** So, reducing the num- different types of components is what we're talking about here in terms of BOM optimization. You want to minimize the number of different BOM items Bill of Materials, by the way.

**Dave Jones:** I've mentioned that, have I? Bill of Materials different BOM items that you have, the different parts. There's huge advantages to doing that. And the bigger and more complex your boards get, the more important this becomes.

**Dave Jones:** So, we talked about like three different potential ways to do this. The first one is value consolidation, which is generally you might get this for resistors and capacitors. There's other components as well, but they're the two biggies that you want to consolidate.

**Dave Jones:** Now, look at this. How many different types of capacitors do they use in this design? Let's have a look. It starts at component number one here. These It's good that they've all sorted them by capacitors.

**Dave Jones:** 26 different types of capacitors. Some pick and place machines might only support 40 reels. We've already taken up half of our reels our reel space just with capacitors. There is no way and this is by the way I'm not a sledging the designers of this a thing at all.

**Dave Jones:** They just didn't bother to do bomb consolidation. There might be reasons they only wanted, you know, 100 of these made. Yeah, it didn't matter, right? Um just the design cost of and getting the manufacture was nothing compared to but if you wanted to make a 100,000 or million of these things, you don't want to be having 26 different types of capacitors.

**Dave Jones:** That's just nuts. So, we want to go in and do some bomb consolidation. Look and check this out right off the bat. We've got one capacitor 11 puff. 11 puff.

**Dave Jones:** Why? When we've got another one which is 13 puff. We've got one of those. We've got one 16 puff capacitor. We've got one 24 puff one two 18 puff.

**Dave Jones:** Come on. You can't tell me that you need precisely 11 picofarads and 13 picofarads. That is ridiculous. The capacitors are going to be 5 10% tolerance anyway. So, the difference between 11 and 13 puff.

**Dave Jones:** Now, look if you're doing a complex RF design or something like that, then yeah, okay, that could matter. But in a lot of cases, you're just going to choose these values because they came out of an application note or it's what came out of your calculator.

**Dave Jones:** For example, you might want to okay, I want like a 1 MHz filter for example. You do your calculations and it comes out to 11 picofarads or 11 nanofarads or whatever it is and or a resistor value of, you know, 6.25 K.

**Dave Jones:** So, you choose the, you know, closest E96 preferred value to that. Well, you don't really have to. So, you really should as part of this optimization process this bomb optimization is go about look at your design and just think critically.

**Dave Jones:** Like really, do I need an 11 picofarad? Couldn't I have used a 13 or maybe a 16 or maybe even an 18 picofarads? I mean, you know, come on.

**Dave Jones:** Right, so let's go into the schematic here and have a look. C92, there it is. C104, 11 picofarads and 13 picofarads. Where's it What's it used for? The power supply.

**Dave Jones:** Look at this. Look at this. The power supply, a switching power supply. That's it, 1.2 volt power supply and they've determined that they need 11 picofarad capacitor and an 8.87 K resistor.

**Dave Jones:** I mean, this is just silly stuff, right? There is no way you need that precision in a compensation network for a just a switching regulator. Obviously, these values have just popped out of the confuser here and they've just whacked them in there and said, "All right, all right, all right, we need 11 picofarad capacitor.

**Dave Jones:** We need a 13 picofarad capacitor." Like, give me a break. No. Go back to the data sheet here, TPS65400. This is an exercise for those playing along at home.

**Dave Jones:** Go into the data sheet and actually have a look at where it It'll It'll probably give you the equations for calculating the compensation values and things like that. Is it that critical?

**Dave Jones:** The answer is almost certainly no. You could easily consolidate these two values here, which are the only ones used in the design. It's the only place it's used and you've got to take up a whole You've got to go buy a whole reel, then your purchasing officer has to then go and purchase these from somewhere.

**Dave Jones:** You've got to find them in stock. They may not have them in stock. It could It could, you know, screw up your entire production schedule just because you decided you needed 11 picofarad cap in there.

**Dave Jones:** Now, this is not uncommon in the industry. It's happened to me many times. It's where the purchasing officers, and yes, large corporations will have purchasing officers. Their sole job is to buy all these source and buy all these parts for the new uh you know, for the latest production run of your widget that you're trying to actually produce.

**Dave Jones:** And they will often come to you and say, "Look, I cannot for the life of me get an 11 picafarad capacitor in an 0603 footprint. The whole world's out of them.

**Dave Jones:** I've scoured all I scoured the gray market, cannot find them. Can we have a substitute?" And a good bill of materials will also have like a substi- like different brands.

**Dave Jones:** In fact, it was company policy at companies at some companies that I've worked at, you would have special like military type ones where you'd have three different manufacturer part number variants.

**Dave Jones:** So, you'd have three choices so that the purchasing people can go and choose any one of those values, and it doesn't matter, they're fully qual- that part was fully qualified for use in the design.

**Dave Jones:** But often they'll come back and they'll go, "Look, I cannot get this. Can I use Can I buy something else?" And you might have to do an engineering change request or whatever it is to go, "Yep, look, I authorize to use a 13 puff capacitor in there instead of 11 puff.

**Dave Jones:** I was just lazy when I designed it and it doesn't matter a rat's ass that it's 11 picafarads or 13." Now, values like these ones, for example, this obviously sets out what the value our 1.2 volt voltage reference.

**Dave Jones:** So, these values are fairly the ratio of them is fairly critical. But you could actually put in a 10k here, like a 13.3k, okay? And yes, 13.3 here, if we go to 1.33, is a both is all three columns here is an E48, E96, and E192 preferred value.

**Dave Jones:** So, you can actually get that value, but like should you actually be using this? Now, generally when I'm doing a design like this, I will go, "Look, I'm going to use a 10K as this bottom one, and then I'll calculate the top one, and then I'll figure out what you know, then I only need to get one oddball value up here instead of two oddball values." And here's the next

**Dave Jones:** thing, with value consolidation, it can actually be better and cheaper and more beneficial to use more resistors in your design than to choose the right value and have to get another complete reel and have another individual bomb item.

**Dave Jones:** For example, this is a classic example of it here. Well, you need a specific value to meet your tolerance of your 1.2 V voltage rail here. Now, just for argument's sake, let's say that you chose a 10K resistor here, for example, and you did your calculations and found that your 1.2 V within whatever tolerance you required, a like a 4.99K, for example, or five Let's say it popped

**Dave Jones:** out at 5K, or even 4.99. What do you do? You don't necessarily go and just buy yet another reel just for that one value. It takes up another slot in your pick-and-place machine, more bill of materials items, when you can just put two 10K resistors in parallel.

**Dave Jones:** You've reused one of your parts here, and sure, you've put in an extra resistor, and sure, it's more board space, and sure, that might be important if you've got a real ultra-dense design.

**Dave Jones:** You may not have the luxury of being able to put two resistors in parallel. I mean, you know, probably the majority of cases in practice, you are going to have the room to put in the two 10K or make room.

**Dave Jones:** A good PCB layout designer can always make room for that extra resistor, just so that you reduce that one extra bomb item. And you can do this again, 16 puff up here, 1.2 1.5 nF.

**Dave Jones:** You know, couldn't we have used 1.2 nF? Look, do we have to use 11k here and 11.3k here? Really? So, this is a really good example and it's why I actually picked uh the when I saw this project, I just picked it like a random and complicated one.

**Dave Jones:** And when I saw this, I went good example, you know, lots of different parts in the bomb. So, yeah, just go through, read your data sheets again, go through your calculations, reevaluate, do your engineering evaluation, and all the stuff that goes along with qualifying your design and everything else.

**Dave Jones:** And you know, almost every project I've ever done, there might be the odd exception, but the vast, vast majority, I've been able to bomb optimize in some way when it comes to uh capacitor and resistor values.

**Dave Jones:** And then if we just uh quickly look at uh some of the uh memory on here, look, we got termination resistors 40.2 ohms. Yeah, we've got a lot of them.

**Dave Jones:** That's fine. This is obviously popped out of their uh polar impedance uh calculator or whatever it is they use to uh calculate the transmission line impedance. We've got 80.6 ohms here, for example.

**Dave Jones:** Uh not sure what that one's doing at uh you know, 240 ohms and things like that. So, all these oddball values will pop out of your confuser here, but don't necessarily blindly follow them.

**Dave Jones:** That can lead to you know, a bomb like this one, which hey, as I said, if you're making, you know, 10 or 100 of these, you just might not care, you know, it popped out.

**Dave Jones:** I couldn't be bothered spending another minute. I was on a tight deadline. I needed to design this thing, you know, and just you know, throw it out out the door.

**Dave Jones:** And it it's fine. The manufacturer will do it, the purchasing people will purchase them all, and Bob's your uncle, but there can be huge value in just spending like a few hours.

**Dave Jones:** It's not, you know, it's like a this design here. Sure, okay, I might spend a whole day like uh checking this, you know, pull up the data sheet for this.

**Dave Jones:** Do we really need our 10.7k in there and things like that, you know? And so, yeah, I you might spend a day just tidying up this, but they obviously spent months designing this thing.

**Dave Jones:** And well, and there's some argument over when you might do this. Some people might actually Okay, go and, you know, the number pops out of your confuser. So, that's what you put in your schematic.

**Dave Jones:** And then And I've done this myself, and there's valid arguments for it. Is once you've done that, then generate your bomb, and then go in and see if you can optimize the bomb.

**Dave Jones:** You can actually do it right at this schematic stage, you know, while you're designing you know, I'm going a 6.81k so anywhere else. So, I'm going to put two resistors in series or parallel to get, you know, near enough a value or something like that.

**Dave Jones:** So, you could argue that it's just it's better to do as a separate pass because then you're not bogging down your design process. You're getting the design down first, and then Breathe in, breathe out.

**Dave Jones:** I've finished my schematic. Okay, let's, you know, you go get your extra coffee or whatever chocolate or whatever it is you need to keep going, and then you go do your second pass bomb consolidation.

**Dave Jones:** So, that's the first part, consolidating your values, mostly resistors and capacitors, but some other parts. Now, the second part is parts consolidation. Where Well, do I really need that part, or can I reuse that part somewhere else?

**Dave Jones:** Not just the value, but the actual component itself. Now, I'll link it in. I've done a video on Muntzing and a bypass capacitors visualized like Muntzing Mad Man Muntz back in the day used to be famous for carrying around a pair of side cutters.

**Dave Jones:** And whenever one of his designers of one of his analog No, this digital rubbish. Analog TVs I finished my design. They showed it to Mad Man Muntz. He'd come around with his side cutters and start snipping out components one by one until it stopped working.

**Dave Jones:** And when it did stop working, he put that last component back in and go, "Right, toss those parts out. We obviously didn't need them." And that's Muntzing. And it is actually a real thing.

**Dave Jones:** And one thing where it really comes in is bypass capacitors. I've shown that I'm not going to say that are they really needed. In most cases, no. It's just general rules of thumb where if you haven't analyzed your power system and it can be quite complex to do this requiring real sophisticated software and you know, specialized software to do it.

**Dave Jones:** Do you need all of these bypass capacitors? Do you need a 10 micro, 1 micro, 100 and a 10 and a 1 and all on the power pins for example.

**Dave Jones:** FPGA data sheets for example like I'm sure go check up the data sheet for the Zynq FPGA using here. They've probably got an application note just dedicated to bypassing.

**Dave Jones:** And you can go over here to Maxim for example. There's Xilinx and there's Altera and other FPGA manufacturer app notes on this power supply solutions for Zynq FPGAs for example and how like you need X amount of bypassing and the impedance curves and why you need all these different values and and like you know, power up surges and things like that.

**Dave Jones:** And you know, there's all sorts of stuff involved in it's it's endless. It really is endless. Anyway, the point is do you need all of these capacitors here? The answer is almost certainly not.

**Dave Jones:** So while they're all but they're all the same values. So but still even when you have if you use too many capacitors, you're even though you got might have 4,000 on a reel.

**Dave Jones:** You know, you manufacturing a lot of boards per hour. Your reels can run out earlier and then somebody's got to you know, a red light flashes on top of the machine.

**Dave Jones:** Quick, I've got to stop the whole production line is stopped because you ran out of your 10 nano farad capacitors cuz you used 10 bazillion gazillion of them on your machines.

**Dave Jones:** Somebody's got to come around and replace the reel and to start up the line again. So you know, and they cost money especially like you're using the more expensive 1 mic and uh 10 microfarad uh ones, for example, they can uh be expensive uh parts, but often, yeah, you can do some months in and you can get away.

**Dave Jones:** But sometimes you won't know this at the design stage. You might just play it safe and go, "Look, I'm just going to belt and braces. I'm just going to put in my 10 microfarads, my 1 microfarad, and my 10 ends, and you know, she'll be right." But there are some gains to be had here by months in uh something like this for volume.

**Dave Jones:** And then that might come down to here. Look, oh wait, we've got three 330 microfarads down here. You know, you might have used a 100 microfarad somewhere else. Could we have used, you know, uh the 330s somewhere else where we used our 100 microfarads or whatever or for, you know, a complex as FPGAs are often complex, you know, they have five, six different power supplies.

**Dave Jones:** That's not uncommon at all uh for a design like this. And you know, can you optimize the number of parts? Now, this isn't the best uh design for this, but uh talk about uh transistors, for example, if you you're doing a lot of uh like switching in your design or whatever and things like that, well, you might be using like a different types of transistors for different reasons.

**Dave Jones:** You might need, "Oh, this one's slightly higher, you know, I need more current for this one." Well, can you actually consolidate these parts? You know, if you've got a high-power transistor here that might cost uh 10 cents, and you've got another uh transistor which you you don't need the high power, but it costs 8 cents.

**Dave Jones:** Like, do you actually need to save that 2 cents and then have a whole extra reel and go and source it and take up uh space on your pick and place machine just because um you didn't want to reuse this 1 amp uh transistor, for example, where you only needed 100 milliamps and you chose another uh transistor?

**Dave Jones:** Like, can you reuse parts like that? Diodes are another classic one, for example, where you might use a uh 1 amp diode on your input, for example, some sort of clamping or protection, uh reverse protection or something, and then you might need another diode in your design.

**Dave Jones:** Do you actually need that to be a 1N914 or some other, you know, a signal diode? Can you actually reuse that same power diode? Try and consolidate your parts and reduce the number of line items on your bomb.

**Dave Jones:** Now, the third type of optimization, once again, it's another design for manufacturing technique. We have to go back to our pick-and-place machine, is consolidating footprints. Now, this one actually Look, this one has Yeah, I think Look Look at these 0201s.

**Dave Jones:** What a pain. Do you really need 0201 capacitors? Look, these 1 microfarads. Do you really need 1 micro 0201 footprints? That's ridiculous. That's half the size of an 0402, which is already small.

**Dave Jones:** Do you really need that? Do you really need even need to go to 0402s? In this particular case, yeah, they probably do. But in a lot of cases, you can actually uh pay more to get boards assembled because they've got 0402s.

**Dave Jones:** And it might also limit the number of manufacturers you can use, especially local manufacturers. Uh for example, let's go back uh to this uh Yamaha machine over here. It's really expensive, like kind of like one of the top of the line uh jobbies.

**Dave Jones:** Yes, it can do 0201, right? So, you know, you might think, "Okay, I can use 0201 resistors on my design." No, don't. Look at the fine print, okay? Let's go over to here.

**Dave Jones:** They've got different types of heads. The ultra high-speed head, for example, yeah, it can do 0201 parts, but they physically have to change the head on the or use a different head on the pick-and-place machine to actually do that.

**Dave Jones:** And the reason that the smaller parts can uh go faster is because they've got less mass. They can pick them up, zoom, all around the board. They can move them faster because then they won't fall off because of the mass of the parts just being held on the nozzle by a vacuum and the heavier the part is the slower their head has to move.

**Dave Jones:** You've got a a giant big power resistor. It has to suck it up and then clunk clunk clunk clunk clunk move it over place. But an 0201 goes That's it.

**Dave Jones:** Done. So this is where the multiple heads and look at this the flexible head here for example 0603. So if you do all of your design with 0603 footprints, they can use this flexible head although they and there's lots of pick and place machines out there that will only go there especially older ones and you know the cheaper ones are used in you know some local manufacturer or

**Dave Jones:** something like that who's not really high-end. They might be limited to 0603. They might be able to do 0402 for you but there's actually going to be a lot of wastage.

**Dave Jones:** So your manufacturer might actually tell you like allow 5% or 10% for wastage for example especially on like a smaller parts and if you especially if you're using semiconductors like or chips like real tiny little packages they might actually be expensive little devices and or yeah really high precision resistors for example.

**Dave Jones:** You can pay a dollar for a high precision like a really good high precision low tempco resistor for example. So like if you choose a real ultra tiny one and there's 5 10% wastage that's going to add up to your assembly cost.

**Dave Jones:** So they might say okay we need 3,000 of these parts but give us a real 4,000 because we're going to like waste a lot of them. And there's a waste bin on the pick and place machine where all these fallen components just drop off and fall into.

**Dave Jones:** So this is why if I was designing this and I looked at this bomb I was doing my bomb consolidation this one sticks out like a dog's hind leg.

**Dave Jones:** 0201 isn't the only 0201 part I know is other one okay so they're using some others but you know like it might stick out sort by you know package type or whatever, and you might it might pop out, "Oh, look, you're like we're using 10402 in this entire design." Really?

**Dave Jones:** Do we have to? Can we Can't we just use an 0603, please? So, just going that one part under a certain size could cost you, you know, a lot of heartache and a lot of money as well, as well as going one part over the number of reels that your assembly line I can actually support.

**Dave Jones:** That can add up to a lot of heartache and a lot of extra cost as well. And they often won't tell you this. They'll just happily accept your project and go, "Yes, we can assemble that.

**Dave Jones:** No worries." And they'll give you a quote, and you won't even know that they're charging you more. So, as I said, we won't get into the fourth one, which is BOM optimizing for cost.

**Dave Jones:** Although, I've got a video which might come up. Let me know if you want to know see a video on a 1-cent voltage regulator. Is it any good? I'll just going to play around with it and see 1-cent voltage regulator can actually do the business.

**Dave Jones:** Anyway, let me know. You give us a thumbs up if you want to see that. Leave it in the comments down below. But anyway, there's so many more ways that you can optimize values in designs like this.

**Dave Jones:** For example, like we've got an I squared C line here. That's going to have certain pull-ups in the lower value pull-up for your I squared C line, the higher speed because it's an open collector output.

**Dave Jones:** The higher the slew rate the faster the slew rate, for example, and the more speed you can get out of your I squared C bus. So, if your you know, Confuser popped out the value of like 1.8K for your pull-up, well, do you need and you don't use 1.8K anywhere else?

**Dave Jones:** Well, why not use a 1.5K? Yeah, might use a bit more power, for example, and that might be a trade-off that you have to go through your design. This is all part of engineering.

**Dave Jones:** Yeah, can I trade off the extra power for the 1.5k pull-up resistor even 1k pull-up resistor versus the calculated 1.8k pull-up that I thought I could get away with?

**Dave Jones:** It might be worth it cuz it save an extra reel. And this video actually was originally going to be me just going through like a dozen different open-source designs on the market and just looking at all values and actually going into the data sheets and and trying to calculate, you know, can we get away with certain values?

**Dave Jones:** LEDs are another classic example like you might calculate, okay, I want 10 milliamps to go through my LED, it's going to be like a pretty bright one. I want 10 milliamps in there.

**Dave Jones:** Well, and you can fuse a pop set the value, well, I need a, you know, 680 ohm resistor. Well, I don't know. Can you get away with like does it have to be that exact brightness?

**Dave Jones:** Can you get away with a little bit more, little bit less to consolidate your bottom items? Anyway, let me know down below. If you do want to see that video where I actually go through a bunch of designs and actually spend hours and hours actually looking at the data sheets say for this and you know, figuring out do we actually need that value?

**Dave Jones:** Do we need precisely this? But yeah, I decided just to show you the or in this case three different ways to consolidate your bomb. And yeah, it's not applicable or designs you may never get to that stage where you need this, but hey, if you want to level up your skills in electronics design, then bomb consolidation can be a vital step in part of your design for manufacturing

**Dave Jones:** just an essential step in your design. You draw your schematic, you do your bomb consolidation, then you do your ESC and then you lay out your board and then you do your other design for manufacturing stuff and it's all tied up in there whichever order you want to do it, it can be really important.

**Dave Jones:** So anyway, hope you found that useful and if you did, please give it a big thumbs up and as always comment down below especially like what things have you up to what other things have you optimized in designs where you know look as marginal and I really I had to actually seriously it may pay you to actually spend like a day or two's engineering effort actually building up

**Dave Jones:** a prototype of this and testing it over temperature and stuff like that just to verify that you know the value you chose can actually work even though it's you know it might be slightly outside the margin and you might try some tolerance resistors you might even do some Monte Carlo simulation analysis which is Monte Carlo analysis in simulation.

**Dave Jones:** I've done a video on that I think I might have. Try and find that. Is where you can like test your design for different values like you know spreading your values like 5% you know 1% tolerance resistors it'll you know go plus minus 1% and rerun the simulation and tell you if it's not going to go tits up on you and things like that.

**Dave Jones:** Anyway, leave it in the going for hours. Leave it in the comments down below what stuff you've optimized. Have you really saved some you know big cost or big headache by doing the bomb optimization or do you just never bother?

**Dave Jones:** Let us know. There's valid reasons for just like in this particular case they didn't bother. It's a very clear this is one of the you know one of the most amazing examples I've seen.

**Dave Jones:** You can tell nobody's even bothered to bomb optimize this and that might be fine. So nothing against the designers of this thing there's valid reasons why you wouldn't bother but if you're going to take this in a high volume production I would not go into high volume production of this board with this bomb like this.

**Dave Jones:** I find it highly offensive. It's just no. I would not over my dead body this thing's going into production with all these different with like 76 minus 27 49 different value resistors 49 reels of resistors on this thing like no.

**Dave Jones:** No over my dead body that's going into production. And I hope you feel the same way, cuz that's that's the engineering spirit. Catch you next time.
