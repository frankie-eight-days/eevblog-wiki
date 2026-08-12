---
video_id: 1YK_GlnUlI8
title: EEVblog 1583 - Advanced Oscilloscope Triggering: Glitch/Pulse/Runt/Interval
url: https://www.youtube.com/watch?v=1YK_GlnUlI8
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 46, "3": 57, "4": 68, "5": 82, "6": 98, "7": 111, "8": 122, "9": 138, "10": 150, "11": 160, "12": 181, "13": 198, "14": 210, "15": 225, "16": 239, "17": 250, "18": 259, "19": 275, "20": 290, "21": 314, "22": 335, "23": 344, "24": 357, "25": 372, "26": 383, "27": 396, "28": 406, "29": 414, "30": 426, "31": 444, "32": 455, "33": 465, "34": 474, "35": 485, "36": 496, "37": 510, "38": 528, "39": 542, "40": 551, "41": 573, "42": 587, "43": 601, "44": 616, "45": 628, "46": 638, "47": 648, "48": 661, "49": 675, "50": 687, "51": 700, "52": 726, "53": 738, "54": 759, "55": 771, "56": 781, "57": 795, "58": 810, "59": 819, "60": 835, "61": 853, "62": 863, "63": 878, "64": 891, "65": 903, "66": 916, "67": 932, "68": 944, "69": 958, "70": 966, "71": 979, "72": 994, "73": 1004, "74": 1013, "75": 1028, "76": 1034, "77": 1047, "78": 1057, "79": 1068, "80": 1084, "81": 1098, "82": 1114, "83": 1127, "84": 1136, "85": 1149, "86": 1158, "87": 1171, "88": 1184, "89": 1197, "90": 1210, "91": 1229, "92": 1242, "93": 1255, "94": 1272, "95": 1282, "96": 1293, "97": 1305, "98": 1315, "99": 1331}
---

**Dave Jones:** Hi, I was playing around with glitches in signals for another thing which I might see a future video on, but I thought it'd be interesting to actually show you the glitch capture capabilities or pulse capture capabilities of modern scopes and actually compare them and see how it useful they are.

**Dave Jones:** Oh, you might have seen one just pop up there. What There There it is again. What I've got is I'm just feeding in a pseudo random 1 megabit per second signal a square wave signal into this and it's got a random glitch both positive like going from the negative going up like this and also from the positive going down like this at about a volt and a half or something like that and it's

**Dave Jones:** doing those random glitches about every 15 milliseconds and unfortunately glitches are something that you might actually encounter sooner or later if Murphy's going to bite you on the backside.

**Dave Jones:** Now, sometimes you'll just see like a glitch like something like just pop up on the screen or a briefly. I think I saw it there very briefly actually pop up and you might think oh, what is that?

**Dave Jones:** Well, there it is again. What is that and how do I trigger off that? Well, of course one of the easiest ways to do it of course with any scope you don't need any fancy glitch capturing or pulse trigger capabilities.

**Dave Jones:** If you just want to actually see if something's there of course, you can just use infinite persistence mode. If you ever see like some weirdness happening on your screen not only turn your intensity up for your waveform cuz you'll see it better, but also turn on infinite persistence display.

**Dave Jones:** So, we can actually on this Rohde & Schwarz MXO 4 here, we can go into settings. It'd be nice if they actually had this up the top or a button, but we can turn on infinite persistence here and let me actually reset that, okay?

**Dave Jones:** I'll clear that after a a of seconds. Boom, we got our first one. Boom, we got another one. Uh boom, there's one over here. Uh come on. Come on.

**Dave Jones:** Capture you, bastard. Come on. Oh, we haven't got one for a while yet. Hang on. They'll They'll come in bursts. No pun intended. Mirror a week. Anyway, you can see how that we're actually capturing these glitches there because uh this just builds up.

**Dave Jones:** This display doesn't clear itself. So, it builds up over time and you can get a picture of these actual uh run pulses. Now, how often can we expect to actually see these things?

**Dave Jones:** Well, we can kind of sort of calculate this. So, what we know is our time base here is 1 microsecond per division. Okay, we've got 10 divisions across the screen.

**Dave Jones:** That means we have an effective wind display capture window here of 10 microseconds wide. Now, as I said before that these pulses are appearing every 15 milliseconds. So, that's quite infrequent when you've only got a like a window like a sample window that's 10 microseconds wide.

