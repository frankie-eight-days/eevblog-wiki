---
video_id: U7soJAFbKwY
title: EEVblog #782 - The Dangers Of Reflow Soldering
url: https://www.youtube.com/watch?v=U7soJAFbKwY
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 35, "3": 57, "4": 77, "5": 92, "6": 102, "7": 116, "8": 141, "9": 156, "10": 178, "11": 185, "12": 204, "13": 219, "14": 239, "15": 255, "16": 266, "17": 284, "18": 299, "19": 311, "20": 322, "21": 339, "22": 349, "23": 366, "24": 378, "25": 394, "26": 405, "27": 424, "28": 434, "29": 446, "30": 454, "31": 470, "32": 481, "33": 496, "34": 508, "35": 519, "36": 537, "37": 553, "38": 575, "39": 588, "40": 600, "41": 620, "42": 646, "43": 661, "44": 671, "45": 685, "46": 697}
---

**Dave Jones:** Hi, here's a real trap for young players. Look what can happen to an already populated PCB if you try and reflow it in a thermal oven. Hmm, I don't think our connector's going to fit anymore.

**Dave Jones:** Oops. Look what's happened to all these through-hole connectors on this Samsung uh dumpster dive 56-in LCD TV I've got. Look at that. Just melted them. Ugh, horrible. Look, the uh flat flex connector survived just fine.

**Dave Jones:** Why is it so? Now, as you saw in a previous video, and if you haven't, I'll link it in down below, check it out, where I tried to repair this uh 46-in Samsung LCD TV I got in the dumpster, and I successfully uh reflowed the T-con processor board here in my reflow oven, no problems whatsoever.

**Dave Jones:** Unfortunately, it didn't fix the uh fault, but I didn't actually damage the board at all. So, I thought, "Uh, you know, I'll reflow the processor board." Um so, I took it out, whacked it in my reflow oven, exactly the same thermal uh profile as what I used for this uh T-con board, and that's what happened.

**Dave Jones:** Hmm, bummer. So, why was there no damage to this uh T-con board at all, even though it's got a very similar-looking connector up there, but this one just melted all of these connectors right along the edge here?

**Dave Jones:** Well, if you'll notice, these are actually uh through-hole connectors on the bottom here. I've actually um uh desoldered a couple of them, but you'll notice that these are all through-hole connectors.

**Dave Jones:** Every single through-hole, there's four of them, and they all melted on this board. Whereas, the T-con board here survived just fine, but you'll notice this connector up the top here is not a through-hole connector.

**Dave Jones:** It's actually a surface mount connector, and that's the key to what's happened here. Because as a general rule, surface mount connectors like this one, even though it looks almost identical to this one apart from all the melting, is that these surface mount ones are designed using higher temperature thermoplastics to actually survive the reflow soldering process used in surface mount boards like this one.

**Dave Jones:** And likewise with this high-density ribbon cable surface mount connector, it's designed with plastics which are designed to survive the temperature profiles. And these through-hole ones are clearly not as higher temperature rated or for as long.

**Dave Jones:** They might survive the same peak temperature, but these this particular type or brand or model or whatever might actually survive them longer than these particular through-hole ones here. Cuz when you solder through-hole components, of course, you're only heating the individual pins on the bottom if you're hand soldering or if you're wave soldering.

**Dave Jones:** Of course, there's a big bubble in solder wave under the bottom here, which then goes along and heats up all the individual pins. And the individual pins are getting hot.

**Dave Jones:** They can get just as hot or hotter than the entire connector here, but that is the difference. In a reflow oven, the entire connector, including all of the plastics, is slowly brought up to temperature, slowly rises up, gets hotter and hotter, and all of the plastic gets to that temperature.

**Dave Jones:** So, if they're not designed to survive it, like these ones here clearly aren't, then oops, that's what happens. But even if you're buying proper surface mount connectors like this, supposedly designed to survive the reflow soldering process, you can still have issues.

**Dave Jones:** Now, here's a photo of some connectors which at a former company we bought these connectors, and look what happened to them. They just melted. These are right-angle through-hole pin headers that were supposedly designed to survive the reflow soldering process, but this particular batch we got weren't.

**Dave Jones:** I don't know, they might have changed the plastic mixture or whatever happened. Supposedly we got them from the same supplier. I don't know, we might have got duped, might got a might have gotten a cheap, you know, clone rip off parts from the Shenzhen market or something, but that's what happened.

**Dave Jones:** From one batch we ordered another batch, worked perfectly. So, yeah. I it's all to do with the type of plastic and the temperature rating of the plastics used in the connector.

**Dave Jones:** Now, here's a typical reflow temperature profile for some lead-free solder paste. This comes from a previous video which I've done, so click here if you haven't seen that where I actually use the thermal oven and reflow the boards and get some data logging plots of my oven here.

**Dave Jones:** And basically, you know, there's all these different they're separated into different sections, but it basically slowly ramps up like this, hits a peak, and then cools back down. Basically almost as fast as it can possibly.

**Dave Jones:** So, you're the reason that it's like a big thick like that is because this is like the temperature range the acceptable temperature range for that particular solder to operate in.

**Dave Jones:** And each particular type of solder is going to have its own type of profile. Different parts can have different temperature profiles. You'll often see temperature profile recommendations in component data sheets as well.

