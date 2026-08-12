---
video_id: qEpkVa_ysaw
title: EEVblog 1510 - $699 Rigol 12bit HDO1000 Teardown - WOAH!
url: https://www.youtube.com/watch?v=qEpkVa_ysaw
source: youtube-asr
---

**Dave Jones:** Hi, in two recent videos we took a look at the new Rigol HDO 4000 series 12-bit oscilloscope. None of that 8-bit rubbish, but it wasn't exactly a hobbyist-friendly price. It was like $2699 or something like that US dollars

**Dave Jones:** starting from. But, as promised, Rigol sent in their new 1000 series scope. It's white instead of black. I don't know. Anyway, be aware. Um, it's the new HDO 1000 series. It's also 12-bit. It's a lower sample rate, 2

**Dave Jones:** gigasamples per second instead of 4 gigasamples per second, but it's still a 12-bit four-channel scope. And this one starts at $699 US dollars. So, whoa. Let's take a look because this is like a serious bit of hardware for a like a hobbyist-friendly

**Dave Jones:** price. But, of course, just like the 4000 series, it's lacking all of your modern stuff to get the price point down, like mixed-signal digital input, arbitrary waveform generator. But, if you need 12-bit performance, you can get it for 699 Yankee bucks. You know, so

**Dave Jones:** here on the EEVblog, don't turn it on. Take it apart. Except, I can't use this cuz it's a Phillips and it's going to have one of those Torx rubbish things. Let's go. But, unlike the 4000 series, there's no

**Dave Jones:** external battery pack connection. Yet, looks like they're still using the case cuz it's still got those moldings in there, but they don't have the slidey door on there. They've filled that in. So, they're reusing the case anyway. We

**Dave Jones:** still get the 10 megahertz reference out, 10 meg reference in, external trigger, auxiliary out. And you get your LXI LAN, your USB device. And you still get the HDMI output at this price point. Nice. Voiding the warranty in 4K

**Dave Jones:** resolution. Oh, yeah. And it does lack the 50-ohm input of the 4000 as you'd expect to save cost, but it's still on the silk screen. Come on, seriously. So, what we expect to see in this is the uh same 12-bit um

**Dave Jones:** acquisition ADC and the same uh front end as well, but uh not including that uh 50-ohm path. And look, yep, they've got the same metalwork. They just haven't included for the battery cuz that's where the battery contact was.

**Dave Jones:** And they've just yeah, they've just added in the extra uh plastic in there and also or haven't punched it out or something. And of course, that's the smart thing to do. You reuse all that. I expect probably a similar main board,

**Dave Jones:** but probably a different FPGA, a lower cost FPGA, because it probably doesn't have the same grunt as the big daddy 4000 series because, you know, that's it's not exactly cheap. Oops, silly me. I goofed up the price of this thing. Um

**Dave Jones:** the two-channel version starts at $699. Yeah, it's um not like you can upgrade it, of course, from two channels to four channels. They physically would not, I'm sure, physically, even though I don't have the two-channel version, they physically would not let you do that.

**Dave Jones:** Anyway, it looks like we've got the same two fan arrangement here. So, yeah, it's all exactly the same. Have to leave that sucker off. And yeah, we're yeah, it's going to be exactly the same. We've got the same

**Dave Jones:** bird that we had before. Everyone uh corrected me on the bird. As expected, I think this is going to be near identical. Um it's got exactly the same heatsink arrangement. Everything's the same. I'll I'll take definitely take the

**Dave Jones:** uh front end off um and take off this, but the applications processor is probably the same. I'd say the FPGA, they're going to be cutting uh cost on that. And all of your uh power supply that looks exactly the same as well.

**Dave Jones:** That's that off-the-shelf uh module that we uh saw before, but it doesn't have the uh battery board in there. So, they're saving a bit of cost cuz they went to a bit of effort to, you know, do that. And that all cost money to switch

**Dave Jones:** in the battery uh option. They got the same board up here for the 50 hertz line trigger, not that 60 hertz rubbish. Except of course they haven't populated the circuitry up here which was the active probe circuitry. So they won't

**Dave Jones:** have that board physically installed of course, but everything else looks absolutely the same. Well, I'm actually stunned by what I'm seeing here. It looks like it has exactly the same front end with the 50 ohm path that 800

**Dave Jones:** megahertz bandwidth front end. I notice that one of the custom ADC A6 is missing. So that explains half the sample rate two gig samples per second instead of four. So obviously the one ADC is handling all four channels here

**Dave Jones:** and you'll notice that there's four differential pairs going in there. So that's how they were getting double the sample rate before. So that's the only thing missing. The FPGA is exactly the same. So this is running the UltraVision

**Dave Jones:** 3 architecture. It looks like all but there's only one difference in the memory up here. It's the same rock chip over here. I'm absolutely shocked. This supposedly 200 meg bandwidth scope has a genuine 800 megahertz front end with the

**Dave Jones:** 50 ohm capability and it doesn't even what the software inside this thing doesn't have the 50 ohm capability. So it's yeah, it's on the front for a reason cuz it's physically in there. I can't believe this. The hackers are absolutely wetting

