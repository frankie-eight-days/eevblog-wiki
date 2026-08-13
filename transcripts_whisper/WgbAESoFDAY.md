---
video_id: WgbAESoFDAY
title: EEVblog #342 - Agilent 90000 Oscilloscope Teardown
url: https://www.youtube.com/watch?v=WgbAESoFDAY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 41, "3": 55, "4": 81, "5": 100, "6": 116, "7": 136, "8": 151, "9": 168, "10": 189, "11": 219, "12": 244, "13": 260, "14": 288, "15": 312, "16": 336, "17": 359, "18": 377, "19": 391, "20": 406, "21": 425, "22": 441, "23": 462, "24": 478, "25": 495, "26": 516, "27": 537, "28": 563, "29": 583, "30": 606, "31": 625, "32": 642, "33": 662, "34": 676, "35": 695, "36": 714, "37": 736, "38": 756, "39": 777, "40": 803, "41": 827, "42": 844, "43": 863, "44": 882, "45": 903, "46": 915, "47": 935, "48": 954, "49": 970, "50": 988, "51": 1002, "52": 1023, "53": 1044, "54": 1061, "55": 1078, "56": 1094, "57": 1118, "58": 1133, "59": 1154, "60": 1171}
---

**Dave Jones:** Well, the time has come. The $140,000 DSA91304A Digital Signal Analyzer, DSA, eh, it's a scope. The Infiniium 13GHz 40G sample per second scope has got to go back. But you know what we say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** Well, kinda. Eh. Now, Agilent told me not to tear this thing down, but they didn't say I couldn't at least take the main cover off, which was pretty darn easy. We should be able to see a few things through the vent holes in the side.

**Dave Jones:** Let's take a look at it. The first thing you notice is these absolutely enormous brushless fans on the side. There they are. They're a Delta Electronics brushless DC fan, made in China, but they would be good quality ones. But they, you know, I mean, the airflow in these things is massive.

**Dave Jones:** That's why it makes a huge amount of noise. If you watch the previous video, you could see, well, you could hear the noise in the background, even picked up by my lapel mic. It really is that loud. And there's not much to see through the fans, unfortunately, just more heatsink stuff.

**Dave Jones:** But the other side's gonna be more interesting. Now if we have a look through the vent holes on the side here, there's the B and Cs on the front panels. And they don't go directly into boards, they go into coaxes. They'd be super-duper high-quality coaxes.

**Dave Jones:** We can see some sort of part number on there, but you can see the four channels and the trigger and stuff like that over on the far side there. And they go through, well they don't, yeah, they just go through a panel there.

**Dave Jones:** A metal panel through to the other side down in here. And I'll try and rearrange the light so that we can see in here. These coaxes basically go up to these boards, these two boards here, directly into the hybrid modules down in there.

**Dave Jones:** Sorry about the focus, it's not the best. I'll try and get some better in a second. And you can see them here, the coaxes coming up from the bottom, directly from the input B and Cs. And two of them go up to two hybrid modules here.

**Dave Jones:** So these are the input hybrids, say for channel 1 and channel 2, I'm not sure which is which, doesn't matter. They're all identical, they're two identical boards, handling two channels each. And the other two coaxes go into these two hybrid front-end modules down in here.

**Dave Jones:** And you can see the hybrid module in there, and that's what you're paying the huge dollars for. Absolutely top dollar, you know, that's where all the money, that's where all the magic goes. You can see some miscellaneous stuff, power supply stuff, there's some chokes.

**Dave Jones:** They'd be powering those, but they would be identical. 13 gig input amplifiers on those hybrid modules going over to the memory under all those heatsinks at the far end you might be able to see in there. And hopefully you can see through there, you can see the other, the heatsinks of the main memory devices and the ADCs and stuff on the far side of those hybrid modules there.

