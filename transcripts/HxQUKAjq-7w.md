---
video_id: HxQUKAjq-7w
title: EEVblog #762 - How Secure Are Electronic Safe Locks?
url: https://www.youtube.com/watch?v=HxQUKAjq-7w
source: youtube-asr
---

**Dave Jones:** Hi, this one's going to be a bit of an unusual one. I came across this CMI home safe here, made in Australia. You bloody beauty. And it's got one of these Lagard digital locks on it. And I thought, "Hmm, I wonder if there's any

**Dave Jones:** way that we can sort of, you know, have a look to see if we can hack into this lock and actually open the thing rather than, you know, like trying to like physically crack into the safe. I wonder

**Dave Jones:** how easy these things are, if there's any vulnerabilities in these locks. So, I thought we'd do a video just seeing if we can do what's called a power line analysis, power line attack on one of these things. And you'll see what I'm

**Dave Jones:** talking about in a few minutes. Now, this is a CMI branded safe. They make a really top quality safes here in Australia, here in Sydney, I believe, actually. And this is the one of their home, you know, one of their basic home

**Dave Jones:** models. And it's the H2D. I'll link in the data sheet down below. And it's a pretty, you know, entry-level home safe. It's probably the absolute minimum you'd want to actually protect anything as opposed to those pieces of [ __ ] that you

**Dave Jones:** get at Bunnings. They're just like at the home, you know, Home Depot or where where or whatever country you're in, those, you know, $50, $100, couple of $100 safes. This is like a, you know, a $700, a safe. It's about the minimum you can

**Dave Jones:** get. And if we have a look inside this thing, we'll see that it's got a 12 mm thick front steel plate. That's not too bad. It's got a deadbolt on the thing. Looks like maybe it has an anti-drill

**Dave Jones:** plate there. I'm not entirely sure. I don't think it's like a proper manganese steel or some other type of anti-drill plate steel. But it's not too bad at all. It's got some reinforcement around the front here. And it's got mounting

**Dave Jones:** holes down the bottom and at the back as well. And 6 mm steel all around. So, it's it's just a basic um, safe that would probably protect you against just the casual opportunistic thief with their crowbar. They probably

**Dave Jones:** couldn't get into this in a hurry, but of course any, uh, professional, uh, thief would just, you know, rip through this with, uh, power tools and things like that, no problems. But if you you you securely mount this to the, uh, back

**Dave Jones:** wall and the, uh, floor to, uh, concrete for example, uh, it's going to stop your basic, uh, thief. So, it's pretty much the minimum that you'd want for a home, uh, safe. But I thought, yeah, is there any vulnerabilities in

**Dave Jones:** these electronic locks? Hmm. Now, this is actually a LG brand, not to be confused with LG the electronic company. This is, uh, La Gard and these are pretty much the industry standard basic electronic lock. Uh, La Gard are one of

**Dave Jones:** less than a handful of top companies in the world who make these electronic locks. You know, there's other brands like, uh, S&G Sargent and Greenleaf, uh, for example, are some of the world leaders in this thing and I believe this

**Dave Jones:** is the, uh, 3750 model. It's their basic model. So, this is used on safes up to, you know, a couple of thousand dollars worth. This, uh, CMI home model, by the way, has a, uh, recommended cash rating, insurance

**Dave Jones:** cash rating of, uh, $5,000. So, it's not, you know, it's not a a real super duper safe, but as I said, probably good enough. Really, if you're interested in what are actually good safes, you know, you really if you want a real proper

**Dave Jones:** one, you need one what's called a TDR safe. They call it different things in different countries, but that's what they're called here. And TDR stands for torch and drill resistant. So, as I said, it's got, uh, like any manganese

**Dave Jones:** drill plates, it's got a glass relocker in there, so it has a glass plate. So, if you try and drill through, uh, to access the, uh, solenoid mechanism and stuff like that, it shatters the glass plate and lockers

**Dave Jones:** come in place and things like that. This one, as I as I showed, only has the one deadbolt here. Others have, you know, multiple deadbolts and they'll have uh you know, anti-cutting, anti-grinding in materials built into the uh steel walls

**Dave Jones:** and you know, things like that. So, yeah, pretty much, you know, if you want a real real safe in {quote marks}, you need a uh TDR uh class safe. So, to open one of these, it's a six-digit combination. It must be uh six digits.

**Dave Jones:** You can program it to be any six digits. This one happens to have um I believe like the original factory code. So, it's just 1 2 3 4 5. If we actually do it incorrect, you'll see that it beeped at

**Dave Jones:** at us, flashed the LED, and if this is actually the handle to turn the thing. Some actually have a separate handle to uh turn the um the bolts in the thing, but this one like that. So, if we go 1 2 3 4 5 6,

