---
video_id: o7xfGuRaq94
title: EEVblog 1485 - PedalCell CadenceX Bike Generator LOL FAIL!
url: https://www.youtube.com/watch?v=o7xfGuRaq94
source: youtube-asr
---

**Dave Jones:** Hi, just a quick follow-up video to a mailbag item that I got, which is a Pedalsel bicycle generator USB thing. So, it's basically a generator here, which goes onto your rim here, spins around, and puts some charge into some

**Dave Jones:** supercaps, which then gives you a dual 5-V USB output so you can charge your phone while you're cycling and stuff like that. Anyway, it was supposed to be dead. The person who sent They sent actually said that they killed two of these things.

**Dave Jones:** And we couldn't see anything in the electronics if you want to see it. Here it is here. It was just a potted thing, so you know, not easy to get in there and sort of like reverse engineer everything. That's the

**Dave Jones:** rectification diodes for the input here, which just comes from the generator here. There's six wires there. So, I thought I'd just a few people asked if I could actually check the motor, actually have a look at the output of the motor, and see if

**Dave Jones:** anything's failed there. So, that's what I'm going to do in this video. So, I'm just going to get a pinout here. I've soldered on six wires, so I'm just going to go around and try and find the pinout for this thing. That one up

**Dave Jones:** there. Oh, no. 16 meg. Why is this 16 meg there? Okay. Anyway, it looks like that first pin doesn't connect to anything. So, that's a not connected. Next, we got one the second pin. So, the second pin here,

**Dave Jones:** which I'll I'm just going there. Doesn't matter which direction. They don't actually have numbers, but this pin here connects to this pin here with 8 ohms. That sounds like a coil to me. Okay, so that's what we've got there.

**Dave Jones:** The three, which I couldn't well, essentially non connected, and three to winding. So, it looks like we have our three windings in there, which is what you'd expect. If you have a closer up look at the board, and I'm going to have

**Dave Jones:** to because it's a gloss solder mask, you can see that Okay, we've got our three power lines there, and the other I can only see one trace coming off that center pin. So, maybe they've got a sensor in there

**Dave Jones:** or something. I can't see anything coming off these other pins. Maybe I can try and measure something pierce through if you're trying to probe through a conformal coating. You can have really sharp probes to make sure you get

**Dave Jones:** through. I'll just buzz that out to see if these go anywhere, but yeah, basically we've got our three winding wires plus our plus potentially up to three sensors there or at least one. Well, that's strange. I'm getting bugger all out of

**Dave Jones:** any of those windings. Nothing. That's 100 mV per division, and it's not a It's not a scale thing. I'm getting nothing. I'm getting nothing. So, what the heck's going on there? I mean, this is, you know, what you'd expect to measure for a

**Dave Jones:** three-phase generator. I don't know about the values 8 ohms, but uh I don't know. Like, this is like a three-phase generator going into a diode rectifier, and that gives you the output voltage. That's exactly what you'd expect. I mean, surely they'd

**Dave Jones:** give me something. If I'm spinning this sucker, I mean, I'm not going hugely fast, I expect to get something. Like, what the So, unless there is something in there cuz there was one trace going off, which looked like I

**Dave Jones:** don't know, it may have been going to a power source or something, but like I can like that's winding resistance that I'm measuring surely. I'm like, what? All right, let's try and actually rotate it faster. Um and you'll notice look

**Dave Jones:** look at all the spikes coming up when I turn on the Dremel, but let's try and net net Let's go pretty fast. I'm getting bugger all out of that. Nothing. There's definitely 8 ohms across there. Okay, and it

**Dave Jones:** doesn't matter which winding I choose. Um it's just it's getting nothing. Wow. What the? So, I don't know. Are all the windings like fused together or something like that? Aha, I found an access uh keyway in here, which gave me access to

**Dave Jones:** the two grub screws here. And tada, I'm now able to get this sucker off. We can potentially open the motor. Seems like a decent motor. It uses like SKS bearings in it. What's that? It's got any branding? There's Well, okay, so

**Dave Jones:** much for that. There's zero branding on that. But as I said, there is an SKS bearing in there. I believe they're okay, aren't they? Um I don't know. Uh I guess I can unfold it, open it up. There we go. Here's a

**Dave Jones:** peekaboo inside there. I'd have to desolder it, but I'm getting um bugger all out of the windings. Oh, I checked the winding resistances again. Yep. So, we've got U Y W there. They're the three windings. We've got VDD, ground, and

**Dave Jones:** then H U there, which H I presume would be Hall effect. So, they've got a Hall effect sensor on one only one of the windings. Obviously, they thought they might have three, but they only did one. So, I guess um

