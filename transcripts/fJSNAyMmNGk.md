---
video_id: fJSNAyMmNGk
title: EEVblog #515 - Battery Ionic Resistance Investigation
url: https://www.youtube.com/watch?v=fJSNAyMmNGk
source: youtube-asr
---

**Dave Jones:** Hi, a little while ago I did a review of this Agilent 34461A multimeter and as a part of the review I was playing around with a 9 V battery like this and I made note of the fact that the reading was dropping like that

**Dave Jones:** and that was due to the 10 meg input impedance of the multimeter and somebody in the comments, sorry I forgot who it is, mentioned that oh no that's that was me holding the battery. That was my uh you know the heat from my hand holding

**Dave Jones:** the battery that was causing the voltage to drop. Well, no that's not the case. It is actually the input impedance of the multimeter. So I thought we'd actually take a quick look at this and just have a little play around with some

**Dave Jones:** basic um uh multimeter loading on various batteries like this. Now because this multimeter is 6 and 1/2 digits we've got for a 9 V battery here we've got 10 microvolts resolution here which is excellent and we can actually get greater resolution

**Dave Jones:** than that as I showed in the review by using the data logging and trend plot function as well. And you can see it dropping now. Now this multimeter like many um good high end bench multimeters and also handheld ones at all it's got two

**Dave Jones:** different types of input impedance. It's got 10 meg standard as your regular digital multimeter will have 10 meg input impedance and that's what we're loading down on this 9 V alkaline battery at the moment but it's also got

**Dave Jones:** a high impedance mode here or high Z. It says auto but what it's jumping to is actually high Z. You can see that on the display there. You'll notice that the voltage is now jumping back up because there's much less load on there. In the

**Dave Jones:** case of this particular multimeter the data sheet just says it's greater than 10 gigohms. So there's a huge difference there and but this should be enough to let us just play around with a couple of batteries here and note some interesting things.

**Dave Jones:** So, let's take a look at it. Now, as you may know a brand new alkaline cell or alkaline manganese dioxide is the typical chemistry used in these most alkaline batteries these days then the open circuit cell voltage can

**Dave Jones:** effectively vary from anywhere from the nominal 1.5 volts per cell or 9 volts in the case of this 9 volt battery which has six 4A cells effectively inside it. If you open up one of these, you'll find six physical 4A size

**Dave Jones:** alkaline cells in there. But, that can vary from 1.5 volts per cell up to about 1.65 volts per cell or for a 9 volt battery up to 9.9 volts open terminal voltage and this large variation is due to the

**Dave Jones:** electrochemistry inside the cell and the purity of the chemicals in there and the materials and oxide layers and layers that form on the plates and you know all sorts of stuff like that. So, it does vary a fair

**Dave Jones:** bit and that will come into play when we try and measure the internal resistance of a battery like this just using the load on our multimeter here. Now, if you have a look at the data sheet for a typical

**Dave Jones:** Duracell alkaline manganese dioxide battery, i.e. your typical alkaline battery, they're pretty much all the same. The brands really there is not going to be a huge amount of difference. All the typical values are all going to be same. Now, the Duracell one happens

**Dave Jones:** to tell you the internal impedance of this thing. There it is, 1,700 milliohms or 1.7 ohms. Now, that value of the internal impedance is actually a consistent across the life of the battery. It really doesn't change much at all and that's the basic electrical

**Dave Jones:** uh contact resistance inside the cell itself. Now, this is really a key point because it's specified at 1 kHz here. And the reason it's specified at 1 kHz is because uh it doesn't include what's called the ionic resistance or the

**Dave Jones:** electrochemistry effects as you'll as I often uh call it inside the cell. So, that's why if you really want to measure the internal impedance of the battery, the internal ES as some people call it the ESR, then you have to do it very

**Dave Jones:** quickly at a rate around about 1 kHz or thereabouts. It can be a bit slower than that, but it can't be in the order of seconds. So, it's not like you can hook up your battery and then a couple of

**Dave Jones:** seconds later take a measurement and then, you know, do your Ohm's law calculations and see if you can calculate that 1.7 ohms because you won't get it because over the longer term period of, you know, hundreds of milliseconds to seconds to minutes to

