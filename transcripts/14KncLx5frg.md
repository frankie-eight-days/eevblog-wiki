---
video_id: 14KncLx5frg
title: EEVblog #905 - REPAIR: HP85 Vintage Computer
url: https://www.youtube.com/watch?v=14KncLx5frg
source: youtube-asr
timestamps: {"0": 2, "1": 23, "2": 42, "3": 53, "4": 73, "5": 84, "6": 93, "7": 104, "8": 115, "9": 133, "10": 147, "11": 154, "12": 168, "13": 182, "14": 195, "15": 204, "16": 222, "17": 233, "18": 256, "19": 269, "20": 278, "21": 292, "22": 306, "23": 319, "24": 338, "25": 358, "26": 370, "27": 385, "28": 394, "29": 407, "30": 423, "31": 436, "32": 448, "33": 457, "34": 467, "35": 478, "36": 487, "37": 498, "38": 510, "39": 524, "40": 532, "41": 556, "42": 571, "43": 585, "44": 596, "45": 610, "46": 619, "47": 639, "48": 655, "49": 671, "50": 691, "51": 706, "52": 722, "53": 733, "54": 742, "55": 751, "56": 766, "57": 777, "58": 787, "59": 798, "60": 813, "61": 826, "62": 835, "63": 849, "64": 862, "65": 871, "66": 898, "67": 910, "68": 926, "69": 940, "70": 957, "71": 973, "72": 993, "73": 1008, "74": 1019, "75": 1032, "76": 1048, "77": 1063, "78": 1083, "79": 1095, "80": 1115, "81": 1131, "82": 1143, "83": 1150, "84": 1160, "85": 1171, "86": 1183, "87": 1206}
---

**Dave Jones:** Hi, in my previous video I did a teardown of this classic HP 85 and it was very interesting. So, click here if you haven't seen that, but um I put it back together afterwards and I went to power it up and Hmm, not even the power light's coming on.

**Dave Jones:** Zippity doo dah. Oops. So, I'm going to try and troubleshoot this thing. So, bear with me. Um I did do something stupid though. When I reassembled it, I completely forgot to put this ground and earth grounding strap from the chassis here up to the main uh main power supply board up here.

**Dave Jones:** Now, I don't think that's going to matter, but technically I switched it on and it did nothing and then I had a quick look around inside and I noticed that was actually um disconnected.

**Dave Jones:** So, I've reconnected that now and it still does exactly the same thing. So, yeah, I don't know. Let's go through and troubleshoot this puppy. Should be fun anyway. Now, granted this could be as easy as uh me just having left a cable out or bad connection or something like that.

**Dave Jones:** Um so, let's have a squeeze around. I don't know. I Maybe you won't see this video or it'll just go on my second channel. I don't know, but let's start.

**Dave Jones:** First thing I'm going to do is a very quick uh primary transformer test. Make sure I haven't blown the fuse cuz that ground could have caused an overload, a lack of ground, or something.

**Dave Jones:** I don't know. Let's uh check that out. Nope, 54 ohms. That's all right for a transformer primary. So, nothing wrong there. Uh fuse hasn't blown. So, it should be powering up.

**Dave Jones:** Now, I really don't think that leaving off that uh earth strap down in there would have caused any issue. Why? Because this is the power This is the transformer power output here, okay?

**Dave Jones:** And look, it's got an earth wire. It looks like well, it does go down to earth if you actually follow that down. So, that middle thing there, uh what I'm going to do is I'm going to measure between that pin, the middle pin, and the earth strap, which is right down in here, and it is a dead short.

**Dave Jones:** So, it's actually connected on the board. So, it's just an alternate path for the um earth there. So, it was, you know, it didn't make any difference. So, leaving that strap off would not have blown anything.

**Dave Jones:** So, copy that. Okay, so what I'm going to do now is measure the output of the uh transformer secondary to make sure we got our voltage going over here.

**Dave Jones:** It should do um because we're measuring the uh primary. So, I'll go between one of the pins there and there. Bingo, 14 V AC. The other one, it should be like a center tap.

**Dave Jones:** There we go. Yep. That I don't know what the actual value should be, but hey, you know, 15 V AC aside, sounds right to me. The Anyway, what we need to check is that the power supply board here is actually getting power, and it is.

**Dave Jones:** So, that's fine. Next step. Now, at this point, it would be wise to actually have the schematic, and we do have the schematic available, but I'm lazy, and also um you know, really, you shouldn't need it at this point.

**Dave Jones:** I mean, there's some obvious stuff here. Here's one of the main uh filter caps, one of the big blue filter caps on the thing, those big studs down in there.

**Dave Jones:** So, bingo, I can actually get in there and measure that big capacitor stud. Are we getting a voltage on it? Mwah, mwah, mwah, mwah. 0.1 V on a 25-V cap.

