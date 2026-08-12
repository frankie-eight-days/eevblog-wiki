---
video_id: tCgtTPwlDSo
title: EEVblog #687 - EFTPOS PIN Pad Terminal Teardown
url: https://www.youtube.com/watch?v=tCgtTPwlDSo
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 34, "3": 45, "4": 59, "5": 71, "6": 84, "7": 109, "8": 120, "9": 134, "10": 146, "11": 164, "12": 171, "13": 182, "14": 190, "15": 203, "16": 218, "17": 233, "18": 242, "19": 255, "20": 263, "21": 275, "22": 286, "23": 300, "24": 313, "25": 330, "26": 344, "27": 357, "28": 375, "29": 393, "30": 401, "31": 420, "32": 432, "33": 446, "34": 460, "35": 472, "36": 481, "37": 491, "38": 503, "39": 524, "40": 539, "41": 552, "42": 564, "43": 578, "44": 586, "45": 598, "46": 622, "47": 634, "48": 651, "49": 668, "50": 678, "51": 699, "52": 716, "53": 726, "54": 736, "55": 751, "56": 764, "57": 774, "58": 785, "59": 792, "60": 807, "61": 822, "62": 831, "63": 858, "64": 872, "65": 881, "66": 891, "67": 905, "68": 913, "69": 926, "70": 935, "71": 957, "72": 968, "73": 982, "74": 995, "75": 1004, "76": 1020, "77": 1030, "78": 1040, "79": 1066, "80": 1080, "81": 1093, "82": 1114, "83": 1122, "84": 1134, "85": 1144, "86": 1156, "87": 1176, "88": 1190, "89": 1199, "90": 1210, "91": 1227, "92": 1236, "93": 1246, "94": 1263, "95": 1277, "96": 1296, "97": 1309, "98": 1320, "99": 1333, "100": 1348, "101": 1370, "102": 1394, "103": 1401, "104": 1420, "105": 1442, "106": 1452, "107": 1461, "108": 1476, "109": 1487, "110": 1497, "111": 1507, "112": 1526, "113": 1539, "114": 1548, "115": 1558}
---

**Dave Jones:** Hi, welcome to Tearown Tuesday. Today we're going to take a look at this Sageum Montineel uh FPOST pin pad terminal. You might call them uh something else in your country, but we call them basically FPOST terminals here or uh pin pads because I used to work at the company who actually supplied this key corp.

**Dave Jones:** I worked there back in 94. Although I wasn't in the pin pad group, I designed the TFT LCD monitors for these type of banking systems back then. Anyway, this is not a Keycor branded model.

**Dave Jones:** It's uh produced by uh Sageium. I'll link in the data sheet for it down below, but it's one of these typical F-POS terminals. Not a particularly recent one, but recent enough to have a smart card interface on here.

**Dave Jones:** And it's also a GSM model. We'll find that out. In fact, tada. There we go. It's got some uh SIM three SIM card slots down there. I'm not sure why there are actually three there and there's an SD card slot in there.

**Dave Jones:** Anyway, so you can use this as a remote terminal and uh it connects and does your electronic uh credit card transaction at your point of sale. And thanks to Luke Stone for sending this one into the mailbag.

**Dave Jones:** He scored it for two bucks at a local garage sale. Fantastic. So, let's tear down this thing and see what's inside. Now, the interesting thing about these uh pinpad foss terminals is basically the security inside of them.

**Dave Jones:** And I'm not talking software security. I'm talking hardware uh anti-tamper security because it's very important for these things not to be hackable. So, you know, somebody can't uh just buy one commercially on the market or access one like this or steal one or whatever and then hack it and put their own uh circuitry inside of their own software or whatever to then steal people's uh credit card numbers

**Dave Jones:** and pin numbers and things like that. So, expect lots of anti-tamper technology inside this thing. And there's industry standards uh for this. This particular one meets the uh PCI PED standard.

**Dave Jones:** And no, PCI doesn't stand for your regular computer PCI slot. It stands for the payment card industry and they're the uh regulatory body that handle uh the security standards both software and hardware and also management uh for these things.

**Dave Jones:** So it's PCI PED standards. So payment card industry PED stands for PIN entry device which is what the industry term is for one of these but we'll just call it FPOS terminal because that's what they're called here in Australia.

