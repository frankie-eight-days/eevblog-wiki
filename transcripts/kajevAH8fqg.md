---
video_id: kajevAH8fqg
title: EEVblog #832 - Keysight U1282A Multimeter Teardown
url: https://www.youtube.com/watch?v=kajevAH8fqg
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 34, "3": 51, "4": 64, "5": 82, "6": 94, "7": 111, "8": 126, "9": 146, "10": 160, "11": 169, "12": 190, "13": 200, "14": 219, "15": 236, "16": 247, "17": 261, "18": 279, "19": 291, "20": 304, "21": 320, "22": 329, "23": 338, "24": 347, "25": 359, "26": 375, "27": 388, "28": 400, "29": 415, "30": 427, "31": 449, "32": 458, "33": 472, "34": 487, "35": 495, "36": 510, "37": 519, "38": 533, "39": 551, "40": 567, "41": 583, "42": 591, "43": 606, "44": 618, "45": 628, "46": 644, "47": 655, "48": 671, "49": 687, "50": 699, "51": 708, "52": 718, "53": 729, "54": 744, "55": 758, "56": 771, "57": 779, "58": 788, "59": 802, "60": 816, "61": 841, "62": 851, "63": 870, "64": 884, "65": 896, "66": 913, "67": 925, "68": 936, "69": 954, "70": 965, "71": 980, "72": 997, "73": 1009, "74": 1028, "75": 1046, "76": 1059, "77": 1072, "78": 1084, "79": 1093, "80": 1108, "81": 1123, "82": 1137, "83": 1150, "84": 1159, "85": 1173, "86": 1187, "87": 1194, "88": 1207, "89": 1222, "90": 1235, "91": 1248, "92": 1263, "93": 1281, "94": 1290, "95": 1298, "96": 1320, "97": 1332, "98": 1346, "99": 1357, "100": 1368, "101": 1383, "102": 1397, "103": 1414, "104": 1430, "105": 1441, "106": 1457, "107": 1469, "108": 1481, "109": 1490, "110": 1506, "111": 1520, "112": 1532, "113": 1548, "114": 1560, "115": 1572, "116": 1586, "117": 1610, "118": 1621, "119": 1640, "120": 1653, "121": 1668, "122": 1687, "123": 1700, "124": 1716, "125": 1730, "126": 1751, "127": 1764, "128": 1783, "129": 1795, "130": 1808, "131": 1819, "132": 1828, "133": 1836, "134": 1849, "135": 1864, "136": 1872, "137": 1887, "138": 1898, "139": 1908, "140": 1920, "141": 1930, "142": 1941, "143": 1952, "144": 1970, "145": 1982, "146": 1997, "147": 2010, "148": 2023, "149": 2033, "150": 2052, "151": 2063, "152": 2074, "153": 2088, "154": 2099, "155": 2114, "156": 2126, "157": 2137, "158": 2146, "159": 2159, "160": 2179, "161": 2191, "162": 2210, "163": 2223, "164": 2235, "165": 2253, "166": 2265, "167": 2276, "168": 2288, "169": 2310, "170": 2323, "171": 2333, "172": 2341, "173": 2360, "174": 2373, "175": 2391, "176": 2401, "177": 2414, "178": 2429, "179": 2440, "180": 2452, "181": 2468, "182": 2482, "183": 2496}
---

**Dave Jones:** Hi, we've got another multimeter teardown. This one's rather exciting because Keysight have released a new series of multimeter. In fact, two new series, the U1280 which we're going to take a look at today, the high-end one, and also the U1240C.

**Dave Jones:** And the U1240C model is designed to replace the U1240B which was derived from the old Escort designs which Agilent at the time actually bought. So, yeah, they've completely revamped, completely replaced this with these super duper rugged new multimeters.

**Dave Jones:** And they want me to pull it apart. Sorry, I was supposed to get a like a world scoop on this. They actually sent them to me before they were actually released at the start of this month, but the courier lost them.

**Dave Jones:** They just vanished into the ether. And there was like two or three multimeters in there. Just yep, vanished. Bloody tool. Pain in the butt. Anyway, they finally got me two new ones of these.

**Dave Jones:** One to pull up one to pull apart and actually review, and the other to beat the crap out of. So, yes, I'm going to have to take one of these puppies canyoning or through some other thing because these are IP68 or 67 rated.

**Dave Jones:** So, waterproof to 1 m and drop proof to 3 m. So, let's go. And well, what the hell, might as well do an unboxing because well, I just opened the box.

**Dave Jones:** Then, we've got ourselves a cal certificate. Beauty. You got a product some fluff lab. Bloody box contents list. Handout don't want to bloody user manual. It's a multimeter. And blah blah whatever blah.

**Dave Jones:** Yeah, they look happy. Yeah, right. Okay, probes. And we've got four AA batteries. One of the big advantages of this, uh, new model, the 1280, here it is. Jeez, I'll show you some size comparisons in a minute, but it's a big beast.

