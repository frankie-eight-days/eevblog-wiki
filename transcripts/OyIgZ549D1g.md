---
video_id: OyIgZ549D1g
title: EEVblog #1137 - Mailbag Monday
url: https://www.youtube.com/watch?v=OyIgZ549D1g
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Mailbag Monday where every Monday I open up a bunch of packages sent in by my viewers to my PO Box. You never know what you're going to find. So, let's get to it and there's only one way to open packages here in

**Dave Jones:** Australia. Let's go. Thank you very much and sorry to unknown person. Um, this obviously came in a uh like a satchel or whatever um and it probably didn't have Mailbag written on it. So, if it doesn't have Mailbag

**Dave Jones:** written on it, I'm going to assume that it's something I've ordered so I'm just going to open it. So, I probably did open this one a while back and went ah that's obviously Mailbag and I didn't check it out. So, let's Oh, yes.

**Dave Jones:** Look at that. Cool. That was That's not the EEevlog logo. I kind of do have an official EEevlog logo. That's not the official one, but that was one of the submitted um ones when I did like the logo

**Dave Jones:** uh design. Well, it's just what's a logo? It's just the name in a font, you know. Um Anyway, oh, we have some It's like we have some sort of uh charger. It's Pearl. Pearl p i r l charger.

**Dave Jones:** Um What Oh, and a power brick with a funny ass Yankee uh plug on it. Absolutely useless, but um yeah, it looks like it's a it's a USB charger. 2.7 amps per port. Sweet. Let's check it out. So, this is the Pearl

**Dave Jones:** charger p i r l and I like the uh case. Look at this. It's got uh alloy top and bottom plates and then inside here is just made up with uh little individual They laser cut or uh routed. Are they PCBs or uh

**Dave Jones:** plastic like fiberglass or plastic? Kind of looks fiber Looks a bit fiber glassy to me. Anyway, there's a board down the bottom and No, no, it is different. No, they're just like uh some sort of, you know, Delrin plastic material or

**Dave Jones:** something like that. Anyway, it claims to be the world's um you know, most powerful, fastest like multi-port charger, 2.7 amps per port. That's genuine on each port delivered all at once. 50 watts total capability anywhere from 7 to I think 17 volts input. So,

**Dave Jones:** you can power it from like LiPo battery packs. You can power it from the supplied plug pack, which is a Meanwell. They're pretty decent. There you go, 15 volts, 4 amps, 50 watts max. So, we should be able to get the full

**Dave Jones:** capability out of this thing. Little LED for each one. Is that a multi-color? And supposedly like all sorts of, you know, ruggedized like, you know, full ESD protection on the ports and individual shutdown. So, if you short out one, it

**Dave Jones:** won't affect the others and all that sort of stuff. Anyway, strip it apart. Very rugged. I think you could run over that with the car, no wuckers.

**Dave Jones:** All right, let's get in there. There we go. That all came off. Oh, yeah. Look at that. So, I'm not sure what material that is. What do we got down there? That's to keep Oh, there are the light pipes, of course. They're the

**Dave Jones:** light pipes going up. That's kind of neat. I love how they've got the individual LEDs on this. None of this, you know, integrated seven segment rubbish. No, sorry, Bob. That's very nice, isn't it? Identical channel isolation. Big ass inductor there. So,

**Dave Jones:** this is all going to be switch mode control, of course. So, it looks like we have a micro up here. We'll have to get in with the part numbers. ICP port there. Looks like is that the USB um

**Dave Jones:** port chip? Oh, I didn't see a Oh, yeah. It It It has a button. It has a secret reset button. Secret squirrel reset button on the top. There you go. Rev 1.02 for those playing along at home. 11

**Dave Jones:** amps total like 5 volts 11 amps output. Sweet. 7 to 17 volts input. So, this looks like this is really nice design. Really liking this. Oops. Um that was me. That was me. I was trying to like separate this plastic bottom and I

**Dave Jones:** had my I obviously had my uh uh thumb on the poor socket here. Let me push that back. Oh, no. Oh, it's a Greek tragedy. Should be able to solder that back in, but obviously there's no front tabs on

**Dave Jones:** this. This is not as rugged as it could be, although of course it's sandwiched. It's sandwiched inside there. So, it's you know, it's not going to lift up. Didn't use this newfangled surface mount rubbish, you know, it had big

