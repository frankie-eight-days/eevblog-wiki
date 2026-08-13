---
video_id: uOOGXORqsqQ
title: Trezor Safe 5 Bitcoin Crypo Hardware Wallet
url: https://www.youtube.com/watch?v=uOOGXORqsqQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 53, "4": 69, "5": 85, "6": 101, "7": 117, "8": 133, "9": 153, "10": 169, "11": 185, "12": 201, "13": 221, "14": 237, "15": 257, "16": 273, "17": 289, "18": 309, "19": 325, "20": 341, "21": 361, "22": 385, "23": 405, "24": 429, "25": 445, "26": 461, "27": 481, "28": 497, "29": 513, "30": 533, "31": 553, "32": 573, "33": 589, "34": 605, "35": 621, "36": 637, "37": 653, "38": 669, "39": 685, "40": 697, "41": 713, "42": 729, "43": 745, "44": 761, "45": 781, "46": 801, "47": 821, "48": 837, "49": 849, "50": 865, "51": 881, "52": 893, "53": 909, "54": 921, "55": 937, "56": 953, "57": 969}
---

**Dave Jones:** Hi, it's crypto hardware wallet time, because you know I'm into the cryptos, and I've used the Trezor wallets. I've got two Model Ts, I've also had an original Model 1 or something it was called, but all my cryptos kept on two Trezor Model Ts,

**Dave Jones:** but you can never have too many crypto hardware wallets, so don't put your eggs all in the one basket. So I thought I'd get a couple more Trezor hardware wallets, but they don't seem to make the Model T anymore, so I got this new Safe 5

**Dave Jones:** model. Basically the same size and shape as the Model RT here, except it's, like, sleeker, more polished. The major difference really is that the old Model T just used a regular microcontroller to store the secure stuff. So, eh, as long as you've got it in your possession, it's fine, but you know,

**Dave Jones:** somebody gets a hold of it, potentially not as secure as if you had a proper secure element. So you can see it's got an EAL6 plus secure element protection. So it's got a dedicated secure chip in there, which has physical which will have physical security.

**Dave Jones:** I'm not sure which actual chip. It's open source, so go look at the schematics. But yeah, the separate physical chip which holds the secure element will actually have physical barriers on the die as well. So if you kind of, like, etch it off

**Dave Jones:** or you try and laser it off or whatever, it's got more better protection. Anyway, can't buy the Model 1 anymore as far as I know, so I'm going to do this new Safe 5. I've also got the much, much cheaper Safe 3. It's exactly the same, except it doesn't

**Dave Jones:** have a touchy-feely screen on it. It's just got two buttons instead. And that one doesn't have the secure element in it. But it is way, way cheaper. So, eh, I'm going to try out both. Now the thing about crypto hardware wallets is you don't want to be caught out by a man

**Dave Jones:** in the middle attack, i.e. a supply chain attack. So you've got to buy it directly from the Trezor website. Mine came from the Czech Republic, and there it is, made in the EU. And I really like the secure case on it. It's got, like, a security zip

**Dave Jones:** seal on it. It comes shrink-wrapped, security zip seal. And then inside, ah, there's a seal. Get it? And then it also comes with a security foil sticker around the USB so you know somebody hasn't shoved something up the clacker in transit. So when you peel that off, it's got the void

**Dave Jones:** thing on there. So I've already peeled that off. So thumbs up for the, ah, like, security measures on the Trezor. But they've always been very good. But yeah, do not buy them on eBay or from any other supplier whatsoever. Order them directly from the

**Dave Jones:** Trezor website. Same thing goes for any other brand crypto hardware wallet. And you get your 20-key wallet backup. You get two of those here. So just a paper one. You can get, like, third-party metal ones. And you can inscribe and they can survive a

**Dave Jones:** nuclear blast and all that sort of jazz. So here we go. I've plugged it in, and it's popped up on the screen there. Trezor.io start. But I've already installed the software on here. So device security check. My device was bought from the official Trezor shop or trusted

**Dave Jones:** reseller. Tick. My hologram was intact and untampered with. Tick. The device package was intact and untampered with. Tick. Or thumbs. So set up my Trezor. Takes 15 minutes. I wonder if you click I have doubts. They probably go big spiel about, you know, how you can get

**Dave Jones:** a man-in-the-middle attack or something like that. Installing firmware. Your Trezor is shipped without firmware. Install the latest firmware in order to use your device safely for Bitcoin only. We recommend no. I want all of them. So install firmware 2.83. There you go. Fixed.

**Dave Jones:** Fixed persistent word. When going to previous word, your recovery process added missing info about remaining shares in Super Shamir recovery. I don't know what that is. I have to investigate that. But yeah, they're always updating the software. And I've only ever had one issue with it, and that was

**Dave Jones:** recently, but it was fixed. Seems like it was fixed in this latest version. It wouldn't detect my wallet. My existing Model T wallets panicked for a bit, actually. But I just went back to a previous version of the Trezor suite software. I'm running this on Windows

**Dave Jones:** 10. And it worked fine, so I knew there was nothing wrong with my crypto or my wallet. It was just a bug. And sure enough, the release for this latest Trezor suite version one of the bug fixes is it fixed a detection thing.

