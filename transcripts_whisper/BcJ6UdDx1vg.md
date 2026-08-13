---
video_id: BcJ6UdDx1vg
title: EEVblog #859 - Bypass / Decoupling Capacitor Tutorial
url: https://www.youtube.com/watch?v=BcJ6UdDx1vg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 37, "3": 49, "4": 69, "5": 85, "6": 105, "7": 121, "8": 137, "9": 157, "10": 173, "11": 189, "12": 209, "13": 229, "14": 245, "15": 261, "16": 281, "17": 297, "18": 309, "19": 325, "20": 341, "21": 357, "22": 373, "23": 393, "24": 413, "25": 429, "26": 445, "27": 461, "28": 481, "29": 493, "30": 509, "31": 529, "32": 545, "33": 561, "34": 577, "35": 593, "36": 609, "37": 629, "38": 645, "39": 661, "40": 681, "41": 701, "42": 725, "43": 745, "44": 765, "45": 781, "46": 797, "47": 813, "48": 829, "49": 849, "50": 869, "51": 885, "52": 905, "53": 921, "54": 941, "55": 961, "56": 977, "57": 993, "58": 1009, "59": 1029, "60": 1049, "61": 1073, "62": 1089, "63": 1105, "64": 1129, "65": 1141, "66": 1161, "67": 1177, "68": 1197, "69": 1213, "70": 1229, "71": 1245, "72": 1261, "73": 1277, "74": 1289, "75": 1305, "76": 1321, "77": 1341, "78": 1357, "79": 1373, "80": 1389, "81": 1405, "82": 1421, "83": 1437, "84": 1457, "85": 1469, "86": 1485, "87": 1501, "88": 1517, "89": 1533, "90": 1549, "91": 1569, "92": 1585, "93": 1601, "94": 1621, "95": 1637, "96": 1657, "97": 1673, "98": 1693, "99": 1709, "100": 1725, "101": 1741, "102": 1765, "103": 1781, "104": 1801, "105": 1817, "106": 1829, "107": 1849, "108": 1869, "109": 1889, "110": 1909, "111": 1929, "112": 1945, "113": 1961, "114": 1977, "115": 1993}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to answer the question, why do you use multiple bypass capacitors? You've probably seen this in many circuits, that you've got your chip here, you've got your power rail, and you might have more than one bypass capacitor just on that one chip, or even just that

**Dave Jones:** one power rail on a chip that might have multiple power rails. For example, it's not that uncommon to find like a one microfarad cap, a hundred nanofarad cap, a ten nanofarad cap, or one nanofarad cap. You can have two, three, or four caps in parallel.

**Dave Jones:** Why? What's going on here? Hmm, let's answer it. Now I actually covered this very briefly back in episode thirty-three, back when I was in the old lab, but it was only like a minute or two explanation, so I thought we'd go more in-depth here.

**Dave Jones:** And I've actually done a video not that long ago on why you would use multiple electrolytic capacitors in parallel, and I came up with a huge list of nine different reasons why you would actually put more than one electrolytic capacitor in parallel. So click here

**Dave Jones:** if you haven't seen that video, it goes in-depth, and it does some thermal testing as well to actually prove it. Now, we're not talking about electrolytic capacitors here, this is a different scenario, we're talking about different value capacitors for, in particular, chip bypassing.

**Dave Jones:** Now, there are very good technical reasons why you would actually want to put multiple capacitors for bypassing applications in parallel, in particular, different values and different types of capacitors. But before we answer that, we have to actually look at what is bypassing. Now, in an ideal world, you wouldn't actually

**Dave Jones:** need bypassing, it'd be completely pointless. Because let's take a look at a chip like this, okay? It does whatever this chip happens to do. We've got a battery or a power supply here, doesn't really matter, and we've got a load, so it's consuming power inside the chip

**Dave Jones:** to do various switching and things like that, and that's what I've shown here with these two MOSFETs in there. Let's assume it's a CMOS chip, doesn't matter. And so it's doing internal switching, it's doing all its business, and we've got a, like a totem pole output, it's driving loads, it's driving

**Dave Jones:** lines, it's doing whatever chips normally do. Now, let's assume that we had a 5 volt supply here, let's go old school, none of this 3.3 volt rubbish. And this 5 volts, in an ideal circuit, you're gonna get 5 volts directly on the pin of this

