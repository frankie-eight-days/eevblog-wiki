---
video_id: W1Q8CxL95_Y
title: EEVblog 1500 - Automatic Transfer Switch REVERSE ENGINEERED
url: https://www.youtube.com/watch?v=W1Q8CxL95_Y
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 33, "3": 49, "4": 65, "5": 78, "6": 85, "7": 94, "8": 105, "9": 114, "10": 123, "11": 133, "12": 153, "13": 166, "14": 183, "15": 192, "16": 205, "17": 220, "18": 237, "19": 247, "20": 271, "21": 285, "22": 296, "23": 312, "24": 324, "25": 336, "26": 345, "27": 355, "28": 370, "29": 389, "30": 405, "31": 415, "32": 426, "33": 444, "34": 455, "35": 476, "36": 489, "37": 499, "38": 511, "39": 522, "40": 534, "41": 543, "42": 558, "43": 567, "44": 580, "45": 588, "46": 600, "47": 609, "48": 623, "49": 649, "50": 671, "51": 683, "52": 691, "53": 702, "54": 713, "55": 729, "56": 742, "57": 755, "58": 764, "59": 774, "60": 783, "61": 798, "62": 812, "63": 819, "64": 831, "65": 845, "66": 860, "67": 869, "68": 884, "69": 897, "70": 908, "71": 917, "72": 927, "73": 936, "74": 947, "75": 958, "76": 972, "77": 981, "78": 992, "79": 1002, "80": 1020, "81": 1035, "82": 1048, "83": 1057, "84": 1072, "85": 1081, "86": 1092, "87": 1104, "88": 1117, "89": 1128, "90": 1142, "91": 1152, "92": 1165, "93": 1175, "94": 1183, "95": 1199, "96": 1211, "97": 1226, "98": 1236, "99": 1250, "100": 1260, "101": 1273, "102": 1285, "103": 1302, "104": 1322, "105": 1334, "106": 1358, "107": 1368, "108": 1389, "109": 1402, "110": 1420, "111": 1433, "112": 1445, "113": 1467, "114": 1476, "115": 1485, "116": 1503, "117": 1519, "118": 1525, "119": 1544, "120": 1554, "121": 1568, "122": 1580, "123": 1587, "124": 1600, "125": 1607, "126": 1617, "127": 1629, "128": 1646, "129": 1658, "130": 1669, "131": 1682, "132": 1693, "133": 1705, "134": 1715, "135": 1724, "136": 1745, "137": 1758}
---

**Dave Jones:** Hi, I've got a real interesting bit of kit for you today that I'm going to uh actually install in my house for my solar battery backup uh solution. But before I install it, I thought I'd show you what it is and uh then do a teardown I or how it works in its operation and then uh do a teardown of it to show you how it works inside because well, I

**Dave Jones:** don't know cuz I haven't torn it down apart yet. This is what's called an automatic transfer switch. It's designed It's got two different mains inputs. Uh it tells you here with nice infographics uh connects to the city power grid and also a backup generator.

**Dave Jones:** That it's a uh DIN rail mount uh thing. It's about 50 bucks Aussie or something. You might be able to get it uh cheaper than that. It's got a manual or an automatic mode so you can manually switch between source A, these you know, the the grid or B, source B, the backup generator.

**Dave Jones:** But it can do this and sense automatically, hence why it's got these sense wires uh coming over here to some internal uh well, maybe electronics, maybe not. Maybe it's some dumb ass like diode relay logic or something like that um inside which is probably more like what I'd expect.

**Dave Jones:** But anyway, we'll see. So we've got our grid uh power input here, active and neutral here. They just call it AL1, active line one, I guess. And then we've got our uh second input here which is our comes from our generator.

**Dave Jones:** But we can actually reverse this. And this is how I'm actually going to use it. I'm going to use it reversed. But I'll explain and show you that later.

**Dave Jones:** So the second input here and then the output which goes to your load is down here which you want to uh power and have backup of uh which is what we're going to do.

**Dave Jones:** In my particular case, I'm going to be powering some fridges. So this is actually a two-pole one. You can actually get a three-pole and a four-pole one uh as well if you want um you know, the additional phases or whatnot.

