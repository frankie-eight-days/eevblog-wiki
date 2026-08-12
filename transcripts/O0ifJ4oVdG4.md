---
video_id: O0ifJ4oVdG4
title: EEVblog #908 - Zener Diodes
url: https://www.youtube.com/watch?v=O0ifJ4oVdG4
source: youtube-asr
timestamps: {"0": 1, "1": 9, "2": 27, "3": 42, "4": 67, "5": 78, "6": 89, "7": 103, "8": 116, "9": 130, "10": 144, "11": 155, "12": 168, "13": 185, "14": 197, "15": 221, "16": 232, "17": 245, "18": 261, "19": 272, "20": 288, "21": 305, "22": 317, "23": 333, "24": 355, "25": 368, "26": 389, "27": 401, "28": 412, "29": 423, "30": 439, "31": 453, "32": 463, "33": 482, "34": 495, "35": 506, "36": 516, "37": 537, "38": 551, "39": 565, "40": 579, "41": 591, "42": 606, "43": 618, "44": 629, "45": 640, "46": 649, "47": 661, "48": 675, "49": 687, "50": 701, "51": 714, "52": 723, "53": 739, "54": 758, "55": 773, "56": 788, "57": 799, "58": 814, "59": 832, "60": 839, "61": 854, "62": 870, "63": 883, "64": 895, "65": 905, "66": 921, "67": 933, "68": 941, "69": 952, "70": 965, "71": 978, "72": 990, "73": 1008, "74": 1032, "75": 1049, "76": 1069, "77": 1082, "78": 1092, "79": 1107, "80": 1122, "81": 1132, "82": 1141, "83": 1162, "84": 1175, "85": 1193, "86": 1207, "87": 1218, "88": 1229, "89": 1241, "90": 1250, "91": 1267, "92": 1283, "93": 1297, "94": 1309, "95": 1321, "96": 1339, "97": 1353, "98": 1364, "99": 1372, "100": 1394, "101": 1411, "102": 1428, "103": 1441, "104": 1452, "105": 1464, "106": 1488, "107": 1508, "108": 1518, "109": 1536, "110": 1546, "111": 1561, "112": 1578, "113": 1589, "114": 1599, "115": 1616, "116": 1627, "117": 1648, "118": 1661, "119": 1677, "120": 1690, "121": 1700, "122": 1710, "123": 1727, "124": 1741, "125": 1755, "126": 1770, "127": 1780, "128": 1793, "129": 1810, "130": 1818, "131": 1830, "132": 1840, "133": 1847, "134": 1857, "135": 1874, "136": 1884, "137": 1895, "138": 1905, "139": 1916, "140": 1927, "141": 1945}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at one of the most fundamental components in electronics, the Zener diode. Let's take a look at it.

**Dave Jones:** Now, you're no doubt familiar with the regular silicon diode and we've got our Schottky diode as well. Same thing for the purposes of today's talk, but we're going to look at the differences between a regular diode and a Zener diode and we're going to take a look at how the Zener diode is useful in a bunch of different applications.

**Dave Jones:** Now, your regular diode like this, you're no doubt familiar that it conducts current in one direction only. It only allows current to flow through, hence why it's got that sort of arrow shape pointing in the direction of the conventional current flow.

**Dave Jones:** And if you try and reverse bias it, it doesn't allow current to flow back up. But the Zener diode is a bit different. It works exactly like a regular diode and allows current to flow through like that and it has the same voltage drop, you know, 0.6 volts to a volt or thereabouts, but it has a special property where it also allows current to flow in the other direction.

**Dave Jones:** You might say, "What use is that? The whole point of a diode is that it blocks current going in one direction." Well, there's something very interesting about the Zener that makes it useful.

**Dave Jones:** Let's take a look. Now, you should be familiar with the characteristic curve of a regular diode like this. Schottky diode is basically exactly the same except it has a smaller voltage drop.

**Dave Jones:** And as you can see on this characteristic curve here, also called an IV curve because it's I versus V, current versus voltage. You can see that until you get to about 0.6 volts, no current will basically flow through this.

