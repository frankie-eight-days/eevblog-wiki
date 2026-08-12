---
video_id: kcxw850YpVc
title: EEVblog #517 - Car Airbag Controller Teardown
url: https://www.youtube.com/watch?v=kcxw850YpVc
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 34, "3": 48, "4": 63, "5": 81, "6": 101, "7": 114, "8": 129, "9": 148, "10": 159, "11": 173, "12": 185, "13": 202, "14": 215, "15": 228, "16": 242, "17": 254, "18": 269, "19": 282, "20": 295, "21": 307, "22": 325, "23": 343, "24": 360, "25": 373, "26": 388, "27": 403, "28": 419, "29": 434, "30": 448, "31": 460, "32": 473, "33": 487, "34": 503, "35": 515, "36": 527, "37": 542, "38": 557, "39": 573, "40": 588, "41": 602, "42": 618, "43": 630, "44": 644, "45": 661, "46": 680, "47": 702, "48": 713, "49": 724, "50": 743, "51": 758, "52": 778, "53": 794, "54": 812, "55": 826, "56": 840, "57": 858, "58": 874, "59": 888, "60": 907, "61": 921, "62": 938, "63": 954, "64": 969, "65": 990, "66": 1013, "67": 1036, "68": 1055, "69": 1074, "70": 1091, "71": 1112, "72": 1127, "73": 1144, "74": 1158, "75": 1173, "76": 1191, "77": 1206, "78": 1225, "79": 1244, "80": 1259, "81": 1275, "82": 1289, "83": 1307, "84": 1320, "85": 1340, "86": 1355, "87": 1369, "88": 1383}
---

**Dave Jones:** Hi, welcome to tear down Tuesday. This one has been sitting on my tear down shelf for quite some time. It came in a quite an old mail bag episode. Now it come came from Joey in the UK. So thank

**Dave Jones:** you very much Joey. It is an airbag control unit from a fairly recent model Hyundai car that has seen better days apparently. So this could be a really interesting and for those playing along at home, there's the part number there and

**Dave Jones:** there's another well it's manufactured by TRW. That's the TRW part number and works on a 12 volt system and we'll have a look at how an airbag controller works. Although I'm not sure how much we're actually going to be able to glean

**Dave Jones:** from this thing, but one thing we do know for starters here is look at this forward arrow here. Obviously that is designed to indicate that the unit must be installed in the car in a certain way cuz airbags only activate with a

**Dave Jones:** basically pretty much a front on front on collision or at a certain angle to a front on collision like that. So obviously that means it's going to have an internal accelerometer or sensor in there to you know some sort of inertial switch or

**Dave Jones:** something to detect that to detect the crash. But I believe old model airbag controllers, they did use mechanical inertial inertial switches or something like that. Some sort of mechanical device to detect it, but all the fairly modern ones including

**Dave Jones:** this one I'm sure use a MEMS accelerometer. So that'll just be mounted on the PCB or it could be mounted on its own PCB and there or something like that. We won't know until we take it apart, but I also believe

**Dave Jones:** that that's not the only sensor in the car for activating these airbags. Don't quote me on this, but I believe there are other especially in these modern cars lots of other sensors mounted around the car. So, it requires

**Dave Jones:** multiple sensors to be activated before this thing will actually blow the airbag. And like passenger passenger detection switches and all sorts of you know weird and wonderful sensors all placed around the car and lots of algorithmic control inside this thing.

**Dave Jones:** Now, I've already I've showed a preview of this in the mailbag before. I've already taken off the metal backing plate from this. It just came off with a couple of screws. I don't have that anymore, but it's gone and clearly we've

**Dave Jones:** actually got quite a few connections on here. So, obviously you know it there's quite a bit of data coming in and out of this thing. And as I said most likely a lot of those are coming from other sensors within the

**Dave Jones:** car. So, we're going to have to try and lever this board out. I think we might be able to lever it out. And these pins are really quite interesting. As you can see they are not soldered. They are actually

