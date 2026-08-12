---
video_id: oRvxjxs3cE0
title: EEVblog 1609 - Composite Amplifier Tutorial + Practical Demo
url: https://www.youtube.com/watch?v=oRvxjxs3cE0
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 30, "3": 47, "4": 60, "5": 72, "6": 86, "7": 99, "8": 115, "9": 134, "10": 149, "11": 163, "12": 179, "13": 191, "14": 206, "15": 220, "16": 239, "17": 256, "18": 270, "19": 286, "20": 301, "21": 317, "22": 330, "23": 346, "24": 361, "25": 380, "26": 398, "27": 416, "28": 434, "29": 449, "30": 466, "31": 481, "32": 494, "33": 510, "34": 528, "35": 542, "36": 561, "37": 578, "38": 593, "39": 610, "40": 623, "41": 638, "42": 652, "43": 671, "44": 684, "45": 697, "46": 710, "47": 726, "48": 741, "49": 752, "50": 767, "51": 781, "52": 793, "53": 808, "54": 818, "55": 834, "56": 850, "57": 866, "58": 881, "59": 896, "60": 914, "61": 928, "62": 943, "63": 959, "64": 972, "65": 989, "66": 999, "67": 1014, "68": 1029, "69": 1042, "70": 1056, "71": 1071, "72": 1083, "73": 1097, "74": 1112, "75": 1126, "76": 1140, "77": 1153, "78": 1169, "79": 1188, "80": 1203, "81": 1218, "82": 1232, "83": 1251, "84": 1265, "85": 1280, "86": 1297, "87": 1312, "88": 1329, "89": 1347, "90": 1363, "91": 1372}
---

**Dave Jones:** Hi, it's time for another installment in the op amp tutorial series. Today we're going to take a look at composite amplifiers and you may not have heard of these before because your regular textbooks pretty much don't mention composite amplifiers at all. But in the

**Dave Jones:** real world when you have to meet system design application goals, you can bet that one day you might have to use a composite amplifier. So anyway, I'll link in all my tutorial series down below for op amps. So this one kind of

**Dave Jones:** follows on from the multi-stage compound amplifier we looked at in the the previous video where we cascaded multiple amplifiers in series to give us increased system bandwidth. And you can do this with composite amplifiers too, but composite amplifiers have a huge

**Dave Jones:** number of other benefits we're going to look at. So in that previous video we looked at a multi-stage amplifier also known as a compound amplifier because the amplifiers the gain of each stage is compounded together to give you a total

**Dave Jones:** system gain. Like this one could be times 10. I've drawn it as a buffer here just for simplicity, but it could be a times 10 amplifier. This one's times 10 gives you a total gain of times 100, but

**Dave Jones:** you get extra bandwidth because you've split the gain of times 10 here and times 10 here. So that's just a little way to increase your system bandwidth. So let's take the simple example of two buffer amplifiers in series here in this

**Dave Jones:** multi-stage compound configuration. Of course, this is just acting as a buffer. This one's acting as a buffer here. Now, why would you do that in this particular case? Well, at the end of this video, hang around, we'll do a practical

**Dave Jones:** breadboard example of kind of what we're looking at here. In the real world in practical applications, you often have multiple system design requirements for your amplifier and some of them can include, you know, input impedance. You might need really high input impedance. You

**Dave Jones:** might need ultra-low input offset voltage, really DC precision stuff. You might need a huge bandwidth. You might need a huge output drive capability, driving ultra-low impedance loads, or driving high-capacitive loads. You might need really low drift with temperature, for example. You might need

**Dave Jones:** ultra-low noise. And Okay, good luck trying to find that perfect amplifier. Even though you can get thousands of amplifiers from your local component supplier, good luck finding like one that does all these things, because you can't. There's no

**Dave Jones:** such thing as often as a perfect amplifier in practice. And this is where composite amplifiers come into play. Composite amplifiers allow you to actually design your circuit so that you can use the best, and you can pick and

**Dave Jones:** choose the best specifications of different types of op-amps, and combine them together into one composite amplifier. It's really cool. So, how does a composite amplifier work? Well, it's really simple. In the multi-stage one we had here, the output

