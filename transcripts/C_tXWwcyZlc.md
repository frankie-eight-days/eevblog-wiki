---
video_id: C_tXWwcyZlc
title: Dumpster HP3488A Switch Teardown + Silverbrook STORY
url: https://www.youtube.com/watch?v=C_tXWwcyZlc
source: youtube-asr
timestamps: {"0": 1, "1": 10, "2": 25, "3": 38, "4": 56, "5": 79, "6": 89, "7": 99, "8": 119, "9": 131, "10": 143, "11": 162, "12": 174, "13": 190, "14": 201, "15": 217, "16": 229, "17": 248, "18": 259, "19": 272, "20": 286, "21": 295, "22": 307, "23": 322, "24": 338, "25": 353, "26": 373, "27": 382, "28": 393, "29": 406, "30": 418, "31": 437, "32": 449, "33": 463, "34": 472, "35": 484, "36": 494, "37": 509, "38": 517, "39": 529, "40": 549, "41": 559, "42": 570, "43": 584, "44": 597, "45": 606, "46": 617, "47": 631, "48": 643, "49": 656, "50": 671, "51": 684, "52": 695, "53": 708, "54": 717, "55": 738, "56": 749, "57": 763, "58": 774, "59": 787, "60": 799, "61": 813, "62": 826, "63": 838, "64": 858, "65": 867, "66": 881, "67": 889, "68": 909, "69": 928, "70": 952, "71": 965, "72": 979}
---

**Dave Jones:** Hi, it's mystery dumpster teardown time again and this one comes from the archives in the bunker. I actually got two of these down here. What is it? It's Hewlett Packard.

**Dave Jones:** None of that Agilent or Keysight rubbish. 3488A switch control unit. Yes, it does look a lot like it. Basically uses the same case as a lot of the you know, the 34 50 What is it?

**Dave Jones:** Not the 3458, the other variant that I've done a video on. Anyway, they're multimeters. They're old school multimeters and stuff like that. But this is basically a relay switching / control unit.

**Dave Jones:** So the idea is that you like have these in large complex test systems or you know, some other control system that you need to basically switch things either switch channels for measurement into multimeters and things like that or you need to you know, control various stuff.

**Dave Jones:** And so it'll have like relay cards. It'll have like you know, basically multiplexer cards and things like that and you can plug in different options into these things and you can see that this one you can have like looks like well, this one is the base unit down here which has the GPIB interface which is how it's all controlled.

**Dave Jones:** None of that serial port rubbish. All old school HPIB and looks like it has five different slots and these these ones are marked marked marked two and three and unit one.

**Dave Jones:** Don't know what the Yeah, it's it's the same is it? I assume yeah. A mux interface card but you can get like various you know, different cards for it.

**Dave Jones:** I won't go through it. Anyway, this sticker here is interesting. I got a story about this. Property of Silverbrook Research Proprietary Limited. Now, I uh, Silverbrook is a legendary infamous company here in Australia.

**Dave Jones:** It's a, like, a research uh, kind of a research think tanky kind of thing run by a guy named Silverbrook, or was run by a guy named Kia Silverbrook.

**Dave Jones:** And I don't know if he still is, but technically he was, um, at one point, uh, the world's largest, or equal, yeah, I think he surpassed the world's largest holder of patents, right?

**Dave Jones:** So, this guy was obsessed with getting patents. So, this think, uh, tank, they would have actually an army of in-house patent attorneys who would uh, like, uh, take one of Kia's, you know, ideas and then patent, like, literally a hundred different ways to implement it.

**Dave Jones:** Um, and they would just churning out. And I believe he got, like, thousands of patents to his name. Absolutely crazy. He was obsessed with passing, you know, Edison and, you know, all those sorts of things.

**Dave Jones:** Anyway, uh, they their main technology was actually this high-speed, uh, not kind of inkjet. I can't remember, uh, mem- memjet. Oh, anyway, it was some sort of printing, high-speed printing, uh, you know, technology.

