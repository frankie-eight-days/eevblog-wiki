---
video_id: aVNfFewFn_Y
title: EEVblog #591 - Agilent 54622D Retro Mixed Signal Osciloscope Review & Teardown
url: https://www.youtube.com/watch?v=aVNfFewFn_Y
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 38, "3": 55, "4": 71, "5": 87, "6": 102, "7": 116, "8": 130, "9": 144, "10": 158, "11": 173, "12": 189, "13": 202, "14": 219, "15": 231, "16": 248, "17": 262, "18": 274, "19": 288, "20": 300, "21": 321, "22": 335, "23": 349, "24": 364, "25": 379, "26": 403, "27": 418, "28": 434, "29": 450, "30": 464, "31": 476, "32": 488, "33": 501, "34": 516, "35": 529, "36": 547, "37": 566, "38": 581, "39": 594, "40": 606, "41": 621, "42": 635, "43": 651, "44": 667, "45": 684, "46": 698, "47": 712, "48": 729, "49": 743, "50": 757, "51": 774, "52": 788, "53": 802, "54": 820, "55": 834, "56": 850, "57": 869, "58": 888, "59": 902, "60": 919, "61": 935, "62": 948, "63": 960, "64": 979, "65": 991, "66": 1008, "67": 1025, "68": 1042, "69": 1055, "70": 1073, "71": 1086, "72": 1100, "73": 1114, "74": 1128, "75": 1141, "76": 1156, "77": 1173, "78": 1187, "79": 1199, "80": 1214, "81": 1223, "82": 1236, "83": 1249, "84": 1266, "85": 1280, "86": 1295, "87": 1310, "88": 1325, "89": 1341, "90": 1354, "91": 1365, "92": 1383, "93": 1397, "94": 1409, "95": 1424, "96": 1436, "97": 1450, "98": 1465, "99": 1474, "100": 1489, "101": 1506, "102": 1523, "103": 1546, "104": 1560, "105": 1576, "106": 1589, "107": 1604, "108": 1617, "109": 1632, "110": 1646, "111": 1660, "112": 1673, "113": 1685, "114": 1697, "115": 1711, "116": 1723, "117": 1739, "118": 1752, "119": 1764, "120": 1778}
---

**Dave Jones:** Hi. Yes, it's vintage oscilloscope time cuz I love oscilloscopes and in particular I love this one, the 54622D Agilent and well, it was Hewlett-Packard back in the day before they changed their name to Agilent. Now they changed their name to bloody Keysight

**Dave Jones:** Technologies. Ah, ridiculous. Anyway, this is like a early 2000s vintage. I believe it came out in 2000 originally for the 546 100 series. Now there is an earlier one to this which is the 54645D and they are significantly different

**Dave Jones:** looking. This one is more modern looking with the round style buttons and the rubber buttons. The other one, the 645D, very similar scope in terms of layout architecture and specs and everything with the mixed signal option, but it had the old style square HP

**Dave Jones:** buttons. This is before they, you know, revamped the interface and went like this and I love this scope. I used this extensively at companies I worked at back in the early 2000s and I'd always specify it in. It was a nice compact

**Dave Jones:** scope like this and really it was pretty much state of the art for its time and it basically still holds up today. I mean, yeah, it's a 100 MHz bandwidth. This series actually went up to 500 MHz and it is only 200 meg

**Dave Jones:** samples per second, but that could double based on a single channel. It was four meg points of memory. I think it was optional eight meg points which was absolutely huge back in its day to get a mixed signal scope with that sort of

**Dave Jones:** deep memory and also and that's four meg per channel as well. You could actually interleave that and get eight meg on a single channel. It was absolutely phenomenal back in its day and it used the megazoom Uh, technology. I believe

**Dave Jones:** it was the I believe it was Megazoom two at the time and you're probably familiar with the modern Agilent uh, 3000 2000 3000 X series scopes. They use the Megazoom four technology. This is the older Megazoom technology and this was