**Dave Jones:** 800 hours battery life. Oh, freaking awesome. You know I'm a fanboy of, uh, big battery life multimeters, and the, um, USB interface lead, the old, uh, school infrared, um, you know, it's got the same, uh, compatible, Agilent Keysight infrared thing that we're used to.

**Dave Jones:** I didn't know it actually came standard with this, but maybe it does. And just for those calibration certificate aficionados out there, I know you're out there, there's the, uh, gear that they use to calibrate this thing, and you get yourself a little cow sticker.

**Dave Jones:** Stick it on. Beauty. But, yeah, that's it. No actual watt test results. I'll tell you what, thumbs up for providing the Maxell alkalines here, not one hung low brand.

**Dave Jones:** And just for kicks, let's take a look at the size comparison here. You can see pretty much the biggest beast, uh, in this lineup here. Against, uh, probably in the ruggedness, uh, department, its direct competitor, the Fluke, uh, 28 Series II, which you've no doubt seen me, uh, beat the absolute crap out of it.

**Dave Jones:** It's also, uh, 3 m drop proof and IP67 rated. So, in terms of ruggedness, yep, and that's, you know, pretty much its main competitor. And compared to a Fluke 87V, it is a monster.

**Dave Jones:** And compare it to one of my favorites, the little compact, uh, Brymens, the, uh, 200 Series Brymens. Uh, it's just, it's really big. So, yes, this thing just does feel absolutely ginormous in your hands, and that's, to me, that's not a good thing.

**Dave Jones:** I, you know, it, it's super duper rugged. Absolutely no worries, uh, about it at all, but it's just absolutely enormous. Takes up a lot of room on your bench if you're going to use this as a bench meter and I don't know why it has to actually be that big.

**Dave Jones:** Okay, it's dual display and the display is absolutely enormous and yes, it is cat four 600 volt input rated. So you have to have the requisite spacings in there to do all that.

**Dave Jones:** Yes, it does use four double a batteries, but hey, I know of a meter maybe coming soon that's not much bigger than this thing and it's got four double a batteries and dual display.

**Dave Jones:** So you know, Anyway, this is a top of the line multimeter. We're talking about $500 street price. The this is the 1282A the 1281A with a few little less features is like $450 US street price.

**Dave Jones:** So I don't know why you'd get the 1281A I you know, your average thinking person probably wouldn't buy that. You'd spring the extra 50 bucks and get this puppy no doubt.

**Dave Jones:** But yeah, it's just a big ass rugged multimeter. But look, curiously, it's got a RMT extra turn line here. You probably guess what that stands for. Stands for remote.

**Dave Jones:** So it actually doesn't come standard with a remote probe, but it can actually get a a remote probe which has an extra pin on there that hooks up and allows you just to like use the hold function apparently the meter.

**Dave Jones:** I don't know why. They've probably done their focus groups with their industrial customers and all we can you know, you don't have to take your hands off the probe.

**Dave Jones:** You can just press it. Well, why can't they have the bloody what's wrong with the touch hold? Your traditional touch hold thing. Anyway, I don't know. It's probably some requirement for it.

**Dave Jones:** I'm not a fan of that. I just I don't know. Gives me the heebie-jeebies for some reason. And the range switch on it, just feels a bit spongy and not indented.

**Dave Jones:** I mean, you know, it's it's indented but not a nice solid feel on it. It's not as good as the 1272 A here, which, you know, has a nice positive click indent.

**Dave Jones:** This is like just like spongy, limp-wristed. But like I said, IP67 rated 3 m or 10 ft drop proof and we'll have to test all that in another video.

**Dave Jones:** That'll be fantastic fun. 0.025% basic DC volts accuracy. I'll link in the data sheet down below. You can go through the specs to your heart's content. But yeah, super rugged, super accurate meter, 60,000 count dual display.

**Dave Jones:** We'll no doubt power it up at the end of this thing. And 800 hours battery life. Bloody beauty. One of the huge selling points of this thing in my opinion.

**Dave Jones:** If you go for the the U1240C series, it's very similar look and feel to this, I believe. It's slightly smaller. It's a 10,000 count 0.09% class instrument. Battery life halves to 400 hours.

**Dave Jones:** But yeah, if you want a more basic, lower cost meter, take a look at the U1240C. It looks pretty jazzy. But one big massive fail, in my opinion, this is their brand new design, top of the line multimeter.

**Dave Jones:** I mean, in a couple of weeks, it's 2016. We have hoverboards and everything now. And they can't build Bluetooth into it. It's still designed to You know, this is they advertise this thing, oh, you can automate the thing with their excellent software, which works on tablets and everything else, and it communicates.

**Dave Jones:** But no, you've got it just uses the same old bloody Bluetooth module, which you don't get with it, by the way. This is a optional extra. I just happened to have one here.

