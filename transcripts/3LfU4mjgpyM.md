---
video_id: 3LfU4mjgpyM
title: EEVblog #397 - Turnigy Accucell 6 Charger Teardown
url: https://www.youtube.com/watch?v=3LfU4mjgpyM
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 39, "3": 56, "4": 71, "5": 88, "6": 103, "7": 115, "8": 131, "9": 147, "10": 161, "11": 177, "12": 197, "13": 216, "14": 237, "15": 253, "16": 271, "17": 289, "18": 302, "19": 318, "20": 334, "21": 348, "22": 361, "23": 374, "24": 388, "25": 408, "26": 425, "27": 440, "28": 452, "29": 468, "30": 484, "31": 498, "32": 510, "33": 523, "34": 536, "35": 555, "36": 574, "37": 594, "38": 610, "39": 629, "40": 647, "41": 666, "42": 684, "43": 699, "44": 711, "45": 727, "46": 741, "47": 758, "48": 771, "49": 785, "50": 800, "51": 814, "52": 829, "53": 849, "54": 864, "55": 879, "56": 896, "57": 911, "58": 926, "59": 941, "60": 962, "61": 978, "62": 990, "63": 1002, "64": 1016, "65": 1029, "66": 1047, "67": 1067, "68": 1086, "69": 1112, "70": 1130, "71": 1142, "72": 1156, "73": 1173, "74": 1198, "75": 1213, "76": 1231, "77": 1250, "78": 1269, "79": 1283, "80": 1296, "81": 1311, "82": 1329, "83": 1345, "84": 1363, "85": 1381, "86": 1404, "87": 1415, "88": 1432, "89": 1449, "90": 1463, "91": 1483, "92": 1506, "93": 1522, "94": 1540, "95": 1556, "96": 1575, "97": 1590, "98": 1610, "99": 1627, "100": 1645, "101": 1662, "102": 1680, "103": 1694, "104": 1707, "105": 1719, "106": 1734, "107": 1750, "108": 1763, "109": 1776, "110": 1791, "111": 1812, "112": 1826, "113": 1841, "114": 1858, "115": 1873, "116": 1890, "117": 1905, "118": 1920, "119": 1935, "120": 1948, "121": 1961, "122": 1978, "123": 1990, "124": 2006}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. I had a couple of people ask after a previous video if I can do a teardown on this Turnigy Accucel 6 because you saw me use this in a lithium polymer battery discharger video I did where I

**Dave Jones:** discharged I got the discharge curve of a 5 amp hour uh LiPo battery from HobbyKing. And I also mentioned this thing is available from HobbyKing as well for the amazingly low folks, amazingly low price of 23 US dollars. Unbelievable. Um this is for a

**Dave Jones:** 5 amp charge charger, 1 amp discharge, and it supports all the different types of batteries, three different types of lithium, nickel metal hydride, NiCad, and lead acid as well. And it's got LCD user interface, all sorts of stuff. It's

**Dave Jones:** got a temp sensor interface with an optional serial well a serial data output as well. It's got controls, it's got fan, it's got a buzzer, and it supports balance charging and balance discharging of all the cells with all

**Dave Jones:** the different types. So you can do single cell, you know, two cell, three cell, four and five and so on. And it's a really amazing little beast for the price, 23 dollars. You got to be kidding me. Even from the Australian

**Dave Jones:** warehouse for HobbyKing, it's only 29 dollars or something. So absolutely amazing. Anyway, I had a few people ask if we could tear it down and have a look. It could be interesting. Now as you can see, it's in a rather nice alloy

**Dave Jones:** case here. I rather like it. It's in two halves. It looks like the front and end plates just pop off with the four screws there. And that's, you know, there's not much to this thing at all. It is quite

**Dave Jones:** small and compact. And as I said, it is actually you know a 5 amp charge capability and 1 amp discharge as well. Now, sorry, max charge 6. There it is. 6 amps charge and 1 amp discharge. And it

**Dave Jones:** you know for this little compact size really is quite neat. And by all accounts it is a very popular unit and works well. So, let's crack open these end panels and see what's inside. As I said, this thing is very popular with the

