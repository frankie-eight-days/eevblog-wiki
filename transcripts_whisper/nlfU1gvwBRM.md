---
video_id: nlfU1gvwBRM
title: EEVblog #520 - Michael's 3D Printer
url: https://www.youtube.com/watch?v=nlfU1gvwBRM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 43, "3": 59, "4": 85, "5": 105, "6": 125, "7": 144, "8": 161, "9": 184, "10": 208, "11": 225, "12": 242, "13": 256, "14": 279, "15": 303, "16": 322, "17": 349, "18": 365, "19": 384, "20": 401, "21": 420, "22": 438, "23": 455, "24": 466, "25": 482, "26": 497, "27": 508, "28": 528, "29": 543, "30": 548, "31": 584, "32": 599, "33": 615, "34": 632, "35": 647, "36": 666, "37": 684, "38": 697, "39": 721, "40": 734, "41": 749, "42": 768, "43": 787, "44": 799, "45": 819, "46": 838, "47": 856, "48": 876, "49": 895, "50": 910, "51": 933, "52": 950, "53": 977, "54": 993, "55": 1009, "56": 1027, "57": 1048, "58": 1063, "59": 1078, "60": 1104}
---

**Dave Jones:** And here with Michael and look at this stunning urban hackerspace streetwear. Doesn't he look stunning? Very cool, very cool. He's going to tell us all about his new do-it-yourself 3D printer. Tell us. Okay, so basically I've got a printer before, but I wanted to make something new.

**Dave Jones:** So I wanted to make it as something that was fairly readily available as far as the framework goes. So I purchased this aluminium box tubing, 25 by 25 millimetre tubing and plastic joining connectors from Buddings. And basically if I hadn't made this out of T-slot, it would have cost me around $400.

**Dave Jones:** Just for the frame? Just for the, yeah, by the time I'd get the nuts and the joiners and stuff like that. Whereas I've done the framing on this for about $160. Nice. So, and as you can see, it's quite, it's quite robust. Yeah, it's sturdy.

**Dave Jones:** And what's the total length of that? This is 700, 700 by 130. And I've built this from a few different designs, based on a few different designs. But it's taken on many different, like there's a nice big scrap bit of yellow parts at home that didn't make the actual build.

**Dave Jones:** But luckily with the hackerspace I've had a lot of different people that were able to share the load and make things for me. So, but the basis is, is that we have, we have two extruders. Yep. So they're dual extruders, rather than be joined together like they would normally be at the current.

**Dave Jones:** Someone's actually done the hard yards with the Marlin firmware to actually make the independent, the extruders work independently. So when it's actually running, this one of them will sit in its home position while the other one does its thing. It could be either two different colors or one could be a support material, stuff like that.

**Dave Jones:** And this one will then return to its home position and this one then will come in with its other color. And what it can actually do is you can set, in the firmware you set an offset so that it knows how far to travel before it actually collides at the collision point.

**Dave Jones:** And what it can do is you can load the same model and tell it to duplicate. And all that happily, then both these extruders will travel at the same time, producing the same part. Because the Y, Y axes will still, still going to travel the same way.

**Dave Jones:** It doesn't matter which way these extruders are happening. So all the parts are custom built from scratch. You can see it. I did steal the parts from somebody else originally, but unfortunately the track that the print has gone down, I haven't been able to use them anymore and I had to go down the road and create them all myself.

**Dave Jones:** Everything's custom built. And how big's your build? Yes, now this is the trick. This is my build platform. So we've got 420 by 210. And so for those people who know Prusas and General 3 printers, it's basically two obvious standard PCB heatbeds side by side.

**Dave Jones:** So I currently have a Prusa Mendel that I've extended to run two different beds. But the problem was that to get the height of what I lost, I lost travel height. And the momentum when the, because the bed on my current Prusa travels this way.

**Dave Jones:** So it's, it's quite a bit of work on the, on the motors when, when this starts to get, get going. So obviously I had to jeopardize speed for the factor that it was just going to. Right, so by mounting in that orientation. Yeah, so now, now we're going to go in this orientation.

