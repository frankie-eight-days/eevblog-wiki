---
video_id: iAcNjVdd25w
title: EEVblog #1108 - Casio CT-X700 Keyboard Teardown
url: https://www.youtube.com/watch?v=iAcNjVdd25w
source: youtube-asr
---

**Dave Jones:** Never had one lesson. Hi, bit of a different teardown today. We've got this new model Casio CT-X700 keyboard. It's $179 US dollars and somebody asked me to take a look at this and how they're actually doing this for

**Dave Jones:** the price cuz apparently for this sort of price it is an absolute killer cuz it has full velocity a full 61 key velocity piano keyboard on it. Now, I've actually done a Yamaha PSR-80, I think it was, quite a few years back and I'll link

**Dave Jones:** that one in down below and at the end as well. And that was a keyboard with velocity control keys, well, sort of from the 1980s. And it was really interesting how they implemented that. So, I thought this might make an

**Dave Jones:** interesting teardown. So, let's have a look at it. And no, I can't play to save my life. I am not the least bit musical, but I am interested, obviously not in the process and the stuff like that. That's okay.

**Dave Jones:** Casio has some whiz-bang technology that goes into this that makes it, you know, sound like hundreds, 600 different instruments and all sorts of stuff. And which is really, you know, amazing. I'm sure they're doing a good job at

**Dave Jones:** that, but I'm really more interested in how they do the velocity keys because if you look at the PSR-80, that Yamaha from the 1980s, I think it was limited to like groups of keys and it was only like three level velocity or

**Dave Jones:** something like that. Whereas this one seems to be across as many keys as you can press at once and all individual based. And also um it seems to be like uh uh not just a fixed level. It seems to be like a pure

**Dave Jones:** velocity level. I'll just demonstrate that here and yes I am uh feeding this uh signal directly into my uh camera so that's how it's so good. And here we go. Like Okay, I'll just And the harder I hit that

**Dave Jones:** the more it sounds like a piano. It's uh they're like truly velocity or at least um you know, I'm not sure how close it is to an actual uh you know, an actual piano um cuz I don't know jack all about this stuff.

**Dave Jones:** But anyway, apparently that's really quite impressive for the price. 179 US bucks. So I won't pretend to know all the functionality on this thing, but it's got like up to six it's got 600 tones, 195 rhythms, 160 song bank, and all

**Dave Jones:** sorts of stuff. Um and yeah, it's very impressive. I'm sure once again, especially for the price. And it's got two large uh speakers on here. I don't know if they're just uh single cone like full range uh ones, but uh they are

**Dave Jones:** quite large as you'd expect. And on the back here, we've got a pedal in a face and audio in. Not sure why. I don't know. Once again, I don't know anything about this music stuff. Um DC jack and uh headphone slash um line

**Dave Jones:** level output that I was able to feed into my camera. Apart from that, just a USB on here and it's got uh MIDI interface and whatnot. However, that works. Meh. And it's powered from six double A batteries, which is uh very

**Dave Jones:** impressive. The original Yamaha from the '80s had like um C batteries. Wasn't it a real pain in the ass? Anyway, um 9.5 volt uh 1 amp jack or six double A batteries. Might have to measure the power consumption of that. As for the

**Dave Jones:** rest of it, well, these moldings down here might give us a clue as to how it's sort of the velocity keys work cuz all this stuff all this uh stuff along here obviously has something or a lot to do

**Dave Jones:** with the the velocity keys. Oh, I think I can see the board. Yeah, I can see the PCB. So, it's not completely sealed on the bottom there. Anyway, let's tear it apart. I find it interesting that these come in blocks like that. There's three

**Dave Jones:** of them along there. So, I'm going to open that up first and see what's what under there. Aha, right away we see the same technique used in the Yamaha keyboard from the '80s and that like they've got this felt in there and that

