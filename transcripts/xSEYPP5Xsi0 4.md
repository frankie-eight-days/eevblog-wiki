---
video_id: xSEYPP5Xsi0
title: EEVblog #931 - Designing A Better Multimeter PART 2
url: https://www.youtube.com/watch?v=xSEYPP5Xsi0
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 24, "3": 43, "4": 54, "5": 63, "6": 83, "7": 96, "8": 107, "9": 121, "10": 133, "11": 143, "12": 152, "13": 163, "14": 173, "15": 183, "16": 197, "17": 208, "18": 235, "19": 246, "20": 258, "21": 273, "22": 285, "23": 294, "24": 311, "25": 329, "26": 339, "27": 354, "28": 368, "29": 378, "30": 396, "31": 411, "32": 434, "33": 446, "34": 462, "35": 476, "36": 492, "37": 516, "38": 528, "39": 543, "40": 553, "41": 562, "42": 569, "43": 588, "44": 605, "45": 620, "46": 632, "47": 646, "48": 655, "49": 675, "50": 685, "51": 703, "52": 711, "53": 722, "54": 731, "55": 740, "56": 751, "57": 767, "58": 781, "59": 792, "60": 804, "61": 815, "62": 831, "63": 842, "64": 855, "65": 864, "66": 876, "67": 893, "68": 903, "69": 921, "70": 936, "71": 951, "72": 965, "73": 985, "74": 994, "75": 1004, "76": 1014, "77": 1022, "78": 1037, "79": 1051, "80": 1062, "81": 1070, "82": 1082, "83": 1093, "84": 1100, "85": 1112, "86": 1126, "87": 1140, "88": 1157, "89": 1182, "90": 1195, "91": 1218, "92": 1229, "93": 1241, "94": 1255, "95": 1272, "96": 1294, "97": 1309, "98": 1320, "99": 1328, "100": 1341, "101": 1359, "102": 1370, "103": 1389, "104": 1412, "105": 1428, "106": 1441, "107": 1463, "108": 1473, "109": 1486, "110": 1504, "111": 1516, "112": 1534, "113": 1546, "114": 1559, "115": 1570, "116": 1582, "117": 1596, "118": 1613, "119": 1627, "120": 1635, "121": 1648, "122": 1660, "123": 1671, "124": 1683, "125": 1702, "126": 1719, "127": 1735, "128": 1748, "129": 1759, "130": 1770, "131": 1783, "132": 1791, "133": 1804, "134": 1820, "135": 1830, "136": 1856, "137": 1866, "138": 1878, "139": 1893, "140": 1905, "141": 1912, "142": 1925, "143": 1934, "144": 1951, "145": 1962, "146": 1976, "147": 1988, "148": 2013, "149": 2034, "150": 2046, "151": 2060, "152": 2068, "153": 2079}
---

**Dave Jones:** Hi. In a previous video, we took a look at how to redesign the current measurement functionality of a typical multimeter and how to make it better in terms of lowering the burden voltage across the not only the shunt resistor, but the fuse as well.

**Dave Jones:** So, click here if you haven't seen that video because this is a follow-on from that. So, it probably may not make much sense where we're starting from here. So, definitely check that out first.

**Dave Jones:** Now, last time we looked at this, what we did is we optimized the ranges here from 500 microamps up to 5 or 10 amps here and we got basically a maximum of 50 millivolt shunt burden voltage plus the fuse burden voltage of 5 or 50 millivolts and that was pretty good.

**Dave Jones:** And we came up with solution with just a couple of muxes here and a times 10 low offset chopper amp here. But this is not necessarily how you'd implement this in practice.

**Dave Jones:** It showed that we went through and got all these ranges and sort of, you know, here's our maximum burden voltage. But as far as practically implementing this goes, we can actually do better than this.

**Dave Jones:** We haven't done any optimization yet. We just figured out this is the concept of what we needed. But there's a way to actually optimize this circuit so that we can actually get rid of these muxes and I want to show you an additional way that which I hinted at in the last video where we can actually get rid of the times 10 chopper amp as well.

**Dave Jones:** And this sort of circuit optimization is a very common technique. You come up with the concept first of what you actually need and then you go through and optimize it from either a component count point of view.

**Dave Jones:** Usually less components the better. You can make it on a smaller size board, usually cost less and we might be able to reuse components for example or other stuff, bomb optimization, bill of materials optimization, all that sort of jazz.

