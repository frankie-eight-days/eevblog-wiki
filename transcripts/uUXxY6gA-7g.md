---
video_id: uUXxY6gA-7g
title: EEVblog 1376 - Tandy 102 Vintage Computer REPAIR
url: https://www.youtube.com/watch?v=uUXxY6gA-7g
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 32, "3": 43, "4": 60, "5": 71, "6": 85, "7": 97, "8": 112, "9": 128, "10": 142, "11": 157, "12": 177, "13": 192, "14": 209, "15": 224, "16": 240, "17": 256, "18": 272, "19": 287, "20": 303, "21": 319, "22": 334, "23": 350, "24": 365, "25": 380, "26": 394, "27": 405, "28": 421, "29": 436, "30": 455, "31": 469, "32": 484, "33": 497, "34": 511, "35": 528, "36": 545, "37": 560, "38": 576, "39": 587, "40": 598, "41": 617, "42": 632, "43": 641, "44": 653, "45": 668, "46": 685, "47": 699, "48": 710, "49": 721, "50": 734, "51": 749, "52": 762, "53": 777, "54": 795, "55": 804, "56": 819, "57": 837, "58": 849, "59": 860, "60": 871, "61": 885, "62": 899, "63": 913, "64": 925, "65": 936, "66": 946, "67": 955, "68": 966, "69": 981, "70": 997, "71": 1008, "72": 1023, "73": 1039, "74": 1058, "75": 1070, "76": 1083, "77": 1096, "78": 1108, "79": 1124, "80": 1139, "81": 1154, "82": 1167, "83": 1181, "84": 1196, "85": 1212, "86": 1222, "87": 1237, "88": 1253, "89": 1266, "90": 1283, "91": 1300, "92": 1312, "93": 1324, "94": 1339, "95": 1362, "96": 1379, "97": 1392, "98": 1406, "99": 1418, "100": 1430, "101": 1443, "102": 1452, "103": 1465, "104": 1480, "105": 1498, "106": 1512, "107": 1526, "108": 1542, "109": 1562, "110": 1573, "111": 1590, "112": 1605, "113": 1621, "114": 1634, "115": 1645, "116": 1664, "117": 1679, "118": 1691, "119": 1710, "120": 1726, "121": 1741, "122": 1759, "123": 1775}
---

**Dave Jones:** Hi, check it out. This is a Tandy 102 portable computer, one of the world's first and most popular portable computers of all time. This is the upgrade to the classic Tandy 100 from 1983. This is the 102. Dates from about this

**Dave Jones:** model came out in 1986 and it's identical to the model 100. It's just a little bit thinner and lighter and anyway, this was basically the most popular notebook computer in the 1980s had a modem built in. Every single like you know, reporter,

**Dave Jones:** journalist had one of these things cuz they could type up their stories, connect it to their acoustic coupler modem and then dial back in and send their story back to the news desk and stuff like that. Let alone countless

**Dave Jones:** other uses, but I've done a teardown video of the original 100, but I also have a Tandy 102. We can see some classic yellowing of the bromine in the plastics here. It's a fire retardant that causes like them to like go yellow over time and

**Dave Jones:** that's fairly typical. But anyway, I did a teardown of the 100. This is the 102 and it's just it used to work, but it's now got a rather unusual fault. So, let's take a look at it and see if we

**Dave Jones:** can fix it. Oh, and by the way, the Tandy 100 is famous for being one of the last computers actually containing significant code written by Bill Gates himself. So, he actually worked on the ROM for this thing. So, the original

**Dave Jones:** Tandy 100. Anyway, let's switch it on and you can see it appears to actually work. Copyright Microsoft text telecom address that had like a spreadsheet, a word processor built in and basic built in and everything. But, you can see up

**Dave Jones:** the top here um there's something weird going on. It's like there's you know, look, you can see the clock up there. It's here 54, 55, 56, but it's all sort of weirdy. Something's going on. This doesn't look correct and well, let's go

**Dave Jones:** into the basic here and let's have a look. Uh yeah, model 100 software, once again, this top corner up here, something weird is going on. We've got two flashing cursors. This should say, you know, something bytes free, right? Um I don't know how I I

