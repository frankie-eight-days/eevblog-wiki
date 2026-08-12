---
video_id: yVqLx7SlHVg
title: EEVblog #622 - How To See Through Objects With A Thermal Camera
url: https://www.youtube.com/watch?v=yVqLx7SlHVg
source: youtube-asr
---

**Dave Jones:** Hi. Now, it's a very common thing in the electronics design industry to measure the thermal performance of a product, especially when you've got like a reasonably large system like uh something like this that's got fans in it and you've got to manage the thermal

**Dave Jones:** performance. I've talked about this a lot on the blog and well, how do you measure it? Well, there's many different ways to measure it, but one of the big mistakes you can make, one of the traps for young players, is to measure things

**Dave Jones:** with the lid off like this. And you've seen me do it in videos cuz I'm just getting like ballpark temperature measurements, but as you should know, the uh with something like this that's got a fan in it, with the lid off,

**Dave Jones:** you're not going to get the true temperature measurement of the devices in there. They're actually going to be hotter than the what they should be. Why? Cuz you haven't got the proper thermal management and the airflow going over the devices, over the heat sinks,

**Dave Jones:** and things like that. So, really, if you want to properly characterize and measure the temperature of a device or the thermal performance of your product, you need to do it with the lid on and everything in place in and they could

**Dave Jones:** have uh air ducting guides inside, for example, you've seen those uh various times in product teardowns and things like that. So, that's all well and good, but how do you measure the thermal performance with the lid on? And of course, one of the best

**Dave Jones:** tools these days, and they're becoming lower and lower in cost, are one of these uh FLIR thermal imaging cameras. This is the E8, very nice, 320 by 200 resolution. Haha, brilliant. And these are great for getting uh thermal uh

**Dave Jones:** measurements of your products like this, overall thermal map, and also individually measuring the thermal performance without having to get your usual uh multimeter and your thermocouple and trying to attach it and stuff like this. These can work really

**Dave Jones:** well, although ultimately, uh thermocouple attachment is probably going to uh end up being the most accurate. These are great if you've got the lid off, but then your temperature measurements inside aren't going to be accurate. So, how do you solve it? Well,

**Dave Jones:** you can't just whack the lid on cuz this is no good anymore. And then, yeah, would uh, often you would have to uh, attach uh, thermal couples through the vent holes and then actually connect them to the devices you want to do, then put the

**Dave Jones:** lid on, and you've got to have multiple thermal couples and all sorts of things. It's a really nasty piece of work. So, how can you measure the thermal performance, especially using one of these thermal imaging cameras, with the

**Dave Jones:** lid on and with all your air flows in place? Well, there's a neat little trick you can use to do it. I'm going to show you. Cling wrap. Beauty. So, taking a product like this as an example, uh, when you

**Dave Jones:** got the lid off like this, yeah, the fan's going full ball, sucking out, trying to suck out the air, but where's the air coming from? Well, just around the inlet to the fan there. It's not coming from anywhere else. So, it

**Dave Jones:** doesn't get to flow from the vent holes here and here. That's what the system is designed for. Air flows into this hole, into this hole, over all of the electronics, and then over these heat sinks here, and then out the back like

**Dave Jones:** that. That's how they've designed the thermal management in this product. Well, with the lid off, all of that's ruined. It's just being sucked there. There's no air flowing over either the electronics or more crucially, these heat sinks at the back here. And the

**Dave Jones:** heat sinks are designed to work with air flowing over them. They're really, uh, you know, if you just put them in still air, they're not very efficient at all. They're vastly more efficient with that air flowing over. So, if we take our

**Dave Jones:** thermal imaging camera here, we can actually see parts of our product that are lit up there. We can see individual chips and uh, relays down in there that are lit up. You can see that the coils on the relays are energized. You can see

**Dave Jones:** our five heat sink devices up here. You can see our transformer over in the corner. And that's all fantastic, but well, these aren't a true temperature measurement. You can see up in the top left corner of the screen there, that

**Dave Jones:** that device in there, you know, 70 80 odd degrees, 85 degrees, something like that. But that's not what it will be with the lid on. It'll be lower than that. So, to solve that problem, yes, we can actually use some cling wrap. We can

