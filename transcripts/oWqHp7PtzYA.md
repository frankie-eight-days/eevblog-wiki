---
video_id: oWqHp7PtzYA
title: EEVblog #860 - Mailbag
url: https://www.youtube.com/watch?v=oWqHp7PtzYA
source: youtube-asr
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. Let's get straight into it. This one comes from Martins's Lazden's from Latvia. Hi to all my Latvian viewers. The name rings a bell. I think uh Martin might be having Martins, sorry. Might be having a second

**Dave Jones:** suck of the Sav. Now, what's the deal with this uh plastic? I'm not sure. Let's go. What do we got here? It's a super [Music] something. We have foam. More foam. A board. Whoa. There's a note in there. Read that in a second. This looks

**Dave Jones:** like a huge board. Looks like a board. Feels like a board. Whoa. Hang on. This is a monster. Wow. Hate these. They've always got sharp pins on the back and everything else. Wow. Look at it. Four processor server motherboard. Wow.

**Dave Jones:** What a beast. Um I believe it's um faulty. Jeez. How many memory slots? two, four, six, eight for each processor. And wow. Wow. What a beast. I don't even know what size that would be. Is that like is there a

**Dave Jones:** um like a like an industry standard for this particular size motherboard? There probably is. I don't know. Sorry. I'm not into server motherboards and whatnot. So, it probably takes, you know, Xeons and or whatnot. So, wow. Thank you very much, Martins. Very nice.

**Dave Jones:** We'll take a quick look at it. Aha. I was just about to say that Martins was uh the one who sent me my Zeon motherboard that um he he says um that he sent sometime sorry it um plus the

**Dave Jones:** Xeons was not able to fulfill your rendering needs. It actually was. I'm using it. Um it's unless somebody sent me two Zeon motherboards. Anyway, yes, I am certainly using the dual processor uh Zeon motherboard. But I think somebody

**Dave Jones:** else sent me uh some Xeons as well. And somebody else sent me some memory. And I've done a video actually building my um Xeon uh rendering machine, which is what I use for rendering here. Um a lot of the limitation for my rendering

**Dave Jones:** actually comes down to various software and codecs and things. Um, but no, the uh the dual Xeon processor machine that I'm uh currently using is a beast and it renders very quick in terms of well at least for doing things that can actually

**Dave Jones:** use all the multiple cores properly like uh Handbreak for example um doing uh transcoding instead of video rendering from my Sony uh movie studio/ Vegas editing uh software but and which is a bit slow when I'm doing 50 frames per

**Dave Jones:** second like you're probably watching this one Um, but that's a codec issue, not because it can't utilize all of the Xeon cores. So, um, but Handbreak, it's super quick. So, thank you very much, Martin. Well, check out this beast. It's a super micro H8

**Dave Jones:** QG6-f for those playing along at home. Yes, I'll link in the data sheet and all the paraphernalia down below, but oh, let's have a quick look at it. Um, for processors, no, this is not a Zeon. As I

**Dave Jones:** guessed before, it's actually a um G34 uh socket here. That's for the AMD Opteron 6000 series processor. What ones it actually uh supports? I don't know. Whatever. And we've got eight dim slots per processor for a total system memory

**Dave Jones:** of 1 terabte. What would you need that for? H I don't know. But obviously, this isn't your standard desktop or gamer PC. It's designed for server stuff which can utilize all the cores, high throughput, all that sort of jazz. Um, standard uh

**Dave Jones:** PCI Express um over here and basically well there's you know like the CPUs do a good chunk of this. I mean it's basically these days I mean all you got is the CPU of course in this case four

**Dave Jones:** of them. Um you've got two Northbridge processors. These are AMD ones um SR 5690 and SR5670. Not sure of the exact differences uh between these two. Haven't really gone into it. Anyway, so they're the north bridges. Um our uh south bridge is here.

