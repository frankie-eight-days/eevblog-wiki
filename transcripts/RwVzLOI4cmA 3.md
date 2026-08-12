---
video_id: RwVzLOI4cmA
title: EEVblog #1307 - TUTORIAL: PCB BOM Consolidation
url: https://www.youtube.com/watch?v=RwVzLOI4cmA
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 25, "3": 39, "4": 53, "5": 70, "6": 83, "7": 97, "8": 110, "9": 123, "10": 136, "11": 150, "12": 165, "13": 180, "14": 195, "15": 208, "16": 220, "17": 234, "18": 250, "19": 262, "20": 277, "21": 290, "22": 305, "23": 316, "24": 329, "25": 341, "26": 353, "27": 367, "28": 382, "29": 398, "30": 413, "31": 427, "32": 440, "33": 457, "34": 470, "35": 482, "36": 499, "37": 511, "38": 526, "39": 537, "40": 553, "41": 564, "42": 580, "43": 594, "44": 608, "45": 624, "46": 638, "47": 651, "48": 667, "49": 680, "50": 691, "51": 703, "52": 718, "53": 733, "54": 744, "55": 759, "56": 774, "57": 788, "58": 800, "59": 819, "60": 831, "61": 845, "62": 862, "63": 878, "64": 890, "65": 902, "66": 916, "67": 932, "68": 955, "69": 974, "70": 986, "71": 998, "72": 1012, "73": 1023, "74": 1036, "75": 1050, "76": 1064, "77": 1078, "78": 1091, "79": 1104, "80": 1118, "81": 1142, "82": 1157, "83": 1173, "84": 1188, "85": 1200, "86": 1217, "87": 1232, "88": 1244, "89": 1261, "90": 1275, "91": 1288, "92": 1302, "93": 1316, "94": 1331, "95": 1346, "96": 1359, "97": 1372, "98": 1383, "99": 1395, "100": 1406, "101": 1419, "102": 1433, "103": 1445, "104": 1459, "105": 1472, "106": 1484, "107": 1496, "108": 1510, "109": 1527, "110": 1543, "111": 1560, "112": 1577, "113": 1588, "114": 1601, "115": 1614, "116": 1627, "117": 1637, "118": 1651, "119": 1663, "120": 1675, "121": 1688, "122": 1704, "123": 1718, "124": 1731, "125": 1745, "126": 1759, "127": 1778, "128": 1790, "129": 1803, "130": 1817, "131": 1832, "132": 1845, "133": 1858, "134": 1874, "135": 1888, "136": 1901, "137": 1916, "138": 1932, "139": 1943, "140": 1956, "141": 1972, "142": 1989, "143": 1999, "144": 2012, "145": 2022, "146": 2038, "147": 2053, "148": 2067, "149": 2080, "150": 2093, "151": 2105, "152": 2117, "153": 2128, "154": 2143, "155": 2158, "156": 2170, "157": 2181, "158": 2194, "159": 2208, "160": 2220, "161": 2233, "162": 2245, "163": 2258, "164": 2271, "165": 2285, "166": 2306}
---

**Dave Jones:** Hi, let's talk about bomb consolidation because it can be quite an important subject when you're designing your product. Now, I've done uh videos on schematics uh before and I'll link them in down below and at the end if you

**Dave Jones:** haven't seen them. One is uh creating a nice readable uh schematic here and another is what is schematic ERC and I've done other videos on design rule checking and things like that. So, designing a your widget like this is a

**Dave Jones:** multi-step uh process. Typically, you'll uh design your schematic first and then you'll do your electrical rules testing your ERC, then you'll lay out your PCB and you'll do your design rules uh checking and then you'll do uh the

**Dave Jones:** generate the manufacturing uh files for it and then you typically get it assembled and everything else. And I've done many videos on uh design for manufacturing uh for example, but there's a step in there which I have mentioned in and

**Dave Jones:** you know, off and on in a few videos, but I've never done a dedicated video on it and it can actually be quite important. It's bomb consolidation. What's bomb consolidation? Well, let's find out. Now, bomb consolidation, whilst there are multiple parts to it

**Dave Jones:** and there's more aspects than just the bomb itself, it is basically done at the uh product schematic design stage or after you've uh designed your schematic. After you design it, you'll do the electrical rules checking of course, but

**Dave Jones:** before you do that, you want to do some bomb consolidation. Now, this is actually uh there's four aspects to this. It's not necessarily just about the bomb, but that's pretty much what we're going to get at in this video. So,

**Dave Jones:** you can think of it more in terms of like a product parts consolidation uh for example. However, you we'll just call it bomb consolidation for the purposes of this video. So, let's just assume that you've already uh designed

