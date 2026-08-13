---
video_id: Yky9yQwZALM
title: Shift Cryptosecurity BitBox02 Crypto Hardware Wallet
url: https://www.youtube.com/watch?v=Yky9yQwZALM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 32, "3": 47, "4": 68, "5": 84, "6": 103, "7": 114, "8": 136, "9": 152, "10": 171, "11": 186, "12": 200, "13": 219, "14": 237, "15": 252, "16": 273, "17": 292, "18": 313, "19": 334, "20": 349, "21": 367, "22": 382, "23": 400, "24": 418, "25": 430, "26": 451, "27": 472, "28": 496, "29": 511, "30": 526, "31": 544, "32": 565, "33": 589, "34": 610, "35": 631, "36": 646, "37": 664, "38": 688, "39": 709, "40": 724, "41": 742, "42": 760, "43": 781, "44": 796, "45": 808, "46": 829, "47": 850, "48": 868, "49": 889, "50": 910, "51": 934, "52": 958, "53": 970, "54": 991, "55": 1003, "56": 1021, "57": 1036, "58": 1051, "59": 1066, "60": 1084, "61": 1099, "62": 1114, "63": 1135, "64": 1153, "65": 1174, "66": 1198, "67": 1216, "68": 1234, "69": 1249, "70": 1270, "71": 1285, "72": 1300}
---

**Dave Jones:** Hi, just a quick one. I'm taking a look at the BitBox-02 crypto hardware wallet. I've had this for quite some time. They sent it to me. It's done by Shift Cryptocurrency. There it is, Shift Cryptocurrency. And yeah, it's a little USB-C hardware crypto wallet.

**Dave Jones:** So I thought we'd take a look at it. And one of the designers of this, Alex, actually posted on the EEVblog forum after seeing my latest video saying, hey, we've actually released the Bohlmann schematic and stuff for this. So yeah, here it is here.

**Dave Jones:** So I'll link it in down below. So let's have a look at the schematic. I haven't actually looked at this yet. So wait a quick, quick quiz. I'm using a different microphone today. If I sound different, something's screwed up. They're obviously using Altium there.

**Dave Jones:** And oh, look at that. There you go. There's the 3D jobby for it. And I think I've looked at the original BitBox. I haven't looked at the 02 though. So we're going to run through just installing it. So they use an ATS-A. Is that one of the secure ones?

**Dave Jones:** I don't know what type of security is actually built into the processor. I don't know whether it's like, you know, physical layer security, anti-glitch featuring and all that. So as in physical security, like the die, so you can't drill through the top of the chip and probe and all that sort of stuff.

**Dave Jones:** So yeah, I think that uses A, but it's basically, yeah, it's that. It's got some I2C memory here. And that's just input protection on the USB. And yeah, that's all there is. There's a touch, a slidy touch sensor on the side of this thing, apparently.

**Dave Jones:** Can we see that on the PCB? Yeah, can we see that? Yeah, okay. So they're using that contact, that one, that one, and that one. And they're using the castellations. I'm not sure why they've got castellations. Maybe that's part of the case or something.

**Dave Jones:** But well, they're not actually castellations. They're just routed out bits. It's only a castellation if you actually have like the half-moon thing in there. But obviously, yeah, they're using those side bits as capacitive sensors. So that's kind of cool on each side. Oh, by the way, somebody posted on the eVBlog forum that the Tresor Model-T I was looking at,

**Dave Jones:** it actually uses blind vias in it. It's like, why? I don't know. But apparently it does. So yeah, they've done some work on the eVBlog forum. Somebody took a couple of hours to tidy it all up, and they've still got a long way to go, apparently.

**Dave Jones:** So anyway, cool. There you go. So this is Anne the Bomb here. Let's have a look. There you go. That's nice. Description and mouse number as well. Very nice. Excellent. So I don't know how open-sourcy this thing is, but they've got it there.

