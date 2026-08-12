---
video_id: a-v53hfAyDU
title: EEVblog 1402 - Rohde & Schwarz NGA100 PSU Teardown + GIVEAWAY
url: https://www.youtube.com/watch?v=a-v53hfAyDU
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 47, "3": 68, "4": 98, "5": 127, "6": 154, "7": 168, "8": 185, "9": 200, "10": 234, "11": 262, "12": 291, "13": 319, "14": 347, "15": 375, "16": 406, "17": 439, "18": 471, "19": 502, "20": 535, "21": 551, "22": 576, "23": 602, "24": 626, "25": 649, "26": 665, "27": 684, "28": 707, "29": 738, "30": 764, "31": 790, "32": 812, "33": 844, "34": 872, "35": 900, "36": 933, "37": 962, "38": 975, "39": 995, "40": 1015, "41": 1038, "42": 1064, "43": 1092, "44": 1120, "45": 1135, "46": 1158, "47": 1176, "48": 1204, "49": 1219, "50": 1245, "51": 1276, "52": 1308, "53": 1331, "54": 1375, "55": 1395, "56": 1414, "57": 1447, "58": 1471, "59": 1499, "60": 1523, "61": 1541, "62": 1556, "63": 1576, "64": 1606, "65": 1619, "66": 1646, "67": 1676, "68": 1703, "69": 1736, "70": 1754, "71": 1773, "72": 1796, "73": 1810, "74": 1826, "75": 1848, "76": 1871, "77": 1890, "78": 1906, "79": 1929, "80": 1949, "81": 1969, "82": 1998, "83": 2029, "84": 2043, "85": 2065, "86": 2095, "87": 2120}
---

**Dave Jones:** Hi, it's teardown time again. We've got another bit of Rohde & Schwarz power supply kit and we love looking at these things. I've had this one for quite a while. I was going to do a video when it was released back in April, but unfortunately, things got in the way.

**Dave Jones:** And we have seen the NGE100 teardown before. I'll link that in up here if you haven't seen it. And it is a cute little smallish form factor triple output 33 watt per channel power supply and this is part of their basic series power supplies, but they've released this new NGA100 series. It's not designed to replace this. It's designed to supplement it and it's a bit of a different beast. It either comes in a single or a dual output. There's no triple output version of this. Now, it's

**Dave Jones:** advertised as a linear power supply whether or not it's a linear output stage like this with a switching tracking pre-regulator that remains to be seen, but it is significantly bigger. Check that out. It is much deeper for actually less output. This is only 40 watts per channel, so 80 watts total.

**Dave Jones:** So, technically, this is less total power output than this series up here. So, it could be completely linear. There's a reason for the size in these suckers. Anyway, exactly the same look and feel form factor. These actually fit in a 19 inch rack mount, so you can actually get a rack mount kit to mount like two of them side by side in a 19 inch rack. So, that's very nice, but they do come with the tilting bail feet on them. And even though it's part of the basic series

**Dave Jones:** supplies, here's where it fits into the overall scheme of things. It's, you know, got some pretty advanced stuff in terms of like low current measurement and resolution and accuracy. It's like 0.02%. It's absolutely crazy and you'll get 1 microamp current resolution out of this thing. So, I'm really looking forward to powering this thing up and having a play around with that. Anyway, we'll do that at the end because, you know, as we say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** But, it comes in two different models. The one we're looking at, this is the NGA142. This is a two-output 0 to 100 V per channel. So, this is rather novel. There's not many power supplies that'll do 0 to 100 V and this will do 0 to 100 V at 2 A per channel. And of course, you can put them in series to do 0 to 200 V at 2 A or you can put them in parallel to do 0 to 100 V at 4 A. The other

**Dave Jones:** model, the NGE102, that is the 35 V supply and that'll do up to 6 A. And as you can see, they use the same terminals that they used on the NGE series up here. I'm not a fan of these.

