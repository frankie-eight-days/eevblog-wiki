---
video_id: 1YK_GlnUlI8
title: EEVblog 1583 - Advanced Oscilloscope Triggering: Glitch/Pulse/Runt/Interval
url: https://www.youtube.com/watch?v=1YK_GlnUlI8
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 28, "3": 46, "4": 62, "5": 73, "6": 86, "7": 100, "8": 113, "9": 127, "10": 142, "11": 157, "12": 177, "13": 195, "14": 211, "15": 225, "16": 242, "17": 253, "18": 265, "19": 278, "20": 294, "21": 312, "22": 330, "23": 342, "24": 355, "25": 372, "26": 386, "27": 399, "28": 412, "29": 424, "30": 434, "31": 449, "32": 461, "33": 474, "34": 488, "35": 502, "36": 524, "37": 540, "38": 553, "39": 569, "40": 586, "41": 599, "42": 612, "43": 623, "44": 636, "45": 648, "46": 661, "47": 675, "48": 689, "49": 705, "50": 720, "51": 734, "52": 747, "53": 761, "54": 771, "55": 784, "56": 799, "57": 814, "58": 830, "59": 850, "60": 863, "61": 878, "62": 889, "63": 902, "64": 916, "65": 932, "66": 947, "67": 960, "68": 973, "69": 987, "70": 1000, "71": 1013, "72": 1028, "73": 1040, "74": 1053, "75": 1065, "76": 1082, "77": 1094, "78": 1107, "79": 1121, "80": 1134, "81": 1149, "82": 1161, "83": 1176, "84": 1188, "85": 1202, "86": 1217, "87": 1231, "88": 1245, "89": 1256, "90": 1270, "91": 1282, "92": 1295, "93": 1307, "94": 1319, "95": 1331}
---

**Dave Jones:** Hi, I was playing around with glitches in signals for another thing which I might see a future video on, but I thought it'd be interesting to actually show you the glitch capture capabilities or pulse capture capabilities of modern scopes and

**Dave Jones:** actually compare them and see how it useful they are. Oh, you might have seen one just pop up there. What There There it is again. What I've got is I'm just feeding in a pseudo random 1 megabit per

**Dave Jones:** second signal a square wave signal into this and it's got a random glitch both positive like going from the negative going up like this and also from the positive going down like this at about a volt and a half or something like that and it's

**Dave Jones:** doing those random glitches about every 15 milliseconds and unfortunately glitches are something that you might actually encounter sooner or later if Murphy's going to bite you on the backside. Now, sometimes you'll just see like a glitch like something like just

**Dave Jones:** pop up on the screen or a briefly. I think I saw it there very briefly actually pop up and you might think oh, what is that? Well, there it is again. What is that and how do I trigger off

**Dave Jones:** that? Well, of course one of the easiest ways to do it of course with any scope you don't need any fancy glitch capturing or pulse trigger capabilities. If you just want to actually see if something's there of course, you can

**Dave Jones:** just use infinite persistence mode. If you ever see like some weirdness happening on your screen not only turn your intensity up for your waveform cuz you'll see it better, but also turn on infinite persistence display. So, we can

**Dave Jones:** actually on this Rohde & Schwarz MXO 4 here, we can go into settings. It'd be nice if they actually had this up the top or a button, but we can turn on infinite persistence here and let me actually reset that, okay? I'll clear

**Dave Jones:** that after a a of seconds. Boom, we got our first one. Boom, we got another one. Uh boom, there's one over here. Uh come on. Come on. Capture you, bastard. Come on. Oh, we haven't got one for a while yet.

**Dave Jones:** Hang on. They'll They'll come in bursts. No pun intended. Mirror a week. Anyway, you can see how that we're actually capturing these glitches there because uh this just builds up. This display doesn't clear itself. So, it builds up

**Dave Jones:** over time and you can get a picture of these actual uh run pulses. Now, how often can we expect to actually see these things? Well, we can kind of sort of calculate this. So, what we know is our time base here is 1 microsecond per

**Dave Jones:** division. Okay, we've got 10 divisions across the screen. That means we have an effective wind display capture window here of 10 microseconds wide. Now, as I said before that these pulses are appearing every 15 milliseconds. So, that's quite infrequent when you've only

