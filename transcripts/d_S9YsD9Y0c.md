---
video_id: d_S9YsD9Y0c
title: EEVblog #984 - World's Best Dumpster Find! ($300k!)
url: https://www.youtube.com/watch?v=d_S9YsD9Y0c
source: youtube-asr
---

**Dave Jones:** Hi guys, down in the dumpster room. Sorry about the crap crap quality. Shooting this on the phone. Didn't have time to go get my good camera. So, audio and video is probably going to suck, BUT CHECK OUT WHAT I FOUND IN THE DUMPSTER.

**Dave Jones:** UNBELIEVABLE. HANG ON. Let's see if we still got it. It looks like a some sort of Keysight, one of these huge series scopes. I'm not sure how old it is. One of those big heavy beasts. I've never found a scope in the UH

**Dave Jones:** DUMPSTER BEFORE. ALTHOUGH, I AM AWARE that there are a couple of you know high-tech companies that would use such a high-end scope in the business park, BUT I WHAT A SCORE. I DON'T KNOW WHAT model number it is. We'll check it out. I'll

**Dave Jones:** get this sucker out and we'll take it back to the lab and check it out. Hopefully, it's a winner winner chicken dinner, but it's in the dumpster for a reason. Let's go. This could be awesome. Holy oscilloscopes, Batman. This has got to

**Dave Jones:** be the dumpster score of the decade. This is You're not going to believe Look at me. Agilent, not this Keysight rubbish. Infiniium DSOX93200 series, but it's the like the top of the line unit, the 32 gig bandwidth, 80 gig

**Dave Jones:** samples per second. Wha I Yeah. Why would you throw this out? I can only imagine that because this is not your average everyday use oscilloscope. Like maximum like 50 ohm inputs only, maximum plus minus 5 volts. You know, you get idiots going around

**Dave Jones:** you know just plugging in and thinking they can use this as a regular scope and just blow the front end. So, it wouldn't surprise me if that's what's happened. Blow in the front end and too expensive to fix the thing, but this

**Dave Jones:** thing is worth a fortune. If it work if it works. Hmm. And it's not in bad nick either. Obviously came out of some lab. I have no idea what that means. And it looks like they got the contact on

**Dave Jones:** there Ed. Good on you Ed. Looks in great nick on the back too. It's got the hard drive as removable here. GPIB interface as you'd expect. PCI Express times four. Expansion DVI output for an external monitor. And curiously though it's only

**Dave Jones:** 25 gig on here. So I guess maybe that's what the option 801 there does. I don't know. I haven't checked. Now unfortunately this doesn't use regular BNCs. As I said this is you know BNCs it might be able to get those

**Dave Jones:** on like you know up to 10 gig scopes or something whatever sort of the maximum. You can get BNCs that go a bit higher I think but basically on this high bandwidth ones you get these custom jobbies. They all look or they feel all

**Dave Jones:** loosey-goosey but they're designed to be that. Looks like they're an SMA but a male one. It's got a Cal output and that's got a similar thing. So yeah I might be able to cobble something together to get a signal in.

**Dave Jones:** All right, fingers crossed. Here we go. Yeah. Hold it down. Nope. Not a sausage. Unfortunately we're getting nothing on there and it doesn't have like a separate power switch on the back. So the the primary is open. Let's

**Dave Jones:** Looks like we're going to have to crack it open. Actually curiously there was no like Cal sticker on the back of this preventing you or the bottom preventing you actually taking this off. This is not coming off without a fight. Three

**Dave Jones:** screws on the back and ow, ow, ow. Bit of bloody aluminum in there. Going to have to get the tweezers out for that, but we're are in like Flynn. Awesome. There's our main standard PC motherboard. Every Nothing uh

**Dave Jones:** nothing particularly special at all. So, it's not like they got a big controller board in here. It looks like everything is just um SATA going over and that's well, you know, SATA is super high-speed interface. It does the business. So, no

**Dave Jones:** worries whatsoever. There's all your serious hardware down in there. That's what you're paying, you know, $100,000 or whatever for. That is a, you know, ooh, some serious serious RF stuff happening down there. Look at that. Wow. Woah, no touchy. And we've got some

**Dave Jones:** serious cooling on here, too. This puppy is going to be loud. You don't want to use this for your everyday use lab scope, even if you could. Now, of course, what we want to look for is the power supply, but I actually came over

**Dave Jones:** here. This is the power supply all in here. It looks like it lists out if you get these cables out, but this the main cable here, it's got a it's got a little, you know, hook catch thing on it, but that was kind of not

**Dave Jones:** all the way in. It was sort of sitting out. So, I'm going to bust it out. That's all right. And that's all right. And the contact is a bit it doesn't make proper click. I expect like a click to go in there, but

**Dave Jones:** let's um let's see. Hey, now we're talking. Up. Now, we're talking. Yeah, it's all over the place. That's just the input stuff on the power supply, but is that all that was preventing this thing powering up? A dicky

**Dave Jones:** a on a power connector. Let's find out. All right, let's try it now. Hello. Whir. Those fans are whirring.

