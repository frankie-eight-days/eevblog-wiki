---
video_id: IpdJEo9r-HQ
title: EEVblog #942 - Mystery Monday Teardown
url: https://www.youtube.com/watch?v=IpdJEo9r-HQ
source: youtube-asr
timestamps: {"0": 2, "1": 17, "2": 33, "3": 47, "4": 64, "5": 75, "6": 84, "7": 97, "8": 118, "9": 135, "10": 151, "11": 168, "12": 183, "13": 194, "14": 211, "15": 223, "16": 233, "17": 248, "18": 260, "19": 278, "20": 294, "21": 313, "22": 328, "23": 343, "24": 361, "25": 380, "26": 395, "27": 413, "28": 428, "29": 442, "30": 458, "31": 474, "32": 492, "33": 506, "34": 521, "35": 534, "36": 548, "37": 566, "38": 583, "39": 602, "40": 618, "41": 631, "42": 647, "43": 660, "44": 676, "45": 689, "46": 703, "47": 715, "48": 732, "49": 751, "50": 769, "51": 784, "52": 797, "53": 816, "54": 831, "55": 848, "56": 865, "57": 879, "58": 891, "59": 906, "60": 920, "61": 932, "62": 947, "63": 964, "64": 977, "65": 990, "66": 1007, "67": 1021, "68": 1036, "69": 1049, "70": 1065, "71": 1079, "72": 1094, "73": 1113, "74": 1128, "75": 1143, "76": 1158, "77": 1170, "78": 1187}
---

**Dave Jones:** Hi, welcome to Mystery Monday or more precisely mystery teardown Monday. I've got a whole bunch of mailbag stuff I've got in the mailbag for like little kind of weren't worthy of a 2-minute teardown sort of you know justified more

**Dave Jones:** than that. So I kept them on a shelf and there it's really overflowing. So I thought like every Monday for a while hopefully I will just take an item at random from that shelf a mystery item and tear it

**Dave Jones:** down. It won't be a you know a huge extensive you know half hour teardown but a little short thing. Yes, I'll still do mailbag Monday when I get enough items and things like that. But anyway, what is the mystery item? Oh.

**Dave Jones:** Let's have a look. It's the Datentechnik the Mega X Datentechnik. Thank you very much. I normally I keep the notes of who sent this stuff in but I don't actually have that. I believe we got this in a mailbag. I

**Dave Jones:** don't think I tore it down in the mailbag hence why I put it up on the teardown shelf. So what this thing is I believe I can't find any actual data on this module itself but what I believe it

**Dave Jones:** is and maybe it was in the original note in the mailbag I can't even find the original mailbag episode when this one was in. So hopefully I haven't torn it down yet. So I don't have any data on

**Dave Jones:** this thing. Maybe there was some info in the original note in the mailbag this one was sent in but I can't actually find the mailbag episode it was in. Anyway, what I believe it is it comes from a company called where are

**Dave Jones:** they? Uh ADP Gauselmann in Germany. Hi to all my German viewers and they're they're actually a gaming company. They manufacture like a gaming gambling machines or some such and what I believe this is is a secure uh, memory / processing module that's

**Dave Jones:** designed to hold the presumably the security keys or the encryption keys or whatever for the machine itself. And it's designed to be prevent physical tampering of this thing. So, if you try and open this and get out the encryption

**Dave Jones:** keys or whatever's encrypted inside this thing, then it's going to prevent you from doing that. It's going to automatically erase the keys and everything else. We've seen this before in uh, like those um, F post terminal machines that you use at your local

**Dave Jones:** uh, shopping center or service station or point of sale machines. They contain encrypted keys in them and likewise they're kept inside a secure tamper-proof module like this. And of course you could potentially just try and hack the thing through the

**Dave Jones:** external pins like this, but these are designed to do all the secure processing. The encryption keys are kept in here. The processing, the decryption or whatever is all done inside this thing. So, the theory goes that if you try and probe

**Dave Jones:** these pins, hack it in any way like that, you're not going to get any useful data out of it. You have to physically hack into this thing, crack it open, and try and get the encryption keys that way. But they're designed if you crack

**Dave Jones:** this thing open, then the keys instantly erase themselves cuz they're held by battery backed SRAM typically inside this thing. So, you know, you open it up, boom, the battery it dis- it loses memory to the SRAM and boom, the keys