**Dave Jones:** I don't know what license or whether or not it's classed as open-source hardware. I'm not sure what the deal is. But anyway, so let's give it a go. All it does is, so this is the box you get. You just get a USB cable thing, an adapter, and an SD card.

**Dave Jones:** There is an SD card in the back of this. But no little sheet to write down your crypto seed. So that's all you get. So how does it work? I don't know. There's no crypto seed. Oh, sorry. Damn. I've got to turn my light on.

**Dave Jones:** There you go. I don't know. Yeah, everything broke. I was trying out another system before, and all my microphone and everything's busted. So yeah, I might go for a hardware solution to all this soon. Anyway, I'm checking it out. Anyway, let's plug it in, shall we?

**Dave Jones:** So here's their app over here. Apparently you can get it for your Google Play. But bugger that. Never do this on your phone. Never. Ever. Using MyARCHE. It supports MyEtherWallet, which is good. Anyway, I've downloaded the app. Here it is. Insert the micro SD card.

**Dave Jones:** Done it. Follow the app instructions. Install the device password on your SD card. I don't know. Anyway, let's go next. Bitbox. Yep. Run Bitbox app. Welcome to the Bitbox app. How can I get a device? Blah, blah, blah. Ah, we want to set it up.

**Dave Jones:** Close guide. Please connect your device. Okay. Plug it in. Comes with a USB-C to USB-C cable and a little USB-A adapter as well. Hopefully I've got a lead long enough. Oh, yeah, just. Bootloader. Okay. Upgrade firmware now. Yeah, I've had it for quite some time.

**Dave Jones:** So we'll upgrade that. Advanced. What's in advanced settings? Show the firmware hash every time it's started. Oh, okay. That's interesting. So somebody's been fiddling with it, maybe? Oh, that's nice. That's nice. I like that. Upgrading. That's a nice bit of integration. I really like that.

**Dave Jones:** Wow, and it's almost linear, too. I hate non-linear bar graphs. Yeah, that's really slick. Come on, you can do it. Upgrade successful. Continuing. Three, two, one. This hardware will self-destruct in five seconds. Please connect your device. Please tap the device for the O2.

**Dave Jones:** Yeah, we've got the O2. Yes, we do. Please tap the device. Verify the pairing code. That is correct. Multi-edition, whatever that is. Great. I want to set up a new bitbox. Create wallet. Restore from your microSD card. Okay, restore from recovery words. Okay.

**Dave Jones:** Yeah, we recommend you proceed in a secure location. Take their advice. By that, it means that nobody's watching. You've got no spyware installed on your computer and all that sort of jazz. So, yeah, create wallet. So I assume they'll give us a paper copy as well,

**Dave Jones:** but then we can more conveniently just back up from the SD card if we want. Confirm on the device. Set password. Okay, here's where we set the password. You are able to flip the screen on this thing, unfortunately. Can't do it right now, I don't think.

**Dave Jones:** Yeah, it's got, as you can see in the video there, that's pretty cool. It's got all the letters. You can do letter-number combinations, so it's not just a number. The interface is kind of okay. Once you're used to it, it seems to work alright.

**Dave Jones:** It's not too bad, given that it's got three switches or four positions. It was a top and bottom, but it's only allowing three. But no, it's doing business. Got to repeat the password, which is sensible, even though it's annoying. I'm going to get one shot at setting it up,

**Dave Jones:** so make sure you verify. Success! Okay, it's locked. It's now unlocked. It's shown a little padlock thing. You will now create a backup on your microSD card. I should store my backup in a secure location. Backup is not password-protected. Anyone with access can access my board.

**Dave Jones:** If I lose or damage my Bitbox, the only way to recover my funds is to restore from my backup. If I lose my backup and Bitbox, then my funds will be lost. I should not insert my microSD card backup into a computer, phone, printer, or any other device other than a Bitbox, too.

**Dave Jones:** Yes, very important. Don't store it on the cloud. Don't store it in your Google account or whatever it is. Make multiple copies on a non-internet connected machine if you're super paranoid. And then keep five copies just in very secure places. Because you really have to treat

