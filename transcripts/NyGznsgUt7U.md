---
video_id: NyGznsgUt7U
title: EEVblog 1747 - Schottky vs PN Diodes & Measurement Traps
url: https://www.youtube.com/watch?v=NyGznsgUt7U
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 33, "3": 50, "4": 59, "5": 74, "6": 84, "7": 97, "8": 109, "9": 122, "10": 141, "11": 158, "12": 173, "13": 181, "14": 195, "15": 208, "16": 219, "17": 228, "18": 243, "19": 259, "20": 273, "21": 288, "22": 296, "23": 315, "24": 325, "25": 338, "26": 350, "27": 366, "28": 375, "29": 391, "30": 405, "31": 421, "32": 432, "33": 442, "34": 454, "35": 467, "36": 485, "37": 500, "38": 512, "39": 526, "40": 539, "41": 555, "42": 567, "43": 579, "44": 593, "45": 608, "46": 625, "47": 635, "48": 644, "49": 654, "50": 666, "51": 676, "52": 685, "53": 696, "54": 706, "55": 713, "56": 722, "57": 733, "58": 747, "59": 763, "60": 779, "61": 793, "62": 809, "63": 821, "64": 831, "65": 843, "66": 855, "67": 868, "68": 879, "69": 888, "70": 898, "71": 916, "72": 924, "73": 937, "74": 956, "75": 982, "76": 994, "77": 1009, "78": 1027, "79": 1046, "80": 1055, "81": 1067, "82": 1077, "83": 1096, "84": 1106, "85": 1118, "86": 1142, "87": 1157, "88": 1178, "89": 1191, "90": 1202, "91": 1214, "92": 1242, "93": 1251, "94": 1262, "95": 1275, "96": 1288, "97": 1305, "98": 1318, "99": 1335, "100": 1348, "101": 1364, "102": 1376, "103": 1390, "104": 1402, "105": 1414, "106": 1430, "107": 1445, "108": 1458, "109": 1470, "110": 1483}
---

**Dave Jones:** Hi, I found this very simple, but in very interesting question posted on X by Blind Vio, who's an excellent follow by the way. Um, and I'll link it in down below if you want to join the discussion on X, but I thought I'd shoot a video explaining what's going on here because we're going to go down a rabbit hole with diodes that you might not be aware

**Dave Jones:** of, especially if you're a beginner, because it's non-obvious. And there can be a big difference between different types of diodes and what applications you use them in. Can be a big trap for young players.

**Dave Jones:** So, the circuit posted is a simple diode flowing from a 5-V USB input to power whatever circuitry is on the other side. We don't care. It's common to use a diode as series input protection like this, but just in case your input voltage is reverse biased for whatever reason.

**Dave Jones:** You don't want to blow up your circuit, and the diode, of course, only allows current to flow in one direction. So, it allows to flow in from the power supply, but it doesn't allow it to flow out.

**Dave Jones:** Hence, the why a diode looks like an arrow. And you can see that the arrow is pointing inwards from the 5-V USB. So, the question is, shouldn't the diode be preventing voltage or current flowing back to the input?

**Dave Jones:** And the answer is, well, yes, it should. So, let's build it up and see what's going on here. So, what I've got here, I've got a 5-V power supply, and I've got a diode in series.

**Dave Jones:** I'm using a surface mount one, so I had to mount it on a board here, but trust me, there's nothing fancy going on here. And if you want to know what it is, it's an STP 2SL60A here.

**Dave Jones:** We'll have a look at that later. And we've got our voltmeter over here, available on evblog.store, by the way. All the best multimeters are on evblog.store. So, we've got the diode in series, and of course, the diode has an anode and a cathode.

**Dave Jones:** Yes, cathode is marked with a K, and it's spelled with a C. Uh, don't ask why. Just is. And you can see that the diode simply shaped like an arrow here pointing in this direction like this.

**Dave Jones:** So, current is only going to flow in that direction. It's not going to flow backwards. That's what a diode does. It literally stops the current from flowing backwards. So, this is actually the same as our Twitter question here except the power supply is simulating the circuit which would normally be powered from an external power supply here.

