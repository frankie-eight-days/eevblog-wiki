---
video_id: TxBJb-Z0XFI
title: EEVblog #479 - Opamp Input Bias Current
url: https://www.youtube.com/watch?v=TxBJb-Z0XFI
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 28, "3": 42, "4": 58, "5": 76, "6": 93, "7": 107, "8": 127, "9": 138, "10": 153, "11": 166, "12": 182, "13": 196, "14": 210, "15": 225, "16": 239, "17": 258, "18": 274, "19": 287, "20": 303, "21": 319, "22": 335, "23": 347, "24": 359, "25": 374, "26": 390, "27": 404, "28": 419, "29": 435, "30": 452, "31": 467, "32": 483, "33": 502, "34": 515, "35": 529, "36": 546, "37": 562, "38": 579, "39": 597, "40": 613, "41": 626, "42": 639, "43": 653, "44": 663, "45": 680, "46": 693, "47": 709, "48": 724, "49": 738, "50": 755, "51": 771, "52": 786, "53": 799, "54": 818, "55": 834, "56": 847, "57": 865, "58": 878, "59": 896, "60": 912, "61": 925, "62": 936, "63": 954, "64": 970, "65": 984, "66": 1004, "67": 1016, "68": 1030, "69": 1044, "70": 1059, "71": 1077, "72": 1093, "73": 1104, "74": 1120, "75": 1139, "76": 1155, "77": 1178, "78": 1196, "79": 1208, "80": 1224, "81": 1242, "82": 1254, "83": 1267, "84": 1283, "85": 1298, "86": 1312, "87": 1321, "88": 1334, "89": 1349, "90": 1362, "91": 1379, "92": 1395, "93": 1411, "94": 1427, "95": 1439, "96": 1453, "97": 1468, "98": 1483, "99": 1496, "100": 1513, "101": 1528, "102": 1542, "103": 1553, "104": 1571, "105": 1584, "106": 1602, "107": 1616, "108": 1629, "109": 1644, "110": 1657, "111": 1673, "112": 1685, "113": 1700, "114": 1713, "115": 1733, "116": 1750, "117": 1766, "118": 1780, "119": 1792, "120": 1805, "121": 1829, "122": 1844, "123": 1861, "124": 1877, "125": 1893, "126": 1910, "127": 1924, "128": 1937, "129": 1952, "130": 1966, "131": 1988, "132": 2005, "133": 2021, "134": 2033}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. This is a follow-up video from my previous one about measuring input offset voltage and some issues I had with an analog devices part. If you haven't seen it, click down below and you'll be able to

**Dave Jones:** watch that. It's a 30-minute video of me marking around measuring some input offset voltages. Great fun. But today, we're going to do something related which we'll get back to on the breadboard and solve our problem from last time.

**Dave Jones:** We've got op-amp input bias currents today. What is an op-amp input bias current and why is it important? Well, let's take a look at it. You've got your basic op-amp here. Doesn't matter what op-amp it is, they're all going to have

**Dave Jones:** what's called an input bias current. Now, uh you're used to dealing with an ideal op-amp. Now, an ideal op-amp, of course, one of the rules for the ideal op-amp is that no current flows into the input pins. But of course, in practice, that's

**Dave Jones:** complete because you're going to have some current flowing into or out of, we'll get into that, these input pins on this op-amp. And that's called the input bias current. And I've labeled that here IB+ and IB-. Now, a data sheet

**Dave Jones:** for a typical op-amp will only usually only show the input bias current as one figure, IB, they'll typically call it. They won't actually specify different input bias currents for the positive and negative. And that's where we'll get into later is the input There's There's

**Dave Jones:** two parameters to do with input bias current. One is the input bias current itself, IB. The other is IOS, which is the input offset current. And that is actually the difference between these two. But we'll get into that in a

**Dave Jones:** minute. Now, this input current in practice can range anywhere from femtoamps, a really schmick precision instrumentation grade op-amp might have, you know, a few tens of femtoamps input current. Or for a really fast wideband with op amp, they don't care about the input

**Dave Jones:** current. So, it's going to be a couple of microamps. They're going to optimize the internal architecture for that op amp. They don't care about the input bias current. They're going to optimize that for bandwidth and slew rate and all

