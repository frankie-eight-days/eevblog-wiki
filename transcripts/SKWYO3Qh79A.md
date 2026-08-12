---
video_id: SKWYO3Qh79A
title: EEVblog #1048 - Ledger Nano S Crypto Hardware Wallet
url: https://www.youtube.com/watch?v=SKWYO3Qh79A
source: youtube-asr
---

**Dave Jones:** Hi, we're going to take a look at the Ledger Nano S cryptocurrency hardware wallet click. I don't know here somewhere or at the end of the video if you want to see the Trezor teardown and I'll kind of do

**Dave Jones:** a bit of a comparison with the Trezor. Now, this is actually a cheaper solution the Ledger Nano S for a hardware wallet than the Trezor. The Trezor is about 170 Australian dollars. The Ledger Nano S is about 119 Australian dollars. It's about

**Dave Jones:** 105 US versus like 70 US or something like that. But prices vary greatly on these things. And by the way, you should only buy these things from the official suppliers. Don't buy it from some one hung low shop on eBay. That's for sure.

**Dave Jones:** But anyway, let's take a look at this. The look and feel of this thing. This is the first time I've actually had it. It's uh not sure what type of plastic that is. Is it some sort of Delran? I'm not sure, but I expected

**Dave Jones:** this one to feel a bit better cuz the Trezor, one of the main complaints I had about it is that it was quite flimsy. Yes, that's not normally there. I've actually dremeled open this case and then I've used my soldering iron to

**Dave Jones:** close it again. It still works a treat. So, it's fine. But yeah, it's just it's just flimsy. It's not like I want like a proper I don't know like a diecast or machined alloy case or something like that. But yeah, the Ledger Nano S, it

**Dave Jones:** doesn't feel any better. I'm not a fan of these flippy things. Some people are. Anyway, they've both got the micro USB there on them. So, that's one of my fears is that you know, if I plug this in and out too much, I use it too much,

**Dave Jones:** I'm going to wear and tear on the micro USB socket there. Anyway, we've got two buttons on the side, a little OLED screen presumably on there. It's smaller than the Trezor. The Trezor is already hard enough to read that thing. Anyway,

**Dave Jones:** um hardware cryptocurrency wallets, so these are the places that you want to store your coins. Be they Bitcoins or altcoins, you want to store them on a hardware wallet cuz it's the most secure location possible. The advantage of a

**Dave Jones:** hardware wallet is that uh when you actually set it up and you generate your seed key, your private seed key, which we'll see here. Let's actually do a little bit of an unboxing. Tada! And we get the requisite uh USB

**Dave Jones:** cables and whatnot and that's it, a few little lanyards. Whoop-di-do. Um let's open this. Welcome. And we should have a recovery card sheet. Did you notice there is no anti-tampering sticker on this box? Yes, I did. There it was uh

**Dave Jones:** wrapped, it was like shrink-wrapped, but there was no security sticker. Why? Because this one actually has a separate uh uh secure chip inside there that does a check, some sort of check, some presumably uh to check the integrity of

**Dave Jones:** the Ledger device's internal software each time it's powered on. So, that's an advantage of the Ledger Nano S over the uh Trezor. The but the Trezor is completely open-source hardware and software. So, not only can you make your

**Dave Jones:** own version of this if you're ultra paranoid, you can actually get the schematics and you lay in the PCB files, you can get your own manufactured. All the firmware, everything is open-source. This one is not. I don't believe there's

**Dave Jones:** a schematic for this um at all and it's some of it is open-source, the applications and the interface are open-source, but uh they do not release the firmware as open-source. And one of the reasons for that is that the uh

**Dave Jones:** cryptographic uh chip, it uses a two two-chip solution. There's a regular micro in here just like the Trezor and uh but it uses a separate cryptographic uh chip which has hardware various hardware protections built into the die to stop, you know, reverse engineering

**Dave Jones:** penetration and things like that. But, yes, the cryptographic chip in here is actually you can't buy it you and you can't get the data sheet for it. It's an under NDA, a non-disclosure agreement. Um that's what why Trezor specifically

**Dave Jones:** didn't use uh one of those chips is cuz they wanted this to be completely open source and it is. So, anyone can come along and check the integrity of this. The Ledger Nano S, not so much. So, for

**Dave Jones:** the ultra paranoid out there, the Trezor is a better bet. But, hey, like there's nothing wrong with the Ledger Nano S, let me tell you. So, anyway, the advantage of a hardware wallet like this is that uh not only are

