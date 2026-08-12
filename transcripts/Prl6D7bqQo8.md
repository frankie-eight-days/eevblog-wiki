---
video_id: Prl6D7bqQo8
title: EEVblog #116 - Retro Teardown - Tandy Radio Shack TRS-80 Model 100
url: https://www.youtube.com/watch?v=Prl6D7bqQo8
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 35, "3": 56, "4": 69, "5": 83, "6": 101, "7": 119, "8": 136, "9": 157, "10": 170, "11": 187, "12": 206, "13": 221, "14": 236, "15": 250, "16": 263, "17": 279, "18": 295, "19": 312, "20": 331, "21": 350, "22": 368, "23": 384, "24": 402, "25": 412, "26": 431, "27": 448, "28": 463, "29": 480, "30": 502, "31": 520, "32": 537, "33": 552, "34": 565, "35": 580, "36": 598, "37": 614, "38": 630, "39": 652, "40": 674, "41": 692, "42": 707, "43": 721, "44": 739, "45": 754, "46": 769, "47": 783, "48": 798, "49": 812, "50": 832, "51": 848, "52": 869, "53": 887, "54": 906, "55": 922, "56": 938, "57": 956, "58": 975, "59": 988, "60": 1002, "61": 1017, "62": 1036, "63": 1054, "64": 1067, "65": 1083, "66": 1094, "67": 1109, "68": 1124, "69": 1138, "70": 1159, "71": 1174, "72": 1188, "73": 1202, "74": 1216, "75": 1231}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's product teardown time today. Yes, not product review, cuz I I didn't really think it was appropriate to

**Dave Jones:** review this particular product because quite frankly, it's 27 years old. Older than a lot of you kitties out there watching. What is it? Well, it's the classic Tandy 100 notebook computer. Woohoo! Check it out. Isn't it sex on a

**Dave Jones:** stick? Really, this is the original 1983 Tandy 100 uh designed and built by Kyocera in Japan, but uh Tandy bought the rights to it and it was phenomenally successful as the Tandy 100 and later the Tandy 102. Um

**Dave Jones:** and it was the last machine It was the last computer that Bill Gates actually wrote a good lot of the code for. So, this has got Bill's code in it, believe it or not. There you go. So, I thought

**Dave Jones:** we'd take a look at it and uh see how technology has changed or see what technology was like back then, the electronics and the design and build quality of the Tandy 100. Now, I thought this was a pretty

**Dave Jones:** appropriate product because it is essentially the world's first notebook/laptop computer and it was phenomenally successful. It sold like over 6 million units of this thing. Unbelievable. It had an unbelievably long life all the way through the '80s and even into the

**Dave Jones:** '90s as well. So, what are the specs on this bad boy, I hear you ask? Well, it's got an Intel 80C85 processor. That's the CMOS version of the classic uh 8085. It's got 24 kilobytes, a whopping 24 kilobytes of

**Dave Jones:** static RAM memory. That's That's kilobytes, kiddies, okay? Not megabytes or gigabytes, okay? 24 kilobytes of memory. The processor runs at a scorching 2.4 megahertz. Can you you believe it? Megahertz. Woo! That's really screaming along. Um it's got a

**Dave Jones:** 240 by uh 64 mono LCD display that could display 40 characters by eight lines. Um it's got an RS-232 interface. It's got a printer interface. It's got a a 300 baud modem. That's 300 bits per second, okay? Not megabits per second. That's bits per

**Dave Jones:** second, kiddies. Um it's got a cassette port. Um it you it could have external um uh floppy drives, as well. I think they s- uh uh stored a whopping like 160 kilobytes or something like that. I'm not sure. Uh

**Dave Jones:** it's got a barcode wand interface, and it's got a full-size QWERTY keyboard with excellent tactile feel. And really, uh it runs from four AA batteries in the back, standard AAs, for 20 hours. Can you believe it? It got a 1-month standby

**Dave Jones:** on those batteries, and it was instant on, instant off. None of this booting up Windows rubbish, okay? Instant on, instant off. Fantastic. And really, it's no bigger or um heavier than today's notebook computers. Fantastic. The one I've got here has got 24

**Dave Jones:** kilobytes of RAM. It is expandable to 32 kilobytes, but this one had a retail price when it launched of 1,400 US dollars. That's 1983 dollars. So, well, do the conversion to today's dollars, but yeah, it was an amazing machine for

