---
video_id: T2aa3X8Y0xs
title: EEVblog1541 - What is this Blown SMD Component? Redux
url: https://www.youtube.com/watch?v=T2aa3X8Y0xs
source: youtube-asr
---

**Dave Jones:** Hi, we have another failed part search video cuz the last one was reasonably popular that I did back here and I'll link it in if you haven't seen it from uh Pooriya Solutions LLC. Well, as it turns out,

**Dave Jones:** the same poster on uh Twitter has sent in yet another one. Uh you saved me once before. Um help with new part ID. So, let's take a look at it because it's interesting to search for uh you know,

**Dave Jones:** failed components cuz this is a common thing you might have to do. You might have to repair a product which you didn't design. So, you've got no schematic for it. You've got no idea. All you've got is the uh part ID on it

**Dave Jones:** hopefully if it's not, you know, burnt off or anything like that when the magic smoke escaped or uh it's just got some obscure code or something like that. It's non-obvious. You've got to figure it out from the rest of the circuit.

**Dave Jones:** This one's going to be relatively quick and simple. I'll link in the last video if you want a bit more in-depth. Anyway, um it looks like we're repairing a Hantek uh handheld oscilloscope here, the uh 2000 um series. So, here is the

**Dave Jones:** suspect in question, U15 here. It looks like, yeah, Ernie Bernie marks on here. It looks like the magic smoke uh has escaped from this. And uh curiously though, the uh design uses another part here which is identical elsewhere in the

**Dave Jones:** design. So, from that we can uh pick out the code here which is 31. It's hard to make out, but that's actually a three. That's actually 31 30 here and the OP tells us that in the uh Twitter post.

**Dave Jones:** So, that's handy and here's an overview of uh the entire board inside the oscilloscope. So, it looks like it uses uh 2 18 uh 650s here, uh rechargeable batteries. And you can see in here, yeah, possible Ernie Bernie mark. That's

**Dave Jones:** where it's uh that's where it's come a guts out. And this is where that other identical one is over here that we actually saw here. So, you can see that's that's part of the uh label over here like this and you can see the trace

**Dave Jones:** coming down like that. So, you can see yeah, label there, trace coming down like that. So, identical part here and here. And an important clue in debugging problems like this is component location. So, you'll notice it's connected through to the tab of this

**Dave Jones:** cell here and this one is likely cuz it's right next to the pin here. Uh Yeah, yeah, yeah, there it is there, right? It's going in there like that by the looks of it. Um so, component placement is everything. So, you know

**Dave Jones:** that the component that we're looking at is right next to the 18650 batteries which don't look like they're just in parallel or series. It looks like they're somehow independent. They could be in series and you know, they could be

**Dave Jones:** like tapping off the middle or something like that. Don't know. But if you only had these two photos to go by here, then you know, it's a little bit harder cuz you wouldn't know the proximity to the batteries. But the battery proximity is

**Dave Jones:** a clue. But anyway, looking at the pin configuration here, you can see that these two pins are shorted together. That's quite unusual. And you can see that this pin here, unless there's a hidden via under there, it doesn't look

**Dave Jones:** like it, that is not connected at all. And then this pin buggers off down here. We can't see what else is down there. And then this one just has a single cap on it. So, given the width of this

**Dave Jones:** trace, it could be a ground. For example, you would assume because when you're designing a PCB, you'll run thin traces like these for the signal wires and you'll run generally the thicker traces for power. So, you can and and

**Dave Jones:** this one's got multiple vias up here, right? Three vias in there. There's a via down here, right? And and this one is quite thick. So, you can assume that these are like power and ground or power rails or something like

**Dave Jones:** that. So, maybe that's the supply for the chip, whatever this doing. But it's got a rather unusual pin configuration. And of course, here's where it pays to know your packages as well. This is a SOT23 package, but it's a five-pin, so

**Dave Jones:** it's what's called a SOT23-5. And that's going to be valuable in our search. But we also know that we've got a series resistor in here as well. So, we've got some sort of RC configuration, some sort of filter configuration. So,

**Dave Jones:** that could be like a power rail or something like that. We don't know if this is like an output. Uh you know, it's hard to tell. But certainly one of the first things you'd suspect is ah it could be a fixed voltage regulator cuz

**Dave Jones:** it's just got a single output filter cap, for example. And I don't know, that could just be a jumper for measuring um you know, in-circuit currents or something like that. Or it could be limiting uh something else. But you

**Dave Jones:** know, I wouldn't rule out a voltage regulator there. So, that'd be one of my first picks. And certainly you could have like a low-power fixed voltage regulator like an LDO uh directly connected to the battery like there. It

**Dave Jones:** could be powering that soft power-up uh circuit because the uh the thing uses like that there's that's that's the power button. I think uses a soft uh power button. So, you know, you you wouldn't rule that out. But

