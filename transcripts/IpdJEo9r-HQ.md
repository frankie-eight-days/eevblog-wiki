---
video_id: IpdJEo9r-HQ
title: EEVblog #942 - Mystery Monday Teardown
url: https://www.youtube.com/watch?v=IpdJEo9r-HQ
source: youtube-asr
timestamps: {"0": 2, "1": 17, "2": 33, "3": 41, "4": 62, "5": 81, "6": 93, "7": 105, "8": 125, "9": 140, "10": 155, "11": 172, "12": 186, "13": 204, "14": 213, "15": 233, "16": 249, "17": 264, "18": 278, "19": 290, "20": 305, "21": 318, "22": 328, "23": 346, "24": 364, "25": 382, "26": 395, "27": 404, "28": 420, "29": 432, "30": 456, "31": 472, "32": 493, "33": 503, "34": 521, "35": 531, "36": 544, "37": 560, "38": 580, "39": 602, "40": 620, "41": 638, "42": 662, "43": 676, "44": 685, "45": 696, "46": 707, "47": 720, "48": 736, "49": 753, "50": 769, "51": 784, "52": 802, "53": 818, "54": 836, "55": 853, "56": 870, "57": 881, "58": 894, "59": 907, "60": 920, "61": 932, "62": 948, "63": 958, "64": 974, "65": 984, "66": 998, "67": 1015, "68": 1038, "69": 1053, "70": 1065, "71": 1076, "72": 1092, "73": 1110, "74": 1120, "75": 1137, "76": 1156, "77": 1163, "78": 1175, "79": 1189}
---

**Dave Jones:** Hi, welcome to Mystery Monday or more precisely mystery teardown Monday. I've got a whole bunch of mailbag stuff I've got in the mailbag for like little kind of weren't worthy of a 2-minute teardown sort of you know justified more than that.

**Dave Jones:** So I kept them on a shelf and there it's really overflowing. So I thought like every Monday for a while hopefully I will just take an item at random from that shelf a mystery item and tear it down.

**Dave Jones:** It won't be a you know a huge extensive you know half hour teardown but a little short thing. Yes, I'll still do mailbag Monday when I get enough items and things like that.

**Dave Jones:** But anyway, what is the mystery item? Oh. Let's have a look. It's the Datentechnik the Mega X Datentechnik. Thank you very much. I normally I keep the notes of who sent this stuff in but I don't actually have that.

**Dave Jones:** I believe we got this in a mailbag. I don't think I tore it down in the mailbag hence why I put it up on the teardown shelf. So what this thing is I believe I can't find any actual data on this module itself but what I believe it is and maybe it was in the original note in the mailbag I can't even find the original mailbag episode when this one

**Dave Jones:** was in. So hopefully I haven't torn it down yet. So I don't have any data on this thing. Maybe there was some info in the original note in the mailbag this one was sent in but I can't actually find the mailbag episode it was in.

**Dave Jones:** Anyway, what I believe it is it comes from a company called where are they? Uh ADP Gauselmann in Germany. Hi to all my German viewers and they're they're actually a gaming company.

**Dave Jones:** They manufacture like a gaming gambling machines or some such and what I believe this is is a secure uh, memory / processing module that's designed to hold the presumably the security keys or the encryption keys or whatever for the machine itself.

**Dave Jones:** And it's designed to be prevent physical tampering of this thing. So, if you try and open this and get out the encryption keys or whatever's encrypted inside this thing, then it's going to prevent you from doing that.

**Dave Jones:** It's going to automatically erase the keys and everything else. We've seen this before in uh, like those um, F post terminal machines that you use at your local uh, shopping center or service station or point of sale machines.

**Dave Jones:** They contain encrypted keys in them and likewise they're kept inside a secure tamper-proof module like this. And of course you could potentially just try and hack the thing through the external pins like this, but these are designed to do all the secure processing.

**Dave Jones:** The encryption keys are kept in here. The processing, the decryption or whatever is all done inside this thing. So, the theory goes that if you try and probe these pins, hack it in any way like that, you're not going to get any useful data out of it.

**Dave Jones:** You have to physically hack into this thing, crack it open, and try and get the encryption keys that way. But they're designed if you crack this thing open, then the keys instantly erase themselves cuz they're held by battery backed SRAM typically inside this thing.

**Dave Jones:** So, you know, you open it up, boom, the battery it dis- it loses memory to the SRAM and boom, the keys are gone. So, inside this thing, we expect to find some batteries.

