---
video_id: kp63MZ6RudE
title: EEVblog #889 - Credit Card RFID/NFC Theft Protection Tested
url: https://www.youtube.com/watch?v=kp63MZ6RudE
source: youtube-asr
timestamps: {"0": 0, "1": 7, "2": 19, "3": 32, "4": 43, "5": 50, "6": 62, "7": 74, "8": 94, "9": 116, "10": 126, "11": 138, "12": 148, "13": 170, "14": 179, "15": 193, "16": 210, "17": 226, "18": 249, "19": 269, "20": 280, "21": 296, "22": 306, "23": 317, "24": 326, "25": 335, "26": 345, "27": 362, "28": 374, "29": 392, "30": 404, "31": 417, "32": 430, "33": 447, "34": 466, "35": 484, "36": 495, "37": 508, "38": 522, "39": 541, "40": 553, "41": 561, "42": 572, "43": 582, "44": 596, "45": 603, "46": 620, "47": 641, "48": 661, "49": 675, "50": 703, "51": 716, "52": 731, "53": 739, "54": 751, "55": 765, "56": 782, "57": 797, "58": 807, "59": 822, "60": 834, "61": 845, "62": 861, "63": 869, "64": 883, "65": 894, "66": 904, "67": 920, "68": 928, "69": 948, "70": 959, "71": 970, "72": 978, "73": 993, "74": 1006, "75": 1017, "76": 1028}
---

**Dave Jones:** Hi. You know doubt familiar with modern credit cards like this one that have an RFID chip embedded in them or tap and go as it's called here in Australia.

**Dave Jones:** It might be called different things in other countries. They actually contain a radio frequency identification device, an RFID chip in them. And no, it's not this thing here. That's the secure chip and pin thing.

**Dave Jones:** It's actually embedded elsewhere in the card. And it's goes under various names. Could be Visa payWave or it could be MasterCard PayPass or various other names depending on which provider you've got.

**Dave Jones:** But they all work on the same RFID technology. We can just use your credit card like this just to tap and go as the name suggests. You just tap it onto a reader like this.

**Dave Jones:** If you've got a reader, you can just go like that. Bam. Hold it there for a second or two and you've instantly paid for your transaction. In Australia at least, it's up to $100.

**Dave Jones:** No need to enter your PIN number. No need to insert your card. No need to swipe it on the back or anything like that. Tap and go. Beautiful. But it's not without its security concerns.

**Dave Jones:** And my interest in this came about because Mrs. EE Vblog got a new handbag here. It's a Gianotti brand for those playing along at home. And it came with this.

**Dave Jones:** Look, RFID blocking technology to assist you in protecting your credit cards against identity theft. Sandler now uses data blocking technology concealed within this bag or backpack is an RFID protective fabric inside the credit card section helps block illegal scanning devices and assists the prevention of data and identity theft.

**Dave Jones:** Fantastic. But does it actually work? Let's test it. Now, let's just talk briefly about the RFID technology in here. There's actually a coil all the way around the card in here that actually does not, contrary to popular belief, act as an antenna cuz this is not an RF base system.

**Dave Jones:** It's It's term RFID is a little bit deceptive in this case. It actually works like a transformer. And if we have a look at another card here, we can actually see the coil inside there.

**Dave Jones:** Check it out. It It It'll go around like that. The chip will be embedded in there somewhere. Not exactly sure where it is. It doesn't matter. But you can see that there's a couple of turns going around in there somewhere.

**Dave Jones:** And what it's doing is acting as a transformer like this. Let's go to Dave CAD. So, this is the receiver part of it here. This could be the phone like we're going to use today.

**Dave Jones:** It could be a legitimate device at the supermarket or on the bus that you want to tap and go and pay with. Or it can be a uh scamming uh skimming device that people can uh walk by you and actually uh once if they get close enough, then they can actually um potentially uh get your card details and actually do a transaction on your card.

**Dave Jones:** They can't actually get your credit card information, but they can do an actual uh transaction. As I said, up to the value of $100. Anyway, this is the receiver like this.

**Dave Jones:** And the receiver generates a constant 13 or packets of 13.56 MHz uh sine wave. And it's a transformer coupled system. The coil inside the credit card actually forms the secondary of a transformer here.