**Dave Jones:** bingo, you might have heard the solenoid click in place, and we're in like Flynn. Now, there's a few attack methods for these uh electronic locks. Uh one which I will just mention because, well, everyone else will want me to mention it

**Dave Jones:** is to use a thermal imaging camera. And if somebody has just operated the lock like, you know, seconds or minutes maybe uh before, then it'll show up as a thermal signature. So, if I go in there and touch touch

**Dave Jones:** those like that, you can see that my thermal signature is showing up there on the buttons, and you can actually determine the order they were pressed in based on how quickly they fade out. But, you can see that's faded out pretty

**Dave Jones:** quickly. So, that's not really a valid attack. And by the way, if you uh do that, you can just go like that afterwards, you know, and nobody's going to be able to see a thing. And this is how people can steal your um PIN numbers

**Dave Jones:** at uh checkouts and things like that. They can just have one of those phone uh thermal imaging uh cameras, and they can steal your PIN number if you're that paranoid. The second method is what's called the bump method, where you

**Dave Jones:** actually just pick up the safe and drop it down on the floor. I kid you not or just bang it on the top like that. Now, this is a valid method for like those real cheap ass safes that you buy at the hardware

**Dave Jones:** store that I mentioned. You know, there's $50, $100, you know, real basic safes or the ones that you get in hotel rooms and things like that. They're susceptible to this bump method. So, you can just like bang on the top of these

**Dave Jones:** cheap safes and you can open it. But, hey, no, this is actually at least a yeah, a decent basic safe. This one is not susceptible to any sort of bump method. It basically means just this the spring-loaded solenoid inside. Just by bumping it, you

**Dave Jones:** can actually operate the solenoid. You don't actually have to defeat it electronically. So, anyway, I might do a video might get one of those cheap $50 safes in Bunnings and actually demonstrate that. But, yeah, that those things are useless. Just do not buy

**Dave Jones:** hardware store safes. They're ridiculous. Now, the third method which was actually quite a valid method and might still be on some really old safes. I'm talking like, you know, 20 years old, early '90s when I believe LaGard was the first introduce a commercial

**Dave Jones:** digital lock. Anyway, the early digital locks were apparently susceptible to what's known in the industry as spiking. And what that means is you can actually remove this front and you could actually get access inside this front electronic lock mechanism to the pins which go to

**Dave Jones:** the solenoid. And of course, if you got that, you can just come along with your you know, like a battery and you could like spike what's called spike the pins and operate the solenoid and bingo, open the thing. But, no, they pretty much

**Dave Jones:** fixed that, you know, a long, long time ago. So, I don't believe there's a single electronic lock, at least not a quality one on the market these days that would be susceptible to that sort of spiking. And of course, the fourth

**Dave Jones:** method would of course be to like, you know, drill through and things like that. But, you know, they're they're they're like physical attacks. I don't I you know, I'm not interested in that sort of thing. But, what I am interested

**Dave Jones:** in is, tada, the 9-V battery that comes down. These are our wire These are the only wires that we have available, and I'm wondering, can we subject this thing to a power line analysis attack? I.e., be able to uh

**Dave Jones:** uh tap into here, measure the uh current going through, and see if we can actually detect any process any changes on the power line, any spikes on the power line based on the internal processor when it changes when you enter

**Dave Jones:** either a correct digit or an incorrect digit, for example. So, I'm thinking that maybe, like, you know, if you enter if you press the correct digit, it goes into one subroutine. If you press an incorrect digit, it goes into another

**Dave Jones:** subroutine. And, that could manifest itself as different variations in timing on current pulses taken from here. And, well, this is all I don't know if it's valid if if we're going to be able to measure anything at all. It depends on how much decoupling

**Dave Jones:** they've actually designed into this thing and stuff like that. But, because it's available, I thought we'd give it a go. Now, before we do that, let's just take a look at the uh deadbolt lock mechanism. This one actually comes in

**Dave Jones:** two types, a deadbolt uh like this or a swing bolt uh mechanisms. So, let's just take this plate off and see what sort of uh wiring we've got coming through from the front. Now, if you see inside that

**Dave Jones:** battery uh holder there, there's really nothing else inside there apart from the wires going up into the uh mechanism and through the hole in the uh front door. Here's the deadbolt lock itself. It's got all the requisite uh

**Dave Jones:** standards. It's UL listed, it's VDS, it's EN 1300 uh rated, and all that sort of jazz. So, you know, it really is a proper electronic lock, and they've actually conveniently tied up. Can I get that out? Oh, there we go. I just