**Dave Jones:** press fit pins which as the name implies you just press these connectors into the PCB and they just hold themselves in place with friction. Now, you might think you know airbag controllers have to be ultra reliable pass many stringent

**Dave Jones:** you know approvals and type testing and things like that. And you might wonder how the hell they can get away with not soldering the pins like that. Well, as it turns out these press fit connectors are actually incredibly

**Dave Jones:** reliable, but there is a lot of art which goes into getting them right and making them reliable. So, the exact diameter of the pin hole the the plating and all that sort of stuff in the hole and getting just exactly the

**Dave Jones:** right pressure on those little press fit pins down in there. There's you know, a lot that goes into that. And uh yeah, they would have had to have that approved. Much vibration and shock testing and all sorts of stuff goes into

**Dave Jones:** that. But yeah, trust me. You find these in a lot of uh ultra-high reliability industries where they don't actually solder because solder joints can be uh brittle. They can crack under stress and vibration and stuff like that. So, it

**Dave Jones:** can actually be more reliable to have these press-fit connectors. And they've got another one over there. And they've got another big device underneath. I'm not actually sure what that is. And that's got a few press-fit connectors as well. And

**Dave Jones:** you can actually see that looks like a um some sort of programming uh port, something like that. Whether or not it's a JTAG port or whether or not um maybe it's designed for getting the data out cuz I believe these airbag

**Dave Jones:** units contain an E-squared PROM in them. Uh they actually store the data from any uh incident, i.e. crash. You know, so that the investigators can come along, read out the data, see exactly, you know, somebody's killed by an airbag or

**Dave Jones:** something. Obviously, you know, there's going to be an investigation. They'll get the data out of it and stuff like that. So, um I'd be surprised if uh there's not an E-squared PROM inside here somewhere. And probably a a

**Dave Jones:** reasonable amount of uh processing power as well. As I said, there's lots of uh proprietary algorithms which go into these airbag controllers these days. And uh I'm not sure if this thing is going to prise out. Oh, yeah.

**Dave Jones:** Yeah, no. I thought maybe we might have to prise out the connectors of the pins. But hang on. Hey, no. That's That's coming out pretty easy. Pretty easy. Yep. Yep. No problem. Ta-da! Oh, we're in like Flynn. Look at that.

**Dave Jones:** Hey, look at that huge Look at that huge cap on there. That's uh uh rather surprising and the board is conformally coated. You can see that all around here. You can see the I get the right angle of the light, you can really

**Dave Jones:** see that. It's not completely dipped. They haven't completely gone and dipped the entire board in conformal coating. Like there's no conformal coating over Well, the top of this chip here and uh and the cap and everything else. So,

**Dave Jones:** they've um clearly Someone's gone over that with a uh brush and just brushed on that conformal coating. Conformal coating is very common in uh in in a ultra high reliability uh device like this because it keeps out the

**Dave Jones:** moisture and uh from the board and uh ensures that it works over a huge um range of climates because uh you know, uh who knows what climates these uh airbags in different countries and things like that. Um many different

**Dave Jones:** varying climates. But uh yeah, it's not a full conformal coating. I'm a bit surprised that it's hasn't been completely gunked actually, but uh the big capacitor there, that's rather interesting. That's obviously that device Yeah, that's the device on the

**Dave Jones:** bottom that had the press fit pins. There's no electrical connection on those ones, but there's the two pins for the cap there and uh they've gone to a lot of trouble to mount that cap in its own big custom housing. It's

**Dave Jones:** not very long. It's not as long as the entire thing. Um or maybe they ended up putting a shorter cap in, but could certainly fit a longer cap in there. And what that's for my guess would be um well, it's you

**Dave Jones:** know, it's obviously not for regular power supply smoothing, right? You can bet your bottom dollar on that. When you've got a capacitor that large, it stores a massive Well, quite a large amount of uh energy. And uh what that

**Dave Jones:** energy is used for either either it's directly on the supply rail, it's actually powering the supply rail and then if there's a power fire in the car, there's still enough power on the rail to keep the circuitry going to blow the

