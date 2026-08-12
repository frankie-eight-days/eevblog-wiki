---
video_id: 9MIzbTpdt80
title: EEVblog #1060 - $35,000 DataIO Unisite Universal Programmer Teardown!
url: https://www.youtube.com/watch?v=9MIzbTpdt80
source: youtube-asr
---

**Dave Jones:** Hi, picture it's in 1980s and all these newfangled programmable devices were coming out. I mean you had always had your traditional EPROMs with the little window on there where you could erase them with UV and you had to program

**Dave Jones:** them, but things like our PLDs started to come out and other one-time programmable microcontrollers started to appear back then, but they didn't have the newfangled flash technology and self-programming and all that sort of thing. And you wanted to program all

**Dave Jones:** these newfangled devices. Well, it was a lot harder back then and you traditionally have maybe, you know, if you were short on budget, you might have a desktop machine that you know, might have had a keypad on it something like

**Dave Jones:** this and you can program your EPROMs and a sort of like a limited selection of programmable devices back then, but what if you're a big company and you wanted to program everything? You wanted one of these newfangled universal

**Dave Jones:** programmers. Well, what did you need? Well, let's check it out. You needed one of these bad boys. This was the standard the Data I/O UniSite universal pin programmer and this thing was the duck's guts probably for probably several decades actually. This

**Dave Jones:** one came out in 1986 and it was the first programmable universal pin programmer with removable cartridges. I'll show you all this in a minute. It all removes out. You could program virtually any device on the market even devices that hadn't been invented yet

**Dave Jones:** because Data I/O were the leaders and they would guarantee that they would add new device support for anything that came out and this puppy could literally program anything with the right type of physical adapter and things like that

**Dave Jones:** and this was the industry standard benchmark programmer to a lot of people that probably still is and it lasted they supported this from 1986 when it first came out, well into the '96 and into the 2000s as well. At

**Dave Jones:** first of all, it started having a data terminal attachment for it. Then they got PIC DOS PC-based software for it. And then they progressed to Windows-based PC software. And they just kept supporting this programmer because the hardware in here was so

**Dave Jones:** comprehensive and so universal. And it could still program almost anything today pretty much as well. But they have dropped Now, I believe they've finally dropped our software support for this. But they kept supporting this device for several decades. And this was the benchmark

**Dave Jones:** universal programmer against which all the others were judged on the market for, as I said, several decades. And if you were serious, if you were sending your, you know, space space probe to Jupiter or something, and you had to

**Dave Jones:** make sure that your devices were programmed correctly, you used one of these babies because this one was a even though it's not like multiple gang and things like that, this was a proper production programmer that would program the devices properly.

**Dave Jones:** Because a lot of these devices had to be If you wanted to actually program and test them properly, you had to program it not only the right voltage using the right protocol and the right signal levels and everything else, but then you

**Dave Jones:** had to verify them at different at the extremes of the voltage rails and stuff like that. And a universal a proper universal programmer like this bad boy could do it all. And I've always wanted to tear down one

**Dave Jones:** of these. I used this in the late '80s and the mid-'90s through to probably the early 2000s at companies I've worked for because it was just like the industry standard programmer. It cost an absolute fortune. But for any big company, this

**Dave Jones:** thing was an absolute necessity. And I can remember, I've never used the Windows later Windows software. I always used the DOS software. I don't think I ever used the terminal one, but yeah, I used the DOS software for this thing and

**Dave Jones:** I have fond memories AND I ALWAYS WANTED TO TAKE ONE APART. BUT, I never I couldn't because it was all you know, it had the calibration seals and everything on it, you know, and and it was like the holy grail bit of

**Dave Jones:** equipment in the company. It had its own section of the lab dedicated and it'd be often run by somebody who knew how to use the thing, you know, sometimes you couldn't just wander up, you know, some Johnny-come-lately come up and oh, I

**Dave Jones:** want to program my chip. It was like, no, you had to find the priest who operated this thing. Anyway, I'm not sure what the price for this puppy was back in the day, but if you had to ask

**Dave Jones:** the price, you couldn't afford it. And it came with like the basic ZIF socket here, but all of these are actually removable. So, we can actually just take these modules out like this. So, this was your basic 40-pin

**Dave Jones:** DIP one, which would you know, if if you had just your DIP packages, that's just fine and dandy. But, you know, if you're wanting to program your PLCC packages and stuff like that, you needed one of these adapters in here.

**Dave Jones:** Look at that bad boy. And we'll take a closer look at these, but yeah, you could actually not only replace that, but you could also replace swap out the entire module like that. Absolutely beautiful. And you could they

**Dave Jones:** made adapters for absolutely anything. And Data I/O were the industry leaders in this and probably still are. I mean, if you want probably the best programmers on the market, you're probably still going to buy them from Data I/O. And of course, companies like