**Dave Jones:** Much less. Yes, much less travel. You should be able to travel faster. Yeah, I should get a travel, fast travel rate because it's not. I mean, it's, it's a little bit different now too, though, that with the, with the new firmwares and the, and the, the ability to have jerk setting.

**Dave Jones:** So it doesn't, so it, or de-acceleration. So that the bed can travel in one direction. Then before it reaches its end point, it could slowly de-accelerate. That's, but the advantage of this is that I have two Prusa size beds. So anything that most people can print, I can, with this new dual extruder set up, I can print two of at one time.

**Dave Jones:** So the objective is that if I'm going to build the average 3D printer, Prusa, I can basically print the whole, the whole kit in one, in one print. So. And you've oriented your shafts like this. This is your drive shaft down here. A lot of the current printers now are moving away from the motors being mounted at the top.

**Dave Jones:** Right. Because obviously, it obviously puts a lot of weight when the motors are being pulled this way. So the whole idea of what we've got here is, is that this, this part here is designed to take the weight so that the weight isn't on the actual motor itself.

**Dave Jones:** A lot of designs where this shaft's either hanging directly from the motor or it's pushing down directly on the motor. And it's actually, actually forcing because there's a spring loaded coupling here. So the weight actually affects. So whereas this system now allows me to keep, keep the weight up off the motor shaft and purely allow the motor to actually do what it's supposed to do and turn the threads.

**Dave Jones:** But, you know, after having a 3D printer before, realizing that even the best printers, you know, you'd like to get in here and do this little tweaking action. So, so rather than do that, I, I added, you know. Little, yeah, you can just rotate that around and tweak it.

**Dave Jones:** Yeah, just, just tweak it around. So. Nice. But yeah, so, but because it, because I had dual extruders, I had to change the design because I had to, not most 3D printers have only got one motor. And we call a pulley on the other end.

**Dave Jones:** Right. Right. But because I had to have dual, I had to have two. So I had to create a system that allowed me to have two motors and two pulleys at either end. And they wouldn't collide. But what I, what I, what I would say though is that a lot of, a lot of, I don't like the printed bearings.

**Dave Jones:** Right. The printed bearings don't work very well. No. So I went down the road of speaking to Mr. China and, and, and making sure, making sure, yeah. Getting Mr. China to look after me and I bought proper, proper bearings. Plus what it allowed me to do is that originally I was going to have much longer dual bearings here.

**Dave Jones:** I'd have a, have a much wider plate that the extruder was going to fit on. Yep. But because I'm using, because these are 12 millimeter rods, these are really, really strong. What it allowed me to do is that these bearings just happen to be wide enough that, that, that there's no, there's no play in there.

**Dave Jones:** So now I've got such a really narrow mounting for the extruder. It makes it really, really cool. Because otherwise it's designed, when I get to here and I come to here, it's designed so that this. Right. Still makes. Go right to the edge.

**Dave Jones:** Yeah, go right to the edge. If I had a. You can use the whole build area. Yeah, yeah, yeah. I'd get right to the build area. So if I had a head much bigger than that, I mean, I'm really already wide as it, as it is.

**Dave Jones:** Huge. And then, yeah, have to take it any wider. So it's, yeah. It takes a little piggyback. It's probably not a model for the fainthearted. No. Because the, the thing was is that in the build process, because I haven't got slots in my rod.

**Dave Jones:** When I, I had to be very accurate. So if I, when I screw these in, if they're not straight. They wouldn't be. But I can't move them half a millimetre higher. That's short. Because now I've got to, you know, we all know what happens when you drill a hole and you can't, you can't move a half a millimetre.

**Dave Jones:** So therefore I'd have to all go down the route of putting bolts in. And if I had to put a bolt in one. I have to make the hole pretty uniform because it has to look nice. And I'd have to put, I'd have to change the hole design.

