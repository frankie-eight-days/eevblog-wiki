---
video_id: n13odoXQYeo
title: EEVblog #642 - TI Connected Launchpad
url: https://www.youtube.com/watch?v=n13odoXQYeo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 36, "3": 67, "4": 88, "5": 110, "6": 127, "7": 147, "8": 165, "9": 189, "10": 204, "11": 221, "12": 238, "13": 255, "14": 271, "15": 287, "16": 305, "17": 322, "18": 340, "19": 356, "20": 376, "21": 396, "22": 412, "23": 432, "24": 448, "25": 464, "26": 480, "27": 492, "28": 508, "29": 528, "30": 552, "31": 568, "32": 592, "33": 604, "34": 620, "35": 644, "36": 656, "37": 668, "38": 688, "39": 704, "40": 732, "41": 752, "42": 768, "43": 784, "44": 804, "45": 820, "46": 840, "47": 856, "48": 872, "49": 892, "50": 912, "51": 928, "52": 940, "53": 956, "54": 976, "55": 996, "56": 1016, "57": 1036, "58": 1052, "59": 1068, "60": 1084, "61": 1096, "62": 1112, "63": 1128, "64": 1144, "65": 1164, "66": 1176, "67": 1192, "68": 1212, "69": 1228, "70": 1244, "71": 1260, "72": 1272, "73": 1288, "74": 1308, "75": 1332, "76": 1348, "77": 1364, "78": 1380, "79": 1404, "80": 1420, "81": 1432, "82": 1452, "83": 1480, "84": 1492, "85": 1516, "86": 1536, "87": 1552, "88": 1576, "89": 1600, "90": 1612, "91": 1628, "92": 1648, "93": 1668, "94": 1696, "95": 1720, "96": 1736, "97": 1756, "98": 1772, "99": 1788, "100": 1808, "101": 1820, "102": 1836, "103": 1852, "104": 1868, "105": 1884, "106": 1900, "107": 1916, "108": 1936, "109": 1956, "110": 1972, "111": 1988, "112": 2020, "113": 2036, "114": 2052, "115": 2068, "116": 2084}
---

**Dave Jones:** Hi, today we're going to take a look at the Texas Instruments Teva C-Series Connected Launchpad. It's one of these super cheap Internet of Things development boards. Now, TI, of course, about four odd years ago or so, released the original launchpad at $4.30. It was absolutely insane price.

**Dave Jones:** This one's almost as insane. It's only $20, even from the likes of Digikey and other distributors. Absolutely incredible for what you get in here. It must almost be cost price, practically. They're friggin' giving these things away. Unbelievable. Anyway, so I get the part number right.

**Dave Jones:** It's got one of these ridiculously long part numbers. It's the EKTM4C1294XL. Whoop-de-doo! Why do I have to give them such friggin' long part numbers? I don't know. Anyway, it's the Connected Launchpad. And it's got a whole bunch of powerful stuff built in. 120 megahertz, 32-bit ARM Cortex-M4 processor in it, 1 mega flash memory, 256k of SRAM, 6k of E-squared PROM.

**Dave Jones:** It's got a 10100 Ethernet MAC and PHY on it, and it's got data protection, CNC, timers, two 12-bit 2-meg sample per second ADCs on it. Yeah, that sounds impressive, but I don't know. We'll have to check the data sheet for that, because it might be 12 bits, but eh, what's the effective number of bits?

**Dave Jones:** How good is it really? I don't know. Usually the ones built into these micros aren't that crash-hot, but still, 12-bit ADC at 2-meg samples per second. Fantastic. It's got PWMs, it's got USB, serial comms, it's got Keil 32-bit code limited C compiler, as well as the IAR 32k C compiler as well.

**Dave Jones:** So yeah, limited 32k, but you can probably do a whole bunch of useful stuff in that. It comes with a starter guide, and apparently pre-programmed with an Internet of Things application. So you can just hook it up, supposedly, out of the box, and it just works as an Internet of Things demo.

**Dave Jones:** Will it? I don't know. Let's try it. So what do we get in the box? Well, let's have a look. We get a quick start guide which we'll take a look at, we get the board, ESD wrap for your protection, and we get one of these ridiculous badly designed pool Ethernet cables, oh, I hate those things.