**Dave Jones:** They don't open very wide. If you have a look there, it's really difficult to get There is a hole down through the threading there. You can get your wire, but I Yeah, I I really don't I'm not a fan of these terminals. Look, you can't open them very wide. There's the hole.

**Dave Jones:** Maybe you can see it down in there. And I I don't know. And they're red and blue. That's that European rubbish color code. So, I Yeah, I don't know. I prefer red and black. Call me old-fashioned. And thanks to Rohde & Schwarz, I actually have two of these to give away.

**Dave Jones:** I've got one 142 model, the 0 to 100 V, and one 102 model, the two-channel 0 to 35 V model. So, stick around for the end of the video for details on that giveaway. Everyone loves a giveaway. Now, on the back, which we didn't get on the NGE model, we've got the sense inputs as well. Rear channel sense on the back. That's really nice for doing remote sensing on loads and stuff like that. So, even though it's a basic series, Um, added that. Fantastic. And then we've got uh digital IO trigger as

**Dave Jones:** well. Really great for production to automated production test systems, which I've done a lot of in my career. Anyway, it's got the LANs and the USBs, and there's a Wi-Fi option as well. Oh, look at the big bolt for the toroidal transformer. Ho ho, everyone's getting a bit moist now. And uh interestingly, they got the voltage selection on the bottom here. Good old-fashioned switches. Nice. I like it. Warranty expires if broken.

**Dave Jones:** Not one stuff given. All right, so let's get this bad boy open. And even though this is the basic series, uh don't get excited that you're going to be able to get a Rohde & Schwarz power supply for a couple of hundred bucks. Um, this is still an advanced uh bit of kit. And it's, I think, um the price, like retail uh price is still like 1,500 Yankee bucks or something. So, it's not cheap, but Rohde & Schwarz don't make cheap bits of kit. That's why it's going to be

**Dave Jones:** really nice inside. So, can we lift this off? Whoa, we're in. Oh, look at that. Beautiful. Oh, very different. Very different to the uh NGE series, which was a real compact uh beast. Um, this one actually has a fair bit of uh space inside, and obviously, it looks like it's a full linear jobby. Cuz look at the size of these power supplies.

**Dave Jones:** Whereas the NGE series, uh that was a linear output stage. Here's a photo inside that with a little itty-bitty tiny output uh heat sink on the uh series pass uh linear element on the output. But then it had a tracking pre-regulator, which um pre-regulates like just just like a volt above the output or something like that. So, you don't need need much output heat sinking, but yep, sure enough, this bad boy looks completely linear.

**Dave Jones:** And that toroidal transformer, oh, absolutely brilliant. And one complaint I had about the previous one is that if you short out that bolt there, then of course you can get a shorted turn on the thing. So, if that that's a trap for young players. So, if that's actually too close to the top case, then you're going to come a gutter. But this one, nah, that's that feels like it that's got a whole finger width in there, so no worries. Oh, you can see you're getting your money's worth inside there. So, all

**Dave Jones:** the output is sleeved. Look at the Oh, it feels Oh, that feels It's not field of vision. Beautiful sleeving on that. And of course all the processing's on the front. We're not too fussed about the processing. There is the Wi-Fi option. I I think that's like a I don't think it comes standard. Don't quote me. Um but yeah, it might be like a software option. But there it is. So, I'm not too fussed. There's an Atmel something or other processor down in there for those playing along at home. Not too fussed,

**Dave Jones:** but yeah, that's the complete controller board down in there. Got the battery back up for the real time clock. It'll have really advanced ADCs on it cuz as I said, we're talking about .02% accuracy. We're talking about 1 microamp current resolution on the 200 milliamp range. So, you know, as we'll see when we power this up, it's got lots of digits for for current measurement. So, if you're a current measurement fanboy, ooh, this is a really It's going to be a really nice option for you for measuring