**Dave Jones:** got a like a window like a sample window that's 10 microseconds wide. So, if you divide 15 milliseconds by 10 microseconds, get 1,500. So, if we reset our persistence here, we can only expect to actually capture this glitch like

**Dave Jones:** that every 1,500 captures of this entire display. Now, of course, your uh scope's going to have a waveform updates per second. You know, how many waveform updates per second which changes based on the current time base and the current memory depth. And

**Dave Jones:** the good thing about the Rohde & Schwarz MXO is we can actually see this. We can go into speed down here and we can actually measure and we can see the waveform update rate here, which is about you know, let's call it 720

**Dave Jones:** waveform updates per second. So, if our scope is capturing one of these 10 microsecond windows at a rate of 730 odd per second, well, we can expect it on average to capture one of those glitches about every 2 seconds or so. And if we

**Dave Jones:** clear it if we wait a couple of seconds, boom, we we got one. Wait another couple of seconds, of course it's going to be more like it's going to be random cuz there's some blind time in there. Boom, about

**Dave Jones:** every 2 seconds. So, you can actually, you know, you can run the numbers on this if you know your acquisitions per second or your waveform update speed. In most scopes you can actually get that from the trigger output. You can measure

**Dave Jones:** it on an external frequency counter. This is the only scope I've got that actually tells me actually the scope actually tells me itself on screen how many waveform updates per second. But, that's pretty cool, huh? We can actually

**Dave Jones:** estimate that. So, I've got a Dave CAD here to illustrate that. You can see that basically our pulses are happening every 15 milliseconds here, but basically because we're we're triggering wherever because there's, you know, it's a very fast trigger rate. But, we're

**Dave Jones:** only capturing this screen here represents only a 10 microsecond capture window as it's called. And really your odds of actually capturing one of those glitches, which are essentially like just moving randomly even though they are a fixed 15 milliseconds apart, as

**Dave Jones:** far as the trigger system goes, they're just moving randomly across here. So, the odds of finding one there are dependent upon your waveform update rate and how lucky you are basically and you know, averages, statistics. So, that's why if I clear that and we're at 700,

**Dave Jones:** you know, 30 or waveform updates per second, we expect to capture one every couple of seconds. Cool, huh? But, the next question is how do we actually trigger off one of these? That's where it gets a bit more

**Dave Jones:** interesting and where your modern scopes have features to actually do this. And the other thing to remember is this has nothing to do with trigger level, right? If I set my trigger level right in the middle there, okay? We will still capture those

**Dave Jones:** because it's got nothing to do with uh triggering. It's just because as I said, they're essentially just randomly wandering in the trigger uh sequence. So, we don't even have to set our trigger level. You can see that we're never triggering off actually one

**Dave Jones:** of these things. So, trigger has nothing to do with it essentially in this particular case, although your mileage may vary. So, modern scopes like this Rohde & Schwarz MSO 4, they will actually have glitch capture capability. So, let's actually turn off Okay, so we

**Dave Jones:** know our glitch is happening there, okay? We've captured it with our persistence view here. So, we know the you know, we can go in there with our cursors or just eyeball measure uh that. So, we know the pulse width that is

**Dave Jones:** happening here. We know the signal level roughly. So, you know, one division up would be a nice trigger level for that. One division down would be a nice trigger level uh for that, for example. So, if we know the pulse width and we

**Dave Jones:** know the trigger level, we can use glitch or pulse uh capture. It depends on the manufacturer, they might call it something uh different. So, let's turn off the uh infinite persistence display there and we're back to here. And as you

**Dave Jones:** can see, like we will very rarely go Well, we got one over there. So, if we want to trigger off that, we go up to trigger here and then we can choose the trigger type. And this actually has

**Dave Jones:** glitch capture here. Now, of course, you can do uh runt and widths and they're different uh styles of trigger, but glitch is essentially a pulse uh width type thing. Now, let's actually set this up. And you can see we're

**Dave Jones:** actually There's something in the middle here as well. So, there's something going on. We're already triggering off something there. Right, so what we want to do is actually set our trigger level here, which you can to and set here or

**Dave Jones:** just use your regular trigger level. Let's try and capture on one of those bottom ones. So, about a division up. We can either choose shorter or longer. We want the shorter option because it's a short pulse. And then we can set the

