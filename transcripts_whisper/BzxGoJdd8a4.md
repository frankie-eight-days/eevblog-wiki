---
video_id: BzxGoJdd8a4
title: EEVblog #1006 - Trezor Bitcoin Hardware Wallet Teardown
url: https://www.youtube.com/watch?v=BzxGoJdd8a4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 38, "3": 55, "4": 76, "5": 94, "6": 110, "7": 130, "8": 149, "9": 167, "10": 180, "11": 200, "12": 221, "13": 235, "14": 255, "15": 273, "16": 288, "17": 304, "18": 324, "19": 343, "20": 360, "21": 379, "22": 394, "23": 416, "24": 430, "25": 448, "26": 468, "27": 483, "28": 498, "29": 518, "30": 533, "31": 550, "32": 566, "33": 581, "34": 598, "35": 616, "36": 635, "37": 651, "38": 668, "39": 689, "40": 709, "41": 723, "42": 742, "43": 757, "44": 775, "45": 794, "46": 821, "47": 839, "48": 859, "49": 874, "50": 896, "51": 917, "52": 935, "53": 953, "54": 970, "55": 987, "56": 1001, "57": 1018, "58": 1037, "59": 1053, "60": 1068, "61": 1102, "62": 1119, "63": 1137, "64": 1157, "65": 1180, "66": 1205, "67": 1226, "68": 1247, "69": 1265, "70": 1288, "71": 1305, "72": 1327, "73": 1349, "74": 1364, "75": 1380, "76": 1393, "77": 1407, "78": 1423, "79": 1440, "80": 1458, "81": 1476, "82": 1492, "83": 1509, "84": 1529, "85": 1542, "86": 1560, "87": 1578, "88": 1591, "89": 1607, "90": 1625, "91": 1644, "92": 1660}
---

**Dave Jones:** Hi, we're going to do a teardown of this Trezor hardware Bitcoin wallet. And thanks to the viewer who sent this into the mailbag, they specifically wanted me to do a teardown of this puppy to see, like, how physically secure and everything else it is.

**Dave Jones:** So, that should be very interesting. Let's take a look. But first of all, what is a hardware wallet? Well, I won't get into what cryptocurrencies are and everything like that. You've no doubt heard of Bitcoin if you're watching this video. Well, this is a way to store your Bitcoins or other handles, Ethereum and Litecoin and various others.

**Dave Jones:** It's a hardware wallet, physically stored on this little device which you plug in to your micro USB here. And the advantages of a hardware wallet over, like, your traditional software wallet or keeping on a USB stick or everything else is that they're encrypted on here.

**Dave Jones:** They're physically secure. You can't get hacked by keyloggers, malware. You can use them on any computer anywhere. You know, nobody can actually recover these unless they have the pin number on the actual device to do it. So, yeah, these are, like, really offer quite a lot of advantages over a software wallet

**Dave Jones:** or just store it on your hard drive, a USB stick or one of those online wallets, for example. So even if this hardware wallet gets stolen, they're not going to be able to steal your coins in there because it's pin number protected. So unless they coerced you into handing over your pin number and getting them that way,

**Dave Jones:** they should be physically secure. It can accept up to a nine-digit pin. And every time you incorrectly try the pin number, the wait time period goes up by a factor of two. So it's practically impossible to guess the pin number on this thing.

**Dave Jones:** But, hey, can you extract the pin number from it? Can you, you know, get something out? Can you physically hardware hack it? Well, that's what we might try and have a little look at in the teardown anyway. And if it does get stolen, you can actually recover them another way using a recovery seed, a recovery process.

**Dave Jones:** So it's really about the secure pin number in this thing is what people need to physically extract your coins from your hardware wallet. So as long as you keep your pin secure, it should be pretty physically impossible to actually crack these things. That's the plan anyway.

**Dave Jones:** Now this is manufactured by Satoshi Labs. It's one of the most, if not the most, popular hardware wallet on the market. I believe it was one of the first on the market. And it's had a few security issues in the past. Like somebody was able to do a side channel analysis, power analysis attack on this thing,

