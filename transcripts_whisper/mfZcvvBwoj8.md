---
video_id: mfZcvvBwoj8
title: EEVblog 1678 - Oscilloscope Trigger Warning
url: https://www.youtube.com/watch?v=mfZcvvBwoj8
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 17, "2": 28, "3": 43, "4": 67, "5": 84, "6": 107, "7": 125, "8": 131, "9": 143, "10": 149, "11": 159, "12": 165, "13": 183, "14": 189, "15": 199, "16": 205, "17": 215, "18": 221, "19": 229, "20": 253, "21": 276, "22": 300, "23": 318, "24": 337, "25": 355, "26": 374, "27": 391, "28": 412, "29": 424, "30": 442, "31": 458, "32": 477, "33": 497, "34": 515, "35": 535, "36": 554, "37": 570, "38": 586, "39": 603, "40": 619, "41": 637, "42": 653, "43": 667, "44": 689, "45": 710, "46": 735, "47": 757, "48": 773, "49": 793, "50": 823, "51": 846, "52": 870, "53": 896, "54": 911, "55": 927, "56": 943, "57": 971, "58": 985, "59": 1007, "60": 1032, "61": 1054, "62": 1071, "63": 1092, "64": 1112, "65": 1129, "66": 1148, "67": 1164, "68": 1179, "69": 1201, "70": 1218, "71": 1231, "72": 1244, "73": 1261}
---

**Dave Jones:** Hi, I wanted to show you a problem with modern digital oscilloscopes where you could potentially come agutter, just like I did recently, and even I was fooled by this. Even though I knew about it, I simply forgot to take it into account when I was doing some measurements recently.

**Dave Jones:** So what I've got here is just a basic DC signal, 10 volts coming from my power supply. I'm 2 volts up per division here, and I can switch this on or off like this. That's it, right? And I've got a trigger point just right in the middle there.

**Dave Jones:** There's nothing fancy with the trigger couplings just set to DC here. There's no noise reject or hold off or anything, right? So it's a pretty simple thing. In my case, I just want basic edge triggering. When it goes from 0 to 10 volts here, positive edge, I want it to trigger, and that's it.

**Dave Jones:** So that's pretty easy, right? We're at 100 milliseconds per division here. I press my single shot button like that, and I turn on my power supply. And Bob's your uncle, right? I can do this all day long. Press single shot, and then, boom, I trigger every single time.

**Dave Jones:** Look at that. Easy. But what happens if I want to go to a slower time base? Let's say 1 second per division here, okay? It's not radically slow, but if I press the single button like this, and I set my output, you can see at 10 volts, it hasn't triggered.

**Dave Jones:** What? What? Why? Why has it not triggered? We're in single shot mode, exactly the same as before, and I press the... I went from 0 to 10 volts, you saw it, and it didn't trigger. What's going on? Well, the trick here is that the oscilloscope had not armed itself yet, because modern digital scopes, this one's no difference, the same as every other scope.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data.

**Dave Jones:** If our trigger point is in the middle here, then we have what's called 50% pre-trigger data and 50% post-trigger data. Let me try that again. Okay, so we start it after five seconds. Okay at one millisecond per division It should now so I will now set the output.

**Dave Jones:** I'll go like that and it does Do it? But what so it did do it as expected, but I hadn't actually shown the armed indicator yet I'll put you out of your misery. I'll show you where it is on the keysight scope. We'll push single here and watch here

**Dave Jones:** It says triggered Apostrophe D. Okay, and the armed indicator Wait for it. Wait for it. Wait for it. It turns to triggered with a question mark after it That is the armed indicator. But if you go back and replay that clip I just showed you I was able to trigger it before

**Dave Jones:** That armed indicator question mark turned up and I'll put up the manual here for this Triggered armed indicator feature and you can see that it says triggered without the question mark is when the Pre-fill buffer is being filled so that pre-trigger Buffer is being filled and it's not able to actually trigger but you saw it in the previous clip