**Dave Jones:** Oh, they're kind of, sort of convenient for travel and things like that, otherwise pain in the arse. And a yet another micro USB cable, as if I didn't already have enough. And you get a relatively fair amount here for your 20 bucks. We've got the main TI processor, of course,

**Dave Jones:** that's the ARM Cortex-M4, that's actually what you're paying for. We've got ourselves a little pulse transformer here for your 10100 Ethernet, of course. And we've got a couple of switches around here doing various things, couple of jumpers for various configuration stuff. And you also get a debug and slash programming interface over here.

**Dave Jones:** So you've got yourself a little debug header, tiny little pitch, and you've got two booster pack connections here, that's their term for, you know, the add-on boards, and they've got a whole bunch. I like how they've labeled the signals on the back there, that's really nice.

**Dave Jones:** And we've got ourselves a MAC address, and supposedly comes already pre-configured, as I said, with that Internet of Things application. Well it seems the quick start guide doesn't entirely suck. We've got a board overview here, and we've got ourselves the debug and power port.

**Dave Jones:** It's powered from the USB port here, it's got like no terminal, it doesn't look like it's got any terminal connections for external power. You have to sort of use that micro USB I think. Although it does have a power select jumper here, so I'm not sure what's going on there, I don't see any other big tabs.

**Dave Jones:** Oh that's right, you can get a battery pack attachment for the booster, so you can come in, your power can come in via the booster connectors apparently. So that's probably what that's switching there. We've got a couple of user LEDs and IOs and user switches and wake and reset switch.

**Dave Jones:** And yeah, that's about all. Not a huge amount on there, it's designed of course to have all the plug-in booster packs. We've got ourselves a pretty funky looking IO map here for the two booster pack connectors. It's kind of weird how they've sort of like staggered them.

**Dave Jones:** I assume that that is the other side of that connector there, and oh yeah, like, you know, I don't know, how does that sort of match up to that kind of thing? I've got to assume that sort of that one there is that row there,

**Dave Jones:** and that column, yeah, that one's that one, and blah, so on. So anyway, that wasn't great, would have been nice to have a photo in there. But anyway, here we go, here's our basic steps for connecting up our Internet of Things demo. I'm going to follow through those and see if it works, or will it be a donkey?

**Dave Jones:** Just a quick look at these jumpers here, I do like how they've labelled those. There we go, power select, power can come from the booster pack, USB on the go, or the in-circuit debugger. You generally wouldn't power it from the in-circuit debugger in system use, of course.

**Dave Jones:** But yeah, that's really nice. 3.3 volt jumper for the microcontroller here, that's nice, assuming that that disconnects all the power from there, that's really useful. Because then you can put your current meter in there, or your microcurrent, whatever, and measure your current consumption of your CPU.

**Dave Jones:** So that could be really nice, I've got another 3.3 volt jumper over here, I'm not sure what that one's actually doing, but yeah, it's handy to be able to get in there and measure your power consumption on these development boards. And just a quick one, here is an example of where

**Dave Jones:** burden voltage on your multimeter to measure current causes an issue. Let's actually probe this thing, I've taken the jumper off, okay? And watch the LEDs down there, you'll see that that LED is barely like, it's not functioning, it's not powering up as it

**Dave Jones:** should, right? But if I connect it over to the amps jack here, and do the same thing, bingo! It powers up, no problems whatsoever, and starts to operate. Because it obviously, the burden voltage of the meter was too high, and it was dropping the voltage to the

**Dave Jones:** microcontroller, it couldn't operate properly at that particular current, and of course you switch over to the amps range, and everything's hunky-dory, and that's the LEDs that I expect when it actually runs the thing. So there you go, that's just a little example of

**Dave Jones:** burden voltage. Ta-da! Okay, step number one, go to ti-exocyte.com TI have partnered with Exocyte, I don't think I'd heard of Exocyte before, but yet another one of the countless internet of things like online cloud type services company that are popping up to get all your stuff connected.

**Dave Jones:** Anyway, they've got a couple of tutorials and things like that here, but we've got to sign up, create an account here. So I won't bore you with the details, we'll come back. Alright, I created an account, and the stupid thing asked you to put in like

**Dave Jones:** a really secure password, and put in like my standard just dumbass password for sites like this, and it just wouldn't accept it, not secure enough! Screw you. Grrr. I hate that sort of crap. Anyway, yeah, logged in, it gave me the email thing, I had

