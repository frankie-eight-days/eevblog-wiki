---
video_id: xGwnAH_qvto
title: EEVblog 1688 - Constant Current Sources EXPLAINED + DEMO
url: https://www.youtube.com/watch?v=xGwnAH_qvto
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 36, "3": 46, "4": 54, "5": 75, "6": 88, "7": 105, "8": 114, "9": 127, "10": 135, "11": 145, "12": 162, "13": 172, "14": 181, "15": 194, "16": 210, "17": 225, "18": 236, "19": 248, "20": 259, "21": 275, "22": 292, "23": 309, "24": 322, "25": 336, "26": 349, "27": 361, "28": 373, "29": 386, "30": 401, "31": 411, "32": 430, "33": 440, "34": 452, "35": 460, "36": 474, "37": 483, "38": 496, "39": 514, "40": 528, "41": 536, "42": 552, "43": 567, "44": 575, "45": 590, "46": 610, "47": 619, "48": 632, "49": 641, "50": 651, "51": 668, "52": 680, "53": 695, "54": 711, "55": 722, "56": 749, "57": 762, "58": 782, "59": 793, "60": 802, "61": 813, "62": 833, "63": 850, "64": 863, "65": 872, "66": 884, "67": 905, "68": 920, "69": 933, "70": 944, "71": 956, "72": 965, "73": 975, "74": 988, "75": 1000, "76": 1011, "77": 1024, "78": 1040, "79": 1053, "80": 1060, "81": 1076, "82": 1089, "83": 1099, "84": 1113, "85": 1123, "86": 1133, "87": 1145, "88": 1163, "89": 1177, "90": 1191, "91": 1202, "92": 1210, "93": 1220, "94": 1229, "95": 1245, "96": 1260, "97": 1269, "98": 1286, "99": 1298, "100": 1316, "101": 1330, "102": 1344, "103": 1357, "104": 1367, "105": 1379, "106": 1392, "107": 1404, "108": 1412, "109": 1426, "110": 1441, "111": 1448, "112": 1460, "113": 1469, "114": 1480, "115": 1486, "116": 1499, "117": 1511, "118": 1522, "119": 1536, "120": 1553, "121": 1565, "122": 1582, "123": 1595, "124": 1606, "125": 1625, "126": 1637, "127": 1651, "128": 1661, "129": 1677, "130": 1685, "131": 1697, "132": 1712, "133": 1724, "134": 1738, "135": 1750, "136": 1762, "137": 1777, "138": 1790, "139": 1799, "140": 1812, "141": 1825, "142": 1841, "143": 1850, "144": 1871, "145": 1882, "146": 1895, "147": 1909, "148": 1920, "149": 1931, "150": 1944, "151": 1963, "152": 1976, "153": 1990, "154": 2005, "155": 2019, "156": 2038, "157": 2045, "158": 2055}
---

**Dave Jones:** Hi, today we're going to take a look at something very fundamental in electronics and it's the constant current source and kind of looked at current sources before in the DC fundamental series and that was basically voltage and current sources or Thevenin equivalent circuits and Norton equivalent circuits and I'll link it in the video if you haven't seen it.

**Dave Jones:** It's essential DC circuit theory but it's not very practical. It's more like theoretical circuit theory stuff. So I thought we'd take a look at what is a current source from a practical aspect because it's very important.

**Dave Jones:** The bench lab power supply you might have is actually capable of not only being a voltage source but it's also capable of being a constant current source as well.

**Dave Jones:** So let's take a look at it. Now of course I've got Ohm's law up here. We've got the Ohm's law triangle here. So this is very fundamental stuff. So if you haven't remembered your Ohm's law triangle, remember it.

**Dave Jones:** Just a very visual way to remember these basic formulas. Of course you can just just remember V equals I times R and then you can just rearrange the formula to derive the others but in this particular case of the triangle, if you want to solve for voltage for example, you just cover up voltage and it's I times R or if you want to solve for current, you cover up

**Dave Jones:** I and it's voltage divided by R or R is voltage divided by current. Simple. Now you're certainly familiar with a voltage source. It's a circle like this with V in it or it could be drawn as a battery like that for example.

