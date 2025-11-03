# Bitwise Cyclic Tag Interpreter
This directory contains an implementation of the [Bitwise Cyclic Tag](https://esolangs.org/wiki/Bitwise_Cyclic_Tag) language.
More specifically, an interpreter for the CT language under `bct.fisl`.
It uses the ring buffer `ringbuf` module to realize the queue in which data is stored.
An adapter `adapter.py` is also included, which provides a parser to convert the number encoding format used by the CT program.
Assuming the interpreter has been compiled and its build copied to this directory, run like this: `./vm.py | python3 adapter.py`.

### Preloaded Example
The interpreter comes preloaded with a [Collatz Sequence](https://en.wikipedia.org/wiki/Collatz_conjecture) program.
The number encoding used here is `(100)^n`, where `n` is the encoded number.
This is parsed by the adapter using a tri-state-machine.

### Theoretical Implications
This implementation proves that FISL is Turing complete, as a proof of the Turing completeness of the BCT has been constructed.
The result is obvious but a proof is still of formal value.
