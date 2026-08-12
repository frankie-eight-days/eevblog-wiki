---
video_id: D9J-AmCcf4U
title: EEVblog 1473 - How Your LCR Meter Works
url: https://www.youtube.com/watch?v=D9J-AmCcf4U
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 23, "3": 46, "4": 59, "5": 67, "6": 92, "7": 106, "8": 119, "9": 132, "10": 153, "11": 167, "12": 188, "13": 196, "14": 209, "15": 218, "16": 231, "17": 241, "18": 252, "19": 269, "20": 277, "21": 293, "22": 302, "23": 312, "24": 330, "25": 346, "26": 359, "27": 374, "28": 388, "29": 397, "30": 410, "31": 420, "32": 444, "33": 454, "34": 472, "35": 484, "36": 509, "37": 523, "38": 534, "39": 548, "40": 557, "41": 568, "42": 579, "43": 594, "44": 604, "45": 615, "46": 628, "47": 643, "48": 661, "49": 680, "50": 690, "51": 703, "52": 717, "53": 726, "54": 752, "55": 773, "56": 785, "57": 800, "58": 812, "59": 831, "60": 846, "61": 859, "62": 871, "63": 888, "64": 910, "65": 923, "66": 944, "67": 953, "68": 965, "69": 981, "70": 993, "71": 1013, "72": 1027, "73": 1045, "74": 1057, "75": 1069, "76": 1085, "77": 1109, "78": 1127, "79": 1136, "80": 1150, "81": 1165}
---

**Dave Jones:** Hi, I recently shot this video as part of another video which I'll link in up here and down below if you haven't seen it where I do in-circuit capacitance measures with an LCR meter and thought I'd do an interlude of how LCR meters work.

**Dave Jones:** So, I go through the whole theory of it. Ended up being 20 minutes long, so I decided to split it out as a second video and that's what you're seeing now, but it's related to the other bench video.

**Dave Jones:** So, you really have to watch them both. Anyway, just pretend this is a stand-alone video and then go watch the other one. Let's go for a brief interlude to the whiteboard to see how LCR meters actually work because this will explain everything that we're seeing here and it's really cool to know and really to properly use your LCR meter, you really should understand the fundamental concepts of how they work.

**Dave Jones:** So, your LCR meter is nothing more than an AC signal source here. That's the test frequency we've got, usually 100 hertz, 120 hertz because of that weird American rubbish, 1 kilohertz, 10 kilohertz, 100 kilohertz.

**Dave Jones:** They can go higher, but they're the general steps in any sort of LCR meter that you're typically going to use. And then that will have a particular test voltage.

**Dave Jones:** It could be like 1 volt RMS for example. We'll get into this later cuz that's also one of the traps for young players. Stick around. So, that say 1 volt RMS signal at whatever frequency you select goes through a series range resistor like this and of course that goes off and they measure the voltage and current across that range resistor and that you saw how just before how our capacitance

**Dave Jones:** meter actually changed ranges, gave us less resolution, less digits when we actually switched frequency, that's because of range resistor limitations. And then it goes directly on the test terminals and then we've got our device under test.

**Dave Jones:** So, we're going to call that X. DUT there. DUT is the industry term for device under test. And then of course the instrument can measure the voltage across the load as well as the voltage across the range resistor and it can also measure the current I as well, which will be the same for both.

**Dave Jones:** Now, here's the trick. We have to start talking about phase angles and complex numbers, which we've coincidentally just looked at in the recent AC fundamentals tutorial series, linked up here and down below if you haven't seen it.

**Dave Jones:** Highly recommend it. Otherwise, you may not understand what we're talking about when we start talking about J's down here. So, the sneaky thing your LCR meter does is it measures both the voltage and current at 0° phase angle and 90° phase angle like this with reference to your reference waveform, which is your signal generator over here.

**Dave Jones:** So, if you've got your signal gen like this, so the signal generator is the reference, and then you'll measure it at this point here and also this point here as well on the waveform.

**Dave Jones:** So, what they do is they measure the voltage and current at this reference point time here on the waveform, and then at 90° here as well. So, this is a kind of a weird graph because we've got voltage on this axis and also voltage on this axis, but you can see that it's a phasor diagram in that it's has a phase angle in there.

**Dave Jones:** So, this just represents that voltage that you're measuring at 90° there. And by measuring the voltage, of course, you can also measure the current cuz you've got a pure range resistor.

**Dave Jones:** And as we've talked about in previous videos, if you're just measuring a resistor, a pure resistor, then your phase angles are all going to be zero like this because there's no reactive components at all.

