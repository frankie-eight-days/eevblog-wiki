---
video_id: 0-IebArtT9I
title: EEVblog #557 - Retro Sinclair ZX Spectrum Computer Teardown
url: https://www.youtube.com/watch?v=0-IebArtT9I
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 51, "3": 66, "4": 86, "5": 101, "6": 121, "7": 136, "8": 156, "9": 171, "10": 186, "11": 196, "12": 211, "13": 231, "14": 251, "15": 266, "16": 281, "17": 296, "18": 316, "19": 336, "20": 356, "21": 371, "22": 386, "23": 406, "24": 421, "25": 436, "26": 451, "27": 466, "28": 481, "29": 506, "30": 526, "31": 541, "32": 566, "33": 586}
---

**Dave Jones:** Lucky last, comes from Australia, from Anonymous. Too bad if it got lost, they never would have got it back. Ah, well, so here we go, from Australia, not Austria. Let's have a look. What have we got? Oh, look at this! Look at this!

**Dave Jones:** Ah, Sinclair! Clive Sinclair! Woo-hoo! The Sinclair ZX Spectrum. Brilliant! I'm sure this is bringing back a lot of memories for those vintage computer buffs. So I'm going to save this for a teardown Tuesday. It will be another vintage teardown, but it's got a date on there.

**Dave Jones:** Made in the UK. Fantastic. Sir Clive Sinclair and the Sinclair ZX Spectrum. I wonder if it works? I don't know, but I've never actually used one. I don't think that one's that huge here anyway. Oh yeah, I don't think this is working at all

**Dave Jones:** because there's no 9 volt power jack in there, but we've got some cartridge expansion here, microphone, earphone and TV composite output. Really bare bones stuff, but this thing, as with all Sinclair stuff, built down to a price, does the bare basics, and well, it was quite

**Dave Jones:** popular for its day. And probably one of the largest selling computers in the UK if I'm not wrong. But there you go. Beautiful. The old rubber keyboard, not that great. No tactile feedback on those things. They've got the basic commands printed on there.

**Dave Jones:** List, bin, in-key, random, int, cos, sin, tan, peak, peak and poke. Oh, those were the days. And you can change your colour. Blue, red, magenta, green, cyan. Fantastic. True video, whatever that is, caps lock, graphics mode. Ah, beautiful. Hi Dave, I noticed you have a taste for Sinclair products.

**Dave Jones:** I do indeed, so please send me a Sinclair ZX Spectrum 48K, oh, massive, for display in your museum. I was hesitant to send it down in its extremely non-working condition, but after seeing your appreciation of the Sinclair TV and the C5, I decided to do it.

**Dave Jones:** I have my own Sinclair C5 now. It's parked down in my parking space down the bottom, but it's a fixer-upper. Unfortunately. Hmm, it's a bit crusty. Anyway, I've got one, proud owner of a Sinclair C5 now, and now a Sinclair ZX Spectrum. As you may have guessed, the unit is

**Dave Jones:** non-functional, as is the case with the TV you received. I have taken apart from this unit to get another ZX Spectrum up and running. Parts taken include the DC barrel connector, the Ferranti ULA, oh, completely gone, two of the high DRAMs, some of the

**Dave Jones:** ZTEX transistors, and the keyboard membrane connectors. Oh man, no, okay, well, it was probably near dead to begin with. He's curious to know why the traces on the bottom of the main board are wrinkly. Hmm, let's find out. Initially thought that maybe the resist coating was flaking off, but doesn't appear that way.

**Dave Jones:** Well, we'll check it out. I had the pleasure of shaking your hand at the Maker Faire in Sydney. I do remember that. And he mentioned this, I believe. That's the closest to any kind of celebrity I've ever been. I think you need to get out more, because I'm not a celebrity.

**Dave Jones:** So thanks for taking the time to chat. I appreciate it. No worries. Thank you for introducing yourself at Maker Faire. I do like it when people come up and say hi. So thank you very much, Brendan. Let's crack it open. I expect all through-hole stuff in here.

**Dave Jones:** Of course the Ferranti, the main Ferranti chip is gone. Sinclair were obsessed with those. They use them in the Sinclair C5 and bloody everything else. You can poke a damn crow probe at. And oh, there we go. Look at that. Oh man, there's no solder mask even.

**Dave Jones:** Look at that. We've just got tin plated. Jeez, they saved a couple of cents there. Old Clive saving the old dollar to go for sort of, you know, the home madey. You know, it's almost like a, you know, a home etcher. It kind of reminds me of a home etcher kind of thing with just the tin plating and no solder mask.

**Dave Jones:** Oh goodness, but that's actually neatly laid out. We've got our RF modulator up here and there's our main oscillator, 4.436 megahertz and you know, there's the main Ferranti. We've got some memory in here and yeah, it's removed a few things and well, yeah, it sucked a few things out.

