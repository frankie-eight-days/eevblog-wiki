---
video_id: TxBJb-Z0XFI
title: EEVblog #479 - Opamp Input Bias Current
url: https://www.youtube.com/watch?v=TxBJb-Z0XFI
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 28, "3": 38, "4": 56, "5": 70, "6": 85, "7": 95, "8": 107, "9": 127, "10": 138, "11": 153, "12": 162, "13": 177, "14": 189, "15": 200, "16": 210, "17": 228, "18": 253, "19": 266, "20": 277, "21": 293, "22": 306, "23": 327, "24": 347, "25": 361, "26": 382, "27": 398, "28": 414, "29": 428, "30": 444, "31": 460, "32": 471, "33": 483, "34": 500, "35": 512, "36": 519, "37": 546, "38": 557, "39": 585, "40": 597, "41": 608, "42": 624, "43": 632, "44": 655, "45": 661, "46": 675, "47": 693, "48": 705, "49": 722, "50": 738, "51": 750, "52": 768, "53": 779, "54": 792, "55": 804, "56": 815, "57": 839, "58": 854, "59": 865, "60": 890, "61": 902, "62": 915, "63": 933, "64": 954, "65": 982, "66": 1002, "67": 1016, "68": 1030, "69": 1038, "70": 1053, "71": 1064, "72": 1087, "73": 1099, "74": 1113, "75": 1132, "76": 1161, "77": 1179, "78": 1196, "79": 1206, "80": 1216, "81": 1235, "82": 1248, "83": 1255, "84": 1267, "85": 1283, "86": 1296, "87": 1313, "88": 1321, "89": 1329, "90": 1338, "91": 1364, "92": 1378, "93": 1407, "94": 1419, "95": 1431, "96": 1444, "97": 1457, "98": 1468, "99": 1480, "100": 1492, "101": 1510, "102": 1522, "103": 1539, "104": 1546, "105": 1560, "106": 1571, "107": 1582, "108": 1602, "109": 1612, "110": 1622, "111": 1639, "112": 1652, "113": 1671, "114": 1680, "115": 1693, "116": 1708, "117": 1720, "118": 1739, "119": 1759, "120": 1778, "121": 1787, "122": 1796, "123": 1812, "124": 1826, "125": 1844, "126": 1864, "127": 1875, "128": 1893, "129": 1905, "130": 1915, "131": 1932, "132": 1944, "133": 1957, "134": 1981, "135": 1999, "136": 2013, "137": 2023, "138": 2038}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. This is a follow-up video from my previous one about measuring input offset voltage and some issues I had with an analog devices part. If you haven't seen it, click down below and you'll be able to watch that.

**Dave Jones:** It's a 30-minute video of me marking around measuring some input offset voltages. Great fun. But today, we're going to do something related which we'll get back to on the breadboard and solve our problem from last time.

**Dave Jones:** We've got op-amp input bias currents today. What is an op-amp input bias current and why is it important? Well, let's take a look at it. You've got your basic op-amp here.

**Dave Jones:** Doesn't matter what op-amp it is, they're all going to have what's called an input bias current. Now, uh you're used to dealing with an ideal op-amp. Now, an ideal op-amp, of course, one of the rules for the ideal op-amp is that no current flows into the input pins.

**Dave Jones:** But of course, in practice, that's complete because you're going to have some current flowing into or out of, we'll get into that, these input pins on this op-amp. And that's called the input bias current.

**Dave Jones:** And I've labeled that here IB+ and IB-. Now, a data sheet for a typical op-amp will only usually only show the input bias current as one figure, IB, they'll typically call it.

**Dave Jones:** They won't actually specify different input bias currents for the positive and negative. And that's where we'll get into later is the input There's There's two parameters to do with input bias current.

**Dave Jones:** One is the input bias current itself, IB. The other is IOS, which is the input offset current. And that is actually the difference between these two. But we'll get into that in a minute.

**Dave Jones:** Now, this input current in practice can range anywhere from femtoamps, a really schmick precision instrumentation grade op-amp might have, you know, a few tens of femtoamps input current. Or for a really fast wideband with op amp, they don't care about the input current.

**Dave Jones:** So, it's going to be a couple of microamps. They're going to optimize the internal architecture for that op amp. They don't care about the input bias current. They're going to optimize that for bandwidth and slew rate and all sorts of other things.

