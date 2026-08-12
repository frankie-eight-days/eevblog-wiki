---
video_id: uLIr1eFjY2s
title: EEVblog #548 - EMC Pre-Compliance Conducted Emissions Testing
url: https://www.youtube.com/watch?v=uLIr1eFjY2s
source: youtube-asr
timestamps: {"0": 1, "1": 23, "2": 42, "3": 60, "4": 79, "5": 97, "6": 121, "7": 138, "8": 160, "9": 183, "10": 195, "11": 211, "12": 219, "13": 238, "14": 255, "15": 271, "16": 282, "17": 302, "18": 333, "19": 356, "20": 366, "21": 384, "22": 399, "23": 413, "24": 428, "25": 447, "26": 463, "27": 476, "28": 490, "29": 503, "30": 515, "31": 530, "32": 538, "33": 553, "34": 563, "35": 582, "36": 593, "37": 603, "38": 620, "39": 631, "40": 641, "41": 660, "42": 680, "43": 699, "44": 720, "45": 732, "46": 745, "47": 759, "48": 772, "49": 784, "50": 798, "51": 814, "52": 823, "53": 835, "54": 850, "55": 863, "56": 873, "57": 889, "58": 910, "59": 920, "60": 936, "61": 951, "62": 966, "63": 991, "64": 1005, "65": 1019, "66": 1030, "67": 1041, "68": 1054, "69": 1062, "70": 1071, "71": 1079, "72": 1096, "73": 1108, "74": 1120, "75": 1136, "76": 1150, "77": 1165, "78": 1178, "79": 1192, "80": 1205, "81": 1222, "82": 1233, "83": 1249, "84": 1258, "85": 1279, "86": 1292, "87": 1304, "88": 1312, "89": 1325, "90": 1335, "91": 1346, "92": 1359, "93": 1378, "94": 1388, "95": 1401, "96": 1413, "97": 1426, "98": 1441, "99": 1456, "100": 1475, "101": 1486, "102": 1497, "103": 1521, "104": 1540, "105": 1552, "106": 1565, "107": 1576, "108": 1588, "109": 1608, "110": 1616, "111": 1628, "112": 1639}
---

**Dave Jones:** Hi, this will be just a relatively uh quick follow-up video to my previous mailbag one where um LD from uh techbox.net uh sent in this very nice uh line impedance stabilization network, which is used for EMC pre-compliance testing uh for in particular uh conducted uh measurements instead of radiated uh measurements, which we'll get into.

**Dave Jones:** So, I thought I'd do a quick video showing you how to do some rudimentary pre-compliance testing with one of these uh line impedance stabilization networks or listen's um and a cheap bottom-of-the-range Rigol uh DSA815 spectrum analyzer.

**Dave Jones:** Now, uh pre-compliance testing is a big deal for um anyone really, any manufacturer manufacturing any electronic product that you want to sell in the commercial market in pretty much um any country in the world, at least if you, you know, care about uh doing it legally and correct.

**Dave Jones:** And you've probably seen these symbols around, this uh CE mark and this FCC mark here, and in Australia this uh C-Tick symbol here. Now, uh different countries have various standards, the CE standard, this is um EMC compliance, electromagnetic uh conformity.

**Dave Jones:** Basically, in the European uh Union have that standard, in uh America it's the FCC, in Australia it's this uh C-Tick compliance standard. So, depending on where you want to sell your product into what markets, um you may have to uh test your product against these various standards to get this mark on your product.

**Dave Jones:** And uh it can cost thousands to tens of thousands of dollars to get your uh product tested. So, you've designed your widget like this uh mains plug pack here, and you you know you've done all the proper design um rules and you know what you're doing, and you're pretty sure it's not going to radiate much and uh you know, it's not going to be susceptible to outside interference even

**Dave Jones:** if you care. Um and you know, you go to get the thing EMC compliance tested, and wah fail. You forgot something, and it's failed the um very stringent uh requirements or very specific requirements for any one of these particular things.

**Dave Jones:** There are more standards than this, of course, and it depends on the type of product, which we won't go into. Uh the details are uh are enormous, but uh when you design your product, if you fail that pre-compliance testing, uh sorry, not pre-compliance, proper compliance testing, then you'll have to re-spin your product, or figure out what's wrong first, and then re-spin your product, and get it tested again.

