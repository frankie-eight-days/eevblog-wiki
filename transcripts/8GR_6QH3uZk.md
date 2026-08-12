---
video_id: 8GR_6QH3uZk
title: Tektronix 2225 Analog Oscilloscope - EEVblog #196
url: https://www.youtube.com/watch?v=8GR_6QH3uZk
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 35, "3": 48, "4": 65, "5": 80, "6": 92, "7": 106, "8": 118, "9": 128, "10": 144, "11": 157, "12": 171, "13": 186, "14": 198, "15": 214, "16": 227, "17": 241, "18": 257, "19": 270, "20": 283, "21": 297, "22": 311, "23": 328, "24": 344, "25": 361, "26": 373, "27": 388, "28": 403, "29": 417, "30": 434, "31": 450, "32": 462, "33": 481, "34": 495, "35": 512, "36": 523, "37": 537, "38": 552, "39": 565, "40": 578, "41": 594, "42": 610, "43": 622, "44": 635, "45": 647, "46": 656, "47": 675, "48": 685, "49": 699, "50": 714, "51": 732, "52": 746, "53": 761, "54": 777, "55": 796, "56": 815, "57": 828, "58": 845, "59": 861, "60": 875, "61": 889, "62": 903, "63": 917, "64": 932, "65": 952, "66": 966, "67": 983, "68": 999, "69": 1018, "70": 1037, "71": 1053, "72": 1068, "73": 1085, "74": 1099, "75": 1113, "76": 1127, "77": 1141, "78": 1153, "79": 1170, "80": 1185, "81": 1198, "82": 1210, "83": 1223, "84": 1238, "85": 1249, "86": 1264, "87": 1275, "88": 1290, "89": 1304, "90": 1315, "91": 1330, "92": 1342, "93": 1356, "94": 1370, "95": 1387, "96": 1400, "97": 1415, "98": 1429, "99": 1448, "100": 1465, "101": 1482, "102": 1507, "103": 1522, "104": 1538, "105": 1554, "106": 1568, "107": 1584, "108": 1599, "109": 1612, "110": 1627, "111": 1640, "112": 1655, "113": 1670, "114": 1683, "115": 1699, "116": 1712, "117": 1732, "118": 1749, "119": 1764, "120": 1779, "121": 1791, "122": 1806, "123": 1822, "124": 1835, "125": 1854, "126": 1865, "127": 1880, "128": 1896, "129": 1909, "130": 1925, "131": 1939, "132": 1953}
---

**Dave Jones:** Hi, welcome to the AAVlog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, look what I just scored, a Tektronix 2225 50 MHz dual channel analog oscilloscope. Beauty. Always wanted one

**Dave Jones:** of these because it is one of only three oscilloscopes, I think it is, that I know of on the market that has a 500 microvolt per division vertical scale. And that's great for measuring real low noise stuff, the

**Dave Jones:** output of power supplies and things like that. So, I thought it'd be just a real nice scope to have. I always got a always wanted one. And I was lucky enough to pick one up here local. These are quite rare to find these in

**Dave Jones:** Australia here, but in in the US they're fairly common. It's a really nice 50 MHz late '80s kind of vintage Tektronix scope. And I've mentioned it before, you should have an analog scope in your lab. You can get them for 50 or 100 bucks,

**Dave Jones:** under 100 bucks. 50 MHz dual channel like this one. Very handy analog scope to have. You know, if you're just relying on your Rigol, you know, digital scope, it's not too bad, but they're noisy and you know, they're just

**Dave Jones:** not as real time as a good analog scope. Highly recommend you get one. So, I thought we'd just I'll do a teardown. Everyone wants to see a teardown, of course, vintage teardown. Do that as a separate video cuz people

**Dave Jones:** like the separate teardown videos. And but for this one, I will just basically power it up. Did I get a dud or not? I don't know. We'll power it up, check it out, check out all the basic functions. So, this

**Dave Jones:** will be a reasonably basic guide on how to test a second hand scope like this. If you pick one up on eBay cheaply, I got this one for 100 bucks Australian, which is pretty darn good value. you can

**Dave Jones:** pay more than this in the US. I was pretty lucky to get this. Um but this should be a reasonable guide to just what to uh check once you get it. Is it within calibration? Do all the functions