**Dave Jones:** marketed to the hilt back in the day and it was extremely popular scope and still holds up today. I I don't know anyone who does not like who's used this and does not like this scope. It is just absolutely brilliant.

**Dave Jones:** sine X on X interpolation, so you could easily get 50 MHz uh, bandwidth out of that. A 32 intensity uh, gray scale screen. Yes, it is only a green screen, but it was true mixed signal, so you'd have the

**Dave Jones:** 16 channel logic analyzer as well. Fantastic. You could configure all that. You could trigger it. It had I squared C triggering in here. Here it is. Where is it? More I squared C triggering. It could do SPI and TV and pulse width

**Dave Jones:** triggering and pattern triggering and all sorts of weird and wonderful stuff. It was pretty much state-of-the-art and I loved the interface for this. It was so easy. Dedicated vertical controls, horizontal that just worked as you'd expect. Simple uh, acquire menus had

**Dave Jones:** real-time mode or there it is. There's uh, most of the time you operated the thing in real time, but maybe right up at the high end you might uh, do the equivalent time sampling, stuff like that. Of course, it had full uh,

**Dave Jones:** averaging. Um, what else have we got here? We've got uh, and it had vectors or dot mode. Now, the huge marketing claim for this thing was that it was 25 million vectors per second. Yes, not waveform updates per

**Dave Jones:** second as you're more familiar with these days in marketing terms, but vectors per second. Whatever the hell that meant. I don't think anyone really knew back then what it actually meant. It display vectors, there it is and it

**Dave Jones:** would basically, uh, those vectors joining the dots, so to speak, the sin(x)/x interpolation, it could do 25 million of those per second. But, I don't think Agilent ever sort of said or explained how that translates into real-world waveform

**Dave Jones:** updating and dead time and all that sort of stuff. But, man, it sounded impressive. Oh, 25 million vectors per second. Nobody else marketed their scopes like that. It was just fantastic. Ah. Anyway, I love this scope, and it's

**Dave Jones:** brilliant, and it's still quite usable today. So, I highly recommend, if you can pick one up cheaply, put it on your eBay watch list, and try and get one of these puppies. They are really good. Woven Electronics, I love it. Here you

**Dave Jones:** go, August 2000. I actually have the full 16-channel logic probes with this, with all the clips and everything. Fantastic. I've got one of the original manuals, I think. And, this one is in very good working condition. And, even

**Dave Jones:** though it was grayscale, one of the beautiful things about this is that the resolution of the screen, which is still not matched by most scopes today. Even you pay 10, 20,000 dollars for a scope, you don't get the resolution that's on

**Dave Jones:** this one. It's got a 1,000 horizontal pixel resolution on its CRT. Absolutely phenomenal. 1,000 pixels. Most of them don't do that. Had exactly 255 vertical pixels for the waveform, so that you didn't, you know, wasn't sort of interpreting anything or adding

**Dave Jones:** pixels or anything like that. So, beautiful, crisp, clear display when you zoomed out and you get all that 4 8 meg of detail in there. Fantastic screen on this thing. It really was. Fan was always a little bit noisy in it, which

**Dave Jones:** was a bit annoying. You can save all your stuff to a 3 1/2 inch floppy disk, of course. And, we'll check out the waveform intensity mode. And, yes, as I said, 32 uh or greenscale levels in there. So, we'll

**Dave Jones:** actually compare it with a modern scope and see if it's any good. But, I just love the way this thing operates. It was no fuss, well-laid out, very simple, basic, nothing to get in the way, and it just worked well. It was a beautiful

**Dave Jones:** scope to use on a day-to-day basis. And yes, this thing had an Easter egg as well. To get to it, a bit convoluted, press uh save recall, go into save, press new file, and then I love the entry mechanism on this. It just worked

**Dave Jones:** so smooth and so intuitively. Anyway, we go in there and we just go uh r o c k. See how quickly I'm entering that? Rock on, dude. Rock on, dude. Creating bitmaps. Woohoo! Here we go. Fantastic. Look at this. Welcome to

