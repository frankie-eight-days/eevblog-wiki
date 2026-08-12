---
video_id: o7xfGuRaq94
title: EEVblog 1485 - PedalCell CadenceX Bike Generator LOL FAIL!
url: https://www.youtube.com/watch?v=o7xfGuRaq94
source: youtube-asr
timestamps: {"0": 0, "1": 26, "2": 37, "3": 53, "4": 62, "5": 74, "6": 88, "7": 102, "8": 118, "9": 131, "10": 146, "11": 160, "12": 175, "13": 188, "14": 202, "15": 222, "16": 242, "17": 256, "18": 267, "19": 278, "20": 288, "21": 299, "22": 314, "23": 329, "24": 347, "25": 358, "26": 374, "27": 395, "28": 405, "29": 419, "30": 434, "31": 451, "32": 474, "33": 501, "34": 527, "35": 553, "36": 571, "37": 587, "38": 596, "39": 613, "40": 625, "41": 635, "42": 650, "43": 666, "44": 685, "45": 697, "46": 710, "47": 720, "48": 745, "49": 755, "50": 768, "51": 781, "52": 797, "53": 814, "54": 830, "55": 838, "56": 854, "57": 872, "58": 889, "59": 899, "60": 909, "61": 931, "62": 950, "63": 965, "64": 978, "65": 997, "66": 1008}
---

**Dave Jones:** Hi, just a quick follow-up video to a mailbag item that I got, which is a Pedalsel bicycle generator USB thing. So, it's basically a generator here, which goes onto your rim here, spins around, and puts some charge into some supercaps, which then gives you a dual 5-V USB output so you can charge your phone while you're cycling and stuff like that.

**Dave Jones:** Anyway, it was supposed to be dead. The person who sent They sent actually said that they killed two of these things. And we couldn't see anything in the electronics if you want to see it.

**Dave Jones:** Here it is here. It was just a potted thing, so you know, not easy to get in there and sort of like reverse engineer everything. That's the rectification diodes for the input here, which just comes from the generator here.

**Dave Jones:** There's six wires there. So, I thought I'd just a few people asked if I could actually check the motor, actually have a look at the output of the motor, and see if anything's failed there.

**Dave Jones:** So, that's what I'm going to do in this video. So, I'm just going to get a pinout here. I've soldered on six wires, so I'm just going to go around and try and find the pinout for this thing.

**Dave Jones:** That one up there. Oh, no. 16 meg. Why is this 16 meg there? Okay. Anyway, it looks like that first pin doesn't connect to anything. So, that's a not connected.

**Dave Jones:** Next, we got one the second pin. So, the second pin here, which I'll I'm just going there. Doesn't matter which direction. They don't actually have numbers, but this pin here connects to this pin here with 8 ohms.

**Dave Jones:** That sounds like a coil to me. Okay, so that's what we've got there. The three, which I couldn't well, essentially non connected, and three to winding. So, it looks like we have our three windings in there, which is what you'd expect.

**Dave Jones:** If you have a closer up look at the board, and I'm going to have to because it's a gloss solder mask, you can see that Okay, we've got our three power lines there, and the other I can only see one trace coming off that center pin.

**Dave Jones:** So, maybe they've got a sensor in there or something. I can't see anything coming off these other pins. Maybe I can try and measure something pierce through if you're trying to probe through a conformal coating.

**Dave Jones:** You can have really sharp probes to make sure you get through. I'll just buzz that out to see if these go anywhere, but yeah, basically we've got our three winding wires plus our plus potentially up to three sensors there or at least one.

**Dave Jones:** Well, that's strange. I'm getting bugger all out of any of those windings. Nothing. That's 100 mV per division, and it's not a It's not a scale thing. I'm getting nothing.

**Dave Jones:** I'm getting nothing. So, what the heck's going on there? I mean, this is, you know, what you'd expect to measure for a three-phase generator. I don't know about the values 8 ohms, but uh I don't know.

**Dave Jones:** Like, this is like a three-phase generator going into a diode rectifier, and that gives you the output voltage. That's exactly what you'd expect. I mean, surely they'd give me something.

**Dave Jones:** If I'm spinning this sucker, I mean, I'm not going hugely fast, I expect to get something. Like, what the So, unless there is something in there cuz there was one trace going off, which looked like I don't know, it may have been going to a power source or something, but like I can like that's winding resistance that I'm measuring surely.

**Dave Jones:** I'm like, what? All right, let's try and actually rotate it faster. Um and you'll notice look look at all the spikes coming up when I turn on the Dremel, but let's try and net net Let's go pretty fast.

**Dave Jones:** I'm getting bugger all out of that. Nothing. There's definitely 8 ohms across there. Okay, and it doesn't matter which winding I choose. Um it's just it's getting nothing. Wow.

**Dave Jones:** What the? So, I don't know. Are all the windings like fused together or something like that? Aha, I found an access uh keyway in here, which gave me access to the two grub screws here.

