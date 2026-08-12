---
video_id: EVcxrYnY1ok
title: Guest Video: TGSoapbox - RF Crystal Detectors
url: https://www.youtube.com/watch?v=EVcxrYnY1ok
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 47, "3": 59, "4": 91, "5": 113, "6": 135, "7": 162, "8": 178, "9": 195, "10": 220, "11": 234, "12": 263, "13": 274, "14": 295, "15": 319, "16": 344, "17": 372, "18": 389, "19": 410, "20": 426, "21": 456, "22": 479, "23": 499, "24": 523, "25": 534, "26": 553, "27": 567, "28": 592, "29": 615, "30": 640, "31": 666, "32": 695, "33": 711, "34": 738, "35": 762, "36": 779, "37": 800}
---

**Dave Jones:** Well, good morning. It's Christmas Eve here in Seattle and it's just below freezing, so maybe we might get a little bit of snow this evening, white Christmas tomorrow. Anyway, I wanted to do a quick video to submit to Dave Jones' EEVblog, hopefully for inclusion

**Dave Jones:** in his holiday videos. Now, the video in question that I'm doing here is responding to a viewer's question on my channel where they looked at a power meter I had and wanted to know, with that power meter, how they would go about working out the sensitivity of a crystal detector.

**Dave Jones:** So here is a set of crystal detectors that I have. This one is an 8470B and it's an N-type connector and it goes from 10MHz to 18GHz. The 8472B is here in the middle and it's an SMA-type connector and it goes from 10MHz to 18GHz as well.

**Dave Jones:** And then on the right here is an 8473C and it is a 3.5mm connector, which is physically the same as an SMA, but they're actually different because of the tolerances. So if you're ever using these things, mostly you will have SMA cables. So it's a good idea to have a little saver in the connector there

**Dave Jones:** so that you wear out this saver and you can throw that away and replace it. Anyway, this is a 10MHz to 26.5GHz crystal detector. Now what these crystal detectors do is they make use of the square law area of these Schottky diodes. And what that means is that below

**Dave Jones:** a certain power, when you put the power into a crystal detector, the slope of a line that shows the correlation between power and the output voltage becomes proportional and linear. And the viewer, let me move these out of the road here and we'll zoom out a little

**Dave Jones:** bit, the viewer wanted to know how to work out what K is here. And K is the sensitivity of the detector. And so if we look over here, you can see how the power input relates to the detector law. And what we're trying to do is get a linear region here, and you can

**Dave Jones:** see this linear region part here. And so they call this, based off this equation here, they call it the square law region because alpha here becomes 2 and hence squared. So when you work out what the equation is, it's the voltage out of the crystal detector is the

**Dave Jones:** sensitivity K, square root of the power squared, which is just the power. So you become linearly related to the power and you can see the voltage, you can see that the lines up here are very linear based on the power and the frequency, 2 GHz here for the voltage that's

**Dave Jones:** being detected. And so he wanted to know how to specifically get that calculated voltage for K. Now, if we jump out here and take a look at the specs, you'll see that typically the sensitivities are quoted in millivolts per microwatt. And so the K value as a unit

**Dave Jones:** of measure, as far as I'm aware, is not well used. So anyway, on most of the data sheets, you'll see sensitivity as millivolts per microwatt in that square law region. And what we want to do is to take these detectors and go ahead and calculate their sensitivity.

**Dave Jones:** So to do that I'm going to need to use three pieces of gear actually. So let's zoom out a bit so you can see these things in a row. The three pieces of gear are going to be a signal generator that's capable of delivering minus 20 dBm at, and we'll pick a middle frequency

**Dave Jones:** of 10 GHz. I'm going to use a power meter that enables me to check the power at the measuring point, and this will be the measuring point here where I have my cable connected to the N-type connector here. And I want to set this to be minus 20 dBm.

**Dave Jones:** And then we'll use a digital multimeter where we can connect it to the BNC connector here on the end, which will show us the voltage that will occur. So let's go set this up. The first thing we're going to go do is set up the signal generator.

**Dave Jones:** Okay, so the signal generator I'm using is my 8673B, and I primarily use this as a local oscillator for a microwave converter. But I'm going to use this particular case because this has a vernier control on the output, and it enables me to very finely adjust the power.

**Dave Jones:** I thought about using my 8340B, which I have here, but unfortunately minus 20 dBm is an attenuator step, so it's very difficult to get the accuracy to get minus 20 dBm. So let's go in and we'll select the range of minus 10 here.

**Dave Jones:** And if you see the vernier here, you can see in the little dial that as I move that back and forward, we're going between minus 10 from that range, so that's minus 20 dBm, up to 3 dBm. So minus 10 dBm would be there, and that lets me go and get

