---
video_id: fpDnVSKfhew
title: Raspberry Pi Compute Module CM4 FAILURE
url: https://www.youtube.com/watch?v=fpDnVSKfhew
source: youtube-asr
timestamps: {"0": 0, "1": 8, "2": 23, "3": 33, "4": 43, "5": 51, "6": 64, "7": 75, "8": 87, "9": 95, "10": 110, "11": 125, "12": 136, "13": 150, "14": 164, "15": 179, "16": 186, "17": 195, "18": 209, "19": 220, "20": 232, "21": 245, "22": 253, "23": 273, "24": 281, "25": 295, "26": 311, "27": 319, "28": 330, "29": 338, "30": 347, "31": 358, "32": 367, "33": 386, "34": 397, "35": 406, "36": 427, "37": 440, "38": 446, "39": 456, "40": 468, "41": 491, "42": 508, "43": 520, "44": 534, "45": 548, "46": 558, "47": 578, "48": 590, "49": 602, "50": 623, "51": 637, "52": 648, "53": 659, "54": 676, "55": 693, "56": 707, "57": 717, "58": 727, "59": 742}
---

**Dave Jones:** Hi, I just wanted to show you a video and document this a failure in a Raspberry Pi compute module 4. So, it's a uh CM 4 as they call it.

**Dave Jones:** There it is. Is it the latest? Have they got the CM5 out? I don't know. I don't follow this sort of stuff. Um anyway, I've got it mounted on one of these uh little adapter boards because normally it has like no I like all the IO is through those.

**Dave Jones:** uh there's two of those very high density um board-to-board interconnects there and that's the only IO on this board on the compute module is available through those IO pins.

**Dave Jones:** So to make it anything useful, you've got to mount it on like an adapter board or you've got to design your product around it. So I've got it mounted on this um wave share.

**Dave Jones:** I don't know. I just got it on eBay somewhere. Um and it's like a you know it's got HDMI and uh Ethernet and USB and USB power in and all the requisite uh stuff, right?

**Dave Jones:** and the Raspberry 4 uh IO header on it. Right. So, this actually comes from and I believe it's failed, but it it actually comes from my ARL gateway. Um you seen this video.

**Dave Jones:** This is for my AERL battery. Uh link in the video if you haven't uh seen it. And uh designed in Australia by Peter who's been on my um who was on the uh video when I installed the battery.

**Dave Jones:** And you can see the compute module uh 4 just plugs in there like that. And then a a heatsink back plate goes on this. And it's just a nice easy way to develop because you know they don't manufacture these in high volume.

**Dave Jones:** So it makes sense to use a compute module Raspberry Pi compute module in something like this. Um and it's got external uh you can power it directly from the battery and stuff like that.

**Dave Jones:** Anyway, um it it had failed and there's nothing wrong with this. Um, then like with the actual gateway itself, I believe there's a problem with the compute module. Now, when I first and I've got a second one of these modules, too, and it works fine on this uh adapter board.

**Dave Jones:** I can hook up a HDMI monitor on here and I can get the, you know, the penguiny boot sequence and all the rest of it, right? So, when I was trying to troubleshoot this one here, which I believe has failed, um, I was getting nothing out of there.

**Dave Jones:** And when I was powering on, even with nothing plugged into the Ethernet, the two Ethernet leads here, they were like both on and dim, like at like quarter brightness or something like that, right?

**Dave Jones:** So, like it indicated that something was wrong. And then, so I was trying to, you know, get the thing working and I couldn't get the damn thing working. And then, um, one time like I went to pick it up and I realized that, ouchie, Ernie, Bernie, Ernie, Bernie.

**Dave Jones:** Um, it turns out that this chip was getting hot and like really hot as in I could barely touch it. So, you know, if as a general not like rule of thumb, if if you can't keep your finger on a chip, then it's probably at 50° Celsius or more, right?

**Dave Jones:** So, um yeah, and this is turns out that this is the um Ethernet uh chip. This is the nick here, right? This is the um network interface chip. It's a uh BCM 5421, a Broadcom Joby.

**Dave Jones:** And this thing was getting so hot I could not touch it. And yeah, okay. Normally, like the Raspberry Pi, like you need a heat sink on it. Here's the voltage regulator down here.

**Dave Jones:** And like you generally put like some, you know, um, seal pads on this and the regulator. I don't believe you regularly have a pad on the um, Ethernet chip.

