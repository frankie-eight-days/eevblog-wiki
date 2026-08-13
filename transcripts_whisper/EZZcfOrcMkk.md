---
video_id: EZZcfOrcMkk
title: EEVblog #727 - How To Kill An Opamp
url: https://www.youtube.com/watch?v=EZZcfOrcMkk
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 37, "3": 57, "4": 77, "5": 97, "6": 117, "7": 133, "8": 149, "9": 169, "10": 189, "11": 205, "12": 225, "13": 249, "14": 293, "15": 309, "16": 329, "17": 349, "18": 365, "19": 381}
---

**Dave Jones:** Hi. You ever have one of those bad days when you just do something incredibly face-palm stupid? Well, yeah, that just happened to me today. I was just checking the calibration of my little microcurrent test jig here. This is the 1 amp one. I've got several of these for

**Dave Jones:** different current ranges and things. And this is the production test jig that goes along and, you know, bang, bang, bang, bang. You put it in and check the microcurrents in production. I sent these to my assembly house. I don't do them here. So they're the ones who operate this.

**Dave Jones:** And I've got a precision current source that I've built. And if you want to I don't know, have I shown inside this before? It's not pretty. There you go. It's not pretty, but there is a small board down in there which is pretty schmick, actually.

**Dave Jones:** It generates a really precision 1 amp current. So it may not look like much, but anyway, this generates the current reference for the microcurrent calibration. And I was just checking the calibration of this where I actually feed in 1 volt into the input into this thing.

**Dave Jones:** So it simulates the 1 volt output from the microcurrent using my voltage reference here. And you'll notice that it's reasonably close to... I've just switched this thing on. So let me plug it in and watch what happens. Oh, am I doing it again?

**Dave Jones:** No. Look! It's dropped down. There you go. Why is it dropped down? From the nominal 1 volt? Well, obviously the output of this voltage reference is being loaded. Why? Because I did something incredibly dumb! I hooked it up and I had my voltage reference set to 10

**Dave Jones:** volts. D'oh! And this thing is powered from, as you can see, two coin cell batteries. So there's like a maximum of a 6 volt range. Yeah, a 6 volt power supply on this thing. In fact it's dropped a little bit down below that

**Dave Jones:** on the rail itself. And of course, d'oh! If you feed 10 volts into the input, in this case the input terminals here are connected directly to an op-amp on here. And if you feed 10 volts in, when you've got a 6 volt rail

**Dave Jones:** whaaa! And well, yeah, something's loading it down. So I think I've killed my input op-amp here. And that's, you know, my dumb. I didn't ruggedize this thing like I would have normally did. I did it in a real hurry. And I didn't put any input

**Dave Jones:** series protection resistors or anything, any input protection at all, any sort of clamping, because it wasn't going to be ever used in a scenario where that was likely to be a problem. Except when it gets back in my hands and I completely screw my own little design by not checking before

**Dave Jones:** I plug the damn voltage reference in. Ah! Unbelievable. So yeah, I think there's something seriously wrong with that chip, and it's loading down my reference. Let's go measure it. And by the way, if you haven't seen this, it's just got a power LED in here and an

**Dave Jones:** InSpec LED, and that's basically it. It tells the production operator, go, no-go, whether or not a microcurrent passes the test. And well, let's, this is the voltage input here which takes the output from the microcurrent, and when you feed in the nominal 1 amps into the microcurrent, this is just a feed-through

**Dave Jones:** like that. So this just feeds the current straight through like that. So no big deal. Obviously 60 ohms, there you go, that is why it's loading down my voltage reference. I've definitely well and truly killed it. This is supposed to go just directly to the input of a high-precision

**Dave Jones:** CMOS op-amp. So it should effectively be infinite input impedance basically. Nope, it's shorted out. So, yeah. Oops. And it's going to be that puppy there, the OPA2376. So it takes the input directly from there, and it's a window comparator, so it drives the LED there from a

**Dave Jones:** voltage reference on the board. So you know, it's a fairly simple device, but yeah, I had no input protection or anything like that. Suck out the chip, and well, I hope I've got another one. I usually buy more than what I need. You know, if I was building one of these

**Dave Jones:** I wouldn't just order one op-amp. You know, because I would have got it from DGK or maybe someone like that. I would have ordered at least a couple of spares. Gonski. And a little bit of clean-up there. And she'll be right, ready for a new one.

**Dave Jones:** Okay, so make sure dumbass me's got it around the right way. I think I have. I've already tacked down one corner pin. And in this case it was unlikely to have taken out anything else on the supply rail. And I checked the voltage reference on here,

**Dave Jones:** it seems to be working just fine. And the other op-amp on here, its functionality is just fine. So there's only basically three main devices on the rail here. And sure enough, ta-da! I'm not sure if you can see that, but anyway, a green light, it's in spec, and I can now

**Dave Jones:** go out of spec and make it jump in and out of spec. And now I can go in and tweak it. It takes actually quite some time to actually recheck and recalibrate this thing. But there you go, it's fixed. So dumbass me. What's the moral of the story?

**Dave Jones:** Why did I do this video? I don't know. I just wanted to share my screw-up with you. So before you plug stuff in, thou shall check voltages. Catch you next time.