**Dave Jones:** chip in here, because there's no internal resistance in the power supply, there's no internal resistance in the battery, whatever you happen to be using, there's no internal there's no resistance on the PCB tracers that you're using, there's no inductance, there's no nothing, it's just an ideal world, and our

**Dave Jones:** ideal chip, everything's hunky-dory. You don't need bypass capacitors, and every other chip on your PCB as well, it's also gonna get exactly 5 volts on that pin, it never moves, it's rock solid, so you don't need any bypassing in an ideal world. Unfortunately, we don't live in an ideal world.

**Dave Jones:** In the real world, unfortunately, everything has resistance, everything has inductance, everything has capacitance, all these parasitic elements, and take your power supply for example, you can't get a perfect power supply, it's gonna have some equivalent series resistance, a resistor in series with it.

**Dave Jones:** Your PCB tracers going from your power supply, like your power supply input connector on your board, for example, to your chip, or to multiple chips, the PCB tracers, they're gonna have resistance, they're gonna have inductance, every piece of wire has inductance, no matter how small, it's gonna have

**Dave Jones:** capacitance down to ground, but we won't look at that in this case. So, what's gonna happen if we have no bypass capacitor on our VCC power pin of our chip, our 5 volts, if the chip is doing nothing, and it's just static, okay, yes, we will get a straight, we will get

**Dave Jones:** just our 5 volt line on there, but the chip is switching, it's doing stuff. There's lots of capacitance inside the chip, capacitance takes switching currents and things like that, so you're getting all these pulses of current. So, our waveform is not gonna be straight like this on our

**Dave Jones:** VCC pin, it's gonna, it might jump up and down like this depending on the switching inside that thing. And then we've got our load as well, our load is powered through the VCC pin through that top transistor up there to actually drive the load, whether or not it's sinking current or sourcing current, so that's

**Dave Jones:** gonna contribute as well. And, hey, depending on the value of these tracers here, it can, you can actually get significant dips and it can drop below the operating voltage of the chip and start causing strange weird things. This is sort of like a gross generalization, but

**Dave Jones:** this is what sort of thing can happen if you've got no local bypassing on your chip. But one of the big problems is not so much the resistance of the tracers, it's more to do with the inductance of the tracers, especially the higher frequency your chips get.

**Dave Jones:** Even, you know, high frequency can be a megahertz or so. Look at an old, you know, computer board from the 1970s or 80s, you know, with hundreds of chips on them. They've all got a bypass cap next to each particular chip because of the inductance

**Dave Jones:** of all the power tracers going there. And remember, we won't go into details but remember, an inductor actually resists change in current. So if your chip or your load suddenly decides it needs to switch, your inductor goes, oh no, I can't change that quickly, I can't do it.

**Dave Jones:** So you're going to get these huge dips and problems and all sorts of stuff. So it all just becomes really nasty and your 5 volt supply for your chip, your power supply, is not the solid power supply you're expecting. So that's why we add in

**Dave Jones:** a bypass capacitor in here like this, right at, as close as possible to the pin of the chip. Because why does it have to be as close as possible? Because you're trying to avoid the inductance in the line here, and every trace has inductance.

**Dave Jones:** So the further away you put your bypass capacitor from the chip the greater the inductance and then causes all sorts of problems when your chip starts to switch at high frequencies. So the goal of when you're bypassing is to try and produce a low impedance, low inductive

**Dave Jones:** supply element. Remember, capacitors store charge so they charge up and then when your chip switches suddenly and it requires a gulp of current, it comes from the capacitor instead of way, way back on the other side of your PCB which has all these long inductances in series and all sorts of stuff

**Dave Jones:** it comes directly from the local capacitor. So it minimizes the amount of inductance and resistance in series with it so that bypass capacitor can supply that little gulp of current that your chip suddenly needs without being affected by the rest of your PCB layout and all

**Dave Jones:** the other parasitics. So let's take a quick look at what actually happens to an output pin here for example, which is really important because it's driving other chips as well as part of your system. So if you get issues on that output signal, it can cause corruption, the other chip may not read it properly