**Dave Jones:** to verify my email, but yeah, and it gives you, apparently gives you 30 free SMS test messages or something. The Exocyte system can apparently send you SMS messages when your data from this device meets certain conditions and stuff like that to alert you.

**Dave Jones:** When you get 30 for free. And after that, I don't know how much it costs anyway. Alright, here we go. We're going to click here to add a new device to our portal. And let's see. Here we go. These are all there. Connect launchpad.

**Dave Jones:** Connected launchpad. There we go, that ridiculous part number. And that's the one I want to, yep, continue. Set it up, enter your MAC address. And here we go, we've got to give it a name. I'm going to call it Bruce. Good on ya Bruce.

**Dave Jones:** And we're in Sydney, Australia. Not Austria. Let's go through and successfully enabled with the CIK, whatever the hell that is. Your device is connected to the Exocyte platform within 24 hours, provision request. What's that garbage? Ah yeah, whatever. Let me play with it.

**Dave Jones:** Add device. No, that's it. We're already done. So let's go home. And there we go, Bruce! There's Bruce. Active, on, active event, nothing. I guess now I have to plug it in. It's all plugged in, I only have one USB port. In fact I had to take off my little Bluetooth dongle, I didn't have any.

**Dave Jones:** And bloody, so many USB connected bloody devices. And I only have one spare port left on my ethernet switch as well. So it's all plugged in. Let's see if the sucker works. Rightio. Come on Bruce, you can do it mate. Here we go, let's click on Bruce.

**Dave Jones:** And we're in! We're in! Online! It's been online time. Okay, it's got an online counter. That's pretty good. Junction temperature of the device. Presumably, it's just got an on-chip transistor, you know, PN junction silicon diode temperature sensor. They're pretty crude, but they do the job.

**Dave Jones:** Two minutes and eight seconds it's been online. Actually, see if I can heat up that chip. See if it changes. Hang on, I'll put my finger on it. I've got my finger on it, and we've got a graph of the junction temperature there.

**Dave Jones:** And... no, no, I've got a bit of noise on that. You know, in fact we've got a lot of noise on that thing. Anyway, that's the junction temperature, and that's all it's displaying at the moment. Next, waiting for device. Hmm. Oh, there you go.

**Dave Jones:** There are 989 launch pads connected around the world. Look at that. Any in Australia? Oh, tell you what, am I the only one in Sydney? No, there's two! There's two! Can you believe it? Two in Sydney, one there, and one... oh, in Glebe.

**Dave Jones:** Somebody in Glebe's got one. Good on ya. And I'm in... I just put Sydney as my suburb. I didn't know that you could actually put in a... that's right, it did ask for a... you could put in an exact GPS location of the thing.

**Dave Jones:** So I could go in there and edit my account, I'm sure, and update that, but I just put in a generic Sydney. So it's just showing, eh, it's smack in the middle of one of the main arterial roads leading to the Sydney Harbour Bridge.

**Dave Jones:** There's the Sydney Harbour Bridge, for those who don't geographically know Sydney. The Opera House is just there, and yep, that's smack on one of the overpasses there leading to the Harbour Bridge. Awesome. And here we go. Yes, I do have the launchpad under my desk here, because of the tiny short little USB cable provided

**Dave Jones:** and stuck in the back of my machine. And please forgive the crudity of that video quality. Anyway, look, I can turn the LED that they were both on before and turn them off. They should be off, I can't see it, it's actually under my desk, but I have no reason to

**Dave Jones:** believe that is not, that LED is not switching off and on. There we go, I'll switch it on again. And woohoo! That was terribly exciting. What happens if we touch the switch? Anything? Nope. Zip. And if we press the buttons here, there we go.

**Dave Jones:** Let's have a look. Three button pushes! And the other one? Let's wait, it takes a while for that counter to update, I think. Yeah, there we go, it does take a while. So I'm going to press those really quick and see if it buffers those button presses, and then

**Dave Jones:** so I'm going to do the one on the left here, I'm going to hit it three times real quick. One, two, three. Will it jump up to ten? Let's find out. It did! There you go, okay, so that's not bad at all. So they've properly