**Dave Jones:** So, the current flows in to the circuit and powers your circuit. And here was using a voltmeter to measure the USB port. So, I've got that diode in series and sure enough we're like our circuit's at 5 volts and our diode's pointing in this direction.

**Dave Jones:** So, why are we reading 5 volts on our multimeter? Shouldn't we be reading 0 volts? You might be thinking, "Oh, Dave, you've got the diode back to front." Okay, well, let's put it in the opposite direction, shall we?

**Dave Jones:** We're still measuring 5 volts. Is this diode blowing? What the hell's going on here? So, I've got another type of diode here. For those playing along at home, it's an SS24.

**Dave Jones:** You know, these are quite decent diodes. We getting the same thing. And you can see the negative mark on the diode there and the positive terminal. So, I do have that diode wired backwards.

**Dave Jones:** Why are we still seeing 5 volts? Shouldn't that voltage be reading 0? Well, yes, it should. So, let's try a different diode. We get the classic 1N4148 signal diode.

**Dave Jones:** It's as jelly bean and as simple as it gets. Negative terminal there. Hopefully, you can see it and we put it in. We're reading 0. That works just fine.

**Dave Jones:** And then if we change the polarity of that, it lets the voltage through because it's forward what's called forward biased. And then when you're reverse biased, we read 0.

**Dave Jones:** So, why does this diode work and the other two didn't? Let's try another diode here you'll be familiar with the classic power diode, the 1N4001. We put that reverse biased, we read zero volts out.

**Dave Jones:** And if we change the polarity of that, sure enough, we're going to measure out five volts. No worries. There's a very little voltage drop on there because there's very little current flowing through that diode because we've got a 10 meg input resistance on our meter here, but you can see it works as a diode.

**Dave Jones:** So, is there something wrong with these diodes? Well, no, they're actually pretty decent diodes. In fact, they're better than these diodes, but they're not better for this application that we're using it in now.

**Dave Jones:** And the application matters. These are actually different types of diode to your regular 1N4001 and your 4148. These are regular PN junction diodes. If you've studied diodes, you're familiar with that.

**Dave Jones:** A diode is a a semiconductor PN junction. That's how it works. I won't go into the physics of it, but it allows current to flow in one direction and not the other direction.

**Dave Jones:** Well, why didn't these diodes do that? Well, they do do that, but they're different types. These are what's called Schottky diodes, named after Walter Schottky. Don't confuse it with Shockley, the more famous Shockley who invented, co-founded, and co-invented the transistor.

**Dave Jones:** No, different person, same field, but yeah, Walter Schottky. And if you go back to the original question schematic, aha, you would have noticed it's not a regular diode symbol.

**Dave Jones:** It's a Schottky symbol which has these little like square tails like this. And that indicates that that's a Schottky diode. And it goes by its more formal name of a Schottky barrier diode.

**Dave Jones:** So, some people call them just a barrier diode, but probably more common just to call them a Schottky diode. And they're different to a regular PN junction diode like your 1N 4001 or your 1N 4148 here.

**Dave Jones:** These are just a PN junction, but the Schottky diode is what's called a metal semiconductor junction. It has an extra metal layer in there, and that gives you a huge advantage in terms of voltage drop.

**Dave Jones:** So, let's measure these diodes with a diode tester on a multimeter. Let's have a look. You can see that it works fine, and we put in the other direction, it reads nothing.

**Dave Jones:** It works exactly like a regular diode. And the other one here? Look at that. No worries. It looks and tests exactly like a regular diode. But you might have noticed something there on that reading.

**Dave Jones:** Look at this. 0.142 V. That's a low voltage drop. So, let's get the classic 1N 4001. Ah, we've got half a volt drop. And the 1N 4148 diode? Once again, half a volt drop.

**Dave Jones:** The Schottky diode's their huge advantage is that they're a much lower voltage drop than your regular PN junction diodes, and that's why people use Schottky diodes in switch-mode power supplies when you care about efficiency.