**Dave Jones:** So that's a multi-cell battery. It usually have a positive up there but a V inside a circle is quite common and visual like that and you have the voltage next to it and it shows that the positive is at the top like this and a voltage source is like a potential source of energy and I'll link it in.

**Dave Jones:** If you haven't seen it, I've done a video on what is the difference between voltage, power and energy and that's really important. So watch that one as well after you watch this one.

**Dave Jones:** So if you've got your lab bench power supply there or or your battery or your mains wall socket, for example, just sitting there, that voltage is going to be across that terminal, but it's not doing anything.

**Dave Jones:** No current's going to flow out unless you put a load across it. So, in this particular case, we'll put a load resistor here of 10 ohms. And our voltage source is 10 volts here.

**Dave Jones:** So, we want to solve for how much current will flow in that circuit. I = V on R, which is equal to 10 volts divided by 10 ohms, which is equal to 1 amp.

**Dave Jones:** And that's what's going to flow in our circuit. Simple basic Ohm's law stuff. Now, we come to our current source here. And a current source is drawn as a circle like this with an arrow pointing in the direction of the conventional current flow, not that electron flow rubbish, but we won't go into that.

**Dave Jones:** So, the current is going to flow out of here and then into whatever load you've got over here. We've got the same 10 ohm resistor over here. And of course, it's very simple.

**Dave Jones:** You're already told that it's a 1 amp current source like this. So, what current is going to flow through the circuit? Well, 1 amp, of course, cuz the current's got nowhere else to go.

**Dave Jones:** It's got no other current branches in there. So, it must flow through the resistor like this. And even if you actually get rid of the resistor and short it out like that, you'll still get 1 amp flowing in your circuit.

**Dave Jones:** And that's where the word constant comes in. The current source or constant current source is an active circuit, and it has to be an active circuit. So, what it wants to do is actually push a constant current of 1 amp through whatever load you actually attach to it.

**Dave Jones:** And there's practical limits to this, but in theory, that's what a constant current circuit wants to do. Wants to push a constant current through a circuit instead of providing a voltage and then the current is determined by whatever your load is.

**Dave Jones:** The load will only take as much current as it needs Um, its particular application. But in this case, the constant current source wants to force a current through that circuit by hook or by crook.

**Dave Jones:** Now, in that other video I talked about about a Thevenin equivalent and Norton equivalent circuits, uh, that's what a current source is. You can model a current source, in fact we did in the previous video.

**Dave Jones:** We won't go through it again, but it's called a Norton equivalent, uh, circuit. And a current source is actually modeled as the current source, but with a source resistance across it.

**Dave Jones:** And you can actually do theoretical, uh, conversions between voltage sources and current sources, but watch my previous video for that. That's all great theoretical, it has lots of uses like that, but we don't want to muck around with that because it doesn't really come into the practical aspects of this circuit.

**Dave Jones:** So, we're going to forget all about this Norton equivalent rubbish, and we're going to take a look at the constant current circuit. But, just drawing a current source on its own like this is actually great for theoretical, uh, stuff that you want to, uh, do, but in a practical sense, it's not really telling you the complete story.

**Dave Jones:** And it's not actually a visual representation of how it works. So, we're going to redraw it. A current source or a constant current source, okay, is actually a voltage source followed in series by a constant current circuit.

**Dave Jones:** As I said, it's got to be an active There's some active circuitry in here that turns a voltage source into a constant current source. There's no such thing as like a constant current source on its own without a voltage source.

**Dave Jones:** That just doesn't exist. So, let's redraw our circuit slightly. I've changed, uh, to a 5-V voltage source here just to make it easy on the table over here. We've got our constant current source of 1 amp.

**Dave Jones:** So, as I said, this is active circuitry which we'll look at in a minute. This is active circuitry in here that wants to push, constantly push, 1 amp into whatever load that you apply to your constant current source over here.

**Dave Jones:** So, let's now put a variable resistor load on here. What happens? I've got a table here. So, we'll start out with a 0 ohm load or a direct short straight across your constant current source.

**Dave Jones:** Now, what happens over on a voltage source over here if you've got your battery or your power supply or your mains you know, 240 or 110 socket, if you short that out, what happens?

**Dave Jones:** The magic smoke escapes, right? You're going to probably blow up your power supply. You short out your battery. If you got one of those newfangled lithium batteries with a very low internal resistance, check out my other videos for that, then massive amounts of current are going to flow.