**Dave Jones:** A resistor, a pure resistor, is not reactive. But then you might have some inductance in the test leads as we saw before, but when we actually switched those uh test leads over, it made a difference.

**Dave Jones:** But in theory, if you're measuring a pure resistive load here, then you wouldn't have any phase angle on your voltages and your currents. They'd all be in phase. So, we just have to apply some arbitrary labels here.

**Dave Jones:** Our voltage phaser like this, you drop it down like this and this gives you you will call it VP. That's your voltage at 0° phase angle. You could call it V0 if you wanted.

**Dave Jones:** And then likewise with your current here, you measure the current which is the voltage across the range resistor there, then you drop that down and that will be your current at 0° phase angle.

**Dave Jones:** We'll call that IP. And then we'll do the same at 90°. We'll take a measurement at 90 and instantaneous measurement at 90° and that will give us our voltage in at 90° which we'll call VQ and the current IQ.

**Dave Jones:** And I had that arrow back to front. And then we can use these two equations here which you don't have to know, don't bother remembering it doesn't matter. I'm just putting there for completeness.

**Dave Jones:** We can get values for the equivalent circuit which we're going to turn our device into. Our device becomes an equivalent circuit with a series resistor we'll call RS and a series reactance which is why we have to call it X.

**Dave Jones:** X is reactance. Remember, we have no idea whether this is a pure capacitor, a pure inductor, a dodgy capacitor, a dodgy inductor, or a pure resistor, or whatever. We don't know.

**Dave Jones:** It depends on the phase angles that we've actually got here for the voltage and current. So we're now talking about instead of capacitance and inductors, we're talking about reactances.

**Dave Jones:** So these two formulas here will give you the value for RS which is your pure resistance. You always have resistance in series with any component. It can be zero ideally, but right it's we have a series resistance and then a reactance value and that's they're calculated slightly differently.

**Dave Jones:** You'll see that these are slightly swapped around here, but as I said, doesn't matter. We measure these things and we calculate an equivalent circuit. And the cool thing is from that equivalent circuit we can calculate everything else that our LCR meter measures.

**Dave Jones:** Now, if you've watched my AC fundamentals series, you'll know all about complex planes and complex numbers and reactances. In fact, I have to do another video on just reactances and AC components and stuff like that.

**Dave Jones:** Actually, this video probably should have came after those videos, but I don't plan ahead. Anyway, we've now got a complex plane. So, we've got J. That's our imaginary operator J, which tells us that we're using complex numbers in the complex plane.

**Dave Jones:** So, we've got JX, which is our reactance. So, our reactance is an imaginary component. And by imaginary, I mean it's the imaginary plane. Uh you have to watch my previous videos if you don't know what this is.

**Dave Jones:** Sorry, go and watch them. So, we've got our complex reactive component JX here, and we've got our real component, of course, on our real line down the bottom here.

**Dave Jones:** And this represents our equivalent circuit. So, XS, uh which is the series component in here, will have a phase angle in the complex plane. And we'll call that phase angle phi down here.

**Dave Jones:** It's different to uh theta, as I've talked about in a previous video. And if you actually drop that vector down like this, then you get the real value for RS here.

**Dave Jones:** And then, there'll be another angle in here, which that symbol there, you might it's a bit weird. That's actually uh delta, which is another lowercase Greek uh letter. And so, with uh phi and delta here, these two angles and uh these values, we can calculate the quality factor, the Q of the component, the Q of the capacitor, as you see on an LCR meter, you'll see Q,

**Dave Jones:** quality factor, and also D, which is your dissipation factor. Have I done a video on capacitors that explains that? Probably. So, you can calculate your quality factor Q is just equal to tan phi here, this phase angle.

**Dave Jones:** And that's actually equal to um the absolute magnitude of XS on RS. So, the absolute value of your series reactant reactants on the value of your series resistance. And likewise, dissipation factor is tan delta here, this angle in here.

**Dave Jones:** And that's equal to your absolute value. That's what those little bars there. They just means take out the sign. They're absolute. Divided by XS here, which is your series reactance.

**Dave Jones:** You'll notice that they're actually opposite. And of course, one on Q is D, and one on D is Q. Easy. And if you have watched my previous AC fundamental series videos, this should probably be up in your head or it's already popped out that if it's a positive angle, if XS is is series reactance is a positive angle like this on the complex plane, then it's inductive.

**Dave Jones:** And if it happens to go negative like that, then it's capacitive. And this is how your LCR meter can detect whether or not you've got a in auto mode, whether or not you've got an inductor or a capacitor.

**Dave Jones:** By knowing what this phase angle XS is here by doing these measurements at different angles. Cool, huh? And we can measure a lot more than quality factor and dissipation factor by just having these two values here.