**Dave Jones:** we've got its own little feedback loop here, and the output drives the input of the second stage amplifier. It's got its own little feedback loop here. It's unity gain here, but of course you can have your gain resistors in there. You

**Dave Jones:** can have your compensation networks and all sorts of things. So, they're two separate amplifiers, and they don't really interact with each other at all, except from like a load point of view. That's it. But a composite amplifier, you actually join these two together so

**Dave Jones:** that they're joined at the hip, and you get the best of both worlds. So, to turn our simple example of two buffer amplifiers here into a composite amplifier, we just break the feedback path here. Instead of taking it from the output of that, we

**Dave Jones:** take it from the output of the second amplifier here. So, the second amplifier, we'll call A2, is included in the feedback loop for A1. And when you do this, it's incredibly powerful because you might choose amplifier A1 because it's an ultra low

**Dave Jones:** offset voltage DC precision amplifier, for example. You know, it's got .1 microvolts offset voltage in it. But, you might want to drive a big load with that thing. And go and look up any ultra low offset, you know, chopper stabilized operational

**Dave Jones:** amplifier, and you'll find that well, they can't drive any load at all, really. So, you include this buffer amplifier in the feedback path here so that the sensing is taken from the output. So, what you're doing here is if

**Dave Jones:** you've got a ultra low offset voltage on the input to here, then what it's going to do is give you that ultra low offset voltage on the output here instead of here, but you get the drive capability of amplifier A2, which might be a huge

**Dave Jones:** like grunty output buffer that can drive hundreds of milliamps or amps. So, you can drive amps of current into your output, but you have the benefit of the ultra low input offset voltage or the ultra low noise or whatever it is of

**Dave Jones:** this input stage and your output stage here combined. You get the best of both of the specs of these two different amplifiers. Now, you might be asking, "Dave, well, why can't we just connect that to there like this and just like

**Dave Jones:** we've got the input offset voltage and we just use the buffer?" Well, go check out the spec of any buffer amplifier like this, any high output drive capability, and you'll find they've got a terrible offset voltage, tens of

**Dave Jones:** millivolts. So, what you're doing is effectively adding like an extra, you know, 10 millivolts or whatever into there. So, you've got your nice precision amplifier like this. Sure, this point here, the output of this amplifier might be, you know, 0.1

**Dave Jones:** microvolts, for example, but then you've added this 10 the horrible offset of this. So, your output here is 10 millivolts. You've just destroyed it, right? You've just destroyed the advantage of using the ultra-low offset here. You might as well not even bother.

**Dave Jones:** But, if you connect that from there to there like this, your output then becomes 0.1, not millivolts, but microvolts. And you've gotten rid of essentially gotten rid of that offset voltage there. But, you haven't really gotten rid of that

**Dave Jones:** offset voltage in this horrible buffer amplifier here. It's just that because you're in a total composite loop configuration like this, if this amplifier here has 10 millivolts offset voltage on the input, then the output of this amplifier will actually drive it at

**Dave Jones:** minus 10 millivolts to compensate for the offset the horrible offset voltage of this, and it'll do it automatically cuz it's sensing the output voltage here. So, it knows how much to add the operational amplifier, due to op-amp action, knows that I know I need to add

**Dave Jones:** 10 millivolts here to keep the input offset voltage here the same cuz you remember your basic op-amp rules. No these input voltages are the same. So, your ultra-precision 0.1 microvolts input offset here is essentially transferred to the output of

**Dave Jones:** this horrible otherwise horrible amplifier here, but you get the benefit of this one doing whatever driving capability you need. Oh, and by the way, this doesn't need to be an op-amp on the input here. You might have seen

**Dave Jones:** in my teardowns of oscilloscopes, for example, reverse engineering an oscilloscope front end, you might find that they use JFETs on the input for like high impedance high bandwidth capabilities. They're actually discrete transistors in there instead of op-amps, but it's still a valid composite

**Dave Jones:** amplifier. You don't have It doesn't have to involve op-amps. All of this could be discrete transistor stuff. It doesn't matter. You could have a discrete transistor like driver output just like you'd have in say a home hi-fi amplifier and a big beefy MOSFETs in

**Dave Jones:** there being able to drive, you know, 4 ohm, 2 ohm loads and stuff like that. But, you might have some nice JFETs on the input here that, you know, really high impedance, low noise, everything else. And you combine the best of both

