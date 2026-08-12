---
video_id: -04CQ0Mug1o
title: EEVblog #166 - HP Agilent E3610A Lab Power Supply
url: https://www.youtube.com/watch?v=-04CQ0Mug1o
source: youtube-asr
timestamps: {"0": 0, "1": 38, "2": 69, "3": 86, "4": 110, "5": 131, "6": 147, "7": 173, "8": 203, "9": 230, "10": 263, "11": 286, "12": 313, "13": 342, "14": 370, "15": 400, "16": 434, "17": 447, "18": 486, "19": 507, "20": 545, "21": 578, "22": 604, "23": 636, "24": 662, "25": 682, "26": 717, "27": 751, "28": 804, "29": 833, "30": 860, "31": 887, "32": 913, "33": 947, "34": 975}
---

**Dave Jones:** Hi, welcome to the AEV blog and electronic engineering video blog of interest to anyone involved in electronic design. I'm your host, Dave Jones. Hi, it's product review time again and might actually be considered a bit of a second-hand, almost retro product review. What is it? It's the Hewlett Packard / Agilent E 3610A bench power supply. Let's take a look at it. Now, I said it was retro because this one is actually branded Hewlett Packard. It comes from the Hewlett Packard days. The model's been around for all the series of these bench power

**Dave Jones:** supplies has been around for a long time and I believe you can still actually buy it under the Agilent name and it comes in several different types. This is the single output type as we'll take a look at, but it's also available in a dual and I believe a triple output as well and you can usually find quite a few of these on eBay. Now, if you're after quite a you know, if you're after a top quality bench power supply for your lab, it's pretty darn hard to beat Hewlett

**Dave Jones:** Packard / Agilent supplies. They make some of the best bench power supplies in the business. They're not cheap, but as I said, you can pick them up on eBay for reasonable amounts of money. Now, this one I've actually got here is the 110 volt version designed for the US market and other markets that use 110 volts.

**Dave Jones:** But of course, here in Australia, we're 240 volts. Now, unfortunately, there is with these series HP supplies, there is no switch on the back to actually switch through to you know, make it switchable from 110 to 240 volts. So, unfortunately, I'm going to have to crack this open and see and that's what this blog's really going to be about.

**Dave Jones:** It's not so much a review of this, it's going to be to see if I can modify this at all or easily anyway to do 240 V operation here in Australia, cuz hopefully inside there'll be like a little jumper switch, or there'll be a on the main board, there'll be a transformer tap, or something like that, that I can just easily swap over to 240.

**Dave Jones:** Here's hoping, but let's crack it open and find out. And just before we take it apart, I thought I'd power it up, cuz I do have a 110 V transformer here in the lab. So, I thought I'd power it up, and it seems to work just fine. And as you can see, I've set it to 10.0 V, also I'm getting 10.02.

**Dave Jones:** And we wind it down, and we uh you know, 2.19, 2.20. It's pretty darn close. And uh if we use the constant uh current, if we switch it around here to amps, and we plug it in, and it's uh currently set to uh 0.25 amps for constant current, and there it is, 252 milliamps. So, that seems to work just fine.

**Dave Jones:** And just a few tips, if you're after a really good bench power supply like this, uh I highly recommend one that's got a low voltage range. This one's actually got two ranges. They call it 2 amps and 3 amps here, and it's got a real meaty push button switch on there, none of that soft button rubbish. And uh this one has a nice low voltage range of 0 to 8 V uh at 0 to 3 amps, and 0 to 15 V at 0 to 2 amps. So, uh what that allows

**Dave Jones:** is, you know, if you get one of those uh cheap Jaycar power supplies, or something, the most common ones are like 0 to 30 V, and really, they're not much, you know, they're just a too wide a range for general electronics uses. Um there's very few reasons you need to go above 15 V. So, a 0 to 15 V supply is a beauty. And it's got constant current uh mode as well, so it's got current adjust and voltage adjust. And this one actually allows you to actually set the

**Dave Jones:** current here, so you're holding the button, and you can set the current without having to short out the output, which is the traditional way that you set the constant current limit on a power supply. So, it's nice if it has a constant current set button as well. Uh But, one of the most important things people uh often uh miss on a good lab bench supply is it must have a nice multi-turn pot. Now, this These Hewlett-Packard ones have a nice 10-turn pot. And as you can see, I