**Dave Jones:** push that in. That's nice, and that connector comes out. We've got ourselves a four-pin connector. That's not surprising at all. So, the solenoid, the circuit for the solenoid is inside this. So, it does not penetrate to the outside. So, that's why I said you can't

**Dave Jones:** actually spike these things and operate the solenoid from the outside. It's pretty much impossible. Um so, but all we've got is the power, of course. These four pins, you'd have the 9-V battery power and the two data pins coming from

**Dave Jones:** the keypad. That's it. So, you know, pretty much you can't attack this thing in any other way apart from the power line analysis attack. That's That's pretty much the only thing you can do. Now, we might see if we can open up this

**Dave Jones:** thing later and have a squeeze if it's easy enough. It looks like that top plate there might actually come off. But, for now, let's try the power line analysis attack. Now, I do actually have a dedicated tool for this job. This is

**Dave Jones:** the Chip Whisperer Light, which was a Kickstarter and was in the Hackaday prize, and you've seen this a little bit before. And this is designed for power line analysis attack exactly like this. But, not everyone's got one of these or

**Dave Jones:** you know, can take this out in the field to crack locks like this. So, I thought that we just try it with the basic the most basic tool available, a a resistor for power line current sensing and an

**Dave Jones:** oscilloscope. Let's see what we can get from that first. Well, this is embarrassing. I got my 10-ohm resistor I was going to whack in series with the battery here, hook my scope up, and um yeah. Hang on.

**Dave Jones:** Wow. It no longer beeps at all. Can you guess what I've done? Well, in case you haven't figured it out yet, no, I cannot get back into this safe. I have locked myself out.

**Dave Jones:** How? Well, a lot of people were probably screaming at me. I forgot to reconnect the cable back in there that goes from the keypad to the solenoid. And I was like playing around with it and I thought Well, I thought I'd plugged it

**Dave Jones:** back in, relocked the thing in the closed position, and nope, because I was, you know, I was going to go, "Yeah, I want to do the shot where I, you know, open the, you know, I do the power line

**Dave Jones:** attack and try and open it, blah blah blah." And no, the solenoid is disconnected inside the keypad, the battery. There's nothing I can do. I have to crack into the to fix this, I have to crack into this safe the

**Dave Jones:** old-fashioned way so I can reach through and reconnect the bloody connector. Hi. Welcome to the AV Blog. Yes, I'm back in the old lab, the garage here, and I brought it here to see if we can drill through the sucker and try AND FIX

**Dave Jones:** IT. LET'S GO. CONSIDERING THAT WE'VE ALREADY GOT THE holes in the bottom and we've also got holes in the back as well. These are the mounting holes. You can mount it to the wall and or floor. Why not um drill a couple more holes in the

**Dave Jones:** bottom? Um that shouldn't actually affect the um safe at all, really. In fact, it provides a couple of more convenient bolt down points. We've got uh 6 mil steel. I'm not sure if it's like hardened steel or mild steel or whatever

**Dave Jones:** it is, but uh yeah, we'll give it a go. Shouldn't be that hard. Now, unfortunately, I've actually loaned out my power drill, so I'm going to have to use my cordless drill.

**Dave Jones:** And I'm through, but of course, I need a much bigger hole than this to manipulate it, but want to have a look and uh shine a torch in there, and I can see pesky plug. So, I want to be a bit above

**Dave Jones:** it. It's down like here or something like that. And of course, I could use like the angle grinder and I'd probably cut through this thing pretty quick. And you know, if you're a pro uh thief and you didn't care about noise, and you

**Dave Jones:** know, this is what you'd be using to crack into um you know, a safe unless it's uh a TDR safe as I mentioned, torch and drill resistant. And then it's just blunt these like, you know, and blunt uh

**Dave Jones:** drill bits uh and just getting a couple of millimeters into the thing. So, uh lead line through all the material cuz uh this this safe is only just uh 6 mm steel. You can get like 12 mm plate and ones for example,

**Dave Jones:** but your good ones actually have steel plate outside, then they have inner material which actually contains all sorts of particles which actually blunt all your drill bits and uh blunt all your uh grinding bits and things like that. And then they have another inner

**Dave Jones:** steel plate. So, that's what the uh TDR um safes have got. Now, the thing with this, of course, is that you've got to go real slow because if you accidentally push through, you could easily cut the cable inside. So, I definitely don't

**Dave Jones:** want to do that. I drilled another one, which is basically bang on to what I want, and even with these um clamp scissor forceps things, it's just short. I can't reach it. Bloody Murphy, every time. The second hole's really handy for

**Dave Jones:** being able to actually see through and see what you're actually uh doing while shining a torch through the hole in the back here to light it all up. But, uh I think I might ultimately um you know, you could use like a uh a borescope, one