**Dave Jones:** And to do that over and over again on a trial-and-error basis is a real pain in the ass. So, any smart company will want to do called uh in uh pre-compliance testing, and you can do that in-house with, as I said, one of these uh line uh impedance stabilization networks for conducted measurements and a cheap ass spectrum analyzer, which you can get these days like this Rigol one.

**Dave Jones:** But, there are several types of emissions that uh your product can actually uh emit. So, we have to talk about those quickly cuz we're only going to look at one today.

**Dave Jones:** Now, I got this diagram from uh Wikipedia. Thank you very much to that Steel Pillow cuz it quite nicely illustrates the four different uh coupling noise coupling uh or emissions coupling mechanisms from your device here, which we'll uh call the source.

**Dave Jones:** One of the major ones, of course, which everyone thinks of uh when they think of, you know, EMC uh compliance and things like that is what's called radiative emissions.

**Dave Jones:** And you're probably familiar with this, you know, your electronic product has lots of switching frequencies in there, very uh fast sharp digital signals uh which uh emit very, you know, broadband uh radiative, you know, noise emissions and things like that.

**Dave Jones:** So, you know, pretty much any product unless it's completely sealed in a metal can with nothing coming in, nothing coming out, and the metal can's 100% effective over the whole frequency range or the desired frequency range, then pretty much your product is going to radiate electromagnetic interference out.

**Dave Jones:** All those little PCB traces, everything inside acting as little antennas and woof, out it comes. And we're not going to look at this one today, but that is the one of that is the major one that everyone thinks about and is a big deal with EMC compliance.

**Dave Jones:** But the other one fewer people know about is conductive emissions, and many products will have to be tested for conductive emissions as well. And this is what we'll cover today.

**Dave Jones:** There are two others, of course, there's capacitive coupling from your source to your victim over here as it's called, and there's also inductive coupling as well. But because inductive and capacitive coupling are near field effects, pretty much they are only covered they're only required to meet some sort of standard in very specific cases for products.

**Dave Jones:** So, most products will not be tested for these near field effects, but they will be tested for radiate radiative interference and or emissions and conductive emissions. So, even if your product was battery-powered like this inside a nice die-cast metal chassis like this, and you know, it's got the lid sealed on and everything, well, in theory, then you wouldn't have any radiated emissions or conducted emissions cuz there's no cables coming in and out of

**Dave Jones:** it. But that's not a very useful product, is it? Usually there's got to be cutouts for screens and things like that so it can actually radiate signals out. Or in this case, even if we had something like this and it was completely shielded like that, bingo, we've just broken that shield with our BNC here, and noise from inside, any switching noise, can couple onto the signal and onto the coax, and bingo, out

**Dave Jones:** it comes. And that's called conductive emissions cuz it's conducting along the copper cables into and out of your product. And take for example the plug mains plug back here.

**Dave Jones:** If this could this could be completely metal shielded till the cows come home, and you know, it may not have any radiative uh in emissions to speak of really, but you've got the mains cable coming in, and you've got the DC power cable coming out.

**Dave Jones:** So, in that case, if this was completely shielded for radiative stuff, your conductive stuff could kill you, and you might fail your compliance testing. So, to do conductive pre-compliance testing, we need one of these uh listen's or line impedance stabilization network.

**Dave Jones:** And I'll explain why it's called that in a second. This one is from uh TechBox, and send it in. It is I'll provide the link down below, and you can buy it from them, or you can make your own.

**Dave Jones:** So, what this is designed to do is insert in series with your power cable coming in. And your power uh comes in here, and then this end here plug what this end these two terminals plug into your product.

**Dave Jones:** And what it does is it AC couples off the signal into your spectrum analyzer there, and inductive filter here basically provides a fixed impedance, hence the name line impedance stabilization network, because basically your supply over here is an unknown impedance.

**Dave Jones:** You don't know what that's uh going to be. It could vary or whatever. It's no good, especially when you're doing that standards testing, if your source varies. So, uh all these uh compliance testing standards specify a specific 50 ohm network like this.

**Dave Jones:** So, this is what it does. This provides a fixed 50 ohm line impedance that you can do a controlled testing over over a specific frequency range which we'll see in a minute.