**Dave Jones:** uh the backs of the keys just you know, it's start it gives them a just a nicer feel when they come back or maybe you know, no sound sort of deadens the sound or the response when you when you push

**Dave Jones:** the key in like that and then it you know, comes back. Just gives it a little bit of give. So, there's absolutely nothing different about those three sections there. So, why they've got those three individual plastic things, well, there could be several reasons.

**Dave Jones:** One, they didn't want to make one single molding that thin that long perhaps. Um but why do they have this at all? Why doesn't this just come over as one big molding? Well, um I that's got to have

**Dave Jones:** something to do with the assembly of this thing. It's got to be assembled in a certain way and maybe they like put the felt in here as a step so they need access down there to put the felt

**Dave Jones:** perhaps and it's just got to be some sort of aid to assembly I would think. All right, this could get a bit tricky. Um like they it's separate sections so the keyboard section seems to be separate from the rest of it.

**Dave Jones:** And the center console. Hey, there we go. We're in like Flynn. We're in like Flynn, look at that. Single-sided, still got the single-sided board for the cost reduction. Nice. And they're just all Ah, let's have a look. Ah, this is

**Dave Jones:** fantastic. If it wasn't for this modern PCB here, this would be straight out of the 1980s. As I said, single-sided PCB for cost reduction here. It is still as cheap as PCBs are these days, it is still cheaper to actually manufacture a

**Dave Jones:** single-sided board. That's why you'll still find them in high-volume consumer products. You know, TVs, things like this, microwave ovens, washing machines, and you know, all sorts like white goods and all sorts of you know, stuff like that. So, it's all I love it. We've just

**Dave Jones:** got our eight-pin dips here on a single-sided board, a bunch of electros, and the connectors, the LCD panel's mounted directly on the back of that. Look at that. Absolutely fantastic. Do they have a ribbon cable for that? I don't know.

**Dave Jones:** We might have to flip it out, but wow. And look, old-school wiring straight under links. Look at that. Someone at the Oompa Loompa Casio Oompa Loompa factory is you know, hand so are they? Yeah, no, they've put put put two links

**Dave Jones:** in there and then soldered the wire between the individual links. Look at that. Wow. Nice. And old-school ribbon cable just going off down to the keyboard down here. This is terrific. And check this out, all the magic happens in one big Casio custom ASIC.

**Dave Jones:** Unbelievable. Like I'm doubting that this is an FPGA. I'll have to look at the smaller chips whether or not there's like an external E-squared prom or something like that, but everything's in there. We'll have to take it out and

**Dave Jones:** look at the double the other side as well cuz like you know, where's all the memory and everything else? But Casio have the clout to you know, do their own custom ASICs for something like this. I don't know if this is a new one

**Dave Jones:** specifically for this keyboard cuz I haven't torn down any other Casio keyboards. But yeah, it's like there's nothing in it. But this is how they get the cost down. This is a $175 retail or whatever. That's the street

**Dave Jones:** price US retail keyboard. And for something of this size and complexity, it's just yeah, they're going to save every cent they can. And it's obviously cheaper to have someone hand solder these ribbons on there like that. Sure it's very quick

**Dave Jones:** and easy. They might even have maybe a you know a bit of a jig for it or something like that than it is to you know piss money away on a connector. Don't want that. And you'll notice the

**Dave Jones:** attention to detail. Look, foam. They put a foam strip all the way along that. The only reason you'd do that is if you want to have an acoustically sealed chamber all the way down in here for your speakers. I mean you know, it's

**Dave Jones:** not the world's best uh speaker design. But you you know, you don't want it leaking out. And you know, it might sound a bit uh bit messy or insert audio file wank word here. So you know, but there are

**Dave Jones:** real you know, there's real science that goes into uh the acoustics of boxes and stuff like that. But obviously that's what they're doing. Maybe that's what they're doing here with the uh foam as well. But why they didn't do it on they

