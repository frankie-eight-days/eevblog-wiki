---
video_id: O0ifJ4oVdG4
title: EEVblog #908 - Zener Diodes
url: https://www.youtube.com/watch?v=O0ifJ4oVdG4
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at one of the most fundamental components in electronics, the Zener diode. Let's take a look at it. Now, you're no doubt familiar with the regular silicon diode

**Dave Jones:** and we've got our Schottky diode as well. Same thing for the purposes of today's talk, but we're going to look at the differences between a regular diode and a Zener diode and we're going to take a look at how the Zener diode is

**Dave Jones:** useful in a bunch of different applications. Now, your regular diode like this, you're no doubt familiar that it conducts current in one direction only. It only allows current to flow through, hence why it's got that sort of arrow shape pointing in the direction of

**Dave Jones:** the conventional current flow. And if you try and reverse bias it, it doesn't allow current to flow back up. But the Zener diode is a bit different. It works exactly like a regular diode and allows current to flow through like that and it

**Dave Jones:** has the same voltage drop, you know, 0.6 volts to a volt or thereabouts, but it has a special property where it also allows current to flow in the other direction. You might say, "What use is that? The whole point of a

**Dave Jones:** diode is that it blocks current going in one direction." Well, there's something very interesting about the Zener that makes it useful. Let's take a look. Now, you should be familiar with the characteristic curve of a regular diode like this. Schottky

**Dave Jones:** diode is basically exactly the same except it has a smaller voltage drop. And as you can see on this characteristic curve here, also called an IV curve because it's I versus V, current versus voltage. You can see that

**Dave Jones:** until you get to about 0.6 volts, no current will basically flow through this. So, if you've got less than 0.6 volts on the diode or roughly, it won't conduct anything. It won't allow current to flow. But once it gets above that

**Dave Jones:** what's called the knee the diode knee here, then it start it can start to conduct current. Once you get above about 0.6 volts, temperature and device dependent and current dependent, it will allow current to flow. That's it. And if

**Dave Jones:** you reverse bias and put a negative voltage on, i.e. you go on this side of the curve here, no current flows. It just stays flat like that. Easy. Now, a Zener diode works exactly the same as a regular diode when you forward bias it,

**Dave Jones:** when you have current going down like this. And you get exactly the same characteristic response at the knee starts at about 0.6 volts and it starts to conduct current. But in the negative direction, when you try and put a

**Dave Jones:** negative voltage on here, i.e. you put the positive here and the negative here and you try and make current flow in the reverse direction, a regular diode just won't conduct anything. But we'll talk about that later. But a Zener diode,

**Dave Jones:** when you reverse bias it and try and make current flow in the reverse direction, it will do nothing for a while. It'll do nothing, but then it'll actually start conducting like a diode in the opposite direction. Weird. And the voltage that it typically

**Dave Jones:** does that is called the Zener voltage, Vz, or it might be called the Zener knee voltage or something like that. So, now we can start to annotate our characteristic graph here with some industry terminology. Up here we've got

**Dave Jones:** the forward characteristic, that is the characteristic of the Zener diode in the forward current direction, like that with the forward voltage. And naturally, we've got the reverse characteristic down here, which shows what happens when you try and push current in the other

**Dave Jones:** direction and you have reverse voltage on it with the Zener breakdown voltage. Now, I actually hinted before that regular diodes may have something a bit unusual with them, too. They actually act like Zener diodes, kind of. And so

**Dave Jones:** do Schottky diodes as well. We'll loop him in, lump him in the same thing. You know how I said when you reverse the voltage on them, they don't allow current to flow. That's what you typically think of a diode, and that's

**Dave Jones:** typically how it kind of works in practice. But ultimately, you get to a breakdown voltage. We'll call that VB here, and at that voltage, it's actually going to do a very similar thing. It's going to break down, or what's called

**Dave Jones:** avalanche in the other direction, very similar to a Zener diode. So you might go, "Dave, what's the difference between a Zener diode and a regular diode?" Well, regular diodes are not designed to work down in this reverse characteristic

**Dave Jones:** region. They're uncontrolled, they're horrible, they drift with temperature, and all sorts of They're not designed to work down here. Zener diodes have been specifically manufactured, specifically doped to actually have a quite a reasonable, controlled characteristic in the reverse breakdown region. Regular