**Dave Jones:** all sorts of issues like that, and you may have actually seen this. Let's take a look. So what we've drawn is another waveform like this in, of course the ideal world, your output will switch from 0 volts up to 5 volts here, it'll be absolutely perfect, there'll be no ring in, there'll be no

**Dave Jones:** overshoot, no undershoot, nothing. But of course, I use those keywords there overshoot and undershoot and ring in. What they're caused by is the inductance in the power supply here even if you've got local bypassing bypass capacities, there's going to be a little bit of inductance in the trace

**Dave Jones:** because you can't put it right on the pins, there's going to be a little bit inside the chip with the bonding wires, for example, that actually, you know, because your die is like inside this, they've got to have the little bonding wire which goes

**Dave Jones:** over inside the chip, that's got a little bit of inductance, and all that can actually lead to ring in on your signal like this, and you've probably seen that before, and then you can get some undershoot down here like this, and causes issues like this

**Dave Jones:** it's all to do with bypassing, and the higher frequency content you've got, the more this becomes a problem and I'm not just talking about the signal frequency itself, it could be you know, 1 kHz, a 1 kHz square wave for example, not high frequency, as you would measure it

**Dave Jones:** on a frequency counter, but remember that a changing digital signal like this, it's not to do with the fundamental frequency, the time difference between here and here, it's to do with how fast the rising and falling edges are, the faster the edge, you know, if it's a really

**Dave Jones:** slow edge like that, it's going to have low frequency content, if it's a super duper fast edge that switches in a nanosecond or something like that, then it's going to have really high frequency content, that's your basic Fourier theory and all that sort of stuff, so even a 1 kHz

**Dave Jones:** signal can actually have this real high frequency broadband content in there, that causes all this ringing, and when you've got a complex system with many chips and everything else, well it can cause a major problem, even if you've only got a single chip solution

**Dave Jones:** like this, if you don't bypass the caps, and it's not getting clean power then internally to the chip, you're still going to get all this effective ringing and things like that, due to the bonding wire inductance, your PCB trace inductance, and everything, your ground inductance here, it's not just your

**Dave Jones:** power line up here, you're going to have some inductance in here, you're going to have some inductance down here like this, so that's why it's important to have your bypass cap directly on the pins of the chip as close as physically possible, and of course if you actually probe your power supply, you'll actually

**Dave Jones:** see this sort of stuff happening here okay, you might have your 5 volts, but then you'll see the ringing on the power supply, like that, so you'll get all these little, you'll see that if you actually probe correctly there's high frequency probing techniques you need to use and everything else, but if you probe that

**Dave Jones:** you can actually start seeing the switching on there, and the, if you have no bypassing or not very effective bypassing your ringing can be very big and cause all sorts of problems so I know what you're saying, Dave, that's all great, but why not just

**Dave Jones:** pack one big bypass capacitor on there that can handle the most amount of current that this thing is going to, pulse current that this switching chip in the system is going to take? Why do you need to have multiple different values and different types

**Dave Jones:** of capacitors on there? Aha! Trap for young players, this is where we have to get into what a capacitor actually does and its impedance versus frequency. Let's go So in a real capacitor, which I've shown in the previous video on electrolytic capacitors, if you maybe want a bit more detail, it's not

**Dave Jones:** just a capacitor. Inside a capacitor, here it is. A real capacitor has an equivalent series resistance, which you might be familiar with the ESR, which is a constant resistance value essentially in series with the actual capacitor itself, but crucially, also inside a capacitor is a little

**Dave Jones:** tiny bit of inductance as well. Lead inductance plus construction inductance and various things and that's called the ESL, the equivalent series inductance. So it's far from just an ideal capacitor. It's an RLC circuit. What happens with RLC circuits? Well you can get resonances and you can get all sorts of funny things happening

**Dave Jones:** and as you should know from your basic component theory for capacitors and inductors, they actually have an impedance or what's called a reactance or capacitive reactance and inductive reactance at a certain frequency. They effectively have like an AC resistance so to speak and these are the standard formulas for your capacitive

**Dave Jones:** reactance and your inductive reactance and they change with frequency. Capacity is inverse with relation to frequency and the inductive reactance goes up with frequency and we're going to have a total impedance for the capacitor so a total AC resistance of the capacitor is actually going to be the ESR

