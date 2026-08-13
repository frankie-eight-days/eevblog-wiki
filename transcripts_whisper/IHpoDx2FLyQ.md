---
video_id: IHpoDx2FLyQ
title: EEVblog #612 - Mailbag
url: https://www.youtube.com/watch?v=IHpoDx2FLyQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 53, "4": 70, "5": 86, "6": 106, "7": 122, "8": 134, "9": 147, "10": 167, "11": 183, "12": 207, "13": 223, "14": 239, "15": 255, "16": 275, "17": 300, "18": 320, "19": 340, "20": 364, "21": 381, "22": 397, "23": 413, "24": 433, "25": 449, "26": 469, "27": 486, "28": 502, "29": 522, "30": 538, "31": 554, "32": 570, "33": 591, "34": 611, "35": 631, "36": 643, "37": 663, "38": 679, "39": 704, "40": 724, "41": 749, "42": 761, "43": 781, "44": 801, "45": 821, "46": 841, "47": 858, "48": 874, "49": 890, "50": 902, "51": 918, "52": 943, "53": 963, "54": 983, "55": 999, "56": 1020, "57": 1044, "58": 1060, "59": 1084, "60": 1101, "61": 1113, "62": 1133, "63": 1153, "64": 1174, "65": 1190, "66": 1211, "67": 1231, "68": 1251, "69": 1271, "70": 1288, "71": 1304, "72": 1324, "73": 1336, "74": 1356, "75": 1377, "76": 1397, "77": 1421, "78": 1437, "79": 1462, "80": 1486, "81": 1511, "82": 1531, "83": 1548, "84": 1560, "85": 1576}
---

**Dave Jones:** Hi, welcome to Mailbag Monday. Yes, I'm in front of the camera this time. I thought I'd do something a little bit different, give you a very quick update. For those who don't follow along on the forum and follow me on Twitter either, where I often talk about this sort of stuff, I was

**Dave Jones:** looking at potentially moving out of my current lab space and getting another lab, but that sort of didn't happen. But what I'm getting here now is a lab upgrade in my current lab slash office here in terms of internet. So instead of my crappy ADSL 2 plus

**Dave Jones:** internet, which is like 900k bits per second upload speed or something, I will this week, hopefully, that's the plan, get an 8x8 symmetrical connection. So that's 8 megabits download, 8 megabits upload. So I'm losing a bit of download speed, but I'm gaining that valuable upload speed, which

**Dave Jones:** I need to upload my YouTube videos efficiently and also the faster speed will allow me to do some more live stream and real-time video stuff. So that should be fantastic. I'll link in down below a forum, a section on the forum where you can

**Dave Jones:** talk about that and I'm asking for ideas about what people want to see, what I can do with the new extra bandwidth. And I'm going to reorganize the lab here, going to put a little mechanical workshop maybe and some more shelving and stuff like that to make better use of the space I've got

**Dave Jones:** here. Anyway, that's just a very quick update. Oh, I will be going in assuming that internet, new internet connection works out, I will be going to a 20 slash 20 meg connection. So I'll eventually have 20 meg upload here, fiber coming into the building and then 20 meg ethernet coming into the lab

**Dave Jones:** here. Oh, fantastic. Can't wait. So I'll be no longer editing my videos at home, the plan is to remove all my editing video editing gear here and be more efficient in the lab here, the lab slash office and do my editing and upload here

**Dave Jones:** because this is where I'll have the fast internet connection. I've done it at home before because that's where I've had my fastest internet connection. The lab here has always been quite slow. So that's fantastic. So let's get on with the mailbag. First of all,

**Dave Jones:** it's a whole bunch of stuff. It's only been like two weeks and in it comes again. Unbelievable. Anyway, I missed a couple of postcards last time. And this one here comes from Marcus and he's in Austria and this is a photo in Salzburg, a stairway up to a castle.

**Dave Jones:** It was taken for those who want to know technically. Oh, I'm Foo! Hello! Love it. Foo. It was taken by a Zenith Horizon 35mm panorama camera. Thank you very much Marcus. Awesome. Next up we have one from Wayne. Good on you Wayne. Good Aussie name.

**Dave Jones:** Wayne, my brother-in-law and father-in-law are both named Wayne. There you go. He did a graduation trip around Taiwan. So there you go. Nice sunny day. Thank you very much. And this one's from David. G'day Dave. And he is in the room next to Wayne.

**Dave Jones:** Go figure. They obviously go to the same university. They're an information and computer engineering ICE student. They focus on human activities recording with embedded systems. Excellent. And this one is Taroko National Park in eastern Taiwan. Awesome. Thanks guys. And next up we have one from Trey.

