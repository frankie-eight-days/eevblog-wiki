---
video_id: tCgtTPwlDSo
title: EEVblog #687 - EFTPOS PIN Pad Terminal Teardown
url: https://www.youtube.com/watch?v=tCgtTPwlDSo
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 34, "3": 48, "4": 61, "5": 74, "6": 92, "7": 105, "8": 120, "9": 136, "10": 148, "11": 161, "12": 173, "13": 183, "14": 195, "15": 209, "16": 228, "17": 239, "18": 255, "19": 267, "20": 282, "21": 300, "22": 313, "23": 327, "24": 344, "25": 357, "26": 375, "27": 389, "28": 401, "29": 415, "30": 429, "31": 446, "32": 462, "33": 474, "34": 488, "35": 500, "36": 520, "37": 535, "38": 547, "39": 564, "40": 580, "41": 595, "42": 611, "43": 625, "44": 638, "45": 651, "46": 664, "47": 678, "48": 695, "49": 711, "50": 726, "51": 740, "52": 753, "53": 768, "54": 781, "55": 792, "56": 807, "57": 822, "58": 839, "59": 853, "60": 866, "61": 879, "62": 891, "63": 907, "64": 922, "65": 935, "66": 950, "67": 965, "68": 976, "69": 989, "70": 1002, "71": 1015, "72": 1030, "73": 1043, "74": 1060, "75": 1078, "76": 1089, "77": 1105, "78": 1119, "79": 1130, "80": 1141, "81": 1156, "82": 1173, "83": 1188, "84": 1199, "85": 1216, "86": 1232, "87": 1246, "88": 1263, "89": 1278, "90": 1296, "91": 1311, "92": 1325, "93": 1342, "94": 1354, "95": 1372, "96": 1386, "97": 1397, "98": 1412, "99": 1428, "100": 1442, "101": 1453, "102": 1466, "103": 1479, "104": 1491, "105": 1505, "106": 1519, "107": 1531, "108": 1543, "109": 1556}
---

**Dave Jones:** Hi, welcome to Tearown Tuesday. Today we're going to take a look at this Sageum Montineel uh FPOST pin pad terminal. You might call them uh something else in your country, but we call them basically FPOST terminals here or uh pin pads because I used to work at

**Dave Jones:** the company who actually supplied this key corp. I worked there back in 94. Although I wasn't in the pin pad group, I designed the TFT LCD monitors for these type of banking systems back then. Anyway, this is not a Keycor branded

**Dave Jones:** model. It's uh produced by uh Sageium. I'll link in the data sheet for it down below, but it's one of these typical F-POS terminals. Not a particularly recent one, but recent enough to have a smart card interface on here. And it's

**Dave Jones:** also a GSM model. We'll find that out. In fact, tada. There we go. It's got some uh SIM three SIM card slots down there. I'm not sure why there are actually three there and there's an SD card slot in there. Anyway, so you can

**Dave Jones:** use this as a remote terminal and uh it connects and does your electronic uh credit card transaction at your point of sale. And thanks to Luke Stone for sending this one into the mailbag. He scored it for two bucks at a local

**Dave Jones:** garage sale. Fantastic. So, let's tear down this thing and see what's inside. Now, the interesting thing about these uh pinpad foss terminals is basically the security inside of them. And I'm not talking software security. I'm talking hardware uh anti-tamper security because

**Dave Jones:** it's very important for these things not to be hackable. So, you know, somebody can't uh just buy one commercially on the market or access one like this or steal one or whatever and then hack it and put their own uh circuitry inside of

**Dave Jones:** their own software or whatever to then steal people's uh credit card numbers and pin numbers and things like that. So, expect lots of anti-tamper technology inside this thing. And there's industry standards uh for this. This particular one meets the uh PCI PED

**Dave Jones:** standard. And no, PCI doesn't stand for your regular computer PCI slot. It stands for the payment card industry and they're the uh regulatory body that handle uh the security standards both software and hardware and also management uh for these things. So it's

**Dave Jones:** PCI PED standards. So payment card industry PED stands for PIN entry device which is what the industry term is for one of these but we'll just call it FPOS terminal because that's what they're called here in Australia. Um FPOS if you