**Dave Jones:** which is that constant fixed value in there plus the impedance of the capacitor at whatever frequency you're talking about plus the impedance of the inductor at whatever frequency you're talking about. So if we go over here and have a look at this graph here, we've got the impedance of the capacitor

**Dave Jones:** the bypass capacitor, it's in ohms of course, so the impedance in ohms versus the frequency here and you get this for a real bypass capacitor, well a real capacitor we just happen to be using in a bypass situation, a real capacitor is going to have

**Dave Jones:** a response curve something like this and this is sort of like an industry standard way to show it, it is not actually a straight line like that because of course a capacitor will actually have infinite impedance down at DC here so it'll taper up like this.

**Dave Jones:** Now if we didn't, if this capacitor didn't have any inductance in it at all, of course this line would not be here and you'd just get a slope going down like that which changes with frequency and you can plot that yourself, put the formula into Excel

**Dave Jones:** and you can do it yourself, it's standard basic component theory but as I said crucially that little inductor in there, it's tiny it could be like Pico-Henry's or something like that but at a particular frequency it's going to start to matter. Now the capacitive reactance operates like this but at some particular frequency

**Dave Jones:** here which is the resonant frequency of this RLC circuit using your standard resonance formula, that's where the capacitive reactance and the inductive reactance are equal and that is going to be the resonance point. At that point then the impedance of the reactance of the inductor

**Dave Jones:** starts to dominate instead of the impedance of the capacitor so hence why it reverses and the resistance starts to go back up and that's a very undesirable thing to happen you don't want this thing to go back up at higher frequencies, you want it to be down

**Dave Jones:** like this, why? Because as we talked about before about the series, effectively the series resistance, the series impedance you want the energy to come directly from the capacitor with no effect whatsoever, with no impedance in the path, no inductance in the path, but when you start adding this real inductance either

**Dave Jones:** inside the capacitor itself or outside of the capacitor with your PCB tracers, inside the chip with the little bonding wires everything else, then this can be a real problem, your impedance starts to rise and your bypass capacitor isn't acting like a good bypass capacitor anymore at these higher frequencies.

**Dave Jones:** And of course these higher frequencies in modern devices, say for an FPGA for example, which have huge densities and a huge amount of switching, huge amount of logic and multiple rails and they take huge amounts of current and everything else and they operate

**Dave Jones:** at extremely high frequencies, like you know, they can switch at hundreds of megahertz but the edges are even faster and you can get frequency components into the gigahertz range fairly easily. And if your reactance of your bypass, the impedance of your bypass capacitor starts to rise at these really high

**Dave Jones:** frequencies up here at hundreds of megahertz or a gig or whatever, then you're going to be in serious trouble. Your bypass capacitor may as well not even be there at these higher frequencies because, yeah, the capacitance is still there it's still got, you know, one microfarad or whatever it is, a lot of capacity, you can

**Dave Jones:** have a lot of energy stored in that one microfarad capacitor, but it's no good it can't get into the chip if there's this massive series impedance in series with the capacitor. It just can't deliver the energy when your IC actually requires it, give me a big

**Dave Jones:** pulse of energy. No, can't do it. Now I think I mentioned before that not only do you have different values here, but you have different packages as well, because the package actually makes a difference. As a general rule of thumb the smaller your package gets, the lower inductance

**Dave Jones:** it's going to have, the lower internal inductance here. So let's assume that this one is a 0603 for example, you know, a SMD package then if you've got an 0805, it's going to look something like that. It's going to have a higher value, so that

**Dave Jones:** could be 0805, and then you could have an, you guessed it 0402 package looking something like that. They're actually going to have different values for the different packages, so it's actually better for higher frequency stuff to use the smaller packages but of course the big question is why do they use different values?

**Dave Jones:** Well different values have remarkably different frequency characteristics as you'd expect. The bigger value capacitors, in this case say one microfarad for example, is going to have a resonant point at a much lower frequency, so it's going to cover the lower frequency range. It's going to have a lower impedance at a lower frequency

**Dave Jones:** once again, it's not this V shape, it's, you know, it's going to be something like this, right? So it's going to actually cover a much broader range at a lower frequency right down here, but eh, work with me. Okay, and then you're going to have different values for assuming like this

