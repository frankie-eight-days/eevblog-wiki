---
video_id: fUV8QQwCrh4
title: EEVblog 1400 - Hard Drive Micro Actuators are AMAZING!
url: https://www.youtube.com/watch?v=fUV8QQwCrh4
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 34, "3": 50, "4": 66, "5": 80, "6": 95, "7": 111, "8": 125, "9": 138, "10": 152, "11": 165, "12": 184, "13": 195, "14": 208, "15": 222, "16": 238, "17": 251, "18": 268, "19": 281, "20": 294, "21": 309, "22": 323, "23": 335, "24": 347, "25": 361, "26": 375, "27": 392, "28": 409, "29": 428, "30": 447, "31": 463, "32": 480, "33": 493, "34": 509, "35": 521, "36": 533, "37": 553, "38": 570, "39": 582, "40": 597, "41": 614, "42": 629, "43": 645, "44": 658, "45": 673, "46": 689, "47": 701, "48": 720, "49": 737, "50": 754, "51": 774, "52": 794, "53": 807, "54": 822, "55": 840, "56": 858, "57": 873, "58": 892, "59": 909, "60": 922, "61": 937}
---

**Dave Jones:** Hi, in a previous video we tore down a Western Digital Red 6 terabyte hard drive and we looked at the absolutely amazing technology inside modern hard drives and in particular we looked at the actuator head like this. It's

**Dave Jones:** actually got six different arms on here and 10 different heads and that reads data on five different platters like this. And there's quite remarkable engineering, science, physics, magnetics and all sorts of materials technology that goes into producing these amazing heads which

**Dave Jones:** ride just 10 nanometers above the surface of the disc as it spins around and records the bits. Absolutely incredible stuff. But there's one thing that I actually just glossed over because I was just looking at oh these must be test pads. But a few people in

**Dave Jones:** the comments pointed out no, these are actually much more interesting. They're actually micro actuators inside the head. So if we have a look at like we've got the main coil here of course and of course this has the very powerful

**Dave Jones:** neodymium magnets over it and of course this just moves the head over the platter like that as it spins around. So the large coil here which has a single winding by the way, it actually doesn't have any feedback on the coil. You don't

**Dave Jones:** when you've got these fantastic little sensors here called your read heads. And so you actually encode the tracking information on the discs and then it can use that to actually get the positioning data for the head. But anyway, that's

**Dave Jones:** beside the point. So that's interesting in its own right. But what's more interesting is that well with this large actuator head like this, it is very difficult to get really micro positioning on there required for the very high density discs that we've got

**Dave Jones:** these days. You know, every year they're coming out with more TPI tracks per inch. Like one inch of the disc they're fitting more and more tracks into that uh uh fixed 1 inch in there, which means that this has to um you know position

**Dave Jones:** itself more precisely. But, with a large head like this and especially a large mass, I mean, you know, it doesn't weigh a lot, but it weighs, you know, a significant amount, and that actually takes time. There's actually inertia

**Dave Jones:** with uh this sort of mass, of course. And so, it takes time even if this coil can actually, you know, microposition precisely, it takes time to spin this mass over to where it needs to go. And then if you need to seek another track,

**Dave Jones:** it's got to move like this, and there's that inertia there. So, that actually slows down uh your read uh write performance when it's got to skip between all the uh tracks in there. So, wouldn't it be nice if you had a lower

**Dave Jones:** mass version of this that you could just microposition? Well, it turns out these heads actually have microactuators on them. Let's take a look. Check this out, okay? What I casually uh thought were last time, these uh I I

**Dave Jones:** just saw like some gold pads here, and I thought, "Oh, they're test pads or something." Didn't really give it a second thought. But, as a few people pointed out, these are actually microactuators. Now, take a look at what's on the side

**Dave Jones:** here. This little arm like this, and then that red stuff in there, you can see there's uh like red goo at one end, red goo at the other end. This is like some sort of, you know, like silicon

**Dave Jones:** type thing holding this um little gold what looks like a gold pad, but this is actually a piezoceramic transducer actuator. So, this is a dual actuator head, and you'll notice the same thing on the I have to get the

**Dave Jones:** light in the right angle. You can see on the other side, they've got the same thing. So, there's actually two microactuators on here, and these are actually attached to the uh head over here, which is much lower mass, of course, than the entire

**Dave Jones:** assembly, the entire arm. And if you pull on one, if you like, you know, excite one side, oh, my pointer just happens to be the exact dimensions. We're actually zoomed in a lot, so it's hard for me to get this,

