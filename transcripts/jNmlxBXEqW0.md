---
video_id: jNmlxBXEqW0
title: EEVblog #919 - How To Charge Li-Ion/LiPo Batteries With A Power Supply
url: https://www.youtube.com/watch?v=jNmlxBXEqW0
source: youtube-asr
---

**Dave Jones:** Hi, I've got a bit of a problem. I've got one of these 18650 rechargeable lithium ion batteries. You're no doubt familiar with these. They're used inside torches and laptops and all sorts of products these days. But actually, I got

**Dave Jones:** this out of a torch I've got and that's the only product I've got which uses an 18650, believe it or not. So, I don't actually have a purpose-designed charger for this thing and it's just gone flat. So, what am I supposed to do? No

**Dave Jones:** worries. We've got a lab power supply. Beauty. Let's see if we can charge it. Now, charging these 18650 cells or any lithium ion or lithium polymer cells can actually be quite dangerous if you don't do it correctly. So, click here if you haven't

**Dave Jones:** seen my video. It's an old one on a complete tutorial on how to charge lithium ion battery. So, this will just be a quick video on how to use a lab power supply to actually charge these things relatively safely. And by the

**Dave Jones:** way, what I'm going to show you here not only works for 18650 cells, it works exactly the same for lithium polymer LiPo cells as well, which you get in all sorts of remote control stuff and things like that. They're basically identical

**Dave Jones:** from a charging point of view. Now, this particular one from Lumintop actually has a built-in protection circuit and it's in the end cap here and sometimes they're actually slightly longer in length than your regular ones that don't have the

**Dave Jones:** protection circuit in them. And this will actually mostly protect the thing, but we're not going to rely on that today. We're going to assume that we're using a charging an 18650 cell that doesn't have any protection built in.

**Dave Jones:** So, we have to know exactly what we're doing. Now, Lumintop don't actually have a data sheet for this thing, but it does tell us that it's a Panasonic NCR 18650B cell. It does say it uses Panasonic cells in particular. So, bingo, we can

**Dave Jones:** actually get the data sheet for this Panasonic cell. So, the specs, rated capacity 3,200 mA hours. They've put 3,400 mA hours. Nah, I don't know. We might not have the exact data sheet. They might have like an upgraded cell,

**Dave Jones:** or it could just be marketing wank. Who knows? Anyway, um it is going to have all the data we need for the charging, and we've got a charging graph as well. Beauty. Now, it must be said that not

**Dave Jones:** all 18650 cells are identical in terms of our charging same Some can be They're They're designed to be charged at a higher rate. Others might have a slightly different voltage depending on the chemistry in there. And I won't go

**Dave Jones:** into any of the details, cuz as I said, I've done a like a 40-minute video um explaining all the ins and outs of lithium ion charging. So, go watch that, but we'll do a quick overview. So, there's two things you need to know to

**Dave Jones:** charge a lithium ion battery like this. You need to know its nominal uh charging voltage, which is critical. This one is 4.2 volts. As I said, it can change depending on slight chemistry differences and other manufacturing differences, but 4.2 is pretty much the

**Dave Jones:** majority out there are going to be 4.2. And it must be 4.2 like plus minus 1%. It is quite critical. Uh so, all the lithium ion charger chips out there might be say half a percent accurate or uh something like that. So, we need to

**Dave Jones:** be fairly accurate on the voltage we're going to use to actually charge this thing. And just any regular 3.5-in digital multimeter should be at least 0.5% accurate, so it's going to be good enough for the purpose. In addition to

**Dave Jones:** the voltage, we also need to know the charging rate, nominal charging rate. In this case, the charging standard rate is 16 to uh 1,625 mA or what's called 0.5C, cuz the capacity is 3,200 mA hours. So, we need to charge this at half of its

**Dave Jones:** nominal rated capacity or nominal rated current. You just take away the hours there. 3.4 uh 3,400 milliamps is 3.4 amps. We need to charge it at half that or 1.7 amps. And charging lithium ion batteries is a two-step process. As I said, I have

**Dave Jones:** a video explaining much more detail than this. There can be like a pre-charge section and all sorts of stuff. Anyway, this is a very simplistic thing. There's a constant current charge mode where first of all it charges at a constant