**Dave Jones:** Um FPOS if you don't know is electronic funds transfer at point of sale. There you go. Um and there are various standards for this. Uh we're going this is um meets the PED standard for the pin entry device, but there's uh separate standards for the uh the DSS standard for the data security standard.

**Dave Jones:** It stands for like the protocol the interfacing and and the key generation and all that sort of stuff. And I think you have to like buy the standards or something like that.

**Dave Jones:** I don't think they're readily downloadable, but if they are, please uh link them in and uh or leave a comment and I'll link them in down below. Anyway, I'm going to link in the data sheet for this thing.

**Dave Jones:** I'm not sure the exact age. We'll uh find out. But yeah, as I said, it's got a smart card interface. It's got a card reader down there. You swipe your card.

**Dave Jones:** You can hardly see that, but there's a little there's the reading head down in there. We'll see that when we open it up. Graphical LCD screen. Um, and it comes with this uh cable which has both an Ethernet uh interface here.

**Dave Jones:** So it does um IP like you can connect to a regular internet connection and it can do your transaction that way which is faster than your regular modem. This will also have a um uh V uh 32 modem in it as well.

**Dave Jones:** Um and it's also got RS23 uh2 interface. Plus it's also got that wireless uh capability with the uh SIM card as well. So maybe you can uh attach like an optional battery pack on here dealer fitted or something like that.

**Dave Jones:** maybe turn it into a portable device. I don't know. Or maybe it's just a complete leadered device. Anyway, it's got three different methods to um uh actually do the uh transaction.

**Dave Jones:** SIM wireless uh Ethernet and dialup as well. Got a couple of USB ports on here, device and host. That I believe is used for the upgrade of the firmware in this thing.

**Dave Jones:** You can actually plug a cable in and plug in a USB key and you can do your uh firmware upgrades and field upgrades that way. So, should be really interesting.

**Dave Jones:** But, and it's got a printer as well. It's just got a little uh cheap ass thermal simple thermal printer in the thing and a security uh looks like a security locking uh tab or something like that.

**Dave Jones:** So, we really want to find out what the anti-tamper mechanisms in this thing. That's going to be the fascinating bit that I want to see. I don't particularly care what processor it uses.

**Dave Jones:** Although these things often use a uh a secure uh processor, a specific uh hardened security processor that has self-destruct mechanisms and things like that. Uh anti-tamper devices built into the processor, not a regular one.

**Dave Jones:** It says it does use a 32-bit risk ARM 9 micro at 200 MIPS in there to do that, but also says it has a co-processor. So, I expect the co-processor to be a security uh hardened processor.

**Dave Jones:** So, this model is the EFT 930S sage monotel. We'll find out the date when we open it. There will no doubt be uh some chips in there, but yeah, like it's got a date of, you know, supplied by key corp in 2010, but when it was uh designed and serviced, you know, it's at least four or 5 year old.

**Dave Jones:** So, um which isn't too bad. So, there we go. That's like a half turn system. You have to uh do that and pull at the same time. Ah, there we go.

**Dave Jones:** That's just a uh cable interface. So, that's got our RS separate RS232 uh Ethernet and it had the USB host. I think that one's for the firmware. So, not entirely sure what the these are the devices over here, but anyway.

**Dave Jones:** So, we can probably do firmware updates through there. RS232 host and ah power. And yeah, I could picture there maybe being a battery uh pack optional extra for that if you just wanted to use the uh SIM module.

**Dave Jones:** No problems. And I don't really know about the uh GPS uh modem inside this thing and the SIM cards here, whether or not, you know, you can just whack any regular SIM card in there and how that's actually uh handled on the uh client side and all that, the payment gateway and all that uh sort of jazz.

**Dave Jones:** I guess you would uh have to be in the industry to know those kind of things. But uh anyway, let's see how we can open it. So, six of those.

**Dave Jones:** But as I said, as soon as we take this case off, I expect there to be at an absolute bare minimum uh anti-tamper uh switch in there built into the case perhaps that as soon as we open the case, it's going to destroy the uh contents of the um of the uh keys and things like that.

**Dave Jones:** But there's probably multiple layers of uh tamper protection in here, not just that. So, let's open it. No, it turns out they're torque screws. I should be able to find the right size one in here.

