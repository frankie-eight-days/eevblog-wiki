---
video_id: 1xicZF9glH0
title: EEVblog #1085 - Bypass Capacitors Visualised!
url: https://www.youtube.com/watch?v=1xicZF9glH0
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 39, "3": 66, "4": 78, "5": 95, "6": 110, "7": 121, "8": 141, "9": 157, "10": 170, "11": 187, "12": 203, "13": 214, "14": 231, "15": 248, "16": 258, "17": 270, "18": 286, "19": 297, "20": 323, "21": 339, "22": 361, "23": 379, "24": 393, "25": 412, "26": 437, "27": 456, "28": 465, "29": 478, "30": 494, "31": 516, "32": 530, "33": 538, "34": 557, "35": 570, "36": 587, "37": 603, "38": 624, "39": 637, "40": 649, "41": 664, "42": 676, "43": 692, "44": 714, "45": 728, "46": 740, "47": 751, "48": 768, "49": 783, "50": 796, "51": 815, "52": 829, "53": 849, "54": 860, "55": 873, "56": 887, "57": 901, "58": 912, "59": 930, "60": 943, "61": 956, "62": 966, "63": 975, "64": 985, "65": 997, "66": 1012, "67": 1024, "68": 1047, "69": 1066, "70": 1078, "71": 1096, "72": 1115, "73": 1127, "74": 1142, "75": 1158, "76": 1177, "77": 1195, "78": 1204, "79": 1223, "80": 1233, "81": 1242, "82": 1263, "83": 1287, "84": 1303, "85": 1321, "86": 1333, "87": 1343, "88": 1355, "89": 1370, "90": 1394, "91": 1404, "92": 1423, "93": 1450, "94": 1476, "95": 1490, "96": 1512, "97": 1525, "98": 1545, "99": 1559, "100": 1569, "101": 1592, "102": 1605, "103": 1616, "104": 1627, "105": 1639, "106": 1655, "107": 1676, "108": 1693, "109": 1718, "110": 1728, "111": 1747, "112": 1768, "113": 1780, "114": 1794, "115": 1809, "116": 1821, "117": 1835, "118": 1852, "119": 1866, "120": 1887, "121": 1902, "122": 1913, "123": 1932, "124": 1955, "125": 1975, "126": 1986}
---

**Dave Jones:** Hi, I did a recent video on months in which I'll link in down below at at the end of this video if you haven't seen it and that's the process of in the particular case of the video I did removing bypass capacitors from a circuit to see if it still worked.

**Dave Jones:** I removed them one by one and ultimately yes, the circuit did still work but it really it was just for fun. It wasn't really a demonstration that you shouldn't use bypass capacitors in your circuit cuz I've done which I'll link in up here it'll be a YouTube card up here to a very popular 30-minute whiteboard tutorial on what are bypass capacitors, how they work, why you use different

**Dave Jones:** values of bypass capacitors in certain situations and I also do some practical demonstrations using a poor man's network analyzer to see the frequency response of that but I thought we'd follow on from this or really part two of the more technical tutorial side of things of why you want to use bypass capacitors and why you actually want to put them right near the components and loop area which I've talked about in the

**Dave Jones:** previous months in video and many other videos as well. So I thought we'd do a practical demonstration rather than the network analyzer one before with frequency responses and all that sort of thing.

**Dave Jones:** Actually get some bypass capacitors and actually put them in different places in a circuit and actually see the effect they have not only high frequency bypass capacitors but lower frequency bulk supply decoupling capacitors as well.

**Dave Jones:** So let's get into it. Now a practical demonstration of bypass capacitors really quite difficult to do on a regular like complex proper product PCB. It's much easier to do if you actually set up an experiment for it.

**Dave Jones:** So what I've got here is a just a single sided copper clad PCB. I haven't done anything to it. I could have you know used a double-sided board routed out and things like that, but it's much easier.

**Dave Jones:** I just use some uh copper tape here to simulate uh traces and have one big ground plane on the bottom. So, we're talking about transmission lines here, but we also talk about uh loop area and it just allows us to put the bypass capacitors in uh different locations along here and see um how it makes a difference.