**Dave Jones:** Hopefully, if that will focus in, you can see the board goes right over to the far side, right next to the fans over there. So it's a full-width board for these two input channels there. Goes all the way over, right over to the fans over there.

**Dave Jones:** And this contains all of your analog front-end, of course, is in the hybrid module. Then it would go into the ADC, and then that would be coupled to the memory. It'd have all your clocks, and there you go, that's a better view of the whole system board down in there.

**Dave Jones:** And all of the magic is under those heatsinks. So even if we could get in, all we'd see is a bunch of heatsinks there, unfortunately. So it wouldn't be terribly exciting. Can we have a look at that device down in there? There's a Xilinx Spartan FPGA and some other miscellaneous stuff all on that main board.

**Dave Jones:** But basically, you've got two of those boards there, shared between two channels. So that's our four-channel scope. And if you have a look in there, you can see some other right-angle BNCs coming from the bottom of... well actually, no sorry, it's the side of this vertical board I'll show you in a second.

**Dave Jones:** And there, they just go along the bottom to the back panel there, your 10 MHz reference in and out. So you can see this vertical board here, it's like a backplane board, and you can see the high-speed interconnects down in there. So the two ADC cards, plus the main Windows processor board on top, plug into this backplane board.

**Dave Jones:** But it's more than just a backplane, it's got some serious circuitry on there. Hybrid or oscillator module or something like that. And it's got some large heatsink devices. You can see the fan on the back of a large heatsink there. But that main board there actually has a fair amount to do.

**Dave Jones:** Check out all that circuitry down in there. So it basically seems to be a four-board system. You've got that backplane board down in there, you've got your two ADC boards and your main processor board. Now if you look at the top cover here, you can see they were even thinking when they designed this,

**Dave Jones:** they put in these studs in here, press studs, for the black pouch which goes on top, which has matching press studs on it. So it sits on the middle like that, so they didn't have to, you know, stick it on with Velcro or something ugly like that.

**Dave Jones:** It was designed into, you know, an integral part of the entire case for this thing. Really nice. And if you have a look at the side down here, they've even moulded in these little feet to allow this thing to stand on the side,

**Dave Jones:** so it doesn't interfere with the carry strap here, in case the carry strap is lower, recessed slightly lower than these side things. So it allows you to stand up on its side to get the screws out and, well, I don't know, use the thing in that orientation if you wanted to, don't know why,

**Dave Jones:** but it just would have been mostly so that, you know, technicians could access the screws, flip it up on its side, and access, because there's screws along the bottom edge here that you have to undo, as well as on the back, to slide this cover off.

**Dave Jones:** So they were really thinking. So let's lift the hood on this puppy, and, yeah, no, there's no, no, they're just not integral heat sinks. Here we go. Ta-da! And we're not going to touch anything inside, but it should at least give us a small peek into what's inside this thing.

**Dave Jones:** And on the top plate here, you can just see some riveted air guides in there, which help channel the air and stuff like that. It wouldn't be for any other reason just to stop some air, you know, blowing over the top of some other wall into some other part,

**Dave Jones:** so you can direct the air through the system exactly where you need it to maximize the cooling efficiency in this thing. Because this thing's going to get damn hot. And here we go. Here's inside this thing. It's got a, it looks like a pretty much a standard,

**Dave Jones:** one of these compact form-factor PC motherboards in here. I'm not up with the latest PC motherboard standards and all that sort of stuff, but standard PCI slots with the backplane here. And some SATA connectors going off, and we've got a main vertical riser board in here,

**Dave Jones:** going down to those two ADC boards. So here's a look at the PC motherboard, and I don't know if they had it custom designed for them. There's the memory module, standard power connector on it, and SATA connectors over there, and, well, some more SATA connectors,

**Dave Jones:** and the, that's a GPIB board. What type? It looks like it's some sort of custom Agilent job. Perhaps. I'm not sure. I would assume so. And there's not much else to it. I mean, there's the IEC mains input filter and cable there, that goes off to the main power supply, which is around here,