**Dave Jones:** And yeah, the software and remote everything is great, but why can't they build that in? On the top of the line meter, that's a complete fail. Anyway, it's got a nice big beefy rubber holster, which we'll take off.

**Dave Jones:** It's got these little ears here, which you'll notice protect the range switch. So, if this falls boom flat on its face, you don't damage your range switch and well, assuming it's a nice even concrete floor floor or something like that, and you don't bang up your screen either.

**Dave Jones:** So, yeah, very nice attention to detail there. They've done that right. And the tilting bail on the thing, you know, it's decent. It's wide enough. It doesn't fall over.

**Dave Jones:** You know, it's all it's all doing the business. So, let's haven't taken this off before, but uh let's try and get this holster off. Can I? I want to replace my batteries.

**Dave Jones:** I think yeah, you got to get the holster off to replace your batteries. Like Luckily, it's got a bloody 800-hour battery life. There's got to be a trick to it.

**Dave Jones:** Hang on. Okay, so that wasn't easy, but I guess you'd get used to it. This is quite interesting. They've they've actually integrated the tilting bail into the meter itself instead of more traditionally into little mounting points on your holster.

**Dave Jones:** Why they've That That just looks silly. Um but I Okay, no problems. Okay, fine. Anyway, um separate battery and fuse compartments fantastic. Now, because this thing is IP67 rated, i.e.

**Dave Jones:** waterproof for being submerged for up to 1 m for like 30 minutes or something, then it's going to have O-ring seals around the battery compartment, of course, and also around the main unit itself when we take this puppy apart.

**Dave Jones:** And yes, it's made in Keysight's Malaysian factory. It's just different to China. Fine. Um yeah, so this looks and feels really solid even without the holster as you'd expect for something that's designed for a 3-m drop.

**Dave Jones:** So, let's get into it. I don't know I don't know what they're doing there. Uh I don't know. It's just It's It really's not a sexy meter out of its holster.

**Dave Jones:** It looks kind of I don't know, almost toy-like. All right, here we go. Taking off the screw screws. I thought I did. There we go. Ta-da! And no eye rings on there.

**Dave Jones:** Captive screws. Very nice. You can't lose those. Attention Oh, we've got to get Oh, no, look at this. Hey, there we go. They've done it. Look, they've got an extra rubber holster on there.

**Dave Jones:** Hey, look at that. And that's integrated with the case. Hey! That's kind of jazzy, isn't it? I like it. Any Oh, um, no, it looks like our battery compartment's up here.

**Dave Jones:** This is just our fuse compartment. So, two separate compartments. Anyway, two massive HRC fuses. What are they? 20 Yep, 20 kiloamps and 10 kiloamps for the 450 milliamps one.

**Dave Jones:** So, nice. But, you know, that's what you can expect in a nice CAT IV 600 V. And this would be genuinely It doesn't have It's not like UL tested or anything.

**Dave Jones:** It's got no independent certifications. Does it? Oh, yeah, there it is under there. CSA independently tested, not UL, not uh Intertek. But, you know, they're all, you know, six of one, half dozen of the other.

**Dave Jones:** That thing there is just a FCS FCC ID code thingo. You can Google it and get a page. All right, so this flap cover is rather interesting. You can see it molded into the slot around there.

**Dave Jones:** So, instead of your more traditional O-ring, they've gone for this. But, of course, it's got a big whopping hole in there, so you can't just rely on I mean, you know, so it's going to seal right around the edge there.

**Dave Jones:** So, it's like an O-ring seal, but uh you know, assuming it gets the right amount of pressure and everything, I'm going to you know, I assume that they've uh designed and tested all of this properly, which I'm sure they have.

**Dave Jones:** And then of course, you're going to have a mating seal around here, and certainly it does. There we go, all the way around. So, that will then push on the top part of it.

**Dave Jones:** So, they've actually got this hinges in here like this, and that goes on there, and assuming that you've designed it right, and you got all your right uh pressures, that should be a decent waterproof seal.

**Dave Jones:** So, yep, thumbs up. But of course, nothing is truly waterproof. No O-ring seal is truly waterproof unless you actually grease it up. So, yeah, I come from a marine electronics background designing underwater stuff.

**Dave Jones:** Oh, yeah, those were the days. Anyway, let's whip open the battery compartment. And yep, they've got the looks like they got the same thing. Here it is. Ta-da! Geez, that's yeah, it's wider though.

**Dave Jones:** It's yep, but it's integrated. Oh, okay. No, they're not integrated, they're just joined together. So, if I took out this one, the whole thing would just lift out. That's rather clever, I guess, how they've molded those in just one big uh piece.

**Dave Jones:** So, that's that's rather neat. I don't mind that at all. And once again, they've got the requisite uh seal around there, which will push on the uh top side of this.

