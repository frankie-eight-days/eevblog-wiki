---
video_id: sNW3Xqtgkus
title: EEVblog #1027 -  Implantable NeuroStimulator Teardown
url: https://www.youtube.com/watch?v=sNW3Xqtgkus
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 27, "3": 40, "4": 64, "5": 77, "6": 91, "7": 104, "8": 122, "9": 134, "10": 151, "11": 164, "12": 182, "13": 196, "14": 205, "15": 221, "16": 235, "17": 243, "18": 255, "19": 265, "20": 294, "21": 307, "22": 319, "23": 334, "24": 358, "25": 372, "26": 403, "27": 429, "28": 454, "29": 467, "30": 486, "31": 501, "32": 517, "33": 525, "34": 540, "35": 560, "36": 576, "37": 590, "38": 607, "39": 620, "40": 628, "41": 643, "42": 659, "43": 679, "44": 694, "45": 713, "46": 725, "47": 739, "48": 764, "49": 780, "50": 799, "51": 822, "52": 837, "53": 852, "54": 867, "55": 881, "56": 897, "57": 911, "58": 926, "59": 938, "60": 950, "61": 968, "62": 981, "63": 990, "64": 1003, "65": 1011, "66": 1024, "67": 1037, "68": 1047, "69": 1068, "70": 1080, "71": 1096, "72": 1111, "73": 1122, "74": 1136, "75": 1151, "76": 1160, "77": 1170, "78": 1185, "79": 1196, "80": 1211, "81": 1219, "82": 1240, "83": 1248, "84": 1261, "85": 1282, "86": 1293, "87": 1305, "88": 1319, "89": 1329, "90": 1342, "91": 1354, "92": 1365, "93": 1386, "94": 1401, "95": 1416}
---

**Dave Jones:** Hi, got a very interesting teardown for you today. Let's check it out. This one's actually a very old mailbag item. Thank you very much Manu for sending this in a long time ago in a mailbag galaxy far, far away.

**Dave Jones:** And sorry I haven't gotten around to doing this. Now, a lot of people are familiar with a product that looks something like this. You might think that this is actually an implantable pacemaker, but it's actually not quite that.

**Dave Jones:** It is different. It's a neurostimulator uh designed to um send impulses into the uh nervous system. Yes, it is an implantable device and it's designed to treat neuropathic pain.

**Dave Jones:** And you know, like presumably very chronic because uh getting one of these installed um implanted into you is not a trivial thing. So, yeah, you'd want to have like a real chronic uh case of neuropathic uh pain to actually uh go to this effort cuz you know, the first step is drugs and other uh you know, opioids and other things to uh treat the pain.

**Dave Jones:** And yes, this one here is actually an ex-implanted device. And yes, it's okay. It has been properly uh sterilized and everything else. So, this used to be inside somebody's uh body.

**Dave Jones:** Sorry, I don't have the details. If you know the serial number, play along at home. Is that your one? Now, a neurostimulator is actually coming all sorts of forms of which uh the pacemaker is effectively uh one of them.

**Dave Jones:** But this one uh doesn't go to the heart. This one I believe actually connects into the uh nerves going into the uh or into the neck. Um but you can get ones that uh connect to your spinal cord and other uh locations.

**Dave Jones:** Now, this one's actually installed in the uh subcutaneous pocket and I'll include a little photo of where that one's uh actually installed. And then the little uh cable, which we don't have uh sadly, which actually interfaces to uh these two uh these two connections in here, but there's actually multiple connections on here.

**Dave Jones:** You can actually see it's actually four pins, so each one of those contains uh two connections. And the cable just goes off to the implantable device. And yes, this is a non-rechargeable thing.

**Dave Jones:** It's got a built-in uh lithium battery, which basically effectively lasts the shelf life. I don't think they actually give a like a guaranteed battery life for this thing, but it's like you know, it's like 10 years in the on plus in the order of the internal uh battery in there, which we'll take a look at when we do the teardown of this thing.

**Dave Jones:** Because obviously, you don't need uh much current at all, effectively nothing, to uh stimulate the neuron. So, this thing could be uh running um you know, practically all the time, and it's not going to flatten the battery.