**Dave Jones:** In theory, an infinite amount of current because current equals voltage divided by resistance. If resistance is zero, even if you have 1 volt here or 0.1 volts or 1 microvolt here, divided by zero, that's an infinite amount of current.

**Dave Jones:** In theory, it's limited by the internal resistance of your power supply, which we won't go into the that, but suffice it to say, right? You short out your power supply, very bad idea.

**Dave Jones:** But constant current sources, they love to be shorted out. That is the best possible load for a constant current source. So, if this constant current source circuitry is designed for a constant current of 1 amp, then if you short out these terminals or have a resistance of 0 ohms, you're going to get 1 amp flowing through there.

**Dave Jones:** So, let's add another table here, which is the voltage across your load resistor OR VR HERE. WHAT happens at 0 ohms? You've got 1 amp flowing through 0 ohms.

**Dave Jones:** 1 * 0 is 0, so there's no voltage across the load, but if you've got, let's say tweak our pot here, tongue at the right angle, 1 ohm here, then you're going to have 1 amp flowing through 1 ohm.

**Dave Jones:** Use your Ohm's law, you're going to have 1 volt across there. And we've got a 5-volt supply. No worries. You might be able to see where this is going now.

**Dave Jones:** We tweak our pot again at 2 ohms, okay? Then our voltage across here is 2 volts. And likewise, 3 volts at 3 ohms resistance cuz the 1 amp is constant, remember?

**Dave Jones:** Unlike over here, it's constantly pushing it through there. And then you'll have 4 volts. And then if you finally tweak it to 5 ohms here, 5 ohms * 1 amp is 5 volts.

**Dave Jones:** But what happens at this point? You're going to come a gutter. So, remember how I said before that a constant current source always has to be paired with a voltage source.

**Dave Jones:** It's useless without it. It doesn't exist on its own. And that voltage source, now we have to introduce another term called compliance voltage. And the voltage source effectively behind making this constant current circuit work is called the compliance voltage.

**Dave Jones:** You can think of it as the power supply voltage over here. And you can actually take a voltage source like this and put on external circuitry, and we'll show this later, and then convert your voltage source into a constant current source.

**Dave Jones:** That's no worries whatsoever. In fact, that's what a constant current source is. It's a voltage source with constant current circuitry. But that's a key term to remember, compliance voltage.

**Dave Jones:** If you've only got 5 volts maximum, maximum compliance voltage of 5 volts, you're not going to get any more voltage drop across your resistor here. The constant current circuit isn't some magic voltage multiplier that's going to multiply the voltage across your load here.

**Dave Jones:** It doesn't work like that. It's going to stop suddenly when it gets to your maximum compliance voltage of 5 volts. We're going to assume that there's no voltage drop loss in here, and that's what it's capable of actually delivering across here.

**Dave Jones:** So, if we follow our chart, we would have expected 6 volts across here, constant current circuit. But our constant current circuit can no longer work as a constant current circuit.

**Dave Jones:** It just doesn't have the compliance voltage, doesn't have the capability to push that current through the circuit anymore. So, what happens? Well, our voltage over here stays at 5 V, the maximum compliance voltage.

**Dave Jones:** In fact, it doesn't matter whether you go 7 ohms, 8 ohms, 9 ohms, it stays 5 5 5 until the cows come home. In fact, you can break this circuit and if you've got an open circuit, you're only going to get your 5 V and with zero current flowing cuz you can't push current through an open circuit.

**Dave Jones:** Your circuit's broken. So, all you're going to be left with left me holding the bag at 5 V across there. Bingo, your constant current circuit is no longer a constant current circuit.

**Dave Jones:** May as well not even be there. It's just a voltage supply. But, as you lower the resistance back down and you reconnect like this, once it gets down to at least 5 ohms or less, bingo, it becomes a constant current circuit again.

**Dave Jones:** Magic. So, how much current do you actually get flowing through here? Uh well, you know that you've got that fixed 5 V across there. So, you simply use Ohm's law.

**Dave Jones:** 5 V divided by 6 ohms in this case. Get your calculator out. That's 0.83 um amps flowing through your circuit like that. Once it ends for 7 ohms, it's 0.71.

