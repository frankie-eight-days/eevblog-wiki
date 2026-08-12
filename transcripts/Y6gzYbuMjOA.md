---
video_id: Y6gzYbuMjOA
title: EEVblog #1355 - NEW Siglent SDS1104X-U $399 4CH Oscilloscope Teardown
url: https://www.youtube.com/watch?v=Y6gzYbuMjOA
source: youtube-asr
---

**Dave Jones:** Hi, we've got a brand spanking new low-cost Siglent oscilloscope. Yes, lower cost and then the previous one, the 1104 XE we've looked at. This is the 1104 XU. Yes, not to be confused with the previous 1104 XE and not to

**Dave Jones:** be confused with all the other models in the 1000 series. We're talking the 1000 X and X plus, the 1000 CFL, the 1000 CML plus and the 1000 DL plus which are all currently listed on their website in the

**Dave Jones:** 1000 series. I wish they'd just like settle on one. Anyway, thank you very much Siglent for sending this one in. It's just been released and it is 100 bucks cheaper than the 1104 XE. It is still four channel. It's well, it's 100

**Dave Jones:** megahertz. What's the differences? Well, let's find out. This won't be a review video. It's more of a teardown video, but let's go through it. So, the differences are this one is 100 megahertz only. There is no 200 megahertz option, so I don't know if

**Dave Jones:** this can be hacked to a higher bandwidth. It may actually have a different front end, which is part of why we want to do this teardown. So, the new XU model here is 399 Yankee bucks as opposed to 499 Yankee

**Dave Jones:** bucks for the 1104 XE model and it's 100 megahertz only as opposed to a 200 megahertz option in this. So, whether or not this one can be hacked up to 200 megahertz, we don't know. That's why we're doing this teardown. We want to

**Dave Jones:** see if like the front ends are different. have they're almost certainly, I think, saving cost in this one. I wouldn't surprise me if they've got a redesigned 100 megahertz only front end. So, I wouldn't get your hopes up at this stage of yeah, hacking this

**Dave Jones:** one to any higher bandwidth or any extra features. Now, the other difference is this is a dual one gig sample per second, whereas this one, I believe, is only a single one gig sample per second. So, if you share that across all four

**Dave Jones:** channels, then you're only going to get 250 meg samples on each channel on all four. So, that's not great. Whereas this one, it actually says on the front quad 500 meg samples a second. So, yeah, it looks like they've halved the bandwidth

**Dave Jones:** or halved the maximum bandwidth and they've halved the sample rate and they've halved the memory as well in it to get the bomb cost down because you know, to save 100 bucks at retail price on this, you're going to have to

**Dave Jones:** be looking at reducing the bomb cost by probably you know, 30, 40 dollars. Something like that. They're going to save it and if the ADC chip alone is 10 bucks, you know, each then well, you can save I'm just ballparking there. I'm

**Dave Jones:** just I don't know what the actual cost of the ADC is, but right there you know, you might be able to save like 10 bucks off the bat by simply having the number of ADCs in there. And this one only has

**Dave Jones:** 128 KFFT whereas this will do one meg point FFT. As you can see, there's no digital option on this. The thing is actually there, but it's not populated and yeah, it wouldn't be populated on the PCBA either. But apart

**Dave Jones:** from that, they're near identical. This one does have the digital button. This one doesn't, but there is the indent in there for the digital button. So, they've used the same plastics as you'd expect. Also, this one doesn't do any bow plots and it doesn't

**Dave Jones:** do any Wi-Fi optional Wi-Fi as well, but it does have the same screen 800 by 480, but apart from that, yeah, that's the 100 bucks difference. But hey, 100 bucks down at this price point, that's quite a large difference. So, it's still 50

**Dave Jones:** dollars more than the Rigol retail price point at 350 US dollars for their four channel scope the 1054Z, but you know, it's this is a more this Siglents are generally a more capable scope than the Rigols. I believe that's still