**Dave Jones:** We were able to trigger it before that question mark turned up after that five second period as we got on the display But the question mark hadn't showed up yet And the manual says when the question mark appears that is when the pre-trigger or pre-filled buffer is done

**Dave Jones:** And it's ready to be triggered so like what the hell's going on there and like What they couldn't be bothered to put like the word armed there or something or ready or something like that? And make it like green and then red when it's been pre-filled or something like that

**Dave Jones:** No, look at this piddly little question mark here And if you don't know how to use your scope and you're not aware that your scope is not You know armed and ready to trigger then you could in my case I was manually triggering things expecting it to capture it and I was getting no capture whatsoever

**Dave Jones:** And you'll notice that that triggered without the question mark has two actual meanings It can mean that your signal is actually triggered like in this particular case like we can actually trigger it like that And you'll see it turned from the question mark back to that and our waveform has popped up and it's triggered

**Dave Jones:** So it has that two meanings of both Being triggered and also sitting there unarmed waiting for that pre-filled buffer It's like like the same thing indicates both like what why so it actually takes Ten seconds in this particular case at one second per division.

**Dave Jones:** It'll be longer, you know Correspondingly longer at longer time basis, but five seconds It's already armed, but it hasn't show it and boom it popped up at the ten second mark there that question mark But it's totally non-obvious that there's this trigger dead time in there while your scope is

**Dave Jones:** Prefilling that buffer and as I said, it's going to be longer if you actually move this over So let's try that so I'll move this all the way over here like this and we expect it to now take nine Seconds to pre-fill that buffer there.

**Dave Jones:** Let's give that a go. Okay, here we go So it'll take nine seconds to pre-fill that but for some reason this key site in key site takes Twice that time period in this case. Yeah, it hasn't gone yet. There's no question mark. It should take 18 seconds

**Dave Jones:** Well, no, there it is. It took 15. Why did it take 15 when there was an extra four there? It's not linear Yeah, okay. It might have some extra buffer outside this window in that direction perhaps, but why does it take twice as long?

**Dave Jones:** It's crazy. So I'll do that again and we've still got our trigger point right out over here I'll turn my output on after five seconds. No, it's not triggering No, eight nine seconds nine seconds I want it was able to start triggering and sure enough it did it was like you can see it was actually capturing that

**Dave Jones:** Data as I was turning them off and on before that but it wouldn't trigger Until like right over here until it had armed itself. So you've got to really be aware It's slower time basis this becomes a big problem It's it's not a problem at faster time basis like we saw at the start of the video because well

**Dave Jones:** It's filling that buffer practically instantly before you can actually move your arm over and trigger manually trigger something So let's see if the new mega zoom 5 key site ASIC makes any difference here So I've got the new key site scope here and let's take a look at the indicators at the top

**Dave Jones:** So let's press the single button and take a look here Triggered with the question mark straight away, but if I Do it like I just cycled the thing trust me I think you might have heard the relay there and boom it captured it like this, but

**Dave Jones:** Not always so it seems to have this weird and I guess good ability to Instantly go into like as if it's like continually sampling in the background already We fill in that buffer which would be fantastic But if we go into single mode like that, yeah

**Dave Jones:** It's already showing it's already armed But I found it doesn't always do that and I haven't figured out under what circumstances it doesn't I haven't been I'll reproduce it on Camera yet. Okay. Let's try that again. I've left it stopped for a period of time and

**Dave Jones:** Bump no question mark again, but I swear I was able to get it to not show the question mark So let's see if we're actually able to Capture something I'll start the timer there and I'll trigger it right now. I triggered it once and

**Dave Jones:** Let's see. Let's wait and see if it's actually able to ah, ah, you'll notice. Oh look no question mark I got it I have no idea how I got it to be no question mark But I triggered it and it's as you can see we've more than waited for the time period

**Dave Jones:** Well, it's now armed and you can see that it is essentially now working the same way So now if I trigger it it'll do the business, right? So we shouldn't wait time for it to show up and boom. There's our yep. It showed up right there

