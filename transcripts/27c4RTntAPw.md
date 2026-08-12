---
video_id: 27c4RTntAPw
title: EEVblog #268 - Xantrex 300V 4A Power Supply Teardown
url: https://www.youtube.com/watch?v=27c4RTntAPw
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 33, "3": 45, "4": 67, "5": 78, "6": 100, "7": 122, "8": 135, "9": 146, "10": 164, "11": 192, "12": 207, "13": 225, "14": 235, "15": 251, "16": 260, "17": 273, "18": 296, "19": 321, "20": 335, "21": 348, "22": 357, "23": 369, "24": 385, "25": 398, "26": 408, "27": 421, "28": 436, "29": 449, "30": 460, "31": 473, "32": 491, "33": 506, "34": 519, "35": 530, "36": 544, "37": 557, "38": 568, "39": 585, "40": 598, "41": 609, "42": 622, "43": 634, "44": 654, "45": 682, "46": 690, "47": 703, "48": 722, "49": 736, "50": 749, "51": 765, "52": 776, "53": 799, "54": 815, "55": 827, "56": 842, "57": 856, "58": 871, "59": 882, "60": 897, "61": 917, "62": 935, "63": 958, "64": 970, "65": 982, "66": 997, "67": 1013, "68": 1027, "69": 1038, "70": 1056, "71": 1077, "72": 1098, "73": 1115, "74": 1135, "75": 1152, "76": 1168, "77": 1181, "78": 1196, "79": 1214, "80": 1225, "81": 1247, "82": 1266, "83": 1278, "84": 1300, "85": 1317, "86": 1326, "87": 1346, "88": 1359, "89": 1377, "90": 1390, "91": 1405, "92": 1420, "93": 1437, "94": 1452, "95": 1476}
---

**Dave Jones:** Hi, it's Teardown Tuesday again. This time around, I've got something big and beefy. It's a Xantrex 300 V 4 A 1200 W one rack unit power supply. What a high-energy stuff.

**Dave Jones:** I love it. Let's check it out. Now, the unit we've got here is the Xantrex XFR 300-4, and it actually comes in a whole bunch of different models from 0 to 6 V at 0 to 200 A right up to 0 to 600 V at 0 to 2 A.

**Dave Jones:** So, this one is the second highest 1200 W, but this one 0 to 300 V DC output with 0 to 4 A. Beautiful. And of course, these aren't bench power supplies at all.

**Dave Jones:** These are designed to go into racks. This is a one rack unit high, and all the voltage and current knobs are on the front, and the power switch is on the front, and a few other miscellaneous function buttons, but all the power output and power input is on the back cuz they're designed to wire into big rack mount power systems, which could power anything custom.

**Dave Jones:** So, even the power cord, even though we've got a standard power cord on here, you'll find it's not a standard IEC input connector cuz these things aren't designed for just general purpose consumer use.

**Dave Jones:** And on the back here, you can see there's a whole bunch of these Phoenix input connectors, and you can see that it's really centered around remote operation. There's various sense lines and remote programming so you can program the current and voltage with external resistors or external pots or external or you can do it using digital control or whatever.

**Dave Jones:** These are very flexible power supplies designed for system use. And we pan over here, we'll see that the there's the output there's the output voltage there. It's it's another Phoenix Uh, terminal block in there with a safety guard on it because these things are high voltage outputs and uh, there's the mains input there.

**Dave Jones:** It's inside a block, but once again, you've got uh, terminal blocks in there to actually screw that in. There's a big strain relief here, but you can actually uh, wire in your cable in, your mains input cable in directly into the unit.

**Dave Jones:** And here's something you don't see every day, made in Canada. Beautiful. Sorry, I don't know the Canadian national anthem. If I did, I'd sing it. Bring a tear to the eye of my Canadian viewers.

**Dave Jones:** And you know what we say here on the EV blog, don't turn it on, take it apart. But, there's a very good reason why you don't want to switch these things on before you take them apart because lots of high voltage, high energy uh, storage caps in here.

**Dave Jones:** So, you really want to let those discharge before you uh, take apart something like this. And any well-designed uh, supply like this Xantrex one, top quality, industry reputable brand, uh, I'm sure it's got uh, discharge bleed resistors in there.