**Dave Jones:** So, if you've got less than 0.6 volts on the diode or roughly, it won't conduct anything. It won't allow current to flow. But once it gets above that what's called the knee the diode knee here, then it start it can start to conduct current.

**Dave Jones:** Once you get above about 0.6 volts, temperature and device dependent and current dependent, it will allow current to flow. That's it. And if you reverse bias and put a negative voltage on, i.e.

**Dave Jones:** you go on this side of the curve here, no current flows. It just stays flat like that. Easy. Now, a Zener diode works exactly the same as a regular diode when you forward bias it, when you have current going down like this.

**Dave Jones:** And you get exactly the same characteristic response at the knee starts at about 0.6 volts and it starts to conduct current. But in the negative direction, when you try and put a negative voltage on here, i.e.

**Dave Jones:** you put the positive here and the negative here and you try and make current flow in the reverse direction, a regular diode just won't conduct anything. But we'll talk about that later.

**Dave Jones:** But a Zener diode, when you reverse bias it and try and make current flow in the reverse direction, it will do nothing for a while. It'll do nothing, but then it'll actually start conducting like a diode in the opposite direction.

**Dave Jones:** Weird. And the voltage that it typically does that is called the Zener voltage, Vz, or it might be called the Zener knee voltage or something like that. So, now we can start to annotate our characteristic graph here with some industry terminology.

**Dave Jones:** Up here we've got the forward characteristic, that is the characteristic of the Zener diode in the forward current direction, like that with the forward voltage. And naturally, we've got the reverse characteristic down here, which shows what happens when you try and push current in the other direction and you have reverse voltage on it with the Zener breakdown voltage.

**Dave Jones:** Now, I actually hinted before that regular diodes may have something a bit unusual with them, too. They actually act like Zener diodes, kind of. And so do Schottky diodes as well.

**Dave Jones:** We'll loop him in, lump him in the same thing. You know how I said when you reverse the voltage on them, they don't allow current to flow. That's what you typically think of a diode, and that's typically how it kind of works in practice.

**Dave Jones:** But ultimately, you get to a breakdown voltage. We'll call that VB here, and at that voltage, it's actually going to do a very similar thing. It's going to break down, or what's called avalanche in the other direction, very similar to a Zener diode.

**Dave Jones:** So you might go, "Dave, what's the difference between a Zener diode and a regular diode?" Well, regular diodes are not designed to work down in this reverse characteristic region.

**Dave Jones:** They're uncontrolled, they're horrible, they drift with temperature, and all sorts of They're not designed to work down here. Zener diodes have been specifically manufactured, specifically doped to actually have a quite a reasonable, controlled characteristic in the reverse breakdown region.

**Dave Jones:** Regular diodes and Schottky got diodes don't. So that's why you use Zener diodes and as opposed to regular diodes in the applications we'll see. But just be aware that regular diodes can do it as well, and that will be the maximum reverse voltage of the diode typically before it breaks down.

**Dave Jones:** And the other thing with diode breakdown voltages is it's usually very high. For example, a 1N914 diode, 4148, it might break down at, you know, 70 or 90 volts or something like that.

**Dave Jones:** You know, really not a very usable voltage in practical circuits. So it's effectively it stops current flowing in the other direction direction for most practical voltages. You know, a 1N4007 breaks down at 1,000 volts, for example.

**Dave Jones:** You know, so really they're not of practical value in that negative region. But Zener diodes have been specifically manufactured and doped to actually work at very usable and very useful breakdown voltages, anywhere from 2 volts up to 30 volts or something like that or even higher and you can use that low and controlled Zener breakdown voltage for useful circuit applications.

**Dave Jones:** Beauty. Now, just to completely mess with your mind, sorry, but no explanation on Zener diodes would be complete without actually at least mentioning this. There are two different types of Zener breakdown.

**Dave Jones:** The red one which we saw here is called avalanche breakdown and that's what happens at high voltages in regular diodes, but there's also another type of Zener breakdown actually called Zener breakdown and it's actually this effect, the Zener effect, the Zener breakdown where Zener diodes get their name from.

