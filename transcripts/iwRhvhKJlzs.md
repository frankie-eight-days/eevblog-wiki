---
video_id: iwRhvhKJlzs
title: EEVblog #747 - PC Based Logic Analyser Project
url: https://www.youtube.com/watch?v=iwRhvhKJlzs
source: youtube-asr
---

**Dave Jones:** Hi, look what I found the other day when I was going through a whole bunch of old stuff here in the lab. Came across some old uh design notes for an old project I did way back in Yes, check out the date,

**Dave Jones:** 1995. So, that's practically 20 years ago now, and I've still got the original design notes for a PC-based logic analyzer project I did in um Electronics Australia magazine in uh October 1996. So, I thought it'd just be nice to

**Dave Jones:** actually uh take a look at um some of these old uh diagrams and see how we did things back in the old day, and maybe I can show you the project. I've got the original prototype here. Have a look

**Dave Jones:** through the magazine, and then maybe see if we can find some of the old design files, and see if we can get them back up and running. Should be interesting. Now, you have to excuse my voice. It is

**Dave Jones:** not the best today, so um I'm doing as good as I can. Now, this is the um the first one I found. It's an old timing diagram, hand-drawn timing diagram I did of the uh control circuitry for this

**Dave Jones:** logic analyzer, as we'll see in a minute. And well, this is what you did back in the day before, you know, simulators and writing uh VHDL or Verilog code, and then running uh simulators on that and stuff like

**Dave Jones:** that. This is how you did digital logic design back in the day. You would hand-draw timing diagrams on this 5-mm graph uh paper like this. It was very handy to do these uh sorts of things on, to line stuff up and things like that.

**Dave Jones:** So, pretty much just designed this on paper and in my head, you know, gray matter simulator, paper simulator, whatever you want to call it, Dave CAD simulator. This is an early uh Dave CAD stuff from 20 years ago. Geez. Anyway,

**Dave Jones:** this is a hobby project I got uh published, and yeah, I can't remember details of this, but uh yeah, these are my original um timing diagram notes. And look, you know, the PC ack signal, whatever PC acknowledge signal, I guess, cuz this was PC

**Dave Jones:** controlled, must stay low during write and then read back and then writing period and waiting for trigger and hold hold hold hold and then uh read back and then write mode here and then I've got I don't know what I've got a question mark

**Dave Jones:** for there, but uh obviously had to do um something tricky at that point and must allow trigger here and all this sort of jazz. So, this is just a neat way to do digital logic design and was very common. And

**Dave Jones:** hey, I would probably still do some stuff like this uh today. I wouldn't simulate everything. I'd still do some things like this on paper. And then in addition to the uh timing diagrams, I've got a control circuit uh concept here, which um it was

**Dave Jones:** probably my it may have been my first draft. I can't actually uh remember of the control circuitry, how I was going to control this PC based logic analyzer. And here's the input here. It's a PC uh parallel port interface, not this USB

**Dave Jones:** rubbish or uh serial. Parallel port was um you know, the one of the major means of controlling projects at the time. And I did quite a lot of projects using the PC parallel port, including a digital storage um scope, uh IC tester, EPROM

**Dave Jones:** programmer, and this uh logic analyzer, and uh some other stuff as well. So, I've got like a 245 here. I've got an 8-bit uh latch cuz you have to latch data in, but I think I went away from

**Dave Jones:** this. We might see this in a minute. Anyway, we've got some uh 6225 650 ns SRAM, which will be used to store the data in, 16-bit binary counter to increment the address. We've got some a mux here, DS um zero. I'm not exactly

**Dave Jones:** sure what I'm doing there at the moment. Have to read the article again. And then just uh some control latching that flip-flops uh trigger sort of stuff, the arm signal. Uh we've got another 16-bit counter here. This would have been the

**Dave Jones:** uh post trigger counter because in a logic analyzer you want 50% pre and post uh triggering so that you can see information before and after the data event. And uh yeah, and that I guess turned into cuz these were at a

**Dave Jones:** these were at a later date. In fact, this one is uh 19 uh 1996. So, this is uh February '96. So, this is significantly after this one. So, I might have like redrawn this one. This might have been like a a a new

**Dave Jones:** revision of it or something like that. But, uh I've got two different chips here as we'll see in the hardware design. I've got my main uh logic analyzer my main control chip which had all the uh control circuitry that we uh

**Dave Jones:** saw here basically embedded. This looks like it was not like my final implementation. And I've got the logic analyzer trigger chip here as well because we needed fully maskable triggering. I e. you had to set in software whether or not you want to

**Dave Jones:** trigger on a high, low, or don't care uh condition or something like that. So, um I here you can see that I've got to got to repeat all this uh circuitry. And this was a 32-channel logic analyzer cuz

**Dave Jones:** this looks like an eight-input um architecture here. So, I would have duplicated that uh four times in my main uh CPLD chip. So, I designed this entire project on paper like this. And I would have had like little crap uh scrap notes

**Dave Jones:** and things like that. I would have had another uh notebook where I recorded um test results and did, you know, some other stuff and things like that. But, um these are basically all I've uh got available in my archive. I'm surprised I

**Dave Jones:** still have them actually. But, now we can go take a look at the final article. Brilliant. So, my final uh design and article was published over uh two issues. First part in October 1996 and second part in November 1996. And uh I

**Dave Jones:** was I was a bit disappointed that I didn't get like a front cover shot. The you know, one of the goals back then was to get a front cover photo of your project or something like that. I didn't. I just got a tiny little uh

**Dave Jones:** 32-channel 40-MHz logic analyzer thing here. And um as you can but I did get a photo in here though. So, yeah, that was all right. I was pretty chuffed though. Now, one interesting bit of history. Look at this. The Tektronix TDS 220.