**Dave Jones:** Should keep them organized. All right, I've taken out the six screws in. Hey, there we go. We broke our little uh security seal there. Not surprising. And what have we got?

**Dave Jones:** Yep, there we go. There's our first Yep. There's our first anti-tamper. There we go. Tactile switch down in there. That's our first anti-tamper mechanism. So, yeah. There. There it is.

**Dave Jones:** There's the little uh button which pushes down on that tab. So, bingo. All the uh we probably screwed the pooch already. If you wanted to get the security uh keys out of this or whatever, you've probably already lost them.

**Dave Jones:** And you add a at a minimum you'd probably have to go back to the uh official dealer and get it reprogrammed or recommissioned or whatever. Um, however that works.

**Dave Jones:** And we've got ourselves a 3v lithium battery there. And no doubt a lot of this stuff is going to be stored in SRAMM. Uh it won't be stored in flash.

**Dave Jones:** So you'd expect to find like the keys and things in SRAM so that they can easily be uh destroyed at a moment's notice when you you know uh and violate any one of the uh tamper mechanisms inside this thing.

**Dave Jones:** Now curiously um a massive 4700 mic 10V surface mount cap. Look at that beast there. So they really want to retain that um uh data. Well, I I reckon that's maybe that's uh for like I don't know some internal real-time clock or something.

**Dave Jones:** And maybe that battery only powers the uh keys and uh other uh encryption uh type data perhaps. And this uh cap reservoir cap just uh keeps maybe the time and date going for uh a long time when it when the power is disconnected perhaps.

**Dave Jones:** I'm not entirely sure. And we have ourselves a pulse transformer there for the Ethernet interface. And we've got our recording head over here, our RS232, our USB uh host over there.

**Dave Jones:** Something that's not populated over here. So, I don't know whether or not that's a factory test or some sort of optional thing. Maybe it's part of the No. Yeah, it's something else.

**Dave Jones:** Um, so could be a optional model fit. Couple of parts missing all around here. Not entirely sure. Another big surface mount cap missing here. So, not entirely sure what's uh what's missing around these parts here.

**Dave Jones:** And I thought there wasn't any screws holding that in place. So, I just pulled on it and boop, off it came. Yeah, it's got a huge board to board inconnect here.

**Dave Jones:** This plastic got a plastic shield there. Not sure. Like a spacer. I'm not sure why they bother putting a spacer in there. Is there some sort of anti-tamper mechanism in that?

**Dave Jones:** Maybe not. Anyway, we've got a large amount of uh shielding around here. So, oh yeah, there we go. Now, given that uh shielding on the back there and a large amount of via stitching, that indicates uh well a uh shielding and all the ground plane flood fill on the top as well and all the via stitching, low impedance stuff that indicates high frequency stuff is at play here.

**Dave Jones:** So, I'm thinking this well has got to be uh really there's no option. has got to be the optional uh by the looks of it, not fitted to this, the uh GPS uh module.

**Dave Jones:** So, these SIMs um are of no use to this uh presumably because there's no uh wireless GPS uh functionality not fitted. Now, whether or not um there's it looks like there's some circuitry on there, whether or not there's maybe another board and there's got to be like an antenna somewhere cuz I don't see an antenna in this uh case at all.

**Dave Jones:** So, that's all optional unfortunately. By the way, we have a date code down in there, 36 week 07. So whether or not it's old stock or whether or not it actually uh came from the uh it was manufactured around, you know, late ' 07 um 08, something like that, not sure.

**Dave Jones:** Now, I just thought for a minute, maybe this was the uh modem stuff and this hadn't been uh uh populated in this one, but like there's no isolation there or uh anything like that.

**Dave Jones:** that you'd expect, you know, isolation relay, isolation slots, dedicated isolated section for a uh V32 uh modem that hooks up to the phone line. So, yeah, that doesn't seem to be uh in there or at least not on the top of anything inside here that we can see so far.

**Dave Jones:** And we have a Viccom DM 9161 chipset there with its own dedicated oscillator. Of course, that's all for the Ethernet, the physical uh aspect of the Ethernet interface. And that one there is just a Joe Blogs RS232 uh interface driver.