**Dave Jones:** 8 ohms, 0.625. 9 ohms, 0.555 555 5 spotted and 10 ohms, it's going to be uh half an amp there. And so on and so on until you get that open circuit as I said and then no current's going to flow and but you're still going to get your 5 V across there.

**Dave Jones:** Okay, so that's fantastic, you say, but what use is a constant current circuit? Why would you want to push a constant current through a through a load? What sort of load would need this sort of thing?

**Dave Jones:** Well, there's countless applications. Just a few of them uh LEDs, for example. Um LEDs are actually cut essentially current driven devices. If you look up a LED uh data sheet, for example, it will specify a maximum or you know, an operational current.

**Dave Jones:** Say 20 milliamps for a standard LED, a high-power LED might be 1 amp or something like that. So, LEDs are typically your LED lighting that I've got it here around me at the moment is driven by a constant current circuit cuz you want to push a known constant current through that circuit, for example.

**Dave Jones:** Laser diodes are another thing, you know, you don't want to push too much current through a laser diode, you can release the magic smoke. Battery charging, for example, I've done videos on specific lithium-ion battery charging.

**Dave Jones:** A lot of batteries will have a not only a voltage charging profile, but they'll have a constant current charging profile where it might start out at constant current and but the battery itself effectively changes its electrochemistry or its electroresistance there and it actually once it actually gets full at that constant current, it turns from constant current mode from here into that constant voltage mode that we saw over

**Dave Jones:** there. For a typical lithium-ion cell, for example, you don't want to go above 4.2 volts, but you don't just want to whack 4.2 volts across it because then if it's got low charge, it can put massive amounts of current through, which can damage the battery.

**Dave Jones:** That's why you have a voltage, you'd have 4.2 volts in series with a constant current driver. So, you can use constant current mode, then it'll automatically, once it reaches a certain resistance or a certain level in your battery that's equivalent to a resistance, it'll switch from current mode into voltage mode automatically.

**Dave Jones:** Magic. Sensors are another one, for example, you might have a photodiode, things like that. Welding stuff, if you want to have like a nice controlled weld, you're doing that with current.

**Dave Jones:** So, a constant current can help out there. Any sort of electroplating process or something like that, once again, you want it to be controlled. So, you might want to push a constant current through there.

**Dave Jones:** And reference circuits, and we can take a look at that in a minute. For example, if you've got a a shunt uh Zener reference voltage, you want to put a known current through that sort of thing.

**Dave Jones:** So, yeah, there's a ton. Leave them in the comments down below other applications for constant current circuits, but there's a ton of them. So, just think of it as circuitry that wants to push that current through that circuit until it reaches a point where it's you exceed the compliance voltage and it just sorry, can't do it anymore.

**Dave Jones:** I give up. I can't push enough current through there. But constant current circuits just love that short circuit. Now, I just spent what? 10 minutes trying to convince you to think about constant current sources as a circuit which pushes out a constant current into a load.

**Dave Jones:** And well, that's true from a certain point of view. And you can actually think of a constant current source. In fact, you probably know a constant current source as a current limiter.

**Dave Jones:** You're familiar with your bench power supply. It's got a voltage knob and it's got a current knob. And you think of that current knob as a current limiter. I.E.

**Dave Jones:** when you're powering your circuit, if something magic smoke escapes in your circuit and it shorts out or does whatever, then the power supply will limit the current going into the load.

**Dave Jones:** And that's how your power supply works. So, your power supply basically contains a current limiting circuit or you can think of it as a constant current circuit. And you can as I said right at the start of the video, you can use your lab power supply as a constant current power supply, which we'll show you in a minute on the bench.

**Dave Jones:** But basically, your power supply contains your voltage source, you know, you turn your knob and you can dial in your voltage, but it also contains basically a what's called a pass transistor or a series pass transistor because it's in series with the output.

**Dave Jones:** Here's the output terminals on your power supply, but it contains a pass transistor which will be used to limit the current going to the output. And usually when you're using a power supply in normal voltage mode, then that's what it's doing.

**Dave Jones:** It's limiting the current. It's working as a current limiter just in case you goof up the circuit, you accidentally short out something cuz you you weren't paying attention when you were probing or something like that.