**Dave Jones:** So, there's a pretty big range there in the input bias current. So, how does that work? Well, let's take a look at the input circuitry or the basic topology of the input circuitry for a bipolar operational amplifier.

**Dave Jones:** So, this is not a FET input. It's a bipolar input op amp. And you'll notice that we have two input transistors here, both NPN going into a current source.

**Dave Jones:** It's a current mirror configuration and I won't go into all the details of, well, any significant detail of input op amp architecture. That requires a whole separate video, but suffice it to say, look, these inputs are connected directly to the base of these transistors here.

**Dave Jones:** and negative input on your op amp over here goes into these transistors. So, naturally, you're going to get some base current flowing in there and in there as well.

**Dave Jones:** And there's ways to lower that, of course. If you use a FET input op amp, well, FETs aren't effectively, right? They're a field effect transistor, no input current. But in practice, there is.

**Dave Jones:** In theory, there's not in practice. But this is a bipolar operational amplifier. You'll do it probably the most common one on the market, although FET ones are pretty darn common as well, CMOS ones.

**Dave Jones:** And there's other ways to lower this input bias current as well. They can actually use a Darlington configuration here so that your input bias current is lower. It's still using the bipolar manufacturing process, but there's issues with that in terms of bandwidth and all sorts of things, which I won't go into.

**Dave Jones:** And the other way to do it is what's called a biased bias offset operational amplifier or a bias offset input. And what they do is they actually put in here a current source in there and in here as well so that that biases the transistor instead of the input bias current.

**Dave Jones:** So, in theory, it cancels it out and you can get very low input bias currents from the input but not zero. They almost never Well, in practice, you can never get down to zero bias current.

**Dave Jones:** So, every practical op-amp, it regardless even if it's input bias compensated, is going to have some form of input bias current or IB. And it'll be mentioned in the data sheet.

**Dave Jones:** Now, these bias currents, they can be a real pain in the ass in precision applications. And there's quite a few uh different ways it can screw you up. Let's take a look at the first problem is the your uh source impedance of uh well, your source impedance.

**Dave Jones:** Okay? That's a series resistance of your source. Let's say it's 10K. Might be a typical value for um some systems. And if our input bias current is a very low 100 picoamps, right?

**Dave Jones:** That's a pretty good op-amp, very low input bias current at 100 picoamps, okay? Then our error that we're going to introduce in our system without ignoring everything else, offset errors and all the rest, is going to be 10K times that 100 picoamps because that 100 uh picoamps is flowing through that 10K resistor.

**Dave Jones:** We've got a 1 microvolt offset already, a 1 microvolt error. And well, it doesn't sound like much, does it? 1 microvolt. But if you're dealing with a precision system, then that can like a you know, a strain gauge or something else you're dealing with, that can be a real big deal cuz that these errors get multiplied by the gain of your op amp.

**Dave Jones:** So, it can screw you up right there. Just be careful. And 100 pA, that's a very low one. So, imagine if your source impedance is like a meg or something like that, and your uh uh bias current's even higher, you can get millivolts of error.

**Dave Jones:** Watch out. Now, the second problem we've got is errors introduced into our uh gain network and our feedback resistor network for this thing. Now, what happens? Let's take this uh inverting op amp configuration, and here's our input voltage, that's our output, of course, and let's ground this input here, and see what happens.

**Dave Jones:** Now, because the input, the uh non-inverting input down here is also grounded, and once again, we go back to our ideal op amp properties, we're assuming our input offset voltage, remember we're not talking about offset voltage yet, is zero.

**Dave Jones:** So, the difference between here and here is going to be zero. Remember, due to op amp action, the op amp does whatever it needs on the output to ensure that the two inputs are exactly the same voltage, if your input offset voltage is zero, which we'll assume.

**Dave Jones:** So, this point here is also 0 V. It's also grounded. So, there's no current flowing through R1 there at all. So, but we still have an input bias current.

**Dave Jones:** Remember, we always have that. It can't get away in this practical configuration. So, where does it come from? Well, it can't come from through this resistor here, because Ohm's law says 0 V across that resistor, doesn't matter what value it is, this R1, no current flows through it.

**Dave Jones:** So, all of the current must come from RF here. In this case, it flows around like that. So, all of our input bias current is flowing through RF, and you might see the problem already.