**Dave Jones:** your schematic. You've laid it out, you've it's beautiful and you're about to do your ERC, but before you do that, you want to think about this is part of the start of your design for manufacturing steps that you're going to

**Dave Jones:** do to can actually design and build your product. Okay, if you're just making a couple of them, it, you know, it doesn't really matter. BOM consolidation's not for every project. But, if you get more and more serious in your designs, and

**Dave Jones:** especially if you're going to high-volume manufacture, and especially with large or complicated boards that we're going to look at today, or even larger ones like the ones you see behind me, these motherboards, and just these enormous boards like this, BOM

**Dave Jones:** consolidation can be really important. In fact, one of the most vital aspects of designing your board. Now, there's potentially four parts to this, and we'll go through them. And they're kind of intermixed, and some of them may or

**Dave Jones:** may not be relevant, depending upon your circumstances as we're talking to. But, the first one, after you've designed your schematic, is to consolidate your values. I.e., the parts values. And we'll get into this in detail in terms of, say, the resistors. If you how many

**Dave Jones:** different types of resistors are you using? How many different types of capacitors? I can you actually change any values on your schematic to match some other part that you're also using on the design. Now, the second part is parts

**Dave Jones:** consolidation. This is where you might want to reuse your parts on your schematic. You may not have thought about this as you're designing your schematic, but you should have in terms of, like, can I reuse this component somewhere else in

**Dave Jones:** the design? Have I got two different types of diodes? Can I get away with one? Have I got, you know, five different types of transistors? Can I get away with two or three different types, and share them, for example? And

**Dave Jones:** the third type of optimization, which is essentially what we're doing here, we're optimizing the design. The third type is to consolidate your footprints. And we'll go into detail why you actually might want that, because, well, if you don't know about uh design for

**Dave Jones:** manufacturing and assembly, you could really come a gutser where it could actually uh cost you more money to get your uh device manufactured. And the fourth type of optimization is cost optimization. Can you actually substitute in parts that have lower cost

**Dave Jones:** and things like that? And we won't really cover that in this video. What we're going to look at in this design is really can we actually reuse uh component values? You know, can get away with using all 10K resistors, the holy

**Dave Jones:** grail of electronics design, by the way, is to use one value of resistor and one value of capacitor in your entire design. It's possible. Give it a go. Anyway, so we won't be looking at uh cost, although we might touch on that.

**Dave Jones:** So, anyway. Anyway, let's get to the first optimization or consolidation type, which is trying to consolidate our values. Right? So, I'm just going to go to the uh KiCad website here and just get a random project. Not necessarily

**Dave Jones:** random. I wanted a complex uh project. So, I found this one, the CIAA. I've mentioned this one before. I've used this in uh some KiCad examples and it's a 12-layer uh design. So, hats off to the team uh that's done this. It uses a

**Dave Jones:** Xilinx Zynq processor and it's a hugely populated a large number of parts both front and back, as we'll see. And uh view project takes you over to the GitHub here. I'll link this in down below. So, it's a really good example.

**Dave Jones:** If you're looking uh to like hone your skills uh for example, like laying out boards, for example, and you think you're getting really good, well, give this one a go. You know, like import the schematic, it's all ready to go, and

**Dave Jones:** then try and lay out the board yourself and see how you go. So, anyway, that's bit of a tangent there, but people keep asking that. How can I get better better at uh PCB design? How can I improve my

**Dave Jones:** skills? Have it better on my resume and things like that? Well, it's by taking a design an existing design like this, a fast track way take an existing design and then start laying out the boards just like blank the board start from

**Dave Jones:** scratch see if you can do it and preferably build up make sure it works but anyway here's the GitHub here and it's got the uh KiCad file and anyway it generates a bill of materials like this this is what most uh CAD programs will

**Dave Jones:** uh generate they'll generate a Excel uh file like this is CSV uh file of all the components you know the number the quantity you've got uh the uh component reference designator the description and then maybe like supplier part numbers manufacturer part

**Dave Jones:** numbers and all that uh sort of jazz footprints and values and all that sort of stuff now we won't use the Excel one today because the uh KiCad had this has this awesome plugin of an interactive uh bomb it like it can generate these you

**Dave Jones:** got to it doesn't come standard with KiCad you got to uh install it but this project actually already came with this it's a HTML file and it's interactive so this is the bomb for this particular uh project here which is like a general

**Dave Jones:** computing uh educational computing platform I believe it is and it this is actually great for you can see that it highlights the components on the board here both front and back as well as we go down so this