**Dave Jones:** even but the generator was generating nothing. So, uh looks like I can pop this PCB out. Tada. Got you. It's our winding. Um It's all a bit rough as guts. Bit how you doing. But uh like, you know, don't see any

**Dave Jones:** melted windings or anything like that. So, there's your rotor. And there's the magnets and the stators and I like I don't know. So, I would have expected to get What? There we go. Something out of that. There you go. That's

**Dave Jones:** interesting. They do have three Hall effect sensors in there. But they're only connecting up one of them. So, yeah, okay. Fine. Whatever. Um I don't even know why they need that. Maybe it like it cuts it off at like a

**Dave Jones:** minimum RPM or something like that would be my guess. So, what I've done is just measured some DC resistance around the pins on here and the operational one up here which is actually connected, um it measures they all all three measure

**Dave Jones:** identical resistances in various combinations on the pin. So, there's nothing obvious in terms of like one of them's, you know, gone kaput, shorted, whatever. So, So, there you go. We're getting 8 and 1/2 ohms on the winding. Well, I've put

**Dave Jones:** this back on. Doesn't spin that good now. It gets stuck in the muck. Put it on AC. And we get something out of it. Not much. Aha. I think what's happened here, I've removed one of those magnets and

**Dave Jones:** I think these were originally attached like this. So, I think what's happened, doesn't make sense to have the magnets in this location. Can start like getting them all out. And wow, there we go. Hello. They're quite powerful. So, I

**Dave Jones:** believe what is supposed to happen is, well, these are supposed to be attached to the rotor and the magnet is supposed to spin like this. So, it's not really a squirrel cage motor, but why they've got the laminations

**Dave Jones:** in there, I don't It's just a rotating magnet um in induction motor with the with the stators, that's how it's supposed to work with a rotating magnet in there. The only conclusion I can come to is that um yeah, these magnets were

**Dave Jones:** supposed to be around this rotor like this, and you supposed to have a rotating magnetic field, which then induces a magnetic field in the state of rotating magnetic field in the moving magnetic field um in the stator coils uh as it rotates, and

**Dave Jones:** um the Bob's your uncle, you get the um three-phase generation out of your stator coils. So, I can only presume that these things were originally like stuck on there, and they just flung themselves apart, and when they do, they just obviously um they

**Dave Jones:** just attract themselves over to uh the stator laminations down in there, and they stick to it, and boom, your motor just flung apart, and that's why it doesn't generate anything anymore. Aha! I got fooled for a second there. I

**Dave Jones:** thought that this looked like um a squirrel cage type motor, cuz you got the laminations in there, and I thought these looked like like at normal distance, visual distance, these actually looked like um the aluminum um bars that often they use

**Dave Jones:** uh copper as well uh to go through there, but these aren't. These are actually these are actually the glue marks between the magnets that were supposed to hold them on. So, I yeah, it's completely come a gutser there. They just haven't

**Dave Jones:** used enough glue on these things. They've just put a little bead down there, and that's it. Unbelievable. I guess it was pedaling too fast and it just spun itself way off. Oh, wow. That is That is terrible. That is terrible, Muriel. Unbelievable.

**Dave Jones:** And especially when you've got like using it on a bike like this where the vibrations are going to be absolutely awful, you know, that like No. No. No. No. No. No. Aha, I got the last of them out here and

**Dave Jones:** that one just falls off, fine, but I can't separate these two. So, they're like glued together. Yep. Yep. So, I think I think that's what's happened. I mean, I like I can't see any like there's no like super

**Dave Jones:** glue residue or anything. Like I can't see anything on there, but these two are obviously stuck together. All the others were kind of like individual and well, and then the whole thing is supposed to go together Oh, like that. Um

**Dave Jones:** I have I got one out. Yeah, but even those last two eventually fell apart. So, like there's basically no glue residue left on there and like there's none There seems to be none on like the base the curved base of this thing,

**Dave Jones:** which is making contact. There was just a absolute little sliver along the edge there and and that's what you can see in the rotor. Unbelievably crap quality. Wow, it's Oh, there's a washer in there as well. That's come

**Dave Jones:** out, but I think that sucker has flung itself apart. I think that's just piss poor uh construction of the rotor. Then once they fling apart, they actually magnetically attach to the stator and then it's then it's completely gone-ski. No wonder we're not

**Dave Jones:** getting anything out of it. So, this seems to be essentially a uh DC motor being used as a generator. Uh you can see the alternating uh north-south magnets there. They've marked it like that. But um yeah, I was