**Dave Jones:** And here we go. Let's lift up the skirt on this thing and uh, you can expect some big electrolytic uh, caps and quite a few of them, probably half a dozen or a dozen and uh, you can expect some big uh, inductors and lots of stuff like that.

**Dave Jones:** Plus uh, some control boards. So, ta-da. Yes. Look at that. Oh, let's check it out. Huh, and it really doesn't disappoint, does it? Check it out. We've got one huge mother of a PCB on the whole thing.

**Dave Jones:** We've got it looks like some digital uh, control board over here. You can tell by the packages there. We've got our front panel board, but uh, look at this big power supply.

**Dave Jones:** Like I said, a whole bunch of electrolytic caps, high voltage, high value caps for about storing the DC cuz what this basically does is convert your AC straight into DC and then it's a basically a DC to DC converter after that.

**Dave Jones:** So, you got a whole bunch of EMI input inductors here. You got input relays. We've got heat sink and we'll check out these devices later. We've got three fans up here.

**Dave Jones:** That's rather interesting placement for the fans actually. Usually you would have them might have them on the back panel here or something like that, but there's a big grill on the back, but yeah, that's rather interesting.

**Dave Jones:** They're going through there. There's some cardboard under there. We'll check out. In fact, that's a whole cardboard piece actually going square piece going right around there just sort of separating things a bit and it goes through here like this and uh But yeah, we've got our big power devices here, couple of transformers and miscellaneous stuff.

**Dave Jones:** Actually, I stand corrected. It's not one huge PCB. If you actually get in look at the details, there's one large input filter board here which basically converts the 240 volts or the mains into DC into high voltage DC and then we've got the second board here which looks like your basically your high power DC to DC converter board.

**Dave Jones:** There's another miscellaneous control board here with a whole bunch of sort of analog type stuff plus your digital board. Now, let's start out with our mains input circuitry here and have a look to see what's happening.

**Dave Jones:** Now, what we've got here here's our terminal block input two HRC fuses just like you'd see in a multimeter high rupture capacity fuses. Then we've got a whole bunch of, uh, EMI stuff.

**Dave Jones:** We've got two MOVs here, by the looks of it. Uh, we've got two relays. I'm not sure what the relays are uh, switching in and out. Maybe it's, um, uh, you know, software controlled.

**Dave Jones:** It's like a a uh, soft start uh, power on or something like something to that effect. And, uh, couple of big uh, uh, big power resistor. There a smaller fuse there.

**Dave Jones:** Not sure what that one's doing. And, uh, some uh, mains rated uh, self-healing uh, caps here. And, uh, this is pretty much, um, just EMI uh, filtering so that it just keeps the uh, noise, um, from escaping back out the main supply.

**Dave Jones:** And, here's our bridge rectifier because this is an AC to DC converter. So, that uh, takes the 240 V or 110 V mains input and converts it uh, directly through a full wave bridge rectifier, as you're familiar with.

**Dave Jones:** But, this here looks like it might be like an earth terminal or something. But, let's take a closer look at that one. And, of course, a big heat sink here for the bridge rectifier.

**Dave Jones:** And, you can see the white um, heat sink compound in there, as well. Now, if I take these two uh, blade uh, terminal wires off here that go through to the main switch on the front panel, you can see the wiring in there coming from this here.

**Dave Jones:** And, it looks like cable, but it's not. It's a dual wire thing going into a little uh, splice um, terminal block there which insulation displacement uh, uh, splice terminal.

**Dave Jones:** So, there's obviously that's some sort of thermocouple that's measuring the temperature of the bridge rectifier. So, they've put, you know, they're not just rectifying this and uh, just be done with it.

**Dave Jones:** They're actually monitoring the temperature. So, presumably, they can um, shut this thing down if it overloads. Yep, you beauty. It's Davecad time. Uh, please excuse the crudity of the model.

**Dave Jones:** Didn't have time to build it to or to paint it, but this schematic here represents what I think is happening on this board and it will map this schematic will map to the physical components down here as we go along and I'll try and explain that.

**Dave Jones:** I haven't actually traced it out, so it won't be a may not be 100% accurate, but it's pretty obvious what's going on by the physical location of the components and based on some basic theory of how common mode input EMI chokes and things work.

**Dave Jones:** What we've got is our mains input over here. We've got our two HRC fuses here. We've got our common mode This is a multi stage common mode choke. So here's the common mode choke with Sorry, got a filter cap there.