**Dave Jones:** hours, it's the ionic resistance or the electrochemistry effects inside the battery that dominate. So, that internal impedance is only valid at those very short time periods there. Now, that warrants a separate video in its own right, how to actually measure and

**Dave Jones:** confirm that internal impedance. We won't be able to do that here today cuz as I said, you've got to do it very quickly. You usually have to set a stable It's usually done with a a pulse um load where you set a stabilizing

**Dave Jones:** pulse and then you drop the load right down and then you measure it straight away and then you take it back up really quickly at near that 1 kHz rate. But if we have a look at the uh typical

**Dave Jones:** discharge characteristics of this cell, it's not that 1.7 ohms that value of the ESR that's increasing under load that's causing the discharge of this cell. It's mostly the ionic resistance at play here over these long time periods. And you'll

**Dave Jones:** notice that it actually starts at very high and then ramps down very quickly. It's not very noticeable on this one. But if we jump over to an Energizer data sheet, once again for the same 9-V battery, you can actually see

**Dave Jones:** down here where for it's This one's, you know, not a particularly high uh load and it is pulsed. And in in this case, it's at 10K / 620 ohms 1 second uh pulse per hour. So, you know, a

**Dave Jones:** fairly light light fairly light pulse load. You can really see the rapid drop in the value here. And that's the electrochemistry or ionic resistance coming into play. And not only does it uh come into play over days, like we've got here, you're also um and

**Dave Jones:** at fairly high loads, this also has a similar drastic drop effect, as we'll see in a minute, over very short time periods in in terms of seconds. And under some and under some unusual scenarios, which we'll also show in a second. So, we'll get a very

**Dave Jones:** We should be able to get a very similar drastic drop like this, but over very short time period. So, it'll be a similar sort of uh graph to this one. So, just remember that 1.7 ohm value and how it will

**Dave Jones:** basically be unmeasurable in the stuff we're going to do today. It won't have an effect at all. Yet, you will still see the voltage drop on the battery, very similar to this sort of thing, because it's not the

**Dave Jones:** internal impedance at play. So, that is why if we set our multimeter to 10 meg input impedance like that, we're going to get a fairly dramatic drop like that in in in the in initial drop anyway of the

**Dave Jones:** voltage of the cell. Now, it will actually start out and drop exactly like we saw on the Energizer graph there. Start out very high, drop dramatically, and then sort of taper out and sort of stay steady. So, if we leave that there

**Dave Jones:** long enough, we will actually see that that stay that value will eventually stabilize. Now, with a 9-V battery and a 10-megohm impedance on our multimeter here, we're only talking 900 nA. And of course, 900 nA * 1.7 ohms

**Dave Jones:** internal resistance, we're only talking about 1.5 microvolts. So, really, you can't even see 1.5 microvolts on here. It's the next digit over effectively. So, you know, really, we're just being swamped by the electrochemical effects here. So, we can't actually see

**Dave Jones:** our internal resistance of our battery just based on the very light load from this multimeter. But, let's have a little play around with this because we can. Let's go into a high impedance mode or 10 gigohms, and let's go into the

**Dave Jones:** display and go into the trend chart here. So, what I'm going to do is I'm in the 10 gigohm high Z state. So, we're only talking with 10 gig 900 picoamps across a 9-V battery. So, there's effectively no load at all. And if you

**Dave Jones:** multiply that by the internal resistance, you know, we're down at 1.5 nanovolts. Absolutely tiny. But, anyway, let's hook that up, and then we're in our trend chart mode. So, let's actually reset our readings on our trend chart here, and

**Dave Jones:** see what we get. So there we go. I've auto scaled that and as you can see it's sort of, you know, it is pretty flat because it's had time to stabilize from that dramatic 10 megaohm load by the way. So what what

**Dave Jones:** we're going to do now is we're actually going to turn on our 10 meg load and of course if you're just talking about the internal resistance of that battery as I said here's our voltage here. Now we would expect it if it's

**Dave Jones:** just based on the internal resistance or the nominal internal resistance. So 1.7 ohms once we put that 10 meg on there if it's just due to the internal resistance of the battery then we'd expect the value here which you can see the numeric

**Dave Jones:** result to only drop by 1.5 microvolts. So we shouldn't expect to see any drop on there at at all. But let's do it. Let's switch it on. 10 meg and bam, look at that. It's dropped right off the scale. So much so

