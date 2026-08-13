---
video_id: ihAG6cMpUlY
title: EEVblog #602 - Introduction to Microphones
url: https://www.youtube.com/watch?v=ihAG6cMpUlY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 27, "2": 44, "3": 63, "4": 88, "5": 108, "6": 130, "7": 154, "8": 180, "9": 193, "10": 211, "11": 234, "12": 271, "13": 293, "14": 312, "15": 338, "16": 354, "17": 371, "18": 402, "19": 424, "20": 444, "21": 463, "22": 480, "23": 512, "24": 541, "25": 560, "26": 589, "27": 607, "28": 633, "29": 653, "30": 674, "31": 692, "32": 708, "33": 735, "34": 759, "35": 782, "36": 807, "37": 825, "38": 846, "39": 863, "40": 877, "41": 899, "42": 925, "43": 947, "44": 964, "45": 981, "46": 1000, "47": 1022, "48": 1057, "49": 1078, "50": 1098, "51": 1127, "52": 1147, "53": 1172, "54": 1201, "55": 1229, "56": 1246, "57": 1269, "58": 1290, "59": 1310, "60": 1335, "61": 1354, "62": 1373, "63": 1390, "64": 1412, "65": 1433, "66": 1454, "67": 1472, "68": 1497, "69": 1515, "70": 1541, "71": 1570, "72": 1589, "73": 1616}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Got something special for you today. Microphones 101. Pretty niche-filled and, well, we need someone who knows all about it. Where is he? It's a computer pop-up. Doug Ford from Doug Ford Analog Design. Hey, Doug. G'day, Dave. If you've been watching the blog, you know Doug, and Doug is the former head designer at Rode Microphones.

**Dave Jones:** And at Jans Electronics. Yep. And I've spent my time also designing telephony headsets for call centres. So you're one of the microphone gurus. No, I've just been forced to gunpoint to find out about microphones. Excellent. So we're going to learn all about it.

**Dave Jones:** Microphones 101. Multiple videos for this one. I don't think we can do it all in one. Probably not. No. Let's go. Pretty much every microphone that I've ever come across, with one exception, relies on air vibration hitting a wobbly diaphragm and then we do something.

**Dave Jones:** Wobbly diagram. Wobbly diaphragm. How's it go? Wobbly diaphragm. Every microphone. Yeah. Yeah, pretty much. And they all then boil down to sensing what's happening with the movement of the diaphragm. Yep. Go back to the earliest days and we had a diaphragm, quite often cone-shaped.

**Dave Jones:** Sound would impinge on that and vibration on that would press against a capsule full of carbon granules. Terminal at the back, terminal at the front. As it pushed on the granules, it would change the resistance of the granules. Right. What about size of the granules?

**Dave Jones:** That would be all the difference, wouldn't it? It does. That would be the secret sauce. Well, to a pretty fair degree. Some variants didn't use granules. They actually used stacked disks of graphite under a small amount of pressure, just enough to hold them together.

**Dave Jones:** Yep. Their resistance varied and they were used in all telephone systems, going pretty much from Alexander Graham Bell or the other Italian guy who apparently beat him to the punch. Right. Whose name I can't remember. Right through to about the 1960s, even 1970s.

**Dave Jones:** There you go. One of the interesting things about those, incidentally. Oh, that'll be the phone, Reg. And action. Action. We've changed our shot. We've changed our shot. This is better. All right. Okay. Carbon granules stuff, I won't dwell on it or anything, but the old telephone beasties that you used to have, the front plate, the back plate and the satchel of carbon granules in there.

**Dave Jones:** After a period of time, the carbon granules would all settle down here. Yep. And stick to each other and get noisy and insensitive. So you'd pick up the handset and bang it on the table a few times to loosen things up. Got it.

**Dave Jones:** Now, after that, they were pretty much the first microphones. And nobody makes those anymore, even for niche applications? If you scraped around on eBay, you'd probably find something. Right. Okay. So there's no application for those anymore, is there? No. Right. No. Except in, maybe, legacy phone systems in upper Slobovia or something.

**Dave Jones:** Who knows? What's much more frequently done these days is you tie that to a coil and suspend that in a magnetic field. That looks familiar. Yeah. Magnetize the hell out of that so that you get a field across there. As the coil moves within the field, you can generate an EMF.

