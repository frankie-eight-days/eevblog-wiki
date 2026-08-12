---
video_id: XgXwfBTKLGU
title: EEVblog #1181 - Car ECO OBD2 OptiFuel Fuel Saver SCAM!
url: https://www.youtube.com/watch?v=XgXwfBTKLGU
source: youtube-asr
timestamps: {"0": 0, "1": 5, "2": 19, "3": 36, "4": 45, "5": 53, "6": 69, "7": 82, "8": 100, "9": 122, "10": 137, "11": 160, "12": 185, "13": 197, "14": 223, "15": 239, "16": 252, "17": 262, "18": 273, "19": 291, "20": 307, "21": 321, "22": 342, "23": 352, "24": 372, "25": 381, "26": 397, "27": 415, "28": 426, "29": 438, "30": 451, "31": 462, "32": 475, "33": 492, "34": 502, "35": 520, "36": 540, "37": 551, "38": 560, "39": 571, "40": 595, "41": 609, "42": 623, "43": 637, "44": 659, "45": 675, "46": 684, "47": 704, "48": 717, "49": 727, "50": 742, "51": 766, "52": 781, "53": 791, "54": 802, "55": 811, "56": 820, "57": 839, "58": 850, "59": 864}
---

**Dave Jones:** Not sure if this is something I ordered on eBay or not. It's got one of these like straight from China, you know, with the free delivery to your $1 item.

**Dave Jones:** So, not sure if it's something I've ordered or something somebody has sent. Oh, yes. Oh, I remember. I actually ordered this. I have to do a video on it.

**Dave Jones:** Now, what this is is one of these OBD2 fuel saver things. You plug it into your OBD port on your car and it's it's supposed to like talk to your engine management computer and do whatever to increase your fuel economy.

**Dave Jones:** And somebody actually sent in an email for this because they saw it on like Facebook and all the scamiest stuff is on Facebook and it cost like a fortune.

**Dave Jones:** Um it was very expensive that they slick website and everything. So, let's actually look at this link that someone sent me and it looks totally scammy. Check it out.

**Dave Jones:** And EcoFuel, choose your fuel type, gasoline car. Look, it looks the exact one that we got. Watch this. EcoFuel checking three warehouses for available stock. Yeah, I'm sure you are.

**Dave Jones:** Reserving your units because I don't want to miss out. Don't want to miss out. It's it's just an animated gift. They're not really checking any of that. It's One EcoFuel at a 50% discount.

**Dave Jones:** 75 bucks. Pay with PayPal. I'm surprised they don't take Bitcoin. Um best seller, two EcoFuels plus one for free. Wow, you're going to want to pony up the small amount extra for the 115 smackers to get three of them when you can buy one for 75 bucks and get three for 115, regularly 450 bucks.

**Dave Jones:** Three-year additional warranty. Look at this. Lock in this great price while you still can. Richard R from It said like three people are currently uh in the checkout process and stuff like David M in Palm West just bought one Eco Fuel and these this just keeps popping up.

**Dave Jones:** This is This is hilarious. But you can see why it just seems like completely scammy. Pay with credit card. Yeah, I'm going to whack my credit card into ecofuel24.pro.

**Dave Jones:** Someone just bought Andrew Long just bought five units and they claim all sorts of stuff at remaps remapping the car's computer. After driving 200 km it adjusts itself to the car according to the driver's habits and all that sort of jazz and but as it turns out it was the really expensive one is exactly the same as this one I got on eBay for like five bucks delivered.

**Dave Jones:** Fantastic. Can you get the patent for it? Anyone? Bueller? It's got the patent number. I don't think so. I expected just there to be nothing in there but sure enough they actually have it it looks legit and they've rubbed the numbers off the micro there so you can't see everything and I have actually mapped out these pins on here and they are the correct pins.

**Dave Jones:** 15% fuel saving, two year warranty. Fantastic. This one's actually done by a company called Nakay also on the plastic enclosure as well and it is a complete and utter scam.

**Dave Jones:** It does not do anything at all. Instructions are really quite vague. It just says press the reset button for 5 seconds after plugging in release the button just wait for a short while it'll communicate a establish connection but it doesn't actually tell you that the button's actually hidden inside here behind here and there's one little hole for the LED but it's actually got three LEDs in there three indicators so I I

**Dave Jones:** don't know there's no other details in here apart from how to find your OBD-II connector so yeah, that's it. But look at how many cars it's compatible with. Of course it is, because it doesn't bloody talk to them.