**Dave Jones:** debounced those and actually buffered those. I'm not sure how quickly it updates the, probably, you know, like it polls it probably every second or something, polls the board, that's typical for these internet of things devices anyway. So let's check out a few other things on here.

**Dave Jones:** I'm going down to the portal menu down here on the left hand side, and here's my portal results summary. And yeah, there's no SMS limit. I was wrong on that, I didn't completely read the email. To get your 30 SMS free SMS things, you've got to fill out a stupid freaking survey.

**Dave Jones:** Ah, unbelievable. Anyway, it can send ten emails daily as part of the service for free I guess, but I don't know about the prices and the plans for this thing. I don't know, check that out for yourself. And shares, we're only allowed a certain

**Dave Jones:** number of, you know, these things based on our current plan. But anyway, look, portal roles, it looks like you can enter viewers, managers, presumably it is public viewable. I've got to set that up. If it is, I'll link it in down below if you can actually see, and you can see the, I'll leave it running

**Dave Jones:** and you'll be able to see my connected launchpad. I'll leave it up there for like, leave it connected for the next couple of days or something like that. Unless I can find something useful for it. But there you go, you can invite users and have them hook up and role of a manager or

**Dave Jones:** viewer. I don't know exactly what's going on there, but it sounds quite comprehensive. Then we've got some scripts. Let's go in here and check this out. Bruce, alert manager handler, waiting, waiting for something. Okay, well I guess we can set up scripts for all you script kiddies out there.

**Dave Jones:** Fantastic. I'm sure it's actually quite powerful. And it's all TI branded here of course, but it's not actually using TI's website, it's actually using ExoCite of course. It's just a subdomain there on the ExoCite website. So all this backend, all this backend frontend stuff is all powered by ExoCite.

**Dave Jones:** So presumably you don't need a Texas Instruments device to use ExoCite. You can hook up any internet of devices thing that you want there. And so what I'm going to do is I'm going to, I might have to try and get, fill out this

**Dave Jones:** stupid survey to get my free SMS's, because I want to like push the button on this thing and set it up and then get it to send me an SMS based on this is all current data, junction game state, whatever that is. Oh yeah, by the way,

**Dave Jones:** I signed up for this thing. It allowed me to choose a time zone, fantastic, but it did not have bloody Sydney listed there. Are you shitting me? All it had was bloody Brisbane or Perth or something like that. Yeah, correct time zone, but

**Dave Jones:** ah, give me a break. Don't want to be bloody Brisbane. Bloody Queenslanders. Well, well, well, look what we have here. What the hell is this? Comm surrogate has stopped working. What the hell is the comm surrogate? Close the program. Shockwave flash may be busy.

**Dave Jones:** Oh, what the hell? Unbelievable. Continue. No, it's just, it's crashed! Unbelievable. What a heap of garbage. What the hell's going on? Maybe I don't have the latest shockwave flash plug-in. I'm sure I updated that the other bloody week when it popped up and annoyed me about it.

**Dave Jones:** This is just, ah! Alright, it just spat the dummy and we're back. I don't know what happened there, but check this out. If we click on junction temperature, look what pops up here. The graph of the junction temperature. This looks really quite powerful.

**Dave Jones:** And there's our device, Bruce. And you can do calculations and all sorts of stuff. You would have to spend hours to sit down and try and study exactly what this exocyte thing's capable of, but this looks pretty powerful. And all the data logging stuff is there.

**Dave Jones:** Delete data source, share data, so I can share it with people, or download it presumably. That's really quite neat. And same thing will happen if I click on the LED one, no doubt. Yep. So we can get data for the LED, see how many times the LED's turned off and on, or the user switch,

**Dave Jones:** or anything else that you want to set up. Not bad. Now I've actually come back the next day, I shut down my machine, well I didn't shut it down overnight, but I put it to sleep mode as I normally do overnight. So I came back today

**Dave Jones:** and look, it's now offline. I had to log back in, it had sort of logged me out from the exocyte thing, but it says Bruce is offline here. And like, I don't know what the deal is. It hasn't like automatically refreshed, my board is still

**Dave Jones:** powered up, it's still plugged into my ethernet connection. By the way, my internet connection was shut down overnight though because my ISP was doing an upgrade thing, so maybe that has something to do with it. But jeez, I would have expected it to

