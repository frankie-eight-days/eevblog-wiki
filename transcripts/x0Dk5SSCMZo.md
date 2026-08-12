---
video_id: x0Dk5SSCMZo
title: EEVblog #1208 - Circuit Analysis & Debugging
url: https://www.youtube.com/watch?v=x0Dk5SSCMZo
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 26, "3": 38, "4": 49, "5": 65, "6": 79, "7": 91, "8": 105, "9": 118, "10": 134, "11": 149, "12": 162, "13": 175, "14": 189, "15": 201, "16": 214, "17": 228, "18": 238, "19": 252, "20": 264, "21": 280, "22": 291, "23": 303, "24": 317, "25": 328, "26": 342, "27": 354, "28": 369, "29": 381, "30": 392, "31": 408, "32": 424, "33": 438, "34": 451, "35": 464, "36": 478, "37": 493, "38": 508, "39": 522, "40": 536, "41": 555, "42": 570, "43": 586, "44": 599, "45": 613, "46": 625, "47": 645, "48": 660, "49": 678, "50": 695, "51": 705, "52": 721, "53": 735, "54": 748, "55": 758, "56": 771, "57": 783, "58": 795, "59": 810, "60": 822, "61": 836, "62": 849, "63": 863, "64": 879, "65": 899, "66": 915, "67": 934, "68": 948, "69": 965, "70": 985, "71": 1003, "72": 1023, "73": 1038, "74": 1053, "75": 1069, "76": 1085, "77": 1097, "78": 1116, "79": 1131, "80": 1145, "81": 1163, "82": 1177, "83": 1191, "84": 1205, "85": 1219, "86": 1236, "87": 1254, "88": 1270, "89": 1288, "90": 1304, "91": 1319, "92": 1334, "93": 1348, "94": 1362, "95": 1379, "96": 1395, "97": 1409, "98": 1422, "99": 1435, "100": 1451, "101": 1463, "102": 1476, "103": 1489, "104": 1501, "105": 1516, "106": 1528, "107": 1540, "108": 1559, "109": 1572, "110": 1586, "111": 1597, "112": 1610, "113": 1621, "114": 1634, "115": 1647}
---

**Dave Jones:** Hi, I thought I'd take a look at a forum question and hopefully uh try and find an answer for this particular uh forum contributor. And I get uh emailed questions like this a lot of times. Somebody has a problem with their

**Dave Jones:** circuit, it doesn't work, they want to figure out why. And unfortunately, I often don't have time to uh answer these questions directly just to due to the volume of email I get. And I've actually got a template form

**Dave Jones:** response um that I don't like to send, but ultimately sometimes I have to say, "Look, I do I think it's better if you ask it on the forum, you'll get a better wider response from people." And the forum is the best place to answer these

**Dave Jones:** sort of things. And occasionally, I'll jump in and uh look at a forum question like this and answer it. I did actually uh potentially answer it down the bottom. I thought I'd make an interesting question. So, the forum

**Dave Jones:** contributor is Darkwing. Uh and Darkwing uh so, I've built this circuit up. Here's a uh it's a 74HC390 uh ripple counter. And all they want to do is divide um a pulse signal coming in. And there's the breadboard circuit

**Dave Jones:** and the Rigol scope and what it's supposed to look like. Of course, it's supposed to be just a simple uh four-bit binary counter. That's it. But it doesn't look like it's counting in binary. It looks there's there's something

**Dave Jones:** there's something going on here. So, let's try and analyze this circuit and see what's going on cuz there's potentially a lot involved in here. We'll go into the data sheets and have a look at the circuit configuration and

**Dave Jones:** try and figure this out. Let's go. Now, I've reverse engineered the breadboard and here's a DaveCAD drawing of that. You can see that we've got the uh the two halves, so to speak, of the uh HC390 ripple counter. The ripple counter

**Dave Jones:** actually contains two sets of these. So, there's a divide by two and a divide by five like this. And you can use them separately or you can do what Darkwing has done here and connect the Q output of the first divide by two into the

**Dave Jones:** divide by five and of course that gives you a divide by 10 counter. Sorry, it's a decade counter. I said it was a four-bit binary. It's actually a decade counter in this particular chip. So and it's driven via an optocoupler over here

**Dave Jones:** and we can see that. Sorry, it's the breadboard's upside down so all the electrons are going to fall out. Can't quite make out the resistor values but I think that there's a 270 ohm in series. I could be wrong and I think it's a 2K7