**Dave Jones:** You don't just want to throw away your power willy-nilly in the losses in your diode. So, that's why Schottky diodes are really useful for like high-frequency switch-mode power supplies with low losses.

**Dave Jones:** That's where you want to use them. But Dave, if it tests like a regular diode on a diode tester, why is it like feeding back the voltage back out?

**Dave Jones:** Look, I've got that's a reverse-biased Schottky diode. So, to figure out why it's doing this, so instead of our voltmeter here, we're going to turn it into a current meter by moving our jack over here.

**Dave Jones:** Oh, insertion error. Warning, Will Robinson. Put it over to microamps over here, and we're going to have a look at what reverse bias current flows through that diode at 5 V cuz 5 V is going to matter.

**Dave Jones:** And look, there's a non-zero reverse current. It's only 2.4 microamps, right? Microamps, that's not much, but it's enough to upset the apple cart in the example circuit that we just had.

**Dave Jones:** That leakage current is the huge downside of Schottky diodes. Schottky diodes, as we'll see in a minute when we go to the data sheet, are about three orders of magnitude worse leakage than a regular, even jelly bean PN junction diode.

**Dave Jones:** You pay a price for having that Schottky barrier construction with the extra metal layer in there. But going back to our original question here, why are we reading 5 V on here when the diode is reverse biased?

**Dave Jones:** And if you use a, you know, 1N4001, it shows zero. Why are we getting something here? It's because multimeters, digital or analog, have an input impedance here, and you might You should know that it's around about 10 megohms.

**Dave Jones:** Could be 10, could be 11. It depends on the meter design internally. But let's just say it's 10 megohms input impedance. So effectively, our multimeter is a 10 megohm resistor.

**Dave Jones:** And you saw that we had some leakage current, some reverse leakage current in this diode of like, what is it? 2.5 microamps or something. And if you get you confused around here, I think it was 2.2 microamps times, just Ohm's law, 10 meg resistor, what do you get?

**Dave Jones:** 22 V. But we've only got a 5 V power supply, so we're going to read a maximum of 5 V here. If it was 22, we'd be able to measure 22.

**Dave Jones:** In fact, we can wind up the voltage. So if we wind the voltage up there, you can see it's going to track, but once we get above that like 22 V or thereabouts, Like we were up to like I I think this is a 40-V diode.

**Dave Jones:** So, I'll just go to 40-V maximum there. You can see it's now only reading 30-V because the leakage of this diode cha- A, changes with voltage as we'll see in a minute in the data sheet in the characteristic curves.

**Dave Jones:** Um and we've got a 10-M resistor there. And sure enough, if I put my fingers across there, I'm going to lower the effective resistance of that and it's going to go up to the maximum 40-V Not not quite.

**Dave Jones:** Have to wet my fingers maybe. And once again, that is not going to happen with a regular PN junction diode. But once again, if I put my fingers across there, I'm adding leakage by effectively putting a resistor across there.

**Dave Jones:** And you can think of that reverse leakage current as an equivalent resistor across the diode. It's a very high value. It's like, you know, mega- tens of megaohms, but it's there.

**Dave Jones:** So, let's have a brief look at what's going on here. I'll link in this website from TTI. It's a just a very nice uh page here with uh basic resources.

**Dave Jones:** And if you want to go into the uh physics of this, which I definitely don't want to do, I'll link in this uh Purdue University uh Schottky diode thing down here.

**Dave Jones:** And it's it's basically uh we've got instead of a PN junction, we've got a metal and N junction here. So, they're physically constructed quite different to a PN junction diode.

**Dave Jones:** It's not a PN junction plus metal. It's just the N junction plus a metal junction like this. So, technically, it's easier to manufacture. You don't have to do any of the extra doping and things um to do that.

**Dave Jones:** But you can get into the physics of it. You can go right down the rabbit hole, which yeah, we do not want to do. But bit time reading, go for it.