**Dave Jones:** pulse width. All right, so we want to set that pulse width just above where we think it is there. Okay? Let's Let's just say 70 nanoseconds or thereabouts. And we're triggering off that thing perfectly. Okay? Oh, I forgot to mention

**Dave Jones:** we're actually in normal uh trigger mode here. Okay? And we can actually do that same thing for the positive glitch up here. Okay? We can set our trigger level up to here. And boom, we're getting that. But we probably want to set that

**Dave Jones:** to negative going now. And bingo, we are now triggering on that actual glitch there. Neat, huh? Now, because we're actually triggering off this glitch here, we're not just randomly wandering through this window back and forth like we were before. Essentially, because

**Dave Jones:** we're triggering on, we expect more than a couple of times waveform updates per second. And you can see we're actually getting that. We can see here it's actually 30s maybe waveform updates per second. So, now we're actually capturing that. Cuz

**Dave Jones:** once we've captured it, it'll rearm and then we'll capture it again. We will capture that more frequently than when it was just randomly wandering through here. So, we're getting a That's why we're getting a faster waveform updates per second there. Now,

**Dave Jones:** this is actually glitch capture because it's where essentially doing What that means is we're doing pulse capture. That's why on a lot of scopes it'll be called pulse capture because we're specifying the actual you know, the pulse width range in here either shorter

**Dave Jones:** either uh lower or more than a certain value. But because it's based on signal level as well, we can actually use runt capture as well to do this. So, this basically instead of working on a horizontal, it works on a vertical

**Dave Jones:** basis. I've been calling this a glitch, but what this is is actually in this particular scenario is actually a classic runt pulse. So, what a runt pulse is is that you can see that the normal signal level like a you know,

**Dave Jones:** it's a TTL type signal level 5 volts, 3.3 or whatever, right? Digital signal, but a runt pulse means that it only goes up a certain amount of way and doesn't reach a certain it doesn't reach the upper digital threshold because if you

**Dave Jones:** know about digital logic, they have upper and lower thresholds before they're actually recognized as a logic one or a logic zero. So, a runt pulse actually doesn't go all the way up to the second threshold. So, you can

**Dave Jones:** actually do and modern scopes actually have also runt triggering. So, that is one of the options there. So, we can choose runt triggering like this and then we've got an upper level like this. So, we set our upper level like that.

**Dave Jones:** So, it might be up here for example and our lower level. So, it was right down at the lower level down there. So, it transitions through one level, but it doesn't transition through the other level. So, you can see those two levels.

**Dave Jones:** It transitions through one, but doesn't go through the other and that's the definition of a runt pulse. And then we can do range here. We can do just a longer, shorter, within, outside or we can do this automatic find level.

**Dave Jones:** Let's see if we can do this. Okay? Boom. There it is. It automatically found it. Very cool. And you'll see that if I choose the upper limit there and I go below the runt value right in there, it's not

**Dave Jones:** going to actually capture it. It's stopped capturing. It's actually frozen. So, if I actually clear that there, you'll find that we won't actually capture that. It's only when we go above that level, boom, that we start to capture that. So, but either runt or

**Dave Jones:** glitch capture in this case works. And I know you're thinking, "Dave, I can capture this using the fancy pantsy history mode of this MXO 4 scope." Well, yeah, not really. It's going to be based on luck. Um and that sliding window and

**Dave Jones:** the odds of actually capturing it like we saw before. So, if I stop this, okay? Yeah, we can go into history mode and over here, we've got 16,000 acquisitions here and you can go through them one by one by one by one until you

**Dave Jones:** try in there of all these waveform captures that it got, but you're going to be waiting there a long time. You're going to look through it like statistically, we've only looked through like 300 so far. We're going to have to look through a

**Dave Jones:** lot more than that before on average we're going to actually find one. We're going to go through pretty quick, so you could easily visually miss one. My mark one eyeball might not actually see it, but you know, you might eventually get

**Dave Jones:** lucky and see one if you're if you're patient enough, but based on the math we did before, you can only expect to capture it every like 1,500 waveform captures on average, so you could be there for a while. Of

**Dave Jones:** course, you can set it to auto scroll through, of course, at a certain speed and you can just try and not to blink and good luck. But those two methods aren't the only ones you can use on this