**Dave Jones:** pull up to VCC and there's a bypass the first thing you might think, "Aha, it's the chip's not bypassed properly." For example, but there's a bypass capacitor in there. I think Darkwing says it's a 100. Here it is.

**Dave Jones:** Does not divide by two. They do the second stage does not output a recognizable pattern. What could be wrong? Is it somehow necessary to stabilize the IC? Darkwing found that if he put a 0.1 microfarad across the VCC

**Dave Jones:** ground, it did a little bit to improve this but probably not much. So can somebody give me a hint? So let's look at the circuit here and you can see that and sure enough let's just assume that the power supply

**Dave Jones:** is fine and hunky-dory and there's a bypass cap on there. You should actually put it directly to the pin over here but it's reasonable. There's a little bit of extra inductance caused by that link there going over but on a breadboard at

**Dave Jones:** the for this particular type of chip at the at these sorts of speeds like at edge rates it doesn't matter. Right? So that's bypassed just fine. So we've got our ground and power going to our chip. I've done a video where you can

**Dave Jones:** potentially make a a mistake and power your chip through your signal pins and I'll have to link that one at the end cuz that is quite fascinating and that's something where some people come a cropper where you think your circuit

**Dave Jones:** is working and it does seem to work in most cases then all of a sudden, you get some input pattern to your chip and it fails. It's because you don't have the power pin connected and it's a reverse

**Dave Jones:** powering through the protection diodes and stuff like that. But let's just assume that all the connections are okay. The first thing you want to suspect on a breadboard is a bad connection. For example, these resistors when you peel if you get

**Dave Jones:** them on the bandolier thing right on the reel, they'll have those bandoliers on them and if you actually just pull them out of that bandolier and go stick them in your breadboard, that's a bad idea because there's actually a bit of

**Dave Jones:** adhesive or glue inside on those tapes. So the ends of the resistor, the ends that you're going to plug into your breadboard might often contain if you just pull them out, they will contain a little bit of glue and that can be um

**Dave Jones:** non-conductive. So you got to play plug it into your breadboard and often that glue is not really it's not all that visible. So you might go to pull your resistor out of your bandolier, plug it in and it might make bad contact

**Dave Jones:** cuz it's got the glue on there. So make sure you either clean that or cut them off the bandolier if you're going to use them in your breadboards. Little trap for young players that one. Come a cropper many times, trust me.

**Dave Jones:** Anyway, let's assume that all the connections in the breadboard are good and there's something wrong with the circuit. Either the wiring of this or there's something wrong with the chips or there's something wrong somewhere else. Well, let's take a squiz. Okay, so

**Dave Jones:** the first thing we're going to do is take a look at the data sheet for our uh Texas Instruments uh 74HC390 and it was a TI part. You can see that down there. It's got a little TI logo

**Dave Jones:** that's upside down. But pretty much any HC series data chip is going to be adequate here. So no problems whatsoever. So let's go down and take a look. Here is our counter the divide by two and the divide by five and you'll

**Dave Jones:** notice that there's a little notch in there. It's called a notch, little circle. That means that this clock is going to go down on the negative edge like that. Oh, sorry, I've got my laser pen on. But, it's going to be uh clocked

**Dave Jones:** on the negative edge, and you can actually see that down here in the uh true table, uh the negative when the clock goes negative like that, it will actually do the count. But, if it goes positive, then you get no change. So, it

**Dave Jones:** counts on the negative edge. And that might actually matter for our circuit configuration, as we'll take a look at. Now, uh let's go down here. There's the internal circuit for those playing along at home if you want to see. Anyway,

**Dave Jones:** uh what we've got is the master reset, and the reset pin of both of these is actually connected down to ground. I've checked that, so that's hunky-dory. So, there's nothing wrong with the reset, and that is an active high because

**Dave Jones:** there's no not in there like that. So, it's and you can look at the truth table, and you can see that. And Darkwing is connected correctly connected the uh Q0 output through to the clock input of uh the divide-by-five counter, so that

**Dave Jones:** gives our divide-by-ten counter. So, that should be hunky-dory, right? Everything looks fine. Right, so we know our chip's bypassed, we know the uh reset is all okay, and the other thing is is that the other pins aren't tied,