**Dave Jones:** So, the symbol is quite different to our regular diode, which is just the straight line. We have these little curly bits on the end. Sometimes they add the little bit going down and sometimes it's just a like that.

**Dave Jones:** Um whatever, but that could be if you just if you don't add the bit that goes down there, then you could easily confuse that with a Zener, which is an angled one.

**Dave Jones:** So, don't confuse it with Zener. I've done a video on Zener diodes. I'll link that in as well. So, I've got some N-type silicon and just a metal junction.

**Dave Jones:** So, it really is that easy. And you can physically see inside a barrier junction diode here. They just have a bit of metal and there's the N-type silicon there.

**Dave Jones:** Easy peasy. And by choosing a different type of metal here, you can actually adjust the effective barrier size in there. You can change the characteristics of your Schottky diode.

**Dave Jones:** So, you might use platinum, titanium, nickel, aluminum, tungsten, or you know, all different types of metals. You can actually select them or even alloys, I guess. If you want to go into the that deep, you can adjust the properties of your Schottky diode.

**Dave Jones:** You can't do that with a PN junction diodes. It's just a PN Well, you can. You can adjust the doping and things like that, but it's a very different physical construction and being able to adjust the properties of your barrier in there.

**Dave Jones:** So, anyway, that's the physics of it. So, here's a classic diode characteristic curve we've got current of forward current versus forward voltage here in this quadrant over here, and then we've got reverse voltage in this direction and reverse current in this direction.

**Dave Jones:** So, a normal diode is shaped like this and so its junction voltage is forward bias voltage is quite high. You saw it was like half a volt, but when you increase the current, it goes higher like 0.7 volts, a volt, so even more at really high current.

**Dave Jones:** So, voltage drop ain't that good. And if you try and use these regular PN junction diodes in switch-mode power supplies and things, where efficiency matters, you can be like losing a lot of um heat, a lot of power in your diode.

**Dave Jones:** So, you'll use a Schottky diode here, which has a much lower forward voltage drop. But, when you reverse bias, uh the voltage on a Schottky diode, this is its curve down here.

**Dave Jones:** It actually has like a little lip there that goes down like that. But, don't worry about that. So, the reverse current is going to be much higher. It's This is not to scale.

**Dave Jones:** It's kind of As I said, it's like three orders of magnitude more reverse bias current, leakage current on a Schottky than a regular PN junction diode, even a jelly bean one.

**Dave Jones:** So, you'll have much greater leakage current at um even very low reverse bias voltages like we saw there, 5 V. That's nothing burger. Um you Yeah, we'll get in microamps of leakage current.

**Dave Jones:** And this changes greatly with temperature as well, as we'll see in a minute. So, let's look at the data sheet of a Schottky diode versus say a 1N4148 regular signal diode.

**Dave Jones:** They tell you right up the front, very small conduction losses, extremely fast switching, low forward voltage drop, high frequency operation. That are some of the main advantages of Schottky.

**Dave Jones:** They're higher frequency switching, they're lower voltage drop, they're even lower noise if that matters to you, and they have no reverse recovery uh charge, and all sorts of things.

**Dave Jones:** They really are excellent diodes, which is why they're incredibly widely used in all sorts of power applications. But, there's two big downsides to Schottky diodes. One is that reverse leakage current we've been looking at.

**Dave Jones:** The other is that they're generally not as high a voltage. You're only talking like 100, 200 V maximum reverse uh voltage on a uh Schottky diode. You can get like a really specialized ones that go a bit higher, but PN junction ones can go very high, like, you know, 500 V or even 1,000 V or something like that.

**Dave Jones:** But, um yeah, the reverse leakage is a killer. So, So, is the one uh used in the uh example. And right off the bat, we've got our electrical characteristics here.

**Dave Jones:** We're going to maximum average reverse current at rated DC blocking voltage. So, at 40 V or whatever this diode is. Look, it's it's milliamps. It's milliamps. We got 1 MILLIAMP.