**Dave Jones:** you in physical possession of it, uh the key is stored in there. When you set this up, uh you're setting up the seed key, which is everything. Let's have a look in the back here. We should get a

**Dave Jones:** sheet to store it. Yep, there it is. To store our 24-word recovery uh phrase on here. And anyone who has these list of 24 uh words, they're not just random characters, they're actually words, I'll show you in a minute. They

**Dave Jones:** don't need your hardware wallet. You keep it in your wallet and somebody steals your wallet, like your physical actual wallet that you put in your pants, then uh or down your dacks if you're super paranoid with one of those

**Dave Jones:** RFID shields in it. Anyway, I've done a video on that. Um which I might link in at the end for those uh tin foil hat people. So, anyone who has has access to these uh keys, which we'll write down, doesn't need this at

**Dave Jones:** all to steal your coins. They can just recover it anywhere. So, actually keeping this secure with your keywords on is more important than keeping this secure. You can lose either of these and if they don't have your PIN code or

**Dave Jones:** password to get in, then they're screwed, right? But, if they get access to this recovery seed, they can can just recover that to an even another hardware device or recover it to a software wallet that uh in the

**Dave Jones:** case of both the Ledger and the Trezor, there's 24 words here. So, any wallet, software or hardware that supports the BIP39 protocol BIP39/44 can use this recovery seed and you can get your coins back. So, don't fear if

**Dave Jones:** one of these fails. A lot of people ask, "Well, what happens if I lose my hardware wallet or it breaks or the connector breaks or whatever like that?" Well, no big deal. As long as you've got this, you can recover. So, the advantage

**Dave Jones:** of these hardware wallets is that the seed is actually generated on this physical hardware itself, which can't be intercepted by the USB. It doesn't travel over the USB. So, if your computer's infected with spyware or malware or whatever where possible, it

**Dave Jones:** cannot read the seed out of this while you're setting it up. So, unless someone is physically looking over your shoulder at these key words when you install it or they've got a copy of this somehow, then it's completely secure. The problem

**Dave Jones:** with setting up a wallet, a software wallet on your phone or your PC is that you can have spyware, malware on there which don't visit those porn sites, kiddies. I'm telling you. They'll steal your cryptocurrency seed from you quicker than you can set

**Dave Jones:** the thing up, I suspect. Or they'll steal it now and hack you later. Anyway, you don't know that your PC or your phone is secure when it could have a screen grabber in there. It could have a key tracker or whatever and it can log

**Dave Jones:** the seeds. So, yeah, you don't want that. That's the advantage of the hardware wallet. You can physically set it up completely isolated from the outside world. Beauty. So, anyway, it doesn't feel as great as I suspected. Is that Can I pop the back off there? Is

**Dave Jones:** that ultrasonically welded? I don't know. I might try and get my knife in there. Anyway, we'll we'll do a teardown of this thing. But yeah, it's just not as uh bulky and secure. Give it a bit of a

**Dave Jones:** twist test there. I can twist. There's a bit of twist in that. Not as much as the Trezor. The Trezor, you know, if you put it in your back pocket, you could really uh get in trouble with that if you sat on it. Could squash the

**Dave Jones:** damn thing. Anyway, maybe it's a bit more robust than Trezor a little bit. But I expected more robustness inside like a hardware wallet. I would happily pay for a premium version of any of these where I could actually uh you

**Dave Jones:** know, like get a more physically robust uh unit. And I'm thinking about uh designing my own version of the uh Trezor because it is open source hardware into a more robust version. But they got the new Model T coming out very

**Dave Jones:** shortly. I have uh pre-ordered one. It's a bit more expensive than this one. Um so, hopefully I'll do a video on that soon. So, anyway, let's uh configure the device. We've got to go to the website. Don't All we do is plug

**Dave Jones:** it in and I'm sure it'll tell us what we need to do. And write down our recovery phrase cuz that's the first step to setting up your hardware wallet. All right, for you ultra tin foil hat people, I'm not going to hook it up the

**Dave Jones:** computer. I'm going to power it from an external battery pack. But as I said, you don't have to do this because the recovery seed it's going to generate here uh does not ever travel over the USB. It's generated internally and displayed

**Dave Jones:** internally. Anyway, oh jeez, that's a tiny tiny little piss ant screen, isn't it? Welcome. Oh jeez, I can my old eyes I can barely read that. Welcome. Press both buttons to begin. Jeez, this is like it really if you