**Dave Jones:** can just tweak that, and I can really finely tweak. I can just touch the knob, and I can tweak that down to 10 mV resolution, no problems at all. Now, if you got one of those cheap uh bench power supplies with just the uh voltage and the uh current like it'll just have like a coarse and maybe a fine voltage current adjustment, they're only single-turn pots, and they're no good.

**Dave Jones:** You can't get the resolution you need on that. And this has a 10-turn pot for the current set as well. So, beautiful. And those pots are uh quite expensive, so you A lot of power supplies you'll actually um you can pay extra to get the 10-turn pots, but it's well worth it. I highly recommend it. And also, it's got an earth output as well. This one's fully floating. Um it's nice if you get the dual one with the negative rail as well, but this is a single output. So,

**Dave Jones:** it'll do what it'll it'll do uh the general job. And if you got a second one, it's a single output, because they're floating outputs, you can They're not mains earth connected unless you link these two together, the ground and the mains earth, then you can actually join power supplies in uh in series to get um that positive and negative supply. So, if you only got a single output supply like this, it it doesn't matter. You get a second supply, bingo, you've got a positive and negative one. And the best bench power

**Dave Jones:** supplies you can get like this one are the are a linear supply. They're not a switch-mode supply, so that gives you much better noise and ripple performance on the output that you really just are very hard pressed to match with a switch-mode power supply. But, because it's linear, it needs a big heat sink on the back, and it is a bit wasteful in terms of energy consumption for a given output power. But, who cares about that? Noise and ripple is much better. Now, I've got a couple

**Dave Jones:** of switch-mode lab supplies up here. I've got this PowerTech big 40-amp uh one here, which is to get that in a linear supply, 40-amp output up to 15 volts. That's, you know, quite a beefy linear supply. So, it's not a bad option for a switch-mode. And this one up here is a an Eltronics kit as well, and it's a switch-mode supply as well, but its noise and performance figures aren't nearly as good as a good-quality linear bench supply like this Hewlett-Packard one. And the linear ones

**Dave Jones:** are far more reliable, as well. Now, as nice as this power supply is, it's not It's not the perfect bench supply, because the perfect bench supply would have an output load switch here to switch the output off and on. But, unfortunately, these series of Hewlett-Packard ones don't have that capability. Now, the interesting thing to note about the construction of this thing is that it doesn't have any screws on it at all. It's got these little tabs here like this that you can see. So, it looks like these uh It looks like the

**Dave Jones:** back panel, at least, flips off, and maybe the front panel, as well, cuz there's a couple of tabs down there. So, let's give that a go, shall we?

**Dave Jones:** Yep. Yep. There we go. That's it. Small screwdrivers to go there and bingo, that's what pops off and it looks like there are no extra uh screws on there. So, it looks like I think that top cover is just going to pop up Yeah, the top cover pops off. So, I've got to pop off Looks like I got to pop off the front panel as well.

**Dave Jones:** So, let's give that a go. Oh, yeah. Yep. All right. Hey, there we go.

**Dave Jones:** And tada! Too easy. Wow, it just pops off and let's see if we can get this lid off. Tada! There it is. Beautiful. I love it. And that was very nice indeed. I love how it just popped off and this uh front panel just uh hinges on the wires here, which we'll take a look at, but there's the big uh transformer as you expect in any linear supply. There's the output transistors there. They're a 2N6056 made in Mexico in a TO3 package just hooked onto the heat sink here. Some

**Dave Jones:** lovely uh grounding wires just going over there and uh the board looks very nice indeed. As you can see, there's the main uh filter cap and you'll notice that they've got the uh they've got the silastic rubber goo there on the cap and it's also on this side here as well and that's a nice little touch to ensure that that capacitor doesn't uh vibrate and uh and fall off and cause damage. So, they've got some more of that on uh the cap over here. So, nice little attention to

**Dave Jones:** detail there. A couple of smaller heat sinks. Pretty standard. It's a very sparse layout. Some of the standard op amps there I recognize. That's an LF 442, LM393, LF411. So, pretty basic stuff really. But, that's what you expect in these standard linear supplies. There's nothing fancy at all.

**Dave Jones:** And they've got some nice 10 turn pots in here, too. They're obviously to tweak and adjust the output range. And as you can see the front panel here just sort of hinges off like that. And it's really really is quite nice. There's those There are those lovely 10 turn pots. They're actually Bourns ones. So, they're super high quality. But, you know, you'd expect that cuz you pay top dollar for a HP HP lab supply. So, you'd expect top quality 10 turn pots that'll last you a