**Dave Jones:** And it just taps off the AC signal. And a good listen device like this one will also contain that surge suppression as well. We've got some 5 volt TVS diodes in here to protect our spectrum analyzer from any surges on the power supply here.

**Dave Jones:** And there's a gas discharge tube and a MOV over here. So, it's pretty well protected. Otherwise, you've got to be careful when you power up your product if it's connected to your delicate RF input of your spectrum analyzer here.

**Dave Jones:** You know how it's always got that you know maximum value. This one's pretty good at you know 50 volts of DC maximum, but some of them you've got to be real careful you don't blow your expensive spectrum analyzer.

**Dave Jones:** And there are various standards for these line impedance stabilization networks. One of them is the CISPR standard here. And you can see that the standard actually provides what the impedance of this listen network is supposed to be.

**Dave Jones:** Here's the upper and lower limits. And you can see this one is actually designed to fit you know fairly much in the middle of that. So, this one actually meets the requirements.

**Dave Jones:** So, having a standards compliant listen box like this absolutely essential for any conductive emissions pre-compliance testing. Now, a proper EMC compliance test facility will have all a proper shielded room to do all this in.

**Dave Jones:** They'll thoroughly meet the requirements. They know what they're doing. But if you're doing simple pre-compliance in your lab, then you know this is a basic best practice way to do it.

**Dave Jones:** And the standards do actually specify this and dimensions and things like that. You start out with basically a horizontal and a vertical ground plane. At the very least you should be using in horizontal ground plane like this with your device under test um up on an insulated wooden uh well some sort of you know insulated uh table like this.

**Dave Jones:** There are as I said uh standards for you know it must be X distance away from the planes and you know things like that but at least one horizontal ground plane on the bottom.

**Dave Jones:** You don't necessarily have to use the vertical one. These ground planes just stop capacitive coupling to uh other uh devices and uh things like that in the room and then you've got your listen device down here.

**Dave Jones:** Very short low impedance coupling because if that's a high impedance if you use a big long lead on there um then you know that isn't a very good uh grounding uh point over the frequency range so it has to be very short very closely connected to that ground plane.

**Dave Jones:** Device under test isolated and then you tap off to your spectrum analyzer. In a proper EMC uh facility this would be outside of the shielded uh chamber and things like that but we won't go into details.

**Dave Jones:** All right. Now what we're going to test here very simply very crude me so don't hold me to task over this okay. It's just an example of pre-compliance uh basic pre-compliance testing.

**Dave Jones:** Little uh USB uh charger one of these crappy little USB chargers in a non-shielded box so it's going to be radiating stuff but of course we're only going to be uh testing the conducted emissions of this thing and I've got myself a ground plane although in this instance it's really not going to matter uh much at all.

**Dave Jones:** You can do it uh basic testing without a ground plane and we've got a power supply up here. There we go. That uh powers our uh 12 volts goes into uh the source part of our uh listen box here and we've got our coax coming out to our spectrum analyzer there.

**Dave Jones:** Rigol DSA 815 and we'll show you how to set that up and uh this just uh mounted above the ground plane here by a certain amount otherwise you just rip out the ground plane and put it on the bench, and I've got the ground the source point of you don't want to ground this side here, you want to ground the source side to your grounding plate on the bottom.

**Dave Jones:** So, that's the setup. Now, I'll show the spectrum analyzer setup in a minute, but as you can see, we are getting a spike here. Now, I've got it disconnected, so it's not powered at all, but it is, you know, still connected through to the device under test side of this, and you'll notice that we're getting a spike here.

**Dave Jones:** That's a We're going from 150 kHz to 30 MHz span at the moment. So, that's like, you know, 25 MHz or something. And if I disconnect this, we'll find that the There we go.

**Dave Jones:** It vanishes. So, that Now, with disconnected, we can get ourselves a baseline. Although, you can see how at the low end over here, it is We do have some noise right down at the low end there.

**Dave Jones:** And if we disconnect our coax from our listen device, there we go. That's our noise floor. So, you can take that noise floor as a reference and actually subtract that out later if you want to, but we're not going to bother with that today.

**Dave Jones:** All right, so here's how to crudely set up our spectrum analyzer for this basic pre-compliance testing. It will, of course, depend entirely upon your device under test, your test setup, what version of the standard you're using, etc., etc.