**Dave Jones:** don't know is electronic funds transfer at point of sale. There you go. Um and there are various standards for this. Uh we're going this is um meets the PED standard for the pin entry device, but there's uh separate standards for the uh

**Dave Jones:** the DSS standard for the data security standard. It stands for like the protocol the interfacing and and the key generation and all that sort of stuff. And I think you have to like buy the standards or something like that. I

**Dave Jones:** don't think they're readily downloadable, but if they are, please uh link them in and uh or leave a comment and I'll link them in down below. Anyway, I'm going to link in the data sheet for this thing. I'm not sure the

**Dave Jones:** exact age. We'll uh find out. But yeah, as I said, it's got a smart card interface. It's got a card reader down there. You swipe your card. You can hardly see that, but there's a little there's the reading head down in there.

**Dave Jones:** We'll see that when we open it up. Graphical LCD screen. Um, and it comes with this uh cable which has both an Ethernet uh interface here. So it does um IP like you can connect to a regular internet connection and it can do your

**Dave Jones:** transaction that way which is faster than your regular modem. This will also have a um uh V uh 32 modem in it as well. Um and it's also got RS23 uh2 interface. Plus it's also got that wireless uh capability with the uh SIM

**Dave Jones:** card as well. So maybe you can uh attach like an optional battery pack on here dealer fitted or something like that. maybe turn it into a portable device. I don't know. Or maybe it's just a complete leadered device. Anyway, it's

**Dave Jones:** got three different methods to um uh actually do the uh transaction. SIM wireless uh Ethernet and dialup as well. Got a couple of USB ports on here, device and host. That I believe is used for the upgrade of the firmware in this

**Dave Jones:** thing. You can actually plug a cable in and plug in a USB key and you can do your uh firmware upgrades and field upgrades that way. So, should be really interesting. But, and it's got a printer as well. It's just got a little uh cheap

**Dave Jones:** ass thermal simple thermal printer in the thing and a security uh looks like a security locking uh tab or something like that. So, we really want to find out what the anti-tamper mechanisms in this thing. That's going to be the

**Dave Jones:** fascinating bit that I want to see. I don't particularly care what processor it uses. Although these things often use a uh a secure uh processor, a specific uh hardened security processor that has self-destruct mechanisms and things like that. Uh anti-tamper devices built into

**Dave Jones:** the processor, not a regular one. It says it does use a 32-bit risk ARM 9 micro at 200 MIPS in there to do that, but also says it has a co-processor. So, I expect the co-processor to be a

**Dave Jones:** security uh hardened processor. So, this model is the EFT 930S sage monotel. We'll find out the date when we open it. There will no doubt be uh some chips in there, but yeah, like it's got a date of, you know, supplied by key corp in

**Dave Jones:** 2010, but when it was uh designed and serviced, you know, it's at least four or 5 year old. So, um which isn't too bad. So, there we go. That's like a half turn system. You have to uh do that and pull at the same time.

**Dave Jones:** Ah, there we go. That's just a uh cable interface. So, that's got our RS separate RS232 uh Ethernet and it had the USB host. I think that one's for the firmware. So, not entirely sure what the these are the

**Dave Jones:** devices over here, but anyway. So, we can probably do firmware updates through there. RS232 host and ah power. And yeah, I could picture there maybe being a battery uh pack optional extra for that if you just wanted to use the uh

**Dave Jones:** SIM module. No problems. And I don't really know about the uh GPS uh modem inside this thing and the SIM cards here, whether or not, you know, you can just whack any regular SIM card in there and how that's actually uh handled on

**Dave Jones:** the uh client side and all that, the payment gateway and all that uh sort of jazz. I guess you would uh have to be in the industry to know those kind of things. But uh anyway, let's see how we

**Dave Jones:** can open it. So, six of those. But as I said, as soon as we take this case off, I expect there to be at an absolute bare minimum uh anti-tamper uh switch in there built into the case perhaps that

**Dave Jones:** as soon as we open the case, it's going to destroy the uh contents of the um of the uh keys and things like that. But there's probably multiple layers of uh tamper protection in here, not just that. So, let's open it. No, it turns