**Dave Jones:** This is almost 20 years old this scope. Look, here it is. Who can remember that? Geez, it was you you know, this was a massively groundbreaking scope. And this was one of the Well, this was one of the

**Dave Jones:** first reviews they got an advanced unit. And 20, can you believe it? 20 years old. This was a complete game-changer. This is where, you know, the first really affordable real-time, i.e., you know, the sample rate 1 gigasample per

**Dave Jones:** second was like 10 times faster than the analog bandwidth of 100 MHz. And it operated, you know, the controls and everything operated pretty much like a real analog scope. And yeah, it's a crap scope by modern um standards. But,

**Dave Jones:** people still pay a huge premium for these. They just I don't know. People have an affinity for them. But, anyway, um yeah, they're horrible by modern standards. Slow, the screen is terrible, limited uh 2 and 1/2 K sample memory,

**Dave Jones:** which is really pathetic. But, back then, man, this was the duck's guts scope. And that's what started for all you youngsters out there who buy their Rigol DS, you know, uh 1054Z and everything these days and take it for

**Dave Jones:** granted. This was the thing that basically started the whole portable digital scope thing. And there you go, it's almost 20 years old. There's the original review. Wow. And sorry about the little non sequitur here. I can't help myself. I just love history. Um

**Dave Jones:** article by uh Jim. Good day, Jim, if you're watching. He still writes for Silicon Chip Magazine. Anyway, he basically nailed the end of the article 20 years ago. If anything can woo low-end scope buyers away from the Asian analog

**Dave Jones:** clones, this new tech uh model surely have a good chance of doing that. And in any case, they surely represent a very significant milestone in scope technology, and I wouldn't be surprised if they change our expectations of scope

**Dave Jones:** packaging and price performance factor forever. Jim absolutely nailed it back then. He knew these things were uh you know, game-changing, and he was bang on. And here's the original full-page ad for the scope. Here we go. Uh $1,400

**Dave Jones:** by the way for the TDS uh 210 60 MHz or 2 grand for the 100 MHz model from Emmona. They're still uh the dealers, and they're of course the Australian reps for Rigol scopes these days. They're the ones that have basically

**Dave Jones:** taken over from these venerable TDS 220s, and John Sawtell was probably still working at Emmona back then, I think. Good day, John. And here's the original article part one. I was really chuffed when it came out, of course, with all my projects. It was the

**Dave Jones:** reason that I did it. Fantastic. Uh I actually um shared it with uh my mate uh Dave Belford at the time. Good day, Dave, if you're um watching. He um he didn't really have too much to do with

**Dave Jones:** this project, but we kind of sort of worked on a few uh you know, concepts and things together. So, I thought I'd just add his name to the article here, and he I didn't tell him I was going to do that,

**Dave Jones:** and he was uh pretty chuffed as well that I added his name to it. Anyway, yeah, got a photo shot, got my original um schematic that I I did in uh Protel uh uh 1.61 for DOS. I would have done all these

**Dave Jones:** things in and all the drawings as well, as you'll see in a minute. Um specifications for this puppy, it was uh TTL CMOS uh compatible, 32 channels, um up to 40 MHz um sample rate, which is pretty good.

**Dave Jones:** Only 20 MHz in state analysis uh mode, though 40 in timing analysis mode. And then latch trigger word mask external uh triggering as well. Uh fully maskable 32 channels, optional glitch capture. I actually don't remember about that. Um

**Dave Jones:** address data disassembly in software and external buffering and triggering boxes, which I did external probes and I think I made some buffer boxes, but yeah, I never sold those. And they published uh my schematics exactly as is, as I said I

**Dave Jones:** would have I believe I did this in uh Protel uh for DOS 1. uh 61, the no dongle edition back when they had dongles. And these block diagram drawings, I did those in uh schematic as well. I did a lot of

**Dave Jones:** stuff in uh schematic Protel schematic back then. I did the front panel um as well, which we'll see in the next um thing. I did, you know, I basically used it as a very simple uh CAD tool. It just

**Dave Jones:** worked. So, anyway, we've got our main um schematic here. We've got the main circuitry for our uh control LSI chip, which uh came from this one we uh saw before. And then we have our trigger control circuitry here. It looks much

**Dave Jones:** better than my original uh concept down in here. So, you can see that I I actually rather like this one. I've uh split it up into uh separate sections, mask and invert uh shift registers. So, basically, I feed in serial data like

**Dave Jones:** this from the PC. It goes into these registers so I can actually set the individual bits on the mask array and the inverter comparator array here. So, if you want to like mask out a bit, i.e., not uh trigger on that bit, you

**Dave Jones:** can set um an individual output here. And that was just an easy way to do this. So, it's a little bit uh confusing, but here's basically the data input to the chip. And the data input goes directly over to the uh invert

**Dave Jones:** comparator array here before it goes onto the masking and then the grouping array in grouping array and then the uh equality output, i.e., uh trigger um output. And these data output uh muxes here, th- this is a 16-channel chip, by

**Dave Jones:** the way, as you'll see in the hardware in a minute. I've got two different uh trigger chips in here. And this was a sneaky bit of uh dual use here. Inside the trigger chip, the trigger chip um I

**Dave Jones:** don't need these muxes for the triggering, of course. I could could have just had the data coming straight into here and then, you know, giving my uh eventual trigger output. But I added um these data output muxes in here to

**Dave Jones:** sort of uh make use of what uh some space I had left in the um uh CPLD um LSI chip. And this Of course, I had to read the data back out to the PC. So, of course, I've got like 32