**Dave Jones:** all the same package for example, a 100n is going to be higher in frequency, and then a 10n again, and then a 1nf, and then a 100p if you want to, is going to be much lower. So what you get and the answer to the question why do you use multiple

**Dave Jones:** bypass capacitors, it's so you get the lowest impedance across the largest frequency range possible. So if you've got all three of these values in here, your final curve is going to look like this. Ta-da! So you've got a much broader lower impedance, so you've got a more effective bypass

**Dave Jones:** capacitance over a bigger frequency range. And that's why you do it. So there you have it, that was a bit longer explanation than what I intended, what was it, 20 minutes or something? To explain how bypassing works and why you use multiple bypass capacitors.

**Dave Jones:** I could have just jumped straight to this and said this is why, which is what I did back in episode 33 or whatever, but eh, there's good background information there to explain exactly what's happening here. So I thought, I hope you found that interesting, but hey, I think we might be able

**Dave Jones:** to reproduce this on the bench and actually show you. Could be a little bit tricky, but eh, let's give it a go. Now, ideally to measure this, we would use a network analyzer. Big expensive bit of kit, which I don't actually have here in the lab, I need to get myself

**Dave Jones:** one. But hey, we can use our red patea here, which you've seen in a previous video, and I'm now powering it from an external plug pack, 2 amp plug pack by the way, via the USB, which seems to have solved the rebooting issues I was getting

**Dave Jones:** before. Even though before, in the previous video, I was actually powering it from a USB 3.0 port, which is supposed to be capable of supplying 2 amps, but eh, I don't know. Anyway, so it's working a bit more reliably now, but I'm still having a few issues with the

**Dave Jones:** impedance analyzer app, which we're going to use today. So we're going to use 3 channels here, and here's a diagram of how it's actually hooked up. We've basically got a 10 ohm shunt resistor in there, and then the device under test. Now, the reason I'm getting this convoluted arrangement

**Dave Jones:** here with the bit of Vero board and the wires and everything else, is that you're probing in this sort of thing, and you're wiring, test cabling, is actually quite critical. If I actually ran coaxes off here and stuff we'd find that we'd be getting all sorts of issues

**Dave Jones:** in our impedance plot the higher up in frequency we go. So yeah, often, just dangling wires like that can be better. So I'm converting my SMA to BNC, then I'm converting BNC to banana, a binding post here. So I can just hook that up and it should be right.

**Dave Jones:** It's a little bit, you know, it's a bit crude but hey, we should be able to show the concept at least. Now the good thing about the Vero board here is that it has two convenient strips like this that allow us to put multiple capacitors in parallel.

**Dave Jones:** So I've got a cap in here, I've just been testing the thing to make sure it all works. And we've got our 10 ohm shunt resistor there, so we can just put as many caps in here as we want. But, with something like this, we're dealing with

**Dave Jones:** high frequency, we're going to go up to 60 MHz today, sweep it all the way up to that frequency. So what we want to do first is actually replace the capacitor with a shunt resistor in there, because we've got a 10 ohm sorry, we've got a 10 ohm shunt resistor, replace the capacitor with

**Dave Jones:** a resistor so that we can actually check to see our frequency response is flat and that we're not getting any weird effects caused by cabling or the test setup. So just like we discussed, what we want to get is an impedance versus frequency

**Dave Jones:** graph. So basically anything that goes up to tens of MHz, we should be able to see something like this. This thing's 125 Mbps, you know, analogue bandwidth, 50-60 MHz something like that, that'll be good enough to see various capacitors in parallel. Hopefully. Now you'll have to forgive me for not doing this

**Dave Jones:** live, so to speak, but not only does it save time, but trust me, I spent a lot of time dicking around with this thing, actually trying to get a result because the test setup is actually quite crude, had a lot of issues with the Red Pattaya software and things like that

**Dave Jones:** and the test feature, even with the short wires that I'm using, the BNCs make a difference, the adapters, all that sort of stuff all comes into play. So I didn't really engineer a proper setup for this, so I was actually lucky to actually get a

**Dave Jones:** usable result out of this. But I should be able to show you something here. So what we've got here is an impedance response graph just like we saw on the whiteboard there, impedance in ohms versus frequency there. In this case we're sweeping from 100 kHz up to

