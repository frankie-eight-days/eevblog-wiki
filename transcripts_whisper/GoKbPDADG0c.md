---
video_id: GoKbPDADG0c
title: The Incredible Switch Replacement Repair
url: https://www.youtube.com/watch?v=GoKbPDADG0c
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 18, "2": 37, "3": 51, "4": 74, "5": 86, "6": 103, "7": 122, "8": 134, "9": 156, "10": 177, "11": 191, "12": 208, "13": 226, "14": 244, "15": 262, "16": 280, "17": 302, "18": 319, "19": 340, "20": 358, "21": 378, "22": 396, "23": 414, "24": 431, "25": 448, "26": 466, "27": 488, "28": 505, "29": 523, "30": 546, "31": 565, "32": 585, "33": 602, "34": 624, "35": 652}
---

**Dave Jones:** Hi. Yes, we're going to revisit this remote control again because there were so many comments on the previous video about how I didn't actually repair it, as if that was, like, the important point of the video I wanted to make. So, first things first, why didn't I repair this in the previous video?

**Dave Jones:** Well, I was at home and I didn't have a, well, I no longer have a lab at home, so I wasn't able to actually fully fix this thing. I just took it apart and shot that video. I thought I'd just upload it quick, but anyway, apparently, and even though I mentioned in the video that, well, it's

**Dave Jones:** just taking out the switch and bridging it, people just seem to think, no, no, no, we've got to repair it, and sure enough, okay, well, I can do 15 minutes of waffle or something like that. I'm actually repairing a simple switch like this, so let's do it.

**Dave Jones:** And yes, my voice still sounds crap because I, yeah. And if you haven't watched the previous video, the summary is this switch here failed and melted into oblivion. As you can see, there's normally a little shaft on there that goes into this, um,

**Dave Jones:** this AB selection switch. On the side of it, this actually selects the channel for this, uh, infrared remote control, but you can see that that's all melted in there. So you can see that that switch really heated up to buggery, and, uh, it's still melted in place there.

**Dave Jones:** So I don't need that AB selection switch, so what I'm going to do is, uh, physically remove the switch and just, uh, bridge one side of it. Yeah, it was just a crappy failed switch, and it failed inside, but there were quite a few

**Dave Jones:** people commenting that, oh, maybe it wasn't the switch. Maybe it was this, uh, rocker switch on top here, which, um, yeah, it just pushes on these two buttons here. Oh, that was pressing against these wires, and these wires shorted out. Well, no, that's not the case, because if these wires shorted out, then sure,

**Dave Jones:** the wires would heat up and everything else, but there's no way, even if they were pressing right up against the metal case of this, you wouldn't get the current flow in there to heat it up and char all that switch. It just isn't going to happen and melt the shaft off and everything else.

**Dave Jones:** It's just not going to happen. The current was passing through that switch, absolutely, no doubt, and the reason it was passing through there, as we saw in the previous video, here is where the battery positive comes in. The three volts from the two AA batteries goes through this switch, comes into the center

**Dave Jones:** contact here, and that trace goes up to one of the contacts on the AB selection channel select switch up here, and the outer case is, of course, shielded, so this pin obviously, uh, shorted over to the metal case, and they've used the metal case as a ground, and as I mentioned in the previous video,

**Dave Jones:** it looks like the reason they've done that is a PCB layout reason, because they wanted the other side of the selection switch to be ground, they couldn't get the trace around the outside of the board there, they probably couldn't, is this still ground up here, I don't know, they couldn't get it

**Dave Jones:** around here like this, so they just decided, oh, let's just use the metal case. We've already got, here's our ground input wire here, already got ground here, we can get, we can use the switch as a jumper, and that's not uncommon in products, but in this case, they've come a gutzer, and the

**Dave Jones:** One Hung Low brand Shenzhen market switch special in there has just, yeah, the sliding contacts have shorted out, and that's it, I think somebody even mentioned that, oh, it, uh, it shorted out all three or something like that, no, no, it's, I guarantee you, it's, uh, it's shorted over, those two have

**Dave Jones:** shorted over in there, and the other thing, uh, a couple of people mentioned as well, did, uh, Huxley, like, chew on this thing and get saliva in there, maybe that would have shorted it out or something like that, well, A, Huxley's four, he doesn't chew on toys, so there's no, no, there's no saliva getting

**Dave Jones:** into there, B, even if there was saliva in there, it's not going to, uh, you need a, a, basically a dead short in there, a ridiculously low resistance in there to get the current flowing to heat it up, it needs to be, you know, near zero, so it's not going to do that, oh, but the saliva could start

**Dave Jones:** the current and then, well, no, it doesn't work like that, we're talking about three volts here, there's no high voltage DC, so you're not going to get high voltage, uh, DC arc over, which is cause, which is called, and is what happened in, what can happen in my previous, uh, recent video on the solar DC