**Dave Jones:** Some sort of obscure detection bug, which I obviously have. But no, I've checked it and it works fine. So, beauty. So install firmware. Let's go. Oop. Yep. Installing firmware. It says installing firmware. I'll get back to you. And it looks like it's done.

**Dave Jones:** Beauty. I'll just show you the github hardware here. And yep, I've got the symbol on there. There you go. And yes, in the hardware on the githubs, they've got the safe 5. So they added that. RISC schematics. Is that all they got? Yep, there you go.

**Dave Jones:** They've got the schematic. So there you go. That's the Trezor. So let's, can we zoom in on this? Here you go. So this is the big-ass micro they've got in here. Where's the part number? Trezor in the Czech Republic. So there you go.

**Dave Jones:** They've got all the protection on the bus there. Ah, there it is. STM32U585. There you go. So the other Trezors just store the secure element inside the micro. But this one here, and that looks like the SD card, micro SD card slot there on the side.

**Dave Jones:** They've got a FET up there for the switch in the power. And where's our secure Optega Trust-M. There you go. So there's our secure element. It's just got I2C interface and Trust, Optega Trust-M. There you go. Looks like it's an Infineon jobby. Easiest way to add security

**Dave Jones:** to your existing Internet of Things design. Grown. Certified tamper-resistant hardware. Yeah, as I said. So that's the standard, I believe. Not currently up on all the physical hardware standards, but yes, it would have. So all this stuff I'm sure is very impressive to all you crypto

**Dave Jones:** aficionados. Oh yeah, the NIST curves up to P512. Absolutely. Oh, they specified a lifetime. That's interesting. 20 years for industrial. Hmm. There you go, data sheet. Does it have any info on like the physical hardware security aspects? I don't know. Yeah, maybe they don't want to tell you, but yeah, it'll have like embedded mesh over the die

**Dave Jones:** and all sorts of stuff like that that actually prevents you from physically probing the die if you happen to get the case off and stuff like that. So, yep. There you go. Cool bananas. So let's continue, shall we? Let's check your device. This check must do a

**Dave Jones:** step to ensure your device's reliability and integrity. Confirm chip inside is genuine from Trezor. Interesting. Once your device has been given a clean bill of health. Okay. Let's see, I'm pretty sure I got a genuine one. Ordered it straight from the website. Came from the Czech Republic.

**Dave Jones:** You can trust the Czech Republic. Authenticate device it says. Allow connected computer to confirm your Trezor 5 is genuine and safe. Yes. Swipe up. Yes. Tap to confirm. Ooh, it had, I think I felt some tactile feedback there. Must have a little vibrator in it.

**Dave Jones:** Don't you love it when your crypto vibrates? Safe 5 is ready to go. Beauty. Continue on Trezor. Know your Trezor. Learn how to use and navigate this device with ease. Swipe up. Swipe down to move through screens. Yep. Learn how to use and navigate.

**Dave Jones:** Blah blah blah. Hold to exit tutorial. Ooh, it vibrates. Create a new wallet. I don't want to recover my old ones. I still want to use my old ones. So, let's create a new wallet. Default type. Backup. Single share backup generates a single set of 20 words.

**Dave Jones:** This backup is upgradable to multi-share. Ah, multi-shared backup. Look at this. It generates multiple 20 word shares to recover your wallet. Set a minimum recovery number, then distribute shares to trusted individuals or hide them securely. I don't think, correct me if I'm wrong, but this was not

**Dave Jones:** an option in the previous Trezors. Or maybe it was and I just forget. But what's going on here is that basically, if we choose this option, which I won't, we can generate multiple 20 word security lists. Okay, one is already ridiculously secure. But if you want to be ridiculously, ridiculously secure

**Dave Jones:** ludicrous levels of security, then you can say, okay, I want to generate 5 different 20 word keyword lists, and to get back into the wallet, to recover it, you need all 5. You can't just use one. You need all 5. So, yeah, I'm not going to do that.

**Dave Jones:** So I'm just going to do a single share. Default. So I'm going to create a new wallet. Confirm on Trezor. By continuing, you agree to the terms and conditions. Yep. Hold to confirm. Continue holding. I'm doing that. Processing. 2 seconds left. 1 second

**Dave Jones:** left. Done. Swipe. Wallet created. Okay. Our wallet's been created. It's swiped up. We should get our word list now. And backup needed, it says on the screen. Sorry if you can't see that, but anyway, backup needed. You don't want to skip backup. You want your

**Dave Jones:** backup. Continue to backup. Your wallet lets your recovery your funds in case of your wallet backup. Never take it, yes. Okay, so he's just ticking these. Never take a picture of your backup or store it digitally. Don't take a photo with your shoe phone and then keep it

**Dave Jones:** in your bloody cloud. Don't even store it on your shoe phone. No. If you want to, physically write out another one. Don't take a photocopy, because photocopiers can have like, they store the images on the hard drive internally. So you can come and get to that way.

**Dave Jones:** So, yeah, just write out another one. And then, once you've written them all out, make sure that you actually check them. There's a verify feature in the Trezor suite software that allows you to verify your list. Store your wallet backup securely and never