**Dave Jones:** 60 MHz on a logarithmic axis there. I tried to set it to start at a higher frequency, but it just wouldn't let me, I'm not sure what's wrong with the app. Anyway, you can see that started off at 100 kHz there and right down to DC, of course

**Dave Jones:** it started off as a nice perfect 10 ohms, exactly what you'd expect, so that just verifies that the system's working. But of course now the parasitics of our test setup come into this, and you can start seeing around about 2 MHz there or so, it starts to roll off and

**Dave Jones:** it's usable up to, say, 20 MHz might be usable. It's down to measuring 7.5 ohms or something like there, you know, good enough for ballpark. But at the higher frequencies of course then it becomes, you know, all the parasitics of the Vero board and everything test fixture come into play.

**Dave Jones:** You can see a bit of noise right at the high frequency, that's because there's not much signal to noise ratio there. But in this case that inaccuracy at the greater than 20 MHz range isn't that bad because some of the impedances, as you'll see, actually go up to

**Dave Jones:** hundreds of ohms and things like that. So, you know, it's kind of usable so I'll sweep it to 60 MHz, but just keep that in mind that, yeah, it's a little bit off up there. And I'll start out by showing you some large value capacitors.

**Dave Jones:** This is a 10 microfarad 1206 package ceramic capacitor, very typical large value bypass cap, and as you can see, it does have that characteristic V-shape response. As I said before, quite much broader than what we saw on the whiteboard, but it's there. You can see there's a resonant point

**Dave Jones:** about 1 MHz there, and then it tapers back up. Now here's a 10 microfarad tantalum capacitor, and you can see it's actually higher in value, goes up to like 1.75 ohms at, you know, 60 MHz or something like that. But you can see it's got a similar shape, similar sort of

**Dave Jones:** resonant frequency around 1.5 MHz. And now this is a, just as a curveball, 47 microfarad electrolytic capacity. You can see it resonates about, you know, 8, 9 MHz or something, tapers back up and obviously that big tail down at the end is due to some parasitics on the

**Dave Jones:** Vero board. Now here's a very typical 100 nanofarad 0805 bypass capacitor. You'll find in practically every product. And you'll see, notice that the impedance scale has now gone up. It's auto-scaling in this red patea software. It was a little bit annoying that I couldn't actually manually scale the thing to see the data.

**Dave Jones:** But it's changed significantly. We were talking about hundreds of millions before, but now down at 100 kHz we're talking like up over 15 ohms. Quite large value. No good for low frequencies. And you'll notice that the resonant point is now up to you know, around about 5 or 6 MHz.

**Dave Jones:** So higher than it was with that larger value capacitance. And now we'll take a look at a 10 nanofarad ceramic capacitor, same 0805 package but you'll notice that the Y scale has changed even, again by an order of magnitude. Down at 100 kHz, it's up

**Dave Jones:** over 150 ohms, or thereabouts. 10 times more than what it was before and you'll notice that now the resonant frequency is right up near 40, 50 MHz or something like that. In fact, this test setup isn't good enough because we're talking about, you know, much

**Dave Jones:** higher frequencies here. But as you can see, they are actually quite broadband. You know, tens of MHz for these values like, you know, quite low impedance. Now if we actually combine a 10 microfarad ceramic with a 100n ceramic and a 10n ceramic, you can see

**Dave Jones:** that we have, look, that rise around about 8 MHz there. So very similar to the combined peak response we got on the whiteboard. Now here's an interesting little trap for young players which we didn't discuss before, but what happens in reality. Now, you can see on the left hand side the same graph we had before

**Dave Jones:** of the combined 10 microfarads plus the 100n there, and you'll notice the big lump in there in the middle at around about 8 MHz or so. Now this is actually undesirable because look at the one on the right as we saw way before.

**Dave Jones:** This is just the 10 microfarad cap on its own, and you'll notice the y-axis are very similar. It's actually a better result just to have the 10 microfarad capacitor there. In this particular case, with these particular values, on this particular Vero board, with all its particular parasitics

**Dave Jones:** and everything, and the values, and the whole, and the test setup, and the whole works, it can actually be detrimental in some cases to put capacitors in parallel. You can form these resonant peaks there, and sometimes it might interact with your hardware in ways that you didn't intend.