**Dave Jones:** this would like you would have contracts with them and they would guarantee to add support for the parts you wanted and full production support and it was properly done and verified and everything. None of this, you know, Shenzhen market eBay programmers and

**Dave Jones:** stuff like that. The software may or may not work. No, these were fully verified and tested and certified. So, anyway, if you do know the price of one of these back in the day, please let us know and

**Dave Jones:** I've been looking for one of these on eBay for a while, but they're rare as hen's teeth in Australia, but one of my viewers just randomly emailed me out of the blue and said, "Hey, they were throwing this in the dumpster.

**Dave Jones:** Would you And I saved it. I just couldn't let them throw it out. Would you like it?" Yes, please. Thank you very much. So, it comes from a secret squirrel organization that well, shall not be named. It's secret squirrel. Not

**Dave Jones:** only do we have the base unit itself, but we also have another adapter. Look at this. I mean, these things would have cost a fortune back in the day. PGA, the pin grid array. Once you could get all

**Dave Jones:** these different bases. I'm not sure what you know, what they actually ultimately went up to. That's 1991. There you go. Made in the USA. USA. Fantastic. So, that would have cost a fortune and also all these adapters. Look, probably still

**Dave Jones:** unused. How much would these have cost? You know, hundreds of dollars each back in the day, but these were adapters for your different size. You know, if you wanted a 52 pin PLCC, you would buy the adapter for it and just snap it in.

**Dave Jones:** Beauty. So, this was actually a fully self-contained unit. Had its own operating system, ran on a 68000 processor. It's got dual floppy drives here. One, I think you would like use it like the operating system disk actually run it and the other would be the

**Dave Jones:** algorithm disk, the programming disk that you'd actually whack in and you'd actually will see on the back you can hook it up to either a data terminal, an old-fashioned, you know, serial data terminal, or in more modern times a PC

**Dave Jones:** running DOS or Windows software, but it was still completely standalone. You just needed like a terminal to you know, to show you stuff on the screen and say, you know, put in algorithm disk number five that supports the part that you

**Dave Jones:** wanted. I have fun memories of doing that, but I'm so excited. I always wanted to tear one of these things down and this is going to have a lot of switching circuitry. Hence the huge massive size of this because it is a

**Dave Jones:** true universal pin programmer. So, it's going to have like a read relay switching on every one of the pins that you can switch through multiple programming voltages cuz you got to remember, back in the day, you know, these EPROMs could and in fact this one

**Dave Jones:** No, that one doesn't have it, but this one here has the voltage written on it. There we go. The programming voltage 12.5 volts, but of course you wouldn't just program it 12.5 volts. There'll be verification runs at different voltages

**Dave Jones:** and stuff like that. So, you know, um a lot of the even the older EPROMs, they went up to 21 or even 25 volts if memory serves me correctly for a lot of the old school ones. So, this would support

**Dave Jones:** voltages at least up to that and this bad boy, I mean it's shaped like this cuz it's going to have all the cards in here, the pin switching and IO cards, but let's take a look at the back. Look

**Dave Jones:** at this old school DTE Yeah, it's even the switches for DCE and DTE. Hands up if you remember that. Data communications equipment, data terminal equipment. And you could actually hook it up to an old, you know, VT100 terminal and still use this puppy.

**Dave Jones:** Anyway, this one was manufactured in 1987. So, this came out in 1986. So, this is, you know, just a year after it came out. So, it's basically one of the original puppies. Love it. Redmond, Washington. And one of the most

**Dave Jones:** interesting aspects of this was as I said, this removable system like this which was you know, fantastic. And but oh yeah, that do not touch pins. Oh, sorry. I'm going to touch them. I'm I'm brave. Little pogo pins in there. I don't know

**Dave Jones:** why they're not all populated. Maybe if you got more IO cards in there actually, you know, this one it only support X number of pins. If you wanted to buy a like a higher pin count version you could do that and it probably has more

**Dave Jones:** pins and different adapters and stuff like that. But all the little like pogo pins in there. But I always found fascinating one of the most interesting things was actually this pad in here. How would you actually where the

**Dave Jones:** contacts? Where's Wally? Try and find Wally in there. Hmm, I think you can probably tell what's going on here. But you would actually plug in your PLCC chip and it actually conduct through this conducting mat. So you'd have this 44 pin PLCC attachment for

**Dave Jones:** example. That would be a classic one and you just whack it in there like that. Then you open it up and tada! You just actually put your chip in there. So these adapters just had a like a spongy

**Dave Jones:** thing on the top just to put pressure down on the chip and then a certain size window which would then expose contacts on the PCB underneath. You put your chip in there. You'd whack it down like that and it

**Dave Jones:** would conduct through those pads. Let's take a look at those conducting pads under the microscope. Because it actually came with spare ones. Awesome. So check it out. We've got the conductive pad replacement kit and I don't know how much these would have

**Dave Jones:** cost. But yeah, like these things would have you would change these after I think they had like a couple of thousand you know, cycles and stuff. So what it is, let's see if we can go all the way

