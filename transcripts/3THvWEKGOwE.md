---
video_id: 3THvWEKGOwE
title: EEVblog #879 - R&S HMO1202 Scope Bandwidth Hack Investigation
url: https://www.youtube.com/watch?v=3THvWEKGOwE
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 35, "3": 45, "4": 60, "5": 74, "6": 88, "7": 102, "8": 117, "9": 130, "10": 142, "11": 156, "12": 169, "13": 189, "14": 202, "15": 221, "16": 233, "17": 250, "18": 265, "19": 279, "20": 291, "21": 303, "22": 318, "23": 332, "24": 348, "25": 364, "26": 377, "27": 396, "28": 411, "29": 430, "30": 443, "31": 458, "32": 473, "33": 485, "34": 501, "35": 516, "36": 531, "37": 544, "38": 555, "39": 569, "40": 581, "41": 595, "42": 608, "43": 623, "44": 640, "45": 655, "46": 671, "47": 683, "48": 702, "49": 717, "50": 729, "51": 744, "52": 758, "53": 769, "54": 782, "55": 795, "56": 805, "57": 817, "58": 828, "59": 841, "60": 852, "61": 866, "62": 881, "63": 900, "64": 913, "65": 928, "66": 943, "67": 960, "68": 973, "69": 987, "70": 1003, "71": 1018, "72": 1030, "73": 1045, "74": 1062, "75": 1076, "76": 1100, "77": 1113, "78": 1126, "79": 1140, "80": 1154, "81": 1171, "82": 1190, "83": 1204, "84": 1220, "85": 1232, "86": 1244, "87": 1269, "88": 1287, "89": 1304, "90": 1317, "91": 1331, "92": 1344, "93": 1360, "94": 1377, "95": 1392, "96": 1410, "97": 1430, "98": 1448, "99": 1462, "100": 1479, "101": 1497, "102": 1513, "103": 1528, "104": 1549, "105": 1564, "106": 1579, "107": 1595, "108": 1610, "109": 1622, "110": 1639, "111": 1652, "112": 1666, "113": 1680, "114": 1692, "115": 1705, "116": 1719, "117": 1733, "118": 1745, "119": 1760}
---

**Dave Jones:** Hi. Now, you've seen this little baby in uh several previous videos of Rohde & Schwarz HMO 1202 series uh scopes. And click here if you want to have a look at the I've done a uh teardown video of

**Dave Jones:** this thing. I've also done videos for uh comparing the FFT mode, which I really like on this thing, and things like that. It's a really nice little compact professional scope.

**Dave Jones:** So, I love this little thing. And you'll notice that up the top here, it does not have a bandwidth listed on it. Um which is quite unusual. And the reason they do that is because this is a software

**Dave Jones:** upgradeable bandwidth scope, as many on the market are nowadays. Probably the you know, a good majority of them actually have the full bandwidth inside them in the vertical amplifiers here. The bandwidth is actually there, but then they software limit you by a

**Dave Jones:** license keys and everything else to various bandwidth. Now, this one is available in uh 100 MHz is the base bandwidth. That's about goes current uh price is about 1,300 US dollars uh for that one. And there's also a 200 MHz

**Dave Jones:** version. And my one here is the 300 MHz version. But you sure wouldn't know it by looking at the front panel, cuz you've got it's just a license key inside which upgrades the bandwidth. So, even the base model 100 MHz unit you buy

**Dave Jones:** for um you know, 1,200 bucks or something like that, is has the full 300 MHz bandwidth in here. So, I thought just for educational purposes, we will uh crack this thing open yet again, and we'll have a look at the front end here

**Dave Jones:** yet again, and see what uh chip it's using, what topology it's using, and see if there's any little tweaks that we can uh make to potentially um get uh greater bandwidth out of the base model unit. Unfortunately, I've

**Dave Jones:** actually got Unfortunately, in quote marks, I have got the 300 MHz license keys already installed for this one because it's full bandwidth, but we should be able to probe some things and and have a look at how they're actually

**Dave Jones:** doing that. Should be fun. Let's go. And the only thing that tells me this is a 300 MHz version is just this sticker on the back they've got here. So, they've obviously this is done at the factory. They've whacked the sticker on, but you

**Dave Jones:** can actually buy the license upgrade later. So, here's inside the unit as we've seen in the previous teardown video. Got metal cans on the top here for our two analog channels and unfortunately metal cans on the bottom which are even more unfortunately