**Dave Jones:** So, if you divide 15 milliseconds by 10 microseconds, get 1,500. So, if we reset our persistence here, we can only expect to actually capture this glitch like that every 1,500 captures of this entire display.

**Dave Jones:** Now, of course, your uh scope's going to have a waveform updates per second. You know, how many waveform updates per second which changes based on the current time base and the current memory depth.

**Dave Jones:** And the good thing about the Rohde & Schwarz MXO is we can actually see this. We can go into speed down here and we can actually measure and we can see the waveform update rate here, which is about you know, let's call it 720 waveform updates per second.

**Dave Jones:** So, if our scope is capturing one of these 10 microsecond windows at a rate of 730 odd per second, well, we can expect it on average to capture one of those glitches about every 2 seconds or so.

**Dave Jones:** And if we clear it if we wait a couple of seconds, boom, we we got one. Wait another couple of seconds, of course it's going to be more like it's going to be random cuz there's some blind time in there.

**Dave Jones:** Boom, about every 2 seconds. So, you can actually, you know, you can run the numbers on this if you know your acquisitions per second or your waveform update speed.

**Dave Jones:** In most scopes you can actually get that from the trigger output. You can measure it on an external frequency counter. This is the only scope I've got that actually tells me actually the scope actually tells me itself on screen how many waveform updates per second.

**Dave Jones:** But, that's pretty cool, huh? We can actually estimate that. So, I've got a Dave CAD here to illustrate that. You can see that basically our pulses are happening every 15 milliseconds here, but basically because we're we're triggering wherever because there's, you know, it's a very fast trigger rate.

**Dave Jones:** But, we're only capturing this screen here represents only a 10 microsecond capture window as it's called. And really your odds of actually capturing one of those glitches, which are essentially like just moving randomly even though they are a fixed 15 milliseconds apart, as far as the trigger system goes, they're just moving randomly across here.

**Dave Jones:** So, the odds of finding one there are dependent upon your waveform update rate and how lucky you are basically and you know, averages, statistics. So, that's why if I clear that and we're at 700, you know, 30 or waveform updates per second, we expect to capture one every couple of seconds.

**Dave Jones:** Cool, huh? But, the next question is how do we actually trigger off one of these? That's where it gets a bit more interesting and where your modern scopes have features to actually do this.

**Dave Jones:** And the other thing to remember is this has nothing to do with trigger level, right? If I set my trigger level right in the middle there, okay? We will still capture those because it's got nothing to do with uh triggering.

**Dave Jones:** It's just because as I said, they're essentially just randomly wandering in the trigger uh sequence. So, we don't even have to set our trigger level. You can see that we're never triggering off actually one of these things.

**Dave Jones:** So, trigger has nothing to do with it essentially in this particular case, although your mileage may vary. So, modern scopes like this Rohde & Schwarz MSO 4, they will actually have glitch capture capability.

**Dave Jones:** So, let's actually turn off Okay, so we know our glitch is happening there, okay? We've captured it with our persistence view here. So, we know the you know, we can go in there with our cursors or just eyeball measure uh that.

**Dave Jones:** So, we know the pulse width that is happening here. We know the signal level roughly. So, you know, one division up would be a nice trigger level for that.

**Dave Jones:** One division down would be a nice trigger level uh for that, for example. So, if we know the pulse width and we know the trigger level, we can use glitch or pulse uh capture.

**Dave Jones:** It depends on the manufacturer, they might call it something uh different. So, let's turn off the uh infinite persistence display there and we're back to here. And as you can see, like we will very rarely go Well, we got one over there.

**Dave Jones:** So, if we want to trigger off that, we go up to trigger here and then we can choose the trigger type. And this actually has glitch capture here. Now, of course, you can do uh runt and widths and they're different uh styles of trigger, but glitch is essentially a pulse uh width type thing.

**Dave Jones:** Now, let's actually set this up. And you can see we're actually There's something in the middle here as well. So, there's something going on. We're already triggering off something there.

**Dave Jones:** Right, so what we want to do is actually set our trigger level here, which you can to and set here or just use your regular trigger level. Let's try and capture on one of those bottom ones.