**Dave Jones:** sorts of other things. So, there's a pretty big range there in the input bias current. So, how does that work? Well, let's take a look at the input circuitry or the basic topology of the input circuitry for a bipolar operational

**Dave Jones:** amplifier. So, this is not a FET input. It's a bipolar input op amp. And you'll notice that we have two input transistors here, both NPN going into a current source. It's a current mirror configuration and I won't go into all

**Dave Jones:** the details of, well, any significant detail of input op amp architecture. That requires a whole separate video, but suffice it to say, look, these inputs are connected directly to the base of these transistors here. and negative input on your op amp over here

**Dave Jones:** goes into these transistors. So, naturally, you're going to get some base current flowing in there and in there as well. And there's ways to lower that, of course. If you use a FET input op amp, well, FETs aren't effectively, right?

**Dave Jones:** They're a field effect transistor, no input current. But in practice, there is. In theory, there's not in practice. But this is a bipolar operational amplifier. You'll do it probably the most common one on the market, although FET ones are pretty

**Dave Jones:** darn common as well, CMOS ones. And there's other ways to lower this input bias current as well. They can actually use a Darlington configuration here so that your input bias current is lower. It's still using the bipolar manufacturing process, but there's

**Dave Jones:** issues with that in terms of bandwidth and all sorts of things, which I won't go into. And the other way to do it is what's called a biased bias offset operational amplifier or a bias offset input. And what they do is they actually

**Dave Jones:** put in here a current source in there and in here as well so that that biases the transistor instead of the input bias current. So, in theory, it cancels it out and you can get very low input bias

**Dave Jones:** currents from the input but not zero. They almost never Well, in practice, you can never get down to zero bias current. So, every practical op-amp, it regardless even if it's input bias compensated, is going to have some form

**Dave Jones:** of input bias current or IB. And it'll be mentioned in the data sheet. Now, these bias currents, they can be a real pain in the ass in precision applications. And there's quite a few uh different ways it can screw you up.

**Dave Jones:** Let's take a look at the first problem is the your uh source impedance of uh well, your source impedance. Okay? That's a series resistance of your source. Let's say it's 10K. Might be a typical value for um some systems. And

**Dave Jones:** if our input bias current is a very low 100 picoamps, right? That's a pretty good op-amp, very low input bias current at 100 picoamps, okay? Then our error that we're going to introduce in our system without ignoring everything else,

**Dave Jones:** offset errors and all the rest, is going to be 10K times that 100 picoamps because that 100 uh picoamps is flowing through that 10K resistor. We've got a 1 microvolt offset already, a 1 microvolt error. And well, it doesn't sound like much,

**Dave Jones:** does it? 1 microvolt. But if you're dealing with a precision system, then that can like a you know, a strain gauge or something else you're dealing with, that can be a real big deal cuz that these errors get multiplied by the gain

**Dave Jones:** of your op amp. So, it can screw you up right there. Just be careful. And 100 pA, that's a very low one. So, imagine if your source impedance is like a meg or something like that, and your uh

**Dave Jones:** uh bias current's even higher, you can get millivolts of error. Watch out. Now, the second problem we've got is errors introduced into our uh gain network and our feedback resistor network for this thing. Now, what happens? Let's take

**Dave Jones:** this uh inverting op amp configuration, and here's our input voltage, that's our output, of course, and let's ground this input here, and see what happens. Now, because the input, the uh non-inverting input down here is also grounded, and

**Dave Jones:** once again, we go back to our ideal op amp properties, we're assuming our input offset voltage, remember we're not talking about offset voltage yet, is zero. So, the difference between here and here is going to be zero. Remember,

**Dave Jones:** due to op amp action, the op amp does whatever it needs on the output to ensure that the two inputs are exactly the same voltage, if your input offset voltage is zero, which we'll assume. So, this point here is also

**Dave Jones:** 0 V. It's also grounded. So, there's no current flowing through R1 there at all. So, but we still have an input bias current. Remember, we always have that. It can't get away in this practical configuration. So, where does it come

**Dave Jones:** from? Well, it can't come from through this resistor here, because Ohm's law says 0 V across that resistor, doesn't matter what value it is, this R1, no current flows through it. So, all of the current must come from RF here. In this case, it flows

