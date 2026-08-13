---
video_id: MwvjAtSr5t8
title: EEVBlog #379 - Yamaha RX-V557 Receiver Fix
url: https://www.youtube.com/watch?v=MwvjAtSr5t8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 57, "4": 77, "5": 93, "6": 109, "7": 137, "8": 153, "9": 173, "10": 201, "11": 217, "12": 233, "13": 245, "14": 265, "15": 281, "16": 301, "17": 317, "18": 333, "19": 353, "20": 369, "21": 389, "22": 405, "23": 425, "24": 445, "25": 465, "26": 485, "27": 509, "28": 529, "29": 553, "30": 573, "31": 593, "32": 609, "33": 625, "34": 645, "35": 661, "36": 681, "37": 701, "38": 721, "39": 737, "40": 757, "41": 781, "42": 793, "43": 809, "44": 825, "45": 845, "46": 873, "47": 889, "48": 923}
---

**Dave Jones:** Hi, yes, we're back on the Yamaha amplifier again. I woke up this morning and decided that I'd have another go at it, and I realized, well, that 4.8 volts on the 5 volt rail was suspicious, as I said in the video, and I thought I'd start by tackling that, but I

**Dave Jones:** uploaded the video last night, I woke up this morning and looked at all the YouTube comments and everyone's saying, it's C405, it's C405, just replace that and Bob's your uncle, and there it is, there, that's what everyone's talking about, C405 223, 22 nanofarad, 6

**Dave Jones:** 30 volt green cap, as they call them, or a metallized polyester capacitor, and everyone's saying that one's the culprit in the switch mode power supply, it's a common fault for these Yamahas, well, yeah, okay, if you serve as Yamahas, maybe it is, but

**Dave Jones:** I don't, these things usually don't fail, I don't think I've ever, I can't recall one of these 630 volt metallized polyester caps failing before, but eh, who knows? So I'm going to desolder that sucker and give it a go. And here's the one I've just desoldered

**Dave Jones:** and I didn't have any in stock, so I had to go to Jaycar and pick one up and it's a 223, 22 nanofarads the voltage isn't marked on there, but Jaycar assure me, it is 630 volts, certainly looks like one, and it's a Suntan brand

**Dave Jones:** registered trademark, hmm, Suntan well, yeah, I might get a Suntan from the explosion that is going to happen when I replace it with a Jaycar cap, but eh, it'll be good enough for today, let's give it a go. And yep, I think we might be onto something

**Dave Jones:** here, check it out, 585 picofarads it's supposed to be 22 nanofarads, so way out, I mean that's at 1kHz, 10kHz, 100kHz eh, whatever, it is way, way off track, so there you go, it has genuinely lost its capacitance, because unlike electrolytic caps like these for example, when the electrolyte

**Dave Jones:** inside actually dries up, these can still retain their capacitance but have high ESR, as we've talked about on many videos, and you can't necessarily see that one of these electrolytic caps has failed just from the capacitance, but it doesn't really happen to these

**Dave Jones:** so this one has genuinely kicked the bucket, so hopefully that will fix it, and that low capacitance obviously was enough to still give it 4.8 volts out on the rail, but maybe now we'll get 5 only one way to find out, let's power it up, and here we go

**Dave Jones:** will it work? Will it work? It's on! Oh yes! Oh! Winner! It was! Look at that! You son of a bitch! Bloody cap! So it was what everyone, well a few people anyway 3 or 4 people said all along, it was that cap, so it was that common fault all along, yeah, common

**Dave Jones:** if you're in the industry and you're used to repairing these things and you know but look at that! You little ripper! What a bobby dazzler! And of course there's probably a lot of people right now just laughing and gloating na na na na na, I knew that, I'm smarter than you!

**Dave Jones:** Yeah, great! Well, you know, if you're into servicing these sort of things and you know that that cap is a common fault, obviously people just said replace C405, replace the red cap, yeah okay, great! Who first found that? You know, and how long did it

**Dave Jones:** take them? And well, you know, I would have eventually found that, I was going to come back this morning and I thought I'm going to tackle that 4.5 volt 4.8 volt rail, so let's actually measure that now and see if it's gone back up to 5 volts.