**Dave Jones:** And tada, I'm now able to get this sucker off. We can potentially open the motor. Seems like a decent motor. It uses like SKS bearings in it. What's that?

**Dave Jones:** It's got any branding? There's Well, okay, so much for that. There's zero branding on that. But as I said, there is an SKS bearing in there. I believe they're okay, aren't they?

**Dave Jones:** Um I don't know. Uh I guess I can unfold it, open it up. There we go. Here's a peekaboo inside there. I'd have to desolder it, but I'm getting um bugger all out of the windings.

**Dave Jones:** Oh, I checked the winding resistances again. Yep. So, we've got U Y W there. They're the three windings. We've got VDD, ground, and then H U there, which H I presume would be Hall effect.

**Dave Jones:** So, they've got a Hall effect sensor on one only one of the windings. Obviously, they thought they might have three, but they only did one. So, I guess um even but the generator was generating nothing.

**Dave Jones:** So, uh looks like I can pop this PCB out. Tada. Got you. It's our winding. Um It's all a bit rough as guts. Bit how you doing. But uh like, you know, don't see any melted windings or anything like that.

**Dave Jones:** So, there's your rotor. And there's the magnets and the stators and I like I don't know. So, I would have expected to get What? There we go. Something out of that.

**Dave Jones:** There you go. That's interesting. They do have three Hall effect sensors in there. But they're only connecting up one of them. So, yeah, okay. Fine. Whatever. Um I don't even know why they need that.

**Dave Jones:** Maybe it like it cuts it off at like a minimum RPM or something like that would be my guess. So, what I've done is just measured some DC resistance around the pins on here and the operational one up here which is actually connected, um it measures they all all three measure identical resistances in various combinations on the pin.

**Dave Jones:** So, there's nothing obvious in terms of like one of them's, you know, gone kaput, shorted, whatever. So, So, there you go. We're getting 8 and 1/2 ohms on the winding.

**Dave Jones:** Well, I've put this back on. Doesn't spin that good now. It gets stuck in the muck. Put it on AC. And we get something out of it. Not much.

**Dave Jones:** Aha. I think what's happened here, I've removed one of those magnets and I think these were originally attached like this. So, I think what's happened, doesn't make sense to have the magnets in this location.

**Dave Jones:** Can start like getting them all out. And wow, there we go. Hello. They're quite powerful. So, I believe what is supposed to happen is, well, these are supposed to be attached to the rotor and the magnet is supposed to spin like this.

**Dave Jones:** So, it's not really a squirrel cage motor, but why they've got the laminations in there, I don't It's just a rotating magnet um in induction motor with the with the stators, that's how it's supposed to work with a rotating magnet in there.

**Dave Jones:** The only conclusion I can come to is that um yeah, these magnets were supposed to be around this rotor like this, and you supposed to have a rotating magnetic field, which then induces a magnetic field in the state of rotating magnetic field in the moving magnetic field um in the stator coils uh as it rotates, and um the Bob's your uncle, you get the um three-phase generation out of your

**Dave Jones:** stator coils. So, I can only presume that these things were originally like stuck on there, and they just flung themselves apart, and when they do, they just obviously um they just attract themselves over to uh the stator laminations down in there, and they stick to it, and boom, your motor just flung apart, and that's why it doesn't generate anything anymore.

**Dave Jones:** Aha! I got fooled for a second there. I thought that this looked like um a squirrel cage type motor, cuz you got the laminations in there, and I thought these looked like like at normal distance, visual distance, these actually looked like um the aluminum um bars that often they use uh copper as well uh to go through there, but these aren't.

**Dave Jones:** These are actually these are actually the glue marks between the magnets that were supposed to hold them on. So, I yeah, it's completely come a gutser there. They just haven't used enough glue on these things.

**Dave Jones:** They've just put a little bead down there, and that's it. Unbelievable. I guess it was pedaling too fast and it just spun itself way off. Oh, wow. That is That is terrible.

**Dave Jones:** That is terrible, Muriel. Unbelievable. And especially when you've got like using it on a bike like this where the vibrations are going to be absolutely awful, you know, that like No.

**Dave Jones:** No. No. No. No. No. Aha, I got the last of them out here and that one just falls off, fine, but I can't separate these two. So, they're like glued together.

**Dave Jones:** Yep. Yep. So, I think I think that's what's happened. I mean, I like I can't see any like there's no like super glue residue or anything. Like I can't see anything on there, but these two are obviously stuck together.

**Dave Jones:** All the others were kind of like individual and well, and then the whole thing is supposed to go together Oh, like that. Um I have I got one out.

**Dave Jones:** Yeah, but even those last two eventually fell apart. So, like there's basically no glue residue left on there and like there's none There seems to be none on like the base the curved base of this thing, which is making contact.

**Dave Jones:** There was just a absolute little sliver along the edge there and and that's what you can see in the rotor. Unbelievably crap quality. Wow, it's Oh, there's a washer in there as well.