**Dave Jones:** and it's got instructions on how to remove the power supply, but I'm absolutely not going to touch anything in this. This thing is worth $140,000. So there's a board on the front panel. It's got some power supply stuff. You can see those little surface mount heatsinks down in there,

**Dave Jones:** so that's mounted on the front panel. There's the backlight inverter for the display. It's a dead giveaway. There's another tiny little board down in there. I'm not sure what that one's doing. And this is actually really nicely system engineered. Take a look at that big right-angle power connector there,

**Dave Jones:** board-to-board connector, which basically transfers all the power by the looks of it. You can tell those big huge tabs on the back of it there. That's a big whopping blade power connector. That goes through to a right-angle board on the power supply down in there.

**Dave Jones:** You can see it. You can see the board down in there. So the power supply's in here, the 240 volts comes in here, does all the power conversion in behind here, and then it pops out on that connector over on the main board,

**Dave Jones:** and then the power from this backplane board comes over to the main processor board. So it's certainly not like an off-the-shelf power supply. It looks all totally custom designed. And a lot of engineering's gone into this. You can bet your bottom dollar. And that's why these things are so darn expensive,

**Dave Jones:** and they wouldn't sell many of these. I mean, you know, it's not just that which makes it expensive. It's the big custom hybrid ADC front-end modules and stuff like that, of course. The real high-speed stuff. But if you have a look at the main board down in here,

**Dave Jones:** actually I'll try and get some light in there and see if we can improve that. All right, let's take a look at this backplane board down here. You can see the right angle connector down in there going to the... going over to the ADC board.

**Dave Jones:** But look at the layout of those bypass caps and all those vias. That is clearly a big-ass BGA on that board there. There we go. You can see all the... all the vias in there. We've got a Xilinx Vertex 4 FPGA down in there.

**Dave Jones:** Some sort of hybrid module on the high side of that. And what else have we got? Just miscellaneous stuff. Standard SO. Nothing much happening there. Some chokes, basically. It's just a whole bunch of power supply stuff down in there. So that backplane clearly is mainly power supply,

**Dave Jones:** but it does have a huge whopping BGA and a Vertex down in there for some sort of acquisition... well, some sort of processing, something like that, when you've got a device that huge. It's obviously doing something of massive importance. And my best guess of that, of course,

**Dave Jones:** given the proximity of these two SATA cables, clearly they're using SATA to get all of the data out of this thing. So that big BGA in there, and possibly that Vertex 4 next to it, is some sort of data serialization system, which basically probably takes all the parallel data,

**Dave Jones:** really high-speed stuff from the main ADC capture boards, and it's serializing that and putting it into the PC. Because this is basically the only way this machine gets the data is through those SATA ports. I mean, you know, there's no other interface. So eventually it comes into the main processor

**Dave Jones:** and gets displayed on the screen via those SATA connectors there. So, you know, there is no direct from that to the display. It's got to go through the SATA serial link into the main Windows processor, and then Windows displays it all. And if you can see that big board-to-board interconnect down in there,

**Dave Jones:** that big huge black block, that is clearly the power going to the ADC board, just by the sheer size of it there. And that would be using huge, you know, high-current blade terminals, just like going, just like it went from the power supply to this main board.

**Dave Jones:** And there's another signal one under that heatsink device with the fan down there. So that'd be a really high-speed, that one down there, very high-speed board-to-board interconnect, and a huge amount of power, because we're talking many, many amps to power the ADCs and the hybrid front ends and the memory,

**Dave Jones:** and all that sort of stuff, working at 13 gig. With those hybrid modules down in there again, you can see that they're individually serial-numbered, and you can bet your bottom dollar, REV2 board, by the way, you can bet your bottom dollar those things are individually tested and characterized,