**Dave Jones:** Dynamic microphone. Dynamic. And a speaker. It's a speaker. Speakers work as mics. Speakers work beautifully as microphones. They're pretty. Beautifully. Beautifully. Beautifully. You get two identical speakers. Maybe three-inch rubbish that you scored out of photocopier or PC speakers. You connect them with a run of wire, and you listen to one and get somebody to talk into the other, you will hear it clear as a bell.

**Dave Jones:** There you go. They are surprisingly effective. Frequency response as a microphone is absolute rubbish. Rubbish. And they're probably insensitive as hell, as well. They're actually relatively sensitive, despite the fact that they're a low-impedance device. Yep. How do you put it? Their voltage sensitivity, you wouldn't write home about.

**Dave Jones:** But their ability to convert sound pressure into electrical energy is probably better than an actual microphone. Right. There you go. So the speaker's got fairly low-impedance wires, and a microphone has way more turns of much, much finer wire. Yep. So it's better at converting it into a voltage output.

**Dave Jones:** Got it. There you go. Okay. And these are still used? They're still frequently used. Most stage microphones these days are dynamic. Shure are probably the recognised leaders in dynamic microphones. Their SM58 is an iconic model being around for... Everyone uses it. I think they just celebrated their 50th birthday or something like that.

**Dave Jones:** Right. So they're fairly frequently used. Because you can scream into... you've got to have them right in your gob, right? Yes. And you've got to scream in. And you can scream into a huge dynamic range? Yes, because there's no fundamental limitation on how loud you take these.

**Dave Jones:** The fundamental limitation, in fact, is moving the cone so far that the corrugations around the edge lose linearity. Got it. There's no other fundamental limitation. And that's probably not going to happen until about 160, 170 or 180 dB SPL. And by then you're deaf.

**Dave Jones:** What? Or a jet engine's just gone by. Yeah. Got it. Incidentally, there's an interesting variation on that where the diaphragm itself is also the conductor that moves in the field. And what they are is a... and I'll draw this in 3D. Picture a sheet of aluminium, typically, which is actually corrugated so that the entire length of it is free to flex in and out.

**Dave Jones:** Right. And then you put around here a dirty grey horseshoe magnet. So if you're looking down from the top, this would be a diaphragm. And you've got this huge magnet around here. Got it. As that flexes backwards and forwards in the magnetic field, you're developing a voltage from the bottom to the top.

**Dave Jones:** Hmm. They're considered by a lot of the studio fraternity to be the duck's guts. All right. But there's an issue. The voltage coming out of those is so low that you have to put those into a transformer quite often with a couple of turns there and a couple of quadrillion turns over here to get any useful voltage out of them.

**Dave Jones:** Got it. The impedance of that is way under an ohm. There you go. They're also reputed to be relatively fragile. If you go pfft at them, that corrugated sheet of very, very thin aluminium just goes thong. Boom. And going over. So these are ribbon mics.

**Dave Jones:** They're ribbon microphones. Ribbon mic. And so the audio fools still use them. Oh, yeah. They still swear by them. And I think they're quite a good microphone. Okay. Realistically, they're no better or worse than any other good quality microphones, but some people just swear by them for certain purposes.

**Dave Jones:** Right. Yep. Well, that's the thing. You'll get a lot of musicians or whatever swearing by a certain mic because it has the certain sound. It's got their sound. It's got their sound. And they might have a microphone that they love using on hi-hats, another couple of microphones that they love using on vocals, this one for guitar cabinets, this one for kick drums, this one for recording outdoor explosions and foley effects and stuff like that.

**Dave Jones:** How much difference is there in terms of the distortion? Because we're talking about the sound differences between mics. It effectively comes down to a distortion component, does it? No. No? First of all, the raw microphone frequency response, which can vary between something that might look like that or something that's got quite a nasty bass peak or whatever you feel like there.

**Dave Jones:** Some of them are simply ruler flat. Measurement microphones are an example. Yes, of course. So the frequency response is one thing, but that's the coarse frequency response. You also get microstructure to the frequency response, which is shaped by the fact that the microphone pickup element is surrounded by stuff.

**Dave Jones:** The supports, whatever kind of mesh housing it's got, the microphone body itself, all of which adds very small deviations in there. Little type of resonant, mechanical resonant type. Some of it's mechanical, some of it's acoustic, some of it's proximity based. If you've got a microphone there that's sitting in a microphone housing, then it's going to receive both the direct sound and anything reflected from the structure.