**Dave Jones:** There you go. So, that cap there, 25-V DC, has got basically bugger all across it. Not zero, but that could just be some residual charge or something. So, has something gone?

**Dave Jones:** Now, at this point once you realize there's no voltage on that cap, this is where you'd probably get out the schematic or I can take out the whole module and just have a visual check to make sure I don't know, but yeah, it's like I don't know what would have blown on this thing um or how I could have blown anything leaving that earth strap off.

**Dave Jones:** I've already verified that that should not have done anything and nothing went pop, didn't smell anything, no magic smoke escaped. Um so yeah, it's just not powering up. There's something wrong.

**Dave Jones:** There's no voltage across that cap. There damn well should be. Otherwise, what the hell's it there for? Now, we've got the schematic, but hey, we didn't have to go to the schematic at this point.

**Dave Jones:** We still could have uh started, you know, and kept probing around, not just randomly monkey bashing on keys hoping to get Shakespeare um probing around, but you know, we could have um basically uh troubleshoot this thing without the schematic, but we've got it to hand.

**Dave Jones:** So, let's have a look. Now, we've established that we've got our AC on here. By the way, here is Here's the ground and there's that earth strap. Okay, so that shows that's going down to earth and this is going down to circuit common.

**Dave Jones:** You can see the ground or you know, ground, not earth like chassis earth. So, that one's going down to chassis. Um now, the cap we actually measured uh was this one over here, 4,500 microfarads.

**Dave Jones:** Right over here, okay? So, that's the main plus 12-V rail, okay? Um so, we're not getting that out. So, the first thing I'd check as I was going to do it anyway is measure across the other main cap, which is our main output uh filter cap for our full-wave bridge rectifier here.

**Dave Jones:** So, let's just measure that one quickly. Um interestingly, we've got a crowbar circuit there. That's nice. Uh any overvoltage it will uh clamp it uh down. And you know, like if you accidentally plugged in uh you know, had it set to 2 uh 110 V and you plugged in your 240, then the crowbar's going to act and hopefully save the rest of it.

**Dave Jones:** It might blow the ass out of your crowbar, but hey, it'll save the rest. So, um anyway, we got ourselves a crowbar. Uh the uh transformer here is actually not a trans Well, it's being used as an inductor, basically.

**Dave Jones:** It's not like an isolated uh transformer. Anyway, interestingly, I see a fuse in there. So, aha, that's the one of the After we check the voltage across here, I'd be checking the continuity of that fuse.

**Dave Jones:** So, the voltage across that cap, it's way, way down in there. So, you don't want to go have both probes in there cuz you don't want to short accidentally short out.

**Dave Jones:** You would get maybe get the adapters, which have the um insulated, you know, the CAT IV adapters on there that just expose the uh points like that. Um but, I don't need to because we've got that handy uh strap.

**Dave Jones:** So, down there with the earth strap, and in we go. And what do we get? 36.6 V is just fine. So, nothing wrong with our full-wave bridge rectifier. So, to access that fuse now, I had to take out the entire assembly, but hey, it was easy.

**Dave Jones:** Four screws and the entire assembly just uh swings out. Oh, five if you count the uh earth strap there. As And we can still power it up from the AC input cuz it's just AC in here.

**Dave Jones:** We don't have a load on it, of course, but hey, it's good enough. We can at least get in there, access stuff, and power it up without powering up any of the uh high-voltage uh CRT stuff over there, either.

**Dave Jones:** So, nice and safe. And I've mentioned this before, but uh you know, we've got a lot of energy in that huge uh cap up in here. So, you just want to make sure it's drained.

**Dave Jones:** So, this is where your low-impedance uh mode on one of these low-Z ranges can uh really come in handy. Actually, I can just go from the uh earth strap there.

**Dave Jones:** There we go. And uh probe that. There we go. It's already discharged, so no worries. Uh I don't Yeah, it's already gone. They don't have a bleeder resistor on it, but uh yeah, the rest of it just discharged it.

**Dave Jones:** So, there's there's no energy left in that. So, it's safe to go probing around. Not from a high voltage point of view. I mean, 35 V is fine, but just from an energy point of view.

**Dave Jones:** Um and certainly I'm measuring ohms and things like that, which we want to go do. Measure our fuse. We don't want any voltages in there upsetting any of our readings.

**Dave Jones:** It's actually really annoying that there's no component designators on the uh board here. No uh silk screen overlay on the thing. So, it's a bit annoying. So, you can either trace things out or you can go to a component overlay, which is in the service manual.

**Dave Jones:** But, we don't need to do that here cuz we know it's on the uh around the transformer there. There it is. It's like There we go. Near uh Q2 there, but we don't know where Q2 is.