**Dave Jones:** airbag. Or whether or not it's just the energy storage device that then, you know, cuz it needs some extra grunt perhaps to blow the airbag. But that's not likely because we're in a 12-V automotive system. We've already got,

**Dave Jones:** you know, a big low impedance 12-V path coming from the main vehicle supply. So really, you know, you don't need it. So I reckon that's most likely reason for that is a backup. You know, is to a supply the power to

**Dave Jones:** all this to keep it going after the crash because after the crash, as I said, you have to write to that E-squared PROM as well. That would be a you know, that would be a requirement of these modules probably to pass type

**Dave Jones:** approval and things like that. They've got to you know, that cuz in a crash you don't want to crash and then all your wiring going to this thing gets severed and then you lose power and it doesn't have time to write the data to the

**Dave Jones:** E-squared PROM or something like that. I don't know, it's unlikely. It doesn't take much time to write, but maybe that's part of the probably stringent requirements. If anyone has any data, you know, documents on the requirements for these airbag controllers, then

**Dave Jones:** please post it cuz I'm sure a lot of people will be interested in the red tape which goes behind getting one of these things approved. I can't see any type of approval marks or uh anything like that. But of course they

**Dave Jones:** would very well be. And that may be another reason why this capacitor is in its own little protective cage like that is that there's going to be some shock uh uh there's going to be shock some shock protection inside that. I mean, they've

**Dave Jones:** got the leads, you know, there's going to be some compliance in the in the leads there and in this plastic housing. So in a big accident like this, they're protecting the capacitor as the supply of the voltage to this airbag controller

**Dave Jones:** to ensure that the charges blow on the airbags and that that crash data is written to an e-squared prom in here somewhere. And the other thing is I'm quite surprised at the amount of processing in this thing. I thought it

**Dave Jones:** would have a bit, but uh yeah, we've got a large quad flat pack, another one under there. We've got quite a few QFN type packages around here by the looks of it. Uh there's an eight-pin SO, that could be the e-squared prom perhaps.

**Dave Jones:** Um but yeah, let's take a closer look at the board. Missing device over here, don't know what's going on there. I'll tell you what, that capacitor took some prize in out, that's for sure. It's even got its own little uh

**Dave Jones:** barcoded part number on there. And another eight-pin SO, maybe the crash data inside there perhaps, but there we go. We can get a good look at all the components now. And the connection for that capacitor looks like it's some uh

**Dave Jones:** maybe welded stud or uh something like that. It's uh hasn't just been uh soldered onto there, that's for sure. And the capacitor in that, uh as you expect, not a one-hung-low brand. It's a Nippon Chemicon uh brand, you know, basically one of the

**Dave Jones:** world's best capacitors. Uh 8400 microfarads, 25 volts. And it's an LGB series, and I went and looked that up, and sure enough, this is a specific series of capacitors designed for airbag applications. There you go. Um so probably much more uh stringent

**Dave Jones:** manufacturing or uh testing requirements or something like that, maybe some extra uh shock and vibration resistance, and I don't you know, a 105°C uh temperature rated. But, um, yeah, specifically designed for airbag applications. Interesting. Now, unfortunately, the conformal coating might make it very

**Dave Jones:** difficult to read some of the part numbers here, but, uh, I'll have a go and I'll probably try and scrape it off if I have to. I'm not going to have time to, you know, use any, uh, solvent to

**Dave Jones:** try and get rid of it or or something like that. So, if I can, uh, read them at a certain angle under the, uh, microscope with light at a certain angle, then I'll try and do that. Otherwise, I'll scrape it off.

**Dave Jones:** And the main processor down in there, well, no surprises. It's a Renesas part. Renesas, uh, the number one microcontroller manufacturer in the world because they, uh, almost dominate the automotive market. Well, they got a massive share in the automotive, uh, microcontroller

**Dave Jones:** market. And, uh, it's a H8, uh, SX 1725 series. And well, you go look at this one up. I'll provide the links below for these things, uh, if you want to check out the, uh, data sheets and, uh,

