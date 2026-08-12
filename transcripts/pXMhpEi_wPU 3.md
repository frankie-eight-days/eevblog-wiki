---
video_id: pXMhpEi_wPU
title: EEVblog #567 - Precision 1A Current Source
url: https://www.youtube.com/watch?v=pXMhpEi_wPU
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 28, "3": 46, "4": 69, "5": 87, "6": 103, "7": 119, "8": 134, "9": 146, "10": 164, "11": 179, "12": 193, "13": 206, "14": 218, "15": 233, "16": 247, "17": 264, "18": 276, "19": 293, "20": 308, "21": 322, "22": 337, "23": 354, "24": 368, "25": 383, "26": 397, "27": 415, "28": 432, "29": 448, "30": 464, "31": 476, "32": 490, "33": 503, "34": 516, "35": 529, "36": 545, "37": 558, "38": 569, "39": 585, "40": 598, "41": 622, "42": 639, "43": 653, "44": 668, "45": 683, "46": 697, "47": 713, "48": 724, "49": 738, "50": 756, "51": 773, "52": 788, "53": 805, "54": 820, "55": 839, "56": 852, "57": 869, "58": 892, "59": 909, "60": 924, "61": 942, "62": 955, "63": 968, "64": 978, "65": 992, "66": 1004, "67": 1018, "68": 1032}
---

**Dave Jones:** Hi, just a quick video on a little circuit that I thought I'd build up and breadboard test here. It is a precision 1 amp current generator and well, I thought well, you know, in theory it should work, but in practice I thought

**Dave Jones:** there might be a few issues. So, I thought I would just lash it up on the breadboard and you know, see how well this thing actually perform. Now, what I'm actually trying to do is get a as I

**Dave Jones:** said, a precision 1 amp output, which is pretty high for a precision constant current output and by precision I'm talking, you know, point over better than point over five percent and absolute. So, it's not trimmed or anything like that and the way I'm doing

**Dave Jones:** that is using a precision LTC 2655-1.25 volt voltage reference and that's normally point over two five percent accurate. So, you know, really quite a decent chip, you know, it's like 10 or 12 dollars in one off quantity. And basically I'm using that as a

**Dave Jones:** precision voltage reference driven across a precision resistor in the final product. I was going to have a not point double over two percent sorry, point over two percent precision resistor in here of 1.25 ohms and of course, Ohm's

**Dave Jones:** law 1.25 volts across 1.25 ohms, you get precisely 1 amp. Now, what you can do with these series voltage references or you know, some of them you can actually the ground doesn't have to be ground. So, you can actually float

**Dave Jones:** that above ground and what I'm doing is using a precision op-amp here. I've chosen OPA 376 for the job, you know, just a really low offset voltage so that the error the offset error of this thing is less than,

**Dave Jones:** you know, the uh point 025% of the 1.25 volts I want here, and I won't go into the math there. But anyway, nice precision uh op amp in there. And basically, what I'm doing, like normally this these precision references can only

**Dave Jones:** source, you know, 5 10 milliamps at best kind of thing. So, you know, it's not like you can get 1 amp out of it. So, we put in a series pass transistor, an NPN one. And just so happens in the data

**Dave Jones:** sheet for the LTC6605, it shows you exactly that configuration, a boosted output current configuration with an NPN transistor. It also shows you another one, boosted output current with an a uh PNP transistor. And um some other manufacturer data sheets use a PNP

**Dave Jones:** one as well, but this one shows, you know, look, 2N2222, uh I max, the maximum output current is set by uh you know, the current capability the NPN transistor. So, I thought, "Okay, I'll put in a Darlington because a you

**Dave Jones:** know, a 2222 is not going to be able to do an amp, and this chip, I think from memory, can only draw like source like 5 milliamps maximum. So, really the gain of uh this transistor here isn't going to

**Dave Jones:** give us our 1 amp output here. So, I thought I'd choose a Darlington NPN, a KSD1692, which looked like it would do the job. I'm not going to go into data sheets and explain uh why. I just want to show you