**Dave Jones:** G'day Trey. He's studying EE in Louisiana Tech University. Awesome. There you go. Some local Louisiana trees. Beautiful. In a park somewhere. There you go. That's all for the postcards. Thank you very much guys. Let's get on to the mailbags. Quite a few of them.

**Dave Jones:** First up we have one from Ocean Controls here in Australia. And you've seen Ocean Controls on the blog before. They do various types of little embedded systems and other stuff. And I think I know what this is. And it's going to be fun.

**Dave Jones:** I like it. This will be state of the art, folks. And it's from Greg Radian. I won't spoil it for you on the top there, so let's just open it up. He sent a couple of things, but one of them is a real cracker.

**Dave Jones:** I love the design of this. Everyone's going to want one of these. Look at this. Let's open it up. And crack it open. What it is is an Arduino shield. You put it together like this somehow, and these go in there like that.

**Dave Jones:** It forms a spindle, and you put some tape in there, and it's a tape dispenser. Awesome! The best and most useful Arduino shield ever! Check it out. Now tell me, how is that not the most useful Arduino shield of all time? Fantastic. Unbelievable.

**Dave Jones:** Everyone needs to get one of these. A few little design issues with it. There's no snap-off here for the tape. And yes, it is, once it's all soldered in place, you can't get the tape out, so it's like a single-use roll. Eh, maybe the, you know, he'll get that right in the Mark 2 version, but

**Dave Jones:** everyone has to get one of these suckers. It makes your Arduino so incredibly useful. It's fantastic. And of course it only works with a genuine Arduino board because of the signal level compatibility on there, but fantastic. If you want one, go to Ocean Control's website, link down below.

**Dave Jones:** Awesome. Everyone needs one of these. And you know what I really like? A letter that's got line numbers on it. Fantastic. Thumbs up. And Greg's also include this little thermometer shield as well, and basically uses the MAX31 855, and as he says, I've done other videos on this, it uses a linear approximation

**Dave Jones:** for the thermocouple voltage and also the cold junction. It's got, it does have cold junction compensation on, and I'll link in my temperature tutorial, thermocouple tutorial video down below if you haven't seen how these things work. Anyway, it's inside the chip instead of right at

**Dave Jones:** the junction itself. But it's only a centimeter or two away, and it's generally okay. It certainly is not as accurate as a precision circle with a NIST lookup, but for low cost per channel, it's good enough. So excellent, thank you very much Greg, that looks very

**Dave Jones:** nice indeed. Got a little prototyping area there as well. If somebody wants this, I think I will give this one away. So first person to leave their details in the YouTube comments or, well, anyway, yeah, let's make it the YouTube comments. First person to leave a comment in there gets it.

**Dave Jones:** And of course that is for a standard K-type thermocouple, which you can get for a dime a dozen on eBay. So that one looks very useful. 8 channel thermocouple, fantastic. You could do some neat temperature logging with that. Oh, and the specs for those playing along at home, 14 bit

**Dave Jones:** resolution 0.25, that translates to 0.25 degrees C over a couple hundred degree range, very nice. Nominal plus minus 2% accuracy, that's all you're going to get on the cheap thermocouples anyway. So that's terrific. And he does say there's a duct tape version coming soon, incredibly useful.

**Dave Jones:** You think the electrical tape one's great, but anyway, look at this documentation, quite thorough. How to assemble this Arduino tape dispenser. Terrific. And it can support two reels wide. Oh, red and black, fantastic work. Everyone should get one. Looks like we've got an Aussie

**Dave Jones:** fest. This one's from Vitibus, Michael Costello. He's in Blackburn South in Victoria. Thank you very much Michael. Let's crack this sucker open. Oh, there's a remote control. Strong. Oh, it's a set-top box. I used to have a strong set-top box. And I think it failed, did it?

**Dave Jones:** Yeah, they all fail. Hang on. Here we go. This strong S.2 seems to have died for submarine and thought it sent it to you for a tear-down. If you wish, thank you very much Michael. It will most likely be the caps in the

**Dave Jones:** thing. Defective. Yeah, crack it open. As you can see, there's not much in these things at all. They're really built down to a prize. And at first glance, that looks quite well designed and laid out. They've got the heatsink well and truly stuck onto the

**Dave Jones:** main chip down in there. Yeah, these set-top boxes, not much in them. There's a little crappy tuner down in there. And just one main chip handling everything. Got some memory coupled onto that. Main's power supply around here. Not a huge amount happening, they're doing the right things.

**Dave Jones:** They've at least got a PCB mount fuse down there, even if it is vertical ended up like that. And well, yeah, a couple of isolation slots and the opto-coupler going between there and there. Yeah, they've got the basics happening. So anyway, it's good enough for the price.