**Dave Jones:** So it breaks the neutral and it breaks the active as well. So depending on which uh source you select, either this one or this one, it switches it through to here.

**Dave Jones:** And that So both of these devices all in here are just going to be a big like mechanical selector uh switch, just switching either of these inputs to the output.

**Dave Jones:** Easy. Let's go to the Dave CAD and I'll show you what I'm doing here and an application for one of these automatic transfer switches. So, this is for my particular application, okay?

**Dave Jones:** You can actually install this for different types of applications, but this is what I'm going to be doing at home. What I want to do is I've actually got three fridges and freezers at home and I want to power all of these from my new uh 3.6 kWh backup battery that I've got which is seen in the previous uh teardown video, link it in if you haven't seen it.

**Dave Jones:** So, 3.6 kWh should just be enough and I just tested it last night actually, it did actually last. Should be enough and it will run I'll do another video running through the numbers, the consumption figures, and figuring out what size backup battery we need and everything else.

**Dave Jones:** But anyway, um that won't be this video. So, what I want to do is disconnect the fridges from my house uh circuit entirely, okay? So, this is your grid that coming in here to your fuse box here and normally the fridges would just be plugged in as you know, I just yet another load inside the house.

**Dave Jones:** But I specifically want to power these like all day, every day from my battery. And I want to charge my battery from my solar system during the day and use that energy at night.

**Dave Jones:** And we don't actually need this automatic transfer switch we've shown here to actually do that, but I'll explain why it's vital actually to have one of these things. Otherwise, you're going to come a gutter.

**Dave Jones:** Now, this is totally different to what's called an AC battery solution for your house, like a Tesla battery or an Nphase battery for example. So, we're not going to look at that and this is not the same as a hybrid inverter which I'm looking at installing as well with a an additional backup battery.

**Dave Jones:** This is just like a standalone independent thing I want to do with these fridges cuz I want to utilize more of my solar output um and I want to like lower my grid consumption cuz at the moment at at night time remember all your fridges and freezers they're running 24 hours a day.

**Dave Jones:** So during the day my solar I've got two different solar systems. One's the Nphase micro inverters, the other is the Sunny Boy string inverter, but it makes no difference, okay?

**Dave Jones:** I've got two different inverters which then put the power onto my fuse box essentially like in parallel with the grid and everything else. And everything I power during the day include I didn't draw my little ionic EV I've got my Zappi charger which actually tracks with the solar output with current transformers on there and allows me to modify the current going into my EV to actually match the solar

**Dave Jones:** output the excess that I would otherwise be wasted pissing away feeding it back into the grid in that direction and getting paid an absolute pittance for it. I want to put it into my EV and I want to put it into my battery to power my fridges at night time.

**Dave Jones:** So what I've done is I've totally disconnected my fridges from the rest of the circuits in my house and they're connected to the output the 240 volt inverter output of my battery generator.

**Dave Jones:** So just imagine that transfer switch is not there, okay? Like that and you could as I said you don't need the transfer switch. You can just I can just connect the fridges directly on the out outlet here and also a this provides some backup power points just in case the grid power fails.

**Dave Jones:** It's incredible people ask but it's incredibly rare here in Sydney. Like I've lived here all my life and the biggest power outage we've had is like five six hours maybe and they're incredibly rare, okay?

**Dave Jones:** So that's why I don't need like a whole backup solution for the whole house and because the power fails all the time. It does happen like up the Blue Mountains for example or other remote areas and stuff like that.

**Dave Jones:** Yeah, your power could be intermittent. In Sydney it's pretty schmick. So anyway, I've got a backup power point and I want to power my three fridges. Say that three times quickly.

**Dave Jones:** Three fridges three times quickly. Um, to power those from my battery. Now, I have actually done the calculations and I'll go through it in another video, but the 3.6 kWh is enough to power these fridges overnight.

**Dave Jones:** But, before I get into the complexities of my solution, right, just imagine that automatic transfer switch is not there and you're happily powering your fridges, right? You get enough power in during the day to recharge the battery and then at night time the fridges are just uh powered from that, right?