**Dave Jones:** are gone. So, inside this thing, we expect to find some batteries. We expect to find some tamper-proof things. So, if you try and drill through it or something like that, you know, if you know exactly where to drill because hey,

**Dave Jones:** you could get one of these things, take it apart, and then figure out exactly what points to drill in, and then you could get yourself a good one with the keys in it, and then know to drill through, so I'd expect some sort of

**Dave Jones:** tamper-proof mechanism inside this thing and uh battery-backed SRAM and some processing and stuff like that. But, the interesting thing will be to see how they've done the physical security because if you can't hack via the pins, which is the whole concept of

**Dave Jones:** it, then you have to go through physically. So, this one's actually been um opened. Whether or not I opened it previously or it's supplied like that. So, thanks to whoever sent this one in. So, let's actually uh crack this sucker

**Dave Jones:** open and hopefully we can see inside. It looks like like, you know, I would have maybe expected them to weld it shut or something like that, but they haven't actually done that. They haven't done it, so we can actually

**Dave Jones:** get inside this thing. Someone's had a go at this. So, let's Hang on. Is this going to come apart? Yep. Hey, hello. So, we've already The keys are already gone, presumably. Aha, what do we got? We got a board.

**Dave Jones:** Just got a copper board on there. Does that come out? Ah, on the top as well. So, I think this is going to be some sort of What's that? Oh, that's actually that's actually carbon um put down onto the copper pad here and

**Dave Jones:** look. Ta-da! They Oh, yeah, look in the corners here. They've got carbon there as well. And these match up with these dots here. So, they're making electrical contact onto this uh ground plane on the back here. So, we'll get a meter and

**Dave Jones:** we'll just confirm that. And I bet you that is Yeah, that is carbon, all right. There we go, 10 ohms or whatever, and that one over there is conductive as well. So, yeah, they're connected um through to this metal

**Dave Jones:** uh case here and the same on the other side. Is it? Yes, the same. Here we go. So, exactly the same so there. So, the first protection mechanism here is if you take off one side of this like this, presumably there's electrical

**Dave Jones:** connection through there and it detects that you're actually removing the metal covers. So, that's the first thing. So, hang on. Hey, hello. Hello. So, that tada, we're in like Flynn. Aha. Look. You can see the pattern on there. I'll

**Dave Jones:** get the macro lens out and we'll have a closer look at that. And we've got a contact there. And bingo, there's our battery. That's our battery there. And yep, it pops out. There we go. Exactly the same security measure on the

**Dave Jones:** bottom side. So, here we go. They've got the batteries in there. They're going to have them soldered directly on like that for higher reliability. They've got two of them for redundancy presumably. And yep, there's the little contacts which go through to the pad there. Yep,

**Dave Jones:** on the other side there. There's our processor and we'll have a closer look. We've probably got some uh SRAM where the keys are held. Nothing's gunked at all. Um so, I kind of expected maybe to see something gunked in there

**Dave Jones:** like a physical protection. But the whole idea is once you remove these, it breaks the circuit. It might just be as simple as coming from the battery in series with maybe the uh They They look like there's traces in

**Dave Jones:** there. Uh like that. So, if you drill through, it's going to break those traces and bingo, um your SRAM presumably um that holds the keys inside this thing will just erase itself and you've lost them. And bingo, there's our SRAM

**Dave Jones:** memory. These are uh Samsung parts and uh SEC could stand for uh secure, but I couldn't find any mention of uh you know, secure type um application for these things in the uh data sheet for this. So, uh but anyway, these are uh

**Dave Jones:** KM68 uh 1 and 68100 um SRAMs, and normally they work from uh you know, like 5-V parts, but they're actually designed for battery backup applications, exactly what what we uh suspected here with the batteries in that they uh retain their data down to 2

**Dave Jones:** V. So, of course, you know, 3-V uh lithium uh cell like this, you want it to work down to lower voltages. So, normally 5-V parts in the system uh will work at 5-V part at 5 V. It'll have a 5-V processor

**Dave Jones:** and data bus and everything else, but hey, you can still retain the data on them down to 2 V, and that's exactly what you need.

**Dave Jones:** And right next to the batteries here, there's a ancient looking part, 26 week 1985. So, I'm not sure what's going on there cuz a lot of parts um elsewhere on the board are much uh later, as I'll show you. But anyway, a 4543, that's a

**Dave Jones:** real-time clock chip. So, this is, you know, fairly old uh tech in here. Here we go. Uh So, here we go. We're talking uh 14th week '99 there, by the looks of it. So, this looks like a 2000.