**Dave Jones:** automatically reconnect. Anyway, there are flashing lights still on the board and it's powered up. I haven't physically touched it since then, so I'm not sure what's going on there at all. And the strange part here is, on this main home screen here, look

**Dave Jones:** it says active on, active event no, so I assume I thought that active on would have meant that it's physically online, but it's not. Look, status offline. All I'm going to do is repower the board and see what happens. Here we go. There we go, I've repowered the board

**Dave Jones:** and by the way, I am still getting that com2 surrogate error or whatever it damn well is. Here we go, yep, it's appeared online. So has the board done something weird when it lost the internet connection? Has it locked up or something like that perhaps?

**Dave Jones:** Because I definitely do know my internet connection went down last night but jeez, you'd expect it to be robust enough to handle that sort of thing and recover. That's what you need from internet of things. Anyway, I don't know, need to hear back on that, whether that's

**Dave Jones:** a bug or not. Alright, now I'm going to assume that the virtual com error message that keeps popping up is due to the fact that I haven't installed the drivers for the virtual com serial port. So it tells you that in the quick start, well it tells you to download this in the quick start guide, so I will

**Dave Jones:** and I'll be back. I really hate drivers like this that just come in a zip file. A, you've got to unzip them, and then it's just the driver files. It doesn't actually give like an install or anything like that, so I've got to

**Dave Jones:** go through the manual process of bloody installing the driver. What a pain in the arse. Okay, so what I'm going to do now is I'm going to try and add an event here. So if I click add an event, I want to get this thing to email me when I push

**Dave Jones:** the button. Okay, something incredibly simple like that. I can't get the SMS to work yet because I filled in that survey thing and you have to wait like 24 to 48 hours before your credits come through on your SMS stuff. Goodness anyway. So user switch one, so let's see what

**Dave Jones:** we can do with user switch one here. Event name, you know, we'll just call it switch or something like that. And I don't know simple, yeah, timeout. Okay, that's not bad. You can count after a certain number of counts. That's pretty good. You can do if then

**Dave Jones:** until. Right, okay, that's pretty good. That looks really quite nice. I like that interface. Alright, what we've got here is we've set up that event. Now it separates events from alerts here and that makes sense really. So what we've done is we've set

**Dave Jones:** up this event called switch which all it does, very simple, that if I press the switch, I just guessed that the constant was one here and I was correct. And then it basically, you can do more complex constructs than that, but I've just set that and you can

**Dave Jones:** see I've already pressed the switch once and it has detected it. So one occurrence in the last seven days. So now we should be able to set up an email alert or some other alert here that is then associated with that event called switch.

**Dave Jones:** Let's try it. So let's do that, add alert here, reference event source, and by the way I haven't read any documentation for any of this, I'm just winging this first time user stuff. So switch on Bruce, if we had more than one event it would have showed up,

**Dave Jones:** and if we had more than one event on more than one device, then presumably they would all show up there. So the switch, there we go, let's alert name, Dave switch email, and alert interval in seconds, no repeat, okay. Email, so the alert, we're email,

**Dave Jones:** send Dave at EEVblog, and we'll just call it Bruce switch. There we go. And submit, and now I'm going to try that and see if that, enter a numerical alert, numerical value, hang on, whoa. Alert interval, zero, okay, forced to put that in.

**Dave Jones:** There we go, submit. So now it should email me that if I push the button. Woohoo! And I'll tell you what, these com surrogate error messages are getting really annoying, they keep popping up like every couple of minutes. Oh, infuriating. Anyway, I'm going

**Dave Jones:** to push the button, reaching under the desk, here we go, and I've pushed the button, it could take a couple of seconds to update that, because it's not a push, I don't think it's a push thing, I think it's a polled, I'm not sure, occurrences,

**Dave Jones:** come on, come on, don't make a fool out of me. Come on, you can do it! You can do it! No, do I have to read, it popped up much quicker than this last time? It really did. It popped up within a few

**Dave Jones:** seconds. So, what? What? Not sure what's going on there. It might have been that com surrogate error message bloody thing, I'll just refresh the entire page, and, nah, false, active, what's going on? What's going on? I don't know, false? As in, pfff, I don't get it.

**Dave Jones:** Well, if I go back into the event here, it now knows that it's associated with this alert here, so that's rather nice, but I have no idea why it's going false and I'm pressing the switch and it's not showing up. I don't know, what do I