**Dave Jones:** but if you excite this top actuator up here like this, this can actually pull the head slightly in this direction like this. And likewise, if you pull the bottom one like this, the head can move a tiny amount, just a little, you know,

**Dave Jones:** and I don't know how many microns, if anyone knows, leave it in the comments down below, but you can actually pull this head side to side. Isn't that super cool? So, I yeah, that's as far as I can

**Dave Jones:** zoom in with the Takano microscope, unfortunately. But yeah, you can see that they're actually cut out there. You So, you can actually see that gap down in there, and that actually, like, you can see right down through the entire

**Dave Jones:** head assembly here, because this head here, I don't know if this is a slight like, what's that marking there, but anyway, it seems to have, is that one of the wires coming over, one of the contacts coming over to the top of that

**Dave Jones:** piezo ceramic actuator. So, this is actually called dual stage actuation. And yeah, we can micro position the head. I'm not sure how far it can actually move like this. I might have to try and put some current into it and see

**Dave Jones:** if I can even see any movement and experiment with this, but it only has to be a tiny amount. So, what you can do, of course, with this is that, so let's say you want to seek to track 10 or

**Dave Jones:** something like that, then you, you know, excite this actuator coil over here, and it boom, it goes over there, and it's near enough to track 10. It might be, you know, plus and minus a couple of tracks, but then instead of trying to

**Dave Jones:** correct it back, instead of trying to use this large actuator coil over here to try and micro correct it, you can actually do it much faster using these piezo actuators. And if you want to jump between, say, tracks nine If you're on

**Dave Jones:** track 10, you want to you know, read or write some data to track 11 or track 12, especially if you're using that uh shingled recording rubbish, um then, you know, it's you use the micro actuators to just go

**Dave Jones:** like that between the tracks. Um in instead of uh using this entire head coil over here. Isn't that very cool? I I think that is absolutely fascinating. Wow. And you can see Let's look at the other side of one. You can

**Dave Jones:** actually see the little tiny uh like What would you call that? Like a little spring arm or something like that. You can actually see one of the flat flex uh connections going to, well, you know, the top or bottom side of that

**Dave Jones:** uh piezoceramic um element there. So, it just extends that flat trace out there and then just puts that contact onto the top of the piezoceramic element. And then you can also see how they're like suspended with that. And you can see how that uh pink

**Dave Jones:** stuff there, that's like it's probably some sort of like epoxy or something like that that uh physically attaches the uh piezoceramic element to the metal head so it can just teeny teeny tiny micro actuations there. Oh, that's that's beautiful. Thing of beauty, joy

**Dave Jones:** forever. Yeah, so you can see the contact on the bottom side there and then the top side has the other side here has is that I assume that then that just goes over to the middle and then that's

**Dave Jones:** just grounded. Is it? So, I I would assume so because there looks to be no other wire going to the top side there. Now, the interesting thing is how exactly do these things work to pull the head side to side? Well, I'm going to

**Dave Jones:** have to guess here. Now, I used to work in the seismic industry for a long time and we used to manufacture our own ceramic piezo transducers and they were called benders and they were called benders for a reason they actually bend.

**Dave Jones:** And they they physically bend well, in our case when acoustic pressure was applied to them, but they would also bend when you apply an electric field to them. So, they they were just a capacitor basically. And and you could

**Dave Jones:** actually hook them up to an LCR meter and you could actually make them sing i.e. emit a sound and that was actually one of our test methods to make sure they're actually connected. You'll go hook an LCR meter up to them when

**Dave Jones:** they're in the product. You could stick your ear up to it, hold your tongue and you could actually hear the thing sing. So, I suspect that that's what's happening here. It's got a bend which means it's got a bend up and

**Dave Jones:** down like that. It can't I can't see how it can actually bend side to side. So, I would assume that maybe flexion up and down caught then due to maybe these springy bits on the side then causes So, up and down

**Dave Jones:** flexion like that causes maybe a tension to pull on the arm and that moves it from side to side. It doesn't move the head up and down, but it it the little micro vibration inside the ceramic element then causes the

**Dave Jones:** you know, a little bit of tension on there and it it pulls it side to side. So, I think it's it's translating the movement like that. Yeah, I I can't see how else it could do it. I can't really see how it

**Dave Jones:** can like contract um when you apply the electric field to it. So, if you do know how it translates that movement into side to side like that instead of up and down, yeah, please leave it in the comments. But, uh yeah, I I I think it's