**Dave Jones:** Can't smell anything. Hello. Hello. Intel Core 2 Duo 3 gig, whatever. Choose an operating system to start. Oh, what Oh. Oh, we're in. STARTING WINDOWS. WOOHOO. And bugger, password. Password is password. Is that you, Lance? Keysight. Joshua. Nope.

**Dave Jones:** Woohoo. We are in. We are in. It turns out it was Agilent with a capital A. I tried Took me a while. I took I tried all combinations of, you know, Agilent one, Keysight one, and all sorts of

**Dave Jones:** stuff. It was Agilent with a capital A. So, we are booting and it's got to initialize all the Keysight software, but we should be able to get in. Wow, that actually took a while to boot, but we are in to the main control screen and

**Dave Jones:** you're not going to believe it. It passes all the internal self-test, vertical, time base, ADC, acquisition memory, which is 2 gig, by the way. This uh all the models in the series I checked have 2 gig of sample memory at

**Dave Jones:** 80 gig samples a second. By the way, the bandwidth uh 32 uh gig halves to gosh darn it, only 16 gig when you turn on all four uh channels. Miss scope group, whatever that is. Passes the self-test. What I'm doing, I

**Dave Jones:** found um some female uh you know, gender changer things for the SMA, so I am able to actually uh connect up to this thing. So, I've got the calibration output actually connected on here and uh I'm actually generating a

**Dave Jones:** for the calibration output. Ah, no, I was it reset. There we go. 100 MHz, bingo! Bingo! So, we can How do we do that? There we go. There we go. Unbelievable. This thing actually works. Channel 1 seems to work just

**Dave Jones:** fine. I actually just did the quick jitter analysis option here and there we're analyzing now. Oh, fancy pantsy. This thing is working like a bought one. I won't go through I've gone through a similar scope before with a similar sort

**Dave Jones:** of interface. The interface is horrible. You would never ever want to use this for anything but specialized purposes. But anyway, we can go in there put up to 260 meg. Oh, look at that 536 meg points. Wow. It's not every day you get to see

**Dave Jones:** two picoseconds per division. Incredible. And that is an absolutely perfect 1 gig sine wave. Channel 1 works just perfectly. I'll try the others. I forgot that this puppy does actually have just the auto scale button. I'm not around. This scope is just

**Dave Jones:** horrible. Yay! Channel 2! Channel 3! Channel 4! Winner, winner, chicken dinner! I have what looks like a fully working four channel 32 gig 80 gig sample per second two gig sample memory Infinitum scope. This is ridiculous. So, I can

**Dave Jones:** only presume that somebody tossed this out because that the only thing I could find wrong with it was that power that dicky power connector which doesn't look like it latches Uh, properly in there and it might have worked its way loose or something and

**Dave Jones:** but I power this thing on and it's working on all four channels. I mean that's that's beautiful. Look at that. I mean we can turn off I've got acquisition I've got averaging mode turned on there but you know you can do

**Dave Jones:** all sorts of advanced analysis with this thing. It's absolutely this is ridiculous. This thing is worth an absolute fortune and check it out it actually comes with all of these applications. I'm not sure if that's fully loaded but look DDR4 display port

**Dave Jones:** 10 gig ethernet like maybe PCI Express. These things I checked the price of the DDR4 test app there. That is about 4,000 4 and 1/2 thousand dollars just for that software option. Now I made a call to check like a rough

**Dave Jones:** price on this. This is a discontinued unit the A series I'm not sure what the latest one is but it's listed as discontinued on Agilent's website but it was like state of the art not that many years ago. It's still a ridiculously

**Dave Jones:** powerful platform. I've been informed that with the software options on this thing it's about 300,000 dollars worth if you bought it brand new. Of course you know you couldn't sell it for anywhere close to that. In fact I

**Dave Jones:** wouldn't even know where to sell this. If you got any ideas where I what I can possibly do with this thing it it is the find of the decade. I might as well give up bloody dumpster diving. There's no point. It cannot be beat. I

**Dave Jones:** I can't fold it so far but maybe there's some little subtle thing but if you've got an idea how I can offload this thing like it have to you can't just whack it on eBay, right? You've got to sell it through some

**Dave Jones:** specialist company who's got the contacts for somebody who needs a bit of kit like this and then it cost a fortune just to calibrate this. An absolute fortune before anyone would bother touching it, you know? Um well, at any

**Dave Jones:** sort of reasonable, you know, high price. Companies are just nuts. Like they're just like nuts. But that's chicken feed to a lot of companies that, you know, it it's nothing. It's served its purpose and I don't know you know,

**Dave Jones:** it probably sat in the corner gathering dust and then one day somebody powered it on and it didn't work and they they tossed it. Wow. Anyway, that is the find of the decade at least. If you like the video, please

**Dave Jones:** give it a big thumbs up and leave your comment down below what I can do with this thing. I can't like what am I going to do with it? Like, you know, it's just a doorstop, really. I mean, it it's ridiculous. If you need

**Dave Jones:** you know, you need a specialist application. Um I'll do more extensive testing, but yeah, leave your comments down below what I can do. Oh.

**Dave Jones:** Nuts. Catch you next time.
