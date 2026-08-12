---
video_id: O2ohz8DyJoQ
title: EEVblog #577 - Precision 1A Current Source Part 2
url: https://www.youtube.com/watch?v=O2ohz8DyJoQ
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 33, "3": 41, "4": 68, "5": 84, "6": 100, "7": 109, "8": 118, "9": 128, "10": 140, "11": 162, "12": 174, "13": 193, "14": 204, "15": 218, "16": 235, "17": 243, "18": 254, "19": 279, "20": 292, "21": 307, "22": 317, "23": 332, "24": 347, "25": 356, "26": 366, "27": 375, "28": 388, "29": 401, "30": 411, "31": 422, "32": 436, "33": 450, "34": 465, "35": 479, "36": 488, "37": 501, "38": 511, "39": 521, "40": 537, "41": 546, "42": 554, "43": 566, "44": 578, "45": 588, "46": 599, "47": 615, "48": 629, "49": 645, "50": 657, "51": 670, "52": 680, "53": 696, "54": 710, "55": 724, "56": 738, "57": 744, "58": 763, "59": 773, "60": 785, "61": 797, "62": 818, "63": 839, "64": 851, "65": 864, "66": 880, "67": 893, "68": 908, "69": 928, "70": 936, "71": 945, "72": 955, "73": 969, "74": 981, "75": 993, "76": 1002, "77": 1019, "78": 1039, "79": 1051, "80": 1061, "81": 1069, "82": 1082, "83": 1100, "84": 1123, "85": 1136, "86": 1157, "87": 1184, "88": 1202, "89": 1215, "90": 1226, "91": 1240, "92": 1258, "93": 1282, "94": 1293, "95": 1307, "96": 1328, "97": 1339, "98": 1351, "99": 1377, "100": 1388, "101": 1409, "102": 1419, "103": 1431, "104": 1443, "105": 1457, "106": 1472, "107": 1487, "108": 1504, "109": 1520, "110": 1534, "111": 1549, "112": 1558, "113": 1572, "114": 1587, "115": 1601, "116": 1616, "117": 1632, "118": 1651, "119": 1671, "120": 1681, "121": 1692, "122": 1706, "123": 1715, "124": 1724, "125": 1736, "126": 1757, "127": 1775, "128": 1788, "129": 1797, "130": 1811, "131": 1821, "132": 1833, "133": 1844, "134": 1855, "135": 1869}
---

**Dave Jones:** Hi, in a previous video, which I'll link it in down below if you haven't seen it, we played around with a precision 1 amp current source. Ignoring all this sort of stuff, we were basically following the application note circuit here in the LTC6655 data sheet.

**Dave Jones:** This is a precision 1.25 V voltage reference. And this thing oscillated the buggery. It was absolutely awful. And and since then I've tried a couple of I've tried the other recommended configuration with the PNP cuz I suspected this thing might oscillate.

**Dave Jones:** That's why I breadboarded the thing up. Never trust these application notes just to work. Oh, you got to build the things up and test them, let me tell you.

**Dave Jones:** And since then I've tried various configurations. I've tried the other one here with the PNP configuration, but that one was a dog too, especially at higher currents. And I tried some FETs in other configuration and various various other things to try and stabilize the loop on this thing cuz internally it's an op amp and well, you know, if you don't get the loop stable, which I won't go into,

**Dave Jones:** it can it can oscillate and that's exactly what we saw, especially at high current load. So, I thought I'd have another crack here using another circuit we you've seen before, which I'll link in down below as well if you haven't seen it.

**Dave Jones:** This is just my simple constant current dummy load. But whoa, hi, a dummy load at its constant current, right? That's exactly what we need, 1 amp. I don't necessarily need the ground referenced output that we had on this circuit here.

**Dave Jones:** You can see the transistors in the upper half and the output current actually goes down to ground like that. Well, don't actually need that cuz it's going to be battery isolated anyway.

**Dave Jones:** So, I figure my load can be on the high side. So, I thought I'd go back to this uh, configuration I've used before, which can also be unstable, of course.

**Dave Jones:** Um, you know, nothing new there. It's still got a loop in here. It's still got the op amp and everything else, and you have to stabilize that loop, but I thought I'd give this one a crack and see what we get.

