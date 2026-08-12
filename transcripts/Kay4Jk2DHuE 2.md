---
video_id: Kay4Jk2DHuE
title: EEVblog #1042 - Siglent's $499 SDS1104X-E 4CH Oscilloscope Teardown
url: https://www.youtube.com/watch?v=Kay4Jk2DHuE
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 28, "3": 44, "4": 56, "5": 91, "6": 107, "7": 122, "8": 132, "9": 154, "10": 172, "11": 190, "12": 203, "13": 216, "14": 227, "15": 241, "16": 265, "17": 271, "18": 288, "19": 307, "20": 318, "21": 329, "22": 344, "23": 354, "24": 366, "25": 383, "26": 396, "27": 406, "28": 418, "29": 429, "30": 437, "31": 446, "32": 458, "33": 469, "34": 493, "35": 518, "36": 531, "37": 542, "38": 558, "39": 574, "40": 585, "41": 595, "42": 610, "43": 621, "44": 629, "45": 645, "46": 661, "47": 672, "48": 687, "49": 697, "50": 710, "51": 718, "52": 730, "53": 743, "54": 768, "55": 778, "56": 797, "57": 812, "58": 832, "59": 843, "60": 861, "61": 874, "62": 893, "63": 901, "64": 914, "65": 929, "66": 942, "67": 955, "68": 972, "69": 986, "70": 1002, "71": 1019, "72": 1036, "73": 1048, "74": 1058, "75": 1074, "76": 1082, "77": 1095, "78": 1105, "79": 1120, "80": 1136, "81": 1149, "82": 1168, "83": 1181, "84": 1192, "85": 1202, "86": 1211, "87": 1223, "88": 1231, "89": 1241, "90": 1253, "91": 1266, "92": 1278, "93": 1291, "94": 1303, "95": 1313, "96": 1325}
---

**Dave Jones:** Hi, yes, we've got another exclusive for you. Siglent very kindly loaned me their brand spanking new be to be released in a couple of days SDS 1104 XE oscilloscope and we've seen the XE oscilloscope before.

**Dave Jones:** I think back in April early this year I did a teardown of the 1102 or the 1202 XE the 200 megahertz version. Well, look, this is their new four channel version.

**Dave Jones:** Check it out. It's basically an identical platform to the existing 1102 and 1202 two channel XE series oscilloscope which they released earlier in the year and that was exciting enough but of course it was only two channels.

**Dave Jones:** But it just couldn't compete with the venerable Rigol DS1054Z because it as well up until now perhaps was the pretty much the only game in town in low cost four channel scopes.

**Dave Jones:** It basically owned it. But everyone's playing catch-up and I we're starting to see a spate of these competitive entry-level four channel scopes and this is fantastic. Now, the retail price on this puppy is going to be $499 US dollars for the 100 megahertz version that we see here the 1104 XE and this is actually way below the $620 for the Rigol DS 1154Z and you don't hack it then if you actually comparing

**Dave Jones:** apples and apples to the 100 megahertz bandwidth four channels then this one actually undercuts the four channel Rigol. But of course the hacks available for the Rigol and everyone just buys the 50 megahertz version and hacks it up to 100 megahertz and gets all the goodness built in.

**Dave Jones:** But this Siglent is designed to be completely competitive with that although it is a higher price point. So the Rigol's currently available for like 350 US dollars on sale or something like that, which is absolutely crazy for a four-channel scope.

**Dave Jones:** So, this one is more expensive, but it is a 100 MHz base model unit. So, yes, it is more expensive, but when you compare apples and apples, it's actually cheaper.

**Dave Jones:** So, basically, all the features are the same as the two-channel version. It's got the 14-meg sample memory standard, 100k waveform updates per second, which is like three times the Rigol 256-level intensity gray scale gray scale display, 1-meg FFT, which is really powerful, and it includes the free serial decoders for the cost.

**Dave Jones:** No need to hack anything. They throw in all the serial decoders for free. Fantastic. It also does bode plotting, which is a little little competitive head nod to the Keysight 1000X series, which, of course, includes that cute little bode plotting feature.

