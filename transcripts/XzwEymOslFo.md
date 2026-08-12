---
video_id: XzwEymOslFo
title: EEVblog #767 - Super Regenerative Receiver Problems
url: https://www.youtube.com/watch?v=XzwEymOslFo
source: youtube-asr
---

**Dave Jones:** Hi, in a previous video you saw me install some LED panel lights on my roof here for shooting these videos and click here if you haven't seen it. I'll link that one in. Now, I showed that I actually had an issue with these

**Dave Jones:** crappy remote control power points that I got from the hardware store Bunnings here and they I'll show them working. This is number one. This is number two. You can have up to four like this and you can turn it on and it actually has a relay

**Dave Jones:** in there which switches the output on. So, you can turn it off and on, no problems at all. This second one, we can turn that off and on, no problems whatsoever. So, everything's hunky-dory but if I take this remote control, you

**Dave Jones:** can't see it but I'm taking it like a meter away. I'm just holding it outstretched hand it doesn't work anymore or it works a bit intermittently. Only number two is working or sometimes and number one is not working at all.

**Dave Jones:** I'm right next to the camera now and number one won't work until I actually get in there, like right close to it. What the hell is going on? Now, of course that seems weird because these don't transmit. These are just

**Dave Jones:** receivers. This is the transmitter here. So, and they've been coded to work with different power points here. Now, you might think well, if they're receivers, well what's the problem? Aha, something in the power board cuz they're both on the same power board. Maybe

**Dave Jones:** there's something conducting here. I don't know, you know, through the same power board. Well, I won't go through the methods to show you that that's not true. Take my word for it. It is not an issue caused by having it on the same

**Dave Jones:** circuit, the same phase, the same power board or whatever. It has to do with the distance, the physical distance between these two units. So, if I space them apart like this, as you saw, they both work, no problems whatsoever if I have

**Dave Jones:** the remote in the middle. If I actually move this one over here so that these are physically closer to each other like this, you'll notice that number one, it turned on, but it won't switch off properly. Only when I got closer to it.

**Dave Jones:** And number two is working just fine, but number one is having a problem there. So, what's going on here? Well, it all has to do with the fact that these aren't, even though they're supposed to be, they aren't just receivers.

**Dave Jones:** Hmm. Are you thinking what I'm thinking? Yep. Pain in the ass trap for young players, super regenerative receivers. Try to say that three times quickly. Super regenerative Super regenerative I give up. Regenerative. Super regenerative. Super regenerative. Super regenerative.

**Dave Jones:** Super regenerative. Super regenerative. Super regenerative. I'm going to get it better every time. Faster. So, to prove that theory I've got that this thing uses a regenerative super or super regenerative receiver, that they're interfering with each other because a super regen, that's easier to

**Dave Jones:** say, I'll stick with that, super regen receiver in these, they actually have an LC tank oscillator in them. And with which actually has positive feedback. They actually oscillate. So, when you got an oscillator, if you don't shield that oscillator inside, it can actually

**Dave Jones:** transmit on basically the same frequency you're trying to receive. So, these two receivers here are trying to receive on the same frequency and you don't design these properly to shield them and they're spewing out all sorts of RF

**Dave Jones:** energy at the frequency that you're trying to receive the damn thing on, then of course they're going to have weird ass problems where it doesn't receive like this because it's being swamped by the nearby device. Now, I have actually checked,

**Dave Jones:** once I separate these by about half a meter, they work fine from like right across the room, and that's how I fixed the problem in my roof. So, it's definitely a proximity effect. And just to show you about this phase thing,

**Dave Jones:** well, I've got one power board connected to one side of my lab, and the other one connected all the way over to the other side, which is a different phase here in the lab. And if I uh hit the button,

**Dave Jones:** hit the music, there we go. Channel one is once again not working. Channel two works a treat. And if I go over here, it just doesn't work. If I separate them like that, if I put them apart, then channel one

**Dave Jones:** will actually work anywhere, pretty much anywhere in the room now. So, no problems at all. But, I must say I do notice a bit of a range difference uh when they are on different phases. So, perhaps there is something

**Dave Jones:** to do with the fact that they might be on the same phase, sharing either the same power board, ultimately going back to the same phase in the same uh power point, which they are up in my roof. So,

**Dave Jones:** yeah, that has some effect. So, maybe there's some RF uh jumping onto the uh mains wiring as well. But, still, the proximity effect is definitely still there. So, I thought we'd actually try and see if we can uh get anything, if

**Dave Jones:** these things are transmitting anything. Now, the frequency we're looking at here is at 433.92 MHz. So, on my uh Rigol spectrum analyzer here, I've set the center frequency at that, and uh I've set a 5 MHz uh span here, and I really