**Dave Jones:** work? And stuff like that. So, let's power it up. Give it a go. Now, one thing I like about the tech uh 2200 uh series, there's a whole bunch of them. This one, the the specific triple 25 I've got here is um I think there's

**Dave Jones:** only one other which has a 500 mV uh per division vertical scale. But um the thing is, they're quite small and they're quite lightweight. This one only weighs about 6 kg. So, if you're buying a second-hand analog scope on eBay,

**Dave Jones:** weight can be a big factor cuz you'll pay shipping costs, especially if you're buying it from uh the US or some other country and shipping it overseas. It can be a big deal. So, this one's reasonably uh lightweight in the scheme of things.

**Dave Jones:** Um unfortunately, this one didn't have a um this one doesn't have the actual uh bail on it, the the tilting bail or the tilting handle, which comes over because it was a rack-mount uh unit. So, but that's not a big deal. You know, if if

**Dave Jones:** you need it really portable, then the tilting bail is important. But some you can pick up a bit cheaper because uh they don't have the tilting bail on. They come out of a rack uh system or something like that. Now, it's a good

**Dave Jones:** basic layout dual channel analog scope. I really like it. You've got your dual channel inputs here. You've got your uh horizontal. You've got your uh triggering totally separate over here. This has got uh auto full auto uh peak-to-peak triggering on it, which is

**Dave Jones:** really nice. It's got um it instead of a dual uh time base, this is only a single time base, but it does actually have um a times 5, times 10, and times 50 mag. So, it works like a dual time base, but

**Dave Jones:** it doesn't have the full uh capability as you get on a full dual time base analog scope. Now, let's take a look at the vertical here and you'll see that the reason I like this one is because it has a times

**Dave Jones:** 10 magnification. Most scopes on the market will only have times five verti vertical mag. So, it says up pull cal for times 10 mag. So, if you pull this here and you get this yellow, you can notice the

**Dave Jones:** yellow there on there. So, you can tell if it's up pulled out at a glance there, which is a really nice feature of this. Now, conveniently it's got two different two different positions here for your times one and

**Dave Jones:** your times 10 probe. Because this doesn't have like an automated probe detection for times 10, it doesn't have menus and all that other stuff where you can and on screen display of the volts per division. If you're using a times 10

**Dave Jones:** probe, which you will be most of the time, then you take this position over here. So, you don't have to multiply in your head. You just look at the one that you're using. I find that really quite handy. And of course it's got all the

**Dave Jones:** basic stuff on your vertical that you want. It's got AC and DC and ground coupling on both channels. It's got invert It's got an add mode where you can add both channels and it's got a subtract mode as well cuz

**Dave Jones:** that's what this channel two invert thing here does. If you want to subtract them, well, you invert channel two. So, you're adding channel one plus minus channel two, which means that you're subtracting them. So, it's got subtract mode and it's got alt and chop as well.

**Dave Jones:** And my almost most scopes have these because it's not a This is not an old school dual beam oscilloscope. This is a dual trace oscilloscope and the difference is actually quite significant, which a lot of people don't understand. This only

**Dave Jones:** has one one beam inside, so it can only project one beam of electrons at once onto the screen. So, if we put it into if we display both channels here, and we here we go. I've got it turned on here.

**Dave Jones:** It does actually work, by the way. It seems to at least power up. Now, we've got the dual channels here, and we can adjust those like this. And that's just fine. Now, it's on alt mode at the moment.

**Dave Jones:** What it means is that the a dual trace oscilloscope can only draw one trace at a time. So, it can only draw that one, and then that one. And this is what alternate means. Alt means it it alternates between these two traces.

**Dave Jones:** It draws this one, and it draws that one, and back at that one. And that's really good for higher time base settings. Now, you'll see this effect if we turn it down to 1 ms per division, 2 ms, you'll start to see it very shortly.

**Dave Jones:** There you go. 10 ms per division, you really start to see it. 20 ms, you'll see it draws that one, and it draws that one. There we go. So, that's why you need chop mode, because what chop does,

**Dave Jones:** instead of alternating between the two, it it slices Well, it still alternates between the two, but it does it not for a whole sweep. It does it like this. It just jumps between them like this. You can't actually see it, cuz it You can't see it