**Dave Jones:** channels, so I've got 32-bit memory in this side and inside inside this thing. How do I read it out? Well, two separate eight-bit muxes here allowed me just to read the data back out from the memory bus, which this was ultimately hooked up

**Dave Jones:** to. So, just a, you know, a bit of um it wasn't just the trigger chip. It also did some data uh read back for the PC, as well. So, if you're wondering just how this worked, well, we've got our inputs over here from the

**Dave Jones:** front panel. We've got our latches here. And these go through to the trigger chip here. The data buses are taken off. So, two separate trigger chips handling that 16 channels each. It didn't have the internal space to do it all in 32, I

**Dave Jones:** don't think. Although, I probably No, I probably could have got a larger chip, but I think physically it was better to do it with two separate chips or something like that anyway. And a separate control chip. This one used the

**Dave Jones:** latest LSI 1016, as we'll see shortly. And this this used the Actually, the 1016 as well on this schematic. Could have sworn I changed that to the 1032. Anyway. So, if you're wondering just how this thing works, well, this inverter

**Dave Jones:** comparator array, that basically can invert each individual bit. So, here's our data input coming in here and there's an input into each of these exclusive NOR gates here. And depending on whether you put a one or a zero

**Dave Jones:** there, you can either feed the signal straight through or you can invert it. That's the benefit of the exclusive NOR gate. So, if you set a one here, then on on here, then it would invert your bit. Why would you want to invert it? Well,

**Dave Jones:** because that's for the positive or negative triggering. You can set each channel for positive or negative, because you had to do that. You had to invert them so that you could then eventually get all in one hit, get your

**Dave Jones:** trigger output here. Then we had what's called a mask array here and that, once again, you'd get the individual bits here. You can program each of your input each of your data inputs to either pass through or not. So, if you put a

**Dave Jones:** one, if you programmed a one onto this input here, then of course, this is an OR gate, so it'll always be one out here. It'll always force a one. So, it doesn't matter what your input data does, you effectively mask out that bit

**Dave Jones:** from your triggering operation. So, with those two steps there, your inverting and your masking, then you just group them all together. This is just one big AND gate basically and then you AND them all together and bingo you get a trigger

**Dave Jones:** output. And as for this control chip here, well, I don't remember exactly all the details. You can actually read the article which I will link in down below. I've actually scanned in the PDF of both of these so you'll be able to read the

**Dave Jones:** whole thing if you like. I think I describe its operation in detail. I'm not going to go through and read it all again anyway. The semantics aren't hugely important but this is basically all the control circuitry um that I did all these timing diagrams

**Dave Jones:** for. So all these yeah, look there's the arm signal for example. There we go. That's the arm signal. Is there a trig signal coming in there? Trig select. So I've obviously changed a few of the names since I did this original timing

**Dave Jones:** diagram but this should be you know fairly close to the final operation of the things. Then as for the trigger section here, basically we've got two different trigger inputs because I've got two trigger chips so I just AND

**Dave Jones:** those yet again. So I'm expanding that huge AND gate we saw before. We've got an external trigger in. This is just a max. We can choose whether or not we want internal or external trigger in and then our trigger in polarity is done in

**Dave Jones:** here not actually in the trigger chips. Now this trigger delay section here, it's a bit of a deceptive title cuz it doesn't actually delay the trigger as such. What it does is it gives you selectable time window that the trigger period has

**Dave Jones:** to stay open for. So you can have like you know just a single trigger pulse or you might need two. It might have to stay high for two clock periods or something like that or four, six, eight or whatever. So

**Dave Jones:** basically you can select these here and that just allows you to stop any spurious trigger signals from causing any issues and then that feeds up here and then um, sets an RS uh, flip-flop here, which basically takes it from the regular arm mode. So,

**Dave Jones:** when it's regularly running, this RAM counter is always filling. So, it's always sampling data when it's just sitting there waiting for a trigger. Going through all the uh, it's a as it says, it's a circular address counter. So, it's just counting through

**Dave Jones:** all of the 32K memory, I think it had. Um, so, it's just going all the way through that. And then, when the trigger signal comes through here like this and makes it through the delay part of it, it it triggers this

**Dave Jones:** flip-flop, sets it in the other direction. And then, what happens is this um, post-trigger counter here starts, which is a divide by 32,768. And then, that will basically, when that's finished counting, it will do end of sample. So, it'll say, "Stop

**Dave Jones:** sampling." And then, what you end up with in your memory is half of your memory sample memory filled with your pre-trigger data and the other half of your memory filled with your post-trigger data. So, it's actually reasonably uh, involved how all that

**Dave Jones:** works. And you've got to go through and figure out all these uh, you know, timing diagrams. And basically, I did like all this in my um, head, basically, how it would work. And the timing diagrams were just there to sort of, you

**Dave Jones:** know, prove it and just give me like a visual representation of, you know, to see if there were any any issues or something like that before I build up my first uh, prototype. And here's part two of the uh, article in the following

**Dave Jones:** month. That was actually quite common. If the article went over like, you know, five or six pages or something like that, they typically split it. And then, you split it into like the first month would be theory and the schematics and

**Dave Jones:** how it works and everything. And then, the second part um, is just like a construction, you know, we've got probe construction and things like that. How to uh, construct the thing. That's internal shot. I can show you that the

**Dave Jones:** real hardware for that in a minute. We've got the um, overlay diagram here, which I'll uh, talk about. And just some probes I did with like an IC test clip and I didn't have any photos of my pods

**Dave Jones:** at the time, my buffer pods and things like that. And of course, they would publish the front panel in actual size. They'd publish the PCB diagram in actual size cuz people would photocopy these and then you know, photo