**Dave Jones:** And whilst this doesn't include an arbitrary function generator, you can get one as an optional extra, and we'll tear down this as well. It is a separate USB dongle-y type device, which you plug in and gives you a 25-meg bandwidth 125-meg sample per second arbitrary function generator.

**Dave Jones:** So, we'll do a quick tear down of that, too. But, and also it includes MSO capabilities as well, but they said that's not ready yet. But, once again, that'll be an external USB thing to turn it into a mixed-signal scope as well.

**Dave Jones:** So, this is pretty exciting. Four-channel scopes are really There's more than just Siglent and Rigol. Now, there's the GW Instek one and other players coming on the market on this low-cost four-channel scope.

**Dave Jones:** So, a very exciting time to get to be buying an entry-level scope. So, we're going to do a quick tear down. I expect it be almost identical to the two-channel version.

**Dave Jones:** And just on the back for those playing along at home, we've got our pass/fail trigger output LAN as standard, and the requisite USB. And another optional extra which can buy they have included it is a little Wi-Fi dongle which plugs into the USB on the back there.

**Dave Jones:** So, that's kind of neat. And we have the requisite metalwork. No signs of any trademark Siglent rust by the looks of it. But before we whip this thing open, if you compare it with the teardown video and photos of the previous unit, actually had the board on the back here and the ethernet was like up here and so it had the vertical processor board.

**Dave Jones:** This one's different, of course. It's got the IO over here like this. So, the main board is going to be on the bottom with the power supply in there.

**Dave Jones:** So, they've got the architecture different because it is physically larger with the four channels and things like that. So, let's open. Hey, it's not bad. And we are in like Flynn.

**Dave Jones:** Errol, that is. And one of the first differences you notice, apart from the main board being on the back instead of vertical like we got on the two-channel, is that the power supply is up in here and it is shielded unlike the two-channel model which actually the vertical board was here and the power supply was just open stuck in here like this.

**Dave Jones:** So, yeah, it's got more metalwork. That's good. If we take a look at the main board here, I've taken the shield off the front ends here and the architecture looks to be basically identical to what we had before.

**Dave Jones:** We've got our FPGA and processor under here. We've still only got the one handling everything. We've got our sample memory tied under that there. I don't know why they've only got three.

**Dave Jones:** They've got a fourth one unpopulated there. But basically you can see how they get the cost down on these things. It's basically a four-channel 200 MHz front end because yes, guaranteed 100 MHz model will have the 200 MHz front end in it.

**Dave Jones:** Just everyone does that these days. So, uh you know, it's very likely that you can hack this up to 200 MHz somehow. You can see there's basically not much else.

**Dave Jones:** We've got our power supply stuff around here. Some uh looks like some, you know, level translators and and stuff like that. Nothing much doing. Some stuff around here for your uh external signal generation and stuff like that.

**Dave Jones:** But, it's basically the big zinc processor under there and Bob's your uncle. And if we have a look at the power supply, it looks uh quite nice. We've got our nice uh earth strap going down to the uh uh crimp uh terminal with the shake proof washer down onto the uh directly Oh, sorry.

**Dave Jones:** Directly down onto the stud down there. Very nice. The board looks uh very nicely designed. Got our high voltage isolation slots. It's got all the regulator stuff. We've got our input filter and our common mode choke and everything and the isolation slots down near the bridge rectifier.

**Dave Jones:** We've got a leelaw Is that a leelon? That looks like a leelon to me. Yeah, whatever. Okay. Mhm. Um but, you know, par for the course in uh ones like this.

**Dave Jones:** Somebody really enjoys their silastic gun there and they like to just follow that around just to stop the capacitors uh flapping around in the breeze. Speaking of flapping around in the breeze, there's that one down there.

**Dave Jones:** There's a bit of silastic under that. And I thought, "Hey, that's not good cuz that's close to the uh metal cage here." But, I checked and that is actually electrically connected through to earth anyway.

**Dave Jones:** So, um it, you know, yeah. Anyway, just have it a flapping around in the breeze next to the metal there. Uh could be a real trap for the young players.

**Dave Jones:** Um it's got nice strapping over the transformer there. Everything looks fine and dandy. What are those capacitors in there? I don't know. I can't read that on the screen.