**Dave Jones:** They've got things to push down on the batteries. So, all right, so we've got six screws holding this puppy in, and uh metal threaded uh inserts, of course, very nice.

**Dave Jones:** And as we saw before, captive uh screws, so they don't fall out. Very nicely designed. I'm thoroughly impressed uh so far. They really know what they're doing. So, let's take this puppy apart.

**Dave Jones:** And self-tappers, no No there, but you know, you get those in all your top-of-the-line meters pretty much, but as long as they're which is fine. There's nothing wrong with self-tappers as long as you got your separate battery and fuse compartments.

**Dave Jones:** And you you know, we should never have to open one of these. I mean, you know, so there's no user serviceable parts inside. Surprised they don't have that on there, but yeah, so there's really no reason you should open it and you probably shouldn't like you know, if you but like how many people are really going to need this thing to be factory waterproof sealed, you know,

**Dave Jones:** so I still recommend you get this puppy crack it open to have a good squeeze inside. Although, I do this so that you don't have to. And yep, there's our there's our O-ring seal.

**Dave Jones:** Op. Here we go. We're in like Flynn. Ta-da! Look at that. Oh. Hang on. Look at the shield and they've put on the back of the battery compartment. They're in big You know, it's almost I'm not going to say after thought, but jeez, I don't know.

**Dave Jones:** Don't know if that's a bit how you doing or not, but anyway, let's disconnect. They've got a connector there for our battery, but ta-da! There's our uh O-ring seal all the way around there.

**Dave Jones:** Not greased up, so meh, you know, but yeah. It'll still work. First thing I actually spotted is just glancing around is why this inductor here has been all gunked.

**Dave Jones:** It's got It's got Silastic all around it. Like, what the? There it is. Try and figure that out. Why have they done that to a poor innocent little inductor?

**Dave Jones:** Don't get it. All right, so let's take a look at the input section here and it looks there's some unusual stuff happening here, but anyway, before I get into that, here's our ground terminal here.

**Dave Jones:** We can see we've got a little thermistor in there at a PTC, you know, positive temperature coefficient thermistor. Dead giveaway is the RT down there. We've got four little surface mount diodes.

**Dave Jones:** That's going to be our diode bridge protection there. And here's our positive input terminal going through another PTC thermistor going through a big ass nice-looking heat shrunk uh big power um series protection resistor.

**Dave Jones:** No worries there. Another uh heat shrunk thermistor here. Why they've heat shrunk the two of those, I don't know, but anyway, it looks really neat and jazzy. And another big series protection resistor here.

**Dave Jones:** So, very nice, but um conspicuously lacking in any move overload protection. So, but hey, this thing's been independently tested, CAT IV rating. It's got all the requisite uh stuff you'd want.

**Dave Jones:** We've got our high voltage uh isolation here where our slots. We've got high voltage isolation slot going through here. We've got big uh blast shield actually and high voltage uh shield actually molded into the back of the case, which goes right through the board or right around that positive input terminal.

**Dave Jones:** So, that's beautifully beautifully designed. No worries there at all, but yeah, just no moves. Rather surprising. Now, the first unusual little item is that uh remote terminal on there.

**Dave Jones:** And you'll notice that there's two contacts. There's an insulator separating the two terminals. So, they've got those bent out coming over all like really custom uh stuff. So, but it looks Hey, it looks superbly designed, but one of the most interesting things, what is going on here?

**Dave Jones:** Here's our two current input terminals, but look, I've never seen a fine wire coming over there, soldered up. It looks brilliant, right? Looks super duper high quality. Wow, all the bells and whistles, but we've got ourselves Hey, that's not even soldered.

**Dave Jones:** That's just a That's just a retention clip. What that is clearly doing of course that's not our main current. All our main current is the, you know, the big beefy uh tag coming out of here soldered directly to down.

**Dave Jones:** Oh, look at all of those Look at those massive vias down there. Oh, yeah. Good stuff, but um yeah, we've got a little clip-on spring terminal here with a little spring down here.

**Dave Jones:** That's obviously our current sense jack. And yes, these are actually a split. If we can uh see down there, there we go. You can actually see the split down in there.

**Dave Jones:** So, that's how they're uh sensing that, but I've never seen an implementation like that. It's rather unusual. Now, silly me, did I say before that this was the uh battery terminal?

**Dave Jones:** Look like it at first glance. I I was going to actually comment on that, but it's not. It's actually the uh piezo transducer up here. So, I really don't like the way that, you know, why have wiring going over the piezo transducer?

**Dave Jones:** It's almost like an afterthought. And I'll show you why because the battery terminals are really very nice. Look at these integrated studs in here. Absolutely brilliant, right? Real super duper rugged stuff.

**Dave Jones:** Then it comes down onto the main board here. So, look, spring terminal meeting up right in there with that integrated stud. That's so you know, that's awesome. And then they go and ruin that with some dicky how you doing wire going under the metal shield here over to your piezo transducer.