**Dave Jones:** the case. I haven't done a modern comparison, but but you know, if you're saving every dollar, then you know, 50 bucks more for this four-channel, if you just want four channels, 100 MHz, then you know, 50 bucks more might buy you,

**Dave Jones:** you know, some other bit of test gear or something like that. They're absolutely identical down here, although, um, this one has a calibration sticker. This one just says calibrated. Oh, nobody signed it. Doesn't give me the, you know, the warm fuzzies. But as far

**Dave Jones:** as the ports go, you don't get the uh, USB on the back, which I had the Wi-Fi dongle on it, so that's why you don't get the Wi-Fi. Um, but you still get the Ethernet LAN. So, I believe it also

**Dave Jones:** doesn't have uh, web-based firmware update, which I believe the uh, E model does. So, haven't tried that, but that's in the comparison table anyway. So, there's your 4K money shot there. And no, I'm not going to turn it on before I

**Dave Jones:** take it apart. Let's take this damn thing apart and uh, see what the difference is is. Uh, we will find, like as I said, reduced uh, bomb cost, reduced componentry, just to get that bomb cost down. Guaranteed. Otherwise,

**Dave Jones:** what's the point? Oh, and the other thing is uh, the front end is only 1 mV per division, as opposed to 500 µV per division on the other model. So, that again is a hint that we might see an

**Dave Jones:** entirely different uh, cheaper front end on this thing. But hey, for a low-cost four-channel scope, you don't need your 500 µV per division. That's just like luxury. And it's got the same flippy feet on it, which feel okay. And the big

**Dave Jones:** rubber baby buggy bumpers on the bottom. And let's avoid the warranty on this bad boy. And I do believe that's the exact same metal chassis, if memory serves me correctly. And right off the bat there, you can see that it is a completely

**Dave Jones:** redesigned PCB. They don't even have the footprint in there. All right, let's see if we can pop the hood on this. Any yep, connections. Oh, nice. We can just whack that out. And beautiful, get the power supply out. Oh,

**Dave Jones:** it's uh got some silicon in there. That's nice. Attention to detail, but yeah, coming out. There we go. And yet, right off the bat, they have changed this. So, here's the old one on the top. Yeah, it's uh significantly changed, as

**Dave Jones:** you can see. There's a single uh ADC down here, as they told us. Um less memory, um as they told us. And uh yeah, it's a distinct lack of or and all the other digital um circuitry and everything else is just

**Dave Jones:** it's just goneski. Um yeah, that's pretty bare-bones. I'll tell you what, these cover plates are not easy to get off at all. You've got to get a knife in there and actually lift up each individual tab. Woah. And yep, as

**Dave Jones:** expected, a significantly simplified, redesigned uh front end. We've only got one relay like we had before. Don't know why they put the uh screening on. That looks like screening tape. Not sure what the deal is there, but um yeah. Look at

**Dave Jones:** that. There you go, that's magnetic shielding. Wow. Why do they need magnetic shielding on the top of the relay, I wonder? Hmm, that's interesting. I'm stretching here. My mind's just instantly went towards, well, what's the only thing behind here, above the relays

**Dave Jones:** here, um on the board, is the switching power supply? Maybe there was coupling in. Maybe they got a different design power supply. I don't know. I'm just I'm totally stretching here. Anyway, we've got a uh SO um 14, which we didn't uh have before. So,

**Dave Jones:** well, yep, there's your savings right there. I mean, you know, relays aren't cheap, right? And uh obviously, they've got uh some redesigned circuitry in here. So, no doubt that's going to be cheaper for the lower bandwidth. They've only got the single ADC up here, and

**Dave Jones:** that's it. As opposed to the two before, and then of course they've got less sample memory, only 14 meg points total, and that would go down of course if you put on the multiple channels almost certainly. So, that you know half the number of so

**Dave Jones:** you save your cost there, you save your cost in your ADC's. You save your cost on the relay and other front end components and stuff like that. You remove out, you know, another bomb cost on like the USB connector and the other