**Dave Jones:** We can measure everything that your LCR meter can measure is calculated from these this equivalent circuit and these two components. So, I got quality factor, dissipation factor. They're the formulas we just took from there.

**Dave Jones:** D is one on Q. And then we've got RP, which is your parallel resistance. And you'll see the symbols on the LCR meter depending on what mode you're in.

**Dave Jones:** Stick around and I'll show you this graphically in a second. But you can see the parallel resistance. For example, one on Q plus plus times RS. Doesn't You don't have to remember these formulas.

**Dave Jones:** Just know that everything is calculated from this simple equivalent circuit like this. And then your impedance is the square root of your series resistance plus your series reactance squared in there.

**Dave Jones:** And then CP, that's your parallel capacitance if you're in parallel mode or series mode. For example, this is the parallel resistance you'll get in parallel with your parallel capacitance.

**Dave Jones:** There's the formula there. And then your parallel inductance has that formula. Remember this is not W, it's omega, which is 2 pi f. You should know that from my previous video.

**Dave Jones:** So it takes into account the frequency when you're calculating the capacitance and the inductance values. And then in series mode on your LCR meter, which can either be automatically or manually selected.

**Dave Jones:** There's usually a series parallel button on there. Then series capacitance will be 1 on omega absolute value of your series reactance down here. And LS is just pretty much the opposite of that.

**Dave Jones:** So you can calculate all these things, everything you see on there, by simply measuring at 0° and 90° like that with a simple range resistor. Now, not every LCR meter goes to this amount of effort to do this.

**Dave Jones:** There are various ways that you can, you know, do this, you know, sort of like cheating a bit brute forcey. But you know, if you want to do this properly and your high-end LCR meters, you know, you get one of your real high-end bench ones and stuff like that, then yeah, they'll be measuring these until the cows come home and calculating all this stuff.

**Dave Jones:** I just find it amazing that from these two simple values here and from simple measurements, all of this just comes out in the wash. So how does your LCR meter determine in auto mode whether or not it's an inductor or a capacitor or whether or not, you know, what are the series what are the dominant values, whether it's a dominant resistor.

**Dave Jones:** You saw it in the measurements before. It thought the capacitor was a resistor in auto mode. It's not that it didn't know any better. It's that's what came out of the dominant thing.

**Dave Jones:** So, what we've got here is our once again our complex plane, positive J operator, positive reactants. This is our reactants whether or not it's positive like this or whether or not it's negative like this.

**Dave Jones:** As I said, if it's positive in relation to the real resistance value RS, remember that. This is the real resistance component. It has no reactants whatsoever, zero phase angle.

**Dave Jones:** If you're measuring LCR meters can actually measure they can measure resistances as well, hence the R in the LCR name. Then, yeah, it'll be like a real resistance like that.

**Dave Jones:** There will be for an ideal component there will be no other capacitance or inductance, but in practice there always is. If you're measuring a real resistor like this with your LCR meter, there's going to be a small amount of capacitance in parallel with it that's going to be CP that we looked at before and then you're going to have LS like this and they're going to be your

**Dave Jones:** components. You'll have tiny little phase angles in there and and if you're lucky your LCR meter can just measure a smidgen of these parasitic values. So, anyway, where the measurement ends up, if it goes negative like this and the LCR meter goes, "Aha, I know this is a capacitive component." And if it goes positive, it knows, "Aha, this has an inductive component." But how much inductance?

**Dave Jones:** How much capacitance in relation to say a capacitor for example, this is the equivalent circuit the real equivalent circuit of a capacitor. It's got some ESR, some equivalent series resistance in here.

**Dave Jones:** It's got some lead inductance and you know, internal inductance of the package and all that sort of stuff. And then you've got the capacitance which is the factor that's going to dominate of course, and but then it's also got some parallel resistance, some leakage in here as well.

**Dave Jones:** So, how ideal this capacitor is depends on how close it gets to minus 90° like this. If it gets right down to minus 90°, it's practically a perfect capacitor.

**Dave Jones:** Well, that's the definition of a perfect capacitor is this will be completely 90°. There's no series resistance when you run those and do these measurements cycle thing here and then we spit out or plug the numbers into those equations and it pops out that well, no, there's no series resistance at all.

**Dave Jones:** There's no series inductance at all and there's no parallel resistance at all. It's a perfect capacitor. But in practice, it doesn't really happen. And likewise for inductors, if it's purely positive 90° like this, then it's a pure inductor.