**Dave Jones:** It should not get ernie burnie hot, especially like seconds after power on. Seconds after power on. And the um, processor didn't get um, hot at all. Um, so yeah, I think something's wrong.

**Dave Jones:** So anyway, so I actually went to shoot a video the other day on this and I thought, uhhuh, I'll get out the flur thermal camera. You can see I've got my flur thermal camera ready to go.

**Dave Jones:** My secondary one over here um bit the dust. Um, so yeah, it's the front panel's missing off it, but this doesn't work for some reason. It can't operate as a used to operate as a camera.

**Dave Jones:** Now it doesn't. So, I've got my um little um handheld jobby here and we can see the temperatures on this. Now, I was going to shoot a video on this and all and it was drawing uh five watts.

**Dave Jones:** Okay, so that five watts, I think most of that was going into that chip to make it really Ernie Bernie hot. And then when I went to shoot this video, I kid you not, it didn't work.

**Dave Jones:** Like, it stopped drawing that five watts and it dropped down to like three watts or something like that. God, you know, it's like the white lab coat syndrome, which is, if you don't know, the white lab coat syndrome is things never faults magically disappear when you invite everyone around with their white lab coats to have a look.

**Dave Jones:** In my case, it's all of you. Um, I invited around I was going to I was about to shoot the video and it just stopped. So, anyway, I thought, oh, that was the end of that.

**Dave Jones:** The chips probably finally died internally or something and like I don't know, right? something's come a gutsa inside the silicon or something because it doesn't look to be like any issues on here and and the and the connectors are all properly seated and everything else.

**Dave Jones:** Right. There's there's no problems at all. So I don't Yeah, maybe something failed in the chip. If you know is that a known issue? I tried to grock that and it didn't know about any known issues in like the Broadcom um chip or anything.

**Dave Jones:** Right. So yeah, I assume that just failed. But then I went to power it up again today and it suddenly d started drawing like random amounts of color like six watts and stuff like that.

**Dave Jones:** So I thought, uhhuh, right. Something's changed again. So, and it seemed to be non-consistent. So, I'm going to plug it in now. I got my power meter here. I've got the power zed, which actually hooks up to the um coms here.

**Dave Jones:** And I can actually get the application program to get like a graph of the current or something. Maybe I'll do that in a minute. But oh, maybe I should run it now.

**Dave Jones:** Okay, so I think that's graph in now. Sorry, I haven't used this u software any at all. So, I I think it's running. So, let me actually plug this thing in.

**Dave Jones:** And we're getting a live reading there uh on the voltage. Right. So, I'll plug it in and boom. It's on 5 volts. 6.5 watts. 6.5 watts. It's doing it.

**Dave Jones:** It's doing it. It's doing something. Let me get my thermal camera back out. Uh sorry. Yeah, the graph's not updating. Ah, bugger. Okay. It's still drawing six watts. Where is the six watts coming from?

**Dave Jones:** It's coming from, as you can see, the Ethernet chip up there is at 70° and the DC toDC converter is at 82, no 73 or 83. Um, anyway, yeah, both of those, the DC toDC converter and the Ethernet chip are too hot to touch.

**Dave Jones:** And this is the processor here where my finger is there pointing to that. So, there you go. That is I better disconnect that now. So, those things were too hot to touch there.

**Dave Jones:** Too hot to touch. So, let me try that again. External power. I've just got this coming from a battery pack. Oh, yeah. Yeah, there it is. There you go.

**Dave Jones:** 6.2 watts. So, there you go. It's consistently doing that again. And trust me, I cannot [Music] Ernie Bernie Ernie Bernie. Um, I cannot touch that Ethernet chip and I can't touch the DC toDC converter because the DC toDC converter is like powering that thing at like 3.3.

**Dave Jones:** It's converting the 5 volts down to 3.3 or whatever and um, powering that Ethernet chip. So, there you go. Um, there's something very, very wrong with this. It's one sick puppy.

**Dave Jones:** Um, what the heck is wrong with that? I don't know. Here we go. I figured out how to get the chart. I had to actually go into uh, on mode there.

**Dave Jones:** Right. So that's just right down in the noise. It will actually auto scale. So sorry you can't um do this other camera at the same time. Switch this. I'm now going to turn it on.