**Dave Jones:** of these uh little, you know, microscope. This is actually a microscope like this, but it can set infinity uh distance focal distance on it, and it's got a little light on the front, and it can work as a webcam. So,

**Dave Jones:** I can hook that up to the PC. It's a USB thing, and have my notebook next to it, and I can actually use that as a borescope to see inside exactly what I'm doing. And you can see the cable just

**Dave Jones:** flapping around in the breeze there, doll. And uh you could use a view like this to manipulate it as you come in from the side, well, from the uh bottom bottom holes. There we go. You can see the hole drilled in the bottom there.

**Dave Jones:** And uh the two holes, but I can uh put this cam in the top hole. Let's have a look at that. Well, I knew I was going to try and break into a safe, but didn't think I'd have to do it this way. Geez.

**Dave Jones:** Uh the I haven't got long enough uh scissor clamp for ceppy things. I'm going to try and get in there maybe with some metal skewers and get the thing. Anyway, I've got my camera set up here with some Blu Tack. I've got a little

**Dave Jones:** screen to look at and manipulate, but jeez, it's not going to be easy. And it's important to get the tongue at the right angle.

**Dave Jones:** So, let's see if we can actually get in here and use a metal skewer. Just got to lift it a bit higher. YES! YES! YES! GETTING HERE off the screwdriver now. I remember that I had to push this

**Dave Jones:** in to It's almost like I got to do maybe two things. I might have to push Hello. I'm hoping that the tension of the cable is enough to push it in because the cable is all tied up the top there. See? It's almost

**Dave Jones:** fallen in off its own bat. It's almost like a There we go. Hang on. No. All I All I've got to do, I think, is push that. I get two screwdrivers in there and I think Bob's your uncle.

**Dave Jones:** Almost had it. Come on. Got it. Got it. Got it. YOU BLOODY I THINK I GOT IT. YOU BLOODY RIPPER. WOOHOO! Bobby Dezler. No worries. All right. The moment of truth. Let's plug in a battery. Hope it's good.

**Dave Jones:** And let's see if we get anything back. Will it beep or not? 2 3 4 5 6 You bloody ripper. Look at that. Beauty. Don't think I'll give up my day job, though. And that actually went in like a

**Dave Jones:** trick. It's perfect with that latching connector. And once it's in, it then slips over and the latch pulls back and Bob's your uncle. We're in. In like Flynn. Too easy. Haha. And the good part about going in the bottom is, as I said,

**Dave Jones:** we really haven't damaged this thing. I can still resell this. No problems at all. And you've just got an extra two bolt holes on the bottom. No big deal at all, cuz these things are traditionally bolted down to the floor. And this one's

**Dave Jones:** got the holes on the back as well, but yeah, no big deal. Beauty. It's like a bought one. Okay, after that little fun detour, sorry about that, but hey, it was kind of fun. Very Hollywood style break into

**Dave Jones:** the safe. I love it. Beauty. Anyway, we've got a resistor in series with the battery here. Just chose a nominal value, 10 ohms. Uh you want it to be high enough value so that you get sufficient uh voltage drop across it

**Dave Jones:** based on the current pulses, any current pulses from the CPU, so that you can actually see it on the scope. So, you don't want, you know, microvolts, hundreds of microvolts. You want, you know, tens, hundreds of millivolts, something like that. But you don't want

**Dave Jones:** it to be too high so that the voltage uh drops out. And it's got to be uh able to operate the uh solenoid too as well. So, anyway, I've got a 10 ohm in there, and I've got single shot capture on my

**Dave Jones:** scope. Let's press a button. Ta-da! Look at that. That's pretty good. That's 100 millivolts per division. So, we've got like uh 250 millivolts or thereabouts that we can actually go in there and look at the data packets. Look

**Dave Jones:** at that. I'm actually quite surprised. We're actually getting significant data detail on that. So, we've got some sort of packet. We'll see how long it's lasting, but we're obviously getting some sort of regular oscillation there. Very interesting. We'll go look at the

**Dave Jones:** frequency and the detail of that. But really, what I'm after for a power power line analysis attack like this, if there is, as I said, any difference between when you press the correct button in sequence and an incorrect button, maybe

**Dave Jones:** the timing changes or some other data inside here changes. And of course, this is where you want a deep memory scope, cuz you've got long packet like this, and you want to go in and see all the details. So, you want the deepest memory

**Dave Jones:** possible. So, you go into the acquire menu and where we're at 14 meg points at the moment. Heck, you know, we can go like the full 56 meg points of this sucker if we want. That's a phenomenal amount of data. And so, we can single

**Dave Jones:** shot capture that again and bingo, that's actually an incorrect one. Oops, I set the wrong time base there. So, you set that and you don't want to waste all your memory, so you want to set it to Well, you want to maximize the use of