**Dave Jones:** through-hole tabs in there. Never would have happened. Also, therein lies the problem when you just like uh put solder paste on these and just reflow them on your pick and place machine. The solder you kind of sort of

**Dave Jones:** get a bit of fillet around the uh side like that, but you don't get it, you know, right over the top like that like you get if you hand solder it and that's going to be more robust. And of course

**Dave Jones:** the uh the pads this is like it's not just a pad and then a thermal relief off to the ground plane. It's actually got uh you know, it's right on the ground plane. So, that's solid. So, that's why

**Dave Jones:** we didn't rip the uh pad off, but the solder joint um certainly failed. And I could, you know, if I got my thumb in there, I could just, you know, lift this entire socket off. So, yeah, like it's not going to be a

**Dave Jones:** problem on the finished product. This is only if you take it apart like me and you dick around with it. Just don't do that. So, I am actually uh concerned about this is an original one. I haven't actually touched that. And

**Dave Jones:** yeah, while there are like, you know, quite reasonable fillets on there, of course it looks, you know, a bit Frosty the Snowman because of the fact that you're using lead-free solder, but um yeah, like all the force plugging in and out these sockets is

**Dave Jones:** going on those two pads, the large tabs at the back, plus those four pins. Yeah, I'm a bit concerned about the robustness of the sockets, these surface-mount sockets. So, here's our power input here. You'll note that we don't have one

**Dave Jones:** large DC-to-DC converter for the whole lot. Instead, what we've got is a little point of load jobby down here. It's a diode zinc and AP65543, and it's a 4-A buck converter. We've got the big-ass inductor for that here.

**Dave Jones:** We've got a some output filtering stuff like that. Not sure how tight tight that loop is in there. Anyway, and then we've got a Texas Instruments 3-A controller here. So, yeah, no wackers. Nice thick traces in there. Bloody black gloss black solder mask.

**Dave Jones:** Should be banned. Anyway, so each channel's absolutely identical. It's got a quality TI 3-A controller. It's 2.7-A rated per port this product. So, the chip's that's more than capable, and the little DC-to-DC converter's more than capable of well as well. They've got no heat

**Dave Jones:** sinking on there. That'd probably be like 90, you know, I do the efficiency curve. We'll have to have a look at the data sheet. I'll include that in if I can. Over the efficiency of that will change with voltage, of course. And

**Dave Jones:** we've got a little ATtiny up there, do we? Just driving our little LED display. So, where's our load measurement being done? Is that little uh instrumentation amp? That No, there it is. There it is. Over there. There's our

**Dave Jones:** shunt resistor. That's measuring the total power. So, they're doing that on the input side. So, that's that looks like the total power displayed here is actually the total power including the efficiency of the DC to DC converter. So, that's

**Dave Jones:** basically our consumption from here. It's not what's actually being delivered, I would presume. Cuz the only way to measure the power output would to be have a uh shunt resistor over here, current shunt, and then measure the power on each

**Dave Jones:** individual port like that and then add them up in software and give the total. But, they're getting like near enough. Maybe they're like in software just uh subtracting a nominal amount for the efficiency of the converter, you know,

**Dave Jones:** under like 10% or 8% or something like that, 5%. All right, let's power this sucker up. Found one of those weird ass Yankee adapters. Hey, hello. 0 0. It doesn't look very good unless you diffuse it. Oh, 0.5.

**Dave Jones:** Five? 0.5 W, there you go. So, it is actually the input. They haven't bothered to subtract the quiescent supply there. Surprised they're using white. Hmm, doesn't look It's not that terrific. I'm not, you know, really keen on the implementation there. So, it's

**Dave Jones:** charging, but like it's only charging at one like 1.2 W. Like absolutely hopeless. And then the LED's not even coming on. Look at like it comes on initially when I plug it in, or it did before. So much for the world's fastest

**Dave Jones:** charger. Yeah, sure, everyone got one of these stupid Apple phones, but like come on. Let's see if it heats our TS80 soldering iron, shall we? It's not so yet. Low volt, forget it. Oh, but look, at least it comes with a

**Dave Jones:** sticky gel pad. Stick it on the bottom so it doesn't flap around the breeze. But, apparently you can just wash these and re-stick. So, it's kind of handy to like, you know, stick it under your bench or, you know, mount it vertically

**Dave Jones:** like that on a surface or or something like that. Might support every other bloody charging format, doesn't support quick charge though. All right, let's turn it on. We are at uh I think it specifies 5.05 V on the output or something like that.