**Dave Jones:** around like that. So, all of our input bias current is flowing through RF, and you might see the problem already. Usually, to you want on an op amp, you're going to have some sort of gain, times 5, 10, 50, 100, even 1,000,

**Dave Jones:** depending on your um uh you know, your uh circuit application. Well, that means RF has your feedback resistor has to be a large value. What do you get when you have a large value resistor with a current flowing through it, IB, even a very

**Dave Jones:** small one? Aha, you're going to get an offset error introduced over and above your VOS. Your which is another figure on the data sheet, your uh input offset voltage. This is in addition to whatever that is. So, this is where input bias

**Dave Jones:** current can be a real pain in the ass for these precision applications. All that bias current flows through RF. So, how do we solve these input bias current issues? They're a pain in the ass for these precision applications. How do we

**Dave Jones:** get rid of it? How do we cancel them out? Well, let's uh have a look at what we've got here. IB+ and IB- one goes into the uh inverting input, one goes to the non-inverting input. So, they're essentially opposite currents. So, you

**Dave Jones:** can actually cancel them out. Now, let's go back to our original non-inverting configuration here, and we've got a simple voltage follower, okay, with our source impedance RS in here, whatever value it is, causing the error due to the input bias current flowing through

**Dave Jones:** it. Well, we know that the other input has an equal and opposite, or should have an equal and opposite input bias current. How do we cancel it out? Very easy. We just put another a feedback resistor in there,

**Dave Jones:** equal to let's call it RS2, equal to the value of RS. So, if IB+ and IB- are equal values, except opposite, cuz they're going into opposing inputs of the op-amp, I won't go into the internal details of it, but

**Dave Jones:** then you can cancel them out by having a a resistor in the feedback loop like that. And how do we solve this inverting op-amp configuration here? Well, essentially, exactly the same thing. Instead of this going to ground down here, we have

**Dave Jones:** a resistor in there going to ground. So, we're going to get our input bias current, and we can actually cancel them out like that. Now, let's call this R B, and what value should R B be? Well, it's a standard formula. It's actually R

**Dave Jones:** F in parallel with R 1. Now, I won't go into how you actually derive that. It's not actually that hard if you want to go into the details, but I won't waste the time doing that. But, that is a basic

**Dave Jones:** formula, and this is a very common thing that you'll see in a lot of circuits. You might have wondered why, well, why does it have this resistor in here? Is it protecting the input somehow? No, you know, it's to do with the input bias

**Dave Jones:** currents in these precision circuits. And of course, if you've got a very large gain here, and R F is much greater than R 1, then you can just say R B equals R 1 because the parallel combination of R F on top of that, to a

**Dave Jones:** rule of thumb, you know, to an order, if you've basically got a gain of 10 or more, and R F is 10 times R 1, you can generally say R B equals R 1, near enough. So, that was too easy, right? We

**Dave Jones:** fixed our input bias current. No big deal, just whacking a resistor in there, and you're right. Unfortunately, what? It doesn't work like that in practice because the input bias currents are not matched. These transistors are never a matched pair. You're never going

**Dave Jones:** to get precisely the same value. There's some op-amps that get really, really close, but in practice, it's not going to be zero, just like the input bias current itself, regardless of the topology used, is not going to be zero,

**Dave Jones:** either. And that's where this IOS comes in. The input offset current is the difference between IB plus and IB minus. So, there's actually two parameters there that you have to look at. Not not only the input bias current itself.

**Dave Jones:** Like, the input bias current could be really low. It might be 10 picoamps, for example. But then, if your IOS is 100 picoamps, for example, then well, jeez, that's all over the shop. There's no way that you can choose a

**Dave Jones:** resistor bias value that's going to work. You might fluke it. You might be able to tweak it for an individual chip or an individual circuit, but just as choosing a generic value to do it, no, you're not going to be able to do

**Dave Jones:** it. Unfortunately, it is just a problem with these op-amps. If you're really If you're doing ultra-precision applications, yeah, you'll have to trim these things to take into account the input bias currents. And on top of that, then we've got our voltage offset, as

**Dave Jones:** well. So, you could get to a point, depending on your particular op-amp you've chosen, that IOS could actually swamp your effective IB, or vice versa, or there's a combination of the two, and it can get really ugly. But on top of that, you