**Dave Jones:** remote control the massive remote control community. And there is quite a lot of um you know reverse engineering done on this. I think people have done new firmware and stuff. I'm not sure about reverse engineering, but they believe

**Dave Jones:** like they've done new firmware and there's people hacking the thing to make it more accurate and stuff like that. So, I mean for the price you know it's it's next to impossible to beat. And apparently it is based on the same model

**Dave Jones:** and that shares like different brands. They're a very similar, but they you know they might have slight differences in them. But apparently the circuitry is almost identical between these units. So, um hopefully this will apply to the other ones as well. And apparently

**Dave Jones:** it's quite well made. We'll find that out in a second. Let's whip this sucker apart. And what do I mean Wait, there we go. What I'm interested in is the discharge capability which we'll have a look at. Yep, there we go. Plates just pop off

**Dave Jones:** and yep ta-da! There we go. Doesn't that look neat? Look at that. That one actually That look The build quality looks very very good. I like it at first glance. Now, the construction of it really is quite neat, quite compact. They've got

**Dave Jones:** the LCD, that's uh soldered directly in there. It's not I don't think that's socketed. No, that's soldered directly in there. We've got a uh vertical riser board here for the um uh balance balance connectors on the side there. It looks like we've got a

**Dave Jones:** whole bunch of load resistors there for the balance channels, 1 2 3 4 5 6 of them there. So, uh apparently, you know, that you would have one of those channels for each uh cell, of course. Um so that you could um discharge the well,

**Dave Jones:** uh load balance each particular uh cell. So, a battery like this uh matching Turnigy uh three-cell um RC battery that I've got for my quadcopter, it you know, a very high discharge capacity, of course, you know, 35 to 45 uh C rating.

**Dave Jones:** So, you know, absolutely, you know, huge amount of discharge current. And there's the main um battery terminals, of course, huge chunky things, but it also has these balance leads coming out, which um allows it to detect across each

**Dave Jones:** individual cell. So, this is a four-pin one, of course. You've got ground, and then the three the voltage across each individual cell in there. So, that allows this thing to um put a load across each cell and then balance out

**Dave Jones:** this battery, cuz it's very important when you've got these massive discharge rate uh batteries that you that these cells are balanced in there. Otherwise, um one cell can die prematurely, and that's going to bring down your pack. And well, these things can, you know,

**Dave Jones:** the energy uh density in these things, they can explode, catch on fire, and do all sorts of weird and horrible things which you don't want to happen. So, that's why it has all these balance inputs and a different connector for um

**Dave Jones:** the number of different cell types there. And it looks like we've got uh some DC-to-DC converter, pretty beefy stuff happening around here. You need that, of course, to get the um higher voltages than the uh 12-V input, of

**Dave Jones:** course. It's just 12-V uh DC input, but it's capable of um packs which are actually uh more than that. So, it's going to have a boost converter in there to generate the higher voltages required. Couple of user interface push

**Dave Jones:** buttons. We've got a buzzer. Got a little fan. It looks like it's probably um under PC control there. I don't think it goes uh the micro uh control there. It doesn't go all the time. And uh there's got to be some extra big

**Dave Jones:** FETs. Ta-da! There we go. Some extra big FETs under the bottom there. That one is uh You can see the seal pad under there. Isolating that from the uh thing they've got some white heat sink compound under there. So, that'll be a

**Dave Jones:** MOSFET under there. Is it got And Yeah, it's got another one. It's hard to see under there, but it's got another one tucked up right under there. So, it looks like they're wedged between there based on that standoffs

**Dave Jones:** under the bottom of the board. So, these screws here will be uh holding down and pressing those uh TO-220 packages against the base, and the base is, of course, used as the heat sink. And under the LCD here, we're going to

**Dave Jones:** have the micro controller, of course, and then probably some more analog uh stuff, some op amps, and a whole bunch more resistors, cuz you're going to need a little bit more than uh what's shown on the outside of this here. So,