**Dave Jones:** just put it over the top of the product where the lid is going to be or whatever covering it is on your particular product you want to test. And of course, being that on, it works like a lid and

**Dave Jones:** it allows the air to flow exactly how it was designed in the system. But as I'll demonstrate now, it's pretty transparent, although not 100%, but pretty well transparent to that infrared heat energy. So, you'll be able to use

**Dave Jones:** your thermal camera to see right through this with all your air flow in place. Let's check it out. All right, let's try this out and see if it works. I've got my FLIR E8 mounted on a an extension arm

**Dave Jones:** here. It doesn't have annoyingly doesn't have a tripod mount on it. I know you can physically hack them to actually add that, but anyway, here we go. It's nice and set up. It's stable. It's actually measuring that heat sink in there, see?

**Dave Jones:** So, the top left temperature up here, that's what the cursor right in the middle. 73.4. So, that heat sink down in there is about 73 and a half degrees or thereabouts. So, I'm going to get my cling wrap now. Here

**Dave Jones:** we go. And I'm going to put it over it. Let's see if it changes. It will change. Of course, there is some loss by doing this, but you'll notice that the heat map will stay exactly the same. It does

**Dave Jones:** not distort the map. So, you can should be able to see it coming across. So, it's 74 74 and it's dropped to 79 and a half. So, there you go, 70. So, it's dropped by 4°. That's instantly. Now, if you leave

**Dave Jones:** it there, it might actually come back up to temperature if you leave it there long enough. So, it's yeah, it's got some loss. So, your absolute temperature is going to be out a bit, but you'll see that that heat map

**Dave Jones:** is still there. That image is not distorted at all. So, there it is. Look at that. Fantastic. So, 4 or 5° drop, you can compensate for that, but the whole idea is that you can still see the thermal image of it and the flow.

**Dave Jones:** And if you're lucky, you'll be able to see the air flow as well through your product. Fantastic. Now, if we take a look at the overall product here, we've got a temperature range, as you can see in the right corner here of, you know,

**Dave Jones:** 83° down to about 27.6 at its lowest part here. Now, what I'm going to do is I'm going to try and leave the FLIR camera in position here and cover it with cling wrap and actually see if we can see a difference.

**Dave Jones:** But, what I'm going to do instead of having the fan blowing out, I'm going to have the fan blowing back in and then see if we can see, maybe if we're lucky, some air flow coming out the holes out the side here,

**Dave Jones:** some air flowing into it. Cuz otherwise, most of the hot parts, as you can see, are up the back of the unit there. So, this isn't a particularly great example from that aspect. So, I'm just going to flip the fan around so that it blows

**Dave Jones:** back out so I can simply just take that out. And ta-da! Now, it's blowing into the product and coming out the vent holes on the side. And yeah, we should, maybe if we're lucky, see a heat map. Ooh, there's my hand.

**Dave Jones:** And here we go. I've had the cover in quote marks on for a little bit and you can maybe you can see a difference down in here. You can see that the heat has more spread and is flowing across here.

**Dave Jones:** You'd have to read individual temperature points to actually see it but the you can see that the thermal spread across these parts here has also changed and gone higher. But once again, you would have to get in there and actually measure those

**Dave Jones:** individual points and you'll notice that the maximum temperature to minimum temperature has also dropped as well. Now, I've been sneaky and I've covered up this left hand vent over here. So, I've only got the air flowing out the

**Dave Jones:** right hand vent. So, you can actually probably see maybe some of the heat spreading across not not out this side but it's spreading in this direction like this. It's probably hard to see. Not the best example but hopefully you

**Dave Jones:** can get the idea. And if you got one of these thermal cameras, you can play around with something like this. So, if we move the camera over towards the side of the chassis over here, you can see that this air flow is flowing out over

**Dave Jones:** this what would ordinarily be a cool area of the board over here and it's flowing all towards this exit bar point over here. This vent hole on the side cuz we're forcing air in at the back here and it's flowing over here and

**Dave Jones:** going there. But once again, you'd have to get in there and measure individual temperature points. But you can see how the concept actually can work. Got this Tektronix TDS 3054 oscilloscope you've seen in a previous video and yes, I've