**Dave Jones:** haven't got great eyesight, these things are terrible. Use left right buttons to change values and interact and navigate through multiple first choice lists. Yeah, great. Okay, configure as new device. It'll gives you different options to either configure a new device

**Dave Jones:** or recover an existing device, I believe, or whatever. So, anyway, we're setting up the new device. Choose a PIN code. So, you can actually go up and down, and this one actually allows you to enter a PIN code of zero, which the

**Dave Jones:** Trezor doesn't do, uh by the way. So, you can uh do that and then just press both buttons, and then that's put it in. So, it's going to ask us to confirm our PIN code. It's a little bit tedious, but

**Dave Jones:** eh, you've got to do it. So, you can have at minimum a four-digit PIN code. I've put in a six-digit PIN code, but you can have up to eight as well. That's very nice. Phrase, here we go. This is

**Dave Jones:** the most important part, because if you get this, if you write this down wrong, and you lose your hardware wallet, you are screwed. You've lost your coins. That's it, all over Red Rover. Word number one, bunker. I've got a bunker.

**Dave Jones:** Cool. Um so, you just write these down on your sheet here. Make sure you get it right. The reason that they use words is that if you like random digits are harder to write down properly, but words are much

**Dave Jones:** easier. So, even if you misspelled it on here, you kind of can, you know, you're not completely screwed. You can uh you know, get the word correct when you reenter it. But, this is the point where you don't want anyone to look over your

**Dave Jones:** shoulder. I really love fury panda. Anyway, you can scroll back and forth at will for as long as you want through all these uh keywords. So, that's great. But, as I said, this is really quite hard to see. If you don't, you know, if

**Dave Jones:** you've got aging eyesight or other eye issues, then you know, it's it's not easy. Okay, we're done. Confirm our recovery phrase. Right, so it's put up the words, and then you have to take your list that you just got down and

**Dave Jones:** actually match the word that matches the select word on here. So, it's a bit tedious to set these things things things up and time-consuming, but well worth it. It didn't ask me to do all 24 of them. It just did like half a dozen

**Dave Jones:** selection there and your device is now ready. We are set up. So, we now have our recovery phrase, which we go put in our safe deposit box somewhere or you know, bury it in the backyard. I don't know,

**Dave Jones:** whatever you want to do with it. Don't lose that bit of paper and we're in like Flynn and here we go. Now, we have to hook it up to the computery thing and do our stuff. So, out of the box it only

**Dave Jones:** supports Bitcoin and Ethereum by the looks of it. You have to down go to the website and install the apps. And we've got some settings on here. Let's go in here. We can do display, brightness, rotate if you want or invert

**Dave Jones:** colors, whoopty-doo. Security, we can auto lock it. We can change our PIN number. We can shuffle our PIN number. Or we can set an additional pass-phrase as well. That's like a two-level protection. The Trezor has this one as

**Dave Jones:** well and for the ultra paranoid, you want both a PIN number and a pass-phrase as well. And you can set up multiple wallets with inside there. So, if someone's got a gun to your head and saying give me your password for your

**Dave Jones:** wallet, then you can give them the PIN code and they can access like a small amount and then you can have a bigger amount hidden away inside. So, yeah. I guess people robbing you have to know that. And the device, for those playing

**Dave Jones:** along at home, firmware 1.31. That's the secure element. So, that's the secure chip processor on the here the and the MCU is the micro-controller unit. That's just the ST arm micro I believe it uses inside this thing version 1.1. Okay,

**Dave Jones:** let's give it a go. Let's actually physically plug this baby in and we've got to enter our PIN code. They're they're the different versions of the Ledger. They all work very similar, so don't worry about that. So, all we have

**Dave Jones:** to do now is basically install the various apps. Now, one very different uh between the Ledger and the Trezor is that you have to basically the PIN code on this you have to dick around actually entering it with the buttons on here. I

**Dave Jones:** much prefer the way the Trezor does it where it actually pops up with a randomized keypad on the screen so that even if you have uh keylogger software or screen grabber software, you know, malware installed on your machine, it

**Dave Jones:** doesn't know the sequence of key codes which is defined inside here. But then you can use your mouse and your PC to actually access that. It's just better than around with those buttons. Entered my PIN code and we're in like

**Dave Jones:** Flynn and uh Windows 10 which I'm using here has just said it it only took like 5 seconds it automatically installed the drivers and it's all set up hunky-dory ready to go. Didn't have to download anything. Beauty. So, we definitely want