**Dave Jones:** share it with anyone. Yep, create wallet backup. Trezor will display your wallet backup. Write it down accurately and store securely. It's the only way to recover your funds. Yep, never put your backup anywhere digital. Yep. Write the following 20 words in order and your wallet backup card words may

**Dave Jones:** repeat. Swipe up. Okay, I'm not going to tell you. You're not going to see any of this, so I'll even stop recording, just in case. Okay, once it did that, I've got my 20 words here, and I'm going to verify those. It puts up

**Dave Jones:** what it does is it just chooses a random one, like, you know, number 7, and then it gives you 3 options, and you have to pick the correct one, and it will basically go through, verify it, make sure you haven't done anything dumb.

**Dave Jones:** But the good thing is, they're English words, so that really, you know, they're pretty hard to goof up unless you get them in the wrong order. Okay, we've backed up the wallet physically on the paper, continue to pin, and we're going to set a physical hardware pin that just

**Dave Jones:** allows you to, you know, so that you've got an extra layer of security there, so that someone physically gets this, and they, you know, and they don't have any other way to, like, physically hack the thing, then, which is really difficult, then they will have to get past

**Dave Jones:** the pin, like this. So, yeah. So you can skip it, but I would not recommend it. All of my hardware wallets have pins on them. And don't put something stupid like 1234, or your postcode, or you know, something dumb like that. And, or somewhere, something that

**Dave Jones:** you've reused somewhere else. Don't do it. Turn on pin protection, enter new pin. I will. Ooh, this keyboard's bigger than the old Trezor one. This keyboard looks bigger than the old Trezor Model RT, because I had a real problem with that. I don't have big fingers, but even I was struggling

**Dave Jones:** to, you know, get the right numbers on there. Processing, two seconds, one second, left, done. Beautiful. Pin protection turned on. Swipe up. Now we can activate the coins that we want to use on this. Myself, not a recommendation at all, but myself, I hold Bitcoin, Ethereum,

**Dave Jones:** I hold Cardano, I hold a little bit of Solana, Ripple, oh, maybe, might have some Ethereum Classic somewhere, but Litecoin, Bitcoin Cash, and yeah, that's it. But I'll install those, no worries. Okay, complete setup. Go to Trezor Suite. Ooh, you can edit the name.

**Dave Jones:** And boom, I am in, and of course, because this is a brand new wallet, I don't have any crypto. Aww. But it's trying to find it. It's trying to find my assets. I really like the Trezor interface. It works really well. I won't go through it, but

**Dave Jones:** yeah, these wallets have all got zippity-doo-dah here. But once I transfer some in, they will show up here, and it just works really well. I like how it works. I won't go into receiving and sending and all that sort of stuff. Trust me, the Trezor Suite

**Dave Jones:** is really nice. I like it. And I even use it for Cardano staking as well, because I stake my Cardano, and that works fantastically as well. So there you have it. There's the new Trezor Safe 5. The Safe 3 will be exactly the same, except it's not touchscreen.

**Dave Jones:** It'll just have two buttons here, so the user interface experience is slightly different. It has a screen on it to tell you what to do. So yeah, it's not as nice as a touchscreen, but it does cost a lot less. But this doesn't have the physical

**Dave Jones:** hardware security in it, but neither did my original Model Ts, which I still love and trust. No worry. So I guess they don't make a touchscreen model without the secure element in it anymore. You've got to pony up for the Safe 5, which is considerably more expensive than the Safe

**Dave Jones:** 3. But something like the Safe 3 is all you need as a basic hardware wallet. I'm just getting the Safe 5 because I can, and I'm really into this sort of stuff. So yeah, I like it. Trezors, as I said, the only crypto hardware wallet that I actually use.

**Dave Jones:** I have a few others, but like Ledges and other ones. But yeah, I don't use them. I use and trust the Trezor ones. So there you go. If you like the video, give it a big thumbs up. And the anti-crypto people are going to flame

**Dave Jones:** below. Go ahead. Care factor? Zero. Oh, by the way, I used to accept crypto on the EEVLOG store back when it was on WooCommerce, but now I've moved it to Shopify, and I've had a few issues with trying to actually get the crypto working again.

**Dave Jones:** But I'm working on it. But at the moment, sorry you can't buy me meters with crypto. Although, you know, manually email me, hey Dave, I want to buy a meter with crypto. No worries, I'll send you an address, and you can just do it, and we can do it manually.

**Dave Jones:** The old-fashioned way. And I prefer the dark mode. Anyway, there you have it. It goes without saying, if you're using a software wallet for your crypto, don't do that. If you're keeping your crypto on an exchange, don't do that. Unless you like trading all the time.

**Dave Jones:** Yeah, don't do that. Keep your crypto safe on a hardware wallet like this. Because the exchanges get hacked. That's happened countless times. So only transfer from your hardware wallet to the exchange when you actually want to sell them, and get your fiat back

**Dave Jones:** to do whatever with. So yeah. Otherwise, no. Hardware wallets are the way to go. Anyway, catch you next time.