**Dave Jones:** So, we're going to build it up on the breadboard here. I've got my N-channel MOSFET. I just pulled one out of the junk bin. It's an RFP3005, and I've now got, which is very nice from Vishay.

**Dave Jones:** Thank you very much, Vishay, for sending me samples of these very nice 1.25 ohm uh, four-terminal uh, 0.02% I think it is precision resistor. Really quite nice. So, this will actually allow us to get some a very nice uh, four-terminal wire measurement even on a dodgy breadboard, which we're going to see.

**Dave Jones:** And I'm using the same thing. Oh, I didn't write it in there, but yes, it's still the LTC6655. I'm going to still stick with that. So, 1.25 V over 1.25 ohms is going to give us my constant current of 1 amp.

**Dave Jones:** But, hey, let's build it up, see if it oscillates. It probably will. Um, we can almost certainly make it oscillate under uh, certain uh, circumstances. The output uh, capacitance here and uh, and the and the uh, load current and the input capacitance and all sorts of stuff.

**Dave Jones:** So, um, yeah, we probably can get it to oscillate, but let's see if we can actually get a precision 1 amp current source on our breadboard, which we intended to last time, cuz these configurations uh, here just sucked.

**Dave Jones:** As I said, thank you very much, uh, Vishay, for sending me samples of this 1.25 ohm. There's the exact part number there. If you're playing along at home, you can actually uh, order these on uh, Digi-Key, but I think there's a minimum volume to actually uh, order them.

**Dave Jones:** So, it's a 1.25 ohm 0.0 uh, 2% and it's the VPR uh, 221 series. I'll actually link in the data sheet down below. Really awesome tempco. Fantastic resistor for using in a precision current source like this.

**Dave Jones:** And here's a little strip they come in. They sent me a few of them. And well, if you're going to make them because these aren't made to order actually.

**Dave Jones:** They you can order any value you like and they will laser trim it for you. Vishay are fantastic. Um And yeah, there it is. A four terminal TO-220 package.

**Dave Jones:** Fantastic. So the two outer pins on there are the current in and out and the two inner pins are the two sense pins in here on our circuit. So even on a dodgy breadboard we can hook this thing up and get really precise four terminal measurements because the two sense pins are tapped right inside the right on the resistor in there.

**Dave Jones:** Hence why I'm going to use a really nice precision resistor like this. So we've got our like .02% precision voltage reference here. We've got our .02% precision four terminal resistor worst case of course.

**Dave Jones:** So we should really be able to get, you know, like a .02% or better one amp current source reference out of this sucker. But even if we do get this thing stable and build it up, there's going to be an issue with this circuit and I've deliberately left it out.

**Dave Jones:** And if you want to try and figure out what it is before we get to it in the video, hopefully I can get the thing stable and we can actually see there's going to be some output error here.

**Dave Jones:** There's not we're not going to get precisely one amp. And try and figure out why. So you can stop the video now, look at the data sheet for the LTC6605, try and figure out why we're not going to get precisely one amp through this resistor.

**Dave Jones:** Hmm. So this is the circuit we're going to build up on the breadboard here. As the data sheet recommends of course the um uh sense line must have a bypass cap of at least 2.7 microfarads and less than .1 ohm ESR.

**Dave Jones:** It's got to be a low ESR because the transfer, you know, function if you look at the loop stability and all that sort of stuff, you can't have too high a value ESR.

**Dave Jones:** The ESR is an equivalent resistor in there like that. So, I've got a 10 microfarad ceramic in there. Should be good enough. I've got a series resistor in here.

**Dave Jones:** I think I've got a 12K, I think it is, just because the gate capacitance, we we just want to slow this thing down. We just want to add um some roll off in there.

**Dave Jones:** So, you want to put a series resistor in there of, you know, some nominal value. So, you know, it can change and maybe we might experiment with that. But anyway, I've just got like a 10 or 12K in there.

**Dave Jones:** No problem. Just a bypass cap on the input here. They recommend, you know, 100n or something like that. I've got one directly from the last video. I got one directly, 100n, directly soldered onto the little surface mount module.

