---
video_id: XqakD0dXdjM
title: Guest Video: Kerry Wong - HP493A 8GHz Microwave RF Amplifier Teardown
url: https://www.youtube.com/watch?v=XqakD0dXdjM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 45, "3": 70, "4": 93, "5": 115, "6": 137, "7": 156, "8": 174, "9": 196, "10": 211, "11": 234, "12": 256, "13": 283, "14": 310, "15": 343, "16": 366, "17": 405, "18": 437, "19": 461, "20": 504, "21": 541, "22": 568, "23": 591, "24": 610, "25": 629, "26": 648, "27": 683, "28": 705, "29": 724, "30": 747, "31": 768, "32": 792, "33": 814, "34": 835, "35": 858, "36": 886, "37": 916, "38": 942, "39": 985, "40": 1013, "41": 1033, "42": 1052, "43": 1076, "44": 1094, "45": 1113, "46": 1134, "47": 1160, "48": 1188, "49": 1211, "50": 1234, "51": 1252, "52": 1277, "53": 1298, "54": 1323, "55": 1340, "56": 1365, "57": 1397, "58": 1429, "59": 1453, "60": 1469, "61": 1489, "62": 1512, "63": 1543, "64": 1562, "65": 1581, "66": 1601, "67": 1624, "68": 1641, "69": 1665, "70": 1689, "71": 1716, "72": 1738, "73": 1767, "74": 1790, "75": 1817, "76": 1837, "77": 1868, "78": 1889, "79": 1911, "80": 1930, "81": 1956, "82": 1974, "83": 2002, "84": 2028, "85": 2049, "86": 2070, "87": 2088}
---

**Dave Jones:** Hi, what you're looking at here on my bench is a Hewlett Packard 493A C-band traveling wave tube amplifier. This one is a working unit and I did a teardown with a few years back, and I will provide a link in the video description down below for those who are interested.

**Dave Jones:** Traveling wave tube is a kind of vacuum tube, but unlike most of the vacuum tubes that have largely become obsolete in an era which is dominated by solid-state devices, these specialty vacuum tubes are still in wide use in radars and satellites due to its high bandwidth, high gain, relatively low noise figure and extremely high reliability.

**Dave Jones:** Theoretically speaking, semiconductor devices should have higher reliability as they do not typically age over time, whereas in vacuum tubes, the filament and cathode material are prone to failures as they age. But in high frequency and high power applications, devices' heat dissipation and power supply reliability become more challenging

**Dave Jones:** and they hinder the overall reliability of power amplifier systems, especially in harsh conditions such as those found in outer space applications. But we have seen more and more silicon carbide and gallium nitride based semiconductors used in high frequency power and high power applications over the years.

**Dave Jones:** Nevertheless, these microwaved vacuum tubes such as magnetron, klystron, and traveling wave tube still have their place in high power microwave applications. I have always been fascinated with these devices, and although I studied these in my university years, but I had never seen an actual device close up before.

**Dave Jones:** So I picked up another one from eBay, and this one is not working, and also I had tested it with parts swapped from this working unit so that I know that the problem of this, the other unit, besides missing a couple of tubes, is that it had a very weak traveling waves tube.

**Dave Jones:** So we can take that one apart and see the magic inside. Oh, by the way, before I do the teardown, not sure if you have ever seen a traveling wave tube amplifier in action before. So let me actually first fire it up and let's take a look.

**Dave Jones:** And for that, I plugged in this unit, and how this works is at first we need to let it on standby. And after it warms up, the high voltage relay would start engaging, and you should hear a click. And after that, we can start our measurement.

**Dave Jones:** So right now, let me just fire this up. It's going to be a little bit loud. So while it's powering up, let's prepare the unit for our measurement. I'm just going to put an adapter on here. Now you just hear, you just heard the click noise, and that's when the power relay actually engaged.

**Dave Jones:** So now this traveling wave amplifier is actually engaged. So let's take a look at the other one. So this one is the traveling wave tube amplifier. And this one is the traveling wave tube amplifier. And this one is the traveling wave tube amplifier.

**Dave Jones:** And that's when the power relay actually engaged. So now this traveling wave amplifier is ready to be used. And let me briefly show you the setup I have here. So for that, I'm going to place this unit backward a little bit so you can see the full picture.