**Dave Jones:** Rohde & Schwarz scope. It's got another very cool mode, trigger mode, that I'll show you here and you can see that we are actually capturing, but it's a slower update right there. There you go. But what we're actually using this time

**Dave Jones:** is what's called interval triggering here. So, it's one of the very comprehensive, you know, types of different triggering systems. Not every scope will actually have this and we've got interval trigger. We can set it up shorter here or we can set it longer

**Dave Jones:** within or outside. So, it's extremely powerful and we've set the trigger level to there, right? And then I've got the interval width set to 80 nanoseconds there. And of course it's going to trigger on anything less than 80

**Dave Jones:** nanoseconds. Very It's another way to actually capture it. Check this out. This is very cool. It's got this fine level here. So it's got this automatic level. Watch this. Fine level. And boom! Look at that. We've captured on

**Dave Jones:** this middle one here, which is yet another glitch. In here like this message is booting. Oh, well, touchy-feely screens. So it's automatically found this glitch in here. This is absolutely fantastic. So as far as I know, this is the only scope I've got that it

**Dave Jones:** will actually do that automatic detection capability and stuff like that. That's It's very cool. So that's very I think that's quite specific to this scope. If you know of another one that I can actually do that, leave in the comments down below, but I

**Dave Jones:** just think that's fantastic. Okay, let's try another excellent modern oscilloscope here, the Siglent SDS 2354X. I don't know that Well, I was looking at it before and it was taking a while, but yeah, it's a I think it's a slower waveform update rate.

**Dave Jones:** Might help if I turn my intensity up a bit. We might see it a bit better, but yeah, not quite. Oh yeah, yeah, got one. We got one. So if we go into our trigger mode here, we go to where the edge type,

**Dave Jones:** but we've got all these different types as well. You notice that it doesn't have They don't call it a glitch like that, but we can use pulse triggering here. It's got runt triggering and drop out and all sorts of things, but we should

**Dave Jones:** be able to do the same thing with pulse triggering. And boom, we've got it here. Now this one does it like explains it a little bit differently here, but we can choose the different limit ranges here. We can choose less than or equal to a

**Dave Jones:** value. We can choose greater than or equal to a value. We can choose within two particular values or we can choose outside two particular values here. But if we choose inside a particular value, so it's within 79 nanoseconds and 2

**Dave Jones:** nanoseconds, boom, there it is there. No worries. And we can also use the runt trigger thing here. Once again, we can choose the different styles there and we've got the positive edge, but I'm only at 28 nanoseconds at the moment. So

**Dave Jones:** if it tran- if it transitions through this signal level here and not this signal level here, we should be able to pick it up. So if I increase that, but that's also dependent upon the time as well. Wait, there it is. So once we got

**Dave Jones:** greater than the pulse width of that little runt pulse there, which we can actually measure use this as a tool to measure it without using our cursors. We see once we hit about 55, once this baby hits 55 miles an hour, you're going to

**Dave Jones:** see some serious runt pulses. And just to show you that you don't need a big fancy expensive oscilloscope to do it. Bottom of the range Rigol DHO800 here, no worries whatsoever. There is our glitch. We're using pulse triggering.

**Dave Jones:** It's got all the different fancy types. We've got We're using pulse triggering at the moment, but it's got runt, it's got timeout, it's got infed, and it's got duration. And more things than you can poke a stick at. No worries. And if you choose pulse,

**Dave Jones:** you've got the different types here. I've got it set to 80 nanoseconds here. You just set the level, Bob's your uncle. So we can set our two levels for runt there and our lower level is around about there. No worries. And bingo,

**Dave Jones:** there's your runt pulse. And of course, you can single shot capture that every single time. So you don't need an expensive scope to get these sorts of advanced trigger capabilities. It's They're now available on the absolute bottom of the range sub $400 scopes.

**Dave Jones:** Brilliant. You just know how to need to know how to use them. And again, to find the runt pulse in the first place, it doesn't matter if you have a fast updating scope or not. In Well, this one's actually pretty quick. You can set

**Dave Jones:** your infinite persistence here, and then we can clear that, and then they'll pop up. No worries. Come on. There we go. Not a problem. So, you know that something's there, and then once you know something's there, you can then set