**Dave Jones:** 5 V uh DC coming in here. Uh the green is the ground. That just goes to the uh big copper ground plane there. And the uh plus 5 V goes to this copper tape, which goes all the way up here to the top pin of a 1 MHz crystal oscillator.

**Dave Jones:** This is a standard crystal oscillator you should be familiar with here. This pin is uh soldered directly down to the ground plane. That's ground pin. The positive pin is soldered directly onto that input uh tape here.

**Dave Jones:** This is uh just a not connected pin. And the output is connected to this copper tape up here. And as I've uh shown in the previous video, I won't go over it again, but I'm using a proper um low inductance uh probing solution here with my 1 gig bandwidth uh Tektronix probes.

**Dave Jones:** You might be able to see that. I've just got a tiny little loop of wire in there so that I can actually connect my probe directly into there. So, we're going to have and the ground is a very short ground uh using the little probe wire attachment here.

**Dave Jones:** Very important if you want to get the best signal uh integrity possible, which is what we want to do here. And that's connected directly to the ground plane. So, we're getting excellent um high signal integrity probing solution.

**Dave Jones:** And then the output from that goes along this uh copper tape, which is 5 mm wide and it's actually around about 1.6 mm thickness. So, standard PCB and that gives roughly 50 ohms uh impedance and we've got that terminated in two 100 ohm resistors in parallel.

**Dave Jones:** So, it's terminated in 50 ohms, and then we've got the same low inductance probing solution there as well. So, the entire point of bypass capacitors, of course, is for digital systems which switch from 0 to 5 V, which we can see up here on the screen.

**Dave Jones:** Here's the output of the oscillator on channel one here, 0 to 5 V. It's only 1 MHz. The frequency actually doesn't matter. What we worry about is the transition time here, and it's reasonably fast.

**Dave Jones:** It's a HCMOS oscillator. So, we've got like 2 ns fall time, and the rise time's going to be similar. So, we just want something with a fast edge so that we can see the transitions on the power supply.

**Dave Jones:** So, what what we've got is a basic circuit here, which you can imagine is a product PCB, which you would design. You'd have your power input here. It'd go along some power traces to your digital chip, which you're particularly interested in.

**Dave Jones:** In this case, we've only got one, but it might be multiple chips in multiple systems, and then it drives an output load. In this case, it's driving a 50-ohm transmission line, 50-ohm load.

**Dave Jones:** So, we need that to actually get decent pulse currents. In this case, 5 V on 50 ohms so that we can actually get some large current transitions in the signal trace, and more importantly, flowing through the ground plane so that we can actually see the effect of bypass capacitors because bypass capacitors matter more for things that take large amounts of current when they're transitioning.

**Dave Jones:** And it doesn't have to be a resistive load, either. This trace down here will also have capacitance. And if this was dry if this was just a regular signal wire driving another, you know, CMOS TTL digital gate over here, that digital gate's got input capacitance.

**Dave Jones:** The trace has input capacitance to ground. And when when your signal transitions like this, you remember capacitive impedance uh formula that it actually acts for a brief period of time, acts as a low impedance or effectively if it if it's an infinite transition time like that, it's effectively the capacitor operates as a short circuit.

**Dave Jones:** So, even if you have no resistive loads, unlike what we've got in this circuit, if you've just got traces and capacitive input gates, all input gates have capacitance even if it is only a couple of picofarads, couple of puff every time you transition in your circuit, it takes a little gulp of current from your power supply.

**Dave Jones:** And that's what bypass capacitors are designed to help with. So, I'll briefly go over bypass capacitors again, but you really have to watch my 30-minute tutorial video to really understand what's happening there.

**Dave Jones:** So, I recommend you watch that first. This is more a practical demonstration, but you have basically two different types of bypass capacitors in a circuit. You have your bulk power supply capacitors, which generally goes right at the power supply input or at the output of a voltage regulator or whatever it is.

**Dave Jones:** And generally that will serve all the chips on the board. So, it basically stores charge and delivers it for the lower frequency type events in your circuit like, you know, the 50 100 hertz mains input ripple for example on a traditional linear AC bridge rectified power supply for example, it would smooth that out.

