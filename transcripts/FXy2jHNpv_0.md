---
video_id: FXy2jHNpv_0
title: EEVblog #52 - Panasonic Plasma TV's Suck (and a Teardown)
url: https://www.youtube.com/watch?v=FXy2jHNpv_0
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 32, "3": 47, "4": 61, "5": 74, "6": 90, "7": 105, "8": 124, "9": 134, "10": 142, "11": 150, "12": 161, "13": 179, "14": 191, "15": 202, "16": 217, "17": 229, "18": 245, "19": 255, "20": 277, "21": 287, "22": 299, "23": 317, "24": 329, "25": 349, "26": 363, "27": 379, "28": 394, "29": 401, "30": 412, "31": 421, "32": 435, "33": 450, "34": 475, "35": 495, "36": 506, "37": 519, "38": 532, "39": 543, "40": 557, "41": 569, "42": 580, "43": 593, "44": 610, "45": 626, "46": 639, "47": 655, "48": 664, "49": 677, "50": 696, "51": 710, "52": 722, "53": 737, "54": 751, "55": 759, "56": 778}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's time for something that ticks me off again.

**Dave Jones:** What is it this time? Well, it's plasma TVs. In this case, specifically Panasonic plasma TVs. Why? Well, I've got a 42-in top-of-the-range Viera Panasonic plasma TV. I've only had it for like 2 and 1/2 years or something like that, and it just died the other day.

**Dave Jones:** Well, it didn't just die. Here's a photo of the actual problem. Take a look at it. As you can see, there's a big black stripe column missing down the right-hand side, and then these thin white lines on it.

**Dave Jones:** And I was just sitting there watching, and bang, there it goes. You know, this And this TV's hardly used at all. It's It's in the main It's in the lounge room, which, you know, we might use it to just watch a DVD occasionally.

**Dave Jones:** So, it probably only gets like 50 or 100 hours use a year at at best, really. So, it's hardly had any use at all, and it's failed in 2 and 1/2 years.

**Dave Jones:** And of course, it's I opted not to get the extended warranty. Yeah, stupid me, right? But hey, you know, it was really expensive at the at the time. It was like $400 or something for the extended warranty.

**Dave Jones:** So, screw that. And I knew Murphy's Law was going to screw me over anyway, so even if I got the extended warranty, it wouldn't have done any good. So, yeah, I've I've had a quote to to actually get it fixed, and no, it's it's not just one of the boards that's failed.

**Dave Jones:** It turns out it's the actual plasma screen itself. And to fix it, $1,275. I can buy a brand new one for that, or less than that. It's crazy. Ah, bloody plasma TVs, they tick me off.

**Dave Jones:** I bought a top of the range Panasonic because I knew, you know, plasma TVs were notorious for failing and things like that. And there's the plasma graveyard out there with all these screens that have just died.

**Dave Jones:** And well, I thought I'd get, you know, Panasonic are supposed to make the best plasma TVs in the business. So, I thought, you know, I'm pretty safe with that.

**Dave Jones:** I knew it wasn't going to get much use. So, you know, I expected it to last a long time. Maybe the power supply or something like that would fail.

**Dave Jones:** I didn't expect that um plasma thing to fail, the actual plasma screen itself. Ah, anyway, uh I thought what would be interesting is to um crack it open and take a look inside.

**Dave Jones:** See what the engineering's like inside one of these modern plasma TVs. So, let's check it out. Okay, now let's take a look inside. I've taken the back panel off here, and um there were a whole bunch of screws around the outside of it here, and uh it it just popped off really easily.

**Dave Jones:** And here it is. I'll see if I can get a wide shot. There it is sitting on the bench. It's absolutely huge, this thing. And uh the good thing is is that you can see it still goes on the stand.

**Dave Jones:** The stand still sits there, and you can just um take the panel off with it sitting on the stand. It's fantastic. I really like that. Anyway, let's take a look at it from an engineering aspect.