**Dave Jones:** lifetime pretty much. It's There's another HP branded board in here. And it's got some They They look like little custom custom devices. I'm not sure. I'll have to have a look at those. But, they're obviously just driving the display there the analog They're probably like an analog to digital converter. And then and then a display driver as well. There's another couple of 10 turn pots up there for adjustment.

**Dave Jones:** But, I like it. Nice little cable looms. And it's just quite nice construction. Beautiful. And interestingly, it looks like there's nothing holding this board in at all. Ta-da! There it is. Look at that. It just comes out as one complete unit.

**Dave Jones:** Beautiful. Now, as for modifying this for 240 V operation, I don't see any internal jumpers on the board at all to actually do that or taps on the transformer that are easily accessible cuz here's the input mains wiring and it goes all the way down to a real main switch on the front and then back and then it looks like straight into the transformer there. So, unfortunately, I can't access the bottom side of that transformer there because it's looks like it's not trivial to take this thing out because if you look down

**Dave Jones:** in there, you will see uh Where is it? You'll see that the output taps on the transformer are soldered directly onto the board down there. So, I could undo these four screws here, but really the transformer is still permanently attached via those direct solder connections. So, it looks like I'm going to have to actually take off this back panel here and to do that I'm going to have to take off these TO3 transistors. I'll have to unscrew and unsolder those from the board to get at

**Dave Jones:** the transformer. What a bummer, but oh well, let's do it. So, there you have it. We've got the heat sink out and I'm massively disappointed. Look, the wiring goes directly into the transformer. There are no solder tabs on that at all. There are no taps so that I can change it to 240 volts. So, what were HP thinking when they did this? They obviously use a different transformer for each market. They could have just had one with taps, surely.

**Dave Jones:** Well, there you go. That's a real bummer. I was hoping there'd be a transformer tap in there that I could switch it to 240 V so, but no, it looks like they use a totally different transformer. That's why it's got standard stamped on it because on the actual transformer itself cuz this is the standard model. I think it's option like 03 or something if you want the 240 V model. So, just be aware of that when you're shopping around on eBay or something trying to buy these babies.

**Dave Jones:** They're a really nice supply. recommend you pick one up if they're at an affordable price. But unfortunately it doesn't have a load switch on it, but hey, that's not a killer. You can't beat a quality HP lab supply on your bench. Go for it. And because I don't remind people of this very often, in fact I don't think I ever have, if you're watching this on YouTube, remember to subscribe. There's a subscribe button up there around about there somewhere. If you're watching this on YouTube, if you're watching on

**Dave Jones:** eevblog.com, go over to my YouTube channel. There's a link somewhere over that side of the page that allows you to do that. And when you subscribe, it gives you the option to get automatic email as soon as I upload a video onto YouTube. Because if you don't know, I upload my videos onto YouTube first before I make it through to eevblog.com and the RSS feed and the iTunes feed.

**Dave Jones:** Sometimes 12 or 24 hours before they actually make it to that site, they're already on YouTube. So, if you want to get my videos first, that's the way to do it. If you wonder how everyone gets the first comment on there, people love to get the first comment. That's how they do it. They get signed up for the automatic email. As soon as it's public, you get it. Beauty. And also if you YouTube also have an RSS feed. So, if you want to do it that way as well

**Dave Jones:** through the YouTube channel, there's buttons over here on my main site eevblog.com. Talk too hard. There's so many options. There's an iTunes option button there somewhere as well if you got your iPhone. I do a podcast version. It's lower resolution than this one. The YouTube version is HD. It's a 1280 by 720. The iTunes version is 270 is 480 by 270. But a lot of people, a couple of thousand people do that option. So please and also don't forget to give thumbs up for the videos if you

**Dave Jones:** like them and comment as well. That's down below. Literally speaking. Almost forgot one thing. In case you weren't aware, I'm now a full-time video blogger. This is my full-time gig. And to pay for it, help pay for it anyway, you'll hear more about this in the future. But to help pay for it, I am accepting recurring PayPal donations. So if you go to eevblog.com, round about there somewhere there's some buttons that'll allow you to sign up and help pay for this thing so that I don't have

**Dave Jones:** to accept sponsors and the wife won't make me go back to work to earn a real living. Thanks. See you.