**Dave Jones:** and actually recover the private key out of the thing. But, yeah, that's been fixed in firmware a couple of years back. So apparently it has not been hacked since. And the other good thing about this is that all the software in here is open source.

**Dave Jones:** So you can actually see, go in there, the community can go in there and analyze exactly what's going on inside this thing. And the private keys are kept secure by Satoshi Labs. So as long as they're physically secure, everything should be fine. And this supports a remote firmware upgrade over the USB.

**Dave Jones:** But you can't just like flash new firmware in there, hacked firmware or whatever. Because the process of doing that will actually wipe your coins. So you can do a firmware upgrade, like a proper firmware upgrade, without losing your coins. But putting in hacked firmware, that's not a sign that doesn't meet the private key at Satoshi Labs.

**Dave Jones:** Then it will wipe all your coins in there. So you can't hack the thing by just doing some sort of firmware hack or firmware upgrade. So what I'm interested in, and what the viewer who sent it in is interested in, is actually what's physically inside this thing.

**Dave Jones:** Is there any extra hardware security protection and stuff like that. There's a few things that I would like to see inside this. Like if I was designing a hardware wallet like this, that could be designed to store an unlimited number of bitcoins. This hardware wallet could store billions of dollars worth of bitcoins.

**Dave Jones:** It could physically do that. So people trust these things to store their bitcoins. It could be worth a phenomenal amount these days. Especially if you bought them years ago or something like that, when they were worth a pittance. And now they're a couple of thousand bucks a bitcoin.

**Dave Jones:** Significant value tied up inside the hardware security inside these things. So if I was designing this thing, just to be sure, there's some measures that I would take in these. And you see these in pinpads and things like that. We've done teardowns of pinpads before,

**Dave Jones:** and some other channels have done pinpad teardowns. If you don't know what a pinpad is, one of those FPOST electronic point-of-sale transaction terminals that you get in shops and banks and things like that, where you put your credit card in. They have lots of hardware security measures in there.

**Dave Jones:** You might pot the products, like a hard potting compound in there. I'd be doing that for physical security. And then you might have some anti-tamper stuff inside these things. So if you try and crack the thing open, then it might just erase the keys if you physically do that.

**Dave Jones:** Or you can actually get physically secure main processors. You can buy them where they have like a physical mesh over the top of the die and other physical security measures. So even if you dissolve the chip in like sulfuric acid and try to get like an electron microscope or other device

**Dave Jones:** to try and actually read the individual data directly off the die and stuff like that, that can actually physically be prevented with the use of these physically secure chips that you can buy. So I'm just curious if it uses one of those. Are there any tamper protection if you open the thing?

**Dave Jones:** It looks to be ultrasonically, you know, heat-welded or something like that. So it looks like we're going to have to Dremel this thing open. But anyway, let's just take a look at doing a side-channel power analysis attack. Because someone actually has done this in the past.

**Dave Jones:** But I think I mentioned before, they have actually fixed that in a firmware update. The hardware may have changed in the couple of years since that hardware side-channel attack was revealed. But that's all fixed now apparently. But let's just have a quick squeeze.

**Dave Jones:** Okay, so let's just do some basic side-channel power line analysis. What I've got is my Roden Schwartz scope here, 10-bit ADC. I've got high-res average mode on, 20-meg sample memory depth maximum. And I'm breaking into the ground line of the USB here. I'm just breaking this out into a 10-ohm current sensor resistor here.

**Dave Jones:** Got that on the scope. Be careful where you put your ground on this. Don't put it on the positive. I've done a whole video on how not to blow up your oscilloscope when probing USB. Stuff like this. So just be very careful with that if you're trying to do something like this.

**Dave Jones:** And we've got it connected. And the good thing is we can get a decent voltage drop across this thing. And it still works. So this is actually fairly tolerant of, you know, inserting resistors in the power line like this to actually get quite a decent voltage.