**Dave Jones:** is handy for like manual pick and placing and uh stuff like that so this is just so hats off to whoever wrote this uh plugin it's really fantastic but I chose this example because it's a really complicated project if we go up

**Dave Jones:** here now if we have a look at the stats for this board it's got 225 components on the front 344 components mounted on the backside most of those are probably bypass uh caps 569 components total uh you know that's that's a huge number of

**Dave Jones:** parts but of course it's still nothing compared to like enormous motherboards and you know hugely other complex uh industrial uh bits of kit. But, it's a really good example of a relatively uh you know, complex modern board that you

**Dave Jones:** might want to have to get uh manufactured once you get uh serious if you're designing, you know, serious uh products. And look at all the parts down here. Here they are. As we said, here it is. There's 161

**Dave Jones:** different components on this thing. Why does that matter? 161 Hmm. That's interesting. This is where for manufacture comes into it. Now, of course, you have to get your little Assume this is this board. Uh you have to get this board pick and place

**Dave Jones:** assembled cuz you're not going to hand assemble something like this. That's just like I've done it and don't don't subject yourself to that. Anyway, you're going to get your widget. Uh you're designing this thing for high-volume manufacture. It's going to

**Dave Jones:** be pick and place machine assembled. Well, you've got to know all about pick and place machines in particular what your particular assembly house has. And you should actually uh choose and talk to your assembly house even at the

**Dave Jones:** design stage, even when you're designing the schematic if you're serious about this sort of stuff. Not Well, not necessary Yeah, if you're Apple and you're designing a new iPhone, of course, yeah, that's absolutely essential to do something like that or

**Dave Jones:** extremely high-volume, you know, farting novelty gadget in the billions or whatever. Yeah, it can really matter, but most designs you probably don't have to talk to the manufacturer, but you should keep some basic rules of thumb uh involved with pick and place

**Dave Jones:** machines. Now, let's have a look at a typical pick and place machine, shall we? Stick with me because this actually guides a lot of our things that we're going to uh talk about in our bomb consolidation. So, buckle up, Dorothy.

**Dave Jones:** Kansas is going bye-bye. So, I just picked this one, Yamaha, one of, you know, the best in the business. This is a It's a Ultra high-speed, 200,000 CPH, which is components per hour. That's the rating that they have

**Dave Jones:** in here. Basically, knowing what your assembly house might typically have, and if they've only got one of these machines, then what what what what you can come a gutser on this board already, even if they have two of these

**Dave Jones:** machines. You can come a gutser already. Why? Because, if you go down here, it actually supports If you go down here and check out the specs down here, here it is. It's got a maximum of 80 feeders. Now, you've seen these before. These are

**Dave Jones:** reels that your components come on. All your resistors, capacitors, diodes, transistors, your ICs, and even your battery uh holders, for example, your CR2032 coin cells. They all come Everything pretty much comes on reels. You can get trays, but let's not worry about that.

**Dave Jones:** Now, these have to go into a feeder into the machine. And you can physically see these feeders up here, and these are cassettes that they that hold these reels and insert. So, they've only got a maximum of these feeders, but aha, fine

**Dave Jones:** print, 8 mm tape width uh type. So, this is an 8 mm type uh one which holds, you know, typical resistors and capacitors. And it can only hold a maximum of 80 of these in the machine, or even less if

**Dave Jones:** you have wider parts, like a like a CR2032 battery, for example. That could be like a really wide tape, and that'll take up several slots in there. So, what that means is that your assembly uh line that you're using at whatever manufacturer

**Dave Jones:** will be limited to how many of these reels they can hold. So, if your design here has more than 80 parts, absolute maximum for that particular uh machine, then it's not that you can't get it manufactured. It's just that they'll

**Dave Jones:** have to put it through multiple passes. Then they'll have to either use different lines, or they'll have to have two of these machines in series. It can pass through one machine, then can pass through another. And some big assembly

**Dave Jones:** houses will have multiple ones of these machines, but just remember this can be a big limitation for your design. And they'll charge Yes, they'll manufacture the board for you and they often won't even tell you. They'll just give you

**Dave Jones:** quote you a price and it's going to be a much higher price to assemble your board cuz they know they have to pass it through two or three times cuz you're using 160 160 different types of components which

**Dave Jones:** all have to come on their own reel. But not only that, then you have to actually go out and buy and source all of these different types of parts. And just missing one part out of those 160 parts,

**Dave Jones:** you might not be able to get your product manufactured. Or you could get it almost all manufactured except for one part. So, the more parts you different types of parts you use on your design, the higher the risk, the greater