**Dave Jones:** can't remember how much memory's in this one, but yeah, something has gone wrong and Microsoft What's all this going on? Something weird. Right, let's clear this, okay? So, everything looks to be working just fine and dandy, but let's have a look

**Dave Jones:** what happens here, okay? What I'll do is I'll just uh like 1 2 3 4. So, everything seems to be working. 5 6 7, but watch this. We go to 8. Oops. Once we went past 8, the cursor

**Dave Jones:** has wrapped back here and it's starting to overwrite. So, 9 0 1 2 3 4 5 6 7 8 and it just keeps overriding like that. And it's no coincidence that it's doing it after the eighth character. So, because, you know,

**Dave Jones:** there'll be an 8-bit bus that's shifting whatever it might store like, you know, one column or something as a byte or, you know, whatever. It's no coincidence that the number is eight. And if we go down here like this, you can see once we

**Dave Jones:** get actually down to the four the fifth line down here, the cursor wraps up here and it duplicates anything on the fifth line. And then duplicates anything on the fifth line on the first line and then once again

**Dave Jones:** continues to wrap. And if we go down another line, it'll duplicate it. Uh so, the uh the eighth line down here, it'll duplicate it on the fourth line. Isn't that fascinating? So, there's obviously something to do with the how

**Dave Jones:** the data's getting into the display driver. The display driver's obviously working cuz the correct characters are showing up. It's like it's basically garbage in, garbage out, pretty much. So, the actual column and line drivers and everything else of the LCD seem to

**Dave Jones:** be just fine. So, we can pretty much rule out that as an issue. It's It's the data being fed into them. And this LCD is going to have multiple driver chips for it. Probably, like there's probably going to be like one chip controlling

**Dave Jones:** like the first four lines here and the first eight characters. probably got another chip controlling that one. So, it's probably that chip up there that's causing some sort of issue. Anyway, luckily, we do have the schematics. Schematics. I need schematics. For those

**Dave Jones:** playing along at home, this is 1986 10th month, I presume. It's like it I presume that's a lowish serial number. If anyone knows, please let us know. A product of Japan. All this stuff's made in Japan. Oh, and if

**Dave Jones:** you don't know, it has a memory protection switch because this didn't have any of that non-volatile rubbish. It was volatile SRAM. It kept your programming when you switched it off. So, good old SRAM. And yeah, you could protect that or not with your batteries.

**Dave Jones:** And there we go. You can plug in expansion RAM there. So, that looks like it has an additional 62256 in there. Oh, okay. Other stuff if you haven't seen it. RS232 serial, a system bus connector, a printer connector, the phone that was your modem

**Dave Jones:** cuz it does actually have and you know, a proper isolation transformer in there. And your cassette tape storage. It had a light pen. You know, good for like inventory control for warehouses and stuff like that. That's the direction

**Dave Jones:** answer originate. For those who are used to your modem sex, you'll know all about that. All right, I think I've got this mostly off. That should lift off. We're in like Flynn. There we go. And the keyboard on this feels beautiful, by

**Dave Jones:** the way. It's just ah it's fantastic. So, there's our LCD up there. Whether or not we can get Oh, yeah. Yeah, we can flippity do dah. You betcha we can flippity do dah that. Ah, that's just beautiful. So, we can still use

**Dave Jones:** this. Let me switch it on and we should find that yep yep, and picked up where we left off. Oh, look. Oh, that's it. I hadn't tried that. It didn't actually Look, it didn't actually refresh the contents up there.

**Dave Jones:** That's interesting. Ah, like it kept everything else but it didn't refresh that. But, when it's getting new data like it is now, I mean if we go down a lot Oh, there we go. No, no, it's updated. But

**Dave Jones:** yeah, it cleared it. That's fascinating. All right, I know you want to see the rest of it. Um I can't remember how this differs from the Oh, yeah. No, this is I do believe this is very different from the 100.

**Dave Jones:** Yep. Um this is This is the revised model, thinner and lighter weight, double-sided load. Look at that. Wow, surface mount. The other one was all through-hole, wasn't it? Anyway, we've got some bodge wires and some bodge caps. Um the the bodge wires look like