**Dave Jones:** Here's our common mode choke. There's the ferrite and with the top winding and the bottom winding there. Then these two gray caps here and here, these go to earth and then we've got another common mode choke here.

**Dave Jones:** Once again, the top winding, the bottom winding there going in this time a parallel filter cap and then we've got two big MOVs here and here because there's two of them.

**Dave Jones:** I'm fairly certain without having to trace it out that they will go down to earth like that. And then you may not be able to see that in there, but there's a tiny little half watt axial resistor in there.

**Dave Jones:** That's actually 1 meg. As I mentioned at the start, that's a 1 meg bleeder resistor just to bleed off any voltage stored on these caps. And then we've got another Well, it's not a common mode choke this time.

**Dave Jones:** We've got two separate inductors here and here and then we've got a another parallel filter cap and then another MOV. In this case, it will be in parallel and go directly across instead of to mains earth.

**Dave Jones:** I almost forgot these two little inductors two extra inductors here and here, so that's another stage of filtering. And then, we'll talk about this soft start in a second, but then it basically goes into the bridge rectifier, which converts the AC input into DC.

**Dave Jones:** So, all this stuff we saw is just for EMI filtering. And well, it's they've really gone to town on that one. And also our overload protection with the MOVs.

**Dave Jones:** So, the standard bridge rectifier here, which is on the big heat sink like this and temperature monitored as we said, converts the 240 volts or 110 volt AC into DC.

**Dave Jones:** And these are our main filter caps here. There's actually 10 of them. And there's a few more off camera here. And I looked at them and I saw that they were only 1,000 microfarad 200 volt.

**Dave Jones:** So, I went, "Well, that's not high enough to put them directly parallel across here." Because if you convert 240 volt mains into DC, you're going to have higher than 200 volts.

**Dave Jones:** So, clearly, cuz they've got them in pairs like this, what they've done is this is not unusual at all. They've put them in series like this to effectively give you a a 500 microfarad cuz it's half the value at 400 volts instead of 1,000 microfarad 200 volts.

**Dave Jones:** And they've done that five times. So, effectively, they've able to create a larger voltage electrolytic filter cap with two lower voltage units. But, if you've seen my capacitor tutorial, you know that's not necessarily a good thing because when these things age and get old or they're mismatched from the factory, they may not share the voltage, you know, you may not get 200 volts across there and 200

**Dave Jones:** volts across the bottom half as well. So, that's why there's two resistors here. There's a big looks like a 5 watt. It's actually 10k and there's another one here.

**Dave Jones:** So, that clearly shows that these are current sharing resistors. Um because that will just help keep this voltage at the center, especially when it first uh powers up to equally share the voltage across these caps.

**Dave Jones:** And now, this soft-start circuit, as I mentioned, that's what this big resistor over here is doing, I think. It's a uh 15 ohm 13 watt resistor, massive power one, and there's two relays here, so I'm not sure exactly uh the configuration, but let's just say there's one relay.

**Dave Jones:** I'm pretty sure it's just going to short out this 15 ohm resistor. Because when you first switch this thing on, these capacitors are going to be discharged, and they're going to go and they're going to suck in all the current.

**Dave Jones:** You're going to have a huge current surge through your diode bridge into your capacitors. And well, that's not such a good thing. So, that's why they put the series resistor in here, surge protection when you first turn it on.

**Dave Jones:** The relays are energized, so you've got the series resistor, which limits the inrush current to the capacitor bank. And then, after a couple of seconds, uh determined by this control circuitry or something else down there, then it switches on the relay, shorts it out, and bingo, you can start operation.

**Dave Jones:** And we get our high voltage DC output directly across the filter caps. And bingo, that's all there is to it. It's uh pretty basic, there's nothing unusual or surprising there at all.

**Dave Jones:** And um this uh there's a bit of control circuitry down there, it's probably an op amp or comparator or something like that. And it's uh obviously, maybe it's doing um some extra, you know, uh mains failure protection or uh mains failure detection or something like that, perhaps, which might automatically um there might be another relay to automatically switch off the power there, but there you go.

**Dave Jones:** It's pretty basic operation, but because it's big and high power, that's why you need a huge board this big. You need the massive inductors, the big filter caps, the big filter capacitors, the big MOVs, and really it takes up a lot of room.