**Dave Jones:** there'll be a bit more circuitry under there, and uh you'll notice that, of course, the um the balance resistors here, if you're wondering why there's so many of them, they're actually paralleled up. So, they just got um 0805 resistors there all in They've got

**Dave Jones:** what? 2 4 6 in parallel there just to get extra power dissipation. And if we have a look at the 4-mm banana jacks here, you can see that they're just soldered directly onto the pad there. I particularly like that um at

**Dave Jones:** all, but you know, I guess it's good enough. Not sure if there's any reports of them having broken off, but anyway, um it will do the job. You can get ones that are actually PCB mounts, so they actually have pins which go through the

**Dave Jones:** board, but I guess they cost a fair bit more. We've got a couple of load resistors here. Um not sure what they're doing at the moment. There's two of them. One will be the discharge with the discharge FET, of

**Dave Jones:** course, but interestingly, it's in the negative. Yeah, we've got one in the negative lead there, so that'll be a MOSFET which we'll take a look at. Dead dead giveaway on the pin out there. You can tell because the I can't see the number at

**Dave Jones:** the moment, but you can tell it's a MOSFET because it's a three-pin device. We've got all four pins connected in parallel there. Another three over there and the one pin there which will be the gate drive. And that is a load resistor.

**Dave Jones:** We've got 0.051 ohms there. Interestingly, they've missed that solder joint there, but I'm trying to budge that. It's obviously soldered on the other side, so not a problem. And it looks like it might have a 3-A poly switch there by the looks of it.

**Dave Jones:** HR30, I'm assuming that's a 3-A poly switch. Not actually sure what that's doing there. It's a It's near the balance circuitry. It's nowhere down near the battery connectors down here. Like it's not you know, in line with um the battery terminals down here, so

**Dave Jones:** it's got something to do with the balance circuits. And that N-channel MOSFET down in there is an FDS6680 or a variant thereof, which is traditionally from Fairchild. And as I said, it's got a 51 mOhm um uh source resistor down the bottom.

**Dave Jones:** And it's rated at 11 and 1/2 amps 30 volts 10 mOhm nominal on resistance. And it looks like we've got an LM2904 dual op-amp down in there. Once again, I'm not sure what brand that is, just a generic brand. And down in here as part

**Dave Jones:** of that DC-to-DC converter circuit down here, we've got a P-channel MOSFET MT8103. And once again, that's a similar order to the other one 13 amps 30 volts nominal 10 mOhms on resistance. And up near the DC input jack, we've got another N-channel

**Dave Jones:** MOSFET, the 6680 that we saw on the battery output. And to see anything more here, we're going to have to crack this thing open. So, I don't I doesn't look like there's any circuitry on the bottom of this thing.

**Dave Jones:** So, I think it's all single-sided load apart from the MOSFETs on the bottom, of course. And this will uh require that I No, there we go. Ta-da! No, nothing on the bottom except the MOSFETs. Now, there's one thing I'm not

**Dave Jones:** hugely keen on here. The ground from the DC input jack, which of course needs to be high current, is just going through one pad over here, one plated pad, and that's it. Granted, it is quite uh quite large, but uh that's all that it's

**Dave Jones:** going through. But it looks like they have designed this for like uh flying wires coming off here or something. So, maybe there's another model that has um wires coming out cuz that's not really a footprint for some sort of connector. Um I think

**Dave Jones:** it's just for like bare wires. And I don't mind the board uh interlocking they've got here. You can see that the uh there's been a routed out slot in that vertical riser board. This is a common technique for joining two boards

**Dave Jones:** together at right angles like that. Soldered on uh both sides like that, of course, because all of the strain on this vertical riser board, when you plug those in, all that strain is being put on those solder joints. So, this is a

**Dave Jones:** fairly uh time-honored rigid method of uh joining and interlocking two boards together like that. And you can see this uh high current uh trace over here and the heavy uh via stitching going from one point to the other cuz they've

**Dave Jones:** obviously got traces on the other side running across here, and they had to get uh all the current from the uh DC-to-DC converter over in this section over here um to the uh output connector over here. So, um they've used, you