**Dave Jones:** with LBJ here and see what we've got. It's just like little conductive gold flex or whatever that are isolated, of course, like insulated from each other, but they're just like a random gold flex and you would actually conduct these things.

**Dave Jones:** They would actually conduct through there and connect the pads top and bottom. And that was That was pretty much it. So, it was kind of crude, but very effective cuz I never had any problems whatsoever with the contacts on these things. They were

**Dave Jones:** fantastic. There we go. That's perhaps a more interesting view. You can actually see the conductive paths right through there. That's great. Love it. And then beautiful concept to come up with that. You know, how do you for a universal thing that could connect

**Dave Jones:** to almost any chip using, you know, whether it was PLCC or whether it was, you know, a a land grid array or something, you know, any sort of, you know, even BGA stuff and things like that, you know, with the contacts on the

**Dave Jones:** bottom, you could do anything just using one of these conductive mats. Ooh, look at that. It's a sine wave. Not quite. So, I know you want to see what's under here. So, let's uh take it I'm not sure if this is the

**Dave Jones:** correct technique for taking it out. I'm going to uh I'm going to brutalize it. There you go. And it just had that universal contact type pad and of course all, you know, real top quality gold plating. Ooh, look

**Dave Jones:** at the colors. Beautiful. Um and it did of course you could put any size PLCC on there with that particular uh pitch. And of course, if you wanted a different pitch or a different pin count or whatever it was or a different style

**Dave Jones:** of package, you'd buy another whole adapter like this because well, you know, you got to upsell. But, yeah, these were so professionally designed and manufactured. These things were bulletproof. Worth every cent. And I've been told by Secret Squirrel

**Dave Jones:** that this one is actually faulty, but anyway, we don't care about it working now. All we care about is what's inside this bad boy. You know, we say here on the EV blog, don't turn it on, take it

**Dave Jones:** apart. First of all, we want to see what's inside these. Are there any circuitry in there? Is there any pin protection? Is there any pin driver stuff? Let's find out. Whoop. Whoop. There we go. It fell out. Oh, jeez. Doesn't look to be much in

**Dave Jones:** there, does there? Is that going to Is that going to pop out? Yep. It's all through hole, of course. Oh, no, look at that. Relays. Relays as far as the eye can see. Beautiful. GI Claire. Never heard of those, but they're

**Dave Jones:** obviously going to be uh top quality ones. Data I/O wouldn't have skimped. And we're probably going to find Oh, yeah, relay drivers, classic ULN uh 2803s. They're the ones with the built-in uh back EMF uh diode protection. So, you

**Dave Jones:** got relay drivers, and then just 74HC stuff. Dating from '86 there. Nothing fancy. Oh, that's a bit how you doing. Look at those diode arrays. I I guess you could buy those diode arrays. There you go. So, they would have had like diode

**Dave Jones:** protection on each one of the pins. Wow. Groovy. They obviously had Either they had them custom manufactured for them, or they uh were like maybe you could buy diode arrays in that sort of single in-line package form factor. Ha.

**Dave Jones:** Either way, neat. Of course, that's a uh four-layer board. It's even got the old school uh layer count designator there. 1986 for those playing along at home. And uh got some LEDs, so we got the uh yeah, got the light pipe up there.

**Dave Jones:** Nicely designed. They went to town and uh little little ferrite beads. Geez, they were serious about keeping the AMC out, weren't they? Little ferrite bead in series with every line going to that IO. Anyway, 74 it's just all 74HC. Doesn't look to be any custom

**Dave Jones:** uh PAL stuff on there at all. So, all the magic is uh well, most of the magic This is just like a pin switching your various voltages. Do we have 40? 2 4 6 8 10 12 14 16 18 20 22 24 26 only

**Dave Jones:** 28. Real eyes. Did this one only support a 28-pin device? It's got a 40-pin ZIP uh ZIP socket, zero insertion force socket, genuine 3M text tool. Yes, it is. Oh, 3M. Those playing along at home or your text tool fanboys, you

**Dave Jones:** just know this baby's going to work. It was tested by Doug G. Good on you, Doug. And the main adapter Oh, look at this bad boy. Haha, what a Bobby Dazzler. We've got ourselves some uh Toshiba parts down

**Dave Jones:** here. Now, these would be programmable devices, surely. I mean, oh, look, genuine bodge wire. Look at that. Wow, fantastic. Going all the way with the LBJ up the top. Beautiful. Anyway, that's a chicken and egg thing. How would they have

**Dave Jones:** programmed these things? On the previous generation programmer? And yep, sure enough, these are a Toshiba CMOS gate array chip. So, basically, you know, equivalent to like an FPGA uh these days, one one-time programmable puppies uh no doubt. And

**Dave Jones:** they would have uh I'm sure Data IO being the programming people, they would have used their own hardware to program these. But of course, this was uh fancy pantsy. We're talking uh Look at this, SO package surface mount stuff. For the

