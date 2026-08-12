---
video_id: u2yRR4G3yTA
title: EEVblog #2 - Burden Voltage, HP Multimeter review
url: https://www.youtube.com/watch?v=u2yRR4G3yTA
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 34, "3": 63, "4": 77, "5": 89, "6": 112, "7": 129, "8": 142, "9": 164, "10": 175, "11": 189, "12": 211, "13": 247, "14": 265, "15": 279, "16": 299, "17": 312, "18": 326, "19": 337, "20": 348, "21": 362, "22": 392, "23": 414, "24": 428, "25": 450, "26": 464, "27": 476, "28": 497, "29": 518, "30": 528, "31": 539, "32": 553, "33": 564, "34": 580}
---

**Dave Jones:** Hi, I'm Dave Jones again. And this is the second EEVblog, the Electronics Engineering Video Blog. I had a ton of feedback from the first one, so number two, here it is.

**Dave Jones:** Now, there are a few people who suggested that I change the drab office background I used last time. So, here we are. We're at the bench. So, it should provide some visual eye candy for uh people who want to be a bit distracted from my talking head.

**Dave Jones:** First up, we've got a book review. And as usual, it's a book of interest to electronics engineers. Now, this time I've chosen High-Speed Signal Propagation by Howard Johnson. His first book, High-Speed Digital Design, it uh a Handbook of Black Magic, is uh basically uh is the industry bible on High-Speed Digital Design, transmission lines, um stuff like that.

**Dave Jones:** So, if you're into anything to do with uh high-speed digital, um you really should have uh a Handbook of Black Magic. But, um this uh one is the follow-up to that.

**Dave Jones:** It's the Advanced Black Magic, and um it it really goes into um more advanced uh topics, and uh that that weren't really covered in the first book. So, they it it doesn't really cover the same ground.

**Dave Jones:** It's a complementary uh book, which uh supplements the other one. So, if you've got that, I'd highly recommend this, and it gives you a great two-volume reference set for uh signal propagation and transmission line design, PCB design, and um high-speed digital stuff.

**Dave Jones:** I've got a handy website for you. Um if like me you spend your day on Digikey and Mouser and Farnell websites just trolling for parts and, you know, trying to find the best price or the best availability and stuff like that, it it can be a real chore.

**Dave Jones:** And um it it it it'd be nice if there was a tool that uh searched all of them at once. And luckily, there is. And I use it like, you know, 10 times a day sometimes.

**Dave Jones:** It's really amazing. It's called findchips.com. And it's a real basic website. It's just got a single search uh window. You just type in the part number you want and it cross-references dozens of different uh vendors and it gives you uh whether or not they're in stock, price, um and all that sort of stuff.

**Dave Jones:** And it's real simple. There's no fluff, there's no ads. Uh the guy who runs it's a bit of a mystery. Um we don't really know. It's just a contact us email.

**Dave Jones:** But uh it's a it's a fantastic site. And uh I've never found it to actually be uh broken. So, it And I do know that uh the likes of Mouser and Digikey and and the big ones um do like to change their uh database access a lot.

**Dave Jones:** So, um the guy's really kept up to date on uh on uh searching for that info. So, give it a go. findchips.com. I've got an article in this month's Silicon Chip magazine, April 2009, about uh this new project I've come up with.

**Dave Jones:** It's really simple. It's called the micro current. And it's uh it fixes a major problem to do with almost every multimeter on the market. Now, I've really um since I developed this little project, I've lost count of the number of people who have uh, been baffled that their multimeter, even a precision Fluke 87 multimeter, uh, that they've they've been using for 20 years is, in many cases, useless at measuring

**Dave Jones:** precision current. Uh, be it in DC or AC circuits. And it's to do with burden voltage. Now, every most people know about burden voltage. There's there is there's a shunt resistor inside the multimeter that drops a voltage when you pass current through it.

**Dave Jones:** No problem. Easy, right? And but most people think it's really small. But it's not. The closer you get to the full scale range of the meter, the the the bigger the drop, obviously.