**Dave Jones:** We expect to find some tamper-proof things. So, if you try and drill through it or something like that, you know, if you know exactly where to drill because hey, you could get one of these things, take it apart, and then figure out exactly what points to drill in, and then you could get yourself a good one with the keys in it, and then know to drill through, so I'd expect some sort of

**Dave Jones:** tamper-proof mechanism inside this thing and uh battery-backed SRAM and some processing and stuff like that. But, the interesting thing will be to see how they've done the physical security because if you can't hack via the pins, which is the whole concept of it, then you have to go through physically.

**Dave Jones:** So, this one's actually been um opened. Whether or not I opened it previously or it's supplied like that. So, thanks to whoever sent this one in. So, let's actually uh crack this sucker open and hopefully we can see inside.

**Dave Jones:** It looks like like, you know, I would have maybe expected them to weld it shut or something like that, but they haven't actually done that. They haven't done it, so we can actually get inside this thing.

**Dave Jones:** Someone's had a go at this. So, let's Hang on. Is this going to come apart? Yep. Hey, hello. So, we've already The keys are already gone, presumably. Aha, what do we got?

**Dave Jones:** We got a board. Just got a copper board on there. Does that come out? Ah, on the top as well. So, I think this is going to be some sort of What's that?

**Dave Jones:** Oh, that's actually that's actually carbon um put down onto the copper pad here and look. Ta-da! They Oh, yeah, look in the corners here. They've got carbon there as well.

**Dave Jones:** And these match up with these dots here. So, they're making electrical contact onto this uh ground plane on the back here. So, we'll get a meter and we'll just confirm that.

**Dave Jones:** And I bet you that is Yeah, that is carbon, all right. There we go, 10 ohms or whatever, and that one over there is conductive as well. So, yeah, they're connected um through to this metal uh case here and the same on the other side.

**Dave Jones:** Is it? Yes, the same. Here we go. So, exactly the same so there. So, the first protection mechanism here is if you take off one side of this like this, presumably there's electrical connection through there and it detects that you're actually removing the metal covers.

**Dave Jones:** So, that's the first thing. So, hang on. Hey, hello. Hello. So, that tada, we're in like Flynn. Aha. Look. You can see the pattern on there. I'll get the macro lens out and we'll have a closer look at that.

**Dave Jones:** And we've got a contact there. And bingo, there's our battery. That's our battery there. And yep, it pops out. There we go. Exactly the same security measure on the bottom side.

**Dave Jones:** So, here we go. They've got the batteries in there. They're going to have them soldered directly on like that for higher reliability. They've got two of them for redundancy presumably.

**Dave Jones:** And yep, there's the little contacts which go through to the pad there. Yep, on the other side there. There's our processor and we'll have a closer look. We've probably got some uh SRAM where the keys are held.

**Dave Jones:** Nothing's gunked at all. Um so, I kind of expected maybe to see something gunked in there like a physical protection. But the whole idea is once you remove these, it breaks the circuit.

**Dave Jones:** It might just be as simple as coming from the battery in series with maybe the uh They They look like there's traces in there. Uh like that. So, if you drill through, it's going to break those traces and bingo, um your SRAM presumably um that holds the keys inside this thing will just erase itself and you've lost them.

**Dave Jones:** And bingo, there's our SRAM memory. These are uh Samsung parts and uh SEC could stand for uh secure, but I couldn't find any mention of uh you know, secure type um application for these things in the uh data sheet for this.

**Dave Jones:** So, uh but anyway, these are uh KM68 uh 1 and 68100 um SRAMs, and normally they work from uh you know, like 5-V parts, but they're actually designed for battery backup applications, exactly what what we uh suspected here with the batteries in that they uh retain their data down to 2 V.

**Dave Jones:** So, of course, you know, 3-V uh lithium uh cell like this, you want it to work down to lower voltages. So, normally 5-V parts in the system uh will work at 5-V part at 5 V.

**Dave Jones:** It'll have a 5-V processor and data bus and everything else, but hey, you can still retain the data on them down to 2 V, and that's exactly what you need.

**Dave Jones:** And right next to the batteries here, there's a ancient looking part, 26 week 1985. So, I'm not sure what's going on there cuz a lot of parts um elsewhere on the board are much uh later, as I'll show you.

**Dave Jones:** But anyway, a 4543, that's a real-time clock chip. So, this is, you know, fairly old uh tech in here. Here we go. Uh So, here we go. We're talking uh 14th week '99 there, by the looks of it.