**Dave Jones:** Now, why they've got a second huge pin count boardtoboard interconnect connector there, I have no idea. It looks like a finer pin pitch than we've got here. So, I don't know.

**Dave Jones:** It's not something you'd ordinarily use for testing. So, maybe it was part of the uh development and uh debug, something like that. And there's nothing fancy happening in most of this.

**Dave Jones:** That's clearly a power switch mode power supply there. Dead giveaway is that uh yeah, it's surrounded by an optional shield which they haven't decided to fit. And when you see big power inductors like that and a big tanelum cap and a little chip next to it controlling it.

**Dave Jones:** Yeah. And a couple of um high value ceramic caps like that in a large package. you know that like to get very low ESR on the output that a switch mode uh controller requires.

**Dave Jones:** It's a dead giveaway. And we got ourselves a beeper up there by the looks of it. And well, not much else happening. Just some miscellaneous stuff down here for the uh USB interfaces over here.

**Dave Jones:** Now, the thing I'm very surprised at is that I can still only see one anti-tamper mechanism, and that was the little tactile switch there, which we saw when we opened the case.

**Dave Jones:** I expected the uh processing is that I'm not sure what that is. We'll get in and have a look. Anyway, looks like we've got some RAM and some flash there.

**Dave Jones:** Um that this is all, you know, I expected this to be either physically potted or protected with some sort of extra anti tamper uh mechanism in some respect or at least make it physically difficult to access by just uh potting the stuff anyway.

**Dave Jones:** But no, no, they've just put in a a halfass shield over that. And uh oh, I can read the part numbers straight off there. H. And clearly there's our ARM A9 processor, but that's not the brand.

**Dave Jones:** That's the model. Uh Mon EFT 3X. So, you know, they're just using an offtheshelf ARM processor as they said. Um what was it? A Risk ARM 9 at 200 uh MIPS.

**Dave Jones:** So, yeah, they're just rebadging that when you buy enough of them. The rebadged date code again, 34th week 07. So, there you go. um you know it's unlikely that two chips are going to be from uh 07 especially a processor like this they generally don't leave those sitting around in stock for all that long on products like this so I reckon yeah it's you know manufactured in late ' 07 or

**Dave Jones:** '08 but keyop have whacked that uh 2010 sticker on it was it although actually come to think of it no it's not that surprising that this is uh not secured in any way cuz this is just the applications processor we haven't goten to the secure processor yet.

**Dave Jones:** So that's probably on the other side of the board making it even more difficult to you know uh hack and get into you because you got to take out the second board.

**Dave Jones:** So that co-processor has got to be on the back of this board somewhere and that could have extra anti-tamper stuff. And there's our magnetic uh recording head down in there.

**Dave Jones:** It's just like your regular uh tape based uh you know cassette tape for you youngsters out there. like a regular head maybe uh possibly you know specifically designed for uh credit card scanning and things like that.

**Dave Jones:** Nothing fancy thing I found a bit surprising is that is that a little bit compliant? Yeah, it could be. Usually they build some uh physical compliance into this thing.

**Dave Jones:** Hence the flex coming out. And uh usually you know they want to uh get some you know bit of compliance in the pressure that this head puts across the credit card that you actually swipe into this thing.

**Dave Jones:** So yeah I think that's what this metal plate here can be doing. Just giving it a little bit of little bit of pressure and some give against the card.

**Dave Jones:** And I was about to say that these metal look there's metal pins there and there. I thought, "Aha, maybe that's some extra anti-tamper or something. Maybe some conductive uh thing, but I can't find any matching uh thing in the top case here." So, I thought maybe that was an extra anti-tamper mechanism, but obviously not.

**Dave Jones:** So, I don't know why they've put metal pins in there, maybe to hold in the uh uh card slot here for the smart card, but yeah, I don't know.

**Dave Jones:** And there's the head for the thermal printer there. And yeah, they do have one individual pixel. So, it's all the way across. I don't know how many uh pixels I'd have across there, but there's one individual thermal element which then just burns the uh heats up and burns a dot in the thermal paper as it passes through.

**Dave Jones:** Looks like we got some gear mechanism, gearing mechanism over here. Tiny little motor on the back there. But yeah, nothing much doing there. They're pretty simple. And in fact, all of that just bingo popped out of there on a flat flex.