**Dave Jones:** worlds using a composite amplifier loop. So, it's not just specific to op-amps. You can use discrete components for either of these or both. So, let's add some gain to this circuit on the output driver A2 here. I've added R3 and R4.

**Dave Jones:** Once again, non-inverting configuration just to make it easier to look at, but this totally applies to the inverting configuration as well. And then we've got R1 and R2 setting the composite gain. So, we have the output say output stage gain. I don't know if

**Dave Jones:** that's the best terminology for it, but let's just call that the A2 output stage gain, but the actual gain of the composite amplifier is actually set by R1 and R2 here. So, if it helps, I've actually redrawn this and you can think

**Dave Jones:** about it as one big amplifier like this, okay? With the output stage A2, that gain stage there inside there with the resistors R3 and R4. And essentially, from the composite amplifier point of view, the gain is only set by R1 and R2. Technically

**Dave Jones:** speaking, the gain of this output stage doesn't actually impact the gain of the entire amplifier unless you go to really extreme levels, but we won't go into details like that. The gain is basically set by R1 and R2 here. I know this is a

**Dave Jones:** little bit confusing. You might think that well, changing the gain in here surely makes a difference. And well, it does. Say you want a total system gain of 10, which is set by these resistors here. If you actually choose R3 and R4

**Dave Jones:** here to give you a A2 stage gain of five for example, but you want a total system composite amplifier gain of 10. If you choose these values to have an A2 output stage gain of say five and you want a

**Dave Jones:** total system gain of 10, then it basically forces A1 here to have a gain of two to give you that total gain of 10. So, if this is times five, this must be times two. And likewise, if you

**Dave Jones:** wanted the gain to be equally shared between these, then you'd have to choose a gain of the square root of 10, which is 3.16. You'd have to set these choose these resistors to the 3.16 gain, and then that would force this amplifier

**Dave Jones:** here to also have a gain of 3.16. And that would come into play when you're talking about say gain bandwidth product as one example of your total composite amplifier. To get your most bandwidth possible, you might want to

**Dave Jones:** split your gains between those two. So, composite amplifiers, they're rather magical. They let you combine the best of different amplifiers, be they discrete components or op amps. Combine you know, input impedance, offset, bandwidth, output drive, drift, temperature drift, and noise, and all

**Dave Jones:** sorts of things. You can combine them together in many different ways, and I couldn't possibly cover all the different scenarios here. It would just take me forever. But as always, there's never a free lunch here, okay? And there

**Dave Jones:** are downsides to composite amplifiers if you don't implement them properly. You might find they oscillate or do other uh weird things. One general rule is that this uh second stage amplifier here must have a gate a greater gain bandwidth

**Dave Jones:** product than the first one here. Otherwise, they tend to oscillate. Now, I won't go into the details why uh that's the case. That's the subject of another more advanced uh video. And then likewise for something like noise, for

**Dave Jones:** example, you might have a really low noise, very schmick, you know, 1 nV per root Hz uh op-amp on the input here, and then your output uh amplifier might be 100 nV per root Hz here, and you can, depending

**Dave Jones:** on the gain of these, I won't go into too much detail, but you can trade off the gain of both of these stages so that you are actually the entire noise of the composite amplifier is actually lower than the worst-case 100 nV per root Hz

**Dave Jones:** here. So, effectively, if this one has enough gain, for example, it can compensate for the noise in the second one, but it's all a balancing trade-off, and it gets a bit complicated if you want to analyze it, but thing to take

**Dave Jones:** away from this is that composite amplifiers allow you to do stuff like that with noise and offset and input impedance and and drive capability and everything. Here's another interesting practical example. Well, excuse the crudity of model. Didn't have time to

**Dave Jones:** build it to scale or to paint it. Let's say you wanted a really precision DC precision high bandwidth amplifier capable of like driving a coax or something like that. Well, how do you do it? Well, you know, you've picked your

**Dave Jones:** buffer amplifier here. Ah, I can drive the coax at 1 gig. No worries, right? But you look at the specs, and it's just got horrible DC precision, right? So, what can you do? Composite amplifier, of course. So, let's say you needed your

