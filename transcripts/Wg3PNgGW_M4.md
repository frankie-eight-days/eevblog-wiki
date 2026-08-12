---
video_id: Wg3PNgGW_M4
title: EEVblog #343 - Spectrum Analyser Tracking Generator Tutorial
url: https://www.youtube.com/watch?v=Wg3PNgGW_M4
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 36, "3": 55, "4": 67, "5": 83, "6": 95, "7": 112, "8": 124, "9": 143, "10": 160, "11": 176, "12": 195, "13": 210, "14": 226, "15": 245, "16": 264, "17": 279, "18": 298, "19": 317, "20": 332, "21": 345, "22": 358, "23": 373, "24": 393, "25": 407, "26": 423, "27": 438, "28": 457, "29": 477, "30": 490, "31": 503, "32": 519, "33": 531, "34": 549, "35": 564, "36": 580, "37": 595, "38": 612, "39": 628, "40": 645, "41": 662, "42": 676, "43": 693, "44": 706, "45": 729, "46": 745, "47": 760, "48": 781, "49": 802, "50": 819, "51": 836, "52": 854, "53": 870, "54": 889, "55": 908, "56": 927, "57": 943, "58": 957, "59": 973, "60": 991, "61": 1006, "62": 1023, "63": 1040, "64": 1056, "65": 1077, "66": 1094, "67": 1108, "68": 1127, "69": 1143, "70": 1161, "71": 1177, "72": 1196, "73": 1212, "74": 1225, "75": 1242, "76": 1256}
---

**Dave Jones:** Hi, if you saw my previous video, I got a package from Le Chee Hung and he sent me a passive probe, but I thought we'd take the board he gave me in the little RF box, the little shielded box, and

**Dave Jones:** have a play around with an LC pi filter. Why? I don't know. Why not? I just wanted to basically show off the performance of such a filter and how to use a spectrum analyzer basically with a tracking generator to get the

**Dave Jones:** response of such a filter like this. So, I'm on a website here. This is calculator edge.com and they've got an online filter for a low pass LC Butterworth pi filter. And if you have a look here, you can see it's pi shaped. If you just

**Dave Jones:** ignore L2, C3, and all the rest of those through there, if you just look at C1, C2, and L1, you can see it's actually a pi shape like that and that's why it's called a pi filter. It's also called a

**Dave Jones:** capacitor input filter because it's got a capacitor on the input. But, yeah, I think it's more commonly known as a pi filter due to the shape. So, I thought, well, what if you wanted to say do a LC filter

**Dave Jones:** pi filter like this? It's a single stage. We're only doing a single stage one cuz the board that Le Chee gave me only supports a single stage on there. So, let's say you wanted to do say a 20

**Dave Jones:** MHz filter. That'll be a 3 dB down, of course. Cutoff frequency of filters is usually always measured at the minus 3 dB point. And let's do 50 ohms because our spectrum analyzer tracking gen output and spectrum analyzer input is

**Dave Jones:** all 50 ohms. So, well, that's the impedance of the load. So, the number of components we want is three. So, we've got a three-component design here, and let's calculate what values. There are standard formulas for this. It's going

**Dave Jones:** to vary depending on your uh PCB uh charac- parasitics and uh stuff like that, but we get a value of not a 795 nano Henries. Let's convert it to micro Henries, which you're probably more familiar with. Um 0.8 micro Henries and

**Dave Jones:** 159 pico Farads or puff as it's called in the trade. Um now, I don't have that exact value. I've only got, say, a 1 micro Henry inductor in my standard kit. So, let's call that, say, 15 MHz. Let's try that again.

**Dave Jones:** Recalculate it. There we go. Bang. 1 micro Henry. Pretty close. And uh 212 pico Farads. Let's change that to a standard, you know, E12 type range. You can get a 220 pico Farad capacitor. I'll have those in my kit. So, um

**Dave Jones:** let's build up a pi LC low-pass filter with 220 pico Farad capacitors, both of them, and a 1 micro Henry inductor and see what happens. We should be able to measure a -3 dB cutoff point of around about 15 MHz, give or take, based on the

**Dave Jones:** component tolerances and some parasitics on the PCB as well. Let's give it a try. So, here's our little low-pass pi filter here. We've got our 1 micro Henry inductor there. We've got a couple of uh links here because there were extra

**Dave Jones:** components on the board there, and we've got our uh 220 pico Farad ceramic cap there and there. So, you can see the pi shape in that. This is the ground along here, and this is the um this is the input over Sorry,

