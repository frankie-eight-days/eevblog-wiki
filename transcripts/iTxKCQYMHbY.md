---
video_id: iTxKCQYMHbY
title: EEVblog #260 - Tracking Pre-Regulator Simulation in LTspice - PSU Part 13
url: https://www.youtube.com/watch?v=iTxKCQYMHbY
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 41, "3": 63, "4": 88, "5": 113, "6": 128, "7": 144, "8": 169, "9": 180, "10": 192, "11": 206, "12": 216, "13": 233, "14": 250, "15": 261, "16": 280, "17": 301, "18": 314, "19": 326, "20": 339, "21": 355, "22": 377, "23": 394, "24": 409, "25": 422, "26": 449, "27": 458, "28": 479, "29": 493, "30": 509, "31": 523, "32": 541, "33": 555, "34": 571, "35": 589, "36": 608, "37": 624, "38": 639, "39": 652, "40": 664, "41": 679, "42": 699, "43": 708, "44": 735, "45": 751, "46": 777, "47": 796, "48": 821, "49": 840, "50": 858, "51": 869, "52": 885, "53": 901, "54": 912, "55": 923, "56": 945, "57": 962, "58": 972, "59": 989, "60": 998, "61": 1016, "62": 1034, "63": 1044, "64": 1055, "65": 1072, "66": 1085, "67": 1095, "68": 1108, "69": 1132, "70": 1141, "71": 1162, "72": 1171, "73": 1186, "74": 1197, "75": 1208, "76": 1219, "77": 1229, "78": 1239, "79": 1251, "80": 1262, "81": 1281, "82": 1294}
---

**Dave Jones:** Hi, in my latest uh power supply video in my RevC schematic I showed how I used what's called a tracking pre-regulator uh to power my regulator, my LT3080 regulator up here so that it didn't dissipate as much power.

**Dave Jones:** I.E. The input side of it here, I wanted to keep uh only a couple of volts above the output voltage so that it doesn't uh drop out but it keeps the dissipation in the LT3080 as low as possible while still getting the advantage of uh the lower noise um inherent in the in a linear regulator for the output as opposed to a switching regulator.

**Dave Jones:** So, I used a tracking pre-regulator down here and it used an e-squared uh pot, one of these adjustable 5K um I-squared-C interface potentiometers that simply adjusted the lower feedback resistor in a typical boost converter like this Micro 2253.

**Dave Jones:** And uh quite a few people asked um uh maybe I should consider a uh tracking pre-regulator that doesn't require software which is one of the disadvantages of this one um is that well, one of the advantages too but a disadvantage in that it requires the software to measure the output voltage and then compensate, continually do that and then continually compensate uh the tracking pre-regulator voltage to match the output.

**Dave Jones:** So, it requires software overhead but it allows some uh flexibility in other aspects but people were asking why didn't I use a or uh consider using a track a fully analog tracking pre-regulator which simply took the output voltage of my LT3080 regulator and fed it back analog without any software and adjusted this DC-to-DC converter output voltage on the fly.

**Dave Jones:** And it's a good question. Uh I use the e-squared uh part because I've done this before. It worked. I wanted to use another I-squared-C device. It was I didn't want to muck around with a um analog uh solution for that.

**Dave Jones:** So, um but I thought I'd uh consider it. And as it turns out, the LT3080 data sheet itself um actually has Here it is. It's in an an example circuit you doing exactly that.

**Dave Jones:** It's got a uh step-down uh converter here on the input. But And it's got this uh TP uh uh 0610L uh P-channel MOSFET here working as the uh pre-regulator element to set the input voltage, in this case, approximately 1.4 V above the uh output voltage of the LT3080.

**Dave Jones:** So, that's actually uh rather novel that because it uses the uh threshold voltage of the P-channel uh MOSFET to actually uh set the voltage above um the LT3080 output voltage.

**Dave Jones:** It's very simple and uh elegant. I rather like it. So, I thought I'd get the uh LTspice uh circuit simulator out and uh uh see how it worked with a generic um step-up uh DC-to-DC converter.

**Dave Jones:** So, let's give it a go. All right. So, here we are inside uh LTspice, which is a free circuit simulator. It's very good. I highly recommend you get it if you want to play around with a uh circuit simulator.

**Dave Jones:** And because it's from Linear Technology, it has all the Linear Technology parts and pretty much only Linear Technology parts. But uh you can add other parts, but uh it has got the LT3080.

**Dave Jones:** Fantastic, which we use. That's great. So, I've uh put the LT3080 over here, and I'm using an which is a uh fairly uh generic uh step-up DC-to-DC converter. It works just like the Micrel 1 ones.