**Dave Jones:** did on these and not on these? I don't know. Anyway, it's interesting. But the foam is mainly just at the back there. So maybe that was like a big port. I don't see any up the top or anything like that. Uh

**Dave Jones:** You can see that the keys are manufactured in what? 2 4 6 7 plus the whatever you call those keys up there. Uh Told you I know nothing about these. Uh and they've done those in one molding. So they just duplicate that

**Dave Jones:** across uh the multiple keys like that. So we can whip that out and uh should start to get in like Flynn. Anyway, down on the input stuff here, some LM4565 low noise op-amps down in there. Couple of little common mode chokes. Got some

**Dave Jones:** Silastic down in there. Somebody had a little bit of fun. I thought they had gilded the lily up here with a double-sided PCB, but no, that one's only single-sided. That's just for the volume pot on the front. But that's nice. I guess they

**Dave Jones:** needed the set back on that, so they couldn't do it on the main PCB. And for the power amplifier down in there, they've got a TA8227. And you can tell it's a power amplifier because the middle pins, like that, join

**Dave Jones:** together. Nice big fat pins. Oh, yeah. They'd actually be power pins and also, of course, extracting that, you know, cuz we're not talking about super power here, but they'd be extracting the heat out of the die, as well. That's their

**Dave Jones:** job. That's why they're thick. Aha, there's your memory on the back, as expected. We've got our working memory and our flash memory, of course. Was there a header on the top? I don't know. There's lots of, you know,

**Dave Jones:** production test points down in there. Maybe they program it through here. What's this over here? I don't know. It looks like they've got a cap on each one of the input pins here from the various, you know, going

**Dave Jones:** Is that like EMC? Something like that. And there's our driver down in there. No surprises just for finding one big full-range driver, you know, no separate tweeter on that thing. There's no need. Wires soldered directly on, as we've

**Dave Jones:** seen on the other boards. None of this crimp connector rubbish. That just costs extra production time, extra scent, or whatever. So, they're shaving the cost there. Obviously, they've got this wall up here that's part of the acoustics. They're kind of trying to

**Dave Jones:** create like maybe a chamber in here and have it sort of come out the side. I'm, you know, I'm sure they've done their testing. It's not, you know, it's not going to set the world alight for 175 bucks. And that's just a regular paper

**Dave Jones:** cone, nothing special, but you know, it does the job for an an internal, uh, keyboard speaker. And I'm sure they've, you know, done at least a little bit of acoustics here to make it at least not sound completely crap. Part number for

**Dave Jones:** those playing along at home. Well, I really am starting to like the, you know, sectionalized construction of this thing with the molding there. That's, you know, the speaker just wraps around like there. The keys obviously like screw on top like this. We'll be

**Dave Jones:** able to uh, those out, no worries. And all the center console like that, you can work on that separately. You can test that separately, bring these together, assemble them in different parts of the, uh, production line, then, you know, bring

**Dave Jones:** them together. There's there'd be a person or two doing like final assembly on each one. Well, it's probably more than a person or two. I don't know the volumes on this. It's got to be large. Anyway, it's very nice. All right, will this be

**Dave Jones:** the big reveal? That's No. Cuz there's some Oh, this has got a Oh. Oh. Hello. Individual Oh. Okay. No. Okay. No, look at that. It's not I thought that was one molding. It's not. It comes apart as two separate

**Dave Jones:** moldings. Looks like the keys have to come out like that and then flip up. Aha! Now we're in like Flynn. Okay, so I don't see any like multi-level stuff. This is obviously the part that's pushing down here because this we

**Dave Jones:** actually saw on the bottom side. That's just like the stop. That's just the, you know, the thing that allows the the range of the key to go like that. Um, yeah. And uh, by the way, I'm not sure how long, you know, these in here

**Dave Jones:** would last, you know, by going bang bang bang bang bang. I'm sure they've, you know, there might be a finite life to that. There's not a lot of range of movement in there. I'm sure they've chosen their type of plastic correctly.