**Dave Jones:** to have a Bitcoin wallet support. So, let's click on the install um like add to Chrome. Okay. Whatever. Ledger Wallet. So, do we have to add a plugin for each individual uh coin, altcoin, and Bitcoin that we want to

**Dave Jones:** support? I Trezor in this case is much easier cuz you install one Chrome app or whatever browser you're using. I'm I'm sure it works on other browsers I just happen to use Chrome. Uh and that's it. You get one app which

**Dave Jones:** supports everything. Although the Trezor has a limited uh coin support, the Ledger actually supports more coins. But you have to set up each one differently. Uh jeez. Add app. Okay. Hm. Launch app. Ledger Wallet Bitcoin. To begin, connect

**Dave Jones:** and unlock your Ledger Wallet. Done. Looks like I've got to actually um select Use wallet to view accounts. Okay. I didn't have to I don't think I had to reconnect. There you go. Which coin do you want to use? Bitcoin. Remember my

**Dave Jones:** choice or Bitcoin Cash. Legacy or SegWit? Woah, see I won't go into the differences between segregated witness, which is all part of the blockchain and how it's split and or like it's complicated. Anyway, um we'll go with the new uh SegWit uh format. No wuckers.

**Dave Jones:** And your wallet is synchronizing. This may take a few minutes. I'll come back. Actually, that didn't take long at all. And then only a few more seconds and we're in like Flynn. There we go. We have our account. We have nothing in it of course

**Dave Jones:** cuz it's a brand new one, but we can just uh send coins directly in. So, we can receive it. Bingo. There's our Bitcoin address. If you want to send me Bitcoins, I don't know. I might damage this in the teardown. Um so, don't send

**Dave Jones:** them to that address. By the way, I do accept Bitcoin and many different altcoin donations. Linked in down below on my website. Thank you very much to everyone who donates. And I have no doubts it will accept our Bitcoin.

**Dave Jones:** Not a problem. Let's try the others. Full and I'm really finding it tedious to enter the PIN code on this. I've said that multiple times, but and as for this uh Bitcoin Cash option here, this is a bit confusing. If you want to If you had

**Dave Jones:** a previous account, you want to claim your cash coins and that's sort of stuff or you can use your split main or split. It's not, you know, if you're a beginner, not entirely obvious. I've already got uh the separate one, so I want to choose

**Dave Jones:** the split option to transact using a dedicated account. So, it's synchronizing. This might take a few minutes. Blah blah blah blah blah. Anyway, that's not obvious if you're a beginner. I want it to just go in there. The Trezor's

**Dave Jones:** uh much better in this particular case. So, there we go. Um I'm going to like send myself some Bitcoin Cash. Yay! I have my first Bitcoin Cash stored on here. I've got .001 Bitcoin Cash. That's the minimum I could uh transfer. In

**Dave Jones:** fact, I transferred point double 02 Bitcoin cashes and the fee was point double 01. So, I received point double 01 Bitcoin cash. Current value is $3.73. So, there you go. Try and hack it and get my Bitcoin cash. Go for it. And that

**Dave Jones:** took a minute and 51 seconds to for those playing along at home for me to transfer that from another exchange that I had to this. So, there you go. It works. We've got settings. We can go in here

**Dave Jones:** and we can take the hardware whether or not we've got an update and stuff like that. And we've got coins required confirmations to spend it and things like that. High fast confirmation, but that will cost you more coins to

**Dave Jones:** actually confirm you know to get a faster transaction. It costs you more. Or if you want to spend and get the minimum amount of fees, you can just go slow if you want it to take a day or

**Dave Jones:** whatever. How long it takes. Bitcoin is pretty notorious slow. Bitcoin cash is faster and Ripple is faster again. So, we can actually do that. We can actually go back in here and we can set up our Ripple wallet.

**Dave Jones:** Cuz I'm into Ripple. Ledger weapon. Like I don't like around having to download all these things, but I guess you only do it once, but it's not it's not terrific. The Trezor is a better easier to use solution, I think,

**Dave Jones:** especially for entering in the PIN code is much less sticky and it's sort of all integrated, but the Trezor supports a larger number of altcoins. Take your pick. Now, this is interesting. It looks like it's an XE there for the Ripple

**Dave Jones:** wallet. So, that's not terrific. Wanted just I thought it was just another Chrome app. Nope, it's an XE. So, there you go. We've got to actually install an XE, create a desktop shortcut. I like the Trezor in that it just worked from