**Dave Jones:** It can really save your bacon. That's great. But this circuitry inside here is actually a constant current circuit. Please excuse the crude DIY model, didn't have time to build it the scale or to paint it.

**Dave Jones:** You've got this series pass transistor here cuz it passes the current from an input to an output. That's why it's called a pass transistor. That's just some industry parlance.

**Dave Jones:** And then there's a very low value resistive current shunt in here in series with your output. It might be .1 ohm or 10 milliohms or something like that, like really low.

**Dave Jones:** Because in normal operation you don't want it to dissipate much power. Then across that shunt resistor you've got an op amp or basically a differential amplifier that measures the voltage across that current shunt resistor.

**Dave Jones:** And then into that circuitry, that op amp circuitry there, we won't go into details about how it exactly works cuz there's many ways to skin this cat. But suffice it to say you feed in a reference voltage.

**Dave Jones:** In this particular case I've shown it coming from a zener. But inside your power supply that voltage reference is actually your current knob which dial in to your set current.

**Dave Jones:** And it's calibrated so that the set current is actually a voltage proportional to that current shunt. So if you've got a 1 ohm current shunt and you've got a 1 volt reference voltage, this op amp circuit, you can see it's a loop here.

**Dave Jones:** The op amp output is controlling this pass transistor to give you a certain voltage drop across this shunt resistor set by the reference voltage. So if your reference voltage is 1-V, your current shunt is 1-Ω, then you're going to have 1-A flowing through the output here.

**Dave Jones:** If you short it out or have a low enough load value, then you bingo, you've got a constant current circuit. And that's exactly what your power supply is doing.

**Dave Jones:** So, you can think of it as either a current limiter or depending on how you want to use it and how you want to look at it, it's a constant current generator.

**Dave Jones:** So, the formula's really easy. Your output constant current is equal to the voltage reference divided by the current shunt resistor. And this op-amp, due to op-amp action (I've done op-amp videos), it keeps drives the base of this transistor.

**Dave Jones:** This is NPN in this particular configuration cuz the arrow's pointing that way, but it can be PNP. And as I said, there's many ways to skin this cat. You can do this many different ways, but this is just a very typical basic example.

**Dave Jones:** And it does what the op-amp does whatever it can to drive that transistor to keep 1-V across that shunt resistor. And if you've got 1-V across that shunt resistor, you must have 1-A going out.

**Dave Jones:** But like before, what happens if you've got no load connected to your power supply? Well, this thing is not magic. It can't just boost the voltage. You're basically going to get out your set voltage here.

**Dave Jones:** I know there's going to be loss in this voltage drop across the pass transistor here and the current shunt, but you have to go into the circuit details. The power supply is not dumb though.

**Dave Jones:** It's just not putting in a voltage here. It's actually tapping off and sensing the voltage on the output like that. So, it's actually sort of like feeding back from the output.

**Dave Jones:** So, if you set your volt power supply to 10-V, yeah, you'll get that 10-V compliance voltage on the output. Now, you don't think of the term compliance voltage when you're talking about a power supply because you're using it in voltage mode operation.

**Dave Jones:** But when you're in current limiting mode, yeah, that compliance voltage, that's what it becomes. You can think of it as a compliance voltage. And some real-world example circuits, uh a cur- a constant current circuit, you can use the TL431, which is just a uh voltage reference um shunt diode.

**Dave Jones:** Basically, you can use it as a shunt voltage reference, but if you put it in series you know, effectively in series like this with a shunt resistor and a pass transistor, um it's actually got a reference voltage of 2 and 1/2 V.

**Dave Jones:** Uh so, it's 2 and 1/2 V divided by that shunt resistor value, and you'll get a constant current out. It's a classic jelly bean component, it's been around forever, costs nothing, and you can use that to generate a constant current that might drive some LEDs or something like that, whatever.

**Dave Jones:** And the formula is 2.5 V divided by RS. And there's an additional term in here, IK, which is actually the cathode uh current. Yes, I know cathode starts with the C, but they use K.

**Dave Jones:** Anyway, let's not go there. Um so, yeah, there's a little tiny bit of current, but usually, you know, it's pretty small, so you can often ignore that uh term there.

**Dave Jones:** But the TL431 is not just a Zener diode like it appears here. Here's the internal circuit for it. It's actually got an op-amp in there. So, it's just working exactly like up here.