**Dave Jones:** D56. I I It's just looks like it's ABS. I don't know. Those numbers mean something F56. Oh, they Hey, oh, are they Do they go as D? Do they go in a specific location? I don't I don't think

**Dave Jones:** so. I think they're all identical moldings. Yep, 282 and this one over here has 282 as well. Oh, we've got some gunk down in here. Check it out. There you go. That's just like some silicone grease, something like that.

**Dave Jones:** Make it smooth as silk. Ah, this is interesting. The black keys though come in a bigger molding like that. Sweet. And they've got exactly the same on the bottom there. So, that contacts this somehow Ooh. Ooh. Secret sauce time. So, this is

**Dave Jones:** interesting. This board starts here and goes all the way with LBJ. I think it goes all the way to the end. So, that that makes sense cuz you don't want to have like a How long's this thing? Like

**Dave Jones:** a meter long or something, 900 mm. want a board that big going through your pick and place. Well, actually that's a That's Is that reflowed? No. Yeah, I think it's reflowed. It's not wave soldered. Anyway, um yeah, so they

**Dave Jones:** split it in. You don't want one big long board. That's why they've got the two ribbon cables, one here and one over here. But, curiously, they do join. And if we have a look down in here, these keys we'll take a look

**Dave Jones:** at. But, uh look, uh this is obviously a um single-sided board and on the top side here, they're using carbon. They just lay down another layer of carbon to actually get in there. Now, this is not going to be a short. These are actually

**Dave Jones:** going to have some resistance. So, let's measure that. There we go. 47 ohms, 44. It's not exactly controlled. I have done a video on these what all these uh carbon tracks are about. Might have to link that in if I

**Dave Jones:** remember. But, uh there you go. Yeah, they're not short. Maybe they're uh doing they are carbon resistors for a reason, perhaps. But, I think the most likely explanation there is that they probably don't have a reason. Uh that I

**Dave Jones:** think that'd be my best guess is that they're not actually using them as resistors. They're just using them as jumpers. They're uh the board was obviously cheaper with these. Cuz look, you know, you got all the traces running

**Dave Jones:** under there. It's just, you know, what you do on a on a double-sided layout. Cuz if they wanted resistors, they've already got to put down these little What are they? Uh diodes, they. There you go. They've already got to put down

**Dave Jones:** these diodes and uh solder those on uh reflow. So, why not do resistors as well? But, the problem with that is is that um you know, you have trouble running all your traces that you need. It's it's just a PCB layout thing under

**Dave Jones:** your resistors. You could probably use some Well, for you know, some longer Well, for resistors in there, perhaps, and achieve the same result. But, uh it's a pretty narrow in there. Anyway, they've decided to do that instead of a

**Dave Jones:** double-sided board. Interesting. And this other black stuff here, it just looks like masking. I We're going to have to remove this to see Oh, it doesn't go all the way with LBJ. Look at that. Wow. Okay. Now, for the big reveal,

**Dave Jones:** what's under these keys here? Are they uh capacitive um type thing? Cuz look, they've got two like um like whole moldings in there like two contact. They'd be contacts. And So, let's lift the skirt up here cuz these

**Dave Jones:** things look like they're that they're um anchored down to the board. I don't really uh Am I going to have to pop it out? Oh, yeah. Yeah, we can pop it. There you go. No wuckers. Yeah. Yeah, she'll be right. Well, I am

**Dave Jones:** surprised. They're just your regular membrane keypad uh contacts on there done with carbon instead of gold plated PCB contact. Look at that. They're they're just your regular carbon contact pads two of them. It's like what? I expected something a bit more advanced

**Dave Jones:** than that than just contact based. Obviously I mean like there's two of them and they're separate for a reason. Obviously one makes contact before the other does. So that's got to be just a slight angle. So when you