**Dave Jones:** Tiny little kangaroo ruby Hey, they they're Rubicons. Not bad at all. So, that really is very nice. Rubicon caps on the output. Very nicely designed and manufactured by the look and look of it.

**Dave Jones:** I like the little lead thing down there on the uh little surface mount TO package there, but yeah, thumbs up to that. All right, so let's have a squeeze under the Takagi microscope here.

**Dave Jones:** Nothing interesting happening around all that sort of stuff. There you go, ALVC translators or whatever what have you. Let's have a look down here. Nothing interesting happening. Got a couple of linear regs there and of course one of the big things is that we're going to have two analog to digital converters which are Well, I'll show you in a second.

**Dave Jones:** There and there because we've got one that shares the dual channel. And you have to have the two ADCs in there to keep your sample rate up. In this case they've it's one gig sample per second, but if you enable all four channels then it drops down to 500 megasamples per second, which is good enough for 100 megahertz bandwidth, not great at all, barely adequate with sine

**Dave Jones:** x on x interpolation for your 200 megahertz bandwidth model. So, not great. So, yeah, the 200 megahertz bandwidth of this sounds great, but when you don't have the sample rate to kind of match it, it's a bit disappointing.

**Dave Jones:** And of course we've got the head 1511 there if I block off the light a little bit. You can see yep, the standard one used in practically everything these days.

**Dave Jones:** Now, if we have a look at the analog front end, it is practically identical layout to the previous one. Um, so the only major difference I can see at first glance is it's got the extra capacitor populated on the footprint there.

**Dave Jones:** So, that's interesting, but apart from that it looks near identical to what we had before. So, yeah, I which is what exactly what you'd expect. Of course they're using exactly the same front end.

**Dave Jones:** So, there you go. Anyway, be high-res photos over on eevblog blog.com for those playing along at home. And then we under here we have our FPGA. I can't take it off.

**Dave Jones:** It's got the thermal adhesive on there, but it's exactly it's going to be well either exactly the same or a slightly increased part, but it's Siglent have said it's the Xilinx uh Zynq processor.

**Dave Jones:** Um so, which is a dual ARM Cortex-A9 or whatever it is uh plus the Artex uh FPGA architecture. So, it's a combined uh processor and FPGA. Um and it is incredibly powerful beast.

**Dave Jones:** I don't know why they've only populated the three parts there. They're all identical memory. Are they anyway? You can decode the part numbers for those playing along at home.

**Dave Jones:** It has 14 megasamples uh standard. So, yeah, why they've got three? Maybe they got two to handle all four channels. Maybe there's some more on the bottom side. I don't know.

**Dave Jones:** Not particularly fast. It's basically exactly the same architecture as we had on the uh FPGA and the the two-channel version. What's that? Look at that. NAND J1 JTAG. Um is that next to what that one?

**Dave Jones:** And then that seems a three pins. That seems a bit weird. Anyway, hmm that's just for uh programming the NAND flash memory, presumably. But, it's got a header as well.

**Dave Jones:** That one is for the Zynq. See? Z Y N Q. So, that is the JTAG I presume the JTAG header for the Zynq. Interestingly, got a reset pin up there.

**Dave Jones:** Hmm, maybe we can uh use that to reboot into some uh debug mode cuz on the previous uh teardown we did actually um hook up to the serial port and uh get the dump out of the thing.

**Dave Jones:** And that's where you're going to be getting the the from. The TX and RX. Uh, no doubt it has the U-Boot uh uh, thing in it and we'll be able to get the boot code out of that.

**Dave Jones:** So, this the hackability in this thing uh, should be pretty decent. And curiously, right over next to the power connector, we've got another five-pin header in there as well.

**Dave Jones:** Huh, what's going on? Is it for that little puppy? What is that thing? Not quite sure why they felt the need to put some tape over that. Is there a short in?

**Dave Jones:** Rest to something on the top of the case? I didn't uh, think so. Anyway, that's our uh, front panel USB, so don't know what's doing there. All right, let's have a look at the boot of this thing.

**Dave Jones:** I've got it uh, hooked up uh, via a serial port USB serial port 115 uh, K board here, 8-N-1, all the usual stuff. I've just uh, actually powered it off and there's the uh, data when you actually power it off.