**Dave Jones:** isolator fail, spoiler alert, sorry, if you haven't seen the video, I'll link it in, uh, where, you know, you get like, in my case, like 400 or even 500 volts from the, uh, PV array string on your roof, well, that's a lot of voltage, and that can, uh, if you get a failed water in your DC isolator, saliva

**Dave Jones:** from the sky, I guess, you get that water in your isolator, then that can start an arc over inside there, and then once that arc over happens, then all the plasmary stuff starts happening, because it's DC, there's no AC to then, you know, reverse current in the other direction, it's just DC,

**Dave Jones:** and it's going to arc over, and it just keeps arcing over and catches on fire, so yeah, nasty stuff, insert photos here, this is a brief demonstration showing the intensity of arc faults on DC solar systems, here we have four solar panels connected together in series, typically DC solar systems for

**Dave Jones:** homes or businesses have many more, by simply bringing the bare conductors into close proximity, we can simulate a fault on the wiring that can be caused by a variety of factors, such as loose connections, corrosion of joints, water ingress, rodents, birds or ants biting through cable

**Dave Jones:** insulation, failed DC isolators, or simply degradation of cable insulation over time, as you can see, with no protection, the arc is very intense, continuous, and a serious risk of fire, so anyone who thinks this is in any way unrelated to an internal shorting switch, well sorry, you're

**Dave Jones:** wrong, that switch open, and or off the board, and then I'm just going to bridge it out, now how would you avoid this at the design stage, well of course, the first problem that went wrong is that you bridged over these pins here, and you probably shouldn't do that, because then you're shorting

**Dave Jones:** out the external case of this, you could have had a series resistor in the positive line going to that for example, but that's an extra part, I can understand why you may not want that, or you could have used ground, fine, you could have used ground your input pin of your microcontroller, but then

**Dave Jones:** you could have used, if there are internal pull-ups in here of this micro, you could have used an internal pull-up, and that could have given you your, you know, your AB channel select, either it's grounded, or it's pulled up high via a resistor, either internal to the chip, or external, but yeah,

**Dave Jones:** to actually hard wire 5 volts like that, you know, fairly chunky trace going over there, and whoop, it shorts out, just went straight through there like that, this switch might have heated up too, so in all likelihood, this chip's okay, because it's, you know, just shorting out the batteries or

**Dave Jones:** whatever, so I fully expect this thing to work when I take out the switch, and simply link those two across there, so yeah, just, I'll just put it permanently on channel B, it's fine, I don't intend to replace the switch, there's just no functional need, yeah, these cheap phenolic boards, they're

**Dave Jones:** terrible, it's just going to crumble in the heat, I don't care how ugly this looks, it's getting what it deserved, oh, it's, it's dropped out, oh, oh, look at the bottom of that, you can see the Bernie, Ernie Bernie on the board, wow, okay, so what I've done now is I've permanently

**Dave Jones:** soldered a link across there, I've done a little break in the trace there, so that power can't get through to there anymore, so the input pin of the micro is tied permanently to the ground over there, and that should do it a treat, and I've actually measured battery terminals with a meter, and I'm

**Dave Jones:** getting 11 meg, so you know, you expect anything non-short, so that's fine, and yeah, I can't get that switch out, so I have to sort of wedge that in there at an angle, I'll put the other switch back, where is it? And no, I'm not going to replace those wires, just to trigger those who want me to replace

**Dave Jones:** it, switch it on, winner, winner, chicken dinner, and we should be able to actually see, can we, I may have to turn the lights off, because camcorder sensors are sensitive to UV, there you go, so there's, there's no tricks, camcorders work just fine, if I stare at that with my eyes,

**Dave Jones:** I can't see it, but camcorders pick it up just fantastic, little, well, can anyone decode that on video? So there you go, that's just a little tip for testing remote controls, get your camera out, and here is a little funky doodad that it actually controls, this is the little,

**Dave Jones:** I did, what is it? I don't know, a pod that goes inside the tube, it races around, obviously you can see it's got a drive wheel here, internal lithium polymer battery there, and just these wheels that, and with this activating lever on the top, like, well, it sort of,

**Dave Jones:** I don't even think it activates, I don't even think there's a switch in there, oh, no, no, I don't think so, I think that just sort of keeps it, sort of a bit of pressure, so that you get, it gets the side of the tube, so that you get contact on your rubber wheel down there, I think that's all it's for,

**Dave Jones:** and you can make it go, so here we go, so if we switch that on, little lights, oh, whoa, there we go, and there we go, so here's an example of the track, which you can assemble into any weird convoluted thing, it's got the little trap door here that you can put it in, so let's switch

**Dave Jones:** it on, and there we go, flishy flashy, and whack it inside, any direction, doesn't matter, all right, let's give it a burl, whoa, ah, and it can get, and it can get caught, like, halfway up, like that, there you go, and you can just reverse it, whoa, fantastic, winner, winner, chicken dinner,

**Dave Jones:** so thank you very much for demanding this video, this high-quality content of replacing a switch to fix this remote control, I hope you liked it, if you did, give it a big thumbs up, catch you next time, whoo!
