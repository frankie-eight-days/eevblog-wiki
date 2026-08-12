---
video_id: uHJzhgqhp38
title: EEVblog727 HowToKillAnOpamp 1920x1080
url: https://www.youtube.com/watch?v=uHJzhgqhp38
source: youtube-asr
---

**Dave Jones:** Hi. You ever had one of those bad days when you just do something incredibly face palm stupid? Well, yeah. That just happened to me today. I was um just checking the calibration of my little uh microcurren um uh test jig

**Dave Jones:** here. This is the 1 amp one. I've got several of these for different uh current ranges and things. And this is the production test jig that goes along and you know, bang bang bang bang. you put it in and uh check the microcurrens

**Dave Jones:** in production. Um this I sent these to my assembly house. I don't do them here. So they're the ones who operate this. And I've got a um precision um current source that I've built. And uh yeah, if you want to I don't know. Have I shown

**Dave Jones:** inside this before? It's it's it's not pretty. Um there you go. It's not pretty, but there is a small board uh down in there which um is pretty schmick actually. It generates a really precision 1 amp um current. So, it may

**Dave Jones:** not look like much, but anyway, this generates the uh current reference uh for the microcurrent calibration. And I was just checking the calibration of this where I actually feed in uh one volt into the um input into this thing.

**Dave Jones:** So, it simulates the 1V output from the microcurren um using my voltage reference here. And you'll notice that it's um reasonably close to I've just uh switched this thing on. So, let me plug it in and watch what happens. Oh, am I

**Dave Jones:** doing it again? No. Look, it's dropped down. There you go. Why is it dropped down um from the nominal one? Well, obviously the output of this voltage reference is being loaded. Why? Because I did something incredibly dumb. I

**Dave Jones:** hooked it up and I had my voltage reference set to 10 volts. D. And this thing is powered from um, as you can see, two um, coin cell batteries. So, there's like a maximum of a 6V uh, range

**Dave Jones:** on, you know, a 6volt power supply on this thing. In fact, it's dropped a little bit um down below that on the rail itself. And of course, though, if you feed 10 volts into the input, in this case, the input uh terminals here

**Dave Jones:** are connected directly to an op amp on here. And if you feed 10 volts in when you got a 6V rail and well, yeah, something's loading it down. So, I think I've killed my input op amp here. And that's, you know,

**Dave Jones:** my dumb. I didn't ruggedize this thing, um, like I would have normally did. I did a real hurry. Um, and I didn't put any input uh input series protection resistors or anything, any input protection at all, any sort of clamping

**Dave Jones:** because it wasn't going to be ever used in a scenario where that was likely to be a problem except when it gets back in my hands and I completely screw my own little design by not checking before I

**Dave Jones:** plug the damn voltage reference in. Oh, unbelievable. So yeah, I think um there's something seriously wrong with that chip and it's loading down my reference. Let's go measure it. And by the way, if you haven't um seen this,

**Dave Jones:** it's just got a power lead here and an inspec lead. And that's basically it. It tells the production operator go no go whether or not a microcurren um passes the test. And well, let's this is the voltage input here which takes the um

**Dave Jones:** output from the microcurren. And when you feed in the nominal 1 amps uh into the microcurren, this is just a uh feed through like that. So this just feeds feeds the current straight through like that. So no big deal. Uh

**Dave Jones:** obviously 60 ohms. There you go. That is why it's loading down my voltage reference. I've definitely well and truly killed it. This is supposed to go just directly to the input of a um you know high precision um CMOS op amp. So

**Dave Jones:** it should effectively be you know infinite input impedance basically. And nope it's shorted out. So yeah. Oops.

**Dave Jones:** And it's going to be that puppy there, the OPA 2376. So it takes the input uh directly from there. And um it just it's it's a window comparator. So it uh drives the uh lead there from a voltage reference

**Dave Jones:** on the board. So you know, it's a fairly simple device, but yeah, I had no input protection or anything like that. I'll suck out the chip and well, hope I got another one. I usually buy more than what I need. You know, if I if I was

**Dave Jones:** building one of these, I wouldn't just order one op amp. Um, you know, cuz I would have got it from Digi Key or maybe, you know, someone like that. I would have ordered at least a couple of spares.

**Dave Jones:** Gonsky. And a little bit of clean up there. And she'll be right. Ready for a new one? Okay. So, make sure dumbass me's got it around the right way. I think I have. I've already uh tucked down one corner pin. And in

**Dave Jones:** this case, it was unlikely to have uh taken out anything else on the supply rail. And I checked the voltage uh reference on here. It seems to be working just fine. And the other op amp on here um its functionality is just

**Dave Jones:** fine. So, there's only basically three main uh devices on the rail here. And sure enough, tada. I'm not sure if you can see that, but anyway, a green light. It's um in spec, and I can now go out of

**Dave Jones:** spec and make it jump in and out of spec. And now I can go in and tweak it. It takes actually quite some um time to actually re check and recalibrate this thing, but there you go. It's fixed. So,

**Dave Jones:** dumbass me. What's the moral of the story? Why did I do this video? I don't know. I just wanted to share my screw up with you. So before you plug stuff in, thou shalt check voltages. Catch you next time.