**Dave Jones:** out they're torque screws. I should be able to find the right size one in here. Should keep them organized. All right, I've taken out the six screws in. Hey, there we go. We broke our little uh security seal there. Not surprising.

**Dave Jones:** And what have we got? Yep, there we go. There's our first Yep. There's our first anti-tamper. There we go. Tactile switch down in there. That's our first anti-tamper mechanism. So, yeah. There. There it is. There's the little uh

**Dave Jones:** button which pushes down on that tab. So, bingo. All the uh we probably screwed the pooch already. If you wanted to get the security uh keys out of this or whatever, you've probably already lost them. And you add a at a minimum

**Dave Jones:** you'd probably have to go back to the uh official dealer and get it reprogrammed or recommissioned or whatever. Um, however that works. And we've got ourselves a 3v lithium battery there. And no doubt a lot of this stuff is

**Dave Jones:** going to be stored in SRAMM. Uh it won't be stored in flash. So you'd expect to find like the keys and things in SRAM so that they can easily be uh destroyed at a moment's notice when you you know uh

**Dave Jones:** and violate any one of the uh tamper mechanisms inside this thing. Now curiously um a massive 4700 mic 10V surface mount cap. Look at that beast there. So they really want to retain that um uh data. Well, I I reckon that's

**Dave Jones:** maybe that's uh for like I don't know some internal real-time clock or something. And maybe that battery only powers the uh keys and uh other uh encryption uh type data perhaps. And this uh cap reservoir cap just uh keeps

**Dave Jones:** maybe the time and date going for uh a long time when it when the power is disconnected perhaps. I'm not entirely sure. And we have ourselves a pulse transformer there for the Ethernet interface. And we've got our recording

**Dave Jones:** head over here, our RS232, our USB uh host over there. Something that's not populated over here. So, I don't know whether or not that's a factory test or some sort of optional thing. Maybe it's part of the No. Yeah, it's something

**Dave Jones:** else. Um, so could be a optional model fit. Couple of parts missing all around here. Not entirely sure. Another big surface mount cap missing here. So, not entirely sure what's uh what's missing around these parts here. And I thought

**Dave Jones:** there wasn't any screws holding that in place. So, I just pulled on it and boop, off it came. Yeah, it's got a huge board to board inconnect here. This plastic got a plastic shield there. Not sure. Like a spacer. I'm not sure why they

**Dave Jones:** bother putting a spacer in there. Is there some sort of anti-tamper mechanism in that? Maybe not. Anyway, we've got a large amount of uh shielding around here. So, oh yeah, there we go. Now, given that uh shielding on the back there and a large

**Dave Jones:** amount of via stitching, that indicates uh well a uh shielding and all the ground plane flood fill on the top as well and all the via stitching, low impedance stuff that indicates high frequency stuff is at play here. So, I'm

**Dave Jones:** thinking this well has got to be uh really there's no option. has got to be the optional uh by the looks of it, not fitted to this, the uh GPS uh module. So, these SIMs um are of no use to this

**Dave Jones:** uh presumably because there's no uh wireless GPS uh functionality not fitted. Now, whether or not um there's it looks like there's some circuitry on there, whether or not there's maybe another board and there's got to be like an antenna somewhere cuz I don't see an

**Dave Jones:** antenna in this uh case at all. So, that's all optional unfortunately. By the way, we have a date code down in there, 36 week 07. So whether or not it's old stock or whether or not it actually uh came from the uh it was

**Dave Jones:** manufactured around, you know, late ' 07 um 08, something like that, not sure. Now, I just thought for a minute, maybe this was the uh modem stuff and this hadn't been uh uh populated in this one, but like there's no isolation there or

**Dave Jones:** uh anything like that. that you'd expect, you know, isolation relay, isolation slots, dedicated isolated section for a uh V32 uh modem that hooks up to the phone line. So, yeah, that doesn't seem to be uh in there or at

**Dave Jones:** least not on the top of anything inside here that we can see so far. And we have a Viccom DM 9161 chipset there with its own dedicated oscillator. Of course, that's all for the Ethernet, the physical uh aspect of the Ethernet

**Dave Jones:** interface. And that one there is just a Joe Blogs RS232 uh interface driver. Now, why they've got a second huge pin count boardtoboard interconnect connector there, I have no idea. It looks like a finer pin pitch than we've