**Dave Jones:** up the requirements to trigger off it. And the classic Keysight 3000, you know this bad boy's going to do it. And we set it to pulse trigger here. Once again, we got positive or negative. We've got the greater less than greater

**Dave Jones:** than or window. So, you see that works just fine. And if I continually single shot capture that, you'll notice that really there is no synchronization between this runt pulse glitch and the actual edges of the waveform itself. So, that's why

**Dave Jones:** it's kind of like free running, as you'd call it. There you go. So, it practically corresponded with You might not see it at all, cuz it might perfectly correspond with a like a rising or falling edge there. So, you

**Dave Jones:** may not see it, but that's what happens when it's not actually synchronized with the actual main waveform itself. And that might actually technically make it harder to do trigger off. And likewise, we can do runt triggering here. We've

**Dave Jones:** got all the usual suspects, and we can select our high and low signal levels, and also we've got our qualifiers as well. They actually call them qualifier. So, a lot of scopes will call these things and the selections and setup of

**Dave Jones:** them, you know, something they'll use some different terminology, but they're essentially all doing all the same thing. And of course, we can't leave the Tektronix fan boys out. So, yeah, we've got pulse width, we've got runt, we've got all of them. So, there you go.

**Dave Jones:** There's the There's There's the pulse width. No problems whatsoever. But wait, THERE'S ONE MORE. There's one more type of triggering that might in this case be able to get it. And that Well, you just saw it update there is zone triggering.

**Dave Jones:** Now, my uh has this. My Rohde & Schwarz has a zone button. You can see it at the top there, but if I press it, it does nothing cuz it's not functional yet. Come on. What are you doing? Um anyway,

**Dave Jones:** yeah, you can actually set up Okay, so you can see I've actually set a I've drawn on the screen a zone there, and it's you see it's actually captured it twice. But the problem with zone triggering is that it's screen-based. So

**Dave Jones:** you don't know Oh, there we go. Do we get another one? You don't know where it's going to pop up on the window, so to speak, because remember it's asynchronous. So what zone triggering can do, if you've got a stable trigger

**Dave Jones:** signal like this, then if we get we can actually set a zone in there where if anything goes like within that window, then it's going to trigger on it. So we can actually turn that on, and we can

**Dave Jones:** draw I've I've done it there. I've drawn a small window there, which is outside of where it would normally trigger, and it's now it's just going to sit there and wait. So and wait and wait and wait. And if you get lucky, but once again

**Dave Jones:** we we got one. There you go. We got one. That actually happened because this actually shifted the trigger signal here and the main signal was here, but it it doesn't matter as long as it went through that window there. So either if

**Dave Jones:** Oh, we got one. We got another one. So if the glitch actually either the glitch is in there or the actual signal is in there, then it you can actually capture on that. And we've actually got the trigger level we can actually turn

**Dave Jones:** it up so that it'll never trigger on the glitch. And we can just sit there waiting and waiting to see if the glitch actually catches actually comes up in there, but you know, you could be waiting a while. So

**Dave Jones:** technically it works, but it's not really the right tool for the job. One, and I can actually draw a little zone around that, okay? And then I can say it must intersect with that, but when I actually run it, you might think that

**Dave Jones:** it's triggering in there, but it's not. It's actually doing that because I'm still on runt trigger mode. So, don't get fooled by that. If I turn that back to regular edge triggering, we're back to the point where it's not going to

**Dave Jones:** actually do that. If we do single shot capture, okay, single shot capture, we're not going to actually get the pulse. It's just going to be like random. It intersects that zone. And that's not really what you want. So,

**Dave Jones:** don't use zone trigger. Anyway, I hope you have enjoyed that look at some more advanced trigger types in modern scopes. But even you don't have to get an expensive one, even the lower end ones have these these days. And I hope you

**Dave Jones:** learned something from that. If you did, please give it a big thumbs up. If you like these sorts of like more advanced test equipment tutorials, please, yeah, thumbs it up. Leave it in the comments down below. And maybe we can do some

**Dave Jones:** more. And as always, you can comment on the EVblog forum or down below. And I had to have a new store as well, EVblog.store, link down below, where you can help keep the blog alive by buying some stuff.

**Dave Jones:** Catch you next time.