**Dave Jones:** Basically, shelf life. So, yeah, incredibly low-powered device. Now, this is the I-Trial 3 from a company called Medtronic, and they're uh pretty much one of the leading uh providers of these, you know, pacemakers, uh neurostimulators, and uh other things.

**Dave Jones:** So, this I believe this design dates from uh '93 or thereabouts. I don't know when this particular one was uh manufactured, but they would you know, a lot of design effort and uh certification goes into these things.

**Dave Jones:** So, once they design them, they typically sell them for a long, long time. Now, of course, these things use medical-grade material cuz they are implantable or fully certified and uh tested, of course.

**Dave Jones:** It's got a uh titanium case. It's got a uh poly uh urethane interface connector block up here and uh silicone rubber um seals and other uh things. And they're actually yes, they are little uh hex screws, basically.

**Dave Jones:** You can get like a specialized uh tool, which actually uh well, comes with it, I believe, when you buy it. Comes straight out of the box with the uh tool to actually uh, get in there and uh adjust well, uh, tighten up the connector once you've plugged it in there.

**Dave Jones:** They don't just shove it in there and just rely on uh, friction. They do actually uh, tighten it up. And they've very thoughtfully provided the pin out on there.

**Dave Jones:** There you go, for the four connections there. Cuz you don't want the doctor to get it backwards, that would really ruin your day. You come out of surgery doing cartwheels and believing that the solar always and you being a good practical ideas.

**Dave Jones:** So, I won't pretend to know the uh, physiology behind all these things. Let's get to what everyone here is for. Let's tear this puppy apart. I think it's going to need the Dremel for this one.

**Dave Jones:** Uh, ultrasonically welded uh, titanium case, of course. Uh, and yeah, that looks serious business. Hmm. And bingo, we're in like Flynn. Check it out. Actually, uh, I went through like one and a half of those uh, Dremel cutting wheels getting through that uh, titanium, but we're in.

**Dave Jones:** And you can see uh, we've basically got the uh, most of the space is taken up with the battery here. Now, this is a lithium final chloride battery, very common in industrial and uh, medical applications like this.

**Dave Jones:** They're typically you won't find them uh, too frequently in any sort of uh, commercial market or things like that. Now, these are actually uh, quite chemically reactive and uh, can be uh, exothermic.

**Dave Jones:** So, they can actually, you know, heat up and potentially explode, but I'm sure that these are specifically designed internal um, you know, manufactured very tight manufacturing tolerances to prevent all that uh, stuff from happening.

**Dave Jones:** So, I'm sure they've uh, done their homework. And I'm using the uh, Tagarno microscope here to take a look. Now, this could actually be a uh, some sort of vent or that actually might be where they filled the electrolyte uh, perhaps and then sealed it off cuz these are wet electrolyte and it would actually react with stuff if it was if it actually leaked out of course but

**Dave Jones:** look we can they've actually using the outside of the case is the presumably the negative terminal there they've actually welded this this gold like big stud thing on there so that and then they can bond wire over there.

**Dave Jones:** Um so they've actually soldered welded or whatever that down to the can and then they've got the wires buggering off in here through looks like a little is that an that feels pretty solid I thought that was like a some sort of plastic tube it could actually be a glass tube or something maybe not entirely uh entirely sure but anyway it's designed to be an insulating tube going through

**Dave Jones:** there taking the wire off um of course uh so that it doesn't there's no chance of it shorting out to the can here and shorting out the battery but interestingly you'll you'll notice that we've got the double bond wires going over here like this this is for redundancy of course in a critical implanted device like this there's no way you're going to rely on one bond wire although they having said that over

**Dave Jones:** here that goes to the connections they have actually just done the one bond wire going off to the case. So like if that broke maybe it's not a huge deal I'm not sure why they decided to do one there but all the other ones you can see through the penetrators here which go outside the case that'd be sealed is that that is a silicone yeah that's rubber

**Dave Jones:** that's rubber I'm not sure if you can see that deform there but that would be a silicone rubber um seal around those uh uh penetrators there which uh go outside the case.

**Dave Jones:** That's the uh term for anything that uh goes through a uh sealed case like this is a penetrator. And we'll actually go out and just have a quick squeeze under there, then you can see the wires actually coming out there like that, and then going into the uh little hex screws are in there.