**Dave Jones:** Rocks. Channel one. Knob rotates the ship. Fire fire fires a missile. Thrust moves the ship. Fantastic. Asteroids-type game. Beautiful.

**Dave Jones:** Boom! I'm dead. Just look at the resolution they're able to get on this screen. It really is phenomenal. Top-notch. And you got to wonder why they were still using a CRT like this back in well, you know, 2000 when they were when

**Dave Jones:** they didn't design and first sold this thing. Well, it was that horizontal resolution. You just couldn't get the LCD to give you that thousand-point horizontal resolution that this thing has. Even as I said, uh even today, you're struggling to find a scope that's

**Dave Jones:** got better than, you know, that 800 by 600-type screen in it. This one's got a thousand points. Awesome. And the other thing is it boots up pretty quick for a digital scope. Check it out.

**Dave Jones:** Hear the floppy drive go, but bang, it's basically straight in. It took more time for the CRT to warm up than it did for the scope to boot. And of course that flicker on the screen you can see is not

**Dave Jones:** actually the screen happening there. That's just the shutter speed of my camera. In this case 25 frames per second, but I can increase that and it'll go away. Oops, sorry. I meant decrease cuz if I increase it I'm now at

**Dave Jones:** a shutter speed of 1/250th of a second and look at that, shocking. And at my maximum shutter speed of 1/2000th of a second, look what we get. But of course the screen is just fine. There's nothing wrong with it visually,

**Dave Jones:** but on the camera that's the effect you get. And here we have the old and the new side by side. Look at that. And well, this is you know, 14-15 years ago vintage and the new 3000X series here.

**Dave Jones:** And the good thing about this of course is that it has a trigger output so we can measure the waveform update speed based on the trigger speed. So I'm feeding in a 1 MHz signal here from the function gen and there it is on the

**Dave Jones:** screen and we can read off the output frequency. Now of course this was advertised 25 million vectors per second which sounds fantastic. So what does that actually give us in terms of update speed? Well, not much by modern

**Dave Jones:** standards. Look at this, 520 Hz. That's bugger all. And actually if I change the that's at 5 nanoseconds per division. So that's the fastest time base. I increase it and it doesn't drop down until uh it's it's dropped down a fraction there.

**Dave Jones:** There we go, 10 microseconds and it's starting to starting to jump around there. But there we go. Now going down until we get to there and we've got to adjust it, and we're down to, you know, that's at 500 microseconds

**Dave Jones:** per division, we're down to like 120 odd hertz. And of course, with our deep memory, which was a big feature in the day, 1 millisecond per division, we can stop our sampling there, and we can zoom right in on that, no problems

**Dave Jones:** whatsoever. Beautiful. That was a killer feature back in the day. Now, here's an interesting aspect. We've got the trigger output here, and you can see we've got our trigger jitter in there. There's actually a fair amount of that,

**Dave Jones:** presumably because it's got uh you know, it's got to do some interruptions stuff like that. Um it's not, you know, like a fixed pulse output. So, presumably that is the processing time that this scope takes to process the waveform after it

**Dave Jones:** actually uh captures it. And you can see if I change the time base like all the way up to maximum 5 nanoseconds per division, as I said before, I have to go right down to what is it? 500 microseconds per

**Dave Jones:** division before we see that uh pulse width change. And it was 1 microsecond before, now it's 585. So, if we jump back, there it is, 1 microsecond. And you can actually see a bit of variability in this if we

**Dave Jones:** uh let's have a look. Change Move some of the controls. Look. See how it slows down if I move the horizontal time base like that, you can see that it's got to process that, and you can see the slower updating rate of that

**Dave Jones:** screen. So, the the waveforms per second is slower updating, so that we're seeing, well, effectively less jitter on there cuz it's not updating nearly as fast. So, you'll see that if we go in here, here's our update Well, let's let let's go right in here

**Dave Jones:** like this, shall we? Let's go in right in there like that, and you can see that if we change that boom, that control causes the horizontal of the the update rate, sorry, to drastically slow down. There we go.