**Dave Jones:** but anyway, the first line and not always, but often is the part number and then the second one is a batch code, a date code, manufacturer's code, something like that. Could be a package code or some other variant uh code. But

**Dave Jones:** we would uh concentrate on 3130 cuz that kind of like that sounds like a part number. So, given the pin configuration like this SOT23-5 and uh you know, and the cap here, you might be thinking a low-dropout voltage

**Dave Jones:** regulator, you might be thinking a MOSFET uh for example. So, you know, something like that perhaps. But then when you take into account the location here, you also might be thinking something to do with the 18650 charger. Uh you know, cuz you got to charge these

**Dave Jones:** batteries presumably like is that a USB There it it charges externally. So, you might be thinking, "Okay, it's part of the charging circuitry. It could be part of battery protection, for example. It could be reverse polarity protection or

**Dave Jones:** some other battery charging protection, battery management, something like that." First thing, of course, see if you can get lucky, Google search it, 3130. Always put like PDF after, or you could put data sheet or something like that, but the PDF is often just enough.

**Dave Jones:** Look, we've got an Allegro data sheet. No, that doesn't look like it. Um the Hall effect switch is not a Hall effect switch. Portable pressure calibrator. Yeah, nah. Oh, a microchip 3D gesture recognition and motion tracking controller. It's not going to

**Dave Jones:** be that, right? So, no, it looks like we're not really lucky there. Like this is just like, yeah, that's a Hall effect switch. Nah, we're not there. So, you could put 3130 regulator PDF, uh op-amps. It doesn't look like an

**Dave Jones:** op-amp circuit configuration. There's no feedback resistors or anything like that. Just had that RC filter there. It's not that. CA3130 op-amps. No, it's it's not really going to be an op-amp. So, I would you wouldn't even bother going down that rabbit hole. Analog

**Dave Jones:** Devices Jobby 3130. Ultra low noise 1.2 meg PWM architecture. No, it's not going to be that because there is no like there's no inductors or anything else. There's no magnetic components around that. So, this is not anything to

**Dave Jones:** do with a switching regulator. So, if we go 3130 MOSFET, what do we get? MOSFET single power N-channel. TSOP. No, that's a TSOP six. That's not it. We've got the op-amp again. We've got a P-channel enhancement mode MOSFET. And we can

**Dave Jones:** check out that, but that's, you know, only a three-pin SOT25. So, it's not going to be that. So, we could put in SOT23-5 into our search terms. So, specifically the five-pin SOT23 like this. And there's that same diodes incorporated,

**Dave Jones:** but uh-huh, we might be getting lucky. Look at this. ABRCL3130 contains advanced power MOSFET, high accuracy voltage calibration circuits, put in an ultra-small SOT23-5. Let's have a look at this bad boy. What does this do? High integration solution for

**Dave Jones:** lithium-ion polymer battery protection. Now we're getting somewhere. It contains an advanced power MOSFET, high accuracy voltage detection circuits and delay circuits in a SOT23-5 package. And here's a typical application. Uh-huh, look at this. So, bingo, what do we have here? We've got

**Dave Jones:** two pins tied together just like we saw on the PCB. We've got an RC circuit with a power as we speculated at the start that that was a possibly a a power pin. So, it looks like there's a MOSFET

**Dave Jones:** inside here which switches between it in the charger negative line like this cuz it's a battery protection. It's measuring the battery it's monitoring the battery voltage through the VDD through the actual power pin. So, it's doing the monitoring and it's powering

**Dave Jones:** the chip as well which is a really nice solution and it's a battery protection device. So, you still need your charger circuitry out here somewhere. But this is just and that explains why also we would see two of them here and here

**Dave Jones:** because you've got one of each protecting each battery cell here. So, that's that's we Have we got a winner winner chicken dinner? Well, here's the pinout here. Four and five tied together just like we saw. This is the dodgy one here certainly. They're

**Dave Jones:** shorted together. This is the other one. They're shorted together. So, and then pin one here we said was not connected. Sure enough, over here, VT, this is the test pin. Uh you would leave that open. You almost unless they tell you it it

**Dave Jones:** specifically tell you here, you know, you must uh tie that test pin, you can look elsewhere in the data sheet, but I guarantee a test pin you leave open, disconnected, unless told otherwise. And if you don't know, manufacturers use

**Dave Jones:** these uh test pins. Yes, it does have circuitry connected up to it, but you might have to apply a certain voltage to it or certain signals or something to get it into a test mode. But yeah, that'd be for their uh automated uh

**Dave Jones:** production testing. So, they'll give you no details on that unless you're manufacturing the chip. You won't know what that is. So, you leave it alone. And of course, uh VDD and pin two here is ground. So, that's what we uh saw