**Dave Jones:** have to do, reboot the bloody board again? Okay, now what I've done is I just deleted this entire event and started from scratch again, I couldn't figure it out. So now it's active, true, and I'm pretty well, look, it's got one occurrence already.

**Dave Jones:** Oops, I haven't pushed it, let's try it again anyway, and I set it, and it deleted the alert as well, the associated alert. So anyway, I've reset it up, let me push the button. There we go, I just pushed it, and will it pop up?

**Dave Jones:** It should, because it's active, right? So it did last time. Yet No, nothing yet. Oh, come on. I'm obviously doing something stupid, right? It's got to be me, it's got to be a pebcac. Now I tried looking at the various tutorials and, well, the tutorial videos

**Dave Jones:** and stuff like that, and it basically stops at that main dashboard type screen. It doesn't go into the events and how to actually script those and things like that, but I'm into the device information screen here, and I think I've got it figured it out.

**Dave Jones:** Look down here, user switch number one. I've pressed it twice, and sure enough, it's like a counter thing. It's not, it doesn't seem to be, well that's the actual value, right? Let me press it again. I have to refresh here. But it should pop up as three, there it is.

**Dave Jones:** So when I, maybe that's the reason why that event thing is maybe caught up in a loop or something like that. That's the only thing I can think of here, if I go into events over here, because that number is no longer I thought it'd go from one when it's pushed

**Dave Jones:** to zero, back down to zero, but maybe it's not like that value there. So I don't know. Alright, now I just got switch two to work. I set up a second one, and I just pressed it, and sure enough, it did come up live.

**Dave Jones:** Let's see what happens if I press it again. Ah, goodness. Here we go. I've pressed it a second time. Will it actually come up with a second occurrence there? No, let me refresh it. Nah, now it's active. Now it's gone false again. What the hell?

**Dave Jones:** Yeah, okay, that's the event. So it's gotta be that number not going back to zero, because look, if comparison is true, then enter event, okay, until comparison is not true, I expect it to go back to zero when you release the switch. I've gotta be doing something dumb.

**Dave Jones:** Surely. But I don't know. I've had a look at the page, and I've looked at the FAQ, and I've had a look at a few things. This demo here, which doesn't show anything, only goes to the dashboard. I don't know. I think I'm gonna give up.

**Dave Jones:** Anyway, on the positive side here, look, I did actually get the email in my inbox. I did get one an hour ago, which was the original one, then I deleted that event and item, and then I created another one and I had Hello Dave, so it does actually work.

**Dave Jones:** It is sending the email, but buggered if I can figure out how to why it's not doing what, look, here we go. Something going on here, but why it's not doing what I expect, I've got no idea. Alright, on the positive side here, after

**Dave Jones:** installing two different drivers here, well manually two different ones, I finally got the Stellaris Virtual Serial Port. It didn't install first, it installed these ones first, and then had to install this separately. Anyway, there's a virtual serial port which hooks up to the code already running inside

**Dave Jones:** the launchpad. And here you go, I am connected, 115k board, and there you go, we can play that tic-tac-toe game. So tic-tac-toe! We're running. Play locally. Play online. There you go, so hopefully remote user starts, so I'm going to do that. And the remote user can start waiting for the remote player

**Dave Jones:** to see if it can access, presumably it's accessing the Exocyte server, and it's waiting. It's thinking. I don't know. So we can leave that off screen, and we can go in here and we can Oh, here we go. Something happened. Something happened to Bruce.

**Dave Jones:** No, it's still waiting for remote player. So anyway, that is supposed to pop up here, and oh no, there we go, that was me. There you go. I didn't put X in the center square. Oh no! Fail. And enter row, there we go.

**Dave Jones:** Okay. So yeah, I can go like 1 and then 1 and boom, it should wait in for the remote player. My one should pop up here, although I've got to manually refresh that. There we go, it popped up. So it works. So anyway, I think I need to

**Dave Jones:** play around with this thing a lot more and maybe try and find some tutorials to figure out, you know, exactly how all this online stuff works. I can actually see the power in this Exocyte stuff. There is quite a bit in here which really excites me in terms of, you know, being able

**Dave Jones:** to configure alerts and events and do stuff like that. And I would obviously have to install the tools, the TI tools, all the compilers and stuff like that to look at the source code to how easy that is to modify and then create your own application.