**Dave Jones:** I don't know. It's like they just like lost all enthusiasm at that point. Oh, who cares about the piezo transducer? We'll just wire that in. And the rain switch, well, we can't really uh see anything.

**Dave Jones:** I've got no real comment on that until we uh take the whole thing apart. But uh yeah, it looks like, you know, decent uh spacing around here, everything else.

**Dave Jones:** So, shouldn't be an issue. We've got our big high-voltage uh cap in there. And it looks like we have our precision uh thin-film uh resistor divider network. Is it or is it a high Is it Is it a high-voltage input resistor?

**Dave Jones:** I can't see the extra pins on there. I think it's just a Is it just a two-pin high-voltage ceramic resistor? Hmm. And yes, obviously all this stuff up here is to do with the uh V sense stuff.

**Dave Jones:** So, this does have uh voltage detection. Um that's what that That circuitry is there and the little uh sensing element. Plus, they got the little ground coming over there.

**Dave Jones:** And uh however they're implementing that. So, it's obviously when they split the ground like that and have some sort of like little antennary-looking things going on here that you know they're doing some sort of electric field uh detection there.

**Dave Jones:** So, yeah. And we've got an unpopulated uh test uh connector. Is it some sort of uh JTAG or some sort of, you know, uh programming header, whatever. Anyway, uh we'll have a closer look up at some of the chips in a minute.

**Dave Jones:** And absolutely no surprises for finding a uh commercial-off-the-shelf uh multimeter front-end chipset. This is the uh High Contact uh HY 3131. And I'm uh a bit familiar with this one.

**Dave Jones:** It's uh not a bad little uh front-end chipset. But in this case, it's designed to be 50,000 maximum count. Um yet this meter is 60,000 maximum count. So, are they uh pushing it somehow?

**Dave Jones:** I'm not that familiar with the actual implementation of it that if that's actually uh possible to do. So, well, I guess they must be. Or do they have a special variant of the uh part or something?

**Dave Jones:** Hmm. Anyway, it's got all the requisite uh input uh switching. And it's got the voltage reference and everything else to do with you know an analog front end and all the stuff surrounded and it's all just you know jelly bean type you know muxes and and switches and things like that.

**Dave Jones:** So you know not much doing there at all. We'll have another look at this puppy over here is a bit special but of course we're going to have a separate processor up here.

**Dave Jones:** So it's going to be on the bottom side of the board cuz there's the crystal low up there so there's got to be another processor on the backside because this is not a processor.

**Dave Jones:** It's just a front end analog chipset and and the output data is serial but I'll link in the data sheet for this puppy. It's really quite special this Hi-can tech data sheet in that it really does show you in-depth all of the switching topology that makes a modern multimeter work.

**Dave Jones:** So it's well worth taking a look at this data sheet. It really breaks it down quite well. Well, looky what we have here our analog devices true RMS converter not the typical 637.

**Dave Jones:** We've got the AD 8436 beauty but look at this. You'll notice a little uh look a little bridge in there and if I flip it around you'll notice there's also some bridges in there.

**Dave Jones:** So that's what happens when you put traces in there that go between the pins and the pin spacing is so small that you can't get your solder mask in between there.

**Dave Jones:** So yeah, the solder's just going to pull there because that's what keeps it from doing that is the solder mask. So no solder mask between pins they're doing that shorts but hey, they're supposed to be there.

**Dave Jones:** So that's okay. Well, that's interesting. We've got a Maxim Max 4611. That's actually a voltage detection chip. So that's Um, likely doing the battery uh low low battery voltage.

**Dave Jones:** So, got a little bit of effort there. Uh, we're probably just going to have some op amps and some muxes there. That one there, the CM053, is that like I'm going to assume that's a uh 4053?

**Dave Jones:** Probably. They've got another one over here. It's a C What is it? A CM052. So, that could be a 4052 mux, I believe. So, yeah, this is going to have some op amps and some muxes and switches and all that sort of jazz in there.

**Dave Jones:** We've got another 4611 for voltage detection. There's two of them. There's two of them. Wow, somebody like those on the bomb. Oh, yeah, old school 7400 H HC390s, very nice.

**Dave Jones:** Look at this HC14 uh Schmitt inverter, no worries. That looks like an E-squared prom. It's upside down. All the electrons are going to fall out. That'll probably be for the uh sample memory.

**Dave Jones:** And then there's a HC04. Is that an Atmel something or other? I'll tell you what I'm not too happy with. There are no uh shake-proof washers or thread locker on any of these uh input terminal screws, by the looks of it.

**Dave Jones:** Hmm. Tell you what, I can see why they've done these though. It's just a very uh convenient uh production step. I mean, you just don't have to solder anything on.

**Dave Jones:** Uh, but you know, they could have had just like this, they could have had just a second terminal coming over, but I yeah, I don't know. Hmm. Anyway, it's neat.