**Dave Jones:** This little puppy, this poor little sad thing under here, which doesn't get a fan. Oh, why are these ones so special? And we've got a Novaton um baseboard management controller up here. A gigabit Ethernet controller here. It's got 2 GB

**Dave Jones:** Ethernet ports on the thing. And uh this is your um SAS RAID uh controller down here. Look at how many 2 4 6 8 10 12 at least 14 Sarda connectors. Unbelievable. And pretty much, you know, not a huge amount else. It's just

**Dave Jones:** really, you know, support stuff, uh power things, which we'll have a closer look at. Look at the amount of um extra power connectors on here. It's I don't know what the total power consumption of this thing, but it's an absolute beast.

**Dave Jones:** And if we have a look at the back here, not a huge amount on it. There's uh some support stuff over here. Um it looks like there's some sort of interface driver over there. Um level translator, something like that. But uh yeah, it's

**Dave Jones:** basically just like huge amount of controlled impedance uh routing. As I've um mentioned in many videos, of course, you can see all the comp controlled impedance differential pairs going in here. This is why they're all funny and snaking. know somebody wasn't drunk when

**Dave Jones:** they actually laid this thing out. They're length matching all of these and that's the way they length match. They add little wiggles in there. And then you've got things like the under the memory here. They got massive ground

**Dave Jones:** planes under there. Even though this is going to be like a I don't know like a 12 layer board. I'm something. I'm not sure of the layer count on this beast, but it's going to be absolutely enormous. But they put those whack on

**Dave Jones:** the bottom of the uh dim modules. And over here we got some more routing. Um, this one curiously has routing through like half of the dim uh dim connectors here. You can see see all the via you can see all the vas there from the dim

**Dave Jones:** connector. They're surface mount. Of course, they're not actually through hole. So, um, but yeah, they decided we need some routing here and oh, we don't need any routing here. So, oh, let's just whack in a ground plane. These ones

**Dave Jones:** over here didn't need it, but uh obviously these ones up here did and another one over here didn't. So, that's all just a part of your layout considerations and things like that. There's our PCI Express slots over here.

**Dave Jones:** More stuff coming down. Look at it. Oh, beautiful. There's that. Uh that's probably a level translator. Looks like an IDT one. No, Cypress. Is it? I can't see on the screen here. Anyway, um power down the bottom, but a bunch of

**Dave Jones:** miscellaneous stuff. They're going to That looks like some uh power control um DC toDC uh converter logic down there. So, let's have a look at the power supplies. And a massive critical part of getting a huge system uh board like this

**Dave Jones:** working is the power supplies. And look at these. They've got uh these are all separate DC toDC converter chips. I haven't looked up the uh part number, but of course, they did giveaways. Look at these big inductors here. And uh

**Dave Jones:** we're going to have they're probably uh polymerbased electrolytic uh caps there. We got our diodes over here. And there's a whole bunch of these. And there's just banks and banks and banks of these. What have they got? You know, how many of

**Dave Jones:** these do they need per CPU? Are these powering just the CPU? Some of them may be uh separately powering the memory, the dim modules perhaps. I don't know. We can actually flip this board over and I'll show you those. There, the ones I

**Dave Jones:** we saw before. There we go. They got some additional controllers on the bottom there. Wow. And there's just like I don't there's like half a dozen banks of these things. So I'm not entirely sure how many rails the uh AMD Opteron

**Dave Jones:** processor takes and whether or not they're all dedicated to those. But yeah, I mean each processor has its own bank. There we go. Another one up there. There we go. Looks like we got some regulation under there. And over there.

**Dave Jones:** Tons of it. We got more down here. These will be powering the uh north bridge here. Wow. Power everywhere. Powers everything. And there's the socket for you socket aficionados. Oh, look at all the little pogo pins. Aren't they

**Dave Jones:** pretty? Oh, look at them. Wow. No wonder these things cost a bucketload. One of the most amazing things about this board though is imagine what the production yield on this is like. Imagine trying to get right the soldering process on these