**Dave Jones:** So, even though it's called RFID because it RF is used in some other uh variants of it, it's actually a magnetic field uh traditional transformer coupled like this. And the chip inside your credit card here actually gets power from this coil.

**Dave Jones:** So, once you get these two close enough, there's a little uh rectifier in there. This is grossly uh simplified, but hey, this is basically how it works. It generates uh power for the chip, and then the chip can drive a transistor which then can modulate the load on the secondary side.

**Dave Jones:** And that will reflect back due to the action, the magnetic fields, you can actually get the modulation on here and it'll send, as we'll see in a minute, it'll send like a packet of 13.56 MHz data like this and then if this chip, if the protocol's right and everything matches up, then this will use a transistor to put a load across the coil and modulate it.

**Dave Jones:** And for the ISO 1443 protocol, which we're talking about here, which is used in these types of modern credit cards, then it's going to modulate that amplitude modulate it at a frequency of 847.5 kHz and then the reader can read back that data and they can communicate and transfer information.

**Dave Jones:** Easy. But the important thing to note here is this is not an RF system. These are not antennas. This is a transformer. It works on magnetic fields instead of an RF field.

**Dave Jones:** So you can take a modern smartphone and use this as an NFC reader. They've got NFC capability built in. 13.56 MHz. There are different frequencies for different RFID systems, but the credit cards use 13.56 and that's what the modern smartphones do.

**Dave Jones:** At least I'm not aware of any smartphones that do the other frequencies, but we can use this as just an app from Research Lab Hagenberg. It's just a free app you can get to read the information from these cards.

**Dave Jones:** So we can put our tag in there and it's just reading tag. Doesn't take a minute. New tag detected and we've and it we've got it. We've read all the information that we can from this card.

**Dave Jones:** Of course, I can't get the money from it cuz I don't have the ability to do transactions, but hey, criminals can potentially do this. So I won't go into the tag information.

**Dave Jones:** It might reveal something about my card here, but um anyway, it's you know, you can get like the hex dump data out of the card and everything else. And you don't actually have to have them touching.

**Dave Jones:** You can actually have them a distance apart, but there is a limit to how far you can have them apart due to the transformer action losses cuz it's a pretty poor transformer.

**Dave Jones:** It's an air-cored. So, the idea behind these uh bags you can buy and you can get wallets as well with this RFID protection technology. And does it work? Well, I actually don't necessarily doubt it cuz it's not hugely hard to actually shield against this.

**Dave Jones:** But as I said, it's not a Faraday cage uh issue. It's not an RF issue, it's a magnetic field issue. So, you know, ideally you'd want what's called mu-metal which actually uh shields out uh magnetic fields.

**Dave Jones:** Now, take something like this die-cast aluminum box for example. You're used to using these to shield your electronics and stuff from uh EMI, right? Now, these are quite effective at RF uh of course, but for magnetic fields, not so much.

**Dave Jones:** But really, the problem is with magnetic fields, um die-cast aluminum like this or aluminum foil or anything else, um really is uh you know, pretty decent at high frequency uh stuff.

**Dave Jones:** But at low frequency, low frequency magnetic fields like down in the kilohertz and things like that, these aren't really effective against magnetic fields. But the good news is is that uh these things operate at 13.56 megahertz.

**Dave Jones:** So, something like this die-cast box or some aluminum foil is going to work a treat at those high frequencies. Even though at low frequencies, even something this thick would actually be pretty useless at shielding magnetic fields.

**Dave Jones:** So, let's not muck around, let's try it. Let's get our credit card inside the outer sleeve of this bag and scanned it. There we go. No problems whatsoever. This bag does not work in the outer pocket, but it doesn't claim to.

**Dave Jones:** If we go back and read the fine print, there's a protective fabric inside the credit card section. So, only the credit card section. So, the rest of the bag, if you've got this card inside your wallet inside the bag, it's not specifically inside the credit card section, eh, you're not protected at all.

**Dave Jones:** And you'll see inside this bag, it looks kind of like magneticky, but uh if you put your your credit card inside any part of this inside here or this outer pocket, as we saw, then it does absolutely nothing apart from a physical distance uh thing getting extra losses in the transformer.