**Dave Jones:** like low power devices. And there's our output board down in there. Nippon Chemicon, of course, when you pay this sort of money for a power supply, even their basic series uses Nippon Chemicon caps. Absolutely very nice. So, we've only got 22 microfarads output cap. Plus I think there's I see some ceramic surface mount jobbies on the back of as well. but I won't uh take that out. But uh yeah, as with all lab power supplies, you want to minimize the amount of output capacitance because when you switch

**Dave Jones:** uh from constant current to constant voltage mode and vice versa, you don't want the energy in these capacitors cuz this is these are after their the current regulation uh circuitry. So, you don't want a huge amount of output capacitance cuz then that can dump current into your load above your uh current your current setting. So, yeah, um so that's good. 22 mic plus uh whatever, you know, a 10 mic ceramic or something on the back or 1 mic or something like that. So, nice low output

**Dave Jones:** capacitance, very nice. And this supply has uh supposedly really fast uh transients as well. So, fantastic for all sorts of production testing. Check out those beasts. Look at them, 6,800 mic a pop, 80 volts uh Nichicons. So, uh they must uh I 80 volts, it's got a 100 volt output. So, I assume that they're in series, are they? Let me just adjust the exposure here cuz those heat sinks uh really like can cause the camera to uh uh under expose for the rest of it. So,

**Dave Jones:** yeah, so we've got two banks of these. Um you might be wondering why we've got three heat sinks here when we've only got a two-channel regulator. Well, one of them, if you have a look down there, is for the bridge rectifier. So, yeah, just one alone for the bridge rectifier.

**Dave Jones:** And we've got a uh fan on the back. Uh of course, the uh heat sinks are all finned correctly to get uh the air flow through here. So, we've got the vents on the side at the front here. So, the air's drawn in here and then goes over the uh fins of the heat sink and extracted out the back there. So, not a particularly large fan. It is uh temperature controlled cuz when you turn it on, it does go and then it eventually uh switches off.

**Dave Jones:** And only if you do high loads will that come on. Nice attention to detail with this little heat sink down here. They've just got some Well, that's actually Oh, that's really hard. It's not really silastic. It's something else. Anyway, they're rigidly mounting on those. So, any vibration on the board won't cause these things to flap around in the breeze and vibrate loose and hit a resonant point and break off. Very nice.

**Dave Jones:** It looks like the code name for this project is Stingray. It's a Stingray motherboard. There you go. There's our mains input down there, beautifully crimped and screwed down to the chassis there. And that Yes, that is an Ethernet cable going from the Ethernet port on the back through to the Ethernet connector on the front panel board. I don't know what times 1600 means and this is has times 1601.

**Dave Jones:** So, I'm not I'm not sure what that's for. Buela Buela. So, our mains cable is heat shrunk like that and that goes over to Here's our input down here. There's our common mode choke and our protection and our X and Y class filtering. So, that's very nice. Can I get the rest of that out? And there's our main switch, real clunking main switch on the front.

**Dave Jones:** Nice. And I assume that this tap on the transformer here with this little power supply part, that's probably just for powering the front panel digital board, I'd say. And there's our voltage selection main switches down on the bottom of the case.

**Dave Jones:** I like how this is just all one big single board construction. Of course, you got to have the front panel separate because that's a totally different technology and it's isolated. And by totally different technology, I mean much higher layer count, everything else for the BGA packages and all the digital whatnots.

**Dave Jones:** But, this one down here, just one big analog jobby. Now, I can't read this detail on the screen here, but that looks like most of the control stuff for one of the channels. It's duplicated on the other side, so we don't need to see the other side there. So, yeah, it looks like we've got two shunt resistors here. They look like a couple of MOSFETs, are they?

**Dave Jones:** Yep, so they'd be doing your range current range switching. Is that your ADC down there? Not entirely sure. If we move over to here, this is the input of course coming from our transformer tap here. We've got input surface mount fusing down there, but that's not designed for protecting your output of course. That only pops in case of circuit failure. Now, in terms of the output here, of course they're going to have the current sense there. You can see the extra sense wire on so the main

