---
video_id: ix2fR-rh1vc
title: EEVblog #1015 - Beware Evil (But Clever) DC Jacks!
url: https://www.youtube.com/watch?v=ix2fR-rh1vc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 46, "3": 63, "4": 82, "5": 101, "6": 119, "7": 133, "8": 152, "9": 170, "10": 184, "11": 203, "12": 223, "13": 239, "14": 253, "15": 270, "16": 284, "17": 300, "18": 318, "19": 340, "20": 360, "21": 374, "22": 392, "23": 406, "24": 424, "25": 436, "26": 451}
---

**Dave Jones:** Hi. This is one of the most annoying product quirks in all of electronics. The center negative DC jack. Blurgh! Now you'll find this on a lot of old gear which we're looking at here. So what they do is your typical DC barrel connector like this, whatever you want to call it,

**Dave Jones:** the outer one is actually the positive, hence why the actual diagram is very descriptive there. And the inner central pin is negative. And this is opposite to pretty much the de facto standard these days which is the center positive pin. And if you go buy a plug pack on the market, almost every modern product is center positive.

**Dave Jones:** So why are some of them center negative? Well, let's take a quick look at it. Now the product I'm actually looking at here is an AND electronic balance or analytical balance. It's one of these laboratory ones, 400 grams maximum. Fantastic. They make really good balancers.

**Dave Jones:** And this one is center negative. How did I find out? Well, some idiot who shall remain nameless went and plugged in a 12 volt plug pack and just got the plug pack out of the big bin of plug packs that you have. And plugged it in, center positive.

**Dave Jones:** Wah, wah, wah, wah. Blew the arse out of the fuse. D'oh! Now depending on who you ask, this center negative thing, which is very quite uncommon these days in mainstream products, is that this actually used to be maybe even the de facto standard way, way back.

**Dave Jones:** And it's somewhere along the line it's flipped and it's become center positive. Why is it so? Now there might be several reasons for this, but there is one particular reason which is actually a very convenient design decision to actually do this, to make it center negative.

**Dave Jones:** So what we'll do is take this apart and have a look inside. There's a quick tear down inside for those who want to see it. Now this one actually has an optional battery pack, and that's the key here. And thankfully we can just get access to the nice little board down here

**Dave Jones:** which has our DC barrel jack and the fuse, which somebody blew the arse out of. And a little jumper connector over here. Now the first thing you'll notice about these DC barrel connectors is that they're usually three pins like this. And if you have a look at the schematic for this,

**Dave Jones:** you can see that it's fairly descriptive of how it operates. There's three separate contacts in there, and one of them is effectively a switch. So when you insert the jack, it can make or break that internal switch. Pin 3 is actually the switch contact.

**Dave Jones:** You can just ignore that and not use it, or you can short out pins 2 and 3 if you're just not using the switch. It doesn't matter, you can just use pins 1 and 2, or pins 1 and 2 and 3 connected. But if you want to use the internal switch in this thing,

**Dave Jones:** then pins 2 and 3, with no DC plug plugged into it, it's normally closed. But then if you plug in the DC plug, then it will actually break pins 2 and 3. And this is important. So I'll demonstrate that here. I've got my probes on pins 2 and 3,

**Dave Jones:** and you can see that's normally closed. But if I plug in my power connector, bingo, it breaks. Hmm, let's go to Davecad, because this is useful. Alright, so let's have a look at what's going on in this little board in here. Now here's our DC jack here, with the three pins 1, 2, and 3 like that.

**Dave Jones:** And this goes into a four-way jumper connector on here, and we'll have, I'll explain this in a second. But basically we're utilizing these three different contacts. Now, we've got ground, which is connected to the center pin, so it's that evil center negative that we're talking about.

**Dave Jones:** But we'll see why it's useful. Now, we have an optional internal battery. This one doesn't have it, but if it did, then the positive of the battery would be connected over to here, and hence pin 3, that switch contact on the DC jack.

**Dave Jones:** And the ground of the battery is just connected directly to the regular common, which is the center pin. So let's have a look at what happens if we don't plug in the jack. So nothing's plugged in here. Well, pins 2 and 3 are normally closed due to the internal jack in there.

**Dave Jones:** And bingo, you can see that the positive of the battery gets shorted and routed through to this pin here. Now, there's a jumper inside the product, which is just connected between here and here. And you can see that jumper link down in there.

**Dave Jones:** It's the center two pins. But now let's plug our DC plug into this thing, and this schematic is quite descriptive, because you can see when you push it in, it literally pushes this lever arm down like that when you actually push it in.

**Dave Jones:** So it's quite descriptive, and it actually breaks the contact between pins 2 and 3 there. So I just love that symbol. Whoever came up with that, genius, great. Anyway, you plug that in, and 2 and 3 are now disconnected. So the positive of the battery is completely disconnected from anything,

**Dave Jones:** and the positive, outer positive here, then goes through to pin 2, just like that. So it's effectively a double-pole, single-throw switch that selects between either the battery or the external DC jack. Brilliant. And that's one of the reasons why, one of the advantages of why

**Dave Jones:** having a center negative actually is useful. Especially back in the old day, you could just use the contacts on the switch to switch between battery and external power use with no additional circuitry required. There's no diodes, no nothing, no active circuitry, nothing fancy-pantsy,

**Dave Jones:** just a simple switch built in to the DC jack. It's fantastic. And that's one of the reasons there might be other reasons out there. I don't know. If you know of them, if you've ever designed products back in the day, and you know why they use center negative,

**Dave Jones:** maybe because, like, everyone else did that had battery products, and then it just, like, rolled over to other products. And if you know exactly when the tide turned, and we went away from the center negative, and it basically, center positive dominates practically every product on the market.

**Dave Jones:** But I believe there's still some products out there, like in Comms Gear, people have told me on Twitter, and other musical, I think Yamaha gear or something like that, somebody was saying, yeah, if you know of gear that still uses the center negative,

**Dave Jones:** but try and find it on a modern consumer product, you won't. It's always center positive. Because they probably have active stuff built in for the battery these days, you know, with lithium-ion batteries, lithium polymer, it's all active charging, and everything's, you know, like, it costs cents to do that nowadays.

**Dave Jones:** But back in the day, you know, it was a big deal. We don't want to waste money on a diode or something like that. So you use, or a couple of diodes, you use the switch built in the jack. Fantastic. So there you go.

**Dave Jones:** I hope you found that interesting. One of the reasons why they might have used center negative back in the day. Anyway, if you want to discuss it, as always, comments and links down below to the EEVblog forum, YouTube comments, all that sort of jazz.

**Dave Jones:** And if you like the video, please give it a big thumbs up, because, you know, that helps, and you've got to engage in videos, and, you know, so leaving comments is the best way to do that. Thanks. Catch you next time.