**Dave Jones:** diodes and Schottky got diodes don't. So that's why you use Zener diodes and as opposed to regular diodes in the applications we'll see. But just be aware that regular diodes can do it as well, and that will be the maximum

**Dave Jones:** reverse voltage of the diode typically before it breaks down. And the other thing with diode breakdown voltages is it's usually very high. For example, a 1N914 diode, 4148, it might break down at, you know, 70 or 90 volts or

**Dave Jones:** something like that. You know, really not a very usable voltage in practical circuits. So it's effectively it stops current flowing in the other direction direction for most practical voltages. You know, a 1N4007 breaks down at 1,000 volts, for example.

**Dave Jones:** You know, so really they're not of practical value in that negative region. But Zener diodes have been specifically manufactured and doped to actually work at very usable and very useful breakdown voltages, anywhere from 2 volts up to 30

**Dave Jones:** volts or something like that or even higher and you can use that low and controlled Zener breakdown voltage for useful circuit applications. Beauty. Now, just to completely mess with your mind, sorry, but no explanation on Zener diodes would be complete without

**Dave Jones:** actually at least mentioning this. There are two different types of Zener breakdown. The red one which we saw here is called avalanche breakdown and that's what happens at high voltages in regular diodes, but there's also another type of

**Dave Jones:** Zener breakdown actually called Zener breakdown and it's actually this effect, the Zener effect, the Zener breakdown where Zener diodes get their name from. The person who founded it, physicist Clarence Zener, way back before you were born. Now, I won't go into the details

**Dave Jones:** of doping the PN regions and all the physics involved in actually manufacturing diodes. It's outside the scope of this thing, really. I'm sure you can Google it if you want to find out more, but just be aware that the

**Dave Jones:** Zener effect, the Zener breakdown is actually quantum tunneling. So, quantum physics is involved in this sort of thing, hence why it was found by a physicist. Anyway, the Zener breakdown occurs at roughly about 5 volts or below. Anything above it roughly 5 volts

**Dave Jones:** is going to be a different effect, avalanche breakdown. So, they're two physically different phenomenon happening inside the Zener diode or both or a combination of both could be happening if it's near to that sort of 5-volt region. So, you know, like a a

**Dave Jones:** 12-volt Zener diode will definitely be working as an avalanche breakdown and a 2.5-volt Zener diode would definitely be working in the Zener, using the Zener effect, it's called. But, you don't need to know that and most people just go the

**Dave Jones:** Zener effect even though they're actually might be talking about an actual avalanche effect instead of a Zener effect. If you're talking about Zener diodes, it's a Zener breakdown voltage. It doesn't matter which voltage it occurs at, it's the Zener effect. And

**Dave Jones:** just a further clarification on the terminology here, the reverse breakdown voltage, I put VB before cuz I was talking about breakdown, but in the data sheet you'll find that as VR for regular diodes. So, just stick with VR. Now,

**Dave Jones:** let's take a look at a typical implementation of a Zener diode here, and we're using the reverse characteristic. Cuz if we use the forward characteristic, you might as well just use a diode. It's just a regular diode. So, that's why in a

**Dave Jones:** circuit like this, oh, I should put that. That's positive and that's negative there. So, you use it in the reverse bias configuration. So, we're looking at the Zener breakdown voltage. And now, hopefully, you can see why the Zener symbol is as it is. Look how it

**Dave Jones:** kinks up there and kinks down there. It looks exactly like the characteristic curve. Bingo. That's actually where the symbol comes from. Now, some typical labels you'll find on a Zener diode data sheet are VZ, which is of course the Zener voltage, the knee

**Dave Jones:** voltage that it nominally happens at. And also, there's the current going through the Zener, which is called IZ, or it could be I test or something like that, but typically or IZT, for example. And then, there's this other weird one,

**Dave Jones:** ZZ. What is ZZ? Z, of course, is impedance. So, it's AC resistance. So, it's effectively the resistance of the diode under AC test conditions. They usually specify it at a particular frequency. There's actually an internal resistance in the Zener, which you need