**Dave Jones:** >> [laughter] >> AND AT 100° C, it's 10 milliamps. Not the microamps anymore, milliamps. Unbelievable. That's just incredibly high leakage. Crazy. But, our 1N4148, our jelly bean PN junction diode, uh reverse current nanoamps.

**Dave Jones:** And 25 nanoamps typically at 20 V, which is quite a high voltage. Um so, yeah. But, you know, it'll go up to you can get microamps at, you know, when you're talking about 150° C, for example, but still like, you know, it's as I said, like can be three orders of magnitude lower at regular uh temperatures and voltages.

**Dave Jones:** So, for the 4148 PN junction, we've got the reverse leakage current here. And you can like it's microamps here. And you can see that at 25, they've got three different characteristic curves for three different uh temperatures.

**Dave Jones:** At 25° C, we're only talking like my 0.01 microamps. We're talking 10 nanoamps here, right at like 20 V. That's just like right there. That's crazy. But, here's the Schottky diode.

**Dave Jones:** Once again, at 20 V here at 25° C, we're in the milliamps now for our reverse leakage current. So, we're talking So, we're talking about like four microamps there, which is basically in around the region that we were measuring there um at the lower voltage, you know, we were measuring like 2.2.

**Dave Jones:** So, yeah, it's basically bang on to the data sheet here. We were just using the SMD version of this. Um so, very similar characteristic uh curves. So, that's why we're measuring a couple of uh microamps, but when you go back and you compare that to the PN junction, you're talking nanoamps.

**Dave Jones:** Three orders of magnitude. That's a thousand times, if you don't know what order of magnitude is. I've done a video on order of magnitude. Look at it. So, to answer the original question, let's go back to the diagram here.

**Dave Jones:** We've got What was missing was the 10-megohm resistor inside the Fluke 77 multimeter here, around about 10 meg, and we've got our reverse-biased uh Schottky diode here, cuz it's a Schottky diode.

**Dave Jones:** It's got three orders of magnitude more leakage. So, there's going to be a reverse leakage current through there. What is that value? We can calculate it with Ohm's law.

**Dave Jones:** We've got 4.73 V divided by 10 megohms. Get your computer out. And that value is 473 nanoamps or 0.473 microamps. Doesn't sound like much, but when you've got a high input impedance multimeter like this, it's going to matter.

**Dave Jones:** And that's why you're reading the voltage there, and that's why with a Schottky diode of 10 nanoamps, run it again. So, 10 meg * 10 nanoamps, should be able to do that in your head.

**Dave Jones:** It's 0.1 V. So, that's why we're reading like we weren't reading precisely zero. We were reading close to zero. It was 0.05 or 0.1 or something, you know, it was in that order because we're getting nanoamps of leakage current.

**Dave Jones:** So, this particular question is interesting because it's a measurement thing when the old-school trap of your multimeter has an input impedance. But, if you had another multimeter like a bench multimeter, they can have gigaohms, essentially almost infinite, not quite, but gigaohms of input impedance on the lower voltage ranges.

**Dave Jones:** It's It's simple Ohm's law. You've got current flowing through that circuit from your 5-V rail here. And that current will increase based on the voltage. So, if we go back to our curve here, we can see here that the leakage current does increase with voltage like this.

**Dave Jones:** It depends on the Schottky diode could be better or worse than this, but it's going to increase. And the PN junction diodes, they'll increase as well. Um you know, a similar sort of order differential increase with increased reverse voltage here, but we're still three orders of magnitude lower than a Schottky.

**Dave Jones:** And there's some other differences with Schottky diodes compared to PN junction. PNs will have avalanche breakdown as opposed to the breakdown of a Schottky, which is more sort of like smooth and gentle and things like that.

**Dave Jones:** And we could maybe if you want a follow up video of you know, stuff like that, let us know in the comments, but there you go. I hope you found that as interesting a question as I did.

**Dave Jones:** There it goes into the differences between different types of diodes. They can make a huge difference depending on the application. So, Schottky diodes in this sort of application uh you want as lower voltage drop there as possible.