**Dave Jones:** It's just using an actual uh part. So, um yeah, classic jelly bean uh component circuit there. Here's an even more classic jelly bean circuit, the LM317. You should be familiar with this.

**Dave Jones:** It's the classic adjustable voltage regulator. But you can actually use it as a constant current source. You just put it in series like this, input output. Well, that normally you have uh some resistors on the output which tap back, feed into the adjust pin, and it's used as constant voltage.

**Dave Jones:** But if you put a shunt resistor in there, and you tie the adjust line to the output, bingo, you've got a constant current source like this, or a current limiter, depending on which way you want to look at it.

**Dave Jones:** And the formula is simple. It's just uh the internal reference voltage, cuz the LM317 has an internal reference voltage of 1.25 volts. So, it's 1.25 volts divided by the shunt resistor.

**Dave Jones:** And as before, there's a little bit of adjustment current, which flows out of the adjust pin there, which is a constant current source in its own sense. Here's the internal block diagram of the LM317, and you'll see that it's actually got a little current source, which actually feeds a tiny amount of current out the adjust pin here.

**Dave Jones:** Um but generally, that's you know, it's like like 100 microamps or something. So, generally, uh you know, if you're talking about an amp or 100 milliamps or something, you can generally ignore that term.

**Dave Jones:** So, it's simply V on R gives you your current source. Beauty. Up until now, we've been talking about constant current sources. It's literally in the name. It sources current out of the positive pin of your power supply or circuit or whatever it is into a uh load.

**Dave Jones:** But uh you can also do constant current as what's called a low-side constant current sink. And if you've watched my do-it-yourself constant current load video, uh lots of people have built up my constant current uh load circuit.

**Dave Jones:** This is just exactly that, the circuit from my constant current load here. So, you can actually do it either way. You can do it what's called the high-side here because it's up on the high, the positive uh side of your uh voltage source, basically.

**Dave Jones:** So, it's called a high-side current source. And this is uh called a low-side current sink because it's not really sourcing anymore. It's really doing it as a sink because it's down the bottom.

**Dave Jones:** Here's your load here. We've got a you know, a string of LEDs through it. Bloody hell. Where were we? Okay, we've got a LED string here. So, this is our load.

**Dave Jones:** So, our load is actually connected directly across the uh voltage source here, our power supply, and the current um sinking because it's sinking, it's just on the low side.

**Dave Jones:** It's These are just industry terms you should get you used to. So, the load is actually on the high side here and our load is a bunch of series LEDs like this that we want to drive at a constant current.

**Dave Jones:** Could be 20 milliamps, could be an amp, whatever. So, it works exactly the same way as it does up on the high side here. We've got our op amp driving a transistor which can be like a bipolar transistor here.

**Dave Jones:** It can be a MOSFET or whatever. I've drawn it as an NPN bipolar transistor, but you do you. And then we've got our reference voltage here. It can be fixed or it can be adjustable.

**Dave Jones:** And if you know your op amp rules, you should if you see my op amp video, then the op amp does whatever it needs to do using op amp action to make these two input terminals, the non-inverting and the inverting, the same.

**Dave Jones:** So, bingo, you're going to get this voltage reference on this non-inverting pin. It's going to be on this It'll drive the transistor and do whatever it needs to to make this non-inverting pin equal to the the voltage reference and you get the voltage reference directly across RS.

**Dave Jones:** So, your current here is equal to your voltage reference divided by your shunt resistor. Easy. Exactly the same as up here except it's on the low side. Got it?

**Dave Jones:** You'll see this all the time. This is super common for doing LED drivers and things like that. So, let's now go to the bench and just have a play around with some stuff.

**Dave Jones:** All right, what we've got here is a standard lab bench power supply and of course you set the voltage and the current. This one doesn't have dual knobs. You have to swap between them, but you know, that's the modern interface.

**Dave Jones:** And you can see that we've got the displayed voltage, current, and power output power here. And we've also got the set voltage and the set current. So, you're setting a current limit there.

**Dave Jones:** It's currently set to 0.5 amps and we haven't got any load hooked on at the moment. They're totally disconnected. So, we're going to read our 5 volts like that.