**Dave Jones:** to take into account when you implement it in your practical circuit. And then, And course, you typically have a series resistor in series with your Zener as well. So this resistor is effectively inside the Zener diode. And this diode

**Dave Jones:** impedance or diode resistance is also known as the dynamic resistance because it's dynamic. It does actually change. It's not a fixed value. And you guessed it, it changes with current and also as with practically every component, temperature as well. And not just your

**Dave Jones:** ambient temperature, the actual junction temperature of the Zener itself because Zeners are used as power devices typically. So they heat up. They dissipate power. Hmm, trap for young players. And you know how I said diodes don't actually conduct anything in the reverse

**Dave Jones:** direction? Well, of course that's not true. No component is ideal and Zeners and diodes, regular ones, have the same thing. They have a reverse leakage. So I drew this as zero because well, it effectively is. You can't really see it

**Dave Jones:** on the graph typically cuz you're talking milliamps down here and the leakage is typically in the order of microamps, tens of microamps, things like that for pretty much both types. Until but as you can see, the knee here

**Dave Jones:** is not a sharp bam knee. It does start to taper like that. Hence a real knee is not just a right angle, is it? No, it's shaped like a knee. Hmm, does the same thing. So let's take a look at some typical applications for

**Dave Jones:** Zener diodes and there are two main applications. The first one we'll take a look at is regulation, i.e. voltage regulation because you can see that the well, you could have seen on the characteristic curve that the Zener produces a stable voltage once it hits

**Dave Jones:** that knee and that can be used for regulation. So I'll take a look at the classic configuration where we've got an input voltage here. We've got a Zener dropper resistor here, RZ, and then we've got the Zener diode itself with

**Dave Jones:** its internal dynamic resistance. Remember that, it's important. And that produces a the drop across it called VZ. Let's have a look for the particular case of a 1N4733, which might be a typical you know, medium power voltage regulation Zener diode. So, let's take

**Dave Jones:** the simple example where we've got no load here. So, we're just generating a reference voltage here from an input voltage VIN of 12 V and with the load open. So, I've disconnected the load there. So, we're only getting We've got

**Dave Jones:** two components, the Zener diode and the dropper resistor here. So, let's go to the data sheet to look at the test current, i.e. the nominal current for the given particular type of Zener that we've got to produce the nominal

**Dave Jones:** voltage. And in this case, IZT, there's actually two version values, IZT. We're looking at IZT1 here and ZZT1. They've got multiple ones just to show you the difference in the dynamic resistance. Anyway, IZT is 50 mA and ZZT at that 50 mA is going to be 5

**Dave Jones:** ohms, but we can actually ignore that as you'll see in a minute because it's a you know, it's an order of magnitude at least less than our dropper resistor is going to turn out to be. So, we can just take

**Dave Jones:** it out of the equation to keep things simple. So, what value dropper resistor RZ do we need? It's easy. It's going to be the input voltage minus the voltage we want, the Zener voltage 5.1, and that will give us the voltage drop across

**Dave Jones:** the resistor here. And then we're just following Ohm's law, resistance equals voltage divided by current. So, it's the voltage drop across RZ divided by our Zener current, our 50 mA, our test current cuz all the current flows through the Zener. There is no load, so

**Dave Jones:** it all flows through. And you punch that in and that gives us a value of 138 ohms. So, if you had 12 V in and you wanted 5.1 V from your Zener, you'd use 138 ohm roughly resistor. And you can

**Dave Jones:** now see why the internal resistance, the dynamic resistance of the Zener, 5 ohms, doesn't really matter. It's more than an order of magnitude out from the 138 ohms, especially when you got no load. Doesn't matter. Easy. And that's all fine and

**Dave Jones:** dandy, and assuming your temperature didn't change, that Zener diode would happily regulate your voltage at 5.1 volts. But, the definition of regulation is keeping a fixed voltage, regulating the output, when your input here varies in voltage. So, let's go through again

**Dave Jones:** and see what happens. So, if we actually go into our data sheet here and have a look at the value for ZZ, I actually read the wrong value off the table. It's supposed to be 7 ohms for this

**Dave Jones:** particular one, but we'll just stick with 5 ohms. You'll notice that at uh IZ2, that second test current, which was uh 1 milliamp instead of 50 milliamps, the dynamic resistance is like 500 ohms or something. It's absolutely huge. But,