**Dave Jones:** one you know, standard 1 meg input impedance here. Well, you can choose your A1 amplifier here to do all the DC precision. So, you'd select it for, you know, very ultra-low DC offset, low drift, low noise, everything else,

**Dave Jones:** right? So, this could handle your DC and low frequency stuff, but it's no good. It's only going to work, I don't know, up to a meg or something like that, right? It's no good for the 1 GHz that

**Dave Jones:** you want. Well, you can have a DC path here and an AC path through the AC coupling cap C1. So, at the higher frequency stuff, you don't really care about that DC precision stuff. So, it simply bypasses your DC precision circuit here. And of

**Dave Jones:** course, you want R1 and R2 to set your total composite amplifier gain here cuz it's feeding back from the output here instead of like feeding from here. So, it's a composite amplifier with the best of really high-frequency AC, high

**Dave Jones:** bandwidth, high drive capability with DC precision. And of course, you might have to add some compensation stuff in here to make sure everything's hunky-dory, but beauty, right? Combines the best of both worlds. Composite amplifiers, brilliant. So, hopefully, you're getting the idea

**Dave Jones:** that composite amplifiers are a very powerful technique to add into your design toolbox in the real world when you have all different sorts of requirements that you need and you can just can't find that perfect op amp. I've lost count of the number of times I

**Dave Jones:** could not find a perfect op amp op amp for a particular configuration and where just cascading them doesn't really get the job done because well, let's go to the bench right now and I'll show you a practical circuit where we combine an

**Dave Jones:** ultra-low offset chopper amplifier with an output buffer and see where it can give us a large drive current output capability with an ultra-low input offset voltage whilst also potentially compensating for any particular problems that we have in this output stage here

**Dave Jones:** in terms of driving. So, we're going to have a really precision, high-drive circuit. Let's go to the bench. All right, let's test an example circuit here on the breadboard. Now, I've got a MAX4239, which you should recognize from the

**Dave Jones:** microcurrent. It's a very low offset voltage chopper amplifier. So, only like microvolts of offset in this thing. I've got a non-inverting configuration with a gain of 10 here, and we're going to feed an input signal to here. And we're

**Dave Jones:** feeding the output here into a BUF634, which is a low impedance output driver for driving like heavy loads up to a couple of hundred milliamps because there's no way that the MAX4239 or any regular op amp can drive a low impedance

**Dave Jones:** load. In this case, we've got a 47-ohm resistor here. There's no way you can drive it. So, we're using this as a buffer amplifier. So, I've currently got the circuit configured like this. It's a classic two-stage compound amplifier,

**Dave Jones:** and the output drives the input of this one, and it drives a 47-ohm. So, we've got a common circuit ground here, and we've got a positive and rail. So, plus minus 2.5-V supply here cuz that's the limitation of our MAX4239.

**Dave Jones:** And before you watch the first part of this video, you might have thought, "Well, what's wrong with that circuit? It's going to work a treat. We're going to We've got a nice precision low offset amp here, and we'll be able to drive

**Dave Jones:** this 47-ohm load no problems whatsoever." But, uh-huh, let's take a look at the spec sheet. Here it is, the BUF634. It can drive up to 250 milliamps, 2,000 V per microsecond. It's really high bandwidth. No worries, right? It can work down to the voltage

**Dave Jones:** that we need. But, what don't they tell you on the front page here? They don't tell you the offset voltage. Well, let's go measure it because the MAX4239 is a little six-pin SOIC-23 here. I've done a second channel video actually soldering this.

**Dave Jones:** I'll link that in if you want to actually see it. I've just converted that into a DIP form factor. We've got our two gain resistors are This is just a pull down resistor on the input here and we've got our load over here and our

**Dave Jones:** output from our amplifier here goes over to the input and then the drives the 47 ohm load. Right, so let's just probe some signals here. Here's our input voltage. You can see that's just over 100 millivolts there. We've got a gain

**Dave Jones:** of 11 here because you have to include plus one for the non-inverting configuration. So our output voltage should be Let's one that up. There you go. Is 1.1 volts there. No worries. So that's on the output of our max 4239.

**Dave Jones:** Well, let's go over to our buffer over here and we can see that is exactly the same. Now watch what happens when I actually connect the load here cuz this will become interesting later. You'll notice that it's dropped a bit. That