**Dave Jones:** Plus, for good measure, I've got another, I think, 47n outside of that on the breadboard. Oh, by the way, input supply here, we're probably going to need like 4 or 5 volts or something like that.

**Dave Jones:** Our output voltage is 1.25 volts, but we've got to have our gate sufficient gate drive voltage as well for our N-channel FET over here. I I haven't looked at the data sheet for this 3055.

**Dave Jones:** I don't actually remember, but yeah, 4 or 5 volts should be good enough. So, I'll set it to 5. Oh, also, an important thing is that the ground reference for this entire circuit, I'm taking off the sense tap for that resistor there.

**Dave Jones:** So, there is no error because we're trying to generate a very precise 1.25 volts across this point. And so, you know, basically, the sense output, the force line drives the voltage for that, but the sense line here and there and there, that's our internal voltage reference.

**Dave Jones:** It's going to produce or going to try and produce 1.25 volts precisely across those two points. So, you want them directly across your sense line there. You don't want to make a mistake of connecting this ground through to here like this.

**Dave Jones:** You want this actually returning, if your input is like this and there's a ground there, you want actually your return current bypassing all of your all of your precision voltage reference circuit in here and going back to your supply like that.

**Dave Jones:** So, you've got two current loops there. One is the huge 1 amp current loop going around like that and the other is just a separate ground in there for the sense resistor.

**Dave Jones:** And this, you know, chip is only going to draw a couple of milliamps, but you definitely want that. Very important. That's why we're using a four terminal resistor. If you don't have a four terminal resistor, then you want to do a proper Kelvin connection right on the point.

**Dave Jones:** And there is our circuit built up there and this op amp isn't used here. That was just from some experience from last time. We might need that again. We'll see.

**Dave Jones:** There's our precision voltage reference on there. As I said, bypass cap, bypass cap on the input. The ground, you'll notice that the ground is reference is separate and actually goes back to the sense terminal over there.

**Dave Jones:** Oh, there's my 1.25 ohm four terminal precision resistor. There's our N-channel MOSFET up here. This will be my current source going from the drain of that thing up to the top there.

**Dave Jones:** There's my 10 micro Farad output cap there. So, let's hook this thing up and plug that in and I'll just measure the output sense line with the scope here and we'll see what we get.

**Dave Jones:** And here's our power supply. I've got it set to 5 volts here, but of course you want to set the output current limit just so you protect your circuit.

**Dave Jones:** Don't want to blow the ass out of the thing. So, I'll set that to 1.1 amps there. So, it can't go over that. It'll self-limit. By the way, no, I don't have any heat sinks on these devices here.

**Dave Jones:** The four terminal precision resistor is only going to dissipate 1.25 watts maximum and that is within the safe operating range of this thing within just into free air like that, what's called free air.

**Dave Jones:** So, uh without a heat sink. So, that'll be fine. The MOSFET over here, no, it's going to get pretty hot. But, you use Ohm's law, work out how much power's dissipated in that.

**Dave Jones:** But, hey, it'll be good enough for just, you know, probing for, you know, 5 seconds and seeing if the thing oscillates. It's, you know, it's not like we're going to leave it there for, you know, an hour or something like that.

**Dave Jones:** It'll just cook the thing to death. So, here we go. Let's see what we get. Let's switch this on. And my circuit's drawing 4 milliamps there. That's sort of what you'd expect for the quiescent current of the circuit here.

**Dave Jones:** And if I plug in my scope's hooked up, I'm at Yeah, yeah, 200 millivolts per division. That'll do it. Let's plug in our load. Hello. Hello. We're getting our 1.25 volts nominal up there.

**Dave Jones:** But, yeah, it looks like we're getting some oscillation. And if we AC couple that, it looks like Yeah, that's that's pretty horrible. We're getting about 50 millivolts peak-to-peak oscillation on this thing.

**Dave Jones:** That's That's pretty awful. Let's see if we can see if we can trigger off that and see what we're getting. Yeah. Look at that. Awful. Similar to what we're getting last time.

**Dave Jones:** So, hey, but, you know, we're getting there. And I reckon we can stabilize this sucker. We should be able to. So, what I'm going to do now is actually hook up the uh hook up my uh ammeter here.

**Dave Jones:** And let's see what value we get because, you know, it should We should get There we go. We're getting near our amp. But, of course, here we go. It's changed.