**Dave Jones:** And while these things fail, I don't know how hot this one gets. Probably not a huge amount. No bulges in the caps there that I can see. But yeah, I'm not going to troubleshoot this thing obviously. But yeah, no bulges in any of those caps.

**Dave Jones:** It's more likely to be the mains, the high-side mains here than the just all the secondary side over here. Although it could be some of these low ESR output caps here, because they will, because it's a switch-mode power supply, if you're getting a

**Dave Jones:** reasonably high current out of here, then there's power dissipating inside the ESR inside these two. Presumably, low ESR caps. Are they? I don't know. Are they labelled as such? Anyway, they should be. Usually in a switch-mode power supply. Yeah, low ESR. It says low ESR down in there, you probably can't see it.

**Dave Jones:** But there you go. So yeah, they heat up due to the internal ESR. And then the internal heating just makes the electrolyte dry out more, which then increases the ESR, and it's sort of a snowball in effect. And your good quality caps, you know, you'll get your 10,000 hours or something, it depends on how you

**Dave Jones:** rate them in your circuit. But the crap ones, whatever brand, crappy brand they throw in here this week in this particular brand, I don't know, could be gone. But typically you might see a bulge in there or something, but I'd need to get my ESR meter on that.

**Dave Jones:** But anyway, that's not too horrible at all. I think that's quite neat and tidy. And yeah, there's nothing on these things, there's just tuner HDMI out, and for all of the, well, it's got components I was going to say legacy stuff, there is, they've just got your audio and

**Dave Jones:** composite video down there, but gee, yeah. It's a set-top box. Meh. I've had these fail. Dime a dozen. And this one is from Her Majesty's Royal Mail. Oh, when's she going to cark it? How old is she? Geez, unbelievable. I don't know. It is from Boldport.

**Dave Jones:** There you go. I haven't offhand, I don't, can't recall. It is, yeah, no name on that, but it's from Cambridge. So let's crack this sucker open and see what we've got. No idea. Interesting. We've got some cardboard happening here, and what else? We've got a note.

**Dave Jones:** Don't want to read the note. It's a corkwood puzzle. Corkwood puzzle. Rejected. Assembly guide missing. Awesome. So we can assemble a puzzle. I, hang on, looks like we have some sort of signage. Oh, look at that. PC, is that, yeah, that's etched PCB

**Dave Jones:** with an acrylic, wedged between an acrylic. I am an engineer superhero. Fuck yeah. Awesome. Brilliant. Thank you very much to Dave Jones. There you go. Terrific. Superhero, second edition, red, 41 of 50, limited edition. Oh, that's terrific. I love it. That's beautiful. It's a coaster of course.

**Dave Jones:** It's a, yep, it's designed to, oh, well no, you'd have to put the rubber feet on the bottom to make it a decent, decent coaster to put your stubby down on there, but there you go. Beautiful. And the guilty party, there he is, SAR.

**Dave Jones:** G'day SAR trimmer. Oh, my face detect has automatically detected your face on the camera. I can't show it here, but it, yeah, it's following your, the little focus thing is following your head around. So there you go, can even recognize your little hand-drawn, cartoony-drawn thing.

**Dave Jones:** Terrific. Now this corkwood puzzle thing is interesting. Inside we have a bag of massive through-hole resistors there, a couple of watts, a couple of huge big 10mm LEDs, and a couple of trannies in there. And let's rip this open. And ah, here we go.

**Dave Jones:** There we go. I don't know what the corkwood thing is, I don't understand that. Ooh, got a taper on that. Ooh, look at that. Sexy little curves on that. Look at that. That's actually quite neat. I'm not sure what it's going to be doing

**Dave Jones:** unless they're little, you know, special LED flasher TO-92s or something like that, I'm not sure what it's going to be doing. Hmm. Check out the layout, it's all squiggly lines. Trademark, squiggly trace, trademark. There you go, fantastic. I'm not sure why, to add to the puzzle feel, I guess.

**Dave Jones:** Ah, here you go, it makes sense. Look, check it out. You use the two boards like that with the components going between them. And he explains, in the 60s and 70s, inventive engineers saved space by using the corkwood assembly. I had no idea it was called

**Dave Jones:** that. There you go. Learn something new every day. Where components were sandwiched between the two circuit boards, this construction became less useful. We've reduced component sizes, yeah, PCB manufacturing, and all the integration we take for granted. These days, but yes, you look inside old radios and things like that, you will find