**Dave Jones:** So. Terrific. There it is. And it's designed to go in a suitcase. It's designed in a suitcase. Yes, sorry. So the drill platform would come off. And this then will lock into here. Yep. And I'll have a carry, carry strap. A strap over the top.

**Dave Jones:** Yeah. And then I'll be able to just carry it around and make it transport. So this will go this way. Yep. And everything will fit. Nice. I need to lock it up. So. And the printhead. Have a look here. The, you've designed, you're using an extruder designed here is it?

**Dave Jones:** Yeah, well, this is our own design. Basically what this is, it's just a aluminium plate. Yep. Because what it does is it works as a heat sink. So, and then what we're doing here is we've seen someone create an idea with this where

**Dave Jones:** I think it's Joseph Cruiser. Right. Created an idea. And then we've got a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, Yep. And then why don't we lock it in here.

**Dave Jones:** So this one, this pushes up in here. Got it. And we, and we lock it in here and that's fine. And what it allows us to do is, um, because of so many, um, materials now that you can't use the same, I mean, it's not really good to use the same nozzle for multiple different

**Dave Jones:** materials. Right. So what we wanted is some way to quick release. Got it. Unplug this, take the outline out. Yep. Put this on the end, lock it in, and away we go again for a different material. So. Yep. Excellent. So, uh, having a 3D printer for quite some time and being in the hackerspace allows you

**Dave Jones:** to mix with different people to then obviously come up with, uh, things that are, that are, um, that are unique and in the best fashion. So. And you've designed all of these bits and 3D printed them from scratch. Well, the only thing, the only thing that's not original to me is this extruder design.

**Dave Jones:** Okay. But other than this extruder design, we're supposed to bolt on the bottom of a plate, a moving plate. I've made it mount 90 degrees and added, add this big block of spacer, but then outside of that, everything is totally from scratch. Right.

**Dave Jones:** How many 3D printed pieces are there? Well, there's, there's a lot, there's a lot because, because this, this, this is the rod, this the rod clamp here. Yeah. This is another, a flat piece here. Yep. And then this other part here is another piece that bolts together.

**Dave Jones:** Right. So. That's a lot of work. Yeah. It was, I mean, as I said, there's a quite a, quite a substantial amount of, uh, yellow plastic in a box I've got at home, um, through some trial and error and thinking, thinking that there was something there that was going to work for sure.

**Dave Jones:** And you bolted on and it's like anything like electronics, you know, you get to design the best and then, uh, not until you put it together that you realize that something doesn't work. So. And how are you going to clamp this onto the base?

**Dave Jones:** Okay. So what, what, what's going to happen now is, um, I want it to be able to make it level. So I printed these, um, feet. So basically it takes a, yeah, a five mil, five mil bolt, um, nylon nut. And then unfortunately I have to pull this frame off because I've got, um, square blocks

**Dave Jones:** made for here that have got, uh, countersunk nuts in them and I'll drill holes and then adjust them all so I can crank it up. And once I've, once I've got it up off the table, then I can put, uh, mount five mil

**Dave Jones:** bolts, um, through the, through the base that then this will then center and lock onto and then have a couple of, uh, spring washers in and wing nuts to lock it down. So, and as you were saying before, that, that, that my only fear and I'm not going to know

**Dave Jones:** until I get going is, is with the momentum, how much rock with the narrow, with the narrow base. Um, and there's other printers out there that use this narrow style base is what, how I got the idea. So, so I've got someone's, there's people printing successfully like that, but that

**Dave Jones:** is not at such a great scale. So therefore their momentum and all that's not anywhere near as much as mine. So it's just going to be, suck it and see. Suck it and see. Yeah. I wasn't going to. Well you can always add, you know, extension feet out here like that.

**Dave Jones:** I've got plans because obviously the joy of these, these joiners is obviously like I've got a three way connector in here now. I can simply go back to Bunnings, get a four, get a four way connector and just add another rod for feet.

**Dave Jones:** So this, this, this was the best, this is the best idea I ever, ever done was, was go this route because originally it was a hundred millimeters narrower because I wasn't going to have dual heads. The distance was fine, but because I had to make it bigger, I just cut a few extra long