**Dave Jones:** expose them, photocopy them one-to-one size, photo expose them and then etch their own boards. I etched my own board for this one. And as I said, this was actually done in Protel schematic software. Got a nice little parts list here, which I would

**Dave Jones:** have given them and they just sort of like reformatted that. But apart from that, I just I gave them basically the article in text format. It would have just been plain text. Now, this logic analyzer design could have been a lot more complex. I

**Dave Jones:** could have designed, you know, like a higher-end one, better performance, better interface, all sorts of stuff. But I wanted I set some very specific goals for this as was common in magazine articles back in the day so that people

**Dave Jones:** could actually build this themselves. And one of the things, of course, was to put it all on one single-sided PCB. And that was a That was a big goal I had, which why which is why for a 32-channel

**Dave Jones:** logic analyzer to fit it onto a single-sided PCB meant that I was forced to go and use these Lattice ISP LSI chips, which we'll take a look at. And I did. I got it onto a single-sided board. I was very proud of

**Dave Jones:** that. Had a few jumper links, of course. Had to jump the odd bus here and there. But yeah, it generally wasn't It wasn't too bad. You know, there's performance penalties you pay for single-sided board in terms of signal integrity and stuff

**Dave Jones:** like that. But it It was just a goal I set. It was just a fun goal I set myself. It was just a fun project. And you know, and that's what I did, basically. And I used the parallel uh uh

**Dave Jones:** port because, well, you know, I was familiar with the parallel port, and everyone had a parallel port at the time, and things like that. So, I used them off-the-shelf available SRAMs. These were common as uh cache memory chips back in PC PCs back in the day.

**Dave Jones:** When you actually had to plug your own uh 62256 SRAM chips beside in into sockets beside your processor to actually do that. And there was a scam that went around back in the uh '90s with the the cache RAM

**Dave Jones:** scam. I'm sure you can Google that one, where they'd sell you fake cache RAM chips, cuz these were quite expensive, but they were readily available. You could walk down to your local uh computer store and buy these uh cache

**Dave Jones:** RAM chips. Very common. Apart from that, standard 74 series uh TTL stuff. And the only special stuff which was available from uh Farnell's at the time, I believe, these Lattice ISP LSI chips are a little bit expensive, but the starter

**Dave Jones:** kit for it was only $99, as I'll show you uh shortly. And it was quite cheap. And, you know, it was pretty advanced to do a project in a magazine using these LSI chips at the time. So, for a very

**Dave Jones:** long time, Electronics Australia was really against, you know, microcontroller-based projects, and you know, anything that used FPGAs or custom uh you know, LSIs like this, and things like that. But, you know, they they agreed to publish this. They went, "Oh,

**Dave Jones:** yeah, you know, it's good and novel enough, and yeah, we're pretty happy that you can actually buy them, and that starter kit's relatively cheap." So, they decided to publish this one, no problems. Now, as far as the uh PC

**Dave Jones:** interface went here, I loved these 74HC uh 259s. Very common. Cuz you only had the 8-bit uh data bus coming out of the PC parallel port, plus a few control lines. I think it was like, you know, 12

**Dave Jones:** lines all up, or something you had available. Some were dedicated inputs and outputs, and stuff like that. Um so, you'd expand them. I It turns out that I needed 16 different control signals. That was the absolute minimum I needed

**Dave Jones:** to control this project. So, I whacked on some HC259s. They're They're addressable uh latch decoders. So, you put So, they've got a three um three input address there. So, I just common those together and then a data line and then a latch line. So, you can

**Dave Jones:** actually latch a one or a zero through to any one of the selectable outputs. And these are very handy chips even today. You know, I would still go for a you know, a HC259 if I needed to do something like this.

**Dave Jones:** They're just great chips. And check it out. I still have my original prototype I built here. And this is the one that they I am sent to them. I physically uh sent them and they photographed it and put it in the magazine and then uh sent

**Dave Jones:** it back to me. That was common in the day. They They didn't trust you to take good photos. This was before digital cameras, folks. They They had to take this with old-fashioned film camera. They didn't trust you to you know, take

**Dave Jones:** They They had their own setup and everything and ways to photograph and uh put it in the magazine. So, yeah, you'd send them your prototype, they'd photograph it, test it of course, and then uh send it back to you to make sure

**Dave Jones:** it did the business. And very simple, it's just data and power leads and these um standard uh 0.1 in headers for the input. Of course, there were like external trigger input. There was an external uh 5 V on here. Ex- external clock,

**Dave Jones:** external 5 V here for external uh probes you could hook up. And if we have a look inside, there's not a huge amount doing here. Yes, it is a rough and ready original uh prototype. We've got our mains transformer, um just the um

**Dave Jones:** ribbon cable going off to the uh 25-way uh deconnector but back for the parallel port. And then we've got our main board. Yes, I etched um this board myself and um they're single-sided. And we've got our uh we've got our three uh socketed

**Dave Jones:** uh lattice chips here. Of course, I had to be socketed. No in-circuit uh uh programming for these uh puppies. I had to put them into an external uh programmer, which I uh a little custom jig which I uh made

**Dave Jones:** for these things, cuz I did sell uh quite a few of these. I sold a package with uh the pre-programmed uh micros and the uh software and things like that. And a lot of people built this um on their own. But, yeah, everything is

**Dave Jones:** socketed because, well, this was an original uh prototype. So, you know, we got some uh got some resistor networks there, and Bob's your uncle. There wasn't too much to this. It was a very simplistic design. But, to get the speed I wanted,