**Dave Jones:** drive and then the main and then sense wire coming back for the positive and negative. They snake all the way along the back of the case over to a relay over here. So, that relay there, that could be for doing your series parallel stuff. So, I'd say that's the case there, and of course that's right near our output sense connections as well. Not sure what's happening down in there.

**Dave Jones:** Hard to get the right light at the right angle to see a part number on that jobby. Once again, can't read that part number from my camcorder screen, but something's going on there, which is interesting. That's smack in the middle of the design, so it's like shared both, but then we've got jumper settings there. Once again, with the X designator, so not sure what what setting that's got.

**Dave Jones:** Here's our bridge rectifier. There's actually another one next to it. It's hard to see in there, but it's a smaller one, and that's duplicated on the other side as well. So, this one heatsink handles four bridge rectifiers. So, one would be the main power bridge rectifier, another one would be a secondary one for pairing something else, like the control stuff.

**Dave Jones:** And there is our main output MOSFETs with a nice-looking temperature sensor on the heat sink there. That's very schmick, of course. Any decent power supply, especially in this sort of price class, even though it's a basic, in quote marks, model. Yep, nice. This thing would be bulletproof. So, there you have it. That's a teardown inside this bad boy, and uh very impressive, of course. Very high-quality construction, high-quality components used, and and it'd be lots of precision parts as well.

**Dave Jones:** As I said, we're talking about 0.02% class accuracy with uh yeah, it'd have a really high resolution ADC in this thing, and current range switching and stuff like that. Let's actually uh put this thing back together, power it up, and I'll show you the resolution on this, which is really quite remarkable for like the bottom-of-the-range instrument. Okay, so let's turn it on, and as with the uh NGE series, you turn it on.

**Dave Jones:** Don't know if you can You can probably hear that, but trust me, that is really loud. I don't know why they have to default to like maximum turn on for the fan. It's really annoying. I know the process is not booted up yet, so the fan just defaults to, you know, 100% on, but if there was some way that they could fix that, that'd be really nice. Anyway, oh. Oh. Straight off the bat, everyone's soiling their pants. Look at the resolution on that current.

**Dave Jones:** We're talking six-digit resolution. This is incredible. That's 10 microamps there on like the full 2-amp range. So, let's change the current here, and sure enough, oh no. No, okay. So, the set current, we can only go to 1 mA. Yeah, I believe I read that in the manual somewhere. That's all right. But, uh the readback current, I assume, unless these are two digits on the end are fake, then yeah, we should be able to read 10 microamps resolution on the 2 amp range.

**Dave Jones:** That'd be incredible. That's amazing dynamic range. You know, if you're developing like a Wi-Fi product or something like that, you can like just keep it on the 2 amp measurement range and measure, you know, like an amp when it's transmitting or you know, you got a some high-powered product uh doing something like uh transmitting a decent amount of RF or whatnot, and then you uh and then when it goes to sleep um or just, you know, background idle or whatever, and it's drawing, you know, 100 microamps or something, you can

**Dave Jones:** still get decent resolution on that. Nice. Yeah, so the minimum we can go there for our constant current mode is 1 milliamp, but of course, that's like plenty. So, let's just uh switch that output on, right? So, we'll set it to 20 volts.

**Dave Jones:** What it Well, look, we can I can show you that uh it can actually go much higher than that. There you go. 100.05 volts maximum. Not too many power supplies on the market can do uh you know, 0 to 100 volts. As I said, uh this is the 142 model. The 102 model actually has uh 35 volts maximum output, I believe.

**Dave Jones:** You know, your more traditional uh voltage range power supply. But, with that, of course, you get extra current. You get 6 amps instead of 2 amps maximum. So, the uh key layout's all the same. The operation is the same as the previous one, except uh of course, the display is uh significantly different to the previous one. As you can see, the uh display is uh significantly different.

**Dave Jones:** This uh new NGA one actually has a lot more information. It's got your P min and P max uh here, and of course, your V min and V max. Uh and of course, it's only uh dual output, and that's why I guess it can display more, but this one could have uh displayed the same sort of info. So, I they do have a new like they've got a B model of this or something, I believe now. I'm not sure what the uh differences are, but yeah,