**Dave Jones:** Because the battery that I've got um, it actually during the day, if you keep the mains connected here, if you actually keep it plugged in to like the grid here, it will actually just supply, it'll keep the battery topped up to 100% or 90% or whatever you set it to, and then it'll supply the fridges.

**Dave Jones:** Anyway, I'll explain how I'm going to do that in a minute. The automatic transfer switch, okay? If you don't have this, right? If this didn't exist and this was just wired straight through to here, what happens if for some reason something happened uh to the generator and the power I don't know, it it failed.

**Dave Jones:** Somebody pressed the switch or it, you know, there's an internal circuit failed, something happens or whatever, or it didn't get enough energy during the day to charge it, or, you know, there there's quite a few things that can go wrong here.

**Dave Jones:** Then, if you're not alerted to that fact, then your fridges are going to defrost pretty quickly and you're going to lose all your frozen stuff. So, yeah, that's going to ruin your day.

**Dave Jones:** So, what the automatic transfer switch, by putting this in here does, it it has a priority input, which I'm going to set as my battery. So, during our normal operation, the priority input comes from the battery and that powers the fridges during the day, as I said, it can be powered from the solar like this automatically.

**Dave Jones:** If this battery fails or it goes flat or does whatever, you know, something, you know, there's a lot of complexity in here. It's got a battery, it's got an inverter system, it's got a charger system, you know, there's a lot of stuff that can go wrong.

**Dave Jones:** So, if for some reason this does fail, this automatic transfer switch, which we've got here, it'll automatically detect that the bat that the generator input has actually we which is the battery has failed and then it'll automatically within like 50 milliseconds or so, it'll switch over to the grid.

**Dave Jones:** So, it'll keep these fridges and freezers all running regardless of what happens. And then as soon as the battery comes back online, I eat you might start you know, somebody tripped the cord or whatever.

**Dave Jones:** Right? And you and you fix the problem, you plug it back in. Well, it'll automatically detect cuz this is the priority input. It'll automatically detect that, "Hey, my battery system's back up.

**Dave Jones:** I'm going to switch from the grid back to the battery." And that's what these automatic transfer switches do. They're very cool. But ordinarily, you would use them the other way around.

**Dave Jones:** Just like what's showing actually on here. Normally, the city power would be the priority input. And then only if the grid fails, then your backup generator will kick in like this.

**Dave Jones:** But I'm actually going to use it reverse. I'm going to actually plug my battery into the priority input, which is the city power, and then have the grid as my backup power.

**Dave Jones:** And you can do that. It it doesn't know the difference. In fact, if you have a look at the instructions over here, it kind of in English it tries to actually tell you this.

**Dave Jones:** Normally, you've got the city power and then source B is the backup power. But note for solar type, the backup power must be connected to the city power. So, it's basically implying that the city power is the priority input.

**Dave Jones:** That's basically what it's saying. If you had another brand of what one of these things, its instructions might say, you know, priority input, you know, backup input, something like that.

**Dave Jones:** Anyway, those who had their thinking caps on might see a problem with my setup that I want to run here. Okay, during the day the solar sun hits the solar panels, inverter, it charges my battery up to, you know, 90% or whatever I set, 100%.

**Dave Jones:** Okay? Then but at night time, it won't come from the solar anymore. It'll come from the grid. So, this battery would never be used to power the fridges, huh?

**Dave Jones:** How does that work? Well, what I'm going to do is I'm going to stick a mechanical doot doot doot timer in there, mechanical or an electronic timer or whatever.

**Dave Jones:** And I'm going to set this to actually disconnect it like 4:00 p.m. in the afternoon once the sunset, and then I can switch it back on at you know, 9:00 a.m.

**Dave Jones:** or whatever. So, from 9:00 a.m. to 4:00 p.m. for example, yes, it'll actually um slow charge um maybe like I I think I've I haven't I have to run the calculations again with the third fridge, but like 400 W should be enough during 9:00 a.m.

**Dave Jones:** to 4:00 p.m. to actually fully charge the battery and then have enough power uh for the night time. Just Just based on calculations and measurements of the consumption of the fridges, then I can actually tailor this time and this charge level to actually be just be enough, you know, with some contingency added on so that during the day, like even on the most cloudiest, overcast, crappy day, I'm still going to get like