**Dave Jones:** So, you know, this is not necessarily how I'd implement it. Now, I did this in my microcurrent gold and I've probably done this in a video, not specifically, but maybe in as part of a video somewhere, I'm sure.

**Dave Jones:** And if you have a look at my microcurrent circuit, you can see it's a little bit complicated, the switching arrangement used in terms of the microamp, the milliamp, and the amps range there.

**Dave Jones:** Now, in this particular case, I came up with a clever switching arrangement for using the type of switch that I had available for the particular current. There was actually limited choices in this.

**Dave Jones:** So, I sort of had to come up with a solution here to match the switching solution that I had found and that I wanted to use. Now, in the nanoamp range, it's pretty easy.

**Dave Jones:** Here's the switch configuration for that, and you can see that there's basically a 10k shunt resistor hooked directly onto the times 10 amplifier. The other two shunt resistors in there aren't used.

**Dave Jones:** Very simple. But if we switch to the microamp range here, then you can see that we're actually switching the 10-ohm resistor in series with the 10 milliohm shunt there.

**Dave Jones:** It's actually in series. We've got both in there, but because the 10 milliohms is three orders of magnitude less than the 10 ohms, it it's still within spec and you can ignore the 10 milliohms there.

**Dave Jones:** And you might notice as well that the 10k is still in parallel with that. So, once again, it's three orders of magnitude larger, so it's still within all the specs we wanted, so you don't have to worry about the 10k in parallel.

**Dave Jones:** Now, in both these cases, we've been reading the voltage directly across the particular shunt resistor the 10k or the 10-ohm resistor used, just like we did in this here.

**Dave Jones:** We're reading directly across any particular shunt resistor every in this range, this range, or this range up here. But something interesting happens if we switch it to the amps range here, you can see that actually the current is switched just through the 10 milliohm shunt resistance, but we're actually tapping off via the additional shunt that 10-ohm shunt resistor, we're actually tapping the voltage off that.

**Dave Jones:** And the reason that we can do that is because the input impedance of our amplifier is extremely high, essentially infinite. There's no input current, so there's no voltage drop across that 10 ohm shunt resistor.

**Dave Jones:** So, we're actually using one of the shunt resistors as a tap to measure the voltage. So, that's actually not an uncommon technique, and you guessed it, we can apply it here as well.

**Dave Jones:** So, let's take a look at how we're tapping this off. As we said before, we just implemented a mux because that just explained it real easy. So, in the amps range down here or the amps and 500 milliamps, we measure directly off the 10 milliohm shunt resistor.

**Dave Jones:** Then when our multimeter switches to 50 or 500 milliamps, we read off this shunt resistor. Well, it's actually across both of them, but it's still directly off the top of the shunt resistor there.

**Dave Jones:** And likewise for this one, we measure directly across that shunt resistor. But what if we can stack them in series like this and actually optimize and even get rid of our muxes.

**Dave Jones:** So, what we're going to do is rub out that. We don't need that tap. We don't need that tap. And let's see if we can just get away with a single tap from the top while cascading these resistors kind of like we did on the micro current.

**Dave Jones:** So, what we did is the 100 ohm resistor here, okay? We can Well, let's put that in there. Let's tap that over to there. So, now we've got all three in series, and we're only now Well, we've only now got this single tap off the top.

**Dave Jones:** Now, if we do that, if we take the case of the micro amp range up here, our range switches up here, so we use our we plug our probe into the micro amps jack.

**Dave Jones:** We short out this, and we've actually got these three resistors now in series like this. So, of course, you might have 90 sorry, this might be a 9 uh 9, for example, 9.9 ohms and then we've got our 1 ohm and our 10 milliohms down here.

**Dave Jones:** It could be 10 ohms, but you know, we mentioned that in the last video. Anyway, if you just want to make it a nice even value across there, you would actually have to take into account that you had all three in series like that.

**Dave Jones:** So, you can see how in this case it works easy. We've basically got our 100 ohm shunt resistor still or slightly higher if you didn't bother changing the values and we just tap off that like that.

**Dave Jones:** Bingo, too easy. Now, if we take the case of the milliamp range, our probe is still plugged into here, our milliamp position switch switches down to here, so it actually this now becomes open circuit here, okay, but we're shorting onto this range.