**Dave Jones:** that we have to go back in here and auto scale that again and you can see it drop down fairly dramatically. Now it's fairly well stabilized there now. You know, there's a still a bit more to go but let's

**Dave Jones:** turn it back and we'll watch it jump back up. There it goes. Look at that. And it should curve back up to our original terminal voltage up there. So we've got some funky very low load, incredibly light load electrochemistry

**Dave Jones:** effects happening within the battery there. Now the original commenter said that that drop of course had to do with the temperature of my hand in the battery and and that actually has nothing to do with it at all. It's

**Dave Jones:** demonstrated that it was actually the load doing that, but let's clear this. Okay, I'm back to 10 meg input impedance here. Now, sorry, I'll get back to displaying recent data. There we go. That's better. There we go. And watch what happens though. This is

**Dave Jones:** quite fascinating. Okay, watch what happens if I squeeze this battery. Woohoo! Look at that. Let's auto scale that again. Squeeze again. Look at that. It's jumping all over the shop. Just squeezing it. It's electrochemistry effects once again causing that to

**Dave Jones:** happen. And if we switch back In in this case, it's a physical It's some physical process inside that battery. Let's go back. Auto scale it again.

**Dave Jones:** And here's where we have to let it settle and stuff like that. So, this is with a 10 meg load. Let's give that a little squeeze. Look at that. There we go. And it's still doing it. And it's no

**Dave Jones:** It's not the leads or anything like that. I mean, you know, I can move this around here and, you know, it's it's not the contacts. I can sort of, you know, I I mean, if I really play around with it,

**Dave Jones:** we might be able to get some something to do with the contacts, but that is physically me squeezing that battery. Or if I put it down like that, here we go. Let's auto scale again. There we go. Look at that.

**Dave Jones:** Fascinating. And we can put it side on like that. Bingo, it does exactly the same thing. And that that is effectively changes in the ionic resistance of that battery due to physical pressure. That was an absolute ripper. Look at that. we got a really we got a

**Dave Jones:** negative uh going pulse there. So that is absolutely fascinating and it takes time to recover because it's the chemical ionic processes within the battery that are actually doing that and I'm sure you could do a a whole PhD

**Dave Jones:** thesis on examining exactly what you know is going on in various cells of different chemistry in terms of pressure, temperature and discharge current and initial loading discharge and all sorts of you know all sorts of stuff but I find that

**Dave Jones:** absolutely fascinating and I've been playing around with this battery quite a bit. So what I'm going to do is actually just that repeat that with a brand new Duracell. So let's whip this one out of the packet and

**Dave Jones:** give it a go. Here we go. Let's put it on. Never been loaded. All right, clear readings and auto scale. There we go. It's dropping down. We've got the yeah, we got the 10 got the 10 meg load on. Oops, let's let's put the

**Dave Jones:** auto on. There we go. So we've got our 10 gig impedance and that recovered fairly quickly there. But you can see that even with a 10 gig load or greater than 10 gig the data sheet doesn't actually tell you the

**Dave Jones:** exact value of it but let's assume it's just 10 gig. That's still only 900 picoamps load on that thing and we can still see the discharge curve of that. Absolutely incredible. There we go. Look at that. That'll take

**Dave Jones:** quite some time to stabilize. And let's see if the Duracell has that uh same effect where we can apply pressure to it. And whoop, yeah, I saw a little little blip in there.

**Dave Jones:** Wait, yep, there we go. Look at that. But it's a different Looks like it's a different effect to our Varta battery.

**Dave Jones:** Check that out. I've actually effectively changed the slope of the discharge of that cell just by Oh, that battery, sorry. It's not a cell. It contains six cells. Just by squeezing that. Absolutely fascinating. And you can see it's starting to recover

**Dave Jones:** there in terms of uh slope. But let's uh actually switch on our 10 meg load now and see what we get.

**Dave Jones:** There we go. We're dropping about 10 microvolts there per second or thereabouts. But uh that one didn't show a dramatic as dramatic effect um with the 10 meg load as the Varta battery did with its I I don't know the uh history

**Dave Jones:** of this uh Varta battery, by the way. It just uh came out of my drawer. I may have used it once or twice in something. And can we see the same effect with a double A? Well, I've got a Varta uh long