**Dave Jones:** But, uh it's in series like it's near one of the taps of the transformer. Anyway, that's all we need to know. So, if you have a look around here, oh, which one looks like a fuse?

**Dave Jones:** Bingo. That one there. So, let's just uh measure that. Should be zero. Bingo. Got you. Yep. Fuse blown. So, no wonder we're getting nothing on the uh output of that big uh 4500 mic cap we're measuring the main 12-V rail because bingo, a fuse is blown.

**Dave Jones:** But, why is it blowing? Does it have to do with that earth strap which I foolishly left off? I I still don't think so. I can't see a mechanism that would do it because the um it it already still had the connection there.

**Dave Jones:** So, uh via the cable. Instead of the strap. So, I coincidence? I don't know. Is there a short somewhere else on the 12-V rail uh throughout our circuit? Maybe on another board?

**Dave Jones:** Perhaps something like that. So, what we should actually do is although he's just measured some voltage on there before, so it's not going to be a dead short, but just for kicks we'll just measure the resistance across our uh the 12-V rail here.

**Dave Jones:** All right, so let's just measure that cap. Oh, hello. Oh, no. No. No. There we go. No, that was just uh and now you can see the cap charging up.

**Dave Jones:** Watch now cuz the cap's charged up. We swap our probes around. Ha, we get zero in the other direction as well. So, just wait a bit. Wait a bit.

**Dave Jones:** So, we put the probes on backwards and it had some residual charge, so it caused the meter to just display zero. Trap the young players. Um di- different meters will vary uh depending on um how they're you know, the chipset and how they measure ohms and everything else.

**Dave Jones:** So, you not every meter's going to be perform the same when you're forcing a voltage onto here during the uh when you've got the resistance range. Let's take the venerable Fluke 87 for example and let's uh probe this puppy.

**Dave Jones:** 175 176 K. Wow. Wow, it doesn't No, I like the uh EVBlog meter much better. Anyway, if we swap it, what do we get? Uh minus 176 K. There you go.

**Dave Jones:** Like completely Well, I was going to say completely opposite, pun intended. Um so, it doesn't show zero. So, a lot of meters are going to perform differently here. By the way, one thing I am suspecting when I took these uh ribbon cables out, there were two of them in particular.

**Dave Jones:** This one, that uh went is actually the output of the power supply. Um it was mis- it was a bit misaligned on the pins. Um apparently, like those connectors um actually let you put them in at like an offset angle.

**Dave Jones:** And maybe um it either wasn't connected or could have been shorting out uh two pins or something like that. So, that could easily have caused it. So, I I'm going to assume that uh that was the cause of the problem.

**Dave Jones:** I.e. me, idiot me, actually didn't, you know, I just shoved them back in thinking it would like self-align on the edges and all the pins. And um but no, I think they were almost touching.

**Dave Jones:** I didn't actually measure it, but it just looked that way and then boom, it popped out and you know, but yeah, I think that could have been the issue.

**Dave Jones:** That would certainly explain a blown fuse on the power supply as one of these connectors uh which is mainly power coming over here these ribbon cables onto the main board.

**Dave Jones:** So, let's hope that's all it was. Otherwise, it doesn't really make sense. I mean, I was using this uh for quite some time and it worked just fine. So, you know, yeah, I think I did something reassembling.

**Dave Jones:** Now, before you jump in and uh replace that fuse, just do some visual inspection to make sure there's no burnt out uh traces going over to the power connector here, no burnout parts or anything like that.

**Dave Jones:** Give it a bit of a smell to make sure none of the magic smoke has escaped. It's just got that uh 30-year-old electronics uh smell. That's the only thing there.

**Dave Jones:** Um but I wouldn't have expected cuz if I shorted out a power supply on here uh accidentally between two pins, you know, we've got uh that 375-mA uh fuse.

**Dave Jones:** It's not much. It's going to blow fairly quickly on a short. And hopefully, we haven't damaged anything else. That's the theory, anyway. Uh 30-year-old electronic smoke. Look at that.

**Dave Jones:** Just wick that solder out there. Couldn't have been bothered turning on my uh solder pump. There we go. Fresh holes. Now, I know this might look a bit how you're doing, but uh this is all I had.

**Dave Jones:** I couldn't find my axial uh fuses, and I think I've only got 1 amp uh types anyway. So, I just uh bodged in a M205 uh fuse holder like this.

**Dave Jones:** That'll get me out of trouble until I get uh a proper axial uh replacement one. Like that, and uh then I'll whack it back in. But, this should get me up and running nice and safely.

**Dave Jones:** So, let's power this baby up outside of the uh unit, and um see what we get, shall we? Bingo, 12 V. Winner winner, chicken dinner. All right, so let's measure some other rails.