**Dave Jones:** So even with this new generation scope the new mega zoom 5asic it does seem to work a bit different But also like more even more inconsistently Lee So I haven't figured out that at all and I won't go into the details here I just want to point out that you know your scope can do like weird things and they have

**Dave Jones:** I haven't put like a big armed in green or something ready Something like that. Give me a nice big indicator or better yet. Let me show you another scope that does it better? Okay, so what I've done is I've completely Repowered this scope and I haven't touched it yet

**Dave Jones:** So it's repel with the default settings and let's try this again So what I'll do is I'll trigger it straight away We'll look at the indicator and then I'll trigger my power supply Like well before the five seconds and see if it actually triggers and see what happens here

**Dave Jones:** Go and I'll trigger that now. Okay, so I just triggered My power supply and you notice that popped up with the question mark straight away But then when I triggered it it it disappeared so it so it has triggered Okay, well apparently right so it went from the armed mode

**Dave Jones:** With the question mark there, and I triggered it with the power supply and it now look it just popped back it popped back Into armed mode and it hasn't displayed our waveform. What the heck? What's going on? Is that a bug or is that a pebcac?

**Dave Jones:** Am I doing something wrong, but it? Said the question mark armed and it didn't trigger so but now it probably will right so let's do it right now No, it didn't what the heck What no it did, but you see it didn't go from like it did on the 3000 from trig?

**Dave Jones:** question mark to Trigged like actual triggered with that jewel terminology. Oh god. It's so confusing But yeah, that's weird And you'll notice that it didn't pop up on the screen straight away like it did on the 3000 which is a handy thing It you had to wait for that five seconds after you actually

**Dave Jones:** Triggered the thing before the waveform would show up and other sky and some other scopes operate like this as well And that's kind of annoying so it's good that the 3000 does that with the mega zoom for a sick? But the mega zoom five on this scope it doesn't do it you have to wait the extra five seconds

**Dave Jones:** But there's something weird going on here, and it's totally non-obvious and oh, I don't know ah it's bizarre So yeah, this can just get like frustratingly weird especially if there's not like a buggy or inconsistent operation Which um there seems to be and I've also noticed that on the 3000 as well where I?

**Dave Jones:** Swear it took 20 seconds at one second per division to arm at one time, but I can't reproduce that We'll go single shot capture here, and we all press my output and Ta-da, it's not triggering Why is it not triggering ah I thought I'd solved it

**Dave Jones:** But it looks like I hadn't Damn, okay Let's look at this new siglent SDS 1204 X HD Series everything's exactly the same as before we're at one second per division here a trigger point in the middle everything's you know Normal trigger nothing fancy whatsoever, so let's stop that okay, and we'll put our scope in

**Dave Jones:** Single shot mode like this and See if you can tell if this one's ready or not You pick it look at this bad boy do this right next to the trigger level control There's an LED there that actually says ready So let's try that again run stop okay, and we'll go single and you can count it yourself

**Dave Jones:** one two three four five Boom ready in the five seconds of the what we expect with the five divisions on the screen with our Trigger point in the center like this so that's how you implement a good trigger system And make it obvious to the user either on the screen or in this particular case an LED on the front panel, right?

**Dave Jones:** So we'll do single and I'll actually trigger it now within the first five seconds couple of times And it's not going to do it right because it wasn't ready now. It's ready I can actually let's do wait for the ten seconds to make sure it didn't actually capture anything nope

**Dave Jones:** and now I will do it and Boom the ready's gone away because it's triggered, and we just have to wait that yep the extra five seconds and Bingo we've got it on the screen so that is a nice implementation use the Schwartz Luke, okay?

**Dave Jones:** We've got the new rodent Schwartz mx-04 series Bobby dazzler. Let's see what we get here, okay? Everything's exactly the same as before one second per second No division yada yada what we're looking for is trigger up here somewhere in here because there's no real