**Dave Jones:** big ground stuff. Is that an inductor or a diode? Not sure. You can see the red glue underneath the chips there. That's to hold them on. Ah, yes, I remember this from the previous teardown. This is absolutely fantastic. This is some uh

**Dave Jones:** PCB routing perfection here. You'll notice that um there's no markings on this chip. That's because it's mounted upside down. It's mounted in a cutout in the PCB. Why have they put uh one row of them like this and the other like

**Dave Jones:** this? This is for PCB routing reasons. It's just the way that the pin outs worked. If you had these chips up the other way, like these ones, it would all be higgledy-piggledy and you need extra layers on your board to to route it all.

**Dave Jones:** It'd be an absolute mess. So, from a PCB layout elegance point of view, they've mounted these chips backwards with a cutout in the board. It's just It It's simply brilliant. It really is. Hats off. Luckily, we do have the service

**Dave Jones:** manual complete with all the schematics, the theory of operation, the whole works. They don't make them like this anymore, unfortunately. Tandy 102 custom manufactured for Radio Shack, a division of Tandy Corporation. Oh, look at this. Look at this. Ah, just a wet dream.

**Dave Jones:** Maintenance disassembly instructions, theory of operation, troubleshooting. Ah, beautiful. I doubt though I actually haven't looked. I doubt they'll have a troubleshooting procedure for like this sort of fault in the LCD, but you never know. Look at this. It's so

**Dave Jones:** comprehensive. Look at it. Look. Look. Fantastic. Bobby Doesler. Anyway, there's the back of our LCD board. And look at this. Here's the LCD driver board. Look at this. We have two rows here because this is a 40 column by eight line LCD. And

**Dave Jones:** obviously, each row of these chips here will be handling four lines. And we've got five for the columns. So, 40 divided by five, eight. Ta-da! Is it just simply this chip that Well, if I'm flipping it the right whichever

**Dave Jones:** way it's, you know, actually flipped. Yeah, it could be M1 M1 up there. That could be it. So, I Yeah. Right off the bat, you would suspect this driver here. It's It's a Hitachi cuz they did all the They still dominate

**Dave Jones:** LCD drivers, don't they? I don't know. Yeah, the standard Hitachi chip set. Anyway, the HD44102 for those playing along at home. So, automatically, you would either suspect this chip has failed or it's getting bad drive signals coming into it. There

**Dave Jones:** could be a chip select, there could be an address line, you know, whatever. There could be some data corruption. But, you know, it's obviously clocking No, it's obviously getting the data in there correct. So, it's got to be some

**Dave Jones:** sort of, you know, like some sort of chip select thing. But, it may not be that chip. It may be off on the main processor board which actually drives it. There's the specs for those playing along at home. Ladies, four AA

**Dave Jones:** batteries. Last like 20 hours you can use this bad boy for. Unbelievable. Anyway, fantastic. 80 I C85 processor. So, we've got theory of operation here. LCD, LCD common drive, LCD segment drive, LCD waveform, uh the block diagram. Yep. Okay, so an

**Dave Jones:** 81C55 drives into the LCD controller and then the LCD. But, it also like it comes via the CPU bus as well. So, it doesn't all come via the PIO. So, the PIO's probably only like driving the chip select lines

**Dave Jones:** and things like that. It is. They don't make theory of operations anymore, do they?

**Dave Jones:** We'll get to the There's the modem interface. I do want to do a video trying to use the modem on this thing. I think that'd be really cool. There's the modem connector interface circuit. Um I've done some experiments before in the

**Dave Jones:** past with I can't remember if it was this 102 or the original 100, but yeah, anyway. LCD. Here we are. The LCD used in the Tandy 102 is composed of electrodes in a matrix arrangement. 64 common signals, 480 segment signals. This part is

**Dave Jones:** subdivided into three segments. The common driver, the segment driver, and the waveform. The common driver, here it is. That's the HD44103. Uses two common driver ICs. K, M11 and M12. Where was that thing we had before? So, yeah, there's your common driver