**Dave Jones:** most part, the only through hole stuff in this is the connectors and the relays. Awesome. You know, I'm not familiar with that relay off the bat, but no doubt they would have been really good. I'm actually surprised not to find read

**Dave Jones:** relays in here. These look like your traditional mechanical relays, but of course you didn't have to like it's not like they switch these for your data and stuff like that. They didn't need that many cycles. All they were switching was

**Dave Jones:** basically the voltage through to a particular pin. So these would only switch, you know, once or a couple of times during the programming of any particular pin. After that, then they'd actually you know, the data just came through data level buffers and things

**Dave Jones:** like that which they could adjust the level of, but yeah, apart from that yeah, cuz they didn't need high cycle count on these relays, but I'm sure they're top quality. And on the back of the board there there's not a huge

**Dave Jones:** amount. There's just a bunch of resistors. They look like caps, but they're actually not. They're the resistors. We've got a couple of 74 old school 74 LS with a badge resistor on it. No worries. But just a bunch of resistors on there and also I

**Dave Jones:** missed the little individual driver transistors down in there. Little driver for each one. Of course these would all be the relay drivers up well, it's just like serial interface relay drivers with then the individual to drive each one, but

**Dave Jones:** there you go. Brilliant. It's a lot of engineering that goes into that though. Now, I'd be surprised if this puppy wasn't designed to come apart real easy because you could I don't know if it's user upgradeable, but you could

**Dave Jones:** certainly you know, buy the base model and then upgrade it later with more pin card capability and stuff like that. I believe this thing might be fully loaded. So took a little bit of coercion, but there we go. Ah, ah, we're in like Flynn. The

**Dave Jones:** would be moon. I didn't show you THE AWESOME PART. AH, LOOK AT THAT. WOW. Isn't that gorgeous? Look at the pin driver cards. Yeah, this sucker is fully populated, ALL RIGHT. THAT'S PANT WETTING STUFF. Look at it. Beautiful.

**Dave Jones:** Of course, all the pin driver cards are going to be absolutely identical, but there you go. All that processing goodness. Beautiful. Thing of beauty is a joy forever. This is interesting. Property of H&R Inc. Does it Silicon Software? Does

**Dave Jones:** anyone know the story behind this? Obviously, these are the ROMs. A date code of '87 there, even though it's copyright '95. It did they hire Silicon Software to write it? Is it Is it a subsidiary or whatnot? Anyway, we've got some

**Dave Jones:** programmable devices here, and oh, look at our beautiful little bodge there on the pin. Yep, I think we have a genuine lifted pin there. Oh, they've chopped it off. Have they? Beautiful. Oh, remove for kernel test. Interesting. So, we just got some

**Dave Jones:** jumpers in there. More programmable, you know, GAL type devices here. And of course, it's all like 74LS 74HC stuff. Another Another genuine bodge there. Oh, seven except a 74F for the screaming 40 MHz clock on there. That was pretty fast back in the day.

**Dave Jones:** You know, you'd want to use You'd be using your 74F stuff for that. It's into Always interesting to note on these teardowns, which chips have selective sockets on them. Look at this 74LS 245. Not sure if that's a repair or if it's a uh

**Dave Jones:** production mod. I'm not sure, you know. I don't think they would have repaired all those. So, you know, some 74 LS 244s, 373s, classic stuff. 74 LS 86 over there. You got your um XOR gate. And you know, they've got a What? There's a few

**Dave Jones:** of them in sockets. They look to be coming out. Have to go around and give those the old uh press one, too. But uh yeah, they've got a few extras over there. So, they may, you know, decided, "Hey, maybe those ones,

**Dave Jones:** you know, there's advantages to taking them out either for uh testing, debugging, or repair purposes. Maybe they're driving stuff. They expected them to fail or whatnot." Hmm. And the 68,000 fan boys have just creamed their pants, I think. And uh there it is. Oh,

**Dave Jones:** it's all rubbed off. People have been intimate. Hmm. Anyway, that little mod there is on the uh address select pin. So, it's come from this uh 74F over here. Of course, they need to address it real quick. So,

**Dave Jones:** um yeah, they use the F series uh logic. F is fast, if you didn't know. And yeah, so they've like tucked a ferrite bead with a resistor going to there. And of course, you got your classic uh multi-layer board routing here. You can

**Dave Jones:** actually see all the square traces in there like that. All the electrons are going to fall out. This is most likely um auto router cuz no uh self-respecting uh designer would add right angles to their traces like that. And of course,

**Dave Jones:** all the chips are all lined up in the same vertical direction like this. And all the traces, almost all of them, run vertical on the top side of the PCB. And on the bottom side, of course, they'll run uh

**Dave Jones:** horizontal across the board like that. That just gives you your best routing. But look, there's not one of them out of place. I like it. Not one little oddball one mounted at right angles. Beautiful. And that's a six-layer jobbie. There you go.