**Dave Jones:** its day, the world's first notebook computer. And you know what we say here on the EEVblog? Don't turn it on, take it apart. I'll just do a quick uh overview of it here. And here's the power switch on the

**Dave Jones:** side here and switch it on and it's instant on. Check it out. And there it is. It's It does have the Y2K bug. Okay, cuz it only stores the year as two digits. But there it is, copyright Microsoft. Here's the main menu. You can

**Dave Jones:** go straight into the basic in here. And there it is, TRS-80 Model 100 software. Copyright They didn't want to put the use the whole word copyright cuz that uses a couple of more bytes of memory. Can't have that.

**Dave Jones:** Can't just be pissing away a couple of couple of bytes of memory like that. So, copyright 1983 Microsoft. This one's 24 kilobytes. So, we've got 21 thousand 161 bytes free. And the QWERTY keyboard on it is is really just

**Dave Jones:** beautiful. And it still works perfectly after 27 years. It's got function keys. It's got caps lock. It's got you know It's got everything, kiddies. It's even got cursor keys. Fantastic. It's got a memory power protect switch here. So,

**Dave Jones:** you can actually protect the memory. You can actually back up the memory and switch it off. It uses four double A's down here. Just standard double A's. No problems at all. It's got an internal Let's pop this open here. It's got a

**Dave Jones:** little expansion port which has a couple of access for the for the extra ROM modules you can actually plug into it, which is rather neat. It's got a built-in Here it is. It's got a RS-232 port. It's the big old DB-25 cuz they

**Dave Jones:** didn't have didn't use the DB-9s in those days. They had the 25-pin ones. The the Centronics printer port, a modem port, a standard It uses a DIN socket and the cassette interface which goes to a cassette recorder for storing and loading. Really

**Dave Jones:** neat bit of unit. Now, it's got direction and ACP for the modem answer and originate modes. There they are. This is the barcode wand interface. There it is. It's a D9. Um And on the side, you've got DC power

**Dave Jones:** input, the display the display contrast. There it is and the on-off switch and that's it. Really nice functional unit. Okay, let's crack it open. Now, to open it up, there's just four screws here, here, here and here. It's

**Dave Jones:** got these nice little rubber feet on the bottom so it sits on the desk nicely. They're threaded machine screw ones into brass inserts, very nice. And then you just pop off a couple of these little clips around the edge here.

**Dave Jones:** So, let's pop a few of those off and bingo, here we go. Here it is. Tada!

**Dave Jones:** And that's the keyboard and LCD, but here's what we want to see. Here's the guts of it. Check it out. Ah, isn't that retro porn for engineers? Brings a tear to the eye. It really does. Now, I'll show you the board closer up

**Dave Jones:** later. We'll go through it in detail, but as you can see, it's separated into two basic halves here via a standard 0.1 inch ribbon header. Classic. Absolutely classic build and some standard Molex connectors here going over into It looks

**Dave Jones:** like they're soldered directly onto the keypad board here. The keyboard circuitry. There's the LCD. It's its own separate unit up here with quad flat packs, which we'll go into. And then you've got the main processor board here, which is only a two-layer job,

**Dave Jones:** which is actually quite remarkable to actually get the layout on there, and it's totally old school. It's totally late '70s, early '80s build quality using off-the-shelf parts. I love it. Okay, let's take a look at the main processor board. Here's our classic

**Dave Jones:** 80C85 CMOS processor. Here's the the 6102 UART chip. You remember back then you had to have a 40-pin DIP chip just for the UART. Classic. And the 81C55 PIO chip, which actually interfaced to the micro to allow you to do the

**Dave Jones:** peripheral input and output and all that sort of functionality. Now, here's your RAM modules down here into 8 kilobyte chunks. Now, this is actually quite remarkable because this uses like a hybrid technology, which in its day was was actually was was pretty novel cuz

**Dave Jones:** normally you would just put in one of these DIP one of these 28-pin DIP style CMOS chips, but they haven't. They've actually gone for this hybrid module, which converts the two SO package chips into it into the standard DIP

**Dave Jones:** configuration. And they've done that three times. This one has 24 kilobytes of RAM, and there's the optional 8 kilobytes which you can plug in. And as you can see, there's your main processor crystal over there. There's some They've got some discrete uh

**Dave Jones:** point-to-point wiring going from here over to here. I'm not sure what that's actually for, but look, there's a little dodgy resistor in there in some heat shrink. Check it out. There's actually It's It's been heat shrunk and put in