**Dave Jones:** presumably the SD card and your recovery sheet like fiat cash. You've got to treat it like cash because anyone with that code, they don't need this hardware device. If they've got your recovery sheet or in this case your recovery SD card, then they can just confirm today's date.

**Dave Jones:** That date is correct. Backup created. Show recovery words. I would never ever rely on just the SD card as the backup for this. You want it on paper. Paper can get burnt, fade away, or do whatever. Solutions for this have stainless steel cards

**Dave Jones:** and you can scribe or punch out numbers and they survive house fires and things like that, which is very good. Even if you're safe, even if you've got a fire rated safe, you don't want to have paper in there. Your paper sheet, and that's your own backup.

**Dave Jones:** You will be presented with 24 recovery words from which form a backup. Write them down on paper. Do not steal them digitally or take pictures of it. Do not say the words out loud because someone could be listening. This backup is not password protected.

**Dave Jones:** Otherwise you'll be asked to confirm each word. Oh, I've got an unlock device again. Geez, they're being ultra secure. Alright, yes, my super secret seed is on here so I'll get some paper and I'll record all these down. And as with all these BIP type recovery seeds

**Dave Jones:** they're all like plain text words. They're all plain English words so I really think that's awesome. Whoever invented that is just fantastic. It's really difficult to write down the words wrong. Even if you've got the exact spelling wrong, it'll automatically correct you when you go to re-enter them.

**Dave Jones:** Ah, this is interesting. I will actually tell you one of my words because that's, you know, it's fine. On the screen at the moment I can... Why did it just vanish? Did it make a bad connection? What the heck? I was in the process of writing down my words.

**Dave Jones:** I shuffled in my sheet. Did I generate some static? What? It just reset itself. Something's locked up. Well that sucks. I was just in the process of writing down my words. No, something's gone wrong. I'll have to re-power. I like it when it powers up.

**Dave Jones:** That's nice. Password again. I want my recovery seed. Did I only get one chance at that? If I only got one chance at that, then I'm screwed. Because I only got like five, six words in. Anyway, if I don't get a chance to do this again

**Dave Jones:** what I was going to say is one of my words was it showed three words on the screen. The one next to it, it said plane. Which I thought, okay, it's plane. But when you shift over one more and it puts that word in the middle

**Dave Jones:** it becomes from plane, it becomes planet. So yeah, the word it cut off the T and it looked like it was a genuine word. So just be careful with that. Maybe they shouldn't allow that at all. Maybe they shouldn't display it. But then it's good to know which is the previous word

**Dave Jones:** so I can understand why they've done that. Manage device, show recovery words. No, I'm good to go. I've got to unlock it again. Wrong password, I've got nine tries left. I've got my words back. Now it's going to ask me to confirm each word.

**Dave Jones:** This could take a while. Right, here we go. So it's giving me multiple selections. So like five to select from each one. So I'm going to go through all 24 and select one of five. Do I have to do this? I'm not sure if I actually have to do this.

**Dave Jones:** I'm pretty sure I got it right. I just cycled it through a second time and I am right. I don't think there's any need to do it. Do you really want to cancel recovery words? Yep, pretty much good to go. I think I'm good to go.

**Dave Jones:** Let's resize Dave head there. Now I have a backup on this. I'll check that later on a non-interwebs connected computer to make sure it's got the stuff on it. So that is my backup. And then we can just do our crypto stuff. It only supports Bitcoin, Litecoin, and

**Dave Jones:** Ethereum. That's disappointing. Does it support tokens under the... I'm not sure it supports tokens under the Ethereum thing. I think that's it. That could be it. This is not a proper review or anything. I'm just setting this up for the first time. Anyway, manage device, firmware's up to date,

**Dave Jones:** optional passphrase, generate random number. That's just for kicks. Generate the following 256-bit random numbers. So using the random number generator built into the secure chip. It's got its own little random number generator. It has to. They're generally pretty good. I mean they're not