**Dave Jones:** end of the USB stuff, and you know, things like that. Like all these little bomb items add up, and all the little and all the support circuitry go along with that. Shave off, you know, cents here, cents here, a few bucks there, a

**Dave Jones:** few bucks there, and before you know it, you know, you've saved you know, 30, 40 dollars on your bomb cost, and that's why they can afford to sell this at 399 US retail instead of 499 US retail. And

**Dave Jones:** is this shielding material magnetic? Well, yeah. It's already electrically shielded, so must be some sort of magnetic shielding. And is it conductive? Wow, I'm really poking the probes in there. No, not really. So, let's actually compare the front

**Dave Jones:** ends here. Now, I've got three different Siglent scopes. This one is the SDS 1202 XE. That's the 200 MHz two channel version released in about April 2017. I've done a teardown video of that. And then we have the SDS 1104

**Dave Jones:** XE, which is the 200, well, the 100 or optional 200 MHz four channel version that was released in about November 2017. And here we have this new low cost one, the 1104 XU. So, this is the original one and it was a totally

**Dave Jones:** different format design. The board was totally different. As you can see, this one used like the way that just the mounting this one like mounted on the bottom, whereas this one was like vertically in the case. This was an

**Dave Jones:** entirely different design. When they went for the 1104 XE, even though it's got XE on it, it was an entirely different construction design inside, very different. But, they kept the front end nearly identical. Leave it in the comments if you spot something I don't,

**Dave Jones:** but differences down here. They've both got like an unpopulated cap on the input here, virtually identical. There are some differences in value. Oh, yeah, that one. Is that different to like here? But, basically, it's exactly the same. The unpopulated footprints are

**Dave Jones:** the same except for these. This large cap here is not present here. But, as I said, this is the 100 MHz model, not not the 200 MHz option. So, yeah, there's very, very little difference at all down in the two-stage front end

**Dave Jones:** down here. Let's just call it like a two divider stage front end. This one doesn't have a cap. This one has a cap. This one has zero ohm resistor. This one doesn't have a zero ohm resistor. It has

**Dave Jones:** some sort of resistance value in there. The transistors, they're all Look, this one doesn't have a cap in here. So, there's slight differences. In the 6 months from this one to this one, they did actually revise it. But, you know,

**Dave Jones:** it's the same transistor arrangement around here. Everything's hunky-dory. But, look at the difference over here. This is where they've reduced the cost. They have redesigned this front end. It's only a single divider stage here. They've only got the one trimmer cap as

**Dave Jones:** opposed to the two uh, caps here. So, we've got our resistor going in here. There's no optional footprint for the cap like we had over here. It's like there's just far fewer Look at this, far fewer divider resistors here. It's just

**Dave Jones:** like it it's much different. Looks like they're doing it up here cuz the OPA4872, that's actually a I believe it's that's a four-way mux. So, that's interesting. Once again, they've got the 595 for of course getting extra digital uh, lines

**Dave Jones:** to control this thing. Variable resistor here which they didn't have on this design over here. So, I don't know what that trimmer resistor would be doing. That's That's rather interesting. You know, trimmer caps you expect of course, right? To actually,

**Dave Jones:** you know, to tweak your response. Some gray-bearded new version Well, probably not at Siglent prices, right? Some some production worker sits there and goes I don't even think you get the tongue angle for this uh, price, really. I think yeah. Anyway,

**Dave Jones:** they they tweak that. So, yeah, it's only a single-stage jobby. So, significant cost savings there. And uh, the 8330, that wouldn't be cheap, would it? Let's go to the videotape. Now, you see, that's a pretty expensive sucker even in

**Dave Jones:** a thousand volume here, right? You're talking, you know, three bucks like it Yeah, they'd get it cheaper than that of course, but, you know, it's a couple of bucks, right? It's a one gig uh, gig low distortion differential um, amplifier,