**Dave Jones:** Uh so, you know, pretty close, near enough. Um let's put a 1 amp load on this thing and see what we get. Yep, 1 amp, no worries. But, look at this, the voltage has jumped up. 5.19 V. Um

**Dave Jones:** uh Beulah, that's outside the spec. Um like, what's going on? Regulation sucks. So, let's actually wind the wick up on this thing and watch that voltage change as we voltage increases as we increase the current. 1.3 Wow, I'm not sure if this is actually

**Dave Jones:** negotiating the current. I think it uh I think it does. Whoop, fan's coming on. But, um Hey, 2. Let's go all the way with LBJ. Let's go to 2.7 amps, can we? Can we? Now it's dropping back down, so it looks

**Dave Jones:** like it has a like a rise and then it comes back to its nominal voltage at 2.7. Is it going to Where's it going to crap itself? Let's have a look. Hey, there we go. No worries. Whoop, and it just

**Dave Jones:** automatically uh restarted itself. I didn't uh turn that off. Oh, there we go. Yep, there's our there's our overload. Got a red light on there. Looks like it's not going to come back on on its own. Now, hey, this is

**Dave Jones:** interesting. Look. 5 W, 7 W. What? What is it What's going on? As for accuracy there, we're down at uh yeah, pretty close to bang on 5 W there. We're getting 5.1 up here. So, that's all right. So, it does look

**Dave Jones:** like it is uh compensating cuz it shows a half when you disconnect this thing, so yeah. Jesus, fly to the moon on half a watt. So, yeah, for me, um this is like not a like it's okay. Um yeah, we're getting

**Dave Jones:** our 2.7 We can get our 2.7 amps per port, but it doesn't support quick charge, which is uh useless for me for my mobile phone. So, you know, your mileage may vary, of course. I don't know. It's probably okay. The robustness of

**Dave Jones:** those USB ports needs to be uh beefed up, I think, cuz I reckon if we, you know, if we really bang this thing in and out, that could be putting some heavy-duty stress on those solder joints. And I think it's

**Dave Jones:** all going to be mostly Does it have little plastic um uh pins on the bottom that go into the board? But, yeah, I don't know. It's okay, but it's not what I was hoping for. Thank you very much, Nick Vassal, from

**Dave Jones:** uh Bridgeport in CT. Is that Connecticut? I think it is. Thank you very much. We uh it sounds innocent enough what this is, but you never know. You're like in the big mailbag. What are we going to get? Uh we've got

**Dave Jones:** the I keep forgetting the name of this stuff, this crinkly Digikey stuff, but hang on. Oh, jeez, that smells that smells vintage.

**Dave Jones:** Or is it No, it smell It can't be It's not the product. The smell's coming from the packaging. No, this is not vintage, so I can just tell. Oh, sweet. Vacuum fluorescent dot matrix. Oh. Thing of beauty is a joy forever. So,

**Dave Jones:** these displays are very cool. They're IEE tron uh displays made in Japan. All the best stuff's made in Japan. And they're designed to be uh you know, standard uh Hitachi LCD interface here, but they're uh dot matrix VFDs or vacuum

**Dave Jones:** fluorescent displays like this. Fantastic. So, we've got the 40 by 32 one, and then we got your more standard one which you might be familiar with, your 16 character by two line displays. So, they're supposed to be like fully interface compatible.

**Dave Jones:** Unfortunately, I have uh try I've sucked out like the wire interface which came with this, put on the pin headers there, and I cannot get the thing to work, unfortunately. Um this one is actually drawing 212 milliamps there. So, it's drawing about

**Dave Jones:** a watt doing nothing. So, they do, you know, they take a lot more than a standard LCD, which is only, you know, a few milliamps, something like that. Oh, no, we got one. We actually got it. Check it out, there it is. Let me switch

**Dave Jones:** off the studio lights, it might look a bit better. It what It wasn't working before. Anyway, we've got some garbled characters. Let me see if I can press reset down here. No, unfortunately, it's not working which works with the LCD,

**Dave Jones:** but as you can see, yeah, it does work. So, maybe I do need to uh you know, maybe I do need to tweak the code or something like that, probably tweak the initialization routine or whatever it is. Um

**Dave Jones:** but yeah, so not fully in this particular case, I didn't write the software for this little board. It's a former mail bag. It's a little geocaching thing I've just hacked it into Normally, it powers the 5 volts from these