**Dave Jones:** Now, the first thing I notice is this quality uh mains input filter here. That's the you plug your mains up into there, and that's a mains input filter. And you notice this um tape stuff here, this spongy sort of uh tape stuff.

**Dave Jones:** That's for um RFI to actually get a good um RFI connection shield into the back panel. And they've got a couple more down here. They've got another one down here, and over here on this side here.

**Dave Jones:** This um this metallic stick on spongy tape stuff and it's it's really good. The attention to detail is quite amazing. And um one of the things I really noticed is um these See these little tiny um uh screw mounts down here?

**Dave Jones:** They're actually gone to a lot of trouble to um to get these surface mount uh washers which extend from the screw down into the um onto the PCB here.

**Dave Jones:** And they've got those all over the set. And it's it really is very nice. Now, uh the main um power supply, this is the main power supply board here and um as you can see it has two huge caps over here and and the it's a single-sided board as you typically get in a uh power supply.

**Dave Jones:** That's why there's lots of links and things in there because that's cheaper to manufacture. But the the uh quality of the components is really actually quite nice. The um there's some there's a couple of fuses there.

**Dave Jones:** There's a couple of input protection uh input protection devices there. And the quality of the power supply and the quality of the components used is actually quite good. Um there's this board here.

**Dave Jones:** sure what this one does. It sort of it only in interconnects with a couple of these nice blue uh ribbon um nice blue uh cable bundles here. And um yeah, it it hooks onto the main processor board which is this one here um which connects to all the input sockets.

**Dave Jones:** There's actually an extra board behind there but um this is the main There's a huge BGA chip there. That's the main processor. Another couple of Panasonic branded uh chips there if you can see them.

**Dave Jones:** Yeah, there we go. Panasonic branded um and there's a Oh, there's an Analog Devices part. I'm not sure ADV 74998. I'm not sure what that one does off the top of my head, but that connects into the uh Here's the um input um uh RF tuner.

**Dave Jones:** There's another block here. This one doesn't have a built-in digital tuner. It's just an analog one. So, um then this was before the analog the built-in digital tuners became so cheap and prevalent.

**Dave Jones:** Now, here's another big driver here. This board here is obviously the driver for the rows because it goes into the via this nice board-to-board interconnect here. It goes into these row drivers.

**Dave Jones:** And as you can see, there's 16 of them down here. There's 16 row driver chips. And because this is a 1024 by 768 panel, I think you'll find that's 64 channels per ribbon cable if you do the math.

**Dave Jones:** I think in the top of my head, I think that's correct. So, as you can see, they're the um they're the row drivers. And they're Panasonic branded as well.

**Dave Jones:** If that can focus. There we go. And they've put this this gunk around the outside of the chip. I'm not sure why they've done that. Maybe for some Maybe it's actually high voltage.

**Dave Jones:** I'm not sure. No, it's probably not. It's I don't know. It's just some sealing around the chip maybe to keep dust or something like that out. Perhaps dust or moisture out.

**Dave Jones:** I'm not quite sure, but um Now, as you can see, there's a couple of speakers down in the bottom here either side. Now, this board in here, this is the obviously the column driver.

**Dave Jones:** And this is what has failed in this TV because in in particular this channel here. Now, there's no actual circuitry on this board to actually do much. It's just like a little driver interface.

**Dave Jones:** And I believe there's eight channels per thing. There's actually two. If we This is a little flat flex cable here. If we get in here and we pop that open like that, it comes down and then under these screws and this column driver is open and bingo, there's your two column driver chips.

**Dave Jones:** So, there's actually a total of eight channels, but because there's two chips per channel, there's um uh there's a total of 16 of these devices and I think that little sucker there is the one that's failed or something like that because it's this side of the screen.

**Dave Jones:** It's this side of the panel, which is actually gone out. So, yeah, and that's like attached. That's like embedded attached to the panels. You can't You can't really fix that.