**Dave Jones:** got here. So, I don't know. It's not something you'd ordinarily use for testing. So, maybe it was part of the uh development and uh debug, something like that. And there's nothing fancy happening in most of this. That's clearly a power switch mode power supply

**Dave Jones:** there. Dead giveaway is that uh yeah, it's surrounded by an optional shield which they haven't decided to fit. And when you see big power inductors like that and a big tanelum cap and a little chip next to it controlling it. Yeah.

**Dave Jones:** And a couple of um high value ceramic caps like that in a large package. you know that like to get very low ESR on the output that a switch mode uh controller requires. It's a dead giveaway. And we got ourselves a beeper

**Dave Jones:** up there by the looks of it. And well, not much else happening. Just some miscellaneous stuff down here for the uh USB interfaces over here. Now, the thing I'm very surprised at is that I can still only see one anti-tamper

**Dave Jones:** mechanism, and that was the little tactile switch there, which we saw when we opened the case. I expected the uh processing is that I'm not sure what that is. We'll get in and have a look. Anyway, looks like we've got some RAM

**Dave Jones:** and some flash there. Um that this is all, you know, I expected this to be either physically potted or protected with some sort of extra anti tamper uh mechanism in some respect or at least make it physically difficult to access

**Dave Jones:** by just uh potting the stuff anyway. But no, no, they've just put in a a halfass shield over that. And uh oh, I can read the part numbers straight off there. H. And clearly there's our ARM A9 processor, but that's not the brand.

**Dave Jones:** That's the model. Uh Mon EFT 3X. So, you know, they're just using an offtheshelf ARM processor as they said. Um what was it? A Risk ARM 9 at 200 uh MIPS. So, yeah, they're just rebadging that when you buy enough of them. The rebadged

**Dave Jones:** date code again, 34th week 07. So, there you go. um you know it's unlikely that two chips are going to be from uh 07 especially a processor like this they generally don't leave those sitting around in stock for all that long on

**Dave Jones:** products like this so I reckon yeah it's you know manufactured in late ' 07 or '08 but keyop have whacked that uh 2010 sticker on it was it although actually come to think of it no it's not that

**Dave Jones:** surprising that this is uh not secured in any way cuz this is just the applications processor we haven't goten to the secure processor yet. So that's probably on the other side of the board making it even more difficult to you

**Dave Jones:** know uh hack and get into you because you got to take out the second board. So that co-processor has got to be on the back of this board somewhere and that could have extra anti-tamper stuff. And there's our magnetic uh recording head

**Dave Jones:** down in there. It's just like your regular uh tape based uh you know cassette tape for you youngsters out there. like a regular head maybe uh possibly you know specifically designed for uh credit card scanning and things like that. Nothing fancy thing I found a

**Dave Jones:** bit surprising is that is that a little bit compliant? Yeah, it could be. Usually they build some uh physical compliance into this thing. Hence the flex coming out. And uh usually you know they want to uh get some you know bit of

**Dave Jones:** compliance in the pressure that this head puts across the credit card that you actually swipe into this thing. So yeah I think that's what this metal plate here can be doing. Just giving it a little bit of little bit of pressure

**Dave Jones:** and some give against the card. And I was about to say that these metal look there's metal pins there and there. I thought, "Aha, maybe that's some extra anti-tamper or something. Maybe some conductive uh thing, but I can't find

**Dave Jones:** any matching uh thing in the top case here." So, I thought maybe that was an extra anti-tamper mechanism, but obviously not. So, I don't know why they've put metal pins in there, maybe to hold in the uh uh card slot here for

**Dave Jones:** the smart card, but yeah, I don't know. And there's the head for the thermal printer there. And yeah, they do have one individual pixel. So, it's all the way across. I don't know how many uh pixels I'd have across there, but

**Dave Jones:** there's one individual thermal element which then just burns the uh heats up and burns a dot in the thermal paper as it passes through. Looks like we got some gear mechanism, gearing mechanism over here. Tiny little motor on the back

**Dave Jones:** there. But yeah, nothing much doing there. They're pretty simple. And in fact, all of that just bingo popped out of there on a flat flex. No problems at all. So you could actually, if you're really keen, you could keep that and uh