**Dave Jones:** the potential assembly cost, and like all sorts of issues to do with that. So, reducing the num- different types of components is what we're talking about here in terms of BOM optimization. You want to minimize the number of different

**Dave Jones:** BOM items Bill of Materials, by the way. I've mentioned that, have I? Bill of Materials different BOM items that you have, the different parts. There's huge advantages to doing that. And the bigger and more complex your boards get, the

**Dave Jones:** more important this becomes. So, we talked about like three different potential ways to do this. The first one is value consolidation, which is generally you might get this for resistors and capacitors. There's other components as well, but they're the two

**Dave Jones:** biggies that you want to consolidate. Now, look at this. How many different types of capacitors do they use in this design? Let's have a look. It starts at component number one here. These It's good that they've all sorted them by

**Dave Jones:** capacitors. 26 different types of capacitors. Some pick and place machines might only support 40 reels. We've already taken up half of our reels our reel space just with capacitors. There is no way and this is by the way I'm not a sledging the

**Dave Jones:** designers of this a thing at all. They just didn't bother to do bomb consolidation. There might be reasons they only wanted, you know, 100 of these made. Yeah, it didn't matter, right? Um just the design cost of and getting the

**Dave Jones:** manufacture was nothing compared to but if you wanted to make a 100,000 or million of these things, you don't want to be having 26 different types of capacitors. That's just nuts. So, we want to go in and do some bomb

**Dave Jones:** consolidation. Look and check this out right off the bat. We've got one capacitor 11 puff. 11 puff. Why? When we've got another one which is 13 puff. We've got one of those. We've got one 16 puff capacitor. We've got one

**Dave Jones:** 24 puff one two 18 puff. Come on. You can't tell me that you need precisely 11 picofarads and 13 picofarads. That is ridiculous. The capacitors are going to be 5 10% tolerance anyway. So, the difference between 11 and 13 puff.

**Dave Jones:** Now, look if you're doing a complex RF design or something like that, then yeah, okay, that could matter. But in a lot of cases, you're just going to choose these values because they came out of an application note or it's what

**Dave Jones:** came out of your calculator. For example, you might want to okay, I want like a 1 MHz filter for example. You do your calculations and it comes out to 11 picofarads or 11 nanofarads or whatever it is and or a resistor value of, you

**Dave Jones:** know, 6.25 K. So, you choose the, you know, closest E96 preferred value to that. Well, you don't really have to. So, you really should as part of this optimization process this bomb optimization is go about look at your

**Dave Jones:** design and just think critically. Like really, do I need an 11 picofarad? Couldn't I have used a 13 or maybe a 16 or maybe even an 18 picofarads? I mean, you know, come on. Right, so let's go into the schematic here and have a look.

**Dave Jones:** C92, there it is. C104, 11 picofarads and 13 picofarads. Where's it What's it used for? The power supply. Look at this. Look at this. The power supply, a switching power supply. That's it, 1.2 volt power supply and they've

**Dave Jones:** determined that they need 11 picofarad capacitor and an 8.87 K resistor. I mean, this is just silly stuff, right? There is no way you need that precision in a compensation network for a just a switching regulator. Obviously, these values have

**Dave Jones:** just popped out of the confuser here and they've just whacked them in there and said, "All right, all right, all right, we need 11 picofarad capacitor. We need a 13 picofarad capacitor." Like, give me a break. No. Go back to the data sheet

**Dave Jones:** here, TPS65400. This is an exercise for those playing along at home. Go into the data sheet and actually have a look at where it It'll It'll probably give you the equations for calculating the compensation values and things like

**Dave Jones:** that. Is it that critical? The answer is almost certainly no. You could easily consolidate these two values here, which are the only ones used in the design. It's the only place it's used and you've got to take up a whole You've got to go

**Dave Jones:** buy a whole reel, then your purchasing officer has to then go and purchase these from somewhere. You've got to find them in stock. They may not have them in stock. It could It could, you know, screw up your entire

**Dave Jones:** production schedule just because you decided you needed 11 picofarad cap in there. Now, this is not uncommon in the industry. It's happened to me many times. It's where the purchasing officers, and yes, large corporations will have purchasing officers. Their

**Dave Jones:** sole job is to buy all these source and buy all these parts for the new uh you know, for the latest production run of your widget that you're trying to actually produce. And they will often come to you and say, "Look, I cannot for

**Dave Jones:** the life of me get an 11 picafarad capacitor in an 0603 footprint. The whole world's out of them. I've scoured all I scoured the gray market, cannot find them. Can we have a substitute?" And a good bill of materials will also