**Dave Jones:** So, here we go, power it up. There you go, U-Boot. We get all the requisite stuff and I'll uh, copy this into a text uh, format and link it in down down below for those who want it and we should eventually get to a prompt.

**Dave Jones:** Come on, you can do it. And I think we're in like Flynn. And we'll have a quick look inside the arbitrary waveform generator, which is a uh, option, of course.

**Dave Jones:** We've got ourselves a got ourselves a Cypress uh, USB interface down here and a Cyclone 4 FPGA. That's exactly uh, what you'd expect. 74HC, got to have a 74HC4051 in there, couple of NEC relay jobbies and uh, what was that?

**Dave Jones:** An LMH6702. I believe from memory that's an output uh, driver. That's exactly what you'd uh, expect given that uh, it's proximity to the output here. Uh what else have we got?

**Dave Jones:** And an OPA 695 wideband current feedback op amp. What else have we got? Uh No output Oh, there's our 49 uh there's our 50 ohm output resistance. Not much else happening on here, is there?

**Dave Jones:** There we go. That's got Is that our DAC? What's that? I've got a negative We've got our negative rail generator down in there. Not much LM393 classic uh dual op amp.

**Dave Jones:** Let's have a look on the bottom here. Aha, now we're talking. There's our DAC. It's a Burr-Brown job. Love Burr-Brown. DAC 904 They're still Burr-Brown. DAC 904 uh Got to have a TL072, don't you?

**Dave Jones:** Another 50 ohm output resistor, another drive. I'm not sure what that number is offhand. Have to check that up. And a three peak. Who's a three Who is Who or what is three peak?

**Dave Jones:** That's interesting. TP1272. Sure enough, that's a single supply rail-to-rail op amp. Go figure. Anyway, another 4051, but that's about all she wrote on there. Nothing too interesting. So, anyway, that is the optional uh oops.

**Dave Jones:** Don't you hate it when your light pipe falls off? That's That goes on there. There you go. It gets the LEDs out to the front panel. Um that's quite neat.

**Dave Jones:** And of course, they save cost by not building this into the scope. Uh if you want the arbitrary waveform generator, you pay for it. Fair enough. As long as the uh software integration's good, I don't mind that concept at all.

**Dave Jones:** So, there you have it. That's a look inside the new Siglent SDS1104X E four-channel scope. Um yeah, it's Hello? There we go. That's our piezoelectric effect. It's actually not too shabby.

**Dave Jones:** Let me Oh, no. There we go. Hang on. Single shot. Oh, isn't it cute? Look at that. We can put it into up normal mode. There we go. Oh.

**Dave Jones:** Hey. Why do we have dual waveforms like that? What's going on? Is that a bug? We're in normal mode. I'd expect it to give me one update, not two.

**Dave Jones:** Is that what? You can't do what? Why is it doing that? Anyway, um yeah, that's our typical piezoelectric shock response, which we get on almost every scope, but jeez, that's Oh, there we go.

**Dave Jones:** Now you really need the high-frequency metal-on-metal like that, but I don't understand what's going on there. It shouldn't do that in normal mode. You should just get normal mode is basically a single shot capture.

**Dave Jones:** Uh I don't get that at all. It's gone through and it's not disarming the sweep, and you only ever get two of them. I don't get it. Don't get that with the Rigol.

**Dave Jones:** Look at that. No worries whatsoever. Normal mode gives you exactly what you'd expect. Let's Siglent and another competitor, the four-channel uh GW Instek GDS-1104B. Um They're It's a very significantly different re- front-end response.

**Dave Jones:** So, it's mechanically coupled. Very Oh, wow. Very, very differently, but anyway. Now, this is interesting. If we try the uh Keysight one here, right? We got a similar thing happening in normal mode, of course.

**Dave Jones:** But look, it I see it popped up with the multiple one the multiple waveforms there, but it figured that you're in normal mode and you wanted that single shot capture, right?

**Dave Jones:** Because it's the high update rate, it's going to show the multiple things. So, maybe it the Siglent one, because it's 100,000 waveform updates per second, the Siglent, which is awesome, but it leaves the artifacts of the uh of the See?

**Dave Jones:** Um whereas the Keysight gets rid of them as I would expect it to. Um if I'm in normal mode and I get a single shot thing which triggers my scope, I damn well want it to capture.