**Dave Jones:** because this one's been out for quite some time. But yeah, that is a nice display. Not as big. I guess it would be nice if it had like options to like make the display a bit bigger or something like that like the fonts a bit bigger and maybe if you didn't need this other stuff, you could have like a bigger display like up here or something like that. But as I said, this has got more digities, more goodness. But look at the resolution difference. I mean, this is only like

**Dave Jones:** three digits for the voltage, four digits resolution for the current. This is six digits for the voltage and six digits for the current. You know, no contest. But of course, there's a reason why both of these models exist. Like this one it might be more suitable for some tasks and this one's more suitable for other tasks. So, it's not like this one is just better in every respect than this one here. It's you know, pros and cons. Go and read the data sheet for yourself. I mean, this is triple output

**Dave Jones:** for starters, smaller form factor. You know, it's significantly different. So, let's switch on our output here and see if we do get the extra two digits measurement resolution there. So, let's see if we go down to 10 microamps and we do. Yep. Yep, that's incrementing by single digits there. Like so, we're down in the noise. Like so, it's even though we've got no load on this thing. Can we actually zero that out? I'm not I'm not sure if they have the ability to do that. That'd

**Dave Jones:** be nice, wouldn't it? Given that you know, they advertise the capability of this thing to measure like down to one microamp. So, apparently there is a 200 milliamp range we can switch to and we get an extra digit yet again. Now, this is interesting though.

**Dave Jones:** Like it's given us like V min 16.5 volts here. So, is that like what it's actually measured? Minimum? Like that doesn't seem to Is that changing? No, it's 16.5 volts minimum. That doesn't make sense. And 3.77 W maximum? I've got this uh set to 100 mA.

**Dave Jones:** It would have been nice to put the display here and show what our current uh limit is. With, you know, I've set that. There it is there. I set it to 100 mA current limit, but they don't actually uh display that. Which with all the information on the screen, like why not?

**Dave Jones:** Yeah, I don't get this at all. Look, I've been playing around with this and uh look, it's I've got no load on here and it's showing me like P max equals .36 W. Where did it get that from? And uh as you saw before, it was like 16 V from 100 V. What was it measuring that minimum when it was ramping down? When I actually switched the output off like that, on and off. If I just I don't know.

**Dave Jones:** Keep doing that a number of times. Will it is it like glitching or something? Or, you know, taking the measurement at the inappropriate time when it's But how it does that for like current? I I don't know. Like I maximum, like 21 mA.

**Dave Jones:** Or where's it drawing 21 mA? I've got no load. Don't get it. So, anyway, yeah, these V min V max, these are operating like your digital multimeter min max mode. Oh, and P min max as well. Um, so it's like historical uh data to show you, but I can't I had a look at the manual and I can't see where it like it doesn't it just mentions this. It doesn't sh- uh tell you where to reset it or anything like that. I mean, you know, you go into menu and it's like,

**Dave Jones:** "Well, where do you reset that?" I don't I don't get it. So, yeah, that's that's strange. I don't like they've got all this uh min max information here. Like there should be like a min max enable button on the front panel. Um, really? I mean, electronic fuse button? Like, you know, that's you could argue you should be like buried away in the menu or remote well remote local that's okay. A log button of course and yes we do actually have USB logging but got no stick. If we plug

**Dave Jones:** in a sticky duder, is it going to just automatically log that and it does 10 readings per second detecting USB. Come on. What? Finally got a USB stick that works. Supports FAT32 only but yeah, there we go logging started. So presumably it like logs all the voltage and current and everything else. I'll overlay what I've got here anyway. So even I've got no load but it should get something. Should log voltage and current for both the channels continuously at 10 times per second. So that's really nice.