**Dave Jones:** Apply power. There you go. 5.1 volts, 6.3 watts. There you go. It's jumped up. It's just very consistent. Very consistent power draw there. There's no like the processor is not running.

**Dave Jones:** Trust me. If I plug in a HDMI into this, I get absolutely nothing out. There is something grossly wrong with that Ethernet chip. It has failed. It has kamagutza and yeah that is just that's very consistent there that is completely kamagutza and even after I turn the power off you can still see it's all it's all hot um granted uh the processor might be look cool because

**Dave Jones:** it's a metal can so the emissivity uh is different on that metal can I'd have to put some black tape on top of that but trust me the the processor like barely gets warm drawing six watts at the moment and I've got my finger on that processor chip And I can tell you it's it's getting a bit warm now.

**Dave Jones:** It's probably at 40° something like that for the processor, but you kind of expect that, right? Oh, no. No. Actually, the processor is getting processor is getting a bit earring Ernie Bernie.

**Dave Jones:** Hang on. Okay. So, what I'm going to do is put some black electrical tape on top of that. Not the greatest uh heat transfer, but it it means that we'll get a a proper emissivity.

**Dave Jones:** um of that because the thermal camera has to be set up to an emissivity figure and um those bright shiny metal cans are not it. Um so yeah, so let's go back to here and let's try that again, shall we?

**Dave Jones:** But of course the board is dead because uh that Ethernet chip should not be getting to is the hottest chip on the board. Oh, sorry. No, that's it. No, the hottest chip 101 degrees the DC toDC converter.

**Dave Jones:** So down here now 70 uh sorry what is it? Well the max is no 79. Why is it saying 100 max 109 and the uh 90 is the Ethernet chip and and you can see that the processor is not really getting any higher than any of the surrounding stuff.

**Dave Jones:** I can still keep my finger on that. Um oh no no no it's getting pretty hot now but still not as hot as the Ethernet chip. The Ethernet chip should not get that hot.

**Dave Jones:** 7.2 watts. 7.2 watts. This is nuts. So, there you have it. I just wanted to show you that. That is uh one sick Raspberry Pi. One sick compute module.

**Dave Jones:** And the poor old DC toDC converter. Of course, it's going to get hot when you're dumping at least five watts. Most of that going in. There's probably like four watts going into um yeah cuz I think sorry there's at least three cuz this uh I've got the other good one I've got I've measured the power on that and it's uh 2.5 watts operational or something 2.4 for what's

**Dave Jones:** operational for the Raspberry Pi doing its um thing running its program for the a AERL battery uh monitor um thing. And yeah, yeah, it's only a couple of watts, but this thing, you saw it, it's taking five or six, but it's had many failure modes.

**Dave Jones:** It's had like three different failure modes. I swear it originally drew five watts and then I went to shoot my video and it was drawing.3. It was it was done.

**Dave Jones:** I thought it was done and dusted. The chip had died. Now it's drawing, you know, like what was it? Seven. Was it 7 watts there? And the Ethernet chip is just getting smoking hot.

**Dave Jones:** Like Ernie Bernie hot. So, it should not do that. It's should probably be um you know, one of the lowest power chips on the board really. Um I I wouldn't the memory even take more than the you know, if you're flogging the guts out of the thing, wouldn't the memory even take more than the um poor old Ethernet chip there?

**Dave Jones:** But uh yeah, so that is one sick puppy and it's not the adapter board because I've used this adapter board successfully with an identical CM4 module from another AERL gateway and I get the HDMI out and it draws a couple of watts and everything's fine.

**Dave Jones:** So yeah. All right. I just wanted to show you that. So if you got any idea, if you heard of any failure modes where the Ethernet chip comes guts, please leave it in the comments down below because we're both very curious.

**Dave Jones:** Peter and I are very curious to know why this Raspberry Pi compute module has failed. It's just weird. Uh, no, I don't have any power over Ethernet things at home doing any of that.

**Dave Jones:** I don't have any of that rubbish. Not that that would be a problem anyway. Um, because it's isolated and it taps from the other side power over Ethernet, but uh yeah, it's I there's none of that.

**Dave Jones:** So, I don't know. Um, it just hooks into my regular gateway at home, my regular router at home. I I don't get why this thing would have failed. Usually they're they're pretty reliable things, but uh yeah, it's got scummy guts.

**Dave Jones:** Wouldn't have expected that, but anyway, thoughts and comments down below. Catch you next time.