**Dave Jones:** your memory, so you want as much a single data packet on there as possible. You want to make sure it's one packet, too. So, you turn the time base down to like 200 milliseconds per division. Reasonable? No. It looks like we've only

**Dave Jones:** got the one packet there. So, as I said, you want the maximum amount of that packet on the screen like that and then bingo, you can capture that and get the absolute maximum detail based on the sample memory of scope. Doing something

**Dave Jones:** like this, you know, you're going to want like a meg or two of memory at least. And just remember when playing around with these locks, you can't just, you know, have unlimited attempts at this because these have lockout features

**Dave Jones:** to prevent just people going in and trying to hack the numbers. For example, if you came along and tried to detect somebody's fingerprint in there by dusting it or something like that. Okay, you might get your six digits, but you

**Dave Jones:** don't know in what order or combination they are, especially if they've used a number multiple times or something. And if you enter the incorrect combination four times, I think this lock is four times in a row, then it'll lock you for

**Dave Jones:** five or 10 minutes or something like that before you can actually try again. So, that just limits just the brute force code attack. Now, first thing we want to do is go in and see if there's any time difference in this packet

**Dave Jones:** based on entering the correct number first, the correct number in sequence, and then an incorrect number in sequence. So, I should be able to re-trigger it. So, we're at 49.2 milliseconds here. So, if we single shot capture that again, we enter to correct

**Dave Jones:** digit. Number one, bingo, that's what we get. Now, if we go in there, single shot capture that again, and we enter say the number eight. Nope, looks like we're getting exactly the same time period. I mean, you can go

**Dave Jones:** in there and check for like a count the number of uh you know, pulses and things like that, but generally um that looks like it's exactly the same. Hmm, scrub that one. Now, I'm actually curious to know the frequency of this signal that we're

**Dave Jones:** getting there cuz it looks like just repeating like that. So, I suspect it might not be the processor, it could be that uh buzzer that we're actually uh hearing that beep every time. Uh you would have to actually know how long the beep goes

**Dave Jones:** for, and that could be the data packet, but the frequency could be the frequency of the beep. So, we have to actually um sample that audio and see what frequency that buzzer's beeping at, and compare it to this. In this case, it looks like

**Dave Jones:** There we go, 4.072 kHz. So, let's see if we can measure the uh buzzer frequency. Now, I just downloaded one of these uh little spectrum analyzer apps for my phone, frequency, I don't know. It was the same It was the one that uh the first one

**Dave Jones:** that pops up, and let's have a look. There we go, it is around about You saw that, around about that 4 kHz mark.

**Dave Jones:** And here's another one called SpecScope that will actually hold and freeze the display. So, let's try that.

**Dave Jones:** So, I think that's a bit too coincidental that this is so repetitive like this. It happens to be practically exactly the same frequency, just over 4 kHz mark. I think it's pretty safe bet to think that the maximum time period

**Dave Jones:** here will actually equal the amount of time that that uh sound buzzes for. Let's round that to say 50 milliseconds or so for that packet. Well, let's actually do it a bit better than that. I can actually capture the audio with my

**Dave Jones:** Zoom H1 here and then load it into Audacity and then we can check it out that way. Much better, much more accurate. And here it is here in Audacity. I didn't get the amplitude right, but it's going to be good enough.

**Dave Jones:** We can actually Well, we can get the length of that, but let's actually go in and have a good look at the spectrum. And what do we get? Here's our peak here. What is it? Tada! 4.077. We measured 4.075.

**Dave Jones:** Bingo. My hunch was correct that this is just the PWM signal driving the piezo transducer in the things. And I'm getting about 54 milliseconds there for that packet. And well, yeah, because it's such low amplitude, I'm not quite

**Dave Jones:** sure where to stop, but yep, it's near enough. It's absolute certainty that this signal that we're seeing is just the piezo transducer. So, because we've gotten that massive amplitude there, you know, a couple of hundred millivolts, well, we're not going to be

**Dave Jones:** able to see anything down on that. So, that was DC coupled. What I'm going to do now is go into AC coupled mode and wind the wick down to 20 millivolts per division. And so, you know, if we run

**Dave Jones:** that, like it's just going to sit there, right? Like that. So, we're just getting like it's nothing, right? The micro's in sleep mode. It's, you know, it's going to do absolutely nothing till it gets a button press and wakes up. So, I'm going

**Dave Jones:** to set my trigger level, you know, just down below, you know, somewhere below that. Get it as close as you can, so it's not triggering. And then bingo, like that. So, Oh, look, we've got a couple of spikes