**Dave Jones:** You've got to actually put the card inside here, and I'm not sure if you can hear that, but it feels different. It feels like there's some metal foil or something inside this section.

**Dave Jones:** So, let's whack our card in there, shall we? And we'll try and read it. Here we go. Or the outside of the bag like this, and you'll see that it doesn't scan at all.

**Dave Jones:** So, it works. Um and that's not terribly, you know, surprising. There's nothing magical about this, but look, if I put inside this other pocket over here and try and read it, bingo, it's going through multiple layers, no problems, of this bag and right through there.

**Dave Jones:** So, it only works if you put it inside the section like this. So, that might protect you against a wimpy little uh phone like this, but what if uh the criminals have some, you know, super high-power uh transmitter {slash} uh receiver that can, you know, generate a bigger magnetic field and read data back?

**Dave Jones:** Well, how effective might this be? Well, we can actually do it get some uh quantitative measurements with a uh near field uh H probe. These are called because it's a magnetic field.

**Dave Jones:** This is not an electric field probe, it's a magnetic field. You've seen these in my videos before. Uh it's a dead giveaway it's a magnetic field because you can see the coil there.

**Dave Jones:** And we can actually stick this in between the credit card and here, and we can pick up the magnetic field, and we'll be able to see it on the scope.

**Dave Jones:** Beauty. And of course, you don't need to buy one of these fancy-pantsy expensive uh shielding handbags or wallets or whatever, um, you can just use Alfoil like this and this is a common trick you see on the internet.

**Dave Jones:** Uh, so let's see if we can read that tag under there. No, we can't. Just a single layer of Alfoil like that is more than enough. If I take that away now, bingo, we'll read it, no problems whatsoever.

**Dave Jones:** So just a single layer of Alfoil is enough to attenuate that even though the magnetic field, as I'll show you in a minute, is actually still getting through there.

**Dave Jones:** It attenuated it enough to actually cause a problem. And there is a bit of a myth going around that if you have two credit cards in your wallet in close proximity or back-to-back like this that they'll cancel out and they'll get, you know, conflict and you won't be able to, uh, read the data out of it and you'll be completely safe.

**Dave Jones:** You don't need any magnetic shielding whatsoever. Well, that's not really true because the, uh, ISO standard 14443, which, uh, determines the protocol and everything to do with, uh, this RFID, uh, technology actually has an anti-collision thing as part of the protocol for both type A and type B cards.

**Dave Jones:** So we can, hopefully, it might it it could make an idiot It's going to make a fool out of me. No, there we go. New tag detected. Okay. So you can actually get a point where they sort of do interfere with each other and it causes a problem, but you can still you can still do it.

**Dave Jones:** You saw we could actually There we go. We can get it to read that no problem. So that really isn't protected. That myth busted. Okay, so let's use our, uh, H field pro which goes from, uh, you know, basically kilohertz up to, uh, several gigahertz.

**Dave Jones:** So it should easily be able to read our 13.56 megahertz. Let's put that on the back here and we'll see that, uh, when you've got our, uh, NFC enabled on your phone, it's reading all the time, periodically actually sending out these packets like this, and trying to wake up the card that's in any card that's in proximity to it, and then looking and sending out a code to enable it, and

**Dave Jones:** then looking for modulation coming back. And if we single shot capture that and go in here, you'll see that this is basically bingo, whoop, there it is, 13.55, 13.56 MHz.

**Dave Jones:** That's our carrier frequency, and it's sinusoidal. All right, put our card behind our phone here, and watch what happens. I'm going to put it in there. Bingo, you should have seen some modulation there.

**Dave Jones:** So, let's see if we can capture that. And you'll notice that it's actually continually stayed on now that that card is in the field. If we take it away, bam, it goes back like that.

**Dave Jones:** Now, I've captured some data here, and you can see that before this trigger point here, here's our 13.56 MHz, it's actually the look, it actually uh it goes down to zero.

**Dave Jones:** This is the receiver, or in this case the transmitter, actually doing that. And we've got different types of data. If we go over here and have a look, we can see this is the return data coming from the card itself, and this is the amplitude modulated data.

**Dave Jones:** We can go in here and have a squeeze at that. There it is. It's just amplitude modulated, so that is the credit card actually modulating that, turning on the transistor, loading down the coil, and modulating that data back.