**Dave Jones:** reuse that. There are there likely they usually have like a driver. I've shown these before in previous videos on the flat flex here. Usually an embedded uh driver uh in there to actually uh drive the elements. There's specific chips you

**Dave Jones:** can get and they're usually only available in die form for attaching directly onto the uh flat flex. So, I think to open the rest of this, I think it just sort of like Ah, look that whole side panel. There you go. That Hey,

**Dave Jones:** there you go. That whole side panel. Oops. I just Look at that. Snapped snapped. The flat flex just sheared right off cuz this is a thicker part of the flat flex down here that goes into there. And this is thinner. So, yeah.

**Dave Jones:** No. Uh, no surprise that it actually sheared off at that point. So, I think the whole thing just lifts out. And as I said, I reckon there's probably another going to be another switch on the bottom here, which will if we if our keys,

**Dave Jones:** secure keys, encryption, and all that sort of jazz, whatever it needs, hasn't been erased already. It most likely is when we get that out. Bingo. Now, here's an interesting aspect to this thing. Of course, there are uh two ways to uh hack

**Dave Jones:** the well at least two ways to hack these things. One is to actually get in to the actual uh circuitry itself and you know get the steal the keys and all that sort of uh jazz and you know maybe hijack

**Dave Jones:** your own circuitry on there all that sort of you know really uh deeply complex stuff. The other simple way is to hack in to the magnetic stripe reader like that. So tap off that and read the signal directly from the card and then

**Dave Jones:** also add some uh circuitry you know like a little if you want to hack these you might add on a little board or something like that to read the keypad like this. So you're basically stealing the um information directly or all you need you

**Dave Jones:** don't have to worry about you know def feeding the encryption mechanism and all that sort of stuff with the keys. All you need to steal is the magnetic card info and people's pin numbers as they actually type them in. I think that's

**Dave Jones:** the majority of uh hacks on these uh type of things, but if you got more info on that. Anyway, so there's two ways to get into this thing. One is through the back of the case, which we saw before,

**Dave Jones:** and the other is through the membrane keypad on the front here. Now, you'll notice, you know, it's just a regular membrane keypad, and there's conductive pads here, which then make contact to our regular buttons. You've seen this before, common in common as mud, every

**Dave Jones:** single product. But look, it's got two additional little contacts there and there that don't made up uh with a button on the front. But look, they have a little little little pin in there molded into the plastic case which then

**Dave Jones:** pushes on this and acts as a button when this thing is finally assembled. And look at that. We've got two pads there and there on the board. Bingo. That's another anti-tamper mechanism. So, if you try and remove that membrane keypad,

**Dave Jones:** bingo, it's going to destroy it and lose the keys, do whatever. And once these things, you have to basically send them back to the dealer or the factory or whatever to get them uh reprogrammed, if that's even possible at all after you

**Dave Jones:** open these things. Maybe not. These things aren't designed to be uh serviced. They're designed to be assembled secure. They got to meet all those um international uh security requirements, all that sort of jazz. So, there you go. We've now um uh already uh

**Dave Jones:** released two anti-tamper mechanisms in this thing. And under there is an on semiconductor NCN64A. That's the driver chip for or the interface chip for the uh SIM modules. Those three SIM modules we uh saw on the backside. And that's got ESD

**Dave Jones:** uh protection built in because the SIM modules of course are easily accessible by uh human fingers. So, you know, you can don't want to uh kill your main input chip here. And you'll notice all the better nails test pins all the way

**Dave Jones:** around here for production testing. Now, once again, this uh co-processor, this is the secure co-processor. And once again, I'm surprised that it's not potted or has any other anti-tamper mechanism in there. And look, it's a um once again, it's got

**Dave Jones:** their own brand on there. It's Mon EFT 3X specifically for this model, but they they're not spinning their own silicon there. I guarantee it. They're just reusing an offthe-shelf uh secure microcontroller. That won't be a regular one. A couple of companies around

**Dave Jones:** specialize in doing secure microcontrollers specifically for this u purpose. and they they will often have like a self-destruct pin on them so that the uh encryption keys which are kept in SRAMM uh destroyed if you don't keep that pin you know powered up or