**Dave Jones:** the uh when the result I'm actually uh getting here. And basically, the good thing about this voltage reference is that it has a um a force output and a sense output. Now, most series voltage references don't have that. They just

**Dave Jones:** have a fixed voltage output, you know, 1.25 volts, 2.5, 5, whatever the output voltage is. This one has a sense one, that's so you can connect it directly across like a precision four-terminal resistor. And you know, that's that's

**Dave Jones:** really quite nice. And that's what allows you in this configuration to use this NPN transistor and then feed it back. And of course you got to have a minimum output capacitance on here as well for stability because a voltage

**Dave Jones:** reference has an internal error amplifier. And I knew that and of course error amplifiers just like linear regulators and low dropout regulators, they can oscillate if you don't have the correct, you know, bypass capacitors on the input and the

**Dave Jones:** output. So that's why I wanted to breadboard this thing up. I wasn't sure. I had a funny feeling that, you know, look it's in the it's in the data sheet, you know, it should just work, but does it? Hmm. Yeah, let's find out. Now, I

**Dave Jones:** forgot to finish explaining how this thing actually works. This op-amp here senses the output voltage across this output current shunt resistor here and then, you know, and it it just basically it's a buffer, that's all it is. And buffers that voltage to

**Dave Jones:** the ground pin. So it raises the ground up instead of being connected through the normal ground, it is the output of the op-amp here. So you raise that ground signal up so the difference between the output sense line here,

**Dave Jones:** which will be tapped, you know, on a in my final circuit tapped off like a four-terminal current shunt resistor like this, then 1.25 V is going to be present directly across that resistor. And by Ohm's law, you know, that's we're going to get a

**Dave Jones:** constant current out of here of 1 amp. And of course all the current flows or almost all of it flows through the Darlington NPN transistor up here with only a tiny, you know, a couple of milliamp milliamp or two. This KSD1692

**Dave Jones:** I chose actually for 1 and 1/2 amps collector current. I think it's like only 1 milliamp base current or something like that. So, you know, it's really nice high gain Darlington transistor. It should in theory work well. But yeah, so this one amp output here,

**Dave Jones:** you may be wondering what this diodes doing down here. Well, even though this op amp nice precision one is a rail-to-rail, if you are feeding this into a direct short, which you may want to do, you know, you're calibrating a

**Dave Jones:** multimeter or something like that. It's got a tiny current shunt in there, right? Then you're bringing this input here right down to ground and that and also the output right down technically to the ground rail here doesn't work

**Dave Jones:** that well. You're even though they're called rail-to-rail, you are still going to get, you know, tens of millivolts offset voltage. And of course, that just ruins your day. So, what you do is you just put a series diode here. It's

**Dave Jones:** dropping, you know, it'd be a Schottky type even though I haven't drawn that, you know, 0.3 volts or even standard diode at 0.6 volts. And then it just raises effectively the input to Well, it raises the voltage here. I'm sorry.

**Dave Jones:** And on the non-inverting input, at least 0.3 or 0.6 volts above. So, it's just above So, it's well above any ground sense issues with this thing. And so, you So, you're avoiding the offset voltage issues right down at the low end of the

**Dave Jones:** rail. So, that's why Anyway, that circuit should in theory work. But I had a thought that this thing could actually oscillate and it may not work that well. And sure enough, I built the damn thing up and well, no, it was horrible. So,

**Dave Jones:** what I've peeled it back to Let's go over here to my breadboard. Now, unfortunately, the voltage reference only comes in one of these tiny little pain in the ass 0.65 mm pitch MSOP packages. Just awful, really. But So, I

**Dave Jones:** put it on an SO8 adapter here. Pain in the ass SO8 adapter had the wrong body width on it. This I think I got these in the mail bag. The wrong body width. So I've had to actually bend the pins down