**Dave Jones:** Okay, so here is our setup. And towards the top over there is a Wavetek 907. That's the microwave signal generator. And it's a X-band signal generator, so it ranges from roughly 7 GHz to 11 GHz. And now we're outputting about 6.95 GHz at minus 31 dBm.

**Dave Jones:** And so the signal from that generator comes into the input of this microwave amplifier. Because this 493A is only from 4 GHz to 8 GHz, which is sitting at the C-band, so I can only use the lower band of that 907 output. And the output from this 493A goes to a detector,

**Dave Jones:** and then goes to the Wavetek 907 power meter. And that power meter is capable of measuring up to about 18 GHz of frequency range. So this is well within its range. So what I'm expecting is that after I power on the 493A, you should see a jump in that dBm reading.

**Dave Jones:** Right now it's sitting at minus 65, 64. So let's turn it on. And as you can see, right now we are sitting at minus 5 dBm. So which means that minus 31 dBm signal gets amplified roughly 25, 26 dBm. And this is actually on the lower end of what this 493A is capable of when it was new.

**Dave Jones:** But right now because it's aged and the emission efficiency of the cathode of that TWT is not as good as when it was new. So that's why the amplification drops below 30 dBm. But in general, this one should be capable of delivering more than 30 dBm amplification.

**Dave Jones:** So just to double check, and now we can see that that's indeed a roughly 25 dBm increase in signal strength. So now let me actually connect the input from that Wavetek generator directly to the detector just for reference purpose. So for that I'm going to cut the RF power and I'm going to disconnect the sensor.

**Dave Jones:** And I'm going to connect the output from the generator directly to the detector. And as you can see, it's more or less minus 30 dBm. And given that our setup has some variations and also the cabling, so that is a pretty good reading.

**Dave Jones:** So roughly speaking, we had about 25 dBm amplification from this traveling wave tube amplifier. We can also put the output signal onto the spectral analyzer to take a look. So for that, let me power up the spectral analyzer. And we should be able to...

**Dave Jones:** It's getting quite noisy here, but we should be able to connect... So I'm going to connect that back to the input, to the 493A. And let me select... First of all, let's select the first band, which is 2227. So let's do a start frequency.

**Dave Jones:** Let's do 4 GHz. Let's do 5 GHz. And let's do the stop frequency. Let's do 8 GHz. And that's good enough. So let me turn it on. So right now, you do not see anything on the spectrum yet, because I haven't powered it on.

**Dave Jones:** Actually, let's change the resolution bandwidth down a little bit. So let's do 1 MHz. OK, so now let me turn on the TWT. And I can close up the... Let's close it up a little bit. So you can see the tone that is roughly at 0 dBm.

**Dave Jones:** And what is interesting is that when I power down the TWT, you can see that the noise floor also rises. So let me turn it off so you can see better. So now it's off. Now it's on. So this is some inherent noise from this amplifier.

**Dave Jones:** Anyway, so now you guys have seen this TWT in action, and I'm going to power it down, and let's open up the other unit that I bought was not working, and we'll see what is inside. Now, I suspect that this unit is much older than the working unit,

**Dave Jones:** and you do see there are some design differences. For example, the switch, instead of turning up and down, it's moving left and right. And also this meter is faded quite a bit. And from the serial number, it seems that this one also is much earlier.

**Dave Jones:** But the construction should be the same, and we will power it down. And also there's something stuck on the meter. You can see actually this is not connected at all, so the meter is just moving by itself. Anyway, so this unit is not working, as I mentioned earlier.

**Dave Jones:** So let's proceed to the teardown. So now we have just opened the top, and we can clearly see what is inside. So how this unit works is not that complicated. Basically, we have some high-voltage rectifier section. This provides the voltage needed by this traveling wave tube.

**Dave Jones:** And then we have a section that handles the modulation and input signal amplification. So really, the core of this unit is just this tube lying down there, which is our traveling wave tube, which is what we're going to be taking it out and take a good look at.

**Dave Jones:** Let's remove this. So my plan for this unit is actually just to do an extreme teardown and keep the parts so that I can service the other working version. And I have not powered on this for a long time, so I know that this is not charged,

**Dave Jones:** but you really need to make sure that the caps are discharged before trying to poke around in these kind of things. Trying to poke around in these kind of vacuum tube devices because most of the vacuum tubes have a very high anode voltage being applied.