**Dave Jones:** Whereas bypass capacitors like 100 nanofarads or 0.1 microfarads that you typically put right next to each IC, just as sort of like an industry rule of thumb, these store charge which actually provide the energy for the higher frequency switching transitions which we get in here.

**Dave Jones:** So, what we're going to take a look at here is we've got some low frequency stuff happening here and we've also got some high frequency stuff happening in here.

**Dave Jones:** So, we'll be able to use the different bypass capacitors and we'll see how these handle the different types of scenarios. So, let's get to it. So, we've got absolutely no bypass capacitance on this circuit at the moment.

**Dave Jones:** It's just switching at 1 MHz with those fast transitions. It's not recommended. Don't not have any bypass capacitors in your design. And channel one here, the yellow waveform, as I said, is the output of the oscillator down here and that's the one we're triggering off.

**Dave Jones:** Whereas channel two, the blue one here, is actually the power supply pin directly on this chip. Because when you're looking at bypassing, you're concerned about in this particular case, concerned about the actual component, which is in this case transmitting or it could be the receiver chip over here, for example, that's actually receiving the signal or both of them.

**Dave Jones:** Anyway, we're concerned with that power supply rail. How stable is that rail relative to the switching currents that this thing is taking? In this case, every time the output goes high like this, it's got to drive that the 50 ohm load.

**Dave Jones:** So, we get it's basically drawing a big gulp of current like that. So, if you have a look here, we've actually got 200 mV per division here for the power supply.

**Dave Jones:** And that's a lot. Look, we've got maybe like 300 mV peak-to-peak of this low frequency ripple, we'll call it, even though it's like 1 MHz like that. Okay? It is still in this particular case, the lower frequency switching stuff.

**Dave Jones:** And that's quite a lot to have your 5 V rail vary by, you know, 300 mV peak-to-peak. That's a That's a lot of ripple on your power supply. That's horrible.

**Dave Jones:** That's because we've got no bypass capacitors on there. And And case, it's actually taking due to various parasitics uh in the circuit because we've got no capacitance whatsoever. It's actually taking what turns into a what looks like a sinusoidal waveform here.

**Dave Jones:** And also, you can see the droop in there. And if we actually change the scale on our channel two here and we move that up, we can see that that power supply corresponds directly with the droop in the output waveform.

**Dave Jones:** So, that's due to no capacitance and various parasitic capacitances and other things in the circuit, which we won't particularly worry about. And if we zoom right in at a 100 mV per division on our power supply, this is the high-frequency ripple there that we want to get rid of with our 0.1 microfarad high-frequency bypass capacitor near the chip.

**Dave Jones:** And it's the worst on the negative transition here. So, we'll concentrate on that. So, let's look at the effect of a 330 microfarad cap a bulk decoupling capacitor on the circuit.

**Dave Jones:** So, I'll put it down here right at the input where you'd normally have it. So, we expect this to affect the low-frequency ripple stuff. Get the polarity correct. And bingo, look at that.

**Dave Jones:** It goes away. Magic. That's the effect of bulk Look, there's virtually none of that ripple and crap that we saw before. Yeah, there's high-frequency noise there, but that's not the job of this capacitor.

**Dave Jones:** So, it's doing an excellent job there of getting rid of that low-frequency stuff. That's what your bulk decoupling's for. But check it out. Even though our low-frequency stuff is gone, our high-frequency stuff is still in there.

**Dave Jones:** It doesn't get rid of that. But aha, let's put this near the chip up here, which is good design practice, and see what happens. Here we go. I'll put it directly on the probe and directly on the pin and the ground plane of this chip.

**Dave Jones:** It doesn't get any better. There we go. It reduced it a little bit. It has some effect, of course, cuz it is working as a high frequency bypass capacitor, but this electrolytic, due to its various uh parasitic inductances and whatnot inside and the ESR inside this thing, it's just not good enough as a high frequency bypass capacitor.

**Dave Jones:** It's really only good for bulk decoupling. Watch my previous video to see what's actually happening inside this capacitor. But, let's do exactly the same thing with a 100 nF uh film capacitor, which they work quite well as um bypass capacitors.

**Dave Jones:** So, let's whack it in here in exactly the same location as before. That one is a bit more effective. But, let's try a more traditional uh ceramic capacitor like this.