**Dave Jones:** But, I'll show you a basic one. Basic one would be 150 kHz to 30 MHz frequency range. So, the first thing we want to do is go into frequency there.

**Dave Jones:** The start frequency we want 150 kHz down there, and our stop frequency is 30 MHz already set up. Now, we also want to go into our bandwidth detector, and our resolution bandwidth, we want to go into that.

**Dave Jones:** So, there it is. Currently set to 9 kHz, and that's what we want it set to for this basic frequency range. Now, the filter type here, uh, Gaussian or EMI, uh, this actually this spectrum analyzer has a specific EMI filter which we want to use if we have it.

**Dave Jones:** I think it might even be an a software optional extra, but you don't necessarily have to do that if you're using the, uh, Gaussian, uh, filter as we'll see in a minute.

**Dave Jones:** And if we go into amplitude, we don't want any input attenuator at all at this stage. So, we'll leave that set to 0 dB. Now, the really important thing is our detector type there.

**Dave Jones:** Uh, for a very quick, uh, first pass measurements, you want to send it to positive peak there. Quasi-peak is what we're going to do for more, uh, detailed measurements of this thing which, uh, takes a lot longer to, um, scan and give you a result.

**Dave Jones:** But the positive peak, that's what we want with our EMI filter if you have it. And what that positive peak detection type is going to do is basically going to give you the worst case at each, uh, frequency point, the worst case value.

**Dave Jones:** And that's really all we care about, you know, does it go over the limit or not? That's pretty much it. Now, for the CISPR standard, uh, EMI testing, the units are always going to be in dB microvolts.

**Dave Jones:** So, we want that set up so our vertical scale there is, uh, 0 dB reference point is 1 microvolt. So, for example, if we're getting 1 mV, a signal was 1 mV in amplitude, then that would be 60 dB above up there.

**Dave Jones:** So, our reference line's down there. This is our inherent, uh, noise floor of spectrum analyzer setup here, and I think we're ready to go. Almost. Now, one thing we can do to see if we're, uh, passing or failing a basic limit is to set a reference level up here to show us whether or not we're pass/fail.

**Dave Jones:** We can do that on this spectrum analyzer or spectrum analyzer different. Some will have it, some won't. I can go into trace pass/fail here. I've already, uh, set it up, so I won't bore you with the details, but I'll turn it on.

**Dave Jones:** and basically it gives us a reference line there and the CISPR 25 standard I just a generic one won't go into details, but it's basically 1 mV reference level across this particular frequency range.

**Dave Jones:** So, 1 mV as the example I used before is 60 dB. So, we want to go into the setup there and you can edit these data points and the amplitude there there it is 60 dB is our reference level at the upper and lower frequencies.

**Dave Jones:** So, it draws a straight line. You can actually set like an envelope in there, but we just want a straight line basically. So, here's our waveform and that if it goes over when we turn this thing on if our signal goes over that purple line there.

**Dave Jones:** Wah! Wah! Warning Will Robinson where we could be exceeding our limit. So, this spectrum analyzer pass fail thing's actually quite good. We can go in there set upper and lower limits, but as you can see I've got a 60 dB which is the 1 mV dB microvolts which is the 1 mV level crude by the standard here and we can set those at both points and now we are

**Dave Jones:** ready to go. We're ready to turn this sucker on. So, here's our noise floor. I'll connect my coax to the listen device and still haven't applied power and you can see that right at the low frequency down in there it's jumped up and you can go have a look at that, but anyway, here we go.

**Dave Jones:** I've got a 12 V supply here. I'm going to plug in my USB charger and let's see what we get. Once again from 150 kHz to 30 MHz with our CISPR 25 standard limit of 1 mV.

**Dave Jones:** I'll plug her in. Tada! Look at that. Once again, we got that peak that we saw before and you can see there's a bit more broadband noise up at the high end there.

**Dave Jones:** You know, that 20 to 30 MHz region up there, but you know, there's the standard. So, you know, we're well below that. Look, and I'll dis- oh disconnect my coax again so you can see that.

**Dave Jones:** So, you can see that's our noise floor of our system, and then it jumped up just a bit at the high end, but what really concerns us is this low end down here, which is above that purple line.