**Dave Jones:** there as some sort of I don't know Well, it's not an Well, the the resistor looks like it's probably a mod, but there's but those connectors are there for a reason. And you'll notice everywhere on the board it uses standard 4000 series

**Dave Jones:** CMOS devices. You can still buy them today in the same packages doing the same job, and they're just all over the shop. 4000 series CMOS and some TL074 op-amps up there which we'll go into, but look at that. 4000 series everywhere

**Dave Jones:** you look. You just They're They're just all over the place. Now, down in this corner over here, check out the real-time clock. There's the 32 kHz real-time clock crystal, and they've gunked it in there. They've They've actually put that that

**Dave Jones:** gunk glue. That's not like a battery residue or something like that. It looks pretty ugly, but that's just old-fashioned gunking stuff that they've used to just, you know, pot all the components to hold that crystal in place. And as you can

**Dave Jones:** see, they're all standard 4000 series CMOS, but there's your timer chip. There it is. That's your clock timer chip, which is right next to the crystal, but 4000 series CMOS again. Some standard SIP resistor networks and standard quarter-watt axial resistors for

**Dave Jones:** everything. I love it. And the bypass caps are all standard disc ceramics. They didn't have, you know, surface-mount ceramics back in those days. You used the old DIP um the old radio disc type devices. And you've got more 4000 series

**Dave Jones:** CMOS. There's your power supply over here. Now, take a look at the power supply circuitry all around here. And here's the schematic of it. Look. Check it out. How old-school is that? All discrete transistor solutions. There's a transformer there. There's So, they're

**Dave Jones:** using this as a switching regulator using discrete parts. I love it. There's a 4A13 down there for the reset. That's part of the uh reset uh circuitry. And it's just quite, you know, really old school. Now you would do that with one

**Dave Jones:** of those uh single chip DC-to-DC converter solutions, of course. But, you know, switching at uh you know, a megahertz or something like that, really efficient devices. But, back then, that's how they did it. Now, if we hold the board up to the

**Dave Jones:** light here, as you can see, it's a double-sided just a standard double-sided layout. There's no inner power planes in there at all. It's all done as a double-sided layout. Brilliant. My hat's off to uh presumably the guy, I don't mean to be

**Dave Jones:** sexist, but uh very few women were actually doing stuff like this back then. So, it probably would have been a guy at Kaypro who laid out this board. I'm sure he put a lot of pride into it. And just fantastic. I love it.

**Dave Jones:** And all this circuitry around here is the modem and the cassette uh interface up here cuz the cassette interface has to handle the modulation and demodulation of the uh serial tape signal, which went to the cassette tape recorder. And then the modem has to

**Dave Jones:** handle um the isolation and um and the regular stuff that a 300 baud modem did. Now, as a comparison, here's one 20 years later. This is from a uh notebook. This is a This is a um pretty much a

**Dave Jones:** top-of-the-range modern modem 20 years later. So, as you can see, all the uh isolation and it has to meet all the much stricter requirements these days. There it is, up close. Much stricter requirements. And uh as you can see,

**Dave Jones:** it's come a long way in 20 years. And this is only 300 bits per second. It's remarkable. But, look at the amount of circuitry. There's actually not that much circuitry in there. It looks like it because there's lots of discrete

**Dave Jones:** resistors, uh diodes, uh the uh caps, and the op amps here and stuff like that, but really ultimately there's not much circuitry in there at all to give you a complete 300 baud modem and um and serial cassette recording interface.

**Dave Jones:** Now, a thing to remember with boards like this uh back in early 1980s, you could do four and more layer boards, but they were prohibitively expensive for a consumer item like this. So, it it would have been a major design

**Dave Jones:** requirement to fit all this circuitry onto a double-sided uh a single double-sided board. Uh single-side load, all actual components, dip through-hole component circuitry using off-the-shelf parts cuz there's no custom devices on here at all. There's no custom ASICs, not a thing. It's all

**Dave Jones:** using off-the-shelf parts. Effectively, anyone could have built this uh back in 1984 using all these off-the-shelf components. But, of course, the uh computer-aided uh CAD technology wasn't wasn't really around back then. Or it was, but it wasn't really affordable for

**Dave Jones:** the individual to use, not even close like it is these days. And it's just remarkable how they've actually um built a mainstream consumer product like this just using all standard off-the-shelf components of the time. You don't see that these days. Very few modern