**Dave Jones:** could be the impedance of my battery source here or whatever, but the fact is that we're still getting that output voltage here, right? But it's dropping a little bit on the output. But let's actually disconnect our signal and we're

**Dave Jones:** measuring the output of the buff amplifier here. Let's actually turn this up. Look at this. We're at 10 millivolts per division. 10, 20, 30 odd millivolts. And what do you know? If you have a look at the spec sheet here

**Dave Jones:** for the buff 634, 30 millivolts offset typical. What? So much for your nice precision circuit that you're trying to do here with your ultra low offset with your max 4239. You've just ruined it because you've used the compound

**Dave Jones:** configuration. And we can actually measure that here with our meter. We'll measure the offset voltage of the max 4239 here. You'll notice, right? It's naff all. And right, it's it's close to zero. It's like well, you know, 100

**Dave Jones:** microvolts there. That might be because I don't have a proper star ground and it's capable of better than that, but it's like it is really low, okay? So that's the output here. And the offset voltage of our bus 634 here, 33

**Dave Jones:** millivolts. So, we've ruined our beautiful little circuit. But, ah, we can change this with one little simple jumper wire to a uh composite amplifier configuration. So, what we're going to do here is we're going to break this and

**Dave Jones:** we're going to have this extended and we're going to connect it to the output here. And bingo, we've now got the buffer amplifier in our feedback loop of the MAX4239. So, our output voltage here now should be determined by our input amplifier,

**Dave Jones:** not by this bus 634. It should eliminate any offset voltage in here by compensating with the gain of this amplifier here. So, here's our feedback resistor coming from the output of the MAX4239. I'll connect that over here to

**Dave Jones:** the output of the buffer amplifier. No worries. And we're still probing the output of the buffer amplifier here. Look what's happened. That offset voltage that was up here, it's dropped down to zero. And we can confirm that with the multimeter

**Dave Jones:** over here, of course, but we don't really need to. There you go, it's zero. But, let's actually go back and have a look now at the output of the MAX4239. You don't get anything from This is now not going to be zero because it has to

**Dave Jones:** compensate for the output voltage here cuz it's sensing this output voltage. So, here's the output of the 4239. Uh 55 minus 55 millivolts there. So, it has to actually uh change the output voltage here to compensate for the

**Dave Jones:** output. But, this is where our line is being sensed now. So, it's now compensating for that bus 634. Now, there's our output signal from the buffer amplifier. And you'll notice that I've got that 47 ohm load connected here

**Dave Jones:** and now we're getting 1.15. So, you remember before that when it was a compound amplifier, when it wasn't sensing the output, we were actually getting a drop here. But, because the gain is now set by the entire composite

**Dave Jones:** amplifier here, driving the 47 ohm load is now accurate. It's 1.1 V. We don't get that drop that we saw before. And I can actually change that back live. Watch this. I'll do this. Sorry, but pin's bending is a pain, and

**Dave Jones:** stick it in there, and look, it's dropped to 860 mV. So, whatever problem that we had in the output stage of this bus 634 actually driving this, whatever loss we had in there, it was being compensated for by the fact that we were

**Dave Jones:** using that composite circuit configuration. So, once again, I'll change that back. And there you go, Bob's your uncle. We're back to 1.1 V. It's now compensating for that. Composite amplifiers, they're fantastic. They work a treat. So, there you go, we

**Dave Jones:** are getting the advantage of this ultra-low offset chopper amplifier, the MAX4239, but we're able to drive big heavy loads with it, high current loads, with our BUF634 composite circuits. They're very handy. So, there you go, I hope you enjoyed

**Dave Jones:** that theoretical and practical look at composite amplifiers. It's something that a lot of textbooks do not teach. But, in the real world, designing real world circuits, you have to often meet unusual requirements. This is just one example, there can be lots of others, um

**Dave Jones:** as we've talked about. So, there you go, I hope you enjoyed that video and found it useful. If you did, please give it a big thumbs up, and as always, discuss down below, and you can always check out

**Dave Jones:** the EEVblog forum down below as well, and the EEVblog merch store, which keeps all this going, eevblog.store. Catch you next time.