**Dave Jones:** In this case, 100 millivolts per division. So we can see that it draws about 40 milliamps or so. So we're actually getting quite a decent signal level there. So we've got one second per division triggered at this point over here. And at the same time that I triggered it, roughly, I connected to the wallet on the website.

**Dave Jones:** So, yeah, it basically was sitting there doing nothing, and then I connected. And sure enough, five seconds later, which matched up with where the information popped up on the screen, took about five seconds to connect and do its business, we see some anomalies here apart from the usual noise.

**Dave Jones:** So let me zoom in. So we'll go into the center here where all this regular stuff is. And as you can see, it's very periodic. But we can get some really good detail on there. And that stuff in there is about 5.3 kilohertz.

**Dave Jones:** It's very periodic. Everything is very periodic. You know, you can, like, scroll all the way through this, and it is identical. So this is your regular processor operations. I can't find any anomalies in there. Really, it's just your regular periodic stuff. It's updating the display and doing your regular processor loops.

**Dave Jones:** I can't find anything that is out of the ordinary there. So I think they actually have fixed that in the firmware. So the first thing we actually get to is this over here. And we can actually, because this is actually lower, you can see it's a lower current here,

**Dave Jones:** we can actually, it's probably, like, turned off the display or blanking, doing something like that. And, look, there's just not enough time in there for it to, you know, for us to extract any usable data. So I think they've hidden that quite well.

**Dave Jones:** I mean, this was a problem. This has been attacked before, and then the information was given to Trezor, and sure enough, like, in the next firmware update, they fixed it. And there might have even been hardware changes since this. This was a couple of years back, so who knows?

**Dave Jones:** They might have tweaked the hardware a little bit as well since then. But this brand new one that I've got, there's just not enough information in there based on the previous power line analysis attack, where they got the private key out of it.

**Dave Jones:** It's just not, there's not enough room. So I think they've fixed it. It's just, yeah, we can actually measure stuff in there, so it'd be, but it looks like they've hidden it really well. So I can't see us extracting anything from that. And we can actually use an E-field probe as well.

**Dave Jones:** I've tried a small H-field probe, and I'm not getting any magnetic coupling over that. But if we put this in certain places over the back, we can actually get a coupling, not via the ground, but just via the PCB inside there, which haven't taken apart, so I don't know the layout yet.

**Dave Jones:** But yeah, we are able to pick something up. Let me show you. Whoa, hang on. I was just capturing some E-field probe stuff, and look, I got some major packets here. I was not connecting via the hardware wallet, but I was doing some 200 millisecond per division stuff,

**Dave Jones:** and look, we've got some, much like we've really got some periodic stuff in there, and you can see it matches the E-field probe here, which you might have a look at in a minute, but you can actually see some huge variability in there.

**Dave Jones:** So is that, but once again, that is very periodic. I don't see any information. Was that like updating the display or something like that? But I don't see any actual data in there, and I was not connecting to the wallet at the times.

**Dave Jones:** And I've tried some E-field and H-field probe stuff, and with the E-field probe, I've been able to kind of get some correlation on here, but no real extra information on there. So yeah, like there's nothing doing with the EMC analysis at all. So whilst I would like to see, you know,

**Dave Jones:** elimination of any possible side-channel attack via the power line like this, I mean, you can do that in the hardware. They obviously haven't bothered, or they've made some tweaks since the hack was originally discovered, and it looks like they've fixed it, but still, you can see some processor stuff,

**Dave Jones:** you can see some periodic interrupts and, you know, stuff like that happening, but I can't see any data. Doesn't mean it's not in there, but yeah, it looks like they've hidden it really well. And what I've got here is it actually starting up from the sleep state,

**Dave Jones:** so I click the trigger and click the website over here, and then we can see it actually power on. And yeah, we do have some stuff down there, but once again, it's like really not enough information to decode. So there's, yeah, there's nothing doing there at all.