**Dave Jones:** So, our shunt resistor is the 1 ohm plus the 10 milliohms in series like this, but we're still tapping off this top bit here because our 100 ohm resistor there's no voltage drop across that cuz it's disconnected here.

**Dave Jones:** Actually, there we go. And the input impedance of our mux or our amplifier or whatever you want, ADC or whatever you want to plug this thing into is extremely high, consider it infinite, especially considering we're down in the hundreds of ohms region here, then there's no voltage drop across this and you're just using that as a sense line to sense directly off this 1 ohm resistor here.

**Dave Jones:** Beauty. And likewise for the amps range, we now move our probe over to here, so effectively the it doesn't matter which position we select here, microamps or milliamps, doesn't matter.

**Dave Jones:** That's now become open circuit and we're now got our 1 ohm in series with the 100 ohm, but it's still high impedance over here, so there's no voltage drop, so we're now sensing directly across the 10 amp 10 milliohm current shunt resistor.

**Dave Jones:** But aha, trap for young players. Remember how in the previous video I said that because this is 10 milliohms, it's a very significant fraction of the PCB trace resistance, it's important to do the four-terminal measurement technique.

**Dave Jones:** What you do is instead of having your 1 ohm like well, let's just get rid of the whole thing, then our 1 ohm resistor, you would actually put that into the tap on the 10 milliohm shunt resistor.

**Dave Jones:** So when you're in the amps range, you're actually tapping that off. But we if you switch to milliamps, for example, you can still use those sense terminals. They're still, you know, really beefy quite terminal, you know, beefy terminals on them usually on the current shunt resistors, then you can actually use that and feed the current back in cuz remember these these are just uh basically just a join in there.

**Dave Jones:** It's just a a solder joint or two traces coming off or whatever that, you know, so you can still feed current through the sense line and that's exactly how I do it on the micro current.

**Dave Jones:** So you can see how now we've actually eliminated our mux here. Beautiful, and that can be fed directly into our amp here. And of course we don't necessarily have to have a mux here.

**Dave Jones:** We could put a a switch in here to actually switch the two ranges. So actually we'll take a quick look cuz there is a little trap in there. So it comes down to whether or not you want to use a mux chip.

**Dave Jones:** You might have a spare mux chip somewhere else in the design. In that case, beauty, you'd probably do it like that. You'd either tap off the input or you'd tap off the output of your times 10 amp here.

**Dave Jones:** But if you want to do it with say a single FET or something like that, a single FET's going to be cheaper than a mux chip. Maybe. Depends. I don't know.

**Dave Jones:** Like a mux chip can be a simple 4051, for example. You know, 4000 series CMOS or the 7400 series equivalent. They're very common in multimeters. If you open up multimeters, you'll find lots of uh 74HC4051s, for example, doing a lot of the switching in there cuz they cost like cents each.

**Dave Jones:** But, if you wanted to get rid of the mux, you could do that and you could just have it as an amplifier like this, for example, straight into your amp, positive negative in, and you could have your resistor, and then that could go into a MOSFET.

**Dave Jones:** I've drawn a JFET there, but whatever. You know, that can go into a switching MOSFET, and then you can go like that, and bingo, Bob's your uncle. You can actually switch in uh whether or not you want your times 10.

**Dave Jones:** So, if this is on equals times 10 gain, because if you actually break this uh circuit, then this resistor's just flapping around in the breeze, it's doing nothing. So, you've just effectively uh created a voltage follower.

**Dave Jones:** You should be familiar with the op-amp basics, and it just becomes a times one voltage follower. So, you can switch in either times one or times 10. But, sometimes there's a trap for young players using this switching in your feedback path here.

**Dave Jones:** Not in this particular case, cuz these resistor values here can be, you know, quite high. They can be, you know, 90k and 10k or uh you know, something like that.

**Dave Jones:** And in which case the on resistance of the MOSFET does not matter. It doesn't actually affect It's pretty insignificant compared to say a 10k there. But, if you were have But, if you had a say a high-speed op-amp or something that used low-value resistors, then you might not want to actually switch this thing with a MOSFET.

**Dave Jones:** So, in this particular case, what you do is you move your MOSFET out of the feedback path and into the path of the input of your op-amp, which is of course high impedance.

**Dave Jones:** Now, I've drawn the MOSFET as a switch here. Could be a mux, a MOSFET, a physical switch, whatever it is. Anyway, so we've moving it out of the path, so it's it doesn't matter what the on resistance of this switch is, there's no current flowing through it because it's into the high impedance input of the op-amp here.

