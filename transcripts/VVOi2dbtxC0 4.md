---
video_id: VVOi2dbtxC0
title: EEVacademy #6 - PID Controllers Explained
url: https://www.youtube.com/watch?v=VVOi2dbtxC0
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 26, "3": 41, "4": 54, "5": 69, "6": 81, "7": 96, "8": 110, "9": 118, "10": 127, "11": 138, "12": 153, "13": 165, "14": 192, "15": 206, "16": 221, "17": 238, "18": 261, "19": 274, "20": 286, "21": 304, "22": 312, "23": 326, "24": 341, "25": 352, "26": 371, "27": 387, "28": 409, "29": 430, "30": 442, "31": 459, "32": 466, "33": 478, "34": 496, "35": 518, "36": 529, "37": 541, "38": 549, "39": 560, "40": 582, "41": 594, "42": 604, "43": 613, "44": 626, "45": 639, "46": 651, "47": 670, "48": 691, "49": 702, "50": 717, "51": 727, "52": 747, "53": 763, "54": 773, "55": 796, "56": 809, "57": 826, "58": 834, "59": 845, "60": 860, "61": 880, "62": 893, "63": 903, "64": 916, "65": 927, "66": 941, "67": 959, "68": 972, "69": 991, "70": 1013, "71": 1033, "72": 1046, "73": 1055, "74": 1065, "75": 1076, "76": 1092, "77": 1108, "78": 1120, "79": 1132, "80": 1141, "81": 1152, "82": 1167, "83": 1182, "84": 1191, "85": 1206, "86": 1216, "87": 1228, "88": 1238, "89": 1252, "90": 1267, "91": 1282, "92": 1294, "93": 1315, "94": 1337, "95": 1353, "96": 1366, "97": 1390, "98": 1404, "99": 1433, "100": 1442, "101": 1462, "102": 1485, "103": 1495, "104": 1514, "105": 1529, "106": 1540, "107": 1558, "108": 1570, "109": 1587, "110": 1601}
---

**Dave Jones:** Hello everyone. Let's talk about the coolest topic ever, maybe. Basic control theory. And what we're going to do is we're going to talk about PID controllers and introduce the most fundamental concepts of control theory.

**Dave Jones:** This is the start of a a few control theory videos. So, any feedback would be really appreciated. So, let's start. So, control theory is something fundamental to most things, but it isn't always on the surface evident.

**Dave Jones:** Rockets are controlling for their their pitch and yaw and other variables for stability. Uh ovens control for their temperature and cars control for all kinds of things, but one of the one of the obvious examples is cruise control, which controls for speed.

**Dave Jones:** Even you in your day-to-day activities are a basic controller or at least a whole ton of them. When you walk to the shop, let's say this guy here, Bob, walking to the shop with his GPS, he gets his coordinate from his geocaching GPS.

**Dave Jones:** Um it just gives you a coordinate and he knows the coordinate of the shop and he can um subtract the two, get the distance, and that distance to the shop is the error, which is basically the fundamental concept of control theory.

**Dave Jones:** Control theory is controlling and minimizing error. So, there's a few things about error. Error is the set point, which is where you want to be, minus the feedback, which is where you are.

**Dave Jones:** And this is an example with the position, but it doesn't have to be the case. It could be with speed or it could be with acceleration or magnetic field strength or energy, power, all kinds of variables can be controlled using the minimization of error or control theory.

**Dave Jones:** An error of zero would often be the position called the steady-state position, and it is usually the goal. In cases where it's not the goal, I'm sure they'd be very happy with zero error anyway.

**Dave Jones:** After getting back from the shop, Bob realized that he'd eaten far too much chocolate, felt guilty, and bought a treadmill. So, on the treadmill, he realized this is another element of control theory.

**Dave Jones:** He's controlling the speed of his feet." But, what is he actually controlling? What is he looking to do? Well, he's not actually controlling his speed, he's controlling his um position.

**Dave Jones:** He wants to be in the center of the treadmill, and if he starts drifting back, he knows he's not going fast enough, and if he starts drifting forward, he knows he's he knows he's going too fast.

**Dave Jones:** So, that is if his actual position is greater than his desired position, then he is he's got an error less than zero. If his actual position is less than his desired position, then his error is greater than zero, and he should speed up.

**Dave Jones:** So, what do we do with this error? Well, we use this error to control effort, and effort is basically how much effort Bob's putting on on the treadmill. If he's not putting on in enough effort, he'll fly off the back and hit his head.