**Dave Jones:** the good thing about ZZ, you can read it from the table, it's it is going to change with relative to the current uh somewhat fairly linearly, but, you know, you can take that figure as a fairly stable one for most practical design

**Dave Jones:** calculations. So, if we increase our voltage and increase our current through our diode, let's just stick with the same 5-ohm value. If we decrease our input voltage a bit, then we can uh stick still stick with the 5-ohm value,

**Dave Jones:** even though the dynamic resistance is going to go up a little bit. You've got to work from something, unless you had a full parametric graph from the data sheet, which often you don't get. So, let's take the example where our input

**Dave Jones:** voltage changes from 12 volts we had before up to 15 volts. We've still got the same resistor. You can't change the resistor after it's in your circuit. So, our input voltage changes, how much variation on our Zener voltage do we

**Dave Jones:** get? I.e., how good is the regulation of this thing? Well, let's see. We need to get the differential. So, with these figures, 15 volts, 138 ohms, and our uh impedance, which now matters and comes into play because we're got a variation

**Dave Jones:** in our input or our load current. In this case, our load current hasn't changed, but our input has certainly changed. So, our dynamic resistance comes into play here. So, we calculate our current again, cuz it's going to change, cuz our input voltage has

**Dave Jones:** changed. So, uh once again, Ohm's law, the voltage drop across our Z here is the voltage on either side of it, 15 V minus our 5.1 V we had before. Let's just take it as uh 5.1 before because

**Dave Jones:** we're just getting a rough differential here. And divided by 138 ohms, Ohm's law, 71.7 mA. We had 50 mA before. Now, it's gone up to 71.7 cuz we've increased our voltage. It's naturally what you'd expect. But, here's where we get the

**Dave Jones:** difference in the current from what we had before, i.e., the delta. That's what that little triangle is. Don't be scared by the delta. It just means difference or change in. So, the change is the value we have now, 71.7 mA,

**Dave Jones:** the value we had before, 50 mA. We've increased our current. We've changed our current. We've got a delta uh current change of 21.7 mA. So, our current's going up. What does that do on the output? When you have the current

**Dave Jones:** flowing through here and it's higher than what it was before, before we had 5.1 V here, VZ, for our nominal dynamic resistance, but now we've increased our current, there's going to be extra voltage drop across this internal resistance. So,

**Dave Jones:** delta VZ, i.e., the change in our Zener voltage, the regulation, is equal to our delta in our current, our change in current, times our resistance. Ohm's law, nothing fancy here, equals 21.7 mA times 5 ohms, a change of 0.11 V or

**Dave Jones:** thereabouts. So, our regulator Our voltage has gone from 5.1 volts to now 5.21 volts. 2% or thereabouts. So, it's an okay sort of, you know, 2% voltage regulator. Kind of does the job. Not terrific, but okay. So, you can see how even with no

**Dave Jones:** load on the output, Zener diodes aren't that great. And the other thing you might have noticed, we've got no load, no load current at all, but we're pissing away 50 milliamps or 70 milliamps just to regulate our 5.1

**Dave Jones:** volts. That's ridiculous. You can use a 7805 regulator and regulate that 5 volts exactly the same and it takes bugger all quiescent current. This thing takes 50 or 70 milliamps quiescent current. They're hopeless as like a regular voltage regulator powering no load. So,

**Dave Jones:** at low currents, they're very inefficient. And the other thing we have to be careful of, this is a 1 watt nominal power dissipation Zener. Are we within the power dissipation limits of this particular Zener diode? Well, the power in the Zener diode is

**Dave Jones:** the voltage of the Zener diode times the current. 5.1 times 50 milliamps, quarter of a watt. No worries. And you might be thinking, "Dave, that quarter watt is going to that's a fair bit of power in just a little package like that. It's

**Dave Jones:** going to increase the junction temperature." Yes, it will and that'll change the dynamic resistance and everything and yeah, it gets more complicated. I could go into a lot more detail, but I don't think we have time. Now, unfortunately,

**Dave Jones:** it gets a little bit more complicated because well, the real world is a little bit more complicated. Let's add our load back and let's say our load has 50 milliamps. We've still got our 5.1 volts Zener voltage, that's what we're