**Dave Jones:** ideal, but they're pretty good random number generators. It's really, you know, it's an art and science to do a proper hardware random number generator. I don't know if you can even prove it. Like prove? Can you actually prove that there's a genuine, like true randomness or something?

**Dave Jones:** It's like, yeah, it's a real you know, many PhD papers have been written on that. Currencies? Oh yeah, I want Aussie. I don't want any of that Euro rubbish. Yankee bucks? I don't even think I want Yankee bucks. Oh, I might have both.

**Dave Jones:** Aha! Yes, here's the Ethereum. Yep, it supports basic attention tokens, wrapped Bitcoin and a few others. Okay, so it doesn't support everything, but it's got a few. That's all right. If you're into your tethers and whatnot. Yeah, it's not comprehensive. Would have been nice to have, you know, more than that.

**Dave Jones:** I mean, everyone's talking about Dogecoin these days, aren't they? Anyway, Bitcoin, Litecoin. I'm sure it works. Okay, so I will receive Litecoin. Your address. What? That's, what is that? It's not generated anything. That's a nothing burger. What is that QR code? Anyway, change to compatible address.

**Dave Jones:** Segwit. Show and verify full address on device. Okay. You can scroll it. I do like the scrollies. It's pretty good. Nice interface for such a compact thing. So that was a good choice. That looks correct. See, why can't I copy that? Show and verify full address on device.

**Dave Jones:** I did. Okay, so we can copy that. Okay, so only a few. Right. But then it doesn't show up here. Not sure what the deal is. Anyway, I'll send myself some Litecoin. Okay, so I'll send myself 0.1 Litecoin, which is worth about 23, 24 bucks.

**Dave Jones:** Send in. Invalid address. Please check carefully and try again. Coins sent to the wrong address cannot be recovered. Show and verify full address on device. Change to compatible address. Segwit. Okay. Okay. Show and verify full address. I will copy that. Okay. I didn't know we needed a different compatible address.

**Dave Jones:** 0.1 Bitcoin. Done. Confirm send. Yep. Okay, it looks like my send-in wallet, yeah, just didn't support, it needed the Segwit address. Okay, I've got an email. Confirm my withdrawal. That just happens to be part of the wallet I'm using at the moment. So, we'll see how long that takes to come through.

**Dave Jones:** So, like a refresh. There we go. We got it. That didn't take long. Like a minute, two minutes tops or whatever. It's still pending, but it's showing up. So, there you go. 0.1 Litecoin. 23.7 Aussie bucks. Beautiful. It works. There you go. So that's the Bitbox02 digital crypto hardware wallet.

**Dave Jones:** It's a bit disappointing that they didn't include a code sheet for it. That would have been nice. So, I've just written it down on the card that came with it. Yeah, they didn't even put a spot to write it on that card here.

**Dave Jones:** Got an FCC compliance card though. And I got some stickers. But that's about it. So, the Bitcoin sticker. I'll use that. Thank you very much. And then it's got numbers as well. So, if you've got multiple ones, you're going to, I don't know why they stopped putting numbers on the others,

**Dave Jones:** but yeah, you can have multiple devices and you can identify them. Like, I've got multiple devices of the same one, and yeah, I could have to put a thing on them to actually identify them. So, there you go. That's sweet. It worked. No buggers.

**Dave Jones:** Everything just worked pretty seamlessly, like the firmware update and everything worked pretty seamlessly. I do like the capacitive touch thing on it. It's all right. Although it did crash once in there. I don't know what the heck happened there. Weird. And I think it might have reset itself again at one point.

**Dave Jones:** Not sure what the deal is. But anyway, it's interesting that they give you the SD card slot even though you don't need that done enough. It's possible to do firmware upgrades via that. But that's used to store the info. So yeah, don't store this recovery on your cloud or whatever.