**Dave Jones:** in there. Absolutely horrible. Anyway, there's my op amp which is an SO8 and this thing even though it's um 0.65 mm pin pitch, I was able to squeeze it onto uh with a bit of uh you know, trickery down there onto the SO8. I

**Dave Jones:** might get the macro lens and show you that up close. So there you go. Even though it's an SO8 adapter, the two middle pins can solder directly on there. And what I did is just lift up the outer pins and then just, you know,

**Dave Jones:** put some little jumper wires over there like that. So that's how I can fit a different a smaller pin pitch one onto a standard SO8 adapter because I didn't have any adapters of the right pitch. Anyway, so this damn thing didn't work.

**Dave Jones:** So what I've done is I've basically uh take I've disconnected the op amp here. So just imagine that's not there. And I've just got my voltage reference with a 2N uh 2222 transistor in there. I've got a load on there of

**Dave Jones:** uh 222 ohm resistors in parallel. So, you know, we're talking this thing should generate about 110 milliamps or thereabouts. You know, well under the 1 amp I want. Um but I just scaled it back to get exactly the same circuit

**Dave Jones:** that they've got in the application note here. And, you know, the bypass yeah, I've got no bypass caps directly on there, but the whole idea of this was that um look, if it worked on a breadboard like with this with the

**Dave Jones:** bypass caps sort of, you know, like a centimeter or or two away at most kind of thing with, you know, going through a breadboard. If it's stable there, then you can be pretty confident when you tighten the loops up and everything on

**Dave Jones:** your final PCB layout, it's going to work a treat. So, you know, I really wanted uh good confidence that it worked on the breadboard. But, you guessed it, it doesn't. And that is my 1.25 V output voltage. And as you can see, 200,

**Dave Jones:** 400, 600, 800, uh 1 V, 1.2, you know, it's near to there, but look how fuzzy it is. It's just got all crap on it. And if I have a look at uh this is the sense output, by the way. And if I have a look

**Dave Jones:** at the force output pin, look at this. Hey, oscillation. There we go. Look at that. Ah. Bob's your uncle. So, that right there is 20 mV per division AC-coupled. That's my sense output. Look, it's just all absolutely horrible. Ah, man. So, just

**Dave Jones:** ignoring all that, I've just got their basic circuit in there. I've got a 10-µF ceramic uh output cap. I've got um a ceramic input bypass cap. Albeit, yeah, they are on the breadboard, but, you know, 2N2222, they make it look like

**Dave Jones:** this thing will just work. And, you know, IMAX, you know, they don't even give you sort of, you know, a maximum recommended output. So, this thing just doesn't work in the application note. Maybe if we tighten the loops up a bit.

**Dave Jones:** Ah, but jeez, it's, you know, it's a bit touchy. So, I actually expect the PNP one possibly to be more stable in that respect, but this, for example, like, you know, 35 mA maximum output. So, I don't really want

**Dave Jones:** to press that one into service to try and get my 1-A output. I wanted to, you know, persevere with this circuit and see if I could get it. So, that's my sense output there. Watch what happens if I disconnect the input bypass

**Dave Jones:** resistor. And I've got this coming from my Rigol linear bench supply, 5 V, by the way. The input voltage really doesn't make a make a difference at all. Let's remove that and you can note that's the input bypass cap and

**Dave Jones:** that's my sense output. You notice the noise went up. Now, I'll just whack in a another bypass cap in there to replace that. Oh, look at that. There we go. Woohoo! Now, one interesting thing with this Rigol scope,

**Dave Jones:** look, I'm not sure, I can't remember which firmware version I'm running, but I might have found a firmware bug. Look at this, right? You know, it's like it's not uh triggering properly. It's jumping all over the place. Now, if we stop

**Dave Jones:** that, of course, we should get a nice clean waveform, but we don't. Look, it's furry and like it's, you know, it's jumping all over the shop just like you get on that. Now, I'm not sure if that's a feature. Now, when you change the time