**Dave Jones:** They all basically work pretty much identically. Uh only very minor differences in there. They have the same uh reference voltage, and they work in exactly the same way. So, I have no doubt that if uh it works for the LT1934 uh 35, it'll work for my Micrel part as well.

**Dave Jones:** So, I've just start for the MOSFET here. I've just chosen a uh generic one from the list. It's got a whole list of uh MOSFETs down here. I just chose the first Fairchild one.

**Dave Jones:** I don't really care. Um I've got a 1 meg uh upper feedback resistor and a 10k lower feedback resistor. So, the upper resistor R2 here, that's just going to set the um upper uh voltage um three upper uh limit that uh this DC-to-DC converter can actually go to.

**Dave Jones:** I've set it to, you know, very high up to 1 uh meg, and then the uh MOSFET will actually uh control the output voltage of the DC-to-DC converter. But, you can actually lower R2 to give you an absolute like a safety uh feature so that your DC-to-DC converter doesn't go over a certain voltage.

**Dave Jones:** So, let's give this a go, shall we? I'm um got a R1 down here um on the set pin of the LT3080. It sets the output voltage. As you know, there's a 10 microamp current uh from the set pin of the LT3080.

**Dave Jones:** So, 10 microamps uh * 100k is 1 V. So, uh we should be aiming for a 1 V uh output voltage on our voltage regulator. So, we'll run this.

**Dave Jones:** I'm um running a uh simulation uh command here. A transient uh response uh stop time 1 second. Um you know, uh time to start saving data a millisecond. That sort of stuff.

**Dave Jones:** So, fairly generic. We'll give that a go. Let's run it, and uh and see what happens. Let's look at it. Probe our output voltage here. And it's set to 3.52 V and our output voltage here is spot on 1 V.

**Dave Jones:** So that's working a treat. And if you watch the values ramp up here, you'll notice that the voltage differential after it's settled down is higher here. This differential voltage here is higher than the differential voltage when it's ramping up, but it eventually settles down to a steady state and then what you see in there is the ripple.

**Dave Jones:** And let's take a look at the differential voltage where got 10 V output here and it looks like we're about 12 11.85 V or thereabouts. Let's, you know, say 11.8 V.

**Dave Jones:** So we're 1.8 V differential above the output voltage. That's not high high enough for us. It's high enough for the LT3080, but we've got an additional, if you remember the schematic for the power supply, an additional 1 ohm current shunt resistor in there which at 1 amp can drop up to a volt.

**Dave Jones:** So we're looking for about a 3 V voltage differential. And that differential voltage will of course depend almost entirely upon the type of MOSFET which you actually use here.

**Dave Jones:** It has some dependence upon the current as well going through here via your resistor values, but not a huge amount. So really you have to get the specific type of um of MOSFET in here and we've actually got the If we have a look at here, we've got the FDC 5614P and we're getting about 1.8 V on the simulator differential.

**Dave Jones:** So if we go in here and actually have a look at the data sheet for that, let's have a look at the gate threshold voltage VGS. There it is.

**Dave Jones:** It's about 1.6 V at an ID current of 250 microamps. So, that's not too far off at all. So, but it can actually vary in the range from 1 to 3 volts, but we're getting fairly consistent we're getting close to the typical value measured there.

**Dave Jones:** So, to get a higher voltage we're going to have to choose a different MOSFET. And I've chosen this second one on the list that's a Philips BSS 84 and we're getting once again it's not too far off the other one.

**Dave Jones:** It's around about 2 volts offset or 12 volts input voltage. And if we have a look at the data sheet for that device, well, it uh here it is here the gate threshold voltage at 1 milliamp ID is from anywhere from 0.8 to 2 volts.

**Dave Jones:** So, really there is no typical figure and we're actually getting that 2 volts. So, it says go have a look at figure 8 down here and that's the gate source threshold voltage as a function of junction temperature.

**Dave Jones:** So, really you know, we don't care cuz our junction temperatures pretty much only going to be ambient here, but it's showing a gate threshold voltage of around about 1 volt at 25° which is what the simulation would be running at.

**Dave Jones:** So, that is a whole volt out. So, this is you know, tricky business. You've got to choose the right device and you may have to actually practically measure it as well.

**Dave Jones:** But I know what you're thinking that's not a milliamp flowing through ID there because I'm now that red waveform there is actually the current flowing through R3 here which is you know, in the order of like 150 microamps or thereabouts.

**Dave Jones:** So, really we need to uh drop that to a K and run that again and see what we get. Well, there it is. It's up to around about a milliamp or so just over and we're getting um Let's have a look here.