**Dave Jones:** Anyway, let's go into our menu here and have a look. Yeah, similar sort of thing. Output protection fuse easy arb easy ramp. There's some features for doing programmability. Current range, there it is current range. So yeah, it's not automatic. We have to go in there and select that. Current range ah, there you go. Current measuring you set it separately for each channel. So let's go low there.

**Dave Jones:** And boom and get out of that. Boom, look at that. One micro amp resolution. Thank you very much. And once again, we're just seeing the like the current noise floor here basically. And ripple and noise here over 20 MHz bandwidth, we're only talking like 150 microvolts RMS. This is no load at 10 volts. It's spec for the 142 is less than 1.5 millivolts. So it's like an order of magnitude under that with no load. The 102 models actually 500 microvolts ripple and noise RMS. And ripple and noise at 3.3 volts at 1.5

**Dave Jones:** amps. I had to set my current range to auto like the current resolution there to auto. You can actually set it and it jumps up. Otherwise, it yeah, you can come a cropper. Anyway, 5 watts there. I've only got like a little in load on it. 12 millivolts peak to peak, but still well under spec at 750 microvolts.

**Dave Jones:** Anyway, this is not a review. I'm not going to go to town actually reviewing the performance specifications on this thing. I'm sure it meets every single one of them. It's a Rohde & Schwarz. Okay, let's single shot capture this into a 2 ohm load. So, 3.3 volts into a 2 ohm load with 2 amp current limit.

**Dave Jones:** We'll just switch that on and boom, that ramped up nicely. You can see it doing some Yeah, it looks like Is it doing some hunting in there? But as always, we're looking for overshoots there and there aren't any. So, yep, that is clean. Although, it's almost as if that is a deliberate ramp on. I wonder if there's like that's part of the No, that wouldn't be part of the easy ramp thing, would it? No. No, it's Anyway, that's only like 2 milliseconds there. So, yeah, no worries.

**Dave Jones:** Doesn't overshoot. That's the main thing. All right, so what I'm going to do now is just test the transient with constant current. So, I've lowered it to 1 amp here. So, how quickly will it go into constant current mode? Will it detect that there's an over current and will it go in? So, let's yep, let's set that up and boom, there you go. That's interesting.

**Dave Jones:** So, there you go. You can see it ramp up like it did before. It went to its 3.3 volts. So, it went to the output voltage and then it took 5 milliseconds. It took like 8 milliseconds or something, 7-8 milliseconds to realize that Oh, I need to go into constant current mode. So, it's over volted on that and there's a little That's interesting little blip in there before it realized No, I need to go into constant current. Thank you very much. So, is that a problem?

**Dave Jones:** Well, potentially. You know, it depends on your application. So, okay, for comparison, let's see how this new Keysight EDU triple output power supply does under exactly the same circumstances. 3.3 volts with 1 amp current limit into my 2 amp resistive load here. So, let's give that a whirl.

**Dave Jones:** And switch it on. I've got exactly the same time base as before. I don't think I've touched that. Lower the trigger level down here. And There you go. That is significantly different. But that one doesn't overshoot in terms of voltage, does it?

**Dave Jones:** So, once again, it's got an interesting characteristic response here that just so happens to be near the That's just a coincidence that it's near my trigger level here. Of course, if I increase my trigger level up above that, we can do that again. There you go.

**Dave Jones:** So, yeah, that's got an interesting response there. But this one doesn't over volt. So, yeah, it's got a bloop bloop. Yeah, so the Rohde & Schwarz one is not that good in terms of its constant current at switch on capability. So, I'm wondering if they can, you know, tweak that in software or something.

**Dave Jones:** Because yeah, that's a potential issue. You don't want your Technically, cuz because you're over voltage in there, you are also over currenting. Cuz it's simple Ohm's law. Voltage at 3.3 volts into your 2 ohms is above your 2 amp your 1 amp current limit, of course. So, yeah, so you're over over currenting here. Whereas the Keysight one won't do that. And I'm sure if we measure a whole bunch of lab power supplies, they're all going to operate they're all going to have their own characteristic response for something