**Dave Jones:** So, we're in trouble down at the low frequency, down at, you know, the hundreds of kilohertz to a megahertz range. So, we want to zoom into that and see what's happening.

**Dave Jones:** So, I've got my marker there, and uh oh, you probably can't see it. Four points it's obscuring it a bit. Bad positioning there, but you know, 4 megahertz, something like that.

**Dave Jones:** So, it's up to a couple of megahertz. There's my marker point. So, 2 megahertz, so let's go from, say, 0 to 5 or something like that, and we'll be able to see that down there.

**Dave Jones:** So, we'll go into frequency, and our stop frequency will change that to 5 megahertz, and now we can get in there, and we can see. Now, you can see that, you know, it's not it we're getting close to our limit, but the average value in there is not, you know, hugely above that line.

**Dave Jones:** We're close, and a couple of peaks are going over. Now, it's time um because this is a very quick updating using that positive peak detector. Now, we want to go into our quasi uh detector.

**Dave Jones:** So, we'll go here, and we'll go into our quasi peak detector, and this one will actually take some time. To twiddle our thumbs, but we'll eventually get a result.

**Dave Jones:** And the problem there was if we go into a sweep, it's set it to uh 970 seconds. That's why we're going to have to wait a while. And if we set it manually to 60 seconds, we can see it uh start sweeping across here, but this isn't going to be accurate.

**Dave Jones:** So, that is uh certainly going to take a while. As you can see, we've gotten this far after, well, 2 and 1/2 minutes. It's going to take about 16 minutes to do that in entire sweep at the recommended uh value of the uh sweep speed of 970 seconds there.

**Dave Jones:** That one took a bit of time. So, what I've done is I've changed my frequency range from 0 Hz to 1 MHz here, and that's giving me a sweep time auto sweep time of 200 seconds, much more reasonable.

**Dave Jones:** And as you can see, we are with the quasi peak detector, we are going above our line there, our reference line. And you notice our reference line jumps up there.

**Dave Jones:** That's because I set it to 150 kHz. I should have set it to zero, and it would have gone all the way across. But anyway, the range, as far as the standard's concerned, is only from In this particular case, it's 150 kHz upwards.

**Dave Jones:** So, even up to a megahertz here, as you can see, we're basically still over that nominal CISPR limit. So, really, we probably want to take it out to a couple hundred couple of megahertz again, and see where it actually falls below that.

**Dave Jones:** But we're definitely pushing our luck here, that's for sure with this design. And I should point out that something like this cheap low-end general purpose spectrum analyzer isn't quite going to give exactly the same results as a proper EMC house would with their $50,000, you know, EMC measurement receiver.

**Dave Jones:** But, you know, we can get a reasonable indication, and that's the whole idea that this thing allows you to do some basic in-house testings, you know, cheap and easily.

**Dave Jones:** Basically, it's just your time inside the house, plus a, you know, a $1,500 or less analyzer, not much at all. And you can do this basic testing, and most importantly, you can actually test things before and after you make changes to the product.

**Dave Jones:** So, we're almost there for a 300 MHz span using quasi peak detect here. And as you can see, it's starting to drop off there, and I can set a marker here.

**Dave Jones:** Where's our marker value? So, anything sort of at point there, sorry, it's a bit hard to see with the tiny little font on this thing, but um anyway, around about, you know, 2.3, let's say 2.5 MHz and under, that's where we're we're probably going to be a bit concerned about that sort of stuff.

**Dave Jones:** So, we might want to look at our design and go, "Well, what can we improve down at that low end?" But as we saw with the wider frequency sweep before, anything like above that 2 and 1/2 MHz, um say it just drops off and it seems to be just fine.

**Dave Jones:** And there it is, exactly the same shot, but back in the real time there. So, we're a bit concerned here with our pre-compliance testing down at the low frequency here.

**Dave Jones:** You know, there's a good chance we may not pass the standard here. And what can we do about it? Let's say this thing, ah, it's got to ship next week.

**Dave Jones:** You know, we can't respin this board and add, you know, uh ferrites on the output and do other stuff to reduce the EMI, you know, change the slew rate of signals inside, tighten up the little PCB layout, all that uh sort of stuff.

**Dave Jones:** What can we do? Well, we can probably try adding on one of these um ferrites, one of these external clamp type ferrites. You may have seen these on products.