**Dave Jones:** whatever. Now this could have been like a modern uh one like say Maxim for example do a max 3250 uh secure microcontroller that does all the AES DEZ you know uh secure key encryption all that sort of stuff. It's

**Dave Jones:** got uh temperature and voltage uh tamper mechanisms and all sorts of fantastic stuff to ensure that you can't uh you know hack and extract the uh keys from this thing. But um that's only available in a BGA package. But I did find an

**Dave Jones:** older school uh Dallas semiconductor of course Dallas owned by Maxim now. And I think this thing cuz it's a 100 pin T QFP. I think it's a Dallas uh DS5240. I can't get the pin outs for this because you need an NDA shock

**Dave Jones:** horror to actually get the full data sheet, but I'll link in down below just the basic uh top level data sheet for this thing. So, that's what I think it is. Dallas Semiconductor DS5240 perhaps it's an 8051 processor.

**Dave Jones:** By the way, that previous Maxim 1 that had a a um ARM Cortex M3, but something like this DS5240 old school 8051 processor, but can access like up to 8 mega RAM, but it's got like 4,096 bit encryption in there. It's got uh

**Dave Jones:** physical uh protection as well. It's got like a pattern that they embed in there over the die. So, if you physically try and like eat away, like actually dissolve away at the plastic, assuming that you got through all the anti-tamper

**Dave Jones:** mechanisms on this thing, if you were actually able to dissolve the plastic on there, there'd be like a physical uh metal barrier over the uh top of the encryption area of the chip, not over the entire chip, but probably just the

**Dave Jones:** encryption area of the chip that actually holds the keys. And it's all SRAM based at all. very fast SRAMM which they uh talk about so that you know if it uh detects any sort of uh temperature tampering, voltage tampering, uh memory

**Dave Jones:** bus uh tampering, things like that, uh probing, all those sorts of mechanisms, it'll just erase the keys in there and bingo, your data is lost. So, this chip in its own right probably has adequate security in there to meet the uh those

**Dave Jones:** international security standards we talked about at the start, but I was just, you know, I'm very disappointed that there wasn't extra security like and that was like fully potted or something like that just to make it just that belt and braces engineering

**Dave Jones:** approach, you know? I mean, yeah, this chip can do it on its own, but just would have been nicer to see some extra security in there perhaps. But, I don't know. Um, yeah, it obviously meets the standards. It's all approved, all that

**Dave Jones:** sort of jazz. And really, the odds of you being able to hack this thing, uh, like in terms of the encryption keys and things like that are borderline zero. So, there you go. I hope you enjoyed the look inside one of

**Dave Jones:** these foss pinpad terminals. And yes, there is a lot of security which goes into these are probably, you know, more on chip on dice stuff than anything else. You know, we've got some basic stuff protecting the keypad and opening

**Dave Jones:** the case for those physical attacks. As I said, a hacker wouldn't be bothered trying to get, you know, the keys out of this or hack that processor in any way. It's just too hard. If they were going to try and hack these things, then

**Dave Jones:** they'd, you know, be uh detecting the uh keypad presses and reading your magnetic strip reader. And that's, you know, you hear reports of uh yeah, people have uh snuck well, not not snuck in, they just do like slide of hand. So, what they do

**Dave Jones:** is they case the place first that they want to target. They've already hacked one of these matching pin pads to what's in a store and uh everything else just to like steal the um the credit card, the basically the PIN number and the uh

**Dave Jones:** credit card uh info on there and uh they just, you know, go into the store, slide of hand, they just, you know, disconnect it. Somebody distracts the attendant while the other one, you know, physically swaps over the unit. So then

**Dave Jones:** you've got a hacked uh unit installed and nobody's none the wiser. Then they come back later and they steal it and it's uh captured all of that data. That's one of the ways that uh these things are often uh hacked anyway. But

**Dave Jones:** yeah, really quite difficult to do. The uh security on these things is really pretty good. So there you go. I hope you enjoyed a look inside these uh pin pads. Data sheets are linked in down below. So check them out. And if you like tear

**Dave Jones:** down Tuesday, please give it a big thumbs up. And um as always, the EE blog forum is the place to discuss it, but YouTube is cool, too. Or the evlog.com website. Catch you next time.