**Dave Jones:** If he puts too much effort in, he runs into this stand thing here at the front, which So, control theory is evident in basically all elements of things you do, from running to walking to your body heat regulation, and while it may not be the uh a PID controller or any like formally represented mathematical controller, it is explainable through basic control theory concepts.

**Dave Jones:** Most control theory textbooks and lectures have diagrams like this throughout the entire book. This is a basic diagram which represents the two previous examples, where the set point is the position Bob should be, and the feedback is the position Bob is.

**Dave Jones:** Um he gets that feedback from his eyes, and he uses his legs to move him to different positions, and his brain controls his legs, and he looks at the error to make decisions with his brain.

**Dave Jones:** So, if we go through that like this, you see why it's called a control loop, because it's a loop. It just goes round and round and round and for control loops in digital systems, it's usually a periodic loop.

**Dave Jones:** It goes round once every second, 10 milliseconds, something like that. Which then makes very fast and sensible, hopefully, adjustments to the system so that the system is controlled. When Bob was walking to the shop, his his position was going up the whole time, but his error was going down and that is what we want to do.

**Dave Jones:** We want to minimize error. So, up the top here, his position is equal to the initial error, if you look over here. And his error is actually the distance to the shop initially.

**Dave Jones:** So, in this case, the error units are in the same units as the position, which is which is much simpler than it could be. Because sometimes you have to convert the units so that they equal each other and they're comparable.

**Dave Jones:** So, one of the most common industry controllers is the PID controller. That's the proportional, integral, derivative controller. And these things are found everywhere from motherboard fan controllers to heaters to balancing Segway things.

**Dave Jones:** They're in all kinds of things and they're quite a primitive controller, but they're really easy to tune and pretty fast to get up and running. So, we're going to talk about that.

**Dave Jones:** Okay, so a PID controller can actually be separated into three different controllers, a proportional controller, an integral controller, and a derivative controller. We're going to talk about a proportional controller's behavior.

**Dave Jones:** A proportional controller is actually analogous to a mechanical spring where the default position is when the spring isn't stretched or compressed and that default position would be the controller's set point.

**Dave Jones:** If the controller the the spring was stretched, then the distance between the set point and the default point is the error. This is the error. When the error is negative, the force is negative.

**Dave Jones:** The controller outputs a force in this case. When the error is positive, then the force is positive, trying to move it back to its set point. Now, you'll notice that there's an equation up this top corner here, and this equation should be quite familiar to many of you.

**Dave Jones:** It's the exact same form as Hooke's law, where Hooke's law is F = K delta X. And delta X in this um is really the difference of positions, but error is a more general way of expressing differences of position.

**Dave Jones:** It's just the difference of an arbitrary unit, which isn't necessarily distance. So, a proportional controller is basically an ideal spring. An integral controller can be used in lots of things, and it's especially useful when you need to have error eventually go to zero.

**Dave Jones:** And these things like there are examples like precision ovens and um anything that balances anything, all kinds of things require zero error because if there is any error, it ends up not performing to spec or ending up halfway uh across a continent if it was a plane, or just it just ends missing its target.

**Dave Jones:** Um So, integral controllers are one of the more useful controllers for in scenarios where you need zero error. Now, we're going to talk about an oven controller. Ovens aren't usually controlled with integral controllers.

**Dave Jones:** They They probably should be controlled with a thing called a bang-bang controller cuz um that is the scenario where bang-bang controllers are basically optimal. But but um for this scenario, because it's simple, we're going to use an integral only controller.

**Dave Jones:** Bit weird, but whatever. Anyway, so in this example, we're trying to heat up this oven, and we're going to do it manually because it's not a very smart oven.

**Dave Jones:** We just have this knob which you can turn, but we've put a thermometer in the oven, and we want to make sure that we're cooking our chicken at Uh no, apparently I'm cooking it at 10° cuz that's what my plot says.

**Dave Jones:** We're cooking our chicken at 10°. All right. Anyway, so initially the oven's temperature is zero because someone put it in the fridge, and that would mean that the error is 10 the set point minus zero the actual point.

**Dave Jones:** So, that's here. Now, if you create get the area of this error here, then that is equivalent to the integral up to time one. So, our effort would be K times the that integral we just had before.

**Dave Jones:** And in this case, the integral's result is just 10, and for simplicity, we're just going to have the constant out the front as one, but this can be anything.

**Dave Jones:** So, initially our control effort U is zero because we haven't actually started the controller, but after time one, we're able to calculate our new control effort, which will be 10.