**Dave Jones:** And you can actually see this ribbon cable here going from this mains input board over here somewhere. So that's obviously, you know, to control the mains failure input detection or something like that.

**Dave Jones:** There may be a bit more, maybe it can measure it or do something like that perhaps, but clearly they've linked that over here and it does some control. And our high voltage DC output here goes over here up into this board here.

**Dave Jones:** Let's take a look at that one. And if we peel back some of this protection cardboard here, we can see the high voltage DC from our supply board coming into here.

**Dave Jones:** We've got another filter cap by the looks of it, and we've got four huge devices mounted on this heat sink which has the three fans. Basically, it's probably, you know, it sucks air from the sides of the unit and I'm not sure which way they're blowing.

**Dave Jones:** They're probably blowing out that way and well, they would be. They'd be blowing across these heat sinks here and out the back. And these four devices are high voltage, high current N-channel MOSFETs.

**Dave Jones:** They're IRFP460s and you can see we've got some temperature sensing coming off here as well in exactly the same crimp configuration that we had for our mains input. Take a look at this.

**Dave Jones:** You'll notice that these screws here, it's an interesting method to join this board through to this board. They've actually got these uh big screw studs here which actually are the high current interface interface connector between these two boards like this.

**Dave Jones:** Beautiful. And what we've got here is a UC3875 phase shift resonant controller, and it controls the four N-channel MOSFETs up here. And if you have a look at the data sheet for that, you can see the output configuration with the four MOSFETs.

**Dave Jones:** And also we've got two IR 2110 high-side MOSFET drivers. And then we've got a power also going over here via this twisted pair cable into another heatsink device with a whole bunch of power MOSFETs and the switching transformers and another choke in there by the looks of it.

**Dave Jones:** And it may be hard to see that, but these transformers are actually mounted on their own PCB, which sits flush with the other PCB. You can see the breakout tabs there from the PCB panel.

**Dave Jones:** And here's the output side of things. We've got two big 400 V this time, 330 microfarad caps. Looks like there's There's There's position for another couple of caps there.

**Dave Jones:** Interestingly, this one has a big jumper on it going across the cap like that. So, and here's our output terminal over here. We've got some output protection and a little bit of control circuitry around there, but that's probably about it.

**Dave Jones:** And what I thought was output protection there perhaps is not It's not these are output filter caps. They're a Z5U dielectric, it says there 1 kV at 0.05 microfarads.

**Dave Jones:** Now, there's a couple of these devices on the board. These are very interesting. They They're actually a 105K, that's 1 microfarad, of course, 400 V. It looks like they're metallized polyester capacitors.

**Dave Jones:** I think it's worth digging up the data sheet on these. They've got one of them there, and also they've got two of them up on the input side of the board over here.

**Dave Jones:** And here they are. They're uh made by a company called uh Pactron, and they're metallized polyester uh PET dielectric. Um they call them cap stick uh capacitors, and they're basically uh ultra-high reliability, high MTBF capacitors, and made in the USA, star-spangled banner.

**Dave Jones:** I love it. And uh they're for high ripple current, high capacitance uh you know, high frequency switch mode uh DC to DC uh converters, and they're high reliability. And it says, "Like all film capacitors, cap stick capacitors have true voltage uh ratings, and unlike other dielectric systems, require no voltage derating for maximum reliability." Excellent.

**Dave Jones:** This is exciting stuff. There you go. So, uh uh it tells you, "Many leading-edge circuit designs take advantage of a film capacitor's inherent reliability at rated voltage to reduce board size and improve performance." Well, I don't think they were going for board size here in this uh huge one rack unit uh case, but there you go.

**Dave Jones:** These are little interesting uh beasts here. They're obviously uh multi-pin to get a lower uh inductance um in there. So, uh if we scroll down here and take a look at uh some of the specs, they range from 0.33 microfarads up to 20 micro.

**Dave Jones:** We're using 105s, which are uh one microfarad. This gives you the lowdown. Uh miniaturized pass filters made possible by high-frequency switching technology need but low ESR and low ESL capacitors to attenuate ripple and reflected RFI over wide uh frequency bands with equivalent series resistance approaching zero.

**Dave Jones:** Excellent. Nonpolar MLP capacitors reliably sink high ripple currents in high-density converters, run cool, and are stable. Ooh, what's not to like? But I'm sure these things aren't cheap. You probably pay uh easily a couple of bucks uh each for these caps, I'm sure.