**Dave Jones:** Usually, to you want on an op amp, you're going to have some sort of gain, times 5, 10, 50, 100, even 1,000, depending on your um uh you know, your uh circuit application.

**Dave Jones:** Well, that means RF has your feedback resistor has to be a large value. What do you get when you have a large value resistor with a current flowing through it, IB, even a very small one?

**Dave Jones:** Aha, you're going to get an offset error introduced over and above your VOS. Your which is another figure on the data sheet, your uh input offset voltage. This is in addition to whatever that is.

**Dave Jones:** So, this is where input bias current can be a real pain in the ass for these precision applications. All that bias current flows through RF. So, how do we solve these input bias current issues?

**Dave Jones:** They're a pain in the ass for these precision applications. How do we get rid of it? How do we cancel them out? Well, let's uh have a look at what we've got here.

**Dave Jones:** IB+ and IB- one goes into the uh inverting input, one goes to the non-inverting input. So, they're essentially opposite currents. So, you can actually cancel them out. Now, let's go back to our original non-inverting configuration here, and we've got a simple voltage follower, okay, with our source impedance RS in here, whatever value it is, causing the error due to the input bias current flowing through it.

**Dave Jones:** Well, we know that the other input has an equal and opposite, or should have an equal and opposite input bias current. How do we cancel it out? Very easy.

**Dave Jones:** We just put another a feedback resistor in there, equal to let's call it RS2, equal to the value of RS. So, if IB+ and IB- are equal values, except opposite, cuz they're going into opposing inputs of the op-amp, I won't go into the internal details of it, but then you can cancel them out by having a a resistor in the feedback loop like that.

**Dave Jones:** And how do we solve this inverting op-amp configuration here? Well, essentially, exactly the same thing. Instead of this going to ground down here, we have a resistor in there going to ground.

**Dave Jones:** So, we're going to get our input bias current, and we can actually cancel them out like that. Now, let's call this R B, and what value should R B be?

**Dave Jones:** Well, it's a standard formula. It's actually R F in parallel with R 1. Now, I won't go into how you actually derive that. It's not actually that hard if you want to go into the details, but I won't waste the time doing that.

**Dave Jones:** But, that is a basic formula, and this is a very common thing that you'll see in a lot of circuits. You might have wondered why, well, why does it have this resistor in here?

**Dave Jones:** Is it protecting the input somehow? No, you know, it's to do with the input bias currents in these precision circuits. And of course, if you've got a very large gain here, and R F is much greater than R 1, then you can just say R B equals R 1 because the parallel combination of R F on top of that, to a rule of thumb, you know, to an order, if

**Dave Jones:** you've basically got a gain of 10 or more, and R F is 10 times R 1, you can generally say R B equals R 1, near enough. So, that was too easy, right?

**Dave Jones:** We fixed our input bias current. No big deal, just whacking a resistor in there, and you're right. Unfortunately, what? It doesn't work like that in practice because the input bias currents are not matched.

**Dave Jones:** These transistors are never a matched pair. You're never going to get precisely the same value. There's some op-amps that get really, really close, but in practice, it's not going to be zero, just like the input bias current itself, regardless of the topology used, is not going to be zero, either.

**Dave Jones:** And that's where this IOS comes in. The input offset current is the difference between IB plus and IB minus. So, there's actually two parameters there that you have to look at.

**Dave Jones:** Not not only the input bias current itself. Like, the input bias current could be really low. It might be 10 picoamps, for example. But then, if your IOS is 100 picoamps, for example, then well, jeez, that's all over the shop.

**Dave Jones:** There's no way that you can choose a resistor bias value that's going to work. You might fluke it. You might be able to tweak it for an individual chip or an individual circuit, but just as choosing a generic value to do it, no, you're not going to be able to do it.

**Dave Jones:** Unfortunately, it is just a problem with these op-amps. If you're really If you're doing ultra-precision applications, yeah, you'll have to trim these things to take into account the input bias currents.

**Dave Jones:** And on top of that, then we've got our voltage offset, as well. So, you could get to a point, depending on your particular op-amp you've chosen, that IOS could actually swamp your effective IB, or vice versa, or there's a combination of the two, and it can get really ugly.