**Dave Jones:** All right, let's power this turd up and see what happens. Our 12-V power is this pin here, and it's supposed to be these two pins up here, four and five, but these aren't actually joined on the board.

**Dave Jones:** They go off to different places. We'll have a look at the board layout in a minute. Let's power it on. And we've got our LEDs. And it's actually drawing a fair amount.

**Dave Jones:** Geez. 50-odd milliamps. And if you put that on there, you can see the LED through there, but you can't really see the other one, so, you know, it's really pretty dodgy.

**Dave Jones:** Um but you can see like it's trying to connect even though we've got nothing hooked up to it. It's just fl- it's flishy-flashying, and like there's no instructions as to what that means, but like, you know, to the casual observer, it looks like this is doing something.

**Dave Jones:** And if we hook it up to just a CAN bus demo that's outputting like just a demo signal, it does exactly the same flishy-flashying. Granted, this is not going to simulate the data that's inside the car, but it doesn't matter cuz this is a complete scam.

**Dave Jones:** And there's another actual bus in there which is called the K-line, which is on the two pins next to it, and that's an older system, I believe. I don't know the exact details, but the CAN bus is the modern one.

**Dave Jones:** Now, it does actually seem to have like different modes. You just saw in that video clip where it actually turned this LED off, and it did that for a while, then it switched it back on, and then the yellow LED in the center here would like come on for like 5 seconds and then turn back off for like 20 seconds.

**Dave Jones:** And now, just magically, it's come back on, and it's connected, I guess, because they don't give you any instructions, even though I've got a completely fake CAN bus here.

**Dave Jones:** And of course, if you disconnect it, it it makes absolutely no difference. So, it does the same sequence regardless of whether or not it's sitting here with no CAN connected, whether or not it's got like just some sort of data pulsating on the CAN bus, or whether or not it's in your car.

**Dave Jones:** So, here's the CAN bus on my Toyota Corolla just under the dash here. I'm just going to plug it in and see if it does any difference in the little light show that we got.

**Dave Jones:** And that's with the ignition off. All right, let's turn the ignition on. So, I press the reset button, and it's doing exactly the same sequence as what's on the bench.

**Dave Jones:** The ignition is on, so I'm following the instructions, and it does diddly squat. Anyway, I'll wait a minute, and if I start the car up, it's going to do exactly the same thing.

**Dave Jones:** So, the way these scams work is that they give you a fake little light show there, and they pretend that it's connecting to something, when in fact it's not.

**Dave Jones:** It's doing diddly squat, cuz how do you support all these different, you know, dozens of different model brand cars, let alone all the different models with all their different ECUs and everything else.

**Dave Jones:** It's complete and utter and they combine it with some, you know, slick marketing to make you want to buy the thing, but even for five bucks delivered on eBay, it's still ain't worth it.

**Dave Jones:** Because it doesn't do anything. It's not even talking to the computer. Uh yellow LED is now switched off, and it will hopefully come back on for the Yeah, there we go.

**Dave Jones:** Comes back on, flashes for a little bit. It does exactly the same sequence as what it does in the lab. Surprise, surprise. Oh, look. Look, it connected. It connected in quote marks.

**Dave Jones:** What a load of BS. Now, CAN bus is a differential signal which is actually terminated with 120 ohms on either end. And if we have a look at the CAN signal that we're actually generating here, it's just a test signal.

**Dave Jones:** You can see that here's the ground here and it's centered around 2 and 1/2 volts here. And that's your positive and negative line. They're just a classic differential signal.

**Dave Jones:** See? Direct opposite. So, the CAN device in this case, our little fake fuel saver has to actually listen to the bus and then try and do arbitration on the bus to be heard and then to be able to once it does that, it actually transmits something.

**Dave Jones:** So, how can we be sure that this thing's not talking to the CAN bus? Cuz really we'd need like a proper ECU connected or a accurate ECU emulator and we'd need to sit there and monitor this in real time over a a fairly decent length of time to see if it actually transmits anything to the CAN bus at all.

**Dave Jones:** Well, we don't need that because let's take a look at the board. Okay, here's the high CAN high and CAN low pin, okay? Well, it might look like they're routed out.

**Dave Jones:** Look at this, it's going through a 10K resistor here over to a pin. This one, the negative here, is going through a 10K resistor over to under there somewhere.