**Dave Jones:** And there's under the rain switch. There you go, we've got some dual wipe contacts on there, but you'll notice that there really is a big lack of uh switching under there.

**Dave Jones:** So, it's most likely there's another uh switching contact uh system on the bottom side of the board. So, So, here we go. I might be able to get all of this out.

**Dave Jones:** Oh, no. No, I forgot the bloody contacts in there on this thing. They're just, uh, push in. How annoying. So, you'll notice that they're a similar, uh, like little, uh, uh, clip mechanism like the other one.

**Dave Jones:** So, that's, you know, they've gone to a lot of effort there. I I Okay, I've got to I can't help but be impressed, I guess. I think somebody had fun.

**Dave Jones:** Holy torpedo. Somebody had fun. Okay, now we should be able to lift this puppy out. I've got all the There we go. Yeah. Yep. Come on, you can do it.

**Dave Jones:** Ta-da! Yes. There's our extra range switch contacts on the bottom there. And, of course, we've got, uh, waterproofing on our buttons. We'll take a closer look at that, but, yep, there we go.

**Dave Jones:** Extra switching on the bottom. Not much else, just got some more, uh, diode, uh, protection happening down there. Another, uh, oh, these must be for the, uh, yeah, they're for the, uh, sense, uh, lines here.

**Dave Jones:** So, yep. Oh, there we go. Gas discharge tubes. Look at that. GDTs. There we go. Spark gap protection. So, there you go. Beauty. We've got, uh, spark gap protection.

**Dave Jones:** No worries. So, you don't need MOVs if you got, uh, spark gap protection there. And, I like how they've done the cutouts on the board. There, you'll notice there's two, uh, two slots cut out there, so they don't So, they're actually truly getting because, you know, if you get a high voltage arc across there, it could actually creep across the board and actually not spark across a spark gap.

**Dave Jones:** So, that's really nice design. They, You know, they knew what they were doing there. So, I have no doubt that this puppy would meet its rated, you know, 600 V CAT IV rating.

**Dave Jones:** All the space and everything seems to be there. It's like very nice input protection. Very well done. Cannot fault that at all, really. Perfect. And as I said, there's the two protection resistors for our sense lines there, those little spring terminals, of course, that we had popping up there.

**Dave Jones:** So, yeah, no worries. They're doing that all hunky-dory, even though they don't actually need transient protection on that, but just they've got that going into. So, that's what this cluster circuitry around here must be.

**Dave Jones:** That must be the input sense circuitry. So, that's a hell of a lot of effort to go to. There's a bit of leftover flux residue on there, but I'm going to going to I'm not going to be too harsh on that.

**Dave Jones:** There's a rather curious device here that is actually in the negative line going to the range switch for the milliamp current range. So, its reference designator is B, which is doesn't seem to make a lot of sense.

**Dave Jones:** But, yeah, what is it? Doesn't look like a polyfuse or anything like that. So, yeah, not entirely sure. Some sort of last-ditch protection for the range switch there, perhaps.

**Dave Jones:** And there is the range switch right there. It's a pretty classic implementation. Why it doesn't feel better, they just haven't designed the angles on the plastics and the you know, the plastic springs in there that well.

**Dave Jones:** So, it just feels a bit spongy, but you know, that's a pretty typical implementation there. But, really, there's nothing too much wrong with the contacts there or the They look like a reasonable quality uh plating on the uh rating PCB uh range contacts there.

**Dave Jones:** As you'd expect they'd be they are gold plated or are they a nickel? It looks goldish plated, but they're more yeah. And I'll just show you the spacing that they've used here and why, you know, this thing would ultimately get its uh you know, cat would be part of getting its cat four rating.

**Dave Jones:** Okay, here's our input um terminal here, it goes through our PTC. Then we've got the series protection resistor here. Okay, big ass huge power protection resistor. And then that from that terminal there, there's our gas discharge tube.

**Dave Jones:** So, that's our overvoltage uh spark gap protection there. And that shunts that down to ground immediately right here. And then uh this on top here, this goes off through another PTC thermistor, then into another uh protection resistor here.

**Dave Jones:** And then so, this protection resistor from here to here. And then the in other side of that protection resistor is also spark gap protected down to the same ground there.

**Dave Jones:** So, they got two levels of spark gap protection with big series power resistors and PTCs in series which increase their resistance in overload conditions. So, you know, two-stage protection there.

**Dave Jones:** And if that's not enough, then the output, the final voltage more input to our multimeter, it goes into the range switch here. And look at the clearance they've got between these.

**Dave Jones:** And I've done a uh video on uh sparking across range switches like that. And I you know, just small gaps like that I was able to spark across it like 5,000 V.

**Dave Jones:** So, this one, you know, depends on the contamination on the board and all that you know, sort of jazz how it uh sparks over. But you know, there's big gap in there.