**Dave Jones:** 3 400 W out of out of this, and I can dump that all into the battery. So, at night time, I can just use a simple mechanical timer, and bingo, I've got myself a an independent battery backup solution that powers all my fridges from my solar and from my battery without having to have some smart-ass AC battery system and stuff like that.

**Dave Jones:** So, you can do this. You can implement it yourself in pretty much any scenario. I think it's really cool. Anyway, I will do when I install this thing, I'll show you an installation and testing and measurements video and all that sort of jazz.

**Dave Jones:** For those that want to see it, there's the entire sheet there, and what's on the other side? I don't know. At least it's all in English. Anyway, for those interested, it does actually come in different models.

**Dave Jones:** I've got the uh 63 amp jobbie here, I think. It looks like it's a breaking current here, 50,000 amps, kiloamps. Thank you very much. It's rated for 8 kilovolt impulses.

**Dave Jones:** That'll be for, you know, the electronics and whatnot, or it doesn't arc over or whatever. Anyway, its transfer time is 50 milliseconds. So, this is just basically like a relay operation.

**Dave Jones:** I You can actually get much more expensive versions of this, which are electronic versions, which have zero switchover They're designed for like real critical backups. Like, you know, if you've got a big server rack or something like you can't just have a big clunking mechanical switch going thump like this.

**Dave Jones:** You know, your server's going to hiccup or whatnot. You know, this will be a break-before-make system. So, yeah, you can't rely on that. And it looks like it also has a single-pole double-throw relay on either side here.

**Dave Jones:** So, this would be for like external indicator lamps. Like, it's got internal indicator LEDs here, but yeah, you can hook up big, you know, like if you hook wired into a big panel or something like that, you could have a big flashing rotating light that the power's failed or whatnot.

**Dave Jones:** Okay, so let's demo this before we tear it down, shall we? I've got my high-voltage differential probe on the output here. I don't have any load. It makes absolutely no difference.

**Dave Jones:** Then I've got a black mains cord input here. That will be the generator, but in this particular case, this will be my will be the grid in my particular application.

**Dave Jones:** And then the gray one up here will match the grid up here. Okay, so let's put it in automatic mode here, and we'll just So, we'll plug in the generator.

**Dave Jones:** It's currently set to the generator, so it shouldn't flip anywhere. Okay? There we go. And there's our mains up there. So, of course, if I wanted to, I can switch over to manual and go clunk like that, and the output is disconnected, and I can clunk it back like that.

**Dave Jones:** It looks like this just indicates It doesn't indicate which one's on. It just indicates which like that there's actually power active there. Now, if we switch this back to auto mode, then the priority input should be this city one.

**Dave Jones:** It should be this gray one. So, at the moment, it's back to the generator, but it should switch back. So, this is how like you'd normally use it, okay?

**Dave Jones:** The mains grid has failed. It's come a gutser. Someone's ran into the power pole and the power's failed, right? A lightning strike somewhere. Transformer's been taken out. You're on your backup generator, but then the grid automatically comes back on.

**Dave Jones:** Hopefully, it should detect this and switch. And it does. Whoa, that was pretty violent, wasn't it? And you probably saw that there was actually a changeover time there. But let's look at my configuration where my battery will be the city grid power.

**Dave Jones:** So, this is my battery here, and let's say that my battery fails. Well, it's going to boom. It physically Did you see it jump? Physically vibrates in there. There must be a huge spring mechanism in there.

**Dave Jones:** It's anyway, that'll be an interesting teardown, but you can see that yeah, that is just going to come back. Okay, so we're currently sourcing from the grid, okay? And if our backup generator fails, nothing happens.

**Dave Jones:** If we do that, then and we're from source B, it will boom, go back to the priority source. Okay, so let's see if we can actually capture the mains switchover time.

**Dave Jones:** So, I've set my trigger here to actually pulse with negative like this and I set it like 8.8 milliseconds or something like that. And that should, hopefully, capture. So, single shot capture.

**Dave Jones:** Let's give it a go. And boom, there we go. Our switchover. And you can see this was before it was coming from source A, so it was coming from the grid.

