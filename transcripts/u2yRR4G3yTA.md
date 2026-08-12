---
video_id: u2yRR4G3yTA
title: EEVblog #2 - Burden Voltage, HP Multimeter review
url: https://www.youtube.com/watch?v=u2yRR4G3yTA
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 36, "3": 60, "4": 77, "5": 91, "6": 112, "7": 129, "8": 142, "9": 160, "10": 172, "11": 186, "12": 204, "13": 226, "14": 247, "15": 264, "16": 283, "17": 304, "18": 321, "19": 335, "20": 348, "21": 370, "22": 400, "23": 420, "24": 437, "25": 454, "26": 471, "27": 491, "28": 513, "29": 526, "30": 541, "31": 556, "32": 572, "33": 589}
---

**Dave Jones:** Hi, I'm Dave Jones again. And this is the second EEVblog, the Electronics Engineering Video Blog. I had a ton of feedback from the first one, so number two, here it is. Now, there are a few people who suggested that I change the drab office

**Dave Jones:** background I used last time. So, here we are. We're at the bench. So, it should provide some visual eye candy for uh people who want to be a bit distracted from my talking head. First up, we've got a book review.

**Dave Jones:** And as usual, it's a book of interest to electronics engineers. Now, this time I've chosen High-Speed Signal Propagation by Howard Johnson. His first book, High-Speed Digital Design, it uh a Handbook of Black Magic, is uh basically uh is the industry bible on High-Speed

**Dave Jones:** Digital Design, transmission lines, um stuff like that. So, if you're into anything to do with uh high-speed digital, um you really should have uh a Handbook of Black Magic. But, um this uh one is the follow-up to that.

**Dave Jones:** It's the Advanced Black Magic, and um it it really goes into um more advanced uh topics, and uh that that weren't really covered in the first book. So, they it it doesn't really cover the same ground. It's a

**Dave Jones:** complementary uh book, which uh supplements the other one. So, if you've got that, I'd highly recommend this, and it gives you a great two-volume reference set for uh signal propagation and transmission line design, PCB design, and um high-speed digital stuff.

**Dave Jones:** I've got a handy website for you. Um if like me you spend your day on Digikey and Mouser and Farnell websites just trolling for parts and, you know, trying to find the best price or the best availability and stuff like that, it it

**Dave Jones:** can be a real chore. And um it it it it'd be nice if there was a tool that uh searched all of them at once. And luckily, there is. And I use it like, you know, 10 times a day

**Dave Jones:** sometimes. It's really amazing. It's called findchips.com. And it's a real basic website. It's just got a single search uh window. You just type in the part number you want and it cross-references dozens of different uh vendors and it

**Dave Jones:** gives you uh whether or not they're in stock, price, um and all that sort of stuff. And it's real simple. There's no fluff, there's no ads. Uh the guy who runs it's a bit of a mystery. Um we don't really know. It's

**Dave Jones:** just a contact us email. But uh it's a it's a fantastic site. And uh I've never found it to actually be uh broken. So, it And I do know that uh the likes of Mouser and Digikey and and the

**Dave Jones:** big ones um do like to change their uh database access a lot. So, um the guy's really kept up to date on uh on uh searching for that info. So, give it a go. findchips.com. I've got an article in this month's

**Dave Jones:** Silicon Chip magazine, April 2009, about uh this new project I've come up with. It's really simple. It's called the micro current. And it's uh it fixes a major problem to do with almost every multimeter on the market. Now, I've really um since I developed

**Dave Jones:** this little project, I've lost count of the number of people who have uh, been baffled that their multimeter, even a precision Fluke 87 multimeter, uh, that they've they've been using for 20 years is, in many cases, useless at measuring

**Dave Jones:** precision current. Uh, be it in DC or AC circuits. And it's to do with burden voltage. Now, every most people know about burden voltage. There's there is there's a shunt resistor inside the multimeter that drops a voltage when you pass current