**Dave Jones:** connectors and all the dim sockets and all these huge, you know, these are probably thousand pin BGAs as well and just tons of them. If one little thing fails in here, well, the entire board is screwed. Imagine how much effort goes

**Dave Jones:** into just getting the reflow manufacturing process correct just to reflow solder this thing. Let alone all the, you know, correct pad geometry for the sockets. Although once you've done that once, it's okay. But just getting the thermal profile right. I mean, you

**Dave Jones:** can't just whack this in your toaster oven and expect it to work. You wouldn't be able to just even whack this thing in a regular uh, you know, professional reflow oven. just getting the profile right and the process and the type of uh

**Dave Jones:** machine you actually need to reflow something like this and get everything correct and the thermals of the board as well soaking the thing and it' be absolutely critical because there'd be a ton of ground plane in here which really

**Dave Jones:** heats these uh well a takes a lot of energy to heat them up b they stay hot for a long time so they're difficult to uh cool down so you know the risk of uh tombstone and other issues caused by

**Dave Jones:** that is absolutely massive. Just go I would not like to do this at all. I would not like to be an assembler going we need you to make this and give us a high yield too. So thank you very much Martins for

**Dave Jones:** sending that one in. Definite keeper. It's like a you know you can almost frame it, whack it up on the wall. God's beautiful work of art and uh yeah, maybe we can I don't know do some something fun with it. I

**Dave Jones:** don't know what, but yeah, it's non- workinging, Martin says. So, yeah, it's a fail board. I have no idea what. Could be anything, but uh wow, what a beast. Thanks, Martins. Next up, one from Australia. Hi to all my Australian

**Dave Jones:** viewers. Bloody ripper. Um sent to that crazy Aussie bloke who loves Sony portables. I do like Sony gear and yes, sorry, I still have a few Sony uh retro uh items for tear down. So, oh maybe hopefully I can do a Sony retro tear

**Dave Jones:** down tomorrow from the viewers of that crazy Aussie bloke in Queensland. Bloody Queenslanders from Brisbane. Um and it's some note foldy thing. Oh, there you go. That's novel. Hi Dave and CL. Oh, here's another gem to add to the collection.

**Dave Jones:** Thank you very much, Andrew and Jim from an unnamed government department. H I wonder what it is. Being up in Queensland, it's not like they're based in Canberra, which is where all our bloody politicians are based. There's my phone

**Dave Jones:** again. Don't get too many calls here at the lab. It's just the wife. Um let's have a look. It is a bit of Sony gear. Oh, in the original box. Look at this. Wow. What? I don't know any. Oh, they taped

**Dave Jones:** it inside. Okay. It's a bit weird. Okay, there we go. Got it. Figured it out. Dummy me. It's a Sony CD um burner. Two-minute tearown. Mobility for enjoying DVDs and CDs. Behold this magnificence from the ' 90s. Hallelujah.

**Dave Jones:** Look at that. Oh, beautiful power burn portable CD ROM drive. So, yeah, I'm a little bit uh confused. It is actually a portable uh writer. It is a portable CD writer, but it can do playback as well. It can do memory

**Dave Jones:** sticks and it's actually an audio uh playback device. You can, you know, actually that's a combo weird ass combo thing. H. And go the custom battery cradle. Oh, look at that. And you can just plug this beast. How do you plug it

**Dave Jones:** in? There we go. Do we plug it? Yeah. I don't know. Dummy Dave. There it is on the bottom. And this flips out and it plugs onto your cradle like that. Yeah. Bug of the 1990s. This is 2003 technology.

**Dave Jones:** Thank you very much. MP3 playback would have been pretty state-of-the-art for the time, wouldn't it? There's our custom rechargeable battery. Some sort of lithium job. And through the magic of YouTube, we're in like Flynn, um, some decent shielding in here. I don't mind