**Dave Jones:** AAA's here, but of course, it doesn't give enough and nope, she's not working, but at least we got something there. So, it might be some initialization routine is different or something like that. But anyway, they're very cool vacuum fluorescent displays.

**Dave Jones:** Fantastic. And basically, a drop-in replacement for your standard LCD. So, if you've got a project and you want it to look a little bit funkier than a standard LCD, albeit at a like orders of magnitude increased current, this fact I turn vacuum

**Dave Jones:** fluorescent very cool. But, if you want to see a video of me hacking around with a vacuum fluorescent display, I highly recommend this one which I'll link in at the end where I actually reverse engineer and hack and get working this

**Dave Jones:** once again a mailbag vacuum fluorescent display just driving it with an Arduino compatible board. So, I'll link that one in. It's very interesting. It's had like a couple of hundred thousand views, I think. Very popular video. Check it out.

**Dave Jones:** So, I won't go to the effort in this mailbag to get these ones working. It's just, you know, more of the same and it's just like a probably just a command thing. Anyway, cool. Thanks. Thank you very much Dr. Ralph Huber from

**Dave Jones:** Wezel in Germany. Weasel? Wezel? In Germany. Hi to all my German viewers. Um contains one electronic device. Not plural, just one. Let's find out what the electronic device is. You never know you're lucky on the big mailbag. Dead. Wrapped in

**Dave Jones:** plastic. Getting there. Oh-ho, this could be fun. Let's check it out. So, thank you very much Ralph. This is the Octopus Curve Tracer. Um it's very simple. We've just got a op amp here. We've just got a some batteries on

**Dave Jones:** the top. This is actually a dual in-cell holder. So, normally for a 1.5 V battery, but I've actually got uh the provided the 12 V batteries fit in here. They're a little bit loosey-goosey, but anyway, that generates our plus minus 12

**Dave Jones:** V rail for our op amp. We've got a function generator input and of course a curve tracer used to be something that was often found on old analog scopes. You know, like 20 meg entry-level analog scopes. A lot of them

**Dave Jones:** had the curve tracer building which allows you to actually measure the parameters of components using the XY mode of the oscilloscope. And it's basically just a function generator through a series shunt resistor and you're basically just measuring the voltage across a shunt

**Dave Jones:** resistor that looks like it down there and you can actually determine on the XY mode of your oscilloscope various parameters of an oscilloscope. So let's see if we can get it working. Unfortunately, we have a look at the

**Dave Jones:** note, there's a few little issues with this design though. So I won't read you the whole lot. You can pause that and you can read for yourself. But anyway, it's basically a the standard result of a function generator. If you get like an

**Dave Jones:** ellipse like a circle on the screen for example, then it's a capacitor or inductor and L-shaped curve you've got a diode, a straight line like it's depend on the value of the slope, you get a resistor, vertical lines a short

**Dave Jones:** circuit and or a horizontal line is basically open circuit. And of course nowadays few oscilloscopes are equipped with a component tester. Many have a wave gen option. So that's the idea of this thing. And of course as he said, this is

**Dave Jones:** nothing new. He's not the first to invent this but there's various problems with it. The 50 amp output of a function generator, yep, it's it's too high a output impedance to drive, you know, various components. So hence why

**Dave Jones:** we've got the op amp on there just to drive it with some low impedance. Anyway, the other problem is that the oscilloscope probes are mains earth reference. So you need a differential probe to do it. And of course an

**Dave Jones:** oscilloscope, you can actually use two channels in subtract mode which then becomes a differential, you know, a poor man's differential probe. It's pretty good for lots of cases and stuff like that. Unfortunately, you can't combine, as far as I'm aware, I don't know of any

**Dave Jones:** scope where you can combine XY mode, like even with a four channel scope, XY mode and have the X be the X channel be the subtraction of the two channels. So, differential probe, differential probe, XY. They're all mains earth reference as

**Dave Jones:** far as I know anyway. Hmm, could be wrong. All right, so what I've done is hooked up a differential probe here. Unfortunately, this is like a high voltage differential probe not optimized for low voltage stuff. So, it's times 10

**Dave Jones:** attenuation but then again, using a times 10 scope probe as well. Anyway, it'll do the business and so I've got the differential probe across the component under test which is these two leads here. And then the scope channel goes

**Dave Jones:** across from ground which is the Y terminal across the little tiny current uh shunt resistor in there. Don't know what value that is, you know, probably like a you know, 10 ohms, 100 ohms, something like that. And tada, we're