**Dave Jones:** There we go. That one's done a reasonable job, but not much better than the film cap, really. Probably about the same. Let's show the effect of that bypass capacitor again.

**Dave Jones:** The .1, notice the height of the uh spikes up there. They're just off uh screen there. But, if you lower that down, look, it gets rid of those effectively, but the .1 microfarads on its own is not enough to get rid of the uh low lower frequency ripple inside there.

**Dave Jones:** You need both capacitors in this particular case. So, I'll clean that up again. Here's the power supply ripple without the cap and with the cap. There you go. You can see there's still a bit of high frequency stuff in there.

**Dave Jones:** That's going to have to do with the uh type of cap and the uh inductance of the leads and other uh traces and, you know, parasitics like that. But, you can see that it got rid of a good bunch of that um high frequency switching stuff.

**Dave Jones:** The reason why this little .1 microfarad one doesn't get rid of the low frequency stuff and the big 330 mic does is because this can store a lot more charge, so it can deliver that charge to smooth out that high current stuff that we've got in there.

**Dave Jones:** If we didn't have a very low impedance load like we've got here and it wasn't uh drawing much current, then we wouldn't actually get that low frequency stuff. And I can show you that by lifting the legs of those resistors there and all we get is the high frequency uh switching.

**Dave Jones:** So, that's what would happen in a circuit if you were just driving another digital gate that uh just had uh switching capacitance. It's just because it's driving a capacitive line, it's actually uh or and/or a transmission line in this case, but effectively every trace is a transmission line, but we won't get into that.

**Dave Jones:** Um that's what's causing this ringing here cuz there's not sufficient bypass, so that um once again, we're on a 100 mV per division. That's a awful lot of ripple happening on your 5-V power supply.

**Dave Jones:** It's horrible. It's got all sorts of ramifications in terms of uh signal integrity, glitches in your circuit transitions and ground bounce and all sorts of you know, weird and wonderful stuff which we won't get into.

**Dave Jones:** But, if we connect the load, bingo, we've got that uh lower frequency uh switching ripple as well due to the high pulse currents actually or high uh transmission driving currents going into that load.

**Dave Jones:** Now, watch the size of these high frequency uh switching transitions on the power supply rail as we move our bypass capacitor closer and further away from our device being decoupled and probed.

**Dave Jones:** So, if I put it fairly close up there, look at that. There's There's our signal level. You can see where they are. And if So, as I slide it towards there, hopefully you'll be able to see that.

**Dave Jones:** There you go. As we get closer and closer to the chip, it lowers in amplitude. And if we get as close as we possibly can, bingo, that's as low as we can get with this particular bypass capacitor because it's got the particular type and the leads on there.

**Dave Jones:** Remember, leads like this always have inductance. That's why surface mount bypass capacitors close to the chip are going to be better than through hole ones. Whereas the bulk decoupling capacitor, it's not going to matter where on there we actually put it.

**Dave Jones:** It's going to do the same job up the top as it does down the bottom. Because it's due to the higher frequencies, it doesn't matter about the lead length or the trace length here.

**Dave Jones:** But there is a limit to that. If we actually go and put this, even use a bigger one, I'll use a 2200 microfarad one. If I put that here, it's going to do exactly the same thing.

**Dave Jones:** It's going to get rid of that ripple. But if we go put it right over here, there is a limit to the effectiveness of this thing. There you go.

**Dave Jones:** It changed a little bit, but really doesn't do a huge amount cuz we've got all the extra inductance of the leads here and everything else and it's closer to the lower impedance source over here.

**Dave Jones:** So, it's going to be placed reasonably close to the low impedance ground over here. Can't be at the other end of the cable right over here. It's not nearly as effective.

**Dave Jones:** And by the way, we don't need 330 microfarads to get rid of that either. We can use a in this case a half a microfarad here, another film cap, and we can put that there and it's going to do a quite respectable job of getting rid of that as well.

**Dave Jones:** You can still see there's a little bit of low frequency stuff in there, but not much. So, you know, even that does a reasonable job. You don't need to overdo it on your bulk decoupling capacitor.