**Dave Jones:** input over here, and output over here. Let's give it a go. So, what we're going to use here is our Rigol DSA 815 9 kHz to 1.5 GHz spectrum analyzer with tracking generator option. And this is absolutely vital. You need one of these

**Dave Jones:** tracking generator options to measure the frequency response, the frequency performance of filters and other circuits like this. So, if you're going to buy a spectrum analyzer like this, this is like a 13 $1,200 base model without the tracking gen, but

**Dave Jones:** spend like an extra 300 bucks and get that tracking generator option. Because if you don't get that, you can't do any of this or it's incredibly difficult. So, the tracking gen makes is well worth the money, trust me. Now, what this

**Dave Jones:** tracking generator does is that when the spectrum analyzer takes the sample at a particular frequency, because instead of an oscilloscope, which is time domain, this is frequency domain, it at a particular frequency which it's measuring that signal at, it outputs that exact same

**Dave Jones:** frequency on the tracking generator output as it sweeps across. So, effectively, this is an RF sweep generator. It It starts at the low frequency and goes all the way up to and it depends on the displayed frequency. You know, if we're over the full range

**Dave Jones:** like we are here, 1.5 GHz, um 750 MHz center, basically from zero to 1.5 GHz, then it's going to sweep over that entire range on the tracking generator output. And it's that sweep, frequency sweep, which allows you to get

**Dave Jones:** the frequency response of your particular circuit under test. Anyway, what we're going to do is turn on our tracking gen here. I don't know why that button, you can't just press it twice and it automatically switches it on. I

**Dave Jones:** don't know, that just would have been nice. Anyway, we've switched on our checking tracking gen here. Our level's going to be 0 dBm. Fine. We don't want a power sweep off the power sweep. We just want a constant

**Dave Jones:** output voltage level from this thing. So, we'll go into frequency Well, we'll go into span here and we'll set full span. So, we're doing our full 1.5 GHz span here. So, our center frequency down here is 750 MHz.

**Dave Jones:** We're going over the full 1.5 gig range or thereabouts. So, let's go into amplitude. And by the way, I've got the just the tracking gen joined straight through to via a 50 ohm coax straight to the RF input. And of course, the

**Dave Jones:** tracking gen output is 50 ohms and the RF input is 50 ohms impedance as well. And that's what we calculated for our pi filter here. So, we're going to go into amplitude here and we'll just auto scale that.

**Dave Jones:** And look at that. Isn't that funny? What did we expect? We actually expected Well, here's the reference level over here, 0 dBm. We expected that to be flat across the whole range because we've just got a coax in there. We've got no other

**Dave Jones:** circuit. So, in theory, you know, this coax can you know, it should be able to do 1.5 gig. I mean, not all coax's can, but you wouldn't expect to see all that garbage in there. You'd expect a flat

**Dave Jones:** line. Why aren't we getting it? And the answer's really easy. Go check the manual for this thing. And if you take a look at the tracking generator option output, you can see it's rated for plus minus 3 dB output level over the entire

**Dave Jones:** 1.5 gig frequency range. So, it's not a great tracking gen at all. And that's not terribly surprising. It's not easy or cheap to make a completely flat and linear tracking gen from, you know, DC to daylight, uh basically 1.5 GHz. I

**Dave Jones:** know that's not daylight to the RF guys out there. Heck, you know, anything under 1 GHz is DC as far as they're concerned, but anyway, it's not that easy or cheap. So, what you're buying here is a spectrum analyzer. And you're

**Dave Jones:** not really buying that good a tracking gen. You're only paying a couple hundred bucks for it. Its performance is not going to be completely ruler flat over the entire frequency range. And this is the actual performance of it, believe it

**Dave Jones:** or not, because um the spectrum analyzer uh input, of course, is going to be pretty good. This is a, you know, a reasonably decent uh spectrum analyzer. So, if we had another, a better, a ruler flat tracking gen, we would see a ruler

**Dave Jones:** flat line. But, because tracking gen's not that great, this is what we get. Now, how do you measure? I mean, you know, we're the amplitudes here, I mean, it's specked in the manual as uh plus minus 3 dB. So,

**Dave Jones:** it's well within that. I mean, you know, we're only talking sort of a peak around 1.3 dB there and uh minus 1.7 or thereabouts uh dB over the entire range. How do we fix that? Well, Rigol know that uh this is a problem. So, you