**Dave Jones:** We then move forward the system by one more second, and the oven is heated up a little bit because we've put a little bit of energy into the heating elements.

**Dave Jones:** Okay, so after the first sample, we're up to this sample two. We're taking a reading at the second second. We now we've realized that the oven has gone up 2°, and that would lower our error by two.

**Dave Jones:** So, it was initially 10°, and 10 minus two is eight. Now, integrals add up areas. That's how they work. And so, the the The of the integral in this case would be 10 plus the area here which is eight.

**Dave Jones:** So, our next control effort for the next period between two and three will be 18. And if you follow this through for a little while, the oven heats up more cuz we're putting more effort in.

**Dave Jones:** We got five and we add the five to the thing and that results in a control effort of 23. 23 is the the area here plus the area here plus the area here.

**Dave Jones:** And the oven has heated up even more at this point and the integral component is actually getting quite large. And notice there's nothing driving the integral component smaller. That's very important.

**Dave Jones:** And it's one of the biggest pitfalls of integral controllers, as we'll see in a moment. So, the oven's temperature is now 9°. We have one more degree to go, so the error is one and we just add that to the the result.

**Dave Jones:** So, that's 24, the effort. And now, we have all that accumulated area here. And we're still probably heating up the oven because even if you dial it up to 11, then it takes ages to heat up.

**Dave Jones:** There is thermal mass of the oven that takes a lot of time to heat up and um that means there's a delay. The integral component has a very high value now.

**Dave Jones:** We're up to We're up to 24 and that means we're going to overshoot our our set point. So, in the next sample, we unfortunately go to neg- we get We end up having an error of -4 because I've overshoot our temperature.

**Dave Jones:** We're at 14° and 10 - 14 is -4. And if you add these areas to the -4 area here, then we end up putting an effort of 20. The slight reduction in effort because this oven has basically no thermal mass, apparently, um results in the error reducing a little bit.

**Dave Jones:** And that again lowers our control effort to 19. And after the next sample, we've finally got zero error, but that's not the end of the story because our control effort is still greater than zero.

**Dave Jones:** So, effort does converge to a value above zero. It It needs to keep heating, but it should be stable at some point, and it isn't yet. At the next sample, we notice it's gone up to one, and that area adds to 20, and at that point the oven's temperature is stable, apparently.

**Dave Jones:** It's the fastest heating oven in the world. It's heated up in 8 seconds. So, really great. Notice that the waveform here ends up going like this a little bit.

**Dave Jones:** And that that trough there here is called overshoot, and this is something very um this is a a problem that integral controllers face. They have a thing called integral windup, and this is the building up of the this area here behind the the current reading.

**Dave Jones:** And there are lots of ways to deal with this. Um many controllers just say, "You will never have more integral windup than value X. It will just limit the the possible um integral value." So, if your limit was was 20, um then this would just limit it to this.

**Dave Jones:** Um and it would never go above 20. We've talked about proportional controllers and integral controllers, and from proportional controllers, we get our response speed, how fast the system will respond.

**Dave Jones:** And from integral controllers, hopefully we get zero error. So, why would we want a derivative controller? It sounds like we've got what we want. Well, not quite. In the scenario where you've got a steady state system, it's reached steady state, and we've got this nice solid line, you want to be able to reject disturbances.

**Dave Jones:** And what is a disturbance? Well, say someone sneezes in front of a pendulum, and then the error goes like this. With an integral controller, it takes a while for system to build up any control effort.

**Dave Jones:** So, the integral controller doesn't really respond well in this scenario at all. With a proportional controller, it does respond, but proportional controllers don't um they don't have the response speed before the the value ends up getting large.

**Dave Jones:** A proportional controller is just a constant times the error. So, what do we do? Well, what we can do is take the derivative. That means the rate of change.

**Dave Jones:** And what is the rate of change when the someone sneezes in front of the pendulum? It's very high. So, with a very high rate of change, we get this nice opposing Well, it could be depending on the sign of the constant.

**Dave Jones:** We get this nice opposing force that as soon as a disturbance occurs, we can resist it and move back to our set point and allow the integral controller to resume its normal business.

**Dave Jones:** Now, there are problems with um derivative controllers, really big problems. And these um mainly the limitations of sensors, um the digi- discretization, and all kinds of things like that mean that any noise on the line, you end up taking the rate of change of noise, which ends up being well, pretty damn noisy.