**Dave Jones:** through it. No problem. Easy, right? And but most people think it's really small. But it's not. The closer you get to the full scale range of the meter, the the the bigger the drop, obviously. Now, a really good meter, like the Fluke 87

**Dave Jones:** V, it will have well, this one actually has 1.8 millivolts per milliamp burden voltage. So, if you pass 200 milliamps through this, if you try to measure 200 milliamps, that's a 360 millivolt drop. Now, that it may not sound like much, but

**Dave Jones:** really 360 millivolts is, if your circuit is 5 volts, bingo, you've already, uh, thrown your circuit out of voltage spec, probably. Let alone a 3.3 volt circuit or I'm working a lot these days on 1.2 volt circuits. So, it's,

**Dave Jones:** you know, a current like this, you really can't a meter like this, you really can't measure precision current with. It's crazy. But, yeah, a lot of people seemed embarrassed that they don't know that their meter is not very precise at

**Dave Jones:** all. And that goes for virtually every meter on the market. There are some that are almost an order of magnitude worse than this, and price really doesn't have much to do with it. You can pay $2,000 for a multimeter it's still going to

**Dave Jones:** have the same problem. So, just be wary of it. Burden voltage. Now, it's time for chip of the week. Ta-da! This is where I mention a really handy chip or some other device. And today, it's not a chip as such, but it's a range of

**Dave Jones:** chips and a technology called ANT. Um the website is thisisant.com. This is ANT. And the ANT chipset is basically a low-power, extremely low-power, wireless networking solution. Um it's primarily used in the fitness market for those chest transmitters that people wear. The ANT

**Dave Jones:** chipsets are a complete single-chip solution that they include RF transmitter, they include the protocol stack, and you can set up private or public networks with these chips. And they're quite easy to use, and the website has a really good

**Dave Jones:** power estimator. So, you type in your parameters, what what data burst rate you want, and it tells you how long your battery is going to last. So, they're really handy. Um they're sort of they they are competition to this new low-power

**Dave Jones:** Bluetooth uh standard that's around. Now, ANT's not actually a standard, it's more of a proprietary solution, but Nordic Semiconductor make the chips for those as well as for the Bluetooth low-power Bluetooth standard. And they're worth keeping in mind if you've

**Dave Jones:** got a really low-power wireless transmitter which you need to implement. So, check it out. Now, it's time for an equipment review. This is where I review a really cool piece of new gear. Now, since the last blog I've been

**Dave Jones:** inundated, absolutely inundated with manufacturers wanting to send me all this new gear. And well, they they say it's in the mail. So, I don't really have anything new this week. So, I decided to go retro. And so, I've chosen the Hewlett-Packard

**Dave Jones:** 3478A bench digital multimeter. Now, it's a old model from the '80s, but it's it's really nice. It's 5 and 1/2 digits, and it's something like point double 04% basic DC volts accuracy. And it's incredibly stable, and you can buy

**Dave Jones:** them these days and be pretty much assured that's still going to meet all its specs. And it's just fantastic 5 and 1/2 digits accuracy, and you you really can't beat it. You can get them on eBay and and all the other

**Dave Jones:** surplus places for not much money at all. They go really cheaply. I think I got mine for like $150 or something like that. It's it's quite cheap, and they're very popular, and there's a lot of them out there on the market. The market's

**Dave Jones:** flooded with them. And really, I think everyone should have one of these. It's on their bench. You really can't beat having a really high precision 5 and 1/2 digit meter on your bench when when you need it. You You wouldn't use it for everyday

**Dave Jones:** use. You'd use your handheld multimeter for that cuz it's more convenient, but you really need you really should have one of these. It's it's got four-terminal resistance measurement. It's got rear terminals on the back as well, which can

**Dave Jones:** be handy. It's mains powered, of course. Um, there might even be a battery option for some model somewhere, but um yeah, it's a really nice bit of kit. I'd highly recommend you pick one up. I forgot to mention one thing about the

**Dave Jones:** HP meter. Yes, the burden voltage actually sucks, but you can't have everything.