**Dave Jones:** in there. Not sure what's going on there, but it it's gone down and back up. That's interesting. And bingo, there's our packet. Don't worry about this overshoot here, that's just because of the AC coupling. This is what I'm

**Dave Jones:** interested in here. So, there's our packet that we saw before. That's the buzzer. But, this could be the processor starting up, waking up, and doing something. So, uh-huh. Now we're getting somewhere. Hmm, so ignore all that. That's just out the

**Dave Jones:** packet that we saw before. And because it's uh 20 milliseconds per division, there it is 20 40. That's our 50 millisecond packet. Hmm, the processor is doing something in here. And that's what you would expect. You expect the

**Dave Jones:** processor, when you push the key, you expect the processor to wake up, do some processing, figure it out if it's the correct uh key or whatever, and then do the buzzer. And that's exactly what we're seeing. Set your time base back

**Dave Jones:** like that. Maybe, you know, set it back here or something. And right to that point, so then we can start actually measuring that period there cuz maybe that time period will vary. So, we should be able to retrigger that one now and have a

**Dave Jones:** look. Let's try it again. Single shot. No. No, we've got another No, that's just could be some other RF or garbage or something like that. So, I'm not sure what the deal is there. There we go, that's better. That's

**Dave Jones:** better. And damn it, I've put myself in lockout mode. It just won't respond to any more beeps and it'll just flash that light every like 10 seconds or something. There we go. And damn, I got to wait like 5 or 10 minutes. Ugh.

**Dave Jones:** And as I showed in a previous video, you got to be careful with uh stuff like this. You can pick up crap and all sorts of things. In this case, all this crap here is coming from my LED lights up

**Dave Jones:** there. So, switch those off. Bingo. Look at that. Now, this is the data I captured here for the correct number. I've turned high res mode on just to get rid of some of that noise and crap, and we can see that we've got

**Dave Jones:** a nice little current draw there, then another little blip, and maybe another little blip, and then we've got the packet which we've seen before. So, anyway, I can actually save this as a reference waveform, for example, and then we can try and capture

**Dave Jones:** it again. So, there we go. We can store that as a reference waveform, and now we can capture it again, and we can just see the difference visually on screen. Of course, I can export this uh data to

**Dave Jones:** a file, and then I can go analyze it on a PC or something like that if I really want. So, here we go. I've got my reference waveform there in white. Now, let me press an incorrect button, say

**Dave Jones:** number eight. Woah, look at that. It looks pretty darn identical to me. Woah, there's there's nothing in that. It just comes down to noise. So, there's no difference in the pulse width there. That's That's got to be the process starting up, doing

**Dave Jones:** something. We even get that little blip there, and we kind of even get that little blip there. So, yeah. Hmm. So, unless there's some more data out here, I'll check, but I don't believe there is. Um we've pretty much

**Dave Jones:** uh come a gutser here, and well, a null result, uh which is kind of what I expected. I didn't expect to find a power line vulnerability uh in this thing. Like, I actually didn't expect to get well, anything out anything useful

**Dave Jones:** out of this, but we've actually gotten and analyzed some useful data here, and well, we just can't pick it. So, they've obviously designed this thing uh really well. Of course, you know, to get around all this sort of stuff, all they've got

**Dave Jones:** to do is design in decent decoupling into this thing, and well, you know, you can't do any power line attacks if there's all that local, you know, a massive amount of local decoupling near the processor, you just won't be able to

**Dave Jones:** see it from right back at the battery terminals. Just a quick explanation on that in Dave CAD, if this is inside the safe, as we'll see in a second, it is like literally inside the safe, it's not outside the keypad, so we only have

**Dave Jones:** access to the current out here. Now, if this is the CPU inside that's drawing little gulps of current when it powers up and and does that sort of stuff, if you've got sufficient bulk decoupling inside the safe like this, then it's

**Dave Jones:** going to get all those high frequency current uh spikes from the decoupling, and then then the cut and then the capacitor's going to charge up at a much slower rate like this, and it's all going to be hidden in so all the detail is going to

**Dave Jones:** be hidden inside here, which you can't actually probe. It's not going to be hidden outside here when you actually measure the current going into the thing. So, yeah, if you if you're trying to design a safe like this and one of

**Dave Jones:** these electronic locks, and you don't want it to be susceptible to power line attacks, well, you just filter the crap out of this line, you know, you can put in big LC filters and all sorts of, you know, massive amount of decoupling in

**Dave Jones:** there. And that's They haven't actually done that by a huge amount cuz we were actually able to measure some things on there, but hey, I think they've taken things into account in the software. So, a smart programmer would ensure that the

**Dave Jones:** lengths of the software loops, regardless of whether or not you press a good or a bad button, they will be exactly the same so that you can't do any power line analysis attack. You know, we could probably get