**Dave Jones:** One really nice secure feature I love about the Trezor is that when you do a transaction, it pops up with a pin that you have to enter, and it's not the same every time. You have to actually have a look down on the device itself

**Dave Jones:** to actually see it randomizes that pin location, so it's not the same. That is really quite neat. So even if somebody had a keylogger on your computer, for example, yeah, they could get where you clicked on that keypad, of course, and they would get, of course, the number of digits,

**Dave Jones:** but they don't know because it's a randomized order like this, so they can't even steal your pin number with a keylogger. Fantastic. And then when you're confirming a transaction, it actually pops up with the actual Bitcoin address on the device itself, so you've got to make sure that matches what's on the screen.

**Dave Jones:** Terrific security, I love it. They've thought of everything. And we're in. Well, there you go. I'm very surprised just to find the bare PCB. Nothing looks potted at all. We should be able to... Looks like we didn't even get the chip number off that.

**Dave Jones:** We'll have a good look at the PCB shortly. We've got some gunk behind the micro-USB connector there. Is that for some extra... just for some extra physical strength? Not entirely sure. Anyway, I'm very surprised that nothing's potted in this thing. That would have been my first port of call if I was designing this,

**Dave Jones:** if anything, just to make it a bit more physically robust. I mean, this thing, they say it's... Oh, actually, that could be for water ingress, maybe. Is that hard or is that soft? Yeah, it's a soft... it's a soft compound. So yeah, that looks like it might be a physical water...

**Dave Jones:** The thing's... I don't think it's waterproof, but it's water-resistant or something like that. So yeah, but they could have done that better to make it entirely waterproof. But I would have potted the thing. That would have been, just as a matter of course,

**Dave Jones:** physically encapsulated into a hard epoxy potting compound over the whole thing. Just to make it physically difficult to access. Anyway, let's see if it still works. Shall we? It still works. Look at that. Right, and I can confirm that that does hook up to my wallet on the computer,

**Dave Jones:** like the web wallet up there. I can see all my information. I can see that it still has my 0.004 bitcoins in there. So it's got like currently $9.89 worth of bitcoins still stuck inside that thing. But that's the thing. I'm very surprised at that.

**Dave Jones:** For something that's designed to protect your valuable bitcoins, which could be worth potentially millions of dollars. I mean, you wouldn't trust it maybe to one device, but still, right? I would have potted this thing, because anyone can just hack that open like I did

**Dave Jones:** and get physical access to the pins of the chip, and then you can start hacking away. Whether or not it's possible to actually, you know, recover the pin from this thing, I don't know. It would require a huge amount of effort probably to try and do that.

**Dave Jones:** But the first line of defense is physical security, and it does not have any. So, and it still works after you open it. So there's no ambient light sensor or microswitch or anything else that any other sort of like anti-physical protection tamper in there

**Dave Jones:** that prevents you from accessing chips. But the problem with that, unlike say the pin pads that I mentioned earlier, the FPOS terminals, they will actually have a, the keys inside will be battery-backed up SRAM, static RAM. So once you get in, and it's actually,

**Dave Jones:** they'll have a separate little micro in there that's actually detecting whether or not it's open. And as soon as, say, an ambient light sensor trips or a microswitch, like a contact, physical contact breaks or something like that to know someone's gone in there,

**Dave Jones:** then it'll just wipe the memory. Whereas this doesn't have any battery or anything like that. That's why, okay, if it doesn't have, you know, some sort of tamper detection that automatically wipes it or whatever, then that's fine, but at least physically prevent the access.

**Dave Jones:** You know, I would have done that, just as a matter of course, really. So what I thought I'd do is just thermally cycle this just to see how it physically survives. And of course, proper thermal cycle, long-term thermal cycle testing is a very time-consuming and complicated process,

**Dave Jones:** but I'm just going to do it the time-poor engineer's way. Use the electronic freezer spray and the heat gun and just cycle it through. I won't do it to the OLED display because that's not what is important because you could actually, the good thing about it not being pot