**Dave Jones:** And for the traveling wave tube, we actually have voltage up to a couple thousand volts floating around. So you really need to be very careful when working with these kinds of devices. But right now, we're not connected. So a lot of these old units use this kind of a modular design,

**Dave Jones:** which is actually make maintenance much easier. And up here, you can see that we have these three pentodes. These are the 8068. They serve as the voltage regulator in series. And then we have these two, the OA2 tubes. These are the reference tubes.

**Dave Jones:** So what they do is they basically are kind of similar to the Zener diodes that we use in lower voltage applications, except these are gas discharge tubes. And here is something that you actually don't see very often. It's the delay relay. So basically, these are the relays for the 90 seconds startup

**Dave Jones:** before the high voltage was applied. And we have some adjustments. And by the way, this unit actually misses two of the relays, so they don't work. So now let me remove the board on the left-hand side. Now I just turned the whole thing around 180 degrees.

**Dave Jones:** And this board is the modulation board. Basically, you can input a signal to modulate the microwave signal. And in essence, it's just a differential amplifier implemented using vacuum tubes. So again, this is nothing spectacular here. So these are really the two main boards.

**Dave Jones:** The remaining circuitry is basically just monitoring the traveling wave tube and also the traveling wave tube itself. So let's proceed to removing the traveling wave tube. And for that, I'm going to… I'm not sure you can read this or not, but it is actually quite nice that some people before me

**Dave Jones:** put down all the markings on that, so you can clearly see which color corresponds to which terminal. So that's very nice. But even though that information is in the manual. Okay, so now let's unscrew all these. And we want to remove the traveling wave tube.

**Dave Jones:** And for those who haven't seen this before, this is the reverse side. And I need to unscrew these screws to free the TWT. But take a look at how beautiful the circuit boards are engineered here. And look at all these resistors. And back here we have some transistors that the casing seems to be gold-colored.

**Dave Jones:** Not sure if those are gold-plated or it's just the color. But I think these might be actually gold-plated to improve the long-term reliability so it doesn't get corroded. And now we have freed that traveling wave tube, let's loosen the RF connectors so we can actually take out the tube.

**Dave Jones:** And now we have freed the traveling wave tube out from its casing. And of course we're going to take this further down, but here let's take a look. Watkins-Johnson And it's 4 to 8 GHz. And there's some thermal conductive material at the bottom.

**Dave Jones:** And you can see that the voltages are actually printed on it. And these are the operating voltages, so the idea is that you adjust the trim pots on the high-voltage supply and the various biasing circuitry to make sure that it is in line with what is printed here.

**Dave Jones:** Now each of these tubes are individually characterized so that the printed out values are actually all different. But before I move on to take that apart, let's just take a look at the transistors used here. And all these, as you can see at the bottom,

**Dave Jones:** are the 2N441s here used. These are two germanium transistors. And this one, SK3009, is another transistor. So nowadays we can't find these transistors anymore, and these are awfully expensive to get. But from the date code here, one is from 73, the 12th week,

**Dave Jones:** and one is from 83. So this unit is at least after 83. Which is interesting because the other unit I'm pretty sure was made around 82, but the serial number of this unit is actually earlier than the other one. So I'm not sure what the deal is.

**Dave Jones:** Maybe they had done some repair to this. I don't know. And now we have this traveling wave tube removed. I thought before we take that further apart, let's at least briefly review the working principle of a traveling wave tube. And the actual mechanism is pretty complex,

**Dave Jones:** and I would strongly recommend you to read a book about it. The book I can think of is Principles of Electron Tubes by Jabotowski and Watson, published in 1965. That book has a very detailed description and mathematics behind how these kind of things work.

**Dave Jones:** But in general, a traveling wave tube is just a so-called velocity modulated tube. And for the traveling wave tube, it's usually constructed with a cathode, which we draw here, and we have some filament here. And basically this one generates an electron. So here we have an opening, and the electron gets shot out

**Dave Jones:** through the length of the tube. So we have the tube is somewhere here. And we have a target here, which is our anode. So this is our collector. Basically, the voltage applied between here, that's our acceleration voltage. Now, inside the tube, we have a structure called a helix.

