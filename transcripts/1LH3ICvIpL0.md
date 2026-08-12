---
video_id: 1LH3ICvIpL0
title: EEVblog 1622 - The BIG BEGINNER MISTAKE with Multimeters
url: https://www.youtube.com/watch?v=1LH3ICvIpL0
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 33, "3": 46, "4": 64, "5": 77, "6": 91, "7": 105, "8": 122, "9": 143, "10": 161, "11": 176, "12": 193, "13": 219, "14": 233, "15": 248, "16": 262, "17": 276, "18": 290, "19": 307, "20": 319, "21": 334, "22": 351, "23": 367, "24": 382, "25": 396, "26": 413, "27": 429, "28": 445, "29": 462, "30": 477, "31": 493, "32": 508, "33": 521, "34": 536, "35": 549, "36": 559, "37": 574, "38": 588, "39": 603, "40": 616, "41": 629, "42": 643, "43": 655, "44": 668, "45": 681, "46": 694, "47": 708, "48": 721, "49": 734}
---

**Dave Jones:** Hi, I just had one of my BM5235 multimeters returned from a customer saying that they believe it's faulty because here's a photo, they had an old multimeter measuring a CAN bus and it was measuring the 60 ohm load on the CAN

**Dave Jones:** bus, no problems. Of course, the CAN bus has a nominal 120 ohm load resistor on each end of the bus. It's a serial transfer bus often used in cars. So, I believe he's using it in automotive. And he sent me photos of the BM5235 not

**Dave Jones:** working and it was showing weird values that weren't the correct 60 ohms on the CAN bus. And it didn't matter whether it was on ohms range or whether or not it was in continuity mode, it just measured the

**Dave Jones:** wrong value. Whereas his old cheapo multimeter measured precisely 60 ohms. What's going on? Now, this is actually no fault of the multimeter whatsoever. In fact, basically the customer got lucky with his old multimeter that it could actually measure the 60 ohms on

**Dave Jones:** the CAN bus. So, I'm going to demonstrate here. I've got a demo board here which has a CAN bus on it and we're measuring our 60 ohms here. I've I've put the extra 120 ohms like simulating the other end of the line. So, we

**Dave Jones:** measure the 60 ohms. So, why is this one working and his one didn't? Well, it's because the CAN bus is not switched on. It's isolated. There's no electrical signals on there. The drivers have been switched off. And you can see

**Dave Jones:** that the CAN bus is actually switched off here. Okay, so there's no signals on the CAN bus. But if I actually enable it by cycling through here, what? Look, zero ohms there. And it doesn't matter whether or not it's in ohms or

**Dave Jones:** continuity mode, it's measuring zero ohms. But it could actually measure anything. Let's try a few more multimeters to see if it's the 235. Got a Fluke 77 or I've modified it to a 177 here. Uh minus minus 305 ohms. What?

**Dave Jones:** How about the classic Fluke 87 5 here? 60 ohms. We switch the CAN bus on. Minus 304. How do you get negative ohms? Keysight U1272A, excellent multimeter. CAN bus off, 60 ohms. CAN bus on, uh minus 208-ish. $20 chippy, the ANENG 8008, which is a

**Dave Jones:** pretty decent meter for the price. Uh whoop, zero, just like the BM235. Fluke 101 meter. What? Does zero, exactly the same as the BM235 again. But interestingly, watch what happens if I change the polarity here from the CAN. So negative is on CAN

**Dave Jones:** low and positive is on CAN high. It's not zero anymore. It's 21 megaohms. 21 million ohms. What's going on? Of course, if we switch the CAN bus off, we're going to go back and we're actually going to measure our 60 ohms,

**Dave Jones:** no worries. Back to the BM235 again. If we change the polarity on the probes, we get 34 megaohms. And if we turn off the CAN bus, we get our proper 60 ohms. Klein Tools MM500. Whoop, overflowed. A really old Metrix