**Dave Jones:** I had to use 74 ACT series chips here. And as I mentioned before, signal integrity was a real issue on a single-sided board like this. Um you just couldn't get your loop area small enough that you could if you used a

**Dave Jones:** double-sided board. So, it's a little bit iffy in that regards when you try and push it. And 74 AC, they they take real huge gulps of current when they uh switch. So, yeah, that was a bit of an

**Dave Jones:** issue, but it it did work though. It's, you know, it was a hobby kit. It wasn't a professional kind of thing. It was just designed as a fun thing to design your own logic analyzer. And ultimately, as long as you're careful with the probe

**Dave Jones:** and things like that, it did work out fairly well up to 40 MHz. Right. So, I thought I'd take a look at some of the stuff I've got. And these are all the original uh files that I have here.

**Dave Jones:** Here's the actual um user program itself, the uh Borland Pascal 7, I think it was, uh source code to it, various uh source code, a uh test program, a uh readme uh document which came with the software, and an actual uh

**Dave Jones:** readme executable, which I wrote myself, which just allowed people to read the uh doc file without having to um you know, have a reader program, like open a text program or anything like that. It just worked. It was only 8

**Dave Jones:** kilobytes, absolutely tiny. I've got all the schematic uh files. There's a whole bunch in here. Looks like there's a whole bunch of revisions. I Looks like I I released version 3.1. So, in in the end, that's what I did

**Dave Jones:** there. And look, original date code of '95. Why there's '93 there? I have no idea what that '90 3 is. That might I don't know. Strange. Anyway, um I've also got And the all the schematic stuff would be in uh Protel

**Dave Jones:** um schematic for DOS. And here's all the projects for the Lattice CPLD I in-circuit programming device. And these are And uh the uh PCB file as well. That's uh Protel for DOS. So, uh here's the um original uh brochure for the

**Dave Jones:** Lattice ISP starter kit, which is what I uh bought at the time. Here we go. Price down the bottom. There we go. 99 bucks. And I'm think that's what I paid. Is this an Australian brochure? I It was pretty cheap at the time for a

**Dave Jones:** development kit. This was incredibly cheap. Um you've got to remember, you know, you didn't get free tools like you did these days. This was a absolutely incredible price. I bought this. Um you know, I probably saw the ad in

**Dave Jones:** Electronics Australia magazine or or somewhere else, something like that, cuz there was no internet back then. And well, there was no web as we know it anyway. So, all you got all your information from your magazines. Anyway, this starter kit Oh, yeah, there it is

**Dave Jones:** at the top. 99 bucks. So, that was really cheap. You got it like a little programming uh cable with it, which hooked up to the parallel port, I probably think it was. Anyway, it worked with the ISP LSI 1016

**Dave Jones:** and 2032 devices. And I thought I used some 2032s in here. And it also supported these ISP GDS generic digital switch chips as well. And I actually wrote some uh software for these um as well and actually um sold it for a

**Dave Jones:** while. Uh and you get the the 9094 data book because well, you couldn't just download PDFs. So, you had to actually get the data book with all the data sheets and everything. So, um yeah, it was that's probably why I use

**Dave Jones:** these Lattice devices because I bought this starter kit and well, you know, what can I do with it? I don't know. Let's do a Let's do a logic analyzer or something. Or I had the idea for the logic analyzer and then I thought, "Aha,

**Dave Jones:** I can use those." Anyway, whichever way it happened, uh it came with some starter kit software. Now, no surprises for guessing. You can't actually buy these Lattice ISP LSI 1016 devices anymore. You They are still listed on Digi-Key, but they've got zero stock and

**Dave Jones:** well, yeah, just don't bother trying to get them. You won't be able to cuz they were discontinued in September 2010 by the looks of it. All devices discontinued. Well, thank you very much. So, my uh project is, you know, pretty

**Dave Jones:** much buggered right there. But anyway, these weren't bad devices at all. I didn't mind them. They were really fast um high-density PLDs or, you know, CPLDs, whatever you want to call them. And they were in-system program compatible. So, they had built-in uh

**Dave Jones:** well, not flash, but they had um EEPROM technology, E-squared uh CMOS technology. So, they were electrically erasable and reprogrammable using the in-system serial cable, which I I think from memory just used the uh just used a couple of lines on the PC parallel port

**Dave Jones:** to actually uh program these things. But on my board, I didn't have an in-circuit programming header cuz I don't think I had the pins available. I think they were uh dual-use pins or something like that. But yeah, um very typical uh

**Dave Jones:** global routing pool arrangement for a CPLD device. Generic logic blocks around the outside. I You could almost Yeah, it's not These aren't FPGA architecture, but they're, you know, typical complex CPLD. Well, your old device is discontinued. Thank you very much, as if

**Dave Jones:** I didn't know. Geez. And here's how you calculate some of the timings. Look at these complex additional equations here for the various sub blocks, the IO cell, the general Is that the routing? No, that's the general routing block, the output

**Dave Jones:** routing block, the general routing pool or something, and the IO cell on the other side. So, you have to do all this to calculate all your, you know, your maximum frequency and your timings. I can't remember if the software actually

**Dave Jones:** did it. All I can remember about the software is, well, I didn't do this in any modern language, you know, VHDL or Verilog, any like high-definition hardware language. I did this like as a schematic block thing, and then manually

**Dave Jones:** placed all of the IO blocks in this thing. So, yeah, it's like a visual drag and drop type thing. So, at the top level I did the schematic, then it gave me all the blocks, and then I manually just routed,

**Dave Jones:** you know, all basically routed this CPLD by hand. I know I remember reading somewhere that oh, you can't use more than 90% utilization of this device. Well, I very clearly remember actually getting 100% utilization in this thing by hand routing it. I think