**Dave Jones:** soldered in place, but there's only one point there one solder point so I can desolder that and lift this can off without having to take the board out. So, yeah, okay, small win. Now, if we have a look at the

**Dave Jones:** front end here, I've got that bottom side can off then there's our BNC. We've got some attenuation switching relays and these uh transistors down in here, they're probably well, they're those SOT23 packages. They're likely transistors. They're probably the JFET

**Dave Jones:** uh front end probably you know, a couple of JFETs and a BJT or something like that. Um and apart from that if and I've got uh here's a photo of the other side of the board. I won't bother taking the

**Dave Jones:** other side of the board. I think you have to get the um whole board out to get that out side and there's nothing terribly interesting there. The part we are interested in is however right here. That puppy that's doing all the business. And here

**Dave Jones:** it is. Sorry about the angle, but uh it's hard to read this number if you don't get the light at the right angle. It's a 6518 and this is quite a common uh part. You'll find these in a lot of um scopes

**Dave Jones:** on the market and we'll see that this might be doing some magic. Let's go to the data sheet. So, here we go. The LMH6518 900 MHz digitally programmable VGA. That's not video graphics adapter. That's variable gain amplifier. And uh

**Dave Jones:** this is specifically, look, it tells you oscilloscope programmable gain amplifier. And uh this is the internal uh block diagram. There's an input preamp. There's a ladder attenuator, which should be being used. Uh most likely is being used by the uh volts per

**Dave Jones:** division setting. So, we'll uh be checking that um here today as well. But, look, bandwidth limiting circuit right inside there. There it is. That's what we're interested in. And it's got a differential output driver. So, differential input, differential output

**Dave Jones:** there. Um and it's got an auxiliary output also tapped off here, which you can use for uh triggering as well. So, that's very handy to um uh you know, when you select channel one triggering, it's most likely going to be coming from

**Dave Jones:** here. Um so, we can actually go down. There's all sorts of uh jazz here. 900 MHz, blah blah blah. We won't go through all the specs, uh which are quite impressive. It's a very nice uh very nice part. Uh

**Dave Jones:** perfect for um scope front ends. Here's our pinout. So, we're actually looking what we want to do is uh tap in to the serial line on this thing, the SPI line. So, uh here they are. Chip select, SDIO,

**Dave Jones:** and S clock there. So, those those three pins, pins 9, 10, and 11, they're the ones we want to tap into to see Oh, by the way, here are the uh here here are the various uh responses for the different attenuation

**Dave Jones:** settings, which we'll see. So, if we go down here, it's they've got very comprehensive uh parametric graphs there. I like it. That's terrific. And uh but, what we want to do is see down here. Here's the signal path, there's ladder step

**Dave Jones:** attenuator, no problems whatsoever. As I said, the volts per division setting is probably doing that. Uh front end attenuators, and we're getting we're getting down here. Trust me. Here comes the exciting part. It's coming. I know it is. I know it is. And

**Dave Jones:** there's an example digital oscilloscope front end. So, maybe that's, you know, they might have used this as an example of how to do this, but, you know, they've been designing scopes for a long time. They would have their own

**Dave Jones:** implementation. So, here's the um SPI pins. It's three-wire SPI interface. Here's the serial protocol stuff, which we'll no doubt have a look at. But, aha, here it is. Table six, the filer filer filter selection data field. And these are the bandwidths. Look, you can

**Dave Jones:** actually choose full bandwidth if you write 000 to a register somewhere in the chip, or you can get 750 650 350, not quite the 300 MHz maximum bandwidth that which this one has. So, the bandwidth is most likely being limited somewhere

**Dave Jones:** else. Here's the theory, but the 200 MHz and 100 MHz bandwidths bingo. They sell 100 MHz and 200 MHz versions of this scope, software licensable software license upgradeable. So, you can bet your bottom dollar all they're doing is setting a couple of

**Dave Jones:** registers inside this chip. You buy your license code, you plug it in, and it says, "Yep, you now have got, you know, MHz for example." All they're doing is setting one just changing a couple of bits in a register there, which limits

**Dave Jones:** the bandwidth inside that front end chip. Because they've already gone to all the expense and effort to design the 300 MHz bandwidth front end and characterize it and everything else. It doesn't make sense to really build a scope that has a 100 a physical 100 MHz

**Dave Jones:** limitation. So, the these companies, very common days, they actually um build the bandwidth into the scope and then software limit the uh options. And they do that in this case using a chip, whereas I think one of the early Rigol

**Dave Jones:** ones where is the DS1052E was it um or the could be the 1054Z as well, I forget. But yeah, it's using like a varicap diode and then uses a digital line to drive that and it sort of sets a