**Dave Jones:** websites for these. But, I found a press release, uh, for this, uh, series, the 1700 series, from, uh, 2007, saying this one is specific this series specifically designed for in-vehicle control application and airbag controllers. So, there you go. Um,

**Dave Jones:** another example of where the automotive industry has such clout that, you know, in terms of volume and, uh, you know, um, profit margin and stuff like that, that these companies bend over backwards to design specific chips and specific

**Dave Jones:** series. And, as you saw, a specific type of capacitor directly for these applications. They target them precisely. Unusual. It's a two-pin package. One large pin on the bottom there and one uh, J lead coming out the side there and

**Dave Jones:** it's probably some sort of diode or something like that. Can't see any type markings on the top through that bubbly conformal coating, but yeah, most likely some sort of big ass diode. Look at the huge pad on the bottom and how it's

**Dave Jones:** heatsink. And there's just a little four pin data line choke there to keep all the crap off the data line coming from wherever it is coming from. I don't know, but yeah, probably part of the CAN bus there.

**Dave Jones:** And this one took a little bit of finding. It's a TLE 8760V and as you can see by the components surrounding it, the big inductors, all the caps, all those passive parts, it's obviously something to do with the power

**Dave Jones:** supply and sure enough, it's an Infineon part once again specifically designed for automotive applications and the example application they're showing their brochure for this thing. Couldn't get a data sheet, but I got a you know, a sales brochure on

**Dave Jones:** their automotive stuff specifically for airbag control systems and it is a power management controller pretty much. It's got a boost It's got a buck converter in there. I think it's got two boost converters. It's got a linear reg in

**Dave Jones:** there. It's got reset watchdog system all in one chip. But once again, specifically designed for the automotive market. And here's Infineon's airbag system solution from their glossy brochure which they give to all the car company executives and design teams.

**Dave Jones:** And there it is. That's what we just looked at, the TLE 8760 and maybe there's other TLE parts in here as well. I mean, these are the squib drivers for the airbags. You can see how tied in these things are. I

**Dave Jones:** mean, look, there's, you know, buckle switches down here, pressure sensors over here, accelerometers and many accelerometers come in here. That's a they've got a an interface chip specifically for that. And of course, they're pushing their own Infineon pushing their own MCU here. I'm not sure

**Dave Jones:** how many how many design wins they get, but I'm sure they get enough. But, that's what's inside their particular airbag ECU solution. But, it seems like TRW have gone for a mix at the very least just at the components we've looked at so far.

**Dave Jones:** They've gone for a main Renesas CPU and then some Infineon stuff around that at least one part. And there's probably wouldn't surprise me if there's a few more Infineon parts in there or Renesas parts perhaps. The part number on that

**Dave Jones:** second largest quad flat pad part there I That's tricky. But, it is quite easy if you view this through the microscope at shallow enough angle with the light. There we go. It's an ST part. And I can't find any data on that one again at

**Dave Jones:** first search. It's got 155457-2 MSA84DC. 99140V6 version 6 perhaps. I don't know, but it's definitely an ST part. And bingo, we have ourselves the accelerometer down here, but I'm surprised that it's two separate devices. It's not just a one

**Dave Jones:** MEMS accelerometer. We've got ourselves two. These are Freescale MMA 6800 series. This one here is the MMA 6821 and this one's the MMA 6856. To the data sheet. Once again, very specifically designed for automotive airbag systems. It's a SPI based two

**Dave Jones:** axis medium G over damped lateral accelerometer. Woohoo! And it's part of their Safesure system. Beautiful. Specifically tailored for the market once again. Plus minus 20 g to plus minus 120 g. Uh you know, single supply SPI uh compatible

**Dave Jones:** 10-bit digital signed or unsigned SPI output. Uh 12 low-pass filter options. Woo! 50 Hz to 1,000 Hz optional offset cancellation. All sorts of goodness down here. So, we have the 21, which is the 120 g on the x-axis, and plus minus 25 g