**Dave Jones:** Is that some Yeah, that's sort of Is that a re- I don't think Is that a re-enterable gel or something? Anyway, there's little uh I believe there's little hex screws in there which uh then screwed down to the uh to the connectors inside there.

**Dave Jones:** But uh yes, by the way, I have actually measured this battery and it measures zero. There's nothing coming out of So, this one is completely and utterly dead. Um I'm not sure if '98 um is the year of manufacture.

**Dave Jones:** That doesn't look like your traditional uh date code type stuff happening there. So, I'm not sure what the deal is there. Now, of course, the interesting stuff is the uh PCB.

**Dave Jones:** And uh one of the first things I noticed, of course, were uh tantalum caps. And a lot of people might be surprised to find tantalum caps in there cuz they're notorious for, you know, catching on fire and uh stuff like that.

**Dave Jones:** But these aren't just some one-hung low things that they're getting from uh the Shenzhen market. These would be fully qualified parts. In fact, every part in this would uh most likely uh by law, I would I guess, uh by certification, uh actually required to be uh signed off by the manufacturer.

**Dave Jones:** The manufacturers of these parts are not good in the data sheets. It's very common to read "Not uh you know, not suitable for implantable devices." If you want to implant them uh or using life-saving devices, things like that, uh then you have to get specific permission from the manufacturer.

**Dave Jones:** So, these would be very uh carefully selected, sought, ordered, and certified, and stuff like that. And we're not talking about using these for, you know, really like high peak currents and stuff like that.

**Dave Jones:** So, it's not really a big deal. Anyway, we've got a ceramic substrate down here, and you can see that we've actually got, technically, a ceramic hybrid. Cuz that, if I can if that focus.

**Dave Jones:** Come on. You can see down in there, that is a hybrid resistor with a little laser trim mark. You'll notice there's another one there as well. So, we've got two resistors.

**Dave Jones:** There could very well be components on the top, cuz I don't see any chips on here. So, most likely on the bottom. But then we've got our multi-layer ceramic caps.

**Dave Jones:** We've got different types here. They'd all have all, of course, be specifically engineered, specifically chosen for the task. We've got one, presumably some sort of in there. What's a 133?

**Dave Jones:** I'm not sure. Those who those SMD code aficionados can go look that one up. That is a 500 micro Henry inductor. It's a bit hard to read that. But yeah, that's 500 mic.

**Dave Jones:** Uh And what is that puppy? Is that another inductor? It's a 289. Doesn't look so different. So, I'm not sure. That almost looks like maybe that could be the coil for the receiver, perhaps, because they've got to have a receiver in this thing um to communicate with it.

**Dave Jones:** Well, at least receive instructions from the handheld patient unit, who can actually, you know, play around with the settings and whatnot for this thing. Now, as for this puppy, got a ceramic top on it.

**Dave Jones:** It's only two pins, so maybe is it uh is it a crystal? Perhaps. Um I don't know. Weird. But of course, one of the most interesting things in here, look, it's a reed switch.

**Dave Jones:** There are contacts there, look, they're welded onto there. It doesn't look like they're soldered, looks like they're welded down somehow, and they're actually blobbed in place like this. That's nice attention to detail.

**Dave Jones:** Of And they're probably a requirement of the production process that you actually blob them down first like that, let it set, and then you come along and go you know, weld weld like that as part of the production process.

**Dave Jones:** But of course, the reed switch, that's a magnetic reed switch, and that looks like a normally closed one. Actually, that looks normally closed to me. If you look at those contacts, so you can switch either the entire device or more likely just like the output or something like that on or off via a magnet which you place presumably on the back of your neck near where the unit is implanted,

**Dave Jones:** and that activates your micro your reed switch. And you might notice this rubber here, that just sits in that little pocket. I really don't know what that's for. It's some sort of a space filler or something.

**Dave Jones:** I don't know why they bothered. Beulah. Beulah. So what we'll do now is just try and uh leave this puppy out. It's going to be stuck in there and uh see if we can access get the board out cuz I think this battery is got to got to come out first.

**Dave Jones:** Yeah, that's held down with adhesive. And that is actually a adhesive because it's got to be that's the only thing inside allowed inside these things. Well, actually on the outside because I guess cuz this is on the ultrasonically welded inside but yeah, we've just got an adhesive strip there.