**Dave Jones:** That's a slow wave structure, and I'll explain it very briefly. So this is kind of encasing the electron beam. And at one end, we have the RF coupled in. So this is RF in. And at the other end, we have the RF coupled out.

**Dave Jones:** And we call it a slow wave structure because when RF goes through this helix, the actual propagation speed in this direction is much slower than the speed of light. And because the RF signal has to travel a relatively longer distance, so imagine we're traveling

**Dave Jones:** at the speed of C, which is speed of light, along the helix. And the actual speed given from the electron's perspective is actually much slower than C. So long story short is by adjusting the electric field applied here so that the electron speed is just

**Dave Jones:** slightly faster than the traveling speed of this RF field down the helix. That's when the energy exchange happens, and you'll hear the word bunching of the electrons. And also, the electron would transfer the energy from the electron field into the RF field, and you get an amplified RF signal out.

**Dave Jones:** So it's really quite magic, and the mathematics behind it is quite complex, but it all boils down to Maxwell equations for those who are studying RF. Anyway, so I thought I would just give a very short primer on that, and now let's move on to take the actual tube apart.

**Dave Jones:** So I'm very excited to see what is inside this thing because I have never seen one before. So I think I'm going to remove, and you can see that this is sealed because they don't want me to monkey around here. So I'm going to remove the top screws first,

**Dave Jones:** and we'll see what we get because I have no clue whether or not we can open it this way where I have to assemble the whole thing. Oh, by the way, so I omitted the fact that when the electron beam is traveling through this tube,

**Dave Jones:** it has to be focused. So there would be typically a quadrupole structure of the magnet around this tube to help focusing the electron beam. So we should see a magnet inside or some magnets inside this tube. And I don't think I have seen a teardown of a traveling wave

**Dave Jones:** tube before. So this could be the first of its kind. And all these wires are silicone wires, which is a very, very thin material. And all these wires are silicone wires, which is quite unusual given that it was made back in the 80s.

**Dave Jones:** So now we have four of these screws removed. Shoot. Can we get in now? And I don't think so. So I think we have to further remove all the screws at the end. Oh, by the way, here we have two more. Sorry about that.

**Dave Jones:** I'm not sure how much these tubes cost when they were new, but it must be costing a fortune because these has to be individually characterized and also they don't have a volume to get the cost down. So all right. So it seems I still have a few more screws

**Dave Jones:** need to be removed before I can actually open this up. So let me do that off the camera, and I'll be back when I manage to open it. It looks like I still have to remove more, but right now, so far, I have just

**Dave Jones:** removed the top two covers and one either side, and I don't see any movement yet. So I'm going to keep removing. Let's remove the two RF couplers and see what's inside here. And OK, I just removed all the screws to this output SMA

**Dave Jones:** connector, and you can see that inside we have a very thick, rigid coaxial connecting to the output. So it looks like we have to further disassemble this unit, these two parts first, but I'm not sure if you can see it. That is the coaxial we're looking at.

**Dave Jones:** It's in there. Yep, that pipe. And I just removed the input and output coax, the cover for the coax, and you can see that it's a nicely machined piece of aluminum, and it's beautiful. Look at that. And now we can see clearly the rigid coax used

**Dave Jones:** for this input and output. Interestingly, this one is actually pinched. I'm not sure if it's deliberate or not. It doesn't look like it's deliberate. I did not pinch this, so I'm not sure if this would affect the performance anyway. But now I can see that the top piece is loose,

**Dave Jones:** but it's still not able to totally open it. So OK, so now I can see. Oh, wait. We might just be able to. Here we go. All right, so let me lift this up a little bit further, and we will clean it up and come back.

**Dave Jones:** And I think this might be as far as I can take this apart for now because the tube inside seems to be either glued onto the main casing, or it's just extremely tight. Unfortunately, if I try to pry it out, it would shatter and break.

**Dave Jones:** But for now, we can actually start appreciating what is inside. Now, I did not totally remove the coaxial. It seems that the coaxial is actually soldered after this coaxial been put in through these two slots. And let me take a little zoom in here.

**Dave Jones:** And I'm not sure if you see this. So we know that the outside is, well, the inside, we have some magnets. Each section of this is actually magnetic, and you can feel that is a screwdriver. But also, we have some shards of some magnets here.