**Dave Jones:** And you can also see a difference. We're in real-time mode at the moment, and we're getting that pulse width there, the positive pulse width about 1.4 microseconds or thereabouts. But if you switch real-time mode off here, bingo, look at that.

**Dave Jones:** It's extended all the way out to 17 microseconds, and then that changes with each time base setting when we're in equivalent sampling mode, and you can see that's equivalent sampling and not actually real-time updating there. And just like the modern Agilent scopes, no,

**Dave Jones:** this one doesn't slow down when you do measurements. Like I add the measurements on there, and you can see there's no difference in the waveform update speed at all. Well, it's I don't know where the 500-and-something hertz has gone. It's now 367. So, I'm not sure

**Dave Jones:** what I've I've changed since then, but it makes uh makes no difference. We're getting 500 hertz before, weren't we? And way, I can turn on cursors, and I can move the cursors around, and look, it's not changing any of that user interaction on

**Dave Jones:** the screen is not changing any of that update rate at all. So, it's only when you do like the horizontal stuff, which is what which is operating on the memory, like, you know, actually the display part of the acquisition system, that it

**Dave Jones:** changes. But anything to do with the cursors or measurements or anything like that or other menus and operating the vertical time base and all that sort of a vertical time base. Duh. Um vertical attenuator, then, you know, it

**Dave Jones:** it doesn't do anything at all. You can go into utility menus and play around and all that sort of stuff. Acquire menu. You can even turn averaging on, for example. Doesn't affect the update rate at all. There it is. Still 361

**Dave Jones:** hertz or 361 waveforms per second. So, it's like this is like on par with like a Rigol DS1052E in terms of waveform updates per second these days, but back then, you know, that marketing slogan, 25 million waveform vectors per second,

**Dave Jones:** that was a killer. And you can even do stuff like pulse width triggering, for example, and doesn't slow it down in the slightest. So, it was, you know, I never had any issues actually using this thing. It was just so fast in operation.

**Dave Jones:** All the controls are super responsive, and it just worked. It was a brilliant scope. Still is. And how does the intensity graded display, as I said, 32 green or gray scale levels compared to the modern 3000 series? Well, they both

**Dave Jones:** look pretty shitty at 100%. I've got my 1 MHz carrier frequency with the 1 kHz AM for 100% AM modulation here, but they're at 100% intensity. So, if you wind that down, we start getting our true analog-like display there. Here we go. Oh, no,

**Dave Jones:** intensity controls over here. Look at that. I reckon it's I reckon it's superior. I like the old-style one better. It really It really resembles an analog scope better than the 3000X series does. I mean, check it out. That's just, you know,

**Dave Jones:** that's like minimum now. I'm down at 0%, and look, you can see the real the higher intensity in the center there, and it's just a beautiful display. If you forget about the flicker, cuz this flicker doesn't happen in real life. We've got some

**Dave Jones:** trigger jitter there, by the way. It's not easy to trigger on this type of signal, but yeah, that is just That is brilliant. I like it. Very analog-like display. I reckon better than the 3000X series. And we can, of course, freeze that and

**Dave Jones:** zoom in to our heart's content. Look at that. There we go. We can see our 1 MHz carrier in there. And yeah, that is That's just beautiful. Absolutely thing of beauty and a joy forever. Look at that. Now, let's see if we can see some runt

**Dave Jones:** pulses. I've got some runt pulses set up on this uh serial signal here, and they should be in there somewhere. And if we change the intensity, this is on the 3000X, you can start to see them in there.

**Dave Jones:** You see that? And of course, if we take our time base out, you can start seeing them in there. And of course, you can uh stop that and Oh, there we go. We caught one. There we go. So, there just occasionally there's

**Dave Jones:** these runt pulses in there like there's a bus conflict or something like that. That's what it's uh simulating. Let's see what we get on the ancient 54622D. Okay, we have 100% intensity. Turn that intensity down. And yep, I can see