**Dave Jones:** Of course this is just an Internet of Things demo, but if you wanted your own application to be Internet connected, enabled, I'm sure it's a fair bit more work than this. But I do kind of see the value in a lot of the power in a lot of

**Dave Jones:** all this, but I've had a lot of issues, quite a few issues with this thing. And maybe it is a pebcac error with stupid me, but hey, you know, I'm trying to use this thing out of the box. I followed the quick start guide and I'm

**Dave Jones:** getting constant errors popping up and all sorts of things and just stuff, like just simple switch events not working as I'd expect them to. But the email alerts seem to work, that, you know, the remote tic-tac-toe game worked and all that sort of jazz.

**Dave Jones:** So I, yeah, I don't know. I'm probably going to call it quits here. This has probably been long enough. It'd take me another hour, a couple of hours to install the C compilers and everything else and look through the code and try and modify it and do

**Dave Jones:** all that sort of example. But hey, you know, it's worth having a play around yourself. I mean, for $20, it's only going to cost you $20 and your time to have a play around with this thing. So I don't know. It's not too bad, but yeah, I think there's probably a few

**Dave Jones:** I suspect there's a few bugs in here and the out of the box user experiences. It kind of worked, but then quite a few issues. So I don't know, take that what you will. That's a look at trying to get this Internet of Things $20

**Dave Jones:** Internet of Things launchpad working. I hope you found it moderately useful. It wasn't a tutorial by any stretch. It was just me using it straight out of the box and following the quick start guide. So you could probably expect a similar thing. Maybe you won't have the

**Dave Jones:** same hassles I will, but yeah, it does kind of work. Anyway, I hope you enjoyed it. If you want to discuss it, jump on over to the TV blog forum. Catch you next time. Whoa, hang on! One last thing. You know how I mentioned the ADC at the start of this?

**Dave Jones:** Well, let's have a look at the data sheet. Brief look. Look at this. Top left corner there, page 1861 of almost a 1900 page data sheet for this chip. Do you believe it? Anyway, it has a whole ADC section. I'm sure you can get a short form

**Dave Jones:** version of the data sheet, but this is the full thing. 1900 pages. That's FPGA-like data sheets. That's just madness. But such is the power and flexibility of these modern micros. They cover absolutely everything. But oh, jeez. Anyway, we've got all the data we could possibly need for the ADC

**Dave Jones:** down here by the looks of it. And let's have a look now. Look at the input leakage current there. 2 microamps maximum. Analog source resistance, 500 ohms. So there you go, that's quite high. You want to drive this with a low impedance source to

**Dave Jones:** minimize your errors, that's for sure. ADC conversion clock runs at 16 megahertz. 1 meg sample per second rate. They claim 2, I thought, as their top level spec there. So I'm not sure what's going on there, whether or not they're claiming the second

**Dave Jones:** channel or not. And maybe you could interleave them. But yeah, conversion time 1 microsecond. Sample time resolution 12 bits. Integral nonlinearity 3 least significant bits maximum. Differential nonlinearity. You know, it's an okay ADC for a 12-bitter. So it's probably doing offset error. There we go, there's your 15 least significant

**Dave Jones:** bits offset error there. Gain error, 30 least significant bits, there you go. So yeah, you know, it starts to get a bit ordinary. And there's your signal to noise ratio stuff. And you can go out and compare this with like a $5 or $10

**Dave Jones:** ADC, like a 12-bit ADC, a real proper one that's designed for performance and linearity and you know, no errors and everything else. So I recommend you go get, and look at all the traps for young players here, look at all these little footnotes here, you've got to look out.

**Dave Jones:** So you've got to read all these, two capacitors in parallel, blah, not valid here, blah blah blah, with signal common. Oh there you go, got to be careful, you've got to read all the fine print there. Nasty. Oh here we go, at 2 meg samples per

**Dave Jones:** second, there you go. So it looks like you can actually, they specify it at 1 meg sample and 2 meg sample, so you probably expect worse specs at 2 meg sample. There we go, 32 megahertz clock there. And yeah, okay. And no, similar.

**Dave Jones:** Similar specs, I think. So there you go. Anyway, I highly recommend you go in and compare that to a real ADC, in quote marks, and see the performance differences. Thank you.