**Dave Jones:** right? So, that's the output driver for the ADC, right? So, they've went Oh, bugger that. We don't need the bandwidth anymore um, because this is a 100 MHz only. There's no 200 MHz options, so we're not going to pay a couple of

**Dave Jones:** bucks. We're going for something cheaper. Thank you very much. But, here's the interesting part. The OPA4872, this is not cheap. It's a multiplexer with amplifier interface. It is not cheap. Like a Like six bucks at 2500. So, they must have been saving

**Dave Jones:** cost on some of the other parts in there to warrant using this unless they're getting it cheap somewhere. Part, it's much more expensive than I would have expected in a 100 MHz front end. Let's take a quick look at the data sheet

**Dave Jones:** here. Um granted, it's got a 500 MHz small signal bandwidth, okay? At 0.1 dB gain flatness to 120 meg. That's you know, probably you know, you got to pay for that gain flatness. You don't want the gain to change over the frequency

**Dave Jones:** response. You want it to be fairly flat in in the oscilloscope amplifier. You know, 0.1 dB good enough for Australia. And they've chosen like a pretty expensive mux there. So, that's interesting. Wow, I didn't expect that. So, unless there's something else

**Dave Jones:** on the bottom of this board, which I doubt, um that's it, right? We've got our front end transistors here and we've got a mux and looks like we've got a divider here, do we? If anyone knows what that is, but

**Dave Jones:** it's obviously like a differential amplifier. You can see the two resistors coming out here. So, if you want to analyze that, um have a go, but yeah, they've used a relatively expensive mux, but at the expense of all the additional

**Dave Jones:** I mean, you save on the real you know, you save on the whole second stage here and stuff like that. So, that's That's fascinating, but yeah, you're not going to get you know, a couple hundred megs performance out of this. It's like It's

**Dave Jones:** lucky if it does 100 meg. And if we look at the ADC in the new model, we've got a head 1511. So, let's see if that was the same. This would be the PLL. You can tell by all

**Dave Jones:** the like you know, the inductors and caps and a few resistors surrounding that. That's just got PLL written all over it, which generates the clock, which then there's your little differential pair going through there. Uh that drives your

**Dave Jones:** ADC here. As I said, they've only got a single ADC. And yep, confirmed, same ADC in the XE model, the HAD1511. And as we've seen before, it's a 1 gig sample per second AD uh converter. It's got uh

**Dave Jones:** once again, it can go into quad channel mode, but once again, because we've only got one of these compared to two in the previous model, it will only do 250 meg samples per second. I guarantee when you power this thing up, that's all the

**Dave Jones:** sample rate you'll get. Two and a half samples, right, per cycle is I yeah, okay, you're not going to alias, but it's, you know, it's it's not very good. Usually, you'll want 10 times. Usually, you know, a a good scope will have like

**Dave Jones:** 10 times. But as I said, technically, it's fine. You're not going to alias the sin(x)/x interpolation. It's going to interpolate it for the given uh response of the front end. Different response front ends uh will have different effects on the uh you know, the type of

**Dave Jones:** interpolation you use and stuff like that. And yeah, but anyway, 250 meg samples, it's disappointing, but hey, for the cost, you still get a four-channel scope. So, don't complain. And really, most of the time, you're not going to be using this damn thing at 100

**Dave Jones:** meg for all four channels anyway. If you, you know, looking at that sort of uh bandwidth, you know, you're going to be looking you know, you're going to be spending more coin on a higher-end scope. So, yeah, this is just a

**Dave Jones:** basically a stripped-down um E-series with redesigned front end. As I said, yeah, they're probably using the same Well, they might be using a less grunty FPGA under there that's uh stuck on with adhesive. I'm not going to thermal

**Dave Jones:** adhesive. Not going to try and get that off. Anyway, we do have Oh, look at that. They've even got the pin headers on there for us. So, um yeah, look, I won't If anyone really wants me to get the boot code, I