**Dave Jones:** The person who founded it, physicist Clarence Zener, way back before you were born. Now, I won't go into the details of doping the PN regions and all the physics involved in actually manufacturing diodes.

**Dave Jones:** It's outside the scope of this thing, really. I'm sure you can Google it if you want to find out more, but just be aware that the Zener effect, the Zener breakdown is actually quantum tunneling.

**Dave Jones:** So, quantum physics is involved in this sort of thing, hence why it was found by a physicist. Anyway, the Zener breakdown occurs at roughly about 5 volts or below.

**Dave Jones:** Anything above it roughly 5 volts is going to be a different effect, avalanche breakdown. So, they're two physically different phenomenon happening inside the Zener diode or both or a combination of both could be happening if it's near to that sort of 5-volt region.

**Dave Jones:** So, you know, like a a 12-volt Zener diode will definitely be working as an avalanche breakdown and a 2.5-volt Zener diode would definitely be working in the Zener, using the Zener effect, it's called.

**Dave Jones:** But, you don't need to know that and most people just go the Zener effect even though they're actually might be talking about an actual avalanche effect instead of a Zener effect.

**Dave Jones:** If you're talking about Zener diodes, it's a Zener breakdown voltage. It doesn't matter which voltage it occurs at, it's the Zener effect. And just a further clarification on the terminology here, the reverse breakdown voltage, I put VB before cuz I was talking about breakdown, but in the data sheet you'll find that as VR for regular diodes.

**Dave Jones:** So, just stick with VR. Now, let's take a look at a typical implementation of a Zener diode here, and we're using the reverse characteristic. Cuz if we use the forward characteristic, you might as well just use a diode.

**Dave Jones:** It's just a regular diode. So, that's why in a circuit like this, oh, I should put that. That's positive and that's negative there. So, you use it in the reverse bias configuration.

**Dave Jones:** So, we're looking at the Zener breakdown voltage. And now, hopefully, you can see why the Zener symbol is as it is. Look how it kinks up there and kinks down there.

**Dave Jones:** It looks exactly like the characteristic curve. Bingo. That's actually where the symbol comes from. Now, some typical labels you'll find on a Zener diode data sheet are VZ, which is of course the Zener voltage, the knee voltage that it nominally happens at.

**Dave Jones:** And also, there's the current going through the Zener, which is called IZ, or it could be I test or something like that, but typically or IZT, for example. And then, there's this other weird one, ZZ.

**Dave Jones:** What is ZZ? Z, of course, is impedance. So, it's AC resistance. So, it's effectively the resistance of the diode under AC test conditions. They usually specify it at a particular frequency.

**Dave Jones:** There's actually an internal resistance in the Zener, which you need to take into account when you implement it in your practical circuit. And then, And course, you typically have a series resistor in series with your Zener as well.

**Dave Jones:** So this resistor is effectively inside the Zener diode. And this diode impedance or diode resistance is also known as the dynamic resistance because it's dynamic. It does actually change.

**Dave Jones:** It's not a fixed value. And you guessed it, it changes with current and also as with practically every component, temperature as well. And not just your ambient temperature, the actual junction temperature of the Zener itself because Zeners are used as power devices typically.

**Dave Jones:** So they heat up. They dissipate power. Hmm, trap for young players. And you know how I said diodes don't actually conduct anything in the reverse direction? Well, of course that's not true.

**Dave Jones:** No component is ideal and Zeners and diodes, regular ones, have the same thing. They have a reverse leakage. So I drew this as zero because well, it effectively is.

**Dave Jones:** You can't really see it on the graph typically cuz you're talking milliamps down here and the leakage is typically in the order of microamps, tens of microamps, things like that for pretty much both types.

**Dave Jones:** Until but as you can see, the knee here is not a sharp bam knee. It does start to taper like that. Hence a real knee is not just a right angle, is it?

