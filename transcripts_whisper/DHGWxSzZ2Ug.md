---
video_id: DHGWxSzZ2Ug
title: EEVblog #357 - USB Supply Power-up Testing
url: https://www.youtube.com/watch?v=DHGWxSzZ2Ug
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 37, "3": 57, "4": 77, "5": 97, "6": 117, "7": 145, "8": 161, "9": 181, "10": 201, "11": 221, "12": 241, "13": 265, "14": 289, "15": 309, "16": 337, "17": 357, "18": 373, "19": 393, "20": 413, "21": 443, "22": 467, "23": 487, "24": 511, "25": 535, "26": 551, "27": 575, "28": 595, "29": 611, "30": 635, "31": 655, "32": 683, "33": 707, "34": 739, "35": 759, "36": 787, "37": 803, "38": 819, "39": 839, "40": 863, "41": 883, "42": 899, "43": 919, "44": 935, "45": 951, "46": 963}
---

**Dave Jones:** Hi, another video in the USB power supply series. I rushed this prototype together for the electronics show, hoping to get it up and running, and I've built the thing, and I'm about to power it up. So I thought we'd go through some power-up checks and see

**Dave Jones:** what we get here. And, wah! I noticed my first fail, of course. Murphy's going to get me every freaking time on this thing. My LCD is supposed to mount on the top like this, and of course it does, but I'm not going to use a connector.

**Dave Jones:** It's going to be the final one, will be soldered directly on to the pin header there, and it sits on there just fine and dandy, but, and it's like it just clears, you know, or sits flush with the DC to DC converter there, but

**Dave Jones:** the whole idea is that I won't be using that socket connector, and this LCD is actually going to sit a little bit lower. And unfortunately, the damn thing hits that DC to DC converter. Wah! And I checked that on the CAD drawing, and

**Dave Jones:** sure enough, my outlines were slightly overhanging there. One was on the mechanical layer, which I had turned off when I was mostly laying out the board, and I just didn't notice. I completely missed it. So yeah, fail. Eh, trap for young players. There you go, that's what happens when you're rushing, you don't

**Dave Jones:** check things properly, or you don't do your proper 3D modeling and then your 3D design rule checking. Ah, for a prototype like this, no need to do that. But there you go, I came a gutser. That's the first Murphy's mistake. The second one then, of course, is, you'll notice that there's no footprint.

**Dave Jones:** There's no chip down on that footprint down in there. That is supposed to be the FT230XS USB to UART converter chip. But unfortunately, it's not available anywhere, even directly from their website until like October or something. Man, I swear that they had stock when I designed

**Dave Jones:** this thing into the circuit, and no, I've come a gutser. So I couldn't get that. I couldn't find stock of it anywhere, really. So yeah, I'm screwed. Anyway, it's not a showstopper, it just means I won't be able to do the serial stuff.

**Dave Jones:** Or I can use bridging another chip if I have to to get it up and running. No big deal really, but yeah. Anyway, I'm sure there's bound to be more errors. So let's get to it. And the first thing I'm going to do is power it from my bench power supply

**Dave Jones:** here, set the current limit, yeah, 130 milliamps, that'll do, to 5 volts, and we'll hook this thing up and see how much current it draws. And that will protect the circuit if something goes horribly wrong. So let's do it. And you'll notice of course I haven't

**Dave Jones:** hooked up a battery yet, I just want to make sure that it all powers up fine and dandy before I connect the battery up. So I'm going to just connect my power supply briefly across here and see what I read. About 60-odd milliamps on the supply there, you can't see that, it's not on

**Dave Jones:** video, but 60 milliamps, that sounds about right. So I'm happy we can power this thing from a regular USB port now, no problems. And hey, bingo, the charge LED has come on! I believe that is correct for no battery connected, so anyway, that's good, let's measure some voltages.

**Dave Jones:** First up I'm going to check the voltage out from the DC to DC converter on the other side of the isolation, and it should be around about, there it is, about 5.5 volts. Because there's no load, effectively, you know, the circuit's drawing very little, so I'm pretty darn