**Dave Jones:** current for a period of time and then it goes into a constant voltage mode. And this way This is why these need intelligent charging ICs to charge these lithium ion batteries. But, our lab power supply, by the its very nature of

**Dave Jones:** having a constant current and constant voltage modes, is going to be able to intelligently do this for us, except it won't have an automatic cutout at the end. So, what we've got here, voltage on the Y axis, time on the X axis here.

**Dave Jones:** Now, this blue curve here is the cell voltage. And let's say the battery is dead and it's like at 3.25 volts or whatever, okay? It's It's a dead battery. And then we want to charge it up. So, we have to charge it in constant

**Dave Jones:** current mode. This other Y axis here is current. So, you can see this is the green is the current uh used to charge the cell. So, you can see it's a constant current. In this case, 0.5 C as

**Dave Jones:** we said before or 1.7 amps. So, we need to drive a constant current through this battery for a set period of time at 1.7 amps. And then, if we do that, the voltage will naturally rise like this, rise, rise, rise until it hits that 4.2

**Dave Jones:** volts, that magic 4.2 volts cutout voltage, which as I said is quite critical. Otherwise, you can damage the cell, it can explode, and heat up, do all sorts of horrible things you don't want to know about. So, you need to

**Dave Jones:** detect when it's at 4.2 volts and then switch into constant voltage mode like this, where then, when we're uh a constant voltage on it, the current will naturally drop down like this. And then, the cutoff point is usually typically

**Dave Jones:** around like 10% of the charge current, for example. So, you know, 170 milliamps, for example, might be a cutoff thing. It doesn't show you that here, but anyway, there's different schemes for that. But, that's the basic two-step charging process. And the great

**Dave Jones:** thing about using a lab power supply like this is that they have constant voltage and constant current modes. So, we can set our voltage our maximum output voltage of, you guessed it, 4.200 volts. And this is quite an accurate

**Dave Jones:** power supply, this uh Rigol DP835. It's like 0.05% accurate. So, yeah, we can be pretty confident that 4.2 is going to be 4.2 for our purposes, more than good enough, order of magnitude better than what we want. And then, we need to set

**Dave Jones:** up our constant current mode or our maximum current that can be drawn of 1.7 amps or 0.5 C for this particular cell. And the good thing about a lab power supply like this is it will automatically switch It It will never

**Dave Jones:** ever deliver more than 1.7 amps, and it'll never ever deliver more than 4.2 volts. So, if we go back to our graph here and have a look at it, this is exactly what we needed to do. In this

**Dave Jones:** mode here, cuz we've got it set to 4.2 volts maximum, in constant current, it'll draw that constant current. It'll try and draw more when you initially switch it on, it'll try and draw more current, but it'll be limited by that

**Dave Jones:** 1.7 amps that we set. So, we'll get that constant current mode. And then, when it actually reaches 4.2 volts, the power supply won't let the voltage, that blue line, go any higher than that. So, it will naturally limit that, and bingo, we

**Dave Jones:** will be in constant voltage mode. And if you actually had, a lot of power supplies will have a constant current mode LED on here. They'll show you when they're in constant voltage or constant current mode. So, lab power supplies are

**Dave Jones:** perfect for this sort of application. But, as I said, the only thing it's not going to do is automatically cut out at the end. It could if you had some fancy pants program or supply, which this one is, um but I'm not going to use that cuz

**Dave Jones:** most people will not have a programmable supply. But, look, the charging is specified at a maximum of 4 hours. So, we can just set a uh stopwatch uh or a countdown timer for 4 hours and get it to go ping when it's finished. So, I do

**Dave Jones:** happen to have a an 18650 uh battery holder lying around, so we can hook that up across here cuz as I said, the voltage across here is critical. But, if you set your 4.2 V limit on here, worst

**Dave Jones:** thing that's going to happen is you're going to get a voltage drop and you're going to get a lower voltage on here, which isn't necessarily a problem, but it's but it can't go over 4.2. So, you are actually protected, your cell's not

**Dave Jones:** going to not going to explode on you. Okay, and we've got our uh 4.2 V maximum voltage set up there and our 1.7 amps. So, let's go and switch this thing on and it will enter that first phase, that

**Dave Jones:** first constant current phase of this. So, we should see it go to 1.7 amps and limit. So, let's switch it on. Make sure you've got the battery around the right way and let's switch it on. Bingo, 1.697 amps. And the other thing we want to do