**Dave Jones:** that at all. Jeez, look, they've even got the little uh, look little shielding tab coming over onto is that top of the motor there. I like that. But more interestingly, look, they're using flat flex as the connecting. Look, you can

**Dave Jones:** see one big conductor inside the flat flex there. They've even taped it down. Thank you very much. So it doesn't flap around in the breeze. They've actually used that to Oh, actually is that spun off from that one. Sorry. Ah, terrible

**Dave Jones:** terrible videography here. But uh yeah, they're using that flat flex single conductor to actually join the screws to actually connect the grounds together. Very neat. No surprises for finding some Sony silicon in there. Sony do a lot of

**Dave Jones:** custom stuff. What's that 3U puppy there? I don't know. Google it. Oh, it's an arm. Is that Yep, there we go. Arm processor. Look at that. Genuine trimmer. Wow. What are we trimming? I tell you what, there's a lot of integration on

**Dave Jones:** this board. And check out the uh fit to envelope design in here. Look at that. This is obviously uh audio and uh power supply stuff because there's our audio output there probably audio output driver there. But all the uh caps in

**Dave Jones:** here and the inductors all um uh you know vertical parts they need a fair bit of space and they all fit into that envelope down there. Oh, spring fell out. It's not going to work anymore. And there you go. The old light pipe. Look

**Dave Jones:** at that. The choice of uh system designer champions everywhere. Little 085 lead in there. That's the way to get the light out the side. Beauty. And more of the flat flex ground in from there to there. Completely ruined by this ugly

**Dave Jones:** wire. Oh, even though it's crimped and done properly and beautifully and taped down, it just a So, let's see what's under this puppy here. Why have we got some rubber insulators on there? Have we? Yep. But, there's our drive mechanism. Nice.

**Dave Jones:** And I couldn't resist. And of course, your laser diode's in there somewhere. And well, this one's a keeper. It's just fun. I don't know. Might be able to do something interesting with it. And there's the eject mechanism as well.

**Dave Jones:** Look, you can see that arm in there. It's got its own little motor. Look at that drive on it. And it's electronic. So, you push the eject button over here. And it's all the way and all the stuff

**Dave Jones:** is over here. So yeah, not not just manual. They went to a lot of effort for that. And don't you just love the jazzy little remote with these Sony's with the LCD probably plays like the track name, the MP3 uh track title or something like

**Dave Jones:** that. A beautiful. Look at that. Rock that on your lapel. So thank you very much Andrew and Jim from the unnamed government department. Hello. Maybe. I don't know. H. Thanks, guys. And yes, I am going through size order yet again. Being a

**Dave Jones:** bit naughty. Just want to get the big stuff off my shelf. Thank you very much. Where is it? Rich. Good day, Rich. Um, he's from the United States of America in Jamaica. Plane to be exact. Jamaica plane. Not plain. It's just plain. There

**Dave Jones:** you go. H. Um. All right. Let's have a look that Rich has sent in here.

**Dave Jones:** It's multiple items. There's three items on the uh customs declaration. We have a note. You know, I usually just skip the notes. What do we have? Oh, the original candy water. The American classic Neco. Never heard nor seen of them.

**Dave Jones:** There you go, Neco. I'll give those a bell. Oh, we have a crusty. Well, this was a Hang on. Hang on. Oh, jeez. I've got a lot of some interesting stuff in here. Here we go. I'll just crack this

**Dave Jones:** open. I do actually have another unit up there. So, once again, it'll be a multiple tear down. Wow. The Garmin GPS 3 Plus. I could only dream about that when I was uh geocaching back in the day. With a little compass as well.

**Dave Jones:** Beauty. Looks like it's um been well used. Got some Velcro on it and uh interesting wedge shape. So like it can sit like on a bench like that. I guess like you know maybe you good for boating and um stuff like that. Perhaps you can