**Dave Jones:** like that. But yeah, um that's a bit disappointing that that overshoots. It may be interesting Let me try the NGE series and see what happens on that. There you go, 3.3 volts, 1 amp. Let's give it a whirl, see what we get.

**Dave Jones:** There's our previous Keysight one, and let's single shot capture that. I've gone back to 5 milliseconds per division. Oh, there you go. Once again, see, significantly different response. 5 milliseconds per division. So, it takes much longer, and it has a different kind of there once again, there it's ramping up. There is some overshoot, and it eventually comes back. Let's just run that again.

**Dave Jones:** And I've got positive edge trigger, so I can just switch it off and on. There you go. Once again, it's overshooting like that. So, yeah, both of these Rohde & Schwarz supplies have a problem with constant current overshooting. No no problems at all with constant voltage, of course, when you switch that on, it's just hunky-dory, but yeah, that's something that they might want to look into. So, I don't know if this would be a real-time software response loop doing that, or whether or not it's a you know,

**Dave Jones:** an analog loop in the supply. But anyway, I hope they can fix that, cuz that's that's certainly something to consider, cuz technically, that is overcurrenting. Not by much, but yeah, both of them do just do that. Interesting. Now, check this out. What I'm going to do is I'm going to actually change this to 20 volts. Let's just mucking around with it, and I discovered this. Okay, I've got the same 1 amp current limit, so you'd expect to it to have the same result. We've seen some

**Dave Jones:** overshoot already in voltage, but on the 20 volt range, this didn't happen on like the lower voltage ranges, but 20 volts. Nothing else has changed. Okay, watch this. Ta-da! Look at that. It ramps up, and it like it it goes up, right? We're 10 milliseconds per division, so after like 6 7 milliseconds or something, it determines, "Oh, I need to current limit, right? So, it's it's headed all the way to it's uh 20 volts and uh then it's come back down and it's it's sort of, you know, clipped it at 4 volts

**Dave Jones:** there and then it goes, "Oh, if it like for another uh you know, 10 milliseconds, 11 milliseconds." Then it goes, "Oops, nope, I'm still over voltage. I need to um like current that down to limit the current." So, that's interesting. But, if we do that at I'll go back to uh 3.3.

**Dave Jones:** Okay, so I'm going to take a 3.3. Single shot capture that again and boom, we got it. Uh once again, it's it's clamped like that, but at a different voltage again now. So, that's interesting. And if I go to 10 volts, let's try that again. Single shot capture, output.

**Dave Jones:** And they are we can see it's sort of starting to do the thing there, but it then goes back down aggressively. So, that that really depends on the uh voltage range that we're actually got there. And another interesting thing, check check this out, right? If we're going to voltage and I'm twiddling this, I'm still in constant current mode, but you'll actually see this go green.

**Dave Jones:** Whoop, you see? It goes green like that and it not sure what the deal is there. So, is it jumping out of constant current mode? Um maybe we need like a live uh display. Okay, so I've got it in roll mode now and we're in current limit down here.

**Dave Jones:** So, let's see what happens if we change this voltage again. Let's go see if it jumps out of constant current mode. Oh, yeah, look look look at that. Look at that, it's jumping out of constant current mode. That's interesting, isn't it?

**Dave Jones:** WOW, WE should be able to single shot capture that. Actually, let me get out of roll mode. All right, so let's see if we can capture this. I've got uh 10 milli sample milliseconds per division. Okay, I'll go into I'll adjust the voltage while we're in constant current mode, remember that, and you watch it, it's going to jump. We saw those little spikes. Now we'll zoom in and we'll capture those spikes.

**Dave Jones:** Can up. No, it just went out there. There we go. Bingo. Captured. It It lasts for like, you know, 12 milliseconds or something like that, and it's jumped out of constant current mode when we adjust the voltage. That's very interesting. Why is it doing that? Oh, it's not a consistent time. That's a bit nasty, isn't it?