**Dave Jones:** probably could. It's got half the amount of RAM that the previous one's got and it really doesn't have much else. It's like there's the LCD connector. We've got some power supplies down here. Once again, this is this will not do 500

**Dave Jones:** microvolts per division. That's what they were getting the That's what they were using the two-stage one before. One stage would have been dedicated to the lower volts per division settings and the other one would have been used for

**Dave Jones:** higher. Now, they're just using like the single-stage relay switching here and the mux. So, yeah, you just you know, it's going to be less performance. I'm still curious to know about the magnetic shields on the relay cuz I don't recall

**Dave Jones:** those being in the previous model. Really simplistic, but that's what I expected. Let's have a quick squeeze at the power supply. Well, there you go. That is significantly different. I'll put up the other one up here and you can

**Dave Jones:** see Yeah, very different power supply even though the power requirements would be the same. Once again, this would have been cost optimized even though the old one would have been cost optimized. This one would be even more cost optimized.

**Dave Jones:** So, yeah, but it looks neat and tidy, doesn't it? They've just gunked it all up absolutely everywhere. Is that a little line or something? Can't quite see. People don't know why I can't see this. You can see this on your big screen. I

**Dave Jones:** can't read this sort of stuff on my camcorder and that's too uh small to actually for me to read from here. Anyway, from a design aspect, it's quite good. Look at all the isolation slots around the through the optos, between

**Dave Jones:** the diode bridge in there, full-wave bridge rectifier, of course, input So, input filtering, input common-mode choke, full-wave bridge rectifier into the high-voltage cap, and that's just driving the primary side switcher here. And there's our isolated isolation slot will go right under that transformer as

**Dave Jones:** well. And just Yeah, secondary side and then just our secondary side regulation. Not sure what voltages they need out of here. So, you know, the 12 and 5 or something. Do they even need a negative rail? Not sure. One curious aspect of

**Dave Jones:** this, look. What is this? Is this for like a switch? Um and what are these like little jumper links down there? Is it like do they have a different design of this thing um like in mind or something? Have they reused it for

**Dave Jones:** something else? I I don't know. That just does not make any sense. Anyway, that's a reasonable enough power supply, especially for the price and it's really seems like well laid out and designed. But yeah, you can bet your bottom dollar

**Dave Jones:** they would have been saving cents anywhere they could. Actually, this is very interesting. You'll notice that on the secondary side here, this is just a diode. So, you know, here's the main primary side switcher here. So, it goes switchers through the

**Dave Jones:** transformer. Then we've just got a rectifier diode there, some caps, and this is an LM317. And well, is that it? I don't see any other control stuff on the secondary side. We've just got an LM 317. Really? Well,

**Dave Jones:** yep. Nothing on the bottom side. That's it. Sneaky little bugger TL431 down there. The classic shunt classic precision shunt reference. So, yeah, apart from that um that's it. Is it? Okay, now let's actually measure the front end noise of

**Dave Jones:** this thing, shall we? So, I've got channel 1 and channel 2. I've got both the electrical shield in place on the back and also the magnetic screening on the back of the relay. So, what we've got here both DC coupled. I've got 50

**Dave Jones:** ohm terminator, but in case you're wondering, no, the 50-ohm termination doesn't make any re- practically any difference whatsoever. If it does, then it's a pretty poor shielded uh scope. So, you can have a look, you can see that in the uh peak-to-peak uh values

**Dave Jones:** there on channel one. As I Yes, cuz it'll have the Yep, it'll have the input uh the uh triboelectric problem. What did I call it? I've done a video on that. Anyway, I'll have to link it in. But,

**Dave Jones:** that makes no difference whatsoever. Uh So, what I've got is I've got the uh peak-to-peak and the RMS of uh channel one and channel two. But, I've done a video on this. The RMS value is not the correct way to actually measure noise,