**Dave Jones:** No, there you go see? It's still 4.83, well it's a bit higher than what it was before, but maybe there's a bit more ripple on it perhaps, or a bit less ripple now or something like that but really that was essentially the same as before, so

**Dave Jones:** it hasn't fixed that, well there you go, 4.79 it's the same. So there you go, as far as the meter's concerned at average DC, it's measuring basically the same so I can only come to the conclusion that it was extra ripple on there or something

**Dave Jones:** caused by that cap being low in value, or something like that, because possibly the under-voltage detection trip out of the microprocessor when it powers up, maybe it's got something like that, you know, it checks to see if the power's good and at a certain level, and maybe that

**Dave Jones:** cap just dropped it under that, but that was leading me astray so if I actually followed that thought that I had last night, that I'd troubleshoot that 4.8 volt rail yeah, I don't know where it would have led me, but I would have

**Dave Jones:** the first thing I was going to do was rip this board out and just, you know, start checking all of the caps in it I wouldn't have suspected the green caps, but I would have measured them anyway, those metallized polyester caps, I would have measured them as a matter of course

**Dave Jones:** just as a methodical thing, which it really wasn't warranted yesterday, when I was playing around with this thing. Yeah, it measured the ESR of a couple of the electrolytic caps, but you know, I wouldn't have expected one of those metallized polyester caps, especially when I was getting pretty close

**Dave Jones:** to the voltage claimed in the service manual for that test point so that's an example of one of those unusual and annoying faults that lead you up the garden path, because you know, the first rule of troubleshooting is thou shalt test voltages, and that's what I was doing, I was getting that

**Dave Jones:** 10.2 volts, I was getting the 5 volts, I checked the voltage regulator, the linear 5 volt regulators on the main board and they were all okay, and you know, everything seemed within tolerance, and you know, and it should have you know, and that shouldn't have been the problem, but well, there's something a bit more subtle

**Dave Jones:** in there, I'm not going to really look into it, I don't care I don't want this video to be another 40 minute job, so what do you know that little bastard right there was the culprit, and it was staring me in the face the whole time, look at it!

**Dave Jones:** I'm the culprit, look at me! Bastard! And yeah once again, it came down to another cap failure, but unlike previous repairs of the monitors I've done and other gear, it's not a classic electrolytic it's a metallized polyester, go figure, well there you go

**Dave Jones:** that's one for the books folks. Now a more common failure mode for these metallized polyester, or sometimes known as film capacitors, more generically known as film capacitors, is a short circuit rather than losing their capacitance like this, but this one I've measured it and it is fine, there is

**Dave Jones:** no shorting or anything else, and you certainly wouldn't get 586 picofarads if it was on the LCR meter, so this one has just lost its capacitance, something, there's some failure mode inside this thing that's made it lose the magic smoke, and its capacitance has dropped

**Dave Jones:** dramatically to the point where it was just capable of keeping the circuit working and still generating that 4.8 volts output voltage, but for some reason not high enough to, you know, make the circuit work as intended. What a bastard. Alright, now let's take a look at what this sucker is doing here.

**Dave Jones:** Now we've got the mains power input here to power cable, there it is, and it comes directly into here and there's our culprit, C405 it just taps the AC mains straight off through this 2.2k resistor here, down into a Zener diode, and then through this

**Dave Jones:** half-wave rectifier here, filtered by C406 there, by the looks of it, and that generates the DC rail, by the looks of it, that powers our control chip over here, and we'll have a look at that in a sec. Now the mains also here goes off

**Dave Jones:** to the transformer, and then the transformer goes through this bridge rectifier here, and that through this switching FET here, Q404 switches that through to the ground of the circuit here, which is not the return for the... here we go, here's the return. The return

**Dave Jones:** is AC coupled through C409 there, through back to the mains earth back there. So this is a rather unusual arrangement, and it'd be interesting to get the scope on it, but I'm not going to do that today, you need a proper isolated probe to muck around on the mains

**Dave Jones:** on the primary side of things like this. But this diode bridge effectively switches, well this FET effectively controls pulsing in this transformer, which then of course generates the pulses in the secondary side here, which is full-wave bridge rectified, and then filtered by C411