**Dave Jones:** this multiple board construction like that, even old printers and stuff like that. It was fairly common back in the day. Oh, it wouldn't be like it'd be early 70s, it wouldn't be late 70s or anything like that. Yeah, that puzzle is a tribute to the construction engineers

**Dave Jones:** that came up with it. The puzzle is to correctly assemble a circuit with the components at hand. Once assembled, all LEDs light up when power is applied. Excellent. There you go. So yeah, the transistors probably work as little switches as part of the puzzle.

**Dave Jones:** Or something like that. Terrific, awesome work. Thank you very much, sir. And he's got a blog and a shop as well where you can buy stuff. Check it out. And what's inside the tiny engineer superhero emergency kit? Contents, PCB, two resistors, one LED,

**Dave Jones:** one capacitor, one FET, and soldering sponges. All you need for adults. More info at... terrific. Let's crack it open. Oh, look at that! Oh, engineer superhero specific sponge! Great! Ah, awesome! Love sponges. And look at that, nice gold, sexy gold-plated board. All it looks like, yeah, once again,

**Dave Jones:** that puzzle. Hey, vehicles IR, check it out. I like it. Terrific. And it looks like you solder the parts in there in line, embedded with the board. That's really quite neat. Thanks very much, sir. That is really interesting. But the most interesting thing is, here we go,

**Dave Jones:** all of my circuits are designed with PCB mod E, is it? An open source software that has written himself in Python. Unbelievable! Massive props for that. Awesome. Thanks, sir. Next up we have one from Jacob Filipowiczka, I'm pronouncing that incorrectly, and I assume it is

**Dave Jones:** yeah, last name slash first name, from Poland. Thank you very much, we don't get many from Poland. So let's crack this sucker open. And I have blanked out what's in it, because I got a few complaints that, oh, I was like reading what's on the

**Dave Jones:** outside of the package, and it was the customs form, and it was given it away. Okay, fair call. I do appreciate that half the coolness of this video. There's a letter in there, but let's have a look first. Is, ooh! Ta-da! It is something that I love.

**Dave Jones:** It is something that I love, old calculator! Look at that polish! I presume it's polish, because I can't read that. A Mark 61 polish calculator. It looks like it's got a fluorescent seven segment display. Ooh! Oh, look! Check it out! We have an original schematic!

**Dave Jones:** Oh! No way! Look at that! Who gives the schematic for their calculator? That is just awesome! Hi Dave, rumour has it I like vintage calculators, yeah, just a bit. So I got one for you, 1994 vintage. I thought it would have been older than that.

**Dave Jones:** Working mint condition Electronica Mark 61. This beauty was designed in 1984 in the USSR. That's more like it. Back in the USSR. No, I won't sing it. I can't sing. It's programmable with 105 steps of memory, 15 registered users, RPM, of course it does, and it's as slow as a dying cow.

**Dave Jones:** Dying cows die slowly, I guess. I have no idea how to program this properly, but apparently people write games through it. Awesome. Well, you know, you've got to have a hobby. Have fun tearing it apart, but you're permitted to also turn on, there's something I want you to, I'm working on an emulator, an old late polish mini-computer

**Dave Jones:** Mira 400 in the mid-90s. I was able to secure tons of documentation. Awesome. Make that available online, because I don't have access to a working machine. It was the main source of knowledge for getting the emulator to work. And I finally boot the operating system now.

**Dave Jones:** Awesome work. A lot of effort goes into that. Thumbs up. What amazes me and what I wanted to share with you is how detailed the documentation was. It's insane. Yes, I'm oh, hang on, there. Oh, okay, that's for the documentation with this calculator is fantastic, let alone the documentation for an old computer.

**Dave Jones:** I can imagine. So I'll put this link in down below so people can check it out. It was part of the end-user documentation back in the 70s. Great. Awesome. Thank you very much Jacob Filipowicz. I love the manual. Oh man, I can't make heads or tails out of this.

**Dave Jones:** But yeah, there's the date, 94. Yeah, fair enough. And terrific stuff. And here we go, I put some batteries in this electronic Mark 61, and well, yeah, because I wouldn't have been able to read that, so I'm glad you told me. And here we go,

**Dave Jones:** will it work? And it works! It's alive! Ah, there we go, we've got pi to 2, 4, 6, 7 decimal places there. Terrific. And then where's our exponent on this thing? Oh goodness, I Yeah, I, you know, there's some stuff you recognise on there.

**Dave Jones:** All the numbers are the same in some of the mathematical stuff, some of the other stuff, meh. Check out the original pouch. Oh, that's just gold. It really is. Oh! And the screw hole actually had some gunk in there, it was actually gunked up.