**Dave Jones:** And then it's 20 milliseconds per division. So, it took about, you know, 20 milliseconds or something like that to switch. You can see some see some switch bounce in there.

**Dave Jones:** No wackers, that's what you'd expect like some contact bounce. It's As I said, this is not an electronic switch. This will just be like as you can hear a physical thumping mechanical switch.

**Dave Jones:** So yeah, it has actually switched from one source to the other even though it looks like the same source because it literally is because we've plugged it into the same mains board here.

**Dave Jones:** But if you had different source voltages, different source frequencies or whatever and they were asynchronous, then you would see it you know, change. And there's the other direction. I think that's a bit quicker.

**Dave Jones:** They're 5 milliseconds per division. 5 10 like 8 milliseconds or something to switch from the backup grid back to the priority source. Well, there you have it. Isn't that interesting?

**Dave Jones:** We got two big ass solenoids here. Like it had to have some sort of spring type system and sure enough if I rotate that, you can see that that shaft just rotates like that.

**Dave Jones:** And of course the big thump and you know, bounce that we saw is just like the solenoid acting so quick that it you know, it just pulls it in one direction or the other like that.

**Dave Jones:** And there's a shaft there with two little micro switches on it. So maybe that has to do with like the actual reversing action that's part of the logic. Maybe I'm not entirely sure.

**Dave Jones:** And like as I suspected, there is like no active circuit doesn't look like there's any active circuitry in here. It's all like relay logic. Are they diodes? Yep. Yep.

**Dave Jones:** So it's like some sort of diode relay logic type thing. And this is interesting. Check this out. This is the load output here and they've actually got huge big braided Yeah, it's just welded onto that plate there and that must I don't can't see how that goes down to the bottom side.

**Dave Jones:** The reason that they do that is so that you've got some compliance when that moves because this is rated for I think 5,000 cycles. So you know, when when this moves back and forth even though it doesn't move a a right?

**Dave Jones:** There is going to be stress in there, so that needs to, you know, expand and contract. And of course, carry the maximum rated current as well. So, yeah. That's and you know, there's just a big contactor plate inside there.

**Dave Jones:** So, the whole assembly actually just lifts out. And yet, there's no additional stuff on the bottom. We'll reverse engineer this in a sec. Oh, okay. So, this relay here, which I thought was NEC, but it's not.

**Dave Jones:** It's NNC. Thank you very much. Um yeah, that's actually doing the normally open uh normally closed uh contacts, the auxiliary contact. So, is that also powering the solenoid? Anyway, we'll find out.

**Dave Jones:** Giant lever in there, which just goes ka-klunk ka-klunk like that. So, yeah, you've just got alternating uh fields on these and then it just goes doop doop slam like that.

**Dave Jones:** So, as one pushes in, the other pushes out. They're physically connected. And that's just connected to the manual switch on the bottom like that. And there you have it.

**Dave Jones:** We can actually see inside. Watch this come over. Look at this giant arm like that just come over. Boom! Like that. So, that's what takes the, you know, tens of milliseconds to switch over.

**Dave Jones:** And they've got giant pads in there. Check out the size of those pads. So, they're absolutely enormous. So, yeah, that's very simple. There's nothing else in there. Not sure what these uh they're just strengthening bars, are they?

**Dave Jones:** They don't look like part of any of the current carrying capacity at all. So, not sure what's doing there. All right. So, I've reverse engineered this. Um it it took quite some effort.

**Dave Jones:** It's it's fairly obvious once you know, but you know, to actually get it right, I had to desolder the relay here. And uh so, hopefully I've got an exact duplicate physically of what's happening here.

**Dave Jones:** These red wires, this red side is the grid side here. And this these blue wires and this blue solenoid here is the backup uh side. And we've got Dave Cad here.

**Dave Jones:** This is the rare portrait version, none of that landscape rubbish. So, yeah, quite rare to see it here. I believe I've got an exact duplicate here. So, we've got the two solenoids up the top here like this.

**Dave Jones:** We've got the lever arm here, and I've got it in the grid position over here, okay? So, we're going to assume that we have both power connected to the grid and to the backup as well.

**Dave Jones:** And our switch is physically in the grid position, okay? So, it's all operational, it's powered up, and we're going to assume that our switch is in the automatic mode as well.