**Dave Jones:** shooting for, that's our regulation voltage. Our input is 12 volts again. Let's have a look. We've got to figure out a new value of RZ because 138 ohms we had last time may well, it's almost certainly not going to work for this

**Dave Jones:** particular current because we've got now got two currents, one flowing down the load, but we also have to maintain that test current that a bias current through the Zener diode. Remember that 50 milliamps we got from the data sheet.

**Dave Jones:** So, we still need 50 milliamps down here, but we also have to account for our load down here. And let's assume our load current is 50 milliamps, then we've got 50 milliamps down here, 50 milliamps down here. Kirchhoff's current law,

**Dave Jones:** we've got 100 milliamps flowing through our resistor here. So, we work out the resistor value the same way. It's a differential volt, it's the voltage across the resistor, the difference, which is 12 volts V in minus 5, but

**Dave Jones:** instead of just the diode test current, we've now got the diode test current plus the load current. So, it's a total of 100 milliamps. Eh, work it out, 69 ohms. Beauty. Good year. But what happens if our load changes? What if

**Dave Jones:** you're powering a microcontroller that draws 50 milliamps during operation, then it goes to sleep? What happens? Well, let's check it. When IL drops to zero, all of the current must flow through the Zener diode. We've got our 69 ohm resistor here cuz it's in

**Dave Jones:** circuit, we can't change it. So, our voltage across the resistor is 12 minus let's assume it's still 5.1 volts, doesn't change a huge amount the regulations. Eh, reasonable. Divided by our 69 ohm resistor. Much lower than 138 we had before. We've now got 100

**Dave Jones:** milliamps. All of that 100 milliamps is now flowing through the Zener. Ooh, better check the power dissipation to make sure we're still within limits of our Zener diode. PZ, 5.1 * 100 milliamps, it's now dissipated in half a

**Dave Jones:** watt. Ooh, it's still within our 1 watt capability of our Zener diode, but it may not have been. We may have found if we used a half watt Zener in there, it might cook. If we used a quarter watt

**Dave Jones:** Zener in there, which might have just been enough before when we're dissipating a quarter watt in here, if our microcontroller went to sleep, magic smoke would escape from our Zener. Mhm. You can see how it starts to get

**Dave Jones:** complicated. What if our load is changing all the time and our input voltage is changing all the time? You have to rejig all the calculations and check and get a compromise value for your Zener dropper resistor and uh it's

**Dave Jones:** it's not pretty. They're but they still So, as for a voltage regulator for powering a circuit, it's okay if you don't care about the efficiency of it and things like that. But they as I said, they have more use in sort of more

**Dave Jones:** niche applications within bigger circuits and things like that. Um you know, reference voltages and stuff like that. But yeah, that's how regulation works. And you're still going to do even if you're using in low-power examples, you're still going to do the same sort

**Dave Jones:** of calculations. But this is why uh often, especially in reference circuits and things like that, you'll find that the Zener is actually powered from a constant current source. So, it's driving a constant current through and it's everything's much simpler. But

**Dave Jones:** anyway, that's basic Zener diode regulation. Can get quite complicated. Then if the temperature changes and the diode temperature rises, and I'll let you redo the calculations as an exercise for when the resistance value changes and the input value changes and the

**Dave Jones:** temperature rises. Go and find the temperature coefficient of the diode in the data sheet and have a play. Now, the other huge application which I can spend an entire video on and I probably will in the future is clipping and more

**Dave Jones:** importantly, clamping protection circuits. So, uh not only used in sort of like audio applications if you want to clip an audio waveform, for example, there might be some audio file reasons why you might want to do that. Um but one of the big ones is

**Dave Jones:** protection. Let's say you've got your IC here, be it a microcontroller or whatever it is, you can actually use Zeners for protection. They're actually pretty decent devices for protection. And uh you have the series current limiting resistor, of course, and the

**Dave Jones:** Zener can clamp the voltage. Let's say you're powering your circuit from 5 volts here, you might choose say a 5.1 volt Zener like this, and it can if you've got a huge spike on your input here, it might go up to 50 volts or

