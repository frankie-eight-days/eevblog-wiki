---
video_id: hkbPJONJLfs
title: EEVblog #950 - Nixie Tube Display Project - Part 2
url: https://www.youtube.com/watch?v=hkbPJONJLfs
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 32, "3": 48, "4": 62, "5": 75, "6": 90, "7": 105, "8": 121, "9": 161, "10": 175, "11": 191, "12": 207, "13": 223, "14": 239, "15": 253, "16": 268, "17": 283, "18": 297, "19": 312, "20": 327, "21": 343, "22": 355, "23": 374, "24": 386, "25": 399, "26": 418, "27": 435, "28": 447, "29": 466, "30": 481, "31": 500, "32": 515, "33": 528, "34": 541, "35": 554, "36": 568, "37": 583, "38": 594, "39": 609, "40": 624, "41": 637, "42": 651, "43": 665, "44": 684, "45": 705, "46": 719, "47": 736, "48": 751, "49": 770, "50": 785, "51": 797, "52": 812, "53": 825, "54": 840, "55": 855, "56": 868, "57": 881, "58": 897, "59": 915, "60": 930, "61": 943, "62": 957, "63": 974, "64": 988, "65": 1003, "66": 1018, "67": 1033, "68": 1044, "69": 1055, "70": 1072, "71": 1086, "72": 1100, "73": 1114, "74": 1129, "75": 1141, "76": 1154, "77": 1169}
---

**Dave Jones:** Hi, welcome to part two of my Nixie tube display driver project. Uh let's have another little look at just driving these Nixie tubes cuz there's a couple of issues outstanding before we actually go into a a final solution that we make into a

**Dave Jones:** schematic and a PCB. Now, the first issue is do you actually need a high voltage driver transistor here, be it within the like the custom microchip serial array that we looked at or individual uh driver transistors or a

**Dave Jones:** transistor array like a ULN2003? Do you actually need the full compliance voltage of 170 V or like say 200 V nominal to drive these things? Well, that's you know a reasonable question to ask and I actually um answered this in a separate video on my

**Dave Jones:** second EEVblog channel uh just an hour or two after uploading my previous video. So, those of my who are subscribed to my second channel and I highly recommend you do cuz occasionally I put updates and other uh miscellaneous

**Dave Jones:** videos like that. Um I'll link that in. But uh rather than just shoot that again, I'll just display that video here for you about the open circuit voltage drop of the Nixie tubes because some people have asked uh there will be a

**Dave Jones:** voltage drop on the Nixie tubes on the pins that you aren't actually switching on with your transistors. So, all the off pins will have so much of a voltage drop on via the Nixie uh tube itself that you can get away with low voltage

**Dave Jones:** uh transistors. Well, hey. We've got some Nixie tubes. Let's measure it. Um I'm powering the Nixie tube from 170 uh volts here through the 22 uh K resistor nominal that I was going to use and people wanted to know

**Dave Jones:** what is the open voltage on the other pins, i.e. when uh they're switched off by the uh driver. And can you actually get away with a lower voltage driver, etc.? Well, let's actually uh take one here and let's go around and measure 49

**Dave Jones:** volts, 24 volts. Quite some variation. 43 Whoops. 122 Ouch. 118 69 40 47 123 odd. There you go. So, there is quite a significant voltage on there. So, 120 223 volts there on a couple of pins. Um That means that just for this particular

**Dave Jones:** Nixie tube, there's obviously great variation in this. So, I could go measure all eight. But, yeah, and you're probably not going to get this from any data sheet. So, that's the kind of open circuit voltage you need withstanding

**Dave Jones:** voltage, the voltage rating of your driver transistor or your driver, you know, transistor array or your whatever you're going to use to actually drive this thing. So, yeah, I'm afraid you can't get away with relying on the voltage drop of the Nixie

**Dave Jones:** tube itself. So, I hope that cleared that up. And by the way, if you're wondering what the voltage is when you strap all the pins together, tie them all together like this, well, you might have guessed. Let's have a look. Bingo. 125 odd volts.

**Dave Jones:** So, it basically ties it to the highest voltage drop or lowest voltage drop of any one of those particular segment display. I don't like using the word segment. One of those particular digits in there. So, as you saw there,

**Dave Jones:** we could get over 120 volts open circuit float voltage on some of those pins. Yes, some of them were quite low that you could use low voltage output drivers like a ULN 2003 or any other sort of like jelly bean low

**Dave Jones:** voltage driver transistor, but hey, some of them aren't. So, you know, we can go measure all the Nixie tubes, but hey, we've got a case where the tubes I've got in hand have up to like 120 volts and it could even be higher than that.