**Dave Jones:** So, this looks like a 2000. Uh yep. Uh Yep, 6 week uh 1999. So, 2000 vintage. We've got ourselves a Atmel microcontroller here, old school uh 90S uh 1200.

**Dave Jones:** Do they even still make that one? Um yeah, maybe. And also on the top side of the board here, a MAX691 uh voltage uh supervisor, microprocessor supervisor. So, that would notify the uh processor when the uh power's removed and uh all that sort of jazz, and uh looks like say HC 573 jelly bean logic regulator.

**Dave Jones:** Yep, some more uh 245 jelly bean stuff, and there's our processor. I can see the Motorola symbol, but uh that's about all she wrote. So, all of our uh uh So, all of our secure key processing and everything else is done inside that baby, presumably.

**Dave Jones:** Um yeah, I'm not sure what the little Atmel micros are doing there. Um that's rather confusing. So, yeah, these SRAMs that are used to uh keep the security keys, or whatever they're trying to uh protect inside this thing, um these are just uh basically regular uh SRAMs.

**Dave Jones:** They're not uh secure uh cryptographic uh SRAMs and uh other memory products, which you can get um these days. Not sure if you You could You probably get them back when this was uh designed and manufactured, but they didn't bother to uh use those some of those like the proper secure chips and secure micros and stuff.

**Dave Jones:** They will actually have um like sometimes an extra security uh protection hardware protection uh embedded inside the die itself. So, they might have like a security mesh on top or something like that, so you can't physically uh try and get through the chip, even if you could defeat all the other uh security measures inside this thing, you still couldn't get through to the uh chip itself.

**Dave Jones:** You've got an extra layer of protection yet again, but this one doesn't have that. So, let's find out what this puppy is. Ah, it's not going to it's not going to peel off nicely.

**Dave Jones:** And it's got one of those silly unreadable codes, so I'll have to uh look at that under the mantis, and get back to you. Is there a code there?

**Dave Jones:** Oh, yeah, there's something there. And there's nothing special about that uh micro at all. Um it's just not the shelf one, it's It doesn't contain any uh hardware security uh measures on the die or anything else.

**Dave Jones:** It's not a a specific security processor or anything like that which might be used in uh the more upmarket uh EFTPOS terminals and things like or other really uh serious ones.

**Dave Jones:** So, anyway, um that just does all the processing and I'm still unsure what that little micro there does. May you know, some sort of supervisory uh role or something like that, perhaps.

**Dave Jones:** Hm. Now, let's take a look at the uh security cover. Hopefully, you might have to watch this in HD. I can't really see it very well on my uh camcorder LCD here, but uh you can see the traces on the PCB there.

**Dave Jones:** So, it's a PCB with all these circular sort of like spiral traces on them, perhaps. Is it I'm not sure of the exact pattern. Anyway, um it that looks like it's just one conductive pad, but I don't think it is because that wouldn't make sense.

**Dave Jones:** I think yep, there we go. That is actually a zebra strip. There we go. That's a better look. That's actually a zebra strip that actually connects um well, it's yeah, it's not the um elastomer uh type one.

**Dave Jones:** It's uh it's different. You'll notice that there's conductive traces on there which go over very fine and that basically connects all these traces in there. There we go. Got four traces and so, these are just be loop traces.

**Dave Jones:** So, that looks like we've got two separate loops there, perhaps. And then um these would likely We'll follow the traces on the board in a minute, but my guess would be that these would uh be in series with the power line uh power uh trace going to those SRAM chips.

**Dave Jones:** So, let's see if I'm right. All right, it's actually hard to trace these uh things, but anyway, these pads go off to transistors and through these resistors. Here, you can likely see that pad go off to these resistors.

**Dave Jones:** So, all of this stuff in here are these those diodes or transistors? They could just be uh diodes, are they? Because that's a common way to switch, or at least some of them, a common way to switch in the power pins from a battery-backed up SRAM.

**Dave Jones:** You just do it through diodes. One comes from the battery through a diode, another one goes via the main main power rail. So, when the power rail fails, the other one the other diode kicks in and powers it from the battery here.

**Dave Jones:** Anyway, uh pin eight over here, this is the power pin over here, and I have actually confirmed um We've got our buzzer on. I have actually confirmed that that doesn't go through to the power of any of the other chips here.