**Dave Jones:** vertically, cuz it disables the trace during that. But, it does actually it chops between the two like that all the way across. So, even at very slow time base speeds, you can get both traces on the screen at

**Dave Jones:** once. And of course, that that works up at higher frequencies as well, but it won't be as bright. And really, you should switch to alt mode if you're up on the higher settings like that. As I said, one of the great things I love

**Dave Jones:** about this scope is that it has 500 microvolts per division vertical scale. Now, as as you can see on the dial here, it only goes down to 5 millivolts per division, but it's got a * 10 * 10 vertical amplifier here, and most

**Dave Jones:** scopes on the market will only have a * 5. So, they'll typically might go down A good oscilloscope will go down to 1 millivolt per division vertical scale, but this one does better does uh twice as good as that at 500 microvolts. So,

**Dave Jones:** if you put down 5 5 millivolts vertical scale, and you pull that knob, bingo. Well, now I've got 500 microvolts per division, which is absolutely fantastic vertical scale. It is absolutely awesome. I love it. Now, we're going to

**Dave Jones:** check out this thing just just to make sure what its noise floor is like to make sure it's actually good. Make sure it's in the vertical scales are within cal. That's the first thing we want to check. Then, we'll move on to the

**Dave Jones:** horizontal, and move on to the triggering, and things like that. But, uh let's see if this thing basically works. So, let's give it a basic check out. First thing we're going to do is make sure we get both traces on the display

**Dave Jones:** here. So, we're going to put it into dual channel position. Alt is a good one just sort of mid-range on your horizontal time base here, you know, 1 volt per division or something like that doesn't really matter. And yes, we are

**Dave Jones:** getting two traces here. Now, we want to test the focus of the traces. As you can see, it really goes out of focus at both It's more towards one end, but as long as you can actually get that reasonably

**Dave Jones:** sharp. Now, that's a pretty good sharp trace. I really like that. No problems at all. And next, you want to test the intensity of it. The intensity is real It goes up really really bright. I like that. And

**Dave Jones:** basically, you want to turn that up to the fastest time base um setting you can get. In this case, it is uh 500 Sorry, 50 microsecond Sorry, 50 nanoseconds per division. Um and that is at full brightness with dual channels up. So,

**Dave Jones:** that's really good. And I can't see any uh screen burn-in here cuz these CRT displays um if if people have just left them on at full intensity, then they can get burned in, but there's no signs of of burning there at all. And we'll uh

**Dave Jones:** check the horizontal coarse and fine here. So, we move it across like that. It looks all right. There's a little bit of a There's a little bit of a wiggle there. I don't know if you can see that. Let's

**Dave Jones:** turn the vertical right up. No, it doesn't seem to matter, but there's a little little slight wiggle there. I'm not sure what that is, but uh make sure you can get the full horizontal uh trace on the screen like

**Dave Jones:** that. And you can do fine and coarse adjust. So, it looks like both fine and coarse work just fine. You want to be able to center it on the screen like that. No problems at all. Uh next thing

**Dave Jones:** you want to do is you're going to want to test the trace rotation when you buy it. Um if it comes from a different uh part of the world, you may have to uh do some trace rotations. So, you want to

**Dave Jones:** make sure that works. Line it up with uh one of the lines on the screen there, one of the reticules and uh it's spot spot-on. I like it. So, our focus intensity works, our horizontal position works, our vertical position works. You want to uh

**Dave Jones:** make sure that the line is nice and flat and it doesn't curve. You can see it starts to curve when it gets down to the bottom of the scope down there, but that's uh of the uh display down there,

**Dave Jones:** but that's fine. So, both uh uh So, that's the channel two position and the channel one position goes all the way up as well. No problems. It looks like it's working absolute treat so far. And the next thing we want to do is plug in our

**Dave Jones:** function generator. Now, I'm using my Agilent 3000 X-Series oscilloscope, the WaveGen module from that cuz that's the highest frequency general purpose function generator I've got here in the lab. So, what I've done is I fed in a 1

**Dave Jones:** kHz sine wave. There it is. There's my scope up there and I've got it set to a 1 kHz sine wave at 400 mV peak to peak. Now, the reason it's 400 mV is because that will give us a full scale down here on