**Dave Jones:** No, it's shaped like a knee. Hmm, does the same thing. So let's take a look at some typical applications for Zener diodes and there are two main applications. The first one we'll take a look at is regulation, i.e.

**Dave Jones:** voltage regulation because you can see that the well, you could have seen on the characteristic curve that the Zener produces a stable voltage once it hits that knee and that can be used for regulation.

**Dave Jones:** So I'll take a look at the classic configuration where we've got an input voltage here. We've got a Zener dropper resistor here, RZ, and then we've got the Zener diode itself with its internal dynamic resistance.

**Dave Jones:** Remember that, it's important. And that produces a the drop across it called VZ. Let's have a look for the particular case of a 1N4733, which might be a typical you know, medium power voltage regulation Zener diode.

**Dave Jones:** So, let's take the simple example where we've got no load here. So, we're just generating a reference voltage here from an input voltage VIN of 12 V and with the load open.

**Dave Jones:** So, I've disconnected the load there. So, we're only getting We've got two components, the Zener diode and the dropper resistor here. So, let's go to the data sheet to look at the test current, i.e.

**Dave Jones:** the nominal current for the given particular type of Zener that we've got to produce the nominal voltage. And in this case, IZT, there's actually two version values, IZT. We're looking at IZT1 here and ZZT1.

**Dave Jones:** They've got multiple ones just to show you the difference in the dynamic resistance. Anyway, IZT is 50 mA and ZZT at that 50 mA is going to be 5 ohms, but we can actually ignore that as you'll see in a minute because it's a you know, it's an order of magnitude at least less than our dropper resistor is going to turn out to be.

**Dave Jones:** So, we can just take it out of the equation to keep things simple. So, what value dropper resistor RZ do we need? It's easy. It's going to be the input voltage minus the voltage we want, the Zener voltage 5.1, and that will give us the voltage drop across the resistor here.

**Dave Jones:** And then we're just following Ohm's law, resistance equals voltage divided by current. So, it's the voltage drop across RZ divided by our Zener current, our 50 mA, our test current cuz all the current flows through the Zener.

**Dave Jones:** There is no load, so it all flows through. And you punch that in and that gives us a value of 138 ohms. So, if you had 12 V in and you wanted 5.1 V from your Zener, you'd use 138 ohm roughly resistor.

**Dave Jones:** And you can now see why the internal resistance, the dynamic resistance of the Zener, 5 ohms, doesn't really matter. It's more than an order of magnitude out from the 138 ohms, especially when you got no load.

**Dave Jones:** Doesn't matter. Easy. And that's all fine and dandy, and assuming your temperature didn't change, that Zener diode would happily regulate your voltage at 5.1 volts. But, the definition of regulation is keeping a fixed voltage, regulating the output, when your input here varies in voltage.

**Dave Jones:** So, let's go through again and see what happens. So, if we actually go into our data sheet here and have a look at the value for ZZ, I actually read the wrong value off the table.

**Dave Jones:** It's supposed to be 7 ohms for this particular one, but we'll just stick with 5 ohms. You'll notice that at uh IZ2, that second test current, which was uh 1 milliamp instead of 50 milliamps, the dynamic resistance is like 500 ohms or something.

**Dave Jones:** It's absolutely huge. But, the good thing about ZZ, you can read it from the table, it's it is going to change with relative to the current uh somewhat fairly linearly, but, you know, you can take that figure as a fairly stable one for most practical design calculations.

**Dave Jones:** So, if we increase our voltage and increase our current through our diode, let's just stick with the same 5-ohm value. If we decrease our input voltage a bit, then we can uh stick still stick with the 5-ohm value, even though the dynamic resistance is going to go up a little bit.

**Dave Jones:** You've got to work from something, unless you had a full parametric graph from the data sheet, which often you don't get. So, let's take the example where our input voltage changes from 12 volts we had before up to 15 volts.

**Dave Jones:** We've still got the same resistor. You can't change the resistor after it's in your circuit. So, our input voltage changes, how much variation on our Zener voltage do we get?