**Dave Jones:** the accuracy at that point. I could also go down a range and then just sit here and play around here. Now I want to set my output to be 10 GHz. We have our 10 GHz there, we have our automatic level control as being internal, so that's a good enough start for

**Dave Jones:** us to go and start measuring the power that we're going to deliver out of that n-type connector. The next thing we need to do is set up our power meter. So here is our power meter, so the first thing we'll do is we'll do a pre-select, so we'll make sure that it's

**Dave Jones:** all set up. We're going to go in and configure it. So these power meters, in this particular case it's an E4418B, you can use the 8400 series power sensor. And this is an 8481A power sensor that goes from 10 MHz up to 18 GHz.

**Dave Jones:** And you can see that I have the power factors here. Now this has been off to a key site and has been calibrated, so it should be reasonably accurate, given that these things are an open-loop power meter. So unlike the 432s or the crystal detectors, which give you an absolute value of the power they're

**Dave Jones:** actually measuring, these work on the accuracy of the underlying power reference here. So this is a 50 MHz 0 dBm power meter, 1 mW power meter reference. So we're going to put this on here, and then we're going to zero that, so that this thing knows what the 0 dBm is.

**Dave Jones:** So we'll just screw this on here. Now, I'm going to go in and select a table, and make sure that you can see here that I have my 8481A table. So that's taken all those calibration figures off the side of the unit, I've entered those in.

**Dave Jones:** So now that we've got that set, I can come over here and go to zero, and we're just zeroing out the thermocouples. We've got one that will measure the ambient temperature, we've got one that will measure the RF that's coming in. And so now we can just go in and calibrate that, and you can see that the power

**Dave Jones:** reference turns on here. And there we go, we're calibrated. So now the next thing I need to do is actually put a frequency in, and I know that we're going to be working at 10 GHz, so let's go in and set that down to 10 GHz.

**Dave Jones:** And here you'll see now the calibration factor is set for 94.5%. And this is how the unit knows what the losses are going to be in the detector. So now that we're set up there, what I need to do is just go and hook

**Dave Jones:** this up to our cable, and we'll now measure and get our minus 20 dBm. So you can see, now that I'm measuring minus 12, so I'm just going to grab that vernier and start taking that down until we get to about minus 20.

**Dave Jones:** And we're going to try and get as close as we can to that minus 20 dBm, and we're going to try and get as close as we can. There we go, that's nice. And it'll bounce around a little bit there, but a couple

**Dave Jones:** of hundredths of a dBm, I'll take that. Alright, so now we just need to go back to our crystal detectors and we can start doing our first measurement. Okay, so we have minus 20 dBm coming out of here, so the next thing for me to do is to hook this up to the crystal

**Dave Jones:** detector and to the DMM, and that's a Rigol DM3058. So let's just hook this up, and now we're going to be reading a voltage here, somewhere in the millivolts. So we're going to be reading a voltage here, somewhere in the millivolts. So what I have is I have a

**Dave Jones:** little app here that I wrote to pull the data off the Rigol, because it's in a sort of inconvenient place. And so here we have 6.69 millivolts, 6.7 millivolts. So let's just say that that's going to be our value. Now if you remember, the sensitivity was going

**Dave Jones:** to be, or the voltage spec was in millivolts per microwatts. And so it's going to be 6.7 millivolts divided by 10 microwatts, because we're at minus 20 dBm. So we're going to get 0.67. And if we come back here and zoom in, here you'll see that for sensitivity it's

**Dave Jones:** greater than 0.5 millivolts per microwatt. So we're greater than that at 0.67. So we're in spec, and that's given us the sensitivity. Now if we want that K factor, we should go in and bring all of those up to volts and watts. So that's 1,000 and 1,000,000.

**Dave Jones:** So basically we're just going to multiply this number when you do the math by 1,000. So let's go and see. And it's about 670. So to work out from this formula here, using the crystal detectors in that sensitivity region, to get K was fairly straightforward.

**Dave Jones:** And for this particular sensor that I have here, it's about 670. Now these are not metrology grade connectors, there's some loss in the cables, all that sort of thing. But that takes you through the process of how to go and get that. So I could go and do it again using each of these,

**Dave Jones:** or I could go and try a different frequency. Remember, the sensitivity will change based on the frequency. Not by a lot, but it will change. So if you're going and needing this value for 18 gig, you need to do it at 18 gig and measure it, and then you can work

**Dave Jones:** back. Anyway, I hope you found this interesting, and I hope this video makes it onto the EEVblog channel. If it doesn't, it'll still make it onto my site, as Dave said. Anyway, check below, my channel is TG Soapbox, and come on over. I have a bunch of videos about old

**Dave Jones:** HulaPackard test gear, or old test gear, and how you can use it and how to repair it. Anyway, look forward to seeing you in the comments. Catch you later. Bye.