**Dave Jones:** So we'll just rip that off. Sorry for you bond wire fishionados. I broke it. Oops. But yeah, that battery certainly is dead. There's no other identifying marks on that either.

**Dave Jones:** So you can see how there's a Is that a Yeah, it's some sort of plastic carrier in there. So we'll try and get a knife in there and I'm going to have to break these beautiful bond wires.

**Dave Jones:** Um bit of a shame but we're going to have to sacrifice this puppy in the name of engineering education I'm afraid. I've already ruined it. was a thing of beauty is a joy forever.

**Dave Jones:** Getting the knife down in there wasn't too uh All right. Come on. Geez, this is uh really tough. I've tried to get the knife down in there but wouldn't have a bar of it.

**Dave Jones:** Completely stuck down probably. All right, I'm pretty darn sure I'm going to have to apply greater force on this to get it out. I expect the ceramic hybrid base to crack before I get this out.

**Dave Jones:** Sorry for those who think this is beautiful and I shouldn't be DESTROYING IT BUT AH THERE WE GO. YEAH, chipped it. And you can see the bloody glue under there.

**Dave Jones:** Unbelievable. Somebody went ballistic on the production line. Why? But I think you can see what's going to be on the bottom. In fact, I don't think there's any other components apart from that one big blobbed ASIC in there.

**Dave Jones:** And trust me, they are running ASICs inside this thing. It's not going to You're not going to find any sort of general purpose micro controller inside one of these puppies.

**Dave Jones:** They're going to be fully custom ASIC design for ultra low power design for the exact uh requirements of what this thing needs to do. So, yeah, it's just completely blobbed.

**Dave Jones:** I don't think there's anything interesting under there at all. Those numbers just some sort of production code. But, yeah, I don't think there's much else in there. Don't think I showed you that before, the beautiful gold-plated end caps on those tantalum capacitors.

**Dave Jones:** Uh Wonder how much they paid for those puppies. Yep, I'm pretty sure that's the only thing under there is a gigantic chip. I don't know uh what size die that would be under there.

**Dave Jones:** But, uh whether or not it's any tiny die and they're just bond wiring bond wiring stuff out. And they're just putting a huge encapsulant uh over the whole thing.

**Dave Jones:** I mean, you wouldn't need a huge This is not, you know, you're not going to use a like a 15 mm die or something in there. But, uh you know, things like the cochlear implants and stuff like that have uh massive requirements.

**Dave Jones:** I should have actually done this before I tried to attack that uh board in there. I thought I'd uh pair it up. And sure enough, uh 3.7 V soldered some wires on there.

**Dave Jones:** Sure enough, 22 odd microamps. So, yeah, that's exactly what you'd expect. This is a 2.7 amp hour uh battery. So, you know, it's basically going to last the uh shelf life.

**Dave Jones:** So, this is the basic operation of it. Now, um little tip, you can get the uh the magnetic uh hanger from your multimeter. And you can use that, hopefully.

**Dave Jones:** Does that Does that change Something's changing. And it's certainly starting to climb up. So, maybe we've switched it on. We've done something. So, like I have no idea if I've damaged this physically.

**Dave Jones:** Um those ceramic hybrids are pretty robust. They basically don't flex. They just uh shatter. So, I don't think that I've actually damaged that hybrid. Um so, looks like it might still be operational, but it's sort of steadily the average current increased in 23 microamps.

**Dave Jones:** Slowly going up, I think. Let's actually take a quick probe of the waveforms here. I've got it on the uh battery common. So, you know, I've no idea where the absolute the actual reference is.

**Dave Jones:** Let's start with the top one there. Aha, this is all 50 hertz stuff. So, too much of a coincydink? Yeah. Um I can't say anything else. That's the mains frequency.

**Dave Jones:** So, what's going on there? I don't know. I don't even know the amplitude levels for uh you know, nerve stimulation neurostimulation techniques. So, and yes, I've tried that with the uh magnet as well, and there's pretty much nothing doing there.

**Dave Jones:** So, Sorry. Tell you what though, we are getting something on one side of what I thought was that the with that white ceramic package there, which I I kind of guess was a crystal.

**Dave Jones:** It's not. Um it's doing something else. So, that's a slow time base. That's 200 milliseconds per division. 1 2 3 4. Like it's just over 800 and you know, 810 milliseconds or something between those pulses.