**Dave Jones:** And they've done likewise on the top here. You can see that trace coming in there. And once again, big clearance to the next contact in there. So, yeah, very nice.

**Dave Jones:** That's why the input protection on this sucker is going to work and work well. And I couldn't see this properly before, but yep, multiple pins on here. This ceramic puppy in here, that's our classic ceramic thin film resistor network.

**Dave Jones:** So, that's where they get the accuracy from on the range switching on the input. And you can see that on the chipset here. You can see that those resistors are pretty critical.

**Dave Jones:** They haven't implemented those using standard surface mount parts. They've gone to the trouble to design and spec in a proper ceramic resistor network where all of the resistors are all matched temp co and everything else.

**Dave Jones:** So, yeah, I have no problems that this thing's going to meet its spec. And there's our buttons there. There we go. We've got the once again, that's acting as a waterproof seal.

**Dave Jones:** They've got a big back in plate on there like that, which then hooks it which levers under there like that and goes down. So, it puts the board's going to put pressure on that and there's going to be a very nice seal there.

**Dave Jones:** So, they've done that really well. Thumbs up. Now, what's our processor going to be? It's under the LCD here. Is it going to be like this thing's remember 800 hours battery life.

**Dave Jones:** So, it's going to have a pretty low power processor. Now, the U1272A multimeter here, if you've seen that teardown, it's somewhere on my channel. Maybe I'll link it in.

**Dave Jones:** It uses the NEC 78K series, you know, fairly old school. So, I don't know. Will this one have the same or will it have like an MSP430 or some other low power micro?

**Dave Jones:** Let's take this thing off. It's going to be a zebra strip under there. Just a single screw. And it looks like we've got exactly the same thing. Let's go in for a closer look.

**Dave Jones:** Yep, it's actually exactly the same. The 78F0485. Exactly the same as what's used in the U1272A. So, they're clearly leveraging all their software there. And looks like we've got some 74 series 595s to do some data demultiplexing.

**Dave Jones:** What, they didn't have enough pins? And the V sensor electric field detection there, there's a little puppy in there, little TI part. I don't know. Anyone want to go look that one up?

**Dave Jones:** There's our little custom LCD holder. Very nice little spring contacts go down to pads on the board for the backlight there. Very nice. And you'll notice that the zebra strips go all the way along there from end to end, but the contacts only go from there to there.

**Dave Jones:** Well, that's not uncommon because well, you're paying for these things anyway. You're not saving a huge amount by making them a little bit shorty, you know, they cost peanuts when you order these things in in a 50,000 quantity or something like that.

**Dave Jones:** So, yeah, you just go the whole length, you make it easy for yourself. All right, I've got it back together. I'm putting the batteries in and I just love how this rubber seal just fits in there like a glove.

**Dave Jones:** Beautiful. And that's not an OJ glove, that's a real fits like a glove. Love it. Will it work? Oh, you bloody ripper. And check out those main display digits.

**Dave Jones:** They're enormous. They're about 19 mm. Beauty. This is going to half turn into a review. Anyway, the probes you are listed. No worries. Not a fan of the I'm never a fan of these CAT IV input thingies.

**Dave Jones:** Hang on. God, how do I get that off? There we go. Got it off and they're not hugely sharp at all, but yeah, they've got these unusual little things on here which retain the CAT IV clips.

**Dave Jones:** If you take these off, they're only supposedly CAT II rated. It's all bull, you know. But yeah, because you know, your fingers can't slide down there and and touch the thing easily.

**Dave Jones:** But, whatever. Um yeah, nice quality probes. They're just a bit unusual on the ends. They're a bit too long, maybe almost. Hmm. Everyone wants to know about the continuity tester.

**Dave Jones:** No worries. I It's almost Oh, I missed the occasional one, but yep, it's latched and fast. Nice. Although, it doesn't have the backlight feature that the um 1272 has.

**Dave Jones:** So, anyway, it it is faster than the 1272. 1272 it'll occasionally miss some. So, yeah, quicker, but Yeah, there are significant differences. Like, it doesn't have the uh smart ohm feature that the 1272 has.

**Dave Jones:** So, why they've dispensed with that, I don't know. And it looks like they don't have the auto hold. They've got the just the hold. Let me try it. No, it certainly doesn't have it.

**Dave Jones:** I mean, take a look. We've got auto hold here. You hold hold this down, and we can actually go into auto hold mode as well as trigger hold mode, which I've shown on a previous video.

**Dave Jones:** And if you've got auto hold mode on, of course, you can just uh probe something. Here we go. Bingo. Minus 6.9 and it holds it. It's like the Fluke touch hold thing.

**Dave Jones:** This thing does not have the auto hold. Why? It's It's got trig hold, which is which is really handy. I've done a video I might have to link in where um Oh, hang on.