**Dave Jones:** And I've shown this auto manual switch here is this switch here. So, I've put it in the auto mode here. And interestingly, it turns out that the auto manual switch, all it does is simply disconnect the solenoids.

**Dave Jones:** It completely disconnects them. Once you put it in manual mode here, you'll see that it disconnects the solenoid through each solenoid powered via a diode bridge here, which is effectively like straight across the mains.

**Dave Jones:** So, this is the backup mains input live and neutral, grid mains input live and neutral here. And the relay is down here, and that's this relay here. I haven't drawn in those extra auxiliary contacts, cuz they have nothing to do with the actual operation of this.

**Dave Jones:** Suffice it to say, this is a four-pole double-throw relay in there. And there's two MOVs in there across the diode the AC input to the diode bridge, they're the two blue MOVs there.

**Dave Jones:** They're 681s, which is about 480 V RMS jobbies. And by the way, there is the LED here is simply a LED and a dropper resistor. That's it. It's a 150 K dropper resistor and a LED across both line and neutral here.

**Dave Jones:** I'll just leave those out for simplicity. Because as you saw, those LEDs don't actually tell you which one's active. They just tell you that you've actually got power coming to the input.

**Dave Jones:** So, they're they're just straight across there. And then we've got our two micro switches here. These are effectively like end of throw limit switches. So, they actually come on they're they're actually normally closed switches.

**Dave Jones:** So, in this position here, in the grid position, this this micro switch is actually active, but because it's normally closed version, when you activate it, it actually becomes open.

**Dave Jones:** And I physically demonstrated this here. How it works is slightly different, but I think this is a better representation. With the armature in the grid position like this, it's going to actually close the micro switch for the backup solenoid over here.

**Dave Jones:** So, I've as I said, I've put all of these switches in the in the current grid position. So, the backup micro switch is enabled. So, the solenoid for the backup solenoid here is sitting here ready to be engaged, but neither of these during static operation, when it's not switching, neither of these are energized.

**Dave Jones:** So, this is actually quite clever. Stick with me. Now, the the relay coil, these two pins here, they're actually connected across the grid side. This is why the grid side is the priority side.

**Dave Jones:** So, you want your priority source to be connected to the relay. So, we're assuming that we have got our grid power here, our priority power source is active, and that pulls it it's normally here when you de-energize the relay, it's normally in the backup position, but when you energize it, when you apply power to the grid, it pulls the contacts this way, and then it's in the grid position like

**Dave Jones:** this. So, at the moment, the bridge, the diode bridge here for that's powering the solenoid here, is actually on. You can see it's physically connected through to here, okay?

**Dave Jones:** So, it's it's energized, but the micro switch here is disconnected. So, the solenoid's not active, and likewise, the backup solenoid here, well, it's connected to the diode bridge. The diode bridge is unfortunately not activated because it's disconnected here cuz it's in the grid position.

**Dave Jones:** So, it's open. So, what happens if the grid, the main priority power source fails? You remove the power from here, well, the relay suddenly switches, de-energizes, and switches back over to here.

**Dave Jones:** So, what that does is instantly activate the uh apply power to the diode bridge for the uh backup side here. And because this micro switch is physically closed by this lever here in this position, okay?

**Dave Jones:** As soon as this power fails, then this diode bridge is going to get power to it, and this micro switch is closed, and this solenoid is going to activate, and it's going to go ka-klunk and pull this armature from here over to here.

**Dave Jones:** But, of course, it's going to take time for this arm to physically travel all the way over like that and deactivate this micro switch and activate this one, okay?

**Dave Jones:** So, it's going to take, you know, like 10 milliseconds or something like that. So, the solenoid activates briefly, and then the armature starts moving, and when this micro switch disconnects, uh there's no more power for the solenoid, but the solenoid has done done its job and effectively latched the switch over into the other position.

**Dave Jones:** Neat. So, it's like a latching relay. So, this micro switch is now closed like this, and it's this solenoid is sitting here waiting, "Oh, come on, give me power.

**Dave Jones:** Give me power so I can switch uh from the backup back to the grid side." And of course, because this is the priority power source, it has the relay coil on it.