**Dave Jones:** there and down there. I don't think it's going to be the common driver because, well, it's common. It's more likely to be the segment uh, drivers. Now, I don't think we're going to have to go into like the internal logic of the 44103 and

**Dave Jones:** the other, uh, common driver. I don't, you know, it's just it's just getting I think it's just getting the wrong stuff clocked into it. I think that is the problem. It could be via any number of reasons. There could be a dry joint

**Dave Jones:** somewhere. One of the driver chips could be failed. Or something could be wrong with the something could else could be loading down the bus, which is, uh, going to be common. Who knows? But, uh, yeah, I don't think we're going to have

**Dave Jones:** to get into that sort of detail. Uh, that's sort of like the last rabbit hole we want to jump down. Show us the schematic, Dave. Okay, after the bill of materials, here it is. Oh, isn't that just brilliant? Absolutely brilliant.

**Dave Jones:** Fantastic. Takes a second just to render a new sharper version. But, anyway, all the goodness it's all down here. All right. So, what we want here's our LCD connector here. Okay? Okay, we've got some CMOS logic doing some stuff here. Not worried about

**Dave Jones:** that yet. Let's have a look at the address and data lines here. Right. So, let's follow this here AD. So, this is the, uh, this is the data, um, bus. It's not actually the address bus. These chip selects are the address. So, if we

**Dave Jones:** follow the data here, okay? This comes over here. It's going Yep, it's coming it's all the way it's coming from here, which, uh, let's not go there. But, let's follow the money up here, up here, up here. Here you go.

**Dave Jones:** There you go. We've got a 245 there. And that's hooked 8085, uh, processor, uh, data bus, right? So, I don't expect there really, uh, like to be any issue with the processor addresses and data buses because everything hangs off that,

**Dave Jones:** right? So, it doesn't everything else works. So, I don't expect that to be an issue. So, that's kind of like the last thing that you would look at here. So, I'm not worried about the data bus there. All

**Dave Jones:** the the seems to be getting in. It's just getting latched wrong. So, there's uh looks like there's all these well, thing is it says chip select 1 2 3 4 here. These ones have no label. So, we'll go check the LCD schematic in a

**Dave Jones:** sec, but these come from PA0 PA1. So, these come from yeah, an 81C55 up here, okay? So, that's being driven from there. So, that's an IO uh coming from the processor. So, it's writing to this and then uh four of those lines are

**Dave Jones:** going into driving the LCD. And then other stuff, you know, look the the read write pins. So, it looks like it does it can potentially read back. I don't know where S1 is coming from or SI, but I

**Dave Jones:** wouldn't expect there like to be any issue with the reset cuz the LCD's just working just fine. And I don't expect that, you know, there's no problem with any of the voltage drivers or any of that sort of stuff, you know? So, all

**Dave Jones:** all the enable here, so you know, you wouldn't bother looking at that. Uh I don't know what this second what this chip select here does, but you know, we're looking at one specific segment of the LCD. So, there's nothing to see

**Dave Jones:** here. Move along now to the LCD schematic. They've got a nice-looking LCD. And it's like, you know, it's very it's laid out very well. Look, you know, like M1 up here is, you know, they've done it overlaid it into

**Dave Jones:** the specific thing. They've got uh information with driving the commons and stuff and the segments and the commons and stuff like this. Absolutely brilliant. So, anyway, so this is looking face on like we saw. And as you saw, we were having problems in this

**Dave Jones:** quadrant here, the first four lines and the first eight characters. Well, as we said, that's going to be controlled by M1 here. So, what's coming into M1? Let's have a look. Tilt your head with me. Once again, I wouldn't expect any of

**Dave Jones:** like the voltage things to be a problem because it's, you know, the fate segments aren't faded. They're not doing anything like that. And they're all just uh you know, common from with all the other chips. It's you know, it's not a

**Dave Jones:** problem. So, it's you know, data going into this sucker. So, it could be you know, I'd be looking at the first thing I'd be probing. I don't know if I got the scope out would be I'm probably going to have to unless you were just

**Dave Jones:** want to go, well, it's probably that one and you know, if you had like an LCD swap or something like that to swap over you might swap it over and you know that it's nothing on the driving side of