**Dave Jones:** Look at that. Our waveform there has changed because we've got some extra inductance in this lead. We only had a little jumper lead before. So, there you go. That's kind of expected um that you wouldn't get precisely the wave in the same waveform.

**Dave Jones:** Let me show you that. Let's put that back in. And I'll show you that that's There we go. Yeah, completely different. There you go. When you add the short because you got the inductance of these leads in here.

**Dave Jones:** So, that is changing the whole uh oscillation frequency of that thing due to, you know, the inductance of this, the ESR of the output caps, and the loop stability, and the poles, and the whole, you know, the whole shebang in there.

**Dave Jones:** And just to show you that, let's That's what we're getting, okay, with the uh huge leads on here. Let's remove the input capacitance. You know how I said I've got the two input caps there?

**Dave Jones:** Well, let's physically take out one of them. I still got one there directly on the input of the chip, but we should expect a little change, and we do get it.

**Dave Jones:** Look at that. We're getting some more high frequency parasitic happening there. That's really, yeah. That's Look at that. So, if we whack our cap back in, and bingo, we're back.

**Dave Jones:** Back from the future. But, if you think you're going to solve this problem by, you know, tweaking your input capacitance on this on over here, then you're completely wrong.

**Dave Jones:** You're in the wrong ballpark because the loop stability of this thing is ultimately uh determined by the phase margin of the um output op amp in there for this voltage reference.

**Dave Jones:** And the as I said, the output um capacitor here, the 10 microfarads with the uh a a it usually specifies in data sheet. It does in this case of it's got to be less than 0.1 ohms.

**Dave Jones:** But, it's not just the ESR of the output, it's actually the output capacitance as well. So, this is where we need to solve our problem. And when you get oscillation on a voltage reference or a regulator like this, usually you're not going to have enough uh capacitance on the output to ensure loop stability in your voltage reference here.

**Dave Jones:** Let's increase the value of that output cap, and I think we're probably Well, hopefully we will solve our issue. That's the uh That's the plan anyway. So, let's whack on a big ass, not a huge value resistor, but a big ass 22 microfarad uh 400 V electrolytic on here and see if that makes a difference.

**Dave Jones:** I'm not going up in value yet, but I'm adding another I'm still leaving in the 10 microfarad uh ceramic cap which we're got in there, but adding another 22 mic in there in parallel.

**Dave Jones:** So, let's uh And yeah, that's on. All right. Let's switch this back on. No, that hasn't solved it, but it's changed it. Look at that. We're on our way.

**Dave Jones:** So, let's go up in capacitance, shall we? 470 microfarad electro, 10 V. So, let's give that a whirl. And there we go. And I'll plug this in live here.

**Dave Jones:** See what we get. Oh, hello. Hello. Oh, 1.2 1.0027. Look at that. We're AC coupled here on on the noise, by the way. So, that's that's 5 mV per division.

**Dave Jones:** Beautiful. We're getting our precision current source near enough to 1 amp. Ah, beauty. What a Bobby dazzler. So, we're down at 5 mV per division here, and if you're curious about that noise, I've got the thing actually switched off now.

**Dave Jones:** All right, our circuit is switched off, and we're still picking up this crap. Okay? So, woo, hello. Look, just putting my hand there is enough to um pick up the interference from the screen here and near my circuit and couple that in.

**Dave Jones:** There's all sorts of AC coupling stuff happening here. So, that is not actually the residual noise of this circuit and we won't go into actually measuring the noise of this thing.

**Dave Jones:** That's why if I switch it on and because this is actually a pretty low noise reference, right? So, the noise isn't actually oscillation of the thing. Here we go.

**Dave Jones:** Let's switch it back on and get our There we go. Noise is exactly the same because we're not using proper low noise measurement techniques here. This noise is a furphy.

**Dave Jones:** It's a red herring. So, you know, don't think that is your output oscillating or being noise or anything like that. No, that's not necessarily so. But anyway, all we're here for today is to stop the oscillation and we have.

**Dave Jones:** We have ourselves a stable precision 1 amp current source. Or do we? Now, as I said before, I gave you a little quiz at the start. This is actually expected.