**Dave Jones:** bandwidth limit and you know, that sort of stuff. So, um this one uses a specific chip which has filter a programmable a digitally programmable filter analog filter. It's not a digital filter analog filter built in. And all they do is flipping those

**Dave Jones:** bits. So, that's what we're going to try today. We're going to probe that bus and see if those bits pop out. I bet you they will. So, this is really easy to find. Here we go. Pin one here and four pins per side

**Dave Jones:** exactly as per the data sheet. 1 2 3 4 5 6 7 8 on that side and bingo 9 10 11 and look, they go out to convenient vias there so that we can um put some little uh mod wire in there.

**Dave Jones:** Like difficult to probe. Like you Yes, you can probe them with your scope, but trying to hold three on there at once is you know, uh it's ridiculous. So, yeah, what we'll do is we'll um solder some uh little

**Dave Jones:** you know, 35 gauge mod wire or something on there and uh we'll be able to then crack into that with our logic analyzer and see what's going on. That'll be fun. And of course, this will apply to any

**Dave Jones:** scope on the market that uses the LMH6518. And if your scope does use this chip in the front end, then and and it's got like selectable bandwidth, then you can bet your bottom dollar that that's what they're that's how they're doing the

**Dave Jones:** bandwidth limiting in this thing cuz this thing has as we saw in the data sheet the 20 MHz bandwidth limit. So, practically every scope has a 20 MHz bandwidth limit and this is almost certainly how they're doing it if they

**Dave Jones:** have this chip. Just send an SPI command in, bingo, you've got your 20 MHz bandwidth limit and it's most likely how they're doing the bandwidth the software license upgradeable bandwidth as well. So, I'll do this using my Tagarno

**Dave Jones:** microscope here and yes, I've got to prop it up on some books. So, why not prop it up on the Art of Electronics? Beauty. So, yeah, because it can't It's got a big working distance, but of course you can't have it flat on the

**Dave Jones:** bench and be this high up. It just the working distance doesn't work there. So, I've got my little remote control and we can zoom in. Yay! Excellent. All right, we're going to use some 38 AWG wire wrap wire should do the

**Dave Jones:** job. Otherwise, known as mod wire, hack wire, whatever you want to call it. Let's go. All right, I think that solder mask coming over the pads, it's almost not quite tinted. It's like, you know, 10-20% tinted, which is really

**Dave Jones:** rather annoying. Hmm. Yeah, we can access the pad, but yeah, having a hard time getting that iron onto it. So, we might actually have to go for a sharper, more conical tip to actually get right in there. So, let's give this

**Dave Jones:** one a whirl. It's not often that I use the conical point tips. So, this is the for those playing along at home, that's the JBC tip I'm going to use now. So, we'll just wax some flux around that chip there.

**Dave Jones:** This is all really fine pitch stuff. You'd have a hard time doing this without magnification. Although, I you know, I can. I've done this stuff before without it, but yeah, it's just a real pain in the ass, but yeah, I don't like

**Dave Jones:** our chances of getting down those vias. And what I'll do is I'll just scrape away some of that solder mask first. Just so that I can get uh more iron contact onto the pad which then can maybe and

**Dave Jones:** solder the wire onto. Let's give that a whirl. This could get messy. It looks ugly, but then you uh clean it up and uh it looks just fine. There we go. I think we got one. Don't like my chances of uh

**Dave Jones:** putting it down the hole, but that's okay. We'll just uh tack it there onto the pad. She'll be right. I stripped a bit too much off there, I think. And just apply a dab of flux again each time just to make

**Dave Jones:** your life easier. And bingo. We have got some more solder in there. By the way, with this um fine conical tip, uh you're going to want to turn the uh temperature up. I've currently got it set to 325.

**Dave Jones:** Whereas uh fine stuff like this I'd normally do with my wedge and things like that at like 275. You know, 270, something like even 265, something like that. But because, you know, the physical surface area is not there, um

**Dave Jones:** then, you know, you might have to turn your uh temp up a bit. But I found just a little experiment uh that, you know, I've had to um you know, up the temperature just a bit. This is why you need a

**Dave Jones:** temperature-controlled soldering iron. Every job is different. That's a bit nasty, but there we go. I think she flowed. Yes, I did uh tin these wires beforehand, but uh yeah, you just want to put a fresh coat on there and don't

**Dave Jones:** have a big blob. And we'll just clean that up a little bit. And uh that will evaporate and she'll be right. No worries. And I've deliberately left these wires long, so um A, you can, you know, handle the ends