**Dave Jones:** cuz it'll take into account the DC offset in here. And uh yeah, as I said, I've done a whole separate video on that. It's very interesting, hasn't I don't think it's cracked 50,000 views, but it's a fascinating watch. So, I'll

**Dave Jones:** definitely link that one in here. Watch it. Explains all about uh the traps in RMS uh noise measurement and standard uh deviation. But, anyway, uh peak-to-peak uh channel one, and we've got uh 700 odd microvolts. Uh channel two is a little bit lower there.

**Dave Jones:** Nothing really in it. And what we What we don't want to look at, actually, is the standard deviation of uh this RMS value here. We actually want the standard deviation function. So, if I call up uh measure here, we can go let's

**Dave Jones:** uh get it on channel uh two, because channel two has the worst uh DC offset. There it is, standard deviation. So, we'll turn that on. Standard deviation on, and bingo, we now have our standard deviation measurement up here. And there you go,

**Dave Jones:** it's giving around about 89 or something like that. So, it was uh different to our the standard deviation of our RMS value here cuz that's a different thing than the regular standard deviation. So, anyway, traffic young players, there's

**Dave Jones:** our noise on uh channel one and we'll get that on channel two as well. Right, so there you go. I've changed that to give us the peak-to-peak and standard deviation. Got all the statistics so you can get the standard

**Dave Jones:** deviation of the standard deviation. All you math nerds can uh go berserk in the comments uh explaining the difference there. But anyway, uh standard deviation of uh the noise, effectively, it is the RMS noise. It's basically the standard

**Dave Jones:** deviation function in this respect is giving you AC RMS cuz normally RMS includes the DC offset and you can see there's a very significant uh DC offset. I've measured it at like, you know, 300, 400 uh microvolts or something like

**Dave Jones:** that. It's very uh significant. You almost see it's not quite half a division there, but it's you know, it's quite significant. You might be able to, you know, calibrate out the scope and the DC offsets and stuff like that. Uh

**Dave Jones:** and that might drift with uh temperature and time and stuff like that. And maybe other channels coming on. Is it going to whoa. See? We're getting actually turn on channel three and our noise actually goes up. There you go. It's 100 up. Yep. So, if

**Dave Jones:** you have a look at, say, uh channel two, standard deviation noise 90. Turn on the channel three and we jumped up to 123. So, we're getting extra noise there. Turn on channel four, it's not going to make a difference. So, actually

**Dave Jones:** enabling that different uh enabling that sample rate, you can see the sample rate actually change up there. So, anyway, we can turn off channel one even. There we go. And does it even get lower? Uh 85. Turn on that.

**Dave Jones:** Uh yeah, it goes up a goes up a smidge. There you go. But that's not unexpected. I mean, these aren't the world's best front end. So, anyway, yeah. It's only 399 bucks. It's you know, it's a cheap front end. But, of course,

**Dave Jones:** good enough for Australia. So, anyway, that's with all the shields magnetic and electrical in place. So, now I'll actually take off that I'll take off the shields and see what difference it makes. And there's the noise without the electrical shield

**Dave Jones:** plates. So, it's kind of important. And by the way, I forgot to mention that they've reused the same plate cuz it's got all the holes in there. So, yeah, they just reused it even though we've only got the two trimmers, one cap, and one

**Dave Jones:** resistor. Still got the six holes, but you know, so there you go. Huge amount, but it's actually electrically the case is not grounded at the moment. If I move that back, there we go. So, without the shield, there you go.

**Dave Jones:** Because I've got you can see the case here, it's not touching like that. There you go. Boom. So, that's all right. Oh, there we go. That's a bit of a shocker, isn't it? There you go. This is with no electrical shield and no

**Dave Jones:** magnetic shield on channel one. So, no electrical shield on channel one and channel two. And this is with the case actually closed. With so with the switching power supply near it. So, I'm going to replace the magnetic shield now. So, let's you