**Dave Jones:** It's drawing zero current cuz there's no load on there, okay? And down the bottom here, you'll notice an LED. CV is constant voltage and CC, it'll turn red when it's in constant current mode.

**Dave Jones:** That's what CC stands for uh for. This is a combined LED, but often you'll have like a separate LEDs or maybe an indicator on the uh screen itself. So, what I've got hooked up to here is a constant current electronic load.

**Dave Jones:** Just as we showed on the whiteboard before, this is a constant current sink or a constant current load. So, it's going to do sink uh current, but you can think of it as just a resistor.

**Dave Jones:** It makes uh no difference, but it's just convenient because we can dial in the current from uh 0 to 2 amps here. And because we've got it set to 0.5 amps here, watch what happens when we take it to 0.5 amps here.

**Dave Jones:** Watch the LED down the bottom. Okay, we've got 100 milliamps there. No worries, it's still in constant voltage mode. But, what happens when we get to 0.5 amps? You can either watch the old-school analog meter or you can watch the uh same digital display up here.

**Dave Jones:** Once we get to Oh, I'm just on just on 0.5 amps, it's still constant voltage. But, if we go just a little bit more, Mav, um uh yeah, it switched to constant current mode.

**Dave Jones:** And you'll notice that we cannot draw any more current from the power supply. This is trying to. In fact, we can take this out and we can actually SHORT OUT OUR POWER SUPPLY like that, but it's still only going to limit it to 0.5 amps there because that is the constant current limiting mode.

**Dave Jones:** But, your power supply is actually a constant current generator as well because it's generating it's generating current out of the output here into your load, which happens to be a short circuit.

**Dave Jones:** We can just dial in our current that we want, 1.3 amps. So, it's actually a constant current generator. You don't think of it as that because you think it's a current limiting, and it is.

**Dave Jones:** That's its most useful purpose because most of the time you're powering uh your circuit under test in constant voltage mode. You only think about constant current mode as a current limiting you know fail safe thing when Murphy's going to bite you in the ass today and magic smoke is going to escape.

**Dave Jones:** This will protect your circuit under test. So if you know your circuit's going to draw 1 amp for example, then you might dial in say 1.1 like that. But you got to be aware of peak currents and things like that as well.

**Dave Jones:** But anyway, yeah, it's a protection thing. But it's also a constant current generator. And we're in constant voltage mode, you output 5 volts, but watch the voltage display when you enter constant current mode, it's going to drop to actually look look at that.

**Dave Jones:** It's winding down cuz this is an electronic load, it's not a resistor. It'd be fixed if it was a resistor, but you saw it wind down there to actually match to give the compliance voltage dropped.

**Dave Jones:** The voltage will match using Ohm's law V equals I times R. So depending on your resistance in your load, it'll match it to meet. It'll drop that compliance voltage to meet whatever your load requires to give you that 1 amp constant current.

**Dave Jones:** So if we try and draw even a short circuit like that, nope, it's still only going to be an amp and then we're down in what? 70 millivolts there?

**Dave Jones:** Now check this out. This is a Keithley 225 current source and what is this magic mysterious bit of kit I've got here in the lab? It magically generates current.

**Dave Jones:** Well, it's actually absolutely no different to a regular power supply over here. Look, it's got a voltage knob except it's called voltage compliance. It'll actually go anywhere from 10 volts all the way up to 100 volts there.

**Dave Jones:** So it's effectively a 100 volt DC power supply and you can dial in the current here. The only difference is it's designed for really low currents, milliamps. So it'll only go to 10 milliamps maximum.

**Dave Jones:** This actually changes the This is the decimal point. So, 1.00 mA there. You can see it'll do microamps, three ranges of microamps, and then nanoamps, and like it can go down to 1 nanoamp.

**Dave Jones:** But, it's actually really just a power supply exactly like this one next to it, except this is designed for large powers and large currents and, you know, things like that.

**Dave Jones:** But, this is designed to generate low current. But, you can see that we've only got two decimal places on the current there. So, the smallest current I can actually set there is what 10 mA.

**Dave Jones:** No, yeah, 10 mA. There you go. Whereas this one I can set down to like nanoamps. So, I've got the output of my current source or power supply over here hooked up through in series through the current meter here, which is the 786.