**Dave Jones:** of them, put your probes on, get them off the board and things like that because, you know, signal integrity is not a big issue here and allows us to put some tape on there. You definitely want to put some tape down on there so

**Dave Jones:** that when you handle these leads on the other end, there's uh no stress on those leads. So, you can get down here, you know, hook up your probes and wiggle them around, no problems whatsoever, move the thing around the bench, and you

**Dave Jones:** know, you're not going to break your little tiny little joint in there. And of course, that wouldn't have been an issue if we could have got these like down the via properly, and then it would have had real, you know, a lot of

**Dave Jones:** mechanical strength. And we probably could have got in there with a smaller gauge like a multi strand wire like this, and we could have got in there and used a smaller stuff like that, maybe got down the via, but

**Dave Jones:** it doesn't matter. This is more than good enough. We just want to probe it. It's not like a permanent fix or anything. But you'll notice that channel two is picking up some 50 hertz hum here cuz we've taken the can off, it's

**Dave Jones:** unshielded, and we've hooked up lines in there, everything's capacitively coupling all over the place, and yeah, that's interesting. So, bugger it. I've had enough of using this thing to probe its own clacker. Let's have a look now at

**Dave Jones:** hooking up the SPI line here. So, I've got all three channels coming in. By the way, it is not a true SPI as you know it cuz SPI, if we go in here, is normally a four-wire thing. We've got our clock,

**Dave Jones:** our whoop bloody touchscreen our MOSI and our MISO, i.e., input and output data signals and chip select. But in this case, it's actually a three-wire SPI interface. It's still SPI, but it's three-wire, so it shares it's bidirectional here. So, it's not as

**Dave Jones:** great a throughput, it goes tristate and everything else. So, anyway, we don't actually have a specific support for that, so I've just set it up here. Haven't set up the bits yet, but let's just trigger this thing and

**Dave Jones:** have a look. I'll press the bandwidth button, and bam, there we go. Look at this. We've got our clock, we've got our data, we have our chip select. This is exactly what we expect. And let's just have a look to see if this data now here

**Dave Jones:** changes. I haven't tried it. Okay? So, we're in um uh let's go to normal uh mode. So, let's go to a quiet yet. We're in normal mode. Okay? So, we're going to run it. Here we go. So, I press it. Let's press it again.

**Dave Jones:** Look. Bingo. There we go. Nice. And now we can get in there and actually decode the bit. That's exactly what I expect. It's exactly as per the data sheet. Here it is. It's exactly what we uh expected with the 24

**Dave Jones:** uh bits or whatever. Here we go. A re uh write operate write operation. There we go. It's supposed to send 24 bits uh the command and then the data field. And we have the data for that. And we can see

**Dave Jones:** the bit changing. Yeah, it's somewhere over here. Yeah, if you correlate it, look, it looks to be in the right spot to have the um the D6, D7, and D8, which is our filter selection field. All right. So, let's just have a look at the

**Dave Jones:** first section, which is the command section here. And uh we'll just expand that out. And here's where it starts here. And the command uh to write is a zero. Uh by the way, the read is a one there. So, that's basically it. All the

**Dave Jones:** others are don't care. So, that's actually pretty uh wasteful. Um so, anyway, it is zero because it's the first transition, remember? After the chip select goes low, um which it which it is, it has done, uh which is way off

**Dave Jones:** screen. It does it sometime before that. Then the first positive edge there is and the data is a zero. So, we are in write mode. So, it is writing. And now we can And all these bits are zeros.

**Dave Jones:** They're all don't care. So, then we have to figure out where the next bits go. Okay. So, this first um high here is actually if you count the positive edges there, unless I'm wrong, then that is the 14th count. So, we've

**Dave Jones:** already got uh the first eight uh bits are the command word. So, it'll be 9 10 11 12 13 and 14 here. So, the first one bit there is we're looking at the um full power. So, it's not in full power

**Dave Jones:** mode. It's obviously in aux high z mode. You'd have to look at the data sheet to know what that does. We don't care about that. We're after the filter. So, the next bit is zero. Sure enough, it is. And then, tada, here we go. It's

**Dave Jones:** this bit, this bit, and this bit. So, we got 0 0 1. Let's have a look down here. 0 0 1. Well, what do you know? Surprise, surprise. 0 0 1. 20 MHz bandwidth. No worries. And what I'll do