**Dave Jones:** know, there it is. But what we actually don't want to look at look the standard deviation I eat the AC RMS noise. There's really nothing in it. It's basically the same as before. So, what we really care about now is that peak to

**Dave Jones:** peak noise. And we can actually trigger off that. There you go. That's the switching. That's the switching converter right there. Hmm, but that's what you'd expect. We've got no electrical shield and no magnetic shield. So, anyway, so we're looking that's what we want to see

**Dave Jones:** there. So, you know, typically 1.6 peak-to-peak and 1.2 on the second channel. All right, so let's move the trigger point up there. Let's free run it. This is with the electrical shield in place, but no magnetic shield on

**Dave Jones:** channel one, but channel two has a magnetic shield. And you can see yeah, mean peak-to-peak 900. Basically, well, it's basically the same on both. So, it really it doesn't seem to be a differentiation there between having the magnetic shield or not having it.

**Dave Jones:** It's the electrical shield that seems to be doing the business. So, why why do they have the magnetic shield there? That's interesting. Maybe there's some other external effects, but jeez, if you've got something like that near your scope,

**Dave Jones:** then you're probably going to come a cropper anyway. So, yeah, that's interesting. Okay, wipe it back on. But yeah, both are about 900 peak-to-peak mean. And magnetic and electrical shields back in place. Ah, mate, like no, no, it's dropped.

**Dave Jones:** Okay, slightly, but I like there's nothing in it really. Not seeing it. Um, I don't know. Anyway, leave it in the comments down below if you spotted something I've missed or you got some other reason why they'd have the magnetic

**Dave Jones:** shields on the relays. Yeah. I mean, it does seem like an afterthought just, you know, sticking them on the top because otherwise you'd buy like a magnetically shielded relay, and you can buy them. They've got little mu metal shields in them. So, yeah, I

**Dave Jones:** don't know. It's cheaper, maybe. Hmm. Nah. Price matters. Yeah, not exactly the world's best uh front end and sampling system, but you know, look, it's a $399 four-channel scope. What more do you want? I mean, you know, seriously. And

**Dave Jones:** there you have it. Like, I won't really go through all the extra um like it's cuz the It's the same as the XE, except it doesn't have the uh digital optional logic analyzer. I don't believe you'd be able to hack this to 200 MHz. Maybe

**Dave Jones:** somebody might be able to increase the bandwidth. You only got the 180C in there anyway, which has to share all four channels. And you got half the amount of memory and stuff like that, but hey, you know, it

**Dave Jones:** for 399 bucks, you're saving 100 bucks over the uh XE version. So, there's definitely a space for this uh in the market. It is 50 bucks more nominal. Once again, these are like just recommended prices, street prices. Your

**Dave Jones:** mileage may vary. And I do believe the Siglent is a more versatile scope than the uh Rigol, but I'd have to do like a modern shootout of, you know, everything um basically. So, yeah, anyway, this is not a review video. It's a teardown

**Dave Jones:** video. Leave us your thoughts down below, but it's interesting that Siglent came out with this uh lower-priced uh version. Obviously, they wanted to compete cuz Rigol's been flogging that 1054Z for uh I don't know, half a decade now,

**Dave Jones:** haven't they? When did I originally do my recommended video? People still watch that and go, "I bought the Rigol because you recommended it." It's like, there's lots of It was the only choice back then, really. It was the obvious choice.

**Dave Jones:** And now, um yeah, there's plenty of competitors, and this one's uh 50 bucks more. And uh whether it's worth more, leave it your opinion down in the comments below. And as always, if you like the video, please give it a big

**Dave Jones:** thumbs up. Check out my alternative platformies over here. You know what to do. Subscribe. Yeah, all that sort of YouTuber stuff. Rate, comment. Whatever happened to rate? Like, you know, you used to be able to rate videos. Like, now it's just like

**Dave Jones:** thumbs-up or thumbs-down. You know, you used to like Anyway. Catch you next time.