**Dave Jones:** indicator over here of any armed or anything, so let's press single and go and I'll press that couple of times and It's waiting waiting you see it switch from pre trig to waiting at that five second mark so Obviously once again this only takes the five seconds to pre fill that buffer and now and you can see that it didn't trigger

**Dave Jones:** And now I will press it on and it'll trigger it shows triggered and when we wait that five second period and right about now There's our waveform. No worries once again. It would have been nice to have that like in a bigger like big

**Dave Jones:** You know red green type indicator rather than just showing like pre trig like that like we press single and It's now pre trig okay at least it's telling us But you know red maybe and then change it to green I don't know have a bigger font or something like that just to make it obvious that your scope is armed and ready to trigger

**Dave Jones:** And how about this cute and affordable Rigol DHO 800 series battery-powered just because I can Let's give this a go shall we once again all the same parameters that we had before our trigger sort of like information like mode Is kind of up here, but our trigger info trigger settings are over here, but our modes over here, so let's go single and

**Dave Jones:** boom like that - it says run run run rabbit run and Now it's waiting so it took that five seconds. They're waiting for that pre trigger period so run What does that mean okay? Yes sampling is running, but once again? It's not telling you that it's actually like armed

**Dave Jones:** and ready to go so like just the lack of Terminology and just the lack of obviousness that it's you know trigger Armed is like a good word ready is a good word something like that So that's why I like that ready led on the front of the sealer

**Dave Jones:** So let's test that again, and I'll psych it a couple of times Cycle cycle cycle cycle in the first five seconds, and it shouldn't have triggered at all No, we've waited our Ten seconds no, it's not going to do it now. It says wait, so we're waiting and I will now trigger and oh

**Dave Jones:** Boom we got that. Oh, I've gone off scale there dumbass me must have this in that times ten mode Oops, but I like how that showed up instantly whereas the other scopes didn't do that they set their Blank for like five seconds before or if you've got to set to a longer time base if you got to set to you know

**Dave Jones:** a minute per division Then you're gonna have to wait five minutes before you even see your waveform I like how that displayed that instantly thumbs up it knows that you've triggered, so why not? Show that data straight away, so that just makes sense

**Dave Jones:** I don't understand why the other scopes don't do that, but yeah, that's nice, so there you go I hope you liked that video and found it useful and interesting and something you may not have thought about before is that a Pre-trigger or pre-arm time for your scope, and it's slow time basis that can really matter especially like

**Dave Jones:** We're only using one second per division if you use like how far can we go on here? 50 seconds per division, but other scopes can go way slower than that and you could wait forever And we saw that some scopes have a nice

**Dave Jones:** Indicator like a lead front panel indicator that says ready. It's sort of you know it tells you exactly that you're ready to trigger Other scopes like this key site have this weird triggered and then the question mark thing some scopes will sit there and wait for that

**Dave Jones:** all that extra Post trigger time period five seconds in this case before it'll display your waveforms others like the Rygo will display it Straight away like that and some scopes like this key site can wait longer than the time period That you might think given the time base and the number of divisions here five seconds you could wait double that

**Dave Jones:** Or in one case, I'm sure in a previous video or edited in here That I actually waited 20 seconds at one second per division before it did that I'm sure that happened at one point So yes scopes is kind of like all over the shop in terms of this ability to

**Dave Jones:** Tell you that they're ready to arm and if you're not aware of this at slow time basis Then you could be doing what I was doing and true. Why isn't my scope triggering? I'm you know It's all set up correctly and you can

**Dave Jones:** Go down that rabbit hole of wasting a whole lot of time thinking that all your trigger Settings are all wrong and your modes wrong and everything else you might have hold off or something else weird Happening when that's not the case at all

**Dave Jones:** It's simply the scope wasn't armed and ready because of that pre trigger pre fill buffer time period Anyway, you found that video interesting Give it a big thumbs up as always discussed down below and visit the EUVblog.scoot store for my new merch Look at this it's even got an orange backlight.

**Dave Jones:** Oh Bobby dazzler catch you next time You