**Dave Jones:** I.e., how good is the regulation of this thing? Well, let's see. We need to get the differential. So, with these figures, 15 volts, 138 ohms, and our uh impedance, which now matters and comes into play because we're got a variation in our input or our load current.

**Dave Jones:** In this case, our load current hasn't changed, but our input has certainly changed. So, our dynamic resistance comes into play here. So, we calculate our current again, cuz it's going to change, cuz our input voltage has changed.

**Dave Jones:** So, uh once again, Ohm's law, the voltage drop across our Z here is the voltage on either side of it, 15 V minus our 5.1 V we had before.

**Dave Jones:** Let's just take it as uh 5.1 before because we're just getting a rough differential here. And divided by 138 ohms, Ohm's law, 71.7 mA. We had 50 mA before.

**Dave Jones:** Now, it's gone up to 71.7 cuz we've increased our voltage. It's naturally what you'd expect. But, here's where we get the difference in the current from what we had before, i.e., the delta.

**Dave Jones:** That's what that little triangle is. Don't be scared by the delta. It just means difference or change in. So, the change is the value we have now, 71.7 mA, the value we had before, 50 mA.

**Dave Jones:** We've increased our current. We've changed our current. We've got a delta uh current change of 21.7 mA. So, our current's going up. What does that do on the output?

**Dave Jones:** When you have the current flowing through here and it's higher than what it was before, before we had 5.1 V here, VZ, for our nominal dynamic resistance, but now we've increased our current, there's going to be extra voltage drop across this internal resistance.

**Dave Jones:** So, delta VZ, i.e., the change in our Zener voltage, the regulation, is equal to our delta in our current, our change in current, times our resistance. Ohm's law, nothing fancy here, equals 21.7 mA times 5 ohms, a change of 0.11 V or thereabouts.

**Dave Jones:** So, our regulator Our voltage has gone from 5.1 volts to now 5.21 volts. 2% or thereabouts. So, it's an okay sort of, you know, 2% voltage regulator. Kind of does the job.

**Dave Jones:** Not terrific, but okay. So, you can see how even with no load on the output, Zener diodes aren't that great. And the other thing you might have noticed, we've got no load, no load current at all, but we're pissing away 50 milliamps or 70 milliamps just to regulate our 5.1 volts.

**Dave Jones:** That's ridiculous. You can use a 7805 regulator and regulate that 5 volts exactly the same and it takes bugger all quiescent current. This thing takes 50 or 70 milliamps quiescent current.

**Dave Jones:** They're hopeless as like a regular voltage regulator powering no load. So, at low currents, they're very inefficient. And the other thing we have to be careful of, this is a 1 watt nominal power dissipation Zener.

**Dave Jones:** Are we within the power dissipation limits of this particular Zener diode? Well, the power in the Zener diode is the voltage of the Zener diode times the current. 5.1 times 50 milliamps, quarter of a watt.

**Dave Jones:** No worries. And you might be thinking, "Dave, that quarter watt is going to that's a fair bit of power in just a little package like that. It's going to increase the junction temperature." Yes, it will and that'll change the dynamic resistance and everything and yeah, it gets more complicated.

**Dave Jones:** I could go into a lot more detail, but I don't think we have time. Now, unfortunately, it gets a little bit more complicated because well, the real world is a little bit more complicated.

**Dave Jones:** Let's add our load back and let's say our load has 50 milliamps. We've still got our 5.1 volts Zener voltage, that's what we're shooting for, that's our regulation voltage.

**Dave Jones:** Our input is 12 volts again. Let's have a look. We've got to figure out a new value of RZ because 138 ohms we had last time may well, it's almost certainly not going to work for this particular current because we've got now got two currents, one flowing down the load, but we also have to maintain that test current that a bias current through the Zener diode.

**Dave Jones:** Remember that 50 milliamps we got from the data sheet. So, we still need 50 milliamps down here, but we also have to account for our load down here. And let's assume our load current is 50 milliamps, then we've got 50 milliamps down here, 50 milliamps down here.