**Dave Jones:** It's outside that path. So now, the gain is purely determined by those two resistors. The MOSFET or switch or mux or whatever, the resistance of that plays no part.

**Dave Jones:** And of course, you would have to have two of them in here like that so that then you could just turn this one off and then turn that one on to get your voltage follower.

**Dave Jones:** Although, you could technically have a high value resistor in there if that wasn't an issue and you wouldn't need your second switch there. So you could switch it off and on.

**Dave Jones:** So anyway, that's nothing really to do with this multimeter. You wouldn't implement it in a multimeter like this, but in some sort of other situation, that can be real handy.

**Dave Jones:** And of course, as I said in the previous video, there it's important that this actually goes down to the tap point on that 10 million ohm shunt resistor. So it's sensing directly across there.

**Dave Jones:** So when you're in the amps mode, that really matters because our 10 million ohm shunt resistor, we're tapping our voltage off there, high impedance, so there's no drop across these, but you could introduce an error due to your ground configuration here.

**Dave Jones:** So it's important to tap it right off that. That's why these current shunt resistors come with four terminals. So there you go, that's kind of groovy. That's how we'd probably implement that in practice if you wanted to go with exactly the same switching and range configuration that we had before.

**Dave Jones:** And that is quite a reasonable solution. Either way would have worked. There's other maybe a couple of other configurations. You can also do switching configurations to do it if you had the range switches available.

**Dave Jones:** You could use those for switching and stuff like that, but that's is a neat solution. I used it in the micro current, works quite well, and you'll find this in a few multimeters as well.

**Dave Jones:** But as I briefly mentioned in the previous video, there's another method to doing this rather than use your times 10 amp. Let's say, cuz these are expensive, these MAX4239s that I'm using in my micro current, these are a couple of bucks a pop.

**Dave Jones:** So, they're actually even like in high volume, in thousands uh volume. So, they're pretty uh expensive little beasts. And also, these fuses are expensive. What if there was a solution where we could get rid of the mux amp because these have limited uh bandwidth as well.

**Dave Jones:** And of course, chopper amps have like a little pole in them at the switching frequency and stuff like that. And uh we won't get into the details, but you know, they might be a little bit uh troublesome.

**Dave Jones:** So, what if we could get away, get rid of the cost of that, get rid of the cost of this extra 600 milliamp or 1 amp fuse up here as well cuz these HRC fuses are a couple of bucks a pop as well, even in volume.

**Dave Jones:** And just get away with the single 11 amp fuse here. And I mentioned MOSFET switching in the previous video. So, that's what we'll take a quick look at now.

**Dave Jones:** And there are actually a couple of just a couple of meters on the market that actually uh do this particular technique that only use the one uh 10 or 11 amp or 15 amp fuse and then do all the switching with MOSFETs.

**Dave Jones:** And once again, if you had the ranges on your range switch, you'd go back to the old days before none of this newfangled auto uh ranging rubbish. If you had a manual range multimeter, you could actually switch to the various ranges on the multimeter and switching, you wouldn't need MOSFET switching.

**Dave Jones:** You'd do it physically on the switch. You couldn't do it for the for the 10 amp range cuz you can't put 10 amps through one of those uh PCB uh wafer switches.

**Dave Jones:** It's not going to work, but you could certainly uh do it in terms of all the other ranges. They can easily handle, in fact, almost every multimeter on the market has the milliamps up to 500 milliamps or whatever the count uh particular count of the meter is going through those wafer PCB range switches.

**Dave Jones:** And a few hundred milliamps like that is fine. Now, one of the problems with MOSFET switching is that as I said before, you have to switch this 10 milliamp shunt resistor and it's like you got 10 or 20 amps momentarily on some multimeters and you've got to switch that.

**Dave Jones:** You can't do it with the wafer range switch, so you've got to do it with a big beefy MOSFET, you know, what like in a big TO220 D squared pack, you know, a decent package rated for 20 or 50 amps or something like that, a big MOSFET.

**Dave Jones:** And there's they're a dime a dozen, right? You can there's a million on the market that can actually do this. So, an N channel big beefy N channel MOSFET like this is required to switch our 10 milliamp shunt resistance and of course we don't want to increase our burden voltage.