**Dave Jones:** know, 12 uh vias in there. And the rule of thumb is typically, you know, um half an amp nominal per via like that. And the two caps on the board here um SWC brand, they're not a name brand, but I

**Dave Jones:** don't think they're particularly uh known as anything uh atrocious. Yeah, nothing going on there at all. But you wouldn't expect a um you know, a Nichicon or something like that in a $23 charger. You've got to be kidding me.

**Dave Jones:** This one is actually uh silasticed down. There we go. We've got some black black gunk under there holding that one down. So, that's a nice touch. This one here isn't held down at all. And along the top here, I'm sensing a microcontroller

**Dave Jones:** ISP interface. You know, I just noticed that there's a bit of alignment issue with a couple of the resistors down here, but uh no big deal. I mean, generally the soldering the reflow soldering quality on this thing is first

**Dave Jones:** class. Now, to desolder this LCD, I thought it would be a nice opportunity to try out my new JBC CD series iron here, and you'll see a review of this. Never used it before, never even powered it on, but they did supply it with a

**Dave Jones:** nice-looking wedge tip, which I should be able to get in there and heat up those and lift off that LCD nicely. So, yeah, grown, it's a button interface with a LCD display and a non-removable stand, which I'm not particularly keen on, but let's

**Dave Jones:** power this thing up and uh see what we get. Ta-da! JBC tools, program version. And God, when your soldering iron has to have a firmware revision number. Tool is in the stand. There we go. It's all It auto detects.

**Dave Jones:** Look at that. And it heats up incredibly quickly. That is like amazing. It's the first time I've ever powered up this thing, first time powered up that tip. You can see the solder actually flowing from one end of the tip

**Dave Jones:** to the other, hopefully there. Wow, that was near instant, really. Absolutely incredible. Looks like it's got a bar graph on there, which I assume will go up as you apply like it applies a pole peak power. I'm assuming, I don't know. Sorry, I

**Dave Jones:** haven't This is not a review. I have not investigated the details on this at all, but I'm assuming that that power will go up to like 100% or will peak up when you apply power to it. So, it's got the

**Dave Jones:** selected temperature there and the I'm presuming the actual temperature. Hmm, let's give it a go. Look at that. It goes to sleep as you put it on the stand. nice. You can see the actual temperature is uh down to 230

**Dave Jones:** there. So, it looks like it goes to sleep at 220. Well, maybe it's cooling down. Maybe it's cooling down. If I well, lift it off, bang, yeah, it goes up to 99% and bang, it's instantly almost instantly back at 350. Very nice

**Dave Jones:** indeed. So, let's leave it on 350 and ah, heats up all those pins at once. Absolutely beautiful. Ah, very nice. I'm impressed. So, let's attempt to desolder this thing. I'm going to go on the uh the pins on the board.

**Dave Jones:** They're just lifting out. If I can get in there to all of them. There you go. That popped out without too much uh grief, although I did uh take out some of the uh through-hole plating there. Oops. But, that's common

**Dave Jones:** with these uh square post ones. If you don't get the holes the right size in the board, you can risk taking out the um uh you know, the pads in there. I mean, a safer way would have been to get in

**Dave Jones:** there and cut all the pins off, and then you could remove each pin one by one, and you could do it quite nicely. But, that worked a treat, that JBC iron. Pretty darn good. I'm impressed. But, you'd want to be for the price.

**Dave Jones:** Unfortunately, uh that didn't work out as intended. I was a bit foolish there. I should have uh chopped off the pins along there and sacrificed the uh LCD cuz what's happened is it looks like some of those holes are uh

**Dave Jones:** were quite small, and we've lifted a whole bunch of pads off there. I mean, this JBC iron was so uh you know, was supplying so much uh power to all those pins, and it felt good as I was lifting

**Dave Jones:** the thing off, but no, what? Fail. Ah, should have sacrificed the LCD instead. Idiot. Burr. It's a real bummer about those uh pads in there, but they can be uh repaired. I was uh hoping The reason I took uh those out is I was hoping to