**Dave Jones:** So, I've actually checked that. Um so, they're not actually connected. So, they are somehow breaking into the power pins of these chips, as you'd expect, cuz that's the whole concept is that it loses the power.

**Dave Jones:** These are SRAMs, so they're a volatile memory. If you remove the power, bam, they're gone. You can't recover them. There's no residual anything in there that that you can actually recover the uh keys from.

**Dave Jones:** They're just simply lost. So, yeah, all this stuff around here um seems, although I haven't figured out where the power actually gets back to over here yet, but uh yeah, it's definitely not connected directly through to the main power rail.

**Dave Jones:** But, one thing I did follow is these two pads on the left side here, they actually go through, if you note the location to that physical hole there, they actually go through to the two pads on the other side.

**Dave Jones:** So, it looks like it's one big loop on the top and bottom side of this thing. So, if you remove either the top side or the bottom side, it's one huge loop going through all of these uh traces on the board.

**Dave Jones:** If you try and drill through this, if you physically remove it, or anything like that, bingo, you're going to break the uh traces on there, and that will just erase uh remove power to the SRAMs here, and keys are goneski.

**Dave Jones:** And as for the ground plane on the other side here, I think and those bumps, um I don't think that's actual uh actual connection at all. They're just uh grounding.

**Dave Jones:** They're just using that as an internal uh ground uh shield. Maybe it like it shorts out, you know, if you try and drill through or something like that. So, there's some additional measure that uh you know, it shorts out the power rail or does whatever.

**Dave Jones:** Um something like that perhaps, but it doesn't look like there's actually any connection to forming a loop between like the uh chassis or anything like that to actually detect it.

**Dave Jones:** But, I could be wrong. You'd have to look into the exact detail, but yeah, I think all the security measure is coming from these things. And if you want to know the uh the actual connection, it's not next to each other like this.

**Dave Jones:** It's alternate ones. Like that. So, that's measuring about 100 ohms there. And it looks like we might have an additional security measure here. They've got one of these things, which looks like a surface mount LED, but they've got one top and bottom here.

**Dave Jones:** And no, I've tried to uh light that puppy up, and they aren't a LED. So, that looks like some sort of maybe ambient light sensor. Whereas, if you physically even if you managed to somehow defeat all the loop protection and everything else here, you physically take it off, and the the light gets in to this thing, then bam, that's going to erase it as well.

**Dave Jones:** So, maybe um yeah, the micro looks like it's it's controlling all of the security measures for this thing. So, yeah, this looks like it's implementing some sort of a smart security solution in that micro handling all that.

**Dave Jones:** So, that you know, it's a bit more advanced than just looping the power pins through the micro through the top and bottom of these things. So, it's a bit more advanced than that.

**Dave Jones:** So, that's all right. So, there you have it. There's a look at a security module for a gaming machine which does the processing that handles the encryption keys or something like that.

**Dave Jones:** If anyone knows the exact details of this, please leave it in the comments down below. But, yeah, that's a rather primitive one compared to some of the more modern-day ones that actually as I said have physical security features on the die.

**Dave Jones:** And there's various specialist manufacturers of these chips designed for FPOS start and other high security terminals that you know, have to keep the encryption keys secure from the factory actually on the on the physical micro themselves with the building memory.

**Dave Jones:** They might have SRAM on there or um in this case, you know, fairly old school. I mean, this thing's at least 16 years old. You know, external SRAM memory like this battery backup.

**Dave Jones:** And you know, they've gone to a fair amount of trouble with the intelligent micro in there to handle all the security and just a physical shield like that that connects over with all those fine looped traces to try and prevent drill through.

**Dave Jones:** So, you know, you shouldn't be able to hack these things through the external pins. So, they would have you know, would have you know, there's probably maybe even standards for this in the gaming industry or whatever Um, actually define, you know, the ability to, uh you know, not hack these things through the pins.

**Dave Jones:** So, you'd have to, you know, go in physically to try and extract the keys or the data or whatever it is they're trying to protect. So, there you go.

**Dave Jones:** That's a rather interesting look inside a secure memory module. And if you liked this new, don't know if it'll last forever, but I might keep it up fairly regularly.

**Dave Jones:** Just a smallish tear down of a random mystery item from my very overflowing bench up there with all the all the tear down stuff on it. Anyway, like that sent in via mailbag and various other stuff.

**Dave Jones:** So, if you like that, please give it a big thumbs up. Woah, that's a big thumb. Catch you next time.