**Dave Jones:** the you know the Chrome web app, and then that was it. Ledger wallet Ripple, here it is. To begin, I've got to unlock the damn thing again. The Ethereum uh one, so we'll give that a whirl. I'll I'll tell

**Dave Jones:** you what. I'm clicking on this thing and it ain't doing jack. So, I I don't know. I've opened it up here. Use your wallet to view account. So, I've got my, you know, I've chosen the Ethereum one on here and it's just quit app.

**Dave Jones:** Maybe I'll like I'll try it again. Okay, I just uh repowered it and reentered my tedious uh PIN code and we're in. So, I'm switched the power off and on again when in doubt. Um yeah, I don't I don't know. The Trezor's always worked

**Dave Jones:** every time for me. This one's kind of not. Maybe it will from now on, but yeah, not a good first impression. Anyway, we can uh receive some ether. I'll send myself some. Beauty. All right, and if we have a look down here,

**Dave Jones:** there's not much Oh, advanced mode. There you go. Let's go ahead and win contract data. Um if we uh receive, we can never receive the uh the hex code or the IBAN uh code. Send by email, print. There's not much else doing there,

**Dave Jones:** really. Gas limit, gas price. I won't go into details of gas. Um but my ether hasn't come through yet. It's probably lost in the ether. And for those playing along at home, that took uh three three and a half minutes basically to transfer

**Dave Jones:** the uh ether over. I transferred 0.1 ether. That was the minimum I can transfer from my other exchange and it cost me 1 milli ether. Geez, it's a bit rich, isn't it? To be fair, the uh Trezor actually doesn't have native support for

**Dave Jones:** uh ether for storing ether in the with the Trezor itself. It actually teams up with my ether wallet and I haven't used it for that and I think that's that's a downside to the Trezor. The Trezor is great for Bitcoin and the

**Dave Jones:** other couple that it supports natively but ether is not one of them. So you got to team up with the software wallet that allows you access to it and it's a multi-step process and so the Ledger is probably nicer solution if you're going

**Dave Jones:** to be storing some ether. Tell you what though, it would have been nice if it it just like got an exchange value from somewhere and told you what the rough price, you know, the rough worth of your ether is like it did for the Bitcoin

**Dave Jones:** one. Bitcoin cash one but yeah, it doesn't do it. That would have been nice. Aha, I RTFM'd, read the freaking manual and I found out why it doesn't run the Ripple app because I haven't installed the Ripple application on here. Obviously,

**Dave Jones:** it should give you like a Ripple option. So I've got to go into the Ledger Manager and I've got to actually download the application to the Ledger device. Don't worry because this is yeah, you can install run the apps on

**Dave Jones:** the main processor but you seed and everything is secure inside that secure hardware chip inside here. So don't worry, there's no vulnerability in there and all the apps are open source. So hey, anyone can go in there and check

**Dave Jones:** the validity of the whole thing. No worries. So now I've got to get and download the manager app. It's just much more around but hey, it supports a lot more altcoins than the Trezor does. There we go. That's better.

**Dave Jones:** Connected to the Ledger Nano S at the moment and it's got we can go to the firmware. No items to display. Anyway, applications. We can download. Here's what we support. Bitcoin, Bitcoin cash, dash, dogecoin, ethereum, fido utf, komodo, litecoin,

**Dave Jones:** stratis hello, Ripple, there we go. We want to download that and a whole bunch of altcoins, which the Trezor does not uh support. They're thinking about adding support for various ones, but it takes time. You can actually pay

**Dave Jones:** these companies to actually include in Trezor and others to uh add support for your um coin. You know, it costs like 50,000, 100,000 dollars or something one of the hardware wallets charges to actually add support. So, if you're developing a new coin, cuz

**Dave Jones:** there's a thousand coins, more than a thousand or something, and if you've developed one, then you can actually pay these hardware wallets, if you've got the money, uh the developers of the hardware wallets to add support for your coin. And well,

**Dave Jones:** it's open source, isn't it? Presumably, you can develop your own open source app, but they will write it for you. Anyway, we are going to download a Ripple and for security, it is asking me to uh confirm processing. It's

**Dave Jones:** installing. Hey, done. That was quick. I should now have access to Yes. I have Ripple. Hey, to begin, connect your Ledger wallet. It's already connected. Like if entered I got I like Argh! Once again, I've got to disconnect

