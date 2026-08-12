---
video_id: mkZFHEeQkQI
title: Unusual Repair - Part 2 - Thermal Boogaloo
url: https://www.youtube.com/watch?v=mkZFHEeQkQI
source: youtube-asr
timestamps: {"0": 0, "1": 26, "2": 55, "3": 88, "4": 112, "5": 126, "6": 156, "7": 181, "8": 209, "9": 234, "10": 263, "11": 282, "12": 317, "13": 358, "14": 389}
---

**Dave Jones:** Hi, you might have seen this BM786, which was returned from a customer. It was brand new. Still got the wrapper on the screen in a recent video where it had a firmware issue where it you would turn it on and it would just stay on this all the segments would stay on the screen like that. In fact, you can actually make it do this by holding down the record button and force it on like that and all the segments come on. But, that's it had nothing to do with the

**Dave Jones:** button. It was somehow the firmware was locked up in this thing and of course I fixed it in that video by reprogramming it because there's a programming header inside the battery compartment there. So, I tagged it. I shipped the customer new one and I tagged this one. There's the serial number for those playing along at home. I sent Brymen the video and they have gotten back to me and said, "Oh, they've passed on to their R&D team. They're not quite sure what the deal is here." But, presumably

**Dave Jones:** they've never seen this fault before as nor have I. And that was actually a very surprisingly very popular video and there was a lot of opinion on this, but a lot of people wanted me to do further testing on this. And the leading theory is that the flash in the flash memory in the internal processor in this thing, which runs it, was corrupt either corrupted in some way or it might have been accidentally incorrectly reprogrammed at the factory after it was tested and after it was

**Dave Jones:** calibrated cuz I have checked the calibration on this thing and it is bang on. So, it definitely worked and went through its whole calibration cycle and was put in the box and shipped to me and then I shipped it to the customer and then all of a sudden it just didn't work anymore. So, whether or not there was a last minute firmware update, which the firmware in I can't see how cuz this hasn't changed. Firmware hasn't changed in this in a quite a long time and

**Dave Jones:** Brymen do not have old stock. They actually manufacture to order, which is kind of annoying for someone like me who can't keep track of stock properly. And oh, emergency, I've run out of stock. Oh, I'm sorry, it's going to be 2 months. We have to manufacture to order.

**Dave Jones:** Um so, yeah, uh Brymen do not keep stock of this thing. So, it's not like it's old stock or anything like that, and they just uh switched out the firmware at the last minute. Um none of that. So, the leading theory is that the cosmic ray or the flashing this uh processor is somehow bad, and uh potentially, we might be able to um provoke it into failing again. Uh I haven't been able to at the moment, but might be able to provoke it into failing again by maybe thermal cycling this

**Dave Jones:** thing. So, uh that's what we're going to do in this video. I'm just going to thermal cycle this thing. I'm going to alternately chuck it in the uh fridge, and then uh the heater, uh thermal chamber that I've got, I'll set that on hot. And then, so I'll meet it I'll kind of like, you know, thermally shock it between hot and uh cold kind of thing. I won't put it in the freezer. I won't be, you know, maybe if the regular fridge doesn't work at 2 or 3° or whatever,

**Dave Jones:** then uh we might try thermally shocking it with the freezer, but how do we know how cold it because, you know, this is like a sealed unit. How do you know how long do you have to leave it in there um to like get it cold in the actual processor cold inside? Well, it's actually got an internal temperature sensor, and um a little uh tip here, um normally, you plug it into temperature mode, you need an external thermo couple, but aha, if you just short it out with a shorting

**Dave Jones:** link or your probes or whatever, it actually measures the internal temperature sensor on the PCB. And that actually could even be inside the processor. I'm not actually uh I haven't double-checked whether or not it's an external temperature sensor inside the uh actual CPU uh itself, which is common um to have internal uh temp sensors in um processors. It's just a PN junction, basically, and then they calibrate it and blah, you know? Um Bob's your uncle.

**Dave Jones:** So, anyway, that's just a little tip how you can use your actually measure the internal temperature of your meter. So, you know, I'll just check it periodically, um turn it on to temperature and see if the internal Once the internal temperature gets down, then I'll remove it from the cold to the heat, heat back to the cold, etc. And we'll thermally shock this thing. Let's give it a go. And into the fridge it goes. I've got a shorting link on there and it'll auto power off, but anyway, I

**Dave Jones:** can periodically open the fridge and check what temperature it's at. Once it's down to like, you know, what's this fridge like 2 or 3 degrees or something? It's been in there a couple of hours, 4.8 degrees. That sounds like as low as it's going to get, I suspect. So, whack it in the thermal oven.

**Dave Jones:** And here it is, my little Peltier egg oven and it's set to 59 degrees. Oh, yeah, that's nice and toasty. So, it's 4. It's 4.9. Let's just whack it in there. It's probably going to get some condensation on the board or whatever, but anyway, we want to shock this thing into like doing something. Insert the do something meme here. It's been an hour and 18 minutes. Let's switch it on. Woo, that's toasty warm.

**Dave Jones:** And 55 degrees. Oh, yeah, that that is toasty warm. This is not feel-a-vision. Oh, 555 spotted. Um so, we're going to whack that back in the fridge. Let's go. Cycle one. Well, it spent the entire weekend in here. The timer's overflowed, so at 60 degrees Celsius. Woohoo! Oh, yeah, that is toasty and yep, it still works and there it is there. Yeah, I suspect that I can keep thermal cycling this until the cows come home and I don't think it's going to do anything. So, maybe, you know, you could

**Dave Jones:** get in there and really shock it with the heat gun and then a freezer spray and something like that, but I think you know, I've only done a couple of cycles here, but yeah, it's it's fine. It's It's not losing anything, but that's what all these long-term tests are about. They're long-term. So, let me know in the comments down below what you want to see me do on this thing and maybe we can torture test it, but I don't know, the flash memory in that processor is

**Dave Jones:** holding up to thermal soaking. I mean, you know, 60° for, you know, like many days is a little bit harsh on the thing if you've got like a marginal flash memory, I'd imagine, but anyway, I didn't really expect this to fail and it didn't and my spidey sense tells me, we're not going to get it to do it. So, anyway, worth a little shot just to see if it immediately failed anyway.