**Dave Jones:** translating possibly vertical vibration into horizontal somehow. But, yeah, these things only move like tens of nanometers. Like, you know, maybe hundreds of nanometers, something like that. It's It's not going to be much. So, yeah, you maybe just see it

**Dave Jones:** flex just a little itty-bitty teeny-weeny bit. Okay, so I'm going to give this a bit of a wiggle wiggle wiggle, yeah, and we'll see if we can get it to I think yeah, I think I'm seeing some movement in that. Geez, there's not

**Dave Jones:** much. It's not much. It's just basically uh almost like the springiness of that uh metal there because it's not like entirely physically decoupled um from the rest of it. It's just like yeah, I think they're just relying on the

**Dave Jones:** springiness of the metal, and it only moves a tiny fraction. And it just moves like like half a bee's dick. That's it. But, that's all it needs with the current density of these uh hard drives, which is absolutely incredible. Yeah,

**Dave Jones:** you don't need it to move by much. That's amazing. Let's see if we can identify the pin for this uh piezoceramic element. And uh I know cuz I come from a piezo element background in the seismic industry, I

**Dave Jones:** know it's going to be in the order of like nanofarads, something like that. So, if we go to the first pin here, ta-da, 2.8 nanofarads. That sounds about right for a piezoceramic transducer. And the other ones are just

**Dave Jones:** like um shorted out. It turns out if you put the ohms range on there, they're like in the order of like 70 ohms, something like that. So, they're obviously the read write head. I never get tired of looking at this assembly.

**Dave Jones:** It's just thing of beauty, joy forever. Wow. It's really remarkable. As I said in the previous video, the hard drive is almost certainly the most precise mechanical object you'll ever own. The most precisely engineered, the one that uses the most advanced material

**Dave Jones:** and manufacturing and you know, engineering science and all sorts of stuff in there. It's just wow, it it's just mind-blowing. People just use these things, you know, like it's just a hard just stores data, right? This unbelievable. Like 40, 50 years of

**Dave Jones:** research and manufacturing technology and almost every branch of engineering and science has gone into making these hard drives possible. It's just mind-blowing. Okay, I'm going to see if I can solder to this. Good luck. Put a little bit of flux.

**Dave Jones:** My smallest tip and 0.35 mm solder. Yeah, no worries. Look at that. Yeah. Oh, I think we got we got something, have we? I'm not sure. Oh, that's probably good enough for Australia.

**Dave Jones:** Well, I'll give that a go. Okay, let's see if we can get this head to move at all. I've got 4 volts peak to peak, 1 hertz. Let's have a look. Can't see any wiggle wiggle. Nope. Nah, come on gaza.

**Dave Jones:** Worth a shot. Unfortunately, even at 10 volts peak to peak, no matter how I probe this, I'm not able to get any actuation at all. So, I'm not sure if I actually have the right contacts. I think I probably do,

**Dave Jones:** or whether or not it requires some, you know, asymmetrical drive or something pulling on one while pushing on the other, that kind of thing. Yeah, I'm not sure. So, yeah, I can't get this to actually do anything. Well, maybe I'll

**Dave Jones:** see if I can find some footage. Maybe someone's got some. In our third generation of helium-sealed drives, Western Digital introduced the industry's first multi-stage microactuator for data center drives, enabling more precise control over head position.

**Dave Jones:** Our microactuator design provides extremely accurate head positioning over the track in noisy, high-vibration environments. The microactuator delivers better performance, data integrity, and overall drive reliability, and enables higher track densities.

**Dave Jones:** So, yeah, we unfortunately we couldn't see anything there, and that's probably not surprising, but anyway, it was worth a shot. Couldn't find any footage at all of these things actually, like, you know, you'd need like microscope shots of these things actually doing their

**Dave Jones:** little wiggle wiggle wiggle yeah business in there, but I find this absolutely fascinating. So, I hope you enjoyed that little look at these microactuators, or are these milliactuators? Because in Western Digital video, there seems to be that having it up at the pivot point up here

**Dave Jones:** at this point seems they kind of seem to call that a milliactuator, and the micro one is a different design like in the actual like closer to the actual head cuz once again, it's a physical mass thing. The less mass that you have to

**Dave Jones:** physically pivot like that, the faster you're going to be able to do that. So, yeah, anyway, that's awesome. So, leave your comments down below if you have any experience with this sort of technology. Seems very cool for like taking out

**Dave Jones:** vibration and all sorts of issues and and potentially you know faster track seeking and and stuff like that or is it just used for vibration? I don't know. Anyway. Comments down below. If you enjoyed it, give it a big thumbs up. Catch you next

**Dave Jones:** time.