**Dave Jones:** At what frequency? Well, let's measure it. And bingo, using our X cursors there, we can get 847.46 kHz. That's exactly what I said the modulation frequency was before. So, yep, the ISO standard is exactly as it says.

**Dave Jones:** Now, if we have a look at the distance between the card and the phone like this, then we can actually I might 200 mV per division, we'll we to see the amplitude difference?

**Dave Jones:** I'll go down like this. I've got that I don't know, a fair distance away. Will we be able to get something? Yep, and it's lower amplitude, of course, but even at that sort of distance, um you know, there's still something there.

**Dave Jones:** It's not enough to actually connect to the card, uh but hey, if you had a more powerful uh reader, you know, if you're a criminal, you had a more powerful reader, you're trying to um skim cards and things like that, you can do it at a greater distance.

**Dave Jones:** Okay, so let's try the Al foil now. Okay, so I'm down at uh 10 millivolts per division. The absolute value doesn't matter, it's just relative to uh 200 millivolts per division we were at before.

**Dave Jones:** And yeah, I'm able to, you know, get something, but if I take away the Al foil, of course, then whammo, we're completely off scale now. There we go. All right, so I've got my credit card inside the shielded thing.

**Dave Jones:** I'll whack my uh probe in there, and we'll give that a whirl. Yeah, we're still getting something at 50 millivolts per division, but, you know, it's it's really right down there.

**Dave Jones:** You'd have to have a super powerful uh you know, uh transmitter side to actually, you know, uh generate in a much larger magnetic field than this one's capable of to actually get that, I suspect.

**Dave Jones:** But, it it's probably not 100% secure, but, you know, I I think it's going to be good enough. I I think these sorts of uh shielded handbags and wallets will actually do what they claim.

**Dave Jones:** And if you're wondering about the uh diecast alloy box, then yep, that's at uh 2 millivolts per division. There's just Oh, did we get something? No, that was just me mucking around.

**Dave Jones:** Yeah, that's going to be pretty effective, as you'd expect, but uh not 100% effective against magnetic fields. But, in the case of the uh amount of field we're talking about with the RFID here at that frequency, then yeah, these things do work.

**Dave Jones:** Okay, just for kicks, I'm going to see if we can capture the uh increase in magnetic field as we get closer. So, I'll single shot capture that. And I'll bring it in.

**Dave Jones:** Don't like our chances. But uh oh yeah, that's quite reasonable. There we go. We started here and we can see getting bigger and bigger, but it wasn't close enough uh to actually uh capture the data like, you know, to sync and do the protocol and uh talk to the card and get the data before it got, you know, fairly close like an inch away or something like that.

**Dave Jones:** So, there you go. I hope you found that interesting. And uh whether or not you believe that, you know, you're really at threat just walking around with your unexposed uh credit cards in your wallet and things like that.

**Dave Jones:** You know, the odds are ridiculously low that somebody's going to uh skim you or something like that. But, you know, they don't necessarily have to walk through you. They could uh set it up in a door frame, for example.

**Dave Jones:** Yeah, as you walk through, they could get you cuz you can couple the magnetic field uh like that as you walk through. And there's many other ways uh to do it, but they have to do a transaction.

**Dave Jones:** It's not like the money just magically vanishes uh from your account. You know, it's got to be a uh transaction and things like that. So, yeah, not a 100% secure uh technology, but hey, confirmed uh these bags and presumably the wallets, they've probably just got alfoil in them anyway.

**Dave Jones:** And alfoil does quite a reasonable job. Just a single layer of alfoil can actually uh protect your cards pretty good. So, yeah, uh if you're paranoid about these things, don't wear it on your head.

**Dave Jones:** Just stick it in your wallet. Catch you next time. Hi, it's teardown Tuesday again. Got something a little bit different. It's one of these Braun electric toothbrushes. You've seen them.

**Dave Jones:** It sits on one of these chargers, wireless uh power transfer to charge the internal battery. We crack it open and check it out. Not only what's inside here, but what's inside the charger as well.

**Dave Jones:** Let's take a look. Could be interesting. There you go. It drops down and if you remove another one, it drops down again. But actually,