**Dave Jones:** most likely by some wise old man with a gray beard, some RF wizard who tweaks every one of those things, and characterizes their performance, and none of them would make it in here unless they passed exhaustive testing. You can see the connection method on the bottom there,

**Dave Jones:** it looks like there's some sort of BGA module, or that could be like, you know, some ball grid array, although I'll have a look under the bottom and see if I can see any pins. It's quite hard to get the camera in there,

**Dave Jones:** but you can see that there's additional circuitry on the bottom side of the board there, a ton of it, actually. Not huge stuff, just support stuff, and there'd be bypass stuff and things like that, but definitely double-sided load, of course. You need that to get the bypass caps right on the modules themselves,

**Dave Jones:** but there's a ton of circuitry on the bottom there, and the modules don't look to be through-hole, of course, they're some sort of BGA system which helps with the signal integrity. Sorry, can't get a better view than that. So there you go, I hope you enjoyed a brief look inside

**Dave Jones:** a $140,000 scope to see where you're getting your money's worth. I'd love to be able to show you more on those ADC boards, but I'm definitely not going to take this thing apart. I was asked not to, but they didn't say I couldn't take the lid off, of course.

**Dave Jones:** So I haven't touched or prodded around inside there, so pretty darn sure it'll still work when I put the lid back on. But as it so happens, there's some more info, and a look at those hybrid modules in the Agilent data sheet. So we'll take a quick look at that.

**Dave Jones:** And here it is. If we have a look at the data sheet for this thing, just the short-form data sheet, they're obviously quite proud of its design and construction and the technology in here, because they tell you all about it. There it is.

**Dave Jones:** Engineered for unmatched real-time measurement accuracy. Use your jitter budget in your design, not on your oscilloscope. Yes, which means it's ultra-low jitter. And if we have a look here, they even give you a nice look at the hybrid module here. You can see inside there, unfortunately it's a little bit,

**Dave Jones:** that's as far as I can zoom in, there's no more resolution in that thing anyway, I don't think, but you can see the hybrid module, you can see the balls on there, of course. And that's, it's really a nice bit of work. I mean, there's a whole lot of RF magic which goes into that.

**Dave Jones:** You know, how many work hours would have gone into producing that, I don't know how big the team would have been, but if you want to know where your money goes in a $140,000 oscilloscope, a good lot of it is just in this hybrid module

**Dave Jones:** and the high-speed custom ADCs which are next to it. And we can actually scroll down here and take a look at those. They're the hybrid modules, as we saw. And there was that FPGA, Xilinx FPGA device. You remember, we were looking from the top side here.

**Dave Jones:** So we were looking from the top side down into it, and we had the coaxes coming up over into there like that, and they're the two hybrid modules. So you've got your 13 gig signal directly from the coax into here, into the hybrid front end,

**Dave Jones:** and then directly into your analog to digital converter here. There it is, sorry, it's a little bit tricky. Analog to digital converter, then there's the memory, high-speed memory controller for the sampling, and then the acquisition memory, the massive amount of acquisition memory. And that's just not standard stuff, that'll all be custom, prime spec stuff.

**Dave Jones:** You're paying top dollar for that. So there you go, that's a... they give you a decent look at the board there. I really like that, you can see the connectors on the side here. So that's almost as good as taking the thing out.

**Dave Jones:** And you can see it's pretty much all in these custom devices, as you saw there was circuitry on the bottom as well, just support stuff, bypass stuff, and miscellaneous stuff like that. But yeah, it is serious business, and that's why this stuff can have up to one gig of that high-speed sample memory,

**Dave Jones:** which is just crazy stuff. So that's where your money's going, folks. You know, everyone goes, oh, why can't it just be a little tiny black box hooked up to a regular Windows PC? No, it can't be! There's, you know, many, many tens of millions of dollars of R&D

**Dave Jones:** which goes into producing that board and those hybrid modules. And I know what you're all thinking, does it smell like $140,000 worth of scope? Oh, yeah! Catch you next time.