**Dave Jones:** You can tell by the uh layer count down here. 1 2 and then you can progressively count see them cuz they're on the bottom layer. So, of course, they would have had uh yeah, a huge 5-V rail in there.

**Dave Jones:** So, a dedicated ground, dedicated 5-V. The rest probably would have been uh you might have done uh power routing. Um and they've done some pin routing and stuff like that here on the top. You can see all the uh pins. Looks like you only had

**Dave Jones:** to populate maybe these boards here if you wanted the uh 40-pin DIP interface. But if you wanted the expanded one, don't know where the extra traces are over on this side. But uh maybe they're on different uh layers or something like

**Dave Jones:** that. And that's the reason why you'll find mod wires on these type of designs back then. It was really expensive to, you know, respin these boards. And you'll find issues later. And these things weren't manufactured by the tens

**Dave Jones:** of thousands, hundreds of thousands, or something, you know. So, you could easily add manual uh mods like that at the production stage, you know, little bodges like that. No worries whatsoever. It's cheaper than uh respinning the board, that's for sure. Check out the

**Dave Jones:** beefy power we've got here. I'm just all those pin drivers and all this processing. Um it must take some grunt. And at the bottom, looks like it's just going to have uh power supply in it. Hmm. I don't know. It might be a lot of

**Dave Jones:** wasted volume in here. Although, you got your floppy drives, of course. And very curiously, it also came with this expansion RAM board, too. So, uh I don't know. That mounted under the bottom or something like that, perhaps. Anyway, uh huh.

**Dave Jones:** Someone pilfered the RAM cuz, you know, RAM was expensive back then. Still is. Uh huh, yes. It must uh plug into here and mount under the bottom somewhere. In fact, I can see another board under there. It came with a base amount of uh

**Dave Jones:** RAM. Not sure what it is. But for those playing along at home who love their RAM part numbers, knock yourself out.

**Dave Jones:** But by far the most interesting thing inside this is the pin driver card. Once again, we see that Toshiba CMOS gate array there, but this one dates from 89. Love the right angle dual in-line 0.1 inch header there with

**Dave Jones:** the soldered on boards. They're very rugged. Love that. Yes, it is actually a dual row. It plugs into the second row down the bottom there as well. But these would have cost a fortune and check out the density in this thing. Wow, look at

**Dave Jones:** that. The This is a brilliant layout. So it's hats off to who whoever laid this puppy out to try and get all that density into the like There wouldn't have been much room left. Would have been tearing their eyes out

**Dave Jones:** trying to lay out that puppy. But anyway, very very nice. We've got ourselves uh some power transistors down here. They're 3055. You should be familiar with those. Fantastic. Um they've got some uh just some mylar under there. Insulating

**Dave Jones:** sheet. These obviously aren't dissipating any power. So they're just flapping around in the breeze. You know I don't like TO220s flapping around in the breeze, but yeah, okay. I don't like it. Anyway, they haven't secured them down, but it's

**Dave Jones:** fine. This thing's, you know, designed to sit on a bench, not designed to be moved around and vibrated and stuff like that. And uh but I love the custom heat sink up the top here. Looks like we've got some

**Dave Jones:** IRF97 something or others there. So we've got some sort of uh power MOSFET there. What are these little puppies? They They They drivers? For the MOSFET? Have to look those up. So I couldn't find any data on that. If

**Dave Jones:** I do, I'll link it in later in the edit, but uh anyway, look, they're very interesting. 0.285 ohm 1% resistor. That's obviously some sort of current sense resistor. So maybe this is some current sense amplifier. and look, I

**Dave Jones:** think they've got a guard trace going right around all those top four pins there. So, maybe that's some sort of, you know, amplifier for the They're obviously doing some pin current sensing there. Hmm. And we find these four MOSFETs there.

**Dave Jones:** You got to wonder, is this like a four-channel card? And on the bottom here, they've got another four Look at that. They look like our bipolar jobs. Are they? And yep, that just must be a quad pin driver just based on the configuration

**Dave Jones:** there. And that kind of makes sense because there's actually, well, I was going to say there's 16 cards here, but there's actually 17 cards. So, 16 * 4 is gives you your 64 pin capability. Why they've got the

**Dave Jones:** extra card, I I don't know. 17 instead of 16? Ooh, that creeps me out. But this is just insane. All this to drive four pins. You can see the complexity if you want to do this properly. You know, these universal programmers

**Dave Jones:** these days I've done teardowns of like a cheap $50 eBay one, which is, you know, fine these days, but it just doesn't hold a candle to these, you know, these old-school ones which did it properly. You know, these were professionally

**Dave Jones:** engineered to basically drive any pin at any voltage. AND THAT'S JUST WOW. I GOT TO FIND THE schematic for this and go through it. And aha, as I start to take these boards out, they've all been like mixed and matched, different