**Dave Jones:** Kirchhoff's current law, we've got 100 milliamps flowing through our resistor here. So, we work out the resistor value the same way. It's a differential volt, it's the voltage across the resistor, the difference, which is 12 volts V in minus 5, but instead of just the diode test current, we've now got the diode test current plus the load current.

**Dave Jones:** So, it's a total of 100 milliamps. Eh, work it out, 69 ohms. Beauty. Good year. But what happens if our load changes? What if you're powering a microcontroller that draws 50 milliamps during operation, then it goes to sleep?

**Dave Jones:** What happens? Well, let's check it. When IL drops to zero, all of the current must flow through the Zener diode. We've got our 69 ohm resistor here cuz it's in circuit, we can't change it.

**Dave Jones:** So, our voltage across the resistor is 12 minus let's assume it's still 5.1 volts, doesn't change a huge amount the regulations. Eh, reasonable. Divided by our 69 ohm resistor.

**Dave Jones:** Much lower than 138 we had before. We've now got 100 milliamps. All of that 100 milliamps is now flowing through the Zener. Ooh, better check the power dissipation to make sure we're still within limits of our Zener diode.

**Dave Jones:** PZ, 5.1 * 100 milliamps, it's now dissipated in half a watt. Ooh, it's still within our 1 watt capability of our Zener diode, but it may not have been.

**Dave Jones:** We may have found if we used a half watt Zener in there, it might cook. If we used a quarter watt Zener in there, which might have just been enough before when we're dissipating a quarter watt in here, if our microcontroller went to sleep, magic smoke would escape from our Zener.

**Dave Jones:** Mhm. You can see how it starts to get complicated. What if our load is changing all the time and our input voltage is changing all the time? You have to rejig all the calculations and check and get a compromise value for your Zener dropper resistor and uh it's it's not pretty.

**Dave Jones:** They're but they still So, as for a voltage regulator for powering a circuit, it's okay if you don't care about the efficiency of it and things like that. But they as I said, they have more use in sort of more niche applications within bigger circuits and things like that.

**Dave Jones:** Um you know, reference voltages and stuff like that. But yeah, that's how regulation works. And you're still going to do even if you're using in low-power examples, you're still going to do the same sort of calculations.

**Dave Jones:** But this is why uh often, especially in reference circuits and things like that, you'll find that the Zener is actually powered from a constant current source. So, it's driving a constant current through and it's everything's much simpler.

**Dave Jones:** But anyway, that's basic Zener diode regulation. Can get quite complicated. Then if the temperature changes and the diode temperature rises, and I'll let you redo the calculations as an exercise for when the resistance value changes and the input value changes and the temperature rises.

**Dave Jones:** Go and find the temperature coefficient of the diode in the data sheet and have a play. Now, the other huge application which I can spend an entire video on and I probably will in the future is clipping and more importantly, clamping protection circuits.

**Dave Jones:** So, uh not only used in sort of like audio applications if you want to clip an audio waveform, for example, there might be some audio file reasons why you might want to do that.

**Dave Jones:** Um but one of the big ones is protection. Let's say you've got your IC here, be it a microcontroller or whatever it is, you can actually use Zeners for protection.

**Dave Jones:** They're actually pretty decent devices for protection. And uh you have the series current limiting resistor, of course, and the Zener can clamp the voltage. Let's say you're powering your circuit from 5 volts here, you might choose say a 5.1 volt Zener like this, and it can if you've got a huge spike on your input here, it might go up to 50 volts or something, you choose a suitable

**Dave Jones:** resistor, you calculate the power dissipation and things like that, and you will it'll clamp it at 5.1 volts, so you don't blow up your chip. Beauty. And the good thing about this is that also in the other direction, if this input goes negative, what happens?

**Dave Jones:** It acts like a normal diode. It conducts and clamps it to 0.6 volts below the rail here, and we'll be able to demonstrate this. Now, I won't go through the full math for choosing the correct input value, as I said, separate video, but take the 1N4733 diode we had before, the 5.1 volts.