**Dave Jones:** But on top of that, you wouldn't know what's even worse? Well, you might have a rail-to-rail op-amp. Now, I mentioned right back at the start, I think, that the input bias current can go either direction.

**Dave Jones:** Now, on a standard bipolar op-amp, like this, or on a FET input op-amp, for example, you're typically going to only going to get your input bias current going one way.

**Dave Jones:** But on rail-to-rail op-amps, they're internally biased, and they've got different configurations, and I won't go into the transistor configuration of an of a rail-to-rail input op-amp, because there's lots of tricks.

**Dave Jones:** They can actually vary in and like that. but basically, it means that current can also flow out of these pins as well, depending on the common mode voltage operating at.

**Dave Jones:** So, if this is zero, for example, you might have a curve like that where your current can be bias current can be positive and negative. So, this can be IB here, positive and negative, and at some transition point where you pass through it, you might end up going in the current may flow out of these pins back out and ruin your day.

**Dave Jones:** It can get really ugly. So, there's all sorts of problems. You got IB, you got IOS, you got V offset, you've got whether or not your input configuration, your topology, your circuit, and all sorts of stuff.

**Dave Jones:** Ah, is there an easy solution? No, afraid not. So, in practice, this can be a really big issue, even for circuits that you might not think are that critical.

**Dave Jones:** So, you got to keep an open mind, watch out for it just in case you get caught. I mean, depending on whether what our supply this can change with supply voltage as well, the common mode here, which is that's V common mode here, depending on what input configuration, whether or not you've got an input bias compensated or rail-to-rail op amp, the supply voltage, all sorts of stuff, and

**Dave Jones:** which configuration you're using, your source impedance. Ah, and we haven't even mentioned temperature. So, how do you know if your op amp has one of these input bias compensated values?

**Dave Jones:** Well, you're typically going to get a plus minus IB value like that. They're usually not going to give it for your input offset, but plus minus IB, that's a dead giveaway that the op amp you're using, even though they may not tell you, is input bias compensated.

**Dave Jones:** So, you can see how complicated this is already getting. And really, you know, we're not even throwing vos into the mix much the input offset voltage which the gain is going to get multiplied which is going to get multiplied by the gain of your op amp here and it can get really really nasty.

**Dave Jones:** So if you see any input offset issues they will typically be a combination of the real input offset voltage which is a separate parameter vos entirely separate parameter on your data sheet up here but it can also include your input bias currents and that's what we saw in the previous video.

**Dave Jones:** If you haven't seen it link it down below. So let's now go back to the breadboard from that previous video and see if we can reduce or eliminate or compensate for these input bias currents and see how it affects our final output offset error and just a quick background to our previous video and you really should watch the previous video it'll be linked down below if you haven't seen this

**Dave Jones:** otherwise it may be a little bit confusing for you but basically we had a analog devices ad 8628 op amp with times 100 gain in the non-inverting configuration and it and we were getting an output voltage which was higher than just the expected offset voltage here.

**Dave Jones:** Now here's the actual circuit we got we got 1k going to ground here we got a 100k here total gain of 101 we're going to call it 100 near enough and the input offset voltage of this particular op amp is supposed to be around about one microvolt.

**Dave Jones:** So we only expect sort of around about 100 microvolts on the output here but this is our output voltage and we're getting over 300 microvolts here and this is our supply voltage we're using a split supply here.

**Dave Jones:** So the ground point is actually in the middle so it's plus minus two and a half volts but our output voltage is higher than what we expect from just a typical device.

**Dave Jones:** And technically, yes, it is within spec because the here it is input offset voltage VOS there at 5 V supply is a typical value of 1 microvolt, but it could be as high as 5 microvolts.

**Dave Jones:** So that would translate to 500 microvolts on the output here. But as I said in the previous video, it that's not actually the case. This op amp is actually typically 1 microvolt or less.

**Dave Jones:** And I've tried multiple op amps and the and that error is coming from somewhere else. Well, guess where? Input bias currents. And if we have a look at our data sheet here, you'll notice that as I explained before, well, there's a figure for IB there, input bias current, and input offset current right here.

**Dave Jones:** Here it is. The AD 8628. It's going to It actually gets higher with the quad package, by the way. That's just to do with the uh process technology that they're actually uh using.