**Dave Jones:** the other pins aren't the inputs on the other side of the chip here cuz I said it's got two of these uh divide-by-ten counters in it, they aren't connected. And generally speaking, you shouldn't leave the inputs floating on CMOS

**Dave Jones:** devices like this. So, I tie pins 1, 2, and 4 down to ground like that, just so that the inputs are tied off. But, in this particular case, I greatly doubt that is the cause of our problems here,

**Dave Jones:** really, because we've got a lot of should have a low impedance drive into the other inputs. Should one half of the uh chip shouldn't affect the other half. It just might the inputs to these uh pins here, if you leave them floating, they

**Dave Jones:** might, uh, uh oscillate, which causes extra power dissipation inside the chip. But, it shouldn't affect the other half of the chip. So, that's not really a problem. Right. So, if the circuit's correct, the power supply is correct, we've got adequate, uh, chip bypassing,

**Dave Jones:** what's the problem? Well, literally the first response I said was that, uh, 74HC, in fact, any, uh, logic, uh, device has a maximum input slew rate. So, make sure your inputs are nice and fast edges. And if we go and have a look

**Dave Jones:** at the circuit up here and see what it's driven from, well, the clock input here is this green wire, uh, pin 15 up here. It's going over to here. It's going through, I believe that's a 270 ohm resistor, and that's jumping over to,

**Dave Jones:** uh, what? Pin six of this, uh, HP 3700. So, let's go and have a look at the HP 3700. You might have already guessed that this is a, uh, AC to AC logic interface. It's an optocoupler. And if

**Dave Jones:** we have a look at our internal circuit, the output is coming from pin six. This is buggering off to our circuit. That's the clock pulse, and you'll notice that that is an open collector transistor. There's nothing, it's not a totem pole

**Dave Jones:** output, which means so there's no active transistor in here that can actually drive this input very fast up to the positive rail. It's an open collector output. So, you have to, of course, rely on a pull-up resistor to VCC here. In

**Dave Jones:** this case, it's, I think it's 2K, uh, seven pull-up. But, even if it's like a very low value, like, uh, 2.7, uh, 270 ohms or something like that. In this particular case, when you go positive, then it's not going to be a nice sharp

**Dave Jones:** edge like that. It's going to have a slew like that. And that could that slew there uh could be in the order of microseconds. It depends on uh the capacitance of the load that you're driving, i.e., the input of the chip

**Dave Jones:** that you're driving, capacitance of the breadboard, capacitance of the PCB circuit traces if you're using a PCB, any other components uh that are connected onto that bus as well, which is why not only 74HC, but any form of

**Dave Jones:** logic will have a maximum fan out, uh which is how many gates you can actually drive. It's due to uh the capacitance, mostly. This transistor here, it should, in theory, give you a nice fast negative-going pulse like that. There

**Dave Jones:** won't be much slew. But we can actually go down. First thing we'll do is go down and have a look at the data sheet, shall we? Let's go and have a look to see if we actually have a value for our slew

**Dave Jones:** rate, shall we? Here it is. Output, which is a rise and fall time, is the output slew rate. So you'll see that the output fall time here, here we go, is 0.5 microseconds, 500 nanoseconds. That's not particularly quick. And so

**Dave Jones:** keep that 500 microsecond figure in mind. And the output rise time is 45 microseconds. But as I said, that varies with the capacitance load and the pull-up resistor that you're actually using. In this case, they give you a for

**Dave Jones:** a nominal that value is for a nominal 4.7 K and 30 puff or 30 uh picofarads output, which might be typical uh input capacitance of a gate or whatever. So there you go, at best, we're probably going to get 500 nanoseconds

**Dave Jones:** fall time, which, as we said, due to this negative not input here, it's a negative-going clock edge. So that's what we're concerned with. So let's go down into the 74 series data sheet and have a look at our maximum rise and fall

**Dave Jones:** time, shall we? Just what you do when you're looking at data sheets, just you know what units it's going to be. It's going to be seconds. So, it's going to be microseconds, nanoseconds, you know, things like that. So, you just want to

**Dave Jones:** scroll down. You like you don't even have to read any of this stuff on the left-hand column over here. Just scroll down. Microseconds, microseconds. Is there any Aha! Microseconds. Clock pulse width. Now, this is the clock pulse width. This is not what we

**Dave Jones:** width of uh the pulse before it'll uh it gets ready to count the next one cuz it's got to propagate through the chip because this is a ripple uh counter. So, let's assume that the clock goes negative here. It takes a certain