**Dave Jones:** So, about a division up. We can either choose shorter or longer. We want the shorter option because it's a short pulse. And then we can set the pulse width.

**Dave Jones:** All right, so we want to set that pulse width just above where we think it is there. Okay? Let's Let's just say 70 nanoseconds or thereabouts. And we're triggering off that thing perfectly.

**Dave Jones:** Okay? Oh, I forgot to mention we're actually in normal uh trigger mode here. Okay? And we can actually do that same thing for the positive glitch up here. Okay?

**Dave Jones:** We can set our trigger level up to here. And boom, we're getting that. But we probably want to set that to negative going now. And bingo, we are now triggering on that actual glitch there.

**Dave Jones:** Neat, huh? Now, because we're actually triggering off this glitch here, we're not just randomly wandering through this window back and forth like we were before. Essentially, because we're triggering on, we expect more than a couple of times waveform updates per second.

**Dave Jones:** And you can see we're actually getting that. We can see here it's actually 30s maybe waveform updates per second. So, now we're actually capturing that. Cuz once we've captured it, it'll rearm and then we'll capture it again.

**Dave Jones:** We will capture that more frequently than when it was just randomly wandering through here. So, we're getting a That's why we're getting a faster waveform updates per second there.

**Dave Jones:** Now, this is actually glitch capture because it's where essentially doing What that means is we're doing pulse capture. That's why on a lot of scopes it'll be called pulse capture because we're specifying the actual you know, the pulse width range in here either shorter either uh lower or more than a certain value.

**Dave Jones:** But because it's based on signal level as well, we can actually use runt capture as well to do this. So, this basically instead of working on a horizontal, it works on a vertical basis.

**Dave Jones:** I've been calling this a glitch, but what this is is actually in this particular scenario is actually a classic runt pulse. So, what a runt pulse is is that you can see that the normal signal level like a you know, it's a TTL type signal level 5 volts, 3.3 or whatever, right?

**Dave Jones:** Digital signal, but a runt pulse means that it only goes up a certain amount of way and doesn't reach a certain it doesn't reach the upper digital threshold because if you know about digital logic, they have upper and lower thresholds before they're actually recognized as a logic one or a logic zero.

**Dave Jones:** So, a runt pulse actually doesn't go all the way up to the second threshold. So, you can actually do and modern scopes actually have also runt triggering. So, that is one of the options there.

**Dave Jones:** So, we can choose runt triggering like this and then we've got an upper level like this. So, we set our upper level like that. So, it might be up here for example and our lower level.

**Dave Jones:** So, it was right down at the lower level down there. So, it transitions through one level, but it doesn't transition through the other level. So, you can see those two levels.

**Dave Jones:** It transitions through one, but doesn't go through the other and that's the definition of a runt pulse. And then we can do range here. We can do just a longer, shorter, within, outside or we can do this automatic find level.

**Dave Jones:** Let's see if we can do this. Okay? Boom. There it is. It automatically found it. Very cool. And you'll see that if I choose the upper limit there and I go below the runt value right in there, it's not going to actually capture it.

**Dave Jones:** It's stopped capturing. It's actually frozen. So, if I actually clear that there, you'll find that we won't actually capture that. It's only when we go above that level, boom, that we start to capture that.

**Dave Jones:** So, but either runt or glitch capture in this case works. And I know you're thinking, "Dave, I can capture this using the fancy pantsy history mode of this MXO 4 scope." Well, yeah, not really.

**Dave Jones:** It's going to be based on luck. Um and that sliding window and the odds of actually capturing it like we saw before. So, if I stop this, okay? Yeah, we can go into history mode and over here, we've got 16,000 acquisitions here and you can go through them one by one by one by one until you try in there of all these waveform captures that it got, but you're going to be

**Dave Jones:** waiting there a long time. You're going to look through it like statistically, we've only looked through like 300 so far. We're going to have to look through a lot more than that before on average we're going to actually find one.

**Dave Jones:** We're going to go through pretty quick, so you could easily visually miss one. My mark one eyeball might not actually see it, but you know, you might eventually get lucky and see one if you're if you're patient enough, but based on the math we did before, you can only expect to capture it every like 1,500 waveform captures on average, so you could be there for a while.

**Dave Jones:** Of course, you can set it to auto scroll through, of course, at a certain speed and you can just try and not to blink and good luck. But those two methods aren't the only ones you can use on this Rohde & Schwarz scope.