**Dave Jones:** There is going to be no series resistance. There's going to be no any parallel winding capacitance. There's going to be nothing. It's a ideal inductor. But usually somewhere, you know, your component's going to be like somewhere like that or it's going to be somewhere like that.

**Dave Jones:** Now, the interesting thing is is that at this angle like this, your quality factor and your dissipation factor, which is just one on Q and vice versa, is equal to one.

**Dave Jones:** So, you'll have that at an angle for the inductive part and you'll have that at an angle for the capacitive part. And whether or not it's uh sort of like below, I guess we could call it, or above um that quality factor, the quality factor actually determines everything for both your capacitor and your inductor.

**Dave Jones:** It determines whether or not um the capacitance is dominating over your parallel resistance. So, in the case of the inductor up here, I've actually drawn like a large inductor here and a small resistor to show that the inductance, if it's if it has a quality factor greater than one, so if it goes in this direction, the quality factor Q goes greater than one.

**Dave Jones:** It can go up to hundreds, thousands, or whatever depending on how perfect uh your inductor is. And if it's under if you have a quality factor under one, it means that the resistance is dominating.

**Dave Jones:** It means that your component is mostly a resistor with a little amount of series inductance in there. So, if the quality factor is less than one, then the LCR meter goes, "Aha, I know this is basically a a resistor with a little bit of inductance." So, it will switch to displaying the resistance as the primary component.

**Dave Jones:** But, if the quality factor is above one, it'll think, "Ooh, this is mostly an inductor." And it will show the inductance on the primary display instead of the resistance.

**Dave Jones:** So, obviously that measurement that we did before of that capacitor in circuit, cuz there's other components in there as we'll talk about in a minute, that means that there was something else in circuit at frequency.

**Dave Jones:** Remember, we have a frequency component in here, and these values are going to be dependent upon the test frequency because your component and your test leads and everything else as we saw, our test leads have series resistance and they have series inductance.

**Dave Jones:** It upsets the apple cart, and the LCR meter thought, "Ooh, it's dominant resistor." Like this, because it was measuring that capacitance at a high frequency. Remember, the capacitive reactance is one on j omega c.

**Dave Jones:** Omega is that 2 pi f component. It has that frequency component. So, the LCR meter is going to try and figure out based on the value that's spat out with the equivalent circuit down here of the quality factor or whether or not it's a resistor down here with maybe a little bit of parallel capacitance and stuff like that.

**Dave Jones:** So, likewise down for the capacitor, if the capacitor has a quality factor greater than one, then of course it's going to be more towards an ideal capacitance, and it'll have a small amount of parallel resistance or leakage like that.

**Dave Jones:** So, that's how LCR meters work, and the takeaway from this is that the test frequency matters. It matters a lot. Basically, if you're measuring large values of capacitance, you want a lower test frequency because then it's not going to think that the resistor is dominating like this.

**Dave Jones:** It's not going to At a high test frequency, your capacitance is going to measure close to a zero relative to the range resistor. So, of course, the other thing is is that it has to know which range you're on.

**Dave Jones:** And you can auto range some LCR meters, but generally they'll do it like automatically based on, you know, they'll just like scan through and uh figure out um you know, whether or not it's a dominant capacitor or whether or not it's a dominant resistor.

**Dave Jones:** And if you choose a high frequency, well, it doesn't matter which range resistor you get, it's just going to think it's a resistor most of the time. And likewise for inductors, you want to have as high a frequency as possible so that it it appears more like a dominant inductor than it does a dominant resistor.

**Dave Jones:** So, hopefully I didn't put you off LCR meters there, but this is the fundamental concepts of how they work. As I said, um some, you know, lower end LCR meters might do it like cheating different ways to actually uh get these values, but any good quality LCR meter, in theory, this is how it's going to measure it and calculate all of those values and what things dominate based on

**Dave Jones:** your reference waveform here and your frequency and your range resistor matters. And it can matter a lot when you measure trying to measure components in circuit as we're doing in this video because all those extra components, it's not just the capacitor there, there's all these other components that are in parallel with it.

**Dave Jones:** Whether or not it's part of a power supply, whether or not it's a you know, a reset cap on a digital logic gate for a reset pin or something.

**Dave Jones:** There's all these There's all these other circuit elements surrounding the capacitor when you try and measure it in circuit. And that makes it really hard. That's why it's easy to confuse your LCR meter depending upon what other circuit configuration is around it.

**Dave Jones:** But as you saw, you can actually do a reasonable job of measuring our capacitors in circuit if you choose force it into the capacitance range so it knows, "Aha, okay, it's definitely a you know, I'm telling you this is a capacitor.

**Dave Jones:** So, you damn well do your best with this range resistor up here to try and measure it as a capacitor."
