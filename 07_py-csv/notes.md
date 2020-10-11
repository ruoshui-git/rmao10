Some notes on K07: 

- Originally I didn't want to edit, but ended up re-writing this

- If we are using funciton once, we can just put everything in main
- in general, I think we should avoid loading the file in the same function that does the calculation. Loading file into dict should be in its own function, but for K07 it doesn't matter

- Even though asked, a dict is really not useful here. We're not looking up anything. We can use 2 arrays, which saves work by not having to hash values when creating the dict. And we need the arrays at some point anyways.

- dict.key() and dict.values() are guaranteed to iterate in insertion order, so they will be aligned property for random.choices. This is not guaranteed a language like Rust.

- we should not have put cumulative weight affecting the random selection as a question we have. I just checked with Python docs that random.choices deals with this. To quote:
        If a weights sequence is specified, selections are made according to the relative weights. Alternatively, if a cum_weights sequence is given, the selections are made according to the cumulative weights (perhaps computed using itertools.accumulate()). For example, the relative weights [10, 5, 30, 5] are equivalent to the cumulative weights [10, 15, 45, 50]. Internally, the relative weights are converted to cumulative weights before making selections, so supplying the cumulative weights saves work.

- This can be improved:

        ```python
        for i in range(len(x)):
            n = x[i]
        ```
    Should also be written as:

        ```python
        for i, n in enumerate(x):
        ```

Other things that can be improved:


- People generally do `for line in f:` instead of `s = f.read` and splitting `s`, but in our case, we needed to index into it, so I guess that's a pass. But it's still not really necessary to do all that.
- `total = float(((x[len(x) - 2]).split(","))[1])` -> `total = float((x[-1]))`
- `x = x[1 : len(x) - 2]` -> `x = x[1:-1]`