**Dave Jones:** So, what you want to do is pick a particular MOSFET that has quite a low RDS on. RDS on is just the drain source resistance. The drain and the source here is just the effective resistance when you switch on that MOSFET hard and you know, a decent one is any jelly bean one is going to be less than 10 milliamps and of course you want it to

**Dave Jones:** be less than 10 milliamps because you you know, and if it's higher than that, then you're more than doubling your shunt resistance here. So, you don't want to do that.

**Dave Jones:** You might pick a couple of milliamps, 5 milliamps might be fine and remember you've also still got the resistance of your HRC fuse up here. So, your MOSFET has to be as low as possible.

**Dave Jones:** Now, just using a single MOSFET like this N channel works just fine. If you put a voltage on here, let's say you put 5 volts or you might only need 3 volts or something like that.

**Dave Jones:** Your multimeter is only working from a couple of batteries. It switches this MOSFET on. I won't explain how MOSFETs work, but it switches on. It acts like a switch.

**Dave Jones:** It's got like 5 or 10 milliamps RDS on. It's on resistance. So, effectively it just works just like a resistor and if the input goes negative cuz you might want to be measuring AC current for example or you you have put the probes in backwards, then it works as a switch.

**Dave Jones:** It doesn't matter. If this voltage on the gate is positive with respect to the source down here, then or VGS is positive, then it's going to switch it on and act like a switch and it works in both directions and everything's hunky-dory.

**Dave Jones:** Now, we could actually put uh shunt resistors in parallel and then switch them like that, but hey, then we get into the same mux problem that we uh did before.

**Dave Jones:** You'd have to switch all the different taps. So, we use our trick before of actually uh cascading them in series like this. So, we'll add our next shunt resistor.

**Dave Jones:** And the goal here is to have a different shunt resistor value for each and every range and we'll switch in the particular shunt resistance. The reason that you want to do that is then we can eliminate the amplifier as we'll see later.

**Dave Jones:** So, yes, we're going to need a different shunt resistor for each one, but MOSFETs are pretty cheap, shunt resistors are pretty cheap, and we might have the space available cuz we've gotten rid of the extra fuse.

**Dave Jones:** We've only got the one 11 amp one up here which is shared between the amps, the milli-amps, and the micro-amps here. So, stick with me. So, we've added in the extra now.

**Dave Jones:** We'll go up a decade because we're going from 5 amps to 500 milli-amps. So, if we had if we're happy with the 50 mV uh drop that we had before, then we'll stick with our 10 milli-ohm uh shunt resistor here.

**Dave Jones:** And our next one will have 50 mV drop as well because then we're using 100 milli-ohms. So, uh but we're using an order of magnitude less current, order of magnitude greater resistance, same voltage drop, Ohm's law.

**Dave Jones:** So, we put that off the tap once again to eliminate any uh issues there in terms of uh sensing. And then we add another MOSFET in up here, but because it's only 500 milli-amps, doesn't need to be nearly as beefy as this one over here.

**Dave Jones:** So, you know, it's still it still has to be reasonably beefy, but not as and not as uh good as this one. In fact, the on resistance can be once again 10 times higher, but yeah, you can use any jelly bean and channel MOSFET in there.

**Dave Jones:** Beauty. So, now if we set this to 0 V, it'll switch off this MOSFET, so that this shunt resistor is disconnected. And if we put our voltage on there, then once again, the gate and the source here, the voltage or the gate actually here and here plus the voltage drop across that and that is going to switch on this MOSFET and bingo, we're using that one.

**Dave Jones:** No worries. And you guessed it, we just continue that ad nauseam. And there you have it. I almost ran out of whiteboard space here, but then you can just cascade these in series these shunt resistors right up to 100 ohm.

**Dave Jones:** So, 10 m 100 m 1 ohm 10 ohm and 100 ohm. And that's what you would use for all your different ranges. So, we'd have to redo this table, but the good thing about this is that the the burden voltage is exactly the same on each particular range depending on the resistor you choose because we're going up by a decade 10 times an order of magnitude each time.

**Dave Jones:** So, if you want to switch on your 500 mA range, well, this becomes 0 V. You'd have 0 V on here. You'd have 0 V on here. And you'd have your 5 V or whatever switching on that MOSFET up there.

**Dave Jones:** And once as I said, these ones down here, these three MOSFETs down here carrying 50 mA or less or five or hundreds of microamps, they can be just nothing MOSFETs.