**Dave Jones:** something, you choose a suitable resistor, you calculate the power dissipation and things like that, and you will it'll clamp it at 5.1 volts, so you don't blow up your chip. Beauty. And the good thing about this is that also

**Dave Jones:** in the other direction, if this input goes negative, what happens? It acts like a normal diode. It conducts and clamps it to 0.6 volts below the rail here, and we'll be able to demonstrate this. Now, I won't go

**Dave Jones:** through the full math for choosing the correct input value, as I said, separate video, but take the 1N4733 diode we had before, the 5.1 volts. It's got a nominal 1 watt capability, but if you have a look at the data sheet, it's

**Dave Jones:** also got a surge current as well. For this particular one, it's about 900 milliamps, and that's like 5.1 volt clamping. That's like 4 and 1/2 watts. But, if you read the little asterisks down the bottom of the data sheet, it

**Dave Jones:** tells you that only applies for 10 milliseconds, and there's actually a typical you can get a typical derating curves and things like that. Here's an example of how you can derate the power, and from that you can just

**Dave Jones:** calculate how much power or pulse power you can actually get in a particular component. But, yeah, that's some data sheets don't have that at all. And there's one neat little configuration, which is two Zener diodes in series here, and what this does, let's say

**Dave Jones:** we've got an audio waveform coming in like this, it's going positive and negative, it's an AC waveform, then the this this Zener diode here is operating in the reverse characteristic, this one's operating in the forward characteristic, so it's operating just

**Dave Jones:** like a diode here. So, when the waveform goes positive, it's going to clamp it at the particular voltage of that Zener plus the 0.6 volts drop across this other Zener which is acting in the positive region acting like a diode and

**Dave Jones:** it'll clamp your waveform at the whatever value you choose for these Zeners. And then when the waveform goes negative the reverse happens. This one here is operating in the reverse characteristic. This one here is operating as a diode.

**Dave Jones:** It does the same thing. It clamps your negative waveform at the Zener voltage plus 0.6 volts and we can demo these sort of things and there's lots of other clamping applications and clipping circuits and all sorts of weird and

**Dave Jones:** wonderful configurations you can do with Zeners. This is one of their huge applications. And check it out. If we use our Rohde & Schwarz HMO scope here, it's got a building component tester and bingo, we can get the characteristic

**Dave Jones:** curve. Which voltage do you think this is? Let's have a look here. We've got current on the vertical scale so it's an IV characteristic curve. So it goes look up to 10 milliamps down to minus 10 milliamps here and voltage on the x-axis

**Dave Jones:** here hence the V. So bingo, we've got our 0.6 volts there of our characteristic. That's the forward characteristic and our reverse characteristic bingo, it's about 5.something-ish. It's actually a 5.1 volt Zener. Beauty. And if we swap it around in the other

**Dave Jones:** direction, what's going to happen? You guessed it. The characteristic is in the other direction. 0.6 volts here, 5.1 volts there. Beauty. Now although this doesn't let me expand the scale here, you can actually still see the knee in there is

**Dave Jones:** not a really sharp and that line there is not actually vertical. It actually slopes slightly in that direction due to you guessed it, the dynamic resistance. And if we just have a rudimentary example here with a 5.1 volt Zener I

**Dave Jones:** just got out of the junk bin, chose a 1K dropper resistor, eh, whatever, I don't know the data sheet for it. Just put in, you know, a nominal resistance value, it might be a bit high, but whatever. Anyway, we can see that when we switch

**Dave Jones:** it on, it's going to regulate at roughly 5.1 V, no worries. And that's like 7 1/2 V input here. So, as you can see, if we go down below the threshold, it's just going to go down as well. It's not going to

**Dave Jones:** regulate, but anything above 5.1, there we go, we're up at 10, but you'll notice that it is actually going up, and that's due to, of course, the dynamic resistance we just learned about. What I've done here is dropped the resistor

**Dave Jones:** by an order of magnitude down to 100 ohms or so, and if we actually go right up to 15 V here, let's have a look. Uh, we're now getting 5.4 V, but look, it's actually increasing, increasing, because the junction

**Dave Jones:** temperature of our Zener is going up. So, there you go. Whoopsie. It's not regulating too well, is it? Hm. And there's a bigger differential. It went from 5.22 V up to 5.47 V as opposed to with the 1K, it went