**Dave Jones:** flavors. The chip over here is a PMI PM355, and that's a JFET input op-amp. So, that makes sense with the with that guard ring that we saw around there. But uh I've got various uh dates on these, and I spread

**Dave Jones:** in at least a couple of years apart. I don't see any real differences in them apart from um actual, you know, brand differences in the uh chips and stuff like that. Maybe, you know, some part substitutions, but no um

**Dave Jones:** it doesn't look like any uh board modification changes or anything like that. And as uh Secret Squirrel told me, this thing it doesn't actually power up, doesn't seem to do anything. Um so, I've got actually the cards uh removed here,

**Dave Jones:** and let's switch it on. Watch the LEDs over here, and there you go. The power LED just flashed, and that was it. Thankfully, there's some test points here. Just going to test them with all the cards out, so, you know, minimum load on

**Dave Jones:** there. All right, we'll just measure some stuff. Oh. That's already on. Uh well, that's supposed to be a 12-V test point. Definitely got it on. Yep, it's supposed to be a 48-V test point. 5 V. What? Not a sausage. I mean, you know,

**Dave Jones:** if you don't get your 5 V, you're not going to boot. Minus 5 V, and there's a 2.5 V, but they did nothing. And I'm just trying to get this board out here, and as you'd expect with a huge multi-way connectors like these,

**Dave Jones:** when you know, there's a lot of force when you actually press down, you know, and users will just slam them in. These are actually rigidly mounted, so I've taken the screws out of the board. You can see that it's Maybe you can see the

**Dave Jones:** bow on that. Obviously, it's held down with these uh steel pins right at the connector. Nice design. Otherwise, it'd be horrible um uh force on the uh joints and everything else. So, they've done that well. Tell you what, this this whole design's quite

**Dave Jones:** complicated. We've got two dual in-line right angle headers up here going up to this board. Don't know what the hell that thing's doing. Um but, it's good that you don't have to take out the jacks for the D25s,

**Dave Jones:** but you got to sort of, you know, you could easily slide that in and bend the pins or do what not, but uh I don't know. You should like they could have done something else with that board. Ta-da!

**Dave Jones:** Main board out. Oh, I better bloody turn off the power. Here you go. Warning high voltage. Geez, they don't even have a an insulating sheet on that bad boy. But there you go. Nothing at the bottom except as I said

**Dave Jones:** all the traces going vertical, couple of budge wires. But there you go. Yeah, the rest of the pins over here aren't populated? Huh. That's interesting. Are they just like power and other stuff? Maybe for future expandability for a different

**Dave Jones:** motherboard or something perhaps. Hmm. Anyway, that's a big ass board. You certainly need a serious business power supply for a bad boy like this. Look at that. We've got our Nippon Chemicon caps. Look at that. They're all red. They go faster. SXC

**Dave Jones:** series for those playing along at home. Um they all looking uh good nick. All the vents look good. All the vents look good. All the vents look good. All the All the vents look good and uh got ourselves uh some power

**Dave Jones:** along there. There's more power along this wall down here. And uh geez, look at the Look at the compound. It's all over the shop. Somebody had fun. Geez, what did they do? Spray paint that on? Anyway, it's all very neat and tidy.

**Dave Jones:** And we come over. Oh, Sprague. Oh, yes, Sprague. Um the mains filter caps on the input DC rectified side. There's our rectifier down there of course. There's our bridge. And uh everything looks hunky-dory. Um you know, it's not up to modern

**Dave Jones:** standards of course, but you know, power supply from the 1980s. Fuses intact down in there. Um but I don't see any visual signs of uh distress. I don't smell anything. So hmm, why are we getting zero volts out

**Dave Jones:** of this puppy? I don't know. Aha, found out what the back board does. Dead giveaway down in that corner. Look, waveform board. So, that must generate the programming, the required, you know, waveform {slash} you know, in quote marks, programming sequence for

**Dave Jones:** the particular pin that they're currently pulsing. Hmm, that's interesting. It's got a bunch of Yeah, what are those up there? They almost look like memory. SRAM chips? No, those are actually PM7545s. These are 12-bit DACs. So, this can

**Dave Jones:** actually generate analog waveforms, presumably like to control maybe the slope of That's a, you know, that's a pretty over-engineered way to do it. Maybe the like the slope of the programming pulse or something like that, because Or is it, you know, truly so universal

**Dave Jones:** that it supports weird-ass analog things? I don't know. Anyway, that that dates from copyright '85 down in there. It made in USA. And down in here, we've got some Analog Devices AD7226s. They're a quad 8-bit DAC. So, I

**Dave Jones:** DACs all over the place. It's full of DACs. All right, let's have a quick look at the schematic for the waveform generator here. It's three pages. Check this out. But let's go up to the first page here, up here in the corner. We've got

**Dave Jones:** ourselves the voltage references AD851 and the usual transistor driver for that. No wackers. We've got some 0.5% resistors. Like doesn't have to be hugely or 0.1%. You know, it doesn't have to be hugely accurate. But yeah, I would figure yeah, if you're designing