**Dave Jones:** here, just because I can, I'll actually line up the waveform with this on the screen here. And that can just be a handy way to actually do it. And the way you do this is with your horizontal here. This is one of your uses for your

**Dave Jones:** fine horizontal control. So, you go in there and because if you don't do that, then you've got these huge big jumps, right? You're always typical 1 2 5 sequence. But if you go in there fine, you can actually adjust this and move it

**Dave Jones:** across and all that sort of stuff. And we said before that that bit was I don't know. Maybe I should stick the paper there. But uh you know, we said that that first bit lined up with that one there. And you just scale it to

**Dave Jones:** match. So, there you go. That's not actually too far out. We could tweak it a little bit better. It doesn't help that uh these things are not uh even like detents like the width there. Anyway, um we can see that uh this

**Dave Jones:** transition here, this would be D6 down here. That's what we got, 001. And then, D5, well, it just squeezes in. That one's a zero as it should be. And LG and HG mode, I can't recall what that is. We'd have to read the data sheet.

**Dave Jones:** That's a zero, so we're in LG, whatever that is. And um, see table seven. This is the ladder attenuation field. So, this value here is going to change based on the attenuation setting and what's required for the front end. So, that

**Dave Jones:** won't change if we just change the bandwidth or anything like that. But, when we change the volts per division setting for channel two, we'd expect this data here to change. So, we know that chipset is definitely being used for the 20 MHz bandwidth

**Dave Jones:** attenuation, which is exactly what you expect. There's no other hardware in there. You don't have to examine any of the rest of the front end circuitry to know that the 20 MHz bandwidth limit is being done inside this LMH chip. So, now we'll we'll undo

**Dave Jones:** the bandwidth. So, remember, my one is software licensed to 300 MHz. Okay? So, we want to see what that goes to. Will it go to full bandwidth or will it go to the 350 meg bandwidth setting? Only one

**Dave Jones:** way to find out. Here we go. I'll hit it. And there we go. I can jump back and forth between those. And because we're triggering on exactly the same point, this is really neat. All right, we'll be able to see it. So, what

**Dave Jones:** we've got is we've got 11 and zero. Okay? So, 110. Let's have a look. What's 110? 1 1 0. Oh, look at that. 750 MHz. Wow, there's one there for full, so it's not 000, but they're certainly not setting it to

**Dave Jones:** 350. So, obviously, because the mine is a 300 bandwidth 300 MHz bandwidth scope, that's the maximum in this range. Obviously, the 300 MHz bandwidth is being um uh done elsewhere like in the hard the rest of the front end is only capable of

**Dave Jones:** 300 MHz. So, they're actually capping it there, but you can bet your bottom dollar that the 200 MHz version and the 100 MHz version of this scope would enable those bits there. I 99.9% sure. So, there you go. That's

**Dave Jones:** interesting to know. Obviously, they've put it to a high uh limit. Maybe they 750 just takes the edge off something perhaps rather than just the full bandwidth cuz I think this chip's capable of like 1 gig or something

**Dave Jones:** ridiculous like that. So, um yeah. It's interesting to know that they've chosen 750 and not 650 and not 350. I can probably understand why they didn't choose 350. Maybe that would have an impact some of the roll off there and

**Dave Jones:** it's issues, you know, to do with pulse response of the front end and everything else. So, you know, there you go. It's set to 750 MHz. All right. So, let's now see what if this ladder attenuation changes here when we change our volts

**Dave Jones:** per division setting. It may not change on every setting, but let's give it a whirl here and Woah, hello. That's significantly changed. I did not expect Oh, no. I think maybe our timing is out. Is it? I'm not sure. I'm changing the

**Dave Jones:** time base range there. I would have expected everything here to remain the same all of the bandwidth stuff, but uh it's not. That's interesting. The bandwidth could change, by the way, right down to like 1 mV per division or

**Dave Jones:** something like that, but I'm going up to 2 V per division. Something else is uh is happening. So, let's have a look at that. There we go, that's better. That's a better look at it. Well, this is interesting. Look, we're

**Dave Jones:** getting no chip select now when I do that. Where's our chip select gone? But, let's do the bandwidth. The bandwidth does do the chip select. And that's the invert button. I'm hitting the invert. Aha! Look, we're getting that Are we getting that extra

**Dave Jones:** packet there? What's going on? Hang on, I'll single shot capture that. Bingo! Look at that. So, the invert is doing two rights there with no chip select. That is interesting. Surely you need the chip select to also do the read. You have to. But, I do find