**Dave Jones:** wouldn't know what's even worse? Well, you might have a rail-to-rail op-amp. Now, I mentioned right back at the start, I think, that the input bias current can go either direction. Now, on a standard bipolar op-amp, like this, or

**Dave Jones:** on a FET input op-amp, for example, you're typically going to only going to get your input bias current going one way. But on rail-to-rail op-amps, they're internally biased, and they've got different configurations, and I won't go into the transistor

**Dave Jones:** configuration of an of a rail-to-rail input op-amp, because there's lots of tricks. They can actually vary in and like that. but basically, it means that current can also flow out of these pins as well, depending on the common mode voltage operating at. So, if

**Dave Jones:** this is zero, for example, you might have a curve like that where your current can be bias current can be positive and negative. So, this can be IB here, positive and negative, and at some transition point where you pass through

**Dave Jones:** it, you might end up going in the current may flow out of these pins back out and ruin your day. It can get really ugly. So, there's all sorts of problems. You got IB, you got IOS, you got V

**Dave Jones:** offset, you've got whether or not your input configuration, your topology, your circuit, and all sorts of stuff. Ah, is there an easy solution? No, afraid not. So, in practice, this can be a really big issue, even for circuits that you might not think are

**Dave Jones:** that critical. So, you got to keep an open mind, watch out for it just in case you get caught. I mean, depending on whether what our supply this can change with supply voltage as well, the common mode here, which is that's V common mode

**Dave Jones:** here, depending on what input configuration, whether or not you've got an input bias compensated or rail-to-rail op amp, the supply voltage, all sorts of stuff, and which configuration you're using, your source impedance. Ah, and we haven't even mentioned temperature.

**Dave Jones:** So, how do you know if your op amp has one of these input bias compensated values? Well, you're typically going to get a plus minus IB value like that. They're usually not going to give it for your input offset, but plus minus IB,

**Dave Jones:** that's a dead giveaway that the op amp you're using, even though they may not tell you, is input bias compensated. So, you can see how complicated this is already getting. And really, you know, we're not even throwing vos into the mix

**Dave Jones:** much the input offset voltage which the gain is going to get multiplied which is going to get multiplied by the gain of your op amp here and it can get really really nasty. So if you see any input

**Dave Jones:** offset issues they will typically be a combination of the real input offset voltage which is a separate parameter vos entirely separate parameter on your data sheet up here but it can also include your input bias currents and that's what

**Dave Jones:** we saw in the previous video. If you haven't seen it link it down below. So let's now go back to the breadboard from that previous video and see if we can reduce or eliminate or compensate for these input bias currents and see how it

**Dave Jones:** affects our final output offset error and just a quick background to our previous video and you really should watch the previous video it'll be linked down below if you haven't seen this otherwise it may be a little bit

**Dave Jones:** confusing for you but basically we had a analog devices ad 8628 op amp with times 100 gain in the non-inverting configuration and it and we were getting an output voltage which was higher than just the expected offset voltage here. Now here's the

**Dave Jones:** actual circuit we got we got 1k going to ground here we got a 100k here total gain of 101 we're going to call it 100 near enough and the input offset voltage of this particular op amp is supposed to

**Dave Jones:** be around about one microvolt. So we only expect sort of around about 100 microvolts on the output here but this is our output voltage and we're getting over 300 microvolts here and this is our supply voltage we're using a split

**Dave Jones:** supply here. So the ground point is actually in the middle so it's plus minus two and a half volts but our output voltage is higher than what we expect from just a typical device. And technically, yes, it is within spec

**Dave Jones:** because the here it is input offset voltage VOS there at 5 V supply is a typical value of 1 microvolt, but it could be as high as 5 microvolts. So that would translate to 500 microvolts on the output here. But as I said in the

**Dave Jones:** previous video, it that's not actually the case. This op amp is actually typically 1 microvolt or less. And I've tried multiple op amps and the and that error is coming from somewhere else. Well, guess where? Input bias currents. And if we have a

**Dave Jones:** look at our data sheet here, you'll notice that as I explained before, well, there's a figure for IB there, input bias current, and input offset current right here. Here it is. The AD 8628. It's going to It actually gets higher

**Dave Jones:** with the quad package, by the way. That's just to do with the uh process technology that they're actually uh using. They've got four of those on the one die, and it's different. So anyway, we've got the single one, the 8628.