**Dave Jones:** amount of propagation delay to get through the gates inside there before the Q output changes and before it can be clocked again. And this is a ripple counter, which means that this Q output, assuming you've tied it to

**Dave Jones:** Assuming you've tied up to here like this, then it'll ripple through here. It's got to go through like that and then the output of this has to go into the clock of the next one. And then it takes propagation delay to get through

**Dave Jones:** to here. And then it takes propagation delay to get through to here and through there. So, uh that is why uh this is why it's called a ripple counter. The clock ripples through all the different gates as opposed to a synchronous counter. But

**Dave Jones:** that's not our issue uh here. Right. So, it's really got nothing to do with the clock pulse width. That's fine. I don't think we're we've got an issue here. And you'll see that's only a minimum value cuz there is no maximum

**Dave Jones:** value for that. It can be 1 Hz. It can change. You can have one clock pulse every year if you want. And it makes no difference. It doesn't care. All the chip cares about is the edge rate. All

**Dave Jones:** it cares is how fast does it Uh Stupid tool. All it cares is how fast does it transition down. How long does it take? So, let's keep going to find some more nanosecondy Aha! Reset removal time, don't worry about that. Reset cuz it's

**Dave Jones:** just tied to ground. We're not having We don't have like a synchronous or asynchronous system reset or anything like that. Reset pulse width is going to have a minimum value. We don't care about that cuz it's just permanently

**Dave Jones:** tied to ground. Let's go down to here. Actually, before we get to that Look, here's our input capacitance. You know how I said before that can change your slew rate. Well, it's a maximum of 10 picofarads here, 10 puff, which isn't

**Dave Jones:** a huge amount and that's maximum. Could be like half that as a typical value. They don't give you any typical values in there, but you know, there's a little bit, half a puff tenth the capacitance in there, so that could matter. But in

**Dave Jones:** this case, that's not really our problem. So, this is interesting. All we've got down here is clock pulse widths. We don't care about reset removal times, pulse width removal time, we don't care about. Clock pulse width again, reset removal Those are That's

**Dave Jones:** for the HCT types. And then we've got switching parameters down here, which are your propagation delays. We're not concerned with propagation delays. That's only a system implementation when you are implementing a ripple counter or how long it takes to ripple through each

**Dave Jones:** segment as I was talking about before. But this isn't anything to do with our maximum slew rate. So, output transition time, this is how long it takes to transition the output. It transitions in typically 15 nanoseconds, for example, goes up

**Dave Jones:** with temperature and stuff like that. But yeah, generally, but it's a reasonably fast output edge on this thing. But all we care about is the input. So, this is interesting. I I did not read this data sheet before

**Dave Jones:** I jumped into this. I'm assuming I assumed it was in here. There is no mention where we're down to the package stuff. There is as actually with Commegatza. There is no mention of the maximum slew rate of the clock input. I must be blind. I

**Dave Jones:** should like prepare for this stuff before I press record. Now, it does tell you up here the switching specifications are for a T rise. That's a little R there stands for is the rise time and the fall times

**Dave Jones:** are 6 nanoseconds. So, all this stuff is tested and all these all these specs apply for when you apply a 6 nanosecond rise and fall pulse. That's very quick actually. So, that's assuming that, but it doesn't actually tell you what the

**Dave Jones:** maximum transition is and there's no like notes that are down here. So, it's got to be in here somewhere. It's not in any of the footnotes down here. So, let's go up all the way. Bingo. Input rise and fall time. Here it

**Dave Jones:** is here. They specify for the different voltages. 500 nanoseconds maximum. So, there you go. So, it's actually going to be slightly under that for 5 volts. Somewhere between like 450, 470, something like that. Absolute maximum value. So, right there if we go back and

**Dave Jones:** have a look at our optocoupler here. Uh we could Commegatza. Like there's like we're already at 500 nanoseconds there. Half a microsecond for the fall time and that's with the transistor pulling it down. That's not the horrible 45 nanosecond

**Dave Jones:** uh rise time with a nominal 4.7 K resistor into that the capacitance load. I Yeah, it might be faster than that, but it's like in the order of tens of microseconds with the resistor 2 K 7 we're talking about here.

**Dave Jones:** Even the four times no good. So, right there we're we're incredibly marginal right there. I like I'd I'd be concerned right at that, let alone for the rise. So, that's a huge red flag. Not only are you operating outside of