**Dave Jones:** It all depends on the amount of bulk current actually being taken in your circuit and at what frequency. So, let's now try the best possible bypass that we can get for this particular scenario, which is a basically a leadless and that's what they are a leadless capacitor service mount capacitor 1206 soldered directly to the ground plane and the pin.

**Dave Jones:** Let's give that a whirl. That's probably the best we can do. It's still going to go through the ground plane. It's still going to go up the lead into the package and the ground lead on the other side is quite tall on the package, but anyway, this should be the lowest amount of high frequency switching noise that we get.

**Dave Jones:** Check it out. That's absolutely amazing. Look at that. We got not much there at all. You remember what we had last time we had it was maybe the same height there, but there was some more undershoot there.

**Dave Jones:** That is really good. So that's obvious, you know, you could eventually get rid of most of it. You can't really eliminate it entirely because ultimately there are going to be package limitations even surface mount even leadless surface mount packages like those capacitors.

**Dave Jones:** They've still got some inductance in them. The ground plane still has some inductance. The bond wire if you're using a surface mount chip, the lead of the chip has some inductance in it as tiny as it is and then the bond wire going over into the chip internally, that's got some inductance in it etc.

**Dave Jones:** etc. And it's and also the probing solution's got a little bit there. So a little bit here, a little bit there, but that's still pretty good for that sort of leaded package there.

**Dave Jones:** I like it. So if we combine that with our bulk decoupling here, we've gotten rid of almost all of our switching stuff. Nice. So I know what you're thinking, Dave, what if we actually change the value of the capacitor?

**Dave Jones:** Does that make a difference in the high frequency content? If you use a lower value cap, will that do it? Because I mentioned in a previous video why you want to use or you might want to use different value capacitors in parallel for different frequency components.

**Dave Jones:** Well, let's try our 0.1 microfarad one again. There we go. Reduces it like that. Okay, in this case I've got the white reference waveform there. I stored the 100 nanofarad cap, and now we'll put in the 2.2 nanofarad cap in exactly the same location.

**Dave Jones:** As you can see, there are some differences there, but basically it's it's not really going to change the peak. The peak, um, which is around about there, is basically the same with both of them, but the 100n had more undershoot like that.

**Dave Jones:** Whereas if you put both of them there, you should be able to combine them. So, that, you know, having the two bypass capacitors on there can make a difference.

**Dave Jones:** Different values, 100 nanofarads and 2.2n. That's the combination because the smaller capacitor, the 2.2 nanofarad, will take care of some of the more higher frequency components, but it all interacts as I explained in the previous video with the lead inductance, like all the package inductance and the parasitics in the circuit and everything else.

**Dave Jones:** So, what do we talk about when we talk about loop area in terms of current flowing like a complete path like this? Well, we have our power supply input over here.

**Dave Jones:** We have our driving chip. We have our load, and we have our return ground path. So, let's assume that we have our bulk decoupling capacitor right at the input here.

**Dave Jones:** Well, when you talk about in this case switching currents and the high frequencies involved, this is how transmission lines work. Well, currents in a circuit will always take the lowest impedance or lowest resistance path from the source through the circuit and then back to the ground terminal like this.

**Dave Jones:** So, if we have our bulk decoupling capacitor over here, for example, then our current will flow up here into our chip. It'll flow along here like this, and then it will actually return from this ground point here, and it'll take the lowest impedance or lowest resistance path, and for low frequency stuff, lowest DC resistance path will basically be straight through there.

**Dave Jones:** I know it it distributes through the PCB and everything like that, but it's basically going to take a direct path. So, all that right around there, that is our loop area, and that's the where the current has to flow.

**Dave Jones:** And here's the trick, the larger the loop area, the larger the physical distance and circle like that, and the higher frequency you go, the more it's going to act like an antenna, and it's going to radiate electromagnetic or EMI electromagnetic interference.

**Dave Jones:** It's going to just generate all that, and your device may not pass your CE, FCC compliance, which I've done a separate video on. So, you always want to minimize this loop area.

**Dave Jones:** Now, for low frequency bulk decoupling, it doesn't matter. That's why it doesn't matter where you put it. Effectively, it still works even if you put it right over here to the input.

**Dave Jones:** And effectively, that's where in a ground plane, that's where it's going to flow start and end at. So, that's okay. But high frequency stuff, uh it's a different ball game.