**Dave Jones:** Input bias current, typically 30 pA. It could be as high as 100 pA there, but you know, it we are going to get the typical uh figure down in here. So aha, 30 pA. Let's have a look. Is it a

**Dave Jones:** coincidence that our output is just over 300 uh microvolts here? Let's do the math, shall we? 30 if IB here, let's ignore this input here. Okay, let's ignore the non-inverting input. Let's just look at the inverting input here. If our input

**Dave Jones:** bias current, let's assume it's going into the pin, then uh if it's 30 pA going in, you remember before, if we ignore the V offset, then there's no voltage drop across this resistor, so all the input bias current,

**Dave Jones:** that whole 30 picoamps, av- you know, typical, is coming through that 100 K resistor. Aha. So, let's do the math here. 30 picoamps, there it is, times 100 K equals 3 microvolts. So, we're getting 3 microvolts error just due to the current

**Dave Jones:** going in there, the input bias current into that inverting input there. But, the gain of the op-amp, of course, is 100. So, we have to multiply that by 100, and of course, you get 300 microvolts. Aha. Look, 300 microvolts or

**Dave Jones:** just over. Is that a coincidence? I think not. Well, it's not going to be the entire story, but it is certainly going to be a lot of the reason for this. And by the way, um if you haven't

**Dave Jones:** seen the previous video, this does change with supply voltage. So, if we drop the supply voltage down, you can actually see it change significantly, and even go negative like that. You remember what we were talking about with that Oops, sorry. It should only go to

**Dave Jones:** 2.7. There we go. 2.7, it's almost going negative there. So, that does change with supply voltage, as I mentioned previously in the video earlier. Now, of course, that's not going to be the only reason, but it's going to have a significant effect on

**Dave Jones:** that. Of course, our V offset is going to come into it, and V offset's going to get multiplied by the gain of 100 as well. And then, we haven't taken into account the input offset on the other pin and stuff like that, but there you

**Dave Jones:** go. That is going to be a very significant reason for it. So, the previous video, yes. I mean, I've done this stuff before, but it's actually been, you know, I don't know, 7 years or something we since I last touched this

**Dave Jones:** sort of stuff. So, I forgot that the error term is going to be coming through the 100k resistor here, and it didn't help that the Analog Devices data sheet actually shows these these exact same values in a typical example

**Dave Jones:** test circuit. So, what You know, I just overlooked it. That can easily happen to even somebody who's done this stuff before, and I made the assumption that it was only going through the 1k, which is incorrect. All of that bias current is

**Dave Jones:** going through there. That's why I I knew that I could have put an additional bias resistor in here like this, but then I knew You know, I I did sort of did the math in my head as I was going

**Dave Jones:** along, and I went, "Oh, it couldn't make an effect. I could make that one 1k, of course, as we've talked about. It should be 100k in parallel with 1k, but you know, it's going to be pretty close to

**Dave Jones:** 1k. So, we can put that in there, but I think you'll find if we do that, and we will do it in a second, that it will change this value. This value will actually change. Now, let's actually get a

**Dave Jones:** average of that, shall we? There we go. It's pretty close. Let's call it 300. Spot on to 300 average. So, what we'll do now is we'll just put a bias resistor in here, and we'll find that it'll likely change. I'd be very

**Dave Jones:** surprised if it doesn't, but it's not going to null out to zero cuz we've still got the V offset plus other issues, and then the supply voltage as well, and this is a rail-to-rail op amp as well, and as I mentioned, and all

**Dave Jones:** that sort of stuff uh sort of comes into effect, and we haven't even mentioned ta-da, the elephant in the room, which is the input offset current, IOS. Look at this. A typical value of 50 picoamps. Look at this. So, it's

**Dave Jones:** actually higher than the input bias current. So, even if both inputs are matched precisely, so even if we had VOS equal to zero, which it's not, but let's assume it was, and both these input bias currents were identical, and we put our

**Dave Jones:** 1K bias resistor in here, this IOS is still going to screw us up because we have an uncertainty there between the two inputs, IB+ and IB- of 50 picoamps. So, you just don't know. You don't know what this chip is going

**Dave Jones:** to do until you actually build it up and test it. All right, so I've now soldered a 1K resistor in there, bias resistor into the non-inverting input there. So, we should be able to compensate for that that claimed input typical input bias