**Dave Jones:** Now, a really good meter, like the Fluke 87 V, it will have well, this one actually has 1.8 millivolts per milliamp burden voltage. So, if you pass 200 milliamps through this, if you try to measure 200 milliamps, that's a 360 millivolt drop.

**Dave Jones:** Now, that it may not sound like much, but really 360 millivolts is, if your circuit is 5 volts, bingo, you've already, uh, thrown your circuit out of voltage spec, probably.

**Dave Jones:** Let alone a 3.3 volt circuit or I'm working a lot these days on 1.2 volt circuits. So, it's, you know, a current like this, you really can't a meter like this, you really can't measure precision current with.

**Dave Jones:** It's crazy. But, yeah, a lot of people seemed embarrassed that they don't know that their meter is not very precise at all. And that goes for virtually every meter on the market.

**Dave Jones:** There are some that are almost an order of magnitude worse than this, and price really doesn't have much to do with it. You can pay $2,000 for a multimeter it's still going to have the same problem.

**Dave Jones:** So, just be wary of it. Burden voltage. Now, it's time for chip of the week. Ta-da! This is where I mention a really handy chip or some other device.

**Dave Jones:** And today, it's not a chip as such, but it's a range of chips and a technology called ANT. Um the website is thisisant.com. This is ANT. And the ANT chipset is basically a low-power, extremely low-power, wireless networking solution.

**Dave Jones:** Um it's primarily used in the fitness market for those chest transmitters that people wear. The ANT chipsets are a complete single-chip solution that they include RF transmitter, they include the protocol stack, and you can set up private or public networks with these chips.

**Dave Jones:** And they're quite easy to use, and the website has a really good power estimator. So, you type in your parameters, what what data burst rate you want, and it tells you how long your battery is going to last.

**Dave Jones:** So, they're really handy. Um they're sort of they they are competition to this new low-power Bluetooth uh standard that's around. Now, ANT's not actually a standard, it's more of a proprietary solution, but Nordic Semiconductor make the chips for those as well as for the Bluetooth low-power Bluetooth standard.

**Dave Jones:** And they're worth keeping in mind if you've got a really low-power wireless transmitter which you need to implement. So, check it out. Now, it's time for an equipment review.

**Dave Jones:** This is where I review a really cool piece of new gear. Now, since the last blog I've been inundated, absolutely inundated with manufacturers wanting to send me all this new gear.

**Dave Jones:** And well, they they say it's in the mail. So, I don't really have anything new this week. So, I decided to go retro. And so, I've chosen the Hewlett-Packard 3478A bench digital multimeter.

**Dave Jones:** Now, it's a old model from the '80s, but it's it's really nice. It's 5 and 1/2 digits, and it's something like point double 04% basic DC volts accuracy. And it's incredibly stable, and you can buy them these days and be pretty much assured that's still going to meet all its specs.

**Dave Jones:** And it's just fantastic 5 and 1/2 digits accuracy, and you you really can't beat it. You can get them on eBay and and all the other surplus places for not much money at all.

**Dave Jones:** They go really cheaply. I think I got mine for like $150 or something like that. It's it's quite cheap, and they're very popular, and there's a lot of them out there on the market.

**Dave Jones:** The market's flooded with them. And really, I think everyone should have one of these. It's on their bench. You really can't beat having a really high precision 5 and 1/2 digit meter on your bench when when you need it.

**Dave Jones:** You You wouldn't use it for everyday use. You'd use your handheld multimeter for that cuz it's more convenient, but you really need you really should have one of these.

**Dave Jones:** It's it's got four-terminal resistance measurement. It's got rear terminals on the back as well, which can be handy. It's mains powered, of course. Um, there might even be a battery option for some model somewhere, but um yeah, it's a really nice bit of kit.

**Dave Jones:** I'd highly recommend you pick one up. I forgot to mention one thing about the HP meter. Yes, the burden voltage actually sucks, but you can't have everything.