**Dave Jones:** It's got another very cool mode, trigger mode, that I'll show you here and you can see that we are actually capturing, but it's a slower update right there. There you go.

**Dave Jones:** But what we're actually using this time is what's called interval triggering here. So, it's one of the very comprehensive, you know, types of different triggering systems. Not every scope will actually have this and we've got interval trigger.

**Dave Jones:** We can set it up shorter here or we can set it longer within or outside. So, it's extremely powerful and we've set the trigger level to there, right? And then I've got the interval width set to 80 nanoseconds there.

**Dave Jones:** And of course it's going to trigger on anything less than 80 nanoseconds. Very It's another way to actually capture it. Check this out. This is very cool. It's got this fine level here.

**Dave Jones:** So it's got this automatic level. Watch this. Fine level. And boom! Look at that. We've captured on this middle one here, which is yet another glitch. In here like this message is booting.

**Dave Jones:** Oh, well, touchy-feely screens. So it's automatically found this glitch in here. This is absolutely fantastic. So as far as I know, this is the only scope I've got that it will actually do that automatic detection capability and stuff like that.

**Dave Jones:** That's It's very cool. So that's very I think that's quite specific to this scope. If you know of another one that I can actually do that, leave in the comments down below, but I just think that's fantastic.

**Dave Jones:** Okay, let's try another excellent modern oscilloscope here, the Siglent SDS 2354X. I don't know that Well, I was looking at it before and it was taking a while, but yeah, it's a I think it's a slower waveform update rate.

**Dave Jones:** Might help if I turn my intensity up a bit. We might see it a bit better, but yeah, not quite. Oh yeah, yeah, got one. We got one. So if we go into our trigger mode here, we go to where the edge type, but we've got all these different types as well.

**Dave Jones:** You notice that it doesn't have They don't call it a glitch like that, but we can use pulse triggering here. It's got runt triggering and drop out and all sorts of things, but we should be able to do the same thing with pulse triggering.

**Dave Jones:** And boom, we've got it here. Now this one does it like explains it a little bit differently here, but we can choose the different limit ranges here. We can choose less than or equal to a value.

**Dave Jones:** We can choose greater than or equal to a value. We can choose within two particular values or we can choose outside two particular values here. But if we choose inside a particular value, so it's within 79 nanoseconds and 2 nanoseconds, boom, there it is there.

**Dave Jones:** No worries. And we can also use the runt trigger thing here. Once again, we can choose the different styles there and we've got the positive edge, but I'm only at 28 nanoseconds at the moment.

**Dave Jones:** So if it tran- if it transitions through this signal level here and not this signal level here, we should be able to pick it up. So if I increase that, but that's also dependent upon the time as well.

**Dave Jones:** Wait, there it is. So once we got greater than the pulse width of that little runt pulse there, which we can actually measure use this as a tool to measure it without using our cursors.

**Dave Jones:** We see once we hit about 55, once this baby hits 55 miles an hour, you're going to see some serious runt pulses. And just to show you that you don't need a big fancy expensive oscilloscope to do it.

**Dave Jones:** Bottom of the range Rigol DHO800 here, no worries whatsoever. There is our glitch. We're using pulse triggering. It's got all the different fancy types. We've got We're using pulse triggering at the moment, but it's got runt, it's got timeout, it's got infed, and it's got duration.

**Dave Jones:** And more things than you can poke a stick at. No worries. And if you choose pulse, you've got the different types here. I've got it set to 80 nanoseconds here.

**Dave Jones:** You just set the level, Bob's your uncle. So we can set our two levels for runt there and our lower level is around about there. No worries. And bingo, there's your runt pulse.

**Dave Jones:** And of course, you can single shot capture that every single time. So you don't need an expensive scope to get these sorts of advanced trigger capabilities. It's They're now available on the absolute bottom of the range sub $400 scopes.

**Dave Jones:** Brilliant. You just know how to need to know how to use them. And again, to find the runt pulse in the first place, it doesn't matter if you have a fast updating scope or not.

**Dave Jones:** In Well, this one's actually pretty quick. You can set your infinite persistence here, and then we can clear that, and then they'll pop up. No worries. Come on. There we go.