**Dave Jones:** And also, if you're using it as a reverse polarity protection like a clamping reverse voltage clamping protection, for example, having this Schottky diode clamp at like you know, 0.2 volts or something, that means that you're protecting other PN junctions, transistors, integrated circuits in your circuit that you clamp them below the typical silicon uh threshold of like 0.6 volts.

**Dave Jones:** Whereas, if you used a regular PN junction diode as a reverse clamping diode, it might be 0.6, 0.7 volts, even more as it clamps the you know, really high current through there.

**Dave Jones:** And then that 0.6 volts can turn on or higher voltage can turn on PN junctions in your circuit that you're trying to protect. And well, yeah, you can release the magic smoke and come a gutter.

**Dave Jones:** So, a Schottky diode is yeah, the perfect thing to use in like a forward voltage drop protection application like this um that just stops reverse current going in this direction, but not leakage current.

**Dave Jones:** So, it'd be an excellent uh reverse clamping uh diode in here to actually protect this point in your circuit uh from any uh reverse voltages. So, um yeah, better than a PN junction diode.

**Dave Jones:** It's just, yeah, in this particular case, it's it's just a measurement thing. But, in this particular case, Line Ve was probably troubleshooting whatever uh circuit this is and just happened to be probing around and saw a 5 V on this point and went, "I haven't got the USB 5 V USB supply plugged in.

**Dave Jones:** Why am I measuring 5 V here if this diode is supposed to block it? Should be reading zero." Nah, it's because of the pesky leakage and the internal resistance of the multimeter.

**Dave Jones:** That's really interesting. And of course, the classic uh trap with uh using multimeters in circuit for measuring voltage is that you've got any point in your circuit, if you're measuring this point here in your circuit, just be aware that you're putting that 10 megaohm resistor across there.

**Dave Jones:** And if you're measuring voltages in high impedance circuits, that can really ruin your day. You can get false readings because your multimeter has a 10 megaohm input resistance or thereabouts on almost every voltage range, AC or DC.

**Dave Jones:** So, to show you the difference what the input impedance of your multimeter makes and how you can actually come a gutser in this particular case uh with a digital multimeter and its high input impedance, this is one of your more rare examples where lower input impedance helps.

**Dave Jones:** So, we've got 10 megaohms input impedance here, but let's get an old school analog multimeter. In this case, we've got a Bobby Dazzler. It's the Triplett 630-NA. I've done a teardown video on this.

**Dave Jones:** And you can see ohms per volt there. So, it's got 10,000 ohms per volt. So, we're on the 12-V range. 12 V * 10,000 is 120k, not 10 meg.

**Dave Jones:** There you go. Using another ohmmeter, we can actually measure that. 120k input impedance, as opposed to 10 meg. So, with our reverse biased Schottky diode here with 10 meg, we're measuring practically the 5 V.

**Dave Jones:** Now, if we plug in our analog meter in parallel, so we've got 10 meg in parallel with 120k, WHICH IS BASICALLY 120K. WHAT? There you go. It's dropped to 0.33 V.

**Dave Jones:** And if we actually lower the range down to three, well, we can barely see it. 3 V there. Look, 0.08 V. Now, if we go to 0.6 V range, then we're even lower input impedance on this multimeter, and we're measuring zero, exactly as we should.

**Dave Jones:** And if I go to the 6-V range, which I can because I've got a voltage doubler here, and if we forward bias our diode, there we go. We're measuring our 5 V, or 4.91 V with a bit of a forward bias voltage drop there.

**Dave Jones:** See? Input impedance, it's everything. Or another way you could have done this is use your low impedance range down here to actually measure. You're going to get like a 2k auto range, but it's so low, it's not going to measure it.

**Dave Jones:** But, it will measure the 5 V in the other direction. We're getting a bit more voltage drop there, 0.2 V because it's a lower value load. It's about 1k, 2k, something like that.

**Dave Jones:** So, there you go. Hope you found that video as interesting as I did. If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.

**Dave Jones:** >> [music]