**Dave Jones:** our scope. You can do it at other values, but it's just I just like to get full scale here. Now, this thing is supposed to output 400 mV per division. My vertical scale here on channel one is 50 mV per division. And

**Dave Jones:** as you can see, if I put it right down there on the bottom, it's just shy of the upper marker there. So, really it's slightly out of cal on the vertical channel. They're not a huge amount. I'm not

**Dave Jones:** overly concerned about that. Now, let's try channel two as well. Let's It's 50 mV per division. Once again, it hasn't triggered from there cuz it's still triggering off channel one over here. So, we need to the source to be

**Dave Jones:** trigger two. Bingo. So, we're now testing our trigger capability from channel one, channel two. Works just a treat. We'll have to test external later, but vertical mobile just select select between the two of them basically. And we select it the channel two there.

**Dave Jones:** There we go. Not a problem. It's It's reasonably clean and nice. I like it. And look, you can actually see if you look in there, you can actually see the step response of the DAC inside the Agilent 3000 series function

**Dave Jones:** generator. You can Let me try and turn that Oh, sorry. Wrong channel. There we go. There we go. Look at that. You can see You can see the DAC. You can see the steps in the output DAC cuz it's a digital

**Dave Jones:** function generator, not an analog. See the steps in it. Look at that. Beautiful. I like it. So, anyway, let's turn it back and Whoop. Really high intensity there. And channel two, once again, it is short. Um it's it's slightly out of cal, but at

**Dave Jones:** least it's consistently out of cal on both channels. So, we'll have to pop it open later, find the adjustment pot, and adjust the vertical. But, that's a good enough. I wouldn't complain about that too much at all. And I've changed the

**Dave Jones:** function gen to 4 volts per division. So, now I'm at 0.5 volts per division on channel two, and it's exactly the same. It's out by the same amount. So, I really like that. Plug it into channel one here, and uh

**Dave Jones:** trigger off channel one. Let's turn it up, and bingo, it's out by, once again, the same amount. It's very consistent across there. So, really I'm I'm quite happy with that. And you can test all the scales in the

**Dave Jones:** same way. You can see that that one is half of the value we had before. And so, therefore, so it looks to work a treat on all ranges. Really, I'm quite happy with that. And one more check right down at

**Dave Jones:** the low end. I've set the function gen to 40 millivolts peak-to-peak, and we've got it on 5 millivolts per division. And once again, out by the same amount. Beautiful. I love it. It's working a treat, and it's relatively

**Dave Jones:** Well, it's it's very noise-free down at 5 millivolts per division. Now, let's try and take it down a bit further and try this times 10 magnification gain. Now, unfortunately, my function generator only goes down to 10 mV peak

**Dave Jones:** to peak, and that's not low low enough to test the 500 microvolts per division range, which this thing's capable of. So, I have built this little contraption here, which is four 50 ohm terminators wired in parallel onto the coax here,

**Dave Jones:** and I've set my function generator to 50 ohms output. And just so happens I've got a little Dave CAD drawing here, which shows what's going on. The function gen is set to 10 mV peak to peak, and that's into a 50 ohm load

**Dave Jones:** because I've turned on the internal 50 ohm load in the function generator. So, if we had a single 50 ohm terminator here, we've actually got four, but if we had a single one, then we would get our 10 we would get that value, 10 mV peak

**Dave Jones:** to peak, into 50 ohms. But, because we've got four in parallel like this, it's actually 12.5 ohms total. And if you do the math, it comes out to drops it down to 4 mV peak to peak, which is great because we've got eight

**Dave Jones:** divisions on our screen here. 500 microvolts per division gives us 4 mV peak to peak full scale. Fantastic. And here it is. It This is not on times five Sorry, times 10 mag, but if we pull it, bingo. There's the There's our sine wave

**Dave Jones:** in on times five mag. Now, you notice that it's actually more than 4 mV peak to peak, and that is not because of the scope. That's an error in our function generator. If we go up here, and we plug it into our

**Dave Jones:** Andromeda up here. Check it out. We actually get Yep, you probably can't see it there, but it's actually 4.7 mV peak to peak. So, the function generator isn't actually spot on. We go into the wave generator. There it is, 10 mV peak to

**Dave Jones:** peak. There's obviously uh some error in that as you'd expect when you get down that low. And uh basically, we are getting 4.7 mV peak to peak. I've got the averaging uh turned on there. If we uh turn the averaging off, we can