**Dave Jones:** have like a substi- like different brands. In fact, it was company policy at companies at some companies that I've worked at, you would have special like military type ones where you'd have three different manufacturer part number variants. So, you'd have three choices

**Dave Jones:** so that the purchasing people can go and choose any one of those values, and it doesn't matter, they're fully qual- that part was fully qualified for use in the design. But often they'll come back and they'll go, "Look, I cannot get this.

**Dave Jones:** Can I use Can I buy something else?" And you might have to do an engineering change request or whatever it is to go, "Yep, look, I authorize to use a 13 puff capacitor in there instead of 11 puff. I

**Dave Jones:** was just lazy when I designed it and it doesn't matter a rat's ass that it's 11 picafarads or 13." Now, values like these ones, for example, this obviously sets out what the value our 1.2 volt voltage reference. So, these values are

**Dave Jones:** fairly the ratio of them is fairly critical. But you could actually put in a 10k here, like a 13.3k, okay? And yes, 13.3 here, if we go to 1.33, is a both is all three columns here is an E48, E96, and E192 preferred value.

**Dave Jones:** So, you can actually get that value, but like should you actually be using this? Now, generally when I'm doing a design like this, I will go, "Look, I'm going to use a 10K as this bottom one, and then I'll calculate

**Dave Jones:** the top one, and then I'll figure out what you know, then I only need to get one oddball value up here instead of two oddball values." And here's the next thing, with value consolidation, it can actually be better and cheaper

**Dave Jones:** and more beneficial to use more resistors in your design than to choose the right value and have to get another complete reel and have another individual bomb item. For example, this is a classic example of it here. Well,

**Dave Jones:** you need a specific value to meet your tolerance of your 1.2 V voltage rail here. Now, just for argument's sake, let's say that you chose a 10K resistor here, for example, and you did your calculations and found that your 1.2 V

**Dave Jones:** within whatever tolerance you required, a like a 4.99K, for example, or five Let's say it popped out at 5K, or even 4.99. What do you do? You don't necessarily go and just buy yet another reel just for that one

**Dave Jones:** value. It takes up another slot in your pick-and-place machine, more bill of materials items, when you can just put two 10K resistors in parallel. You've reused one of your parts here, and sure, you've put in an extra resistor, and sure, it's more board

**Dave Jones:** space, and sure, that might be important if you've got a real ultra-dense design. You may not have the luxury of being able to put two resistors in parallel. I mean, you know, probably the majority of cases in practice, you are going to have

**Dave Jones:** the room to put in the two 10K or make room. A good PCB layout designer can always make room for that extra resistor, just so that you reduce that one extra bomb item. And you can do this again, 16 puff up here, 1.2

**Dave Jones:** 1.5 nF. You know, couldn't we have used 1.2 nF? Look, do we have to use 11k here and 11.3k here? Really? So, this is a really good example and it's why I actually picked uh the when I saw this

**Dave Jones:** project, I just picked it like a random and complicated one. And when I saw this, I went good example, you know, lots of different parts in the bomb. So, yeah, just go through, read your data sheets again, go through your calculations,

**Dave Jones:** reevaluate, do your engineering evaluation, and all the stuff that goes along with qualifying your design and everything else. And you know, almost every project I've ever done, there might be the odd exception, but the vast, vast majority, I've been able

**Dave Jones:** to bomb optimize in some way when it comes to uh capacitor and resistor values. And then if we just uh quickly look at uh some of the uh memory on here, look, we got termination resistors 40.2 ohms. Yeah, we've got a lot of

**Dave Jones:** them. That's fine. This is obviously popped out of their uh polar impedance uh calculator or whatever it is they use to uh calculate the transmission line impedance. We've got 80.6 ohms here, for example. Uh not sure what that one's doing at uh you know, 240

**Dave Jones:** ohms and things like that. So, all these oddball values will pop out of your confuser here, but don't necessarily blindly follow them. That can lead to you know, a bomb like this one, which hey, as I said, if you're making, you know, 10 or

**Dave Jones:** 100 of these, you just might not care, you know, it popped out. I couldn't be bothered spending another minute. I was on a tight deadline. I needed to design this thing, you know, and just you know, throw it out out the door. And it it's

**Dave Jones:** fine. The manufacturer will do it, the purchasing people will purchase them all, and Bob's your uncle, but there can be huge value in just spending like a few hours. It's not, you know, it's like a this design here. Sure, okay, I might

**Dave Jones:** spend a whole day like uh checking this, you know, pull up the data sheet for this. Do we really need our 10.7k in there and things like that, you know? And so, yeah, I you might spend a day