**Dave Jones:** Uh yep. Uh Yep, 6 week uh 1999. So, 2000 vintage. We've got ourselves a Atmel microcontroller here, old school uh 90S uh 1200. Do they even still make that one? Um yeah, maybe. And also on the top side of the board

**Dave Jones:** here, a MAX691 uh voltage uh supervisor, microprocessor supervisor. So, that would notify the uh processor when the uh power's removed and uh all that sort of jazz, and uh looks like say HC 573 jelly bean logic regulator. Yep,

**Dave Jones:** some more uh 245 jelly bean stuff, and there's our processor. I can see the Motorola symbol, but uh that's about all she wrote. So, all of our uh uh So, all of our secure key processing and everything else is done inside that

**Dave Jones:** baby, presumably. Um yeah, I'm not sure what the little Atmel micros are doing there. Um that's rather confusing. So, yeah, these SRAMs that are used to uh keep the security keys, or whatever they're trying to uh protect inside this

**Dave Jones:** thing, um these are just uh basically regular uh SRAMs. They're not uh secure uh cryptographic uh SRAMs and uh other memory products, which you can get um these days. Not sure if you You could You probably get them back when this was

**Dave Jones:** uh designed and manufactured, but they didn't bother to uh use those some of those like the proper secure chips and secure micros and stuff. They will actually have um like sometimes an extra security uh protection hardware protection uh

**Dave Jones:** embedded inside the die itself. So, they might have like a security mesh on top or something like that, so you can't physically uh try and get through the chip, even if you could defeat all the other uh security measures inside this

**Dave Jones:** thing, you still couldn't get through to the uh chip itself. You've got an extra layer of protection yet again, but this one doesn't have that. So, let's find out what this puppy is. Ah, it's not going to it's not going to peel off nicely.

**Dave Jones:** And it's got one of those silly unreadable codes, so I'll have to uh look at that under the mantis, and get back to you. Is there a code there? Oh, yeah, there's something there. And there's nothing special about that

**Dave Jones:** uh micro at all. Um it's just not the shelf one, it's It doesn't contain any uh hardware security uh measures on the die or anything else. It's not a a specific security processor or anything like that which might be used in

**Dave Jones:** uh the more upmarket uh EFTPOS terminals and things like or other really uh serious ones. So, anyway, um that just does all the processing and I'm still unsure what that little micro there does. May you know, some sort of

**Dave Jones:** supervisory uh role or something like that, perhaps. Hm. Now, let's take a look at the uh security cover. Hopefully, you might have to watch this in HD. I can't really see it very well on my uh camcorder LCD here, but uh you can see

**Dave Jones:** the traces on the PCB there. So, it's a PCB with all these circular sort of like spiral traces on them, perhaps. Is it I'm not sure of the exact pattern. Anyway, um it that looks like it's just one conductive pad, but

**Dave Jones:** I don't think it is because that wouldn't make sense. I think yep, there we go. That is actually a zebra strip. There we go. That's a better look. That's actually a zebra strip that actually connects um well, it's yeah, it's not the um

**Dave Jones:** elastomer uh type one. It's uh it's different. You'll notice that there's conductive traces on there which go over very fine and that basically connects all these traces in there. There we go. Got four traces and so, these are just

**Dave Jones:** be loop traces. So, that looks like we've got two separate loops there, perhaps. And then um these would likely We'll follow the traces on the board in a minute, but my guess would be that these would uh be in

**Dave Jones:** series with the power line uh power uh trace going to those SRAM chips. So, let's see if I'm right. All right, it's actually hard to trace these uh things, but anyway, these pads go off to transistors and through these resistors.

**Dave Jones:** Here, you can likely see that pad go off to these resistors. So, all of this stuff in here are these those diodes or transistors? They could just be uh diodes, are they? Because that's a common way to switch, or at least some

**Dave Jones:** of them, a common way to switch in the power pins from a battery-backed up SRAM. You just do it through diodes. One comes from the battery through a diode, another one goes via the main main power rail. So, when the power rail

**Dave Jones:** fails, the other one the other diode kicks in and powers it from the battery here. Anyway, uh pin eight over here, this is the power pin over here, and I have actually confirmed um We've got our buzzer on. I have actually confirmed

