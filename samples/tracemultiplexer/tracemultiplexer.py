"""
Simulate a program where two threads write to the same log
file. Exhibit nondeterminism in scheduling threads. Try to synchronize
so that only one thread at a time can write to the log.  Detect unsafe
states where both threads may write to the log.  Identify log messages
that may have been corrupted by unsynchronized writes from both
threads.

The simulated multi-threaded program has been instrumented to save
traces of its API calls in a log.  Instead of simply calling the API
functions, each thread instead calls the *tracecapture* function,
which calls the API function but also saves the call (with arguments)
and return (with return value) in the trace log.  The tracecapture
function uses a lock:

    tracelock = lock()

    def tracecapture(thread_id, call, args): # call is action name
        tracelock.acquire()
        log(thread_id, call, "start", args) # log the call with arguments
        tracelock.release() # release here allows threads to interleave
        ret = call(*args)
        tracelock.acquire()
        log(thread_id, call, "finish", ret) # log the return with return value
        tracelock.release()
        return ret

The purpose of *tracelock* is to ensure that only one thread at a time
can write to the trace log.  To allow threads to interleave, the first
*tracelock.release()* *precedes* the call, otherwise the call might
block and hold *tracelock*, prevent other threads from running while
that call blocks.

This model program exhibits nondeterminism in thread scheduling, so
traces (paths through the graphs) differ in the order that API calls
and returns are made, which results in different orders for messages in
the log.

Parameters (constants that do not change when the model executes):

program: models the multi-threaded program.  It is a sequence of API
call ids (action ids) for each thread, first index is thread id,
second index is thread pc.  Here we model a simple program with just
two threads, where each thread makes just one API call, executes
tracecapture just once, and writes just two log messages.  With a few
revisions, we could also handle a more complicated simulated program
(with more threads and more actions).

unsynchronized: set False to use tracelock, True to ignore tracelock


State:

pc: program counter for each thread, indexed by thread_id
Indicates which action in program each thread is executing

phase: phase of each thread, indexed by thread id
models progress through the tracecapture function (see above)
For each API call in program, phases in order are: ready, start, call, finish
phase[thread] == start means thread holds tracelock to write call start
phase[thread] == finish means thread holds tracelock to write call finish
After processing last API call in its thread, phase[thread] == done

log: contents of the tracelog written by all the threads

Actions:

Each action represents progress through the phases of tracecapture.
Each action might be enabled for more than one thread in some states; 
this models the nondeterminism of threading.

"""

from copy import copy

## Parameters

# This simple program has only two threads, with only one API call in each

program = (( 'listfiles', ),  # thread 0
           ( 'openfile', ))   # thread 1

threads = list(range(len(program))) # one element of program for each thread

unsynchronized = False # False: use tracelock, True: ignore tracelock

### State

# tracecapture state

pc = list() # program counter for each thread
phase = list() # phase of each thread in tracecapture
log = list() # contents of tracelog written by all threads

# file system state

files = list() # filenames in filesystem
listing = list() # listfiles return value, FIXME ret should be in tracecapture

### Safety condition

# phases where a thread can write to the log
writing = ('start','finish')

def writing_threads():
    """
    list of threads that can write to the log
    """
    return [ t for t in threads if phase[t] in writing ]

def state_invariant():
    """
    At most one thread can write to the log
    """
    return len(writing_threads()) <= 1


### Other necessary functions

# run is allowed to stop
def accepting():
    return all([ phase[t] == 'done' for t in threads ])

# reset before another run
def reset():
    global pc, phase, log
    pc = [ 0 for thread in program ]
    phase = [ 'ready' for thread in program ]
    log = []
    files = []

### Initialize

reset()

### Actions

def start_enabled(thread): 
    return (phase[thread] == 'ready'
            and (not writing_threads() # lock is free
                 or unsynchronized))   # ignore lock - might corrupt file

def start(thread):
    phase[thread] = 'start' # acquire lock
    # write log, if it might be corrupted write 'XXX' at the end
    if state_invariant():
        log.append((thread, program[thread][pc[thread]], 'start'))
    else:
        log.append((thread, program[thread][pc[thread]], 'start', 'XXX'))

def call_enabled(thread):
    return phase[thread] == 'start' # holding lock

def call(thread):
    global listing # we reassign whole list, we don't just update it
    phase[thread] = 'call' # release lock, execute call
    action = program[thread][pc[thread]]
    # for now. handle each action in *program* as a special case inline here
    if action == 'openfile':
        files.append('file0') # only works if openfiles just called once
    if action == 'listfiles':
        listing = copy(files) # must copy now because open may change files

def finish_enabled(thread): 
    return (phase[thread] == 'call'
            and (not writing_threads() # lock is free
                 or unsynchronized))   # ignore lock - might corrupt file

def finish(thread):
    phase[thread] = 'finish' # acquire lock
    action = program[thread][pc[thread]]
    # for now, handle each action in *program* as a special case inline here
    if action == 'openfile':
        ret = files[-1] # most recently appended
    if action == 'listfiles':
        ret = listing # most recently appended
    # write log, if it might be corrupted write 'XXX' at the end
    if state_invariant():
        log.append((thread, action, 'finish', ret))
    else: 
        log.append((thread, action, 'finish', ret, 'XXX'))

def exit_enabled(thread):
    return phase[thread] == 'finish' # holding lock

# For now, handle exit as a special case, assign phase 'done'.
# If the simulated threads had more than one action, here we
# would advance to the next action and reset phase to 'start'.
def exit(thread):
    phase[thread] = 'done'  # release lock, indicate done


### Metadata

state = ('pc', 'phase', 'log', 'files', 'listing')

actions = (start, call, finish, exit)

enablers = {start:(start_enabled,), call:(call_enabled,),
            finish:(finish_enabled,), exit:(exit_enabled,)}

domains = { start: { 'thread': threads },
            call: { 'thread': threads },
            finish: { 'thread': threads },
            exit: { 'thread': threads }}