**Dave Jones:** Of course, yep. All of which adds to what a lot of people call this microphone microstructure. Right. And some people claim it's audible, some people don't. I'm bowing out of that particular argument. Directional characteristics have a whole lot to do with it. We'll come to that one.

**Dave Jones:** Okay. Overload characteristics and linearity. And oddly enough, sometimes even just the kind of noise floor of the microphone. Got it. How easy is it to characterize and measure something like that, even with a $50,000 audio precision and professional level mics and stuff like that?

**Dave Jones:** Which aspect? Well, actually getting the frequency response of the microstructure. Actually being able to see the difference. That's actually a lot easier now with the advent of FFT based measurement systems. Once upon a time with swept sine measurement systems, really difficult to see.

**Dave Jones:** Right. But FFT based stuff. Just pulls it out of the... Yes. Pulls the data out of it. Mind you, sometimes you can't tell what's microstructure, what's FFT measurement system noise and randomness, and what's room reflection and structure around the actual measurement system itself.

**Dave Jones:** Right. Yeah. They will show up differences. Got it. Yeah. But the whole issue about linearity and SPL capacity has a lot to do with it. And as we'll see, the directionality of the thing has a whole lot to do with it too. Right.

**Dave Jones:** Okay. Yes, the patterns. Are we going to get into patterns here? We will shortly. Shortly. Excellent. Next week, people. All right. Other types of microphones. Well, no, actually patterns we'll get into this time. Okay. Sorry, you can edit that shit out, can't you?

**Dave Jones:** Probably. Yeah. We're not doing a one pass recording, are we? Yes, we are. All right, let's go. Other kinds of microphones. There's one that's come up recently, which is a fiber optic cable with a cut end, and sound pressure impinging on the cut end of the fiber optic cable can be sensed by an interferometer.

**Dave Jones:** Yep. A laser interferometer down at the receive end. Guess what? Still a variation on a wobbly diaphragm. Right. Everywhere you look, they're all going to be based on wobbly diaphragms. The only one that's not is this laser-based system, which apparently can sense the movement of a given air volume.

**Dave Jones:** Right. By using, again, laser interferometry techniques. It's all smoke and mirrors, but no. No pun intended. No pun absolutely intended. The big one, the big technology that's in use these days, though, is the condenser mic or electric mic. Right. An electric mic is a variation on a condenser mic.

**Dave Jones:** Effectively the same. You have your diaphragm. Notice I've drawn the corrugated edges so that it can actually flex, although that might not necessarily be there, near a parallel plate. And what we're sensing is the capacitance between usually a gold-spotted film on there and a metal plate over here.

**Dave Jones:** Why does it need to be gold-spotted? Basically because you need a conductive surface. Oh, of course. But it doesn't have to be gold. Gold just sounds fancy in marketing. And it doesn't rot off. Got it. Silver will. Oh, okay, yes. Silver corrodes. Yes, it tarnishes.

**Dave Jones:** Similarly, very, very, very thin stainless steel is also used. Okay, interesting. As the diaphragm. Yep. But mostly it's gold-spotted. Okay. And the reason for that is mylar, thin-sheet mylar, is a nice material to use for a diaphragm because it's flexible but stiff, if that makes sense.

**Dave Jones:** It does. Sputter some conductive material like gold. You could use aluminium. It's a bugger to connect to. Right. And even connecting to the gold sputtering is a bit of an exercise. Oh, okay. Right. So it's not just in China somebody just solders it on with a high current.

**Dave Jones:** Have you ever tried soldering mylar? No, it's not very good. Your iron just goes straight through it. So what is it, a point, is it a point contact, pressure contact? It's usually a pressure contact, in fact. Let's take that right to the edge.

**Dave Jones:** It's glued onto a ring. Right. It's either a conductive glue between there and that ring. So it would be the entire circular ring that conducts through, not just one point. And just occasionally, and I've got an example here, you'll see they actually put a screw through the middle there.

**Dave Jones:** So that actually forms an annular-shaped diaphragm because it's that bit that vibrates. The screw stays rigid, the ring stays rigid, and that vibrates as an annulus. Right, okay. And they do the electrical connection off that screw. Interesting. There you go. But it all boils back down to wobbly diaphragms.