**Dave Jones:** the thing and replug it. I might even have to like restart the app. I don't like it. Once again, turn the power off and on again and we're in like Flynn. All right, I'm still waiting for my Ripple, but uh if

**Dave Jones:** we send it, then the fee is very low, point double oh one Ripple. Um that's a lot less than what my other uh exchange charged me, that's for sure, like a many orders of magnitude less, but uh come on. Seems to be a low frequency

**Dave Jones:** Ripple. Hey, we're in and that took uh two minutes, just over two minutes and we've got our 25 was the minimum Ripple I could uh send, and I got point charge point 15 Ripple. I think I got ripped.

**Dave Jones:** So, what I don't like about this uh Ledger is that I compared to the Trezor is that yeah, I've got all these different um apps to run to access my different altcoins, and that might be okay, but I kind of even the Trezor

**Dave Jones:** doesn't support many. I I can actually swap between uh Bitcoin, Bitcoin Cash, and the other ones within so I just the one web-based um you know, extension web extension on Chrome, and it just works really well, and it gives me a little graph of how

**Dave Jones:** many like the amount of uh you know, coins that have been trading over time and stuff like that. Um I don't you know, this one has like it looks like it has a history, but it doesn't give you like graphs or anything

**Dave Jones:** like that. So, the Trezor's a nicer interface. And then if we want to uh send some Bitcoin Cash for example, so let's uh send that. Okay, let's go. Here we go. Preparing transaction. Let's send some Bitcoins. Here we go.

**Dave Jones:** And it says the amount. Now, here's the problem which I have with the Ledger is that it uh gives you the amount. That that that flicky you see is actually the uh just the camera frame update rate. It doesn't give you the

**Dave Jones:** full address. So, that's not good. Whereas the Trezor will give you the full address cuz it has the bigger screen on there, and you can make sure every digit is correct. So, technically speaking, you could exploit that with a

**Dave Jones:** man-in-the-middle what's called a man-in-the-middle attack. I won't explain that, but it's it's possible in theory anyway. Like it's highly unlikely, but because it doesn't display the confirm the full address on here, it could potentially be spoofed, and yeah,

**Dave Jones:** it's it's just an exploit. Um but it's just a technical thing. It's not a huge deal, but yeah, technically that is possible. So, I'm going to confirm my amount and confirm that and confirm the address and what? Fees. And I've got to confirm

**Dave Jones:** the fees. Confirm transaction. There we go. Use wallet to view access. Sending failed. What? What? What? What? Why? An error occurred. Huh. It's not a great first experience, is it? Don't know why. Just tried again. Failed again. I don't

**Dave Jones:** know. What do I don't have don't have enough Bitcoin Cash to pay for it or what? What's going on? And I was just about to send some Ripple back, but I just remembered you got to actually seed it

**Dave Jones:** with exactly with a minimum of 20 Ripple for the first transaction and I don't I'm a pauper. I've only got 4.84 Ripple. Oh. Now, this is weird. I just put in another 50 Ripple in. I sent another 50

**Dave Jones:** Ripple over. Took a couple of minutes and sure enough, it's now showing up as 74.70 balance. It was actually showing up as zero for like 30 seconds there. I like I started to panic like my Ripple had disappeared. Um and but like where is

**Dave Jones:** the transaction? Like like it hasn't last operations. It's showing up there, but my balance is that's the that's the first one I transferred, not the second one. So, like will it make a fool out of me now if I refresh it?

**Dave Jones:** I don't get it. Anyway, let's send some Ripple. Send. Confirm transaction. Unexpected error occurred. I confirm transaction. Unexpect I give up. I give up, really. I'm having problems sending Bitcoin Cash and Ripple. Like what the hell? No, hold on to your hats.

**Dave Jones:** It is like it confirmed with the address up here eventually, but it kept saying error. Now it says that the transaction's being processed. So, I'm not getting good vibes out of this thing. Um like it's just seems buggy.

**Dave Jones:** Not not the least bit impressed by it, really. No, I just got unexpected error again. This just This is hopeless. And here it is. We're in like Flynn. This is far too easy. A hardware wallet should not be this easy

**Dave Jones:** to get into. Now, I I know this has been a bit pedantic on my part, um but I want two things from a hardware wallet. A, I want it to be physically robust so that it can survive. I know that if you lose

**Dave Jones:** it, then you can recover from the pass phrase, but you know, that's like a last resort sort of thing. I want it to be robust and I want it so that people can't uh physically access the thing and