**Dave Jones:** So, the the last one. I mean, you know, cuz there's multiple trigger points there with this thing. Maybe if I do it like that, it's going to be a bit more controlled.

**Dave Jones:** Yeah. Right? But because I'm doing the high frequency one like that, there's a bit uh yeah, I'm getting multiple vibrations coming through and triggering that multiple times, but in the end, you just want one screen like that.

**Dave Jones:** So, I don't know what the heck's going on with the Siglent. Is that Is it a PEBCAK or is it just the way it operates? Do they think that's better?

**Dave Jones:** I don't get it. Oh, check it out. No, the Sig- It did go away before. I think I captured it there, but now it's not. So, but I did actually see one go away.

**Dave Jones:** So, I'm not sure what the deal deal is. It's Uh anyway, anyway. Um that is the new Siglent SDS1104X E. Thank you, Siglent, for uh loaning this one before it's released.

**Dave Jones:** Oh, there you go. Look. It just magically Was that me talking? Is that my my I'm talking I talk so loudly that it's coupling through to the input? I don't know what's going on there.

**Dave Jones:** That's a bit quirky. Hmm, more investigation required. Anyway, yes, I do plan on doing videos uh reviewing and maybe like a shootout comparison or something like that. Um but it's interesting 499 US bucks with all the serial uh decoders built-in, by the way.

**Dave Jones:** There they are, I2C, SPI, UART, CAN, and LIN buses all built-in. The 14 meg sample memory, the bode plotting, which I haven't uh looked at yet. But yeah, you can actually do a bode plot.

**Dave Jones:** There you go. Uh 1 meg FFT, which is awesome, which you can do these days inside that Zynq uh FPGA. Um and which you see on other scopes like the GW Instek one does.

**Dave Jones:** If you just want the 1 meg points, that's proba- FFT, if that's important. The Siglent uh so the GW Instek one's a bit of a killer in that regards.

**Dave Jones:** Anyway, this one's got 1 meg FFT as well. And uh it has Wi-Fi dongles and maybe um and it's supposed to have the MSO capability, but that's not out yet.

**Dave Jones:** And the separate arbitrary waveform generator, whatchamacallit, is a bit pricey, I believe, for the option. But uh anyway, this is not a review. I just wanted to show you this cuz it's very exciting.

**Dave Jones:** You can get a four-channel scope for 499 bucks with all the serial decoders built-in, a crap load of sample memory. Uh you know, the the sample rate's good enough.

**Dave Jones:** I wouldn't be paying the extra for the 200 MHz one of this. It's just the sample rate's not good enough, especially if you're utilizing all the four channels. It's just, you know, it's it's not great at all.

**Dave Jones:** Um but hey, for the for the price, if you can hack this thing, which I believe it's going to be hackable, so there's probably going to be a lot at this price point, probably going to be a lot of people working on this one.

**Dave Jones:** Um it's pro- likely just like a software hack or uh something like that. Um so anyway, we'll see. I've already tried a few things. I've tried to uh redo the model number and uh stuff like that.

**Dave Jones:** So I've tried to go in and uh where is it? Uh update. Yeah, I've tried No. Where is it? System status. Anyway, I've tried to go in there and change like the model number uh the SDS and it's not sticking and stuff like that.

**Dave Jones:** That was a real old Rigol hack back in the day and that one's not working. But, I mean, there's probably a way to hopefully hack this. There's no point getting the serial decoders cuz you get all that uh for free.

**Dave Jones:** So, yeah. Here you go. It's pretty jazzy. We are the winners. Now, it's No. No, see, I I don't get it. Anyway, the market's the winner on this one.

**Dave Jones:** That's us. Four channel scopes for like Well, you can get the Rigol for 350. This one's 499 for 100 meg bandwidth with all the decoder crazy. When I was a boy.

**Dave Jones:** Anyway, high-res teardown photos down below, discuss down below that screen dump for the BIOS boot thing, all linked in down below, and videos at the end. If you liked it, please give it a big thumbs up.

**Dave Jones:** Engagement always helps. Uh and, you know, there's a subscribe button and watch the thing videos or whatever. You know the deal. Catch you next time.