**Dave Jones:** MX44. Whoop, 360K. Different again. Uni-T 61E, 60 ohms and then what? Zero. 121GW, and then 45 kiloohms, whatever it is. Once again, totally different. So why do we get the incorrect reading when we switch the CAN bus and measure a live circuit here?

**Dave Jones:** It's because well, anyone with any decent experience of using multimeters knows that you never uh use the ohms range to measure a live circuit. And indeed, here's the user manual for the BM2235. Here it says, if you use it on a live

**Dave Jones:** use the ohms range on a live circuit, it may give you incorrect readings. And also, it could potentially damage the meter, but most multimeters on ohms range actually have like decent protection in them. In fact, you can put 240 V mains across this in

**Dave Jones:** ohms range and you're not going to damage it, but you're certainly not going to be able to measure anything in circuit because ohms range works by putting a current through your resistance and back into the meter and measuring the voltage drop across it.

**Dave Jones:** And if your circuit is feeding in external voltages via a low impedance path, that can upset the reading and the current and your meter can measure an incorrect value. It might be slightly out, it may be way out, it may show zero

**Dave Jones:** that we saw, it might show negative values cuz the multimeter is just absolutely confused. The software doesn't know what to do and it's just putting a negative number in there even though you can't get a negative resistance. So, yeah. Don't use ohms

**Dave Jones:** range to measure your live circuit. If you do, you get what you get and you don't get upset. So, in this particular case, the customer either got really lucky with that multimeter that somehow it's not disturbed at all by the external voltage

**Dave Jones:** that happens to be here on his particular CAN bus that he's measuring or he's measuring it with the CAN bus switched off. Either one of those, but I couldn't find a single meter here in the lab that wouldn't give me an incorrect

**Dave Jones:** reading on this particular CAN bus. So, let's get a bit more technical. If we probe across the CAN bus here with our oscilloscope, this is what we get. We get a packet of data which is basically with 500 mV per division here. So, it's

**Dave Jones:** about a 2-V peak-to-peak signal here and it's just I'll stop that so you can actually see it. It's all this data in here. And well, all this stuff is being superimposed on your multimeter and your multimeter is trying to feed current through that

**Dave Jones:** 60 ohm resistor, yet it's having this driver chip in there force all of these voltages and all this high frequency switching stuff I across essentially your load resistor that you're actually trying to measure. And well, the multimeter does is not designed for

**Dave Jones:** this. It's not designed to handle external voltages and currents being actually pushed in to essentially pushed into the multimeter. So, it's going to really upset the apple cart. That's why you could get just any unpredictable result when you try and measure ohms on

**Dave Jones:** a live circuit. You don't know how your multimeter is going to react cuz it's not specified at all for any external voltages. And it's a similar reason why you don't measure resistors in circuit. Here's a 10k resistor in circuit. What

**Dave Jones:** does it measure? It might measure 10k, but in this case, nope, 3.5k. It's It's not because this board's powered up. It's not It's switched off, but there are other components in parallel with that resistor that when this multimeter

**Dave Jones:** drives current out here, it may go elsewhere in the circuit and not all of it goes through the resistor. So, it's can upset the reading. This is like using multimeter 101 stuff. Don't measure resistors in circuit. Almost any

**Dave Jones:** multimeter manual should tell you that. Break the circuit before measuring. Same thing applies when you're measuring a powered up circuit. Any external voltages can upset the apple cart. Now, I won't go into major detail on the CAN bus, but it is actually a differential

**Dave Jones:** signal and it doesn't actually sit on zero like this. And if we actually change the polarity of our single-ended probe here, and I won't go into single-ended versus differential, look, there you go. It goes in the opposite direction. And if we don't probe across

**Dave Jones:** the bus and actually take it to the circuit common ground here, then we measure something different again because it's actually a biased signal. Well, now we're at 1 V per division, so it's actually biased by 1 2 2.5 V. So,