**Dave Jones:** life double A battery here um brand new uh straight out of the packet, unused. And let's take a look. I've got it in the high impedance mode at the moment. And uh there you go. It's fairly flat. It's fairly stabilized. And we can go

**Dave Jones:** back and we can auto scale that, of course. Uh sometimes it doesn't auto scale to the center. But anyway, we should be able to see if there's any uh pressure effects in this one, too. So, let's It's sort of harder to put a bit

**Dave Jones:** pressure on a double A, but you can see that it Yeah, look at that. It's It's auto scale Ah. Auto scale that. Check it out. We did get a drop there. Will it recover? I don't know. We'd need

**Dave Jones:** some time to actually find that out. And I've left it for just over 20 minutes here, and you can see that it didn't recover at all. There's that little period there where we where we actually pressed the thing, stepped down, and it

**Dave Jones:** looks like I permanently hurt the poor little bugger, and it never recovered at all. Permanently dropped its voltage, and you can see that there is a ramp down, very slow little slope there, drop in voltage over that time. Now, whether

**Dave Jones:** or not that's due to the trauma, I guess, of actually pressing that cell, or whether or not it's the very gentle, once again, still high impedance load on this thing or not, I don't exactly know. But, anyway, it's interesting. And once again, if

**Dave Jones:** you're wondering, no, it doesn't really have anything to do with the contacts. I've just got my alligator clips hooked on here, and you know, I can play around with this thing, and and give it a bit bit of a uh

**Dave Jones:** bit of a go there, and really Look at that. Maybe a little slight something happening there, but it's not the contacts going dodgy or anything like that, especially at these incredibly low loads. And you can actually see the recovery of the double

**Dave Jones:** A Varta cell there when it went down to 10 megaohm load, and then I set it back to high impedance mode, and it ramped up over the span of about 30 minutes, right back to the original value up there. And

**Dave Jones:** you can see with the double A battery here how we dropped down to I was playing around with it down to 10 megaohms load there. Then I switched it back to high impedance, and look at the total time, 30 basically 30 minutes

**Dave Jones:** there to slowly ramp back up right up back to the original value there. That shows you how slow changing the this, you know, ionic electrochemistry is inside these cells. A really quite a slow process. And look at the values

**Dave Jones:** we're talking about here. We're barely talking about uh 100 microvolts there total change. Fourth decimal place stuff. I mean, really small values. But, 6 and 1/2 digit meter like this with the actual actually, it's more than 6 and 1/2

**Dave Jones:** digits when you're in this uh trend chart mode can really show you these differences. One of the benefits of one of these really uh high-resolution digital multimeters. And here's a brand new with Duracell double A fresh out of

**Dave Jones:** the pack. Uh long expiry date, and I haven't loaded it with 10 megaohms. It's on the 10 gigaohm thing. So, this thing has never been loaded out of the box, and you can see it dropping down, you know, at fairly consistently like that

**Dave Jones:** until it'll get to a point where it's going to stabilize fairly well. And that is even for that incredibly light 10 gigaohm load. Absolutely incredible. And check that out. After 6 minutes, there's our initial drop we saw before, and I

**Dave Jones:** thought it was flattening out, but now it's sort of recovering a bit. And there you have it. It's practically recovered covered to exactly where it was straight factory fresh there. So, that initial dip was due to the 10 gigaohm load on

**Dave Jones:** there. Slowly recovered. Well, let's see what happens if we uh give this thing a little pressure test.

**Dave Jones:** No, hardly anything at all on that fresh Duracell. No, not that we No. There we go. Got a little something there, but not much at all. And just for kicks, we'll go back to the 9-V battery, but this time Energizer, fresh out of

**Dave Jones:** the pack. Let's give it a go. Here we go. 10-GΩ load, so never been loaded, fresh out of the pack. Clear that, and we will auto scale. And bingo. There we go. We get that initial drop again every time. And

**Dave Jones:** that's over 14 minutes there, and you can see that we haven't had any recovery at all, but we have had a change in slope. I mean, you can see the big large slope there, and then it flattens out a bit, and then we've got sort of

**Dave Jones:** another slope down in here. So, it's gradually taping off, but that's after almost 15 minutes. Now, can we actually get a pressure change in that? Well, let's give it a go.