**Dave Jones:** They've got four of those on the one die, and it's different. So anyway, we've got the single one, the 8628. Input bias current, typically 30 pA. It could be as high as 100 pA there, but you know, it we are going to get the typical uh figure down in here.

**Dave Jones:** So aha, 30 pA. Let's have a look. Is it a coincidence that our output is just over 300 uh microvolts here? Let's do the math, shall we? 30 if IB here, let's ignore this input here.

**Dave Jones:** Okay, let's ignore the non-inverting input. Let's just look at the inverting input here. If our input bias current, let's assume it's going into the pin, then uh if it's 30 pA going in, you remember before, if we ignore the V offset, then there's no voltage drop across this resistor, so all the input bias current, that whole 30 picoamps, av- you know, typical, is coming through that 100 K

**Dave Jones:** resistor. Aha. So, let's do the math here. 30 picoamps, there it is, times 100 K equals 3 microvolts. So, we're getting 3 microvolts error just due to the current going in there, the input bias current into that inverting input there.

**Dave Jones:** But, the gain of the op-amp, of course, is 100. So, we have to multiply that by 100, and of course, you get 300 microvolts. Aha. Look, 300 microvolts or just over.

**Dave Jones:** Is that a coincidence? I think not. Well, it's not going to be the entire story, but it is certainly going to be a lot of the reason for this.

**Dave Jones:** And by the way, um if you haven't seen the previous video, this does change with supply voltage. So, if we drop the supply voltage down, you can actually see it change significantly, and even go negative like that.

**Dave Jones:** You remember what we were talking about with that Oops, sorry. It should only go to 2.7. There we go. 2.7, it's almost going negative there. So, that does change with supply voltage, as I mentioned previously in the video earlier.

**Dave Jones:** Now, of course, that's not going to be the only reason, but it's going to have a significant effect on that. Of course, our V offset is going to come into it, and V offset's going to get multiplied by the gain of 100 as well.

**Dave Jones:** And then, we haven't taken into account the input offset on the other pin and stuff like that, but there you go. That is going to be a very significant reason for it.

**Dave Jones:** So, the previous video, yes. I mean, I've done this stuff before, but it's actually been, you know, I don't know, 7 years or something we since I last touched this sort of stuff.

**Dave Jones:** So, I forgot that the error term is going to be coming through the 100k resistor here, and it didn't help that the Analog Devices data sheet actually shows these these exact same values in a typical example test circuit.

**Dave Jones:** So, what You know, I just overlooked it. That can easily happen to even somebody who's done this stuff before, and I made the assumption that it was only going through the 1k, which is incorrect.

**Dave Jones:** All of that bias current is going through there. That's why I I knew that I could have put an additional bias resistor in here like this, but then I knew You know, I I did sort of did the math in my head as I was going along, and I went, "Oh, it couldn't make an effect.

**Dave Jones:** I could make that one 1k, of course, as we've talked about. It should be 100k in parallel with 1k, but you know, it's going to be pretty close to 1k.

**Dave Jones:** So, we can put that in there, but I think you'll find if we do that, and we will do it in a second, that it will change this value.

**Dave Jones:** This value will actually change. Now, let's actually get a average of that, shall we? There we go. It's pretty close. Let's call it 300. Spot on to 300 average.

**Dave Jones:** So, what we'll do now is we'll just put a bias resistor in here, and we'll find that it'll likely change. I'd be very surprised if it doesn't, but it's not going to null out to zero cuz we've still got the V offset plus other issues, and then the supply voltage as well, and this is a rail-to-rail op amp as well, and as I mentioned, and all that sort of stuff

**Dave Jones:** uh sort of comes into effect, and we haven't even mentioned ta-da, the elephant in the room, which is the input offset current, IOS. Look at this. A typical value of 50 picoamps.

**Dave Jones:** Look at this. So, it's actually higher than the input bias current. So, even if both inputs are matched precisely, so even if we had VOS equal to zero, which it's not, but let's assume it was, and both these input bias currents were identical, and we put our 1K bias resistor in here, this IOS is still going to screw us up because we have an uncertainty there between the two inputs, IB+ and IB- of

**Dave Jones:** 50 picoamps. So, you just don't know. You don't know what this chip is going to do until you actually build it up and test it. All right, so I've now soldered a 1K resistor in there, bias resistor into the non-inverting input there.