**Dave Jones:** there's our signal there and we're probing the high bus. And if we probe the low bus, there you go. It goes from 2.5 V in the negative direction. So, it goes positive and negative above and below 2.5 V. So, we've effectively got a

**Dave Jones:** 2.5 V offset voltage on there. Here's another simple example. I've got a just a 62 ohm resistor here and I've connected across a power supply here which is switched off, but it's not 62 ohms. It's already already there's

**Dave Jones:** something inside there that's upsetting the apple cart, right? Even though this output is switched off because there's something across these terminals even when you switch it off that causes it to drop from its 62 ohms. So, let's actually switch the output on here. I've

**Dave Jones:** got a set to 0 V here and it doesn't really upset it at all. But, what happens if I change my voltage by .1 just .1 100 mV .1 V. It's gone up to 647 ohms. What happens if I change it to .2

**Dave Jones:** V? 2.5 k ohms. Look at this. 4 k like a 40 like 59 k, right? You just have no idea and now it's open, right? You have no idea what's going to do what's going to happen. And if we swap

**Dave Jones:** the polarity of it here, look at this. What do we get? We get that zero that we saw before, okay? And I bet you if I tried this on a Fluke multimeter, we might be able to get that

**Dave Jones:** negative we saw before. And sure enough, there it is -1 meg at 1.2 V there and we switch it off and we get a once again like that 58 ohms there. So, like come on. And we'll swap the polarity back on

**Dave Jones:** the Fluke and see what we get here. There you go, 1.3 meg. So, when the polarity was swapped here, it's going to show a negative, but the EEVblog Brymen meter didn't show that. Why? Is there something wrong with the

**Dave Jones:** Fluke? No, absolutely not. This is one of the best industry standard meters on the market. There's nothing wrong with the BM9235 either. There's nothing wrong with any of the multimeters that we've seen. It's just when you introduce an external

**Dave Jones:** voltage or you have something in parallel with your resistor that you're trying to measure on your ohms range, you're going to come a gutser like this and well, you can't take your reading at face value. It's absolute 101 beginner

**Dave Jones:** stuff when you're using a multimeter on ohms range, don't have anything else in parallel with your resistor. You can try and measure resistors in circuit on an unpowered circuit and occasionally, you know, there's often not enough things in

**Dave Jones:** parallel and there are some multimeters that actually have a low enough threshold voltage on them called a low ohms range and they actually output less than 0.6 volts on the terminals here and that's not enough voltage to turn on

**Dave Jones:** active semiconductors within your circuit. It was very common back in the 1980s, for example, for multimeters to have low ohms range, but some multimeters will have it by default and the output voltage on here can change depending on the range that you're

**Dave Jones:** actually using. So, what I'm doing here is I'm using the BM9235 to measure the output voltage of the ohms range on this Fluke here and you'll see we're 2.8 volts on the 60 meg ohms range, but if I

**Dave Jones:** actually change that to the 600 ohms range, we're 7.3 volts cuz this thing uses a 9 volt battery, whereas you won't get those higher voltages on a multimeter that uses say two AAA batteries, only 3 volts maximum. So, we

**Dave Jones:** change the range again and again and look, 600k range is down to 3 1/2 volts, change it to 6 meg, it's back up to 5.6 volts. So, it's all over the shop. So, just that output voltage alone, that can

**Dave Jones:** actually change how you measure resistors in circuit, which is why it's not recommended to do it because you don't know what your multimeter's outputting in voltage. It's not specified for it. It's just something that you have to be very cautious in

**Dave Jones:** doing and especially when you're measuring live circuits like this CAN bus here that can inject voltages and currents with different impedances into your circuit and it's going to screw up your multimeter. You're going to come again at her. So, there you go. I hope

**Dave Jones:** you learned something very interesting about your multimeter. And this is kind of like beginner level stuff, but you usually learn it the hard way as I think this customer has. But anyway, if you enjoyed that video, please give it a big

**Dave Jones:** thumbs up and as always discuss down below. Catch you next time.