**Dave Jones:** actually see that it's a bit noisier than that. But uh you turn the averaging on and bingo. So, this thing is uh our Tek 2225 is working a treat. I love it. Now, you can actually see when we've got no input down here, it's

**Dave Jones:** actually picking up a whole bunch of noise on * 5 um uh * 10 mag. Sorry, I'm so used to saying * 5 uh magnification for vertical. This is * 10. So, uh that's the same on channel one. Or let's

**Dave Jones:** try channel two. Oh, it's not as bad on channel two. So, if we turn them both on there, you'll uh notice that um Oh. What have we got here? We've got uh add. There we go. That's the problem. There's

**Dave Jones:** your problem. Right, we've got alt mode. And look, uh channel one is a bit Channel one is a lot noisier. It's got something on there. So, something's going on there. It's not the best. When you turn it down, you can notice a bit

**Dave Jones:** more noise, but you turn the time base up, it's definitely got something something on that. So, I'm going to actually apply a uh terminator to that and see if we can get that to go away. Yes, it certainly does. If we terminate

**Dave Jones:** that, it's gone. So, likewise on channel two. So, I'm not sure where that's coming from. Maybe something internally. Of course, if I put my hand near it or my hand on the control, something like that. So, when you're

**Dave Jones:** measuring low noises like this, just uh it noise pick up is a major issue. But, um I do deem that to be uh pretty decent and uh working reasonably well right down at its 500 microvolts per division. Now, we have to check out

**Dave Jones:** our horizontal as well. Now, I'm feeding in my 1 kHz signal and I've got it set to 0.1 ms per division, 100 µs per division, and you'd expect to get 10 divisions there, but you don't. It's actually shorter that. So, uh the

**Dave Jones:** horizontal isn't uh isn't really uh spot on. That needs to be uh adjusted as well if you want to calibrate this thing. I mean, you know, if if you just want to get uh signals on there, then, you know, it's it's good

**Dave Jones:** enough. But, uh yeah, I would I would be tempted to go in there and tweak that just so that's that's a bit too far out, I think. I'm not happy with that. So, we have to uh cal that internally.

**Dave Jones:** And we need to check our trigger as well, of course, now. So, we'll take our trigger level here and we just uh adjust it and make sure it goes uh make sure it goes between pretty close to the positive and negative um values

**Dave Jones:** there, and it certainly does. And uh if we uh choose the negative slope trigger and do the same thing, yep, that's working perfectly. No problems at all. And that's in the peak-to-peak auto triggering mode. We also want to test

**Dave Jones:** the uh normal mode as well. So, we move it over to normal and we turn it back to peak-to-peak and you see it, boom. It uh goes straight in there. But, if we go to normal mode, once we get past that

**Dave Jones:** trigger threshold up there, it should vanish. So, yep, it does. There you go. And likewise on the bottom side, once we reach that just past the negative uh bottom of that waveform down there, bingo, gone. And once again, then

**Dave Jones:** positive and negative, and it works a treat. So, normal mode works as well. And we'll check the single sweep mode over here. So, take it all the way over, and we get nothing on the screen. This is where you're probably going to want

**Dave Jones:** to turn your intensity up like this, and then press the trigger button. There it is. Bang. No problems at all. And a very simple way to test your trigger hold off down here is to set it to minimum, and note the brightness of

**Dave Jones:** the trace here. And as you turn your hold off control up, it should dim like that. And that's a very basic test that indicates that the trigger hold off is working as well. And we're going to want to do a quick

**Dave Jones:** test on the external input to make sure it works as well. Um now, this triggering off channel one at the moment up there, but if I turn it down to external here and external and the source actually to uh external, cuz this

**Dave Jones:** external mode you can choose between the 50 Hz line frequency or external divide by 10 or external or uh Z input, but there you go. It's uh try and it's triggering stably, and if I disconnect that, of course, it loses its trigger.

**Dave Jones:** Works a treat. And we'll just check our line triggering here as well. This means that it actually gets the trigger source uh from the 50 Hz mains or if you're in the US, it'll be 60 Hz uh mains, but