**Dave Jones:** in there and like try and maybe get some minute differences and things, but jeez, it is yeah, it's it's looking completely shot at this point. And if I make that time base a bit slower, you can see that

**Dave Jones:** there's just nothing out here. So, um that reference waveform stays the same period. So, there's our our buzzer and that's the AC coupling recovery. But yeah, we got like nothing. And of course, it goes without saying that the main processor is in

**Dave Jones:** here and also the flash e-squared prom storage, whatever it is, for the PIN code is all inside this thing which is sealed inside the safe. So, when these things wear out, in particular this one because it rotates like this,

**Dave Jones:** it is not the world's most reliable design because well, you know, cables have to rotate and things like that. So, the ones with the levers on them are a much much more reliable design than this one. But hey, this is only on a

**Dave Jones:** relatively cheap safe. So, it's okay. But yeah, you might have to replace this thing. The buttons wear out. For example, the wires inside well, the wires inside break, you're screwed as I mentioned in a second. But you can

**Dave Jones:** actually physically take this off and actually replace these things without um losing your passcode. So, if those things break, it it doesn't matter. You just replace the keypad on the front and the passcode is still stored in there. So, you can still

**Dave Jones:** get back into your safe. No problems at all. Now, if you can see right down in there, you can actually see the cable there. And if I rotate this, you can see that cable inside move. And you know, if you

**Dave Jones:** do this too many times, then yeah, your cable might you might eventually get a break in the cable. So, but I'm sure they've used, you know, top quality multi-strand cable in there. So, it's designed to be rotated like that. But

**Dave Jones:** still, you know, it eventually could wear out if you open and shut this thing too many times. So, let's see if we can actually see anything useful inside here. I hope it uh can come apart. Okay. Well, that came

**Dave Jones:** out no problems at all. And by the way, this is the older model than the 3740. The newer one's the 3750. It looks identical. But no surprises. This thing's over 10 years old. And is that version 1.00? Is that the

**Dave Jones:** firmware? Hmm, that's a worry. And we're in like Flynn. Check it out. There's the cable going off to the solenoid in there. And there's some decoupling action happening there. That's a decent amount of uh tantalum. So, that's all right. But uh

**Dave Jones:** obviously wasn't enough for us to see some sort of uh stuff. Surprise, surprise. I expected like a microchip picking there perhaps. But no, we've got an ST micro ST62T uh 25. And this is a one-time programmable OTP microcontroller. Not

**Dave Jones:** this modern flash rubbish. Heck, it's not even E-squared PROM. It is um yeah, an OTP uh micro very, you know, I'd like discontinued these days. They don't use these anymore. So, there's no internal uh E-squared PROM in that to actually

**Dave Jones:** store the code. So, ta-da. That's why you can just see it in 93C64. So, they get an Once again, that's ST. So, they've got an external uh 1K serial E-squared PROM. And that's what stores your PIN code in there. But

**Dave Jones:** this is yeah, very old school. But considering that this design no doubt dates back to Leggards, you know, very early design. Maybe like back in like 1990 or very early '90s, then yeah, I guess it's not that uh surprising. And

**Dave Jones:** the legacy uh micro still continued over. Hey, they've got the code. It's all been verified and proven. So, you know, you don't want to go messing with it when you've got a winning product, a market-leading product like that. And

**Dave Jones:** there's nothing too exciting happening. External uh 4 MHz uh crystal here. We've got uh the decoupling as I said, we're going to have some regulation. We've got a PNP drive transistor up here for our uh solenoid. no problems whatsoever. And

**Dave Jones:** yeah, that's a bit uh looks like we've got a big-ass diode protection, little uh poly switch in there, and Bob's your uncle. Now, if we have a look to see how this thing works from the inside. Sorry, I haven't

**Dave Jones:** screwed it back in, but you can see that the only thing stopping pulling that back is that little plate which drops down there, which actually has a taper on it like that. And well, let's punch in the right code

**Dave Jones:** and see what we get. And bingo, it allows that to go through in there. So, there's something in there that actually releases that pin. And then once it goes back, of course, boom, it just drops back into place and

**Dave Jones:** locks like that. Nothing you can do. There's the back of the main board. Actually got lots of uh test pads on here, all numbered. So, obviously some sort of uh decent amount of uh bed of nails production test in

**Dave Jones:** there. And if we take this all apart, if we get our solenoid out there, here we go. We can have a look at the Here's our little uh plate that has this spring on it, so it keeps it sprung down in there.

**Dave Jones:** That's what keeps it sprung to solenoid, and that just uh sits in there. So, let me see if I can uh power this thing up with this backing plate off, and you can have a look in there. And if you want to