**Dave Jones:** it rather fascinating that that's a hell of a lot more than uh 24 uh cycles, but uh both of these are supposed to be 24 read and write to this um serial interface, this uh three-wire SPI, are supposed to be uh 24

**Dave Jones:** cycles. And we're getting a lot more than that. My only conclusion is that there's something else on the bus. The chip select is not going low there. So, this chip is not being selected. This data is not destined for this chip.

**Dave Jones:** Another one which we could capture perhaps that um is doing the chip enable. There we go. So, we need to actually trigger enable to get this. Okay, I'm now triggering from channel one and bingo! There we go. That's the only data that

**Dave Jones:** matters. So, there's other The only other conclusion, part B, the only other conclusion is that there are other chips on this bus, hence why they're using the three-wire interface with the tri-state ability because only they only this LMH chip is being

**Dave Jones:** accessed here and that is the data. So that's actually the data. That's actually the data that we want to look at for the front end, okay? So let's let's call that up. There we go. Uh let's just have a look

**Dave Jones:** at it that way and now I will change the time base setting. There whoop. There we go. There we go. You can see it changing all those lower order bits changing there. Yep. Lower order bits changing. So if I'm right

**Dave Jones:** down to 1 mV per division, 2 5 10 20 There you go. And there's all our lower bits. All our lower bits changing to match Tada! That data table there for the ladder attenuation. So they are using the internal um attenuators inside that

**Dave Jones:** chip as well as the bandwidth. So we have other chippies in there that are doing something all hooked onto the same bus. Duh! How annoying. That sort of you know, it was a bit of a red herring there for a little bit but uh

**Dave Jones:** yep, easily figured it out. Trigger off the uh chip select. No worries. Anyway, what I wanted to determine is that I was that filter being implemented in the LMH chip and yes, it is exactly as it expected. No worries whatsoever in the

**Dave Jones:** attenuation and all that sort of stuff and um almost certainly the bandwidth of these things with the license options is being set in the bits in that chip and that's it. Unfortunately, um I don't seem I don't uh I can't find an option

**Dave Jones:** to actually uninstall my 300 MHz license here. If I was able to do that, then I you know, in and revert back to the 100 MHz base unit, we'd be able to verify that that 100 MHz um option

**Dave Jones:** Tada! In there was actually being set and um you can bet your bottom dollar it is. That's how they're doing it because they've got a 100 MHz model, they've got a 20 MHz model. They're engaging the 20 MHz, so they're definitely doing it.

**Dave Jones:** It's working for your regular 20 MHz bandwidth limit. So, almost certain that they're engaging both of those cuz we know it's the same hardware and this 750 MHz figure is being engaged is being set when on you know, the full bandwidth for the 300 MHz

**Dave Jones:** version of this scope. So, that's interesting that you could actually get in here and hack this thing. It's it's a bit ugly, but you could if you wanted to. If you had the 100 MHz low-end version of this scope, you could

**Dave Jones:** have a little micro on that bus that actually in turn because it's not a full like a proper SPI bus, you can't just like plug it in series with the bus cuz there's other as we saw, there's other chips here on the

**Dave Jones:** bus there, right? So, you don't want to interfere with any of those, but what you could do is anytime that you you know, you could sit in the micro could sit there and watch it. It'd have to intercept the chip select line of course

**Dave Jones:** and then but if it did that, you could actually feed data on there to do that, but you'd have to make sure that you didn't conflict with any of the other data here cuz you're writing onto a common data bus which is clearly

**Dave Jones:** shared with something else. I don't know what. There's nothing obvious in the other front end. Some of the chips are not easy to identify and yeah, I don't know what they're doing. So, but you got to be careful not to

**Dave Jones:** overwrite that other data cuz who knows what's going to be happening, but it's possible to actually get in there and just use in you know, little man in the middle attack so to speak and tweak those register settings to get

**Dave Jones:** yourself the full bandwidth scope. So, there you go. I hope you found that interesting and educational even if we did follow a few red herrings down a few rabbit holes there, it was fun nonetheless. If you want to discuss it,

**Dave Jones:** leave comments down below, EV blog forum, all the usual stuff. Hope you enjoyed it. Catch you next time. So, this has got to be a pet cat. I'm just trying to sanity check to figure out what's going on here. Sorry about

**Dave Jones:** all this. This is like real time, you know, this is a real problem I'm encountering here, so I'm going to show it. But I I'm getting nothing there. I swear I swear I'm probing exactly the same damn point down there. There's the

**Dave Jones:** probes. Look, probing exactly the same point. And like, what? What? That is one of the weirdest things