**Dave Jones:** So, obviously, we need driver transistors rated to that sort of voltage. But, as a few people pointed out, the classic uh 74141 driver chip, which is now obsolete, although yes, some people have pointed out that some company in Russia still

**Dave Jones:** manufactures it or something like that. I don't necessarily want to use that. I want to use a more modern readily available solution. Anyway, they pointed out that that 74141 is actually a fairly lowish voltage rating on those open

**Dave Jones:** collector output driver transistors in there, and fair enough. It's, you know, 50, 60, 70 volts, something like that. So, how can these things work? Well, if you have a look at the internal diagram for this thing, aha, look at the output pins. You can

**Dave Jones:** see that there's actually Zener diode clamps on the output. So, that's how they're getting away with it. So, what if we actually implemented a Zener diode clamping system on a more modern jelly bean driver that we have available?

**Dave Jones:** Well, the classic ULN 2003, you can do this, and we can actually use these to drive the Nixie tube displays, although there might be a potential issue, which we'll just verify here. Now, if you're not familiar with the ULN 2003, it's a

**Dave Jones:** an array of seven high voltage driver transistors. By high voltage, I mean 50 volts maximum rating. So, obviously, on their own, not good enough for driving our Nixie tubes. And inside each one is an open collector driver transistor, a

**Dave Jones:** high voltage type, but in this case, high voltage means 50 volts. 50 volt maximum rating, not good enough for our Nixie tubes on its own. But, if you have a look at the internal structure of these things, then they've

**Dave Jones:** also got a common diode array on all seven outputs like this tied together and then it goes to the common pin. So, aha, what we can do is we can then hook this up to our Zener diode clamp like that and

**Dave Jones:** bingo, we can clamp all of these pins. So, imagine this output here is driving our Nixie tube, it's going to one of the open pins on our Nixie tube here. Okay, and it's at 120 volts or whatever. This

**Dave Jones:** pin is at 120 volts, then we're going to it's going to be this diode here is going to be forward biased and then that is going to be clamped to a maximum, you know, let's say we used a, you know, a

**Dave Jones:** 48 volt Zener on there, you know, anything somewhere lower than our maximum 50 volt rating of our driver transistor, then obviously this pin here is going to be clamped at 48 volts plus the diode drop here, so 48.6,

**Dave Jones:** whatever. Still just call it the clamp voltage and Bob's your uncle, we're protecting that transistor. But, because they're all tied together common like this, all of the outputs are basically going to be tied to you know, the same maximum clamp voltage

**Dave Jones:** there. But, hey, this is a way that we can use the jelly bean ULN2003 cuz these things are as common as mud. And a few people have asked what I mean by a jelly bean component. Well, a jelly bean

**Dave Jones:** component is one that's super cheap, super available, usually, you know, almost by definition available from many different manufacturers. So, you know, 7400 series logic, 4000 series CMOS logic, Uh, you know, generic uh, you know, 741 op amps and uh, ones like

**Dave Jones:** this, the ULN2003. It's actually a series, the ULN uh, 2000 series drivers. There's different versions. There's a 2004 and whatnot. And they all have different uh, pros and cons. There's even like a low voltage drive uh, version than this that's specifically

**Dave Jones:** designed for, you know, 3.3 V logic input. But but the standard ULN2003 or 2003A available from, you know, countless different manufacturers for, you know, cents each or whatever. They uh, cost really cheap. Um, they can easily accept uh, 3 V input uh,

**Dave Jones:** or 3.3 V logic or 5 V logic. Not so great if you're driving hundreds of milliamps through the If you really want to turn them on hard, turn on this output transistor really hard, then, you know, the input uh, driving voltage can

**Dave Jones:** matter. But we're only talking about like a milliamp or two here. Not a problem. So, we can easily get away with uh, you know, CMOS TTL uh, type compatible 3.3 V and 5 V logic input uh, drive on

**Dave Jones:** this transistor. The basic difference between the different families in here is usually the uh, base resistor cuz they've got a base resistor built in and it's actually not just one transistor, it's actually a Darlington pair. So, it's actually uh, two transistors to

**Dave Jones:** give you extra gain there. But basically, the different families just have different value dropper resistors in there. But I mentioned a potential issue here and let's just have a quick look at it and do a quick measurement. Now, uh, let's assume that we've got our

**Dave Jones:** Nixie uh, driver here. We've got our 22K dropper resistor, got our 120 V supply up here. We've got one of the uh, transistors turned on here. So, one of the outputs of the ULN2003 is on. So, it's basically uh, because we've chosen