**Dave Jones:** So, as soon as the line workers are finished fixing the grid, good on you, champs, um then it applies uh power back onto here, and the relay flips back, and then this solenoid activates very briefly, and it goes clunk back into the other position, and it's reset itself.

**Dave Jones:** So, it goes flop like that and flip backwards. And it's basically a latching relay like that. That is a really neat system. I like it. It basically relies on the physical time that it takes for this thing to, you know, travel over.

**Dave Jones:** You know, you saw it on the scope there, tens of milliseconds or whatever. Um but that was enough time to activate the solenoid and pull that armature in and clunk.

**Dave Jones:** And when it's static like this, none of these solenoids are active. And of course, if you switch this to manual position, it just disconnects uh the diode bridges. They're They're They're They're not connected anymore, so you can just manually just go clunk clunk like that, and it makes no difference to the uh relay circuitry at all.

**Dave Jones:** Wait, hang on. We've got a bonus. We've got a different brand. Let's see if it's the same. It looks uh very similar. In fact, the boxes are all near identical.

**Dave Jones:** This here is the new The box for the new one. It's an automatic transfer switch, dual power. This is the one we tore apart before, the dual power automatic transfee switch.

**Dave Jones:** So, yeah, I'm I'm I'm going to guess that this one is more of the real McCoy genuine article, and this one we looked at before is the dodgy brothers uh cheaper one.

**Dave Jones:** So, let's quickly open this. And as you can see, it's actually it it looks a bit better. I prefer this uh switch to the other little slidey switch over there.

**Dave Jones:** This is much better, and this is physically really really hard to move. Wow. And on the bottom here is a bit different. It uses a better quality DIN lock-in mechanism.

**Dave Jones:** It just It just looks and feels like a, you know, a better quality unit than what we just tore down. So, inside, it looks like the operation's going to be absolutely identical.

**Dave Jones:** I wouldn't even bother reverse engineering this, but I like how it's got separate boards off here. The diode bridges are off on a different board. So, let me get that open.

**Dave Jones:** That's just a relay board. It looks like it doesn't have the auxiliary contacts. That's only a two-pole, is it? Rather than a four-pole. We have before. But, look, it's basically exactly the same operation.

**Dave Jones:** We've got the lever arm here, which is much more difficult to pull across like that. But, it basically works absolutely identical. So, it's got the override switch here, and this is why it's it's it's lever force is not as good as the other one.

**Dave Jones:** So, it requires more force to actually change it over. But, they've got the bridge down there and the mob on a separate board like that. But, check out the limit switch here, like the end of travel switch here.

**Dave Jones:** It's like a big PCB, big blocky PCB mount thing. I've never seen one like that before. I'm not going to take it apart further. But, yeah, you can see the armature in there.

**Dave Jones:** It works exactly the same way as the other one. So, yeah, but I like the look of that. You know, that micro switch just looks bigger and beefier. But, if I had to guess, I'd say this is the real McCoy.

**Dave Jones:** Does it have a brand? It doesn't actually have I I have to get the documentation. Anyway, I reckon that's the real one cuz it's a transfer switch, not a transfer switch um like that.

**Dave Jones:** And that Yeah, so this no fuel one, I think it's a slightly cheaper knockoff of this This might be the original one. I don't know. If you know the history of you know, who is the originator of this actual design, then please let us know.

**Dave Jones:** But, there are significantly different implementations there. I can't get that um I don't know how to get the rest of that switch open. I think I'd have to destroy the whole lot.

**Dave Jones:** I'm not really interested in that to look at the actual contactors in there. But, yeah, you know, I I think this one it's the vibe. The vibe of this one is better.

**Dave Jones:** But, there you go. I hope you found it interesting. Automatic transfer switches absolutely fascinating and they're really simplistic, but incredibly um clever how they actually work these things. You know, you've got your priority source and it's just basically a latching relay um type system, so to speak.

**Dave Jones:** So, fascinating. Hope you liked that. If you did, please give it a big thumbs up and as always discuss down below. And I don't do it very often, but thank you for all my uh patrons over at uh Patreon who uh did help keep funding this whatever it is I do.

**Dave Jones:** All right. Catch you next time.