**Dave Jones:** No problems at all. So you could actually, if you're really keen, you could keep that and uh reuse that. There are there likely they usually have like a driver.

**Dave Jones:** I've shown these before in previous videos on the flat flex here. Usually an embedded uh driver uh in there to actually uh drive the elements. There's specific chips you can get and they're usually only available in die form for attaching directly onto the uh flat flex.

**Dave Jones:** So, I think to open the rest of this, I think it just sort of like Ah, look that whole side panel. There you go. That Hey, there you go.

**Dave Jones:** That whole side panel. Oops. I just Look at that. Snapped snapped. The flat flex just sheared right off cuz this is a thicker part of the flat flex down here that goes into there.

**Dave Jones:** And this is thinner. So, yeah. No. Uh, no surprise that it actually sheared off at that point. So, I think the whole thing just lifts out. And as I said, I reckon there's probably another going to be another switch on the bottom here, which will if we if our keys, secure keys, encryption, and all that sort of jazz, whatever it needs, hasn't been erased already.

**Dave Jones:** It most likely is when we get that out. Bingo. Now, here's an interesting aspect to this thing. Of course, there are uh two ways to uh hack the well at least two ways to hack these things.

**Dave Jones:** One is to actually get in to the actual uh circuitry itself and you know get the steal the keys and all that sort of uh jazz and you know maybe hijack your own circuitry on there all that sort of you know really uh deeply complex stuff.

**Dave Jones:** The other simple way is to hack in to the magnetic stripe reader like that. So tap off that and read the signal directly from the card and then also add some uh circuitry you know like a little if you want to hack these you might add on a little board or something like that to read the keypad like this.

**Dave Jones:** So you're basically stealing the um information directly or all you need you don't have to worry about you know def feeding the encryption mechanism and all that sort of stuff with the keys.

**Dave Jones:** All you need to steal is the magnetic card info and people's pin numbers as they actually type them in. I think that's the majority of uh hacks on these uh type of things, but if you got more info on that.

**Dave Jones:** Anyway, so there's two ways to get into this thing. One is through the back of the case, which we saw before, and the other is through the membrane keypad on the front here.

**Dave Jones:** Now, you'll notice, you know, it's just a regular membrane keypad, and there's conductive pads here, which then make contact to our regular buttons. You've seen this before, common in common as mud, every single product.

**Dave Jones:** But look, it's got two additional little contacts there and there that don't made up uh with a button on the front. But look, they have a little little little pin in there molded into the plastic case which then pushes on this and acts as a button when this thing is finally assembled.

**Dave Jones:** And look at that. We've got two pads there and there on the board. Bingo. That's another anti-tamper mechanism. So, if you try and remove that membrane keypad, bingo, it's going to destroy it and lose the keys, do whatever.

**Dave Jones:** And once these things, you have to basically send them back to the dealer or the factory or whatever to get them uh reprogrammed, if that's even possible at all after you open these things.

**Dave Jones:** Maybe not. These things aren't designed to be uh serviced. They're designed to be assembled secure. They got to meet all those um international uh security requirements, all that sort of jazz.

**Dave Jones:** So, there you go. We've now um uh already uh released two anti-tamper mechanisms in this thing. And under there is an on semiconductor NCN64A. That's the driver chip for or the interface chip for the uh SIM modules.

**Dave Jones:** Those three SIM modules we uh saw on the backside. And that's got ESD uh protection built in because the SIM modules of course are easily accessible by uh human fingers.

**Dave Jones:** So, you know, you can don't want to uh kill your main input chip here. And you'll notice all the better nails test pins all the way around here for production testing.

**Dave Jones:** Now, once again, this uh co-processor, this is the secure co-processor. And once again, I'm surprised that it's not potted or has any other anti-tamper mechanism in there. And look, it's a um once again, it's got their own brand on there.

**Dave Jones:** It's Mon EFT 3X specifically for this model, but they they're not spinning their own silicon there. I guarantee it. They're just reusing an offthe-shelf uh secure microcontroller. That won't be a regular one.

**Dave Jones:** A couple of companies around specialize in doing secure microcontrollers specifically for this u purpose. and they they will often have like a self-destruct pin on them so that the uh encryption keys which are kept in SRAMM uh destroyed if you don't keep that pin you know powered up or whatever.