**Dave Jones:** press the key down like that, this bottom one connects first, right? It it just hits on the bottom there cuz they're they're not angled or anything like that. That's what I said before. I was looking for any sort of like stepped

**Dave Jones:** base thing there that we saw in the Yamaha keyboard. You have to check the teardown out of that. It had like three layers if memory serves me correctly. And yeah, so it pushes on that first hole first and then the next hole. So

**Dave Jones:** using a combination of those and the timing, I guess between them is how they can determine the velocity. So that's incredibly simplistic. That's not what I was expecting. I was hoping for some, you know, wing wizbang capacitive, you know,

**Dave Jones:** like distance sensor or or something like that cuz I I I don't think they're doing that. You couldn't do that like over the long cables and everything. It it just doesn't work out. They're simply a contact based system.

**Dave Jones:** Well, I'm gobsmacked. But they obviously make it work. But I guess you'd have to have an expert playing this cuz I'm not one of them and to determine how good the velocity feature is in this thing. But at least

**Dave Jones:** it has the velocity feature. But yeah, they're just using two layers there and probably almost certainly the timing between them to you know, to realize how far and how fast you're pressing the key. So, wah, wah, wah, wah. So much for that. That's

**Dave Jones:** all there is to the teardown, really. Sorry. I expected something more advanced, but they're getting away with it. Simply, cheaply. Good on Casio. So, this kind of makes sense now why they've done those carbon resistors, in quote marks, um, up here. And because this is

**Dave Jones:** a single-sided board, and basically if you wanted like to use your traditional like gold contact, uh, membrane pads down here, then well, they wouldn't have had anything up here for the jumpers. You couldn't put in individual jumper links. That would have cost a fortune.

**Dave Jones:** That would have forced them to a double-sided PCB just for layout reasons. The designers decided, "No, it's actually cheaper to go for a single-layer board and have the carbon process, and then we can do the carbon pads down here. We don't We can save the

**Dave Jones:** cost of the, uh, gold, uh, flash on the, uh, PCB, and we can, uh, do away with the individual resistors on there. And but the cost of the double-sided board, it was just cheaper to do it like this.

**Dave Jones:** So, once you decide to go single-sided board to save, uh, cost, then you go, "Well, let's put the carbon on here for the, uh, jumpers as well as the contacts." No worries. Well, someone's got to be a rebel. Blue. Somebody in the

**Dave Jones:** design department thought, "I want blue keys, damn it." Um, it's exactly the same, except they're blue. I think the reason for that though is because this has 13 keys, and these ones have 12. So, it's just a way to

**Dave Jones:** differentiate these. They don't mix them up in production. Clever. Cuz it'd just ruin your day if you picked up a 13-way one and tried to shove it in the 12-way one. Like you got all the way along, you're pushing in all

**Dave Jones:** these little pain-in-the-ass little things down in here, pushing them down. Oh, no, I used the wrong bloody one. Ah, Friday afternoons. Okay, standby current. There you go. Got to wait for it to caps to charge up. Ah, six odd mic, five odd

**Dave Jones:** mic. It's not too shabby. It's dropping. Not too shabby, huh? This battery is going to last forever on standby. All right, let's try the operational current. I'm going to use three hands here. Here we go. 211, 279 once it's powered up.

**Dave Jones:** 284, there you go. Up, ah, turned off. Anyway, couple hundred milliamps. Anyway, it's always interesting taking a look in low-cost consumer products like this to see how they're designed and engineered to get the price down. I hope you found it

**Dave Jones:** interesting. So, there you go. I hope you like that quick look inside this Casio CT-X700 keyboard. And apparently it's like pretty decent for the price. Um, I don't know. Let me know. Comments down below. Stand to be corrected. Anyway, if you

**Dave Jones:** like the video, please give it a big thumbs up. As always, there'll be videos at the end here. I'll put in that Casio that Yamaha teardown here and just some other random videos. Check them out. Catch you next time.