**Dave Jones:** current. So, let's switch the supply in here, 5 volts, and look, it has actually dropped. There you go. It's dropped from 300. It's all over the shop. There's a bit of noise on there. Let's get an average of that.

**Dave Jones:** There you go. Let's say it's dropped to 180. I think it's it's changing because it's probably still something still a bit warm there, perhaps from my soldering iron. You've got to be careful of that. That can be a trap for young players

**Dave Jones:** when you're measuring critical stuff like this and you've just soldered it. The chip could be hot, the components could be hot, whatever. Anyway, it's dropped from 300 down to 200. So, that is a change which I I would have been surprised if

**Dave Jones:** we didn't get any. There we go, it's 240. So, it's not quite You know, it's changed by 70 microamps, but it's still as you can see, even with the input bias resistor in there, properly designed, it's still not happening. So, how can we

**Dave Jones:** solve this? Well, of course, we could put a pot in here and actually tweak that out and null it out, but that's not actually a solution for the final circuit I want. So, what we're going to have to do here is drop these values

**Dave Jones:** because as I said, all that bias current IB looks like it probably dominates. I I basically what I want to do is reduce uh I fix this circuit so that the input bias current really doesn't have an effect. It's dominated by the VOS term

**Dave Jones:** there. So, let's change let's lower these by an order of magnitude and we should see let's leave this 1K in Well, no, actually I'll take out the 1K. Right? I'll take out the 1K. I'll short it back down to ground. Let's lower these by an

**Dave Jones:** order of magnitude. So, I'll put 100 ohms and 10K in there and we should find that 300 we got before drops down to you know, in theory it should drop down to 30. Right? If VOS doesn't come into it,

**Dave Jones:** but it could drop down to 100 or something like that. But, we should find that we'll get better than what we're getting here now. And there you have it. It dropped, but not by a huge amount. You know, we're only

**Dave Jones:** talking uh what average you know, 240. It's dropped like 60 microvolts or something like that. Not a huge amount when we change dropped these by an order of magnitude. But, then again, we don't have that bias resistor in there. So, let me add 100 ohms in

**Dave Jones:** there. And bingo, there you go. With 100 ohm bias resistor in here, that's look we're getting it's a bit noisier. I got a huge resistor on there. It's probably picking up something, but let's get an average on that. There we go. It's

**Dave Jones:** dropped down to an average of like 50 or 60 microvolts. So, we've effectively you know, really gotten down to just what we expect with the V offset voltage there cuz I on a typical chip like this, I expect it to be slightly under 100 1

**Dave Jones:** microvolt. So, like point which would be this digit here would be one. So, if we had one there, it would equate to a V offset of 1 microvolt cuz of the gain of a hundred. So, the fact that we're getting around about point

**Dave Jones:** seven if in theory we've nulled out both those input bias currents and we're not sure if we have. I mean, that's the thing with this, right? We don't actually know what we've uh well, we know we've achieved something, right?

**Dave Jones:** We've trimmed this thing down so it's better, but we don't actually know what the exact culprit was cuz this is a rail-to-rail um op-amp here, so we don't exactly know the topology. Add that this is a chopper amp as well, so there's going to be

**Dave Jones:** input switching uh current and all sorts of stuff to do with that and this isn't just your regular op-amp, by the way. It's an input It's I've done a whole video on chopper amps, which I'll link in down below as I

**Dave Jones:** did link on on the previous video. So, you know, we've tweaked it by lowering these values and adding in our proper bias resistor and you know, we can probably say now that VOS dominates, but does it? Uh we don't know because we've

**Dave Jones:** only got one sample of this chip. I'd have to do like, you know, ten samples to get sort of meaningful uh data to see as what the exact culprit is. We don't know uh whether the input bias is flowing in

**Dave Jones:** or out of either of those pins, you know, it's just crazy. And well, let's see what happens if we change the supply rail. Here we go. Oh, sorry. I got to switch off my average mode. It's not a rolling

**Dave Jones:** average, it's a average over time there. So, let's start back up at our maximum supply rail of five volts. Let's say we're getting a hundred. There we go. That's different to what Anyway, it's jumping around a bit. It's