**Dave Jones:** wrapped it all up. Check it out. Woohoo. So, as you know in previous video, this thing actually stops working if you don't have the fan on. It overheats in like a couple of minutes and the software detects that and actually shuts

**Dave Jones:** the thing down. So, what I've done is I've wrapped it in plastic. It's dead wrapped in plastic. All right, and I've basically sealed up all of this side. So, the fan sucks in here like this over the main

**Dave Jones:** ASIC down the bottom which actually gets hot, the main ADC chipset and all that sort of stuff. So, it gets really hot. That's the thing that's shutting down. So, the air goes in here. It's got nowhere to go but out this other side.

**Dave Jones:** Ordinarily on this thing, the vent holes are over here somewhere, but I've just got it coming out the end cuz I just want the air to go in and flow through and go over. All right, here we go.

**Dave Jones:** Let's power it up and see what we get. I'm capturing this video cuz you can actually stream out of this via the USB. So, here we go. Look, you can actually see the uh There we go. Look, you can see the main

**Dave Jones:** ASIC right up there heating up. You can see the four uh front end chips, the four front end hybrids. They're all heating up. The uh probably analog to digital converter in there is the one at the back, the

**Dave Jones:** ADC. I can't remember. Um this one here, that'll be the transformer core powering up. Uh and yeah, some of the front end components there on the power supply. So, that's the entire power supply board in there. This is the DC to DC uh

**Dave Jones:** converter powering the main board. So, there's some voltage regulators. They're just uh free-standing TO-220s there. And uh there we go. Hopefully, can we actually see I think we You see some I think we can see some of this air

**Dave Jones:** flow happening here cuz this is all cold stuff down here, but it's it what should be cold, but it's not because that air flow is happening and flowing out this side of the board over here. There you go. So, it looks like we are

**Dave Jones:** getting to see a bit of air flow and maybe if you use your imagination and see some heat spreading out that way or maybe not. Maybe not. But, yeah, I can definitely see a heat pattern flowing out that way. So, that's

**Dave Jones:** that is really quite neat. We can leave that running for a bit, of course, and uh it shouldn't shut down like the um like it does without the case because this is effectively you've got a case on it and

**Dave Jones:** that air flow. I mean, this That's the thing. This cling wrap is not you know, it's not that great, okay? It's going to have loss in it and everything else, but it allows you to see the thermal profile through that without

**Dave Jones:** distortion, really. And it gets most crucially it does get that air flow happening, which is what you want to test your real product. So, that's working really quite well. I'm rather uh rather pleased with that.

**Dave Jones:** There you go. Yeah, all that stuff over there should be Yeah. Yeah, you can see it all heating up around here. And all flowing out. That is neat. And you can see the fan, of course. You can see the motor in the center of the fan

**Dave Jones:** there. Okay, what I'll do now is I will change the image mode because you can see all of the creases. You can see the cling wrap and everything else, you know? It really screws things up because this camera is so good that it has this MSX

**Dave Jones:** technology, which overlays a true image in the true visual image over the top so that you can see more detail and I love it. It is absolutely brilliant. But if we switch to it, there it is, thermal MSX

**Dave Jones:** and you can see the you can see the physical cling wrap on there, the reflection from my studio lights and the creases and all sorts of stuff. But if we put it in traditional thermal mode, bingo, there it is and

**Dave Jones:** that looks much better. I like it and hopefully, yeah, it's it's hard to tell but you can sort of see the heat spreading out towards this corner of the thing where it's all escaping right out here. So, that

**Dave Jones:** is brilliant. I mean, that is basically so you get the benefits of having that case on there and getting your true air flow, but look, it's like this thermal imaging camera is seeing right through the case of the instrument. It's

**Dave Jones:** fantastic. I love it. So, there you go. I hope you found that a useful little tip there of how to see through your product with a thermal imaging camera. It works remarkably well, actually and yes, this thing is still going. It hasn't rebooted, so

**Dave Jones:** it's working just like the real thing with the case on. Fantastic. I hope you enjoyed it. Catch you next time.