**Dave Jones:** Not a problem. So, you know that something's there, and then once you know something's there, you can then set up the requirements to trigger off it. And the classic Keysight 3000, you know this bad boy's going to do it.

**Dave Jones:** And we set it to pulse trigger here. Once again, we got positive or negative. We've got the greater less than greater than or window. So, you see that works just fine.

**Dave Jones:** And if I continually single shot capture that, you'll notice that really there is no synchronization between this runt pulse glitch and the actual edges of the waveform itself. So, that's why it's kind of like free running, as you'd call it.

**Dave Jones:** There you go. So, it practically corresponded with You might not see it at all, cuz it might perfectly correspond with a like a rising or falling edge there. So, you may not see it, but that's what happens when it's not actually synchronized with the actual main waveform itself.

**Dave Jones:** And that might actually technically make it harder to do trigger off. And likewise, we can do runt triggering here. We've got all the usual suspects, and we can select our high and low signal levels, and also we've got our qualifiers as well.

**Dave Jones:** They actually call them qualifier. So, a lot of scopes will call these things and the selections and setup of them, you know, something they'll use some different terminology, but they're essentially all doing all the same thing.

**Dave Jones:** And of course, we can't leave the Tektronix fan boys out. So, yeah, we've got pulse width, we've got runt, we've got all of them. So, there you go. There's the There's There's the pulse width.

**Dave Jones:** No problems whatsoever. But wait, THERE'S ONE MORE. There's one more type of triggering that might in this case be able to get it. And that Well, you just saw it update there is zone triggering.

**Dave Jones:** Now, my uh has this. My Rohde & Schwarz has a zone button. You can see it at the top there, but if I press it, it does nothing cuz it's not functional yet.

**Dave Jones:** Come on. What are you doing? Um anyway, yeah, you can actually set up Okay, so you can see I've actually set a I've drawn on the screen a zone there, and it's you see it's actually captured it twice.

**Dave Jones:** But the problem with zone triggering is that it's screen-based. So you don't know Oh, there we go. Do we get another one? You don't know where it's going to pop up on the window, so to speak, because remember it's asynchronous.

**Dave Jones:** So what zone triggering can do, if you've got a stable trigger signal like this, then if we get we can actually set a zone in there where if anything goes like within that window, then it's going to trigger on it.

**Dave Jones:** So we can actually turn that on, and we can draw I've I've done it there. I've drawn a small window there, which is outside of where it would normally trigger, and it's now it's just going to sit there and wait.

**Dave Jones:** So and wait and wait and wait. And if you get lucky, but once again we we got one. There you go. We got one. That actually happened because this actually shifted the trigger signal here and the main signal was here, but it it doesn't matter as long as it went through that window there.

**Dave Jones:** So either if Oh, we got one. We got another one. So if the glitch actually either the glitch is in there or the actual signal is in there, then it you can actually capture on that.

**Dave Jones:** And we've actually got the trigger level we can actually turn it up so that it'll never trigger on the glitch. And we can just sit there waiting and waiting to see if the glitch actually catches actually comes up in there, but you know, you could be waiting a while.

**Dave Jones:** So technically it works, but it's not really the right tool for the job. One, and I can actually draw a little zone around that, okay? And then I can say it must intersect with that, but when I actually run it, you might think that it's triggering in there, but it's not.

**Dave Jones:** It's actually doing that because I'm still on runt trigger mode. So, don't get fooled by that. If I turn that back to regular edge triggering, we're back to the point where it's not going to actually do that.

**Dave Jones:** If we do single shot capture, okay, single shot capture, we're not going to actually get the pulse. It's just going to be like random. It intersects that zone. And that's not really what you want.

**Dave Jones:** So, don't use zone trigger. Anyway, I hope you have enjoyed that look at some more advanced trigger types in modern scopes. But even you don't have to get an expensive one, even the lower end ones have these these days.

**Dave Jones:** And I hope you learned something from that. If you did, please give it a big thumbs up. If you like these sorts of like more advanced test equipment tutorials, please, yeah, thumbs it up.

**Dave Jones:** Leave it in the comments down below. And maybe we can do some more. And as always, you can comment on the EVblog forum or down below. And I had to have a new store as well, EVblog.store, link down below, where you can help keep the blog alive by buying some stuff.

**Dave Jones:** Catch you next time.