**Dave Jones:** It's got a nominal 1 watt capability, but if you have a look at the data sheet, it's also got a surge current as well. For this particular one, it's about 900 milliamps, and that's like 5.1 volt clamping.

**Dave Jones:** That's like 4 and 1/2 watts. But, if you read the little asterisks down the bottom of the data sheet, it tells you that only applies for 10 milliseconds, and there's actually a typical you can get a typical derating curves and things like that.

**Dave Jones:** Here's an example of how you can derate the power, and from that you can just calculate how much power or pulse power you can actually get in a particular component.

**Dave Jones:** But, yeah, that's some data sheets don't have that at all. And there's one neat little configuration, which is two Zener diodes in series here, and what this does, let's say we've got an audio waveform coming in like this, it's going positive and negative, it's an AC waveform, then the this this Zener diode here is operating in the reverse characteristic, this one's operating in the forward characteristic, so it's operating just

**Dave Jones:** like a diode here. So, when the waveform goes positive, it's going to clamp it at the particular voltage of that Zener plus the 0.6 volts drop across this other Zener which is acting in the positive region acting like a diode and it'll clamp your waveform at the whatever value you choose for these Zeners.

**Dave Jones:** And then when the waveform goes negative the reverse happens. This one here is operating in the reverse characteristic. This one here is operating as a diode. It does the same thing.

**Dave Jones:** It clamps your negative waveform at the Zener voltage plus 0.6 volts and we can demo these sort of things and there's lots of other clamping applications and clipping circuits and all sorts of weird and wonderful configurations you can do with Zeners.

**Dave Jones:** This is one of their huge applications. And check it out. If we use our Rohde & Schwarz HMO scope here, it's got a building component tester and bingo, we can get the characteristic curve.

**Dave Jones:** Which voltage do you think this is? Let's have a look here. We've got current on the vertical scale so it's an IV characteristic curve. So it goes look up to 10 milliamps down to minus 10 milliamps here and voltage on the x-axis here hence the V.

**Dave Jones:** So bingo, we've got our 0.6 volts there of our characteristic. That's the forward characteristic and our reverse characteristic bingo, it's about 5.something-ish. It's actually a 5.1 volt Zener. Beauty.

**Dave Jones:** And if we swap it around in the other direction, what's going to happen? You guessed it. The characteristic is in the other direction. 0.6 volts here, 5.1 volts there.

**Dave Jones:** Beauty. Now although this doesn't let me expand the scale here, you can actually still see the knee in there is not a really sharp and that line there is not actually vertical.

**Dave Jones:** It actually slopes slightly in that direction due to you guessed it, the dynamic resistance. And if we just have a rudimentary example here with a 5.1 volt Zener I just got out of the junk bin, chose a 1K dropper resistor, eh, whatever, I don't know the data sheet for it.

**Dave Jones:** Just put in, you know, a nominal resistance value, it might be a bit high, but whatever. Anyway, we can see that when we switch it on, it's going to regulate at roughly 5.1 V, no worries.

**Dave Jones:** And that's like 7 1/2 V input here. So, as you can see, if we go down below the threshold, it's just going to go down as well. It's not going to regulate, but anything above 5.1, there we go, we're up at 10, but you'll notice that it is actually going up, and that's due to, of course, the dynamic resistance we just learned about.

**Dave Jones:** What I've done here is dropped the resistor by an order of magnitude down to 100 ohms or so, and if we actually go right up to 15 V here, let's have a look.

**Dave Jones:** Uh, we're now getting 5.4 V, but look, it's actually increasing, increasing, because the junction temperature of our Zener is going up. So, there you go. Whoopsie. It's not regulating too well, is it?

**Dave Jones:** Hm. And there's a bigger differential. It went from 5.22 V up to 5.47 V as opposed to with the 1K, it went from uh there was only a 100 mV change, basically.

**Dave Jones:** Now there's like 200 plus mV differential. Big difference. And a very simple clamping example. Here I've got a 5.1 V Zener, a 1K dropper, and the yellow waveform is the input.