**Dave Jones:** It was, like, this printing head, and they just patented, like, a thousand different ways to do it or something. And, uh, you know, it they had like prototypes, and they were actually producing stuff in-house and things like that.

**Dave Jones:** And, um, but it never really went anywhere. I think it got bought out by somebody in the end who, in the end, uh, decided that, "No, we own all the patents." I think that maybe there was some lawsuit suit or legal, uh, quibbles over who owns the patents, but I believe, uh, Kia eventually lost all his patents.

**Dave Jones:** So, I think it was, yeah, signed over to the investors or something like that. And the company's like gone. Uh, I don't know if they're gone bust now, but they might have been absorbed into something else.

**Dave Jones:** And they never actually produce this miracle 3D uh printing technology, high-speed printing technology. I can't remember the exact details, but anyway, I went for a job there once. Um this was a long time ago, probably 15 years ago or something now because I've been doing the EV blog like for full-time for a decade now and doing it for 12 years.

**Dave Jones:** It was before the blog, before I went to Altium, I believe Yeah. Yeah, it was before I went to Altium. Anyway, so it was at least 4 years Yeah, so it's got to be at least 15 years ago now.

**Dave Jones:** Uh went for a job interview at Silverbrook Research, and they were like really uh you know, they were they were top top guys there working on right like really you know, really innovative uh type stuff.

**Dave Jones:** And I can't remember what the job was for. It was, you know, design engineer, you know, doing something or other. And uh and the So I went in for a couple of interviews with the technical uh team, and they like really liked me.

**Dave Jones:** They really wanted me, and you know, it was a it was a done thing, but I had to pass a third interview hurdle, which was uh to meet with uh Kia Silverbrook's right-hand man.

**Dave Jones:** So everyone who got hired at this company like uh they famously like hired like every PhD graduate and, you know, so anyone like you know, master's and PhD like minimum.

**Dave Jones:** So I I don't have a master's or PhD, but you know, I was just being hired as a general design engineer, but they sucked up all of the like uh you know, highly qualified researchers in the country in the country in various uh fields.

**Dave Jones:** And anyway, so everyone apparently who was hired at the company had to be vetted by Kia's right-hand man. So anyway, I went in for the cuz the company, by the way, was I believe like famously a like a a flat uh tier horizontal tier company.

**Dave Jones:** There was Kia Silverbrook and everyone else. And it was like it sounds like Altium, you know, all all all decisions go you know, the head honcho. Anyway, um so yeah, I was I was interviewed by him and he was very strange Don't know.

**Dave Jones:** Can't remember calling names or anything, but anyway, very strange individual. So so the technical guys are in the meeting as well and they're asking me some technical questions and this guy, you know, he's looking at my resume and you know, like what's all this stuff about publishing things?

**Dave Jones:** And I go, "Oh, yeah, yeah, you know, I've published like cuz everyone likes it when you publish stuff and anyway, so he uh went what's this deal with publishing?

**Dave Jones:** And I went, you know, and and he kind of like shook his head like this is bad. This is not good. You you publish things cuz they were Remember, this was a super secretive company.

**Dave Jones:** Apparently, they uh like hid how much like milk and consumables they buy lest anyone try and figure their competitors, whoever they were, try to figure out how much funding they have based on the head count and stuff like that.

**Dave Jones:** So everything was like super secret. How many people they hired, all that sort of stuff was like super secret. They they had hundreds of people working for them. Um but anyway, so they were really paranoid about secrecy.

**Dave Jones:** So they he saw that I had published stuff and he's like shaking his head and I'm kind of going, "Okay, is that a problem?" And he's, you know, nodding and going, "Uh yeah." And I go, "Well, what's, you know, obviously, I wouldn't publish about stuff about what the company's doing and things like that." And he's Sorry about the static shot here.

**Dave Jones:** This is boring, but anyway, telling a story. And he uh like and and it eventually got to a point where we started like I started going, "Well, what would be acceptable?