**Dave Jones:** just tidying up this, but they obviously spent months designing this thing. And well, and there's some argument over when you might do this. Some people might actually Okay, go and, you know, the number pops out of your confuser.

**Dave Jones:** So, that's what you put in your schematic. And then And I've done this myself, and there's valid arguments for it. Is once you've done that, then generate your bomb, and then go in and see if you can optimize the bomb. You

**Dave Jones:** can actually do it right at this schematic stage, you know, while you're designing you know, I'm going a 6.81k so anywhere else. So, I'm going to put two resistors in series or parallel to get, you know, near enough a value or

**Dave Jones:** something like that. So, you could argue that it's just it's better to do as a separate pass because then you're not bogging down your design process. You're getting the design down first, and then Breathe in, breathe out. I've finished

**Dave Jones:** my schematic. Okay, let's, you know, you go get your extra coffee or whatever chocolate or whatever it is you need to keep going, and then you go do your second pass bomb consolidation. So, that's the first part, consolidating

**Dave Jones:** your values, mostly resistors and capacitors, but some other parts. Now, the second part is parts consolidation. Where Well, do I really need that part, or can I reuse that part somewhere else? Not just the value, but the actual

**Dave Jones:** component itself. Now, I'll link it in. I've done a video on Muntzing and a bypass capacitors visualized like Muntzing Mad Man Muntz back in the day used to be famous for carrying around a pair of side cutters. And whenever one

**Dave Jones:** of his designers of one of his analog No, this digital rubbish. Analog TVs I finished my design. They showed it to Mad Man Muntz. He'd come around with his side cutters and start snipping out components one by one until

**Dave Jones:** it stopped working. And when it did stop working, he put that last component back in and go, "Right, toss those parts out. We obviously didn't need them." And that's Muntzing. And it is actually a real thing. And one thing where it

**Dave Jones:** really comes in is bypass capacitors. I've shown that I'm not going to say that are they really needed. In most cases, no. It's just general rules of thumb where if you haven't analyzed your power system and it can be quite complex

**Dave Jones:** to do this requiring real sophisticated software and you know, specialized software to do it. Do you need all of these bypass capacitors? Do you need a 10 micro, 1 micro, 100 and a 10 and a 1 and all on the power pins for example.

**Dave Jones:** FPGA data sheets for example like I'm sure go check up the data sheet for the Zynq FPGA using here. They've probably got an application note just dedicated to bypassing. And you can go over here to Maxim for example. There's Xilinx and

**Dave Jones:** there's Altera and other FPGA manufacturer app notes on this power supply solutions for Zynq FPGAs for example and how like you need X amount of bypassing and the impedance curves and why you need all these different values and and like you know, power up

**Dave Jones:** surges and things like that. And you know, there's all sorts of stuff involved in it's it's endless. It really is endless. Anyway, the point is do you need all of these capacitors here? The answer is almost certainly not. So while they're

**Dave Jones:** all but they're all the same values. So but still even when you have if you use too many capacitors, you're even though you got might have 4,000 on a reel. You know, you manufacturing a lot of boards per

**Dave Jones:** hour. Your reels can run out earlier and then somebody's got to you know, a red light flashes on top of the machine. Quick, I've got to stop the whole production line is stopped because you ran out of your 10 nano farad capacitors

**Dave Jones:** cuz you used 10 bazillion gazillion of them on your machines. Somebody's got to come around and replace the reel and to start up the line again. So you know, and they cost money especially like you're using the more expensive 1 mic and uh 10

**Dave Jones:** microfarad uh ones, for example, they can uh be expensive uh parts, but often, yeah, you can do some months in and you can get away. But sometimes you won't know this at the design stage. You might just play it safe and go, "Look, I'm

**Dave Jones:** just going to belt and braces. I'm just going to put in my 10 microfarads, my 1 microfarad, and my 10 ends, and you know, she'll be right." But there are some gains to be had here by months in uh

**Dave Jones:** something like this for volume. And then that might come down to here. Look, oh wait, we've got three 330 microfarads down here. You know, you might have used a 100 microfarad somewhere else. Could we have used, you know, uh the 330s

**Dave Jones:** somewhere else where we used our 100 microfarads or whatever or for, you know, a complex as FPGAs are often complex, you know, they have five, six different power supplies. That's not uncommon at all uh for a design like

**Dave Jones:** this. And you know, can you optimize the number of parts? Now, this isn't the best uh design for this, but uh talk about uh transistors, for example, if you you're doing a lot of uh like switching in your design or whatever and things