**Dave Jones:** have a look, this just uh there This is the rotating plate in the bottom there, which then just when you rotate it, it just pulls this thing back. Now, we've just got this little metal rod in there. And obviously, when the solenoid kicks

**Dave Jones:** in, it's going to suck that all the way in there. And then, of course, this thing is free to move up, and this whole thing push back. Too easy. So, if we try that again, Oh, you could see that. I hopefully you

**Dave Jones:** saw that. Oh. It fell out. Oops. Gravity's a [ __ ] Wow, for a minute there I thought I found a massive vulnerability in this thing. Like, if you hold it up like that, no problems at all. But if you hold it up like that,

**Dave Jones:** boom! It come It opens. And I thought, what the hell? Surely if you just tip the safe on its side, there is you know, it's got no way that would that vulnerability would have been found. It's because the pin was able to slip uh

**Dave Jones:** via gravity all the way back in to the solenoid without having it actually on. Wow, but no, as it turns out, no. There's nothing wrong with it at all because look what I found. I realized that they must have something else in

**Dave Jones:** the shaft. What? I found a little spring on the floor which must have fell out. And that's what keeps the pin uh pushed out um of that thing. So, maybe technically, you know, some bump vulnerability there, but the pin There's not enough mass in

**Dave Jones:** that pin though. It's all to do with the mass of the pin in that solenoid and the spring behind it which normally keeps it out. Oops, I got to disassemble it and reassemble it with the right part. Hmm.

**Dave Jones:** So, maybe you can see what I mean by bumping. I've put the spring in there now which keeps it out. And that's fine and dandy, but if you boom, you know, if you bump the safe like that, boom, the spring could

**Dave Jones:** technically go back into there, but it has to go all the way back in and you've got to turn it at the right time. So, I'm sure Legard have done their homework on that. Anyway, like uh yeah, trying to bump a 40-kilo

**Dave Jones:** safe like this. Hmm. No, that seems pretty good. I can't can't do anything to that at all. Can't get it to release. So, no, you can't bump these locks. And what about a drilling attack uh like through the front, for example, to try

**Dave Jones:** and uh you know, get that solenoid pin to operate and stuff like that? Well, I think good luck with that. I mean, maybe in theory, but jeez, I don't in in practice it would just yeah, I like you're better off just uh you know,

**Dave Jones:** cutting into it uh some other way, I think. So, yeah, that wouldn't be terribly easy. So, these things aren't particular, I don't think. These are particularly easy to defeat in this particular scenario. I mean, you know, there's no way you can uh sort of crack

**Dave Jones:** in there from outside and get access to the E-squared uh prom and read the code out. You can't do power line analysis attack. You can't bump the things. So, they're they're pretty darn secure electronic locks. No wonder this is

**Dave Jones:** like, you know, the industry-leading almost um de facto standard electronic lock on even, you know, quite decent medium to high-range safes. So, there you go. I hope you liked that video. Even though we didn't successfully defeat this electronic lock, we did actually, well,

**Dave Jones:** kind of sort of crack into it Hollywood style by the drilling and the camera and all sorts of that things. I thought it was a great fun. And it's an interesting engineering exercise to see how these things uh designed and built to be

**Dave Jones:** secure. And even though we didn't find the uh vulnerability in these things, it's uh that's actually good to know. And well, we don't want any uh publication bias here. So, it's always good to publish even negative results like this cuz it actually, even

**Dave Jones:** though it's negative, it proves that these things are uh pretty darn secure. I like it. But, one of the issues is even if we were successful in our powerline attack here and we could figure out what the combination was,

**Dave Jones:** well, what the numbers are. And that's the key point. You can only figure out what digits are actually used in the combination, but you've still got a six-digit combination. So, when you have the lockout feature of these electronics

**Dave Jones:** locks, four unsuccessful attempts locks you out for 5 minutes, well, how the hell are you going to do it in any reasonable amount of time? You can't. You're going to be screwed. So, if you're a thief getting in there, even if

**Dave Jones:** you had a little automated jig to uh you know, micro to plug up to it and it go it told you what six digits there, you don't have hours to sit there and try and hopefully guess the combination.

**Dave Jones:** It's you know, you want to be bam, in and out. So, yeah, these things are still secure even if we were able to do something here. So, I hope you enjoyed that. If you want to discuss it, jump on

**Dave Jones:** over to the eevblog.com. I'll probably have some high-res photos of the lock and inside uh the thing up on eevblog.com as well. There'll be a link to the forum down below and follow me on Twitter and you know, all that sort of

**Dave Jones:** jazz and subscribe and you know, give it a thumbs up if you like it. The other way. Catch you next time.