**Dave Jones:** potentially do hardware side channel attacks or whatever it is on this thing to extract your seed key from it. Uh like, you know, let's just be ultra paranoid and say that, you know, you're carrying one of these through the

**Dave Jones:** airport or something and they go, "Oh, you've got a hardware wallet. Let's We're going to inspect that." And they take it from you, they take it into another room. What are they going to do to it? You just don't know. And in this

**Dave Jones:** case, it's just got a clip-on plastic case. I just got my knife in the side and boop, it pops straight off. So, anyone could physically take this apart and access the hardware in here, access the pins directly, probe them, do

**Dave Jones:** whatever without and without you knowing that they've even opened the thing. And like jeez, put some potting in here. In fact, if you got one of these, um I would probably just open it up and fill it up with some potting compound A to

**Dave Jones:** make it more robust and B to make it uh more physically uh secure. Anyway, I know it's being very pedantic because these things, especially the um ledger here, is very secure. So, what have we got inside here? Well, we've got an STRM uh micro.

**Dave Jones:** It's a 32F042K. And uh there's no external clock on here, so it's running from an internal clock, uh which is different to the uh Trezor. If you've seen the teardown of that, it's actually got an external clock. And that's technically marginally

**Dave Jones:** more secure with the using the internal clock cuz then you can't do uh attacks uh fit like hardware attacks that uh hacking attacks that try and use the uh clock, slow it down, and glitch the clock, and do all sorts of uh things

**Dave Jones:** like that. Now, this is what makes the Ledger so good. This is the um ST uh 31H320 uh secure chip. This is where your seed device is generated and stored. Unlike the Trezor, which is just stored inside a regular arm microcontroller, and

**Dave Jones:** you're just relying on the not very good security inside a physical hardware security inside an arm micro. These chips are specifically designed in the industry to be really secure devices, and they're certified and rated by various, you know, certification

**Dave Jones:** agencies for uh security and that type of stuff. They're used in type inside all types of uh secure products. And they'll physically, even though you can't get a data sheet for this cuz it's under a non-disclosure agreement, uh you

**Dave Jones:** might be able to maybe find some patterns on it or something like that. But, it's uh probably got like a mesh physically covering the die in there and uh other various uh physical uh protection to stop you actually probing device. So, device. So,

**Dave Jones:** even if you were able to uh dissolve away the chip itself with some acid, this one actually looks, you know, is it is it ceramic? Uh I don't know. Anyway, it's not your regular plastic package by looks of it.

**Dave Jones:** But yeah, even if you were able to dissolve that away, then you can't physically get in there and probe the die cuz they've probably got some mesh protection or other physical hardware protection inside the chip itself. And that's what makes the Ledger technically

**Dave Jones:** uh more secure than the Trezor is because it uses that device. So, there you go. Up here, we've got another ST part. This is actually a ST8R00. And this is actually a boost converter. A boost voltage converter. So, why they

**Dave Jones:** need a boost voltage converter in there? I'm not sure. Do they need it for the chip or for the display? Perhaps. Uh strange. And for those who are curious, there's the bottom of the board. There's no components on there. It's just a

**Dave Jones:** double-sided uh board. And there is the display. Now, I could actually get like the scope in there and try and you know, do some power line monitoring to see if there's data coming out and stuff like that. But

**Dave Jones:** really, I'm like this is one of like one of the industry's best secure chips. And there's like like there's no way I'm going to be doing like be going to be able to hack this thing. So, for those people who

**Dave Jones:** say, "Oh, just give it a try. Hook it up." Well, no, I don't have the expertise to hack secure crypto chips and stuff like this. Nor do I have the time to even try. So, I'd really be wasting my time

**Dave Jones:** with you know, trying to do that. Uh many other people have tried, I'm sure, that are experts in the field. Anyway, um yeah, my only complaint is that it's like God, they couldn't even glue this on. They couldn't even glue it on. Like

**Dave Jones:** you know, let alone like or ultrasonically welded or anything. Like at at least the Trezor is like glued together and you have to pretty much Dremel the case open so that some you physically know if someone's tried to

**Dave Jones:** access your hardware in there. Um which is more important for that because like this chip is pretty darn secure. So I guess it it's just like a small argument, but if somebody ever did find an exploit for this um and they didn't

**Dave Jones:** and it wasn't publicly known and they could physically get access to your hardware, then well, you know, they could technically get in there and get your data, but we're entering ultra paranoid territory. I mean, they have to A, physically get