**Dave Jones:** something like this, you know, you want to be 5. Oh, you know, you want to be a 5-V supply plus minus .1 or or something like that. Anyway, here's our two DACs, uh 7545, and we've got a Looks like we've got a

**Dave Jones:** transistor output driver here. Check it out, 29 um 05s, and then they're just then they're driving uh some higher power ones. So, this is for yet the device under test VCC. So, that's the VCC for the chip, and uh VCC sense. So,

**Dave Jones:** we're sensing that back, are we? What the Yeah. Geez, that's serious business for generating, you know, this all this just to generate the 5-V the VCC rail for your device under test. Amazing. Then, we've got three more DACs here

**Dave Jones:** generating three different reference voltages. Um where are these? Power bus, comparator bus, analog bus. What the Okay, so it's the analog bus that contains the device under test VCC and all the different reference voltages generated from these three different

**Dave Jones:** 12-bit DACs. Wow, unbelievable. Let's go down to the overvoltage crowbar. Look at that. Where's that? Where's that between? Uh 42 V. Okay, so that must be the absolute uh maximum capability of this thing. Anything over that, it will

**Dave Jones:** absolutely clamp it down with a proper crowbar. Just turns on the uh SCR, and and, you know, just shorts everything out to protect your device under test. Beautiful. So, these are our positive and negative supplies, are they? Plus OC, minus OC.

**Dave Jones:** What? Local high and logic low supplies. Okay. So, these must be the voltages for the the the logic levels of the device under test. So, if it's a 3.3 V part, for example, then they're obviously generating those, by the looks of it.

**Dave Jones:** Plus 21 V. Uh fine current clamp. So, it's got all these current references. FCLR. So, what can it drive? It could drive constant currents into pins, presumably. That's amazing. Unbelievable. Overcurrent integrator, slew rate reference. So, it can actually

**Dave Jones:** control the slew rate. That's so not unexpected to be able to control the uh slew rate. I think I might have mentioned that uh before, the ability to uh do that on the um a programming uh rails. And of course, current supply.

**Dave Jones:** Wow. That's great. That is unbelievable. So, all that that waveform board just like that's got more in it than what, probably any other universal programmer currently on the market, except for, you know, the ultra high-end ones. Unbelievable. And here we

**Dave Jones:** go. We've actually got the description in the maintenance slash service manual. The primary function of the waveform board is to produce several individually controlled voltages for use by the pin drivers. These voltages provide the pin drivers with power to operate, to serve

**Dave Jones:** as reference levels, to control the pin drivers, and provide voltages which are either re-regulated and applied to the part being programmed or switched there entirely. Hm. That doesn't tell you much, does it? So, are these all the different uh

**Dave Jones:** levels that it can generate? Still doesn't really raw voltages. Wow. I'll have to link in all this stuff down below. A great bedtime reading. There you go. You can read that to your heart's content the functional operation for all this stuff.

**Dave Jones:** They don't make them like this anymore. And just look at the capability they've added here. The FCLC power supply is to set a clamp voltage on the pin driver's output when the pin driver's fine current source is sinking

**Dave Jones:** current. Unbelievable. Like you know, 99% of the devices out there will not need this to be able to actually program them, but it this is a true universal programmer. And then the other one is for the fine does the same

**Dave Jones:** similar thing but for the fine current source. Unbelievable. And you know, they've got 12-bit DACs to do this. And then they've also got a dedicated clamp voltages well so that that's what those diodes were on the you know, those

**Dave Jones:** single inline package diodes were to clamp the individual pins. They actually program the voltage that goes onto the common of those diodes so that the pins cannot go like 0.6 volts above whatever you program the clamp voltage to be.

**Dave Jones:** That's fantastic. And it looks like the power supply is from computer products Boschert Incorporated certified by manufacturer to comply with IEC 348. Thank you very much. So I did a quick poke around in the power supply and cleaned it up and I've

**Dave Jones:** put it back. There wasn't anything obvious. So that'll have to be a separate video troubleshooting that cuz I'd love to get this baby up and running cuz I have no doubt all the digital stuff all still works. All the pin

**Dave Jones:** driver boards it still work. I have no I no doubt if we got the power supply up. Pretty confident this sucker would you know, still work. Floppies, yeah, they're pretty reliable. 720K floppies in there. It's still work a treat. And

**Dave Jones:** if we actually have a look at the the newfangled task link software cuz it didn't always use this task link software. I don't know where they got that name from, but uh it used to use the high-rise uh software it was called.

**Dave Jones:** That's the one I used uh back in the day and that was um not any terminal, but like a DOS-based uh software. Anyway, you could also get uh TaskLink for DOS as well and then they progressed over to

**Dave Jones:** Windows. And this software supported the different systems, of course, and the UniSite uh stuff down here. And this uh software dates from '97. This is version uh 3.1 or something like that. But if we go in and we actually select device,