**Dave Jones:** like that, well, you might be using like a different types of transistors for different reasons. You might need, "Oh, this one's slightly higher, you know, I need more current for this one." Well, can you actually consolidate these parts? You know, if you've got a

**Dave Jones:** high-power transistor here that might cost uh 10 cents, and you've got another uh transistor which you you don't need the high power, but it costs 8 cents. Like, do you actually need to save that 2 cents and then have a whole extra reel

**Dave Jones:** and go and source it and take up uh space on your pick and place machine just because um you didn't want to reuse this 1 amp uh transistor, for example, where you only needed 100 milliamps and you chose another uh transistor? Like,

**Dave Jones:** can you reuse parts like that? Diodes are another classic one, for example, where you might use a uh 1 amp diode on your input, for example, some sort of clamping or protection, uh reverse protection or something, and then you might need

**Dave Jones:** another diode in your design. Do you actually need that to be a 1N914 or some other, you know, a signal diode? Can you actually reuse that same power diode? Try and consolidate your parts and reduce the number of line items on your

**Dave Jones:** bomb. Now, the third type of optimization, once again, it's another design for manufacturing technique. We have to go back to our pick-and-place machine, is consolidating footprints. Now, this one actually Look, this one has Yeah, I think Look Look at these

**Dave Jones:** 0201s. What a pain. Do you really need 0201 capacitors? Look, these 1 microfarads. Do you really need 1 micro 0201 footprints? That's ridiculous. That's half the size of an 0402, which is already small. Do you really need that?

**Dave Jones:** Do you really need even need to go to 0402s? In this particular case, yeah, they probably do. But in a lot of cases, you can actually uh pay more to get boards assembled because they've got 0402s. And it might

**Dave Jones:** also limit the number of manufacturers you can use, especially local manufacturers. Uh for example, let's go back uh to this uh Yamaha machine over here. It's really expensive, like kind of like one of the top of the line uh

**Dave Jones:** jobbies. Yes, it can do 0201, right? So, you know, you might think, "Okay, I can use 0201 resistors on my design." No, don't. Look at the fine print, okay? Let's go over to here. They've got different types of heads. The ultra

**Dave Jones:** high-speed head, for example, yeah, it can do 0201 parts, but they physically have to change the head on the or use a different head on the pick-and-place machine to actually do that. And the reason that the smaller parts can uh go

**Dave Jones:** faster is because they've got less mass. They can pick them up, zoom, all around the board. They can move them faster because then they won't fall off because of the mass of the parts just being held on the nozzle by a vacuum and

**Dave Jones:** the heavier the part is the slower their head has to move. You've got a a giant big power resistor. It has to suck it up and then clunk clunk clunk clunk clunk move it over place. But an 0201 goes

**Dave Jones:** That's it. Done. So this is where the multiple heads and look at this the flexible head here for example 0603. So if you do all of your design with 0603 footprints, they can use this flexible head although they and there's lots of

**Dave Jones:** pick and place machines out there that will only go there especially older ones and you know the cheaper ones are used in you know some local manufacturer or something like that who's not really high-end. They might be limited to 0603.

**Dave Jones:** They might be able to do 0402 for you but there's actually going to be a lot of wastage. So your manufacturer might actually tell you like allow 5% or 10% for wastage for example especially on like a smaller parts and if you

**Dave Jones:** especially if you're using semiconductors like or chips like real tiny little packages they might actually be expensive little devices and or yeah really high precision resistors for example. You can pay a dollar for a high precision like a really good high

**Dave Jones:** precision low tempco resistor for example. So like if you choose a real ultra tiny one and there's 5 10% wastage that's going to add up to your assembly cost. So they might say okay we need 3,000 of these parts but give us a real

**Dave Jones:** 4,000 because we're going to like waste a lot of them. And there's a waste bin on the pick and place machine where all these fallen components just drop off and fall into. So this is why if I was

**Dave Jones:** designing this and I looked at this bomb I was doing my bomb consolidation this one sticks out like a dog's hind leg. 0201 isn't the only 0201 part I know is other one okay so they're using some others but you know like it might stick

**Dave Jones:** out sort by you know package type or whatever, and you might it might pop out, "Oh, look, you're like we're using 10402 in this entire design." Really? Do we have to? Can we Can't we just use an 0603, please? So, just going that one

**Dave Jones:** part under a certain size could cost you, you know, a lot of heartache and a lot of money as well, as well as going one part over the number of reels that your assembly line I can actually support. That can add up to a lot of

**Dave Jones:** heartache and a lot of extra cost as well. And they often won't tell you this. They'll just happily accept your project and go, "Yes, we can assemble that. No worries." And they'll give you a quote, and you won't even know that