**Dave Jones:** base, but, you know, it works. So, that's what I would have expected when you press the stop button, but no, it doesn't. It it I don't know. Feature or bug? You tell me. Anyway, so, that's how sensitive this thing is just to, you

**Dave Jones:** know, the bypass cap like that in there. So, that input bypass cap seems pretty critical. So, what I might do is actually go in there and like solder it directly on the pins of the adapter or something like that. Maybe

**Dave Jones:** not directly onto the chip itself, but maybe onto the adapter and well, that might improve things. All right, so what I've done is soldered uh bypass uh input cap directly across that and let's see what we get.

**Dave Jones:** Look at that. Absolutely awful. And that's directly across the pins of the SO8 adapter. How close does this bloody input bypass cap need to be? Unbelievable. So, if we put the original one back on there as well, look, there we

**Dave Jones:** go. That's knocked that down. I mean, it's still bad. I mean, it's still oscillating, especially for a precision reference. It's absolutely useless, but there you go. That is loop stability of the error amplifier inside this bloody voltage reference.

**Dave Jones:** Ah, it's all over the shop. Now, of course, if we put no load on there, it should be okay. And yep, there it is. 1.2502 volts. And yeah, I have actually done the I have configured it without the

**Dave Jones:** series pass transistor in there at all. So, just the voltage reference V in V out tied force and sense together. And yeah, it's you know, it's exactly spot on like that. So, it's okay, but once you put any sort of load on this thing,

**Dave Jones:** it's useless. It just takes off. So, there it is normally, and let's hook up a 40 4-ohm resistor, which is about 28 milliamps or something like that. Here we go. Here we go. Look, you can see it. Not

**Dave Jones:** that you know, for a precision reference, it's just no good. It's hopeless. And if we swap the transistor for our high gain Darlington KSD3692, and let's have a look what happens. This is with no load at all. There we go, and that's the force line.

**Dave Jones:** There's the force line. Woohoo! Look at that. And of course, this is going to be a function of the output capacitance as well. So, I've got a 3.3 mic poly cap in there instead of my Well, in parallel with my 10 mic ceramic, and I

**Dave Jones:** can actually, you know, take those out. And I've had a play around with it. And here we go. We change our config We change the oscillating frequency. Look at that. And the type totally, but the thing is still

**Dave Jones:** oscillating and that is the sense output. That is not the uh force output. So, here's the force output. Look at that. Whoa, man. There's a shocker. Woo. So, sorry for those of you like a happy ending on their video. I said this

**Dave Jones:** one will be quick. So, there is no happy ending. I haven't finished playing around with this thing at all. I just wanted to show you that uh you know, don't just trust the application notes like that in the application circuits.

**Dave Jones:** Build them up and verify that they actually work because this one oscillates like a So, sure. Yeah, if you build this up on a PCB, you know, it's going to be uh the loops are going to be tighter and of course you have to

**Dave Jones:** choose your components carefully and it's going to be better, but the fact is, you know, you may not get this on the first spin or the second or the third. You know, it's a pain in the ass. So, if you can't get it just, you know,

**Dave Jones:** at least um semi-stable on a breadboard like this just using uh you know, when you're trying different types of input and output caps and things like that and it's just all over the shop, then you know, you're going to be in

**Dave Jones:** trouble. You know, you just don't have good confidence in this thing building up on a breadboard. And yeah, like try doing an amp on this thing and other stuff like forget it, you know, that's just the um transistor, you know, on its

**Dave Jones:** own with no load and it's oscillating like that. It's just crazy. But hey, you know, that's what I suspected it would do and it certainly did. So, I'm glad I didn't uh go straight to PCB on this circuit. And so, just be wary of these

**Dave Jones:** sorts of things. Don't trust those app notes. Hm, especially stuff like this with error amps. And yeah, this is going to uh there's going to be a lot of factors involved here for the uh stability of uh the error amplifier inside this uh

**Dave Jones:** reference. So, you know, really it there's a lot involved in getting this thing right and it's not going to happen today. But anyway, I hope you enjoyed that video. Catch you next time.