**Dave Jones:** put a uh socket in there so that I could um then uh plug the LCD in and out for uh hacking development. Still doable, just ugly. And what we have there, no surprises, an ATmega uh 32 A, so um A U version. And what else

**Dave Jones:** have we got around here? We've got a uh HCF4051. So, we've got an analog switch there. And uh what have we got up here? We've got an LM32 four. Woah, hey, classic LM324. Let's have a look at this other

**Dave Jones:** one. Let's have a look. Ah, it's another uh 29 LM2904 dual op-amp. So, we've got a couple of LM 2904s. And LM393 comparator. And around the DC-to-DC converter there, we've got another 6680 um N-channel MOSFET there. So, there's

**Dave Jones:** no controller at all for the DC-to-DC converter. So, clearly they're uh doing that in the micro, by the looks of it. And down under there, we've got an IRFZ44N. And that looks like it's the main uh discharge MOSFET. And the reason I know

**Dave Jones:** that's the discharge MOSFET is cuz there's the drain there, connected directly through to the positive terminal via a little wimpy trace there, cuz this is only a 1-amp uh discharge. Uh of course, it's not uh it's not a

**Dave Jones:** huge discharge current. And then the uh source, if you look here, goes down to, tada, that resistor down there, which is also tapped off for the uh voltage read that will probably go over to one of the ADC

**Dave Jones:** pins well, you know, probably through some dividers or some amp or something through to the analog to digital converter in the ATmega and then it goes to ground through this resistor here. And if you're familiar with my previous

**Dave Jones:** videos on the dummy do-it-yourself dummy load, which I'll link in, then this is a classic N-channel MOSFET dummy load resistor circuit and that's particularly what I'm interested in here because we have for what 23 bucks um a effectively what should be if you can

**Dave Jones:** just hack the firmware in this thing. It's just an ATmega, it's got an LCD, it's got the buttons, it's got the case which is acting as a heat sink. It's a could be a relatively nice little not particularly high power

**Dave Jones:** dummy load. You can program the thing for a constant current, constant power or constant resistance. Hmm, neat. So clearly this other MOSFET here is the one with this 51 milliohm source resistor here is the one that's used for

**Dave Jones:** the constant current charging. You can tell the huge big fat traces on there. And it looks like we've got pairs of transistors here to switch in the balance loads across here. One for cuz there's six balance channels there with six

**Dave Jones:** balance loads as well. So looks like it's a some sort of dual transistor configuration controlled via the micro almost directly by the looks of it. And the other TO-220 device is a 78 05. Why are they had to uh heat sink

**Dave Jones:** that, I'm not entirely sure. Now, I was going to do a bit of reverse engineering on this circuit, but I thought I'd uh check first to see if somebody's already done it. And uh I think that they have.

**Dave Jones:** I'm not sure if it's an original uh schematic or whether or not it's um uh yeah, actually reverse engineered and they've drawn it uh in CAD, but it's not for exactly the same one, it's for the uh BC-6 uh charger, which is a almost

**Dave Jones:** identical uh charger, not quite. And the uh circuitry does seem to be almost uh identical. There's a few um uh There's a few devices that are different, but the actual uh topology and the circuit itself appears to be

**Dave Jones:** pretty close to identical to this uh Turnigy um Accucel-6. Now, let's start by taking a look at the main uh DC-to-DC converter circuitry here. And as you can see, it's a classic buck-boost topology. I've uh circled the uh three components for the uh buck part

**Dave Jones:** of it, a P-channel MOSFET, the diode down there, and the main inductor, which you uh see on the board. So, if we have a look at the main board down here, we're going to see there is our P-channel MOSFET. There's our diode

**Dave Jones:** going to ground. Just there, that's ground, and there's our inductor going through to the boost part of the circuit here. And of course, the boost start classic topology. We've got our inductor. First, we've got our uh N-channel MOSFET, which is that one

**Dave Jones:** there. And then, we have our output diode there, and our big filter cap. There it is. They've got a little little snubber on there as well. And uh that is um controlled by the dual comparator here, the LM uh 393.

