---
title: "Programmer humor"
date: 2005-07-01 15:42:00 -0600
mood: amused
song: "Sylver - Make It  (Radioseven - www.radioseven.se )"
original_url: https://restless-coder.livejournal.com/16952.html
---

`int zero(int x, int y, int z) { return 0; } // ha ha, screw you, x y and z!`

Also, the following chatlog provides a raw illustration of the sorts of problems I deal with at work, as well as a lengthy demonstration of what happens when I get going with [afgncaapvaljean](https://afgncaapvaljean.livejournal.com/).

(14:14:36) **WhtSMatrx:** Are you serious about there being interest in people who program theoretically?  
(14:15:00) **Restless Warrior:** What do you mean?  
(14:15:26) **Restless Warrior:** Look at it this way: no matter how much of a code monkey you are, someone has to design the original algorithms that everyone else rips off.  
(14:15:31) **WhtSMatrx:** You had said that many people find it difficult to come up with the creative way to program something.  
(14:15:49) **Restless Warrior:** You have a bag of X,Y,Z coordinates in 3D. You want to connect them together coherently.  
(14:15:59) **WhtSMatrx:** Surely there are many of those people about.  
(14:16:01) **Restless Warrior:** You figure out that a Delaunay triangulation is a good way to do this.  
(14:16:06) **Restless Warrior:** But how to go about constructing one of these?  
(14:16:21) **Restless Warrior:** Not as many as you think. I'd say most coders are not very good at writing efficient mathematical algorithms.  
(14:16:25) **WhtSMatrx:** I don't know what a Delauney triangulation is.  
(14:16:27) **Restless Warrior:** Some can, some can't.  
(14:17:23) **Restless Warrior:** It's a particular kind of triangular mesh--by definition, the one with the triangles closes to equilateral on average, basically.  
(14:17:43) **WhtSMatrx:** I see.  
(14:18:16) **WhtSMatrx:** How do you mean, connect them coherently?  
(14:18:29) **Restless Warrior:** Anyway, if you can think about problems like that and come up with robust, efficient algorithm to solve them, then everyone will love you. I'm not sure how much of a *market* there is for that... some. It's the sort of thing that professors do.  
(14:18:47) **Restless Warrior:** I was trying to give an example to answer your original question, and you are getting interested in the mathematical details. =P  
(14:19:13) **WhtSMatrx:** I see.  
(14:19:16) **WhtSMatrx:** Well, yeah.  
(14:19:20) **WhtSMatrx:** That's what I do.  
(14:19:32) **WhtSMatrx:** Sounds like you're looking for a topological mapping of sorts.  
(14:19:36) **Restless Warrior:** Let's say in a room, you have sampled the temperature at 1000 random coordinates.  
(14:19:41) **Restless Warrior:** Absolutely.  
(14:20:08) **Restless Warrior:** Now, I pick an X,Y,Z coordinates and ask: from those 1000 points you've already sampled, take a guess at what the temperature is at my new point, given a continuous field.  
(14:20:40) **WhtSMatrx:** Ahhh!  
(14:20:47) **WhtSMatrx:** That IS an interesting question!  
(14:21:00) **WhtSMatrx:** Ooo!  
(14:21:06) **WhtSMatrx:** Me likey!  
(14:21:17) **WhtSMatrx:** Hmm.  
(14:21:23) **Restless Warrior:** The Delaunay triangulation (or in this case in 3D, a tetrahedralization), constructs a framework for those 1000 points. It connects them into a tetrahedral mesh, such that any given point lies within exactly one tetrahedron. In other words, it identifies that point's four nearest neighbors instantly.  
(14:21:27) **Restless Warrior:** Well, nearly instantly.  
(14:21:43) **Restless Warrior:** You can find the enclosing tetrahedron by walking the structure. "Marching tetrahedra"  
(14:22:08) **Restless Warrior:** I thought you'd like that. =P  
(14:22:25) **Restless Warrior:** But the hard part is constructing the tetrahedralization. Once you have it, it's great.  
(14:22:38) **WhtSMatrx:** I can think of a number of methods, but few of them consider a drastic change in temperature.  
(14:22:48) **WhtSMatrx:** I would imagine.  
(14:22:51) **Restless Warrior:** It turns out the best Delaunay algorithms right now are about O(n log n).  
(14:23:49) **WhtSMatrx:** n representing the volume of space, or the number of sampled points?  
(14:23:53) **Restless Warrior:** The "take a guess at the temperature" question is simply a matter of interpolation from existing points. The question is, which existing points? The nearest neighbors are a good bet. If you want to get fancy, you can grab the points from the tetrahedra that border the enclosing tetrahedron and do some variant on bicubic.  
(14:23:59) **Restless Warrior:** n representing the number of samples.  
(14:24:18) **Restless Warrior:** I believe there is one that is O(n log log n) but it is still slow.  
(14:24:40) **WhtSMatrx:** Interesting.  
(14:25:10) **Restless Warrior:** There are a bunch of Delaunay algorithms out there. But it's an example of a problem that most programmers go "oh crap, gotta find some code to do that" and just port it or whatever.  
(14:25:32) **Restless Warrior:** The mathematically-oriented coders will actually take a crack at it, and the 1000 copycats will just steal their code.  
(14:25:41) **Restless Warrior:** But that's what I mean when I say there is a demand for mathematically-oriented coders.  
(14:26:16) **WhtSMatrx:** Neat!  
(14:26:22) **WhtSMatrx:** What an interesting puzzle.  
(14:26:28) **WhtSMatrx:** Hmm.  
(14:26:39) **Restless Warrior:** Even the people who *could* come up with a triangulation algorithm don't necessarily want to, because it's time consuming. Better to use existing code.  
(14:27:00) **Restless Warrior:** 3D graphics has a lot of puzzles like this.  
(14:27:13) **WhtSMatrx:** Problem: What if the outlying points are cold, and gradually get warmer, and the chosen point seems near the center of the heat?  
(14:27:24) **WhtSMatrx:** I'd bet.  
(14:27:39) **Restless Warrior:** Your problem needs to be specified further, I think.  
(14:27:56) **Restless Warrior:** If the chosen point's nearest neighbors are all warm, then the point is likely to be warm also.  
(14:27:57) **WhtSMatrx:** Like, say, a candle in a room.  
(14:28:17) **WhtSMatrx:** Points closer to the candle will be warmer, points farther will be colder.  
(14:28:17) **Restless Warrior:** Well, part of the issue with the candle situation is points chosen for sampling originally.  
(14:28:41) **Restless Warrior:** If they sample one point every foot along each dimension, and don't happen to hit the candle, it's not going to be adequately represented.  
(14:28:42) **WhtSMatrx:** There SHOULD be an algorithm for determining roughly the heat of the candle.  
(14:28:45) **Restless Warrior:** But that's a limitation of the dataset.  
(14:29:58) **WhtSMatrx:** Sure.  
(14:30:19) **Restless Warrior:** So, assuming the sampling density is high enough to represent the candle, then interpolation should yield a reasonable answer.  
(14:30:29) **WhtSMatrx:** I don't see how.  
(14:31:25) **WhtSMatrx:** say all the datapoints around the candle are, say, 95 degrees, as opposed to 28 as an average in the room.  
(14:31:32) **Restless Warrior:** Ok.  
(14:31:39) **WhtSMatrx:** The candle is actually, say, 126 degrees.  
(14:31:53) **Restless Warrior:** But no sample was taken directly on the candle itself?  
(14:32:01) **WhtSMatrx:** How will you detect a (essentially) point source?  
(14:32:02) **WhtSMatrx:** No.  
(14:32:04) **Restless Warrior:** Then the sampling density doesn't adequately represent the candle, like I said.  
(14:32:33) **Restless Warrior:** The less linear the temperature differences, the less well interpolation will work.  
(14:32:49) **WhtSMatrx:** It seems like you're saying, As long as the sampling is large enough that the point you pick is one of the sample points, this Delaunay algorithm will work.  
(14:32:53) **WhtSMatrx:** Ahh.  
(14:32:55) **WhtSMatrx:** I see.  
(14:33:12) **Restless Warrior:** Well, your candle is pretty close to a discontinuity in the field.  
(14:33:26) **WhtSMatrx:** So, it's not equipped to handle discontinuities.  
(14:33:28) **Restless Warrior:** Interpolation by definition assumes continuity, and works better the "more" continuous it is.  
(14:33:30) **Restless Warrior:** Right.  
(14:33:42) **WhtSMatrx:** That's what I was assuming, but I wanted to make sure.  
(14:33:46) **WhtSMatrx:** Interesting.  
(14:33:54) **Restless Warrior:** Discontinuity is by definition impossible to predict.  
(14:33:55) **WhtSMatrx:** I don't know if yours is the method I'd use.  
(14:34:07) **Restless Warrior:** It's the method everyone uses... I'm interested in hearing alternatives.  
(14:34:26) **Restless Warrior:** Marching cubes or marching tetrahedra. Very popular.  
(14:34:40) **Restless Warrior:** Because it's very efficient.  
(14:34:43) **WhtSMatrx:** Take vectors from the chosen point to the data points.  
(14:35:11) **WhtSMatrx:** The magnitude of the vector determines, inversely, the level of impact it has on the result.  
(14:35:18) **WhtSMatrx:** Average them, using the offset.  
(14:35:38) **WhtSMatrx:** Seems it should yield a pretty good result, and not have a particularly high overhead.  
(14:35:57) **Restless Warrior:** To every data point in the set?  
(14:36:03) **WhtSMatrx:** Sure.  
(14:36:20) **Restless Warrior:** That's basically multilinear interpolation, but using every data point instead of just the X nearest.  
(14:36:22) **WhtSMatrx:** Actually, inverse square, not just inverse.  
(14:36:28) **Restless Warrior:** Inverse square is more often used for that, yes.  
(14:36:35) **Restless Warrior:** And it's terribly inefficient when the number of samples is large.  
(14:36:40) **WhtSMatrx:** Is it?  
(14:36:42) **Restless Warrior:** It's O(n) to compute.  
(14:37:05) **WhtSMatrx:** Better than O(nlog(n)).  
(14:37:10) **Restless Warrior:** That's the compute the mesh, dude!  
(14:37:29) **Restless Warrior:** Once you have the mesh, interpolating a new point is something like O(log n)  
(14:37:42) **WhtSMatrx:** You don't NEED to calculate the mesh with my method.  
(14:37:54) **Restless Warrior:** Let's say you want to interpolate 10,000 new points.  
(14:37:58) **Restless Warrior:** That's O(n) 10,000 times.  
(14:38:09) **Restless Warrior:** Whereas with my method, it's very close to O(1) for each.  
(14:38:11) **WhtSMatrx:** I see.  
(14:38:20) **Restless Warrior:** Especially if the 10,000 new points are in a coherent order spatially.  
(14:38:31) **Restless Warrior:** Because with marching tets, you can start with the last correct tet and march from there.  
(14:38:34) **Restless Warrior:** Do you get what I'm saying?  
(14:38:39) **WhtSMatrx:** Sure.  
(14:39:00) **Restless Warrior:** The only mildly challenging part is finding the enclosing tet.  
(14:39:08) **Restless Warrior:** And trust me, it is much faster than O(n).  
(14:39:15) **WhtSMatrx:** \*Grumbles\* My method would work. Just inefficiently.  
(14:39:19) **Restless Warrior:** Yes, it would work!  
(14:39:24) **Restless Warrior:** It is not bad.  
(14:39:53) **Restless Warrior:** It really depends on how many points you need to interpolate.  
(14:39:57) **WhtSMatrx:** But, I see the point.  
(14:39:58) **Restless Warrior:** Your method is better for 1.  
(14:40:15) **WhtSMatrx:** One could make it simpler by simply using the nearest log(n) points.  
(14:40:24) **Restless Warrior:** But then you have a problem again.  
(14:40:31) **WhtSMatrx:** There'd be some error, but it wouldn't be egregious.  
(14:40:31) **Restless Warrior:** How do you know which points are nearest without checking them all!  
(14:40:44) **WhtSMatrx:** Point.  
(14:41:13) **WhtSMatrx:** Divide them into Tetrahedra.  
(14:41:15) **Restless Warrior:** As long as you're doing the work of computing distance between the sample and every point in the set, you may as well factor them into the computation at that point; it's not any slower.  
(14:41:21) **WhtSMatrx:** DAMN YOU!  
(14:41:27) **Restless Warrior:** \*laughs maniacally\*  
(14:41:31) **Restless Warrior:** You begin to see!  
(14:42:06) **WhtSMatrx:** What a charming problem!  
(14:42:13) **Restless Warrior:** I like it.  
(14:42:32) **Restless Warrior:** I spend almost a year porting and creating triangulation algorithms for this.  
(14:42:37) **Restless Warrior:** s/spend/spent  
(14:43:03) **WhtSMatrx:** Wow!  
(14:43:31) **Restless Warrior:** The ultimate solution would be to sample enough points to glean the raw mathematics behind the field. Then you'd just have the formula. But practically it doesn't work that way. =)  
(14:43:44) **WhtSMatrx:** Right.  
(14:43:47) **Restless Warrior:** What formula does a room's temperature follow? Something mind bogglingly complex.  
(14:43:58) **WhtSMatrx:** That's what I was going for with my discontinuity concept.  
(14:44:01) **Restless Warrior:** Yep.  
(14:44:10) **Restless Warrior:** Discontinuity will basically screw you, I will admit that.  
(14:44:16) **Restless Warrior:** But it's not fair. It's like asking what life in a black hole is like.  
(14:44:24) **WhtSMatrx:** Heh heh...  
(14:44:28) **WhtSMatrx:** Magical.  
(14:44:29) **Restless Warrior:** You simply can't observe it. =)  
(14:44:34) **WhtSMatrx:** Err, Mystical.  
(14:44:34) **Restless Warrior:** With fluffy bunnies, I'm sure.  
(14:44:43) **Restless Warrior:** Psionic bunnies.  
(14:44:45) **Restless Warrior:** With pancakes on their heads.  
(14:44:52) **WhtSMatrx:** Excellent!  
(14:45:04) **WhtSMatrx:** That's a delightful problem!  
(14:46:06) **WhtSMatrx:** Hmm.  
(14:46:17) **WhtSMatrx:** Topology should have something to say about this.  
(14:46:53) **Restless Warrior:** Heh, googling for "Delaunay topology" yields the Javadoc for visad.Delaunay, a class I wrote, as the first hit.  
(14:47:10) **WhtSMatrx:** Continuity implies compactness, which should possibly make the conclusion a bit clearer.  
(14:47:19) **Restless Warrior:** What do you mean?  
(14:48:06) **WhtSMatrx:** Compact: For any cover of a set S, there exists a finite subcover which is a cover of S.  
(14:50:16) **Restless Warrior:** What are the subsets being considered as part of the cover? The tetrahedra?  
(14:50:22) **WhtSMatrx:** Which, of course, your tetrahedra would qualify as, for a finite place.  
(14:50:45) **Restless Warrior:** Well, you don't just want to cover the samples, though. You want to cover the entire space within the convex hull defined by the samples.  
(14:50:54) **Restless Warrior:** And the tetrahedra actually do that exactly.  
(14:51:09) **Restless Warrior:** Remove even one and it's you've created an area within the convex hull that doesn't have an enclosing tet.  
(14:51:17) **WhtSMatrx:** No, the cover covers the space, not just the samples.  
(14:51:41) **Restless Warrior:** If you are talking about the space, then the tets are a minimum set cover.  
(14:51:48) **WhtSMatrx:** Indeed.  
(14:51:57) **WhtSMatrx:** There are rules about this.  
(14:52:01) **WhtSMatrx:** Why tets?  
(14:52:08) **Restless Warrior:** I mean, you could define one huge tetrahedron that covers the space and more, but it would defeat the purpose. =P  
(14:52:13) **WhtSMatrx:** There are plenty of other tilings of 3space.  
(14:52:16) **Restless Warrior:** Because they are the simplest 3D structure. The d4, so to speak.  
(14:52:28) **WhtSMatrx:** Well, not plenty.  
(14:52:33) **WhtSMatrx:** But a few.  
(14:52:34) **Restless Warrior:** And you can guaranteed arrange four or more samples in 3D into a tetrahedralization.  
(14:52:38) **Restless Warrior:** You can't necessarily do that with, say, cubes.  
(14:52:55) **Restless Warrior:** Everything can be decomposed into tets.  
(14:52:59) **WhtSMatrx:** Why not?  
(14:53:01) **Restless Warrior:** A cube is just two tets.  
(14:53:06) **Restless Warrior:** Err, not two.  
(14:53:07) **Restless Warrior:** Five.  
(14:53:09) **Restless Warrior:** Right...  
(14:53:17) **WhtSMatrx:** Misshapen.  
(14:53:54) **Restless Warrior:** Ok, fine. You have your eight points forming a perfect cube. And one more off to the side. How do you cover that with just cubes?  
(14:54:05) **Restless Warrior:** Without overlap.  
(14:54:24) **Restless Warrior:** Because overlap is death to the topology; it makes it unclear which samples to use for the interpolation.  
(14:54:41) **WhtSMatrx:** Oh, so, you get your tets from the data points defining the vertices?  
(14:55:02) **WhtSMatrx:** I thought you were just having the datapoints be contained within the tet.  
(14:55:05) **Restless Warrior:** Dammit. Four. I think a cube decomposes into four tets. I actually built a little cube out of paper to figure this out once upon a time. =P  
(14:55:19) **WhtSMatrx:** Should be five.  
(14:55:25) **Restless Warrior:** Ok.  
(14:55:33) **WhtSMatrx:** One in the center, and one for each non-adjacent corner.  
(14:55:55) **Restless Warrior:** Oh, yes. Sorry about that. The tets' vertices are samples within the data structure. That's how you use them for interpolation. You take the vertices of the enclosing tet as the samples to use for the interpolation.  
(14:56:16) **WhtSMatrx:** That seems unnecessarily cludgy.  
(14:56:21) **WhtSMatrx:** I'm meaning no offense.  
(14:56:24) **WhtSMatrx:** BTW.  
(14:56:25) **Restless Warrior:** That's fine.  
(14:56:43) **WhtSMatrx:** I thought the point was to have all the tets be the same volume.  
(14:56:43) **Restless Warrior:** I didn't invent this stuff.  
(14:56:49) **Restless Warrior:** Oh, not at all.  
(14:57:10) **WhtSMatrx:** That makes it much more ooby.  
(14:57:27) **Restless Warrior:** The point is that it's very straightforward to interpolate a point's value from the four nearest neighbors, using a weighted average.  
(14:57:40) **WhtSMatrx:** So, any given new point will be outside the tet structure (Unless you call walls a side) or WITHIN one of the tets.  
(14:58:07) **WhtSMatrx:** What if a point falls on a line?  
(14:58:18) **WhtSMatrx:** How do you tell which tet a point is in?  
(14:58:45) **Restless Warrior:** That's an edge case (he he, geeky math pun!), but you can simply use the three nearest points instead of 4. Or, alternately, 5 points, by including the other point from both adjacent etts.  
(14:58:56) **WhtSMatrx:** World's most bizarre conversation.  
(14:58:57) **Restless Warrior:** That's where marching tets comes in.  
(14:59:00) **Restless Warrior:** I love it!  
(14:59:19) **WhtSMatrx:** I bet you call that the tet offensive.  
(14:59:25) **Restless Warrior:** So, you start by picking an arbitrary tet.  
(14:59:31) **WhtSMatrx:** (Sorry.)  
(14:59:37) **Restless Warrior:** It is O(1) to check which side of a plane a point lands on.  
(14:59:46) **WhtSMatrx:** OH!  
(14:59:49) **WhtSMatrx:** Of course!  
(14:59:52) **WhtSMatrx:** Damn!  
(14:59:58) **Restless Warrior:** If it lies on the "correct" side of all four sides of the tet, then it is inside, and you're done.  
(15:00:04) **Restless Warrior:** Otherwise, you know which "direction" vaguely it's in.  
(15:00:10) **WhtSMatrx:** Right!  
(15:00:11) **Restless Warrior:** And you walk to the adjacent tet across that plane.  
(15:00:13) **Restless Warrior:** Make sense?  
(15:00:13) **WhtSMatrx:** Obvious.  
(15:00:24) **WhtSMatrx:** Indeed.  
(15:00:27) **Restless Warrior:** Eventually, in a cartesian space, you will converge on the actual enclosing tet.  
(15:00:31) **Restless Warrior:** It's very clever, really.  
(15:00:40) **WhtSMatrx:** Damn.  
(15:00:42) **WhtSMatrx:** That's sexy.  
(15:01:11) **Restless Warrior:** And that's what I was talking about when I said finding a new point's value is "something like" O(log n). Because you don't actually have log n tets...  
(15:01:37) **Restless Warrior:** It's hard to say exactly what the efficiency is, but you will almost never need to walk through every tet.  
(15:01:38) **WhtSMatrx:** Right.  
(15:01:46) **Restless Warrior:** You'll take a fairly efficient straight-line path there.  
(15:02:04) **WhtSMatrx:** So, generating the tet space is the struggle.  
(15:02:10) **Restless Warrior:** Right.  
(15:02:29) **WhtSMatrx:** Which you could do randomly, I suppose.  
(15:02:46) **WhtSMatrx:** Organically, anyway.  
(15:02:58) **Restless Warrior:** And also like I said before, if you have a bunch of points to interpolate, then you can save a lot of time. Because you can make the walking even faster, by sorting the points spatially to minimize the number of tets to walk.  
(15:03:01) **WhtSMatrx:** How do you make sure a new point is not outside the tet space?  
(15:03:16) **WhtSMatrx:** Take as data points the corners?  
(15:03:20) **Restless Warrior:** Well, if it's outside, you will eventually reach a tet that is adjacent to the convex hull and the algorithm will indicate it's out there.  
(15:03:26) **Restless Warrior:** Now, if the hull isn't convex, it's harder.  
(15:03:39) **WhtSMatrx:** Right.  
(15:03:40) **Restless Warrior:** Oh, a lot of people do that.  
(15:03:59) **Restless Warrior:** Take as data points combinations of -INFINITY and +INFINITY in the space.  
(15:04:06) **Restless Warrior:** And they get these infinitely huge edge tets.  
(15:04:10) **Restless Warrior:** It's kind of funny.  
(15:04:29) **Restless Warrior:** You don't have to do that though.  
(15:04:31) **WhtSMatrx:** Heh, yeah, that sounds kind of, umm, inefficient.  
(15:04:35) **Restless Warrior:** Not at all.  
(15:04:55) **WhtSMatrx:** No?  
(15:04:56) **Restless Warrior:** The math surrounding infinity is actually very straightforward and well-defined.  
(15:05:06) **WhtSMatrx:** Not that.  
(15:05:08) **Restless Warrior:** And just as efficient as with finites.  
(15:05:17) **Restless Warrior:** Why not?  
(15:05:22) **WhtSMatrx:** It seems that taking as a datapoint infinity would distort the results.  
(15:05:43) **Restless Warrior:** Umm, only if you use that point in your interpolation results, which is an obvious no-no.  
(15:06:02) **Restless Warrior:** It's just for spatial purposes, to make the walk algorithm a little simpler.  
(15:06:04) **WhtSMatrx:** Oh, so you just use LESS points.  
(15:06:20) **WhtSMatrx:** Like, the three on the outside.  
(15:06:23) **Restless Warrior:** If you walk into one of the infinitets, you just say "outside structure"  
(15:06:27) **Restless Warrior:** Sure, that's another option.  
(15:06:30) **WhtSMatrx:** Ahh.  
(15:06:36) **Restless Warrior:** In our software, we interpolate stuff that is "close" to the hull.  
(15:07:07) **Restless Warrior:** If it is too far away though, then we just should NaN.  
(15:07:10) **Restless Warrior:** s/should/shout  
(15:07:26) **Restless Warrior:** Err, we uses NaN (not a number) to represent "missing"  
(15:07:42) **Restless Warrior:** And apparently we talks like Gollum now.  
(15:08:26) **Restless Warrior:** Anyway, I'm still thinking about a tetrahedralization using vertices that are *not* the sampled data points.  
(15:08:32) **Restless Warrior:** I can't see how that would be very useful.  
(15:08:58) **Restless Warrior:** You'd have to keep a record of which tetrahedron each of the original samples falls into.  
(15:09:11) **WhtSMatrx:** I can imagine a really sexy, if incredibly machine intensive, method of calculating outside.  
(15:09:25) **Restless Warrior:** What's that?  
(15:10:13) **WhtSMatrx:** Interpolate a lot of points, chosen randomly, within the overall tet structure.  
(15:10:22) **WhtSMatrx:** Call it the subspace.  
(15:10:48) **WhtSMatrx:** Recalc the structure using those new ones as datapoints. Wash, rinse, repeat.  
(15:10:54) **WhtSMatrx:** Generate the mathematics.  
(15:11:09) **Restless Warrior:** "Generate the mathematics"?  
(15:11:15) **WhtSMatrx:** Indeed.  
(15:11:25) **Restless Warrior:** I was following you through "wash, rinse, repeat"  
(15:11:36) **Restless Warrior:** That wouldn't grow the structure though.  
(15:11:44) **WhtSMatrx:** Not at all.  
(15:11:52) **Restless Warrior:** It would simply reorganize it, and introduce error.  
(15:12:10) **WhtSMatrx:** But it gives you, potentially, enough data to figure out the functions defining the space, or a very rough guess at them.  
(15:12:20) **WhtSMatrx:** Then push them out.  
(15:13:00) **WhtSMatrx:** I love this, for it can produce hideously wrong answers, for all the right reasons!  
(15:13:40) **Restless Warrior:** Back to the 'equal volume tets' thing you mentioned: after finding the enclosing tet for a new point, you'd interpolate using your vector approach (weighted average) from the data samples known to be within that tet. This would give you a more efficient way to determine neighbors that are "near enough" to the point, although it may be better to use samples within that tet, as well as all other tets that share at least one vertex, to ensure all very close points are considered. Still, then the trick becomes choosing the correct volume and positioning of the tetrahedron structure, to make sure you don't end up with (e.g.) one big tet enclosing the entire dataset.  
(15:14:46) **Restless Warrior:** Oh, you're trying to use the interpolated data as additional information for gleaning a mathematical function. That is not my area of expertise, but my intuition is that such a thing is extremely difficult, if not untenable, in general.  
(15:14:48) **WhtSMatrx:** Nice segue.  
(15:15:01) **Restless Warrior:** Sorry, I was working on typing that up as you were talking about your thing.  
(15:15:06) **WhtSMatrx:** No worries.  
(15:15:20) **WhtSMatrx:** I thought you found the idea as ridiculous as it is.  
(15:15:28) **Restless Warrior:** Hehe.  
(15:15:39) **Restless Warrior:** I'm not saying it can't be done. I just don't know how.  
(15:15:52) **WhtSMatrx:** It can be.  
(15:16:13) **WhtSMatrx:** But, like I said, it's inefficient and error prone.  
(15:16:52) **WhtSMatrx:** Hmm.  
(15:16:55) **WhtSMatrx:** How about this,  
(15:17:59) **Restless Warrior:** Do you see what I'm driving at with the equal volume tets? I think you're still stuck trying to decide how to divide up the vertices such that they fall into a good distribution of "buckets" so to speak.  
(15:17:59) **WhtSMatrx:** Instead of equal volumes, which, granted, is kind of yeech, why not calculate tets of differing volumes, each of which contain a datapoint at its center?  
(15:18:15) **WhtSMatrx:** Right.  
(15:18:25) **WhtSMatrx:** Equal volume is out, for the moment.  
(15:19:00) **Restless Warrior:** Heh, you're stumbling onto something similar to Voronoi power diagrams, which is a dual to the Delaunay triangulation. =)  
(15:19:19) **WhtSMatrx:** Yeah, they're not entirely dissimilar.  
(15:19:34) **Restless Warrior:** [http://www.cs.cornell.edu/Info/People/chew/Delaunay.html](http://www.cs.cornell.edu/Info/People/chew/Delaunay.html)  
(15:19:37) **WhtSMatrx:** Plus, you get to use epsilon delta balls.  
(15:20:04) **WhtSMatrx:** I didn't know they had already defined this so well.  
(15:20:14) **WhtSMatrx:** Wow.  
(15:20:22) **Restless Warrior:** Oh yeah.  
(15:20:23) **WhtSMatrx:** You know, we're pretty clever.  
(15:20:43) **Restless Warrior:** See. Computation geometry. What I'm saying!  
(15:20:59) **Restless Warrior:** If you say so. I probably would have never figured this stuff out on my own. =)  
(15:21:18) **WhtSMatrx:** You'd have come up with my first algorithm.  
(15:21:23) **Restless Warrior:** Absolutely.  
(15:21:32) **Restless Warrior:** It is the "naive" approach. =)  
(15:21:47) **WhtSMatrx:** Then you'd have seen the problem.  
(15:22:03) **Restless Warrior:** "The Delaunay triangulation is built within a large triangle whose vertices are well off-screen. That's why in the Delaunay triangulation there are lines heading off-screen. This technique makes the code simpler since otherwise additional code would be needed to handle new sites that are outside the convex hull of the previous sites."  
(15:22:04) **WhtSMatrx:** And the problem then becomes, how do I find just the CLOSEST points?  
(15:22:09) **Restless Warrior:** Yep.  
(15:22:17) **Restless Warrior:** Indeed.  
(15:22:42) **WhtSMatrx:** You might have come up with this.  
(15:22:54) **Restless Warrior:** Perhaps.  
(15:22:57) **WhtSMatrx:** I'd have come up with my epsilon delta balls.  
(15:23:06) **Restless Warrior:** Still, computing a Delaunay triangulation efficiently is tricky.  
(15:23:17) **Restless Warrior:** There are six or seven major algorithms people have come up with for it.  
(15:23:17) **WhtSMatrx:** I'd have started with cubes.  
(15:23:23) **Restless Warrior:** Cubes are a lot messier.  
(15:23:28) **WhtSMatrx:** Right.  
(15:23:34) **WhtSMatrx:** I think I would've gotten that.  
(15:23:39) **WhtSMatrx:** Maybe not.  
(15:26:38) **WhtSMatrx:** Hmm.  
(15:26:42) **WhtSMatrx:** I wonder.  
(15:26:50) **WhtSMatrx:** Could there be something else to try here?  
(15:27:03) **WhtSMatrx:** Could each point, ohh, radiate?  
(15:28:01) **WhtSMatrx:** Take the average temperature in the room, using the data points.  
(15:28:24) **WhtSMatrx:** Use that as a base temperature, and assume that each point radiates its own temperature.  
(15:28:36) **WhtSMatrx:** Generate the field equations from there.  
(15:29:04) **Restless Warrior:** You're just converting the values to a deviation from the average, which is fine, but it changes nothing. It's an offset.  
(15:29:35) **WhtSMatrx:** Except, I'm looking at ways to generate a field.  
(15:30:10) **WhtSMatrx:** Because, of course, having an equation you can plug coordinates into is O(1).  
(15:30:16) **Restless Warrior:** Of course.  
(15:30:46) **Restless Warrior:** How does reducing the average sample value to zero assist in uncovering the field?  
(15:30:53) **WhtSMatrx:** Heh, I once teased my professor by telling him I could make an algorithm at 1/n.  
(15:31:12) **WhtSMatrx:** Which was true.  
(15:31:56) **Restless Warrior:** But with N defined only within `[0, 1]` or something?  
(15:32:03) **Restless Warrior:** Err `(0, 1]`  
(15:32:17) **WhtSMatrx:** No.  
(15:32:31) **WhtSMatrx:** Give you a hint.  
(15:32:48) **WhtSMatrx:** N defined from `[1, maxint]`  
(15:33:03) **Restless Warrior:** For 1-bit numbers?  
(15:33:12) **WhtSMatrx:** Nope.  
(15:33:27) **Restless Warrior:** So, N defined from `[1, 2^32]` shall we say?  
(15:33:31) **WhtSMatrx:** Sure.  
(15:34:37) **Restless Warrior:** Sorry, I don't get it.  
(15:34:46) **WhtSMatrx:** I'm glad I'm relaying this over computer. Yo'd hit me in person when I tell you.  
(15:34:56) **Restless Warrior:** Hehe. I know it's going to be something stupid; I'm ready for it.  
(15:35:36) **WhtSMatrx:** The programs runs a fairly intensive process for 1 to Maxint/N times.  
(15:36:08) **Restless Warrior:** Right, I thought about that.  
(15:36:15) **WhtSMatrx:** Heh heh.  
(15:36:35) **WhtSMatrx:** Worst! Concept!  
(15:36:38) **WhtSMatrx:** EVAR!  
(15:36:42) **Restless Warrior:** But it's not really fair to say that's 1/N. It's maxint/N.  
(15:36:53) **Restless Warrior:** I know they are basically the same thing in big-O.  
(15:37:01) **WhtSMatrx:** Well, yeah.  
(15:37:10) **Restless Warrior:** It's just, it's more fair to say that maxint/N operation are required.  
(15:37:15) **WhtSMatrx:** I'm entirely taking advantage of the mathematical ambiguity.  
(15:37:24) **Restless Warrior:** I wouldn't call it "worst"... perhaps "most useless"!  
(15:37:36) **Restless Warrior:** No real problem is helped by that idea!  
(15:37:44) **WhtSMatrx:** Exactly!  
(15:37:55) **Restless Warrior:** Well, except for delays.  
(15:38:13) **WhtSMatrx:** \*Sighs\* Why must I be cursed with such an esoteric sense of mathematical whimsey?  
(15:38:34) **Restless Warrior:** If you *want* to stall for time, then you could use it. It's similar to keeping track of the number of ms elapsed during some operations, then waiting for 60-n ms after that to ensure that exactly 60 ms pass total between frames or something.  
(15:38:58) **Restless Warrior:** Although I'm not sure how to adapt that example to apply to 60/n instead of 60-n.  
(15:39:10) **WhtSMatrx:** It's not supposed to be USEFUL!  
(15:39:20) **Restless Warrior:** Ha, I'm *making* it useful!  
(15:39:29) **WhtSMatrx:** Curse you!  
(15:39:50) **Restless Warrior:** You want useless! I'll give you useless! `public int ident(int n) { return n; }`  
(15:39:54) **Restless Warrior:** Now *that's* useless!  
(15:40:09) **WhtSMatrx:** What's that do?  
(15:40:18) **Restless Warrior:** It's the identity function.  
(15:40:26) **WhtSMatrx:** which does?  
(15:40:33) **Restless Warrior:** Returns the same value that was inputted?  
(15:40:46) **Restless Warrior:** Useful in mathematics but useless directly for programming.  
(15:40:47) **WhtSMatrx:** Oh!  
(15:40:54) **WhtSMatrx:** I see,  
(15:40:59) **Restless Warrior:** I mean, if you already have `n`, you have `n`.  
(15:41:05) **WhtSMatrx:** Ehh.  
(15:41:16) **WhtSMatrx:** Useful as a template, maybe?  
(15:41:34) **Restless Warrior:** Yeah, in OO programming it could be good for subclassing or something.  
(15:41:42) **Restless Warrior:** But that's true of almost anything.  
(15:41:56) **Restless Warrior:** Even `public int zero(int x, int y, int z) { return 0; } // ha ha, screw you, x y and z!`  
(15:42:14) **WhtSMatrx:** Heh, I like that.  
(15:42:19) **Restless Warrior:** Yeah, me too. =)  
(15:42:28) **Restless Warrior:** It makes me chuckle, enough that I'm considering posting it in my LJ. =P  
(15:42:34) **Restless Warrior:** And you thought *your* sense of humor was isoteric.

* * *

"Programming is like pinball. The reward for doing it well is the opportunity to do it again."