**Dave Jones:** That's That's actually a chip on flex on the flex um Mylar flexible cable thing. So, that's not really fixable. That's why you've got to get a whole new panel.

**Dave Jones:** Okay, so how do I know it's actually the plasma screen itself that's failed? Well, what I've done is I've disconnected the channel down here, which is at fault and I believe it's just that particular chip there.

**Dave Jones:** It's not actually this one. So, it's only the columns driven by this chip, which are actually failed. So, um let's I've plugged it in and let's switch it on and let's see.

**Dave Jones:** So, we should now get um two columns that are actually missing. Come on. Power up. Power up. And bingo, there it is. As you can see It's hard to get in here.

**Dave Jones:** Sorry about that, but as you can see, I've got the same fault as before with the black um column. Sorry, yeah, the black column down there with the white stripe and the white stripe is still there.

**Dave Jones:** So, that tells me that really there is something the same fault as there even though I disconnect that channel. so really there's you know there's something funny going on inside the actual um plasma screen itself.

**Dave Jones:** And as you can see, the extra column now, the same width column is doing a funny thing cuz it's not plugged in. So, um yeah, that's you know there's something a fault there.

**Dave Jones:** And I'll plug that board back in and show you that that extra column comes back. Okay, so here it is. I've plugged that um channel back in and it's going to come on and bingo, as you can see the picture's come back from that column and I'm left with the original fault of the black um column with the white stripe.

**Dave Jones:** So, there you go. It does look like it is the actual plasma screen. Now, let's have a look at the quality of the uh construction and layout on um on this column uh sorry, row uh driver board.

**Dave Jones:** These these electrolytic caps aren't in a good spot cuz they're between two heat sinks. And the heat sinks are going to get hot and as I've explained in previous blogs, the um the caps can actually um uh heat up and that actually reduces their life.

**Dave Jones:** So, that's not so good, but I can't see anywhere else you can actually um put them though. But um yeah, the the quality of the components used in this thing is really quite nice and and they're excellently machine assembled and and you know, it it really is.

**Dave Jones:** I can't see any bodgy stuff at all in this entire design. And that's what you get when you buy a quality brand like a Panasonic. But that didn't stop it bloody well failing, did it?

**Dave Jones:** No. But um the but the quality of construction is is really quite nice. And there's a couple of fans up here and they've got a um they've you know they've got the the foam surround on them just to just to quieten them down a bit.

**Dave Jones:** And um yeah, it's just it's just really really superb construction. I like it. Thumbs up. So, there you go. That's what's inside a modern plasma TV. And as you can see, the engineering is actually very, very good.

**Dave Jones:** It's quite It's almost pornographic. The amount of engineering work that goes into uh you know, designing and and building a a plasma TV is actually quite remarkable. But um you know, that didn't do me any good, did it?

**Dave Jones:** Cuz the Panasonic, the bloody thing, it it died on me after just you know, a few hundred hours USE AT MOST. GARBAGE. SO, HERE'S THE EEVblog tip of the week.

**Dave Jones:** Don't buy a plasma TV. And in particular, don't buy a bloody Panasonic. I would have been better off buying two of the cheapy OneHungLow brand ones. I could have used one and then kept the other one in the box for the same price I paid for this damn Panasonic.

**Dave Jones:** I could have got the new one out and just replaced it. Oh. You know what else ticks me off? It's when you're an electrical engineer, an electronics engineer like that, and people realize that, they go, "Oh, can you fix my TV?

**Dave Jones:** You must be able to fix MY TV." NO. GO AWAY. I CAN'T fix your TV. Go to your local SERVICE GUY. I'VE GOT TOO MUCH gear to fix a TV.

**Dave Jones:** I'm crippled. I've got too much knowledge. I can't do it. Let your local TV repair guy do it. He's got the parts. He's got the experience. Don't come to me.

**Dave Jones:** Screw this. Fix that Panasonic.