**Dave Jones:** from uh there was only a 100 mV change, basically. Now there's like 200 plus mV differential. Big difference. And a very simple clamping example. Here I've got a 5.1 V Zener, a 1K dropper, and the yellow waveform is the input. Uh, it's

**Dave Jones:** uh just a 7 V square wave, which just goes down to it goes between 1 and 7. Uh, and the blue waveform is the output across the Zener diode. And you can see both 1 V per division. The Zener diode clamps that

**Dave Jones:** output voltage at 1, 2, 3, 4, 5 V. I've got both uh channels set to the same ground position or reference there, and it clamps the output nicely, and it's going to do it very, very sharply. There's going to be no issues there whatsoever

**Dave Jones:** in terms of response time and stuff like that. But, you can see if we go in there, aha, look at that. That is our input and our output. That is due to our dynamic resistance. It's not going to follow it

**Dave Jones:** precisely. It is not an ideal Zener diode. So, yeah, but it's not going to overshoot. It's never going to overshoot. Beautiful for clamping. I'll just show you the difference between the 1K and the 100 ohm resistor here. I've

**Dave Jones:** got a 1K in there at the moment, and I'll keep the same time base, and you can see it has a particular characteristic response. Let's pack whack in the 100 ohm. There we go. It is significantly sharper. Now, I'm going to

**Dave Jones:** show you the AC clipping. There's the 0 V point for both waveforms. Blue's the output again. Feeding in 15 V peak-to-peak on the yellow waveform there. And you can see the blue one is definitely clipping. Look at that.

**Dave Jones:** Bingo. And what's it clamping at? 2 V per division, and 2 4 6. It's a These are both 5.1 V Zener's. It's because of that additional diode drop operating the forward characteristic region that adds in that not quite 0.6 V in this case.

**Dave Jones:** It's going up to 1 V because of the current and everything else the characteristic. But, there you go. It's out of the 5.1 to the diode drop in positive and negative clamping. Neat. And just to show you that Zener diodes

**Dave Jones:** don't work at arbitrarily low currents, I've got my Keithley current source here. 5.1 V Zener. I've got This is the decimal point. This is the milliamp mode. So, I've got 1 0. That's 10 mA. Okay, and we're getting our 5.1 V. It's,

**Dave Jones:** you know, hunky-dory. I can go like, "Whoa, right." It's getting a bit, you know, it's getting a bit, how you doing when we go up in current towards 100 milliamps. Anyway, let's drop it down a range, okay? So, we now are 1 milliamp. It's

**Dave Jones:** still working just fine. Let's go down to the microamp range. So, we're 100 microamps now. Look, 100 mic is 9.45 volts. It's starting to drop. What happens if we go down to 10 microamps? Not looking too good, is it? 1 microamp.

**Dave Jones:** Nope. So, you can't go down to arbitrarily low current. Zener diodes don't work at low currents like this. Even with a 10 volt compliance voltage. Look, right? 10 volts is plenty of compliant. This is the maximum uh the compliance voltage means the

**Dave Jones:** maximum this current source will output. Even if I go up to a 100 volts compliance source. Okay, it's a 100 volt power supply, but it's a constant current of 1 microamp. It just can't do it. It's not enough current for the

**Dave Jones:** Zener to operate at. Anyway, I hope you enjoyed that look at Zener diodes. It's been much longer than I thought. I thought I could maybe do this in 15 minutes, and now it's been at least double that. Sorry. Anyway, um if you

**Dave Jones:** want to cover Zener diodes sort of and we didn't even go completely in depth here. Yeah, these sort of things take time. Fundamentals take time to learn, unfortunately. Anyway, if you like the video, please give it a big thumbs up.

**Dave Jones:** Discuss below. All that sort of stuff. Hope you enjoyed it. Catch you next time. Today, we're taking a look at a real basic building block circuit called the peak detector. Now, what a peak detector is, if you've got an analog input signal

**Dave Jones:** that you want to know what value it peaks at, as the name suggests. If you've got your that could be a voltage like that, you want the positive peak voltage on that. Or negative. It's much easier to do it with two simple

**Dave Jones:** components. Turns out, all you need to do for a peak detector