**Dave Jones:** So, we should be able to compensate for that that claimed input typical input bias current. So, let's switch the supply in here, 5 volts, and look, it has actually dropped.

**Dave Jones:** There you go. It's dropped from 300. It's all over the shop. There's a bit of noise on there. Let's get an average of that. There you go. Let's say it's dropped to 180.

**Dave Jones:** I think it's it's changing because it's probably still something still a bit warm there, perhaps from my soldering iron. You've got to be careful of that. That can be a trap for young players when you're measuring critical stuff like this and you've just soldered it.

**Dave Jones:** The chip could be hot, the components could be hot, whatever. Anyway, it's dropped from 300 down to 200. So, that is a change which I I would have been surprised if we didn't get any.

**Dave Jones:** There we go, it's 240. So, it's not quite You know, it's changed by 70 microamps, but it's still as you can see, even with the input bias resistor in there, properly designed, it's still not happening.

**Dave Jones:** So, how can we solve this? Well, of course, we could put a pot in here and actually tweak that out and null it out, but that's not actually a solution for the final circuit I want.

**Dave Jones:** So, what we're going to have to do here is drop these values because as I said, all that bias current IB looks like it probably dominates. I I basically what I want to do is reduce uh I fix this circuit so that the input bias current really doesn't have an effect.

**Dave Jones:** It's dominated by the VOS term there. So, let's change let's lower these by an order of magnitude and we should see let's leave this 1K in Well, no, actually I'll take out the 1K.

**Dave Jones:** Right? I'll take out the 1K. I'll short it back down to ground. Let's lower these by an order of magnitude. So, I'll put 100 ohms and 10K in there and we should find that 300 we got before drops down to you know, in theory it should drop down to 30.

**Dave Jones:** Right? If VOS doesn't come into it, but it could drop down to 100 or something like that. But, we should find that we'll get better than what we're getting here now.

**Dave Jones:** And there you have it. It dropped, but not by a huge amount. You know, we're only talking uh what average you know, 240. It's dropped like 60 microvolts or something like that.

**Dave Jones:** Not a huge amount when we change dropped these by an order of magnitude. But, then again, we don't have that bias resistor in there. So, let me add 100 ohms in there.

**Dave Jones:** And bingo, there you go. With 100 ohm bias resistor in here, that's look we're getting it's a bit noisier. I got a huge resistor on there. It's probably picking up something, but let's get an average on that.

**Dave Jones:** There we go. It's dropped down to an average of like 50 or 60 microvolts. So, we've effectively you know, really gotten down to just what we expect with the V offset voltage there cuz I on a typical chip like this, I expect it to be slightly under 100 1 microvolt.

**Dave Jones:** So, like point which would be this digit here would be one. So, if we had one there, it would equate to a V offset of 1 microvolt cuz of the gain of a hundred.

**Dave Jones:** So, the fact that we're getting around about point seven if in theory we've nulled out both those input bias currents and we're not sure if we have. I mean, that's the thing with this, right?

**Dave Jones:** We don't actually know what we've uh well, we know we've achieved something, right? We've trimmed this thing down so it's better, but we don't actually know what the exact culprit was cuz this is a rail-to-rail um op-amp here, so we don't exactly know the topology.

**Dave Jones:** Add that this is a chopper amp as well, so there's going to be input switching uh current and all sorts of stuff to do with that and this isn't just your regular op-amp, by the way.

**Dave Jones:** It's an input It's I've done a whole video on chopper amps, which I'll link in down below as I did link on on the previous video. So, you know, we've tweaked it by lowering these values and adding in our proper bias resistor and you know, we can probably say now that VOS dominates, but does it?

**Dave Jones:** Uh we don't know because we've only got one sample of this chip. I'd have to do like, you know, ten samples to get sort of meaningful uh data to see as what the exact culprit is.

**Dave Jones:** We don't know uh whether the input bias is flowing in or out of either of those pins, you know, it's just crazy. And well, let's see what happens if we change the supply rail.

**Dave Jones:** Here we go. Oh, sorry. I got to switch off my average mode. It's not a rolling average, it's a average over time there. So, let's start back up at our maximum supply rail of five volts.

**Dave Jones:** Let's say we're getting a hundred. There we go. That's different to what Anyway, it's jumping around a bit. It's a bit noisy, but we drop in and look at that, folks.