**Dave Jones:** Uh you know, for me to like do I have to stop publishing things?" And he's he's going like he's nodding and I'm going, "Well, what if I wrote a book about gardening or a a or if I started a garden in blog, would that be a problem?

**Dave Jones:** And you know, I just like picked it like it's totally non-random thing. I'm not a gardener. Just picked a totally, you know, thing out of left field and he went, yep, that'd be a problem.

**Dave Jones:** And I went, why? It's And he just wouldn't answer. Like really strange. Um and so I'm like at this point going, yeah, this guy I don't think I want to work for this company.

**Dave Jones:** Um so yeah, and and the technical people, you could see that like they're in the meeting as well and they're just like like their heads are going low and they're face palming there.

**Dave Jones:** And so my I could read their minds. It's like, ah, not this again. Kind of thing. Anyway, anyway, so I didn't get the job. I got I got uh [ __ ] canned by the um yeah, Kia Silverbrook's right-hand man.

**Dave Jones:** So even though all the technical team wanted me. So there you go. I almost got into Silverbrook Research. And I know many people have almost gotten into Silverbrook Research for similar reasons.

**Dave Jones:** Anyway, sorry about that. Um but yeah, anyway, calibration certificate quite old. Let's have a look inside this thing, shall we? Wow, these have some very sexy long screws in them.

**Dave Jones:** Check this out. Yes, I'm using this bad boy because well, look at the size of these just for kicks. Anyway, oh, that one's loosey-goosey. Boss, someone somebody forgot to tighten that one up.

**Dave Jones:** Cuz there are no screws on the side. Well, there we have it. It's a very modular. There's a huge power brick down here. Look at that thing. Um that's like, you know, an off-the-shelf power brick.

**Dave Jones:** How do we Oh, yeah. There we go. That's the rear interface contacts. So it's just a card edge thing. And they're all There's like a There's just like screw probably just like screw terminal blocks in there.

**Dave Jones:** Oh, no. There you go. What are those uh They're not Do you just push them in? Can we just pull those out? Are they Yeah, I'm not sure what the deal is there.

**Dave Jones:** Do you need a special tool to Oh, no, there we go. No, the screw screws in the top there, doll. So, these modules just will slide out like that.

**Dave Jones:** Tada! And they just got shielding plates top and bottom. You can see the relays in there. We'll take a look at those. They're probably like NECs, Fujis, something like that.

**Dave Jones:** Oh, they're just links there. There's not much in there. Yeah. There's uh driver [ __ ] down there. You can see those. We'll whip the top off in a minute.

**Dave Jones:** Oh, there we go. Look at that. None of that solder mask rubbish. Wow, is that like just Yeah, that's just like gold plate without solder mask. Ooh, sexy. Wow, I'm going to get a nice photo of that.

**Dave Jones:** That's beautiful. Ah, and they've done the same over here for the LCD as well. Couple of chip-on-board things with just the gold plate um traces. Gold flash. Absolutely brilliant.

**Dave Jones:** It's probably thick as, too. And uh Oh, made in Morocco. Hi to all my Moroccan viewers. ST. I didn't know ST made power bricks, but there you go. There you go.

**Dave Jones:** It's got a couple of control lines and looks like a plus S, minus S, VO, whatever. Some discrete stuff over there. And there's our main switch. It's actually just runs cable from the front.

**Dave Jones:** And then it's, you know, it's all over the shop. The mains connector is actually on the back of this module here, like this. And then that runs the cable along the side to the power switch over here.

**Dave Jones:** And then it's got to run all the way along here, over here, all the way over to the power transformer on this side, it's like uh it's No, the layout's just all wrong.

**Dave Jones:** Um nope. Nope. Nope. Nope. Anyway, got a big-ass reservoir cap and just a probably a 7805 or something down there. That's a uh bridge rectifier. Go straight into the mains cap and that's all she wrote.

**Dave Jones:** So, basic full wave rectifier coming from, you know, it doesn't need much. It's just got to drive the relays and things like that. Not And the processor, of course.