**Dave Jones:** it's 50 here. So, I've set my function generator to 50 Hz, and I if I go below 50 Hz, you'll see it's scrolling one direction, going across like that. And if I go above 50 Hz, it'll go back in

**Dave Jones:** the other direction. And of course, if you had the ex- if you had it exactly the same frequency as the main frequency, it would actually be stationary, but I can only adjust my function generator in 0.1 Hz increments.

**Dave Jones:** So, my mains here in Sydney at the moment is somewhere between 50 .0, that's 50.0, it's going in one direction, and 50.1 Hz. There you go. So, it's somewhere in between there. So, the mains frequency in Sydney at the moment

**Dave Jones:** is probably 50.05 hertz or thereabouts, give or take. And we'll do a quick functional check on our trigger coupling up here. I've got a AC coupling and it should work on DC in that peak-to-peak order. Now, if I

**Dave Jones:** turned over to normal mode here, okay, in AC coupling, it should trigger. But, on low frequency at my 1 kilohertz test signal, um it should actually completely attenuate that so there's nothing to trigger on. So, it should disappear. And

**Dave Jones:** high frequency, it should work a treat. And if you keep it in auto mode, then it's pretty much it's still going to try and get a trigger there even with the low frequency filter on. But, if we put on low

**Dave Jones:** frequency or reject filtering and we increase our frequency here, then it should eventually trigger at What have we got? Way up there. It's way up there. It's We're in the megahertz region at the moment. Let me turn that back. Frequency

**Dave Jones:** gen was a bit overzealous there. But, if I put that down to you know, that's 90 kilohertz, 50 That's 10 That's 10 kilohertz roughly and it's just starting to trigger at 10 kilohertz. There you go. So, it's an

**Dave Jones:** order of magnitude thing really. So, anything over 10 kilohertz this thing's going to trigger on nicely. And likewise with the high frequency reject filter, it's 8 kilohertz at the moment. If I turn up the frequency on that thing, it should eventually not

**Dave Jones:** trigger at all. Let's see what frequency it stops triggering at. 50 kilohertz, 60, 70, 80 130 kilohertz, still got 170, 160, 150 kHz. There you go, it's barely triggering now. 180 kHz and it's stopped triggering completely. That works a

**Dave Jones:** treat. And if you're a really keen TV service tech, you might go in and test your TV line and your TV field mode, but I'm not going to bother. Now, let's go back to the horizontal here. I'm feeding in a 100 kHz sine wave

**Dave Jones:** and uh let's put it onto the alt horizontal mode, shall we? And it hasn't displayed anything at the moment. That's because And it's on times five uh magnification uh time base. That's because we haven't done the trace separation. There it is. Bingo. There is

**Dave Jones:** our magnified There's our magnified waveform. So, if we turn that down, we can actually uh separate the traces like that and actually get both of them on the screen at once. So, that's our times five. Uh that That

**Dave Jones:** looks like times five to me. I won't go in there and measure it, but it looks pretty good. And that's times 10. There it is, okay? So, that looks like it works an absolute treat. And we can even go to

**Dave Jones:** times 50 here and bingo, there it is. That's the times 50 magnification. And of course, if we just go over to mag here, it'll just display the magnified waveform like that, but you can do both or just the one. So, there you go. That

**Dave Jones:** looks like it works fine. I like it. And we should actually check that that value is spot on. I've got times uh 10 mag at the moment with the 100 kHz, so I'd expect uh that to be 10 divisions across and it's

**Dave Jones:** not. It's slightly out, just like it is with the um main time base as well. But that should come back in once we calibrate the main time base. Another thing we haven't checked is the probe adjust here. So, I've got a times 10

**Dave Jones:** probe, so we're actually going to use the times 10 uh setting over here, not the times one. So, we're on 0.1 V per division. It says we should be getting 500 mV peak-to-peak at 1 kHz. Are we? Well,

**Dave Jones:** not quite uh five divisions there, so it's a little bit out, uh but not a problem. And uh we should be getting basically 1 kHz, but once again, the time base is out just like it was before. So, looks like our uh probe

**Dave Jones:** adjust is working fine. Let's have a quick check of the high frequency bandwidth here. I've uh I'm I'm feeding in the highest frequency I've got from my function generator, which is 20 MHz at uh uh 4 V peak-to-peak. Now, um