**Dave Jones:** go into tracking gen here and you use what's called the normalize function. And that basically compensates for the poor performance of the tracking gen. So, we can what it can do is it can store this waveform and then subtract it

**Dave Jones:** from your final signal to give you a, you know, a proper response. And it has this capability built in. It's easier and cheaper to add this capability in software than it is to uh design and build a ruler flat uh

**Dave Jones:** tracking gen on this thing. So, what we want to do uh you use your coax directly input and output. So, before you take any measurements, you compensate for the tracking gen. So, you just store it and you turn normalization

**Dave Jones:** on. Nope, it didn't like that. Press it again. There we go. It's updating the reference trace and bang, there's our ruler flat response. So, now we can disconnect this and we can plug our circuit in series with it and test

**Dave Jones:** it and it will automatically compensate for that stored reference. It'll normalize it. So, what we want to do here is go into frequency, set our set of frequency to say 10 MHz or thereabouts. And the frequency span, okay, let's just do 20 to start off

**Dave Jones:** with. And we'll take our little filter here and we'll plug it in series here with the input. Ta-da, there it is. Okay, so we've got a filter in here and let's try and measure the response of this thing. And bingo, look at what we

**Dave Jones:** get. Look at here's our filter response dropping off there. This garbage here, um I'm going to say that's um from setting up the uh reference um level. We did it over the full uh span range. We could uh redo the uh

**Dave Jones:** normalization across a smaller range and we should be able to get rid of that, but I just want to show you the roll-off. So, let's just assume that that's flat, okay? So, let's change our um our frequency span here. It's currently

**Dave Jones:** set to 20 MHz, so this is 0 to 20 MHz here with a center frequency of 10 MHz and let's expand that and we can see where it gets -3 dB down. Actually, we'll try and measure that with one of the markers.

**Dave Jones:** So, how we do that is we just hit marker over here and we've got different we've got various markers in various modes, but here's the little marker number one and it tells us and we can adjust use the knob over here

**Dave Jones:** to move that back and forth. So, we want minus 3 dB and we're expecting around about 15 MHz for that and what do you know? Pretty darn close. Look at that. Ah, magic 15.06 MHz. So, we've accurately measured the minus 3 dB

**Dave Jones:** roll-off point of our LC pi filter here. So, let's have a look. Let's expand. Let's go into span here and expand this range. I'll use my knob again and you can see the changing value. I could type it in. I can just

**Dave Jones:** type in a value on the keypad here if I wanted to, but let's just use the Let's just increase it to 30 MHz and you can see it's going off here. So, let's rescale that. Let's just auto scale

**Dave Jones:** that. There we go and let's expand that span again. Let's go up in frequency. You can see it's rolling off nicely. Beautiful. And it's starting to level out actually. There we go. We're up to 100 MHz span now. So, this is 100 MHz and you'll

**Dave Jones:** notice it's actually going back up. Look at that. And if we keep increasing our span, we're at almost 300 MHz now. Look at this. Isn't this interesting? You know, we're at 600 MHz span there and you can see the fall off of our

**Dave Jones:** filter, but it hasn't just continued to fall off like a brick wall, it's actually recovered, it's reversed, and is, you know, we're talking minus 17 dB to minus 15 dB up here. I mean, it was down to around a minus 27 dB there, but

**Dave Jones:** it's gone back up, and it has a response like that. And of course, if we go over the full 1.5 gig range of the spectrum analyzer, it rolls off, and it recovers like that. Why is it doing that?

**Dave Jones:** So, what's causing it? Let's take a look at our circuit here. We've only got basically uh four components on this entire thing. I know, you're thinking, "What, there's only three?" No, there's actually four. Um there's the inductor, of course. We've got our two capacitors,

**Dave Jones:** plus the circuit board as well. Remember, circuit board is a component like anything else. It has a dielectric constant, acts as inductance, capacitance, all sorts of stuff like that when you start getting up into high frequencies, but this is FR4. It's going

**Dave Jones:** to be more than good enough, especially at the uh um 70 MHz that we're uh seeing um this thing uh change on us. So, we've we're using um uh NPO ceramic capacitors here. They should be more than good enough uh for this

**Dave Jones:** sort of frequency range. So, you go, "Aha, the inductor." So, let's take a look at the inductor I used. And this is what I used. I had it in my kit here. It's an NLC 453232 uh 1 uh micro Henry, but it's a

**Dave Jones:** basically a um a power inductor. It's not designed for RF stuff. So, what we're seeing is the self the low-ish self-resonant frequency of this inductor. It is not a good inductor at high frequencies. It doesn't work as it's supposed to. And that's