**Dave Jones:** Uh, it's uh just a 7 V square wave, which just goes down to it goes between 1 and 7. Uh, and the blue waveform is the output across the Zener diode.

**Dave Jones:** And you can see both 1 V per division. The Zener diode clamps that output voltage at 1, 2, 3, 4, 5 V. I've got both uh channels set to the same ground position or reference there, and it clamps the output nicely, and it's going to do it very, very sharply.

**Dave Jones:** There's going to be no issues there whatsoever in terms of response time and stuff like that. But, you can see if we go in there, aha, look at that.

**Dave Jones:** That is our input and our output. That is due to our dynamic resistance. It's not going to follow it precisely. It is not an ideal Zener diode. So, yeah, but it's not going to overshoot.

**Dave Jones:** It's never going to overshoot. Beautiful for clamping. I'll just show you the difference between the 1K and the 100 ohm resistor here. I've got a 1K in there at the moment, and I'll keep the same time base, and you can see it has a particular characteristic response.

**Dave Jones:** Let's pack whack in the 100 ohm. There we go. It is significantly sharper. Now, I'm going to show you the AC clipping. There's the 0 V point for both waveforms.

**Dave Jones:** Blue's the output again. Feeding in 15 V peak-to-peak on the yellow waveform there. And you can see the blue one is definitely clipping. Look at that. Bingo. And what's it clamping at?

**Dave Jones:** 2 V per division, and 2 4 6. It's a These are both 5.1 V Zener's. It's because of that additional diode drop operating the forward characteristic region that adds in that not quite 0.6 V in this case.

**Dave Jones:** It's going up to 1 V because of the current and everything else the characteristic. But, there you go. It's out of the 5.1 to the diode drop in positive and negative clamping.

**Dave Jones:** Neat. And just to show you that Zener diodes don't work at arbitrarily low currents, I've got my Keithley current source here. 5.1 V Zener. I've got This is the decimal point.

**Dave Jones:** This is the milliamp mode. So, I've got 1 0. That's 10 mA. Okay, and we're getting our 5.1 V. It's, you know, hunky-dory. I can go like, "Whoa, right."

**Dave Jones:** It's getting a bit, you know, it's getting a bit, how you doing when we go up in current towards 100 milliamps. Anyway, let's drop it down a range, okay?

**Dave Jones:** So, we now are 1 milliamp. It's still working just fine. Let's go down to the microamp range. So, we're 100 microamps now. Look, 100 mic is 9.45 volts. It's starting to drop.

**Dave Jones:** What happens if we go down to 10 microamps? Not looking too good, is it? 1 microamp. Nope. So, you can't go down to arbitrarily low current. Zener diodes don't work at low currents like this.

**Dave Jones:** Even with a 10 volt compliance voltage. Look, right? 10 volts is plenty of compliant. This is the maximum uh the compliance voltage means the maximum this current source will output.

**Dave Jones:** Even if I go up to a 100 volts compliance source. Okay, it's a 100 volt power supply, but it's a constant current of 1 microamp. It just can't do it.

**Dave Jones:** It's not enough current for the Zener to operate at. Anyway, I hope you enjoyed that look at Zener diodes. It's been much longer than I thought. I thought I could maybe do this in 15 minutes, and now it's been at least double that.

**Dave Jones:** Sorry. Anyway, um if you want to cover Zener diodes sort of and we didn't even go completely in depth here. Yeah, these sort of things take time. Fundamentals take time to learn, unfortunately.

**Dave Jones:** Anyway, if you like the video, please give it a big thumbs up. Discuss below. All that sort of stuff. Hope you enjoyed it. Catch you next time. Today, we're taking a look at a real basic building block circuit called the peak detector.

**Dave Jones:** Now, what a peak detector is, if you've got an analog input signal that you want to know what value it peaks at, as the name suggests. If you've got your that could be a voltage like that, you want the positive peak voltage on that.

**Dave Jones:** Or negative. It's much easier to do it with two simple components. Turns out, all you need to do for a peak detector