**Dave Jones:** that that doesn't go through to the power of any of the other chips here. So, I've actually checked that. Um so, they're not actually connected. So, they are somehow breaking into the power pins of these chips, as you'd

**Dave Jones:** expect, cuz that's the whole concept is that it loses the power. These are SRAMs, so they're a volatile memory. If you remove the power, bam, they're gone. You can't recover them. There's no residual anything in there that that you

**Dave Jones:** can actually recover the uh keys from. They're just simply lost. So, yeah, all this stuff around here um seems, although I haven't figured out where the power actually gets back to over here yet, but uh yeah, it's definitely not

**Dave Jones:** connected directly through to the main power rail. But, one thing I did follow is these two pads on the left side here, they actually go through, if you note the location to that physical hole there, they actually go through to the

**Dave Jones:** two pads on the other side. So, it looks like it's one big loop on the top and bottom side of this thing. So, if you remove either the top side or the bottom side, it's one huge loop going through

**Dave Jones:** all of these uh traces on the board. If you try and drill through this, if you physically remove it, or anything like that, bingo, you're going to break the uh traces on there, and that will just erase uh remove power to the SRAMs here,

**Dave Jones:** and keys are goneski. And as for the ground plane on the other side here, I think and those bumps, um I don't think that's actual uh actual connection at all. They're just uh grounding. They're just using that as an internal uh ground uh shield.

**Dave Jones:** Maybe it like it shorts out, you know, if you try and drill through or something like that. So, there's some additional measure that uh you know, it shorts out the power rail or does whatever. Um something like that perhaps, but it

**Dave Jones:** doesn't look like there's actually any connection to forming a loop between like the uh chassis or anything like that to actually detect it. But, I could be wrong. You'd have to look into the exact detail, but yeah, I think all the

**Dave Jones:** security measure is coming from these things. And if you want to know the uh the actual connection, it's not next to each other like this. It's alternate ones. Like that. So, that's measuring about 100 ohms there. And it looks like

**Dave Jones:** we might have an additional security measure here. They've got one of these things, which looks like a surface mount LED, but they've got one top and bottom here. And no, I've tried to uh light that puppy up, and they aren't a LED.

**Dave Jones:** So, that looks like some sort of maybe ambient light sensor. Whereas, if you physically even if you managed to somehow defeat all the loop protection and everything else here, you physically take it off, and the the light gets in

**Dave Jones:** to this thing, then bam, that's going to erase it as well. So, maybe um yeah, the micro looks like it's it's controlling all of the security measures for this thing. So, yeah, this looks like it's implementing some sort of

**Dave Jones:** a smart security solution in that micro handling all that. So, that you know, it's a bit more advanced than just looping the power pins through the micro through the top and bottom of these things. So, it's a bit more advanced

**Dave Jones:** than that. So, that's all right. So, there you have it. There's a look at a security module for a gaming machine which does the processing that handles the encryption keys or something like that. If anyone knows the exact details

**Dave Jones:** of this, please leave it in the comments down below. But, yeah, that's a rather primitive one compared to some of the more modern-day ones that actually as I said have physical security features on the die. And there's various specialist

**Dave Jones:** manufacturers of these chips designed for FPOS start and other high security terminals that you know, have to keep the encryption keys secure from the factory actually on the on the physical micro themselves with the building memory. They might have SRAM on there or

**Dave Jones:** um in this case, you know, fairly old school. I mean, this thing's at least 16 years old. You know, external SRAM memory like this battery backup. And you know, they've gone to a fair amount of trouble with the intelligent micro in there to

**Dave Jones:** handle all the security and just a physical shield like that that connects over with all those fine looped traces to try and prevent drill through. So, you know, you shouldn't be able to hack these things through the external pins.

**Dave Jones:** So, they would have you know, would have you know, there's probably maybe even standards for this in the gaming industry or whatever Um, actually define, you know, the ability to, uh you know, not hack these things through the pins. So, you'd have

**Dave Jones:** to, you know, go in physically to try and extract the keys or the data or whatever it is they're trying to protect. So, there you go. That's a rather interesting look inside a secure memory module. And if you liked this

**Dave Jones:** new, don't know if it'll last forever, but I might keep it up fairly regularly. Just a smallish tear down of a random mystery item from my very overflowing bench up there with all the all the tear down stuff on it. Anyway,

**Dave Jones:** like that sent in via mailbag and various other stuff. So, if you like that, please give it a big thumbs up. Woah, that's a big thumb. Catch you next time.