**Dave Jones:** And it basically takes the output from the error the error amplifier output here. I've circled that up there, and that comes from the the sense amplifier on the low side N-channel MOSFET, which detects the charge current there. So, that's working

**Dave Jones:** as the error amplifier, and that's and they can read that off as well. That's going off to the ADC as well. And they actually tell you there I mean, if I'm not sure if you can see that in there, but it tells you that

**Dave Jones:** it goes off to ADC channel 3. This So, this schematic is quite detailed, and it tells you the actual ADC channel. So, the error amplifier comes in there, and the actual set voltage is controlled via a PWM, presumably a 10-bit one from the

**Dave Jones:** Atmel microcontroller. And they actually tell you which one it uses. It's OC1B there, and that sets the voltage. Now, it looks like that they've got a like a switch off here. There's a a control signal which comes in here, and that

**Dave Jones:** just pulls the output of the PWM low. Anyway, this control signal looks like it just disables that output, pulls it low there, and also it goes around to here, and pulls that one low as well. Now, the LM

**Dave Jones:** 393 isn't able to drive the Well, they haven't made it drive the MOSFETs directly because it's just a totem pole output. So, they've got the pull-up resistor there, and they've got the two transistors here, which form the totem pole driver with a 10-ohm series

**Dave Jones:** resistor to drive the gate of the large current MOSFETs there. OC1A, that is the constant discharge one, which is also up here. And here is the part of the circuit that I'm uh particularly interested in because this could be this what essentially is a

**Dave Jones:** a dummy load just like you've seen in my previous videos here. There's our N-channel MOSFET. It's the IRFZ244, which of course is the main one on the back of the board there, the main heat sink one there. And then we've

**Dave Jones:** got our current sense resistor .5 ohms down there. And that is a nice little constant current dummy load or depends on the software you could do constant power, constant resistance, or whatever. So, it wouldn't be too hard at all to hack this thing

**Dave Jones:** into a nice little dummy load. Not particularly huge power unless you wanted to beef the components and the heat sinking up a bit, but certainly very usable. And they're tapping the voltage off here, amplifying that, and that's going off to

**Dave Jones:** ADC channel two there. Now, here's our positive and negative battery input here, and you can see that in battery part bat plus bat minus. And that we've got a differential tap on that via this via these two fixed dividers into the LM2904

**Dave Jones:** op amp here. Now, you may notice that there's no feedback there. So, you may wonder what's it doing? Is it acting as a comparator or something? Well, no, the feedback path is actually the output here through the charging current

**Dave Jones:** MOSFET, through the current voltage tap here, and then through the op amp, through the error amplifier, and then that error signal is fed back into down here, which then mixes in with your PWM set voltage to control your

**Dave Jones:** switching MOSFET for which then it goes directly to the battery output. So, that's your feedback system there with that error amplifier. And once again, we've got like a little safety circuit here. This NPN transistor just regardless of what's happening just

**Dave Jones:** pulls the gate of that MOSFET low and just switches off the whole thing. And we saw a similar thing down here where there it is. There we go. That just shorts out the PWM um signals there and just switches it all off. And this whole

**Dave Jones:** thing is rather clever. I like it. It's all sort of, you know, the buck boost converter here is integrated with the entire feedback system for the constant current and constant voltage charging modes. It really is quite nice with the amp here

**Dave Jones:** and the current set fit down there with the current sense resistor and tapping off it. It really is quite neat. I like it. It's very clever. And here's our DC input jack here and they've got a reverse protection MOSFET in there. They didn't

**Dave Jones:** like put a diode in series or something and it dissipate too much power. So, they decided to put a MOSFET in there. So, if you plug in the input voltage backwards, which could easily happen on these types of things considering that

**Dave Jones:** they're used in all sorts of weird and wonderful scenarios out in the field, that's just some reverse protection. Although, there's more than one way to skin a cat there. An easier way would have been a P channel MOSFET up on the

**Dave Jones:** high side, but they just decided to go for the N channel MOSFET, the 44 68, which is used elsewhere and just the voltage divider. So, positive input there turns on the gate and switches the ground. So, they're actually