**Dave Jones:** No, I'm going to have to switch out of the recent mode. Yeah, there we go. We've We've got it to change. Auto scale. Yeah, there we go. We changed the slope, but once again, going downwards, just like the Duracell one, and opposite

**Dave Jones:** to what we saw in the Varta battery. And there we go. It's starting to level back out. So, let's give that a squeeze again.

**Dave Jones:** Yep. There we go. Pressure effects once again. And let's see what happens if we switch to 10-MΩ mode. There we go. 10-MΩ, and once again, we we don't get a huge drop at all. So, that brand new Energizer out

**Dave Jones:** of the packet effectively shows very little difference at all there, uh, between the 10-MΩ gigabyte and the 10-GΩ impedance. That's purely because it's totally fresh. So, that Varta battery we were playing with with at the start, obviously had a little bit of use in it

**Dave Jones:** and wasn't, you know, directly factory fresh like this Energizer one or the Duracell. And just for more kicks, we have a Coles brand battery. I have no idea who actually manufactures this one, but we'll give this a go. Check out that

**Dave Jones:** one. We got a sudden drastic drop there and that wasn't me touching this thing at all. That Oh, look. Look Look at that. Look at that. Isn't that unusual? What's going on there? That is really really weird. Wow.

**Dave Jones:** Look at that. Let's turn on Well, look. See, another drop. I swear I'm not touching that. I am not touching that at all. I won't even breathe on it. Very interesting. Let's see what happens if we switch our 10-megaohm load on there.

**Dave Jones:** Oh, wow. Look at this. This fresh Coles battery, straight out of the packet, we've got ourselves a big drop like we got on the Varta one. So, maybe that Varta one wasn't used. Maybe it's just the physical construction is different

**Dave Jones:** and the chemistry is Well, yeah. Well, the chemistry is technically the same, but there we go. Yeah, we got the same thing we see in the Varta battery. So, there you go. There It's not a Varta battery, this one I know, cuz this one's

**Dave Jones:** made, according to the packet, in South Korea. And yep, and the Varta one is made in Germany. So, there you go. But, basically exactly the same thing that we saw in the Varta battery. So, that Varta Varta battery, um I was fairly sure knew

**Dave Jones:** that fairly sure that hadn't really been used, maybe for, you know, 5 minutes in something very light or something at best, but it looks like this is Coles one has confirmed that effectively Duracell and the Energizer ones are almost identical in terms of

**Dave Jones:** their response. Um but this one is very similar to the Varta, almost identical. So let's see if that should recover now if we turn that load back. Uh yep. Yeah, it works exactly the same as the Varta. Look at that.

**Dave Jones:** So I reckon that Varta one was actually brand new. And this one has confirmed it. So that was well worth doing, that Coles one. That was very, very interesting. Now let's see what happens if we do the squeeze test. We're Actually, I won't

**Dave Jones:** touch that. We're probably better off clearing that, actually, starting a fresh there. And I'll just turn it off there. So auto scale. And let's not wait. Come on. I can't wait. Let's give that a little press. Yep, goes up just like the Varta one.

**Dave Jones:** Confirmed. Two different types. We've discovered two different types of alkaline construction 9-V batteries. Wow. That is fascinating. As a Yeah, as squeeze again. It's done exactly the same thing. Woohoo! This is great. I love playing around with stuff like

**Dave Jones:** this. So there you go. I hope you found that interesting and you learned something there. And of course this isn't, you know, a scientific test. This was just a little quick uh throw-it-together to show you that Well, to show the original YouTube commenter

**Dave Jones:** that I had nothing to do with the temperature of my hand. It was actually the load, even the incredibly light load of the multimeter combined with the electrochemistry and the ionic resistance in the battery that was causing those drops, but we also played

**Dave Jones:** around with the fact that these things are pressure sensitive. If you like that video, please give it a big thumbs up on YouTube cuz that always helps a lot. And if you want to discuss it, jump on over

**Dave Jones:** to the EV blog forum. That's the best place to do it. Although, you can always leave comments in YouTube as well. And if there's enough interest, maybe I might follow this up with some more testing. But if you've got a high

**Dave Jones:** resolution multimeter like this, have a play around with this cuz this sort of stuff is absolutely fascinating. It would be interesting to see what results we can get if we do some more scientific, you know, more methodical testing on

**Dave Jones:** these things. But there you go. Catch you next time.