**Dave Jones:** Maybe even 10 bucks, who knows? That's why these things are mega expensive, these types of power supplies. And I got some more temperature sensing action down here. Once again, exactly the same crimped configuration as before.

**Dave Jones:** And we've got some extra chokes here. There are only a couple of turns on the ferrites, and these look like ceramic thick film resistors. Silly me, I should have looked at the number of legs on these.

**Dave Jones:** These aren't MOSFETs, these are actually diodes. They're an IXYS DSC130. Can't find any info on them, but presumably very high power and probably quite expensive. There's nothing to write home about on the front panel here.

**Dave Jones:** Pretty basic seven-segment LED display interface with the sockets just putting them out a set distance basic stand-off construction with the big 40-pin DIP. No surprises. I ICL7107. And we have some calibration adjustment pots here.

**Dave Jones:** They've been gunked up with the red set, so someone has put their tongue at the right angle, tweak those, and then set those down so vibration doesn't affect them.

**Dave Jones:** And standard LED stand-offs there, some basic push-button switches, and the 10-turn pots for the voltage and current controls. And after all this awesome power stuff, I think the digital uh side's a bit of a letdown, but what the hell, we'll check it out anyway to see what processor it's actually using.

**Dave Jones:** Nothing exciting, I'm sure it's a very old school. But we'll check it out nonetheless. And let's see, does it pop off? Oh, no, we've got to undo the uh screws for the D9.

**Dave Jones:** Now, this board here is actually the uh optional uh remote control board, so you don't get this in the standard configuration, but bingo, there it is. Might be upside down, but there it is, made in Canada.

**Dave Jones:** Interface card. Brilliant. Very old school uh disk ceramics just bent over like this, all crowded in there. Quite old school, I love it. Fox crystal. Uh we've got a ROM here and uh a local uh regulator and um a PLCC uh package uh processor.

**Dave Jones:** You don't see uh PLCC packages in sockets too much these days. Not too many surprises. It's a Motorola uh MC68HC11. But of course, it seems to be dual processor cuz there's another second 61 uh 68HC11 as well.

**Dave Jones:** Uh we've got another ROM up here, so there's uh two ROMs, and probably an inter- interface and control or something like that. We've got a jack up here and uh not much else.

**Dave Jones:** So, that's the uh interface uh board, couple of miscellaneous 74HC series circuitry, but uh yeah, not much happening there. And here's the Phoenix uh connector inputs. There's some uh jumpers here and uh I can once again uh a bunch of uh 10-turn uh trim pots there, and uh one there are set with the red gunk.

**Dave Jones:** And there's things like I monitor, uh you monitor, I program, uh you program, and they're uh set and here's the uh Phoenix input connectors down here, which uh control the voltage and current remotely.

**Dave Jones:** Not exactly sure what this uh daughterboard here is doing. It's got a uh trim pot on it and it can couple of op-amps and things like that. So, um yeah, they've put that as a secondary board just uh basically sitting on top of the other one, directly soldered onto the main board.

**Dave Jones:** And basically, that's all the uh control stuff inside this if you ignore the optional um interface uh board, then this is all your remote programming voltage stuff, which controls your main DC to DC converter in here.

**Dave Jones:** Here's your out. So, here's your DC input board up the top. It comes in here, and it goes across. This is your main high frequency DC to DC converter section, some output filtering, and it goes straight to the output over here.

**Dave Jones:** And this circuitry just controls it with some display stuff and miscellaneous power stuff over there. Too easy. So, there you go. That's the Xantrex ZFR 300 300 V 4 A power supply.

**Dave Jones:** And it's a really top-shelf brand huge quality industrial designed properly designed system rack mount power supply. I was pretty darn impressed. It was basically they spared no expense in this thing.

**Dave Jones:** It's all uses prime top-shelf components. And it's really well designed, really laid out, really modular. A lot of thoughts gone into these. Really pros have designed this. It It'll be very high reliability, and you'll pay for that sort of stuff, too.

**Dave Jones:** So, I hope you like that. I certainly did. It was very interesting. So, remember if you like teardown Tuesday, give the video a thumbs up. Helps a lot. And if you got any theory and ideas about how exactly all of this DC to DC converter works, jump on over to the EEVblog forum and discuss it cuz this sort of stuff very interesting.

**Dave Jones:** Catch you next time.