**Dave Jones:** You know, they don't need any power handling capability at all, really. So, and the RDS on it practically doesn't matter. Any MOSFET's going to do the job. Provided, of course, that the VGS on is suitable here.

**Dave Jones:** And you have to choose a particular MOSFET and I won't go into the details cuz that's a whole separate video of how to choose a MOSFET for something like this that has a particular VGS on voltage that you want and ensures that 0 V on here can genuinely switch all these other ones off.

**Dave Jones:** And you might think, "Aha, Dave, there's a trap for young players here, because we've cascaded them. The VGS here is going to be dependent upon the shunt resistor value, because it's not between here and here, it's between here and here, and it's between here and here, and it's between here and here down here, because you're going to get that drop across the shunt resistor."

**Dave Jones:** But as we said, the maximum shunt resistor and the maximum burden voltage on each range is only 50 mV, regardless of which range you're on, full scale for a 5,000 count multimeter or 50,000 count multimeter, then 50 mV doesn't really add much to the VGS.

**Dave Jones:** So, you might put this to zero, and yeah, this one here is 50 mV higher, but that's the MOSFET is going to be off. It's going TO BE HARD OFF.

**Dave Jones:** SO, that's pretty clever. By simple logic level drive on each one of these MOSFETs, you might want to get a logic level drive MOSFET. You can actually get those.

**Dave Jones:** Um they're just a particular characteristic that works nicely with uh you know, typical 3.3 or 5 V logic levels, then you can just turn on each FET like that, and switch in current shunt resistor.

**Dave Jones:** Beauty. And as before, the cascading nature of these resistors works as a voltage tap. So, you would actually have this going off one single tap into our amplifier, our ADC, or whatever it is, but because our burden voltage is so low, we don't need that times 10 amplifier anymore.

**Dave Jones:** We've actually gotten rid of it. If you're happy with the 50 mV plus the fuse uh plus a tiny bit for the MOSFET as well uh burden voltage, and yeah, you know, that's pretty good.

**Dave Jones:** So, you just have this one tap point, and even if you had this one here turned on, and this one here all the others turned off, and you were measure and you're on your amps range here, it's the the voltage tap is on that four terminal thing, so we've got no loss on our no errors introduced by our PCB.

**Dave Jones:** It goes through this resistor, can't go anywhere else, this MOSFET's off. It's going to be super ridiculously high impedance, so it's effectively open circuit, same with this one, boom, and you've just got a basically 100 ohm just over 110 111.1 ohms going into your amplifier, which is high impedance, so there's no drop across there, so you're tapping off that voltage.

**Dave Jones:** You don't need any switching for the taps. Beauty. All right, so if we redo our table down here like we had in the previous video for our new switching MOSFET configuration, we've got 50 millivolts burden voltage just due to the shunt resistance on each range.

**Dave Jones:** You do the same as before, you just multiply the current by the range resistor, but because it's dropping by order of magnitude changing by an order of magnitude each time, the 50 millivolts remains constant except for the 10 amp range, but let's not worry about that.

**Dave Jones:** Then and then we have our particular burden voltage specified in volts per amps, and then we have the actual burden voltage because that was theoretical. Over here is just theoretical due to the shunt resistor, but of course we have the MOSFET, the RDS on of the MOSFET, plus the 10 or 11 amps or whatever HRC fuse up here.

**Dave Jones:** So it's going to be our 50 millivolt burden voltage, but we have to add on another 50 millivolts due to our HRC fuse up here. It's going to be in the order of 10 milliohms, could be 20, something like that, cold resistance.

**Dave Jones:** It will actually increase when it heats up, but let's not get into those sort of details. We'll just uh you know, ballpark sort of back of the envelope stuff here.

**Dave Jones:** Um 50 millivolts there, plus 25 millivolts for the RDS on. This might be 5 milliohms for example, so 5 milliohms times your 5 amp, 25 millivolts. So your total burden voltage, your true burden voltage across your terminals here on that 5 amp range at lowish currents until it heats up, of course.

**Dave Jones:** The fuse heats up. Talking 125 millivolts, something like that. Still pretty decent. Not a problem on the amps range. Now, it starts to get better and better as you go up the ranges.