**Dave Jones:** The exact value we're getting here, please don't let me scream at me if I'm leaving this on too long cuz that FET's going to heat up. Anyway, if I talk too long, which I always do.

**Dave Jones:** The output is pretty close to 1 amp there. Look at that and you might think that's bang on, but do the math there. That's 0.27% and you remember this thing should be 0.02.

**Dave Jones:** It should be an order of magnitude better than that. So, that should be 1.00027 or something like that. And it's not to do with the layout of my circuit cuz I'm pretty confident that is right cuz we've used the proper four-terminal Kelvin resistance.

**Dave Jones:** So, we've got an extra 2.7 milliamps in there. Why? Now, this of course is where you have to read the data sheet. And if you're reading it carefully or if you've seen the forum before where where we've actually discussed this after the uh uh previous video, then you'll notice that pin six VoutS, right?

**Dave Jones:** That sense line coming back in, you might think, "Well, it's not going to take any current at all, right? It's going to be the input to the op-amp, but it's not."

**Dave Jones:** And look, we've got two internal resistors in here. There is going to be some current flowing into this pin. And if you read up here, what does it tell you?

**Dave Jones:** Uh this pin sinks 2 milliamps. The output error is uh is the resistance of the PCB trace, so that could matter. And it talks about this in the data sheet.

**Dave Jones:** I recommend you read it. Times that 2 milliamps regardless of the load current. Aha, 2 milliamps. Bingo. What do Oh, I I left this on. Oops, should be smoking now.

**Dave Jones:** Uh it's dissipating for a 5 W heat in that poor little sucker. That's where our 2 milliamp errors coming from. Got you. Hoho, poor little sucker. So, what we've got happening here is here's our load up here.

**Dave Jones:** Here's our ammeter. We've got a precise Yes, we do have a precise 1.25 V across our precision 1.25 ohm resistor. Yes, so we are getting precisely 1 amp flowing through here like this, down through the resistor and out the bottom, but we've got a 2 milliamp error current coming down here and going Oh, thank you.

**Dave Jones:** I need to go in there, down to ground. So, we've got a precision Even though we've got that precise voltage across there, our resistor, we think, "Oh, yeah, we definitely have to generate our 1 amp through there.

**Dave Jones:** That's Ohm's law." Aha, we forgot about this sneaky little current path going down there, little bastard. And that's where our 2 milliamp errors coming from. In this case, it's only .2% So, it's not much, but hey, we're trying to design a precision current source here at .02% order of magnitude better, 10 times better than that.

**Dave Jones:** So, that 2 milliamps is killing us. So, what we need to do is actually put an op-amp buffer in here like this, positive, negative. So, then of course there's no current flowing into that op-amp because it's a high impedance input, so the error is going to be negligible, not even half a bee's dick, and all of the current, of course this is powered from plus V up here, so all

**Dave Jones:** the current is coming from this terminal up here, that extra 2 milliamps is sourced from up here instead of through our load over here. So, therefore, if we add in that buffer, which may affect the loop stability of this thing, of course, so hey, we could be back to square one with our loop stability.

**Dave Jones:** We might have to compensate, but anyway, that is the way that we're going to fix that. But, of course, if you're astute, you would have realized that look, we've still got our 10 microfarad uh In fact, our 470, sorry.

**Dave Jones:** What did we use, like a 470 microfarad in there to make it stable on the output of this op-amp now. And hey, op-amps do not like having a large capacitance on the output.

**Dave Jones:** So, that thing could oscillate on its own. So, we're going to move that cap back over to the input here, and uh so, I'll put that 470 mic back on the input there, and there'll be nothing on the output of this op-amp, and we'll just be driving that sense line directly.

**Dave Jones:** Let's see what we get. All right, let's switch this sucker on, and hook it in. I got my 470 mic on there. I hope it's all right. I've got my op-amp in there, it's powered, and fingers crossed.

**Dave Jones:** Hello. Look, no whoop no noise, and look, we're down to point 1.0006, so we're uh now point 0 6% accurate. Awesome. So you remember we were getting 1.0027 before and the data sheet said well it was a nominal 2 milliamps into that pin.