**Dave Jones:** And yeah, have the paper recovery seed is always the best. Because then you don't actually have to restore it into here. If you've got the paper recovery seed, you can just restore it to any hardware device, any vendor's device that supports that particular seed,

**Dave Jones:** or a software wallet, or anything. You can just very quickly restore your wallet to anything. But, of course, this one is probably, I don't know, probably incompatible with the BitBox O2. So don't rely just on this. But yeah, it's kind of cool. And it's open source as well.

**Dave Jones:** There you go. Digikey and Mouserbox, they are doing it a bit better than Trezor anyway. Although Trezor did that for their original one. I don't know why the Model T is different. I think they just couldn't be bothered, because I'm probably the only one who's ever bothered them about it.

**Dave Jones:** I can remember contacting them about seeds when it first came out. I said, hey, where's all the open source files? And they said, oh yeah, we'll get around to it. Which is fair enough. They're spending all their time on what they should, which is the firmware and software side of things.

**Dave Jones:** Because hardware is like, even if everything was available, and it was turnkey, who would actually make their own Trezor or BitBox or whatever? Hardly anyone. You can round it down to zero. So yeah, so many nerds like me, that would bother. So there you go.

**Dave Jones:** The BitBox O2. Geez, have I had it for that long? Maybe. I love that they've got an x-ray. Check it out. That's pretty cool. Yeah, I like that. And yeah, and the finger. Capacitive touch. That's a nice interface. Oh, that was a separate chip, was it?

**Dave Jones:** Oh, I missed that. Was it a separate secure chip? Oh yeah, sorry, I thought that was an I2C interface. Like memory or something. But no, sorry, that's the secure device. Okay, but the Atmel secure, I think the AT, oh no, sorry, I was mixing that up.

**Dave Jones:** That's the ATSAM 851, is it? Yeah, that's just, yeah, that's not, that is not the secure device. It's the ATEC C508. There you go. There it is. That's a microchip jobby. Did they develop that or did they buy someone who had the secure tech?

**Dave Jones:** I don't know. But yeah, first crypto device to integrate. Elliptic curve Diffie-Hellman key arrangement. For all you Diffie-Hellman fanboys out there. Which make it easy to add confidentiality in digital systems and other things. Nodes, grown, home automation, industrial to highly secure, asymmetric authentication.

**Dave Jones:** It's got all the pillars. You want all the pillars? Signature, elliptic curve digital signature algorithm. Wow, sounds impressive. Elliptic curve cryptography. Yeah, that sounds pretty schmick, doesn't it? Although, yeah, it's all happening inside the chip. And all the secure stuff's happening inside the chip.

**Dave Jones:** So it's not like it's going over the I2C bus. I'm sure that's not the actual case. So cryptographic coprocessor with secure hardware-based key storage, because that would be pointless if you just sent it over the I2C bus. It's all done on the chip.

**Dave Jones:** Two high-endurance monotonic counters. Wow. Guaranteed unique 72-bit serial number. There you go. It's got a FIPS random number generator. I don't know what that is, but all you FIPS fanboys certainly would. 10k of eSquared problem memory for key certificates data. That's pretty generous.

**Dave Jones:** 10k. Oh, that's bits. None of that byte rubbish. Works on 2 to 5.5 volts, 150 nanoamps sleep current. Okay, that's anti-cloning, message security. Yeah, I don't know what the physical 3-lead contact... You can get a 3-leaded package? What? What? I don't get it.

**Dave Jones:** 3-lead contact top view. Yeah, I don't know how it does its anti-counterfeiting thing, protect firmware. Yeah, I don't know, like, if it's got physical... I'm sure it's got, like, physical die protection and glitch protection and all sorts of stuff, but yeah, anyway, that's interesting.

**Dave Jones:** So there you go, that's the BitBox02. That was fairly seamless, took a little bit to set it up. You know, they're always a little bit fiddly with the interfaces and stuff like that, but yeah, the slider's pretty good. Not too shabby. I'll link it in down below, BitBox02.

**Dave Jones:** Catch you next time.