**Dave Jones:** consumer items will be made using just regular off-the-shelf components because it can't because you can't meet the form factor requirements, you can't meet the power requirements, and all that sort of stuff. It's, you You it's unthinkable to do an iPhone or something

**Dave Jones:** like that using off-the-shelf components these days. And there we have the backup battery for the CMOS memory, so you could actually remove the batteries, you could replace them, and it would still retain all of your contents, no problems whatsoever.

**Dave Jones:** But, as you can see, there's lots of even 27 years later, all these electrolytic capacitors, none have leaked, none have bulged, nothing like that. They're still all in remarkable condition because they actually made them properly back then. Whereas, now

**Dave Jones:** the market's flooded with one-hung low brand, you know, capacitors that fail. Everyone's familiar with failing capacitors in consumer products these days, but this still works perfectly 27 years later. And I'm sure it'll still be probably working in another 20 or 30 years as

**Dave Jones:** well. You'll probably be able to switch it. Well, I don't know, maybe not. You might have to replace a few caps after after 60 odd years, but still, it's in remarkable condition, and it still works a treat. I love it.

**Dave Jones:** And the other thing to remember with boards and layouts like these, these double-sided boards spread all over the place. They've got Yeah, they've got ceramic bypass caps everywhere, but really, you know, layout wasn't critical back then, not even close because this

**Dave Jones:** thing only runs at 2.4 MHz. You could brutalize the layout back then, have it as big as you want, big inductive traces all over the place, and it really wouldn't matter a rat's ass. The thing would pretty much still work. It's

**Dave Jones:** brute-force engineering. Now, here's something I find really interesting. This is the LCD display board. Check out how many drivers they need for the 240 by 64 LCD display. There are two things I find remarkable about this. One is that it

**Dave Jones:** actually uses quad flat pack technology, which was fairly advanced back then. It was fairly fairly novel. And also, check it out. They've actually flipped this one these ones up the top these top row upside down. It's the same chip, but

**Dave Jones:** it's it's actually they've actually done a cutout in the board. They've actually routed out the board. It's been cut out, and they've flipped that chip up and they've flipped it on its back and soldered it on the underside like that.

**Dave Jones:** It's brilliant. It's absolutely brilliant. Why they've done that is because it makes the PCB layout possible using a double-sided board. So, if they had to flip these top row of chips up the other way just like they do with

**Dave Jones:** these ones here, then they wouldn't have been able to fit this Well, they would have had a lot harder time fitting this on a double-sided board with routing space and all that sort of stuff. And because they would have had to have a

**Dave Jones:** lot more uh vias and all sorts of things. So, that was a really novel technique a novel layout and manufacturing technique to lower your cost. One of the things I found really remarkable about this wasn't so much the

**Dave Jones:** computer itself, which is great, but was the documentation that came with it. And the kind of documentation they did back in those days I'll add a link to the service manual for this thing. It has the complete theory of operation. It's

**Dave Jones:** got all the schematics, the bill of materials, the the PCB layout, all sorts of stuff. It's all in there. And it was written by people who knew what the hell they were talking about. It was written by the engineers who designed it most

**Dave Jones:** likely. And it's just remarkable documentation. Check it out. So, there you go. I hope you enjoyed that trip down electronics and computer memory lane there. I thought that was rather fascinating. Just the construction, the double-sided boards, the all discrete circuitry they did back

**Dave Jones:** then, and just designing a real winning product like this that that lasted for almost more than a decade in the consumer market. It's really remarkable. You hardly get that uh these days, but you know, over 6 million units sold, and

**Dave Jones:** it was designed to meet a need, the world's first notebook computer. Look at it. It's tiny. Really, back considering the computers which were back in those days, and it did its task and did it well. Sure, it's only got, you know, 24

**Dave Jones:** or 32 kilobytes of memory, but hey, you know, it's got a 20-hour battery life from a set of double A's. It lasts a month on standby. Really practical stuff that you're struggling to even get these days. Show me a notebook computer with

**Dave Jones:** 20 hours life these days. And really, back then, before the information revolution, you know, all you wanted to do was type a document or something like that. It's not like you could play video games and surf the web. And well, you

**Dave Jones:** know, this did the job and did it perfectly. And you can't type more than 32 kilobytes of stuff in a day, really. So, it was remarkably practical. I love it. I wish people would just design things simplistically like this these

**Dave Jones:** days. Bloody iPhones. See you next time.