**Dave Jones:** Well we've eliminated that 2 milliamps. It's vanished and now we're just getting that point 7. We're getting like point 7 before. Well point double 0 point triple 0 7 before in terms of offset if we didn't account for the 2 milliamps.

**Dave Jones:** Take out the 2 milliamps. There we go. Bang. I'm curious to know what happens if we remove our 470 mic cap now. Let's see if it goes back to being No.

**Dave Jones:** There we go. It's still stable. We've got a bit more noise but uh not a problem at all. So this thing is now stable without that um output capacitance there cuz we've entirely changed the uh loop parameters of this uh circuit.

**Dave Jones:** The poles and everything else it's the whole thing has completely changed by adding the op amp buffer in that feedback loop. Oh hello. I just put in a 10 microfarad ceramic.

**Dave Jones:** I was just going to boast that uh putting in this uh putting in this op amp has ironically made this thing more stable but look at that. That's horrible.

**Dave Jones:** That's five that's uh 10 millivolts uh per division there. So that's that uh little 10 microfarad ceramic. It doesn't like that at all. But if I put in that uh well it it works without it um or with the uh 470 but looks like that that 10 microfarad is in the sweet spot which makes a little bit of oscillation within the loop we've got here.

**Dave Jones:** So that's why uh this kind of circuit you can make stable for one precise load you've got and and well and that's what I'm going to use this for is a precision one amp current generator and that's fine.

**Dave Jones:** But if you're using this to power all sorts of different loads at different currents, then well, you could come a gutser. So, just be careful that getting loop stability in all sorts of circuits like this is not easy and uh really unless you've got the exact uh simulation model of that uh reference chip turn that off.

**Dave Jones:** It's getting a bit hot. Um then you uh you know, you really have to build this thing up and you know, try it on your actual load to make sure it works.

**Dave Jones:** And that's what we get if we put in a 100 nF. Look at that. 100 nF by the way, I'm putting these caps directly across the uh sense line of the input of the op amp there.

**Dave Jones:** So, there you go. That's uh 50 mV per division. That's that 100 amp. Pretty horrible. So, it looks like we still do need that high value value cap across here to make this thing stable.

**Dave Jones:** Not surprising. And you know how I said this uh gate series resistance in here is going to matter at the moment I've got a 12K resistor in there just to uh slow the thing down because we're going to get some gate capacitance here and we can cause the thing to oscillate that way.

**Dave Jones:** So, what I've got now, okay, let's So, let's actually short that out. There's our output. Okay, it's stable. I've actually got no capacitance here at the moment, but you can see with the 12K resistor in there, it's nice and stable.

**Dave Jones:** Now, what I'll do is I'll short out that. There we go. I short it out that 12K resistor. Haha! Look at that. So, we've got some pretty darn awful 500 mV per division noise there.

**Dave Jones:** So, let's with that shorted out resistor, let's see See we can uh even our 470 mic cap across our sense resistor there can't you know can't settle that oscillation down.

**Dave Jones:** We really have to remove that we really have to include that 10k in there. So the other thing to note about this is that this thing really doesn't change much even though these devices are heating up.

**Dave Jones:** I mean they're you know way too hot to touch. The effects probably up at 100° 80 or 100° or something now and you know the I don't know the four terminal precision shunt resistor you know might be at 60° or something.

**Dave Jones:** I don't know. I haven't put a thermometer on there but getting it pretty warm. So um but look I mean it's pretty ultra stable. That's because this if you go have a look at the data sheet for this precision resistor it's tempco is bugger all.

**Dave Jones:** These things practically have no drift at all like two ppm per degree C. Oh and if you're wondering what op amp I used in there yes it does actually matter.

**Dave Jones:** I've used a really precision trimmed op amp the OPA 376 VOS offset voltage of five microvolts typical which translates to our with our 1.25 volts here of point triple 04% error.

**Dave Jones:** So it's adding bugger all error into our circuit here and that's what you want. And I just tried another four terminal resistor in here because we were I was still getting you know point double 06% which is higher than we'd like.

**Dave Jones:** So higher than what we really expect. So I tried a different one and there you go it hasn't changed by a huge amount as you'd expect because these are point 02% precision resistors or better and I'm sure they're actually better.