**Dave Jones:** you could auto routed it, but it was, you know, pretty piss-poor. So, I hand routed the thing. It wasn't a huge design. And if I could get the software working, I'd show you, but unfortunately, I can't. Now, as it turns

**Dave Jones:** out, Lattice still make available this ISP Leaver project software. It's like designed to support all these legacy devices. So, you can actually still get it. It runs in Windows 7, no problems at all, which which all fine, but it doesn't support

**Dave Jones:** these files. It actually needs a um schematic SYNC file, and mine don't have that. Mine have Mine have like LPR files. The JED is the standard JEDEC output, which you use to program the binary image you use to program the chip with the

**Dave Jones:** programmer software, and the LIF I don't remember what the LIF file is, but the LPR I think is the project file schematic, you know, information for the thing. And I actually found an old note, which I even noted at the time or a couple of

**Dave Jones:** years after that I released this design that the new software does you know none of Lattice's other software which supports these chips actually support the file from the starter kit. So, you get locked into the starter kit, and you

**Dave Jones:** have to It's got its own file format and everything, so you have to continue to use the starter kit software to actually get the thing going. Big trap for young players. I got really duped with that bloody $99 starter kit,

**Dave Jones:** didn't I? So, that if you're using this in a professional application, you'd be you know, screwed if you have to support this, you know, years after the design was finished. Gladly, you know, I didn't have to do that, but jeez, yeah. Watch out for

**Dave Jones:** bloody Beware of starter kits using custom software. Lattice bastards. Anyway, if you want to see a screenshot of my DOS software. Yes, it is DOS, none of this Windows rubbish back in 1990 5, 1996. So, it was written, as I said, in Borland

**Dave Jones:** Pascal 7, I believe it was. So, I'll try and get that up and running in a minute, but that's a screenshot. It did all sorts of weird and wonderful stuff behind that. There were all sorts of menu options and things like that, which

**Dave Jones:** I don't think are are shown there. I completely forget. Here's an old photo of the original prototype board hooked up to a test pattern generator. I was using that to generate some test patterns and like, you know, verify the

**Dave Jones:** software and do all that sort of jazz. And because I did the PCB and the schematic in AutoTrax, look, I can actually still download this from the Altium website even today. They actually released uh Protel as it was called back then,

**Dave Jones:** Protel AutoTrax. Uh that was the name of the company. And the company's name was Protel before they changed it for Altium, for all you young whippersnappers out there. And they make it available, DOS freeware 1.61. So, I should be able to load in my PCB files,

**Dave Jones:** but I don't think they um and they released like an Easy Trax version, which is like a low-cost uh version at the time, but they never actually released, as far as I'm aware, the schematic, the you know, the companion schematic tool

**Dave Jones:** for it, which is ridiculous. I don't know why they released AutoTrax, which is the PCB program, and didn't release the schematic one. Oh, well. And here's this uh software for those Lattice GDS uh chips, GDS generic digital switch. And this is exactly what

**Dave Jones:** they were. So, I wrote this program because you had to like define these things in like a text file and then compile it. And it was a real uh pain in the ass. So, I wrote this user interface, this graphical user

**Dave Jones:** interface, to allow you to like change the outputs. Could be like buffers, inverters, open, VCC. So, you these are all the pins on the chip. So, you can get different types of chips and I think the software scaled to different devices

**Dave Jones:** and things like that. This is the ISP GDS 22. And um I I've finally released this into the public domain. I did uh sell this at one point, and quite a few people bought it. They were reasonably popular little niche chips back in the

**Dave Jones:** day. Yeah, but you could read it, you could program them directly down through the parallel port. I can't remember exact uh details, but yeah, those were the days. And well, who uses those anymore? I don't know how long they

**Dave Jones:** lasted, but I think their uh lifetime was pretty short, these uh Lattice GDS devices. Now, as it turns out, you can still run Borland Pascal 7. They actually released several versions of this as freeware or whatever it uh was, but I've

**Dave Jones:** got to run this in like a DOSBox. I could actually copy it over uh to the other machine, but I was able to get this running on my Windows um 7 machine, and we can actually Oh, it's a bit It's

**Dave Jones:** a bit how you doing there? So, I'm not sure what's going on there, but anyway, PCLA, we can actually the logic analyzer, we can load in Ta-da! There's my original source file. And there we go. I stopped it. There was something wrong with the

**Dave Jones:** mouse there. Anyway, here we go. We're in like Flynn. PC-based logic analyzer, 1996. And all the color uh color syntax highlighting. Oh, that was the duck's guts back in the day. Look at that. Magic. And here's all the original

**Dave Jones:** source for it. There were There were two programs. One was the main or two source files. One was the main program, and one was How do I go back? Oh, goodness. And one was the main program, and one was

**Dave Jones:** the uh uh interface program, I think. So, if we go up to uh up Alt C, compile. If we try to compile the thing, line too long. Yeah, oops, that was uh Yep, that was me. I goofed that. Something wrong there.

**Dave Jones:** And compile. Line too long. Oh, goodness gracious. Couldn't have more than 256 characters on a line, I think, back then. All right, here we go. Here we go. Let's try this. Compile. File not found, graph.tpu. Ooh, why not? Um

**Dave Jones:** because it obviously found our CRT library, found the DOS library, couldn't find the graph library. So, if we take graph out of the equation, but it's not going to work. I mean, but let's just see what happens. Could not find PCLA I10 TPU. Maybe I

**Dave Jones:** have I haven't copied that file in. It's not in the correct directory, all that sort of stuff. So, yeah, I can't immediately compile this, but if I wanted to, I I could. So, it's it's still a win. Um