**Dave Jones:** this device and B, and really it's much easier just to go to your bedside drawer and try and find your recovery seed card um than to try and extract your seed out of this, but you know, anyway, this is

**Dave Jones:** technically more secure than the Trezor. So if you're you know, if you're worried about vulnerabilities inside uh just your regular ST micros in in your Trezor, that's where your code your seed is stored. So it's more vulnerable, it's

**Dave Jones:** got an external clock, there's various uh more side channel attacks you could potentially do to that than an already proven and secure and industry rated uh secure chip like is what's used in the Ledger here. Why can't they just sell a

**Dave Jones:** version or fill this with potting compound? Why? Just pot it. I know it costs more as a manufacturing step, but they already make an absolute monster margin on these things anyway. As you can see, there's not much in it. I don't

**Dave Jones:** know how much the secure chip costs though. Well, there you have it. That's a look at the Ledger Nano S. And well, in a little bit of a comparison with the Trezor here. And have I seen enough in

**Dave Jones:** the Ledger Nano S to make me want to switch from the Trezor which I've been using? Um basically, no. A lot of people swear by this thing and it is cheaper than the Trezor. So, if you looking for

**Dave Jones:** the cheapest hardware solution and you should be using a hardware solution to store your coins coins, absolutely no doubt. So, a lot of people swear by this thing, but I've had too many little niggling problems with this and I still

**Dave Jones:** haven't been able to send anything using this. So, I I I don't know what's up. I still need to play with it some more, but to you know, an app a separate app for every single coin that you've got to

**Dave Jones:** support, but it does support more coins than the Trezor. Yeah, I'm I'm not really impressed by this, but in terms of hardware security, technically this one's better than this cuz it uses the secure uh chip in it to

**Dave Jones:** store your seed and it's an industry standard chip and it's well-proven. Um whereas the Trezor just uses your standard micro. So, technically, in theory, this is susceptible and it has been in the past and they've fixed it, but it hasn't been a major deal, but

**Dave Jones:** it um technically, cuz it uses a standard non-secure micro, uh not only susceptible to uh like USB attacks, power glitching attacks, and other uh sorts of stuff like that, but it's also susceptible to like a supply chain type

**Dave Jones:** attack. I you buy it from the one hung low merchant on eBay and well, you know, there's no way for this to know, like it doesn't have any uh like device ID built in. It can't sort of, you know, checksum itself. The

**Dave Jones:** firmware checksums itself, but not as good as this. This actually has an individual secure ID inside the secure chip itself. So, technically, that's another exploit possible with this thing. That's why you've got to buy it from a genuine supplier or you can build

**Dave Jones:** your own from scratch cuz this thing's completely open source hardware and this one's not. So, there's pros and cons both ways. There's absolutely no clear winner here, but I'm I'm going to stick with my Trezor for now. I'm going to

**Dave Jones:** play with the Ledger Nano S some more. But as I said, really any technical argument about which one is more secure is pretty moot when it's basically in theory cuz you've physically got the device and really you're more vulnerable

**Dave Jones:** by the actual seed card that you need to write down the words is much more vulnerable than these things. So, you know, if you could debate which one is more secure. Technically this one's a bit better, but this one's open

**Dave Jones:** hardware, so it's fully checkable, etc., etc. You can build your own, whatever. Like it doesn't really matter. It's all about the user interface experience and the fact that you've got a proven hardware wallet. So, they're both fine from that aspect. Looking forward to

**Dave Jones:** getting the new Trezor which is coming out, the model T. I've pre-ordered one of those. But yeah, I I don't know. There's just I expected better from this. I've had too many little glitchy problems and and I still can't get back

**Dave Jones:** into my ether wallet. By the way, I'm clicking the damn button to get in and I'm repowering it and I I I can't recommend this at this stage. Whereas the Trezor, I've been using this and I haven't really had a single issue

**Dave Jones:** with it and I've been getting my split coins and stuff on it and I've been using the beta wallet for this thing, not just the main wallet, and I've had no issues. So, yeah, Ledger Nano S, I'm not going to call it a fail, but I I

**Dave Jones:** just need to spend some more, you know, I need to figure out a few more things with this thing, I think. So, yeah, not I really can't recommend it at this stage. Anyway, that was a long video. Hope you found it

**Dave Jones:** useful. Catch you next time. Oh, yeah, discuss down below, all that sort of YouTube-y stuff that we say and subscribe wherever it is at the end and watch videos at the end of this thing. You know, whatever. Catch you next time.