**Dave Jones:** it's actually quite uh telling in what it supports here. I mean, let's go down to something that might be familiar to you youngsters out there, which would be some Microchip stuff, for example. So, these did support uh micro

**Dave Jones:** uh control Can I just type in Microchip? That'd be easier, wouldn't it? Um Microchip, there we go. And it did support Microchip uh microcontrollers as well as Microchip memory and uh as you know, E-squared PROM and EPROM and

**Dave Jones:** everything else back in the day. And you'll notice that they're all like uh the 16C They're all the C versions. There's some of the uh E-squared PROMs, I believe there are. But uh yeah, there's You'll notice that there's what's missing is

**Dave Jones:** some of the new um F series stuff, which of course use, you know, there's a 17 series, but they're all the C the um one-time programmable or uh the either the one-time programmable type or the reprogrammable uh type E-squared PROM version. Um so,

**Dave Jones:** they don't support any of the flash stuff because that's I think Was there one there? Oh, there was a couple. Okay, the 16F84 was basically the first uh flash programmable micro on the market, I think. Um and it's the one that, you

**Dave Jones:** know, changed everything. May Basically, make microcontrollers what you think of them today with the building reprogrammable uh flash memory. And that's pretty much when you know, and just the Microchip parts, but other types of microcontrollers started getting their own built-in uh

**Dave Jones:** programming stuff. So, you didn't have to apply a high voltage external pulse like you did with some of the early 16 uh C series PIC stuff. You had to actually apply a higher voltage. You couldn't just program them with your 5 V

**Dave Jones:** or your 3.3 V system voltage. But, once they changed over to the flash memory, and they had built-in uh boost voltage, you know, it just took care of everything for you inside the chip. And all you did is you hook up

**Dave Jones:** your 5 V or your 3.3 V signal to there, and you know, Bob's your uncle. It You could program this using a $10, you know, serial parallel adapter or uh something like that. You didn't need these big universal programmers that

**Dave Jones:** knew how to test these things over uh you know, at the right voltage with the right algorithm and everything else. Everything else was every the programming stuff was all handled inside the chip. So, that's pretty much when these universal uh programmers became

**Dave Jones:** less relevant in terms of uh being able to actually um properly support the algorithms for all the different types of uh chips and the both voltage and data algorithm type stuff. So, yeah, that's pretty much where it ended. You know, but apart from

**Dave Jones:** that, you probably wouldn't notice anything different with the uh universal uh programmer software that you'd get these days for your cheap, you know, $50 programmers and things like that. It has the um the you know, step-by-step processes, the blank check, the uh

**Dave Jones:** program device, and device, and stuff like that. But, in the case of these universal programmers, it could actually put when it verified, it could actually put extremes of the uh voltage rails in there and verify it over a much wider

**Dave Jones:** range and things like that. So, yeah, this thing was the duck's guts back in the day. So, although you can buy universal programmers these days in {quote} marks, they're not quite the same thing as these old-school universal programs,

**Dave Jones:** which could generate almost any voltage and put it onto any pin in any configuration and things like that. This thing wasn't necessarily the fastest thing out there, not by a stretch, but if you wanted to program a device

**Dave Jones:** properly and have it guaranteed certified reliable, then this was the way to do it. So, there you go. I hope you enjoyed that vintage teardown of the classic Data I/O Unisite programmer. And this baby was the reference standard for

**Dave Jones:** several decades. Unbelievable the support that they had behind this and unbelievable the amount of effort they went to do design a true universal programmer. Oh, you know, that's just four channels. Like compare that with a modern teardown of a little tiny

**Dave Jones:** universal programmer I've done that you know, which is okay for today's modern devices, but you know, if you truly want to cover everything on the market from you know, the 70s onwards, um then I only something like this would

**Dave Jones:** do the job, really. Um but as always like you know, you can get similar capabilities to these these days as technology has marched on. You can you know, you get this in a smaller form factor USB interface all the rest all

**Dave Jones:** the works and stuff like that. But you know, modern devices you know, you don't need to program and program them with you know, 20-something volts and stuff like that. So, it's a little bit different. It's sort of like a backward

**Dave Jones:** compatibility thing. But you know, if you want to program modern stuff, then you know, just this little mini pro that I've done a video on teardown on or something like this, you know, well on one which are universal programmers for

**Dave Jones:** modern devices don't have nearly the same capability as something like this. But for modern stuff, more than good enough. It's all in the software pretty much. You know, the interface to actually drive the chip isn't isn't that hard at all. Just a bunch of serial

**Dave Jones:** drivers and uh and whatnot and uh Bob's your uncle, but yeah, you can't beat that. That was the duck's guts and to a lot of people it still is. Hands up if you had one of these hands up if you

**Dave Jones:** still use it. Or maybe a later variant of it. Discuss down below and as always if you liked it, please give it a big thumbs up. Catch you next time.