**Dave Jones:** you know, 20 years later, I could probably still use Borland Pascal 7, compile it, get it up and running. No reasons why I couldn't uh modify this program if I needed to and uh recompile it. Now, please excuse the crudity of my

**Dave Jones:** screen capture here. I'm going to use an old uh Windows XP notebook. Let's see if we can get uh Protel Autotrax up and running and load that PCB. Yeah. Let's do it. Uh here we go. Wait. Here we go. We're

**Dave Jones:** going to load it up. Now, uh it contained Protel back in the day had two programs. One was Tracks Edit, uh which was the Autotrax program itself that you used to edit the PCB. Then it had Tracks Plot as well, which you used to generate

**Dave Jones:** the uh Gerbers. That didn't um come standard in there. So, let's go Tracks Edit. So, woohoo! Look at that. We're rocking 640 by 480 16-color VGA. Yeah, baby. It was capable of higher resolution. It could use like the Hercules graphics

**Dave Jones:** card. Woohoo! I think that was like 800 by 600, or was it 720 by something? I can't remember. Anyway, this is version 1.61 ND stood for no dongle after they removed the hardware dongle that you had to plug in your parallel uh port. And

**Dave Jones:** this was the standard version of Protel Autotrax for like a decade or more. You know, people were still using this well into the mid-2000s. There might even still be You Some people still rocking this program. Um So, it's all uh menu It's all uh hot key

**Dave Jones:** uh base. So, even the hot keys back then still work today in the modern version of Altium Designer. They don't work in the new version of uh CircuitMaker, unfortunately. But, mm anyway. Um here we go. Auto Tracks 1.61. So, we can go

**Dave Jones:** to file and then L for load. And I've copied my uh original file in there. So, let's load that up. And bingo. Look at that. We're in like Flynn. And here's my original PCB file. No problems at all. I can go in there and

**Dave Jones:** edit that to my heart's content. Look how slow the redraw is. This is on a two a modern Well, modern in quote marks two gig uh Pentium machine. So, imagine what it was like back in the day. It was like

**Dave Jones:** These were horribly slow graphics routines in this thing. And by the way, uh Protel uh Auto Tracks was uh written in Borland Pascal. Same as what my uh program's written in for the PC-Based Logic Analyzer. Borland Pascal incredibly popular. And even today, a

**Dave Jones:** lot of people don't know this, Altium is actually written in Delphi, which is a Windows version of Pascal. Uh basically, it came from the Borland Pascal um stable. It would used to be Borland Delphi, which I used to um start out

**Dave Jones:** writing my programs in Borland Delphi as well as uh Microsoft Visual uh Basic as well. And uh but, it's not all Delphi these days. It There's kind of kind of like all new stuff is like C++ or whatever. You know, more modern stuff.

**Dave Jones:** But, there's a whole mix of, you know, Delphi. So, Altium has this huge legacy baggage with all this uh Delphi uh code. It was really hard to find programmers. In fact, it was practically impossible to find programmers who had experience

**Dave Jones:** with Delphi. So, they'd hire you and then you'd have to learn Delphi to, you know, um they actually had to learn uh Pascal. Uh cuz most people were used to C. So, but yeah, it was incredibly slow. Even a faster machine did not help

**Dave Jones:** the screen redraws on this. And like and you can't even see the um the holes in your pads. None of this modern what what you see is what you get uh rubbish. So, yeah. But I can still load this program after all this time.

**Dave Jones:** No problems whatsoever. I don't know if it runs on like a Windows uh 7 machine. You can probably get it to run, but yeah, I don't know. But it works. No problems whatsoever. Beauty. Check it out. My board contains uh 717

**Dave Jones:** holes, which I had to drill all by hand. Uh contains six strings, 2,449 tracks. There's the info. This size look at that, you know, free memory. Whoa, you got 88K free. Whoo. And EMS, who remembers mucking around with EMS

**Dave Jones:** memory? Ah, that was the duck's guts back in the day. But yeah, this is Protel Autotrax 1.61. If you haven't seen it before. Now, I can't remember if I can actually load a Autotrax 1.61 file into a modern version of Altium

**Dave Jones:** Designer. I don't think so. I might have to like um I I know that Protel for Windows uh 2.8, I think it was, you could actually load these legacy files in. So, you might have to do two-step process if you

**Dave Jones:** wanted to get it into a modern uh version of Altium Designer. I don't actually have Altium Designer installed on my machine at the moment. I've only got um CircuitMaker. And I've tried um the new version of CircuitMaker, and it

**Dave Jones:** doesn't um import these older files at all. And the companion schematic uh program, which they don't make available, but I still have it on my old uh hard drive here, S-Sketch Edit. Let's load up Sketch Edit and woohoo, it looks

**Dave Jones:** almost identical 3.31. That was the standard forever. And uh load up the schematic file. I will have to Oh, I didn't copy the file in. Oh. So, if I want to get that file, I've actually got to go in here

**Dave Jones:** and change the path manually like this. I love it. Uh project. So, I can now go file load and uh I should be able to find my There's my original digital storage scopes, all sorts of projects, tons of projects, PC logic analyzer.

**Dave Jones:** There we go, 3.1 C. That's That'd be the control chip. That'd be the trigger chip. Um actually, that'd be the block diagram. There we go. There's that block diagram. Ta-da! That I had published in the magazine. There we go. Beautiful.

**Dave Jones:** Still loads. No problems whatsoever. And uh uh the file load. You've got to go end and then backspace and then like that. It's a little bit uh but let's see if we can get up the original uh schematic. PC