**Dave Jones:** Say the 500 milliamp range here, we've still got our 50 millivolts due to our 100 milliohm shunt resistor here, but then, cuz we dropped our current by an order of magnitude, our but our fuse up here is still the same fuse on all these ranges, whereas 50 millivolts before, it's now 5 millivolts.

**Dave Jones:** And then, and let's just assume that we use the same MOSFET in here with the same RDS on, then it's dropped from 25 millivolts to 2.5. So, it starts to become much less significant.

**Dave Jones:** And of course, when you go up a range again, it starts to be less than an order of magnitude different, so we just call it meh. 50 millivolts plus meh, best spec ever.

**Dave Jones:** And that's the the same for all these three ranges up here. So, you can see how this configuration is actually better than the previous one we came up with, cuz it was we only had one range here, which was meh.

**Dave Jones:** Now we've got three, or maybe even four with meh. Beauty. And of course, we don't need the amplifier. We've just got times one amplifier in there, it can go straight into the ADC, the multimeter chipset, whatever.

**Dave Jones:** So, you don't need anything, but you've just got you know, now you've got five MOSFET switching configuration here, but you know, MOSFETs are reasonably cheap, as long as you have the space for the layout, and you are happy to buy the shunt resistors and everything else.

**Dave Jones:** It's actually a pretty good solution. I like it. Now, of course, if you wanted to actually improve, if you weren't happy with the 50 millivolts burden voltage, you could say decrease all these range resistors by an order of magnitude, so this instead of 10 milliohms could become 1 milliohm or maybe 5 milliohms, you know, choose your value.

**Dave Jones:** Doesn't matter, drop them all by the same order, and then you can use your times 10 amp. If you drop this to one miliohm, 110 miliohms, 100 miliohms, one ohm, 10 ohms, then you use it.

**Dave Jones:** Just whack in a times 10 amp, a fixed times 10 amp. You don't have to change any of the gain on it. So, that's an advantage from the previous circuit as well.

**Dave Jones:** But, I know what you're saying, "Dave, you've forgotten all about the protection. Where's the protection? You're going to blow the ass out of this thing if you apply a voltage directly across here." Well, let's have a look at protection.

**Dave Jones:** If you remember the circuit from the previous video, we actually had the a diode bridge across the input for the milliamp ranges only. The amps range kind of takes care of itself.

**Dave Jones:** The amps range is usually a big, beefy sort of nichrome resistance wire shunt in there. So, it's it's not going to melt away anytime soon. And the MOSFET's going to be able to handle itself.

**Dave Jones:** It's big and beefy. You've chosen well. And the HRC fuse is going to blow if you put any voltage across there which exceeds that 10 amp current. It'll just It'll blow.

**Dave Jones:** So, that's no worries. But, what happens when you've got this MOSFET disconnected? You've got zero volts here, and then you apply it. So, this MOSFET switched off, actively switched off, and then you apply a voltage on here, and you can blow the ass out of this range resistor, or this one, or this one, if you apply voltage.

**Dave Jones:** So, we definitely need our back-to-back diode protection, just like we did last time, and I had a diode bridge across here to protect these lower ranges. Now, we could just use the diode bridge again, or back-to-back Schottky's, or whatever, or you know, whatever you wanted to do.

**Dave Jones:** But, aha, we can reduce our bill of materials cost by reusing the same component, and using a property of our big fat beefy MOSFET here we've probably paid, you know, quite a few uh cents for this uh MOSFET here.

**Dave Jones:** We want to get our money's worth out of here. If you know your MOSFETs, which you should, it has a diode in here called a body diode because it's in the body of the construction of the MOSFET.

**Dave Jones:** Won't go into details. I've probably done that in my how a transistor works video perhaps. Anyway, which I'm going to link in down below. If you haven't checked that out, there's a a reverse effectively a reverse body diode in there.

**Dave Jones:** And these are usually pretty beefy in these big MOSFETs like this. So we've already got diode protection in there if we put a positive here and a negative in there.

**Dave Jones:** Even if this MOSFET is switched off, the body diode doesn't switch off. It's always there. It's inherent, usually unwanted, often unwanted characteristic of this particular diode. But in this case, it's actually really good.

**Dave Jones:** It's also good for some other uh configurations as well. But that diode, if you've got a positive one on here, we've still got remember our 10 mΩ shunt resistor here.

**Dave Jones:** It's a big beefy bit of wire. Practically short circuit. It's never going to blow. It's always going to be there. So effectively, we have diode protection across all these other resistors here.