**Dave Jones:** So you know, it's not just magic. You can't just put 10 different values and whack them all in. You know, you could actually get an issue with resonances between caps. So it's a potential pitfall. Just watch out for it. In this case it's not particularly bad, but look, just the 10 microfarads

**Dave Jones:** on its own would technically be better in this particular case. Now here's a better response if we actually combine 4 caps. A 10 mic, a 1 mic, a 100n, and a 10n. Once again, all SMD ceramics in various size cases. And you can see that that

**Dave Jones:** 8 MHz peak has gone away. It's, you know, still well you can argue that this is a bit better than the original 10 microfarads just on its own. But yeah, it's hard to see this because the higher frequency ones really need a higher frequency response test system, which we don't have here.

**Dave Jones:** And here's my 4 ceramics in parallel here. 10 microfarads, 1 microfarad, 100n, and 10n. Various different package sizes and the package sizes are going to make a big difference in terms of the ESR and the impedance response of the individual capacitor. It's not just capacitance value.

**Dave Jones:** Package plays a big part. So I couldn't really get lots of visually good results with just the SMD ceramic capacitors. They're just too good. So I got like a really poor axial, sorry, radial-leaded 47 microfarad electrolytic capacitor and put that in parallel with a

**Dave Jones:** 10n ceramic on there. And you can see that, you know, peak around you know, 15, 16 MHz or something like that. But the extra 10n ceramic brings the impedance of that way back down again at the higher frequencies which is desirable of course.

**Dave Jones:** And that little tail back in up after 40 MHz is just due to the test system as we saw right back at the start. But the 10n would allow much better high frequency performance into the hundreds of MHz and things like that, that the 47 microfarad electrolytic on its own

**Dave Jones:** it'd just keep going up and up and up and it'd be hundreds of ohms at that it'd just be way off the scale at that frequency. And you may as well not have it at all. So that's a reasonable example visual example of how combining those two caps actually

**Dave Jones:** can, you know, get a reasonably smooth response over a very broad range from 100 kHz right up to, you know, maybe a few hundred MHz or something like that, but we can't see it. But yeah, it would be quite decent performance over that big entire range.

**Dave Jones:** So you use the 47 micro for decoupling big heavy current bursts and the 10n for all the high frequency switching. Now here's a little interesting aside. You may have seen weird looking surface mount caps like this in a wide package like this. Well

**Dave Jones:** why? You may not have thought anything of it. Well these are actually special low inductive capacitors designed specifically for this application. Now if we have a look at this little snippet from an AVX app note on these low inductance or the evolution of ceramic capacitors here, you can

**Dave Jones:** see that say a 1206, your standard 1206 one has about 1200 pH or thereabouts of inductance right? But if you take that exact same size chip, the 1206 and you put the caps on the sides, the conductive caps on the sides instead of the ends, same size cap but

**Dave Jones:** 170 pH. And if we have a look at this TDK data sheet for their C series, their specific low ESL equivalent series inductance that we've been talking about, they're called reverse geometry. And they just put the conductive end caps actually on the side of the capacitor instead of on the ends, and it makes the world of

**Dave Jones:** difference. And if you're designing high frequency switch mode power supply or something, you might see real performance critical stuff where the bypassing is really going to matter then you might typically find these low ESL caps in there. So there you go, I hope you enjoyed that rather lengthy look at how

**Dave Jones:** bypass capacitors work and why you put multiple values and types in parallel. There's some real good reasons for it. And sorry I couldn't really comprehensively show this, this test setup is pretty crude, it's not the best thing, you really need a really high frequency

**Dave Jones:** high performance system and carefully laid out test setup and everything else. But hey, just with this we were able to see so it did actually take quite a lot of mucking around and trial and error just trying different caps and different sizes and packages and values and things like that

**Dave Jones:** just to try and get a response. And I probably, you know, ultimately could get a more realistic example of what I showed on the whiteboard there, but I hope you get, I hope that was good enough and you really get an idea of how it can really make a difference, especially at really

**Dave Jones:** high frequencies. You can imagine just, you know, extrapolate those graphs right out and assume we've got a perfect test system and can make one heck of a difference. Anyway, if you liked that video please give it a big thumbs up and all that sort of jazz, you know where to discuss it and links down below for data sheets and

**Dave Jones:** other app notes and things. Catch you next time.