**Dave Jones:** logic analyzer the trigger. Here we go. PCLA 30C. Let's have a look at that. Oh, sheet two. I did it on two separate sheets. Now, I'm sorry, 3.1. There we go. Loaded up sheet number one. Bingo. We're in like Flynn. There we go. And all this

**Dave Jones:** might seem very clunky to you, but you know, you I was so super quick at this. I did professional I was working as a professional PCB designer using Protel for DOS 1.61, you know, before I switched over to the Windows

**Dave Jones:** um version. And you just got so quick with these with the hot keys and everything else. There we go. That's the schematic as per um published in Electronics Australia. Beauty. And once again, yeah, to my load these schematic files

**Dave Jones:** into the modern software, might have to do a multi-step process, but it's probably possible. Now, if we have a look at our original files here, my original program, and try and load it, I think we'll have a problem here.

**Dave Jones:** This is the original program, version 1.0. Yeah, rocking it. Ah, wa error 200. I think we'll get that same error at with my readme program that I wrote as well, because I wrote that in Borland Pascal. Yep. Now,

**Dave Jones:** this is a a famous bug in Borland Pascal that in Borland Pascal 7 that any modern machine and modern in {quote} marks. I mean, this is a Pentium M 760 processor at 2 gig, but any machine back in the day over, I think it was about

**Dave Jones:** 200 MHz processor speed. If your machine was too fast, there was a bug in the graphics routine in Borland Pascal 7 that actually spun up this runtime error. So, you had to either manually slow your machine down, or you had There was a patch that they

**Dave Jones:** eventually made like a patch available. Someone made a patch available for it, but then you had to recompile your software and generate the executable with that patch, and I never did that, cuz I think the patch came out like a

**Dave Jones:** couple of years later, and I never went back to the project and recompiled it. So, old old Borland Pascal programs try and run them on any machine over about 200 MHz, coincidentally, throws up runtime error 200. Wa, fail. So, there

**Dave Jones:** you go. This was a rather lengthy, sorry about that, look at my original PC Logic Analyzer program. Got a bit carried away here. Very nostalgic about this sort of stuff, but I just wanted to see if you know, I could actually load and

**Dave Jones:** these files back in and sort of we've got some wins, you know, the PCB and schematic. Yeah, I can um still load those in and edit those and probably import them into a modern version of uh Altium software if I had to. Yes, I can

**Dave Jones:** still run the original uh source code in Borland uh Pascal uh 7, no problems whatsoever. Um but yeah, we failed on the Lattice ISP chips. A, they're dis- physically uh discontinued. You might be able to get old stock, things like that. I couldn't

**Dave Jones:** download the Lattice ISP starter kit software anywhere. Maybe if I tried a bit harder, maybe if I had looked on some old floppies somewhere, maybe an old hard drive or something like that, I might be able to get the original software, but yeah,

**Dave Jones:** I pretty much got screwed on that because A, I used a starter kit, which uh wasn't compatible with Lattice's main uh software, otherwise I could have used their modern um software to do that. I didn't write it in a high uh level

**Dave Jones:** language cuz that's, you know, you didn't need to. It was so small that and the and the software was really good from what I remember. Um you know, the graphical user interface, the schematic, which is what I was familiar with. I

**Dave Jones:** didn't know higher level uh hardware languages at the time. I'm not even sure if it was an option for these Lattice uh CPLDs. Um but anyway, so you know, there's no VHDL or no Verilog that you can import these

**Dave Jones:** days, but the project is so small, it doesn't matter. If you really needed to duplicate this stuff, you just take the schematics that you've got these days and uh you know, just redo it in a modern um FPGA or modern CPLD. It

**Dave Jones:** wouldn't take you days work to, you know, to reconstruct the thing, so you wouldn't bother getting old software and uh stuff like that and trying, unless you were really desperate. It's a very common uh issue in industry is um

**Dave Jones:** support for uh these sorts of um projects and things like that. Um all these legacy projects, a lot of companies they got procedures in place to keep mirrors of old hard drives so that you've got the existing uh software

**Dave Jones:** and things like that. But yeah, well, sometimes you just um you just can't do it. You just you know, you just get stuck with these you know, if you don't put proper procedures in place to uh keep all of this old um software and old

**Dave Jones:** uh development systems and the programming cables and you know, all that sort of uh stuff, any custom programmers, things like that. So, yeah, if you it can be a real issue. So, it can still happen today. You can get

**Dave Jones:** caught out. You design something now with a modern uh chip or a modern micro, for example, might get discontinued. Yeah, you might have the source code in C or something like that. Not too hard to port over, but you know, there's

**Dave Jones:** still lots of traps. If you're doing FPGAs these days, you'll be using VHDL VHDL or Verilog. They're not going to go anywhere. So, you know, in 10 20 years time you'll still be able to recompile uh stuff for those, I'm sure. So, there

**Dave Jones:** you go. I hope you enjoyed that rather long-winded look at one of my old projects from almost 20 years ago. Wow, I've got even older ones in some other places, but it's amazing I even found in my original hand-drawn

**Dave Jones:** images. But anyway, hope you enjoyed it. If you want to discuss it, jump on over to the EE Vblog forum. Link's down below. YouTube comments, blah blah blah. Uh follow me on Twitter, stuff like that. Hopefully, if you've reached this far, hopefully

**Dave Jones:** I'm getting a new look EE Vblog website uh soon. So, probably more details about that on the forum and the blog as uh things progress on that. But that's um yeah, it's due for a revamp. I haven't revamped it Well, I haven't touched it

**Dave Jones:** since I originally launched the blog back in jeez, whenever. How long was that ago? Jeez, is WordPress going to be discontinued? I won't be able to Oh, no, legacy. Catch you next time.