**Dave Jones:** And likewise, for surface mount components, here you go. Look up the data sheets for them and you'll likely find a thermal profile for some of the better manufacturers. For example, here's a data sheet for a high rose, which is a pretty reputable manufacturer of these type of connectors, the DF 13 series.

**Dave Jones:** Look, here it is. Recommended temperature profiles. You You see the preheating uh phase here. These are the different phases I was talking about of the soldering process. And look at this.

**Dave Jones:** Look, max 230° here for 60 seconds soldering. If it goes over 60 seconds, all bets are off, right? And they they don't basically do not guarantee that uh and it tells you down here as well in this table.

**Dave Jones:** Look, more than soldering more than 220° C for 10 to 30 seconds. So, you know, if you go over that the things can melt and it doesn't take that long at all.

**Dave Jones:** Uh you know, you could go 10 seconds over and that could be the difference between your connectors melting and not melting. And here is the actual temperature profile of my beta layout thermal oven which I captured with my Agilent data logging multimeter and this is a tablet shot.

**Dave Jones:** I did this in the previous video. You can see, you know, it ramps up sort of in a similar kind of way and it reaches, you know, a peak temperature 230° or 240° or whatever it was.

**Dave Jones:** Um and then the the problem with these type of types of cheap ass do-it-yourself ovens, especially the ones that aren't fan forced, they can't cool down very quickly. So, if you don't open that door quick enough and sort of, you know, get all that heat out and sometimes just opening the door is not enough, it can stay there for too long.

**Dave Jones:** And look, we're we're talking, you know, it can stay there for like a couple of minutes, right? That's well over the data sheet values for these sorts of things typically.

**Dave Jones:** So, you know, all bets are off. As I said, you don't know what your particular connectors are going to do unless you got the correct data sheet and some data sheets don't even tell you all that sort of stuff.

**Dave Jones:** So, it's all pretty hit and miss, but basically, yeah, you've got to not try and keep them at a hot temperature like this for too long, just the absolute minimum required.

**Dave Jones:** So, it's a really fine balancing act. So, in the case of this board here, we just got unlucky. And uh well, you know, you could have uh thought that well, okay, these are through-hole connectors, maybe we should take care.

**Dave Jones:** I actually, by the way, put the board in like this, so these connectors were at the front, so I couldn't even visually monitor uh those connectors uh at the back here.

**Dave Jones:** So, you know, if I really had my uh brain um in gear, and I know this stuff, so I should have like gone, "Oh, yeah, okay, I should be extra careful with uh you know, these through-hole connectors, maybe there's some issues there or something like that.

**Dave Jones:** Put them at the front, really start to monitor them." But by the time you start seeing it melting, it's probably too late. So, yeah. Um yeah. Oops. Just completely come a cropper.

**Dave Jones:** And other data sheets for this uh TE Connectivity one, for example, um this is a through typical through-hole uh boxed pin header like this. And um look, it's wave solder capable, okay?

**Dave Jones:** It doesn't say anything about reflow at all in this data sheet. So, unless you specifically went and asked the manufacturer, that you know, you just don't know if this is compatible with say the uh paste uh in pin uh soldering process.

**Dave Jones:** And that's um here's actually a uh shot courtesy of uh Phoenix Connectors. They've got a um like an app note uh thing on this, and this shows how you can actually uh reflow solder uh regular through-hole connectors using a reflow oven process.

**Dave Jones:** You actually put paste inside the hole, then put in the connector in, and then reflow it like a surface mount component. But if you use one of these uh connectors which doesn't have the high temperature uh thermoplastic in it to enable that, and it's only wave solder compatible, and you haven't checked, well, you can come a cropper just like this.

**Dave Jones:** So, the moral of the story, just be careful using these cheap-ass do-it-yourself thermal ovens. They're not that great. They're not that precise, not that controlled, and just be aware that you can actually have problems like this.

**Dave Jones:** And in this case, I was probably a bit gung-ho. You know, I just reflowed the T-con board, and it just survived fine and dandy. So, I just whack this one in, not giving it a second thought.

**Dave Jones:** Doh! Silly me. Through-hole connectors on the side. Cuz apart from that, everything else on this processor board survived just fine. It was just these right-angle connectors. In this case, the particular type of plastic, particular connector, who knows who the manufacturer is, who knows where they sourced them from.

**Dave Jones:** They just didn't like it because this board is they almost certainly soldered this thing using a wave, like a two-step process. They did the SMD reflow stuff, of course, which is, you know, 95% of the stuff on here, and then they put it through a dip soldering process, a wave soldering process, where it all bubbles up underneath, and solders these connectors on the edge here.

**Dave Jones:** So, I was actually able to desolder these things pretty easily using my desolder pump. So, you know, probably ultimately repairable. It's not too big a deal just melting some connectors like this if I can get replacement ones or or an equivalent one and just sort of bodge it in.

**Dave Jones:** I could even like individually take out the pins and just solder the pins back and just sort of bodge in the connector if I was really desperate, but yeah, it's just a little oopsie.

**Dave Jones:** Trap for young players. Yeah, I got caught out. Hope you learned something useful out of that video, and if you liked it, please give it a big thumbs up and discuss it on YouTube and over at the blog and everything else.

**Dave Jones:** And by the time you see this, I've probably got a new website over at EEVblog.com as well. That'll be like I'll slowly be adding uh more features and stuff to that over the next month or two.

**Dave Jones:** So, check it out. Hope you enjoyed it. Catch you next time.