**Dave Jones:** For high frequency stuff, we're shown that a bypass capacitor is more effective over here, right on the chip itself. So, effectively, this capacitor becomes the source for all those high frequency transitions we've seen, and it'll do the same thing.

**Dave Jones:** It'll flow out the your high frequency currents will flow out here like this, but your return path won't be back over to your large decoupling capacitor I here, because it's a lower impedance at that higher frequency to to actually travel under that I've shown it sort of like next to the transmission line but it's actually under the transmission line and you can prove this you know mathematically and field

**Dave Jones:** equations you know all sorts of weird and wonderful advanced theory to us show that this is the case but the current will actually flow back under that transmission line.

**Dave Jones:** So that becomes your loop area. So here's where good high frequency design comes in and why you put your high frequency bypass capacitor right next to the chip because you're minimizing that loop area for generating electromagnetic interference.

**Dave Jones:** If you put this bypass capacitor well away from the chip over the here then it has no choice but to follow that as the lower impedance ground and if you do that bingo you've got this large area again at high frequencies and when you have that large loop area wah wah wah wah you're probably going to be starting to fail your EMC compliance.

**Dave Jones:** This thing's going to be radiating to buggery and it can also pick up things as well the larger the loop area. Now I'd love to actually show you that on the board and I actually was hoping that I'd be able to actually show you the current and the mapping flowing through the board under here like this using my aim I probe a 520 positional current probe which has a magnetic head on it

**Dave Jones:** but really you can't pick up the currents. If you put it on here there we go directly on the trace you can actually see the switching currents in the trace but unfortunately it's down in the noise floor for the actual current path but all is not lost yet.

**Dave Jones:** Look at this. If I take my bypass capacitor and put it over here or anywhere and probe right on the leg. Look at that. Bingo. You can see that all that current is flowing through the lead of that poor little bypass capacitor.

**Dave Jones:** So, all that So, that shows that it has to be flowing across the ground plane like this and all the way back to that cap. So, the closer we put it over here, then the smaller the loop area we're going to get.

**Dave Jones:** Now, unfortunately, this doesn't have the bandwidth to really show the detail in the high frequency switching stuff which we've been used to. But, as I showed in the Months in video, there's an IBM research paper which I'll link down below where they've actually visually mapped the currents in the ground planes like this.

**Dave Jones:** And you can check that in link down below. But, here's a screenshot of that. And it's very cool. Unfortunately, we don't have the tools to do that. So, it really does matter where you put your bypass capacitor in the circuit and why it should be near the chip.

**Dave Jones:** But, there's a whole lot more involved in this. It's not always as simple as that. But, that's why it's a good, like, you know, rule of thumb just to, you know, have a bypass capacitor.

**Dave Jones:** Its value is not that critical in most cases next to each or, you know, nearby groups of chips in your particular digital layout. But, that can vary depending on whether you got a full ground plane like this one or whether you not you've got a double-sided board and it's all filled in and higgledy-piggledy and grounds running everywhere.

**Dave Jones:** That's a different kettle of fish. And I hope to show that better in a follow-up video to this. I hope it works. All right. So, what we're going to do now is take a very crude and quick look at what this thing is radiating.

**Dave Jones:** I've got my how you doing antenna hooked up to here. Yes, it is a piece of solder. No worries. I've got my Rigol spectrum analyzer here. Got a 500 MHz span on here.

**Dave Jones:** I got it switched off, so that is like our baseline at minus 77 dBm there. Don't worry about the setup. This is not, you know, absolute first class type measurement system.

**Dave Jones:** We just want to see if we can see a difference by putting the bypass capacitors on here. Okay, that's our baseline around minus 77 dBm. Okay, it's just come on.

**Dave Jones:** This sweep here will show us our spectrum. There we go. Pretty filthy. Look at this So, this is 100 MHz, 50 MHz per division. So, at around about like 125 MHz is a big broadband content in there.

**Dave Jones:** At around about what, 230 MHz or something, we've got a some content in there and some higher up stuff there. So, that's with no bypassing at all. All right, now I'm going to put on the 100 microfarad bulk decoupling cap.