**Dave Jones:** is that you could actually replace the OLED display if that failed, but then of course you could buy a new wallet as well and re-seed the thing and use your recovery seed that way. But we want to do the chip, and yeah, just for kicks.

**Dave Jones:** Why not? Let's go. And I'm doing that at about 100 degrees, so, you know, not hot enough to melt the solder. Thermal cycled that a couple of times, and I re-checked by connecting to it, and my bitcoins are still there. So, yeah, like, we could go to town.

**Dave Jones:** I might do it a few more times just for kicks, but I don't expect any issues. It's just a bog-standard micro. You could, of course, get the industrial temperature rated one, of course, just for extra, you know, I would pay extra to get the higher rated, more qualified device.

**Dave Jones:** But, meh. All right, let's have a look at this under the Togano microscope. The first thing you notice is the shine on there. That's a conformal coating. That is to help the water protection, moisture protection, stuff like that. So they've tried to make it a bit more reliable.

**Dave Jones:** You can see where they've mastered off around the tactile switches there. So, you know, that's a reasonable moisture protection. So that's a nice little measure. It's not a security measure at all. It's just purely for water ingress. And it's basically just one arm chip on a board with a USB.

**Dave Jones:** That's basically it. This would be the JTAG interface. We could follow the traces down to there, but it's one arm. There won't be anything under the LCD there. The OLED display there is physically down on the board. So there's nothing else. There's just the one arm chip.

**Dave Jones:** So it's basically just a software solution, which is fine. Which is, you know, basically all that's required. And we can actually get in there. And it looks like there's that. And ST part 32F205RET6. Let's go to the data sheet. But I'm pretty sure this is not a physically secure processor.

**Dave Jones:** So that's a bit... it's just a regular Joblogs processor. I'm a little bit disappointed in that. Peel off our gunk there. There we go. Got access to our pins. And of course those test pads on the bottom, they're for production bed of nails testing.

**Dave Jones:** So we could, like... This thing is easily probable. But it's all a matter of the software security side, as I said. So that's where all the magic happens. So I guess it doesn't need to be any fancier than this. But I just maybe would have used just a secure processor

**Dave Jones:** as a matter of course. Because if you get in there and dissolve away all the epoxy case with a sulfuric acid, then you can get access to the die. And technically, if you didn't damage it during that process, which is possible, you could get in there with an electron microscope

**Dave Jones:** or other means and physically see, and physically extract the, presumably, the pin number out of it. But that'd be, you know, real advanced, pretty advanced skills. But maybe it's possible. But the interesting thing about this is even if you could dissolve the chip in sulfuric acid, get access in there,

**Dave Jones:** recover the pin, the security, you could reflash the programming fuse in there, load some firmware on, which, you know, some hacked firmware, which could extract it or whatnot, you know, spoof it into extracting the pin code out of the thing and get it working that way.

**Dave Jones:** All that takes significant time, whereas if you, once you realize your Tresor hardware wallet has been stolen, you can simply change the recovery seed key for the thing, which would effectively should present and prevent them actually doing that. You know, it basically renders the thing physically useless

**Dave Jones:** once you've changed that recovery seed. So, yeah, I, you know, it's probably adequate. I guess my main concerns are, like, adequate from a hacker security point of view. My main concerns would be just the physical reliability of the wallet. I would have, okay, they've done some

**Dave Jones:** conformal coding in here, which is okay to prevent moisture ingress and stuff like that. Is there a, you know, a little bit there which is exposed and moisture can get in under the chip and like, whatnot. I just physically would have potted the whole thing.

**Dave Jones:** Like, that's not a huge extra cost. I would have done that as a matter of course, really. And there's not a huge amount of capacitance or diode protection in here to prevent that power line attack. But as we saw, you know, there's not real,