**Dave Jones:** a bit noisy, but we drop in and look at that, folks. It's going negative now. There you go, which is okay. It's to be expected. There you go. Now, we're down at its minimum supply rail of 2.7 volts and

**Dave Jones:** we're getting basically a negative uh we've gone all the way from positive up to uh hold. Hang on, bloody multimeter. There we go. Average. We've gone all the way from positive to negative there because this is a rail-to-rail op-amp. As I said, the

**Dave Jones:** topology we've got allows currents to flow either way and in combination with V offset, which also could change over change over the supply rail range. So, our common mode range is different and our bypass decoupling as well, which we

**Dave Jones:** saw made a difference in the previous video. All these things combined make this a little tricky circuit to actually null this thing out completely over the supply range, but I'm pretty happy with that. By adding the bias resistor in

**Dave Jones:** there, we've done a pretty good job. I mean, I don't care if it fluctuates plus minus like that over the supply voltage range. You kind of expect it to do that really as long as it's within your acceptable margin. I mean, before when

**Dave Jones:** we're getting 300 microvolts, in some chips I was measuring we're getting 500 microvolts. That clearly wasn't acceptable for my purposes that I want it for. So, but this sort of range, you know, plus minus 100 microvolts or 1

**Dave Jones:** microvolt essential V offset combined, then hey, that's just fine. And then if we install a 500 ohm trim pot as the bias resistor here, you'll notice that we can actually tweak it. Let's uh get our average there. Watch see it's stable. Now, I can uh

**Dave Jones:** tweak this thing. Look at that. Not a problem at all. So, you can actually tweak your input bias current. You can null them out, but then you've got to do that at a particular uh supply voltage, of course, and common

**Dave Jones:** mode range. But, of course, if you start changing your voltage rail here, then you're going to find that that setting is what? Look, no good anymore. So, yeah, it's only going to be valid that particular bias current for a

**Dave Jones:** particular supply and common mode input range. Oh, and by the way, if your bias resistor here is actually uh large in value, then noise can become a problem, thermal noise. So, you may want to actually bypass that with a cap. And for

**Dave Jones:** those curious about the bypass caps, I've removed both of these, and I've put a .47 mic directly across the rails like that. Once again, we're back to a 100 ohm input resistor there, and there is our offset voltage, or our equivalent

**Dave Jones:** offset voltage with our 5-V rail. And, of course, if we take that down, it's just going to drop again and again and we'll probably find that one sucker there go a bit negative down at 2.7. And it makes no difference if we leave both

**Dave Jones:** those caps in and put a .47 across there as well. It's still not going to fix, in quote marks, the issue. So, what we've got here is a chopper amp. Its internal architecture is unknown to us. It uses some ping-pong patented

**Dave Jones:** architecture that Analog Devices have come up with. It auto zeros and chops and does slices and dices and makes your bread for you and does all sorts of things. Um yeah, it's going to we're not going to get a consistent

**Dave Jones:** well, a VOS and or input bias currents that can go in either direction for both of the inputs over the supply voltage range here. So, uh what are you left to do? Not much. You either put up with it over your supply

**Dave Jones:** voltage range, or you fix it at a particular voltage range, or you choose some other op amp. It's up to you. And for those curious if we're actually able to measure the input bias current on here, well, let's give it a go, shall

**Dave Jones:** we? Not particularly easy, but I've hooked up my Keithley picoammeter, there it is, and that at 5-V supply rail, it's the 1-nA range, so we're talking picoamps there. So, 1620 odd picoamps into that non-inverting input. That's uh through

**Dave Jones:** that 100- ohm bias resistor. And if I That's at 5 V, and if I lower the voltage, so that's 4 and 1/2, we'll probably see it change. It's a bit noisy there. This isn't the lowest noise setup. I could uh

**Dave Jones:** I'd have to dick around a lot more to get lower noise. That's 3.5 V. There we go, we're getting almost down to zero. Will it actually go in the opposite direction? 2.7? Yeah, it does. So, there we go. That's at 2.7, it's actually gone

**Dave Jones:** the other way. Ta-da! So, there you go. I hope you enjoyed that follow-up Fundamental Friday to the previous video. And if you like the concept, give it a big thumbs up. And if you want to discuss it, you

**Dave Jones:** know where to do it, the EE blog forum, or you can leave comments on the blog website or on YouTube. Catch you next time.
