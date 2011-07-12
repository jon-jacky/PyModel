"""
tracenolock.py - like tracemultiplexer.py but no sych on tracelock
Simply comment out the check for free tracelock in start_enabled and
finish_enabled.

Simulate a multi-threaded program that has been
instrumented to save traces of its API calls in a log. 

Demonstrate the nondeterminism in the order in which API calls and
returns are made, and the order they appear in the trace log.

Parameters (constants that do not change when the model executes):

program: models the multi-threaded program.  It is a sequence of API
call ids (action ids) for each thread, first index is thread id,
second index is thread pc.

State:

pc: program counter for each thread, indexed by thread_id
Indicates which action in program each thread is executing

phase: phase of each thread, indexed by thread id
models progress through the tracecapture function (see README)
For each API call in program, phases in order are: ready, start, call, finish
phase[thread] == start means thread holds tracelock to write call start
phase[thread] == finish means thread holds tracelock to write call finish
After processing last API call in its thread, phase[thread] == exit

log: contents of the tracelog written by all the threads

Actions:

Each action represents progress through the phases of tracecapture.
Each action might be enabled for more than one thread in some states; 
this models the nondeterminism of threading.

"""

## Parameters

# This simple program has only two threads, with only one API call in each

program = (( 'listfiles', ),  # thread 0
           ( 'openfile', ))   # thread 1

threads = range(len(program))

### State

pc = list() # program counter for each thread
phase = list() # phase of each thread in tracecapture
log = list() # contents of tracelog written by all threads

def reset():
    global pc, phase, log
    pc = [ 0 for thread in program ]
    phase = [ 'ready' for thread in program ]
    log = []

reset()

def accepting():
    return all([ phase[t] == 'exit' for t in threads ])

### Actions

def start_enabled(thread): 
    return (phase[thread] == 'ready')
            # and not [ t for t in threads if phase[t] == 'start']) #lock is free

def start(thread):
    phase[thread] = 'start' # acquire lock
    log.append((thread, program[thread][pc[thread]], 'start')) # write log

def call_enabled(thread):
    return phase[thread] == 'start' # holding lock

def call(thread):
    phase[thread] = 'call' # release lock, execute call

def finish_enabled(thread): 
    return (phase[thread] == 'call')
            # and not [ t for t in threads if phase[t] == 'finish']) #lock is free

def finish(thread):
    phase[thread] = 'finish' # acquire lock
    log.append((thread, program[thread][pc[thread]], 'finish')) # write log

def release_enabled(thread):
    return phase[thread] == 'finish' # holding lock

def release(thread):
    if pc[thread] + 1 < len(program[thread]): # more actions remain
        phase[thread] = 'ready' # release lock
        pc[thread] += 1 # advance to next action
    else:
        phase[thread] = 'exit'  # release lock, indicate done

### Metadata

state = ('pc', 'phase', 'log')

actions = (start, call, finish, release)

enablers = {start:(start_enabled,), call:(call_enabled,),
            finish:(finish_enabled,), release:(release_enabled,)}

domains = { start: { 'thread': threads },
            call: { 'thread': threads },
            finish: { 'thread': threads },
            release: { 'thread': threads }}