**Dave Jones:** on the y-axis. And check out the block diagram of this puppy. Here we go. We've got our overdamped uh y sensor and our x sensor in here. And we've got a delta sigma converter, sign C filter, uh various low-pass filters, compensation,

**Dave Jones:** linear interpolation, offset cancellation, output scaling. Ah, wonderful stuff. It's got a built-in 8-meg oscillator and digital regulators and all sorts of uh power supply stuff. And it's got its own um internal array, one-time programmable array in there. And uh this is a dual

**Dave Jones:** um axis one, but the other chip, the 6856, is identical to this except it only has the x-axis in here. It doesn't have this y-axis on the top. And that part there looks like some sort of SMD diode, but

**Dave Jones:** it's actually a 10-MHz crystal. And the remaining parts on the board are once again very difficult to find information, but I did get the uh E-squared prom. That was pretty easy. That's an STM 95256 256 K-bit E-squared prom. So, that would have the uh that

**Dave Jones:** would be storing the crash data in that thing, presumably. And this one down in here has got S5051G on it. And I have not been able to find any data on that one. So, sorry, no idea. And that one there, no surprises

**Dave Jones:** for guessing that's a CAN bus driver and that's an Infineon TLE6250G. So, they did you know, at least use some other Infineon parts on here. So, what say we rip that E-squared prom off and see if we can read it, huh? It's worth a

**Dave Jones:** shot. Well, it really wasn't nice getting that chip out with that conformal coating on it. Let me tell you, it was real difficult. I used uh some chip quick solder here and it really it was a real dog to get off. Um I almost thought that

**Dave Jones:** I killed it. Almost thought I damaged it. But no, I managed to uh get it out relatively intact and uh put it in my little SO ZIF socket here. So, let's read the contents or try to. And here it is. Excuse the lack of

**Dave Jones:** proper screen capture here. And all the top bit of it is FFFFFF. Of course, my little you know, $30 programmer actually supported this ST device. But look, we got some data. And bingo, look, null null null and that

**Dave Jones:** looks like some real data. There we go. DS2S CSP1K. I have no idea what that is, but it looks like we do have some legitimate data out of this thing. And we'll we've got some numerical sequences there. And of course, I didn't really expect to

**Dave Jones:** find anything that exciting in here. It's not like, you know, it's it's just it's um Well, as I said, presumably a part part of its function is to store the crash data in here. So, who knows about the

**Dave Jones:** contents, but anyway, I was able to read it and uh presumably after a crash, if it was involved in a crash, you could if you knew how to, you could reset the data and reprogram that chip and put it back into use, but

**Dave Jones:** jeez, that'd be pretty desperate. And there you have it. I hope you enjoyed the teardown of that reasonably modern airbag controller there. And I was a little bit surprised at the complexity of this thing, but you know, these

**Dave Jones:** modern things more and more standards, more and more algorithms go into detecting the things and stuff like that. So, you know, fairly advanced stuff in these airbag controllers and super duper reliable. And they use a lot of specific parts designed specifically

**Dave Jones:** by the chip manufacturers for the airbag market, which you know, isn't surprising in the automotive industry, but if you're not used to that sort of industry, then you go, you know, why can't they design a special chip for me,

**Dave Jones:** for my industry? Well, they do. I've worked in the seismic industry where manufacturers provide specific ICs designed just for seismic data acquisition, you know, world-leading delta sigma converters, for example, that are specifically designed for the low sample rates and

**Dave Jones:** things like that. Similar in the automotive here, although not as sort of specialized really. They you could use them as more generic parts like the main processor here, for example, isn't just for airbag controllers. That's just one of the recommended applications. They

**Dave Jones:** also recommend it can be used for you know, other dash stuff, more more generic sort of processing and things like that. So, there you go. If you do have any info on some of the parts which I couldn't identify in there, please

**Dave Jones:** leave them in the comments. And if you want to discuss it, the comments or the EV blog forum is the place to do it. If you like Teardown Tuesday, please give it a big thumbs up. Catch you next time.

**Dave Jones:** Shh.