**Dave Jones:** disconnecting the ground in there and you'll notice that the main electrolytic filter cap there is after the switching transistor. So, if you apply a negative voltage, it's not going to blow up your electrolytic cap when it's backwards. And you can see the balance uh circuit

**Dave Jones:** here and uh just as I suspected uh right at the start, we've got a Darlington uh configuration here and then another uh driver transistor driven directly from the uh from a pin on the micro there. So, there's our six load resistors in

**Dave Jones:** parallel. Looks like they're 120 ohms. Six of them in parallel and that uh this is drawn a bit um upside down, really. They've got um battery negative at the uh top and then they've got the balance one pin and then the next one goes from

**Dave Jones:** the balance one pin to the balance two pin and so forth. So, um as you can you know, it would be like that. We would have a cell like that and then our next cell would be like and

**Dave Jones:** that's if that's our ground there, then our next um Almost drew that back to front. It's a bit confusing here, but then that's our next cell and then goes in here and then our next cell like that and so forth and

**Dave Jones:** that just taps off um that each individual cell like that and uh There we go. Looks something like that and that just taps off each one of those cells and that allows them to allows the software to just to balance the uh put a

**Dave Jones:** load across each cell and then balance it out like that. So, it's rather neat. So, if you flip it around the other way, you'll get an idea. There's the positive of each battery cuz of course these uh multi-cell battery

**Dave Jones:** packs like this one, this one's a uh three-cell pack. There it is, three-cell 11.1 volts nominal and that will contain these three cells in series. And if they're not balanced correctly, one of them can uh die and your battery's going to have

**Dave Jones:** a very short life, or could uh end quite violently. And then we've just got some uh buffers here tapping off each in each particular uh balance cell like that, and they go directly um well, sorry, I was about to

**Dave Jones:** say directly into the ADC. They don't, they go down to the uh 4051 marks down here, and there's some more uh dividers down here as well. And they go into all the channels of the 4051, and then the uh micro pins select

**Dave Jones:** which channel it wants to uh which uh cell voltage it wants to measure, and that goes through to the main ADC via a low-pass filter. And this schematic here shows a um USB interface uh serial uh chip here, which um isn't um included in

**Dave Jones:** this design, so that must be uh something to do with a different model. But apart from that, this uh schematic does look like it is pretty much um the exact uh schematic of the Turnigy Accucel 1 that we've got here. I haven't

**Dave Jones:** really uh found any uh errors on it yet. I mean, there might, you know, might be component uh value differences and uh stuff like that, component uh types, but the uh general topology looks to be absolutely identical. So, there you have

**Dave Jones:** it. That was rather interesting. That's the Turnigy Accucel 6 charger, and um I don't really recommend uh you get one and sort of uh hack its charging capabilities. It's already uh you know, um very well uh suited to that, and by all

**Dave Jones:** accounts, an excellent uh charger. So, I highly recommend you get one just as a general-purpose charger, and at $23, you've got to be kidding me. Well, I've got to pay postage on top of that, but jeez, this thing is absolutely dirt

**Dave Jones:** cheap, and it's uh designed and built quite well. I rather like it, but I find it interesting that it should be easy to uh hack this thing to uh write your own uh firmware and turn it into a

**Dave Jones:** relatively good little dummy load constant current constant power constant resistance dummy load and you know it's not going to dissipate a huge amount of power but it's certainly usable and you can expand it you can you know change

**Dave Jones:** the resistor down here you can heatsink that mounted on the bottom press against the bottom of the case you can add a larger heatsink on the bottom of the case or something like that and but you know so it might make the basis

**Dave Jones:** of a nice little do-it-yourself hacked dummy load. Give it a try you might see some future videos on it maybe I'll have a go at it myself that was the intention anyway so I hope you enjoyed that if you want to discuss it

**Dave Jones:** jump on over to the EEVblog forum that's the place to do it and remember if you like teardown Tuesday please give it a big thumbs up. Catch you next time.