**Dave Jones:** We're getting still our 2-V voltage differential slightly over it. Well, looks like we've run into a file here. I've I've changed the device to a SI3443 MOSFET and look what's happening to the output voltage.

**Dave Jones:** It's a fixed like 3.5 V and the output voltage of course isn't working cuz we're trying to set it to a volt down here and I don't know what's going on there.

**Dave Jones:** What? File. The simulation obviously doesn't like this SI3443 device. Very curious. And there you go. The same thing has happened again with an IRF7404 MOSFET. Exactly the same thing.

**Dave Jones:** It's It's really weird. It's as if that model is not compatible with this circuit somehow. There's something some little glitch in there, but this is not uncommon with simulators.

**Dave Jones:** You'll find that you know there are various configurations of things that cause them to play up and you know just not play ball generally with what you're trying to do.

**Dave Jones:** So, it looks like um the particular type of MOSFET which we're choosing there makes a difference. Let's go back to the BSS 84 here and let's close that and let's run that again and bingo.

**Dave Jones:** Now we're fine. No problems whatsoever. So, yeah. That is weird. Now, the first thing I'm going to suspect here is um the LT3080 because the gate here of the MOSFET is trying to read back from the output of the LT 3080.

**Dave Jones:** And that output is dependent upon the input voltage, which is set by the MOSFET, which then generates the 10 microamps to generate the set current through here, which generates the output voltage.

**Dave Jones:** So, that somehow, maybe, I'm thinking that extra loop in there is confusing it somehow to do with this particular MOSFET, of course. So, really, there's only one way to prove that, and that, I think, is to take the gate voltage from the set pin down here and drive our set pin directly, like we're doing inside the actual PSU circuit.

**Dave Jones:** Let's delete this here, and well, we can actually delete the resistor. We're not going to need it. Now, what I'm going to do is I'm going to actually insert a voltage source here on our set pin, like this, and we will That's exactly what we're doing inside our power supply circuit.

**Dave Jones:** So, we'll do that, and we'll set it to, say, 10 volts again. And I changed the output MOSFET back to the one that was giving the trouble. I've got the IRF 7407 in there, and let's take that gate voltage directly from down here, and let's simulate this sucker again, and see what happens.

**Dave Jones:** And bingo, we are getting a There you go. There you go. It's working. It's working a treat again. Not a problem. So, there you go. That was the MOSFET that was giving us trouble before if you measured our gate voltage from the output there.

**Dave Jones:** So, obviously, there's a there's a trap there in the model of how the LT, either the LT 3080 model, or how the MOSFET or the interaction of the two, you'd have to go in and look at the spice models themselves and know how the spice engine works and does all the simulation and things like that and maybe I'm someone who's more knowledgeable on that sort of stuff

**Dave Jones:** might be able to uh um figure out exactly what it's actually doing there but what I'm going to do is I'm now going to um take the gate voltage here and sense it from the output and see if it still works.

**Dave Jones:** Let's give that one a go and here we go. What? No, there we go. It's a problem. So clearly there's an issue there when it senses it from the output based on that MOSFET.

**Dave Jones:** So it's not really the set pin that's actually it's not really the voltage down here that's doing it. It's the it looks like it's the sensing from the output.

**Dave Jones:** So let's actually do that again and take that gate voltage from down here but don't have the voltage so forced on there. So just rely on the 1 meg to set the output voltage to 10 volts.

**Dave Jones:** So let's run that again and see what happens. Bingo. There you go. So we don't need to force that voltage. So it's not the So it's not the voltage being forced on there.

**Dave Jones:** It's it's actually the act of taking the output from there. So it's got something to do with that extra loop calculation or something it's got to do in there to to do that.

**Dave Jones:** So maybe there is some sort of something we can a few knobs we can tweak in the simulator to actually I get around that. I don't know. I'm not too fussy.

**Dave Jones:** I'm not going to look into it any further. If any anyone knows exactly why, please let us all know. But there you go. That's not an uncommon trap in these circuit simulators to actually find that you know, something there's some little oddball thing between the two components or with the simulator that doesn't work and gives you unexpected results.

**Dave Jones:** Now, if we actually oh, hang on. Something's going on here. Look at this. Our blue voltage, our output voltage is dipped back down. It's overshot. It doesn't it's gone up to 12 volts.

**Dave Jones:** It's gone way above our um Yeah, that doesn't work. Okay, that's not that's not good. So, we need to actually set that with the V set with the voltage set there clearly.

**Dave Jones:** So, that's not going to work. But anyway, these it's a common thing. These circuit simulators can get little traps like this. Imagine if we got that flatline that we had before first up when we first started running the simulator.