**Dave Jones:** like wedge it up in the console or something like that would be my guess. Anyway, um that was probably the ducks guts back in the day. It's going to have a helical antenna in there and uh beauty. Wonder if it still works.

**Dave Jones:** Probably does. Super reliable these things. Um, all these old GPS's I've looked at, they always still work. Weirdass custom four pin connector on the back, but awesome. So, we have a Gin GPS. I've got another GPS, I think. And

**Dave Jones:** we have a probe style oscilloscope. It's a rat shack. Rat Shack for originally $89.99. Wow. There you go. Radio Shack. Oh, it even comes with a three and a half inch floppy probed. Oh, for Windows and DOSs version 4.1. So, we got a date

**Dave Jones:** on this thing. 1996 Tandy Corporation. All rights reserved. Oh jeez. 2-minute tearown. Beauty. The original candy wafer made in the United States of America since 1847. These are equivalent to um I guess fruit tingles here in Australia. Um I'm

**Dave Jones:** not a big fan of the cut wafery thing. I think I much prefer the fruit tingles. Hm. Tastes exactly the same. All right, let's see if this Bobby Dazzler still works. Woohoo. It does. But oh, look some lines on the uh screen there. Ah,

**Dave Jones:** it's the GPS 2 Plus. Or is it three? GPS 3 plus. Searching the sky. I don't think it's going to find too much here in the middle of a concrete building. H. But check it out. This puppy rocked a full

**Dave Jones:** 12 channels back in the day. Uh the original model, well the manual um for the GPS 3 dates to 1997, but this plus addendum, this is the G GPS 3 plus dates to 1999. So let's party. Look, it's 1999. Wow. Check it

**Dave Jones:** out. That's surprisingly budgy. But jeez, look at the uh look at the RB electrolytic here. just it's glued. At least it's salasticked down to the bottom there. But they got the leads going all the way out there. It's like

**Dave Jones:** it was an oopsie. And whoops. We got to add some capacitance. Oh, something's not quite stable enough. And uh even this puppy wasn't enough and they had to add this one over here. So, what the what's going on there? Anyway, here's

**Dave Jones:** here's our receiver. And uh that's coming from our um helical antenna. I don't need to rip all that apart. It's just a two-minute tear down. And with that under the can there, which is soldered down, by the way, I won't take that off. Probably

**Dave Jones:** maybe an old first generation surf uh chipset perhaps. I'm not sure of the exact date on that. Probably around there. Um little bit of look, a little bodgege on the uh uh RTC crystal there. There we go. 32.768

**Dave Jones:** kHz watch crystal. And then they've just slastic that down. Bit of hot snot there. Down. know why they didn't use a proper surface mount job. I Yeah, it's just surprisingly a little bit how you doing for like a, you know, a leading edge gin

**Dave Jones:** product. Well, there's something you don't see every day. Intel 386 EX processor down in here. Wow, that's a fair bit of grunt. M Why, you know, not maybe not optimized for the job. Uh maybe they chose that because the

**Dave Jones:** development was easier uh perhaps. But yeah, that would be sucking a bit of the joy juice. You can tell this thing's designed for the marine environment. You know, the big rubber uh seal around the outside here. And um the rubber look

**Dave Jones:** rubber seal on the custom uh power connector at the back here. And some of the um this, you know, the screw in here has some salastic on the bottom of it. And uh do we have Yep. We got a rubber

**Dave Jones:** seal around the battery compartment there for the four AA's. Ah, yep. This is designed to sit in a boat maybe, you know, like in the front console or something like that. Whip up your helical antenna. You got to have an

**Dave Jones:** erect helical antenna. And Bob's your uncle. And Rich reckons there's a myth about these Neco wafers. These things were inspired inspired a useful manufacturing shortcut for the first radar systems during World War II. But every trace of that tail seems to have