**Dave Jones:** Really quite ugly. The regulator over here, that looks a bit dodgy. We have a floater. Look at that. Just a bent 7805 just floating off the board there. They didn't even bother to solder it or screw it down. Ah, good on you Clive.

**Dave Jones:** And of course they didn't gild the lily on the edge connector, literally. I'm quite surprised that Clive decided to spring for silkscreen on this stuff. I mean, you know, really? Oh, pissing away money there, Clive. Copyright 1983, issue 3. But wait, look at the bottom.

**Dave Jones:** We have spared no expense. We've got solder mask. Look at that. Why do it on the top and not the bottom? I don't really know. I don't get it. But there's the crinkly he's talking about. Let's check it out. And there it is, yes.

**Dave Jones:** The famous crinkled ground planes. Very common for the day and the reason for that is because, well, this is all templated traces. This is not SMOBC, or that's the acronym for solder mask over bare copper, which they do these days. Back in the old days like this, they used to just tin

**Dave Jones:** a plate, all of it, part of the manufacturing process, they'd just tin plate everything, all the traces and everything, including these ground planes here. And of course if you've seen the solder coating that you get, how they increase the current handling capacity of solder traces by wave flowing, you'll notice that you'll

**Dave Jones:** you've seen this in previous videos, that it comes up in like globs and all sorts of stuff. So there's obviously tin that builds up and it's not a really nice even surface, and it's not hot air leveled either, which is another process. So they didn't even bother with that.

**Dave Jones:** So what they do is they tin the copper on here, and then they apply the solder mask over the top, and the tin tinning underneath that is actually, so it's not, a lot of people think it's the solder mask crinkling, but it's not.

**Dave Jones:** It's actually the tin built up under there. Which, I'll scrape that off, we'll be able to see it. So there you go, you can see that the tin is, you know, that's how the tin was actually laid down on the board, because they didn't bother to level that out.

**Dave Jones:** That happens on large solder masses like this, large thermal masses like this. That's why you generally won't see, you'll see tiny amounts on the traces there, you can see little tiny pits there, but generally the smaller traces like that are going to be pretty smooth.

**Dave Jones:** And you'll get parts of the ground plane that are smooth, but then the process of actually laying the tin on top of the copper just, you know, forms all of these, you know, globs and traces and things like that, and then they just coat the solder mask

**Dave Jones:** on top. So that's why it's crinkly. And the hardware designed for this was done by a guy called Richard Altwasser, who worked at Sinclair for a couple of years and then went on to a computer company, found a computer company of no note, and went bankrupt apparently.

**Dave Jones:** I wonder what he's doing these days, I wonder what he's working on. If anyone knows, hey, maybe he's even watching. Good on you Richard. Anyway, here's the NEC D780C, it's a Z80 equivalent, Z80 compatible processor of the time. So yes, this is a classic Z80 machine.

**Dave Jones:** And then we've got a Sinclair branded Hitachi mask ROM here. And yeah, that contains a ROM they didn't even bother socketing the thing. Once again, saved a couple of cents on the socket there, so yeah, can't upgrade the bloody firmware in the thing.

**Dave Jones:** And of course, most of the magic's done inside the Ferranti ULA or uncommitted logic array in this thing, and the graphics were simply stunning for the day. Text was 32 columns by 24 characters, absolutely hopeless. And 256 by 192 graphics in like half a dozen

**Dave Jones:** colours. It was, yeah, pretty crusty, but hey, you know, it was extremely popular for the day, and as with all Sinclair stuff, it was affordable. And the much loathed rubberised membrane keyboard here. There was a Chiclet model I think as well, but yeah, I kind of always

**Dave Jones:** liked the look of this, you know, I liked just the colour of the keys, but it copped a lot of flack for it apparently. And to get it out, you've got to prise off the front bezel like that, and that's just all glued down.

**Dave Jones:** And ta-da! We're in like Flynn. And there's our complete rubber membrane. Aha! Right, so they're using just a two-part sandwiched membrane in there, so they haven't got like the carbon backing on the keys, the keys are just rubber. And that pushes down, ah, we can't even separate that

**Dave Jones:** really, I think that's, yeah, that's moulded together as one sheet. So there we go, there's the individual keys. I'm not sure how reliable that sucker was though. So that is a quick look inside the Sinclair ZX Spectrum, another Clive Sinclair classic. And well, yeah, pretty crusty, built down to a price, but hey, it was

**Dave Jones:** very popular in the UK, so you know, credit where credit's due. Good on you Clive, and thank you very much Brendan for sending in this bit of vintage retro computer technology. We love this stuff here on the EEVblog. www.eevblog.co.uk