**Dave Jones:** That's come out, but I think that sucker has flung itself apart. I think that's just piss poor uh construction of the rotor. Then once they fling apart, they actually magnetically attach to the stator and then it's then it's completely gone-ski.

**Dave Jones:** No wonder we're not getting anything out of it. So, this seems to be essentially a uh DC motor being used as a generator. Uh you can see the alternating uh north-south magnets there.

**Dave Jones:** They've marked it like that. But um yeah, I was a bit little bit confused by the laminations in there. We've got our steel laminations. It almost looked um squirrel cagey.

**Dave Jones:** So, I guess that's to you know, confine the magnetic field better or whatever. I don't know. I don't tear enough apart enough motors to uh know this sort of thing.

**Dave Jones:** And of course um yeah, you'd find three Hall effect sensors on a DC brushless uh motor. Um but normally they're a motor to drive them. In this particular case, they're using it as a generator and they're only using one of the um Hall effect sensors output as I said maybe to you know, detect low RPM or something like that cuz they don't have to uh drive the thing or anything like

**Dave Jones:** that. I don't think they've got any synchronous uh converter in there or anything to um to do that. I don't think it's that fancy. Um so, yeah. That's it.

**Dave Jones:** That's just spun itself apart. It's completely come agasser. So, that's just terrible, Muriel. Really. I mean, no wonder surprised it like lasted as long as it did. Uh like I don't believe it.

**Dave Jones:** Okay. So, I'm going to actually attempt to uh glue these magnets back on. Um just going to use some Aerodite, I guess. Use some 5-minute epoxy. Um you know, just just hold it on temporarily um to try and get this thing back in.

**Dave Jones:** If I try and actually just put it in with the just the magnets holding themselves around there and onto there, then it it doesn't have enough strength. It just sort of goes like and just sucks the magnets over onto the uh laminations of the stators there.

**Dave Jones:** Hopefully, it doesn't ooze out. But I'll put some on there and just uh try and stick the magnets on. Uh I won't give up my uh day job for a uh role on the production floor, that's for sure.

**Dave Jones:** Well, I'm not going to be riding my bike with this anytime soon, but there you go. And it doesn't feel so very smooth, but uh I think I might have goofed the magnets up in there because I uh the little red permanent marker they had on there, well, it wasn't permanent.

**Dave Jones:** They'd all rubbed off and um there while I was like physically handling them and it was a dog trying to get it back on. So, yeah, but they but there you go.

**Dave Jones:** That's 1 V per division. So, it's now working. Let's try the Dremel again. Wow, look at that. Okay, let's go to 10 V per division. Try that again. Look at that, 10 V per division.

**Dave Jones:** There you go. Winner, winner, chicken dinner. So, there you have it. This uh Cadence X Pedal Cell Bike Generator, convert your cycling motion into electricity to charge your devices, um is a load of crap.

**Dave Jones:** As I said, the person who sent it in has gone through two of these and yeah, that's just it just tore itself apart. Um that's just a brushless uh DC motor they're uh pressing into use as a generator on the bike and it didn't have nearly enough glue and then it's come a gutser.

**Dave Jones:** And how many out there, I don't know. Have you got one of these? Are they like, you know, chats on the forums about Cadence X uh generators failing and stuff like that.

**Dave Jones:** So, yeah, there's nothing wrong with the electronics, which I thought was um looks, you know, quite decent, actually. Um and I'm sure if I actually hooked that back up to here, it'd, you know, it'd work again.

**Dave Jones:** And it was interesting how it uh flung itself apart in there and the magnets stuck to the stators. And when I took it apart, I'm going, "This is kind of like how does this kind of work?" Um, you know, cuz it it just didn't make sense from a like a a traditional motor topology point of view, but it makes sense when you realize that all the damn magnets are

**Dave Jones:** flung off the stupid thing. Anyway, I hope you enjoyed that video. If you did, please give it a big thumbs up and discuss down below what you think about the implementation of this brushless DC motor and pressing it into service as a generator cuz that that that looks like all it is.

**Dave Jones:** It's not like a purpose-designed industrial type, you know, like commercial-grade motor in my opinion anyway, my vast opinion in our bicycle generators. Um, yeah, let us know what you think down below.

**Dave Jones:** Like, is this just like absolute garbage or like were they onto something with you know, using this with they just you know, bought a dodgy brand or maybe this is just like had a dodgy batch from the factory or something.

**Dave Jones:** I don't know, but you know, when when you mount this on a bike, there's going to be a ton of vibration on here and that's and that's going to you know, transfer down to the shaft and that's going to be shaking the buggery out of the magnets and I yeah, it's just completely fallen to bits and it was just interesting how like it felt smooth as silk.

**Dave Jones:** It felt like, you know, before I took it apart, was smooth as and we could measure the three stator coils in there and it said like it should have worked, but no, there there was no rotating magnet.

**Dave Jones:** So, no rotating magnetic field. Eh, you don't get much out of your stator coils when your magnetic field's not moving. Anyway, catch you next time.