**Dave Jones:** Beauty. Assuming that you put a negative voltage onto your input here. But what happens if you put positive? We want another diode on there. Yeah, we could just whack another suitable diode in there in terms of leakage and everything else um on there.

**Dave Jones:** But hey, we've already got this MOSFET in our bill of materials. Aha. So what we do is we use our same MOSFET that we chose in here and we put it in the reverse direction.

**Dave Jones:** So now we've got the source here, the drain here, whereas before the drain was here and the source was down like this. Put it backwards, swap those two, and then we just join these two gates together like this, and bingo, we have another body diode in there like that back-to-back using the same bill of materials item.

**Dave Jones:** So, there's one less reel we put on our pick and place machine and everything else. That comes down into, you know, just practical considerations for designing uh stuff like this.

**Dave Jones:** So, you would use the same MOSFET, just put it back-to-back, and it doesn't matter if you tie these two gates together, it'll still work exactly uh the same. You can go simulate this or build it up and uh try it out for yourself.

**Dave Jones:** Just put these back-to-back. The The gate this still operates the same. If you put 0 V here, the MOSFET switches off. If you put uh 5 V or 3.3 or whatever uh voltage you want on there, then it should switch on, and it works for both positive and negative currents.

**Dave Jones:** And now, all of these range resistors here are entirely protected due to these body diodes and this big beefy 10 amp current shunt. Winner winner, chicken dinner. So, there you go.

**Dave Jones:** There's another look at how to reduce burden voltage in a typical multimeter. And there's a couple of meters on the market that actually use MOSFET uh switching like this.

**Dave Jones:** A Gossen one in particular and an old Tektronix uh TX 3 uh one as well, which was sold as the Fluke 189 for a brief uh 180 series for a brief uh period of time there.

**Dave Jones:** And it MOSFET switching can actually work quite well. And you reduce your cost. Maybe you'd have to do a whole BOM cost analysis, but you've only got one HRC fuse now.

**Dave Jones:** We had two before. Um but now you've got some beefy MOSFETs in there, but you've saved the cost of your amplifier unless you wanted to decrease all these resistors and use a times 10 amp, but you've gotten rid of the amplifier, you've gotten rid of any uh muxing uh considerations and stuff like that, and it's still protected.

**Dave Jones:** And the good thing is it's good for for user because you're less likely to blow a fuse on this. How many times have you blown your milliamp range fuse on your multimeter?

**Dave Jones:** Come on, put your hand up. Yeah, everyone's done it. It's much harder though to blow your amps range. So, we're using a big beefy 11-amp fuse to actually protect all these other even the fiddly little 50 500 microamp range as well.

**Dave Jones:** And by the way, you could have a 50-microamp range easily without any really any major noise issues apart from the usual uh stuff. You'd still have 50 milliohm full scale.

**Dave Jones:** You'd add another MOSFET and use a 1K resistor up there. Winner. That's a pretty nice configuration. I kind of like this. There's lots of advantages to it. Not a huge number of disadvantages, but you know, this might be maybe a more expensive all up option, which is why a lot of manufacturers very few actually implement this except on real high-end expensive meters.

**Dave Jones:** So, there you go. I hope you learned something interesting here in terms of you know, it's amazing what you can do with such a simple thing. I just want to reduce the burden voltage of a multimeter, and you can go into all sorts of stuff, and then you can get into MOSFET selection, and and then you you know, you get into body diode, and and pulse uh uh

**Dave Jones:** pre- pulse response of your MOSFETs and your body diodes and everything else, and how they withstand any pulse currents coming in, and they can you know, you can really go down the design rabbit hole there, but that's really interesting.

**Dave Jones:** We've got several interesting configurations there over these two videos to you know, reduce the burden voltage in multimeters. And a lot of manufacturers, they just really don't bother. Um you know, you could probably implement it with little or no additional cost.

**Dave Jones:** So, as always, if you like that video, please give it a big thumbs up, cuz that always helps a lot. And if you want to discuss it, links down below to the AV blog forum and all that sort of stuff.

**Dave Jones:** And thank you to all For Patreon uh supporters. If you want to support me, there's a Patreon link at the end of the video usually, and follow me on Twitter and all that sort of jazz, social media stuff, you know.

**Dave Jones:** Anyway, catch you next time.