**Dave Jones:** is to protect it, we want to uh set our timer. So, let's go in there. I'll set my timer to 4 hours. Let's start that. It'll count down. This will beep at me at the end of 4 hours cuz you don't want

**Dave Jones:** to leave this running overnight or something like that. You can overcharge the cell, damage it. You don't want to do that even though it's sort of a bit self-limiting. Just Yeah, and you want to cut it off after about that nominal 4

**Dave Jones:** hours. And you want to use your battery, don't you? But, what you can see is that the voltage on the cell is slowly rising with that constant 1.7 amp uh charge on there. So, that's exactly what it's doing. It's charging at a fixed 1.7 amps

**Dave Jones:** cuz we set that and the voltage is slowly slowly going to rise and you'll find that after maybe, I don't know, time says 100 minutes here, whatever it is. It'll change depending on the cell and all sorts of stuff and and the

**Dave Jones:** initial discharge voltage and how much capacity was in there, etc. So, it'll charge up until once it hits 4.2 volts, the power supply will automatically switch out of constant current mode and we'll have 4.2 volts on here and then we'll see the

**Dave Jones:** current start to drop. So, I'll leave that running and get back to you. And after 2 hours, we're still charging at 235 milliamps. So, there you go. We'll wait I'll wait until it gets down to, I don't know, maybe 5% of the 1.7

**Dave Jones:** amps or thereabouts. Sorry about the focus on this. I goofed it up, but you'll be able to see it that little CC mark for constant current mode and you'll be able to watch it switch to a constant voltage mode once it hits 4.2

**Dave Jones:** volts. And just over 3 and a quarter hours, oops, I stepped out and I let it go. Well, further than I wanted, but it it doesn't matter. It's down to 26 milliamps now and that's only like 1.5% of our original charge current and

**Dave Jones:** that's probably as low as you need to go. It's diminishing returns from this point. Most of the energy's been put back into this thing. So, leaving it longer is not going to help. As I said, anything under that 10% mark, 5% maybe,

**Dave Jones:** would be a typical cutoff figure of that 1.7 amps that we were charging at there. So, yeah, we'll call it quits. And you don't want to actually trickle charge or float charge lithium-ion batteries like this because it can actually build up or

**Dave Jones:** plate the uh, lithium inside the metallic lithium inside the battery and yeah, you don't want to do that. They're not designed for that. There are, um, there are chip sets designed for float charging and they use like a pulse, uh,

**Dave Jones:** slow pulse type, uh, system which I've mentioned in the previous video, I think. So, yeah, you definitely don't want to leave this over running overnight. Overnight probably won't, you know, it's not going to leak and damage your battery too much, but you don't

**Dave Jones:** want to, you know, leave it too much further. Anyway, you want to use your battery. So, take it off once it drops below 5% or 10%. Yes, you can actually, uh, take it off at any point during this

**Dave Jones:** charging process and use it. You can take it off when it switches from constant current to constant voltage charge mode, for example, and you might, but it's only going to have like half the capacity, uh, put back into it or

**Dave Jones:** something of that order. So, you know, it depends on how much charge you want to put in. But, as I said, once you get below that 5% and 10%, 5% uh, figure here of your, uh, half C charging or your charging rate, then it

**Dave Jones:** is very much diminishing returns. So, at the end of that, we can just switch that off and bingo, we've got a fully charged battery, you little ripper. And yes, you'll see the voltage, uh, slowly drop down and it'll stabilize at a

**Dave Jones:** particular, uh, value. So, there you go. I hope you enjoyed that, uh, video of how to charge a lithium ion, uh, rechargeable battery, not lithium primary. Definitely don't do this on lithium primary batteries like coin cells and other, uh, type batteries. Uh,

**Dave Jones:** lithium ion rechargeable batteries with your bench power supply, you little ripper. If you liked it, please give it a big thumbs up. Catch you next time. Hi, it's lithium ion battery tutorial time. There are actually two different types. Don't confuse these with lithium

**Dave Jones:** ion and lithium polymer cuz they're the same thing. In fact, they're the, uh, new type of anode material. I won't go into the construction of batteries. You can look those up yourself. But, the anode in there You two different types

**Dave Jones:** of materials. This is uh, very simplistically what's inside a lithium ion charger.