**Dave Jones:** things. It's on the LCD module and then you might go, well, okay, it's got to be this chip here and then you know, but even if you do that, you've still got to like probe it to see like it could be a

**Dave Jones:** dry joint. Could be a bad solder joint on one of these control pins or something like that. Once again, I don't think it's the data because the data actually gets in there. You saw it as we we were we were able to write into these

**Dave Jones:** particular segments. It's just that yeah, the interesting thing is when we were driving this one here in this bottom corner of the LCD like this. So, if we were driving like line five here, line one would like duplicate the stuff

**Dave Jones:** on line five here. So, when we're writing data to this, it's also appearing on this and you might think, oh, okay, you know, there could be like some short between maybe there's some I don't know, there's there's some tin whiskers or something

**Dave Jones:** happening and there's a little short between, you know, just throwing that one out there. I keep that in your back of your mind, but this is where you got to like go back to here and look nine eye all these other lines all these chip

**Dave Jones:** selects are being driven. So, I don't know why the labels were missing. They they're certainly going up here. It's a bit hard to read, but you can see that's that CS28 there for example. So, that's CS21. Oh, they're actually out of order. 67123

**Dave Jones:** like so that chip for example is there and that makes sense because we need 10 of them, okay? Cuz we've got 10 pins here, 10 chip selects and we've got 10 chips total. So, it's almost as if like the chip

**Dave Jones:** select for this one is shorting to the chip select for this one. Yeah, so we've got CS21 here. And that'll be This will be CS2 6. Yes, so okay, it matches the M1 M2. So, yeah, we're looking at that line

**Dave Jones:** there and that one there. That's what's happening. Uh so, I you know, like it's not like those two lines. I can't see how they're going to be shorted or whatever, but it could be something as simple as like an

**Dave Jones:** open line somewhere in and then it's getting crosstalk from the other lines. So, yeah, I look, you know, you can analyze this until the cows come home. You have a bunch of hypotheses and you just go in and check them all out. So,

**Dave Jones:** let's open this sucker up and I'd just start with just probing around here for example and just seeing hopefully we can probe get access to the chips. Haven't taken apart yet. Get access to the chips and probe them while we're actually

**Dave Jones:** using the thing. Otherwise, you know, you got to like soldering mod wires to get test signals out and things like that. You know, but first of all, open up, give it a bit of a visual inspection and then yeah, we'll get

**Dave Jones:** probing. Anyway, there's our suspect up there, M1. So, what I'm going to do is I'm going to have a get that under the microscope and have a good look at it. Do the visuals looking for any, you know, dodgy solder joints, any hairline

**Dave Jones:** cracks, any bridges caused by tin whiskers for example, which you know, a growth over time. They can grow out and short out pins and stuff like that. Yeah, just generally have a squeeze. You can just really see it quite clearly

**Dave Jones:** here how it just duplicates. Let's go to the next line. Look, let's shift that up. Check this out. I wonder why they've exposed the solder mask along there. Just a little slither there, there, there. It's interesting they've done it on

**Dave Jones:** every chip. Like this one at the top here, it's got it on all four sides. Look at that. You'll also notice on the board here how they've got all these traces running off the edge of the board like this up here. They've got up here

**Dave Jones:** like this. They're just buggering off over here. One of the column drivers over here just goes off the uh even down these signals down here. Why are they doing that? Well, that's probably for some sort of uh production panel testing

**Dave Jones:** would be uh my guess and then they um shear the things off, they route them off uh later. All right, let's have a look. M1, that all looks pretty schmick. I haven't seen any tin whiskers or shorts or anything. Might want to go

**Dave Jones:** over this. See if there's any bad solder joints. Like as in physically not soldered. See if I can move any of these pins. They're all looking pretty good. Nothing's loosey-goosey there. Really is no issue. There whatsoever. I mean, it could

**Dave Jones:** certainly be the chip. Like I I would not rule out the chip. Hang on for a second. I was just looking for a place to probe and I was looking at the pins I'm interested in down here and I see a

**Dave Jones:** little dag. Hello, Mr. Dag. I'm going to I'm actually going to measure between these two pins and see what's what. Can't be that easy, surely. Those two pin Oh, no. No, 125 ohms. My meter's beeping at 125 ohms. I'm