**Dave Jones:** We're still going to get a lot of that high frequency content. It's changed it a little bit. Look, we've still got some content here at 250 odd MHz and we've still got all this broadband content down there around the 100 MHz mark.

**Dave Jones:** Now, let's just put our on our .1 microfarad bypass cap. We've got to wait for the cycle to start again. Here it goes. And bingo, a quite well, now our content around there has narrowed, but we still have some content up at 250 MHz.

**Dave Jones:** Why is it so? Well, let's take a look at the scope screen. It'll tell us. All right, this is with our .1 microfarad bypass cap. If you have a look, we're at 2 nanoseconds per division.

**Dave Jones:** What is uh the period there? Well, it's about 4 nanoseconds. What's that? Eh, it's round about that 250 MHz mark that we saw. So, that uh small amount of content there at the 250 MHz mark is going to be due to that uh high frequency stuff there.

**Dave Jones:** And if we put both bypass caps on there, it's going to be not nearly as high around that 250. We've basically neutered that out now. But, you can see how if we remove the bypass caps, it's actually shifted frequency somewhat because the parasitics are all different in there.

**Dave Jones:** So, it's going to uh ring at a different uh frequency. So, that also can cause a problem if you try and mix your bypass capacitors. I've explained this in the previous video.

**Dave Jones:** And um due to the parasitics inside these capacitors and the parasitics in the trace and the lead lengths and everything else, um you could potentially get these to resonate at a frequency that you don't want them to resonate at.

**Dave Jones:** So, it's not always, you know, 100% guaranteed the best idea to put multiple caps in parallel. Or even choosing the wrong value bypass cap could choose could form a resonant tank circuit at a particular frequency and you could end up getting a spike on your spectrum.

**Dave Jones:** And well, that comes down to Murphy. Usually happens on a Friday afternoon. So, let's go for broke and put on our bulk decoupling cap here and our two smaller ones reasonably close.

**Dave Jones:** There we go. And let's see how this spectrum changes. We've got to wait for it. See how it just knocks it all down at the uh between like uh you know, 200 MHz and 500 MHz.

**Dave Jones:** You can see how it's changed drastically by adding those bypass caps. You know, if I take them off, boom, the crap starts coming back. So, all this horrible broadband content here and here is caused by all this ringing in here.

**Dave Jones:** Look at it. It's just just horrible. And the amplitude is, you know, incredibly high. So, it's it's just radiating like buggery. And well, that kind of stuff, yeah, you're probably not going to pass your uh CE FCC uh emissions compliance.

**Dave Jones:** So, I've put that uh 1206 ceramic uh capacitor back and you can see that our um high frequency uh switching noise there is like bugger all, really. Um but we're still getting this content right up here at like 125 odd megahertz.

**Dave Jones:** But yeah, everything else is reasonably low. And that's with our 100 um that's with our bulk uh decoupling cap on there. If we remove the bulk decoupling cap, nah, it doesn't really affect any of the uh that bulk high frequency content at 125.

**Dave Jones:** And if we switch it off, of course, you can see that it all buggers off. So, um all that content is being radiated by our uh circuit under test.

**Dave Jones:** And of course, we've got the 1 megahertz uh fundamental oscillator as well um spewing out the stuff. So, it's not just the uh high frequency ringing on there, but you could definitely correlate the high frequency ringing to uh that uh what was it, you know, 250 odd megahertz uh peak on there.

**Dave Jones:** And all this stuff matters. I mean, it's, you know, these maximum peaks matter when you're testing um EMC compliance. And if we have a look at our 1 megahertz fundamental here on a 10 megahertz uh span, so we're 1 megahertz uh per division there, there's our fundamental at 1 megahertz, then the harmonic at 3 megahertz, 5, 7, 9, and so forth.

**Dave Jones:** So, I hope you enjoyed that video. It was a bit longer than I expected, but hopefully it shows the difference between bulk decoupling capacitors and the higher frequency ones and having multiple ones in parallel in terms of not only signal fidelity over here, but also in terms of loop area and how that actually generates electromagnetic interference.

**Dave Jones:** So, hope you enjoyed that. If you did, please give it a big thumbs up and as always discuss down below and the other videos will be linked in at the end somewhere here.

**Dave Jones:** Catch you next time.