**Dave Jones:** Not like, it was plugged, but oh man. Unbelievable. Anyway, it's a flat head. So let's whip this sucker open, see what we've got inside. A self-tapper. And obviously I've got to pry open the side of the case. Now that is interesting, check that out.

**Dave Jones:** Of course, no solder mask on this sucker, just tin plate traces. They've got this secondary board here, which is just held on, directly soldered in there. So I'm not sure what's going on with that. It's almost like it's an afterthought. And look at these interestingly

**Dave Jones:** potted chips here, like surface mount. I'm going to get a close-up of that. Now that is fascinating. Not sure I've ever seen anything like that. Is that hard? No, it's gunked. Okay, no, so that's not a hard potting, so is that like a bare

**Dave Jones:** die, is that like a flip chip down and then reflowed maybe with bumps on the bottom to reflow down onto the bottom like a BGA type part? Or are there little bond wires they've got going? I can't see anything going off. So, or maybe it's a, you know,

**Dave Jones:** an LCC type package with, well I can't even see any like castellations on the side or anything like that to solder it down. So I don't want to destroy it and dig into that, but that is fascinating. Never seen anything like that before.

**Dave Jones:** Ah no, here's what's going on. Look at this, they've got a little, like a, you know, a flex PCB, so it's bare die on flex PCB like that, and then the flex PCB is soldered onto like the same pad for like an SO

**Dave Jones:** package. Very interesting. So they've got that for that one and the one under there. Presumably it's the same for these as well. Presumably it's the same for these and we just can't see it, they've, you know, the mounted on the, oh yeah, there it is.

**Dave Jones:** Yeah, I can see the membrane under those ones. There we go. There we go, just didn't see it on that bottom one there. Eh, got something hanging off there? What's that strand? I don't know. But that, that is fascinating. And that is the crusty old switch mechanism.

**Dave Jones:** Oh goodness. So this lift-up module here, probably some sort of oscillator, did give away as the adjustment pot on the top here, plus you know, just a bunch of through-hole parts on there with some sort of clip-on plastic cover. So let's get that off and see what's under.

**Dave Jones:** Yeah, there we go. Look at that. That's like, you know, some sort of voltage regulator. Is it charging? Did it use rechargeable batteries or something like that? And the trim pot could be, well, it may not be an oscillator, I don't know. But yeah, that is, that is

**Dave Jones:** weird. Jeez, look at that, just tacked on with its own plastic cover. Weird. And even funnier is this old mains adapter plug pack for it. Oh, my god, how crusty is that? It feels just awful. It really does. It's got some little piss ant cable on there

**Dave Jones:** with some sort of custom connector. Oh, it's just awful. And even though I can't read a word of this, of course you can, the universal language is electronics, we can read that. And it looks like we got ourselves that module in there was a DC to DC converter.

**Dave Jones:** Check it out, on the separate board. And it's powering the chips over here, not exactly sure what they're doing. Hmm. Ah, there we go, we've got ourselves a RC oscillator on there, I guess. So is that generating multiple phase clocks or something? I don't know.

**Dave Jones:** Hmm. This schematic's got it all. Look at these, they've got all these waveforms in here. Fantastic notes, timing diagrams, brilliant. For those at home who can read that, go for your life. But absolutely thorough documentation, unbelievable. Look, there's the individual chip pinouts there.

**Dave Jones:** Absolutely terrific. I love it, pinout of the display. Oh, man. Thing of beauty and a joy forever. So thank you very much, Jacob, for that interesting look at a Soviet Polish Electronica Mark 61 calculator from the 80s, even though it was manufactured in 94.

**Dave Jones:** So they kept manufacturing it, I guess. I don't know, I wonder when it stopped, but geez, that is fascinating. And it doesn't feel, listen to that creak. Oh, that is just, that's screwed together, folks. And that is just awful. But fascinating construction inside.

**Dave Jones:** Thank you very much, Jacob. And that's all we've got for the mailbag this week. I do actually have like three more items, but I'm going to call it quits today, I think the video's already long enough. And I've got yet more microcurrents to ship this afternoon,

**Dave Jones:** so I'd better get to it. In fact, it's, eh, there it is, 2.30pm on a Monday, so I've got to pack and ship another 100 microcurrents and maybe I can get that done before peak hour hits. I've got to drive off to the mailing depot.

**Dave Jones:** So I hope you enjoyed Mailbag, and if you want to discuss it, jump on over to the EEVblog forum, the link is down below. Although you can leave comments on YouTube or the blog website as well, and I do read them all and I try and

**Dave Jones:** respond to as many as I possibly can. Hope you enjoyed it. Catch you next time. Go to Beadaholique.com for all of your beading supply needs!