**Dave Jones:** 22K there, it's around about 2 milliamps um, that we're going to have flowing. But all these other ones are turned off. All these transistors are switched off and we've just got basically these forward biased diodes, hopefully depending on the voltage output here. If

**Dave Jones:** it's higher than uh the rated voltage of the Zener, then it's going to be forward voltage. If it's lower, as you saw the measurements before, some of them are, then hey, it's not going to it's going to be reverse biased. But some of these

**Dave Jones:** outputs are going to be up to, as we measured before, like 120 odd volts or something like that. So, we're going to actually get current flowing through the 22k resistor here through let's say this is 120 volts here, open circuit voltage,

**Dave Jones:** then that's going to flow through here down and be clamped by this 48 volt Zener diode. So, how much leakage current do we get total out of all these other pins um if we clamp this here? So, I'm just going to do a simple

**Dave Jones:** measurement here. Don't have a 48 volt Zener to hand, but hey, I'll just use like a 30 volt Zener. We'll just whack it in um and see what we get. So, let's give it a whirl. Okay, so what I've got here is

**Dave Jones:** I've got a digit turned on, digit zero, whatever, it's a random one. 170 volt supply up here. I've got my 22k dropper resistor. I'm measuring the current at about 1.6 milliamps through that 22k resistor. And what I've done is I've

**Dave Jones:** shorted all the other pins, all the other spare ones on the Nixie tube here, shorted those out. So, I've got that going through a 30 volt Zener here. The reason I'm shorting all of them together is sort of like a worst case thing

**Dave Jones:** because these uh diodes, because they're all going to a common terminal, could be doing that anyway. So, um I'm now going to whoop measure the There we go. 1.6 milliamps flowing through the 22k resistor. I'm going to measure the leakage current um

**Dave Jones:** through all the other pins shorted together and through with that 30 volt Zener clamp. So, here we go. Bingo, that didn't change. We're getting in about 0.33 milliamps, so 330 microamps leakage current shorting all the other pins together into a 30-V Zener. So, that's

**Dave Jones:** It's not a problem, and the Nixie tube is still working just fine. It makes absolutely no difference to the brightness whatsoever. So, looks like that solution will work a treat. Now, the other issue that I didn't really cover in the

**Dave Jones:** previous video about I looked at some of the Microchip serial driver chips, and some of them looked fairly ideal except they had totem pole outputs. And what a totem pole output is is an output that instead of just having an open collector

**Dave Jones:** like this one, i.e., the collector pin is just open, it's not connected to anything else inside the chip. Inside here, these are not open collector outputs. They're what's called a totem pole because they're got ones top and bottom, they look like an old Indian

**Dave Jones:** Indian totem pole. Anyway, something like that. It means that it's got a transistor which actively drives low and a transistor which actively pulls it high as well. So, it's often called a push-pull output driver totem pole, whatever. Now, there's an potential

**Dave Jones:** issue here, and it can be a major one. And so, we'll actually measure this and show why totem pole outputs aren't really suitable. We really need an open collector or open drain output like this. I've just drawn generic FETs in

**Dave Jones:** there, don't worry about that. They can be MOSFETs, they can be BJTs, whatever. Now, let's assume that we've got the 170-V supply, 22-k dropper, we've got our Nixie tube, we've got one of the segments, of course, turned on being

**Dave Jones:** driven low, but we've got all the other, you know, nine outputs here actually, you know, just floating, flapping around in the breeze. Now, if we're driving it with one of these microchip drivers that has a totem pole output, it's got a high

**Dave Jones:** HV pin on a high voltage active pin like that. So, surely you would put you would take that up to your 170 V supply. That's naturally where you'd put it. But, aha, will that cause a problem if this output

**Dave Jones:** transistor shorting on shorting all these other pins back up to the 170 V supply? I think we might come a gutser. So, I won't experiment with my good Nixie tubes. I remember that I had some that I think it was Fran, was it,

**Dave Jones:** who sent these into a very early mailbag? I've actually got three others. They're basically the same, the 12B type. So, I'll use one of these. These are look bendy soldered from boards. Obviously, they've still got the some of

**Dave Jones:** the pads left on there. Have they? Oops. Anyway, we'll try one of these because, you know, we don't want to damage one of our precious Nixie tubes that I'm going to use for my eight display solution. Okay, so what I've got here is

**Dave Jones:** the Nixie tube hooked up, 170 V supply, 22 K dropper resistor. I've got one of the segments turned on. It's segment zero again, not that it matters. Okay, what I'm going to do now is actually short one of the other outputs here