**Dave Jones:** they're charging you more. So, as I said, we won't get into the fourth one, which is BOM optimizing for cost. Although, I've got a video which might come up. Let me know if you want to know see a video on a 1-cent voltage

**Dave Jones:** regulator. Is it any good? I'll just going to play around with it and see 1-cent voltage regulator can actually do the business. Anyway, let me know. You give us a thumbs up if you want to see that. Leave it in the comments down

**Dave Jones:** below. But anyway, there's so many more ways that you can optimize values in designs like this. For example, like we've got an I squared C line here. That's going to have certain pull-ups in the lower value pull-up for your I squared C line, the

**Dave Jones:** higher speed because it's an open collector output. The higher the slew rate the faster the slew rate, for example, and the more speed you can get out of your I squared C bus. So, if your you know, Confuser popped out the value of

**Dave Jones:** like 1.8K for your pull-up, well, do you need and you don't use 1.8K anywhere else? Well, why not use a 1.5K? Yeah, might use a bit more power, for example, and that might be a trade-off that you have to go

**Dave Jones:** through your design. This is all part of engineering. Yeah, can I trade off the extra power for the 1.5k pull-up resistor even 1k pull-up resistor versus the calculated 1.8k pull-up that I thought I could get away with? It might

**Dave Jones:** be worth it cuz it save an extra reel. And this video actually was originally going to be me just going through like a dozen different open-source designs on the market and just looking at all values and actually going into the data

**Dave Jones:** sheets and and trying to calculate, you know, can we get away with certain values? LEDs are another classic example like you might calculate, okay, I want 10 milliamps to go through my LED, it's going to be like a pretty bright one. I

**Dave Jones:** want 10 milliamps in there. Well, and you can fuse a pop set the value, well, I need a, you know, 680 ohm resistor. Well, I don't know. Can you get away with like does it have to be that exact

**Dave Jones:** brightness? Can you get away with a little bit more, little bit less to consolidate your bottom items? Anyway, let me know down below. If you do want to see that video where I actually go through a bunch of designs and actually

**Dave Jones:** spend hours and hours actually looking at the data sheets say for this and you know, figuring out do we actually need that value? Do we need precisely this? But yeah, I decided just to show you the or in this case three different ways

**Dave Jones:** to consolidate your bomb. And yeah, it's not applicable or designs you may never get to that stage where you need this, but hey, if you want to level up your skills in electronics design, then bomb consolidation can be a vital step in

**Dave Jones:** part of your design for manufacturing just an essential step in your design. You draw your schematic, you do your bomb consolidation, then you do your ESC and then you lay out your board and then you do your other design for

**Dave Jones:** manufacturing stuff and it's all tied up in there whichever order you want to do it, it can be really important. So anyway, hope you found that useful and if you did, please give it a big thumbs up and

**Dave Jones:** as always comment down below especially like what things have you up to what other things have you optimized in designs where you know look as marginal and I really I had to actually seriously it may pay you to

**Dave Jones:** actually spend like a day or two's engineering effort actually building up a prototype of this and testing it over temperature and stuff like that just to verify that you know the value you chose can actually work even though it's you

**Dave Jones:** know it might be slightly outside the margin and you might try some tolerance resistors you might even do some Monte Carlo simulation analysis which is Monte Carlo analysis in simulation. I've done a video on that I think I might have.

**Dave Jones:** Try and find that. Is where you can like test your design for different values like you know spreading your values like 5% you know 1% tolerance resistors it'll you know go plus minus 1% and rerun the simulation and tell you

**Dave Jones:** if it's not going to go tits up on you and things like that. Anyway, leave it in the going for hours. Leave it in the comments down below what stuff you've optimized. Have you really saved some you know big cost or big headache by

**Dave Jones:** doing the bomb optimization or do you just never bother? Let us know. There's valid reasons for just like in this particular case they didn't bother. It's a very clear this is one of the you know one of the most amazing

**Dave Jones:** examples I've seen. You can tell nobody's even bothered to bomb optimize this and that might be fine. So nothing against the designers of this thing there's valid reasons why you wouldn't bother but if you're going to take this

**Dave Jones:** in a high volume production I would not go into high volume production of this board with this bomb like this. I find it highly offensive. It's just no. I would not over my dead body this thing's going into production with all

**Dave Jones:** these different with like 76 minus 27 49 different value resistors 49 reels of resistors on this thing like no. No over my dead body that's going into production. And I hope you feel the same way, cuz that's that's the engineering spirit.

**Dave Jones:** Catch you next time.