**Dave Jones:** can't see much there at all. It's like right down in the noise. So, uh I was actually rather surprised by that. But, I think we can do a bit better. And just to prove that we can actually see something, here we go. I've

**Dave Jones:** got to hold down the button, of course, to continuously uh transmit, but you can see the carrier frequency there. It's almost bang on 43 433.92. So, that's close enough. And you can see no problems whatsoever. And I'm not sure

**Dave Jones:** about the modulation scheme used to select the different channels, but I'm not not concerned about that at all for today's video. But you can see the carrier and the carrier will now just vanish. But, if we plug this thing in, and no, I've

**Dave Jones:** tried it. It doesn't make any difference if you have this combined and things like that. It doesn't actually do anything. It's All we can see is that transmitting from the transmitter, as you'd expect. I'll show you how close it

**Dave Jones:** is. It's like sitting right on top of this thing. So, um yeah, the antenna's like right on top. But this thing does actually have a preamp in it. So, if we go into amplitude and we go down here, we can

**Dave Jones:** turn on the RF preamp and that gives us like, I don't know, five or more dB down gain in there. And uh we might be able to start see a hint of a couple of things here. Actually, silly

**Dave Jones:** me, had the reference level set for 0 dBm. If I go down to -30 dBm, and I set my RF preamp on, then tada, look, we can see some crap in this 5 MHz span we've got here around the free Look, we're getting

**Dave Jones:** some spikes in here. And to prove that it is this thing, if I actually disconnect it like that, boom. Look at that. It's gone. Right. So, now we're getting a huge bunch of I I won't touch the antenna

**Dave Jones:** this time. I'll put it here, for example. We'll plug it in. And bingo, look, getting the spike there. And something there. So, we're getting We're definitely getting something. And of course, if I switch the transmitter back on, wooshka,

**Dave Jones:** there we go. Okay, as you'd expect, cuz we're damn well transmitting. But, you can see that the receiver here is actually doing something because it's not shielded and the receiver has to be around that frequency. So, it's actually

**Dave Jones:** it's not that high. It's not that great. But, uh anyway, we should be able to see something a bit more if we go over to the uh Tektronix scope. And hopefully you can see that we're getting it a bit better here.

**Dave Jones:** We're getting quite a few spikes there. There we go. You know, we're talking about minus, you know, 96 DBM, you know, like it's really quite low and the receiver is just over that. And once again, I'll prove it. If I disconnect

**Dave Jones:** it, boom, right? It vanishes. There's our natural noise floor with the antenna just sitting there on the bench like that. And you plug this sucker in and whishka, we get that. If we What happens if we plug two in?

**Dave Jones:** Did that amplitude go up? But, you know, like cuz they're going to have slightly different frequencies, right? These things are not They're not even crystal They're not even going to be uh crystal controlled oscillators inside these things. So,

**Dave Jones:** they're just going to be like um LC uh tank circuits basically. So, that that are like hand uh tuned most likely. So, yeah, we're getting something there. So, you can see that these things transmit. And you can see that if I go down to a

**Dave Jones:** 100 Hz resolution bandwidth here, it's a bit slower on the updating, of course, as you'd expect. But, yeah, you can really see the peaks in here. So, this thing is uh definitely transmitting across you know, a fairly broad band. It's not like

**Dave Jones:** centered like right on the uh receiver, but you know, it looks like maybe the receiver's here and it's well, it's going to be near enough to the uh transmitter. So, you know, which is uh 435.92 there and it's supposed to be uh 433.92,

**Dave Jones:** but as I said, I reckon these suckers have got uh crappy little um hand-tuned LC oscillators in them. Hmm, you think what I'm thinking? Yep, tear down. If we take a look inside this sucker, here it is, and I had a bit

**Dave Jones:** of trouble getting into it cuz it used these stupid little uh security um screws, the one with the, you know, that little uh thing in there, and uh just to stop you using a flathead. And, of course, I've

**Dave Jones:** got like a security uh bit set, no problems at all, but it was too recessed down in there. I could get these ones out, but I couldn't get these ones out, so uh nothing you can't fix with a Dremel.

**Dave Jones:** Now, because this thing is built down to a price, yeah, we're not going to see anything too fantastic in here. We've got uh the leads welded onto the uh contacts down in there. That's meh. And, obviously, flip it over the other

**Dave Jones:** side here, we've got ourselves the uh the relay. That'll be a one-hung low brand. It's a Hong Chin. It's a Hong Chin. Yeah, super quality. Anyway, there's our relay. Oh, it switches it off. We've got ourselves um hey, a decent that looks

**Dave Jones:** like a reasonably quite a reasonable quality X class uh cap there, but uh basically, there is not much else in here. This is um I expected a little bit more than this, but a classic uh super regenerative uh circuit, super regen