**Dave Jones:** Not a huge uh requirement. Just the other side of that backplane there. Look at this, USA made. USA. USA. Anyone has any clue what those characters are under the HP-IB connector there, please leave it in the comments cuz what the And you have to actually unscrew the top cover.

**Dave Jones:** This board doesn't actually come out as a module. And all the 6800 or 6809, sorry, 6809 fanboys go wild. There you go. Um and what else have we got?

**Dave Jones:** That's our GPIB in it. That'd be our GPIB chip, would it? Yep. And the other 6800 support chips, of course. And uh what have we got? Some memory down there.

**Dave Jones:** Just some Yep, interface stuff, glue logic. We've got a ROM. And, you know, not a huge amount more. It's just a processor. That's it. And then there's a mains input up there.

**Dave Jones:** I've got a uh input filter, of course. But it's about all she wrote. Looks like we have a Pozi drive fanboy at HP. Just Phillips, please. And there's the relay board.

**Dave Jones:** Well, I was wrong on the relay brand, wasn't I? Um and Aeromat uh relay. Yeah, like it rings a bell, but I like I'm a Japanese, of course. Made in Japan.

**Dave Jones:** All the best stuff's made in Japan. Um except, of course, USA. USA. USA. Um so, yeah, like we've just got a 74 interface, uh you know, latch logic. So, it's just like latching on a bus and stuff like that.

**Dave Jones:** As I said, driver transistors up the top and just some links for setting various configurations of the output and it's just boring. There's the wave indicator, goes in this direction.

**Dave Jones:** They couldn't afford to put the extra bit on there to show that it's an arrow. So, it's like Come on. Anyway, and and look, they even went we need a label here, but they didn't bother putting one.

**Dave Jones:** So, that's all she wrote. Um you know, this is what you expect. It's like a 6809 processor driving a parallel backplane bus which then latches into you know, the various five-channel modules and address for whatever, you know, cards you want to put into it and that's it.

**Dave Jones:** It's just a mux. Like, but I haven't actually looked at the configuration of these. Is this like a Can you like switch onto a common bus and things like that?

**Dave Jones:** Let's actually take it out. Aha. Common, yeah, look. So, there's some common there. So, it'd depend on the mux module, of course. You might have different configurations. One might be, okay, you switch different inputs.

**Dave Jones:** This is what I'm used to in test engineering, for example, is to have like a common bus and then you switch different things into it and then you go off the common bus.

**Dave Jones:** Well, you can't go into it cuz this doesn't do any measurement or anything. It's purely just relay switching module. Anyway, the common bus would then go out onto some pins and then that common bus would then go into your, you know, your LCR meter or your voltmeter or whatever instrument that you're measuring your stuff with.

**Dave Jones:** So, there you have it. Just a brief teardown of the HP 3488A switch control unit. Think of it as a multiplexer, whatever. I don't know about the different cards, but I'd be absolutely stunned if uh well, Keysight these days don't make a direct software equivalent to this thing, you know, complete command equivalent uh to this thing.

**Dave Jones:** It wouldn't be in, of course, the old school HP uh packaging like this. Might be in the Of course, it'll be in more modern uh you know, Keysight form factor, but I can guarantee you it'll be fully backward compatible cuz there's countless systems out there that uh you know, are still running 20, 30 years later and they need to keep these things going and they don't want to rewrite the

**Dave Jones:** software. It's all still there and they want to replace the unit and they have to replace it with a software compatible unit. That's why the Keysight's latest multimeters, of course, all backward com- software backward compatible, command backward compatible with all their old multimeters.

**Dave Jones:** That was one of their like really key goals and so all their gear would still be software backward compatible with this, I'm sure. Anyway, that's it. Um yeah, it's a box with a processor and a bunch of relays in it.

**Dave Jones:** Catch you next time. Oh, 14-segment LCD, look at that. Oh, thing of beauty. Joy forever.