**Dave Jones:** going to get rid of that dag. No, it's still 125 ohms. I think that's a nothing burger, but jeez, that was that was coincidental. Okay, it's probing time. What I did is I just soldered a uh little uh 0.1 in header pin onto uh the ground

**Dave Jones:** pin there, which is uh pin five and pin six is ground. So, that just allows me There was no other like convenient uh ground point, unfortunately. And I'll include the schematic here. So, what we're looking at, we want to probe the

**Dave Jones:** chip select pins. Um, that's like definitely the first port of call. So, we're talking pins 16, 15, 14, CS21, pin 14. That's the culprit that we actually want, right there. So, pin 12, 10, eight. So, you know, there's a whole

**Dave Jones:** bunch of They'll be on this side of the connector over here. So, it's working. It's powered up. So, 2 4 6 8. Wasn't one of them pin eight? I think. There we go. We're getting bus activity, 5 volts. And

**Dave Jones:** Yep. Yeah, if I press the like just pressing the enter key. 10's 10's doing nothing. Okay, with Oh, no. No, sorry. I just wasn't probing it properly. You got to get through. You might have some flux on the pins or

**Dave Jones:** whatever. Always some good to have sharp pointed probes to get through. If you ever That's a tip. Like ever have like if you're signal's missing or something like that and you think, "Oh, there this should be a signal there. What's going

**Dave Jones:** on?" Don't chase that red herring down a rabbit hole. Just check that you're actually piercing the like any flux or any other contaminant on the joint that you've got a nice sharp pin. That's number 12. Yeah, it's all these chip selects. They're all

**Dave Jones:** working. Now, 14. This is the bad boy. Hello. Hello. Hello. Number 14. Let me Yeah, I'll push really hard on that. Yep, number 14. Let's go to 16. Yeah, 16's there. Bingo. Winner, winner, chicken dinner. We found it.

**Dave Jones:** Exactly as I suspected. Yep, pin 14 there, CS21, which drives our M1 chip, which drives the quadrant up here, which is the chip select for this chip up here. So, obviously, it's now the chip select on this one here is just flapping

**Dave Jones:** around in the breeze. It's just floating. So, it's picking up cross-talk from basically everywhere else. So, that's why it's like latching in the same data. You know, it's because it's a common data bus among them. So, they're all

**Dave Jones:** getting the same data. So, there's no wonder that this this chip is shifting in the same data as you're typing in over here somewhere, for example. So, it's yeah, the chip select is just, you know, it's been enabled. I think the

**Dave Jones:** Yeah, the read write will be all the same. They'll all be the same, right? So, it's writing the data. It's only the chip select that makes a difference between these chips. And this sucker is floating. So, that means our fault is

**Dave Jones:** actually on this board. Or it could actually be on the ribbon cable. It could have like a broken ribbon cable or something like that. Yeah, it may not be electrical fault at all. It may be mechanical job. Or it could have a bad

**Dave Jones:** contact on the ribbon cable. The first thing you do is just reseat the ribbon cable on both ends. Okay, those contacts look pretty shiny. No wackers there. Let's plug it back in. Nope, same problem. It's not that. It looks like

**Dave Jones:** the drive side or the other side of that connector. So, unfortunately, this ribbon cable goes through the board here. So, I'll have to take out the entire board. Well, not unfortunately, means we get to look at the other side.

**Dave Jones:** There you have it. There's the rest of the board. Yeah, it's still all through-hole jobs, mostly. Although, we do have some surface mount. I don't think the previous version had any surface mount apart from the LCD, did it? But I could be wrong. Anyway, yeah,

**Dave Jones:** there's all our modem stuff out there. There's our isolation transformer for our modem. And the 8085 made by Oki in Japan. All the best stuff made in Japan. 81C55 is down here. And there, that chip contains Bill Gates himself. Copyright

**Dave Jones:** 1983 Microsoft. So, yeah, that's the the ROM is soldered in. Hmm. Let's measure our backup battery there. Sorry, you can't see it. 3.42 volts. That's still pretty good. And again, there doesn't no to be any corrosion on the contacts at all.