**Dave Jones:** Uh this'll do nicely for our negative. Um that's our plus 12, which we uh measured before. The good thing is they don't have silk screen, but they do have it etched in the copper.

**Dave Jones:** This should be plus 5. Yep, 5.12. That's fine and dandy. That's within the usual uh 5% uh tolerance, i.e. 4.75 to 5.25. And usually on high current or high power 5 V uh computers like, you know, old-school stuff like this, which chew a bit of uh current on the 5 V rail for all the uh digital logic, then you probably want to set it like slightly to the high side.

**Dave Jones:** You don't want to set, you know, trim it to precisely 5 V thinking you're really smart trimming it right like that, and then getting drop over the cables and the connectors and the traces and everything else out to the uh large boards and things like that.

**Dave Jones:** So, it's common to actually set that uh reasonably high. This is plus 6. Yep, 6.17. Um I think that's it. I'm happy with that. Winner. Now, here's where I think the problem came about.

**Dave Jones:** This allows me Well, you see, it allows me to put them at an angle that is not lined up. Hopefully, you can see that. That is not lined up with those.

**Dave Jones:** So, I've got to be very careful about putting that back in and lined up perfectly with the pins. So, I've got to do that for all four of these plus the other ones um down the bottom going to the uh CRT display, as well.

**Dave Jones:** All right. So, let's try this again. Here we go. Hopefully, I've got it uh Okay. Uh yes, I've put the earth strap back there, but I Like I said, I That should not matter uh cuz it's already connected through the earth of that one.

**Dave Jones:** So, anyway, let's go. Hey! Power LED. Power LED. I'm liking the power LED. That means we've got 5 V on our rail. Bingo! Error 23 self-test. OH, WOW. WOW, something else has screwed up.

**Dave Jones:** But, the processor's working. So, we're getting our 5 V on our CRT's working. So, that's interesting. What self-test has failed? Hmm. Murphy. Heh. That wasn't That fuse just alone just wasn't going to fix it.

**Dave Jones:** Nah, it was never going to be my day. Now, the interesting thing is uh look, I have not got the memory expansion pack plugged in. So, this one is actually uh 16K of RAM built onto the main board.

**Dave Jones:** It's supposed to be 8K, but uh maybe it was, you know, an Maybe it was an optional extra at the factory. Maybe it's an aftermarket update. Um just plug in extra chips I higher capacity chips.

**Dave Jones:** I don't know, but 16K on board. That's why we're getting uh 32K total with the extra 16K pack, but look, everything's working just fine. I mean, I I can run programs and and stuff, and it's What is error 23?

**Dave Jones:** Let's go to the manual. Well, the manual doesn't tell me what the self-test error is, but um oh. I'm I'm not having a good day. I forgot to plug in the printer and the tape deck.

**Dave Jones:** Unbelievable. Let's try that again, shall we? You can do it. Yes! Winner! List. Woohoo! And we can actually run the self-test. It's got a test key up here. It's great.

**Dave Jones:** And that would have got There's the CRT. So, it's scrolling all the memory, so that was Oh. Oh. Oh. We don't have any paper in there. Nope. But, yep.

**Dave Jones:** It passed the self-test. No worries. Try that again with some paper this time. Scroll that CRT memory. Love it. Boom! There we go. Winner. And I might have to do another video maybe trying to fix this tape drive cuz it doesn't seem to work.

**Dave Jones:** I just ran the catalog command cat, and you know, it's supposed to read from the tape if there's anything on it. You know, presumably tapes are very reliable, so they had something on there.

**Dave Jones:** But, yeah, it just it doesn't stop when it rewinds or anything. It just doesn't seem to Yeah, there's something could be something physical wrong with the capstan in there.

**Dave Jones:** Not, you know, pinching correctly or something like that. I don't know what the deal is, but the motor's whirring and light's going, but it's not doing much else. So, there you go.

**Dave Jones:** I hope you enjoyed that little repair video. It was kind of It was good that I screwed that up, actually. It We got a nice little repair out of this.

**Dave Jones:** As simple as it was, a fuse, but hey, step-by-step, tracking it down, eventually found it, and then we forgot to plug the cables back in. Dole, double dole. And yeah, I'm a twit.

**Dave Jones:** But anyway, we fixed it. If you like that, please give it a big thumbs up. And as always, um links to other videos are here, and subscribe, and you know, all that sort of stuff, and forum, and yeah.

**Dave Jones:** Whatever. Catch you next time. Hi. Welcome to Teardown Tuesday. Yes, we're going back to the future of computer technology today, right back to 1977, where it all began. One of the pioneering computers of the modern era, and one of the biggest-selling computers that a lot of people forget about.

**Dave Jones:** Everyone remembers the Apple II, and computers like that, but well, this thing was actually the biggest-selling computer of its day.