**Dave Jones:** the And these are just typical values, too. They could change with temperature and and parameter spread across production units and stuff like that. Already we're really concerned that that's not going to meet our specification for our rise and fall times. And of course, this is a

**Dave Jones:** known problem when you try and clock logic chips or even just transition the inputs and things like that. You can cause them to go metastable. So, yeah. Um I think we got it. There's not really much practical difference between any of

**Dave Jones:** the logic HC or HCT or F or anything else. Like, there can be small differences and if you're designing right on the edge of the spec, the brand of the chip might make a difference. There's a few cases where I've I've

**Dave Jones:** personally had that, but generally speaking, when you're modestly designing, it shouldn't matter at all. But if you remember, as we saw on the data sheet, it was already typically 500 ns, so we're already borderline even going negative with that fast transition with

**Dave Jones:** the open collector output there, it's still borderline slow. And what happens is if your input is too slow, it can cause the chip to go into a metastable state. Metastability. Have I done a separate video on that? If I haven't,

**Dave Jones:** I've covered it in in some video somewhere. Anyway, metastable state, which means you don't don't know what what it's doing. It could be getting multiple clock clock pulses, it could be getting none, it could be skipping pulses, getting multiple ones, which is

**Dave Jones:** why we could be seeing this weird effect, a counting effect that we're getting here, because this could be a meta stable input caused by slew rate. So, I'm almost 100% certain that the input slew rate caused by this

**Dave Jones:** optocoupler here is open collector optocoupler and this pull-up resistor here is what's causing the problem. The in this case, the negative going pulse is just is too slow for this thing and it just it can't count properly, which

**Dave Jones:** is why it's giving you a weird counting configuration. So, if Darkwing actually bypasses that and feeds it from a nice clock source from your signal generator or some other TTL device, you'll fix it. Or if you really wanted

**Dave Jones:** to use this if you had to use the optocoupler, obviously feeding in some sort of AC signal wants to convert that to digital and then clock the thing, which is fine. But in this case, you want a Schmitt trigger

**Dave Jones:** input and I'm sure I've done a video on Schmitt triggers. If I have, I'll link it in. A Schmitt trigger won't get into a meta stable state, but most chips do not have Schmitt trigger inputs, Schmitt trigger clock or data

**Dave Jones:** inputs. So, in this particular case, if you wanted to use your 74HC390 still, then you would put a say a 74HC14, which is a Schmitt trigger inverter in front of that so that it would clean up that low signal. So, if you've got your

**Dave Jones:** optocoupler like this here, okay, and you've got your pull-up resistor like this, instead of feeding that in your 74HC390, you feed it into a 74HC14 and I can draw my Schmitt in there like that. That's the symbol for a Schmitt

**Dave Jones:** inverter and this input here can be as slow as a wet week. It can take a second to ramp up and the Schmitt just goes I'll convert that into a nice beautiful in this case, sorry, nice, beautiful negative, cuz it's an inverter, nice,

**Dave Jones:** sharp negative going output pulse, which then you can feed in to the clock input of your chip, and Bob's your uncle. You won't get any more metastability on your 390 over here, and that will fix the problem. So, yeah, these optocouplers

**Dave Jones:** are notoriously bad for driving chips. Other things with open collector, like an I2C bus, for example, this is why the I2C bus, which is an open collector bus, they the typical recommendation is 2.2k pull-up resistors, but you might lower

**Dave Jones:** that to 1k if you want the bus to operate faster, if you've got more things on the bus, which have more capacitance, which causes a greater rise time in your signal when it transitions from negative to positive. Those open collector buses and other

**Dave Jones:** clocks, like optocouplers, are a real pain in the butt. So, I reckon that is the problem. So, I've actually been waffling on for like 20 minutes about the slew rate and how that's a problem, and it will be. But, that doesn't mean

**Dave Jones:** that's the only problem here. There could be multiple problems. And, by the way, looking at this, the issue is is that this this is the input, this is the Is that the Yeah, no, that's the clock one, the clock two,

**Dave Jones:** and it's like inverting that. So, that could be caused by the metastability problem of the first divide-by-two counter that we're looking at. But, once you get the output of that chip, you don't and you're feeding it into the

**Dave Jones:** second stage here, you don't have that meta stable Well, you still have a metastability problem, but you don't actually have it this chip go meta stable, because the input should be transitioning nice. But, the problem with that is is that the output of your