**Dave Jones:** I can see the runt Yeah, there we go. I should have had the exact same time base to make it fair, but you can start seeing the runt pulses in there. No problems at all. Look at that. It's all showing

**Dave Jones:** up. Yeah, not a problem. Look. Bam! And so really, that is that works quite well. Just like even though it hasn't got that super fast updating 1 million waveform updates per second, although I'm not sure at that time base

**Dave Jones:** is not 1 million on the uh 3000X series, but you can certainly still see those pulses in there. No problems whatsoever. I like it. It's just as useful a troubleshooting tool as the 3000X is. And let's try that on a modern

**Dave Jones:** Well, modern 5-year-old Rigol 1052 E. And well, you can occasionally pick them up there, but the waveform No, the waveform updates in is much faster on the 54622D. That's for sure. You can just sort of see the run pulses in

**Dave Jones:** there. And because this hasn't got an intensity graded display, it's not going to help you any in terms of turning that intensity down. I don't know. But that that's in the center. So that's that's got nothing to do with it.

**Dave Jones:** No, in fact, that's just the Is that just the graticule? No, I don't know. But anyway, not nearly as good as the 10-year-older 54622D. No contest. And it also has a fairly comprehensive set of internal self-tests as well and built-in signals. There you

**Dave Jones:** go. It's generating various things and switching them internally. You can probably hear the relays clicking. Boom boom boom. There we go. And passed. It's very quick, too. I like it. And it does have built-in math functions, not a huge

**Dave Jones:** amount, but you know, it does integrals and it does FFTs. And you know, everything's just fine. So about the only major thing it's lacking that you might get in a modern scope say is a segmented memory for example. And well,

**Dave Jones:** yeah, like there's other things like there's no pushable buttons for example, like centering the horizontal back. That'd be nice, things like that. You know, just small things, but as far as a you know, a modern functional scope goes, this one can

**Dave Jones:** pretty much hold its own against most scopes these days. Of course, the big feature back then of course was the mixed signal stuff. And you can do FFTs at the same time. So I've got FFTs two uh digitals sorry, 16 digital channels

**Dave Jones:** plus the two analog Well, there we go. The two analog channels as well all superimposed. Shame it's not color in this respect, but you know, it's it's pretty good. You can change the size of the waveforms of course. You can make

**Dave Jones:** them tiny like that, medium, or big. You can actually set the threshold voltages to a user-defined level. So you know, it's got a full level cap- Well, full level capability. There we go. I've got a uh uh so many different scopes, so many

**Dave Jones:** ways to use them and you can set the user defined voltage pretty, you know, it's a pretty usable mixed signal scope and it's got I believe 400 meg samples per second on the digital channels and 1 meg per channel for the digitals, I

**Dave Jones:** believe. Don't quote me on that though. And as far as your internal I squared C triggering for example goes, well, you can set the the clock line to the end of the analog channels or any of the digital channels, same with the data

**Dave Jones:** line and then you can trigger off start stop conditions and frames and you know, it's it's all there. But I know what you're saying, "Dave, I want to see inside it." All right, here we go. Let's take this sucker apart. By the way, I

**Dave Jones:** didn't show you the back. It's got a nice carry handle as well and there we go. We've got hey, old school parallel port RS232. There's an option interface for a external modules. There's a trigger out and external trigger input. Nothing

**Dave Jones:** fancy. As I said, the fan was a bit loud. And just two screws on the back and we're in.

**Dave Jones:** You called it, in like Flynn. Look at that. There we go. Fairly neat and compact on the inside. I mean, look at that. There's you know, plenty of space still left in there of course, but as you'd expect the main board is on the

**Dave Jones:** bottom which we should be able to have a look at. Ta-da, there it is. Have a good look at that and pretty standard you know, neck board and the CRT and all that sort of stuff. So, nothing fancy going on there at all. And

**Dave Jones:** it is very neat and tidy and built very well. I like I'm not particularly keen on the bigger ribbon cable just going from the mains board over here by the looks of it. That's obviously carrying that's carrying all the power out of it. So,