**Dave Jones:** been wiped from the internet. At least they taste slightly better than something you'd find out of a year. 1940s electronics. Excellent. Oh, look at this thing. Includes Windows. Windows 95 MS DOS compatible software. Wow. Because yeah, you want to like get serial out of

**Dave Jones:** your handy scope, your probe scope. Sorry. Cat number 22310 for those playing along at home. Ah, beautiful. Ideal for on the spot testing of electronic circuits. Selectable input ranges 1VT, 10 volt, 100vt, 20 meg max sampling rate, 5 meg effective

**Dave Jones:** bandwidth. None of this equivalent time sampling rubbish. Um, on a 16 by 32 pixel LCD. Oh goodness, the Radio Shack probe scope. But look at this. Custom manufactured in Germany for RadioShack, a division of Tandy Corp in Fort Worth,

**Dave Jones:** Texas. And of course, the thing with this, there's no ground attachment on the front none of this high frequency probing rubbish. Uh designed to connect to the circuit under test. So yeah, you managed to find a point on your board

**Dave Jones:** and hook these puppies up. Um just like logic probes back in the day, you know. Um and yeah, so you don't need the ground attachment there cuz it's coming through the system ground over here. Goodness, look at the

**Dave Jones:** loop. Anyway, it's going to be absolutely horrible. But, you know, I guess it served a purpose back in the day. It's a live probe scope. It requires 9 to 15 volts in here. But yeah, look. Okay. What do we do? Probe

**Dave Jones:** scope. Neat. Somebody went to a lot of trouble to do that. AC/DC coupling. Thank you very much. And ground. Jeez, it's got everything. It's even got a funky zero level knob. Oh yeah, I play with that thing all day. Okay. So, how

**Dave Jones:** do we actually make it work? Do we push this button? I assume we push this button here because it's just sitting there. Oh, yeah. There we go. Version 3.0 1995. Here we go. So, it wouldn't even power on. You have to There we go.

**Dave Jones:** We're in. Tada. Oh, I can make it do something. Can I pick up 50 Hz hum? Here we go. How do we change the time base? Press it. Hey, there we go. 100. Is that 100 nconds? Five microsconds. There we go.

**Dave Jones:** We're going to get there. It's actually like you can't you can just go in one direction. That's it. There we go. We're starting to see it. We're starting to see it. Hold on to your hat. Tada. We have our 50 Hz h.

**Dave Jones:** Look at that. What a bobby dazzler. And here's inside. And Germany. All right. Who or what is Bob Lincoln? Good day, Bob. Oh, look at that. The LCD is just hanging, flapping around in the breeze there. It's just that's a

**Dave Jones:** serial interface job. You can see the number of pins. Very small. Looks like there's a micro with some uh firmware. And what's that puppy? What's a ZMD U825 H? Wow. COP 8 processor for all you COP 8 fanboys. There's got to be a

**Dave Jones:** couple left out there. There you go. Oh, it's actually a Wittig uh test technology. It's the Aussie fox. Beauty. That's not Aussie. That's Aussie. Aussie. Oh, right. Isillus. Yeah. No. Fail. Anyway, witty. Somehow I don't think there's much overload protection

**Dave Jones:** going on there. Straight over to the uh switch down here. And well, yeah, there ain't much in there, is there? H. Thank you very much, Rich, for sending those uh items in. interesting tearowns. Urgent crowdfunding ends uh 30th of

**Dave Jones:** March. Awesome. Let's crack it open. Thank you very much, Ben Wang. He's from Crow's Nest here in Sydney. So, a red zipper thing. The red zipper thing failed. Oh, bloody. Is this a This is a genuine Australia Post

**Dave Jones:** um envelope, too. Ah, what a load of garbage. Anyway, jeez. You going to put the red pull tab on there. Make sure it bloody well works. We got a bear board. So, let's check it out. And Ben's had a