**Dave Jones:** divide-by-two counter, because it's being clocked by a slow slew input. That could be going metastable. The output could be oscillating like buggery, doing all sorts of weird things, and then that might not have the setup and hold times

**Dave Jones:** or the clock pulse width requirements that we saw in the data sheet before to then clock the divide by five. So, once again, I would have expected to see a more normal count on this side here. So, what I'd be doing if I was dark

**Dave Jones:** winging, I'd also be zooming in on my Rigol scope on that yellow waveform there and checking out to see if there's any multiple clocks. In fact, can you get a hint of that in there? Maybe not. But, yeah, zoom in on your time base,

**Dave Jones:** zoom in and see if you're getting multiple transitions on there and if it's oscillating, then you know it's like it's going metastable and going crazy like that. But, yeah, why why we're not getting a more normal count down here, I don't know.

**Dave Jones:** The reset uh pin, no, that's uh tied to ground. So, that's all right. So, really it can only be the inputs uh really causing that. So, there might be some goofy setup and hold output of your first divide by two stage

**Dave Jones:** maybe oscillating all that, doing all sorts of weird stuff, doesn't meet the requirements for the clock pulse of the second stage, and that's goofing up the clocking of the second stage and stuff like that. Cuz if you go back here and

**Dave Jones:** have a look at the internal diagram for this thing, it's, you know, it it it's relatively complicated, right? if if your inputs uh like you've got your clock pulse here, okay, pin 12, then it's got to drive all

**Dave Jones:** these gates here, and if it's doing all sorts of oscillations, there's going to be like setup and like setup times and and stuff like that, minimum clock clock pulses, as I said, that we saw in there. And if you're not meeting any of those,

**Dave Jones:** then this can really screw up this configuration in here, and that's probably why we're seeing the weird count there Uh than, of course, cuz the pin 12 that we're driving, there's no there shouldn't be a slew rate problem

**Dave Jones:** there cuz it's being driven from the output of the divide-by-two counter, which should be a nice uh sharp TTL HC, you know, CMOS slew rate. So, yeah, that shouldn't be a problem, but yeah, it There's some funny business

**Dave Jones:** going on there, which is screwing everything up. But, I think ultimately, the problem is the input slew rate. If you fix that, everything else should fall into line. That's the plan, anyway. So, there you go. I hope I've

**Dave Jones:** answered Darkwing's question. I hope he follows up uh with this and lets us know what the problem is. Anyway, so that's what I said down here is has maximum input slew rate. Yep, your clock pulse is coming from an optocoupler, that will be

**Dave Jones:** creating a slow positive That's actually a negative edge. Sorry, positive edge. Yes. Um and potentially a slow negative edge as well. That optocoupler is not that quick. Um and try reducing your pull-up resistor for starters, etc. So, there you go. Um and Flubby Dust down

**Dave Jones:** here mentioned, yeah, the floating inputs. But, in this particular case, that's I That's pretty sure that's not the problem here. It's not going to interfere with the other half of the chip. Just might be oscillating and drawing more power consumption would be

**Dave Jones:** the only thing if that. So, there you go. I hope you found that interesting. I could go into details about logic threshold levels and metastability and all sorts of stuff. But, all this sort of stuff requires its own video video in its own right,

**Dave Jones:** really. So, anyway, if you I hope that's the answer. Otherwise, I'm going to be really embarrassed if I missed something and it's just this breadboard wiring error or it's a as I said, a contact problem or or something

**Dave Jones:** like that. But, yeah, notorious these optocouplers when you're driving. You don't want to drive signals directly from open collector like that. So, in this particular case, the first step would be to simply reduce the value of the resistor. Go really low. Go go

**Dave Jones:** hundred ohms and see if that fixes the problem or look at that edge with your scope. It's got a Rigol scope there, more than good enough to look at the the slew rate either the positive and negative. In this

**Dave Jones:** the positive one's going to be the worst cuz it's got the pull-up resistor, but also the negative just to see how fast and sharp that pulse is. That Rigol should be more than good enough of more than good enough to measure, you

**Dave Jones:** know, the tens of nanoseconds or hey, in this case hundreds of nanoseconds are possibly that we're going to get there. Any slow any low bandwidth scope will be able to do that. So, there you go. Hope you found that interesting. If you did,

**Dave Jones:** please give it a big thumbs up and as always discuss down below. Catch you next time.