**Dave Jones:** Yep. Okay. Microphones are used everywhere. Telephones, any recording device that you've ever come across. You've got one on your shirt right now. Yeah. Look, guys, just look around the room where you are and count how many appliances you've got that have got a microphone in them.

**Dave Jones:** Yep. And they're almost universally going to be an electric microphone, and we're going to come to operation of electric microphones shortly. But let's just have a look at the wobbly diaphragm and the acoustics involved, and how do we get different pickup patterns. Your one is an electric condenser.

**Dave Jones:** Reason being that you don't have enough power down here to support an external polarizing voltage of 60 volts, 90 volts, 200 volts, whatever it takes. So it's assuredly going to be an electric condenser as opposed to an externally polarized condenser. But it is a cardioid pattern, I believe.

**Dave Jones:** That may quite conceivably be so. Yes. Even in such a small size, they can get a cardioid pattern. We'll get into that. Yeah. Let's picture, first of all, the simplest microphone, which will be a wobbly diaphragm, and we'll ignore how we're sensing its movement.

**Dave Jones:** We'll just take that as a given. And we'll put that in a sealed can. All of a sudden, we've formed an omnidirectional microphone. It doesn't matter whether the waves are coming at it that way or that way or whatever. Any pressure that impinges on that diaphragm will cause it to wobble.

**Dave Jones:** The sound can come at it from the back. It's still going to cause pressure on that corresponding vibration. There is, of course, a caveat in that simple frequency dependency. Of course. We're starting to lose some arrays there. If the wavelength coming across that is fairly long, let's just draw that there, and the size of that is small compared to a wavelength,

**Dave Jones:** then it really doesn't matter what direction the waves are coming at it from it's going to receive. As soon as the diaphragm becomes physically large enough that, as drawn here, you might get a pressure wave there and a null there, pressure there and a null there.

**Dave Jones:** How physically big are we talking about? Quarter wavelength. Quarter wavelength. Once you get to a full half wavelength, that's the danger mark. Because when that becomes a half wavelength long and the sound is coming at it from the side, it means that... I'll just redraw this for clarity.

**Dave Jones:** We really are going to have to address that shortly. We're losing the fight. From the side, let's say we've got pressure wave, null, pressure wave, null, pressure wave. As they move across the surface, we've got a positive pressure wave, negative peak, positive peak, negative peak, rather than null.

**Dave Jones:** Got it. Simultaneously on the diaphragm, you're going to have a positive pressure peak and a negative pressure peak. They're going to cancel. So the frequency response from the side is actually going to be damn near zero at that frequency. Right. That's... how do you put it?

**Dave Jones:** When the diaphragm comes to be equal to pretty much a half wavelength, that's when you're going to get a null. How can it be, though, because audio is such a massive wavelength? Not really. Okay. Maths. It's maths time. All right. And I'll have to go dual polarity here for the Imperials and the Metricists.

**Dave Jones:** But, okay. Propagation velocity equals frequency times wavelength. Okay. For the Imperials, we'll call that 345 metres a second, or I think it's about 1,100 feet per second. Feet. No. No. Yes, yes, yes, yes, yes. You've got some U.S. viewers. They're still using feet and inches.

**Dave Jones:** And furlongs. Yeah. And rudes and poles and, yeah. No, that's the British. Right. Okay. At a kilohertz, say, okay, equals 1 kilohertz times 345 millimetres. So, at a kilohertz, that's about a wavelength. Okay. Now, a little microphone like that is way smaller than that.

**Dave Jones:** So, at a kilohertz, your typical little omni mic that might be 10 millimetres on diameter, it's going to be very, very omnidirectional. Okay. Let's go to 10 kilohertz, and the wavelength is down to 34.5 millimetres. Okay. How about that? We're getting down there.

**Dave Jones:** Okay. Yes. Go to 20 kilohertz, and we're down to about 17 odd millimetres, and that's definitely the danger point for your typical 10 millimetre or half inch microphone. Okay. I won't bother it. Thank you. Okay. That's 17 millimetres. Is that right? All right.

**Dave Jones:** Okay. So, that's a caveat on omnidirectional microphones. They really are omnidirectional until the wavelength gets too small. Right. And that means that a typical half inch measurement microphone, and let's show a half inch measurement microphone. Let's go get one. These are two of my measurement microphones.