**Dave Jones:** second sucker. The sav here. He's from North Sydney Boys High School. Uh year 11 student. And you might remember um it's a new improved version of what we've seen before. The board the Perf Plus 2 allows uh any two points to be

**Dave Jones:** connected together with zero wires and some solder bridges. Project is currently over 200% funded. Beauty. Um, and we'll end on the 29th of March. So, I'll link it in down below. He's just soldered a couple of things on here to

**Dave Jones:** show us how it works. And he did the uh remote boot thing. So, what third sucker the sav h it is doesn't look very impressive, but it's a proto board. That's the whole that's the whole idea. Let's have a quick squeeze. So, if we

**Dave Jones:** take a look up close, you can see that the uh traces going one direction here. Uh, so it's a big strip just like a verarboard. So, it kind of combines like a vera board and matrix board, but you

**Dave Jones:** can actually dis but you can but by default they're all disconnected as opposed to all connected together with a vera board and then you have to cut away these ones. If you want to join them up, well, you just do little solder blob

**Dave Jones:** like that. It's tiny little what is it? I don't know five like sixth hour eighth hour gap or something in there and uh you just put a little solder blob across. And of course, all the ones they go in different directions. So, just

**Dave Jones:** like routing back in the old days, these ones go vertical and these ones go horizontal. Very, very flexible. I love these things. So, say for example, this Atmill processor here, you've got that one trace going directly down like that.

**Dave Jones:** So, if you wanted to, you could just solder, you know, if you have to join that pin to that pin, no worries. You just join those two together with that one strip. And then on the other side here, you can actually then you've got

**Dave Jones:** them going in the other direction. It's quite flexible. So like all these uh proto boards like this, I like this one. And they've each got their own unique niche use. So it's worth having like a many like there's no one board that is,

**Dave Jones:** you know, one prototype board that's suitable for absolutely every project, every requirement that you come up with. So, it's worth having many different types of these protoboards just in your junk box so that you can, you know, whip

**Dave Jones:** them out and uh do a quick project. This is quite neat. Well worth having in addition to your standard Vera boards, in addition to your uh, you know, your more functional ones for all your surface mount stuff and things like

**Dave Jones:** that. Definitely good work, Ben. A I only saw the second uh page of this thing and Ben's uh got himself a patent on this thing. Do you believe it? The field configurable electrical routing matrix for electronic prototyping. Well,

**Dave Jones:** okay. Good on you, Ben, if that's your thing. If that floats your boat. Next up, one from Deutsland. Hi to all my German viewers, which is a very significant part of my audience. Thank you very much. Um, Eek Ike. E I K E. Um,

**Dave Jones:** Sha, thank you very much. I don't know. Ike, call you. Ike, that sounds better. Sorry if it's wrong. Oh, nice flowers on the postage stamps. Anyway, um let's check it out. It's a uh Okay, I'll maybe give you a bit of a

**Dave Jones:** spoiler. It's something Texas Instruments. So, let's check it out. What will it be? Wow. Oh, an IBO 83 calculator. Wow. Simple forbanger as they're called. Um what? Well, in the calculator um uh world, the forbanger is a four function

**Dave Jones:** calculator. And jeez. Yeah. Oh, wow. Made in Japan. All the best stuff's made in Japan. Woo. All right, let's have a look. Thank you very much. Eek, you sent a note. But here we go. That's not the Texas Instruments thing. This is a Texas

**Dave Jones:** Instruments thing when they came in a handy carry case. Yeah. Just rocking up and just cruising the streets, you know. Yeah. I'm ready with my whatever it is, the TI5029. Oh, look at that. Wow. Rocking the streets with your

**Dave Jones:** Once again, it's a Yeah, it's a forbanger. It doesn't even have um oh it's got totalizing and stuff like that, but it doesn't really have any financial um stuff. It's not really like a one of those proper financial uh calculators