**Dave Jones:** So, I like is that the stimulation period or whatnot? Hm, no idea. And I can't actually get the magnet to activate the reed switch. There we go. Let's try it again.

**Dave Jones:** Boom, there we go. Got it. So, unfortunately, it looks like that's pretty much all we can do for this uh thing. And well, there's not much in here at all.

**Dave Jones:** The teardown wasn't uh as interesting as I thought it might be, but I didn't know what I was expecting really. I mean, it's not like it's a uh you know, like a cardiac uh pacemaker or anything like that.

**Dave Jones:** It's just a neurostimulator, very low-power neurostimulator that's uh designed to be um implanted into the nervous system, the uh spinal column, or the uh nerves going into the neck or even a direct brain.

**Dave Jones:** I don't think this model does the direct uh brain stuff, but uh yeah, it's designed for neurostimulation for pain relief and your chronic, you know, pain relief if you're desperate enough to get one of these uh installed.

**Dave Jones:** If you've got one of these, let us know. Leave it in the comments down below how it's working for you, what the procedure was to install it, how you how it was, you know, did they have to calibrate the thing for your individual requirements?

**Dave Jones:** You know, how often do you have to use it? Is it always firing or do you only put the magnet thing on the back of you to activate it when you get in uh chronic pain or whatnot?

**Dave Jones:** Let us know cuz I really don't know any I don't know anyone who actually uses one of these things, but I've I'm led to believe they're, you know, not that uncommon uh in the general population, you know, cuz there's like like I think it's 5 to 10% of the population or something suffers from some sort of uh new neurological uh type pain.

**Dave Jones:** So, I guess there's, you know, got to be, you know, at least a partial percent of people that uh uh chronic enough to warrant uh one of these neurostimulators.

**Dave Jones:** But, so I hope you found that teardown interesting at least. I mean, the most interesting part of this is basically, well, a lot of people say the boring part, and it is uh but it's critical is the certification of the design process.

**Dave Jones:** It can take years and years and years. I've actually done some work for an implantable uh device company and they, you know, just the amount of effort that goes into like not only designing the ASIC chip, but designing every single part, qualifying every single part that goes into it, and everything else is just a ridiculous amount of work.

**Dave Jones:** And if I'm conceiving the latest our product or, you know, next generation product to when it actually gets released to market can be, you know, like 5 to 8 years or something like that.

**Dave Jones:** It is a long development cycle. Uh cuz, you know, implantable devices have to be ridiculously certified. So, they certainly weren't trying to make this thing as small as possible.

**Dave Jones:** I mean, the new generations are probably thinner and smaller, but you know, they they've made no real effort to shrink that down apart from the ASIC, of course, which probably does, you know, a fair bit.

**Dave Jones:** But, you know, it's a probably a fairly complex ASIC. But, yeah, I mean, this is basically just made some large-scale parts on here. Made no effort effort to get it down, especially with the connector and everything like that.

**Dave Jones:** So, you know, these would be pretty bulky inside you. But, like I said, this is early '90s tech, I believe. It would have That's when Well, that's when the data sheet, the manual for this thing.

**Dave Jones:** So, this probably would have been designed in the late '80s. So, just take that into account. So, thank you very much, Manny, for sending that in. And I did actually get another one, which is the a Prime Advanced.

**Dave Jones:** Here, I actually got two of these. So, I was able to tear down that one. But, maybe now in maybe in a separate video I can tear down this, but it's probably very similar.

**Dave Jones:** This one is actually spinal cord neuro neurostimulation. So, it's actually a 16-channel job. So, yeah, really much more advanced than this little I don't know whether it's like four-channel or whether or not it's like two-channel or whatever with the uh pros, but yeah, 16 channel job, probably extremely similar inside those.

**Dave Jones:** And yeah, um this one is the non-MRI one. You can actually get the latest version is like MRI compatible, so you can put them inside MRI machines and you're not going to like they're not going to explode or, you know, sort of be extracted from your body or whatnot.

**Dave Jones:** Um so, yeah, specific ones designed to be MRI compatible. Anyway, hope you enjoyed that look at implantable medical electronics. If you did, please give it a big thumbs up and as always, discuss down below, especially if you've got one of these.

**Dave Jones:** Be really interested to hear from people who've got one of these puppies installed. Catch you next time.