**Dave Jones:** exactly what we're seeing on the spectrum analyzer here. So, we can see it here. There, I've got my marker there. You can see the little one going around, and it's uh reversing there at about 65 MHz. So, that's going to be around the

**Dave Jones:** self-resonant frequency of this inductor, i.e., where it rolls off and stops becoming the inductor you expect it to be. And then you get in to all sorts of parasitics cuz it's wire wound. There's a, you know, there's a whole

**Dave Jones:** bunch of wires in there wound around, and you get into winding capacitance and all sorts of stuff, and it's not working as the inductor it was down at these lower frequencies below 70 odd MHz there. Now, let's try a slightly

**Dave Jones:** different one, the NLC 322522. Once again, 1 micro Henry. Let's see if that changes that self-resonant frequency point. And you can really see the wire-wound nature of this one. The other one was fully encapsulated, so we couldn't see it. But this one here, you

**Dave Jones:** can clearly see the inductive winding inside this thing and exactly how many turns it's got. And if I just disconnect the filter here, so we've got nothing going in, you can, bingo, see the noise floor of the unit down here. Okay, I've

**Dave Jones:** soldered the new inductor in there. Let's plug it in and see what we get. We're exactly the same as before. Uh what? No, we're still on around about 70 MHz there. Bummer. I was hoping we'd see at least a bit of a difference. But

**Dave Jones:** I managed to uh uh steal this one off a old VGA video card, and I measured that at 500 nano Henry. So, half a micro Henry. So, it's, you know, it's going to adjust our frequency somewhat. All right, let's

**Dave Jones:** give this one a try. Here, and let's have a look. Ah, bummer, still around that 70 MHz mark. All right, let's try one of these SMD ferrite beads. Once again, salvaged from a board. I have no idea of its

**Dave Jones:** value, but let's see what it does. Hey, it's uh not better. The frequency has changed though. We're now about 125 MHz before it starts bending back there, but certainly its performance is pretty terrible up at the high end up

**Dave Jones:** here. I mean, you know, we're only talking Well, it's you know, peaking around minus 7 dB. Awful. But really all that experimentation is for naught because we are not going to escape this characteristic notch response. You can see how it goes down

**Dave Jones:** and then it recovers. That's called a notch response in our low-pass filter there. So, it's it's not working nearly as good as a low-pass filter up at the high past a certain frequency point. So, when you're designing one of these

**Dave Jones:** filters, you will design it for that particular frequency which you're trying to attenuate at best there because after that, it's just going to recover and it's going to have that notch type response. And this is actually characteristic of one of these LC pi

**Dave Jones:** filters. You can't escape it. The only way to escape that notch response is to change to a different type of filter, either a T type filter or a multi-stage filter or something like that to really attenuate this high-end stuff cuz it all

**Dave Jones:** has to do with the parasitics of the inductor and the parasitics of the board and everything else in there. It's just totally characteristic of a very simple LC pi filter. Nothing you can do about it. Hey, but it was fun trying a few

**Dave Jones:** different values anyway. And I'll just show you another thing with the noise floor here. I've got the full frequency range here, 1.5 GHz. So we're going into span, we've gone full span there. And we're uh in the amplitude we're auto scaling that

**Dave Jones:** and you can see it's, you know, round about minus 65 dB. I've got no normalization on here and you can see that it's, you know, around about that figure, but there's an RF preamp you can switch on. And if you go into RF preamp here and

**Dave Jones:** switch that on, you'll notice noise floor, bang, goes much, much lower. And if you want to know if the tracking turn switching on the tracking gen makes a difference to the noise floor with the preamp on, very little. Watch this.

**Dave Jones:** There we go. It's just slight You can see a slight difference there by switching on the tracking gen. So that'll be the internal crosstalk. So I hope you like that. That was just a bit of a play small play

**Dave Jones:** around with an LC pi filter and measuring its response on a low-end spectrum analyzer with a tracking generator output. There are other ways to do it, of course, with your sig gen and your oscilloscope and stuff like that. Um and there are ways

**Dave Jones:** to do it without the tracking gen option in spectrum analyzer, but it is actually quite hard. But with that tracking gen option, you can see how easy it is. And perhaps we can follow this up later with that different things, but it's worth

**Dave Jones:** playing around with something like this. It was good fun. So I hope you liked it. If you want to discuss it, jump on over to the EVblog forum. And if you do like it, give it a big thumbs up. Catch you next time.