**Dave Jones:** down here to generate our 10 volt, that generates our 10 volt rail, our 10.3 volts nominal, which we were measuring just fine and dandy. So as I said I think there was excess ripple in there, which we would have really only found that

**Dave Jones:** if we had a scope hooked up to this thing and we knew what the level was supposed to be, because you know we were getting like 10.2 volts or 10.28 or something like that. Now if we have a look at this controller chip here, you would think

**Dave Jones:** okay it's some switch mode controller IC, very advanced but take a look at the part number. It's not! It's a TC4013 and that's not some obscure one, yes folks, that is a 4000 series CMOS dual flip-flop, and that's all it is. So they're basically taking

**Dave Jones:** 50 hertz in here, they're half-wave rectifying it, generating that voltage rail up here, VDD, for the chip. The one flip-flop in here is not used, you can see they've tied all the inputs low there, but the other side, they are using it, and they

**Dave Jones:** tap off various parts to generate the clock. Here's this 1 mega resistor through R413 here, and then they filter that a little bit with C407, and that generates the clock pulses into the digital clock pulses into the 4013 here. And then the data

**Dave Jones:** line for that is then tapped off the half-wave rectified part here. So you know, it's absolutely bizarre. And then they've got something else going on here, some sort of feedback mechanism from the Q1 output here through these diodes. Oh, I'm not even going to bother thinking

**Dave Jones:** about it. If you want to try and simulate or analyze how this whole thing works, it would make for some interesting investigative work, actually. This is their low-power, this is how they get their 0.1 watts standby, this is their ultra-low-power green power supply.

**Dave Jones:** Green in quote marks. And it's, you know, it's rather novel and convoluted at the same time. So your guess is as good as mine. Why C405 there when it presumably lost its capacitance? I don't know what happens to it at the high voltages.

**Dave Jones:** I only tested it on the LCR meter at low voltages. It will be different most likely. But that dropped from 22 nanofarads, its original value, down to like, you know, 500 picofarads. 500 puff. But it was still able to give 0.3 volts out of here, nominal.

**Dave Jones:** So your guess is as good as mine as to what lowering that value there did to the clocking, the 4013 flip-flop here, which then controls the switching FET for the bridge rectifier and the primary side of the transformer. Oh man, go figure. So that is one of those pain-in-the-ass fixes where the voltage

**Dave Jones:** is measured, you know, fairly close to what you expected. So you sort of, you know, move on, okay, tick, move on to something else to see if there's something else obvious. And this is how you can waste hours and hours of service time.

**Dave Jones:** And you wonder why service techs charge so much sometimes if they, you know, if you didn't know that C405 was a common fault in these Yamahas and you had to start from scratch like I did, and I'm not a service repair tech that does this for a living.

**Dave Jones:** And you know, you've got to trace these things and you can be led down the garden path and you wonder why it takes them hours and hours to fix just a simple bung capacitor in there. I mean, yeah, okay, with hindsight we could have gone through and

**Dave Jones:** systematically tested all the capacitors in here and checked them. And yeah, with hindsight we would have found that problem, because that would have stuck out like a pair of dog's balls really. A C405 would have, you know, 500 picofarads, bang, oh that must be it, replace it, bang, fixes it.

**Dave Jones:** Not a problem. But, eh, didn't happen. Them's the brakes. I'm a man, I'm a thunder Can't you hear, can't you hear the thunder I'd better run, you'd better take cover Yes folks, it works! We have an absolute winner! So thanks for everyone who told me about that cap.

**Dave Jones:** Yeah, thanks a lot. Actually, you robbed me of my chance to solve it myself this morning. I was sleeping like, you know, thinking last night in my sleep, as you do, that oh, I'm going to tackle that board again, and oh, you robbed me of my win!

**Dave Jones:** Thanks a lot! I'm a man, I'm trying to take me Because I come from the land of plenty I come from the land I'm under Yeah, yeah, women's glow and men's thunder Can't you hear, can't you hear the thunder I'd better run, you'd better take cover

**Dave Jones:** music music music