**Dave Jones:** circuit uh uses a single You can well, you can do it with a single transistor, and bingo, there's our single transistor. Bingo, there is our tunable uh coil, and you'll notice, as I uh suspected, no crystal in there, none of

**Dave Jones:** that crystal rubbish. Accurate frequency, no siree Bob. They just somebody in the factory just gets in there and gives that a little uh tweak with the uh correct turn angle. So, these things are going to uh um drift like there's no to Well, I Well,

**Dave Jones:** I'm not assuming that's going to drift a lot. Maybe that's a maybe a bad assumption. But anyway, um yeah, it's a single transistor LC uh tank oscillator basically. And um we've got some surface mount uh caps on the bottom there. So, there's not much

**Dave Jones:** not much doing there at all. I'm not going to bother reverse engineering this thing. I can pretty much guarantee that's a uh regen uh circuit or regen oscillator. Might get the part number on that transistor though. There we go. We've got ourselves

**Dave Jones:** a KSP 10. That's a UHF VHF RF transistor. No surprises whatsoever. So, we've only got a couple of turns in that uh coil there. And what's it No, it's all a bit how you're doing. Really. I mean, but you know, this is

**Dave Jones:** what your classic uh regen circuit is. There's nothing to it at all. Oh, do we have a diode in there? Oh, fancy pantsy. And if you're wondering what that chip is, sorry, it's a bit hard to get the uh

**Dave Jones:** number here, but I've looked and it's a classic LM358. So, yeah, nothing to do with the RF at all. Maybe that's the uh demodulation part. And that eight-pin SO down in there, I've got no idea. They've actually I can't see any number on that

**Dave Jones:** at all. I think they've rubbed the number off there. Maybe it's like a little eight-pin uh micro or something perhaps. But of course, the takeaway from this is that there is no shielding in this thing. There's nothing in the

**Dave Jones:** case at all. There's no, you know, RF can or anything shielding the regen receiver at all with the antenna coming out. In fact, you may be wondering where's the antenna? Where's Wally? Well, that's Wally right there. They using the

**Dave Jones:** uh the tank coil as the antenna. So yeah, it's pretty dodgy, but you know, these things are only designed for a short range and they're, you know, kind of sort of getting away with it. But yeah, when you combine the fact that yeah, it

**Dave Jones:** doesn't have a real antenna on the thing and it's a regen circuit, which is a unshielded regen circuit, which is effectively transmitting as lower level as it is, but still, when you put two of these things side by side, it's enough

**Dave Jones:** for them to interfere. And if you want to see inside the transmitter, well, here it is. A couple of coin cells in there and well, look at that. Single chip solution. Bob's your uncle. None of this stuff that we saw in the transmitter.

**Dave Jones:** So, there's our antenna, obviously, just around there. It's AC coupled, runs around there. They don't They haven't populated that part in there. So, that's obviously it. Nothing fancy at all. I don't think there'll be anything on the other side. So, that's obviously some

**Dave Jones:** sort of custom RF transmitter chip to do this. Oh, actually, this one's fancy pantsy. Look at that. Crystal, 30 MHz, but let's get in there and get the exact frequency. 13.56. You'll find that will be a multiple of

**Dave Jones:** our transmit frequency. And bonus points for anyone who can do that calculation in their head. You might be able to do a rough calculation, but 13.36 MHz 5.6 MHz, sorry, is exactly 1/30 tooth 1/32 of 433.92. So, obviously, they've got a 32 times

**Dave Jones:** multiplier in there. Now, hold on to your hats. This is fascinating. My assumption that this is some sort of RF you know, custom RF remote device is wrong. That is just a Holtek 4801 OTP micro. There is no RF

**Dave Jones:** circuitry here at all. I don't see any external transistors. There was nothing on the top side at all. Unbelievable. They must just be relying on the harmonics of the uh pumping out a square wave. You got to be me. Actually,

**Dave Jones:** what I'm doing now, I've got the scope on directly probing the output of this thing, and we're like down at 10 mV per division. So, it's not just pumping a square wave into there. If we go right in, this won't have the

**Dave Jones:** memory resolution, but yeah, look. We can actually see the carrier frequency. This is Sorry, this is only a 200 MHz um scope. I could use a higher bandwidth one, but yeah, basically, we are seeing a 433 MHz carrier there. It's about 2 ns uh

**Dave Jones:** per division. So, it's going to be, you know, 2.3 ns for that 433 MHz. So, that That matches up. So, we are actually seeing We are actually seeing the carrier frequency there. It's not just a harmonic. They're doing something there

**Dave Jones:** to uh convert that. Doh! No, I figured it out. This is uh the standard Holtek microcontroller, but the T3 on the end of the part number there I was looking at the wrong data sheet. The T3 is a

**Dave Jones:** separate chip with, you guessed it, a built-in RF transmitter. Doh! Yeah, Holtek make these um custom micros with RF transmitters pretty much specifically for this sort of application. And I was just thinking, "Well, how do they combine that