**Dave Jones:** themselves right about now. I'm going to take a high res photo and we'll do some direct comparisons to see if we can see any differences. Wow, I can't believe it. Check this out. They've used clearly the same PCB. It's a different

**Dave Jones:** production run as you'll see, but it is the same PCB. Obviously they've designed this so that they consolidate the PCB on both and it's near identical populated apart from the extra ADC and some stuff for the front panel active probe connections and

**Dave Jones:** that's it. Look, I'll get rid of my ugly mug here, okay? So that you can see it. Now, I've got two two photos. This is the HDO 4000 which is a brighter image and I can switch this to the HDO 1000, okay? And now we

**Dave Jones:** can switch back and forth. So I've done my best to align this, but you'll see there's a few component positional like minor as in they've mine in mine very minorly shifted things as I'll tell you in a minute. Unfortunately, with

**Dave Jones:** Earth and View, if I turn the paint on, it sort of like sort of like resizes the image there if I've got the paint on, but still it works. So like clearly, we're missing the second ADC here, okay? Right, that's

**Dave Jones:** all to do with the front panel active probe compensation. So yeah, all of that stuff there, right? This chip here, whatever that is, is still missing on both and then we've got a little loan I think that was a low noise regulator

**Dave Jones:** from the previous teardown. I'd have to watch that again, but that's obviously missing. Then we've got a couple of filter caps missing here. One's a little three-pin jobby. So clearly, what's going on here is the one ADC here which

**Dave Jones:** is a custom Rigol chip set. That's their 12-bit thing. It's got the four pairs in here, the four differential pairs which all come out of here, that goes into there, that goes into there and that goes into there, but that is the only

**Dave Jones:** difference. You'll notice the Arctic 7. Check out the part number right here. It's exactly the same. It's exactly the same. So they haven't saved any cost there at all and there's one number difference in the DDR I think it's three or four memory, I

**Dave Jones:** can't remember which one, but this is a 2 DP47 and this is a 2GP 47. And the second line of the number there is exactly the same. I have to look up that and put that overlay that later. But as you can see this QR code

**Dave Jones:** here is different for these and that's moved from over here. If I move my paint here, you'll notice that the day code down here the 37th week 22 for the HDO 1000, okay, that's moved to here. This is the 34th week 22. So this would just

**Dave Jones:** be like a natural difference in builds as they're iterating these things. And yeah, but I have no doubt that they're going to consolidate the PCB once they've ironed out all the production, you know, everything's fine and hunky-dory. The two scopes will have

**Dave Jones:** absolutely identical boards in them except for the chipset here. You've got to be kidding me. Now if you have a look at the front end down here there is no difference. It's still got Look, it's still got the 50 ohm path.

**Dave Jones:** You remember how it goes Oh well sorry, well yeah, it goes through this relay, goes through that relay and that's the 50 ohm path and then it's got the 1 meg path which then this is the AC coupling

**Dave Jones:** here or DC coupling and it goes through the relay and then there's the 1 meg path. And it's the exact same chipset. Of course it's the same chipset. That's what I expected. But there obviously this has this 200

**Dave Jones:** megahertz scope. That's the highest bandwidth they sell in the HDO 1000 series. It's clearly got an 800 megahertz bandwidth with 50 ohm input termination. This is absolutely identical. I guarantee if you went in there and measured every single

**Dave Jones:** component it would be the same. Wow. This is like a hacker's dream come true I think. Well you've got to pony up the extra $999 for the four if you want the four channels. But for that it looks

**Dave Jones:** like in theory you get all the same hardware except one less ADC, so your sample rate drops, which is not great if you're talking 800 meg bandwidth and you know, 2 gig samples per second for a single channel and then you lower it,

**Dave Jones:** but still this is crazy. Anyway, you'll notice other interesting little things like around here for example, on the HDO 4000, it's which is a older revision board, they've actually got the voltages 1 V0, 1 V8, 1 V2, they've vanished on

**Dave Jones:** the newer one. So, that's interesting and you'll notice like little small positional changes that I've noticed. Check out over here as I change this. Notice the parts haven't changed, but like that little cap there, watch that sucker, right? It it's not due to just

**Dave Jones:** differences in my camera angle. They they're there's a subtle shift in the components. They've made a subtle to get an extra trace through the PCB design has gone need to like turn it to the right angle, shuffle them a bit this way and I'll be

**Dave Jones:** able to fit an extra trace in there or something. So, they've done some shuffling there. Look at that big unpopulated inductor there, which is unpopulated on both, but you notice how the silk screen, it's it's physically and and the pad is expanded. It's a

**Dave Jones:** slightly different footprint and they're still unpopulated. So, I don't know. If you'll take a look up here at these fan connectors, you'll see that these will actually slightly shift, but it looks like the footprint stayed the same. It's just the