**Dave Jones:** Now this could have been like a modern uh one like say Maxim for example do a max 3250 uh secure microcontroller that does all the AES DEZ you know uh secure key encryption all that sort of stuff.

**Dave Jones:** It's got uh temperature and voltage uh tamper mechanisms and all sorts of fantastic stuff to ensure that you can't uh you know hack and extract the uh keys from this thing.

**Dave Jones:** But um that's only available in a BGA package. But I did find an older school uh Dallas semiconductor of course Dallas owned by Maxim now. And I think this thing cuz it's a 100 pin T QFP.

**Dave Jones:** I think it's a Dallas uh DS5240. I can't get the pin outs for this because you need an NDA shock horror to actually get the full data sheet, but I'll link in down below just the basic uh top level data sheet for this thing.

**Dave Jones:** So, that's what I think it is. Dallas Semiconductor DS5240 perhaps it's an 8051 processor. By the way, that previous Maxim 1 that had a a um ARM Cortex M3, but something like this DS5240 old school 8051 processor, but can access like up to 8 mega RAM, but it's got like 4,096 bit encryption in there.

**Dave Jones:** It's got uh physical uh protection as well. It's got like a pattern that they embed in there over the die. So, if you physically try and like eat away, like actually dissolve away at the plastic, assuming that you got through all the anti-tamper mechanisms on this thing, if you were actually able to dissolve the plastic on there, there'd be like a physical uh metal barrier over the uh top of the

**Dave Jones:** encryption area of the chip, not over the entire chip, but probably just the encryption area of the chip that actually holds the keys. And it's all SRAM based at all.

**Dave Jones:** very fast SRAMM which they uh talk about so that you know if it uh detects any sort of uh temperature tampering, voltage tampering, uh memory bus uh tampering, things like that, uh probing, all those sorts of mechanisms, it'll just erase the keys in there and bingo, your data is lost.

**Dave Jones:** So, this chip in its own right probably has adequate security in there to meet the uh those international security standards we talked about at the start, but I was just, you know, I'm very disappointed that there wasn't extra security like and that was like fully potted or something like that just to make it just that belt and braces engineering approach, you know?

**Dave Jones:** I mean, yeah, this chip can do it on its own, but just would have been nicer to see some extra security in there perhaps. But, I don't know. Um, yeah, it obviously meets the standards.

**Dave Jones:** It's all approved, all that sort of jazz. And really, the odds of you being able to hack this thing, uh, like in terms of the encryption keys and things like that are borderline zero.

**Dave Jones:** So, there you go. I hope you enjoyed the look inside one of these foss pinpad terminals. And yes, there is a lot of security which goes into these are probably, you know, more on chip on dice stuff than anything else.

**Dave Jones:** You know, we've got some basic stuff protecting the keypad and opening the case for those physical attacks. As I said, a hacker wouldn't be bothered trying to get, you know, the keys out of this or hack that processor in any way.

**Dave Jones:** It's just too hard. If they were going to try and hack these things, then they'd, you know, be uh detecting the uh keypad presses and reading your magnetic strip reader.

**Dave Jones:** And that's, you know, you hear reports of uh yeah, people have uh snuck well, not not snuck in, they just do like slide of hand. So, what they do is they case the place first that they want to target.

**Dave Jones:** They've already hacked one of these matching pin pads to what's in a store and uh everything else just to like steal the um the credit card, the basically the PIN number and the uh credit card uh info on there and uh they just, you know, go into the store, slide of hand, they just, you know, disconnect it.

**Dave Jones:** Somebody distracts the attendant while the other one, you know, physically swaps over the unit. So then you've got a hacked uh unit installed and nobody's none the wiser. Then they come back later and they steal it and it's uh captured all of that data.

**Dave Jones:** That's one of the ways that uh these things are often uh hacked anyway. But yeah, really quite difficult to do. The uh security on these things is really pretty good.

**Dave Jones:** So there you go. I hope you enjoyed a look inside these uh pin pads. Data sheets are linked in down below. So check them out. And if you like tear down Tuesday, please give it a big thumbs up.

**Dave Jones:** And um as always, the EE blog forum is the place to discuss it, but YouTube is cool, too. Or the evlog.com website. Catch you next time.