**Dave Jones:** happy with that. 5.5 volts, and where's our DC, our 2.5 volt voltage regulator? Down here? Oh, wrong side of the cap. Should be 2.5 volts. And it is! So our voltage regulator is working just fine. So we don't have any shorts on the board at all,

**Dave Jones:** so nothing grossly wrong there, like loading down our power supply. Happy with that, that's always the first step. Is something shorted out? Nope. And next up we want to measure the charge current of the battery. I want to check the battery charging circuitry, which is around there,

**Dave Jones:** so let's measure, first of all, measure the battery voltage. Existing battery, I've just got a, like a small 4.2 volt charging lithium ion. Sorry, lithium polymer cell here, and it's 3.81 volts. So there's already some charge in that, so when we hook up that battery and plug in

**Dave Jones:** the power, it probably won't go into the constant current charging mode, it might jump perhaps directly into the constant voltage charging mode. And we'll be able to see that, the voltage on the battery, whether or not it's spot-on 4.2 volts, because this is like a plus-minus

**Dave Jones:** 5%, 0.5% or 0.75% chip, or thereabouts, 4.2, or whether it's lower than that. So if it's lower than 4.2 it means it's in constant current charging mode, and if it's 4.2 it means it's switched over into constant voltage charging mode, and then we expect the current to drop off.

**Dave Jones:** And I've done a tutorial on this. I'll have to link it in, actually, so click here and you can see my lithium ion charging tutorial if you haven't seen that. So let's give this a go. I'll hook my meter up to milliamps. Ah, it's beeping at me, go away stupid

**Dave Jones:** default AC current. Yeah, blow it out your bum. Alright, now, let's measure the current in this thing. So yeah, let's hook up the battery. Here we go, we shouldn't have to disconnect, we'll just leave it, we'll just hot-connect the battery on there and what do we get?

**Dave Jones:** Bang! 120 milliamps and dropping. Beautiful. Pretty happy with that. It looks like, because it's dropping, it's not a constant current. I believe it is in constant voltage charge mode, which is kind of what I expected. So I'd expect to measure the voltage on there at precisely 4.2 volts.

**Dave Jones:** Alright, so I've left this meter here connected up measuring the battery current there, and it's just dropped below 100 milliamps and it is dropping. So I'd expect the battery voltage if I actually measure it, to be ta-da! 4.2 volts, spot on. So it's definitely switched over from constant current

**Dave Jones:** charging mode into constant voltage charging mode. And basically once this current gets low enough to the lower cut-out threshold programmed into the microchip charger chip there, then it will actually cut off. And that will be the end of charge and that LED should turn off.

**Dave Jones:** But that could take, I don't know, hours. So yeah, not going to wait for that, but that seems to be working a treat. Alright, next up what I'm going to do is disconnect the USB and we should, it should stay off, it should stay switched off

**Dave Jones:** until we press the on button to switch it off. So hey, hang on. Hello? Hello? We've got 16 milliamps, that should be off. Let me disconnect the battery. Okay, so we're going to connect the battery and... no! Wah! Uh-oh! That should definitely be

**Dave Jones:** off! Let's have a look at the circuit. Now here's the charging part of the circuit, and here's the battery. And Q1 there should be switched off by R7, it should be held off. But it looks like it's somehow conducting, so it's switched on and it's conducting current out there.

**Dave Jones:** And it can't be conducting back into the DC to DC converter and the chip itself, because that diode there, D4 is it, is going to be reverse bias. So really, so that current draw is coming from the rest of the circuit somehow, but there's something

**Dave Jones:** going on in here which has switched that transistor on. Q1 there is on, almost certainly, because there's nowhere else the current can flow unless there's something wrong with the charger chip here, because it's supposed to have, and when you remove the input power, it's supposed to have an

**Dave Jones:** off-state leakage current of, you know, like a microamp or half a microamp or something tiny like that. So unless that chip's faulty, this transistor must be turned on, or there could be a short on the board causing something, so let's measure a few voltages.

**Dave Jones:** Okay, let's measure the output of D6, which is actually the power rail, and see if, there it is, yeah, 3.42 volts, and on the other side of it, 3.7, yep. So that transistor is definitely switched on, because then it's feeding the voltage into that diode D6, and of