**Dave Jones:** here. That's what we suspected that that one might might be a ground there. And of course, as you saw the RC uh circuit here powering this thing, and Bob's your uncle. We've found it, right? It It has to be this part. There's absolutely no

**Dave Jones:** way. It's not like it It may not be this actual manufacturer. There may be someone else. Uh Shi- Shikues? Shi- Shiyues? I don't know how you pronounce that. Never heard of them before. And the interesting thing is you can't

**Dave Jones:** actually buy this from LCSC. They've got 80 in stock there. There it is. Um but it looks looks like they got another variant, the SKCL 3130. So, we should have a look at that one cuz it could actually be that. They're

**Dave Jones:** both SOT23-5s here. So, yeah, I wouldn't I wouldn't rule that out. What is the difference here? So, it could be either of those. It's a series high integration lithium ion protection. It's protection again. I don't know. You'd have to go into this

**Dave Jones:** It's exactly the same configuration. So, the only difference is the BR at the front or SK at the front. So, you might have to go into If In fact, if you're replacing this, I would uh like they've got the two different ones for a reason.

**Dave Jones:** So, So, it's got all this cool stuff in, and it should have an internal diagram. Yep, yep, there it is there. Right. So, it's got tons of stuff. So, it's got overvoltage, overcurrent, you know, detection and stuff like that. Charge

**Dave Jones:** detection and everything. Right. It's got overtemperature protection built in. So, it's got a little, you know, silicon temperature sensor and stuff. So, yeah, okay. What's what's the difference? So, we actually flick through these. Um having a hard time seeing the

**Dave Jones:** difference. The top level stuff is exactly the same. Okay, it must have some small operational difference. No, I'm not seeing the difference in the internal logic. What? Is it just a Well, it's the same package. Zero volt battery charging

**Dave Jones:** function. Oh, jeez. We're going to need like a difference comparator to highlight the differences between I'm I'm not seeing it. The difference has to be absolutely minute. Oh, here we go. I'm seeing a little change in this wording down here. No,

**Dave Jones:** they've just got the word the there instead of turns the controller off and stops charging. Oh, okay. Over discharge condition. This looks different. Yes, I'm I'm I'm not going to like go into the in-depth differences between those. But if you were, you know, it could make

**Dave Jones:** a significant difference if you were actually to choose the correct one there. So, that's rather interesting that we found a part that has that subtle little difference. So, anyway, if you didn't get lucky with like a Google search like this, then you have to start

**Dave Jones:** going into you have to try and figure out what type of chip it is. So, let's actually let's let's take out MOSFET there. Let's just search for 3130. Yeah, it's it's the first link there. So, just 3130 sot23-5. Can we remove PDF? Is that

**Dave Jones:** going to get us lucky? Yeah, it's still it's still the first shot there. It's still the first result. So, that's that's pretty lucky Google foo there. Just to type in 3130 and sort 235, but if you don't type in the package, let's

**Dave Jones:** try just sort 23. Oh, yeah, we we we still get it. So, even not putting in five, we still get that as the first thing. So, this could have taken us seconds or it depends on whether Murthy's asleep today or not. But

**Dave Jones:** anyway, for a product like this, you could search your Digi-Key's and your Mouser's and your other Western sources, but often you might go into I like using LCSC um for cuz they do great parametric and like functional search as well. So,

**Dave Jones:** we can go into battery management ICs. So, you might like find it's a battery You could probably type 3130 into there and you'll find, you know, it'll be one of uh the parts. But, you know, you could go in here and type, "Okay, uh you

**Dave Jones:** search You might think it's a battery management IC." So, you go in here and you can eliminate all the packages. So, you go all the way down here and sort 235 and sort 235L. L is the low profile, so

**Dave Jones:** it's just thinner if you're designing ultra-thin mobile shoe phone or whatever. Um, so then we apply that and that's 205 parts remaining, is it? And then yep, there it is there. We actually got it. Um, sort 235 battery management IC.

**Dave Jones:** There's another battery management IC, but that's, you know, they aren't the right numbers. But yeah, yeah, bang, we got it there by just searching for the category of battery management ICs and or you might search for battery protection or

**Dave Jones:** something like that as well. And sort 235, the package type, bingo, we got it. But not always got fairly lucky today. So, there you go. I hope you enjoyed this component search video. Even this one was relatively simple and we got

**Dave Jones:** fairly lucky fairly quickly. It's a MOSFET battery protection IC. So, the charging circuitry must be elsewhere. But anyway, thank you very much Pura Solutions. I'm sure I'm butchering that for yet another rather interesting repair component failed component search

**Dave Jones:** where the magic smoke escaped. If you like these types of videos, please give it a big thumbs up and as always discuss down below. Catch you next time.