**Dave Jones:** So, you keep putting control effort in um which which is from the noise, and you don't really want to be doing um this this sort of thing because it ends up causing kind of like a instability in the system.

**Dave Jones:** It makes the system very noisy and audibly noisy in the case of pendulums and and the case of cruise control, the vehicle would be like shaking or something. An example of this equation is actually in a damper.

**Dave Jones:** A damper is something that absorbs energy, and it stops um endless oscillations in things. And this is actually the same form um the equation is in the same form as the damper equation.

**Dave Jones:** That's the equation that represents this mechanical element. And these are This is a uh fundamental element in car suspension. If you just had a spring, you'd be bouncing all over the place.

**Dave Jones:** If you um add the damper, you can make sure that your car kind of smoothly smoothly copes with shock as it did with disturbances before. The other thing that the derivative controller does is absorb energy.

**Dave Jones:** So, it does resist change in any scenario, including change which results from control effort. So, it has its pitfalls. That is that can be a pitfall. The derivative component can also help to reduce the settling time of a system.

**Dave Jones:** Um this is improving the settling time. This is because the derivative component um it acts against change of error. So, if the system has reached its set point, then it's going to resist any change away from that set point.

**Dave Jones:** And this includes overshoot. So, this is the equation which might be scary to some many that represents a PID controller. The proportional controller added to the integral controller added to the derivative controller.

**Dave Jones:** And now, this form isn't what you see in control textbooks very often because the form here is actually easier to work with with um a process called tuning. Tuning is the process of improving the constants in front of the controllers, the the proportional, integral, and derivative controllers, to improve the response of the system.

**Dave Jones:** You might want it to respond faster to disturbances. You might want it to reach steady state faster. You might want it to be slower. And this form makes tuning a bit easier because it allows you to use a process called Ziegler-Nichols tuning.

**Dave Jones:** Um which gives you a starting point for the values of these constants. You wouldn't want to You wouldn't want to rely on just that process, but it does give you a starting point for the constants in front of the components.

**Dave Jones:** So, let's talk about tuning. So, if we have a response that looks like this, what should we do? Well, in this scenario, we don't want it to ring like this.

**Dave Jones:** We don't want it to have this this this period here. Um uh T D. Um we don't want it to have that. We want it to look like this.

**Dave Jones:** We've We've got our constants from the Ziegler-Nichols tuning process, and we want to improve it. We want to We want to make it closer to our shape. So, what do we do?

**Dave Jones:** Well, oscillations like this are caused by the component of the integral and the proportional component. And if the integral component has a dominant um is a dominant component, then it's very likely that integral windup is causing this overshoot.

**Dave Jones:** So, let's try to reduce our integral component. Now, it's likely that you end up with something like this. Um and that might's not still be with your response. So, you you notice that the integral component is no longer significant in the control effort when compared to the proportional component.

**Dave Jones:** So, now let's reduce the proportional component. Now, that doesn't oscillate anymore, but we we do want it to perform a little bit of faster. So, what do we do?

**Dave Jones:** Well, the integral component now, we can change it and probably we can increase it. We know that our value of the integral component is somewhere between the constant that it was initially and after our tuning.

**Dave Jones:** So, let's take the average of those two values. Let's call them K1 + K2. And that will be the new integral constant. And now, we probably will get a little bit of overshoot.

**Dave Jones:** Um but now we've got that response time. Now, we haven't really got any derivative component yet. So, we now want to start working on that. We're now testing our disturbance rejection.

**Dave Jones:** So, now we're testing the response to disturbances. So, we start bumping it and we notice that in the normal case it decays really slowly. We want it to behave like that first curve.

**Dave Jones:** So, we increase the derivative component so that it's still relatively insignificant in the initial curve, but when there is huge rates of change like this, it has significance. So, it it is more significant than proportional component.

**Dave Jones:** So, we increase the value um maybe by a few percent, 10% or something. And then we see how that response ends up. And you'll probably end up with something like that.

**Dave Jones:** So, you do it again. And now you notice that you end up with the response you want as you slowly iteratively improve the coefficients. Now, each time you change one of these variables, the response you're probably kind of wrecking your tuning for the other variables.

**Dave Jones:** So, you have to retune those as well. Um and this process is an iterative process. You you slowly improve it and there's actually an absolute ton of methods of doing this.

**Dave Jones:** Um there's probably thousands of them. There there are tons of methods to get the initial values and I think Ziegler-Nichols the ultimate cycle method is probably the easiest and I'm going to show you how to use that in a moment.