**Dave Jones:** that's the that's the power ribbon cable going down to the main motherboard on the bottom like that. Not too spectacular how they've routed that arrangement and the front panel board. Look at that, they've just got the ribbon cable going from the front panel

**Dave Jones:** there. So, that's a bit untidy, but as you can see, nice big clunking power switch there going all the way lever arm going all the way through to real clunking power switch at the back. None of this standby power rubbish and uh uh

**Dave Jones:** it's very neat and well designed. There's the neck board on the back there. That's fairly nice held in place by silastic there on the inside. And the CRT is certainly well braced inside this metal chassis here. So, I really like

**Dave Jones:** that. That's really quite well mounted and tough and rugged. Beautiful cuz this sort of was a portable scope as far as, you know, scopes went. This was designed to be a lightweight sort of portable scope you could take anywhere. That looks like a

**Dave Jones:** nicely designed and nicely laid out power supply board. In fact, it looks like it may have even been done by Agilent. I'm not not entirely sure. It doesn't look like your usual shopped out job, but it is very well spaced.

**Dave Jones:** The main cap in here nip on chemicon no problems. The other ones over there are rubicons. So, top quality caps as you'd expect and that's a very neatly designed well spaced out. It's not, you know, one of those compact designs that have uh

**Dave Jones:** thermal issues these days. And of course, the fan is free standing over here easy to replace the fan if you want to put a silent one in there. And there's the front panel board and one of the really good things about this scope

**Dave Jones:** is the quality feel of the knobs and and the verniers or the the encoders on there. And these encoders, I'm not sure what brand they are. Have no idea, but they just feel fantastic and nice big, you know, solid uh, heavyweight sort of

**Dave Jones:** feel to them as you turn them. They actually require a fair bit of force. They just feel like they're going to last forever. And probably one of the best, uh, encoder knob feels I've ever encountered on a scope or any bit of

**Dave Jones:** gear. Just very nice. I love that sort of, you know, nice I It's hard to convey. You have to sort of play with it yourself, of course, but they just feel beautiful to spin. They really do. And there's the money shot. Let's take a

**Dave Jones:** look inside at those specific chips. You can see the big two MegaZoom branded, uh, ASICs over here. Not just one, but, uh, looks like it's a dual, uh, chipset. Maybe one per channel or, uh, something like that. Who knows, but, uh, yeah,

**Dave Jones:** that is neatly laid out. And, uh, easy access to the floppy drive here. Uh, if you want to modernize this, you could just replace it with, uh, one of those ones you can buy on eBay that, uh, duplicate the floppy interface, but they

**Dave Jones:** actually have a USB key on the front. And you can just, uh, stick a USB key instead, and it should be fully compatible. And there you have it. There's the main, uh, MegaZoom technology. No, they aren't two identical chips. They're actually two

**Dave Jones:** separate chips here. This is the MSO mega. So, this one, uh, they're using for the digital channels, almost, uh, certainly. And this one they're using for the analog channels. And yes, they do have, uh, slightly different part numbers on them. There you go. There's a

**Dave Jones:** closer shot of the two chips for those playing along at home. HP branded UPD 67823S1.

**Dave Jones:** Uh, go figure. Is it a HP ASIC or is it, uh, just some rebranded, uh, regular, uh, you know, processor? Wouldn't be an arm, of course, but some other, you know, 32-bit processor or something just re-badged, most likely. Well, Googling

**Dave Jones:** that one, all I get for the UPD 67823 is that it is an NEC part now, Renesas, of course, uh, and that it's an ASIC. Hmm. Bingo, there it is. NEC Gator 8.44 micron technology, 3.3 V big ass 672-pin

**Dave Jones:** BGA, ultra high performance submicron gate target of applications kind high speed, low power dissipation, blah blah blah, reasonable price, blah blah blah. It's got Here we go. Well, I'll link in the data sheet anyway. 11 base arrays with the raw gates from 33K to 382K