**Dave Jones:** If the first thing you see is a a silly flatline coming from this thing, then you're going to sit there scratching your damn head going, "What the hell's going on?

**Dave Jones:** I you know, why isn't my thing working? I'm using the right models and it's following everything and everything's hunky-dory." Imagine if you got that straight off the bat, you'd be absolutely you know, racking your brain trying to figure out what was going on there.

**Dave Jones:** And that can be a real trap with circuit simulators. Sometimes you got to play around with them to get them to play ball. Now, here's a MOSFET, the FQB 11 P06 that actually has a 4-V VGS, which is what it's showing here.

**Dave Jones:** But unfortunately, that's only available in like a power type package. It's a little bit expensive, not really what I want. I don't need a power uh MOSFET here. I want a little signal uh MOSFET.

**Dave Jones:** So, the parametric search is in like uh Digikey and stuff like that might actually be hard to uh come by because they do actually list the uh VGS here.

**Dave Jones:** Um but it's, you know, it's only a maximum value. They don't list the typical what it's going to be. So, there's the you know, there it is. So, it's really hard to sort of um might be a bit hard to find a suitable device using uh parametric uh search like this.

**Dave Jones:** Well, there's one way to actually uh deal with this. If you've got a particular uh low VGS device which you like, it's low cost, it's in the right package you want, and it's only got the 2-V offset, but you need say 3 V or something like that.

**Dave Jones:** Well, you can just whack in a couple of diodes in here, and that's exactly what I've done here. I've put in a couple of 1N uh 914s, which depending on the currently going to drop about 0.6 V each.

**Dave Jones:** So, you'd expect if this was if this BSS84 was giving us a 2-V offset before, you'd expect it now to be about 3.2 and bingo. That's exactly what we get here.

**Dave Jones:** I've run the simulation, and there it is. 10 V output voltage is the blue line, and about 13.2 V for the um DC-to-DC converter voltage. So, that's a little trick that allows you to boost the VGS of your chosen uh MOSFET just by adding a couple of diodes in there because gate and source you're just um increasing the value by putting a couple of diodes in there.

**Dave Jones:** But, that's not very good. If you use those diodes somewhere else in your design, that might be okay, but you've got two of them. What's a better way? Well, let's try something else.

**Dave Jones:** And one neat way to do it, of course, is to use an LED. So, that's exactly what I've got here. I've got a uh QTPL uh 690C LED. It's a typical uh, surface mount red um, LED and basically you expect about a 1.8 V uh, drop at a very uh, low current for this LED.

**Dave Jones:** So, if we zoom in here and have a look, we're getting bingo. If we're getting normally without uh, the diode without the LED there at all, we'd be getting about a 2 V offset.

**Dave Jones:** We're getting There it is, 13.8 or 3.8 V 2 + 1.8 V drop in our diode. And as a bonus, uh, you might be able to use that diode as a power indicator or something like that as well.

**Dave Jones:** I mean, there's not much uh, current flowing through this thing. If we take a look, there's only 1.2 mA flowing through this which is set by the lower the lower value of the resistor down here.

**Dave Jones:** But, um, you know, you can uh, change that value to actually um, give you a usable indication. But, a good uh, modern high-efficiency LED will um, still allow you to get, you know, a bit of brightness out at 1.2 mA.

**Dave Jones:** But, there you go. So, um, really that's a way that we can uh, tweak this um, to choose a MOSFET of our choosing that has the right package and the right voltage.

**Dave Jones:** But, just uh, boost it up a bit more so that we do have um, just adequate uh, margin on our LT3080 here because we need um, depends on the output uh, current.

**Dave Jones:** I think it's 1.6 V maximum is the absolute maximum uh, drop out voltage. It can be lower because our V control doesn't have to be tied to our input pin.

**Dave Jones:** We can try it tied to the other side of our um, offset our current uh, offset pin. If we take a look at the schematic back here. Oh, and we take a look at the LT 3080 again.

**Dave Jones:** Once again, the V the um, VC pin which powers the internal circuitry doesn't have to be powered from the input pin. We can actually take that. In fact, that's what I'm doing in this design.

**Dave Jones:** I'm taking it from the other side of uh, the um, current uh, shunt resistor. So, the dropout voltage effectively um is much smaller than if we just tied these two pins together, but depending on the package you get for the LT uh 3080, um some small smaller pin count packages actually have those two pins tied internally.

**Dave Jones:** So, you would have to take into account the voltage drop, but there you go. Um that's not a bad solution. I rather like that. I think I might probably implement this in my power supply design.

**Dave Jones:** So, I hope you enjoyed that. I'll catch you next time.