**Dave Jones:** pick and place and it's just reflowed. There's an offset there on the reflow. So, it's So, we've got our JTAG header up here. The I think serial UART was here, wasn't it? I haven't probed that yet. I might have to probe it. I just

**Dave Jones:** cannot believe that they used exactly the same front end. It's the you know, sure, okay, they've spent the NRE on the chip, the non-recurring engineering is what NRE is. They spent the money developing the chip, so you're going to

**Dave Jones:** use it in here, right? They're churning these things out by the I don't know. I I going to say millions, not quite. But anyway, they're turned them out. So, I expected them, of course, because it's the same 12-bit everything's the same,

**Dave Jones:** right? And the 1000 only has a 500 microvolt per division front end, but we know on the HDO 4000 was only a software improvement. It's not a true 100 microvolt per per division front end. So, it's exactly the same front end and

**Dave Jones:** it's got the 50 ohm path. Yet, this thing in the software does not let you enable a 50 ohm input. But, it's there. It's physically there with an 800 MHz bandwidth. So, if you can somehow hack this thing to try and like fool it into

**Dave Jones:** thinking cuz you just simply copy the firmware and like make it into a like a HDO and it doesn't know the difference. That is a you know, maybe maybe there's like a couple of resistors that set the model

**Dave Jones:** somewhere. Maybe, but I don't know. I I'd have to sit here. Leave it in the comments if you can actually see spot anything. I mean, I haven't spent a lot of time with this. There's another chip missing in here, of course. Um that's

**Dave Jones:** just a regulator. It's It's the same product. Wow, I did not expect this to be exactly the same product. The application processor over here is the same. The DRAM's is exactly the same. And they're going to consolidate into the same

**Dave Jones:** board. I'm sure in 6 months time if you buy the both products, they'll be exactly exactly the same revision boards and everything's hunky-dory, but yeah, there's no difference. Oh my goodness. So, what sort of margin are they making

**Dave Jones:** on these? I mean, you know, they've included all the bells and whistles in this. It's the same FPGA. It's got like and land They haven't even They haven't even skipped on like the HDMI output or anything like that. They've haven't even

**Dave Jones:** skipped on the 50 ohm. It's It's embedded in there. You know, external 10 MHz reference, for example, they're including all that sort of stuff in this bottom-of-the-line HDO 1000. It's a really interesting move from Rigol to make uh you know, such

**Dave Jones:** powerful hardware in their low-end. Usually, every We've seen it time and time again with the oscilloscope teardowns. They'll the probably, you know, they'll move they'll remove things to um do this, but it contains the same hardware as the HDO

**Dave Jones:** 4000. Just leaving off one ADC chip. Surprisingly, even did that. So, as the hardware in the oscilloscopes, the chips that go into making up this thing um cost, you know, a relatively so little in terms of the margin of the that

**Dave Jones:** they're making on the product. I mean, obviously, the margin's going to be way higher on the HDO 4000 cuz I identical hardware apart from the one chip. We're talking dollars, you know, tens of dollars difference in a $2,000

**Dave Jones:** difference scope. So, maybe they're you know, they're not making much if any margin on the I'm sure they're making some, right? They'd be making some margin, otherwise, they wouldn't do it. On the HDO 1000, and they're just making

**Dave Jones:** a killing on the HDO 4000. This is unbelievable. I just love doing this. I could do this all day, but leave it in the comments down below if you can spot any subtle differences, cuz I am shocked. I think there's going

**Dave Jones:** to be quite a few people working on hacking this HDO 1000 series. Just I mean, how much does this 12-bit ADC cost that they're that is the only component missing? And the active probe front end is physically missing the board and the

**Dave Jones:** connections and the cables and a couple of parts on the board to enable that and stuff, but come on. So, there's no changes under my head there. Just disabled my head, so I can turn that back on. And yeah.

**Dave Jones:** Well, there you go. That is a huge Like, is that the first time in this oscilloscope market that there's been such a same exact same hardware and board used in such a price differential? We're talking $699 to $26.99. We're talking a

**Dave Jones:** $2,000 difference and they haven't changed the front end. But then again, they that's amazing thing with front ends these days. They can get so damn good that you can build an 800 megas, you know, a decent performance 12-bit

**Dave Jones:** dynamic range front end, like low noise, you know, 500 micro microvolt per division front end, uh 12-bit uh performance, you know, low noise performance with you know, and you can afford to not even leave off like the 50 ohm thing. Like I

**Dave Jones:** got what? What? Unless they got some plan. Maybe this scope is so early to market that they do plan on adding the 50 ohm capability to that. Wow, I'm absolutely amazed. So, there you go. That's all for this video. I'm not going

**Dave Jones:** to analyze it further cuz I've already done in the HDO 4000 video. So, thoughts and comments down below. Just wait until the hack happens. I somebody somebody's going to buy one of these and they're going to get to work. And yeah. Anyway,

**Dave Jones:** I might try if if I I'll do the UART thing, but I'll leave that to a second channel video. I might see if I can get something out of the UART and stuff like that. But yeah, anyway, interesting,

**Dave Jones:** huh? Catch you next time.