**Dave Jones:** We know how to tune, but we don't know how to get a starting point. We What are we tuning from? Well, the way to get a starting point is to do the following.

**Dave Jones:** In most systems it's accept Well, many systems it's acceptable to um test the unit a fair bit before you end up having to use it. So, what we do in this process is we have the unit with its with just a proportional controller.

**Dave Jones:** We have let's say the oven. We have the oven with just that proportional controller. So, we have this this oven and we've got a digital controller sensing the temperature sensing the temperature and adjusting the oven accordingly.

**Dave Jones:** So, what do we want to do? Well, if we make the proportional component too large, then we end up with a system that does this. And the response gets these ever-increasing sinusoids, and this is very unstable.

**Dave Jones:** This is This is the the basic definition of an unstable system. What we want to do is have it a stable sine wave so that the amplitude is roughly not changing.

**Dave Jones:** Actually, that that's that's the way Ziegler-Nichols is done, but I think you should probably aim for something that is stable but decays extremely slowly. You're looking at the error, and you want the error to have this just constant sinusoid, which uh might seem a bit weird cuz that's exactly not what we want to happen, but this is how we do the Ziegler-Nichols tuning.

**Dave Jones:** We start off with a constant for KP, the proportional controller, that just oscillates like this. Now, when you have this constant, you can use the equations that many have come up with that use this value to create a starting point for your system's controller.

**Dave Jones:** From before, we have our KP value. And when the KP is equal to the gain that results in a stable sinusoid, then it is called K U. So, KU is the gain at which you got a stable sinusoid.

**Dave Jones:** Now, presumably, you can measure the sinusoid's period. I assume you can measure the sinusoid's period, and that value is quite important because we're going to use it in this tuning method, and that value is called TU.

**Dave Jones:** With KU and TU, you can use them in this equation here to get default values for the the controller coefficients. So, 0.6 KU * 0.6 * the value of KU is the coefficient for the proportional controller and you can use that value as a starting point.

**Dave Jones:** TU divided by 2, that's the period divided by 2 is the coefficient for the the constant for the integral controller and the the period divided by 8 is the the constant in front of the derivative controller.

**Dave Jones:** So, that actually gives us everything. We now have an initial value for KP, KI, and KD because we have an initial value for KP, TI, and TD. And to tune the values, all you do is expand this equation and then you can tune the values in front of the controller as if you had the controller before and it's much it's easier to do the iterative improvement tuning on this

**Dave Jones:** equation than it is on this equation in my opinion. So, after you get these TI values and TD values, I would convert it to the form you see above here.

**Dave Jones:** That is simply by doing this. You just the KI equals KP on TI and KD equals TD. KD and that's it. Now, I am aware that control theory can be a little bit dry.

**Dave Jones:** So, this is just the start. This is the boring part of this. What we have coming is a nice little inverted pendulum balancing robot which will just wander around the office balancing and this is going to be designed, uh 3D printed, and then we're going to use that Ziegler-Nichols tuning to just get it to balance in a empirical way.

**Dave Jones:** If anyone wants to know more about this, leave them in the comments below. If anyone wants to know the theory, the mathematical the theory behind this and how you can derive controllers from math alone.

**Dave Jones:** Leave it in the comments below, vote up that comment, and I'd be happy to do that. So, thanks. Okay, so I finished shooting my video. I finished editing, and then I find this beautiful plot on Wikipedia.

**Dave Jones:** But, it's worth it. This plot shows the effect of a step response on a system and the effect of changing the PID constants in front of the components. So, the first thing they tune here is the proportional component, and then the integral component, then the derivative component.

**Dave Jones:** And the plot kind of shows the the change of the response of the system. Now, this system this plot here is showing how a system responds to a step input.

**Dave Jones:** That is where the set point, where the system should be, is set to one, and you kind of just view how that looks. So, initially you notice about this system is that it has some steady-state error.

**Dave Jones:** That means that the system's response doesn't converge to the set point. And the way you deal with this is by increasing the integral component. They do this, and they remove the steady-state error.

**Dave Jones:** Unfortunately, as they increase the integral and proportional component, overshoot of the system substantially increases. The way they deal with that here is by increasing the derivative component. And because the derivative component resists change, it it it it's it hates change.

**Dave Jones:** It does help in reducing the oscillations, as oscillations are of course change and overshoot is change. It really just wants the line to be flat and stationary. So, I hope this plot helped.

**Dave Jones:** I had to add it in after rendering. Um see you. Mhm.