**Dave Jones:** Wow. Yeah, um like you shouldn't It shouldn't jump out of constant current mode when you adjust the voltage like that. Uh I think we have a glitch. Anyway, this isn't going to be a review. There's going to be like this has a whole stuff a whole bunch of stuff. As I said, uh it's got the arbitrary waveform stuff.

**Dave Jones:** It does the easy ramp, which is I think I've had a look at that in previous videos on the previous model, haven't I? But uh yeah, of course you can turn on remote sensing here, channel fusion. I assume that's parallel and series, cuz that's hilarious. Channel fusion.

**Dave Jones:** Connection mode. Yeah, that'll be series parallel, surely. Oh. Can we Can we Oh, yeah. Yeah, there Yeah, series parallel. Channel fusion. I love it. Germans. I'm sure if you want to look into this, there's a whole bunch of stuff that you can play around with. Ethernet, the wireless LANs, the digital IO, and stuff like that. What can we do with our digital IO?

**Dave Jones:** Uh that's It's just trigger, I believe. I don't think it's uh uh output on condition, output on. See, there you go. So, when it's receives a digital input trigger on channel one or whatever, you can, you know, make it do stuff. You can make it I don't know. Can you condition like that.

**Dave Jones:** Let's have a look. What options do we have? Output on, output off, fuse trip. There you go. Constant current mode, voltage level. There you go. So, critical event, easy arb active, so you can turn on your arbitrary mode. I was hoping it would do that. So, yeah, that's that's pretty flexible stuff. Utilities, system test, update, service, all that sort of jazz.

**Dave Jones:** Anyway, there you go. That is very cool. That's I like the current resolution on this thing. Um absolutely amazing. I can't remember the specs on the current. Hang on. It's actually uh 0.03% of the current, which sounds impressive, but it's got a little uh plus 500 microamps next to it. So, the uh low current stuff, absolute accuracy, you get the resolution uh of course, which is down to 1 microamp.

**Dave Jones:** Accuracy not necessarily there, but still, to get that sort of resolution on a uh you know, basic series power supply like this is really quite incredible. So, 0 to 100 uh volts, very versatile. Go up to 200 volts in series with uh that sort of current resolution. Very versatile supply. Or you can get the uh 102 version, which is the uh zero, you know, your more traditional uh 35-V model. Anyway, if you want me to do any specific uh tests on this, I can, and just dump it on my EVblog2 channel.

**Dave Jones:** About to hit 100,000 subscribers on there. So, definitely go check out and subscribe to EVblog2 and set the bell notification, all that sort of wanky business. And as I said, I've got uh two of these bad boys to give away. One is the 104 model you see here, the 100-V.

**Dave Jones:** One is the 102 model, the 35-V uh 6-A jobby. So, what I'm going to do, because the uh YouTube uh comment system is always a show. Um I'm just like, no. I'm going to go I'm going to create threads over on the EVblog forum, and one of them will be a random draw. So, I'll link to a EVblog thread down below.

**Dave Jones:** Check it out. You have to be a an existing EVblog forum user. You can't just join now and one post and you know, enter. Sorry, but you know, it's for those who contribute to the site. I think that's fair enough. And I'll also give one away to a hacker space, maker space, school, something like that. So, that will be judged by me. So, I'll have a separate thread for that. Put in your you know, submit a video entry or whatever. Submit, I don't know. I'm just

**Dave Jones:** yeah, we're a hacker space and we need one of these things and I don't know. I'll choose a worthy winner. So, thank you very much Rohde & Schwarz for providing these to give away to my audience. That's fantastic and an interesting look inside a completely linear supply this time instead of the combined tracking switching pre-regulator which you get in this. But, of course, you get advantages in that it is more powerful.

**Dave Jones:** It's got triple channel, of course, more total output power, a smaller form factor, all that sort of jazz. But, yeah, if you want a nicer cleaner linear supply like this, then check it out. Link down below. So, if you like the video, give it a big thumbs up. As always, discuss down below. Catch you next time.