**Dave Jones:** a bit little bit confused by the laminations in there. We've got our steel laminations. It almost looked um squirrel cagey. So, I guess that's to you know, confine the magnetic field better or whatever. I don't know. I don't tear enough apart enough motors to

**Dave Jones:** uh know this sort of thing. And of course um yeah, you'd find three Hall effect sensors on a DC brushless uh motor. Um but normally they're a motor to drive them. In this particular case, they're using it as a generator

**Dave Jones:** and they're only using one of the um Hall effect sensors output as I said maybe to you know, detect low RPM or something like that cuz they don't have to uh drive the thing or anything like that. I don't think they've got any

**Dave Jones:** synchronous uh converter in there or anything to um to do that. I don't think it's that fancy. Um so, yeah. That's it. That's just spun itself apart. It's completely come agasser. So, that's just terrible, Muriel. Really. I mean,

**Dave Jones:** no wonder surprised it like lasted as long as it did. Uh like I don't believe it. Okay. So, I'm going to actually attempt to uh glue these magnets back on. Um just going to use some Aerodite, I guess.

**Dave Jones:** Use some 5-minute epoxy. Um you know, just just hold it on temporarily um to try and get this thing back in. If I try and actually just put it in with the just the magnets holding themselves around there and onto there, then it it

**Dave Jones:** doesn't have enough strength. It just sort of goes like and just sucks the magnets over onto the uh laminations of the stators there. Hopefully, it doesn't ooze out. But I'll put some on there and just uh try and stick the magnets on.

**Dave Jones:** Uh I won't give up my uh day job for a uh role on the production floor, that's for sure. Well, I'm not going to be riding my bike with this anytime soon, but there you go. And it doesn't feel so very smooth,

**Dave Jones:** but uh I think I might have goofed the magnets up in there because I uh the little red permanent marker they had on there, well, it wasn't permanent. They'd all rubbed off and um there while I was like physically handling them and

**Dave Jones:** it was a dog trying to get it back on. So, yeah, but they but there you go. That's 1 V per division. So, it's now working.

**Dave Jones:** Let's try the Dremel again. Wow, look at that. Okay, let's go to 10 V per division. Try that again. Look at that, 10 V per division. There you go. Winner, winner, chicken dinner. So, there you have it. This uh Cadence X

**Dave Jones:** Pedal Cell Bike Generator, convert your cycling motion into electricity to charge your devices, um is a load of crap. As I said, the person who sent it in has gone through two of these and yeah, that's just it just tore itself

**Dave Jones:** apart. Um that's just a brushless uh DC motor they're uh pressing into use as a generator on the bike and it didn't have nearly enough glue and then it's come a gutser. And how many out there, I don't

**Dave Jones:** know. Have you got one of these? Are they like, you know, chats on the forums about Cadence X uh generators failing and stuff like that. So, yeah, there's nothing wrong with the electronics, which I thought was um looks, you know, quite decent,

**Dave Jones:** actually. Um and I'm sure if I actually hooked that back up to here, it'd, you know, it'd work again. And it was interesting how it uh flung itself apart in there and the magnets stuck to the stators. And when I took it apart, I'm

**Dave Jones:** going, "This is kind of like how does this kind of work?" Um, you know, cuz it it just didn't make sense from a like a a traditional motor topology point of view, but it makes sense when you realize that all the damn magnets are

**Dave Jones:** flung off the stupid thing. Anyway, I hope you enjoyed that video. If you did, please give it a big thumbs up and discuss down below what you think about the implementation of this brushless DC motor and pressing it into service as a generator cuz that

**Dave Jones:** that that looks like all it is. It's not like a purpose-designed industrial type, you know, like commercial-grade motor in my opinion anyway, my vast opinion in our bicycle generators. Um, yeah, let us know what you think down below. Like, is this just like

**Dave Jones:** absolute garbage or like were they onto something with you know, using this with they just you know, bought a dodgy brand or maybe this is just like had a dodgy batch from the factory or something. I don't know, but

**Dave Jones:** you know, when when you mount this on a bike, there's going to be a ton of vibration on here and that's and that's going to you know, transfer down to the shaft and that's going to be shaking the

**Dave Jones:** buggery out of the magnets and I yeah, it's just completely fallen to bits and it was just interesting how like it felt smooth as silk. It felt like, you know, before I took it apart, was smooth as and we could measure the three stator

**Dave Jones:** coils in there and it said like it should have worked, but no, there there was no rotating magnet. So, no rotating magnetic field. Eh, you don't get much out of your stator coils when your magnetic field's not moving.

**Dave Jones:** Anyway, catch you next time.