**Dave Jones:** either. It's one of those printing calculator things. We've even got the old roll. And um I don't know. Accountants still use those. Apparently they still sell them. Um go figure. All right. 2-minute tear down. So I can send

**Dave Jones:** in these two puppies from uh 1975 here. this Ibico and uh this TI for all you TI fanboys out there. Um from about 1990 and check it out. Vacuum fluorescent display. Oh, isn't that a thing of beauty? Wow. And it's a sharp for the

**Dave Jones:** win. Check it out. It's alive. Well, it's doing. Yep. There we go. Yep. There we go. It's a winner. Winner winner chicken dinner. Beautiful. Wow. Crusty. Check it out. And we got ourselves an well Epson printer. There we go. You just playing

**Dave Jones:** along at home. Marked 1990. There we go. But look at this. There's nothing in it. But this puppy, look, they've converted the dip into surface mount. Well done. Well, overall, that's just a pretty horrid, bodgeged together piece of crap, really. I mean, look at

**Dave Jones:** these. Look at the caps just tacked on the back here. Ah, you know, this is production, but ah, you know, I don't know. Label is probably cheap in 1990. There we go. You can see down in there how they print the things. That's

**Dave Jones:** effectively like a daisy wheel. I got ourselves a FedEx one. Thank you very much, Edward Hopkins. Um, who I presume is from Oh, no. I was going to say the US. um based on FedEx and well FedEx operate everywhere but you know anyway

**Dave Jones:** um from Sagal thank you hi to all my viewers in Sagal I wonder have I'm not pronouncing that correctly am I sagal sagal is it uh senagle I don't know that's how Aussies might pronounce it anyway I don't know

**Dave Jones:** oh postcards presumably from the country which I can't pronounce correctly look at that beautiful and a victorious looking dude. And it turns out Edward is actually uh formerly from the US. Um originally from the US, now in Dhaka in uh Sagal.

**Dave Jones:** Awesome. And we've got some Look at this. Makes a skin crawl. Look at it. Tada. Cheapy. Look at that. one of the $2 cheapies which we've um seen before. Don't know if we've opened Don't know if we've done one of these before

**Dave Jones:** though, but you know, can't leave out the old analog. Check it out. Ah, the specs on the back, which are no doubt thoroughly impressive. And it's a Sunma brand trying to play off uh Senoir which are of course the um highly regarded

**Dave Jones:** Japanese manufacturer of um analog meters. So yeah, that's just Oh, that's terrible. Muriel. Wow. Apparently these things cost $1 US and the other is 60. Are you kidding me? Oh wow. It won't take 2 minutes to tear down these. will

**Dave Jones:** just open them and point and laugh. All right, let's play spot the error in the labeling. Got to be kidding me. Wow. This has to be the world's best analog meter. Look at this. 5%. Look on the 200

**Dave Jones:** all the ranges. Unbelievable. With a 1 megga ohm input impedance. Brilliant. How they get the 200 millolt range out of that? I It's magic. This should say warning to avoid electric shock. Throw immediately in the bin. It doesn't get any better than

**Dave Jones:** that. Superb soldering job. Oh, it's just just can't be beat. Look at this. How can is there any better multimeter than this? I haven't seen one. Three and a half digit display, you say? Okay. And don't you I just hate it when

**Dave Jones:** these companies rebrand. It's just bloody HP all over again and Agelant all over again. Was Sunwa. Now it's Sunma. I guess they didn't want the electrons to fall out. Or do they? With the M to the W. Just a little rule of thumb. Beware

**Dave Jones:** any multimeter that comes shrink wrapped. Luckily, the battery comes pre-installed. Hey, no worries. All it needs is one of those 9V batterizers they're promising. It will get 800% more battery life out of this thing. Beauty. That shot's got meme written all over

**Dave Jones:** it. We've seen this exact model before. So, yeah. No comment required. So, thanks to everyone who sent something into today's mailbag. If you liked it, please give it a big thumbs up. Catch you next time.