**Dave Jones:** this uh once the problem with this Tektronix 2225 is if you use it on standard time base, it's just really it's not fast enough. That's as fast as it goes, okay? So, you know, I can see the 20 MHz signal there, but you can't

**Dave Jones:** easily get in there and measure its frequency and stuff like that. So, it really forces you to use your uh forces you to use the mag mode, which is okay. There's nothing inherently wrong with that. It's just uh not as nice as um

**Dave Jones:** some other scopes which have the main time base which uh goes down to that. But anyway, that's okay. And you'll notice that it it's a bit fuzzy here. Once again, if we go here, our frequency is uh slightly out again, of course,

**Dave Jones:** because our main time base is out as we've verified before, but uh as you can see, the amplitude has dropped a bit from um uh where it was before. So, uh really, you know, it's um it's it's starting to

**Dave Jones:** roll off there, I think. Now, one thing I didn't mention with the vertical channels is uh that um the bandwidth the quarter bandwidth 50 MHz is only for uh basically all of your um basically from your five millivolt range and up. Once you engage

**Dave Jones:** this times 10 magnification here, you will actually drop the bandwidth. In in the case of this oscilloscope, its bandwidth with the times 10 gain on any either of these vertical channels, the bandwidth drops to about five megahertz. So, it drops by an order of magnitude,

**Dave Jones:** uh basically. So, just something to watch out for. You don't get the full 50 megahertz quoted bandwidth down at your very low um volts per division settings. Just a little trap to watch out for. Now, as you can see, my 20 megahertz signal

**Dave Jones:** looks a bit fuzzy there. That's because my intensity is right up and it's causing a bit of a blooming effect on that signal. Now, I you know, I don't know if um uh this you know, if there's actually

**Dave Jones:** something wrong with here and the and there and the triggering is you know, there is a bit of trigger jitter or its performance at the high frequency isn't as good as it should be. I'm not sure. I'd need a reference uh 2225 scope to

**Dave Jones:** actually uh compare its true performance there. But anyway, that's more than good enough for my purposes. I'm not fussed with the high frequency uh performance of this thing anyway. So, um now, if you wanted to actually test the

**Dave Jones:** bandwidth, I've mentioned this before of any scope really, but in particular these analog ones is you can feed in a square wave. And if you don't have a 50 megahertz um uh function generator, that's fine. Just feed in a 1 kHz square wave with a very

**Dave Jones:** fast rise and fall time. And you'll be able to um see you'll be able to by measuring the That's a square wave I'm feeding in now. It's not terminated properly and all that sort of stuff. But um you'll be able to measure the rise

**Dave Jones:** time, the rise and fall time of the oscilloscope uh will basically be equal to um uh the Well, the bandwidth will be equal to 0.35 on the rise time. So, um that's a way to actually calculate the bandwidth of your analog oscilloscope.

**Dave Jones:** If you don't have a function generator to go to that high. I've men- I've demonstrated that and mentioned that in one of my Rigol blogs if you want to check it out. And the last thing I'm not fussy about,

**Dave Jones:** but the beam find, yep, beam find works. Now, there you go. That's I've done some basic tests on this thing and apart from some slight calibration issues with the vertical channel and the horizontal, they've drift a bit. I

**Dave Jones:** should be able to bring those back into cal by tweaking some pots inside or something like that, but yeah, I'm quite happy with this. It It works. It was advertised as working, but I took a bit of a risk. I don't think they were

**Dave Jones:** It was actually showing any waveforms in the actual ad for it, but I deem that to be a winner. There you go. So, you know, don't be too scared to buy these analog scopes on eBay, but one tip, if you are going to

**Dave Jones:** buy it and you really want to be sure that it's working, at least buy one that actually shows both waveforms on both channels. Like hooked up to just the probe adjust signal or something like that. If you can If you got both signals on there

**Dave Jones:** and showing a basic waveform, then you can be pretty sure that it's going to do most of its basic functions. And if it is slightly out like this, then you can just start tweaking it back into calibration, get the service manual, and

**Dave Jones:** do that. So, there you go. This was fun, and I really like this. It does seem to perform reasonably well. I'm quite happy with it. I'm going to download the service manual for it and get in there and tweak the pots and have some fun, I

**Dave Jones:** think. See you. Oh.