**Dave Jones:** So I'm not sure what the deal is. And these are clearly magnets, but I don't know why would they be floating around inside. So we have one piece here, and we have one piece here. OK, it's another piece. And I think I have one more piece here.

**Dave Jones:** So the only thing I can think of is they did some kind of calibration afterwards, and the certain magnetic field is not strong enough. So they have to correct it by putting some of these magnetic pieces material in there. I'm not totally sure, but that's certainly the only explanation I have

**Dave Jones:** as everything is meticulously put together. And you can look at the machining of these beautiful casing. And so this must have cost a fortune to make. And if you look at the anode side, you will see that. If I can focus here, we also have some adjustment.

**Dave Jones:** Here, let me move this out of the way. So we also have some adjustment screws. We can do some fine adjustment of the anode plate, presumably here. And so this section would be the section that I, in my earlier drawing, actually I can show you here.

**Dave Jones:** So that section would be where the helix is. And so the input and output would be directly coupled into and out from that helix slow-wave structure. And other than that, this is just a vacuum tube inside. And so that is really amazing. And we have some custom writing here, 462.

**Dave Jones:** Not sure what that means. Either it's a QA number or it's some specifics that we don't know of. And here also we have some writing, 35C2. All right. After some try, and I was able to finally free this from this casing. Actually, it was quite tightly fit inside.

**Dave Jones:** Basically, I had to pull it from one side like this so that the whole unit, the whole assembly actually comes out from this groove. So it's like that. Now, in the meantime, I also desoldered the SMA connectors so that you can see the rigid coax here.

**Dave Jones:** So this is actually quite compact, this tube. And considering that this tube would output at least one watt of RF power while the input is only one millivolt. And so when I was wiggling here, I noticed that this part actually has a lot of this silicone material.

**Dave Jones:** And after I remove that, I can pull this out and check this out. So this is the electric gun version of the TWT. And it's just like any other vacuum tube. Actually, inside we have filament and we have some coated cathode material. And also we have certain plates here to help forming the electric beam.

**Dave Jones:** And I'm not actually quite certain how this is connected, whether it's vacuum sealed. It has to be vacuum sealed towards the other end. So I wonder if I somehow broke the vacuum. I'm not entirely sure. The only way to find out is to further open this portion apart.

**Dave Jones:** So let me try that to see if I can loosen this up and open it apart. OK, after a little bit of investigation, it actually appears that I did manage to break this tube, which is evident. You can probably see there's a little crack on the top of the glass.

**Dave Jones:** So that's why this piece came off. And in order to see a little bit more, I had to use a Dremel to cut off one end because this is the end where the electron gun was housed in. And I couldn't see anything from this end, so I cut it off.

**Dave Jones:** And now you can see that actually it did break off right here. And basically, originally this tube is like this. Basically, the electron beam gets formed inside this electron gun. And there are various voltages similar to your vacuum tubes that helps the beam to focus.

**Dave Jones:** And after that, the beam enters a helix. Actually, you can see portions of it right here. This is kind of like a springy structure. That's, I believe, part of the helix. As you can see that also from inside this tube. It depends on the light.

**Dave Jones:** You might get a glimpse of the first few turns, about an eighth of an inch down into that hole. And as you can see that we also have this magnet material for the casing. As mentioned earlier, this magnet material basically creates a magnetic field,

**Dave Jones:** which is a quadrature magnet arrangement. So it's NS, NS. So basically, the field helps the electron beam to stay focused and racing down through this tube. And in the meantime, the RF signal gets passed in from this one end and so travels along the helix and down the tube.

**Dave Jones:** And when the electron beam, as I mentioned a little earlier, travels down slightly faster than RF field down the helix, then that's when the energy gets transferred from the beam to the RF field. And thus we get a magnified signal coming out from this end.

**Dave Jones:** So this tube is certainly a very precise piece of engineering. And, you know, of course I broke it, but it was actually made very robust. When you think about this, this is a metal tube. Well, the tube itself probably is glass, but it's encased in metal

**Dave Jones:** and there's no, it's very rigid. So it probably can withstand a lot of vibration and in harsh environment. So anyway, I hope you have enjoyed the teardown and also hope you will learn something new. And if you like the video, please give it a big thumbs up

**Dave Jones:** and do remember to subscribe, share, and also remember to like. I will catch up with you next time.