**Dave Jones:** well, Nixie tube pins to the 170 V supply and we're going to measure the current doing that. So, I've got my second current meter hooked up to the positive supply here. So, that's the on the top of the 22 K resistor

**Dave Jones:** there. So, right on the 170 V. So, let's hook on one of the other pins and I don't think it's going to be pleasant. Whoop. 9 mA. The current for the other one is through the 22 K resistor. Well, yeah, that's

**Dave Jones:** not very pretty. So, let's have a look at the display. What happens to it when we do that? So, we've got 1.5 mA at the moment. I'll turn on I'll connect one of the other pins. And yeah, the zero still lights up, but

**Dave Jones:** we're drawing like 8 9 milliamps, something like that. Oops. So, that's of course undesirable for the health of our Nixie tube and the reason why we can't use one of these totem pole output drivers. But hey, what if we hook the HV

**Dave Jones:** pin to the other side of the 22K resistor like that? So, we're basically only shorting out the pin. Well, we can try that, too. I'll just change that from here to here. All right, let's try that. Hook it up to a random pin and look at

**Dave Jones:** that. It's only 100 micro 80 microamps, something like that. It's very nice, as you'd expect. Um shorting out the any of the floating Nixie pins to the positive uh anode up there is no problems whatsoever. So, you could

**Dave Jones:** potentially hook that HV pin back up to on the other side of your dropper over here. But the problem with that is uh these, as you saw on the Microchip data sheet, these are high number of output drivers on the one chip. They're like 32

**Dave Jones:** or 64 output drivers and you've got separate dropper resistors for each one of your Nixie tubes like this. So, you'd have to dedicate one chip to one Nixie tube like that to be able to tie that individual pin back. I wouldn't like to

**Dave Jones:** uh tie them across multiple Nixie tubes. You could probably get away with it, but I like just no. And of course, some of these driver chips also had a built-in uh current source as well down in here. You could actually a bias uh pin, a bias

**Dave Jones:** voltage that you didn't need the dropper resistor up here and that's another thing which maybe you could potentially use to get away with using a totem pole output driver, but you So, it's possible, but yeah, you've got traps

**Dave Jones:** like that. Just be careful how you hook it up, but anyway, I don't think I'm going to be using a totem pole output solution. So, there you go. That's just a couple of extra uh measurements there. I hope you uh enjoyed that. So, what I'm

**Dave Jones:** going to do is I think like I do like the Microchip uh driver solutions. They're really good, but some people have uh I'm not complaining, but they've, you know, um said, "Hey, wouldn't it be nice if you could just

**Dave Jones:** use a jelly bean solution that everyone can get in every country, etc., etc." Okay. Well, yeah. All right. Let's go instead of a discrete transistor solution. I don't like that. I think I'll actually implement the jelly bean ULN uh 2003 with a um suitably uh high

**Dave Jones:** voltage uh zener on the common pin. The only issue with this is that they come in, you know, packs of seven. Um you get seven drivers like this. So, yeah, it doesn't even drive one Nixie tube. So, you know, you've got to share drivers

**Dave Jones:** across multiple Nixies and uh stuff like that, but yeah, that's not really an issue. And also uh strapping uh the unused pins together like this to a uh in this case where, you know, a clamp voltage cuz we're going to we've

**Dave Jones:** measured like 125 V on here. So, we're definitely going to with all the pins uh shorted together, which they do with the diodes. So, um basically, we're applying what's called a pre-bias to all these pins. And um some designs do this

**Dave Jones:** actually deliberately. But one of the uh common reasons is that uh yeah, you can uh use lower voltage output uh driver transistors by applying this uh pre- bias uh clamp for in this case via uh diodes. And that's how some designs

**Dave Jones:** actually do it. They use discrete diodes as well. This uh pre-bias and they actually hook it up to a particular uh supply is to prevent some of the uh segments uh some of the digits from actually uh glowing due to leakage

**Dave Jones:** currents and stuff like that, but I, you know, it's not really an issue here. Sometimes like this will go away depending on if you put like a filter on uh front like a red filter or whatever, um orange filter on uh front of the uh

**Dave Jones:** particular display, but we're not too concerned about that. I mean, we're really getting into the nitty-gritty details of Nixie tubes and and particular variations between tubes and manufacturers and brands and all that sort of jazz, you know, it's Yeah.

**Dave Jones:** Anyway, this is often called a pre-bias as well, and that's kind of sort of what we're doing here.
