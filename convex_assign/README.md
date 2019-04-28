# assign `N` things into `K` bins, presumably each bin can support `N/K` things. 

Survey each thing for the bin it'd prefer, limited to rank ordering. 
Interpret _utility_ of being assigned to a project as the index of that project appearing in the reversed preference list

# optimization problem-- find the assignment that maximizes `self.total_utility()`. 

I'm 98% it's exponential in num projects, a rough upper bound is ~$\binom{n}{n//k} ^{k}$ where n is number of people and k is number of projects (and, i.e. python, n//k is floor divide). I *don't* expect brute force `argmax` to be viable. 

have to workshop an exact solution sometime. 



# one way to approach optimization is derivatives, but what's *derivative of utility with respect to assignment*, holding preferences constant? 

An assignment `Dict[project, List[person]]`, and with the constraint that **every person is in exactly one project** it is in fact _invertible_. But every invertible map from A to collections of B is also a non-injective map from B to A, so we could in fact rewrite `assignment` as `Dict[person, project]`. 

what is a derivative? it is when the observer _wiggles_ input to see what it does to output. our input type is a set of non-injective maps. 
## How do we wiggle a set of non-injective maps? 
i'm _guessing_ something to do with [finite differences](https://en.wikipedia.org/wiki/Finite_difference#difference_operator). 




## _this was dumb stream of conscious before i noticed that i needed to be looking at finite differences._ 

_holding preferences constant, what is the derivative of utility with respect to assignment?_

_assignment is a `Dict[bin, List[agent]]`. I don't know how to take a derivative from that input target. With the constraint that every agent can only appear in one list, and the constraint that no agent is left behind._ 

_These two constraints make it an _invertible_ function. Notice that every invertible map from A to some collections of B is isomorphic to a non-injective map from B to A._

_Would the type of `Injection[agent, bin]` be easier as an input type to derive with respect to??_ 

_suppose we start with the formalism `df/dx = lim(f(x+h)-fx / h)`. What does `x+h` mean? "wiggling" tiny amounts of input here would mean _rearranging_ the assignment. Like, the group action that changes the mapping, that moves one arrow to a different place (or switches two arrows for eachother?) but we couldn't have a `limit as h goes to zero`, we couldn't `divide by h` in this sense... could we?_ 

_Unless `dividing by h` is _inverse of h_, meaning if `x` is an assignment that contains `Alice -> pizza` and `bob -> tofu`, `+h` applies the switching action, so it literally takes the difference between the utility of the assignment that contains `alice -> pizza, bob -> tofu` and subtracts from it the utility of the assignment that contains `alice -> tofu, bob -> pizza`._ 

_Perhaps the h in the denominator isn't undoing an action (because once we've mapped to numbers --- utility --- we can't rearrange the assignment really), it's _counting the amount of such actions_, so `h=3` had 3 reassignment actions, etc., and h=1 is in fact our best approximation..._

## _no wait, think recurrences not derivatives._

_of course. the discrete version of derivative is difference. idiot._