**Dave Jones:** They're omnidirectional. And expensive. One of them particularly, this one from PCB Pizzatronics. Pizzatronics. Yeah, I know them. It's my main measurement microphone, and if I can remember how to open the damn thing. Okay. It's a half inch measurement microphone, half inch diameter there,

**Dave Jones:** with nice simple BNC connection there. BNC straight out. Nice. Yeah. There's actually a reasonable amount of electronics in the body. The actual microphone is only just that tip. Yep. In fact, now that's fairly tight. Oh, here we go. There we go. That shows you possibly, if we get the angle just right,

**Dave Jones:** that there's actually not a lot down in there. The microphone section itself is just the bare couple of top millimeters there. Okay. There it is. Wow. You can see it's got a, is that a film? Down the bottom, you're probably going to be hard pressed to see what's going on there,

**Dave Jones:** but we'll draw a cross section of that one maybe later and have a little look at that. That's the inside of a half inch lab measurement microphone. Yep. Incidentally, these have got pretty much a ruler flat frequency response from about, I think, 10 or 20 hertz up to about 15 kilohertz,

**Dave Jones:** and from 15 kilohertz through to 40 kilohertz, the response is characterized. It's not perfectly flat, though. It deviates by about a dB, dB and a half, something like that. That's still not too shabby. Yeah, it's pretty damn flat. Right. In its main band, how flat are we talking?

**Dave Jones:** Oh, 0.1 dB, 0.2 dB. Right. Possibly flatter. In fact, I think that any deviations are more the result of the measurement system than the microphone. Got it. So you rely on the inherent flatness of it as a measurement mic, or could you take into account the full measured characterization of it?

**Dave Jones:** Well, that would be too much of a pain, wouldn't it? As long as we don't disturb the mechanical construction of that head. And why has that head got so many openings like that? Basically, it needs protection for the diaphragm, yet acoustic transparency so that the sound gets to it.

**Dave Jones:** Yep, of course. And with a large number of relatively small openings like that, we get better than 50% opening ratio, and it will accept sound from pretty much any angle. So it behaves pretty much like a bare diaphragm, just with a bit of protection.

**Dave Jones:** So this is a multi-thousand dollar omni-measurement mic? I suspect these days they're about two, two and a half thousand dollars. Wow, nice. Cost me, I think, about $1,600 when I bought it, and that was half a dozen years ago. And who can actually calibrate these?

**Dave Jones:** The manufacturer can calibrate them for frequency response. We keep this honest because we've also got a one kilohertz spot calibrator, which generates 94 dB sound pressure level plus or minus 0.2 dB, and we use that for spot checks just to make sure that its sensitivity is consistent.

**Dave Jones:** How do you couple in that generator to it? Is it a set distance away, or is it inside a cavity? It's inside a cavity. It actually push fits into. It's a push fit, right. Yes, so it's sealed in there. Got it. And the calibrator itself has internal feedback

**Dave Jones:** and its own internal servo system to maintain consistent pressure inside that cavity. Secondary microphones are basically almost identical, except that these ones here, they really are awfully, awfully similar. It's identical? What are you talking about? Oh, no. You bought a Swiftie. Well, actually, damn near it.

**Dave Jones:** Yeah. Spot the difference. Pretty close. This one is from 797 Radio Factory. Well, I think they call themselves 797 Audio these days, China. And these cost about $250, $300. Way cheaper than these ones. And I trust them almost as much because they come with a very nice cal certificate.

**Dave Jones:** You trust the Chinese cal certificate? Oh, yeah. Well, Brill and Kerr printout. Ah, Brill and Kerr printout. Yep, yep. Okay, I can trust that. Okay. Yep. Which shows the free field and pressure response. And you'll notice that that goes to 40 kilohertz. Yep.

**Dave Jones:** And deviates by, well, in this case, I think a dB and a half at 18 on kilohertz with a positive peak of about, what's that, a dB at 40 kilohertz. That's pretty good. Yeah. For a couple hundred bucks. Yeah. So, again, we can keep these microphones honest with the microphone calibrator with regard to sensitivity.

**Dave Jones:** And we can reasonably assume that the frequency response is going to be flat within the frequency band of interest to us. Okay.