**Dave Jones:** It's going negative now. There you go, which is okay. It's to be expected. There you go. Now, we're down at its minimum supply rail of 2.7 volts and we're getting basically a negative uh we've gone all the way from positive up to uh hold.

**Dave Jones:** Hang on, bloody multimeter. There we go. Average. We've gone all the way from positive to negative there because this is a rail-to-rail op-amp. As I said, the topology we've got allows currents to flow either way and in combination with V offset, which also could change over change over the supply rail range.

**Dave Jones:** So, our common mode range is different and our bypass decoupling as well, which we saw made a difference in the previous video. All these things combined make this a little tricky circuit to actually null this thing out completely over the supply range, but I'm pretty happy with that.

**Dave Jones:** By adding the bias resistor in there, we've done a pretty good job. I mean, I don't care if it fluctuates plus minus like that over the supply voltage range.

**Dave Jones:** You kind of expect it to do that really as long as it's within your acceptable margin. I mean, before when we're getting 300 microvolts, in some chips I was measuring we're getting 500 microvolts.

**Dave Jones:** That clearly wasn't acceptable for my purposes that I want it for. So, but this sort of range, you know, plus minus 100 microvolts or 1 microvolt essential V offset combined, then hey, that's just fine.

**Dave Jones:** And then if we install a 500 ohm trim pot as the bias resistor here, you'll notice that we can actually tweak it. Let's uh get our average there. Watch see it's stable.

**Dave Jones:** Now, I can uh tweak this thing. Look at that. Not a problem at all. So, you can actually tweak your input bias current. You can null them out, but then you've got to do that at a particular uh supply voltage, of course, and common mode range.

**Dave Jones:** But, of course, if you start changing your voltage rail here, then you're going to find that that setting is what? Look, no good anymore. So, yeah, it's only going to be valid that particular bias current for a particular supply and common mode input range.

**Dave Jones:** Oh, and by the way, if your bias resistor here is actually uh large in value, then noise can become a problem, thermal noise. So, you may want to actually bypass that with a cap.

**Dave Jones:** And for those curious about the bypass caps, I've removed both of these, and I've put a .47 mic directly across the rails like that. Once again, we're back to a 100 ohm input resistor there, and there is our offset voltage, or our equivalent offset voltage with our 5-V rail.

**Dave Jones:** And, of course, if we take that down, it's just going to drop again and again and we'll probably find that one sucker there go a bit negative down at 2.7.

**Dave Jones:** And it makes no difference if we leave both those caps in and put a .47 across there as well. It's still not going to fix, in quote marks, the issue.

**Dave Jones:** So, what we've got here is a chopper amp. Its internal architecture is unknown to us. It uses some ping-pong patented architecture that Analog Devices have come up with. It auto zeros and chops and does slices and dices and makes your bread for you and does all sorts of things.

**Dave Jones:** Um yeah, it's going to we're not going to get a consistent well, a VOS and or input bias currents that can go in either direction for both of the inputs over the supply voltage range here.

**Dave Jones:** So, uh what are you left to do? Not much. You either put up with it over your supply voltage range, or you fix it at a particular voltage range, or you choose some other op amp.

**Dave Jones:** It's up to you. And for those curious if we're actually able to measure the input bias current on here, well, let's give it a go, shall we? Not particularly easy, but I've hooked up my Keithley picoammeter, there it is, and that at 5-V supply rail, it's the 1-nA range, so we're talking picoamps there.

**Dave Jones:** So, 1620 odd picoamps into that non-inverting input. That's uh through that 100- ohm bias resistor. And if I That's at 5 V, and if I lower the voltage, so that's 4 and 1/2, we'll probably see it change.

**Dave Jones:** It's a bit noisy there. This isn't the lowest noise setup. I could uh I'd have to dick around a lot more to get lower noise. That's 3.5 V. There we go, we're getting almost down to zero.

**Dave Jones:** Will it actually go in the opposite direction? 2.7? Yeah, it does. So, there we go. That's at 2.7, it's actually gone the other way. Ta-da! So, there you go.

**Dave Jones:** I hope you enjoyed that follow-up Fundamental Friday to the previous video. And if you like the concept, give it a big thumbs up. And if you want to discuss it, you know where to do it, the EE blog forum, or you can leave comments on the blog website or on YouTube.

**Dave Jones:** Catch you next time.