**Dave Jones:** The 121G W is measuring the output voltage over there or the compliance voltage. And then I've got my decade resistor box up here. It's currently set to 0 ohms, so it's actually shorted out.

**Dave Jones:** So, let me actually put in 1 K, so it's now a 1 K resistor. And you can see that the voltage actually stepped up there because it's no longer a short.

**Dave Jones:** So, get your confuser out and calculate Ohm's law for the 1 mA flowing what resistance it needs to throw and flow through to generate that compliance voltage. I've got the compliance voltage set.

**Dave Jones:** It's actually set to 9 V over here. Okay, that's as low as it actually goes. So, look what happens, right? At 8 K, it's fine. We're measuring precisely 1 mA because this is a precision current source.

**Dave Jones:** And if I go to 9, oopsie, we're right on the limit there. So, we've gone from constant current mode all this time. Okay, even though this doesn't have an indicator saying constant current constant voltage, now we've actually gone into constant voltage mode.

**Dave Jones:** I I can adjust the resistor to 20 K, for example, and the current is just going to drop because it's just working as a voltage source now. You can see.

**Dave Jones:** But, basically, it is absolutely no different to a lab power supply. Your lab power supply is a constant current source. Just depends on the way you use it, uh your application and what load you're whether you want to put a constant current in the load or whether you're not you've got a constant voltage load, which most of the time.

**Dave Jones:** What is one of the classic applications for a constant current driver? Well, I mentioned it before, an LED strip. And I've got one. It's pretty long. Salvaged it out of an old uh dumpster LCD uh TV.

**Dave Jones:** But, there you go. Um and these have quite significant voltage drop for each LED. But, they're essentially current uh driven devices. They need current to actually work. So, I've got them hooked up here, and I've got a compliance voltage of 9 V uh dialed in here.

**Dave Jones:** But, you can see that uh they're not on. There's no current going through. Even though I've got one uh milliamp set here, this is a source. It's supposed to, you know, force out that 1 milliamp of current out of here.

**Dave Jones:** Well, where is it? It's not there because these uh the threshold voltage of these uh LEDs has not been met yet. So, we have to dial up our compliance voltage here.

**Dave Jones:** Look, we're still We're at 33 V now. That's still not enough to get any current. 33, 37 37 Wait. Oh, look. Current's starting to go up there. There you go.

**Dave Jones:** Tiny little bit at about 43 V there, compliance voltage, and bingo, the LEDs are now lit. Hopefully, you can see that. Trust me. Studio lights The studio lights there, you can see it.

**Dave Jones:** We're drawing our 1 milliamp there, and the LEDs are lit up nicely. And if we increase our compliance voltage even more, I've got that set to a maximum of a V over there, but it's going to stop at 45 volts because that is the voltage drop of all these LEDs.

**Dave Jones:** I've got 2 4 6 8 9 LEDs. I calculate the voltage drop on each LED there. It's pretty high for your 45 volts for almost 46 volts there, but we're going to limit it to 1 milliamp.

**Dave Jones:** So, I can just turn up the current 2 milliamps, 3 milliamps, etc. And the LEDs are just going to get brighter and brighter. Cool, huh? So, we're operating in constant current mode because we've got a load, these LEDs, that are essentially current driven devices.

**Dave Jones:** You have to pass a current through them, and whatever voltage drop across them, the 46 volts, that's just what happens to drop due to the characteristics of these LEDs, but we don't hook a 46-volt power supply up to them.

**Dave Jones:** If we did that with no current limiting resistor, try that at home. Yeah, you'll release the magic smoke from your LEDs. That's why you have current limiting in your power supply here, and also you would use a current source to drive LEDs.

**Dave Jones:** So, it doesn't matter what the mains voltage is. You can plug it into 110 volt mains if you Yanks, you know, 230 volts here in Australia or 245 as I've got here in the lab, and my LED lights here still going to be the same brightness because they've got a constant current driver.

**Dave Jones:** Hope you enjoyed that video. I found it useful. If you did, please give it a big thumbs up. As always, discuss down below in the comments or over on the EEVblog forum.

**Dave Jones:** That's where all the action's happening. And don't forget to check out the EEVblog.store cuz that's kind of what pays for all this. Don't make much money on YouTube these days.

**Dave Jones:** Let me tell you. Catch you next time.