**Dave Jones:** That's sort of worst case. These things you know never hit their worst case. So I can only presume that extra error that we're getting in there because we expect better than that, um, is due to the contact resistance on my breadboard in here.

**Dave Jones:** So, this is not ideal. Either that or my voltage reference is out of tolerance. So, what I've done is I've soldered up another chip. This is the old one with the dodgy, uh, pins that I had to, uh, bend inwards to make it, uh, fit.

**Dave Jones:** Anyway, I've soldered on a, uh, brand new, uh, LTC, uh, 6605 and let's have a look at what we get. Bingo! That is, uh, half, I think, roughly half of what we're getting before.

**Dave Jones:** So, we're now .03% and technically, that's within side our error budget, because our, um, cuz the voltage reference is at .025%, I believe, uh, nominal in itself. And then we've got the, uh, precision current shunt of, uh, .02%.

**Dave Jones:** So, yeah, there you go, within our error budget. So, maybe, I don't know, maybe this little puppy has had a bit too much abuse from all the, uh, experimenting that we've got there, but I'm I'm pretty happy with that.

**Dave Jones:** It's, uh, more than good enough for my, um, application here. So, there you have it. There's our precision 1 amp current source, and we got it stable, and we got it to work on a breadboard.

**Dave Jones:** Brilliant! That's what we want. Even, uh, within our, uh, error budget of our two main parts here, which is our voltage reference and our, uh, precision resistor here. So, I think I might, uh, do a custom little, uh, board for this.

**Dave Jones:** I'm not sure I had exactly the final, uh, form factor it's going to be built in. Little box, it's going to be powered from batteries, it's going to be powered from like four, uh, D cell batteries.

**Dave Jones:** I didn't, uh, test the input, uh, voltage range there. The voltage range can perhaps, uh, go, uh, down a bit, I'm not sure. I'll probably add a like a little low battery indicator or something like that.

**Dave Jones:** But this is going to work a treat, and of course that fit there needs a heat sink. Um technically, this resistor here uh precision resistor doesn't need a heat sink, but I would put a small heat sink on that as a matter of course.

**Dave Jones:** And uh this one, yeah, I got to test it over uh you know over continuous load and all that sort of jazz, but jeez, pretty darn happy. And if you're curious to know what the uh switch-on performance of this uh current source is with the uh 470-microfarad cap across there, so let's uh give it a go.

**Dave Jones:** Little dodgy uh alligator clip here. So, up, yeah, there's our contact bounce. There we go. I That's That's pretty dodgy. Let me try that again. So, yeah, there's a switch-off, and let's see if I'm going to get a clean switch-on.

**Dave Jones:** There we go, that's pretty clean. That little bit of noise in there is just from my uh contact bounce there, but that turns on pretty nicely, but you're only going to get that nice uh turn-on with a uh large-value cap in there.

**Dave Jones:** If you've got, you know, a smaller value or no value at all, as we found it was still stable with no value cap in there, um then well, your transient performance isn't going to be smooth like that.

**Dave Jones:** It's probably going to overshoot. In fact, I can probably give that a go. Here we go. So, I've taken the cap out, and woah, there we go. Now, let me try that again.

**Dave Jones:** It's hard to capture. I need a proper switch. There we go, got it. There we go. Got a massive amount of overshoot there. So, our 470-mic helps with that.

**Dave Jones:** So, it's a fairly clean switch-on with that 470-mic value. So, there you go. I hope you enjoyed that video of this uh precision 1-amp current source. And yeah, it's good enough for my application where we're getting, you know, 0.03% here on the breadboard.

**Dave Jones:** Not a problem. Its uh switch-on performance seems quite stable. So, I'm pretty happy with that. More than good enough for my application. So, I'm going to build this sucker up and use it.

**Dave Jones:** And if you want to have a play around with it, by all means do yourself. So, thank you very much Yuval at Vishay for getting me that precision 1.25 ohm current shunt resistor.

**Dave Jones:** Awesome. Got a link in the data sheet for that thing down below. I do recommend you take a look. Vishay make some awesome resistors and they actually sent me some other goodness as well, which we might take a look at one day.

**Dave Jones:** Very, very nice. Top of the range precision resistors. Mm. Resistor porn. Love it. Catch you next time.