**Dave Jones:** And these are a common technique for just this thing where where your product's finished, oh no, but we failed our compliance testing and we still want to ship this thing.

**Dave Jones:** So, what you can do is just add a couple of these to your power wires on the output. You may have seen them and they may have been like a heat shrink on the outside, for example, added after the fact to make your product pass that EMC compliance.

**Dave Jones:** So, let's see if it makes a difference. Here's our live display here. And let me clamp it over once and we probably with only one, so we've only got like one turn in there, we really don't expect to see any different any drop at all in that, right?

**Dave Jones:** Not much at all. But if we wrap it around that a couple of times on just this one lead here, I think we might be in luck. So, there you go.

**Dave Jones:** I've got a couple of turns inside that thing, and bingo, look, it's dropped us down a hell of a lot. You can see that by adding an extra turn in there, we're almost under even right down at the bottom end there.

**Dave Jones:** So, we're doing pretty good. Let's add another one to the negative line here. All right, here we go. Let's see if we can see this change live. I'll just clamp this over on my negative line there, and look at that.

**Dave Jones:** Oh, beauty. So, that's not exactly the best solution to your problem here. If you can fix it inside your product, you uh certainly would if you had the time to uh you know, re-spin.

**Dave Jones:** That's why you do the in-house testing. The in-house uh pre-compliance testing at the design stage, at the prototype stage, allows you to get a quick ballpark indication of whether or not you're going to pass this um will pass AMC compliance, whether or not you're on the border.

**Dave Jones:** And when doing simple bench testing like this, even the ground plane isn't going to uh save you really. Just be careful about external uh electromagnetic fields here, which can uh you know, radiate into your test system.

**Dave Jones:** That's why these things are done in proper uh shielding enclosures, things like that. We're just mucking around here on the bench doing some basic testing. As we've seen before, my LED lights above me that I use for shooting, watch this, if I get rid of them, we'll probably see this higher end broadband noise disappear.

**Dave Jones:** Or lower. Look look at that. And I switch it, that spike is still there. Switch it on and see. So, just be careful about what things are radiating into your test system here, or capacitive or inductive coupling.

**Dave Jones:** Just be aware of it. And if you're wondering, does this metal shield make a big difference in this particular installation? No, not really. Let me remove it live here.

**Dave Jones:** Oh, there we go. A bit more higher broadband noise there, but you know, essentially it's not going to change the issue that we had at the lower end. And of course radiated testing would be a whole different ball game again, and that requires a calibrated antenna which you connect up to your spectrum analyzer in a shielded anechoic room.

**Dave Jones:** I've done videos on on those before those indoor test sites for EMC compliance, which I should link in down below actually, but this one was just a basic video to show you how you can do some basic conducted pre-compliance measurements.

**Dave Jones:** And the good thing is is that you can do these measurements even though if they're not you know, absolutely correct to the absolute value, you can see if you're getting anywhere close to the standard to the standards limit or not.

**Dave Jones:** And if you are, then you can make changes to your product and then rerun the exact same test setup in house. Doesn't cost you much to spin a new design and add little, you know, like you might put some little ferrite beads in there.

**Dave Jones:** You might do this or that. You might shield this or that or do something. And to and then you can see the changes that in your product what they make to your conducted and your radiated emissions as well.

**Dave Jones:** So, it's really, you know, one of those vital things in house EMC pre-compliance because it's much cheaper to do it in house at the design stage than it is to get a report back, "What?

**Dave Jones:** Failed." So, there you go. There's a very brief look at some basic in house EMC pre-compliance testing. And don't please don't take this video as gospel cuz there the standard is incredibly complex and it depends a hell of a lot on your device under test and all sorts of stuff.

**Dave Jones:** So, you know, and the test setups and the the frequency range and the type and your product, and the different classes of product that you can have within the standard.

**Dave Jones:** So, this might be, you know, a class four or a class three standard or something like that, depending on what value it actually meets, and the market you intend to sell into, and etc., etc.

**Dave Jones:** But, anyway, there's I'm sure a lot of people with a ton of EMI EMC experience will no doubt point out some really good links on the forum and in the comments.

**Dave Jones:** So, if you do have those, please add them. Hope you enjoyed it. Catch you next time.