**Dave Jones:** there doesn't seem to be anything to see there, because they've spoofed that, fixed it in software, which is, you know, entirely possible. So the fact that, you know, stuff does get back out, like, you know, you can see the processor cycles, the interrupt

**Dave Jones:** cycles inside this thing and other stuff is leaking back out through the power line. It's not a big deal, as long as you know about that fact and you can compensate for that in software. So you can, the software's open source, so you can go see the changes

**Dave Jones:** they made since this was originally, had that power line hacking. You can see what, you know, anti-spoofing stuff they've done there. It's all, it'll all be documented in the source code, surely. So there you have it. That's the Trezor hardware wallet from Satoshi Labs.

**Dave Jones:** And it's just a microcontroller with lots of software magic. And that's all there is to it. There's no extra hardware security, which I'm a little bit surprised at, but it, you know, it's not a real issue, because it's all about the software security.

**Dave Jones:** They really have thought about this thing, and apart from the power line attack, which they have fixed, that I don't believe, please correct me in the comments down below if you know of another successful hack attempt on these things to get the PIN and recover the bitcoins out of it.

**Dave Jones:** Either hardware or software, please let us know. Yes, we could hook up the programmer on there to get in there, but we're not, they've thought about this, okay? They're, right, it's all about the firmware in there is signed via the secret key at, the private key at Satoshi Labs,

**Dave Jones:** and if you try and do anything to the firmware, it's just going to erase those keys. So, you know, there's pretty much going to be no attack. I'm not going to say it's impossible, but I haven't heard of anyone doing it, and I'm not going to try and do it, because that's not my expertise,

**Dave Jones:** like, you know, software hacking and STMicro, for example, or any sort of cryptographic hacking and stuff like that. I'll leave it up to those more experienced, and I'm sure a lot of people have tried, and there's only been the one successful power line attempt as far as I know.

**Dave Jones:** So, it seems pretty solid. Although it just occurred to me, what if you actually hooked up the ST-ARM programmer to the programming port on this thing? I've got one here, it costs like, you know, tens of dollars, they're dirt cheap. And what if you could actually get in there and modify the eSquared Prom content

**Dave Jones:** where it actually stores that pin enable thing? So if you get, like, the pin incorrect, for example, it will store it in the eSquared Prom that you got it wrong, and then the next time you power it up, you could, like, it reads that,

**Dave Jones:** and then it determines, right, you've got to wait a longer period, and then an exponentially longer period as you do more attempts. But if you could somehow automate the power cycle process, and also find and reset that eSquared Prom contents where it actually stores that,

**Dave Jones:** maybe you could have an infinite, well, a very fast process for actually systematically attacking the pin and running through all the pin number contents. Although maybe, you know, you can only write to an eSquared Prom so many times, so it might die before you get to the pin number,

**Dave Jones:** especially if it's nine digits long, for example. But you never know. I, you know, I thought that maybe there might be something there, but yeah, I'd have to set up this and find where it's actually stored in there and actually try it, and it's a lot of effort.

**Dave Jones:** Maybe for a second video, or maybe someone else out there can give it a try, or maybe they already have, and it's not an issue. Anyway, that just came to mind. But I think, like, this thing should have a version, or, you know, maybe you can pay more for a, you know, a premium version

**Dave Jones:** that is just, like, instead of having the plastic case on the thing, actually encase the entire thing in epoxy potting compound, and it becomes the case. It becomes one big solid monolithic block with just the cut-out window for the LCD and the switches.

**Dave Jones:** The switches could even be done capacitively coupled, or something like that, perhaps. But yeah, I would, you know, I'd like to see a more physically robust device than this. If I was, you know, trusting huge sums of bitcoins on this thing, then, you know, I'd want some.

**Dave Jones:** I'd love, like to pay for a more premium physically robust device. But the security, I think's, you know, they're probably as good as you're going to get software-wise. So I hope you enjoyed that video and found it interesting and useful. If you did, please give it a big thumbs up.

**Dave Jones:** Catch you next time. Thanks for watching.