**Dave Jones:** microcontroller with the RF transmitter?" It's sort of, you know, they're not sort of like very compatible uh silicon type uh processes. But, hey, look. it tells you they've actually got a dual die package there, separate RF transmitter die. So, I'm actually rather

**Dave Jones:** surprised at the simplicity of this. Uh a lot of regen receivers I've seen actually have a uh transformer in them. So, yeah, this one uh doesn't. It's just a uh just literally a single transistor. We've got a couple of caps.

**Dave Jones:** We've got a uh a coil forming an LC resonant tank circuit, and uh Bob's your uncle. And just to prove that uh separating them a distance actually works, there we go. I've got them like just under a meter

**Dave Jones:** apart, and of course, I can switch one on, two on, one off, two off. It's fine. And I'll walk halfway across the well, the other side of the room here, like 5 m away, and uh see if I can do it. So,

**Dave Jones:** here we go. I'll turn one off, uh one on, two on. All right, over the other side of the lab now, and one off. No, it doesn't do it. Oh, there we go. Two off. There we go. All on. I can switch both.

**Dave Jones:** There's like an all button. There we go. And there's an all off button. There we go. So, there's a slight uh slight problem with receiver number one there. So, yeah, it's it's still not the best, but it definitely fixes up in the lights. I

**Dave Jones:** put them like this far apart up in the roof, and that fixed all my problem. So, it still is a bit of a bit of an issue, but you know, definitely not like it was before. But, ultimately, what I think's happening

**Dave Jones:** here is not so much like these spikes. It's basically uh that these things are generating broadband noise pretty much, that's actually raising the noise floor. And when you've got a tiny little piss ant coil in there uh trying to act as the antenna, and

**Dave Jones:** you've got a little, you know, piss ant transmitter like this, it's just totally poor system design. And by broadband noise, I can show you what I mean by this. I've got my nice little uh tech box near field probes here. I've got one

**Dave Jones:** of my magnetic H field probes hooked up to my uh 3G wideband amplifier here. And let's take a look at it on the Rigol. Here, I've got it hooked up. Of course, you get nothing closed, but when you get in here, oh, actually I have to

**Dave Jones:** pull back on that. Sorry. When you get in here and magnetically couple that in, you can see this is a 500 MHz span. So, that's 50 MHz per division there on the X axis. So, you can see how

**Dave Jones:** broadband this noise actually is. Sure, it's centered on that uh carrier frequency. I've actually got it centered on 433.92 here. Oops, foot's not all the way out. But, yeah, it's centered on that, but look how broadband that is. It's

**Dave Jones:** absolutely incredible. And if I press the uh transmitter, of course, yeah, we get our little spike in there, but look, it's just it's very touchy to try and pick that up, but yeah, there we go. Uh just the

**Dave Jones:** coil is right in this corner here. If I put it in this corner, we're basically we don't pick that up very well well at all. So, we're trying to pick up the magnetic field from that coil, and it's

**Dave Jones:** just massively wideband. So, these things just uh horribly designed, just generating lots of wideband noise which swamps the tiny little signal coming from this transmitter. So, if you have them too close together, yeah, one or both of them can actually play up. Now, of

**Dave Jones:** course, we could go to town trying to analyze this and get in, you know, proper measurements and uh checking the the modulator, how they're doing the modulation for the different channels, and all sorts of stuff like that. Uh I I

**Dave Jones:** couldn't be bothered. I just wanted to verify that this thing was actually putting out something, even though it's a very low level. And that's what we could see on the uh scope, but it it was, you know, more than enough to cause

**Dave Jones:** problems uh when you put these things close together like this. And it's a very well-known problem with these things, apparently. And a lot of people said this straight away when I did the previous video. They said, "Just physically separate them like this, and

**Dave Jones:** problem solved." And you know, at at first thought you might think that's stupid cuz these are receivers. What difference does it make how close the receivers can be? Well, if they're a piss-poor design like this with no shielding, not

**Dave Jones:** that there's inherently anything wrong with a regen circuit like this, but you've got to design it right. It's all about the systems engineering and getting the damn thing right. And these things are built for a couple of bucks.

**Dave Jones:** Down to the, you know, the manufacturing cost on these is a couple of dollars. Build them right down, you know, shave every last cent off the thing. And well, you can't put a metal can on it. No, sirree, Bob. That'll waste couple of

**Dave Jones:** cents. Screw that. So, they've just gone for the you know, absolute simplest design they could. Single transistor super regen circuit in there. And well, they radiate a bit and cause interference. There you go. Trap for young players. So, I hope

**Dave Jones:** you found that interesting. If you want to discuss it, jump on over to the EV blog forum. Links always down below. Catch you next time.