**Dave Jones:** Nothing doing there. Plug that back in. And I've re-seated that and nope, same old same old. So, you know, good thing about this is you can actually get this right out and work on the bench. I mean, look, we can actually it's actually

**Dave Jones:** better to work on it now on the front of the board like this because we can just have our LCD just facing up. Fantastic. Oh, that is probing heaven. Beautiful. Beautiful. Good thing is is that we can actually

**Dave Jones:** probe the top of this connector cuz the even numbered pins actually come out over here. So, let's go pin 14 again. 14. Ta-da! There it is. Same problem. All right, so it's not the cable at all. It's not the the ribbon cable or the

**Dave Jones:** connectors or anything to do with the LCD. It is definitely coming from driver on the circuitry. Although, haven't inspected the solder joint. Now, hang on. Check this out. Pin two, four, six, eight, 10, 12, 14. That trace going through there, what is

**Dave Jones:** that? Gouge taken There is no way that is a coincidence. Is that some sort of like gouge, chunk taken out of there? That's That's way too much of a coincidence that it's there. I'm going to get that under the

**Dave Jones:** microscope. There's no way that's a coincidence. Has that been reworked? Hmm, I don't know. But look, come on. That's not a coincidence, is it? That looks black. That looks like it's rotted away or something. Am I wrong? That looks dodgy as. Let me

**Dave Jones:** buzz it. Hang on. I'll see if I can get Yeah. Yeah. Yeah, there we go. That side. Right? But it won't go over to here. Yep. Here you go. Winner winner chicken dinner. Found it. It's a track. Wow, wouldn't have bet on

**Dave Jones:** that. A track on the main board that's somehow like corroded away. I don't know. And the chips, you tell me, has that been I'm looking at it like the other chips on here, they don't have the same flux

**Dave Jones:** residue on them. I reckon this is probably had a repair done to it. Just looking at some of the other chips there, you know, these don't have any of that cuz this is all wave uh soldered. That's why it's got the

**Dave Jones:** glue. Although, that one still does have the glue under it. Look. So, not sure what the deal is. Yeah, it's actually corroded away. Let me clean that up. I'm not entirely sure how. I I have to lift my microscope up

**Dave Jones:** here because um it's designed for like cuz the board's too high. So, at at extreme zooms like this, but look at that. Yeah. Yeah, it's some sort of corrosion that's got into that and that's eaten through that poor little track.

**Dave Jones:** That was it. I found it. By pretty good deduction there. That was one of our hypotheses that uh the chip select was flapping around in the breeze, maybe. It was just getting cross talk from something else. And that turned out to be the case. So,

**Dave Jones:** yeah, all I got to do is fix that. Should be as good as new. Let's just scrape away some of the solder mask on the pad there. And this is post editing Dave here. Yeah, my capture froze. Um I'm going to

**Dave Jones:** like uh probably replace that with a um hardware capture solution soon, like dedicated hardware, like a uh Blackmagic's ATEM, probably. Anyway, little jumper Yes, we have a winner. Winner, winner, chicken dinner. Here it is. No worries. Basic, January 1st, 1900.

**Dave Jones:** Uh yeah, Y2K bug. Um yeah, didn't end the world though. Trust me, that was a thing. Those who remember the Y2K bug, oh jeez, I can Yeah, I was the Y2K engineer at uh Was it Tally's or Cellnet? No, it was

**Dave Jones:** probably Tally's Australia at the time. And you I had to go around and certify that everything I'm talking every little piece and project that contained a microcontroller or anything that had no real-time clock in it. I would still have to

**Dave Jones:** write a report certifying that it was Y2K compatible. Anyway, basic tada TRS-80 Model 100 software copyright 1990 cuz you want to save a few characters. Every character was precious. In 1983, Microsoft Bill Gates himself might have written that.

**Dave Jones:** 29,382 bytes free. Done. Fantastic. Winner winner chicken dinner. Hope you like that repair video. If you did, give it a big thumbs up and as always you can discuss down below and catch me on Odyssey and all the other

**Dave Jones:** platforms. You know what to do. Catch you next time.