**Dave Jones:** course it's dropping, it's a Schottky, you know, so it's dropping about 0.3 volts or thereabouts, and so that bugger of a transistor is switched on. Why? Well I had a quick look under the microscope for some shorts and stuff, it all looked fine, you know, unsoldered joints or anything like that.

**Dave Jones:** No, you know, incorrect component type, it all just seemed fine, so let's measure the gate of that transistor, Q1, well, MOSFET. Where is it? It's that one there. 0.6 volts. That's bizarre, that should drop to, hang on, this is where I need my third hand,

**Dave Jones:** have to hold my tongue at the right angle, push the button, should drop down to 0. It does, there you go. So why is it at 0.6 odd volts? And, oh, hang on, I know, I'm getting a very bad feeling, 0.6 volts is probably not a coincidence, it's a diode

**Dave Jones:** drop of a bloody NPN transistor! Hang on, where's the circuit? And what do we have in our circuit here? There it is, a 2N3904. We're getting one diode drop from there to ground. And I have a horrible feeling that I've seen this before, I reckon this, because I've done

**Dave Jones:** it before, I've made this stupid mistake before, I reckon the footprint of that 2N3904 transistor might be back to front. Because I thought, oh, I'll go through as a final step and check all the transistor footprints, but I didn't, I was rushed for time, I wanted to get my board out.

**Dave Jones:** I reckon the son of a bitch is back to front! Check the data sheet. And there you go! What a mongrel, that was an easy fix though! Absolute classic mistake! I've done it many times before and I'm sure I'll continue to do it, and

**Dave Jones:** I've said it before and I'll say it again, one of the classic rules of electronic design is never assume anything. Never assume your footprint's correct, never assume something's going to work, always double-check it. And I was in a hurry, I didn't do it,

**Dave Jones:** and yep, I got caught out. Ah, happens every time. I think everyone, sooner or later, in the industry is going to make that same mistake. You're going to get a footprint back to front, and here it is! I've hooked it up, and we're getting, well, let's go

**Dave Jones:** down to microamps, and there you go. It's like not even, you know, I could get out the microcurrent of course, but I'm not characterizing the performance of this thing. There you go! 0.15 microamps reverse leakage from the battery. And if I press the button, let's

**Dave Jones:** go back to milliamps there, and if we press the button, here we go, should switch on. There we go, 15 milliamps, and it should switch off when I release the button. And sure enough, it does! Not a problem whatsoever. It's working fine because it's not latching on, because there's no software in the microcontroller to

**Dave Jones:** latch on the power. But that's working like a treat! Ah, beautiful. Man, I've now got to flip all the other resistors as well. What a pain. And it was pretty easy, all I had to do here was rotate the device around like that, so normally this pin

**Dave Jones:** would be up here of course, because these are the two bottom pads on the footprint, and that's the top pad there on the SOT23, I just rotated it around, and bingo! Problem fixed. And depending on how you swap the pins, there's many ways to do it, and some

**Dave Jones:** transistors can have different pin-outs depending on the manufacturer and the type, so just be careful, it's very easy to do. Depending on what you, how you goof up the footprint, you can either rotate it like that or you flip it upside down, you have to bend the pins down and then do it, or rotate,

**Dave Jones:** or a combination of both. So there you go! Pain in the butt, but easy fix in the end. And I'm sure I'll find other things wrong with the board, it's not a big deal. This was just a rush prototype board, just to get something out

**Dave Jones:** there. I fully expected to have a second revision of this board, and all these things, as long as you go through, find them in the prototype testing, not a problem. You just fix it up in the next rev. Woof! There you go. I don't

**Dave Jones:** think I'll test this any further, because there's not much more to test. I really need some software in this thing. I haven't done the software yet, so I think I'll head on home and start to cut in some code. So I hope you like that,

**Dave Jones:** and if you do, please give it a big thumbs up, and if you want to discuss it, jump on over to the EEVblog forum. Catch you next time. www.eevblog.com