**Dave Jones:** measuring a capacitor just 100 and capacitor and we get ourselves a circle. Of course, I'm using the function generator just generating the 1 kilohertz signal. So, the good thing about this is that you can actually test component at the frequency you want. So,

**Dave Jones:** you could actually, you know, go up to you know, 20 megahertz here if you really wanted to. You know, you could go all the way with LBJ and things are going to whoop. Whoop, there we go. So, we still have our circle but now

**Dave Jones:** we're starting to distort. Look at that. Because I think our amplitude we'll probably find our amplitude is Yep. Once you get to a certain point, your amplitude becomes too much and you're going to saturate like that. You're not going to get your circle

**Dave Jones:** anymore. So, little trap for young players but anyway, a capacitor will give a circle and and if we change out a capacitor, there's our open circuit. So, we get our horizontal line. And if we clip our resistor on there, get a

**Dave Jones:** sloping line like that and that's exactly what we get. So, it's a resistor because they're linear And what do we get? A linear line. Oh. And of course, if we go to a non-linear component, doesn't get any more non-linear than a

**Dave Jones:** diode. Or does it? Which is the most non-linear component? Anyway, there we go. We get our traditional um Whoop. There we go. We get our traditional L shape. So, uh there you I won't go into all the details of uh component testers,

**Dave Jones:** but yeah, like a real simple do-it-yourself component tester you can make it uh yourself, you know, there's no need to I don't even know if he hasn't linked in. Don't even know if he sells a uh kit or whatnot, but it's

**Dave Jones:** basically just a uh low impedance uh function gen uh output just knob out there. You can do it without it, but it's just not as uh sensitive, but anyway, can can convert your um scope into a component tester. Neat. Anyway, if you do know of

**Dave Jones:** an oscilloscope that actually does allow that like a four you need a four-channel one that allows you to actually do XY mode with the subtraction of 1 - 2 and uh 3 - 4, let us know in the comments, cuz that'd

**Dave Jones:** be awesome. I Offhand, I don't know if there's one that does it. And in theory, it should be able to do it with these newfangled digital scopes, because it's it's just really essentially just a software function. What the heck? We'll just open up a

**Dave Jones:** couple of bonus um China eBay ones. A lot of people just buy just random like $2 stuff delivered on eBay. Uh Australian Capital Territory 2153. It's a phone accessory. Spoiler alert. Um Let's have a look. This could be bad.

**Dave Jones:** What do we got? What? What is that? What is that? What is that? I I don't know what that is. It's like a That's a like a mobile phone like cover or something. I don't And like, you know, like a

**Dave Jones:** There's that like that lens. That's the lens for the like the LED that lights up. That's the aperture. You know, that's the cutout for the camera that goes in there. It's like it's a phone. Um have I Why would somebody send me this? I don't

**Dave Jones:** know. A new phone adapter thing. I don't get it. Okay. Um plastic toy gift. Doesn't get much better than Australian Capital Territory. Again, from the same mob. So, they couldn't send it in the same packet. And this is like, you know,

**Dave Jones:** a dollar delivered. Plastic toy gift. What do we got? Not condoms. A finger condom. Just what I always wanted. Thank you very much. Medical level. Oh, yeah, you got to trust the medical level finger condom. All right. Let's have a look.

**Dave Jones:** Ta-da! Sealed for our protection. Oh, yeah. Yeah. Oh, got to ah, greasy as. Mm. Yeah. Well, you might as well go all the way with LBJ. You can't be too sure these days. Catch you next time. Ooh, peppermint flavored.

**Dave Jones:** Hope you enjoyed mailbag Monday. If you did, please give it a big thumbs up cuz that always helps a lot. And you can subscribe by clicking down here. Make sure you also click on the bell notification icon so that YouTube

**Dave Jones:** actually notifies you of new videos. Speaking of which, videos you can watch over here and over here. Just random ones. Maybe another mailbag. Who knows? It's a lucky dip. As always, you can leave comments down below or on the EV

**Dave Jones:** blog forum, which is much better place to discuss them. I try and read and respond to comments where possible, particularly in the hours after I release a video. And as always you can support me down below on Patreon, PayPal donations,

**Dave Jones:** crypto, merch, products, all that sort of crap I'm shilling, you know, whatever. Hope you enjoyed it. Catch you next time.