**Dave Jones:** gates. Puzzles. So, architecture mixed transistor sizes, lovely. I like it. And it's got PCI interface blocks. Fantastic. PLLs, there you go. So, very FPGA like. And there it is the UPD 67823. So, it's 56,000 800 available gates, usable gates, only

**Dave Jones:** 39,000 and 200 IO pads. Uses three metal layers in the technology. There you go. Interesting. So, what are they doing inside? That thing is it's something to do with the, you know, triggering system perhaps or something like that. Maybe

**Dave Jones:** interface controls for the mega zoom ASICs because it may be like the wave a waveform update processing on the screen or something like that. Although, that's the mega zoom. But, yeah, it's interesting that it's located between the analog channels down here. So, this

**Dave Jones:** is the front end. Here's the analog inputs, the digital inputs. Located between physically located between them and the mega zoom ASICs. So, that's rather interesting. Looks like we might have another processor over here. So, that's the one that probably controls

**Dave Jones:** the screen and stuff like that. We've got our flash memory over here and things like that. So, it's not sort of the main, you know, applications processor controlling this thing. I think that's probably going to be over here. So, it's something to do with the

**Dave Jones:** mega zoom acquisition and or triggering and or something like that. If anyone knows, please let us know. And all of that's running from a main 200 MHz clock oscillator. They're not mucking around there. And there you go for you Motorola

**Dave Jones:** 68,000 fans. There's the main application processor 68 C020 classic. And there's the ROMs tucked under there. And there's what I'll call the analog mega zoom ASIC cuz it's dedicated to the analog channels. And then we've got our two sample memories

**Dave Jones:** here, separate ones per channel. And likewise for our digital mega zoom ASIC. Once again, as as I mentioned before, separate memory for the digital channels, which is great. It doesn't share the analog channels. And there's quite a few memory chips surrounding

**Dave Jones:** that dedicated to all 16 channels. And I popped off the metal can on the front end and tada, there it is. Looks like we got some Lucent chips here. Let's take a close look at those. That's effectively one complete channel. Basically, they're

**Dave Jones:** duplicated above it for the other channel. There's another sort of relay up under there, which is under the plastic, which I can't really show you at the moment without disassembling the whole thing. There's not much there. Trust me. I might be able to get the

**Dave Jones:** shot in there cuz it's actually fairly dodgy how the BNCs are done in there. So, I'll show you those in a second. We've got ourselves a Lucent probably, I don't know, custom part. I don't know. We'll have to Google that,

**Dave Jones:** but I don't anticipate much luck there. But that's all we've got on the analog front panel front end. Not much, of course, but hey, it's not huge. This is only a 100 MHz bandwidth front end. You know, kiddie stuff. There it

**Dave Jones:** is, VB 1985. Good year. Back to the future. Awesome, but no, I did nothing. Search doesn't turn up anything on that. So, yeah, some sort of custom analog part. So, there's the BNC on the front panel. That's probably the best shot I could get. It's

**Dave Jones:** securely mounted onto the front panel. No problems at all, of course, but then it's just running bare wire over to the main board there. And that other wire there isn't I don't think that's ground. I think that's the ID for the times 10

**Dave Jones:** probe. So, there you go. That's about all she wrote for the Agilent 54622D mixed signal MSO scope. Fantastic scope for its day, incredibly popular, sold incredibly well. Everyone wanted one of these puppies and still a quite a usable

**Dave Jones:** scope today. So, well worth putting There's a whole bunch of part numbers as I said, the newer model like this with the rounder button is older style with the squarer button, slightly lower spec, but still very usable mixed signal scope

**Dave Jones:** today if you can pick one up at a decent price. So, well worth putting on your eBay watch list, that's for sure. So, anyway, I hope you enjoyed that look at this 14-15 year old scope. And if you liked it, please give it a

**Dave Jones:** big thumbs up, of course. And if you want to discuss it, EEVblog forum is the place to do it. That is linked down below and as always, there will be high-res teardown photos on EEVblog.com. That's linked in down below, as well.

**Dave Jones:** Catch you next time.