**Dave Jones:** No. If I can get rid of that. There we go. Trig hold. Okay, so it looks like it's going to do the same thing with trig hold, but um it's which is very handy for uh when you probe something, it'll automatically add it to sample memory, but um it does not have the same, you know, auto hold capability.

**Dave Jones:** It's just Why? Did they determine, "Oh, we're going to do away with that and going to have this stupid remote uh uh probe interface thing. It's like uh it's dumb.

**Dave Jones:** And also, they don't have the uh low impedance voltage mode to get rid of ghost voltages. And this seems like an insane uh thing because this is you know, it's super rugged drop proof design for the field, industrial as you can get, and it does not have a low impedance mode like the 1272A does.

**Dave Jones:** I it's nuts. And it doesn't even have It doesn't look like it has a um setup menu like the U1272A does either. Look, you can go in and you can set up various things.

**Dave Jones:** You can't do that. There is no setup um thing at you know, we can get into different uh displays and stuff like that. DBM, DB volts. Okay, fantastic. But um yeah, that like it uses exactly the same processor.

**Dave Jones:** It's obviously leveraging same software. It's you know, very similar sort of you know, look and feel in terms of the uh user interface, but they're very different meters. On the capacitance range, they do both have a resolution of one uh puff, so beauty.

**Dave Jones:** But actually, come to think of it uh it makes sense that this thing does not have the auto hold mode because the uh whole tech uh chipset that they're using in this thing, front end chipset, um you know, it does not allow that capability.

**Dave Jones:** You're basically limited by your front end chipset. But if you actually have a look at the U1272A teardown I've done, then you'll see that it doesn't have any uh traditional multimeter uh front end.

**Dave Jones:** It does it all basically uh discrete in terms of you know, just basically uh muxes and switches and things like that. And it's got like an off-the-shelf um analog-to-digital uh converter with a uh programmable gain amp front end.

**Dave Jones:** So, they can implement that auto hold stuff in software. Whereas, it looks like they can't do that uh for some reason due to the multimeter chips. Although, you know, you can read the data out and like you could still do it in software, but that's probably a limitation of the of where the lack of auto hold mode on this thing comes from.

**Dave Jones:** And I'm not sure why we've actually got a pulse output here like 600 hertz by default 50% duty cycle. I don't don't know why you need that on an industrial meter like this.

**Dave Jones:** And of course it's going to be bang on. You wouldn't expect anything less. Well, it's hard to quibble about that one. One lousy least significant digit out on the resistance range.

**Dave Jones:** I think that's a pass. Oh, by the way, one thing I have haven't actually showed you yet. I have to do a teardown and a play around with an review of this puppy, too.

**Dave Jones:** There it's been out for a while, but it's the U1461A and it's a similar look and feel just like this one and it's also IP67 rated as well, but this one's actually an installation resistance tester up to a from 50 volts up to 1,000 volts combined with a multimeter as well.

**Dave Jones:** So, once again, it's very similar look and feel, but it's got the auto hold functionality and the setup mode that you find in the U1272A. So, it it's different yet again.

**Dave Jones:** It's weird. And yes, it does have an OLED display. They don't actually have in this upper model, they don't actually have an LCD display version, but the OLED display is a lot longer battery life than it used to be, but still yeah, I would have preferred an LCD version.

**Dave Jones:** Anyway, just want to show you the then bloody backlight thing. It almost looks like it's gone off completely, but uh you know, look I it's just No, that's Yeah, no.

**Dave Jones:** Well, and tripod fail. Thumbs down. I need a new tripod for Christmas. It's the 21st. I don't think Santa's going to be able to deliver one in time. Ah.

**Dave Jones:** So, there you go. I hope you liked a look inside this new uh new 1282A or 1280 series multimeter from Keysight. And it's a real beast of a unit in terms of uh you know ruggedness and waterproof.

**Dave Jones:** It's you know probably equivalent to the Fluke 28 series in that respect and it's pretty hard to fault the design of this thing. Really well built and well designed, well constructed.

**Dave Jones:** So, big thumbs up to that. So, yeah I have to do a separate video actually uh reviewing this thing and maybe the other one the uh 1461A in comparison with some other meters and have some fun there.

**Dave Jones:** But yeah, that requires a whole separate video. This one's been long enough. And yeah, um as I said about $500 street price. That's not a cheap multimeter. But by the way, um you can actually get they've got a buy two get one free get the third free promotion at the moment.

**Dave Jones:** Goes until uh February 29th. So, it it involves all their whole range of stuff. So, it's probably worth looking into if you're looking to uh buy at least a few of these um well, a few meters or something like that.

**Dave Jones:** So, it could bring the price down significantly. Anyway, it's um yeah, it's built up to a price. That's for sure. Very nice. Anyway, I hope you enjoyed it. Um there'll be some high-res teardown photos on eevblog.com linked in down below.

**Dave Jones:** And if you liked it as always, please give it a big thumbs up. Discuss it in the comments or on the forum. Catch you next time.