**Dave Jones:** rods and fit it in and box your uncle. But there's been many iterations of this design where, where originally for some strange reason I had these ones that come up here and they went back and I thought, oh, that's great, you know. Oh, what I'll do is I'll mount my electronics in there and then I've gone, holy crap, holy

**Dave Jones:** crap, the plastic's going to travel in here. It's another of those things where, you know, you have a brain freeze until it's all together and you go, oh, crap, it's not going to work. But yeah, I have to say, if anyone was going to have a look at building a printer, seriously,

**Dave Jones:** go down to Bunnings and just buy a few bits of this. It's cheap, it's cheap really. Go and buy a few, go and buy one link and get them in a 1.2 meter link I think. Go and buy yourself one link of that and a half a dozen connectors and like Lego, just

**Dave Jones:** cut some up into links and just whack this together and go, oh, cool, let's see what I can make. It's really, really good and it's much cheaper, as I said, it's much cheaper than T-slot. Yeah, they're very expensive. And if you go, oh, don't make a mistake, you know, you go down to Bunnings and get some

**Dave Jones:** more. If you cut something too short out of something that's come from the US or when you get it from here, it's $50, you know, it's a really expensive $100 cut that you actually make and that's gone. Well, it's looking good at this stage.

**Dave Jones:** Yeah, no, I'm really good. Looking really fantastic. Really good. And another couple of weeks left of work maybe. Yes, yes. So basically all I've got now, other than the feet adjustment, which is not a really huge process, is the electronics. So once the electronics are done, because I'm going to run 24 volts, the whole system

**Dave Jones:** on 24 volts, so the electronics are allowing it to go that way now, rather than power these motors with 12 volts. This is a very big machine. Yeah, it is. So obviously I'm much better at running on 24 volts because I'm going to get a lot more

**Dave Jones:** grunt out of it. And because I'm running two cruiser heatbeds, I have to run them, I wire them in series and I run them on a 29 volt power supply that obviously I tweak up to, a 24 volt power supply that I tweak up to 29, just because otherwise it takes a half an hour for the temperature

**Dave Jones:** to get up, so I need to just spike it a little bit and get the temperature up. The other thing that I had a look at is that I want to get the heat up really quickly. The problem is, the next thing is, now because I'm using Kapton tape or something like that,

**Dave Jones:** it's the factor of getting the temperature down that I have to wait. Got it. So I decided to mount two 50 millimetre fans in here. Ah, to blow it, right. So then when I'm going to finish that, I'm going to add some green energy code and then

**Dave Jones:** cool the bed down. Very nice. Any concerns about warping on such a huge build plate? Yes, yes. We'll wait and see. Yeah, yeah, yeah. Now, I mean obviously with now, my personal opinion is that if you're going to build something big, you need to use a brim.

**Dave Jones:** So most of your cucuras or your slices will either have brim around the outside. I find that you build underneath it. Oh, rough. Yeah, rough's crap. Rough's crap. You've got to spend two years to get the raft off as compared to, because generally you

**Dave Jones:** don't have a problem with the middle of your part lifting. It's always the edges. So either turn brim on, or if you don't want to turn brim on, just be very smart on adding a little circle or anything to the corner of your model.

**Dave Jones:** You can. And then to trim it off later and that'll solve your problem. Nice. But yeah, it's a bit of exercise and we've got touch wood. Touch wood, when we get to the day we turn it on and crank her up, that she runs smoother

**Dave Jones:** than what... And you'll post some videos? I will. I will post some videos. Fantastic. So, let me get a quick plug in. Yep. Okay, so also I run a 3D printer parts website called 3DPrinterBits.com.au. Nice name. So you can get all your motors and plastic and belts and all things 3D printed.

**Dave Jones:** It's Melbourne based. Yep. So, and we send all around Australia and stuff like that. So yeah, 3DPrinterBits.com.au. Awesome. Thank you very much Michael. No worries, thanks.
