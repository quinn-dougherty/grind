# assign `N` things into `K` bins, presumably each bin can support `N/K` things. 

Survey each thing for the bin it'd prefer, limited to rank ordering. 
Interpret _utility_ of being assigned to a bin as the index of that bin appearing in the reversed preference list of each thing. 

# optimization problem-- find the assignment that maximizes `self.total_utility()`. 

I'm 98% it's exponential in num projects, a rough upper bound is ~$\binom{n}{n//k} ^{k}$ where n is number of people and k is number of projects (and, i.e. python, n//k is floor divide). I *don't* expect brute force `argmax` to be viable. 

# solutions proposed
Something like [simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing) could work ok. Our friend also sketched what an evolutionary solution would look like. 

[This solution](https://github.com/J-DM/Roth-Peranson) could be adapted, few differences. This was actually an issue among med schools and someone got a nobel for solving it.  

_The following were notes, stream of consciousness
# one way to approach optimization is derivatives, but what's *derivative of utility with respect to assignment*, holding preferences constant? 

An assignment `Dict[project, List[person]]`, and with the constraint that **every person is in exactly one project** it is in fact _invertible_. But every invertible map from A to collections of B is also a non-injective map from B to A, so we could in fact rewrite `assignment` as `Dict[person, project]`. 

what is a derivative? it is when the observer _wiggles_ input to see what it does to output. our input type is a set of non-injective maps. 


## How do we wiggle a set of non-injective maps? 
i'm _guessing_ something to do with [finite differences](https://en.wikipedia.org/wiki/Finite_difference#difference_operator). 

We know we can _rearrange_ the mapping. Maybe a mapping containing both `alice->pizza, bob->tofu` is "one step away" from a mapping that's exactly the same except `alice->tofu, bob->pizza`. But will that help us with the _numeric_ side, the value/utility of a mapping?