**Dave Jones:** It's got to be connected to a pin, doesn't it? Well, the first thing is that you don't put two 10Ks in series on a CAN bus. It's terminated in 120 ohms on the bus.

**Dave Jones:** Lower than that because it's like each end or whatever. So, like it's just not even if this thing wanted to drive the CAN bus and could, it couldn't do it because the two 10K series resistors wouldn't provide the drive capability in order to go onto the bus, but have a look down here.

**Dave Jones:** Let's just Should we zoom in a bit closer? What What What What The silk screen is over the pad. That There is no solder on that pin at all.

**Dave Jones:** It is not connected cuz the pad was not exposed and that is the That is the line leading to the CAN high line. Half of these pins aren't actually connected to the board.

**Dave Jones:** So, you don't need a simulator or any monitoring at all to know this thing just physically cannot connect to the CAN bus. It's a scam. So, they're actually doing a rather poor job at this.

**Dave Jones:** I'd at least would have connected it to the CAN bus even if it didn't do anything cuz then you would really to debunk this thing and call it a scam, you would have to, as I said, monitor that CAN bus in real time, have a a simulator or emulator or whatever for the ECU and you'd have to see that it actually did it actually transmit something and that's actually quite a a

**Dave Jones:** complex and involved thing to do, especially if you want to, you know, test it over hours cuz it might sit there monitoring for hours being uh gathering all this data and only then might it actually start talking to the ECU and trying to program something, but I like they didn't even go to that sort of effort.

**Dave Jones:** So, I didn't know why they even why they bothered with this sort of complexity at all. It's just ridiculous, but they've deliberately This is done at the PCB design level.

**Dave Jones:** You deliberately mask over those pins so they're not even connected. It's just nuts. Got a 5-V regulator here, a couple of here to drive the LEDs, and that's and a button to do a fake reset on the thing, and it just goes through a light show sequence.

**Dave Jones:** That's it. Just designed to con people into thinking that it's connected. It doesn't even show these LEDs. Like, it's only got the one hole for this LED here. It's just an absolute boondoggle of a of a device.

**Dave Jones:** The problem with this sort of things people want to believe in this sort of stuff. It's like the audio fool, audio file, you know, uh products that don't do anything.

**Dave Jones:** It's like, if you pay like $5,000 for an IEC power cable to hook up to your amplifier, so that's going to increase the sound stage and the presence and all that other then trust me, you're going to hear the difference because you paid five grand for that thing.

**Dave Jones:** You will hear it. Likewise, if you pay for one of these uh fuel saving devices, there's a very good chance that you're going to see fuel savings because you believe in it, and that's you're going to like your mind's just going to go, "Oh, yeah, it's like it's giving me an extra, you know, mile per gallon or whatever." I converted for you Yanks there, you know, liters per 100 Ks here.

**Dave Jones:** Because they don't do controlled proper controlled testing, they've got no way to actually back that up. So, you'll get the positive reviews on the website. There'll be a few negative ones as well, of course, but people just ignore those and they'll look, Joe Bloggs got like an extra couple of miles per gallon or something like that.

**Dave Jones:** So, it's got to be a winner. It's got like four stars on Amazon or something. And of course, the company will add in fake reviews as well, and these things just they can't do anything.

**Dave Jones:** It's not even connected. So, it doesn't even like monitor the CAN bus for like signals so that at least changed it when you turn the ignition on. The light sequence is just the same either way.

**Dave Jones:** Also, don't fall for these scams. When you see websites with the look and feel like the one we showed at the start, you just know these things are a scam.

**Dave Jones:** Now, that's I said it before, there might be genuine ECU things out there that can actually and I know there are people out there who modify, uh, you know, their ECU by writing various things.

**Dave Jones:** You can clear errors and do all sorts of things that might help improve it. And I'm not saying that's not possible because, hey, the manufacturers do it, right? It's all It was part of that emissions, um, scam thing where they would have different modes and they reprogrammed the ECU to pass the emission standards and stuff like that.

**Dave Jones:** So, you know, it is possible, but these devices here are a complete and utter scam. They're not even bloody connected. Unbelievable. So, don't fall for it. Anyway, I hope you enjoyed that video and found it useful.

**Dave Jones:** If you did, please give it a big thumbs-up and as always, you can discuss down below. Let us know if you actually do this legitimately on cars cuz I'm sure I know that there's a lot of my audience who do automotive, uh, stuff and things like that.

**Dave Jones:** So, you know, it certainly is possible, but not with not with one of these. Unbelievable. Catch you next time.
